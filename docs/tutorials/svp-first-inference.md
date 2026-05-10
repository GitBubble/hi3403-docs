---
title: 在板上跑一个 AI 模型
description: 把模型转成 SVP 可执行格式，在 Hi3403 上推理
---

# 教程：在板上跑一个 AI 模型

**目标**：把一个公开的 ONNX 模型（YOLOv5n）转成 SVP 可执行的 `.om` 格式，
拷到 Hi3403V100 上推理一张图，看输出。

**用时**：约 45 分钟

!!! info "前提"

    本教程假设你已经在 PC 主机装好了 [ATC 工具](../multimedia/atc/tool/index.md)
    （Pegasus SDK 的一部分）。ATC 不在板子上跑，只在 PC 上做模型转换。
    板端运行环境用 [`hi3403-build`](../tools/hi3403-build.md) 产出的 Ubuntu
    镜像，里面 SVP 推理库（`libacl*.so`）已经装在 `/usr/lib/`。

**前置条件**：

- PC 主机：装好 ATC 与 Python 3.10+
- 板子：通过 [quickstart](../get-started/quickstart.md) 启动起来了
- 网络：PC ↔ 板子在同一局域网

## 整体流程

```mermaid
flowchart LR
    onnx[YOLOv5n.onnx<br>主机] --> ATC[ATC 转换<br>主机]
    ATC --> om[yolov5n.om<br>主机]
    om -.scp.-> board[拷到板子]
    board --> SVP[SVP 推理]
    SVP --> result[检测框输出]
```

## 步骤 1 — 在主机准备 ONNX 模型

``` bash
mkdir -p ~/yolo-pegasus && cd ~/yolo-pegasus

# 从 ultralytics 拉一个轻量级 yolov5n
wget https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5n.onnx

# 准备一张测试图
wget https://ultralytics.com/images/bus.jpg
```

## 步骤 2 — 用 ATC 转换为 .om

ATC 把 ONNX 转成 SVP 能执行的 `.om` 格式。**ATC 命令的精确参数随
SDK 版本变化** —— 下面是常见的 SS928V100 用法，请以
[ATC 工具使用指南](../multimedia/atc/tool/index.md) 为准：

``` bash
atc \
    --model=yolov5n.onnx \
    --framework=5 \
    --output=yolov5n \
    --input_shape="images:1,3,640,640" \
    --soc_version=SS928V100 \
    --log=info
```

参数说明：

| 参数 | 含义 |
|---|---|
| `--framework` | `1`=Caffe，`3`=TensorFlow，`5`=ONNX |
| `--input_shape` | 模型输入张量形状 |
| `--soc_version` | 目标芯片（部分 SDK 写 `Hi3403V100`，部分写 `SS928V100`）|

成功后会得到 `yolov5n.om`，约 8 MB。

!!! tip "ATC 跑得慢？"

    第一次跑会编译算子库，5–10 分钟正常。后续转换同结构的模型秒级。

## 步骤 3 — 拷到板子

``` bash
scp yolov5n.om bus.jpg hi@<板子IP>:~/
```

## 步骤 4 — 在板子上推理

SDK 在 `pegasus/platform/ss928v100_gcc/smp/a55_linux/mpp/sample/` 下面提供
若干 SVP / ACL 相关 sample（名字随 SDK 版本不同；常见 `nnie_sample`、
`acl_sample`、`svp_sample`）。把对应 sample 编出来，拷到板子上跑：

``` bash
ssh hi@<板子IP>
chmod +x sample_acl
./sample_acl ~/yolov5n.om ~/bus.jpg
```

期望输出形式（具体格式取决于你跑的 sample，以下示意）：

```
[INFO] Loading yolov5n.om ...
[INFO] Model loaded, input: 1x3x640x640 FP16
[INFO] Inference: 6.8 ms
[INFO] Detected 4 objects:
  - bus       conf=0.91  bbox=[12,234,810,720]
  - person    conf=0.86  bbox=[671,366,809,716]
  - person    conf=0.79  bbox=[222,406,344,861]
  - person    conf=0.75  bbox=[48,398,242,891]
```

## 步骤 5 — 提速：量化

FP16 的 yolov5n 在 SS928V100 上推理 ~7 ms。用
[AMCT](../multimedia/amct/index.md) 量化到 INT8 之后，能压到 ~3 ms：

``` bash
# 在主机上 —— 命令名按你装的 AMCT 版本可能是 amct_onnx 或 amct
amct_onnx calibration \
    --model=yolov5n.onnx \
    --save_path=yolov5n_int8.onnx \
    --input_shape="images:1,3,640,640" \
    --data_dir=./calibration_images/
```

然后再跑一遍 `atc` 把量化后的 ONNX 转成 `.om`。

## 步骤 6 — 自己写推理代码

调 SVP 的核心 API（基于 ACL 接口）：

``` c
#include "acl/acl.h"

int main(void) {
    aclrtContext ctx;
    aclrtStream stream;

    // 1. 初始化
    aclInit(NULL);
    aclrtSetDevice(0);
    aclrtCreateContext(&ctx, 0);
    aclrtCreateStream(&stream);

    // 2. 加载模型
    uint32_t model_id;
    aclmdlLoadFromFile("yolov5n.om", &model_id);

    // 3. 准备输入 / 输出 buffers
    aclmdlDataset *input  = aclmdlCreateDataset();
    aclmdlDataset *output = aclmdlCreateDataset();
    /* ... allocate buffers, copy image data ... */

    // 4. 推理
    aclmdlExecute(model_id, input, output);

    // 5. 后处理 bbox / NMS
    /* ... */

    // 6. 清理
    aclmdlUnload(model_id);
    aclrtDestroyStream(stream);
    aclrtDestroyContext(ctx);
    aclrtResetDevice(0);
    aclFinalize();
    return 0;
}
```

完整代码模板见 SDK 的 SVP / ACL sample 目录。
ACL 的完整 API 见 [SVP API 参考](../reference/api/svp/index.md)。

## 接下来

<div class="grid cards" markdown>

-   :material-tune-variant:{ .lg .middle } __量化提速__

    ---

    AMCT 把 FP32 模型压到 INT8。

    [:octicons-arrow-right-24: AMCT 量化](../multimedia/amct/index.md)

-   :material-chart-line:{ .lg .middle } __性能分析__

    ---

    Profiling 工具找瓶颈。

    [:octicons-arrow-right-24: Profiling 工具使用指南](../tools/profiling/index.md)

-   :material-bookshelf:{ .lg .middle } __SVP API__

    ---

    [:octicons-arrow-right-24: SVP API 参考](../reference/api/svp/index.md)

</div>
