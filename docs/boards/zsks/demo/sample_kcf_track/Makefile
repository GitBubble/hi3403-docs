# 编译所需的公共文件
include ../Makefile.param
SVP_COMMON_PATH := $(SDK_PATH)/mpp/sample/svp/common

# 编译后生成的可执行文件名
TARGET := main

TARGET_PATH := $(PWD)/out

# 编译此工程需要包含的头文件
CFLAGS += -I$(PWD)
CFLAGS += -I$(SVP_COMMON_PATH)
CFLAGS += -I$(SDK_PATH)/mpp/out/include/svp_npu

# 编译此工程需要依赖的.c或.cpp文件
SMP_SRCS += $(wildcard $(SVP_COMMON_PATH)/*.c)
SMP_SRCS += $(wildcard $(PWD)/*.c)

# 编译此工程需要包含的库和宏
CFLAGS += -O3 -g -Wall -DUSE_USB_CAMERA
CFLAGS += -fstack-protector-strong

# 编译工程所需的mk文件

include ../smp_linux_user_space.mak


