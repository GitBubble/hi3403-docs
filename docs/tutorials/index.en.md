---
description: End-to-end practical tutorials - follow along and get results in 30–60
  minutes each
title: Tutorials
---

# Tutorials

Finished following the Hi3403 document quickstart? Here are several end-to-end practical tutorials,
Covers the most common development tasks. Each tutorial has complete code, commands, expected output,
Follow up and it will take about 30–60 minutes for results.

<div class="grid cards" markdown>

-   :material-camera-iris:{ .lg .middle } __Collection → Encoding → Streaming__

    ---

    Capture frames with MIPI camera, encode in H.264, and push to LAN via RTSP.
    *~45 minutes*

    [:octicons-arrow-right-24: Enter](capture-encode-stream.md)

-   :material-brain:{ .lg .middle } __Run an AI model on the board__

    ---

    Convert the ONNX model to SVP `.om`, perform board-side inference and see the output.
    *~45 minutes*

    [:octicons-arrow-right-24: Enter](svp-first-inference.md)

-   :material-palette:{ .lg .middle } __Adjust an ISP color bug__

    ---

    The color temperature when photographed with the board is rather cold. Open IQS (Image Quality Debugging Tool) and change the AWB parameters.
    Save to SYS_CONFIG.
    *~30 minutes*

    [:octicons-arrow-right-24: Enter](isp-color-tuning.md)

</div>

## What else do you want to see?

This is the first edition of the tutorial series. If you write good end-to-end tutorials, welcome
[Raise a PR](../community/contributing.md)。
We are working on these topics:

- Running GStreamer on Hi3403
- Integrate Hi3403 into ROS 2
- Make a camera application with OpenHarmony
- Secure boot signing and burning
- Multi-board PCIE cascade networking