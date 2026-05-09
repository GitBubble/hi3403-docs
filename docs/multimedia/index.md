---
title: 多媒体与 AI
description: MPP、ISP、编解码、音频、SVP NPU、ATC、IVE/IVS
---

# 多媒体与 AI

Hi3403 真正的核心能力 —— 媒体处理与 AI 推理。本节涵盖 MPP V5.0
的所有子系统、ISP 图像处理与调优、编解码、SVP（NPU）的模型转换与推理、
以及计算机视觉中间件 IVE/IVS/DPU/HNR。

## 媒体处理 (MPP)

<div class="grid cards" markdown>

-   :material-video-input-component:{ .lg .middle } __MPP 概览__

    ---

    MPP V5.0 的整体架构、子系统划分、数据流。

    [:octicons-arrow-right-24: 进入](mpp/index.md)

-   :material-camera-control:{ .lg .middle } __ISP & 图像调优__

    ---

    Image Signal Processor：从 RAW 到 YUV 的全流程，以及调优指南。

    [:octicons-arrow-right-24: 进入](isp/index.md)

-   :material-television:{ .lg .middle } __HDMI__

    ---

    HDMI 输出的开发参考。

    [:octicons-arrow-right-24: 进入](hdmi/index.md)

-   :material-shape:{ .lg .middle } __图形 / TDE / GFBG__

    ---

    GPU、TDE 二维图形加速、GFBG 帧缓冲。

    [:octicons-arrow-right-24: 进入](graphics/index.md)

-   :material-image-multiple:{ .lg .middle } __开机画面 (Splash)__

    ---

    开机 logo 的制作与显示流程。

    [:octicons-arrow-right-24: 进入](splash/index.md)

</div>

## AI 与计算机视觉

<div class="grid cards" markdown>

-   :material-brain:{ .lg .middle } __SVP 2.0 (NPU)__

    ---

    Hi3403 内置的 NPU。开发指南 + API 参考。

    [:octicons-arrow-right-24: 进入](svp/index.md)

-   :material-swap-horizontal:{ .lg .middle } __ATC 模型转换__

    ---

    把 Caffe / PyTorch / ONNX 模型转换为 SVP 可执行的格式。

    [:octicons-arrow-right-24: 进入](atc/index.md)

-   :material-chart-bell-curve:{ .lg .middle } __AMCT 量化__

    ---

    模型量化工具：把 FP32 模型转成 INT8/INT16，提升吞吐。

    [:octicons-arrow-right-24: 进入](amct/index.md)

-   :material-eye:{ .lg .middle } __IVE / IVS / DPU / HNR__

    ---

    传统 CV 加速器：图像处理、视频结构化、深度感知、降噪。

    [:octicons-arrow-right-24: 进入](cv/index.md)

-   :material-motion-sensor:{ .lg .middle } __MotionFusion__

    ---

    运动信息与图像信息融合的开发参考。

    [:octicons-arrow-right-24: 进入](motionfusion/index.md)

-   :material-shake-vertical:{ .lg .middle } __DIS 防抖__

    ---

    数字图像稳定（防抖）模块的调试指南。

    [:octicons-arrow-right-24: 进入](dis/index.md)

-   :material-blur:{ .lg .middle } __3DNR 降噪__

    ---

    三维降噪模块的开发参考与调优。

    [:octicons-arrow-right-24: 进入](3dnr/index.md)

-   :material-contrast-circle:{ .lg .middle } __黑白彩色双路融合__

    ---

    用 mono+color 双路传感器做高动态成像。

    [:octicons-arrow-right-24: 进入](dual-fusion/index.md)

-   :material-camera-burst:{ .lg .middle } __抓拍__

    ---

    高速抓拍的使用指南。

    [:octicons-arrow-right-24: 进入](snapshot/index.md)

</div>

<div class="related" markdown>

## 相关资源

<div class="grid cards" markdown>

-   :material-bookshelf:{ .lg .middle } __API 参考__

    ---

    所有 MPP / SVP / IVE / IVS / TDE / GFBG 的接口手册。

    [:octicons-arrow-right-24: 进入](../reference/api/index.md)

-   :material-help-circle:{ .lg .middle } __MPP FAQ__

    ---

    MPP V5.0 常见问题答疑。

    [:octicons-arrow-right-24: 进入](../reference/faq/mpp/index.md)

</div>

</div>
