/*
 * Copyright (c) 2025 HiSilicon (Shanghai) Technologies Co., Ltd.
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
 * Modifications Author: yaohongtao (yht@cust.edu.cn)
 */

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <pthread.h>
#include <sys/prctl.h>
/* 新增v4l2相关头文件 */
#include <fcntl.h>           // 文件控制
#include <errno.h>           // 错误处理
#include <unistd.h>          // POSIX API
#include <string.h>          // 字符串操作
#include <sys/mman.h>        // 内存映射
#include <sys/ioctl.h>       // IO控制
#include <sys/select.h>      // select复用
#include <linux/videodev2.h> // v4l2核心

#include "svp_acl_rt.h"
#include "svp_acl.h"
#include "svp_acl_ext.h"
#include "sample_audio.h" // 包含音频文件
#include "audio_aac_adp.h"
#include "sdk_module_init.h"
#include "common/sample_common_svp_osd.h" // osd头文件
#include "common/sample_common_svp.h"
#include "common/sample_common_svp_npu.h"
#include "common/sample_common_svp_npu_model.h"

#define SAMPLE_SVP_NPU_SHAERD_WORK_BUF_NUM     1
#define SAMPLE_SVP_NPU_YOLO_TYPE_NUM           12
#define SAMPLE_SVP_NPU_YOLO_THRESHOLD_NUM      1
#define SAMPLE_SVP_NPU_PATH_LEN 0x100

static int g_last_played_class_id = -1;
static td_bool g_svp_npu_terminate_signal = TD_FALSE;
static td_s32 g_svp_npu_dev_id = 0;
static sample_svp_npu_task_info g_svp_npu_task[SAMPLE_SVP_NPU_MAX_TASK_NUM] = {0};
static sample_svp_npu_shared_work_buf g_svp_npu_shared_work_buf[SAMPLE_SVP_NPU_SHAERD_WORK_BUF_NUM] = {0};

static sample_svp_npu_threshold g_svp_npu_rfcn_threshold[SAMPLE_SVP_NPU_RFCN_THRESHOLD_NUM] = {
    {0.7, 0.0, 16.0, 16.0, "rpn_data"}, {0.3, 0.9, 16.0, 16.0, "rpn_data1"}
};

static sample_svp_npu_threshold g_svp_npu_yolo_threshold[SAMPLE_SVP_NPU_YOLO_TYPE_NUM] = {
    {0.9, 0.15, 1.0, 1.0, "rpn_data"},  // yolov8
};

static sample_svp_npu_roi_info g_svp_npu_yolo_roi_info[SAMPLE_SVP_NPU_YOLO_TYPE_NUM] = {
    {"output0", "output0_"},  // yolov8
};

static sample_vi_cfg g_vi_config;
static ot_sample_svp_rect_info g_svp_npu_rect_info = {0};
static td_bool g_svp_npu_thread_stop = TD_FALSE;
static pthread_t g_svp_npu_thread = 0;
static sample_vo_cfg g_svp_npu_vo_cfg = { 0 };
static pthread_t g_svp_npu_vdec_thread = 0;
static ot_vb_pool_info g_svp_npu_vb_pool_info;
static td_void *g_svp_npu_vb_virt_addr = TD_NULL;

static ot_sample_svp_media_cfg g_svp_npu_media_cfg = {
    .svp_switch = {TD_FALSE, TD_TRUE},
    .pic_type = {PIC_1080P, PIC_CIF},
    .chn_num = OT_SVP_MAX_VPSS_CHN_NUM,
};

static sample_vdec_attr g_svp_npu_vdec_cfg = {
    .type = OT_PT_MJPEG,
    .mode = OT_VDEC_SEND_MODE_FRAME,
    .width = FHD_WIDTH,
    .height = FHD_HEIGHT,
    .sample_vdec_picture.pixel_format = OT_PIXEL_FORMAT_YVU_SEMIPLANAR_420, /* 420:pixel_format */
    .sample_vdec_picture.alpha = 0,      /* 0:alpha */
    .display_frame_num = 2,               /* 2:display_frame_num */
    .frame_buf_cnt = 5,                   /* 5:2+2+1 */
};

