---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/抓拍使用指南/抓拍 使用指南.md
---

# Preface
**Product Version<a name="section2422mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table2425mcpsimp"></a>
<table><thead align="left"><tr id="row2430mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p2432mcpsimp"><a name="p2432mcpsimp"></a><a name="p2432mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p2434mcpsimp"><a name="p2434mcpsimp"></a><a name="p2434mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row2436mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p2438mcpsimp"><a name="p2438mcpsimp"></a><a name="p2438mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p2440mcpsimp"><a name="p2440mcpsimp"></a><a name="p2440mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row22121948133617"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p368135114363"><a name="p368135114363"></a><a name="p368135114363"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p16681151103616"><a name="p16681151103616"></a><a name="p16681151103616"></a>V100</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **Note:**
>This document uses Hi3403V100 as an example. Unless otherwise specified, Hi3519AV200 content is consistent with Hi3403V100.

**Revision History<a name="section2441mcpsimp"></a>**

The revision history records the descriptions of each document update. The latest version of the document contains updates from all previous document versions.

<a name="table126443203200"></a>
<table><thead align="left"><tr id="row264516207203"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p><strong>Doc Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p><strong>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p><strong>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p>The 1st temporary version release.</p>
</td>
</tr>
</tbody>
</table>

# Consumer Snapshot Solution Usage Guide
## Overview<a name="ZH-CN_TOPIC_0000002441723221"></a>

The consumer snapshot solution is mainly designed for the camera function in consumer electronic products. It supports Normal and PRO capture modes, allowing single or multiple photos with different exposure times. The consumer snapshot solution also supports HDR, SFNR, MFNR, and DE post-processing algorithms.

The snapshot data path is divided into single-pipe and dual-pipe modes. Each pipe can be online or offline, and each data path is suitable for different scenarios.

## Important Concepts<a name="ZH-CN_TOPIC_0000002441683353"></a>

-   Single-pipe mode: Capture and preview use the same ISP path.
-   Dual-pipe mode: Capture and preview use different ISP paths.
-   PRO (Professional) mode: In professional mode, the ISP controls sensor exposure to capture multiple images with adjustable exposure time and gain. This can be used for HDR multi-exposure compositing or capturing images with fixed exposure times.
-   ZSL (Zero Shutter Lag): Zero shutter lag capture, reducing delay caused by shutter latency, capturing the image at the moment the capture is triggered.

## Snapshot Data Paths<a name="ZH-CN_TOPIC_0000002408124058"></a>

VI pipe working modes are divided into offline mode and online mode. The snapshot data path is built on VI, so it also has these two modes.

In capture scenarios, video preview and snapshot resolutions are usually different. Also, ISP processing for snapshots needs optimization for skin tones, which differs from the video preview path. Hence, the snapshot data path is divided into single-pipe and dual-pipe modes.

Consumer electronic products also have ZSL mode capture for special scenarios.

>![](public_sys-resources/icon-notice.gif) **Caution:**
>The online/offline relationship between VI and VPSS only affects the position of the snapshot YUV output, not the snapshot control flow. Therefore, references to online/offline below refer to whether the snapshot VI pipe is online or offline.

In summary, there are many kinds of snapshot data paths. Each is suitable for different scenarios. We recommend customers adopt the dual-pipe offline mode, which offers optimal power consumption control and shorter capture times.

### Dual-Pipe Offline Mode Capture<a name="ZH-CN_TOPIC_0000002441683357"></a>

In dual-pipe offline mode, data from a single sensor is bound to two different pipes after VI Dev timing parsing. The upper pipe handles video preview and recording, while the lower pipe handles capture. Both are offline.

Preview/recording resolutions are typically smaller, so Bayer Scale is applied to reduce processing resolution and power consumption.

Capture resolutions are typically larger. Users are not always capturing, so the lower pipe is started only when needed.

Sensor exposure is controlled by the upper video pipe's ISP.

User settings for capture-related attributes and the trigger capture interface use the lower pipe number. Internal data synchronization is handled by VI and ISP drivers.

This data path supports NORMAL and PRO mode capture. PRO mode controls sensor exposure for long/short shots only after calling ss_mpi_snap_trigger_pipe.

### Single-Pipe Offline Mode Capture

Preview and capture share one pipe. Only when switching to capture mode are sensor and VI switched to the larger capture resolution.

### Single-Pipe Online Mode Capture

Similar to single-pipe offline, but the data path is online.

> Note: The Hi3403V100 VI module currently supports only 1 online pipe. If there are multiple sensor inputs, all sensors must be processed offline.

### ZSL Mode Capture

Same data path as dual-pipe offline, but VI driver internally caches a RAW data queue. After calling ss_mpi_snap_enable_pipe, VI starts caching RAW data. Calling ss_mpi_snap_trigger_pipe selects the ZSL capture frame.

ZSL mode only supports NORMAL mode photos.

## Functional Description

### Frame Rate Control During Burst Capture

Frame rate control during burst capture is implemented via the frame rate control in ot_vi_pipe_attr, set through ss_mpi_vi_create_pipe or ss_mpi_vi_set_pipe_attr.

## API Reference

The module provides the following MPI:

