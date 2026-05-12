---
title: 术语表
description: Hi3403 平台中的缩写、专有名词与一句话解释
---

# 术语表

Hi3403 / Pegasus 文档里到处都是缩写。这个表给每个名词一句话解释 ——
为新接触这个平台的人做翻译。

## 芯片与子系统

`Hi3403V100` / `Hi3403V100`
:   同一颗芯片的两种叫法。Hi3403 是产品代号，Hi3403V100 是芯片代号，
    完全等价。配套有 Hi3519AV200（少一个 NPU 簇的精简版）。

`SoC`
:   System on Chip。把 CPU、NPU、ISP、编解码器、各种 IO 控制器集成
    到一颗芯片里。

`A55`
:   ARM Cortex-A55 处理器核心。Hi3403V100 有 4 颗 A55，运行 Linux 和
    用户空间程序。

`SVP`
:   Smart Vision Platform 2.0 —— Hi3403 的 NPU。跑 AI 模型推理。
    [参考](../multimedia/svp/index.md)

`ISP`
:   Image Signal Processor —— 图像信号处理器。把 sensor 输出的 RAW
    数据处理成可看的 YUV/RGB（去噪、白平衡、色彩、HDR、Gamma…）。
    [参考](../multimedia/isp/index.md)

`MPP`
:   Media Processing Platform —— 海思的多媒体处理软件框架。视频采集、
    编解码、图像处理、音频、显示输出全在 MPP 里。
    [参考](../multimedia/mpp/index.md)

`MMZ`
:   Media Memory Zone —— 媒体内存区。MPP 用的物理连续内存池，
    避免普通 Linux 内存的碎片问题。

`NMA`
:   Non-cacheable Memory Allocator —— 非缓存内存分配器，
    用于 DMA 传输的缓冲区。

## 多媒体子系统

`VI`
:   Video Input —— 视频输入。从 sensor / MIPI-CSI 收图。

`VO`
:   Video Output —— 视频输出。到 HDMI / MIPI-DSI / VGA。

`VPSS`
:   Video Process SubSystem —— 视频处理子系统。缩放、裁剪、
    色彩空间转换。

`VENC` / `VDEC`
:   Video Encoder / Decoder —— H.264 / H.265 / JPEG 编/解码器。

`AENC` / `ADEC` / `AI` / `AO`
:   音频编码 / 解码 / 输入 / 输出。

`AEC` / `ANS`
:   Acoustic Echo Cancellation / Acoustic Noise Suppression。

`TDE`
:   Two-Dimensional Engine —— 2D 图形硬件加速器。
    [参考](api/tde/index.md)

`GFBG`
:   Graphics FrameBuffer Group —— 图形帧缓冲管理。
    [参考](../multimedia/graphics/gfbg/index.md)

`GDC`
:   Geometric Distortion Correction —— 几何畸变矫正子系统。
    把鱼眼镜头的图拉直。

## AI / 计算机视觉

`ATC`
:   Ascend Tensor Compiler —— 模型转换器。把 Caffe / ONNX / PyTorch
    模型转成 SVP 可执行的 `.om` 文件。
    [参考](../multimedia/atc/index.md)

`AMCT`
:   Ascend Model Compression Tool —— 模型量化工具。FP32 → INT8 / INT16，
    模型变小、跑得快。
    [参考](../multimedia/amct/index.md)

`IVE`
:   Intelligent Video Engine —— 传统计算机视觉硬件加速器
    （直方图、Canny、形态学、光流……）。
    [参考](api/ive/index.md)

`IVS`
:   Intelligent Video System —— 视频结构化框架。

`DPU`
:   Depth Processing Unit —— 深度感知模块（双目视差等）。

`HNR`
:   Heterogeneous NR (Noise Reduction) —— 异构降噪。
    [参考](../multimedia/cv/hnr/index.md)

`DIS`
:   Digital Image Stabilization —— 数字图像防抖。
    [参考](../multimedia/dis/index.md)

`MotionFusion`
:   把运动信息（陀螺仪 / IMU）和图像信息融合，用于电子防抖与超分。
    [参考](../multimedia/motionfusion/index.md)

## 安全与加密

`KLAD`
:   Key Ladder —— 密钥派生硬件单元。
    [参考](api/klad/index.md)

`CIPHER`
:   通用加解密硬件加速器（AES、SM4、SHA、RSA…）。
    [参考](api/cipher/index.md)

`OTP`
:   One-Time Programmable memory —— 一次性可编程存储器，存放设备
    密钥、Boot 配置等。
    [参考](api/otp/index.md)

`TBBR`
:   Trusted Board Boot Requirements —— ARM 的可信启动规范。
    Hi3403 的安全启动基于 TBBR。

`TF-A` / `ATF`
:   Trusted Firmware-A —— ARM 的安全启动固件，运行在 EL3。
    Hi3403 用 v2.2。

## 系统启动

`U-Boot`
:   通用 Bootloader。Hi3403 用 v2020.01。
    [参考](../soc-linux/uboot/index.md)

`bl31`
:   ATF 的 Stage 3.1 —— 安全启动链路里运行在 EL3 的最后一站，
    然后跳到 U-Boot 或 Linux。

`DTB`
:   Device Tree Blob —— 设备树二进制文件。描述硬件给内核看。

`eMMC` / `SPI` / `NAND`
:   三种启动介质。eMMC 是最常用的板载 Flash；SPI 容量小但便宜；
    NAND 是工业控制场景。

## 工具与平台

`hi3403-build`
:   一键构建 Ubuntu 镜像的社区脚本。
    [参考](../tools/hi3403-build.md)

`BurnTool`
:   海思官方的图形烧录工具。
    [参考](../tools/burntool/index.md)

`MindCmd`
:   板端命令行调试工具，含 AI 一键推理。
    [参考](../tools/mindcmd/index.md)

`ToolPlatform`
:   海思可视化调试平台。
    [参考](../tools/toolplatform/index.md)

`SDK`
:   Software Development Kit —— Hi3403 的开发包，包含 MPP 库、
    内核驱动、sample 代码。分 GCC-GLIBC 和 CLANG-MUSL 两个变体。

## 别的常见缩写

`Hi3403V100` ↔ `Hi3403V100` —— 见上面"芯片与子系统"。

`Topeet` / `LubanCat` / `ebaina` / `rkh` / `zsks`
:   开发板 OEM。分别是迅为、野火、易百纳、润开鸿、中山旷视。
    [开发板对比](../get-started/board-picker.md)

---

发现术语没有？欢迎 [提 PR](../community/contributing.md) 补一行。
