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
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include "sdk_module_init.h"
#include "securec.h"
#include "sample_svp_npu_process.h"

int main(int argc, char *argv[])
{
    td_s32 ret;

#ifdef CONFIG_USER_SPACE
    SDK_init();
#endif

    sample_svp_npu_acl_v4l2_kcf();

#ifdef CONFIG_USER_SPACE
    SDK_exit();
#endif
    return 0;
}
