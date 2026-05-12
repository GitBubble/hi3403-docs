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
#include <termios.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/prctl.h>
#include <linux/videodev2.h>
#include "sample_comm.h"
#include "sample_common_svp.h"
#include "sample_common_svp_npu.h"
#include "sample_common_svp_npu_model.h"
#include "sample_kcf_track.h"
#include "sample_svp_npu_process.h"

#ifndef OT_SAMPLE_SYS_ALIGN_SIZE
#define OT_SAMPLE_SYS_ALIGN_SIZE 64  // 常见对齐值，根据 SDK 调整
#endif
#ifndef CIF_WIDTH
#define CIF_WIDTH 200
#endif
#ifndef CIF_HEIGHT
#define CIF_HEIGHT 200
#endif

// getch实现放在文件顶部
static int getch(void)
{
    struct termios oldt;
    struct termios newt;
    int ch;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return ch;
}

td_s32 sample_common_svp_get_def_vo_cfg(sample_vo_cfg *vo_cfg);
static td_bool g_svp_npu_terminate_signal = TD_FALSE;
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
    .pic_type = {PIC_1080P, PIC_CIF}, // Changed to PIC_1080P for main stream
    .chn_num = OT_SVP_MAX_VPSS_CHN_NUM,
};

static sample_vdec_attr g_svp_npu_vdec_cfg = {
    .type = OT_PT_MJPEG,
    .mode = OT_VDEC_SEND_MODE_FRAME,
    .width = FHD_WIDTH, // Changed to FHD_WIDTH
    .height = FHD_HEIGHT, // Changed to FHD_HEIGHT
    .sample_vdec_picture.pixel_format = OT_PIXEL_FORMAT_YVU_SEMIPLANAR_420, /* 420:pixel_format */
    .sample_vdec_picture.alpha = 0,      /* 0:alpha */
    .display_frame_num = 1,               /* Keep 1 */
    .frame_buf_cnt = 3,                   /* Keep 3 */
};

static vdec_thread_param g_svp_npu_vdec_param = {
    .chn_id = 0,

    .v4l2_device = "/dev/video0",           // 摄像头设备
    .width = FHD_WIDTH,                     // Changed to FHD_WIDTH
    .height = FHD_HEIGHT,                   // Changed to FHD_HEIGHT
    .pixel_format = V4L2_PIX_FMT_MJPEG,     // MJPEG格式

    .type = OT_PT_MJPEG,
    .stream_mode = OT_VDEC_SEND_MODE_FRAME,
    .interval_time = 1000, /* 1000:interval_time */
    .pts_init = 0,
    .pts_increase = 0,
    .e_thread_ctrl = THREAD_CTRL_START,
    .circle_send = TD_TRUE,
    .milli_sec = 0,
    .min_buf_size = (FHD_WIDTH * FHD_HEIGHT * 3) >> 1, /* 3 Re-calculated for 1080P */
    .fps = 30, /* 30 fps */
};

td_void sample_vb_cfg_init(ot_vb_cfg *vb_cfg, ot_size size_1080p, ot_size size_cif)
{
    td_u64 raw_size_1080p = 0;
    td_u64 raw_size_cif = 0;

    raw_size_1080p = (td_u64)size_1080p.width * size_1080p.height * 3 / 2; /* 3 2 YUV420: 1.5 bytes per pixel */
    vb_cfg->max_pool_cnt = 2;  /* 2 pool */
    vb_cfg->common_pool[0].blk_size = (raw_size_1080p + OT_SAMPLE_SYS_ALIGN_SIZE - 1) & ~(OT_SAMPLE_SYS_ALIGN_SIZE - 1);
    vb_cfg->common_pool[0].blk_cnt = 10;  // 块数，根据需要调整（对于1080P，建议10-20）

    raw_size_cif = (td_u64)size_cif.width * size_cif.height * 3 / 2; /* 3 2 raw size */
    vb_cfg->common_pool[1].blk_size = (raw_size_cif + OT_SAMPLE_SYS_ALIGN_SIZE - 1) & ~(OT_SAMPLE_SYS_ALIGN_SIZE - 1);
    vb_cfg->common_pool[1].blk_cnt = 4;   /* 4 pool */
}

td_void sample_center_rect_init(ot_sample_svp_rect_info *center_rect)
{
    int frame_w = FHD_WIDTH;
    int frame_h = FHD_HEIGHT; // Use FHD resolution for initial box
    int box_w = CIF_WIDTH;
    int box_h = CIF_HEIGHT; // A reasonable box size for FHD
    int x = (frame_w - box_w) / 2; /* 2 half of x */
    int y = (frame_h - box_h) / 2; /* 2 half of y */

    center_rect->num = 1;
    center_rect->rect[0].point[0].x = x;
    center_rect->rect[0].point[0].y = y;
    center_rect->rect[0].point[1].x = x + box_w;
    center_rect->rect[0].point[1].y = y;
    center_rect->rect[0].point[2].x = x + box_w; /* 2 index of 2 */
    center_rect->rect[0].point[2].y = y + box_h; /* 2 index of 2 */
    center_rect->rect[0].point[3].x = x;         /* 3 index of 3 */
    center_rect->rect[0].point[3].y = y + box_h; /* 3 index of 3 */

    printf("[MAIN-2] Setting input rect: (%d,%d) to (%d,%d)\n",
           center_rect->rect[0].point[0].x, center_rect->rect[0].point[0].y,
           center_rect->rect[0].point[2].x, center_rect->rect[0].point[2].y); /* 2 index of 2 */
}

