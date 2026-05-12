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

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <pthread.h>
#include <errno.h>
#include <signal.h>
#include <limits.h>

#include "sample_comm.h"
#include "audio_aac_adp.h"
#include "audio_dl_adp.h"
#include "ot_resample.h"

#include "sample_audio.h"

static ot_payload_type g_payload_type = OT_PT_AAC;
static td_bool g_aio_resample  = TD_FALSE;
static ot_audio_sample_rate g_in_sample_rate  = OT_AUDIO_SAMPLE_RATE_BUTT;
static ot_audio_sample_rate g_out_sample_rate = OT_AUDIO_SAMPLE_RATE_BUTT;

#define sample_dbg(ret) \
    do { \
        printf("ret = %#x, fuc:%s, line:%d\n", ret, __FUNCTION__, __LINE__); \
    } while (0)

#define sample_res_check_null_ptr(ptr) \
    do { \
        if ((td_u8*)(ptr) == TD_NULL) { \
            printf("ptr is TD_NULL,fuc:%s,line:%d\n", __FUNCTION__, __LINE__); \
            return TD_FAILURE; \
        } \
    } while (0)

/* function : PT number to string */
static char *sample_audio_pt2_str(ot_payload_type type)
{
    if (type == OT_PT_G711A) {
        return "g711a";
    } else if (type == OT_PT_G711U) {
        return "g711u";
    } else if (type == OT_PT_ADPCMA) {
        return "adpcm";
    } else if (type == OT_PT_G726) {
        return "g726";
    } else if (type == OT_PT_LPCM) {
        return "pcm";
    } else if (type == OT_PT_AAC) {
        return "aac";
    } else {
        return "data";
    }
}

/* function : open adec file */
static FILE *sample_audio_open_adec_file(ot_adec_chn ad_chn, ot_payload_type type,
    const td_char *file_name1, const td_char *file_name2)
{
    FILE *fd = TD_NULL;
    td_char asz_file_name[FILE_NAME_LEN] = {0};
    td_s32 ret;
    td_char path[PATH_MAX] = {0};

    /* create file for save stream */
#ifdef __LITEOS__
    ret = snprintf_s(asz_file_name, FILE_NAME_LEN, FILE_NAME_LEN - 1,
        "/sharefs/audio_chn%d.%s", ad_chn, sample_audio_pt2_str(type));
#else
    ret = snprintf_s(asz_file_name, FILE_NAME_LEN, FILE_NAME_LEN - 1,
        "%s/%s/audio_chn%d.%s", file_name1, file_name2, ad_chn, sample_audio_pt2_str(type));
#endif
    if (ret < 0) {
        printf("[func]:%s [line]:%d [info]:%s\n", __FUNCTION__, __LINE__, "get adec file name failed");
        return TD_NULL;
    }

    if (asz_file_name[0] == '\0') {
        printf("[func]:%s [line]:%d [info]:%s\n", __FUNCTION__, __LINE__, "adec file name is NULL");
        return TD_NULL;
    }

    if (strlen(asz_file_name) > (FILE_NAME_LEN - 1)) {
        printf("[func]:%s [line]:%d [info]:%s\n", __FUNCTION__, __LINE__, "adec file name extra long");
        return TD_NULL;
    }

    if (realpath(asz_file_name, path) == TD_NULL) {
        printf("[func]:%s [line]:%d [info]:%s\n", __FUNCTION__, __LINE__, "adec file name realpath fail");
        return TD_NULL;
    }

    fd = fopen(path, "rb");
    if (fd == NULL) {
        printf("%s: open file %s failed\n", __FUNCTION__, asz_file_name);
        return NULL;
    }
    printf("open stream file:\"%s\" for adec ok\n", asz_file_name);
    return fd;
}

