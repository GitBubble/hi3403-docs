# 编译所需的公共文件
include ../Makefile.param

# 编译后生成的可执行文件名
TARGET := main

TARGET_PATH := $(PWD)/out

# 编译此工程需要包含的头文件
CFLAGS += -I$(SDK_PATH)/mpp/out/include

# 编译此工程需要依赖的.c或.cpp文件
SMP_SRCS += $(wildcard $(PWD)/*.c)

# 编译此工程需要包含的库和宏
ifeq ($(CONFIG_OT_ISP_HNR_SUPPORT), y)
CFLAGS += -DSAMPLE_HNR_SUPPORT
MPI_LIBS += $(REL_LIB)/libss_pqp.a
MPI_LIBS += $(REL_LIB)/libss_hnr.a
endif

# 编译工程所需的mk文件

include ../smp_linux_user_space.mak
