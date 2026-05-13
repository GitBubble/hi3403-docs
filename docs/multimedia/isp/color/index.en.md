---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ISP 颜色调优说明/ISP 颜色调优说明.md
---

# Preface
**Overview<a name="section302mcpsimp"></a>**

This document is written for debugging and issue localization of AWB, CCM, and CLUT algorithms. It provides detailed instructions on calibration, parameter tuning, and other usage guidelines, aiming to offer solutions and assistance for problems encountered during development.

>![](public_sys-resources/icon-note.gif) **Note:**
>This document uses Hi3403V100 as an example. Unless otherwise specified, Hi3519AV200 content is consistent with Hi3403V100.

**Product Version<a name="section306mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table309mcpsimp"></a>
<table><thead align="left"><tr id="row314mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row320mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p322mcpsimp"><a name="p322mcpsimp"></a><a name="p322mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p324mcpsimp"><a name="p324mcpsimp"></a><a name="p324mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row650476102011"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p16117171192015"><a name="p16117171192015"></a><a name="p16117171192015"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1711771112016"><a name="p1711771112016"></a><a name="p1711771112016"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section325mcpsimp"></a>**

This document (guide) is mainly intended for the following engineers:

-   Technical support engineers
-   Software development engineers

**Symbol Conventions<a name="section331mcpsimp"></a>**

The following symbols may appear in this document, and their meanings are defined below.

<a name="table334mcpsimp"></a>
<table><thead align="left"><tr id="row339mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p341mcpsimp"><a name="p341mcpsimp"></a><a name="p341mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p343mcpsimp"><a name="p343mcpsimp"></a><a name="p343mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row345mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p347mcpsimp"><a name="p347mcpsimp"></a><a name="p347mcpsimp"></a><a name="image138"></a><a name="image138"></a><span><img id="image138" src="figures/zh-cn_image_0000002424362258.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p349mcpsimp"><a name="p349mcpsimp"></a><a name="p349mcpsimp"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row350mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p352mcpsimp"><a name="p352mcpsimp"></a><a name="p352mcpsimp"></a><a name="image139"></a><a name="image139"></a><span><img id="image139" src="figures/zh-cn_image_0000002424362198.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p354mcpsimp"><a name="p354mcpsimp"></a><a name="p354mcpsimp"></a>Indicates a medium-level hazard which, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row355mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p357mcpsimp"><a name="p357mcpsimp"></a><a name="p357mcpsimp"></a><a name="image140"></a><a name="image140"></a><span><img id="image140" src="figures/zh-cn_image_0000002424202358.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>Indicates a low-level hazard which, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row360mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p362mcpsimp"><a name="p362mcpsimp"></a><a name="p362mcpsimp"></a><a name="image141"></a><a name="image141"></a><span><img id="image141" src="figures/zh-cn_image_0000002457840937.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p364mcpsimp"><a name="p364mcpsimp"></a><a name="p364mcpsimp"></a>Conveys device or environment safety warning information. If not avoided, it may result in device damage, data loss, performance degradation, or other unpredictable results.</p>
<p id="p365mcpsimp"><a name="p365mcpsimp"></a><a name="p365mcpsimp"></a>A "Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row366mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p368mcpsimp"><a name="p368mcpsimp"></a><a name="p368mcpsimp"></a><a name="image142"></a><a name="image142"></a><span><img id="image142" src="figures/zh-cn_image_0000002424202378.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p370mcpsimp"><a name="p370mcpsimp"></a><a name="p370mcpsimp"></a>Supplementary explanation of key information in the main text.</p>
<p id="p371mcpsimp"><a name="p371mcpsimp"></a><a name="p371mcpsimp"></a>A "Note" is not a safety warning and does not involve personal, device, or environmental injury information.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section372mcpsimp"></a>**

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

# Principles Introduction
## Color Tuning Overview<a name="ZH-CN_TOPIC_0000002457840885"></a>

The ISP system supports two levels of color tuning schemes.

The first is the basic color tuning scheme. The system color is mainly controlled by AWB+CCM+GAMMA, with a consistent color style across the entire gamut. This means the 3x3 CCM matrix converts the sensor's native color space (device-dependent color) to the sRGB standard-defined color space (device-independent color). The characteristic is that the sensor's response is linearly extended to the target space, meaning all colors receive the same linear extension. The color presentation varies depending on the sensor's spectral response characteristics.