static vdec_thread_param g_svp_npu_vdec_param = {
    .chn_id = 0,

    .v4l2_device = "/dev/video0",           // 摄像头设备
    .width = FHD_WIDTH,                     // 采集分辨率宽
    .height = FHD_HEIGHT,                   // 采集分辨率高
    .pixel_format = V4L2_PIX_FMT_MJPEG,     // MJPEG格式

    .type = OT_PT_MJPEG,
    .stream_mode = OT_VDEC_SEND_MODE_FRAME,
    .interval_time = 1000, /* 1000:interval_time */
    .pts_init = 0,
    .pts_increase = 0,
    .e_thread_ctrl = THREAD_CTRL_START,
    .circle_send = TD_TRUE,
    .milli_sec = 0,
    .min_buf_size = (FHD_WIDTH * FHD_HEIGHT * 3) >> 1, /* 3:chn_size */
    .fps = 30,
};

// 音频线程
typedef struct {
    int class_id;
} audio_play_param;

void* audio_play_thread(void* arg)
{
    audio_play_param* param = (audio_play_param*)arg;
    td_s32 audio_ret = TD_SUCCESS;

    switch (param->class_id) {
        case 0:
            audio_ret = sample_audio_adec_ao("fruit_audio", "pear");
            break;
        case 1:
            audio_ret = sample_audio_adec_ao("fruit_audio", "watermelon");
            break;
        case 2: /* 2: case of orange */
            audio_ret = sample_audio_adec_ao("fruit_audio", "orange");
            break;
        case 3: /* 3: case of banana */
            audio_ret = sample_audio_adec_ao("fruit_audio", "banana");
            break;
        case 4: /* 4: case of apple */
            audio_ret = sample_audio_adec_ao("fruit_audio", "apple");
            break;
        default:
            audio_ret = TD_SUCCESS;
            break;
    }

    if (audio_ret != TD_SUCCESS) {
        sample_svp_trace_err("play audio failed!\n");
    } else {
        sample_svp_trace_info("play audio success!\n");
    }

    free(param); // 释放参数
    return NULL;
}

static td_void sample_svp_npu_acl_terminate(td_void)
{
    if (g_svp_npu_terminate_signal == TD_TRUE) {
        printf("\033[0;31mprogram termination abnormally!\033[0;39m\n");
    }
}

/* function : svp npu signal handle */
td_void sample_svp_npu_acl_handle_sig(td_void)
{
    g_svp_npu_terminate_signal = TD_TRUE;
}

static td_void sample_svp_npu_acl_deinit(td_void)
{
    svp_acl_error ret;

    ret = svp_acl_rt_reset_device(g_svp_npu_dev_id);
    if (ret != SVP_ACL_SUCCESS) {
        sample_svp_trace_err("reset device fail\n");
    }
    sample_svp_trace_info("end to reset device is %d\n", g_svp_npu_dev_id);

    ret = svp_acl_finalize();
    if (ret != SVP_ACL_SUCCESS) {
        sample_svp_trace_err("finalize acl fail\n");
    }
    sample_svp_trace_info("end to finalize acl\n");
    (td_void)sample_common_svp_check_sys_exit();
}

static td_s32 sample_svp_npu_acl_init(const td_char *acl_config_path, td_bool vi_en)
{
    /* svp acl init */
    svp_acl_rt_run_mode run_mode;
    svp_acl_error ret;
    td_bool is_mpi_init;

    is_mpi_init = sample_common_svp_check_sys_init(vi_en);
    sample_svp_check_exps_return(is_mpi_init != TD_TRUE, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR, "mpi init failed!\n");

    ret = svp_acl_init(acl_config_path);
    sample_svp_check_exps_return(ret != SVP_ACL_SUCCESS, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR, "acl init failed!\n");

    sample_svp_trace_info("svp acl init success!\n");

    /* open device */
    ret = svp_acl_rt_set_device(g_svp_npu_dev_id);
    if (ret != SVP_ACL_SUCCESS) {
        (td_void)svp_acl_finalize();
        sample_svp_trace_err("svp acl open device %d failed!\n", g_svp_npu_dev_id);
        return TD_FAILURE;
    }
    sample_svp_trace_info("open device %d success!\n", g_svp_npu_dev_id);

    /* get run mode */
    ret = svp_acl_rt_get_run_mode(&run_mode);
    if ((ret != SVP_ACL_SUCCESS) || (run_mode != SVP_ACL_DEVICE)) {
        (td_void)svp_acl_rt_reset_device(g_svp_npu_dev_id);
        (td_void)svp_acl_finalize();
        sample_svp_trace_err("acl get run mode failed!\n");
        return TD_FAILURE;
    }
    sample_svp_trace_info("get run mode success!\n");

    return TD_SUCCESS;
}

