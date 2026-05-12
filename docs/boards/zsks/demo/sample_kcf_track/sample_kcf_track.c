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
#include <pthread.h>
#include <string.h>
#include <termios.h>
#include <unistd.h>
#include <stdlib.h>
#include "ss_mpi_ive.h"
#include "sample_common_svp.h"
#include "sample_common_ive.h"
#include "sample_kcf_track.h"

#define KCF_QUEUE_LEN  4          /* 简化环形队列深度 */

/* **** 新增：KCF 用到的全局结构 **** */
static sample_yolo_kcf_info g_kcf_info = {0};          /* 资源句柄、互斥锁等 */
static ot_sample_svp_rect_info g_new_rect;             /* NPU 推过来的检测框 */
static pthread_mutex_t g_rect_mutex = PTHREAD_MUTEX_INITIALIZER;
static td_bool g_has_new_rect = TD_FALSE;              /* 标记框是否更新 */
static td_bool g_stop_flag = TD_FALSE;
static pthread_t g_get_frame_thd  = 0;
static pthread_t g_track_thd      = 0;
static int g_kcf_mode = 0; // 0=只画红框, 1=跟踪

// 新增：全局保存最后有效框和丢失计数（替代线程内的局部静态变量）
static ot_sample_svp_rect_info g_last_valid_rect = {0};
static td_s32 g_lost_count = 0;

#define KCF_BOX_WIDTH  200   // 统一宽度
#define KCF_BOX_HEIGHT 200   // 统一高度

static void kcf_rect_to_roi_info(const ot_sample_svp_rect_info *rect, td_u32 base_w, td_u32 base_h)
{
    if (rect->num == 0) {
        return;
    }
    // 只用第0个框，不做任何选择
    g_kcf_info.roi_num = 1;
    g_kcf_info.roi_info[0].roi_id = 0;
    g_kcf_info.roi_info[0].roi.x = rect->rect[0].point[0].x * OT_SAMPLE_QUARTER_OF_1M;
    g_kcf_info.roi_info[0].roi.y = rect->rect[0].point[0].y * OT_SAMPLE_QUARTER_OF_1M;
    g_kcf_info.roi_info[0].roi.width = rect->rect[0].point[1].x - rect->rect[0].point[0].x;
    g_kcf_info.roi_info[0].roi.height = rect->rect[0].point[2].y - rect->rect[0].point[1].y; /* 2 index */
    // 后续宽高限制代码可保留
    if (g_kcf_info.roi_info[0].roi.width > 684) { /* 684 pic width */
        g_kcf_info.roi_info[0].roi.width = 684;   /* 684 pic width */
    }
    if (g_kcf_info.roi_info[0].roi.height > 684) { /* 684 pic height */
        g_kcf_info.roi_info[0].roi.height = 684;   /* 684 pic height */
    }
    if (g_kcf_info.roi_info[0].roi.width  < KCF_BOX_WIDTH) {
        g_kcf_info.roi_info[0].roi.width  = KCF_BOX_WIDTH;
    }
    if (g_kcf_info.roi_info[0].roi.height < KCF_BOX_HEIGHT) {
        g_kcf_info.roi_info[0].roi.height = KCF_BOX_HEIGHT;
    }
    if ((g_kcf_info.roi_info[0].roi.x / OT_SAMPLE_QUARTER_OF_1M) + g_kcf_info.roi_info[0].roi.width > base_w) {
        g_kcf_info.roi_info[0].roi.x = (base_w - g_kcf_info.roi_info[0].roi.width) * OT_SAMPLE_QUARTER_OF_1M;
    }
    if ((g_kcf_info.roi_info[0].roi.y / OT_SAMPLE_QUARTER_OF_1M) + g_kcf_info.roi_info[0].roi.height > base_h) {
        g_kcf_info.roi_info[0].roi.y = (base_h - g_kcf_info.roi_info[0].roi.height) * OT_SAMPLE_QUARTER_OF_1M;
    }
    if (g_kcf_info.roi_info[0].roi.x < 0) {
        g_kcf_info.roi_info[0].roi.x = 0;
    }
    if (g_kcf_info.roi_info[0].roi.y < 0) {
        g_kcf_info.roi_info[0].roi.y = 0;
    }
    if (g_kcf_info.roi_info[0].roi.width & 1) {
        g_kcf_info.roi_info[0].roi.width--;
    }
    if (g_kcf_info.roi_info[0].roi.height & 1) {
        g_kcf_info.roi_info[0].roi.height--;
    }
}

