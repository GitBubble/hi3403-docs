/*
 * Copyright (c) 2025 HiSilicon (Shanghai) Technologies Co., Ltd.
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
 */
#ifndef __HOST_UVC_H__
#define __HOST_UVC_H__

#include <linux/videodev2.h>
#include <linux/uvcvideo.h>
#include <linux/usb/video.h>
#include "sample_comm.h"
#ifdef __cplusplus
#if __cplusplus
extern "C" {
#endif
#endif

#ifndef V4L2_PIX_FMT_H265
#define V4L2_PIX_FMT_H265     v4l2_fourcc('H', '2', '6', '5') /* H.265 aka HEVC */
#endif

typedef struct {
    const td_char *name;
    td_u32 fourcc;
    td_char n_planes;
} format_info;

typedef struct {
    const td_char *pattern;
    const td_char *type_name;
    td_s32 do_capture;
    td_s32 do_set_format;
    td_u32 pixelformat;
    td_s32 do_file;
    td_u32 input;
    td_u32 width;
    td_u32 height;
} uvc_ctrl_info;

td_s32 sample_host_uvc(td_s32 argc, td_char *argv[], uvc_ctrl_info *ctrl_info);
const td_char *sample_uvc_v4l2_format_name(td_u32 fourcc);

#ifdef __cplusplus
#if __cplusplus
}
#endif
#endif /* End of #ifdef __cplusplus */

#endif /* end of #ifndef __HOST_UVC_H__ */
