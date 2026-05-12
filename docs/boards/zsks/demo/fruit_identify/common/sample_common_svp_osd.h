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

#ifndef SAMPLE_COMMON_SVP_OSD_H
#define SAMPLE_COMMON_SVP_OSD_H
#include "ot_common.h"
#include "sample_comm.h"
#include "xvp_common_osd.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    ot_rgn_chn_attr chn_attr;
    xvp_osd_info osd_info;
    td_s32 handle;
    ot_mpp_chn chn;
} sample_mpp_osd_info;

int sample_osd_init(sample_mpp_osd_info *mpp_osd_info);
int sample_osd_exit(sample_mpp_osd_info *mpp_osd_info);
int sample_osd_draw_text(td_float score, td_u16 class_id, td_u16 x, td_u16 y, sample_mpp_osd_info mpp_osd_info);
int sample_osd_clean_text(sample_mpp_osd_info mpp_osd_info);

#ifdef __cplusplus
}
#endif

#endif