/* **** 简单把 video_frame 填到 ot_svp_img **** */
static void kcf_fill_image(const ot_video_frame_info *frame, ot_svp_img *img)
{
    img->phys_addr[0] = frame->video_frame.phys_addr[0];
    img->phys_addr[1] = frame->video_frame.phys_addr[1];
    img->stride[0]    = frame->video_frame.stride[0];
    img->stride[1]    = frame->video_frame.stride[1];
    img->width        = frame->video_frame.width;
    img->height       = frame->video_frame.height;

    /* 根据 VPSS 输出像素格式决定 IVE 输入类型 */
    switch (frame->video_frame.pixel_format) {
        case OT_PIXEL_FORMAT_YVU_SEMIPLANAR_420:
        case OT_PIXEL_FORMAT_YUV_SEMIPLANAR_420:
            img->type = OT_SVP_IMG_TYPE_YUV420SP;
            break;
        case OT_PIXEL_FORMAT_YVU_SEMIPLANAR_422:
        case OT_PIXEL_FORMAT_YUV_SEMIPLANAR_422:
            img->type = OT_SVP_IMG_TYPE_YUV422SP;
            break;
        default:
            /* 回退为 420，必要时可扩展 */
            img->type = OT_SVP_IMG_TYPE_YUV420SP;
            break;
    }
}

typedef struct {
    td_s32 x;
    td_s32 y;
    td_s32 w;
    td_s32 h;
} BoxPosition;

// 限制框在画面范围内
static void clamp_box_to_frame(BoxPosition* box, const ot_video_frame_info* frame)
{
    const td_s32 max_w = frame->video_frame.width - 2; /* 2 pixel */
    const td_s32 max_h = frame->video_frame.height - 2; /* 2 pixel */

    // 确保最小尺寸
    box->w = (box->w > KCF_BOX_WIDTH) ? box->w : KCF_BOX_WIDTH;
    box->h = (box->h > KCF_BOX_HEIGHT) ? box->h : KCF_BOX_HEIGHT;

    /* 4 允许超出的最大范围（框宽的1/4） */
    const td_s32 max_overlap = box->w / 4;
    if (box->x + box->w > max_w + max_overlap) {
        box->x = max_w - box->w;
    }
    if (box->y + box->h > max_h + max_overlap) {
        box->y = max_h - box->h;
    }
}

// 消除位置抖动
static void smooth_box_position(BoxPosition* current, BoxPosition* last, td_bool* is_first_frame)
{
    if (*is_first_frame) {
        *last = *current;
        *is_first_frame = TD_FALSE;
        return;
    }

    // 微小变化时保持上一帧位置
    if (abs(current->x - last->x) <= 2 && abs(current->y - last->y) <= 2 && /* 2 pixel */
        abs(current->w - last->w) <= 2 && abs(current->h - last->h) <= 2) { /* 2 pixel */
        *current = *last;
    } else {
        *last = *current;
    }
}

// 确保坐标和尺寸为偶数
static void align_to_even(BoxPosition* box)
{
    box->x &= ~1;   // 清除最低位保证为偶数
    box->y &= ~1;
    box->w &= ~1;
    box->h &= ~1;
}

