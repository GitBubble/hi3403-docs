---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/黑白彩色双路融合调试指南/黑白彩色双路融合调试指南.md
---

# Preface
**Overview<a name="section143mcpsimp"></a>**

This document is written for developers working with Mono-Color Fusion (MCF) tuning. It introduces the basic principles, operating procedures, and optimization methods for MCF.

>![](public_sys-resources/icon-note.gif) **Note:** 
>This document uses the Hi3403V100 as an example. Unless otherwise specified, Hi3519AV200 and Hi3403V100 content is identical.

**Product Versions<a name="section146mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table149mcpsimp"></a>
<table><thead align="left"><tr id="row154mcpsimp"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p156mcpsimp"><a name="p156mcpsimp"></a><a name="p156mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p158mcpsimp"><a name="p158mcpsimp"></a><a name="p158mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row160mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p162mcpsimp"><a name="p162mcpsimp"></a><a name="p162mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p164mcpsimp"><a name="p164mcpsimp"></a><a name="p164mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row10658134621312"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p812864918138"><a name="p812864918138"></a><a name="p812864918138"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p41282499138"><a name="p41282499138"></a><a name="p41282499138"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section165mcpsimp"></a>**

This document (this guide) is primarily intended for the following engineers:

- Technical support engineers
- Software development engineers

**Symbol Conventions<a name="section171mcpsimp"></a>**

The following symbols may appear in this document. Their meanings are as follows.

<a name="table174mcpsimp"></a>
<table><thead align="left"><tr id="row179mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.3.1.1"><p id="p181mcpsimp"><a name="p181mcpsimp"></a><a name="p181mcpsimp"></a><strong id="b182mcpsimp"><a name="b182mcpsimp"></a><a name="b182mcpsimp"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79%" id="mcps1.1.3.1.2"><p id="p184mcpsimp"><a name="p184mcpsimp"></a><a name="p184mcpsimp"></a><strong id="b185mcpsimp"><a name="b185mcpsimp"></a><a name="b185mcpsimp"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row187mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p189mcpsimp"><a name="p189mcpsimp"></a><a name="p189mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="/multimedia/dual-fusion/tuning/figures/zh-cn_image_0000002424362286.png" height="23.94" width="66.5"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a>Indicates a high-risk hazard that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row192mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p194mcpsimp"><a name="p194mcpsimp"></a><a name="p194mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="/multimedia/dual-fusion/tuning/figures/zh-cn_image_0000002424202450.png" height="23.94" width="66.5"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a>Indicates a medium-risk hazard that, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row197mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p199mcpsimp"><a name="p199mcpsimp"></a><a name="p199mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="/multimedia/dual-fusion/tuning/figures/zh-cn_image_0000002457841081.png" height="23.94" width="66.5"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a>Indicates a low-risk hazard that, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row202mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p204mcpsimp"><a name="p204mcpsimp"></a><a name="p204mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="/multimedia/dual-fusion/tuning/figures/zh-cn_image_0000002457841065.png" height="23.94" width="66.5"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p206mcpsimp"><a name="p206mcpsimp"></a><a name="p206mcpsimp"></a>Used to convey equipment or environmental safety warning information. If not avoided, it may result in equipment damage, data loss, performance degradation, or other unpredictable results.</p>
<p id="p207mcpsimp"><a name="p207mcpsimp"></a><a name="p207mcpsimp"></a>"Notice" does not involve personal injury.</p>
</td>
</tr>
<tr id="row208mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p210mcpsimp"><a name="p210mcpsimp"></a><a name="p210mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="/multimedia/dual-fusion/tuning/figures/zh-cn_image_0000002424362302.png" height="23.94" width="66.5"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a>Supplementary explanation of key information in the main text.</p>
<p id="p213mcpsimp"><a name="p213mcpsimp"></a><a name="p213mcpsimp"></a>"Note" is not a safety warning and does not involve personal, equipment, or environmental harm.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section214mcpsimp"></a>**

The revision history accumulates descriptions of each document update. The latest version of the document contains the updates from all previous versions.

<a name="table126443203200"></a>
<table><thead align="left"><tr id="row264516207203"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p146456203200"><a name="p146456203200"></a><a name="p146456203200"></a><strong id="b8645172022010"><a name="b8645172022010"></a><a name="b8645172022010"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p364512062019"><a name="p364512062019"></a><a name="p364512062019"></a><strong id="b1464512200200"><a name="b1464512200200"></a><a name="b1464512200200"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p664522018206"><a name="p664522018206"></a><a name="p664522018206"></a><strong id="b156451420152010"><a name="b156451420152010"></a><a name="b156451420152010"></a>Modification Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row56451520182017"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p1564572014209"><a name="p1564572014209"></a><a name="p1564572014209"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p126451920132014"><a name="p126451920132014"></a><a name="p126451920132014"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1664582017209"><a name="p1664582017209"></a><a name="p1664582017209"></a>First provisional release.</p>
</td>
</tr>
</tbody>
</table>

# Functional Description
In low-light scenarios, images captured by an RGB sensor often have very poor signal-to-noise ratio with severe loss of detail. Based on the new RGB + Mono dual-sensor architecture, the color image captured by the RGB sensor fully retains color information, while the IR image captured by the Mono sensor, combined with IR fill light technology, has a relatively higher signal-to-noise ratio and better detail representation.

Mono-Color Fusion (MCF) technology is used to fuse the above color image and IR image, retaining color information while fully enhancing image detail and signal-to-noise ratio, thus improving image quality in low-light scenarios.

