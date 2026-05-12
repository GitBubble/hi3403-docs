---
title: "Foreword — DPU 2.0 tool guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/DPU2.0 工具使用指南/DPU2.0 工具使用指南.md
---

# Foreword

**Overview**

This document is written for engineers using the DPU for binocular
stereo-vision development. It walks through the tooling required to
generate the inputs the DPU needs.

**Product version**

| Product | Version |
|---|---|
| Hi3403V100 | V100 |
| Hi3519AV200 | V100 |

**Audience**

Primarily aimed at:

- Technical-support engineers
- Software-development engineers

**Change history**

| Doc version | Release date | Description |
|---|---|---|
| 04 | 2025-08-29 | Aligned with the v1.1 beta3 release. |
| 03 | 2024-12-30 | Updated to match the v1.1 beta2 release. |
| 02 | 2024-09-30 | Tracked the changes shipped with v1.1 beta1. |
| 01 | 2024-06-30 | First release. |

**Symbol conventions**

| Symbol | Meaning |
|---|---|
| **DANGER** | Hazard with a high level of risk; if not avoided, will result in death or serious injury. |
| **WARNING** | Hazard with a medium level of risk; if not avoided, could result in death or serious injury. |
| **CAUTION** | Hazard with a low level of risk; if not avoided, could result in minor or moderate injury. |
| **NOTICE** | Potentially hazardous situation; if not avoided, could damage equipment, lose data, degrade performance, or yield unanticipated results. |
| **NOTE** | Important information, best practices, and tips not related to personal injury. |

## What is DPU?

**DPU** (Depth Processing Unit) is the binocular stereo-vision
hardware accelerator on Hi3403V100. It computes per-pixel disparity
from two synchronised cameras (a "stereo rig") in real time, which can
then be turned into a depth / distance map.

## Tools provided

The DPU 2.0 tool suite covers the offline preparation steps:

- **Camera calibration** — intrinsic + extrinsic parameters of each camera.
- **Stereo rectification** — derive the rectification map from calibration data.
- **Disparity-tuning** — interactively adjust DPU parameters with live preview.
- **LUT generation** — compress the rectification + tuning data into the
  look-up tables the DPU consumes at runtime.

The end-to-end workflow takes you from a pair of raw stereo videos
through to a `.bin` file the on-board DPU loads.

## Workflow at a glance

```mermaid
flowchart LR
    cap[Capture<br>checkerboard pairs] --> calib[Camera calibration]
    calib --> rect[Stereo rectification]
    rect --> tune[Disparity tuning<br>preview]
    tune --> lut[LUT generation]
    lut --> board[Load on board → DPU runtime]
```

## Where to go next

The full tool walkthrough — installation, capturing calibration
patterns, parameter ranges, troubleshooting — lives in the rest of the
upstream guide. The Chinese page renders today via the i18n fallback
(switch the language toggle to read it directly); a fully translated
English version is on the docs roadmap.

For the runtime side (how to load the LUT and call the DPU APIs from
your application code), see the [MotionFusion](../../motionfusion/index.md)
chapter and the
[OpenHarmony / Linux peripheral interface](../../../soc-linux/peripherals/index.md).