// 设置矩形顶点坐标
static void set_rect_points(ot_sample_svp_rect* rect, const BoxPosition* box)
{
    rect->point[0].x = box->x;
    rect->point[0].y = box->y;
    rect->point[1].x = box->x + box->w;
    rect->point[1].y = box->y;
    rect->point[2].x = box->x + box->w; /* 2 index of 2 */
    rect->point[2].y = box->y + box->h; /* 2 index of 2 */
    rect->point[3].x = box->x;          /* 3 index of 3 */
    rect->point[3].y = box->y + box->h; /* 3 index of 3 */
}

static void kcf_bbox_to_rect(const ot_ive_kcf_bbox bbox[], td_u32 num,
    const ot_video_frame_info* frame, ot_sample_svp_rect_info* rect)
{
    rect->num = (num > 0) ? 1 : 0;
    if (rect->num == 0) {
        return;
    }
    // 初始化转换参数
    static BoxPosition last_box = {0};
    static td_bool first_frame = TD_TRUE;

    BoxPosition current = {
        .x = bbox[0].roi_info.roi.x / OT_SAMPLE_QUARTER_OF_1M,
        .y = bbox[0].roi_info.roi.y / OT_SAMPLE_QUARTER_OF_1M,
        .w = bbox[0].roi_info.roi.width,
        .h = bbox[0].roi_info.roi.height
    };

    // 处理流程
    clamp_box_to_frame(&current, frame);
    smooth_box_position(&current, &last_box, &first_frame);
    align_to_even(&current);

    // 设置输出矩形
    set_rect_points(&rect->rect[0], &current);
}
/* 边界检测辅助函数 */
static td_bool is_touching_border(const ot_sample_svp_rect *rect, td_s32 screen_w,
    td_s32 screen_h, td_s32 threshold)
{
    td_s32 rect_left = rect->point[0].x;
    td_s32 rect_top = rect->point[0].y;
    td_s32 rect_right = rect->point[1].x;
    td_s32 rect_bottom = rect->point[2].y;

    return (rect_left <= threshold) || (rect_top <= threshold) ||
        ((screen_w - rect_right) <= threshold) || ((screen_h - rect_bottom) <= threshold);
}

/* 绘制矩形辅助函数 */
static void draw_tracking_rect(const ot_video_frame_info *frm,
    const ot_sample_svp_rect_info *rect_info, td_bool is_touching_border)
{
    td_u32 color = is_touching_border ? 0x00FFFF00 : 0x0000FF00;
    sample_common_svp_vgs_fill_rect(frm, rect_info, color);
}

/* KCF训练辅助函数 */
static void train_kcf_on_new_rect(const ot_video_frame_info *frm)
{
    pthread_mutex_lock(&g_rect_mutex);
    kcf_rect_to_roi_info(&g_new_rect, frm->video_frame.width, frm->video_frame.height);
    g_has_new_rect = TD_FALSE;
    pthread_mutex_unlock(&g_rect_mutex);

    td_s32 ret = ss_mpi_ive_kcf_get_train_obj(
        g_kcf_info.padding, g_kcf_info.roi_info,
        g_kcf_info.roi_num, &g_kcf_info.cos_win_x,
        &g_kcf_info.cos_win_y, &g_kcf_info.gauss_peak,
        &g_kcf_info.obj_list);
    if (ret != TD_SUCCESS) {
        printf("[KCF] get_train_obj failed 0x%x, w=%u h=%u\n", ret,
               g_kcf_info.roi_info[0].roi.width,
               g_kcf_info.roi_info[0].roi.height);
    } else {
        printf("[KCF] train_obj_num=%u\n", g_kcf_info.obj_list.train_obj_num);
    }
}

/* 处理丢失目标情况 */
static void handle_lost_target(const ot_video_frame_info *frm)
{
    g_lost_count++;
    printf("[KCF] Lost target (count=%d), keep last rect\n", g_lost_count);

    if (g_last_valid_rect.num > 0) {
        sample_common_svp_vgs_fill_rect(frm, &g_last_valid_rect, 0x00FFFF00);
    }

    if (g_lost_count >= 10 && g_last_valid_rect.num > 0) { /* 10 lost count */
        pthread_mutex_lock(&g_rect_mutex);
        g_new_rect = g_last_valid_rect;
        g_has_new_rect = TD_TRUE;
        pthread_mutex_unlock(&g_rect_mutex);
        g_lost_count = 0;
    }
}

