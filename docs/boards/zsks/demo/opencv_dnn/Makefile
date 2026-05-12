LLVM ?= 0

ifeq ($(LLVM), 1)
    COMPILE_CHAIN := clang
else
    COMPILE_CHAIN := gcc
endif

# 编译所需的公共文件
include ../Makefile.param
OPENCV_PATH := $(PWD)/../../../opensource/opencv/$(COMPILE_CHAIN)

# 编译后生成的可执行文件名
TARGET := main

TARGET_PATH := $(PWD)/out

# 编译此工程需要包含的头文件
CFLAGS += -I$(PWD)
CFLAGS += -Wno-psabi -I$(OPENCV_PATH)/include/opencv4

# 编译此工程需要依赖的.c或.cpp文件
SMP_SRCS += $(wildcard $(PWD)/*.c)

# 编译此工程需要依赖的.cpp文件
CXX_SRCS += $(PWD)/main.cpp

# 编译此工程需要包含的库和宏
CFLAGS += -O3 -g -Wall -DUSE_USB_CAMERA
CFLAGS += -fstack-protector-strong 
MPI_LIBS += -L$(OPENCV_PATH)/lib
MPI_LIBS += -lopencv_world

# 编译工程所需的mk文件

include ../smp_linux_user_space.mak
