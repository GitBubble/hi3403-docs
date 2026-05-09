---
title: 教程
description: 端到端的实战教程 —— 跟着做，每个 30–60 分钟内出结果
---

# 教程

跟着 Hi3403 文档走完了 quickstart？这里是几个端到端的实战教程，
覆盖最常见的开发任务。每个教程都有完整的代码、命令、预期输出，
跟着做大约 30–60 分钟出结果。

<div class="grid cards" markdown>

-   :material-camera-iris:{ .lg .middle } __采集 → 编码 → 推流__

    ---

    用 MIPI 摄像头抓帧，H.264 编码，通过 RTSP 推到局域网。
    *~45 分钟*

    [:octicons-arrow-right-24: 进入](capture-encode-stream.md)

-   :material-brain:{ .lg .middle } __在板上跑一个 AI 模型__

    ---

    把 ONNX 模型转成 SVP `.om`，板端推理，看输出。
    *~45 分钟*

    [:octicons-arrow-right-24: 进入](svp-first-inference.md)

-   :material-palette:{ .lg .middle } __调一个 ISP 颜色 bug__

    ---

    板子拍出来色温偏冷。打开 IQS（图像质量调试工具），改 AWB 参数，
    保存到 SYS_CONFIG。
    *~30 分钟*

    [:octicons-arrow-right-24: 进入](isp-color-tuning.md)

</div>

## 还想看什么？

这是初版教程系列。如果你写了好的端到端教程，欢迎
[提 PR](../community/contributing.md)。
我们正在补这些主题：

- 在 Hi3403 上跑 GStreamer
- 把 Hi3403 集成进 ROS 2
- 用 OpenHarmony 做相机应用
- 安全启动签名与烧录
- 多板 PCIE 级联组网