static td_void sample_audio_adec_ao_init_param(ot_aio_attr *aio_attr, ot_audio_dev *ao_dev)
{
    aio_attr->sample_rate  = OT_AUDIO_SAMPLE_RATE_48000;
    aio_attr->bit_width    = OT_AUDIO_BIT_WIDTH_16;
    aio_attr->work_mode    = OT_AIO_MODE_I2S_MASTER;
    aio_attr->snd_mode     = OT_AUDIO_SOUND_MODE_STEREO;
    aio_attr->expand_flag  = 0;
    aio_attr->frame_num    = 30; /* 30:frame num */
    if (g_payload_type == OT_PT_AAC) {
        aio_attr->point_num_per_frame = AACLC_SAMPLES_PER_FRAME;
    } else {
        aio_attr->point_num_per_frame = SAMPLE_AUDIO_POINT_NUM_PER_FRAME;
    }
    aio_attr->chn_cnt      = 2; /* 2:chn num */
#ifdef OT_ACODEC_TYPE_INNER
    *ao_dev = SAMPLE_AUDIO_INNER_AO_DEV;
    aio_attr->clk_share  = 1;
    aio_attr->i2s_type   = OT_AIO_I2STYPE_INNERCODEC;
#else
    *ao_dev = SAMPLE_AUDIO_EXTERN_AO_DEV;
    aio_attr->clk_share  = 1;
    aio_attr->i2s_type   = OT_AIO_I2STYPE_EXTERN;
#endif
    g_aio_resample = TD_FALSE;
    g_in_sample_rate  = OT_AUDIO_SAMPLE_RATE_BUTT;
    g_out_sample_rate = OT_AUDIO_SAMPLE_RATE_BUTT;
}

td_void sample_audio_adec_ao_inner(ot_audio_dev ao_dev, ot_ao_chn ao_chn, ot_adec_chn ad_chn,
    const td_char *file_name1, const td_char *file_name2)
{
    td_s32 ret;
    FILE *fd = NULL;

    ret = sample_comm_audio_ao_bind_adec(ao_dev, ao_chn, ad_chn);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
        return;
    }

    fd = sample_audio_open_adec_file(ad_chn, g_payload_type, file_name1, file_name2);
    if (fd == TD_NULL) {
        sample_dbg(TD_FAILURE);
        goto adec_ao_err0;
    }

    ret = sample_comm_audio_creat_trd_file_adec(ad_chn, fd);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
        fclose(fd);
        fd = TD_NULL;
        goto adec_ao_err0;
    }

    printf("bind adec:%d to ao(%d,%d) ok \n", ad_chn, ao_dev, ao_chn);

    sleep(2); /* 2: sleep 2 seconds */

    ret = sample_comm_audio_destory_trd_file_adec(ad_chn);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
    }

adec_ao_err0:
    ret = sample_comm_audio_ao_unbind_adec(ao_dev, ao_chn, ad_chn);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
    }

    return;
}

/* function : file -> adec -> ao */
td_s32 sample_audio_adec_ao(const td_char *file_name1, const td_char *file_name2)
{
    td_s32 ret;
    td_u32 ao_chn_cnt;
    td_u32 adec_chn_cnt;
    ot_audio_dev ao_dev;
    ot_aio_attr aio_attr;
    const ot_ao_chn ao_chn = 0;
    const ot_adec_chn ad_chn = 0;

    sample_audio_adec_ao_init_param(&aio_attr, &ao_dev);

    adec_chn_cnt = aio_attr.chn_cnt >> ((td_u32)aio_attr.snd_mode);
    ret = sample_comm_audio_start_adec(adec_chn_cnt, g_payload_type);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
        goto adec_ao_err3;
    }

    ao_chn_cnt = aio_attr.chn_cnt;
    ret = sample_comm_audio_start_ao(ao_dev, ao_chn_cnt, &aio_attr, g_in_sample_rate, g_aio_resample);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
        goto adec_ao_err2;
    }

    ret = sample_comm_audio_cfg_acodec(&aio_attr);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
        goto adec_ao_err1;
    }

    sample_audio_adec_ao_inner(ao_dev, ao_chn, ad_chn, file_name1, file_name2);

adec_ao_err1:
    ret = sample_comm_audio_stop_ao(ao_dev, ao_chn_cnt, g_aio_resample);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
    }

adec_ao_err2:
    ret = sample_comm_audio_stop_adec(ad_chn);
    if (ret != TD_SUCCESS) {
        sample_dbg(ret);
    }

adec_ao_err3:
    return ret;
}