static td_s32 sample_svp_npu_acl_dataset_init(td_u32 task_idx)
{
    td_s32 ret = sample_common_svp_npu_create_input(&g_svp_npu_task[task_idx]);
    sample_svp_check_exps_return(ret != TD_SUCCESS, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR, "create input failed!\n");

    ret = sample_common_svp_npu_create_output(&g_svp_npu_task[task_idx]);
    if (ret != TD_SUCCESS) {
        sample_common_svp_npu_destroy_input(&g_svp_npu_task[task_idx]);
        sample_svp_trace_err("execute create output fail.\n");
        return TD_FAILURE;
    }
    return TD_SUCCESS;
}

static td_void sample_svp_npu_acl_dataset_deinit(td_u32 task_idx)
{
    (td_void)sample_common_svp_npu_destroy_input(&g_svp_npu_task[task_idx]);
    (td_void)sample_common_svp_npu_destroy_output(&g_svp_npu_task[task_idx]);
}

static td_void *sample_svp_npu_acl_thread_execute(td_void *args)
{
    td_s32 ret;
    td_u32 task_idx = *(td_u32 *)args;

    ret = svp_acl_rt_set_device(g_svp_npu_dev_id);
    sample_svp_check_exps_return(ret != TD_SUCCESS, TD_NULL, SAMPLE_SVP_ERR_LEVEL_ERROR,
        "open device %d failed!\n", g_svp_npu_dev_id);

    ret = sample_common_svp_npu_model_execute(&g_svp_npu_task[task_idx]);
    if (ret != SVP_ACL_SUCCESS) {
        sample_svp_trace_err("execute inference failed of task[%u]!\n", task_idx);
    }

    ret = svp_acl_rt_reset_device(g_svp_npu_dev_id);
    if (ret != SVP_ACL_SUCCESS) {
        sample_svp_trace_err("task[%u] reset device failed!\n", task_idx);
    }
    return TD_NULL;
}

static td_void sample_svp_npu_acl_model_execute_multithread()
{
    pthread_t execute_threads[SAMPLE_SVP_NPU_MAX_THREAD_NUM] = {0};
    td_u32 idx[SAMPLE_SVP_NPU_MAX_THREAD_NUM] = {0};
    td_u32 task_idx;

    for (task_idx = 0; task_idx < SAMPLE_SVP_NPU_MAX_THREAD_NUM; task_idx++) {
        idx[task_idx] = task_idx;
        pthread_create(&execute_threads[task_idx], NULL, sample_svp_npu_acl_thread_execute, &idx[task_idx]);
    }

    td_void *waitret[SAMPLE_SVP_NPU_MAX_THREAD_NUM];
    for (task_idx = 0; task_idx < SAMPLE_SVP_NPU_MAX_THREAD_NUM; task_idx++) {
        pthread_join(execute_threads[task_idx], &waitret[task_idx]);
    }

    for (task_idx = 0; task_idx < SAMPLE_SVP_NPU_MAX_THREAD_NUM; task_idx++) {
        sample_svp_trace_info("output %u-th task data\n", task_idx);
        sample_common_svp_npu_output_classification_result(&g_svp_npu_task[task_idx]);
    }
}