The basic principle diagram of the MCF module is shown in [Figure 1](#fig1275217156391).

**Figure 1**  MCF module basic principle diagram<a name="fig1275217156391"></a>  
![](figures/MCF模块基本原理图.png "MCF模块基本原理图")
# Key Parameters
<a name="table244mcpsimp"></a>
<table><thead align="left"><tr id="row251mcpsimp"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.1"><p id="p253mcpsimp"><a name="p253mcpsimp"></a><a name="p253mcpsimp"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.1.5.1.2"><p id="p255mcpsimp"><a name="p255mcpsimp"></a><a name="p255mcpsimp"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.3"><p id="p257mcpsimp"><a name="p257mcpsimp"></a><a name="p257mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.4"><p id="p259mcpsimp"><a name="p259mcpsimp"></a><a name="p259mcpsimp"></a>Range</p>
</th>
</tr>
</thead>
<tbody><tr id="row261mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p263mcpsimp"><a name="p263mcpsimp"></a><a name="p263mcpsimp"></a>IR Filter</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.2 "><p id="p265mcpsimp"><a name="p265mcpsimp"></a><a name="p265mcpsimp"></a>mono_flt_radius</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.3 "><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a>Filter window radius for the brightness of the IR image. A larger radius extracts stronger detail, while the base layer becomes correspondingly blurrier. This filter window radius can be configured separately for high-frequency, mid-frequency, and low-frequency components of the IR image.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.4 "><p id="p269mcpsimp"><a name="p269mcpsimp"></a><a name="p269mcpsimp"></a>[1,2]</p>
</td>
</tr>
<tr id="row270mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p272mcpsimp"><a name="p272mcpsimp"></a><a name="p272mcpsimp"></a>mono_flt_bias_lut[9]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p274mcpsimp"><a name="p274mcpsimp"></a><a name="p274mcpsimp"></a>This lookup table controls the intensity of detail extracted from the IR image at different brightness levels. A larger value extracts stronger detail. This lookup table can be configured separately for high-frequency, mid-frequency, and low-frequency components.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p276mcpsimp"><a name="p276mcpsimp"></a><a name="p276mcpsimp"></a>[1,128]</p>
</td>
</tr>
<tr id="row277mcpsimp"><td class="cellrowborder" rowspan="6" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p279mcpsimp"><a name="p279mcpsimp"></a><a name="p279mcpsimp"></a>Color Filter</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.2 "><p id="p281mcpsimp"><a name="p281mcpsimp"></a><a name="p281mcpsimp"></a>color_flt_radius</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.3 "><p id="p283mcpsimp"><a name="p283mcpsimp"></a><a name="p283mcpsimp"></a>Filter window radius for the brightness of the color image. A larger radius makes the brightness base layer of the color image blurrier. This filter window radius can be configured separately for high-frequency, mid-frequency, and low-frequency components of the color image.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.4 "><p id="p285mcpsimp"><a name="p285mcpsimp"></a><a name="p285mcpsimp"></a>[1,4]</p>
</td>
</tr>
<tr id="row286mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p288mcpsimp"><a name="p288mcpsimp"></a><a name="p288mcpsimp"></a>color_flt_sgms</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p290mcpsimp"><a name="p290mcpsimp"></a><a name="p290mcpsimp"></a>Spatial parameter for generating the color image filter. The actual value is color_flt_sgms/10.0. A larger value produces stronger filtering and a blurrier image. This parameter can be configured separately for high-frequency, mid-frequency, and low-frequency components of the color image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p292mcpsimp"><a name="p292mcpsimp"></a><a name="p292mcpsimp"></a>[1,50]</p>
</td>
</tr>
<tr id="row293mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p295mcpsimp"><a name="p295mcpsimp"></a><a name="p295mcpsimp"></a>color_flt_sgmr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p297mcpsimp"><a name="p297mcpsimp"></a><a name="p297mcpsimp"></a>Range-domain parameter for generating the color image filter. A larger value produces stronger filtering and a blurrier image. This parameter can be configured separately for high-frequency, mid-frequency, and low-frequency components of the color image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p299mcpsimp"><a name="p299mcpsimp"></a><a name="p299mcpsimp"></a>[1,255]</p>
</td>
</tr>
<tr id="row300mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>color_hf_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p304mcpsimp"><a name="p304mcpsimp"></a><a name="p304mcpsimp"></a>Enable signal for extracting high-frequency information from the color image. Only takes effect in the high-frequency layer of the color image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p306mcpsimp"><a name="p306mcpsimp"></a><a name="p306mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row307mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p309mcpsimp"><a name="p309mcpsimp"></a><a name="p309mcpsimp"></a>color_hf_gain</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p311mcpsimp"><a name="p311mcpsimp"></a><a name="p311mcpsimp"></a>Controls the high-frequency information overlay intensity of the color image. Takes effect only when color_hf_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p313mcpsimp"><a name="p313mcpsimp"></a><a name="p313mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row314mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>color_med_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>Enable signal for median filtering of the color image. Only takes effect in the high-frequency layer of the color image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p320mcpsimp"><a name="p320mcpsimp"></a><a name="p320mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row321mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p323mcpsimp"><a name="p323mcpsimp"></a><a name="p323mcpsimp"></a>Hist Proc</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.2 "><p id="p325mcpsimp"><a name="p325mcpsimp"></a><a name="p325mcpsimp"></a>hist_adj_en</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.3 "><p id="p327mcpsimp"><a name="p327mcpsimp"></a><a name="p327mcpsimp"></a>Histogram correction enable signal.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.4 "><p id="p329mcpsimp"><a name="p329mcpsimp"></a><a name="p329mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row330mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p332mcpsimp"><a name="p332mcpsimp"></a><a name="p332mcpsimp"></a>hist_adj_mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>Histogram correction mode.</p>
<p id="p335mcpsimp"><a name="p335mcpsimp"></a><a name="p335mcpsimp"></a>0: No correction;</p>
<p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>1: Correct the color image;</p>
<p id="p337mcpsimp"><a name="p337mcpsimp"></a><a name="p337mcpsimp"></a>2: Correct the IR image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p339mcpsimp"><a name="p339mcpsimp"></a><a name="p339mcpsimp"></a>[0,2]</p>
</td>
</tr>
<tr id="row340mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>hist_adj_str</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p344mcpsimp"><a name="p344mcpsimp"></a><a name="p344mcpsimp"></a>Histogram correction strength.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p346mcpsimp"><a name="p346mcpsimp"></a><a name="p346mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row347mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p349mcpsimp"><a name="p349mcpsimp"></a><a name="p349mcpsimp"></a>Detail Gain</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.2 "><p id="p351mcpsimp"><a name="p351mcpsimp"></a><a name="p351mcpsimp"></a>fusion_det_gain</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.3 "><p id="p353mcpsimp"><a name="p353mcpsimp"></a><a name="p353mcpsimp"></a>Global overlay intensity of IR image detail. The actual overlay intensity is fusion_det_gain/128. This parameter can be configured separately for high-frequency, mid-frequency, and low-frequency components of the IR image.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.4 "><p id="p355mcpsimp"><a name="p355mcpsimp"></a><a name="p355mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row356mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p358mcpsimp"><a name="p358mcpsimp"></a><a name="p358mcpsimp"></a>fusion_mono_det_adap_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p360mcpsimp"><a name="p360mcpsimp"></a><a name="p360mcpsimp"></a>Enable signal for adaptive adjustment of IR image detail overlay intensity. This parameter can be configured separately for high-frequency, mid-frequency, and low-frequency components of the image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p362mcpsimp"><a name="p362mcpsimp"></a><a name="p362mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row363mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p365mcpsimp"><a name="p365mcpsimp"></a><a name="p365mcpsimp"></a>fusion_mono_det_lut[33]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p367mcpsimp"><a name="p367mcpsimp"></a><a name="p367mcpsimp"></a>This lookup table adaptively adjusts the IR detail overlay intensity based on the difference in brightness between the IR image and the color image. The actual adjustment gain is fusion_mono_det_lut/128. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_mono_det_adap_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row370mcpsimp"><td class="cellrowborder" rowspan="12" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>Blending</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.2 "><p id="p374mcpsimp"><a name="p374mcpsimp"></a><a name="p374mcpsimp"></a>fusion_alpha_mode</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.3 "><p id="p1363171119513"><a name="p1363171119513"></a><a name="p1363171119513"></a>Blending mode for the brightness base layer of the color image and IR image.</p>
<p id="p1526251416520"><a name="p1526251416520"></a><a name="p1526251416520"></a>0: Global alpha blending;</p>
<p id="p376mcpsimp"><a name="p376mcpsimp"></a><a name="p376mcpsimp"></a>1: Adaptive alpha blending. This parameter can be configured separately for high-frequency, mid-frequency, and low-frequency components of the image.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.4 "><p id="p378mcpsimp"><a name="p378mcpsimp"></a><a name="p378mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row379mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p381mcpsimp"><a name="p381mcpsimp"></a><a name="p381mcpsimp"></a>fusion_global_alpha</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p383mcpsimp"><a name="p383mcpsimp"></a><a name="p383mcpsimp"></a>Global alpha value for blending the brightness base layer of the color image and IR image. fusion_global_alpha is the blending weight for the visible light brightness base layer, while (255 - fusion_global_alpha) is the blending weight for the IR brightness base layer. This parameter can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_alpha_mode=0.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p385mcpsimp"><a name="p385mcpsimp"></a><a name="p385mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row386mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>fusion_ratio_scale</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p390mcpsimp"><a name="p390mcpsimp"></a><a name="p390mcpsimp"></a>Scaling parameter for the brightness ratio between the IR image and the color image. The default value is 255. A smaller value produces a larger ratio. Takes effect only when fusion_alpha_mode=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p392mcpsimp"><a name="p392mcpsimp"></a><a name="p392mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row393mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p395mcpsimp"><a name="p395mcpsimp"></a><a name="p395mcpsimp"></a>fusion_ratio_bias_lut[9]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>Adaptively adjusts the brightness ratio value based on the brightness of the IR image. Larger values in the table produce a larger calculated brightness ratio. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_alpha_mode=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>[1,127]</p>
</td>
</tr>
<tr id="row400mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p402mcpsimp"><a name="p402mcpsimp"></a><a name="p402mcpsimp"></a>fusion_mono_ratio_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p404mcpsimp"><a name="p404mcpsimp"></a><a name="p404mcpsimp"></a>Enable signal for adaptively adjusting the brightness ratio based on the brightness of the IR image. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_alpha_mode=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p406mcpsimp"><a name="p406mcpsimp"></a><a name="p406mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row407mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p409mcpsimp"><a name="p409mcpsimp"></a><a name="p409mcpsimp"></a>fusion_mono_ratio_lut[33]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p411mcpsimp"><a name="p411mcpsimp"></a><a name="p411mcpsimp"></a>Controls the adjustment gain for the brightness ratio at different brightness levels based on the brightness of the IR image. The actual adjustment gain is fusion_mono_ratio_lut/128. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_mono_ratio_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p413mcpsimp"><a name="p413mcpsimp"></a><a name="p413mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row414mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p416mcpsimp"><a name="p416mcpsimp"></a><a name="p416mcpsimp"></a>fusion_mono_flat_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p418mcpsimp"><a name="p418mcpsimp"></a><a name="p418mcpsimp"></a>Enable signal for adaptively adjusting the brightness ratio based on the flatness of regions in the IR image. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_alpha_mode=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p420mcpsimp"><a name="p420mcpsimp"></a><a name="p420mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row421mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p423mcpsimp"><a name="p423mcpsimp"></a><a name="p423mcpsimp"></a>fusion_mono_flat_bias_lut[9]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p425mcpsimp"><a name="p425mcpsimp"></a><a name="p425mcpsimp"></a>Adaptively adjusts the brightness ratio value based on the flatness of regions in the IR image. Larger values in the table produce a larger calculated brightness ratio. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_mono_flat_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>[1,255]</p>
</td>
</tr>
<tr id="row428mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p430mcpsimp"><a name="p430mcpsimp"></a><a name="p430mcpsimp"></a>fusion_mono_flat_lut[33]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p432mcpsimp"><a name="p432mcpsimp"></a><a name="p432mcpsimp"></a>Lookup table for obtaining gain values based on the flatness of regions in the IR image, used to adjust the brightness ratio. The actual gain value is fusion_mono_flat_lut/8. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_mono_flat_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p434mcpsimp"><a name="p434mcpsimp"></a><a name="p434mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row435mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>fusion_color_ratio_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p439mcpsimp"><a name="p439mcpsimp"></a><a name="p439mcpsimp"></a>Enable signal for adaptively adjusting the brightness ratio based on the brightness of the color image. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_alpha_mode=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p441mcpsimp"><a name="p441mcpsimp"></a><a name="p441mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row442mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p444mcpsimp"><a name="p444mcpsimp"></a><a name="p444mcpsimp"></a>fusion_color_ratio_lut[33]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p446mcpsimp"><a name="p446mcpsimp"></a><a name="p446mcpsimp"></a>Controls the adjustment gain for the brightness ratio at different brightness levels based on the brightness of the color image. The actual adjustment gain is fusion_color_ratio_lut/128. Can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_color_ratio_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p448mcpsimp"><a name="p448mcpsimp"></a><a name="p448mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row449mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p451mcpsimp"><a name="p451mcpsimp"></a><a name="p451mcpsimp"></a>fusion_alpha_lut[33]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p453mcpsimp"><a name="p453mcpsimp"></a><a name="p453mcpsimp"></a>Uses the brightness ratio between the IR image and the color image to look up the fusion alpha value for blending their base layers. Larger values in the table give the IR image base layer a larger fusion weight alpha, and the color image base layer a smaller weight (255 - alpha). This lookup table can be configured separately for high-frequency, mid-frequency, and low-frequency components. Takes effect only when fusion_alpha_mode=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p455mcpsimp"><a name="p455mcpsimp"></a><a name="p455mcpsimp"></a>[0,255]</p>
</td>
</tr>
<tr id="row456mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p458mcpsimp"><a name="p458mcpsimp"></a><a name="p458mcpsimp"></a>Color Correct</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.2 "><p id="p460mcpsimp"><a name="p460mcpsimp"></a><a name="p460mcpsimp"></a>color_correct_en</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.3 "><p id="p462mcpsimp"><a name="p462mcpsimp"></a><a name="p462mcpsimp"></a>Color correction enable signal.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.4 "><p id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a>[0,1]</p>
</td>
</tr>
<tr id="row465mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>cc_uv_gain_lut[255]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>Color correction coefficient table. Applies gain to chrominance saturation based on the ratio between the brightness of the fused image and the brightness of the color image. The actual correction coefficient is cc_uv_gain_lut/128, meaning when the coefficient for a given ratio is 128, no adjustment to chrominance saturation is applied for that ratio. Takes effect only when color_correct_en=1.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p471mcpsimp"><a name="p471mcpsimp"></a><a name="p471mcpsimp"></a>[0,511]</p>
</td>
</tr>
<tr id="row472mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p474mcpsimp"><a name="p474mcpsimp"></a><a name="p474mcpsimp"></a>cc_thd_y</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><a name="ul476mcpsimp"></a><a name="ul476mcpsimp"></a><ul id="ul476mcpsimp"><li>When this parameter is from 1 to 127, if the brightness of the visible light image is below this threshold, the intensity of color correction is gradually reduced from the threshold down to brightness 0.</li><li>When this parameter is 0, the above function is disabled.</li></ul>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p480mcpsimp"><a name="p480mcpsimp"></a><a name="p480mcpsimp"></a>[0,127]</p>
</td>
</tr>
</tbody>
</table>

# Tuning Instructions
## MCF End-to-End Tuning Flowchart<a name="ZH-CN_TOPIC_0000002457840741"></a>

**Figure 1**  4K@30fps MCF end-to-end tuning flowchart<a name="fig498963145116"></a>  
![](figures/4K-30fps-MCF端到端调试流程图.png "4K-30fps-MCF端到端调试流程图")

**Figure 2**  4M@30fps MCF end-to-end tuning flowchart<a name="fig082311423517"></a>  
![](figures/4M-30fps-MCF端到端调试流程图.png "4M-30fps-MCF端到端调试流程图")
## ISP Basic Image Quality Tuning<a name="ZH-CN_TOPIC_0000002457840693"></a>

Under normal illumination, the visible light component is used predominantly or entirely, with little or no IR component fusion. The fusion intensity should be turned down, and ISP and 3DNR tuning is the same as for a single channel and is not described further in this document.

It is assumed here that the device has fill light or the mono sensor has good sensitivity — i.e., the IR channel gain is significantly lower than the color channel gain. Otherwise, due to variations in IR reflectance across different materials, there is no benefit to incorporating the IR channel.

When an IR fill light is present, the exposure levels of the IR and visible light channels differ considerably. Exposure metering is adjusted separately, and in principle, as much content as possible should be included. Because of the IR fill light, the visible light channel should use a blue filter to block IR components and reduce color cast in the visible light image.

In low-light environments, mono-color fusion is the primary approach. At this point, ISP and 3DNR need to be tuned together so that the images entering MCF contain sufficient content. Tuning is split into the IR channel (IR image) and the color channel.

### IR Channel<a name="ZH-CN_TOPIC_0000002424202090"></a>

1.  Demosaic must be enabled for the IR channel; otherwise, issues such as grid artifacts may appear. Other adjustments for sharpness and contrast are similar to those for ordinary images. Since IR images are prone to overexposure, LDCI and Dehaze modules can be used to appropriately increase highlight detail.
2.  Since the gain of the IR and color channels differs significantly, if a soft and natural fused image is desired, the high-frequency detail (edges) of the IR channel should not differ too much from that of the color channel. Detail should primarily be conveyed through the mid- and low-frequency components of the IR image. The high-frequency component should be roughly comparable to that of the color channel. If sharpness is the primary concern rather than naturalness, the results from step 1 may be used.
3.  Because many materials have vastly different reflective properties for IR and visible light, if the color representation of such materials (e.g., fabric, dyes, metal) is not a concern, use the results from step 1. If the overall color representation of objects is important, try to make the brightness distribution of the IR image as close as possible to that of the color image, so that the IR brightness information can be used more effectively.
4.  For the 4K@30fps MCF pipeline, due to overall VPSS performance constraints, the current IR channel cannot pass through VPSS 3DNR. When the IR channel noise is not severe, or when softness and naturalness of the fused image are not critical, BayerNR temporal filtering is used to suppress noise, and the luma denoising of 3DNR after fusion is tuned to suppress graininess in static and flat regions. For the 4M@30fps MCF pipeline, the current IR channel can pass through VPSS 3DNR, and both BayerNR and 3DNR can be used jointly for denoising.

### Color Channel<a name="ZH-CN_TOPIC_0000002424361870"></a>

**Sharpness<a name="section1711111269321"></a>**

Since fine textures and mid-to-high-frequency details are primarily supplemented by the IR channel, the color channel should avoid methods that enhance high-frequency noise, such as Demosaic's nddm_mf_detail_strength, nddm_hf_detail_strength, Sharpen's texture_freq, and the last point of texturestr — all of these values should be set as small as possible. LDCI and DRC should be appropriately reduced based on actual noise conditions, balancing contrast and noise. For BayerNR tuning, the key parameters to focus on are user_define_md, user_define_slope, user_define_dark_thresh, and user_define_color_thresh. Note that user_define_md for the color channel must be kept always on; otherwise, the motion/static judgment for the color image will be abnormal. Currently, the motion/static judgment of BayerNR for the color channel needs to reference information from the IR channel, which mitigates inaccurate motion/static judgment caused by excessive noise in the color channel itself under extremely low light. Some object edges in the IR channel may not be visible due to overexposure or reflectance issues; in such cases, the edges from the color channel must be used, so the color channel also needs relatively strong edge representation. For this, it is recommended to set Demosaic's nddm_strength to around 32 to avoid grid noise while adequately representing edge strength and noise. For Sharpen, reduce texture_freq (recommended below 100), set the last point of texturestr below 128, and set edge_filt_strength to 63, so that objects are enhanced as edges rather than textures, avoiding a significant increase in noise. Sharpen's detail_ctrl can be moderately reduced, with the judgment criterion being that edge sharpness remains acceptable. To minimize noise as much as possible, 3DNR tuning here needs to coordinate with BayerNR. Currently, both BayerNR and 3DNR include temporal processing; BayerNR's temporal processing can be used preferentially, with 3DNR's temporal processing serving as auxiliary.

**Color Dimension<a name="section191131126193210"></a>**

Since the fused image must still maintain a certain level of color saturation while color noise is also significant, some processing is required. First, adjust AWB: if an accurate light source correction is needed, no special handling is required; otherwise, the light source color can be partially retained to reduce the pronounced color noise that occurs at low color temperatures. In the CCM, appropriately reduce the coefficients of the red and blue components — i.e., reduce the main R and B coefficients. The CA module should be enabled as much as possible to reduce saturation in dark areas and increase saturation in bright areas. CLUT can be used, following a principle similar to CA: preserve color in high-SNR areas and reduce saturation of low-SNR colors. The recommended tuning for chroma denoising in 3DNR is: for the nr_c0 level, set sfc to 31 and tfc to 31 to suppress flickering chroma noise; for the nr_c1 level, set both the foreground and background sfn to 7, with the difference being that the foreground's sf7 hybrid filter tends toward filter 5 while the background's sf7 hybrid filter tends toward filter 6. Note that filter 5 removes chroma noise but also causes some loss of normal color, which involves a trade-off. Specific parameters are shown in [Figure 1](#fig13993142443410).

**Figure 1**  Recommended parameters for color channel 3DNR chroma noise tuning<a name="fig13993142443410"></a>  
![](figures/彩色路3DNR色噪调试建议参数图.png "彩色路3DNR色噪调试建议参数图")

After tuning the color channel, the overall result is shown in [Figure 2](#fig9166426103219).

**Figure 2**  Color channel tuning result<a name="fig9166426103219"></a>  
![](figures/彩色通路调优效果图.png "彩色通路调优效果图")

**Contrast<a name="section1120026183211"></a>**

Gamma, LDCI, and Dehaze can be adjusted based on the actual application, similar to ordinary low-light tuning methods. The main concern is balancing dark-area noise. Additionally, with the assistance of the IR channel, try to minimize the contrast difference between the visible light channel and the IR channel.

## Mono-Color Fusion Adjustment<a name="ZH-CN_TOPIC_0000002457840725"></a>

-   Adjust the color image base layer independently
    -   Control the filtering strength of the visible light brightness by adjusting the filter radius color_flt_radius and the filter coefficient control parameters color_flt_sgms and color_flt_sgmr. Larger radius values and larger control parameter values produce stronger filtering and a blurrier base layer.
    -   The color image has separate base layers for high-frequency, mid-frequency, and low-frequency components, and the above parameters can be adjusted independently for each.

-   Adjust the IR image base layer and detail layer independently
    -   Control the filtering strength by adjusting the filter radius mono_flt_radius. A larger radius produces an overall blurrier base layer and a stronger detail layer, making details more pronounced and coarser.
    -   The lookup table mono_flt_bias_lut[9] controls the detail intensity at different brightness levels. Larger values in the table produce stronger detail at the corresponding brightness. The lookup table has only 9 values, which corresponds to dividing the pixel brightness value range (e.g., [0,255]) into 8 equal segments, with linear interpolation yielding the detail intensity at any brightness. Greater intensity makes details more pronounced and coarser.
    -   The IR image has separate base layers and detail layers for high-frequency, mid-frequency, and low-frequency components, and the above parameters can be adjusted independently for each.

-   Adjust the IR image detail overlay intensity
    -   The IR image detail overlay supports adjustable global intensity via the fusion_det_gain parameter. A fusion_det_gain of 128 means the detail layer is directly overlaid without any gain adjustment to the overlay intensity.
    -   The IR image detail overlay supports adjustable adaptive intensity. Setting fusion_mono_det_adap_en to 1 enables the adaptive adjustment function. The lookup table fusion_mono_det_lut[33] contains 33 gain values, which corresponds to dividing the value range of the pixel brightness difference between the IR image and the color image into 32 equal segments, with linear interpolation yielding the detail overlay intensity gain for any brightness difference.
    -   The IR image has separate detail layers for high-frequency, mid-frequency, and low-frequency components, and the above parameters can be adjusted independently for each.

-   Adjust the base layer blending weight of the color image and IR image
    -   When fusion_alpha_mode is 0, the base layers of the color image and IR image use global alpha blending mode. The parameter fusion_global_alpha sets the global blending weight of the color image base layer, while the IR image base layer weight is (255 - fusion_global_alpha). The default value of this parameter is 255. If set too low, the overall color appearance may be affected due to excessive blending of the IR image base component.
    -   When fusion_alpha_mode is 1, the base layers of the color image and IR image use adaptive alpha blending mode, where the fusion alpha value is adaptively calculated based on the brightness ratio Ry between the IR image and the color image.
    -   The lookup table fusion_ratio_bias_lut[9] adjusts the brightness ratio Ry based on the brightness of the IR image. Larger values in the table produce a larger calculated brightness ratio. The lookup table fusion_ratio_bias_lut[9] has 9 offset values, which corresponds to dividing the IR image brightness value range into 8 equal segments, with linear interpolation yielding the offset value at any brightness.
    -   When fusion_mono_flat_en is 1, the lookup table fusion_mono_flat_bias_lut[9] is used to adjust the brightness ratio Ry based on the flatness of regions in the IR image. Larger values in the table produce a larger calculated brightness ratio. The lookup table fusion_mono_flat_bias_lut[9] has 9 offset values, which corresponds to dividing the IR image region flatness value range into 8 equal segments, with linear interpolation yielding the offset value at any flatness. Additionally, the lookup table fusion_mono_flat_lut[33] can be used to apply gain control to the brightness ratio Ry based on the flatness of regions in the IR image. The table has 33 gain values, which corresponds to dividing the IR image region flatness value range into 32 equal segments, with linear interpolation yielding the gain value at any flatness.
    -   When fusion_mono_ratio_en is 1, the lookup table fusion_mono_ratio_lut[33] is used to apply gain control to the brightness ratio Ry based on the brightness of the IR image. The table has 33 gain values, which corresponds to dividing the IR image brightness value range into 32 equal segments, with linear interpolation yielding the gain value at any brightness.
    -   When fusion_color_ratio_en is 1, the lookup table fusion_color_ratio_lut[33] is used to apply gain control to the brightness ratio Ry based on the brightness of the color image. The table has 33 gain values, which corresponds to dividing the color image brightness value range into 32 equal segments, with linear interpolation yielding the gain value at any brightness.
    -   Based on the Ry value adjusted by the above offset and gain values, the fusion alpha value for the IR image and color image is obtained via lookup table. The lookup table fusion_alpha_lut[33] has 33 weight values, which corresponds to dividing the Ry value range into 32 equal segments, with linear interpolation yielding the IR image fusion alpha for any Ry. The color image fusion weight is then (255 - alpha).
    -   The above parameters can be adjusted independently for high-frequency, mid-frequency, and low-frequency bands.

-   Adjust the color of the fused image
    -   When color_correct_en is 1, the color correction function is enabled. cc_uv_gain_lut[255] is the color correction coefficient table that applies gain processing to the chrominance saturation of the image based on the ratio between the brightness of the fused image and the brightness of the color image. The brightness ratio range before and after fusion is 0-255, and the actual saturation gain is cc_uv_gain_lut/128.
    -   To avoid amplifying the saturation of chroma noise in low light, cc_thd_y can be set. When the brightness of the color image is below the threshold cc_thd_y, the degree of chrominance saturation compensation is gradually reduced from the threshold down to brightness 0.

        **Figure 1**  MCF tuning style example<a name="fig2192183017464"></a>  
        ![](figures/MCF调试风格示例图.png "MCF调试风格示例图")
## Post-Fusion 3DNR Adjustment<a name="ZH-CN_TOPIC_0000002424361910"></a>

The purpose of passing the fused output through VPSS 3DNR is primarily to remove chroma noise caused by the uvgain curve in the MCF module boosting overall color saturation, as well as to remove graininess in static and moving regions caused by the IR image not having passed through 3DNR. The tuning method is the same as for color images.

# Calibration
## Calibration Environment and Method<a name="ZH-CN_TOPIC_0000002424361950"></a>

### Purpose and Method of Calibration<a name="ZH-CN_TOPIC_0000002424202066"></a>

The purpose of calibration is to estimate the external parameters of the lenses, i.e., the relative position between the dual lenses / dual sensors and the overlapping effective region between the dual lenses / dual sensors. The algorithm will use the external parameters obtained from calibration to align the two images, facilitating subsequent dual-channel fusion processing.

Calibration is based on global registration, so for a dual-lens structure, it cannot resolve parallax issues for different depths within the same scene. Therefore, the distance of interest for the device must be determined in advance. After calibration and registration, the parallax between the two images at the distance of interest and its vicinity will be relatively small.

During calibration, assuming the distance of interest is 5 meters, position the device 5 meters from the calibration scene, directly facing the center of the calibration scene, and capture images from both channels simultaneously.

### Calibration Environment Requirements<a name="ZH-CN_TOPIC_0000002424202026"></a>

The fields of view of the two lenses should be similar. Before calibration, it is necessary to subjectively confirm that the framing of the two channels is roughly equivalent.

The ambient light must be sufficient and uniform, ensuring that the captured dual-channel images have no obvious noise, no reflections, and small differences in brightness/contrast; otherwise, global registration may fail.

The calibration scene does not require a special pattern, but it must have very rich details to ensure that the scene contains sufficiently abundant and distinct feature points; otherwise, global registration may fail.

The calibration scene should be as planar as possible, such as a poster with rich detail, or it can be a real scene, but the real scene should not contain too much depth.

During calibration, avoid moving objects or changing light in the scene to prevent motion from affecting calibration.

In the dual-channel images captured for calibration, the calibration scene should fill the entire frame.

A reference diagram of the calibration scene is provided below. See [Figure 1](#_fig26861861) for details.

**Figure 1**  Recommended MCF calibration scene example<a name="_fig26861861"></a>  
![](figures/MCF标定场景推荐示例图.png "MCF标定场景推荐示例图")
>![](public_sys-resources/icon-note.gif) **Note:** 
>MCF calibration uses GDC for both FOV correction and stabilization. Enabling FOV correction along with two or more channels of gyroscope stabilization may cause insufficient performance.

## Using the Calibration Library<a name="ZH-CN_TOPIC_0000002457840713"></a>

### Function Interface Description<a name="ZH-CN_TOPIC_0000002457880833"></a>

Please refer to the *Mono-Color Fusion Development Reference*.

### Usage Instructions<a name="ZH-CN_TOPIC_0000002424361858"></a>

1.  Enter the code path: ./sample/mcf/
2.  Execute ./sample_mcf 0
3.  The calibration results are output as follows:

    ```
    show matrix of calbration: 
    1052905,         657,   -13045049, 
    -2007,     1051702,    11698003, 
    1,           0,    1048576, 
    show crop region of calibration： 
    x:16,  y:0,  width:1904,  height:1056 
    num of refer feature:   968 
    num of register feature: 771 
    num of match feature:  100
    ```

4.  These are the lens correction matrix and the overlapping effective region between the dual lenses / dual sensors, respectively, along with the feature point information returned by calibration, including the reference image, the image to be corrected, and the number of matched feature points.

### Usage Restrictions<a name="ZH-CN_TOPIC_0000002424361922"></a>

The resolution of the input images for the calibration function must not exceed 4096*2160. The two input images must be the same size. Additionally, the image width, height, stride, and the ROI (image top, bottom, left, right crop widths) must be 8-aligned.

Examples are provided below.

1.  If the actual resolution is 4096x2160, downsample both calibration images by a factor of 4 horizontally and 4 vertically to obtain two calibration images at 1024x540 resolution.
2.  Use the two 1024x540 calibration images as input to the calibration library, configure the input resolution as 1024x540, and run the calibration library program.
3.  Process the obtained calibration parameters.

    If the calibrated matrix coefficients are:

    ![](figures/zh-cn_formulaimage_0000002424202430.png)

    Then the matrix coefficients actually used for correction are modified to:

    ![](figures/zh-cn_formulaimage_0000002424362262.png)

    If the calibrated effective region parameters are [x, y, w, h], then the effective region parameters actually used for correction are modified to [x*4, y*4, w*4, h*4].

    Here, 4 is the horizontal and vertical downsampling factor of the image.

# Tuning Methods for Common Issues
## Color Image Smearing in Extremely Low Light<a name="ZH-CN_TOPIC_0000002457880769"></a>

-   Verify that the motion/static judgment thresholds for the IR image are tuned properly — i.e., motion regions should be processed primarily in the spatial domain to prevent smearing in the IR image.
-   Verify that the color channel is using Bayer3D in user-defined mode — i.e., the tuning parameters user_define_md, user_define_slope, user_define_dark_thresh, and user_define_color_thresh are configured.
-   Verify that the temporal parameters of 3DNR for the color channel image (e.g., tfs, math) are reasonable, with the criterion being that no large-grain rain-like noise is produced, to avoid motion smearing in the color image under extremely low light caused by improper 3DNR temporal parameter tuning.
-   When the color channel uses both HNR and BNR modules, ensure that MCF preprocessing is used first — i.e., ot_mcf_vi_attr's enable is true. At this point, when HNR is in advance mode, HNR and BNR modules operate in parallel without fusion processing. In this case, BNR's motion/static judgment is affected by parameters such as user_define_md, user_define_slope, user_define_dark_thresh, and user_define_color_thresh.

## Large Brightness Difference Between IR and Color Images Causing Abnormal Fusion<a name="ZH-CN_TOPIC_0000002457880821"></a>

-   Verify that the IR image exposure is reasonable. Since the sharpness of the fused image comes from the IR image, the exposure time of the visible light image can be appropriately limited to improve the sharpness of moving objects.
-   Verify that the brightness of the color image is reasonable. If the color image brightness is insufficient, IspDgain can be appropriately compensated, but note that under extremely low light, using too much IspDgain will introduce chroma noise in the color image that is difficult to remove.

## Blur and Noise Artifacts in Motion Regions After Fusion<a name="ZH-CN_TOPIC_0000002457880809"></a>

-   Verify the performance of the color image and IR image in motion regions. Blur, noise, and similar issues should primarily originate from the color image. Try to ensure good performance of the IR image in motion regions.
-   In global alpha blending mode, reduce the value of fusion_global_alpha; or in adaptive alpha blending mode, increase the values of the fusion_alpha_lut[33] curve to raise the fusion weight of the IR image and improve the fused image quality. However, the color performance of the fused image will degrade and needs to be weighed as needed.

## Color Cast After Fusion<a name="ZH-CN_TOPIC_0000002457880845"></a>

-   Since the brightness and contrast distributions of the color image and IR image differ greatly, if the IR image information accounts for a large proportion after fusion, it will significantly affect the color performance of the fused image, causing issues such as color cast and reduced saturation. The front-end ISP pipeline must be tuned to ensure that the color channel and IR channel are as close as possible in terms of brightness and contrast performance.
-   Verify that color_correct_en is set to 1 and adjust the cc_uv_gain_lut[255] curve as needed. Note that higher curve values produce stronger color saturation compensation, but will also make chroma noise more pronounced — a trade-off is required.
-   To suppress chroma noise in dark areas, reduce the color saturation compensation for dark areas by setting the threshold cc_thd_y to lower the saturation compensation intensity in brightness regions below cc_thd_y.

## Poor License Plate Performance After Fusion<a name="ZH-CN_TOPIC_0000002424202102"></a>

-   Verify that the license plate performance in the color image is normal. ISP color channel tuning should ensure that the color and sharpness of license plates in the color image are normal.
-   Verify the license plate performance in the IR image. Through ISP IR channel tuning, make the IR license plate overexposed or nearly overexposed.
-   When the IR license plate is overexposed or nearly overexposed, verify that the fusion_mono_ratio_en parameter is set to 1. Based on the degree of IR license plate overexposure, adjust the lookup table fusion_mono_ratio_lut[33]. This lookup table is generally set in a decreasing form, rapidly reducing the corresponding lookup table value to 0 near the highlight value of the IR license plate.
-   Note that in non-traffic-capture scenarios, such as nighttime black-light scenarios, the color exposure time approaches 40 ms while the IR exposure is only around 10 ms. In such cases, the IR image cannot precisely control overexposed regions. Setting fusion_mono_ratio_en to 1 often forces the IR image to select the color image in overexposed regions, but the color image brightness is typically quite dark, resulting in image layering issues. In this case, it is recommended to set fusion_mono_ratio_en to 0 to avoid image layering.

## Poor Calibration Results<a name="ZH-CN_TOPIC_0000002457840669"></a>

-   Check whether the calibration environment is appropriate.
-   For dual-lens structures, parallax issues inherently exist and cannot be resolved by global registration-based calibration algorithms. In such cases, a region of interest (e.g., the center of the frame) can be set, and the calibration algorithm will prioritize calibration quality in that region. For dual-lens structures, the projective projection mode is recommended.
-   For beam-splitter structures, parallax theoretically does not exist. A region of interest can be set as needed, and the affine projection mode is recommended.
