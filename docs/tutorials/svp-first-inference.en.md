---
title: Run an AI model on the board
description: Convert a model to SVP-executable format and run inference on Hi3403
---

# Tutorial: run an AI model on the board

**Goal**: convert a public ONNX model (YOLOv5n) to SVP-executable `.om`
format, copy it onto a Hi3403V100 board, run inference on a single
image, and inspect the output.

**Time**: ~45 minutes

!!! info "Prerequisites"

    This tutorial assumes you have the [ATC tool](../multimedia/atc/tool/index.md)
    installed on a PC host (it ships with the Pegasus SDK). ATC does not
    run on the board — it is a host-side model converter. The on-board
    runtime uses the [`hi3403-build`](../tools/hi3403-build.md) Ubuntu
    image, which already has the SVP runtime libraries (`libacl*.so`)
    installed under `/usr/lib/`.

**You'll need**:

- PC host: ATC + Python 3.10+
- Board: booted via [quickstart](../get-started/quickstart.md)
- Network: PC ↔ board on the same LAN

## High-level flow

```mermaid
flowchart LR
    onnx[YOLOv5n.onnx<br>host] --> ATC[ATC convert<br>host]
    ATC --> om[yolov5n.om<br>host]
    om -.scp.-> board[copy to board]
    board --> SVP[SVP inference]
    SVP --> result[detections]
```

## Step 1 — Prepare the ONNX model on the host

``` bash
mkdir -p ~/yolo-pegasus && cd ~/yolo-pegasus

# Pull a small yolov5n
wget https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5n.onnx

# Test image
wget https://ultralytics.com/images/bus.jpg
```

## Step 2 — Convert to .om via ATC

ATC turns the ONNX into the SVP-executable `.om` format. **Exact
arguments vary by SDK version** — the snippet below is a common
SS928V100 invocation; refer to the
[ATC user guide](../multimedia/atc/tool/index.md) for the authoritative
flags:

``` bash
atc \
    --model=yolov5n.onnx \
    --framework=5 \
    --output=yolov5n \
    --input_shape="images:1,3,640,640" \
    --soc_version=SS928V100 \
    --log=info
```

| Flag | Meaning |
|---|---|
| `--framework` | `1`=Caffe, `3`=TensorFlow, `5`=ONNX |
| `--input_shape` | Model input tensor shape |
| `--soc_version` | Target chip (some SDK versions take `Hi3403V100`, others `SS928V100`) |

You should now have `yolov5n.om` (~8 MB).

!!! tip "ATC running slow?"

    The first run compiles operator kernels — 5–10 minutes is normal.
    Subsequent conversions of similar models are seconds.

## Step 3 — Copy to the board

``` bash
scp yolov5n.om bus.jpg hi@<board-IP>:~/
```

## Step 4 — Run inference on the board

The SDK ships several SVP / ACL samples under
`pegasus/platform/ss928v100_gcc/smp/a55_linux/mpp/sample/` — exact names
vary by SDK version (commonly `nnie_sample`, `acl_sample`,
`svp_sample`). Cross-build the relevant sample, copy its binary to the
board, and feed it your `.om`:

``` bash
ssh hi@<board-IP>
chmod +x sample_acl
./sample_acl ~/yolov5n.om ~/bus.jpg
```

Expected output (the exact format depends on which sample you ran):

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

## Step 5 — Speed up: quantize

YOLOv5n at FP16 lands around 7 ms on SS928V100. Quantize to INT8 with
[AMCT](../multimedia/amct/index.md) and the same model drops to ~3 ms:

``` bash
# On the host — command name is amct_onnx or amct depending on version
amct_onnx calibration \
    --model=yolov5n.onnx \
    --save_path=yolov5n_int8.onnx \
    --input_shape="images:1,3,640,640" \
    --data_dir=./calibration_images/
```

Then re-run `atc` on the quantized ONNX to produce a new `.om`.

## Step 6 — Roll your own inference code

The SVP runtime exposes the ACL API:

``` c
#include "acl/acl.h"

int main(void) {
    aclrtContext ctx;
    aclrtStream stream;

    // 1. Init
    aclInit(NULL);
    aclrtSetDevice(0);
    aclrtCreateContext(&ctx, 0);
    aclrtCreateStream(&stream);

    // 2. Load model
    uint32_t model_id;
    aclmdlLoadFromFile("yolov5n.om", &model_id);

    // 3. Prepare input / output buffers
    aclmdlDataset *input  = aclmdlCreateDataset();
    aclmdlDataset *output = aclmdlCreateDataset();
    /* ... allocate buffers, copy image data ... */

    // 4. Inference
    aclmdlExecute(model_id, input, output);

    // 5. Post-process: bbox / NMS
    /* ... */

    // 6. Cleanup
    aclmdlUnload(model_id);
    aclrtDestroyStream(stream);
    aclrtDestroyContext(ctx);
    aclrtResetDevice(0);
    aclFinalize();
    return 0;
}
```

Find a complete buildable starting point in the SDK's SVP / ACL sample
directory. Full ACL API: [SVP API reference](../reference/api/svp/index.md).

## Next

<div class="grid cards" markdown>

-   :material-tune-variant:{ .lg .middle } __Quantize for speed__

    ---

    AMCT compresses FP32 to INT8.

    [:octicons-arrow-right-24: AMCT quantization](../multimedia/amct/index.md)

-   :material-chart-line:{ .lg .middle } __Profile to find bottlenecks__

    ---

    [:octicons-arrow-right-24: Profiling tool](../tools/profiling/index.md)

-   :material-bookshelf:{ .lg .middle } __SVP API reference__

    ---

    [:octicons-arrow-right-24: SVP API](../reference/api/svp/index.md)

</div>