static td_void sample_svp_npu_acl_deinit_task(td_u32 task_num, td_u32 shared_work_buf_idx)
{
    td_u32 task_idx;

    for (task_idx = 0; task_idx < task_num; task_idx++) {
        (td_void)sample_common_svp_npu_destroy_work_buf(&g_svp_npu_task[task_idx]);
        (td_void)sample_common_svp_npu_destroy_task_buf(&g_svp_npu_task[task_idx]);
        (td_void)sample_svp_npu_acl_dataset_deinit(task_idx);
        (td_void)memset_s(&g_svp_npu_task[task_idx], sizeof(sample_svp_npu_task_cfg), 0,
            sizeof(sample_svp_npu_task_cfg));
    }
    if (g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_ptr != TD_NULL) {
        (td_void)svp_acl_rt_free(g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_ptr);
        g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_ptr = TD_NULL;
        g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_size = 0;
        g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_stride = 0;
    }
}

static td_s32 sample_svp_npu_acl_create_shared_work_buf(td_u32 task_num, td_u32 shared_work_buf_idx)
{
    td_u32 task_idx;
    td_u32 work_buf_size;
    td_u32 work_buf_stride;
    td_s32 ret;

    for (task_idx = 0; task_idx < task_num; task_idx++) {
        ret = sample_common_svp_npu_get_work_buf_info(&g_svp_npu_task[task_idx], &work_buf_size, &work_buf_stride);
        sample_svp_check_exps_return(ret != TD_SUCCESS, ret, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "get %u-th task work buf info failed!\n", task_idx);

        if (g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_size < work_buf_size) {
            g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_size = work_buf_size;
            g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_stride = work_buf_stride;
        }
    }
    ret = svp_acl_rt_malloc_cached(&g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_ptr,
        g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_size, SVP_ACL_MEM_MALLOC_NORMAL_ONLY);
    sample_svp_check_exps_return(ret != TD_SUCCESS, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR,
        "malloc %u-th shared work buf failed!\n", shared_work_buf_idx);

    (td_void)svp_acl_rt_mem_flush(g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_ptr,
        g_svp_npu_shared_work_buf[shared_work_buf_idx].work_buf_size);
    return TD_SUCCESS;
}

static td_s32 sample_svp_npu_acl_init_task(td_u32 task_num, td_bool is_share_work_buf,
    td_u32 shared_work_buf_idx)
{
    td_u32 task_idx;
    td_s32 ret;

    if (is_share_work_buf == TD_TRUE) {
        ret = sample_svp_npu_acl_create_shared_work_buf(task_num, shared_work_buf_idx);
        sample_svp_check_exps_return(ret != TD_SUCCESS, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "create shared work buf failed!\n");
    }

    for (task_idx = 0; task_idx < task_num; task_idx++) {
        ret = sample_svp_npu_acl_dataset_init(task_idx);
        if (ret != TD_SUCCESS) {
            goto task_init_end_0;
        }
        ret = sample_common_svp_npu_create_task_buf(&g_svp_npu_task[task_idx]);
        if (ret != TD_SUCCESS) {
            sample_svp_trace_err("create task buf failed.\n");
            goto task_init_end_0;
        }
        if (is_share_work_buf == TD_FALSE) {
            ret = sample_common_svp_npu_create_work_buf(&g_svp_npu_task[task_idx]);
        } else {
            /* if all tasks are on the same stream, work buf can be shared */
            ret = sample_common_svp_npu_share_work_buf(&g_svp_npu_shared_work_buf[shared_work_buf_idx],
                &g_svp_npu_task[task_idx]);
        }
        if (ret != TD_SUCCESS) {
            sample_svp_trace_err("create work buf failed.\n");
            goto task_init_end_0;
        }
    }
    return TD_SUCCESS;

task_init_end_0:
    (td_void)sample_svp_npu_acl_deinit_task(task_num, shared_work_buf_idx);
    return ret;
}

