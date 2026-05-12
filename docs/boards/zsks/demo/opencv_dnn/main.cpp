/*
 * Copyright (c) 2025 Zhongshan Kuangshi Microelectronics Technology Co., Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Contact Information
 * Author: yaohongtao
 * Phone: +86-18604465633
 * Email: yht@cust.edu.cn
 */

#include <opencv2/opencv.hpp>
#include <iostream>
#include <atomic>
#include <csignal>
#include <unistd.h>
#include <chrono>
#include "host_uvc.h"
#include "media_vdec.h"
#include "sdk_module_init.h"

using namespace cv;
using namespace std;
using namespace std::chrono;

td_bool g_uvc_exit = TD_FALSE;

// 优化内存管理类
class MemoryManager {
public:
    static void optimizeMemory()
    {
        cv::setUseOptimized(true);
        cv::setNumThreads(4);  /* 4: Number of CPU cores */
    }
};

static void sample_uvc_exit_signal_handler(int signal)
{
    printf("收到退出信号，准备退出...\n");
    g_uvc_exit = TD_TRUE;
}

int main(int argc, char** argv)
{
    // 优化内存使用
    MemoryManager::optimizeMemory();

    int ret;
    uvc_ctrl_info ctrl_info = {0};
    struct sigaction sig_exit;
    sig_exit.sa_handler = sample_uvc_exit_signal_handler;
    sigaction(SIGINT, &sig_exit, nullptr);
    sigaction(SIGTERM, &sig_exit, nullptr);
    ret = sample_host_uvc(argc, argv, &ctrl_info);
    if (ret != TD_SUCCESS) {
        return TD_FAILURE;
    }
#ifdef CONFIG_USER_SPACE
    SDK_init();
#endif
    // OpenCV V4L2 video capture
    VideoCapture cap(0, cv::CAP_V4L2);
    if (!cap.isOpened()) {
        printf("Error: Failed to open camera device!\n");
        return -1;
    }

    int width = ctrl_info.width;
    int height = ctrl_info.height;
    int fps = 30;

    // 设置摄像头参数
    cap.set(CAP_PROP_FRAME_WIDTH, width);
    cap.set(CAP_PROP_FRAME_HEIGHT, height);
    cap.set(CAP_PROP_FPS, fps);
    cap.set(CAP_PROP_BUFFERSIZE, 4);  /* 4: Increase buffer size */

    // 根据格式设置摄像头参数
    const char* type_name = sample_uvc_v4l2_format_name(ctrl_info.pixelformat);
    if (strcmp(type_name, "MJPEG") == 0) {
        cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    } else if (strcmp(type_name, "YUYV") == 0) {
        cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('Y', 'U', 'Y', 'V'));
    } else {
        std::cerr << "只支持 YUYV 或 MJPEG 格式，请用 -fYUYV 或 -fMJPEG 参数启动！" << std::endl;
        return -1;
    }

    // 验证设置是否成功
    int actual_width = cap.get(CAP_PROP_FRAME_WIDTH);
    int actual_height = cap.get(CAP_PROP_FRAME_HEIGHT);
    double actual_fps = cap.get(CAP_PROP_FPS);

    printf("Requested resolution: %dx%d @ %d fps\n", width, height, fps);
    printf("Actual resolution: %dx%d @ %.2f fps\n", actual_width, actual_height, actual_fps);
    printf("Using format: %s\n", type_name);

    if (actual_width != width || actual_height != height) {
        printf("Warning: Camera does not support requested resolution, using actual resolution\n");
        width = actual_width;
        height = actual_height;
    }

    // 初始化人脸检测器，使用更快的参数
    const string modelPath = "./onnx/face_detection_yunet_2023mar.onnx";
    Ptr<FaceDetectorYN> detector = FaceDetectorYN::create(
        /* 256 144 input width height 0.6 score_threshold 0.7 nms_threshold */
        modelPath, "", Size(256, 144), 0.6, 0.7, 100); /* 100 top_k */
    if (!detector) {
        printf("Error: Failed to create face detector\n");
        return -1;
    }

    // 初始化媒体链路
    if (sample_uvc_media_init(type_name, width, height) != TD_SUCCESS) {
        std::cerr << "media start failed!" << std::endl;
        return -1;
    }

    const int MAX_RETRIES = 3; /* 3: max retries */
    int retry_count = 0;
    bool device_reconnected = false;
    int empty_frame_count = 0;
    const int MAX_EMPTY_FRAMES = 10; /* 10: max empty frames */

    // 预分配Mat对象
    Mat frame;
    Mat faces;
    Mat yuvFrame;
    vector<uchar> mjpeg_buffer;
    mjpeg_buffer.reserve(width * height * 3 / 2);  /* 3 / 2  YUV420 memory size */

    // 创建MJPEG编码器
    vector<int> mjpeg_params = {
        IMWRITE_JPEG_QUALITY, 90,  /* 90: JPEG quality */
        IMWRITE_JPEG_OPTIMIZE, 1,
        IMWRITE_JPEG_PROGRESSIVE, 0
    };

    // 预分配VPSS缓冲区
    ot_size pic_size;
    pic_size.width = static_cast<td_u32>(width);
    pic_size.height = static_cast<td_u32>(height);

    if (strcmp(type_name, "YUYV") == 0) {
        // 预分配YUYV缓冲区，每个像素2字节
        yuvFrame.create(height, width, CV_8UC2);
    }

    // 新增：人脸检测相关变量
    int frame_count = 0;
    vector<Rect> last_detected_faces;
    vector<float> last_confidence_scores;
    const int DETECT_INTERVAL = 5;  /* 5: Detect every 5 frames */

    while (!g_uvc_exit) {
        cap >> frame;

        if (frame.empty()) {
            empty_frame_count++;
            printf("Empty frame %d/%d, attempting to reconnect...\n", empty_frame_count, MAX_EMPTY_FRAMES);

            if (empty_frame_count >= MAX_EMPTY_FRAMES) {
                if (retry_count < MAX_RETRIES) {
                    printf("Attempting to reconnect camera (attempt %d/%d)...\n", retry_count + 1, MAX_RETRIES);
                    cap.release();
                    sleep(1);

                    cap.open(0, cv::CAP_V4L2);
                    if (cap.isOpened()) {
                        cap.set(CAP_PROP_FRAME_WIDTH, width);
                        cap.set(CAP_PROP_FRAME_HEIGHT, height);
                        cap.set(CAP_PROP_FPS, fps);
                        cap.set(CAP_PROP_BUFFERSIZE, 4); /* 4 cap prop buffer size */
                        if (strcmp(type_name, "MJPEG") == 0) {
                            cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
                        } else {
                            cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('Y', 'U', 'Y', 'V'));
                        }

                        actual_width = cap.get(CAP_PROP_FRAME_WIDTH);
                        actual_height = cap.get(CAP_PROP_FRAME_HEIGHT);
                        actual_fps = cap.get(CAP_PROP_FPS);

                        printf("Camera reconnected successfully\n");
                        printf("New resolution: %dx%d @ %.2f fps\n", actual_width, actual_height, actual_fps);

                        retry_count = 0;
                        empty_frame_count = 0;
                        device_reconnected = true;
                        continue;
                    }
                    retry_count++;
                    printf("Retry %d/%d failed\n", retry_count, MAX_RETRIES);
                } else {
                    printf("Failed to reconnect after %d attempts\n", MAX_RETRIES);
                    break;
                }
            }
            continue;
        }

        empty_frame_count = 0;
        retry_count = 0;

        if (device_reconnected) {
            printf("Reinitializing media pipeline...\n");
            if (sample_uvc_media_init(type_name, width, height) != TD_SUCCESS) {
                std::cerr << "media reinit failed!" << std::endl;
                break;
            }
            device_reconnected = false;
        }

        // 人脸检测逻辑
        frame_count++;
        bool is_detect_frame = (frame_count % DETECT_INTERVAL == 0);

        if (is_detect_frame) {
            // 预处理阶段
            Mat small_frame;
            resize(frame, small_frame, Size(256, 144), 0, 0, INTER_NEAREST); /* 256 144 resize width height */

            // 检测阶段
            detector->detect(small_frame, faces);

            // 处理检测结果
            const int minFaceSize = 50; /* 50 min face size */
            last_detected_faces.clear();
            last_confidence_scores.clear();

            if (faces.rows > 0) {
                float scale_x = static_cast<float>(frame.cols) / small_frame.cols;
                float scale_y = static_cast<float>(frame.rows) / small_frame.rows;

                for (int i = 0; i < faces.rows; ++i) {
                    int x = static_cast<int>(faces.at<float>(i, 0) * scale_x);
                    int y = static_cast<int>(faces.at<float>(i, 1) * scale_y);
                    int w = static_cast<int>(faces.at<float>(i, 2) * scale_x); /* 2 the number of width */
                    int h = static_cast<int>(faces.at<float>(i, 3) * scale_y); /* 3 the number of heigth */
                    float score = faces.at<float>(i, 4); /* 4 the number of socre */

                    if (w >= minFaceSize && h >= minFaceSize) {
                        last_detected_faces.emplace_back(x, y, w, h);
                        last_confidence_scores.push_back(score);
                    }
                }
            }
        }

        // 绘制人脸框
        for (size_t i = 0; i < last_detected_faces.size(); ++i) {
            rectangle(frame, last_detected_faces[i], Scalar(0, 255, 0), 2); /* 0 255 0 R G B, 2 Line width */
            char scoreText[20]; /* 20 text buffer size */
            ret = snprintf(scoreText, sizeof(scoreText), "Conf: %.2f",
                last_confidence_scores[i] / 100); /* 100 get the percentage */
            if (ret < 0) {
                printf("[func]:%s [line]:%d [info]:snprintf failed\n", __FUNCTION__, __LINE__);
                break;
            }
            putText(frame, scoreText, Point(last_detected_faces[i].x,
                last_detected_faces[i].y - 5), /* 5 pic height minus 5 */
                /* 0.5 scaling ratio 0 255 0 R G B, 1 Line width */
                FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 255, 0), 1);
        }

        // 后续处理保持不变
        if (strcmp(type_name, "MJPEG") == 0) {
            imencode(".jpg", frame, mjpeg_buffer, mjpeg_params);
            ret = sample_uvc_media_send_data(mjpeg_buffer.data(), mjpeg_buffer.size(),
                width, &pic_size, "MJPEG");
        } else {
            // YUYV格式转换
            cvtColor(frame, yuvFrame, COLOR_BGR2YUV_YUY2);
            ret = sample_uvc_media_send_data(yuvFrame.data, yuvFrame.total() * yuvFrame.elemSize(),
                yuvFrame.step, &pic_size, "YUYV");
        }

        if (ret != 0) {
            ret = -errno;
            std::cerr << "write error: " << strerror(-ret) << std::endl;
        }
    }

    printf("--media exit...\n");
    sample_uvc_media_stop_receive_data();
    sample_uvc_media_exit();
    cap.release();

#ifdef CONFIG_USER_SPACE
    SDK_exit();
#endif

    return 0;
}
