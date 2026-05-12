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
#include <signal.h>
#include <getopt.h>
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include "host_uvc.h"

#ifdef __cplusplus
#if __cplusplus
extern "C" {
#endif
#endif

#define array_size(a)    (sizeof(a) / sizeof((a)[0]))

format_info g_pixel_formats[] = {
    { "YUYV", V4L2_PIX_FMT_YUYV, 1 },
    { "MJPEG", V4L2_PIX_FMT_MJPEG, 1 },
    { "H264", V4L2_PIX_FMT_H264, 1 },
    { "H265", V4L2_PIX_FMT_H265, 1 },
    { "NV12", V4L2_PIX_FMT_NV12, 1 },
    { "NV21", V4L2_PIX_FMT_NV21, 1 },
};

static struct option g_opts[] = {
    {"file", 2, 0, 'F'}, /* 2 is a number */
    {"format", 1, 0, 'f'},
    {"help", 0, 0, 'h'},
    {"size", 1, 0, 's'},
    {0, 0, 0, 0}
};

static const format_info *sample_uvc_v4l2_format_by_fourcc(td_u32 fourcc)
{
    td_u32 i;

    for (i = 0; i < array_size(g_pixel_formats); ++i) {
        if (g_pixel_formats[i].fourcc == fourcc) {
            return &g_pixel_formats[i];
        }
    }
    return TD_NULL;
}

static td_void sample_uvc_usage(const td_char *argv0)
{
    printf("sample_uvc_usage: %s device [options]\n", argv0);
    printf("supported options:\n");
    printf("-f, --format format             set the video format\n");
    printf("-F, --file[=name]               write file\n");
    printf("-h, --help                      show help info\n");
    printf("-s, --size WxH                  set the frame size (eg. 1920x1080)\n\n");
    printf("inquire USB device format: ./sample_uvc  --enum-formats\n\n");
    printf("example of setting USB device format:\n");
    printf("    ./opencv_dnn  /dev/media0  -fH264  -s1920x1080 -Ftest.h264\n");
    printf("    ./opencv_dnn  /dev/media0  -fH265  -s1920x1080 -Ftest.h265\n");
    printf("    ./opencv_dnn  /dev/media0  -fMJPEG -s1920x1080 -Ftest.mjpg\n");
    printf("    ./opencv_dnn  /dev/media0  -fYUYV  -s1920x1080 -Ftest.yuv\n");
    printf("    ./opencv_dnn  /dev/media0  -fNV21  -s640x360   -Ftest.yuv\n\n");
    printf("note: set macro MEDIA_WORK to 0 to write file on disk.\n\n");
}

static const format_info *sample_uvc_v4l2_format_by_name(const td_char *name)
{
    td_u32 i;
    for (i = 0; i < array_size(g_pixel_formats); ++i) {
        if (!strcmp(g_pixel_formats[i].name, name)) {
            return &g_pixel_formats[i];
        }
    }
    return TD_NULL;
}

static td_void sample_uvc_list_formats(td_void)
{
    td_u32 i;
    for (i = 0; i < array_size(g_pixel_formats); i++) {
        sample_print("%s (\"%c%c%c%c\", %u planes)\n", g_pixel_formats[i].name, g_pixel_formats[i].fourcc & 0xff,
            (g_pixel_formats[i].fourcc >> 8) & 0xff, (g_pixel_formats[i].fourcc >> 16) & 0xff,  /* 8,16:shift */
            (g_pixel_formats[i].fourcc >> 24) & 0xff, g_pixel_formats[i].n_planes);             /* 24:shift */
    }
}

static td_s32 sample_uvc_get_opt(td_s32 argc, td_char *argv[], uvc_ctrl_info *ctrl_info)
{
    td_s32 c;
    const format_info *info;
    td_char *endptr;

    while ((c = getopt_long(argc, argv, "B:c::Cd:f:F::hi:Iln:p::q:r:R::s:t:uw:x:", g_opts, TD_NULL)) != -1) {
        switch (c) {
            case 'f':
                if (!strcmp("help", optarg)) {
                    sample_uvc_list_formats();
                    return TD_FAILURE;
                }
                ctrl_info->do_set_format = 1;
                info = sample_uvc_v4l2_format_by_name(optarg);
                if (info == TD_NULL) {
                    sample_print("Unsupported video format '%s'\n", optarg);
                    return TD_FAILURE;
                }
                ctrl_info->pixelformat = info->fourcc;
                break;
            case 'F':
                ctrl_info->do_file = 1;
                if (optarg) {
                    ctrl_info->pattern = optarg;
                }
                break;
            case 'h':
                sample_uvc_usage(argv[0]);
                return TD_FAILURE;
            case 's':
                ctrl_info->do_capture = 1;
                ctrl_info->do_set_format = 1;
                ctrl_info->width = strtol(optarg, &endptr, 10); /* 10:base */
                if (*endptr != 'x' || endptr == optarg) {
                    sample_print("Invalid size '%s'\n", optarg);
                    return TD_FAILURE;
                }
                ctrl_info->height = strtol(endptr + 1, &endptr, 10); /* 10:base */
                if (*endptr != 0) {
                    sample_print("Invalid size '%s'\n", optarg);
                    return TD_FAILURE;
                }
                break;
            default:
                sample_print("Run %s -h for help.\n", argv[0]);
                return TD_FAILURE;
        }
    }
    return TD_SUCCESS;
}

static td_void sample_uvc_ctrl_info_init(uvc_ctrl_info *ctrl_info)
{
    ctrl_info->pattern = "frame-#.bin";
    ctrl_info->width = 640;     /* 640:width */
    ctrl_info->height = 480;    /* 480:height */
    ctrl_info->pixelformat = V4L2_PIX_FMT_YUYV;
}

const td_char *sample_uvc_v4l2_format_name(td_u32 fourcc)
{
    const format_info *format;
    static td_char format_name[5];     /* 5: array len */
    td_u32 i;
    format = sample_uvc_v4l2_format_by_fourcc(fourcc);
    if (format) {
        return format->name;
    }

    for (i = 0; i < 4; ++i) {       /* 4: format */
        format_name[i] = fourcc & 0xff;
        fourcc >>= 8;               /* 8: shift */
    }

    format_name[4] = '\0';     /* 4: end */
    return format_name;
}

td_s32 sample_host_uvc(td_s32 argc, td_char *argv[], uvc_ctrl_info *ctrl_info)
{
    int ret;
    sample_uvc_ctrl_info_init(ctrl_info);
    ret = sample_uvc_get_opt(argc, argv, ctrl_info);
    if (ret != TD_SUCCESS) {
        return TD_FAILURE;
    }
    if (optind >= argc) {
        sample_uvc_usage(argv[0]);
        return TD_FAILURE;
    }
    return TD_SUCCESS ;
}

#ifdef __cplusplus
#if __cplusplus
}
#endif
#endif /* End of #ifdef __cplusplus */
