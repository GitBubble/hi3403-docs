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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <sys/poll.h>
#include <sys/time.h>
#include <fcntl.h>
#include <errno.h>
#include <pthread.h>
#include <math.h>
#include <unistd.h>
#include <signal.h>

#include "sample_comm.h"
#include "easy_log.h"
#include "xvp_common_osd.h"
#include "sample_common_svp_npu.h"

#define OVERLAY_MIN_HANDLE 20
#define BUFFER_SIZE 16
#define CLASS_BUFFER_SIZE 10
#define DOUBLE_OF_SIZE 2
#define BACKGROUND_ALPHA 255
#define OSD_BUFFER_SIZE 32
#define WIDTH_OF_MIN 1920
#define HEIGHT_OF_MIN 1080
#define WIDTH_OF_MAX 2560
#define HEIGHT_OF_MAX 1440

void sample_osd_region_init(ot_rgn_attr *region, ot_size img_size)
{
    td_s32 i;
    region->type = OT_RGN_OVERLAYEX;
    region->attr.overlay.canvas_num = 2; /* 2: canvas num */

    for (i = 0; i < OT_RGN_CLUT_NUM; i++) {
        region->attr.overlay.clut[i] = (td_u32)(0x000fff0f * (i + 1) * (i + 1));
        region->attr.overlay.clut[i] |= 0xff000000;
    }
    region->attr.overlay.pixel_format = OT_PIXEL_FORMAT_ARGB_1555;
    region->attr.overlay.size.width = img_size.width * DOUBLE_OF_SIZE;
    region->attr.overlay.size.height = img_size.height * DOUBLE_OF_SIZE;
    region->attr.overlay.bg_color = 0xffff;
}

void sample_osd_chn_attr_init(ot_rgn_chn_attr *chn_attr)
{
    chn_attr->type = OT_RGN_OVERLAYEX;
    chn_attr->is_show = TD_TRUE;
    chn_attr->attr.overlay_chn.bg_alpha = BACKGROUND_ALPHA;
    chn_attr->attr.overlay_chn.fg_alpha = BACKGROUND_ALPHA;
    chn_attr->attr.overlay_chn.qp_info.enable = TD_FALSE;
    chn_attr->attr.overlay_chn.qp_info.is_abs_qp = TD_FALSE;
    chn_attr->attr.overlay_chn.qp_info.qp_val = 0;
    chn_attr->attr.overlay_chn.dst = OT_RGN_ATTACH_JPEG_MAIN;
    chn_attr->attr.overlay_chn.layer = 0;
}

void sample_osd_info_init(xvp_osd_info *osd_info, ot_rgn_attr region)
{
    osd_info->border_color = 0x0;
    osd_info->font_color = SAMPLE_SVP_NPU_RECT_COLOR;
    osd_info->factor = 2; /* 2: factor of osd info */
    osd_info->width = region.attr.overlay.size.width;
    osd_info->height = region.attr.overlay.size.height;
    osd_info->stride = region.attr.overlay.size.width;
}

int sample_osd_init(sample_mpp_osd_info *mpp_osd_info)
{
    printf("sample_osd_init ...\r\n");
    td_s32 ret;
    ot_rgn_attr region = {0};
    ot_mpp_chn chn = {0};
    ot_rgn_chn_attr chn_attr = {0};
    xvp_osd_info osd_info = {0};
    char osd_str[BUFFER_SIZE] = "scissors 0.00";
    unsigned char gb_str[BUFFER_SIZE] = {0};
    ot_size img_size = {BUFFER_SIZE};

    chn.mod_id = OT_ID_VPSS;
    chn.dev_id = 0;
    chn.chn_id = 0;

    xvp_common_osd_utf8_to_gb2312((unsigned char *)osd_str, strlen(osd_str), gb_str);
    xvp_common_osd_calculate_canvas_size(gb_str, 1, &img_size.width, &img_size.height);
    printf("%s-%d l:%d w:%u h:%u\n", __func__, __LINE__, strlen(gb_str), img_size.width, img_size.height);

    sample_osd_region_init(&region, img_size);

    ret = ss_mpi_rgn_create(mpp_osd_info->handle, &region);
    if (ret != TD_SUCCESS) {
        LOGE("ss_mpi_rgn_create failed with %#x!", ret);
    }

    sample_osd_chn_attr_init(&chn_attr);
    ret = ss_mpi_rgn_attach_to_chn(mpp_osd_info->handle, &chn, &chn_attr);
    if (ret != TD_SUCCESS) {
        LOGE("ss_mpi_rgn_attach_to_chn failed with %#x!", ret);
    }

    sample_osd_info_init(&osd_info, region);
    mpp_osd_info->chn = chn;
    mpp_osd_info->chn_attr = chn_attr;
    mpp_osd_info->osd_info = osd_info;

    xvp_common_osd_init(NULL);

    return 0;
}