-   ss_mpi_snap_set_pipe_attr: Sets capture attributes.
-   ss_mpi_snap_get_pipe_attr: Gets capture attributes.
-   ss_mpi_snap_enable_pipe: Enables the capture pipe.
-   ss_mpi_snap_disable_pipe: Stops the capture pipe.
-   ss_mpi_snap_trigger_pipe: Triggers capture.

### ss_mpi_snap_set_pipe_attr

Sets capture attributes. Parameters: vi_pipe (VI pipe number), snap_attr (capture parameter attribute structure pointer). Return 0 for success, non-zero for error.

Requirements: ot_common_snap.h, ss_mpi_snap.h, libss_snap.a.

Notes: PIPE must be created. Capture parameters must be valid. WDR mode does not support capture.

### ss_mpi_snap_get_pipe_attr

Gets capture attributes.

### ss_mpi_snap_enable_pipe

Enables the capture pipe.

### ss_mpi_snap_disable_pipe

Stops the capture pipe or interrupts an ongoing capture data stream.

### ss_mpi_snap_trigger_pipe

Triggers capture.

## Data Types

Snapshot-related data types: ot_snap_attr (capture parameter structure), ot_snap_type (NORM/PRO enum), ot_snap_norm_attr (Normal parameters: frame_cnt, repeat_send_times, zsl_en, frame_depth, rollback_ms, interval), ot_snap_pro_attr (PRO parameters: frame_cnt, repeat_send_times, pro_param), ot_snap_pro_param (op_mode, auto_param, manual_param), ot_snap_pro_auto_param (exp_step), ot_snap_pro_manual_param (exp_time, sys_gain).

## Error Codes

SNAP API error codes include: OT_ERR_SNAP_INVALID_PIPE_ID (0xa0538002), OT_ERR_SNAP_ILLEGAL_PARAM (0xa0538007), OT_ERR_SNAP_NULL_PTR (0xa053800a), OT_ERR_SNAP_NOT_SUPPORT (0xa053800c), OT_ERR_SNAP_NOT_PERM (0xa053800d), OT_ERR_SNAP_NO_MEM (0xa0538014), OT_ERR_SNAP_NOT_READY (0xa0538018).

# Post-Processing Algorithms for Capture
## Overview

PHOTO represents post-processing algorithms in the consumer capture solution, including HDR, MFNR, SFNR, and DE.

## Important Concepts

-   HDR (High Dynamic Range): Improves dynamic range by compositing PRO mode multi-exposure images.
-   SFNR (Single Frame Noise Reduction): Single frame denoising.
-   MFNR (Multi-Frame Noise Reduction): Multi-frame denoising.
-   DE (Detail Enhancement): Compensates for detail loss from BNR processing.

## Functional Description

PHOTO module operation depends on DSP resources. The PHOTO library is compiled into the DSP0 image by default. Ensure ss_mpi_svp_dsp_load_bin has loaded the DSP0 image before calling PHOTO interfaces.

-   HDR currently supports 3-to-1 compositing.
-   HDR supports special optimization for face regions.
-   MFNR currently supports 4-to-1 compositing.
-   DE requires BNR RAW data.
-   Input/output frame data Stride must be 128-byte aligned; pixel width and height must be multiples of 8.
-   Input YUV supports NV21 non-compressed format only.
-   PHOTO algorithms run on DSP with 32-bit address bus, limited to 4GB address space.

## API Reference

-   ss_mpi_photo_alg_init: Initializes a PHOTO algorithm.
-   ss_mpi_photo_alg_deinit: Deinitializes a PHOTO algorithm.
-   ss_mpi_photo_alg_process: Starts processing for a PHOTO algorithm (blocking).
-   ss_mpi_photo_set_alg_coef: Sets image effect coefficients.
-   ss_mpi_photo_get_alg_coef: Gets image effect coefficients.

### ss_mpi_photo_alg_init

Initializes a PHOTO algorithm. Requires DSP bin loaded and MMZ-allocated public memory.

### ss_mpi_photo_alg_deinit

Deinitializes a PHOTO algorithm.

### ss_mpi_photo_alg_process

Starts PHOTO algorithm processing. Blocking interface. Multi-frame compositing requires multiple calls.

### ss_mpi_photo_set_alg_coef / ss_mpi_photo_get_alg_coef

Set/get algorithm image effect coefficients.

## Data Types

PHOTO algorithm types: OT_PHOTO_ALG_TYPE_HDR, OT_PHOTO_ALG_TYPE_SFNR, OT_PHOTO_ALG_TYPE_MFNR, OT_PHOTO_ALG_TYPE_DE.

Structures: ot_photo_alg_init, ot_photo_alg_attr, ot_photo_hdr_attr, ot_photo_sfnr_attr, ot_photo_mfnr_attr, ot_photo_de_attr, ot_photo_face_info, ot_photo_alg_coef, ot_photo_hdr_coef, ot_photo_image_fusion_param, ot_photo_dark_motion_detection_param, ot_photo_sfnr_coef, ot_photo_mfnr_coef, ot_photo_de_coef.

Fusion modes and parameters are described for weight_curve_method and weight_calc_method combinations.