// 辅助函数：根据class_id播放音频（如果类别发生变化）
static void play_audio_if_class_changed(void)
{
    int max_idx = -1;
    double max_score = 0.5;

    // 检测到目标时，启动音频播放线程
    for (int i = 0; i < g_svp_npu_rect_info.num; i++) {
        if (g_svp_npu_rect_info.rect[i].score >= max_score) {
            if (max_idx == -1 || g_svp_npu_rect_info.rect[i].score > g_svp_npu_rect_info.rect[max_idx].score) {
                max_idx = i;
            }
        }
    }
    // ...existing code...
    if (max_idx != -1) {
        int current_class_id = g_svp_npu_rect_info.rect[max_idx].class_id;
        if (current_class_id != g_last_played_class_id) {
            pthread_t audio_thread;
            audio_play_param* param = malloc(sizeof(audio_play_param));
            if (param != NULL) {
                param->class_id = current_class_id;
                pthread_create(&audio_thread, NULL, audio_play_thread, param);
                pthread_detach(audio_thread); // 不阻塞主流程
                g_last_played_class_id = current_class_id; // 只在播放时更新
            }
        }
    }
}

static void get_detection_results(void)
{
    // 循环打印置信度和类别ID
    for (int i = 0; i < g_svp_npu_rect_info.num; i++) {
        const char* class_name = NULL;
        switch (g_svp_npu_rect_info.rect[i].class_id) {
            case 0:
                class_name = "梨子";
                break;
            case 1:
                class_name = "西瓜";
                break;
            case 2: /* 2: case of orange */
                class_name = "橘子";
                break;
            case 3: /* 3: case of banana */
                class_name = "香蕉";
                break;
            case 4: /* 4: case of apple */
                class_name = "苹果";
                break;
            default:
                class_name = "未知";
                break;
        }
        printf("score:%lf, class_id:%d, name:%s\r\n",
            g_svp_npu_rect_info.rect[i].score,
            g_svp_npu_rect_info.rect[i].class_id,
            class_name);
    }
}

static td_s32 sample_svp_npu_acl_frame_proc(const ot_video_frame_info *ext_frame,
    const ot_video_frame_info *base_frame, td_void *args)
{
    td_s32 ret;
    td_void *virt_addr = TD_NULL;
    sample_svp_npu_detection_info *detection_info = TD_NULL;
    sample_svp_npu_thread_args *thread_args = (sample_svp_npu_thread_args *)args;
    td_u32 size = (td_u32)(ext_frame->video_frame.height * ext_frame->video_frame.stride[0] *
        SAMPLE_SVP_NPU_IMG_THREE_CHN / SAMPLE_SVP_NPU_DOUBLE);

    virt_addr = g_svp_npu_vb_virt_addr +
        (ext_frame->video_frame.phys_addr[0] - g_svp_npu_vb_pool_info.pool_phy_addr);
    ret = sample_common_svp_npu_update_input_data_buffer_info(virt_addr, size,
        ext_frame->video_frame.stride[0], 0, &g_svp_npu_task[0]);
    sample_svp_check_exps_return(ret != TD_SUCCESS, ret, SAMPLE_SVP_ERR_LEVEL_ERROR, "update data buffer failed!\n");

    ret = sample_common_svp_npu_model_execute(&g_svp_npu_task[0]);
    sample_svp_check_exps_return(ret != TD_SUCCESS, ret, SAMPLE_SVP_ERR_LEVEL_ERROR, "model execute failed!\n");

    play_audio_if_class_changed();

    // ...existing code...
    if (thread_args->model_name == SAMPLE_SVP_NPU_RFCN || thread_args->model_name == SAMPLE_SVP_NPU_YOLO) {
        detection_info = thread_args->detection_info;
        if (detection_info->is_cpu_rpn == TD_FALSE) {
            ret = sample_common_svp_npu_roi_to_rect(&g_svp_npu_task[0], detection_info, ext_frame, base_frame,
                &g_svp_npu_rect_info);
            sample_svp_check_exps_return(ret != TD_SUCCESS, ret, SAMPLE_SVP_ERR_LEVEL_ERROR, "roi to rect failed!\n");
        } else {
            ret = sample_common_svp_npu_roi_to_rect_cpu(&g_svp_npu_task[0], detection_info, ext_frame, base_frame,
                &g_svp_npu_rect_info);
            sample_svp_check_exps_return(ret != TD_SUCCESS, ret, SAMPLE_SVP_ERR_LEVEL_ERROR, "roi to rect failed!\n");
        }
        ret = sample_common_svp_vgs_fill_rect(base_frame, &g_svp_npu_rect_info, SAMPLE_SVP_NPU_RECT_COLOR);
        sample_svp_check_exps_return(ret != TD_SUCCESS, ret, SAMPLE_SVP_ERR_LEVEL_ERROR, "vgs fill rect failed!\n");

        // 在屏幕上打印信息检测到的水果信息
        int i;
        for (i = 0; i < (g_svp_npu_rect_info.num); i++) {
            sample_osd_draw_text(g_svp_npu_rect_info.rect[i].score, g_svp_npu_rect_info.rect[i].class_id,
                g_svp_npu_rect_info.rect[i].point[0].x, g_svp_npu_rect_info.rect[i].point[0].y,
                    thread_args->mpp_osd_info);
        }
        if (g_svp_npu_rect_info.num == 0) {
            thread_args->mpp_osd_info.chn_attr.is_show = TD_FALSE;
            sample_osd_clean_text(thread_args->mpp_osd_info);
        }
    }
    get_detection_results();

    return ret;
}