int sample_osd_exit(sample_mpp_osd_info *mpp_osd_info)
{
    printf("sample_osd_exit ...\r\n");
    td_s32 ret;
    xvp_common_osd_exit();

    ret = ss_mpi_rgn_detach_from_chn(mpp_osd_info->handle, &mpp_osd_info->chn);
    if (ret != TD_SUCCESS) {
        LOGE("ss_mpi_rgn_detach_from_chn failed with %#x!", ret);
    }

    ret = ss_mpi_rgn_destroy(mpp_osd_info->handle);
    if (ret != TD_SUCCESS) {
        LOGE("ss_mpi_rgn_destroy failed with %#x!", ret);
    }

    return 0;
}

int sample_osd_draw_text(td_float score, td_u16 class_id, td_u16 x, td_u16 y,
    sample_mpp_osd_info mpp_osd_info)
{
    printf("sample_osd_draw_text ...\r\n");
    td_s32 ret;
    const char classes[][CLASS_BUFFER_SIZE] = {"梨子", "西瓜", "橙子", "香蕉", "苹果"};
    char osd_str[OSD_BUFFER_SIZE] = "西瓜 0.00";
    unsigned char gb_str[OSD_BUFFER_SIZE] = {0};
    ot_size img_size = {0};
    ot_bmp bitmap = {0};

    bitmap.width = mpp_osd_info.osd_info.width;
    bitmap.height = mpp_osd_info.osd_info.height;
    bitmap.pixel_format = OT_PIXEL_FORMAT_ARGB_1555;
    bitmap.data = (td_void*)malloc(bitmap.width * bitmap.height * DOUBLE_OF_SIZE);

    ret = snprintf(osd_str, sizeof(osd_str), "%s %0.2f", classes[class_id], score);
    if (ret < 0) {
        printf("%s:snprintf failed, ret:0x%x.\n", __FUNCTION__, ret);
    }
    memset_sp(bitmap.data, bitmap.width * bitmap.height * DOUBLE_OF_SIZE, 0x0,
        bitmap.width * bitmap.height * DOUBLE_OF_SIZE);
    memset_sp(gb_str, sizeof(gb_str), 0, sizeof(gb_str));
    xvp_common_osd_utf8_to_gb2312((unsigned char *)osd_str, strlen(osd_str), gb_str);

    xvp_common_osd_draw_text((unsigned char *)bitmap.data, gb_str, 0, 0, &mpp_osd_info.osd_info);
    ret = ss_mpi_rgn_set_bmp(mpp_osd_info.handle, &bitmap);
    if (ret != TD_SUCCESS) {
        LOGE("ss_mpi_rgn_set_bmp failed with %#x!", ret);
    }
    int min_x = (int)(x * WIDTH_OF_MIN / WIDTH_OF_MAX);
    int min_y = (int)(y * HEIGHT_OF_MIN / HEIGHT_OF_MAX);

    if ((min_x % DOUBLE_OF_SIZE) != 0) {
        min_x = min_x + 1;
    }
    if ((min_y % DOUBLE_OF_SIZE) != 0) {
        min_y = min_y + 1;
    }
    printf("min_x:%d, min_y:%d\r\n", min_x, min_y);
    mpp_osd_info.chn_attr.attr.overlay_chn.point.x = min_x;
    mpp_osd_info.chn_attr.attr.overlay_chn.point.y = min_y;
    mpp_osd_info.chn_attr.is_show = TD_TRUE;
    ss_mpi_rgn_set_display_attr(mpp_osd_info.handle, &mpp_osd_info.chn, &mpp_osd_info.chn_attr);

    if (bitmap.data != NULL) {
        free(bitmap.data);
        bitmap.data = NULL;
    }

    return 0;
}

int sample_osd_clean_text(sample_mpp_osd_info mpp_osd_info)
{
    ss_mpi_rgn_set_display_attr(mpp_osd_info.handle, &mpp_osd_info.chn, &mpp_osd_info.chn_attr);
}