static void process_kcf_tracking(const ot_video_frame_info* frm,
    ot_sample_svp_rect_info* draw_rect)
{
    td_s32 ret;
    ot_ive_handle handle = 0;
    ot_svp_img src_img;

    // 填充图像数据
    kcf_fill_image(frm, &src_img);

    // 执行KCF处理
    ret = ss_mpi_ive_kcf_proc(&handle, &src_img, &g_kcf_info.obj_list,
        &g_kcf_info.kcf_proc_ctrl, TD_TRUE);
    if (ret != TD_SUCCESS) {
        printf("[KCF] kcf_proc failed 0x%x\n", ret);
        g_kcf_info.bbox_obj_num = 0;
        return;
    }

    // 获取目标边界框
    ret = ss_mpi_ive_kcf_get_obj_bbox(&g_kcf_info.obj_list, g_kcf_info.bbox,
        &g_kcf_info.bbox_obj_num, &g_kcf_info.kcf_bbox_ctrl);
    if (ret != TD_SUCCESS) {
        printf("[KCF] get_obj_bbox failed 0x%x\n", ret);
        g_kcf_info.bbox_obj_num = 0;
        return;
    }

    // 处理有效目标
    if (g_kcf_info.bbox_obj_num > 0) {
        kcf_bbox_to_rect(g_kcf_info.bbox, g_kcf_info.bbox_obj_num, frm, draw_rect);

        td_s32 screen_w = frm->video_frame.width - 2;
        td_s32 screen_h = frm->video_frame.height - 2;
        td_bool touching_border = is_touching_border(
            &draw_rect->rect[0], screen_w, screen_h, 5);

        draw_tracking_rect(frm, draw_rect, touching_border);
        g_last_valid_rect = *draw_rect;
        g_lost_count = 0;
    }
}

/* 主线程函数（重构后） */
static void *kcf_track_thread(void *args)
{
    (void)args;
    td_s32 ret;
    const ot_vo_layer vo_layer = 0;
    const ot_vo_chn vo_chn = 0;
    const td_s32 milli_sec = 20;
    const td_s32 vpss_grp = 0;
    const td_s32 vpss_chn = 0;
    ot_sample_svp_rect_info draw_rect = {0};

    while (!g_stop_flag) {
        ot_video_frame_info frm;
        ret = ss_mpi_vpss_get_chn_frame(vpss_grp, vpss_chn, &frm, milli_sec);
        if (ret != TD_SUCCESS) {
            usleep(1000); // 1000 sleep 1ms
            continue;
        }

        // 红框模式处理
        if (g_kcf_mode == 0) {
            ot_ive_kcf_bbox initial_bbox[1];
            initial_bbox[0].roi_info = g_kcf_info.roi_info[0];
            kcf_bbox_to_rect(initial_bbox, 1, &frm, &draw_rect);
            sample_common_svp_vgs_fill_rect(&frm, &draw_rect, 0x00FF0000);
            g_kcf_info.bbox_obj_num = 0;
            goto send_and_release;
        }

        // 训练模式处理
        if (g_has_new_rect) {
            train_kcf_on_new_rect(&frm);
        }

        // 跟踪模式处理
        if (g_kcf_mode == 1 && (g_kcf_info.obj_list.train_obj_num != 0 ||
            g_kcf_info.obj_list.track_obj_num != 0)) {
            process_kcf_tracking(&frm, &draw_rect);
        } else if (g_kcf_mode == 1) {
            g_kcf_info.bbox_obj_num = 0;
        }
        // 处理丢失目标
        if (g_kcf_mode == 1 && g_kcf_info.bbox_obj_num == 0) {
            handle_lost_target(&frm);
        }

    send_and_release:
        ret = sample_common_svp_venc_vo_send_stream(&g_kcf_info.svp_switch, 0,
            vo_layer, vo_chn, &frm);
        if (ret != TD_SUCCESS) {
            printf("[KCF] sample_common_svp_venc_vo_send_stream failed 0x%x\n", ret);
        }
        (td_void)ss_mpi_vpss_release_chn_frame(vpss_grp, vpss_chn, &frm);
        usleep(8000); // 8000 sleep 8ms
    }
    return TD_NULL;
}

