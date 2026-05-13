---
description: MPP, ISP, codec, audio, SVP NPU, ATC, IVE/IVS
title: Multimedia & AI
---

# Multimedia & AI

The real core capabilities of Hi3403 - media processing and AI reasoning. This section covers MPP V5.0
All subsystems, ISP image processing and tuning, encoding and decoding, SVP (NPU) model conversion and inference,
and computer vision middleware IVE/IVS/DPU/HNR.

## Media Processing (MPP)

<div class="grid cards" markdown>

-   :material-video-input-component:{ .lg .middle } __MPP Overview__

    ---

    The overall architecture, subsystem division, and data flow of MPP V5.0.

    [:octicons-arrow-right-24: Enter](mpp/index.md)

-   :material-camera-control:{ .lg .middle } __ISP & Image Tuning__

    ---

    Image Signal Processor: RAW to YUV workflow, plus tuning guide.

    [:octicons-arrow-right-24: Enter](isp/index.md)

-   :material-television:{ .lg .middle } __HDMI__

    ---

    Development reference for HDMI output.

    [:octicons-arrow-right-24: Enter](hdmi/index.md)

-   :material-shape:{ .lg .middle } __shape/TDE/GFBG__

    ---

    GPU, TDE 2D graphics acceleration, GFBG frame buffer.

    [:octicons-arrow-right-24: Enter](graphics/index.md)

-   :material-image-multiple:{ .lg .middle } __Splash__

    ---

    The process of making and displaying the boot logo.

    [:octicons-arrow-right-24: Enter](splash/index.md)

</div>

## AI and computer vision

<div class="grid cards" markdown>

-   :material-brain:{ .lg .middle } __SVP 2.0 (NPU)__

    ---

    Hi3403 built-in NPU. Development Guide + API Reference.

    [:octicons-arrow-right-24: Enter](svp/index.md)

-   :material-swap-horizontal:{ .lg .middle } __ATC model conversion__

    ---

    Convert Caffe / PyTorch / ONNX models to SVP executable format.

    [:octicons-arrow-right-24: Enter](atc/index.md)

-   :material-chart-bell-curve:{ .lg .middle } __AMCT quantization__

    ---

    Model quantization tool: Convert FP32 models to INT8/INT16 to improve throughput.

    [:octicons-arrow-right-24: Enter](amct/index.md)

-   :material-eye:{ .lg .middle } __IVE / IVS / DPU / HNR__

    ---

    Traditional CV accelerator: image processing, video structuring, depth perception, noise reduction.

    [:octicons-arrow-right-24: Enter](cv/index.md)

-   :material-motion-sensor:{ .lg .middle } __MotionFusion__

    ---

    Development reference for fusion of motion information and image information.

    [:octicons-arrow-right-24: Enter](motionfusion/index.md)

-   :material-shake-vertical:{ .lg .middle } __DIS anti-shake__

    ---

    Commissioning guide for the Digital Image Stabilization (anti-shake) module.

    [:octicons-arrow-right-24: Enter](dis/index.md)

-   :material-blur:{ .lg .middle } __3DNR Noise Reduction__

    ---

    Development reference and optimization of 3D noise reduction module.

    [:octicons-arrow-right-24: Enter](3dnr/index.md)

-   :material-contrast-circle:{ .lg .middle } __Mono + Color Dual-Sensor Fusion__

    ---

    Use mono+color dual-channel sensor for high dynamic imaging.

    [:octicons-arrow-right-24: Enter](dual-fusion/index.md)

-   :material-camera-burst:{ .lg .middle } __capture__

    ---

    User guide for high-speed capture.

    [:octicons-arrow-right-24: Enter](snapshot/index.md)

</div>

<div class="related" markdown>

## Related resources

<div class="grid cards" markdown>

-   :material-bookshelf:{ .lg .middle } __API Reference__

    ---

    Interface manual for all MPP/SVP/IVE/IVS/TDE/GFBG.

    [:octicons-arrow-right-24: Enter](../reference/api/index.md)

-   :material-help-circle:{ .lg .middle } __MPP FAQ__

    ---

    MPP V5.0 FAQ.

    [:octicons-arrow-right-24: Enter](../reference/faq/mpp/index.md)

</div>

</div>