static td_s32 sample_svp_npu_acl_vb_map(td_u32 vb_pool_idx)
{
    td_s32 ret;

    if (g_svp_npu_vb_virt_addr == TD_NULL) {
        ret = ss_mpi_vb_get_pool_info(g_svp_npu_media_cfg.vb_pool[vb_pool_idx], &g_svp_npu_vb_pool_info);
        sample_svp_check_exps_return(ret != TD_SUCCESS, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "get pool info failed!\n");
        g_svp_npu_vb_virt_addr = ss_mpi_sys_mmap(g_svp_npu_vb_pool_info.pool_phy_addr,
            g_svp_npu_vb_pool_info.pool_size);
        sample_svp_check_exps_return(g_svp_npu_vb_virt_addr == TD_NULL, TD_FAILURE, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "map vb pool failed!\n");
    }
    return TD_SUCCESS;
}

static td_void *sample_svp_npu_acl_vdec_to_vo(td_void *args)
{
    td_s32 ret;
    ot_video_frame_info base_frame;
    ot_video_frame_info ext_frame;
    const td_s32 milli_sec = SAMPLE_SVP_NPU_MILLIC_SEC;
    const ot_vo_layer vo_layer = 0;
    const ot_vo_chn vo_chn = 0;
    const td_s32 vpss_grp = 0;
    td_s32 vpss_chn[] = { OT_VPSS_CHN0, OT_VPSS_CHN1 };
    td_u32 size;
    td_u32 stride;
    td_u8 *data = TD_NULL;

    (td_void)prctl(PR_SET_NAME, "svp_npu_vdec_to_vo", 0, 0, 0);

    ret = svp_acl_rt_set_device(g_svp_npu_dev_id);
    sample_svp_check_exps_return(ret != TD_SUCCESS, TD_NULL, SAMPLE_SVP_ERR_LEVEL_ERROR, "open device failed!\n");

    ret = sample_svp_npu_acl_vb_map(OT_VPSS_CHN1);
    sample_svp_check_exps_goto(ret != TD_SUCCESS, fail_0, SAMPLE_SVP_ERR_LEVEL_ERROR, "map vb pool failed!\n");

    ret = sample_common_svp_npu_get_input_data_buffer_info(&g_svp_npu_task[0], 0, &data, &size, &stride);
    sample_svp_check_exps_goto(ret != TD_SUCCESS, fail_1, SAMPLE_SVP_ERR_LEVEL_ERROR,
        "Error(%#x),get_input_data_buffer_info failed!\n", ret);

    while (g_svp_npu_thread_stop == TD_FALSE) {
        ret = ss_mpi_vpss_get_chn_frame(vpss_grp, vpss_chn[1], &ext_frame, milli_sec);
        sample_svp_check_exps_continue(ret != TD_SUCCESS, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "Error(%#x),ss_mpi_vpss_get_chn_frame failed, vpss_grp(%d), vpss_chn(%d)!\n", ret, vpss_grp, vpss_chn[1]);

        ret = ss_mpi_vpss_get_chn_frame(vpss_grp, vpss_chn[0], &base_frame, milli_sec);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, ext_release, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "Error(%#x),ss_mpi_vpss_get_chn_frame failed, VPSS_GRP(%d), VPSS_CHN(%d)!\n", ret, vpss_grp, vpss_chn[0]);

        ret = sample_svp_npu_acl_frame_proc(&ext_frame, &base_frame, args);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, base_release, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "Error(%#x),sample_svp_npu_acl_frame_proc failed!\n", ret);

        ret = sample_common_svp_venc_vo_send_stream(&g_svp_npu_media_cfg.svp_switch, 0, vo_layer, vo_chn, &base_frame);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, base_release, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "Error(%#x),sample_common_svp_venc_vo_send_stream failed!\n", ret);