static void sample_kcf_info_init(ot_svp_mem_info total_mem, td_u32 list_mem_size)
{
    g_kcf_info.list_mem = total_mem;
    g_kcf_info.list_mem.size = list_mem_size;

    g_kcf_info.gauss_peak.phys_addr = g_kcf_info.list_mem.phys_addr + list_mem_size;
    g_kcf_info.gauss_peak.virt_addr = g_kcf_info.list_mem.virt_addr + list_mem_size;
    g_kcf_info.gauss_peak.size = SAMPLE_KCF_GAUSS_PEAK_SIZE;

    g_kcf_info.cos_win_x.phys_addr = g_kcf_info.gauss_peak.phys_addr + SAMPLE_KCF_GAUSS_PEAK_SIZE;
    g_kcf_info.cos_win_x.virt_addr = g_kcf_info.gauss_peak.virt_addr + SAMPLE_KCF_GAUSS_PEAK_SIZE;
    g_kcf_info.cos_win_x.size = SAMPLE_KCF_COS_WIN_SIZE;

    g_kcf_info.cos_win_y.phys_addr = g_kcf_info.cos_win_x.phys_addr + SAMPLE_KCF_COS_WIN_SIZE;
    g_kcf_info.cos_win_y.virt_addr = g_kcf_info.cos_win_x.virt_addr + SAMPLE_KCF_COS_WIN_SIZE;
    g_kcf_info.cos_win_y.size = SAMPLE_KCF_COS_WIN_SIZE;

    g_kcf_info.kcf_proc_ctrl.tmp_buf.phys_addr =
        g_kcf_info.cos_win_y.phys_addr + SAMPLE_KCF_COS_WIN_SIZE;
    g_kcf_info.kcf_proc_ctrl.tmp_buf.virt_addr =
        g_kcf_info.cos_win_y.virt_addr + SAMPLE_KCF_COS_WIN_SIZE;
    g_kcf_info.kcf_proc_ctrl.tmp_buf.size = SAMPLE_KCF_TEMP_BUF_SIZE;
}

static void sample_kcf_proc_ctrl_init(void)
{
    g_kcf_info.kcf_proc_ctrl.csc_mode = OT_IVE_CSC_MODE_VIDEO_BT709_YUV_TO_RGB;
    /* 0.001 learning rate  1024 Quantization scaling factor 32 Additional scaling factor */
    g_kcf_info.kcf_proc_ctrl.interp_factor = (td_u1q15)(0.001 * 1024 * 32); /* 降低学习率，减少抖动 ≈327 */
    g_kcf_info.kcf_proc_ctrl.lamda = 10; /* 10 lamda */
    g_kcf_info.kcf_proc_ctrl.sigma = (td_u0q8)(0.5 * 256); /* 0.5 * 256 降低sigma，提高稳定性 ≈77 */
    g_kcf_info.kcf_proc_ctrl.norm_trunc_alfa = (td_u4q12)(0.15 * 4096); /* 0.15 * 4096 降低截断因子 ≈614 */
    g_kcf_info.kcf_proc_ctrl.response_threshold = 5;  /* 5 提高阈值，减少误检 */
    g_kcf_info.kcf_proc_ctrl.core_id = OT_IVE_KCF_CORE0;
}

static void sample_kcf_bbox_ctrl_init(void)
{
    g_kcf_info.kcf_bbox_ctrl.max_bbox_num = SAMPLE_KCF_LIST_NODE_MAX;
    g_kcf_info.kcf_bbox_ctrl.response_threshold = 12;  /* 12 threshold */
    g_kcf_info.padding = 48;   /* 48 padding */
}