// 1. 程序启动时，推送中心红框，KCF只画红框不训练
static td_void sample_svp_npu_kcf_tracking_loop(td_void)
{
    ot_sample_svp_rect_info center_rect = {0};
    sample_center_rect_init(&center_rect);
    sample_kcf_set_det_rect(&center_rect, 0);

    int tracking_on = 0;

    struct termios oldt;
    struct termios newt;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    newt.c_cc[VMIN]  = 0;   // 非阻塞
    newt.c_cc[VTIME] = 0;
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);

    while (!g_svp_npu_terminate_signal) {
        fd_set read_fds;
        FD_ZERO(&read_fds);
        FD_SET(STDIN_FILENO, &read_fds);
        struct timeval tv = {0, 0}; // 立即返回

        if (select(STDIN_FILENO + 1, &read_fds, NULL, NULL, &tv) > 0) {
            char ch = 0;
            if (read(STDIN_FILENO, &ch, 1) > 0) {
                if (ch == ' ') {
                    tracking_on = !tracking_on;
                    sample_kcf_set_det_rect(&center_rect, tracking_on);
                    printf("[MAIN] %s\n", tracking_on ? "Set to tracking mode" : "Set to red box mode");
                } else if (ch == 'q' || ch == 'Q' || ch == '\x03') { // \x03 = Ctrl+C
                    break;
                }
            }
        }
        usleep(100000); // 100000 100ms，降低 CPU 占用
    }

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
}

td_void sample_svp_npu_acl_v4l2_kcf(td_void)
{
    td_s32 ret;
    ot_vb_cfg vb_cfg = {0};
    ot_size size_cif;
    ot_size size_1080p;

    g_svp_npu_terminate_signal = TD_FALSE; /* 清除退出标志 */
    // 计算 1080P 的 blk_size
    sample_comm_sys_get_pic_size(PIC_1080P, &size_1080p);  // 从 SDK 获取标准分辨率 (1920x1080)
    // 计算 CIF 的 blk_size
    sample_comm_sys_get_pic_size(PIC_CIF, &size_cif);  // 从 SDK 获取标准分辨率 (352x288)
    sample_vb_cfg_init(&vb_cfg, size_1080p, size_cif);
    ret = sample_comm_sys_init(&vb_cfg);  // 初始化系统 VB
    if (ret != TD_SUCCESS) {
        printf("[SYS] init failed 0x%x\n", ret);
        return;
    }
    /* ** 2. 新增：获取默认VO配置 ** */
    ret = sample_common_svp_get_def_vo_cfg(&g_svp_npu_vo_cfg);
    if (ret != TD_SUCCESS) {
        printf("[VO] get default config failed 0x%x\n", ret);
        sample_comm_sys_exit();  // **** 新增：清理系统 VB ****
        return;
    }
    /* 3. 根据采集分辨率重新设定 VB 图像类型，避免无谓的 4K 内存开销 */
    g_svp_npu_media_cfg.pic_type[0] = PIC_1080P;
    g_svp_npu_media_cfg.pic_type[1] = PIC_CIF; /* 备用，不使用 */

    /* 4. 启动 V4L2->VDEC->VPSS->VO 通路（内部自动绑定） */
    ret = sample_common_svp_create_vb_start_vdec_vpss_vo(&g_svp_npu_vdec_cfg, &g_svp_npu_vdec_param,
        &g_svp_npu_vdec_thread, &g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
    if (ret != TD_SUCCESS) {
        printf("[PIPE] create pipeline failed 0x%x\n", ret);
        sample_common_svp_destroy_vb_stop_vdec_vpss_vo(&g_svp_npu_vdec_param, &g_svp_npu_vdec_thread,
            &g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
        return;
    }
    /* 4. 启动 KCF 跟踪——内部线程会从 VPSS grp0 chn0 拉帧并画框 */
    ret = sample_kcf_track_init(&g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
    if (ret != TD_SUCCESS) {
        printf("[KCF] init failed 0x%x\n", ret);
        sample_common_svp_destroy_vb_stop_vdec_vpss_vo(&g_svp_npu_vdec_param, &g_svp_npu_vdec_thread,
            &g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
        return;
    }

    sample_svp_npu_kcf_tracking_loop();

    sample_kcf_track_deinit();
    sample_common_svp_destroy_vb_stop_vdec_vpss_vo(&g_svp_npu_vdec_param, &g_svp_npu_vdec_thread,
        &g_svp_npu_media_cfg, &g_svp_npu_vo_cfg);
    sample_comm_sys_exit();
}
