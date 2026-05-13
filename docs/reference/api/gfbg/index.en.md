---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/GFBG API 参考/GFBG API 参考.md
--- # Preface
**Overview<a name="section413mcpsimp"></a>** This document mainly introduces the GFBG API, data types, and Proc debug information. >![](public_sys-resources/icon-note.gif) **Note:**
>- Unless otherwise specified, is identical to Hi3403V100, and is identical to . **Product Version<a name="section418mcpsimp"></a>** The product version corresponding to this document is as follows. <a name="table421mcpsimp"></a>
<table><thead align="left"><tr id="row426mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p428mcpsimp"><a name="p428mcpsimp"></a><a name="p428mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p430mcpsimp"><a name="p430mcpsimp"></a><a name="p430mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row432mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p434mcpsimp"><a name="p434mcpsimp"></a><a name="p434mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p436mcpsimp"><a name="p436mcpsimp"></a><a name="p436mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p441mcpsimp"><a name="p441mcpsimp"></a><a name="p441mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p166081349121314"><a name="p166081349121314"></a><a name="p166081349121314"></a>V101</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p215119511412"><a name="p215119511412"></a><a name="p215119511412"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Target Audience<a name="section446mcpsimp"></a>** This document is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions<a name="section451mcpsimp"></a>** The following symbols may appear in this document. <a name="table451mcpsimp"></a>
<table><thead align="left"><tr id="row456mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p458mcpsimp"><a name="p458mcpsimp"></a><a name="p458mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p460mcpsimp"><a name="p460mcpsimp"></a><a name="p460mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row462mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a><a name="image109"></a><a name="image109"></a><span><img id="image109" src="figures/zh-cn_image_0000002441654509.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p466mcpsimp"><a name="p466mcpsimp"></a><a name="p466mcpsimp"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section489mcpsimp"></a>** <a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.1%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.18000000000001%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Revision Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.1%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.18000000000001%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First interim release.</p>
</td>
</tr>
</tbody>
</table> # Overview
## Overview<a name="ZH-CN_TOPIC_0000002408255058"></a> Graphic Framebuffer Group (GFBG) is a module of the digital media processing platform that manages image overlay layers. Based on Linux Framebuffer, it provides basic Linux Framebuffer functions and extends additional graphics layer control features such as inter-layer Alpha, origin setting, and FB extension modes. ## Reference Domain Description<a name="ZH-CN_TOPIC_0000002441694349"></a> ### API Reference Domain<a name="ZH-CN_TOPIC_0000002441654501"></a> This manual uses 9 reference domains to describe API information. Their functions are shown in [Table 1](#_Ref177443220). **Table 1** API Reference Domain Description <a name="_Ref177443220"></a>
<table><thead align="left"><tr id="row6358mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="p6360mcpsimp"><a name="p6360mcpsimp"></a><a name="p6360mcpsimp"></a>Reference Domain</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="p6362mcpsimp"><a name="p6362mcpsimp"></a><a name="p6362mcpsimp"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="row6364mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6366mcpsimp"><a name="p6366mcpsimp"></a><a name="p6366mcpsimp"></a>Purpose</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6368mcpsimp"><a name="p6368mcpsimp"></a><a name="p6368mcpsimp"></a>Briefly describes the main function of the API.</p>
</td>
</tr>
<tr id="row6369mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6371mcpsimp"><a name="p6371mcpsimp"></a><a name="p6371mcpsimp"></a>Syntax</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6373mcpsimp"><a name="p6373mcpsimp"></a><a name="p6373mcpsimp"></a>Lists the header files and API prototype declarations required to call the API.</p>
</td>
</tr>
<tr id="row6374mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6376mcpsimp"><a name="p6376mcpsimp"></a><a name="p6376mcpsimp"></a>Parameters</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6378mcpsimp"><a name="p6378mcpsimp"></a><a name="p6378mcpsimp"></a>Lists API parameters, parameter descriptions, and parameter attributes.</p>
</td>
</tr>
<tr id="row6379mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6381mcpsimp"><a name="p6381mcpsimp"></a><a name="p6381mcpsimp"></a>Description</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6383mcpsimp"><a name="p6383mcpsimp"></a><a name="p6383mcpsimp"></a>Briefly describes the working process of the API.</p>
</td>
</tr>
<tr id="row6384mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6386mcpsimp"><a name="p6386mcpsimp"></a><a name="p6386mcpsimp"></a>Return Value</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6388mcpsimp"><a name="p6388mcpsimp"></a><a name="p6388mcpsimp"></a>Describes the return value of the API.</p>
</td>
</tr>
<tr id="row6389mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6391mcpsimp"><a name="p6391mcpsimp"></a><a name="p6391mcpsimp"></a>Note</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6393mcpsimp"><a name="p6393mcpsimp"></a><a name="p6393mcpsimp"></a>Supplementary instructions and precautions.</p>
</td>
</tr>
<tr id="row6394mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6396mcpsimp"><a name="p6396mcpsimp"></a><a name="p6396mcpsimp"></a>Reference</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6398mcpsimp"><a name="p6398mcpsimp"></a><a name="p6398mcpsimp"></a>Lists other API functions related to this API.</p>
</td>
</tr>
<tr id="row6399mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6401mcpsimp"><a name="p6401mcpsimp"></a><a name="p6401mcpsimp"></a>Related Data Types</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6403mcpsimp"><a name="p6403mcpsimp"></a><a name="p6403mcpsimp"></a>Lists data types related to this API.</p>
</td>
</tr>
<tr id="row6404mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p6406mcpsimp"><a name="p6406mcpsimp"></a><a name="p6406mcpsimp"></a>Error Code</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6408mcpsimp"><a name="p6408mcpsimp"></a><a name="p6408mcpsimp"></a>Describes the error codes returned by the API.</p>
</td>
</tr>
</tbody>
</table> ### Data Type Reference Domain<a name="ZH-CN_TOPIC_0000002408255006"></a> **Table 1** Data Type Reference Domain Description <a name="_Toc123456"></a>
<table><thead align="left"><tr><th class="cellrowborder" valign="top" width="27%"><p id="Reference Domain">Reference Domain</p>
</th>
<th class="cellrowborder" valign="top" width="73%"><p id="Meaning">Meaning</p>
</th>
</tr>
</thead>
<tbody><tr><td class="cellrowborder" valign="top" width="27%"><p>Definition</p>
</td>
<td class="cellrowborder" valign="top" width="73%"><p>Data structure or enumeration type definition.</p>
</td>
</tr>
<tr><td class="cellrowborder" valign="top" width="27%"><p>Description</p>
</td>
<td class="cellrowborder" valign="top" width="73%"><p>Describes the function of the data type.</p>
</td>
</tr>
<tr><td class="cellrowborder" valign="top" width="27%"><p>Members</p>
</td>
<td class="cellrowborder" valign="top" width="73%"><p>Describes the members of the data structure.</p>
</td>
</tr>
<tr><td class="cellrowborder" valign="top" width="27%"><p>Note</p>
</td>
<td class="cellrowborder" valign="top" width="73%"><p>Supplementary instructions and precautions.</p>
</td>
</tr>
<tr><td class="cellrowborder" valign="top" width="27%"><p>Reference</p>
</td>
<td class="cellrowborder" valign="top" width="73%"><p>Lists other API functions related to this data type.</p>
</td>
</tr>
<tr><td class="cellrowborder" valign="top" width="27%"><p>Related Data Types</p>
</td>
<td class="cellrowborder" valign="top" width="73%"><p>Lists data types related to this data type.</p>
</td>
</tr>
</tbody>
</table> # API Reference
## API Categories<a name="ZH-CN_TOPIC_0000002408255074"></a> GFBG AP Is are mainly accessed through ioctl system calls on the Framebuffer device node (/dev/fbX). AP Is are divided into: - **Standard functions**: Linux standard Framebuffer ioctl operations.
- **Extended functions**: GFBG-specific extended ioctl operations, including general functions, layer control functions, and module parameter functions. ## ioctl Functions<a name="ZH-CN_TOPIC_0000002408255022"></a> The GFBG module uses the Linux standard ioctl system call. The ioctl command format is as follows: ```
#include <sys/ioctl.h> int ioctl(int fd, unsigned long request, ...);
``` - **fd**: File descriptor of the Framebuffer device.
- **request**: The ioctl command code.
- **...**: Optional parameter (usually a pointer to a data structure). ## Standard Functions<a name="ZH-CN_TOPIC_0000002408095170"></a> ### FBIOGET\_VSCREENINFO<a name="ZH-CN_TOPIC_0000002408255078"></a> [Purpose]
Get the current framebuffer variable screen information. [Syntax]
```
#include <linux/fb.h>
int ioctl(int fd, FBIOGET_VSCREENINFO, struct fb_var_screeninfo *var);
``` [Parameters]
- fd: Framebuffer device file descriptor.
- var: Pointer to the output struct fb_var_screeninfo. [Description]
This ioctl retrieves the current variable parameters of the framebuffer, including resolution, color depth, timing parameters, etc. [Return Value]
Returns 0 on success, -1 on error with errno set. ### FBIOPUT\_VSCREENINFO<a name="ZH-CN_TOPIC_0000002408255102"></a> [Purpose]
Set the framebuffer variable screen information. [Syntax]
```
int ioctl(int fd, FBIOPUT_VSCREENINFO, struct fb_var_screeninfo *var);
``` [Description]
Sets the framebuffer's variable parameters. After changing parameters, the hardware may need to be reconfigured. ### FBIOGET\_FSCREENINFO<a name="ZH-CN_TOPIC_0000002441694273"></a> [Purpose]
Get the framebuffer fixed screen information. ### FBIOPAN\_DISPLAY<a name="ZH-CN_TOPIC_0000002408095106"></a> [Purpose]
Pan the display to a different position in the virtual screen buffer. [Description]
Used for double-buffering and smooth scrolling by changing the visible area's start offset. ## Extended Functions<a name="ZH-CN_TOPIC_0000002408095098"></a> ### General Functions<a name="ZH-CN_TOPIC_0000002441654493"></a> #### FBIOGET\_CAPABILITY\_GFBG<a name="ZH-CN_TOPIC_0000002441654445"></a> [Purpose]
Get the capability information of the GFBG device. [Syntax]
```
#include <ss_ot_common.h>
int ioctl(int fd, FBIOGET_CAPABILITY_GFBG, ot_gfbg_capability *cap);
``` [Parameters]
- cap: Pointer to the output ot_gfbg_capability structure. [Description]
Returns the capabilities supported by the GFBG module, such as maximum layer count, supported mirror modes, alpha support, etc. #### FBIOGET\_SCREEN\_ORIGIN\_GFBG<a name="ZH-CN_TOPIC_0000002441694257"></a> [Purpose]
Get the current display origin (start position) of the graphics layer. [Syntax]
```
int ioctl(int fd, FBIOGET_SCREEN_ORIGIN_GFBG, ot_gfbg_origin *origin);
``` [Description]
Returns the X and Y coordinate offset of the current graphics layer. #### FBIOPUT\_SCREEN\_ORIGIN\_GFBG<a name="ZH-CN_TOPIC_0000002441654497"></a> [Purpose]
Set the display origin of the graphics layer. [Syntax]
```
int ioctl(int fd, FBIOPUT_SCREEN_ORIGIN_GFBG, ot_gfbg_origin *origin);
``` [Description]
Allows repositioning the graphics layer origin to achieve split-screen or overlay effects. #### FBIOGET\_SHOW\_GFBG<a name="ZH-CN_TOPIC_0000002441654505"></a> [Purpose]
Get the current show/hide status of the graphics layer. #### FBIOPUT\_SHOW\_GFBG<a name="ZH-CN_TOPIC_0000002408255046"></a> [Purpose]
Set the show/hide status of the graphics layer. #### FBIOGET\_MIRROR\_MODE<a name="ZH-CN_TOPIC_0000002441694297"></a> [Purpose]
Get the current mirror mode of the graphics layer. #### FBIOPUT\_MIRROR\_MODE<a name="ZH-CN_TOPIC_0000002408095118"></a> [Purpose]
Set the mirror mode of the graphics layer. #### FBIOGET\_ALPHA\_GFBG<a name="ZH-CN_TOPIC_0000002441654413"></a> [Purpose]
Get the alpha blending configuration of the graphics layer. #### FBIOPUT\_ALPHA\_GFBG<a name="ZH-CN_TOPIC_0000002408095146"></a> [Purpose]
Set the alpha blending configuration of the graphics layer. #### FBIOGET\_COLORKEY\_GFBG<a name="ZH-CN_TOPIC_0000002408095110"></a> [Purpose]
Get the colorkey configuration of the graphics layer. #### FBIOPUT\_COLORKEY\_GFBG<a name="ZH-CN_TOPIC_0000002408095094"></a> [Purpose]
Set the colorkey configuration of the graphics layer. #### FBIOGET\_DEFLICKER\_GFBG<a name="ZH-CN_TOPIC_0000002408095186"></a> [Purpose]
Get the de-flicker configuration of the graphics layer. #### FBIOPUT\_DEFLICKER\_GFBG<a name="ZH-CN_TOPIC_0000002441654469"></a> [Purpose]
Set the de-flicker configuration of the graphics layer. #### FBIOGET\_VER\_BLANK\_GFBG<a name="ZH-CN_TOPIC_0000002441694317"></a> [Purpose]
Get the vertical blanking status. [Description]
Used to synchronize frame buffer updates with the display vertical blanking interval to avoid tearing. #### FBIOGET\_COLKEY\_MULTI\_GFBG / FBIOPUT\_COLKEY\_MULTI\_GFBG [Purpose]
Get/set multi-window colorkey configuration. #### FBIOPUT\_CSC\_GFBG / FBIOGET\_CSC\_GFBG [Purpose]
Get/set the CSC (Color Space Conversion) matrix for the graphics layer. #### FBIOGET\_LAYOUT\_GFBG / FBIOPUT\_LAYOUT\_GFBG [Purpose]
Get/set the GFBG layer layout configuration. [Description]
Configures the layer binding relationship with the VO device. #### FBIORESET\<X\>_GFBG (FBIORESET_ALPHA_GFBG, FBIORESET_COLORKEY_GFBG, etc.) [Purpose]
Reset specific GFBG parameters to their default values. ### Layer Function<a name="ZH-CN_TOPIC_0000002408095126"></a> #### FBIOGET\_LAYER\_ID / FBIOPUT\_LAYER\_ID [Purpose]
Get/set the current operation layer ID for multi-layer GFBG configurations. (Additional layer-specific ioctls follow the same pattern for alpha, colorkey, show, origin, etc., but with layer ID applied.) ### Module Parameter Function<a name="ZH-CN_TOPIC_0000002408095178"></a> Module parameters can be configured when loading the gfbg.ko module, or through proc file system interfaces at runtime. # Data Type
## GFBG Capability<a name="ZH-CN_TOPIC_0000002408095162"></a> ### ot\_gfbg\_capability [Definition]
```c
typedef struct { ot_gfbg_layer layer_id; ot_gfbg_bool mirror; ot_gfbg_bool colorkey; ot_gfbg_bool alphablend; unsigned int max_layer_num;
} ot_gfbg_capability;
``` [Description]
Describes the capability information of the GFBG device. [Members]
- layer_id: Supported graphics layer ID.
- mirror: Whether mirror mode is supported.
- colorkey: Whether colorkey is supported.
- alphablend: Whether alpha blending is supported.
- max_layer_num: Maximum number of graphics layers. ### ot\_gfbg\_alpha [Definition]
```c
typedef struct { ot_gfbg_alpha_flag alpha_flag; unsigned int alpha0; unsigned int alpha1;
} ot_gfbg_alpha;
``` [Description]
Alpha blending configuration structure for GFBG layers. ### ot\_gfbg\_colorkey [Definition]
```c
typedef struct { unsigned int key; unsigned char mask_r; unsigned char mask_g; unsigned char mask_b; unsigned char mask_alpha;
} ot_gfbg_colorkey;
``` [Description]
Colorkey configuration structure. Pixels matching the colorkey become transparent. ### Additional Data Types The GFBG API defines additional data types for mirror mode, origin, CSC matrix, layout configuration, and multi-window colorkey. Refer to the header files for complete definitions. # Proc Debug Information GFBG provides debug information through the proc file system: - `/proc/umap/gfbg`: Displays overall GFBG status, including layer configurations, alpha settings, colorkey settings, mirror modes, and current display status. Note: In heterogeneous systems, VO runs on the Lite OS side while GFBG runs on the Linux side. When a graphics layer is closed, the default CSC parameters are restored. The VO proc information may temporarily not reflect GFBG layer updates.