static td_s32 sample_kcf_media_cfg(const ot_sample_svp_media_cfg *media_cfg)
{
    if (media_cfg != TD_NULL) {
        g_kcf_info.svp_switch = media_cfg->svp_switch;   /* {TD_FALSE, TD_TRUE} */
    } else {
        g_kcf_info.svp_switch.is_venc_open = TD_FALSE;
        g_kcf_info.svp_switch.is_vo_open   = TD_TRUE;
    }

    g_stop_flag = TD_FALSE;
    // Removed g_get_frame_thd creation
    if (pthread_create(&g_track_thd, NULL, kcf_track_thread, NULL)   != 0) {
        return TD_FAILURE;
    }
    // 在 sample_kcf_track_init 末尾添加
    g_kcf_info.roi_num = 1;
    g_kcf_info.roi_info[0].roi_id = 0;
    td_u32 safe_margin = 50; /* 50 Edge safety distance */
    td_u32 init_x = (1920 - KCF_BOX_WIDTH) / 2; /* 1920 PIC of width */
    td_u32 init_y = (1080 - KCF_BOX_HEIGHT) / 2; /* 1080 PIC of width */
    // 确保初始位置不靠近边缘（至少50像素缓冲）
    if (init_x < safe_margin) init_x = safe_margin;
    if (init_y < safe_margin) init_y = safe_margin;
    g_kcf_info.roi_info[0].roi.x = init_x * OT_SAMPLE_QUARTER_OF_1M;
    g_kcf_info.roi_info[0].roi.y = init_y * OT_SAMPLE_QUARTER_OF_1M;
    g_kcf_info.roi_info[0].roi.width = KCF_BOX_WIDTH;
    g_kcf_info.roi_info[0].roi.height = KCF_BOX_HEIGHT;

    return TD_SUCCESS;
}

td_s32 sample_kcf_track_init(const ot_sample_svp_media_cfg *media_cfg, sample_vo_cfg *vo_cfg)
{
    memset(&g_kcf_info, 0, sizeof(g_kcf_info));
    pthread_mutex_init(&g_kcf_info.det_mutex, NULL);

    /* ---------------- KCF 内存初始化 ---------------- */
    td_s32  ret;
    td_u32 list_mem_size;
    td_u32 total_size;

    /* 1. 计算对象链表大小 */
    ret = ss_mpi_ive_kcf_get_mem_size(SAMPLE_KCF_LIST_NODE_MAX, &list_mem_size);
    if (ret != TD_SUCCESS) {
        printf("kcf get mem size failed 0x%x\n", ret);
        return ret;
    }

    /* 2. 申请一整块连续内存 (list + gauss + cosX + cosY + tmp) */
    total_size = list_mem_size + SAMPLE_KCF_GAUSS_PEAK_SIZE +
        SAMPLE_KCF_COS_WIN_SIZE * 2 + SAMPLE_KCF_TEMP_BUF_SIZE; /* 2 is a number */

    ot_svp_mem_info total_mem = {0};
    ret = sample_common_ive_create_mem_info(&total_mem, total_size);
    if (ret != TD_SUCCESS) {
        printf("kcf alloc total mem failed 0x%x\n", ret);
        return ret;
    }

    /* 3. 切分子区域 */
    sample_kcf_info_init(total_mem, list_mem_size);

    /* 4. 创建对象链表 */
    ret = ss_mpi_ive_kcf_create_obj_list(&g_kcf_info.list_mem, SAMPLE_KCF_LIST_NODE_MAX, &g_kcf_info.obj_list);
    if (ret != TD_SUCCESS) {
        printf("create obj list err 0x%x\n", ret);
        return ret;
    }

    /* 5. 生成 GaussPeak / CosWin 窗口 */
    g_kcf_info.padding = 48; /* 48 is 1.5*32 */
    ret = ss_mpi_ive_kcf_create_gauss_peak(g_kcf_info.padding, &g_kcf_info.gauss_peak);
    if (ret != TD_SUCCESS) {
        printf("create gauss peak err 0x%x\n", ret);
        return ret;
    }
    ret = ss_mpi_ive_kcf_create_cos_win(&g_kcf_info.cos_win_x, &g_kcf_info.cos_win_y);
    if (ret != TD_SUCCESS) {
        printf("create cos win err 0x%x\n", ret);
        return ret;
    }

    /* 6. 填写 kcf_proc_ctrl 默认参数 */
    sample_kcf_proc_ctrl_init();

    /* 7. 初始化 bbox ctrl */
    sample_kcf_bbox_ctrl_init();

    /* 8. 继承媒体配置中的开关，使 KCF 线程能够把结果帧送到 VO/VENC */
    ret = sample_kcf_media_cfg(media_cfg);
    if (ret != TD_SUCCESS) {
        printf("kcf media cfg err 0x%x\n", ret);
        return ret;
    }

    return TD_SUCCESS;
}

