0LLVM ?= 0

ifeq ($(LLVM), 1)
    COMPILE_CHAIN := clang
else
    COMPILE_CHAIN := gcc
endif

# 编译所需的公共文件
include ../Makefile.param

OSD_PATH := $(PWD)/../../../opensource/osd/$(COMPILE_CHAIN)

# 编译后生成的可执行文件名
TARGET := main

TARGET_PATH := $(PWD)/out

# 编译此工程需要包含的头文件
CFLAGS += -I$(PWD)
CFLAGS += -I$(PWD)/common/
CFLAGS += -I$(OSD_PATH)/include/
CFLAGS += -I$(SDK_PATH)/mpp/sample/audio/adp/
CFLAGS += -I$(SDK_PATH)/mpp/out/include/svp_npu

# 编译此工程需要依赖的.c或.cpp文件
SMP_SRCS += $(wildcard $(PWD)/*.c)
SMP_SRCS += $(wildcard $(PWD)/common/*.c)
SMP_SRCS += $(SDK_PATH)/mpp/sample/audio/adp/audio_aac_adp.c
SMP_SRCS += $(SDK_PATH)/mpp/sample/audio/adp/audio_dl_adp.c

# 编译此工程需要包含的库和宏
CFLAGS += -O3 -g -Wall -DUSE_USB_CAMERA
CFLAGS += -fstack-protector-strong
MPI_LIBS += $(OSD_PATH)/lib/libxvp_osd.a
CFLAGS += -DOT_ACODEC_TYPE_INNER
CFLAGS += -DOT_ACODEC_TYPE_HDMI

# 编译工程所需的mk文件

include ../smp_linux_user_space.mak