base_release:
        ret = ss_mpi_vpss_release_chn_frame(vpss_grp, vpss_chn[0], &base_frame);
        sample_svp_check_exps_trace(ret != TD_SUCCESS, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "Error(%#x),release_frame failed,grp(%d) chn(%d)!\n", ret, vpss_grp, vpss_chn[0]);
ext_release:
        ret = ss_mpi_vpss_release_chn_frame(vpss_grp, vpss_chn[1], &ext_frame);
        sample_svp_check_exps_trace(ret != TD_SUCCESS, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "Error(%#x),release_frame failed,grp(%d) chn(%d)!\n", ret, vpss_grp, vpss_chn[1]);
    }
    ret = sample_common_svp_npu_update_input_data_buffer_info(data, size, stride, 0, &g_svp_npu_task[0]);
    sample_svp_check_exps_trace(ret != TD_SUCCESS, SAMPLE_SVP_ERR_LEVEL_ERROR, "update buffer failed!\n");
fail_1:
    (td_void)ss_mpi_sys_munmap(g_svp_npu_vb_virt_addr, g_svp_npu_vb_pool_info.pool_size);
fail_0:
    (td_void)svp_acl_rt_reset_device(g_svp_npu_dev_id);
    return TD_NULL;
}

static td_void sample_svp_npu_acl_pause(td_void)
{
    printf("---------------press Enter key to exit!---------------\n");
    if (g_svp_npu_terminate_signal == TD_TRUE) {
        return;
    }
    (td_void)getchar();
    if (g_svp_npu_terminate_signal == TD_TRUE) {
        return;
    }
}

static td_void sample_svp_npu_acl_set_task_info(td_u32 model_idx)
{
    g_svp_npu_task[0].cfg.max_batch_num = 1;
    g_svp_npu_task[0].cfg.dynamic_batch_num = 1;
    g_svp_npu_task[0].cfg.total_t = 0;
    g_svp_npu_task[0].cfg.is_cached = TD_TRUE;
    g_svp_npu_task[0].cfg.model_idx = model_idx;
}

static td_void sample_svp_npu_acl_set_detection_info(sample_svp_npu_detection_info *detection_info, td_u32 index,
    td_bool is_cpu_rpn)
{
    detection_info->num_name = g_svp_npu_yolo_roi_info[index].roi_num_name;
    detection_info->roi_name = g_svp_npu_yolo_roi_info[index].roi_class_name;
    detection_info->has_background = TD_FALSE;
    detection_info->is_cpu_rpn = is_cpu_rpn;
    detection_info->idx = index;
    /* use PIC_BUTT to be a flag, get the input resolution form om */
    g_svp_npu_media_cfg.pic_type[1] = PIC_BUTT;
    g_svp_npu_terminate_signal = TD_FALSE;
}

static void sample_svp_audio_init()
{
    // 初始化音频编解码器
    ss_mpi_aenc_aac_init();
    ss_mpi_adec_aac_init();
}

static void sample_svp_audio_exit()
{
    // 反初始化音频
    ss_mpi_aenc_aac_deinit();
    ss_mpi_adec_aac_deinit();
}