void sample_kcf_track_deinit(void)
{
    g_stop_flag = TD_TRUE;
    // Removed g_get_frame_thd join
    if (g_track_thd) {
        pthread_join(g_track_thd, NULL);
    }
    /* 释放 KCF 内存与对象链表 */
    ss_mpi_ive_kcf_destroy_obj_list(&g_kcf_info.obj_list);

    /* 仅需释放一次整块内存，避免重复 free 导致 mmb not found 警告 */
    sample_svp_mmz_free(g_kcf_info.list_mem.phys_addr, g_kcf_info.list_mem.virt_addr);

    pthread_mutex_destroy(&g_kcf_info.det_mutex);
}

// 修改 sample_kcf_set_det_rect，只在切换到跟踪模式时设置 g_has_new_rect
void sample_kcf_set_det_rect(const ot_sample_svp_rect_info *rect, int mode)
{
    pthread_mutex_lock(&g_rect_mutex);
    g_new_rect   = *rect;
    if (mode == 1) {
        ss_mpi_ive_kcf_destroy_obj_list(&g_kcf_info.obj_list);
        ss_mpi_ive_kcf_create_obj_list(&g_kcf_info.list_mem, SAMPLE_KCF_LIST_NODE_MAX, &g_kcf_info.obj_list);
        g_has_new_rect = TD_TRUE;
        // 重置上一次的黄色框信息，避免切换时残留
        memset(&g_last_valid_rect, 0, sizeof(ot_sample_svp_rect_info));
        g_lost_count = 0;
    } else if (mode == 0) { // 切换到红色框模式：强制红框回到中央
        // 计算屏幕中央坐标（基于1920x1080分辨率）
        td_u32 center_x = (1920 - KCF_BOX_WIDTH) / 2;  // 中央x坐标
        td_u32 center_y = (1080 - KCF_BOX_HEIGHT) / 2; // 中央y坐标
        // 重置红框的初始位置到中央（与初始化时一致）
        g_kcf_info.roi_info[0].roi.x = center_x * OT_SAMPLE_QUARTER_OF_1M;
        g_kcf_info.roi_info[0].roi.y = center_y * OT_SAMPLE_QUARTER_OF_1M;
        // 保持宽高不变（KCF_BOX_WIDTH x KCF_BOX_HEIGHT）
        g_kcf_info.roi_info[0].roi.width = KCF_BOX_WIDTH;
        g_kcf_info.roi_info[0].roi.height = KCF_BOX_HEIGHT;
    }
    g_kcf_mode = mode;

    if (mode == 0) {
        g_kcf_info.obj_list.train_obj_num = 0;
        g_kcf_info.obj_list.track_obj_num = 0;
        g_kcf_info.bbox_obj_num = 0;
    }
    pthread_mutex_unlock(&g_rect_mutex);
}

td_u32 sample_kcf_get_bbox_num(void)
{
    return g_kcf_info.bbox_obj_num;
}
