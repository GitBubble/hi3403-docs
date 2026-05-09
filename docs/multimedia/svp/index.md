---
title: SVP 2.0 (NPU)
description: Hi3403V100 内置 NPU 的开发指南与 API 参考
---

# SVP 2.0 (NPU)

SVP（Smart Vision Processor）是 Hi3403V100 内置的 10.4 TOPS @ INT8 NPU，
负责跑深度学习模型。本节提供开发指南，API 参考请见 参考 章节。

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __开发指南__

    模型部署、运行时调用、性能优化。

    [:octicons-arrow-right-24: 进入](dev/index.md)

-   :material-bookshelf:{ .lg .middle } __API 参考__

    `ot_svp_*` 接口手册。

    [:octicons-arrow-right-24: 进入](../../reference/api/svp/index.md)

-   :material-swap-horizontal:{ .lg .middle } __ATC 模型转换__

    Caffe / PyTorch / ONNX → `.om` 全流程。

    [:octicons-arrow-right-24: 进入](../atc/index.md)

</div>