**Figure 1** Basic color tuning flow chart<a name="fig135251247917"></a>
![](figures/基础调色流程图.png "基础调色流程图")

The saturation of all colors increases or decreases with the CCM. Conflicts may arise between different hues. Due to the 3x3 matrix, color adjustment for dark areas, mid-brightness, and highlights is consistent.

The second is the advanced color tuning scheme. The system color is mainly controlled by AWB+CCM+CLUT+GAMMA+CA, and the color style can be adjusted as needed.

**Figure 2** Advanced color tuning flow chart<a name="fig11753153218217"></a>
![](figures/height级调色流程图.png "height级调色流程图")

Two mapping styles are described: gamut-edge inward mapping (reduces high saturation colors to avoid out-of-gamut) and outward mapping (increases saturation for more vivid colors).

## AWB Module Working Principle<a name="ZH-CN_TOPIC_0000002424202166"></a>

The AWB module consists of two parts: the hardware WB information statistics module and the Firmware AWB strategy control algorithm. It calculates RGB means of gray points to determine AWB gain coefficients.

## CCM Module Working Principle<a name="ZH-CN_TOPIC_0000002424202130"></a>

A 3x3 Color Correction Matrix corrects the sensor's spectral response deviation from human vision. Supports 3 to 7 color temperatures.

# AWB Debugging
## Statistics Module Debugging<a name="ZH-CN_TOPIC_0000002457880949"></a>

Gray point condition parameters: white_level (brightness upper limit), black_level (brightness lower limit), cr_max/cr_min (R/G chromatic aberration limits), cb_max/cb_min (B/G chromatic aberration limits). Solution differences exist between platforms (Hi3403V100 uses 16-bit input without black level).

### Statistics Output Description

Output parameters: global_r/g/b (mean RGB of gray points), count_all (normalized count), zone_avg_r/g/b[] (per-zone means).

## AWB Calibration<a name="ZH-CN_TOPIC_0000002424362006"></a>

Parameters: ref_color_temp, static_wb[4], curve_para[0-2] (Planckian curve), curve_para[3-5] (color temperature curve).

Calibration: Capture 24-color card RAW under D50/D75/A/5000K-5500K light sources. Select 3 KIs (A/D50/D75 recommended). Supports up to 32 light sources. Manual/semi-auto adjustment via ot_mpi_isp_cal_gain_by_temp().

Confirmation: Planckian Curve with Shift < 32, color temperature error < 500K for sources below 6500K.

## AWB FW<a name="ZH-CN_TOPIC_0000002457840861"></a>

ot_isp_awb_attr: alg_type (LOWCOST/ADVANCE/NATURA), speed, color temperature limits, ct_limit, shift_limit, gain_norm_en, rg/bg_strength, cb_cr_track, luma_hist, zone_wt.

ot_isp_awb_attr_ex: tolerance, zone_radius, curve_l/r_limit, extra_light_en, in_or_out, multi_light_source_en, fine_tune_en.

## Problem Localization<a name="ZH-CN_TOPIC_0000002424362042"></a>

Analyze Raw data: confirm black level/RGGB, disable CCM/Gamma, configure manual AWB, check Gamma, test mixed light sources. Use 3A analysis tool: verify count_all, check gray point conditions, confirm indoor/outdoor detection, check color temperature range, verify gray blocks within white area.

# Basic Color Tuning Scheme
## CCM Debugging<a name="ZH-CN_TOPIC_0000002457880853"></a>

### CCM Calibration

3x3 matrix calculated from 24-color card data. Supports 3-7 color temperature groups. Configure ISP/Display Gamma, LAB Reference, color block weights, difference standard (CIE76/CIE94/CIE2000), autoGain, BT.2020.

### Manual CCM Modification

CCM formula with white balance preservation conditions. Adjust coefficients to correct color issues (red/purple cast, saturation).

### WDR Mode CCM

Use long-frame RAW, disable autoGain, reduce DRC impact, use Gamma.

### Factors Affecting CCM

Source/target gamma, target color space, white balance, ispdgain.

# Advanced Color Tuning Scheme
## CLUT Debugging<a name="ZH-CN_TOPIC_0000002424361966"></a>

Input methods: color card pairs (24/140 samples), arbitrary color pairs, HSL parameter adjustment (hue +-20, sat 0.4-1.6x, light 0.6-1.4x).

Applications: color card and color value (skin tone) examples.
