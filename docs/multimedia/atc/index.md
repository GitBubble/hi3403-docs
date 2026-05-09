---
title: ATC 模型转换
description: 把 Caffe / PyTorch / ONNX 模型转换为 SVP 可执行格式
---

# ATC 模型转换

ATC（Ascend Tensor Compiler / 华为模型编译器）把开源框架的模型转换成
SVP NPU 可执行的 `.om` 格式。本节涵盖工具用法、自定义算子、计算图优化。

<div class="grid cards" markdown>

-   :material-toolbox:{ .lg .middle } __工具用法__

    `atc` 命令行工具的常用参数与典型工作流。

    [:octicons-arrow-right-24: 进入](tool/index.md)

-   :material-graph:{ .lg .middle } __计算图__

    ATC 计算图的结构与优化。

    [:octicons-arrow-right-24: 进入](graph/index.md)

-   :material-puzzle-plus:{ .lg .middle } __自定义算子__

    SVP 上实现并注册自定义算子，让 ATC 能编译你的模型。

    [:octicons-arrow-right-24: 进入](custom-op/index.md)

</div>
