---
title: ATC model conversion
description: Convert Caffe / PyTorch / ONNX models to SVP-executable format
--- # ATC model conversion ATC (Ascend Tensor Compiler — HiSilicon's model compiler) converts
open-source-framework models into the `.om` format that the SVP NPU can
execute. This section covers tool usage, custom operators, and graph
optimization. <div class="grid cards" markdown> - :material-toolbox:{ .lg .middle } __Tool usage__ Common arguments and typical workflows for the `atc` CLI. [:octicons-arrow-right-24: Open](tool/index.md) - :material-graph:{ .lg .middle } __Compute graph__ The structure and optimizations of the ATC compute graph. [:octicons-arrow-right-24: Open](graph/index.md) - :material-puzzle-plus:{ .lg .middle } __Custom operators__ Implement and register custom operators on SVP so that ATC can compile your model end-to-end. [:octicons-arrow-right-24: Open](custom-op/index.md) </div>
