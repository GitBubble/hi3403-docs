---
title: 在板上跑一个 AI 模型
description: 把 ONNX 模型转成 SVP 可执行格式，在 Hi3403 上推理
---

# 教程：在板上跑一个 AI 模型

**目标**：把一个公开的 ONNX 模型（YOLOv5n）转成 SVP 可执行的 `.om` 格式，
拷到 Hi3403V100 上推理一张图，看输出。

**用时**：约 45 分钟

**前置条件**：

- 已经按 [quickstart](../get-started/quickstart.md) 启动了 Hi3403
- 主机上装好了 [ATC 工具](../multimedia/atc/tool/index.md)（PC 端工具）
- 网络通畅（要下载 YOLOv5n.onnx）

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

ATC 把 ONNX 转成 SVP 能执行的 `.om` 格式：

``` bash
atc \
    --model=yolov5n.onnx \
    --framework=5 \
    --output=yolov5n \
    --input_shape="images:1,3,640,640" \
    --soc_version=Hi3403V100 \
    --log=info
```

参数说明：

| 参数 | 含义 |
|---|---|
| `--framework=5` | 5 = ONNX（1=Caffe，3=TensorFlow，5=ONNX） |
| `--input_shape` | 模型输入张量形状 |
| `--soc_version` | 目标芯片 |

期望输出：

```
ATC start working now, please wait for a moment.
ATC run success, welcome to the next use.
```

成功后会得到 `yolov5n.om`，约 8 MB。

!!! tip "ATC 跑得慢？"

    第一次跑会编译算子库，5–10 分钟很正常。后续转换同结构的模型秒级。

## 步骤 3 — 拷到板子

``` bash
scp yolov5n.om bus.jpg hi@192.168.1.42:~/
```

## 步骤 4 — 在板子上推理

SSH 到板子：

``` bash
ssh hi@192.168.1.42
```

用 SDK 自带的 `sample_svp` 推理：

``` bash
cd /opt/pegasus/sample/svp
./sample_svp infer ~/yolov5n.om ~/bus.jpg
```

期望输出：

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

FP16 的 yolov5n 推理 6.8 ms。用 [AMCT](../multimedia/amct/index.md) 量化到
INT8 之后，能压到 ~3 ms：

``` bash
# 在主机上
amct_onnx calibration \
    --model=yolov5n.onnx \
    --save_path=yolov5n_int8.onnx \
    --input_shape="images:1,3,640,640" \
    --data_dir=./calibration_images/ \
    --calibration_config=config.json
```

然后再跑一遍 `atc` 把量化后的 ONNX 转 `.om`。

## 步骤 6 — 写自己的推理代码

调 SVP 的核心 API：

``` c
#include "acl/acl.h"

int main(void) {
    // 1. 初始化
    aclInit(NULL);
    aclrtSetDevice(0);
    aclrtCreateContext(&context, 0);
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

    // 5. 取出结果
    /* ... post-process bbox / NMS ... */

    // 6. 清理
    aclmdlUnload(model_id);
    aclrtDestroyStream(stream);
    aclrtDestroyContext(context);
    aclrtResetDevice(0);
    aclFinalize();
    return 0;
}
```

完整代码见 SDK 的 `sample/svp/sample_svp_yolo.c`。

## 把 AI 接到视频流

下一步：把这个推理接到 VENC 之前，对每帧检测物体并画框。

→ 见 [采集 → 编码 → 推流](capture-encode-stream.md)

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