/* 处理线程管理模块 */
static td_s32 start_processing_thread(sample_svp_npu_thread_args *args)
{
    td_s32 ret;

    ret = sample_common_svp_npu_set_threshold(&g_svp_npu_yolo_threshold[0],
        SAMPLE_SVP_NPU_YOLO_THRESHOLD_NUM, &g_svp_npu_task[0]);

    sample_svp_audio_init();
    g_svp_npu_thread_stop = TD_FALSE;

    ret = pthread_create(&g_svp_npu_thread, 0, sample_svp_npu_acl_vdec_to_vo, (td_void*)args);

    return TD_SUCCESS;
}

/* function : show the sample of yolo. RPN processed by npu */
td_void sample_svp_npu_acl_yolo_npu(void)
{
    td_s32 ret;
    ot_mpp_chn chn;
    td_s32 handle;
    const td_u32 model_idx = 0;
    const td_char *om_model_path = "./data/model/fruit_identify.om";
    sample_svp_npu_detection_info detection_info = {0};
    sample_svp_npu_thread_args args = {SAMPLE_SVP_NPU_YOLO, &detection_info};

    sample_svp_npu_acl_set_detection_info(&detection_info, 0, TD_FALSE);

    if (g_svp_npu_terminate_signal == TD_FALSE) {
        /* init acl */
        ret = sample_svp_npu_acl_init(TD_NULL, TD_FALSE);
        sample_svp_check_exps_return_void(ret != TD_SUCCESS, SAMPLE_SVP_ERR_LEVEL_ERROR, "init failed!\n");

        /* load model */
        ret = sample_common_svp_npu_load_model(om_model_path, model_idx, TD_FALSE);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, process_end0, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "load model failed!\n");

        /* get input resolution */
        ret = sample_common_svp_npu_get_input_resolution(model_idx, 0, &g_svp_npu_media_cfg.pic_size[1]);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, process_end1, SAMPLE_SVP_ERR_LEVEL_ERROR,
            "load model failed!\n");

        /* start vdec vpss venc vo */
        ret = sample_common_svp_create_vb_start_vdec_vpss_vo(&g_svp_npu_vdec_cfg, &g_svp_npu_vdec_param,
            &g_svp_npu_vdec_thread, &g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, process_end1, SAMPLE_SVP_ERR_LEVEL_DEBUG,
            "init media failed!\n");

         // osd init
        sample_osd_init(&args.mpp_osd_info);

        /* set cfg */
        sample_svp_npu_acl_set_task_info(model_idx);

        ret = sample_svp_npu_acl_init_task(1, TD_FALSE, 0);
        sample_svp_check_exps_goto(ret != TD_SUCCESS, process_end2, SAMPLE_SVP_ERR_LEVEL_ERROR, "init task failed!\n");
    }
    /* process */
    if (g_svp_npu_terminate_signal == TD_FALSE) {
        // 处理线程启动
        ret = start_processing_thread(&args);
        sample_svp_check_exps_goto(ret != 0, process_end3, SAMPLE_SVP_ERR_LEVEL_ERROR, "create thread failed!\n");

        (td_void)sample_svp_npu_acl_pause();

        g_svp_npu_thread_stop = TD_TRUE;
        pthread_join(g_svp_npu_thread, TD_NULL);
    }

process_end3:
    (td_void)sample_svp_npu_acl_deinit_task(1, 0);
process_end2:
    sample_osd_exit(&args.mpp_osd_info);
    (td_void)sample_common_svp_destroy_vb_stop_vdec_vpss_vo(&g_svp_npu_vdec_param, &g_svp_npu_vdec_thread,
        &g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
process_end1:
    (td_void)sample_common_svp_npu_unload_model(model_idx);
process_end0:
    (td_void)sample_svp_npu_acl_deinit();
    (td_void)sample_svp_npu_acl_terminate();
    sample_svp_audio_exit();
}

int main(void)
{
#ifdef CONFIG_USER_SPACE
    SDK_init();
#endif
    sample_svp_npu_acl_yolo_npu();
#ifdef CONFIG_USER_SPACE
    SDK_exit();
#endif

    return 0;
}
