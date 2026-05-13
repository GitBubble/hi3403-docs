---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/IVS API参考/IVS API参考.md
--- # Preface
**Overview<a name="section122282764510"></a>** This document is written for programmers developing recognition analysis solutions using IVS. It is intended to provide reference information supported by IVS during development, including AP Is, header files, error codes, etc. **Product Version<a name="section12318719459"></a>** The product versions corresponding to this document are as follows. <a name="table1324247124515"></a>
<table><thead align="left"><tr id="row8283167154518"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p1728315720455"><a name="p1728315720455"></a><a name="p1728315720455"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p92831478451"><a name="p92831478451"></a><a name="p92831478451"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row628310712459"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p628411716459"><a name="p628411716459"></a><a name="p628411716459"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p152841577456"><a name="p152841577456"></a><a name="p152841577456"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Intended Audience<a name="section1924037154519"></a>** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions<a name="section133020216410"></a>** The following symbols may appear in this document, and their meanings are described below. <a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002441733537.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section2467512116410"></a>** <a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First interim version release</p>
</td>
</tr>
</tbody>
</table> # Overview
## Overview<a name="ZH-CN_TOPIC_0000002408134140"></a> IVS (Intelligent Video Surveillance) is a higher-level recognition video capture application API compared to IVE (Intelligent Video Engine). Users can quickly develop related recognition applications based on IVS. The recognition applications currently supported by IVS include: MD (Motion Detection). # MD
## Functional Description<a name="ZH-CN_TOPIC_0000002441733317"></a> ### Motion Detection<a name="ZH-CN_TOPIC_0000002408134128"></a> Motion detection detects the motion state of a video by detecting changes in video brightness, producing video detection analysis results. #### Basic Concepts<a name="ZH-CN_TOPIC_0000002408294084"></a> - MD Algorithm The MD algorithm includes two types: frame difference method (MD\_ALG\_MODE\_REF) and background method (MD\_ALG\_MODE\_BG). - Frame Difference Method (MD\_ALG\_MODE\_REF) An algorithm that directly uses the user-specified image as a reference frame to produce video detection analysis results is called the frame difference method. - Background Method (MD\_ALG\_MODE\_BG) During MD processing, a background image of the current video is generated. An algorithm that then uses the background image as a reference frame to produce video detection analysis results is called the background method. - Background Update Weight When the MD algorithm is set to the background method, each MD process generates a static partial image. This partial image and the background undergo a pixel value overlay. New background = (static partial image overlay weight x static partial image + dynamic partial image overlay weight y old background) >> 16. >![](public_sys-resources/icon-notice.gif) **Caution:**
>If using a 64-bit operating system, the MMZ address used must be within a 4 GB space, otherwise exceptions may occur. ## API Reference<a name="ZH-CN_TOPIC_0000002441733361"></a> The MD API provides basic interfaces for initialization, exit, handle acquisition, handle release, background acquisition, and detection processing. This functional module provides the following AP Is: - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309): Initialization.
- [ss\_ivs\_md\_exit](#ZH-CN_TOPIC_0000002408134148): Exit.
- [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333): Creates an MD channel.
- [ss\_ivs\_md\_destroy\_chn](#ZH-CN_TOPIC_0000002441853505): Destroys an MD channel.
- [ss\_ivs\_md\_set\_chn\_attr](#ZH-CN_TOPIC_0000002408294068): Sets MD channel attributes.
- [ss\_ivs\_md\_get\_chn\_attr](#ZH-CN_TOPIC_0000002408294052): Gets MD channel attributes.
- [ss\_ivs\_md\_get\_bg](#ZH-CN_TOPIC_0000002408134192): Gets the background.
- [ss\_ivs\_md\_proc](#ZH-CN_TOPIC_0000002441733297): Detection processing. ### ss\_ivs\_md\_init<a name="ZH-CN_TOPIC_0000002441733309"></a> [Description] Initializes motion detection. [Syntax] ```
td_s32 ss_ivs_md_init(td_void)；
``` [Parameters] None. [Return Values] <a name="table288mcpsimp"></a>
<table><thead align="left"><tr id="row293mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p295mcpsimp"><a name="p295mcpsimp"></a><a name="p295mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p297mcpsimp"><a name="p297mcpsimp"></a><a name="p297mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row299mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p301mcpsimp"><a name="p301mcpsimp"></a><a name="p301mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p303mcpsimp"><a name="p303mcpsimp"></a><a name="p303mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row304mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p306mcpsimp"><a name="p306mcpsimp"></a><a name="p306mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p308mcpsimp"><a name="p308mcpsimp"></a><a name="p308mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph311mcpsimp"><a name="ph311mcpsimp"></a><a name="ph311mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - Before calling other MD interfaces, this interface must be called first for initialization, and it only needs to be called once. Otherwise, an error is returned.
- This interface must be used together with [ss\_ivs\_md\_exit](#ZH-CN_TOPIC_0000002408134148). [Example] None. [Related Topics] [ss\_ivs\_md\_exit](#ss_ivs_md_exit) ### ss\_ivs\_md\_exit<a name="ZH-CN_TOPIC_0000002408134148"></a> [Description] Exits motion detection. [Syntax] ```
td_s32 ss_ivs_md_exit(td_void);
``` [Parameters] None. [Return Values] <a name="table333mcpsimp"></a>
<table><thead align="left"><tr id="row338mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p340mcpsimp"><a name="p340mcpsimp"></a><a name="p340mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row344mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p346mcpsimp"><a name="p346mcpsimp"></a><a name="p346mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p348mcpsimp"><a name="p348mcpsimp"></a><a name="p348mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row349mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p351mcpsimp"><a name="p351mcpsimp"></a><a name="p351mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p353mcpsimp"><a name="p353mcpsimp"></a><a name="p353mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph356mcpsimp"><a name="ph356mcpsimp"></a><a name="ph356mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization before calling this interface to exit. Otherwise, an error is returned. [Example] None. [Related Topics] [ss\_ivs\_md\_init](#ss_ivs_md_init) ### ss\_ivs\_md\_create\_chn<a name="ZH-CN_TOPIC_0000002441733333"></a> [Description] Creates an MD channel. [Syntax] ```
td_s32 ss_ivs_md_create_chn(ot_md_chn md_chn, ot_md_attr *md_attr);
``` [Parameters] <a name="table376mcpsimp"></a>
<table><thead align="left"><tr id="row382mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.4.1.2"><p id="p386mcpsimp"><a name="p386mcpsimp"></a><a name="p386mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.3"><p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row390mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p392mcpsimp"><a name="p392mcpsimp"></a><a name="p392mcpsimp"></a>md_chn</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p394mcpsimp"><a name="p394mcpsimp"></a><a name="p394mcpsimp"></a>Channel number. Valid range: [0, 63]</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p396mcpsimp"><a name="p396mcpsimp"></a><a name="p396mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row397mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>md_attr</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>Channel information pointer.</p>
<p id="p402mcpsimp"><a name="p402mcpsimp"></a><a name="p402mcpsimp"></a>Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p404mcpsimp"><a name="p404mcpsimp"></a><a name="p404mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> [Return Values] <a name="table406mcpsimp"></a>
<table><thead align="left"><tr id="row411mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p413mcpsimp"><a name="p413mcpsimp"></a><a name="p413mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p415mcpsimp"><a name="p415mcpsimp"></a><a name="p415mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row417mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p419mcpsimp"><a name="p419mcpsimp"></a><a name="p419mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p421mcpsimp"><a name="p421mcpsimp"></a><a name="p421mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row422mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p424mcpsimp"><a name="p424mcpsimp"></a><a name="p424mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p426mcpsimp"><a name="p426mcpsimp"></a><a name="p426mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph429mcpsimp"><a name="ph429mcpsimp"></a><a name="ph429mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_chn\_attr](#ss_ivs_md_get_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_destroy\_chn<a name="ZH-CN_TOPIC_0000002441853505"></a> [Description] Destroys an MD channel. [Syntax] ```
td_s32 ss_ivs_md_destroy_chn(ot_md_chn md_chn);
``` [Parameters] <a name="table457mcpsimp"></a>
<table><thead align="left"><tr id="row463mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p465mcpsimp"><a name="p465mcpsimp"></a><a name="p465mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.4.1.2"><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.3"><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row471mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p473mcpsimp"><a name="p473mcpsimp"></a><a name="p473mcpsimp"></a>md_chn</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p475mcpsimp"><a name="p475mcpsimp"></a><a name="p475mcpsimp"></a>Channel number. Valid range: [0, 63]</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p477mcpsimp"><a name="p477mcpsimp"></a><a name="p477mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> [Return Values] <a name="table479mcpsimp"></a>
<table><thead align="left"><tr id="row484mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p486mcpsimp"><a name="p486mcpsimp"></a><a name="p486mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p488mcpsimp"><a name="p488mcpsimp"></a><a name="p488mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row490mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p492mcpsimp"><a name="p492mcpsimp"></a><a name="p492mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p494mcpsimp"><a name="p494mcpsimp"></a><a name="p494mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row495mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p499mcpsimp"><a name="p499mcpsimp"></a><a name="p499mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph502mcpsimp"><a name="ph502mcpsimp"></a><a name="ph502mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_chn\_attr](#ss_ivs_md_get_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_set\_chn\_attr<a name="ZH-CN_TOPIC_0000002408294068"></a> [Description] Sets MD channel attributes. [Syntax] ```
td_s32 ss_ivs_md_set_chn_attr(ot_md_chn md_chn, ot_md_attr *md_attr);
``` [Parameters] <a name="table534mcpsimp"></a>
<table><thead align="left"><tr id="row540mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.4.1.2"><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.3"><p id="p546mcpsimp"><a name="p546mcpsimp"></a><a name="p546mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row548mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p550mcpsimp"><a name="p550mcpsimp"></a><a name="p550mcpsimp"></a>md_chn</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p552mcpsimp"><a name="p552mcpsimp"></a><a name="p552mcpsimp"></a>Channel number. Valid range: [0, 63]</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p554mcpsimp"><a name="p554mcpsimp"></a><a name="p554mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row555mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>md_attr</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p559mcpsimp"><a name="p559mcpsimp"></a><a name="p559mcpsimp"></a>Channel information pointer.</p>
<p id="p560mcpsimp"><a name="p560mcpsimp"></a><a name="p560mcpsimp"></a>Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p562mcpsimp"><a name="p562mcpsimp"></a><a name="p562mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> [Return Values] <a name="table564mcpsimp"></a>
<table><thead align="left"><tr id="row569mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p571mcpsimp"><a name="p571mcpsimp"></a><a name="p571mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p573mcpsimp"><a name="p573mcpsimp"></a><a name="p573mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row575mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p577mcpsimp"><a name="p577mcpsimp"></a><a name="p577mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p579mcpsimp"><a name="p579mcpsimp"></a><a name="p579mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row580mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p582mcpsimp"><a name="p582mcpsimp"></a><a name="p582mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p584mcpsimp"><a name="p584mcpsimp"></a><a name="p584mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph587mcpsimp"><a name="ph587mcpsimp"></a><a name="ph587mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned.
- Static channel attributes (alg\_mode, sad\_mode, width, height) cannot be changed; they must match the values used when the channel was created. Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_get\_chn\_attr](#ss_ivs_md_get_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_get\_chn\_attr<a name="ZH-CN_TOPIC_0000002408294052"></a> [Description] Gets MD channel attributes. [Syntax] ```
td_s32 ss_ivs_md_get_chn_attr(ot_md_chn md_chn, ot_md_attr *md_attr);
``` [Parameters] <a name="table620mcpsimp"></a>
<table><thead align="left"><tr id="row626mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p628mcpsimp"><a name="p628mcpsimp"></a><a name="p628mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.4.1.2"><p id="p630mcpsimp"><a name="p630mcpsimp"></a><a name="p630mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.3"><p id="p632mcpsimp"><a name="p632mcpsimp"></a><a name="p632mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row634mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p636mcpsimp"><a name="p636mcpsimp"></a><a name="p636mcpsimp"></a>md_chn</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>Channel number. Valid range: [0, 63]</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row641mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>md_attr</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>Channel information pointer.</p>
<p id="p646mcpsimp"><a name="p646mcpsimp"></a><a name="p646mcpsimp"></a>Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.3 "><p id="p648mcpsimp"><a name="p648mcpsimp"></a><a name="p648mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table> [Return Values] <a name="table650mcpsimp"></a>
<table><thead align="left"><tr id="row655mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row661mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p663mcpsimp"><a name="p663mcpsimp"></a><a name="p663mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p665mcpsimp"><a name="p665mcpsimp"></a><a name="p665mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row666mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p670mcpsimp"><a name="p670mcpsimp"></a><a name="p670mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph673mcpsimp"><a name="ph673mcpsimp"></a><a name="ph673mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_get\_bg<a name="ZH-CN_TOPIC_0000002408134192"></a> [Description] Gets the motion detection background. [Syntax] ```
td_s32 ss_ivs_md_get_bg(ot_md_chn md_chn, ot_svp_dst_img *bg);
``` [Parameters] <a name="table704mcpsimp"></a>
<table><thead align="left"><tr id="row710mcpsimp"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.1"><p id="p712mcpsimp"><a name="p712mcpsimp"></a><a name="p712mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.4.1.2"><p id="p714mcpsimp"><a name="p714mcpsimp"></a><a name="p714mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p716mcpsimp"><a name="p716mcpsimp"></a><a name="p716mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row718mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.1 "><p id="p720mcpsimp"><a name="p720mcpsimp"></a><a name="p720mcpsimp"></a>md_chn</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.4.1.2 "><p id="p722mcpsimp"><a name="p722mcpsimp"></a><a name="p722mcpsimp"></a>Channel number. Valid range: [0, 63]</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p724mcpsimp"><a name="p724mcpsimp"></a><a name="p724mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> <a name="table733mcpsimp"></a>
<table><thead align="left"><tr id="row740mcpsimp"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.1"><p id="p742mcpsimp"><a name="p742mcpsimp"></a><a name="p742mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.1.5.1.2"><p id="p744mcpsimp"><a name="p744mcpsimp"></a><a name="p744mcpsimp"></a>Supported Image Type</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p746mcpsimp"><a name="p746mcpsimp"></a><a name="p746mcpsimp"></a>Address Alignment</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.5.1.4"><p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>Resolution</p>
</th>
</tr>
</thead>
<tbody><tr id="row750mcpsimp"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p752mcpsimp"><a name="p752mcpsimp"></a><a name="p752mcpsimp"></a>bg</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.5.1.2 "><p id="p754mcpsimp"><a name="p754mcpsimp"></a><a name="p754mcpsimp"></a>OT_SVP_IMG_TYPE_U8C1</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p756mcpsimp"><a name="p756mcpsimp"></a><a name="p756mcpsimp"></a>16 byte</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.5.1.4 "><p id="p758mcpsimp"><a name="p758mcpsimp"></a><a name="p758mcpsimp"></a>64x64 to 1920x1080</p>
</td>
</tr>
</tbody>
</table> [Return Values] <a name="table760mcpsimp"></a>
<table><thead align="left"><tr id="row765mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p767mcpsimp"><a name="p767mcpsimp"></a><a name="p767mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p769mcpsimp"><a name="p769mcpsimp"></a><a name="p769mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row771mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p773mcpsimp"><a name="p773mcpsimp"></a><a name="p773mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p775mcpsimp"><a name="p775mcpsimp"></a><a name="p775mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row776mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p778mcpsimp"><a name="p778mcpsimp"></a><a name="p778mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p780mcpsimp"><a name="p780mcpsimp"></a><a name="p780mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph783mcpsimp"><a name="ph783mcpsimp"></a><a name="ph783mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned.
- Background data can only be retrieved when using the background method. Otherwise, an error is returned. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_proc](#ss_ivs_md_proc) ### ss\_ivs\_md\_proc<a name="ZH-CN_TOPIC_0000002441733297"></a> [Description] Motion detection processing. [Syntax] ```
td_s32 ss_ivs_md_proc(ot_md_chn md_chn, ot_svp_src_img *cur, ot_svp_src_img *ref, ot_svp_dst_img *sad, ot_svp_dst_mem_info *blob)；
``` [Parameters] <a name="table815mcpsimp"></a>
<table><thead align="left"><tr id="row821mcpsimp"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.4.1.1"><p id="p823mcpsimp"><a name="p823mcpsimp"></a><a name="p823mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.4.1.2"><p id="p825mcpsimp"><a name="p825mcpsimp"></a><a name="p825mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.4.1.3"><p id="p827mcpsimp"><a name="p827mcpsimp"></a><a name="p827mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row829mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p831mcpsimp"><a name="p831mcpsimp"></a><a name="p831mcpsimp"></a>md_chn</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.4.1.2 "><p id="p833mcpsimp"><a name="p833mcpsimp"></a><a name="p833mcpsimp"></a>Channel number. Valid range: [0, 63]</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p835mcpsimp"><a name="p835mcpsimp"></a><a name="p835mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row836mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p838mcpsimp"><a name="p838mcpsimp"></a><a name="p838mcpsimp"></a>cur</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.4.1.2 "><p id="p840mcpsimp"><a name="p840mcpsimp"></a><a name="p840mcpsimp"></a>Current frame image pointer; must not be NULL.</p>
<p id="p841mcpsimp"><a name="p841mcpsimp"></a><a name="p841mcpsimp"></a>For detailed definitions, see Section 3.1 of the "IVE API Reference".</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p843mcpsimp"><a name="p843mcpsimp"></a><a name="p843mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row844mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p846mcpsimp"><a name="p846mcpsimp"></a><a name="p846mcpsimp"></a>ref</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.4.1.2 "><p id="p848mcpsimp"><a name="p848mcpsimp"></a><a name="p848mcpsimp"></a>Reference frame image pointer; must not be NULL.</p>
<p id="p849mcpsimp"><a name="p849mcpsimp"></a><a name="p849mcpsimp"></a>For detailed definitions, see Section 3.1 of the "IVE API Reference".</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p851mcpsimp"><a name="p851mcpsimp"></a><a name="p851mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row852mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p854mcpsimp"><a name="p854mcpsimp"></a><a name="p854mcpsimp"></a>sad</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.4.1.2 "><p id="p856mcpsimp"><a name="p856mcpsimp"></a><a name="p856mcpsimp"></a>Sad pointer.</p>
<p id="p857mcpsimp"><a name="p857mcpsimp"></a><a name="p857mcpsimp"></a>Based on md_attr-&gt; sad_out_ctrl, if output is required, must not be NULL.</p>
<p id="p858mcpsimp"><a name="p858mcpsimp"></a><a name="p858mcpsimp"></a>For detailed definitions, see Section 3.1 of the "IVE API Reference".</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p860mcpsimp"><a name="p860mcpsimp"></a><a name="p860mcpsimp"></a>Output</p>
</td>
</tr>
<tr id="row861mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p863mcpsimp"><a name="p863mcpsimp"></a><a name="p863mcpsimp"></a>blob</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.4.1.2 "><p id="p865mcpsimp"><a name="p865mcpsimp"></a><a name="p865mcpsimp"></a>Region information pointer.</p>
<p id="p866mcpsimp"><a name="p866mcpsimp"></a><a name="p866mcpsimp"></a>Must not be NULL.</p>
<p id="p867mcpsimp"><a name="p867mcpsimp"></a><a name="p867mcpsimp"></a>For detailed definitions, see Section 1.4 of the "SV Px.0 API Reference".</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p869mcpsimp"><a name="p869mcpsimp"></a><a name="p869mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table> <a name="table870mcpsimp"></a>
<table><thead align="left"><tr id="row877mcpsimp"><th class="cellrowborder" valign="top" width="8.91089108910891%" id="mcps1.1.5.1.1"><p id="p879mcpsimp"><a name="p879mcpsimp"></a><a name="p879mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="43.56435643564357%" id="mcps1.1.5.1.2"><p id="p881mcpsimp"><a name="p881mcpsimp"></a><a name="p881mcpsimp"></a>Supported Image Type</p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.1.5.1.3"><p id="p883mcpsimp"><a name="p883mcpsimp"></a><a name="p883mcpsimp"></a>Address Alignment</p>
</th>
<th class="cellrowborder" valign="top" width="36.633663366336634%" id="mcps1.1.5.1.4"><p id="p885mcpsimp"><a name="p885mcpsimp"></a><a name="p885mcpsimp"></a>Resolution</p>
</th>
</tr>
</thead>
<tbody><tr id="row887mcpsimp"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.1.5.1.1 "><p id="p889mcpsimp"><a name="p889mcpsimp"></a><a name="p889mcpsimp"></a>cur</p>
</td>
<td class="cellrowborder" valign="top" width="43.56435643564357%" headers="mcps1.1.5.1.2 "><p id="p891mcpsimp"><a name="p891mcpsimp"></a><a name="p891mcpsimp"></a>OT_SVP_IMG_TYPE_U8C1</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.5.1.3 "><p id="p893mcpsimp"><a name="p893mcpsimp"></a><a name="p893mcpsimp"></a>16 byte</p>
</td>
<td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.1.5.1.4 "><p id="p895mcpsimp"><a name="p895mcpsimp"></a><a name="p895mcpsimp"></a>64x64 to 1920x1080</p>
</td>
</tr>
<tr id="row896mcpsimp"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.1.5.1.1 "><p id="p898mcpsimp"><a name="p898mcpsimp"></a><a name="p898mcpsimp"></a>ref</p>
</td>
<td class="cellrowborder" valign="top" width="43.56435643564357%" headers="mcps1.1.5.1.2 "><p id="p900mcpsimp"><a name="p900mcpsimp"></a><a name="p900mcpsimp"></a>OT_SVP_IMG_TYPE_U8C1</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.5.1.3 "><p id="p902mcpsimp"><a name="p902mcpsimp"></a><a name="p902mcpsimp"></a>16 byte</p>
</td>
<td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.1.5.1.4 "><p id="p904mcpsimp"><a name="p904mcpsimp"></a><a name="p904mcpsimp"></a>64x64 to 1920x1080</p>
</td>
</tr>
<tr id="row905mcpsimp"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.1.5.1.1 "><p id="p907mcpsimp"><a name="p907mcpsimp"></a><a name="p907mcpsimp"></a>sad</p>
</td>
<td class="cellrowborder" valign="top" width="43.56435643564357%" headers="mcps1.1.5.1.2 "><p id="p909mcpsimp"><a name="p909mcpsimp"></a><a name="p909mcpsimp"></a>OT_SVP_IMG_TYPE_U8C1/ OT_SVP_IMG_TYPE_U16C1</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.5.1.3 "><p id="p911mcpsimp"><a name="p911mcpsimp"></a><a name="p911mcpsimp"></a>16 byte</p>
</td>
<td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.1.5.1.4 "><p id="p913mcpsimp"><a name="p913mcpsimp"></a><a name="p913mcpsimp"></a>Based on md_attr-&gt;sad_mode, corresponds to 4x4, 8x8, 16x16 block modes, with height and width being 1/4, 1/8, or 1/16 of cur respectively.</p>
</td>
</tr>
<tr id="row914mcpsimp"><td class="cellrowborder" valign="top" width="8.91089108910891%" headers="mcps1.1.5.1.1 "><p id="p916mcpsimp"><a name="p916mcpsimp"></a><a name="p916mcpsimp"></a>blob</p>
</td>
<td class="cellrowborder" valign="top" width="43.56435643564357%" headers="mcps1.1.5.1.2 "><p id="p918mcpsimp"><a name="p918mcpsimp"></a><a name="p918mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.5.1.3 "><p id="p920mcpsimp"><a name="p920mcpsimp"></a><a name="p920mcpsimp"></a>16 byte</p>
</td>
<td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.1.5.1.4 "><p id="p922mcpsimp"><a name="p922mcpsimp"></a><a name="p922mcpsimp"></a>--</p>
</td>
</tr>
</tbody>
</table> [Return Values] <a name="table924mcpsimp"></a>
<table><thead align="left"><tr id="row929mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p931mcpsimp"><a name="p931mcpsimp"></a><a name="p931mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p933mcpsimp"><a name="p933mcpsimp"></a><a name="p933mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row935mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p937mcpsimp"><a name="p937mcpsimp"></a><a name="p937mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p939mcpsimp"><a name="p939mcpsimp"></a><a name="p939mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row940mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p942mcpsimp"><a name="p942mcpsimp"></a><a name="p942mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p944mcpsimp"><a name="p944mcpsimp"></a><a name="p944mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408294036">Error Codes</a><span xml:lang="fr-FR" id="ph947mcpsimp"><a name="ph947mcpsimp"></a><a name="ph947mcpsimp"></a>.</span></p>
</td>
</tr>
</tbody>
</table> [Requirements] - Header files: ot\_common\_svp.h, ot\_common\_md.h, ss\_ivs\_md.h
- Library file: libss\_md.a [Notes] - [ss\_ivs\_md\_init](#ZH-CN_TOPIC_0000002441733309) must be called first for initialization. Otherwise, an error is returned.
- md\_chn must be a channel number already created by [ss\_ivs\_md\_create\_chn](#ZH-CN_TOPIC_0000002441733333). Otherwise, an error is returned.
- The maximum number of output region information entries is 254. For region information, see the data type ot\_ive\_ccblob in Section 3 of the "IVE API Reference". The cur\_area\_threshold in the info member of ot\_ive\_ccblob is the area threshold information after block division. The connected region information output here is stored contiguously.
- In the same thread, after completing initialization and channel creation, call the ss\_ivs\_md\_proc interface only once for the same channel. [Example] None. [Related Topics] - [ss\_ivs\_md\_create\_chn](#ss_ivs_md_create_chn)
- [ss\_ivs\_md\_destroy\_chn](#ss_ivs_md_destroy_chn)
- [ss\_ivs\_md\_set\_chn\_attr](#ss_ivs_md_set_chn_attr)
- [ss\_ivs\_md\_get\_bg](#ss_ivs_md_get_bg) ## MD Data Types<a name="ZH-CN_TOPIC_0000002441853461"></a> ### ot\_md\_alg\_mode<a name="ZH-CN_TOPIC_0000002441733345"></a> [Description] Defines the MD algorithm mode. [Definition] ```
typedef enum { OT_MD_ALG_MODE_BG	= 0x0,/*Base on background img*/ OT_MD_ALG_MODE_REF	= 0x1,/*Base on reference img*/ OT_MD_ALG_MODE_BUTT
}ot_md_alg_mode;
``` [Members] <a name="table984mcpsimp"></a>
<table><thead align="left"><tr id="row989mcpsimp"><th class="cellrowborder" valign="top" width="72%" id="mcps1.1.3.1.1"><p id="p991mcpsimp"><a name="p991mcpsimp"></a><a name="p991mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.1.3.1.2"><p id="p993mcpsimp"><a name="p993mcpsimp"></a><a name="p993mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row995mcpsimp"><td class="cellrowborder" valign="top" width="72%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p997mcpsimp"><a name="p997mcpsimp"></a><a name="p997mcpsimp"></a>OT_MD_ALG_MODE_BG</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.3.1.2 "><p id="p999mcpsimp"><a name="p999mcpsimp"></a><a name="p999mcpsimp"></a>Background method.</p>
</td>
</tr>
<tr id="row1000mcpsimp"><td class="cellrowborder" valign="top" width="72%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1002mcpsimp"><a name="p1002mcpsimp"></a><a name="p1002mcpsimp"></a>OT_MD_ALG_M<span xml:lang="en-US" id="ph1003mcpsimp"><a name="ph1003mcpsimp"></a><a name="ph1003mcpsimp"></a>ODE_REF</span></p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.3.1.2 "><p id="p1005mcpsimp"><a name="p1005mcpsimp"></a><a name="p1005mcpsimp"></a>Frame difference method.</p>
</td>
</tr>
</tbody>
</table> [Notes] None. [Related Data Types and Interfaces] None. ### ot\_md\_attr<a name="ZH-CN_TOPIC_0000002408134180"></a> [Description] Defines MD channel attributes. [Definition] ```
typedef struct { ot_md_alg_mode alg_mode; /*Md algorithm mode*/ ot_ive_sad_mode sad_mode; /*Sad mode*/ ot_ive_sad_out_ctrl sad_out_ctrl; /*Sad output ctrl*/ td_u32 width; /*Img width*/ td_u32 height; /*Img height*/ td_u16 sad_threshold; /*Sad thresh*/ ot_ive_ccl_ctrl ccl_ctrl; /*Ccl ctrl*/ ot_ive_add_ctrl add_ctrl; /*Add ctrl*/
}ot_md_attr
``` [Members] <a name="table1026mcpsimp"></a>
<table><thead align="left"><tr id="row1031mcpsimp"><th class="cellrowborder" valign="top" width="19%" id="mcps1.1.3.1.1"><p id="p1033mcpsimp"><a name="p1033mcpsimp"></a><a name="p1033mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="81%" id="mcps1.1.3.1.2"><p id="p1035mcpsimp"><a name="p1035mcpsimp"></a><a name="p1035mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1037mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p id="p1039mcpsimp"><a name="p1039mcpsimp"></a><a name="p1039mcpsimp"></a>alg_mode</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1041mcpsimp"><a name="p1041mcpsimp"></a><a name="p1041mcpsimp"></a>Algorithm mode.</p>
</td>
</tr>
<tr id="row1042mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p id="p1044mcpsimp"><a name="p1044mcpsimp"></a><a name="p1044mcpsimp"></a>sad_mode</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1046mcpsimp"><a name="p1046mcpsimp"></a><a name="p1046mcpsimp"></a>Sad mode. For detailed definitions, see Section 3.3 of the "IVE API Reference".</p>
</td>
</tr>
<tr id="row1047mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p id="p1049mcpsimp"><a name="p1049mcpsimp"></a><a name="p1049mcpsimp"></a>sad_out_ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1051mcpsimp"><a name="p1051mcpsimp"></a><a name="p1051mcpsimp"></a>Sad output control. For detailed definitions, see Section 3.3 of the "IVE API Reference".</p>
<p id="p1052mcpsimp"><a name="p1052mcpsimp"></a><a name="p1052mcpsimp"></a>Only supports OT_IVE_SAD_OUT_CTRL_16BIT_BOTH, OT_IVE_SAD_OUT_CTRL_8BIT_BOTH, and OT_IVE_SAD_OUT_CTRL_THRESHOLD output controls.</p>
</td>
</tr>
<tr id="row1053mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1055mcpsimp"><a name="p1055mcpsimp"></a><a name="p1055mcpsimp"></a>width</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1057mcpsimp"><a name="p1057mcpsimp"></a><a name="p1057mcpsimp"></a>Image width. Must be an even multiple of the macroblock width. Range: [64, 1920]</p>
</td>
</tr>
<tr id="row1058mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1060mcpsimp"><a name="p1060mcpsimp"></a><a name="p1060mcpsimp"></a>height</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1062mcpsimp"><a name="p1062mcpsimp"></a><a name="p1062mcpsimp"></a>Image height. Must be an even multiple of the macroblock height. Range: [64, 1080]</p>
</td>
</tr>
<tr id="row1063mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1065mcpsimp"><a name="p1065mcpsimp"></a><a name="p1065mcpsimp"></a>sad_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1067mcpsimp"><a name="p1067mcpsimp"></a><a name="p1067mcpsimp"></a>Sad threshold.</p>
<p id="p1068mcpsimp"><a name="p1068mcpsimp"></a><a name="p1068mcpsimp"></a>Value depends on sad_out_ctrl:</p>
<a name="ol1069mcpsimp"></a><a name="ol1069mcpsimp"></a><ol id="ol1069mcpsimp"><li>OT_IVE_SAD_OUT_CTRL_8BIT_BOTH, range [0, 255]</li><li>OT_IVE_SAD_OUT_CTRL_16BIT_BOTH and OT_IVE_SAD_OUT_CTRL_THRESHOLD, range [0, 65535]</li></ol>
</td>
</tr>
<tr id="row1072mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1074mcpsimp"><a name="p1074mcpsimp"></a><a name="p1074mcpsimp"></a>ccl_ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1076mcpsimp"><a name="p1076mcpsimp"></a><a name="p1076mcpsimp"></a>CCL control parameters. For detailed definitions, see Section 3.3 of the "IVE API Reference". CCL control parameter member information applies to the image after block division.</p>
</td>
</tr>
<tr id="row1079mcpsimp"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1081mcpsimp"><a name="p1081mcpsimp"></a><a name="p1081mcpsimp"></a>add_ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.1.3.1.2 "><p id="p1083mcpsimp"><a name="p1083mcpsimp"></a><a name="p1083mcpsimp"></a>Add control parameters. For detailed definitions, see Section 3.3 of the "IVE API Reference".</p>
</td>
</tr>
</tbody>
</table> [Notes] None. [Related Data Types and Interfaces] None. ## Error Codes<a name="ZH-CN_TOPIC_0000002408294036"></a> IVS error codes mostly share the same definitions as IVE error codes. The first part of the IVS error code table is identical to that in the "IVE API Reference", with additional special codes listed at the end. **Table 1** IVS error codes <a name="_Ref248310770"></a>
<table><thead align="left"><tr id="row1100mcpsimp"><th class="cellrowborder" valign="top" width="22.54%" id="mcps1.2.4.1.1"><p id="p1102mcpsimp"><a name="p1102mcpsimp"></a><a name="p1102mcpsimp"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="41.03%" id="mcps1.2.4.1.2"><p id="p1104mcpsimp"><a name="p1104mcpsimp"></a><a name="p1104mcpsimp"></a>Macro Definition</p>
</th>
<th class="cellrowborder" valign="top" width="36.43%" id="mcps1.2.4.1.3"><p id="p1106mcpsimp"><a name="p1106mcpsimp"></a><a name="p1106mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1108mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1110mcpsimp"><a name="p1110mcpsimp"></a><a name="p1110mcpsimp"></a>0xa01d8001</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1112mcpsimp"><a name="p1112mcpsimp"></a><a name="p1112mcpsimp"></a>OT_ERR_IVE_INVALID_DEV_ID</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1114mcpsimp"><a name="p1114mcpsimp"></a><a name="p1114mcpsimp"></a>Device ID is out of valid range</p>
</td>
</tr>
<tr id="row1116mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1118mcpsimp"><a name="p1118mcpsimp"></a><a name="p1118mcpsimp"></a>0xa01d8003</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1120mcpsimp"><a name="p1120mcpsimp"></a><a name="p1120mcpsimp"></a>OT_ERR_IVE_INVALID_CHN_ID</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p xml:lang="fr-FR" id="p1122mcpsimp"><a name="p1122mcpsimp"></a><a name="p1122mcpsimp"></a>Channel group number error or invalid region handle</p>
</td>
</tr>
<tr id="row1124mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1126mcpsimp"><a name="p1126mcpsimp"></a><a name="p1126mcpsimp"></a>0xa01d8007</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p xml:lang="it-IT" id="p1128mcpsimp"><a name="p1128mcpsimp"></a><a name="p1128mcpsimp"></a>OT_ERR_IVE_ILLEGAL_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1130mcpsimp"><a name="p1130mcpsimp"></a><a name="p1130mcpsimp"></a>Parameter is out of valid range</p>
</td>
</tr>
<tr id="row1131mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1133mcpsimp"><a name="p1133mcpsimp"></a><a name="p1133mcpsimp"></a>0xa01d8008</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p xml:lang="it-IT" id="p1135mcpsimp"><a name="p1135mcpsimp"></a><a name="p1135mcpsimp"></a>OT_ERR_IVE_EXIST</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1137mcpsimp"><a name="p1137mcpsimp"></a><a name="p1137mcpsimp"></a>Attempting to create an already existing device, channel, or resource</p>
</td>
</tr>
<tr id="row1138mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1140mcpsimp"><a name="p1140mcpsimp"></a><a name="p1140mcpsimp"></a>0xa01d8009</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1142mcpsimp"><a name="p1142mcpsimp"></a><a name="p1142mcpsimp"></a>OT_ERR_IVE_UNEXIST</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1144mcpsimp"><a name="p1144mcpsimp"></a><a name="p1144mcpsimp"></a>Attempting to use or destroy a non-existent device, channel, or resource</p>
</td>
</tr>
<tr id="row1145mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1147mcpsimp"><a name="p1147mcpsimp"></a><a name="p1147mcpsimp"></a>0xa01d800a</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1149mcpsimp"><a name="p1149mcpsimp"></a><a name="p1149mcpsimp"></a>OT_ERR_IVE_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1151mcpsimp"><a name="p1151mcpsimp"></a><a name="p1151mcpsimp"></a>NULL pointer in function parameters</p>
</td>
</tr>
<tr id="row1152mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1154mcpsimp"><a name="p1154mcpsimp"></a><a name="p1154mcpsimp"></a>0xa01d800b</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1156mcpsimp"><a name="p1156mcpsimp"></a><a name="p1156mcpsimp"></a>OT_ERR_IVE_NOT_CFG</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1158mcpsimp"><a name="p1158mcpsimp"></a><a name="p1158mcpsimp"></a>Module not configured</p>
</td>
</tr>
<tr id="row1159mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1161mcpsimp"><a name="p1161mcpsimp"></a><a name="p1161mcpsimp"></a>0xa01d800c</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1163mcpsimp"><a name="p1163mcpsimp"></a><a name="p1163mcpsimp"></a>OT_ERR_IVE_NOT_SUPPORT</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1165mcpsimp"><a name="p1165mcpsimp"></a><a name="p1165mcpsimp"></a>Unsupported parameter or function</p>
</td>
</tr>
<tr id="row1166mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1168mcpsimp"><a name="p1168mcpsimp"></a><a name="p1168mcpsimp"></a>0xa01d800d</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1170mcpsimp"><a name="p1170mcpsimp"></a><a name="p1170mcpsimp"></a>OT_ERR_IVE_NOT_PERM</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1172mcpsimp"><a name="p1172mcpsimp"></a><a name="p1172mcpsimp"></a>Operation not permitted, e.g., attempting to modify static configuration parameters</p>
</td>
</tr>
<tr id="row1174mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1176mcpsimp"><a name="p1176mcpsimp"></a><a name="p1176mcpsimp"></a>0xa01d8014</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1178mcpsimp"><a name="p1178mcpsimp"></a><a name="p1178mcpsimp"></a>OT_ERR_IVE_NO_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1180mcpsimp"><a name="p1180mcpsimp"></a><a name="p1180mcpsimp"></a>Memory allocation failed, e.g., insufficient system memory</p>
</td>
</tr>
<tr id="row1181mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1183mcpsimp"><a name="p1183mcpsimp"></a><a name="p1183mcpsimp"></a>0xa01d8015</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1185mcpsimp"><a name="p1185mcpsimp"></a><a name="p1185mcpsimp"></a>OT_ERR_IVE_NO_BUF</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1187mcpsimp"><a name="p1187mcpsimp"></a><a name="p1187mcpsimp"></a>Buffer allocation failed, e.g., requested image buffer too large</p>
</td>
</tr>
<tr id="row1188mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1190mcpsimp"><a name="p1190mcpsimp"></a><a name="p1190mcpsimp"></a>0xa01d8016</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1192mcpsimp"><a name="p1192mcpsimp"></a><a name="p1192mcpsimp"></a>OT_ERR_IVE_BUF_EMPTY</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1194mcpsimp"><a name="p1194mcpsimp"></a><a name="p1194mcpsimp"></a>No image in buffer</p>
</td>
</tr>
<tr id="row1195mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1197mcpsimp"><a name="p1197mcpsimp"></a><a name="p1197mcpsimp"></a>0xa01d8017</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1199mcpsimp"><a name="p1199mcpsimp"></a><a name="p1199mcpsimp"></a>OT_ERR_IVE_BUF_FULL</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1201mcpsimp"><a name="p1201mcpsimp"></a><a name="p1201mcpsimp"></a>Buffer is full of images</p>
</td>
</tr>
<tr id="row1202mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1204mcpsimp"><a name="p1204mcpsimp"></a><a name="p1204mcpsimp"></a>0xa01d8018</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1206mcpsimp"><a name="p1206mcpsimp"></a><a name="p1206mcpsimp"></a>OT_ERR_IVE_NOT_READY</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1208mcpsimp"><a name="p1208mcpsimp"></a><a name="p1208mcpsimp"></a>System not initialized or corresponding module not loaded</p>
</td>
</tr>
<tr id="row1209mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1211mcpsimp"><a name="p1211mcpsimp"></a><a name="p1211mcpsimp"></a>0xa01d8021</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1213mcpsimp"><a name="p1213mcpsimp"></a><a name="p1213mcpsimp"></a>OT_ERR_IVE_BAD_ADDR</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1215mcpsimp"><a name="p1215mcpsimp"></a><a name="p1215mcpsimp"></a>Illegal address</p>
</td>
</tr>
<tr id="row1216mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1218mcpsimp"><a name="p1218mcpsimp"></a><a name="p1218mcpsimp"></a>0xa01d8022</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1220mcpsimp"><a name="p1220mcpsimp"></a><a name="p1220mcpsimp"></a>OT_ERR_IVE_BUSY</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1222mcpsimp"><a name="p1222mcpsimp"></a><a name="p1222mcpsimp"></a>System busy</p>
</td>
</tr>
<tr id="row1223mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1225mcpsimp"><a name="p1225mcpsimp"></a><a name="p1225mcpsimp"></a>0xa01d8040</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1227mcpsimp"><a name="p1227mcpsimp"></a><a name="p1227mcpsimp"></a>OT_ERR_IVE_SYS_TIMEOUT</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1229mcpsimp"><a name="p1229mcpsimp"></a><a name="p1229mcpsimp"></a>IVE system timeout</p>
</td>
</tr>
<tr id="row1230mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1232mcpsimp"><a name="p1232mcpsimp"></a><a name="p1232mcpsimp"></a>0xa01d8041</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1234mcpsimp"><a name="p1234mcpsimp"></a><a name="p1234mcpsimp"></a>OT_ERR_IVE_QUERY_TIMEOUT</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1236mcpsimp"><a name="p1236mcpsimp"></a><a name="p1236mcpsimp"></a>Query timeout</p>
</td>
</tr>
<tr id="row1237mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1239mcpsimp"><a name="p1239mcpsimp"></a><a name="p1239mcpsimp"></a>0xa01d8042</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1241mcpsimp"><a name="p1241mcpsimp"></a><a name="p1241mcpsimp"></a>OT_ERR_IVE_BUS_ERR</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1243mcpsimp"><a name="p1243mcpsimp"></a><a name="p1243mcpsimp"></a>Bus error</p>
</td>
</tr>
<tr id="row1244mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1246mcpsimp"><a name="p1246mcpsimp"></a><a name="p1246mcpsimp"></a>0xa01d8043</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1248mcpsimp"><a name="p1248mcpsimp"></a><a name="p1248mcpsimp"></a>OT_ERR_IVE_OPEN_FILE</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1250mcpsimp"><a name="p1250mcpsimp"></a><a name="p1250mcpsimp"></a>Failed to open file</p>
</td>
</tr>
<tr id="row1251mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1253mcpsimp"><a name="p1253mcpsimp"></a><a name="p1253mcpsimp"></a>0xa01d8044</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1255mcpsimp"><a name="p1255mcpsimp"></a><a name="p1255mcpsimp"></a>OT_ERR_IVE_READ_FILE</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1257mcpsimp"><a name="p1257mcpsimp"></a><a name="p1257mcpsimp"></a>Failed to read file</p>
</td>
</tr>
<tr id="row1258mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1260mcpsimp"><a name="p1260mcpsimp"></a><a name="p1260mcpsimp"></a>0xa0308003</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1262mcpsimp"><a name="p1262mcpsimp"></a><a name="p1262mcpsimp"></a>OT_ERR_ODT_INVALID_CHN_ID</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p xml:lang="fr-FR" id="p1264mcpsimp"><a name="p1264mcpsimp"></a><a name="p1264mcpsimp"></a>ODT channel group number error or invalid region handle</p>
</td>
</tr>
<tr id="row1266mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1268mcpsimp"><a name="p1268mcpsimp"></a><a name="p1268mcpsimp"></a>0xa0308008</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1270mcpsimp"><a name="p1270mcpsimp"></a><a name="p1270mcpsimp"></a>OT_ERR_ODT_<span xml:lang="it-IT" id="ph1271mcpsimp"><a name="ph1271mcpsimp"></a><a name="ph1271mcpsimp"></a>EXIST</span></p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1273mcpsimp"><a name="p1273mcpsimp"></a><a name="p1273mcpsimp"></a>Attempting to create an already existing device, channel, or resource</p>
</td>
</tr>
<tr id="row1274mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1276mcpsimp"><a name="p1276mcpsimp"></a><a name="p1276mcpsimp"></a>0xa0308009</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1278mcpsimp"><a name="p1278mcpsimp"></a><a name="p1278mcpsimp"></a>OT_ERR_ODT_UNEXIST</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1280mcpsimp"><a name="p1280mcpsimp"></a><a name="p1280mcpsimp"></a>Attempting to use or destroy a non-existent device, channel, or resource</p>
</td>
</tr>
<tr id="row1281mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1283mcpsimp"><a name="p1283mcpsimp"></a><a name="p1283mcpsimp"></a>0xa030800d</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1285mcpsimp"><a name="p1285mcpsimp"></a><a name="p1285mcpsimp"></a>OT_ERR_ODT_NOT_PERM</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1287mcpsimp"><a name="p1287mcpsimp"></a><a name="p1287mcpsimp"></a>Operation not permitted, e.g., attempting to modify static configuration parameters</p>
</td>
</tr>
<tr id="row1289mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1291mcpsimp"><a name="p1291mcpsimp"></a><a name="p1291mcpsimp"></a>0xa0308018</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1293mcpsimp"><a name="p1293mcpsimp"></a><a name="p1293mcpsimp"></a>OT_ERR_ODT_NOT_READY</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1295mcpsimp"><a name="p1295mcpsimp"></a><a name="p1295mcpsimp"></a>ODT not initialized</p>
</td>
</tr>
<tr id="row1296mcpsimp"><td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.2.4.1.1 "><p id="p1298mcpsimp"><a name="p1298mcpsimp"></a><a name="p1298mcpsimp"></a>0xa0308022</p>
</td>
<td class="cellrowborder" valign="top" width="41.03%" headers="mcps1.2.4.1.2 "><p id="p1300mcpsimp"><a name="p1300mcpsimp"></a><a name="p1300mcpsimp"></a>OT_ERR_ODT_BUSY</p>
</td>
<td class="cellrowborder" valign="top" width="36.43%" headers="mcps1.2.4.1.3 "><p id="p1302mcpsimp"><a name="p1302mcpsimp"></a><a name="p1302mcpsimp"></a>ODT system busy</p>
</td>
</tr>
</tbody>
</table> ## Proc Debug Information<a name="ZH-CN_TOPIC_0000002408294100"></a> ### Overview<a name="ZH-CN_TOPIC_0000002441853473"></a> Debug information uses the proc file system under Linux, which can reflect the current operating status of the system in real time. The recorded information can be used for problembitbit and analysis. [File Directory] /proc/umap [Information Viewing Method] - On the console, you can use the cat command to view information. `cat /proc/umap/md` can view the MD proc information. Other commonly used file operation commands can also be used, for example, `cp /proc/umap/md ./` to copy the file to the current directory.
- In an application, the above files can be treated as ordinary read-only files for read operations, such as fopen, fread, etc. >![](public_sys-resources/icon-note.gif) **Note:**
>The following 2 situations should be noted when describing parameters:
>- For parameters with values of {0, 1}, if the specific mapping between values and meanings is not listed, a value of 1 indicates affirmative, and 0 indicates negative.
>- For parameters with values of {aaa, bbb, ccc}, if the specific mapping between values and meanings is not listed, the parameter meaning can be directly determined based on the values aaa, bbb, or ccc. ### MD Proc Information Description<a name="ZH-CN_TOPIC_0000002441853441"></a> [Debug Information] ```
~ # cat /proc/umap/md
[MD] Version: [Vx.x.x.x B0xx Release], Build Time[Feb 20 2020, 16:42:49] ---------------------------md chn attr-----------------------------------
no. w h alg sad_mode sad_out_ctrl sad_thr ccl_mode ccl_init_thr 0 720 576 0 0 0 200 1 16 ccl_step xwt ywt frm_rate cost_tm_per_frm
4 32768 32768 0 2625
``` [Debug Information Analysis] Records the working status information of MD. [Parameter Description] <a name="table1330mcpsimp"></a>
<table><thead align="left"><tr id="row1336mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1338mcpsimp"><a name="p1338mcpsimp"></a><a name="p1338mcpsimp"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1340mcpsimp"><a name="p1340mcpsimp"></a><a name="p1340mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1342mcpsimp"><td class="cellrowborder" rowspan="14" valign="top" width="21.21%" headers="mcps1.1.4.1.1 "><p id="p1344mcpsimp"><a name="p1344mcpsimp"></a><a name="p1344mcpsimp"></a>md chn attr</p>
<p id="p1345mcpsimp"><a name="p1345mcpsimp"></a><a name="p1345mcpsimp"></a>Channel attributes</p>
</td>
<td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.1.4.1.1 "><p id="p1347mcpsimp"><a name="p1347mcpsimp"></a><a name="p1347mcpsimp"></a>no.</p>
</td>
<td class="cellrowborder" valign="top" width="59.35%" headers="mcps1.1.4.1.2 "><p id="p1349mcpsimp"><a name="p1349mcpsimp"></a><a name="p1349mcpsimp"></a>Channel number.</p>
</td>
</tr>
<tr id="row1360mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1362mcpsimp"><a name="p1362mcpsimp"></a><a name="p1362mcpsimp"></a>alg</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1364mcpsimp"><a name="p1364mcpsimp"></a><a name="p1364mcpsimp"></a>Working algorithm.</p>
<p id="p1365mcpsimp"><a name="p1365mcpsimp"></a><a name="p1365mcpsimp"></a>0: Background method;</p>
<p id="p1366mcpsimp"><a name="p1366mcpsimp"></a><a name="p1366mcpsimp"></a>1: Frame difference method.</p>
</td>
</tr>
<tr id="row1367mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1369mcpsimp"><a name="p1369mcpsimp"></a><a name="p1369mcpsimp"></a>sad_mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1371mcpsimp"><a name="p1371mcpsimp"></a><a name="p1371mcpsimp"></a>Sad mode.</p>
<p id="p1372mcpsimp"><a name="p1372mcpsimp"></a><a name="p1372mcpsimp"></a>0: 4x4 macroblock;</p>
<p id="p1373mcpsimp"><a name="p1373mcpsimp"></a><a name="p1373mcpsimp"></a>1: 8x8 macroblock;</p>
<p id="p1374mcpsimp"><a name="p1374mcpsimp"></a><a name="p1374mcpsimp"></a>2: 16x16 macroblock.</p>
</td>
</tr>
<tr id="row1375mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1377mcpsimp"><a name="p1377mcpsimp"></a><a name="p1377mcpsimp"></a>sad_out_ctrl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1379mcpsimp"><a name="p1379mcpsimp"></a><a name="p1379mcpsimp"></a>Sad output control.</p>
<p id="p1380mcpsimp"><a name="p1380mcpsimp"></a><a name="p1380mcpsimp"></a>0: OT_IVE_SAD_OUT_CTRL_16BIT_BOTH;</p>
<p id="p1381mcpsimp"><a name="p1381mcpsimp"></a><a name="p1381mcpsimp"></a>1: OT_IVE_SAD_OUT_CTRL_8BIT_BOTH;</p>
<p id="p1382mcpsimp"><a name="p1382mcpsimp"></a><a name="p1382mcpsimp"></a>4: OT_IVE_SAD_OUT_CTRL_THRESHOLD.</p>
</td>
</tr>
<tr id="row1383mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1385mcpsimp"><a name="p1385mcpsimp"></a><a name="p1385mcpsimp"></a>sad_thr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1387mcpsimp"><a name="p1387mcpsimp"></a><a name="p1387mcpsimp"></a>Sad threshold.</p>
</td>
</tr>
<tr id="row1388mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1390mcpsimp"><a name="p1390mcpsimp"></a><a name="p1390mcpsimp"></a>ccl_mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1392mcpsimp"><a name="p1392mcpsimp"></a><a name="p1392mcpsimp"></a>CCL mode.</p>
<p id="p1393mcpsimp"><a name="p1393mcpsimp"></a><a name="p1393mcpsimp"></a>0: 4-connected;</p>
<p id="p1394mcpsimp"><a name="p1394mcpsimp"></a><a name="p1394mcpsimp"></a>1: 8-connected.</p>
</td>
</tr>
<tr id="row1395mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1397mcpsimp"><a name="p1397mcpsimp"></a><a name="p1397mcpsimp"></a>ccl_init_thr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1399mcpsimp"><a name="p1399mcpsimp"></a><a name="p1399mcpsimp"></a>CCL initial threshold.</p>
</td>
</tr>
<tr id="row1400mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1402mcpsimp"><a name="p1402mcpsimp"></a><a name="p1402mcpsimp"></a>ccl_step</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1404mcpsimp"><a name="p1404mcpsimp"></a><a name="p1404mcpsimp"></a>CCL step.</p>
</td>
</tr>
<tr id="row1405mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1407mcpsimp"><a name="p1407mcpsimp"></a><a name="p1407mcpsimp"></a>xwt</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1409mcpsimp"><a name="p1409mcpsimp"></a><a name="p1409mcpsimp"></a>Background method update X weight.</p>
</td>
</tr>
<tr id="row1410mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1412mcpsimp"><a name="p1412mcpsimp"></a><a name="p1412mcpsimp"></a>ywt</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1414mcpsimp"><a name="p1414mcpsimp"></a><a name="p1414mcpsimp"></a>Background method update Y weight.</p>
</td>
</tr>
<tr id="row1415mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1417mcpsimp"><a name="p1417mcpsimp"></a><a name="p1417mcpsimp"></a>frm_rate</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1419mcpsimp"><a name="p1419mcpsimp"></a><a name="p1419mcpsimp"></a>Frame rate.</p>
</td>
</tr>
<tr id="row1420mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1422mcpsimp"><a name="p1422mcpsimp"></a><a name="p1422mcpsimp"></a>cost_tm_per_frm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1424mcpsimp"><a name="p1424mcpsimp"></a><a name="p1424mcpsimp"></a>Time per frame (unit: us).</p>
<p id="p1425mcpsimp"><a name="p1425mcpsimp"></a><a name="p1425mcpsimp"></a><strong id="b1426mcpsimp"><a name="b1426mcpsimp"></a><a name="b1426mcpsimp"></a>Note: Frame rate and time per frame are calculated every 10 seconds.</strong></p>
</td>
</tr>
</tbody>
</table>
