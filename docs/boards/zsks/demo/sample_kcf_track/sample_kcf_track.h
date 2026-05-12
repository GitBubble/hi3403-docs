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

#ifndef SAMPLE_KCF_TRACK_H
#define SAMPLE_KCF_TRACK_H

#include <pthread.h>
#include "sample_comm.h"
#include "ot_common_svp.h"
#include "sample_common_svp.h"
#include "sample_common_ive.h"

#ifndef SAMPLE_YOLO_KCF_INFO_T
#define SAMPLE_YOLO_KCF_INFO_T
#define SAMPLE_KCF_MAX_OBJ  4

typedef struct {
    ot_ive_roi_info      roi_info[SAMPLE_KCF_MAX_OBJ];
    td_u32               roi_num;

    /* 训练相关内存 */
    ot_svp_mem_info      cos_win_x;
    ot_svp_mem_info      cos_win_y;
    ot_svp_mem_info      gauss_peak;
    ot_svp_mem_info      list_mem;     /* KCF 对象链表内存 */
    ot_ive_kcf_obj_list  obj_list;
    ot_ive_kcf_proc_ctrl kcf_proc_ctrl;
    ot_ive_kcf_bbox_ctrl kcf_bbox_ctrl;

    /* 跟踪结果 */
    ot_ive_kcf_bbox      bbox[SAMPLE_KCF_MAX_OBJ];
    td_u32               bbox_obj_num;

    /* 帧缓存 */
    ot_video_frame_info  frame_info_arr[1];

    /* 互斥 */
    pthread_mutex_t      det_mutex;

    /* 其它 */
    td_u3q5              padding;        /* 调 API 需要的 padding 值 */
    ot_sample_svp_switch svp_switch;
    sample_vo_cfg      vo_cfg;           /* VO configuration */
} sample_yolo_kcf_info;
#endif

#define SAMPLE_KCF_LIST_NODE_MAX   64
#define SAMPLE_KCF_GAUSS_PEAK_SIZE  455680
#define SAMPLE_KCF_COS_WIN_SIZE     832
#define SAMPLE_KCF_TEMP_BUF_SIZE    47616

/* 说明：
 * 1. sample_kcf_track_init 内部会创建获取帧+跟踪线程并一直运行；
 * 2. 检测线程（NPU/RFCN 或 YOLO）每获得一次新检测框，调用 sample_kcf_set_det_rect
 *    把第一只目标的 rect 信息推送给 KCF，KCF 会在下一帧里自动训练 / 跟踪；
 * 3. sample_kcf_track_deinit 会安全地结束线程并释放内存。
 */
td_s32 sample_kcf_track_init(const ot_sample_svp_media_cfg *media_cfg, sample_vo_cfg *vo_cfg);
void   sample_kcf_track_deinit(void);

void sample_kcf_set_det_rect(const ot_sample_svp_rect_info *rect, int mode);

td_u32 sample_kcf_get_bbox_num(void);

#endif /* SAMPLE_KCF_TRACK_H */
