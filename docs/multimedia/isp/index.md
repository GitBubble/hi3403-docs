---
title: ISP 图像信号处理
description: ISP 调优、传感器适配、颜色管理、IAE 迁移与开发参考
---

# ISP 图像信号处理

ISP（Image Signal Processor）负责把传感器吐出的 RAW 数据加工成可用的
YUV 图像。本节分为 调优、传感器适配、颜色管理、IAE 迁移、开发参考
五个部分。

<div class="grid cards" markdown>

-   :material-tune-vertical:{ .lg .middle } __调优 (Tuning)__

    ISP 整体调优流程与工具链。

    [:octicons-arrow-right-24: 进入](tuning/index.md)

-   :material-camera-iris:{ .lg .middle } __传感器适配 (Sensor)__

    驱动新传感器、接入到 ISP pipeline。

    [:octicons-arrow-right-24: 进入](sensor/index.md)

-   :material-palette:{ .lg .middle } __颜色管理 (Color)__

    AWB、CCM、Gamma 等颜色相关模块。

    [:octicons-arrow-right-24: 进入](color/index.md)

-   :material-swap-horizontal:{ .lg .middle } __IAE 迁移__

    把上一代 IAE 的调参/算法迁移到新 ISP。

    [:octicons-arrow-right-24: 进入](iae-migration/index.md)

-   :material-book-open-variant:{ .lg .middle } __开发参考__

    ISP 开发参考手册章节合集。

    [:octicons-arrow-right-24: 进入](dev-ref/isp-开发参考-1-2.md)

</div>
