---
title: "IMP"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ISP Dev Reference/ISP Dev Reference (6).md
---

# IMP
IMP refers to Image effect modules. The corresponding API interfaces must be called after calling the ss_mpi_isp_init interface.

## Sharpen<a name="ZH-CN_TOPIC_0000002470925214"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470924874"></a>

The Sharpen module is used to enhance image clarity, including adjusting the sharpening attributes of image edges and enhancing the clarity of image details and textures. It can independently control the sharpening strength of directional edges and non-directional detail textures. Additionally, it can control the overshoot (white edges/white spots) and undershoot (black edges/black spots) of the sharpened image, and suppress noise enhancement.

### API Reference<a name="ZH-CN_TOPIC_0000002470924988"></a>

- [ss_mpi_isp_set_sharpen_attr](#ZH-CN_TOPIC_0000002504084757): Set image sharpening attributes.
- [ss_mpi_isp_get_sharpen_attr](#ZH-CN_TOPIC_0000002503964843): Get image sharpening attributes.

#### ss_mpi_isp_set_sharpen_attr<a name="ZH-CN_TOPIC_0000002504084757"></a>

【Description】

Set image sharpening attributes.

【Syntax】

```
td_s32 ss_mpi_isp_set_sharpen_attr(ot_vi_pipe vi_pipe, const ot_isp_sharpen_attr *shp_attr);
```

【Parameters】

<a name="table20464mcpsimp"></a>
<table><thead align="left"><tr id="row20470mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p20472mcpsimp"><a name="p20472mcpsimp"></a><a name="p20472mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.4.1.2"><p id="p20474mcpsimp"><a name="p20474mcpsimp"></a><a name="p20474mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p20476mcpsimp"><a name="p20476mcpsimp"></a><a name="p20476mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row20478mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p20480mcpsimp"><a name="p20480mcpsimp"></a><a name="p20480mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p20482mcpsimp"><a name="p20482mcpsimp"></a><a name="p20482mcpsimp"></a>vi_pipe number.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p20484mcpsimp"><a name="p20484mcpsimp"></a><a name="p20484mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row20485mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p20487mcpsimp"><a name="p20487mcpsimp"></a><a name="p20487mcpsimp"></a>shp_attr</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p20489mcpsimp"><a name="p20489mcpsimp"></a><a name="p20489mcpsimp"></a>Image sharpening attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p20491mcpsimp"><a name="p20491mcpsimp"></a><a name="p20491mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

【Return Value】

<a name="table20493mcpsimp"></a>
<table><thead align="left"><tr id="row20498mcpsimp"><th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.1"><p id="p20500mcpsimp"><a name="p20500mcpsimp"></a><a name="p20500mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.2"><p id="p20502mcpsimp"><a name="p20502mcpsimp"></a><a name="p20502mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20503mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p20505mcpsimp"><a name="p20505mcpsimp"></a><a name="p20505mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p20507mcpsimp"><a name="p20507mcpsimp"></a><a name="p20507mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row20508mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p20510mcpsimp"><a name="p20510mcpsimp"></a><a name="p20510mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p20512mcpsimp"><a name="p20512mcpsimp"></a><a name="p20512mcpsimp"></a>Failure, the value is the error code.</p>
</td>
</tr>
</tbody>
</table>

【Requirements】

- Header files: ot_common_isp.h, ss_mpi_isp.h
- Library files: libot_isp.a, libss_isp.a

【Notes】

None

【Example】

None

【Related Topics】

[ss_mpi_isp_get_sharpen_attr](#ss_mpi_isp_get_sharpen_attr)

#### ss_mpi_isp_get_sharpen_attr<a name="ZH-CN_TOPIC_0000002503964843"></a>

【Description】

Get image sharpening attributes.

【Syntax】

```
td_s32 ss_mpi_isp_get_sharpen_attr(ot_vi_pipe vi_pipe, ot_isp_sharpen_attr *shp_attr);
```

【Parameters】

<a name="table20534mcpsimp"></a>
<table><thead align="left"><tr id="row20540mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p20542mcpsimp"><a name="p20542mcpsimp"></a><a name="p20542mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.4.1.2"><p id="p20544mcpsimp"><a name="p20544mcpsimp"></a><a name="p20544mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p20546mcpsimp"><a name="p20546mcpsimp"></a><a name="p20546mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row20547mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p20549mcpsimp"><a name="p20549mcpsimp"></a><a name="p20549mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p20551mcpsimp"><a name="p20551mcpsimp"></a><a name="p20551mcpsimp"></a>vi_pipe number.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p20553mcpsimp"><a name="p20553mcpsimp"></a><a name="p20553mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row20554mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p20556mcpsimp"><a name="p20556mcpsimp"></a><a name="p20556mcpsimp"></a>shp_attr</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p20558mcpsimp"><a name="p20558mcpsimp"></a><a name="p20558mcpsimp"></a>Image sharpening attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p20560mcpsimp"><a name="p20560mcpsimp"></a><a name="p20560mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table>

【Return Value】

<a name="table20563mcpsimp"></a>
<table><thead align="left"><tr id="row20568mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.3.1.1"><p id="p20570mcpsimp"><a name="p20570mcpsimp"></a><a name="p20570mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.1.3.1.2"><p id="p20572mcpsimp"><a name="p20572mcpsimp"></a><a name="p20572mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20573mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.3.1.1 "><p id="p20575mcpsimp"><a name="p20575mcpsimp"></a><a name="p20575mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.1.3.1.2 "><p id="p20577mcpsimp"><a name="p20577mcpsimp"></a><a name="p20577mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row20578mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.3.1.1 "><p id="p20580mcpsimp"><a name="p20580mcpsimp"></a><a name="p20580mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.1.3.1.2 "><p id="p20582mcpsimp"><a name="p20582mcpsimp"></a><a name="p20582mcpsimp"></a>Failure, the value is the error code.</p>
</td>
</tr>
</tbody>
</table>

【Requirements】

- Header files: ot_common_isp.h, ss_mpi_isp.h
- Library files: libot_isp.a, libss_isp.a

【Notes】

None

【Example】

None

【Related Topics】

[ss_mpi_isp_set_sharpen_attr](#ss_mpi_isp_set_sharpen_attr)

### Data Types<a name="ZH-CN_TOPIC_0000002504084939"></a>

- [OT_ISP_SHARPEN_LUMA_NUM](#ZH-CN_TOPIC_0000002504084895): Number of luminance sharpening weight intervals.
- [OT_ISP_SHARPEN_GAIN_NUM](#ZH-CN_TOPIC_0000002503964815): Number of detail sharpening weight intervals.
- [ot_isp_sharpen_manual_attr](#ZH-CN_TOPIC_0000002470925194): Defines ISP Sharpen manual attributes.
- [ot_isp_sharpen_auto_attr](#ZH-CN_TOPIC_0000002470924892): Defines ISP Sharpen auto attributes.
- [ot_isp_sharpen_detail_map](#ZH-CN_TOPIC_0000002504085051): Whether to display the image detail grayscale map.
- [ot_isp_sharpen_attr](#ZH-CN_TOPIC_0000002503965141): Defines ISP Sharpen attributes.

#### OT_ISP_SHARPEN_LUMA_NUM<a name="ZH-CN_TOPIC_0000002504084895"></a>

【Description】

Number of luminance sharpening weight intervals.

【Definition】

```
#define OT_ISP_SHARPEN_LUMA_NUM         32
```

【Notes】

None.

【Related Data Types and Interfaces】

- [ot_isp_sharpen_manual_attr](#ot_isp_sharpen_manual_attr)
- [ot_isp_sharpen_auto_attr](#ot_isp_sharpen_auto_attr)

#### OT_ISP_SHARPEN_GAIN_NUM<a name="ZH-CN_TOPIC_0000002503964815"></a>

【Description】

Number of detail sharpening weight intervals.

【Definition】

```
#define OT_ISP_SHARPEN_GAIN_NUM         16
```

【Notes】

None.

【Related Data Types and Interfaces】

- [ot_isp_sharpen_manual_attr](#ot_isp_sharpen_manual_attr)
- [ot_isp_sharpen_auto_attr](#ot_isp_sharpen_auto_attr)

## Gamma<a name="ZH-CN_TOPIC_0000002471085182"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470925176"></a>

The Gamma module performs nonlinear luminance space conversion on the image to adapt to the output device. The Gamma module uses the same Gamma table when correcting R, G, and B. The intervals between Gamma table nodes are equal, and image pixel values between nodes are generated using linear interpolation.

### API Reference<a name="ZH-CN_TOPIC_0000002504084967"></a>

- [ss_mpi_isp_set_gamma_attr](#ZH-CN_TOPIC_0000002470924914): Set Gamma attributes.
- [ss_mpi_isp_get_gamma_attr](#ZH-CN_TOPIC_0000002471085092): Get Gamma attributes.

#### ss_mpi_isp_set_gamma_attr<a name="ZH-CN_TOPIC_0000002470924914"></a>

【Description】

Set Gamma attributes.

【Syntax】

```
td_s32 ss_mpi_isp_set_gamma_attr(ot_vi_pipe vi_pipe, const ot_isp_gamma_attr *gamma_attr);
```

【Parameters】

<a name="table20720mcpsimp"></a>
<table><thead align="left"><tr id="row20726mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p20728mcpsimp"><a name="p20728mcpsimp"></a><a name="p20728mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.4.1.2"><p id="p20730mcpsimp"><a name="p20730mcpsimp"></a><a name="p20730mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p20732mcpsimp"><a name="p20732mcpsimp"></a><a name="p20732mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row20733mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p20735mcpsimp"><a name="p20735mcpsimp"></a><a name="p20735mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p20737mcpsimp"><a name="p20737mcpsimp"></a><a name="p20737mcpsimp"></a>vi_pipe number.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p20739mcpsimp"><a name="p20739mcpsimp"></a><a name="p20739mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row20740mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p20742mcpsimp"><a name="p20742mcpsimp"></a><a name="p20742mcpsimp"></a>gamma_attr</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p20744mcpsimp"><a name="p20744mcpsimp"></a><a name="p20744mcpsimp"></a>Gamma attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p20746mcpsimp"><a name="p20746mcpsimp"></a><a name="p20746mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

【Return Value】

<a name="table20749mcpsimp"></a>
<table><thead align="left"><tr id="row20754mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.3.1.1"><p id="p20756mcpsimp"><a name="p20756mcpsimp"></a><a name="p20756mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.1.3.1.2"><p id="p20758mcpsimp"><a name="p20758mcpsimp"></a><a name="p20758mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20759mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.3.1.1 "><p id="p20761mcpsimp"><a name="p20761mcpsimp"></a><a name="p20761mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.1.3.1.2 "><p id="p20763mcpsimp"><a name="p20763mcpsimp"></a><a name="p20763mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row20764mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.3.1.1 "><p id="p20766mcpsimp"><a name="p20766mcpsimp"></a><a name="p20766mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.1.3.1.2 "><p id="p20768mcpsimp"><a name="p20768mcpsimp"></a><a name="p20768mcpsimp"></a>Failure, the value is the error code.</p>
</td>
</tr>
</tbody>
</table>

【Requirements】

- Header files: ot_common_isp.h, ss_mpi_isp.h
- Library files: libot_isp.a, libss_isp.a

【Notes】

None

【Example】

None

【Related Topics】

[ss_mpi_isp_get_gamma_attr](#ss_mpi_isp_get_gamma_attr)

#### ss_mpi_isp_get_gamma_attr<a name="ZH-CN_TOPIC_0000002471085092"></a>

【Description】

Get Gamma attributes.

【Syntax】

```
td_s32 ss_mpi_isp_get_gamma_attr(ot_vi_pipe vi_pipe, ot_isp_gamma_attr *gamma_attr);
```

(Parameters, Return Value, Requirements follow the same pattern.)

【Related Topics】

[ss_mpi_isp_set_gamma_attr](#ss_mpi_isp_set_gamma_attr)

## DRC<a name="ZH-CN_TOPIC_0000002471084976"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470925060"></a>

The DRC algorithm is used to perform Dynamic Range Compression on data after WDR synthesis. Images typically need to be displayed on display devices. CRT monitors generally have a dynamic range of less than 50dB, while the dynamic range of WDR-synthesized data can reach 120dB. If displayed directly on a CRT monitor, dynamic range mismatch would cause loss of detail in areas with very high or very low brightness.

The purpose of the DRC algorithm is to ensure that both the observer of the real scene and the observer of the display device have the same visual experience. The DRC algorithm compresses high dynamic range images into the dynamic range of the display device while preserving as much of the original image's details and contrast as possible.

**Figure 1** Dynamic Range Compression<a name="fig040711214316"></a>  
![](figures/Sharpen的像素亮度luma和锐化强度luma_wgt的关系曲线.png)

### API Reference<a name="ZH-CN_TOPIC_0000002503965163"></a>

- [ss_mpi_isp_set_drc_attr](#ZH-CN_TOPIC_0000002470925106): Set dynamic range compression parameters.
- [ss_mpi_isp_get_drc_attr](#ZH-CN_TOPIC_0000002504084695): Get dynamic range compression parameters.

#### ss_mpi_isp_set_drc_attr<a name="ZH-CN_TOPIC_0000002470925106"></a>

【Description】

Set dynamic range compression parameters.

【Syntax】

```
td_s32 ss_mpi_isp_set_drc_attr(ot_vi_pipe vi_pipe, const ot_isp_drc_attr *drc_attr);
```

【Related Topics】

[ss_mpi_isp_get_drc_attr](#ss_mpi_isp_get_drc_attr)

## Mesh Shading<a name="ZH-CN_TOPIC_0000002504084945"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470925100"></a>

The LSC module is mainly used to handle vignetting (shadows around the lens edges) caused by non-uniform optical refraction of the lens. Currently popular processing methods include the Radial (coaxial circle) method and the Mesh (grid) method.

In Hi3403V100, the Mesh Shading algorithm uses the Mesh (grid) method for lens calibration/correction. The algorithm divides the entire Bayer domain image into 32x32 sub-regions, each approximately equal in size.

During data processing, the algorithm processes each channel in the RAW domain separately.

### API Reference<a name="ZH-CN_TOPIC_0000002471085046"></a>

- [ss_mpi_isp_set_mesh_shading_attr](#ZH-CN_TOPIC_0000002471085058): Set Mesh Shading algorithm parameters.
- [ss_mpi_isp_get_mesh_shading_attr](#ZH-CN_TOPIC_0000002470925048): Get Mesh Shading algorithm parameters.
- [ss_mpi_isp_set_mesh_shading_gain_lut_attr](#ZH-CN_TOPIC_0000002470925160): Set Mesh Shading gain LUT attributes.
- [ss_mpi_isp_get_mesh_shading_gain_lut_attr](#ZH-CN_TOPIC_0000002504084899): Get Mesh Shading gain LUT attributes.

## Defect Pixel<a name="ZH-CN_TOPIC_0000002471085180"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471084974"></a>

The Defect Pixel Correction module uses dynamic and static methods to detect and correct defective pixels in images. Due to sensor process or material issues, some pixel points may have abnormal brightness (bright spots or dark spots). The Defect Pixel module has two working modes: Static Defect Pixel Correction (SDPC) and Dynamic Defect Pixel Correction (DDPC).

Static correction is applied to fixed defective pixel points by calibrating coordinates using a calibration tool, storing them in a static defect pixel table, and using this table for correction. Dynamic correction uses neighborhood pixel comparison algorithms to dynamically detect and correct possible defective pixel points in real time.

### API Reference<a name="ZH-CN_TOPIC_0000002504084721"></a>

- [ss_mpi_isp_set_dpc_attr](#ZH-CN_TOPIC_0000002471084902): Set defect pixel correction attributes.
- [ss_mpi_isp_get_dpc_attr](#ZH-CN_TOPIC_0000002471085016): Get defect pixel correction attributes.
- [ss_mpi_isp_set_dpc_dynamic_attr](#ZH-CN_TOPIC_0000002503964873): Set DPC dynamic attributes.
- [ss_mpi_isp_get_dpc_dynamic_attr](#ZH-CN_TOPIC_0000002503964807): Get DPC dynamic attributes.

## Crosstalk Removal<a name="ZH-CN_TOPIC_0000002504084817"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085116"></a>

The purpose of cross-color removal is to reduce the color cross-talk phenomenon in images caused by the increasing photosensitivity of pixel sensors, which leads to increased optical crosstalk between different color channels of adjacent pixels. Eliminating or reducing this crosstalk improves image color reproduction.

### API Reference<a name="ZH-CN_TOPIC_0000002503964987"></a>

- [ss_mpi_isp_set_xtalk_attr](#ZH-CN_TOPIC_0000002470925054): Set cross-color removal attributes.
- [ss_mpi_isp_get_xtalk_attr](#ZH-CN_TOPIC_0000002504085025): Get cross-color removal attributes.

## Denoising Algorithm<a name="ZH-CN_TOPIC_0000002504084747"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470925042"></a>

The ISP denoising algorithm can be divided into two processing stages. In the RAW domain denoising stage, since valuable signal and noise are mixed together, reducing noise inevitably causes some loss of detail. To balance this, current denoising algorithms apply different denoising intensity levels based on the image brightness. The algorithm independently adjusts the denoising strength for both the luminance channel and the combined chrominance channel, making denoising more flexible.

In the YUV domain denoising stage, the image has been demosaiced and separated into luminance and chrominance information. Human vision is more sensitive to luminance noise than chrominance noise, so the denoising strategy differs: luminance noise is mainly removed through 2D + 3D filtering, while chrominance noise is primarily handled by median filtering.

### API Reference<a name="ZH-CN_TOPIC_0000002504084959"></a>

- [ss_mpi_isp_set_nr_attr](#ZH-CN_TOPIC_0000002504085001): Set denoising attributes.
- [ss_mpi_isp_get_nr_attr](#ZH-CN_TOPIC_0000002504084741): Get denoising attributes.
- [ss_mpi_isp_set_nr_attr_ex](#ZH-CN_TOPIC_0000002504085049): Set denoising extended attributes.
- [ss_mpi_isp_get_nr_attr_ex](#ZH-CN_TOPIC_0000002504084729): Get denoising extended attributes.
- [ss_mpi_isp_set_ynr_attr](#ZH-CN_TOPIC_0000002471085002): Set luminance denoising attributes.
- [ss_mpi_isp_get_ynr_attr](#ZH-CN_TOPIC_0000002470925166): Get luminance denoising attributes.
- [ss_mpi_isp_set_cnr_attr](#ZH-CN_TOPIC_0000002471084994): Set chrominance denoising attributes.
- [ss_mpi_isp_get_cnr_attr](#ZH-CN_TOPIC_0000002504084871): Get chrominance denoising attributes.

## Dehaze<a name="ZH-CN_TOPIC_0000002470924958"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002504084855"></a>

Dehaze is implemented by dynamically changing the contrast and brightness of the image. The image is divided into blocks, the pixel values within each block are counted, the fog concentration is estimated, and the dehazing intensity is adjusted according to a local adaptive curve. Dehaze has manual and automatic modes, and the dehazing intensity can be adjusted in both modes.

### API Reference<a name="ZH-CN_TOPIC_0000002504084833"></a>

- [ss_mpi_isp_set_dehaze_attr](#ZH-CN_TOPIC_0000002470924876): Set dehaze attributes.
- [ss_mpi_isp_get_dehaze_attr](#ZH-CN_TOPIC_0000002470925172): Get dehaze attributes.

## False Color Removal<a name="ZH-CN_TOPIC_0000002503964915"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002504084735"></a>

High-frequency components can easily cause high-frequency aliasing during image interpolation. When a lens is pointed at a resolution test chart and there is no OLPF on the sensor surface, false colors are prone to appear in the high-frequency part of the resolution.

False color removal mainly refers to removing the false color phenomenon caused by interpolation errors in the high-frequency part. Increasing the false color removal intensity will reduce the false color phenomenon but may cause normal colors to become grayscale.

### API Reference<a name="ZH-CN_TOPIC_0000002504084933"></a>

- [ss_mpi_isp_set_false_color_attr](#ZH-CN_TOPIC_0000002470925142): Set false color removal attributes.
- [ss_mpi_isp_get_false_color_attr](#ZH-CN_TOPIC_0000002471085044): Get false color removal attributes.

## Demosaic<a name="ZH-CN_TOPIC_0000002471085200"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085040"></a>

The Demosaic module converts input Bayer data into RGB data. In the Bayer data obtained from the CFA (Color Filter Array), each pixel can only obtain one color component among the three primary colors R, G, and B. To obtain a color image, it is necessary to use the color component values of the current pixel and surrounding pixels to estimate the other two missing component values of the current point.

This module can output higher image resolution, significantly improving weak details and sharpness.

**Figure 1** Demosaic Principle Diagram<a name="fig15860155811308"></a>  
![](figures/texture_strength-OT_ISP_SHARPEN_GAIN_NUM-强度曲线示意图.png)

### API Reference<a name="ZH-CN_TOPIC_0000002504084755"></a>

- [ss_mpi_isp_set_demosaic_attr](#ZH-CN_TOPIC_0000002504084729): Set Demosaic attributes.
- [ss_mpi_isp_get_demosaic_attr](#ZH-CN_TOPIC_0000002470924954): Get Demosaic attributes.

## BayerSharpen<a name="ZH-CN_TOPIC_0000002471085192"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085006"></a>

The BayerSharpen module is used to enhance image clarity, including adjusting the sharpening attributes of image edges and enhancing image details and textures. It can also control the sharpening intensity of image edges in the horizontal and vertical directions. Additionally, it can control the overshoot and undershoot of the sharpened image and suppress noise enhancement.

### API Reference<a name="ZH-CN_TOPIC_0000002504085061"></a>

- [ss_mpi_isp_set_bayer_sharpen_attr](#ZH-CN_TOPIC_0000002504084801): Set BayerSh sharpen attributes.
- [ss_mpi_isp_get_bayer_sharpen_attr](#ZH-CN_TOPIC_0000002504084893): Get BayerSharpen attributes.

## Black Level<a name="ZH-CN_TOPIC_0000002503965159"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470924920"></a>

Black level usually refers to the brightness value that the sensor still outputs when there is no external light input. ISP needs to subtract this brightness value for color processing.

### API Reference<a name="ZH-CN_TOPIC_0000002503965145"></a>

- [ss_mpi_isp_set_black_level_attr](#ZH-CN_TOPIC_0000002503964765): Set black level attributes.
- [ss_mpi_isp_get_black_level_attr](#ZH-CN_TOPIC_0000002471085038): Get black level attributes.

## FPN Removal<a name="ZH-CN_TOPIC_0000002470924868"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085228"></a>

The sensor converts optical signals into electrical signals and outputs the image through millions of ADC devices. Variations in the photodiode size, doping concentration, contamination during production, and MOS field-effect transistor parameter deviations in each pixel structure can cause changes in the pixel output signal. The noise caused by these deviations is fixed for a given individual pixel, known as Fixed Pattern Noise (FPN).

The FPN removal module is used to eliminate these fixed pattern noises.

### API Reference<a name="ZH-CN_TOPIC_0000002503965067"></a>

- [ss_mpi_isp_set_fpn_attr](#ZH-CN_TOPIC_0000002471084904): Set FPN removal attributes.
- [ss_mpi_isp_get_fpn_attr](#ZH-CN_TOPIC_0000002504084731): Get FPN removal attributes.

## CA<a name="ZH-CN_TOPIC_0000002470925112"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002504084871"></a>

The color adjustment module supports color gamut adjustment in YUV space. This module has two modes: CA mode and CP mode (thermal imaging coloring). Only one of the two can be used at a time.

In CA mode, a pixel point (Y, U, V) can be mapped to another pixel point (Y', U', V') through the following formula.

### API Reference<a name="ZH-CN_TOPIC_0000002503964989"></a>

- [ss_mpi_isp_set_ca_attr](#ZH-CN_TOPIC_0000002471084976): Set CA attributes.
- [ss_mpi_isp_get_ca_attr](#ZH-CN_TOPIC_0000002471085082): Get CA attributes.

## CAC<a name="ZH-CN_TOPIC_0000002470924984"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085048"></a>

Chromatic Aberration refers to the optical phenomenon where a lens cannot focus light of all wavelengths to the same point. It is a lens-related defect mainly caused by different wavelengths of light having different refractive indices (dispersion). Chromatic aberration can be divided into two types:

- Axial Chromatic Aberration: Lens has different refractive indices for different light, so different colors focus on different focal planes. Large aperture lenses are prone to this type of aberration; stopping down the aperture can reduce axial chromatic aberration.
- Lateral Chromatic Aberration: Different wavelengths of light are magnified differently by the lens.

### API Reference<a name="ZH-CN_TOPIC_0000002503964841"></a>

- [ss_mpi_isp_set_cac_attr](#ZH-CN_TOPIC_0000002504084711): Set CAC attributes.
- [ss_mpi_isp_get_cac_attr](#ZH-CN_TOPIC_0000002470925176): Get CAC attributes.

## WDR<a name="ZH-CN_TOPIC_0000002503964833"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470925054"></a>

Since traditional image sensors have a relatively low dynamic range, capturing high dynamic range scenes with traditional sensors results in either overexposed bright areas (losing many details) or underexposed dark areas (details difficult to discern). To record every detail of a high dynamic range scene, multi-exposure image synthesis can be used.

The purpose of the WDR algorithm is to synthesize the long and short frame data output from the sensor into one frame of 20-bit data. Long and short frame data is first buffered in DDR and then simultaneously sent to the WDR module for synthesis. The synthesis principle is optimal selection: for brighter areas, short frame data is used; for darker areas, long frame data is used.

**Figure 1** WDR Synthesis Diagram<a name="_Ref498504952"></a>  
![](figures/edge_strength-OT_ISP_SHARPEN_GAIN_NUM-强度曲线示意图.png)

### API Reference<a name="ZH-CN_TOPIC_0000002471084902"></a>

- [ss_mpi_isp_set_wdr_attr](#ZH-CN_TOPIC_0000002504084973): Set WDR attributes.
- [ss_mpi_isp_get_wdr_attr](#ZH-CN_TOPIC_0000002471085066): Get WDR attributes.
- [ss_mpi_isp_set_wdr_compensate_attr](#ZH-CN_TOPIC_0000002504084889): Set WDR compensation attributes.
- [ss_mpi_isp_get_wdr_compensate_attr](#ZH-CN_TOPIC_0000002504084849): Get WDR compensation attributes.

## AWB Mass Production Calibration Tool<a name="ZH-CN_TOPIC_0000002504084875"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002503964911"></a>

> ![](public_sys-resources/icon-caution.gif) **CAUTION:** 
> AWB mass production calibration results correct individual differences by modifying the static white balance coefficients of AWB. Therefore, users modifying static white balance coefficients through the MPI interface will invalidate the mass production calibration.

The AWB mass production calibration tool implements correction of AWB difference parameters for different devices during mass production. Users can call the ss_mpi_isp_get_lightbox_gain interface to obtain the average Rgain and Bgain values of several blocks in the center of the image under a uniform light source in the color temperature range of 4500K to 6500K with a uniform background environment. These AWB gains are used to correct AWB difference parameters for different devices during mass production.

## ColorTone<a name="ZH-CN_TOPIC_0000002470924966"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002504084771"></a>

The ColorTone module is used to adjust the overall color tone of the image.

### API Reference<a name="ZH-CN_TOPIC_0000002470925072"></a>

- [ss_mpi_isp_set_colortone_attr](#ZH-CN_TOPIC_0000002504084749): Set ColorTone attributes.
- [ss_mpi_isp_get_colortone_attr](#ZH-CN_TOPIC_0000002503964775): Get ColorTone attributes.

## LDCI<a name="ZH-CN_TOPIC_0000002471084892"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085194"></a>

Local Contrast enhancement is used to improve image contrast and detail in local areas.

### API Reference<a name="ZH-CN_TOPIC_0000002504084689"></a>

- [ss_mpi_isp_set_ldci_attr](#ZH-CN_TOPIC_0000002503964771): Set LDCI attributes.
- [ss_mpi_isp_get_ldci_attr](#ZH-CN_TOPIC_0000002504084815): Get LDCI attributes.

## Radial Crop<a name="ZH-CN_TOPIC_0000002503965135"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471084978"></a>

The Radial Crop module is used to crop the edge area of a circular image.

### API Reference<a name="ZH-CN_TOPIC_0000002471084970"></a>

- [ss_mpi_isp_set_radial_crop_attr](#ZH-CN_TOPIC_0000002471085054): Set Radial Crop attributes.
- [ss_mpi_isp_get_radial_crop_attr](#ZH-CN_TOPIC_0000002470925182): Get Radial Crop attributes.

## CSC<a name="ZH-CN_TOPIC_0000002503964863"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002470925138"></a>

The CSC (Color Space Conversion) module is used for conversion between different color spaces, such as converting RGB to YUV or YUV to RGB.

### API Reference<a name="ZH-CN_TOPIC_0000002504084937"></a>

- [ss_mpi_isp_set_csc_attr](#ZH-CN_TOPIC_0000002504084985): Set CSC attributes.
- [ss_mpi_isp_get_csc_attr](#ZH-CN_TOPIC_0000002504084991): Get CSC attributes.

## CLUT<a name="ZH-CN_TOPIC_0000002470925122"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002504085015"></a>

The CLUT (Color Look-Up Table) module uses a 3D color lookup table for color mapping and adjustment.

### API Reference<a name="ZH-CN_TOPIC_0000002503964787"></a>

- [ss_mpi_isp_set_clut_attr](#ZH-CN_TOPIC_0000002504084977): Set CLUT attributes.
- [ss_mpi_isp_get_clut_attr](#ZH-CN_TOPIC_0000002471085064): Get CLUT attributes.

## PreGamma<a name="ZH-CN_TOPIC_0000002470924928"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002503965137"></a>

The PreGamma module performs gamma correction before image processing.

### API Reference<a name="ZH-CN_TOPIC_0000002471085014"></a>

- [ss_mpi_isp_set_pregamma_attr](#ZH-CN_TOPIC_0000002504084755): Set PreGamma attributes.
- [ss_mpi_isp_get_pregamma_attr](#ZH-CN_TOPIC_0000002471085206): Get PreGamma attributes.

## Get ISP Module Virtual Address<a name="ZH-CN_TOPIC_0000002504084915"></a>

### API Reference<a name="ZH-CN_TOPIC_0000002471085086"></a>

- [ss_mpi_isp_query_vir_addr](#ZH-CN_TOPIC_0000002470924960): Query ISP module virtual address.

## Query Internal Status Information<a name="ZH-CN_TOPIC_0000002470924974"></a>

### API Reference<a name="ZH-CN_TOPIC_0000002504084955"></a>

- [ss_mpi_isp_query_inner_info](#ZH-CN_TOPIC_0000002470925200): Query ISP internal status information.

## DNG<a name="ZH-CN_TOPIC_0000002503964931"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085088"></a>

The DNG module implements raw image data output in DNG format, supporting the DNG standard for digital negative image storage.

### API Reference<a name="ZH-CN_TOPIC_0000002504085027"></a>

- [ss_mpi_isp_set_dng_attr](#ZH-CN_TOPIC_0000002503964767): Set DNG attributes.
- [ss_mpi_isp_get_dng_attr](#ZH-CN_TOPIC_0000002471085028): Get DNG attributes.

## MeshShading Mass Production Calibration Tool<a name="ZH-CN_TOPIC_0000002470925162"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471084954"></a>

The MeshShading mass production calibration tool implements correction of Lens Shading Correction difference parameters for different devices during mass production.

### API Reference<a name="ZH-CN_TOPIC_0000002470924932"></a>

- [ss_mpi_isp_set_mesh_shading_calibration_attr](#ZH-CN_TOPIC_0000002504084971): Set MeshShading calibration attributes.
- [ss_mpi_isp_get_mesh_shading_calibration_attr](#ZH-CN_TOPIC_0000002504084911): Get MeshShading calibration attributes.

## RGB-IR<a name="ZH-CN_TOPIC_0000002503964859"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002471085020"></a>

The RGB-IR module supports image sensors with RGB + IR filter arrays, enabling simultaneous visible light and infrared image capture.

### API Reference<a name="ZH-CN_TOPIC_0000002504085023"></a>

- [ss_mpi_isp_set_rgbir_attr](#ZH-CN_TOPIC_0000002503964921): Set RGB-IR attributes.
- [ss_mpi_isp_get_rgbir_attr](#ZH-CN_TOPIC_0000002471084968): Get RGB-IR attributes.

## Auto Flicker Type Detection<a name="ZH-CN_TOPIC_0000002503964893"></a>

### Function Description<a name="ZH-CN_TOPIC_0000002503965111"></a>

The Auto Flicker Type Detection module automatically detects the power frequency type (50Hz/60Hz) of the light source environment and configures the anti-flicker frequency accordingly.

### API Reference<a name="ZH-CN_TOPIC_0000002470924988"></a>

- [ss_mpi_isp_set_anti_flicker_detect_attr](#ZH-CN_TOPIC_0000002504084743): Set auto flicker detection attributes.
- [ss_mpi_isp_get_anti_flicker_detect_attr](#ZH-CN_TOPIC_0000002471085142): Get auto flicker detection attributes.
