---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/TDE API参考/TDE API参考.md
--- # Preface
**Overview<a name="section102mcpsimp"></a>** This document mainly introduces the TDE API, data types, and Proc debug information. >![](public_sys-resources/icon-note.gif) **Note:**
>- Unless otherwise specified, is consistent with Hi3403V100. **Product Version<a name="section105mcpsimp"></a>** The product version corresponding to this document is as follows. <a name="table108mcpsimp"></a>
<table><thead align="left"><tr id="row113mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p115mcpsimp"><a name="p115mcpsimp"></a><a name="p115mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p117mcpsimp"><a name="p117mcpsimp"></a><a name="p117mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row119mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p121mcpsimp"><a name="p121mcpsimp"></a><a name="p121mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p123mcpsimp"><a name="p123mcpsimp"></a><a name="p123mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p128mcpsimp"><a name="p128mcpsimp"></a><a name="p128mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p25392377163"><a name="p25392377163"></a><a name="p25392377163"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13835920181"><a name="p13835920181"></a><a name="p13835920181"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Target Audience<a name="section133mcpsimp"></a>** This document is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions (see original document for icon images)** **Revision History** | Document Version | Release Date | Revision Description |
|---|---|---|
| 00B01 | 2025-09-15 | First interim release. | # Overview
## Overview<a name="ZH-CN_TOPIC_0000002408119226"></a> Two Dimensional Engine (TDE) is a hardware acceleration module for 2D graphics operations. It provides functions such as bit block transfer, color fill, rectangle drawing, line drawing, rotation, scaling, de-flicker filtering, alpha blending, and colorkey operations. ## Module Loading<a name="ZH-CN_TOPIC_0000002441718473"></a> ### Load Command<a name="ZH-CN_TOPIC_0000002441678589"></a> ```
insmod tde.ko [parameters]
``` ### Parameters<a name="ZH-CN_TOPIC_0000002441718437"></a> #### Parameter g\_is\_resize\_filter<a name="ZH-CN_TOPIC_0000002408279214"></a> Controls whether to enable the resize filter. 0 = disable, 1 = enable (default). #### Parameter g\_max\_node\_num<a name="ZH-CN_TOPIC_0000002408279198"></a> Sets the maximum number of job nodes. Default is 60. Range: [1, 64]. #### Parameter g\_tde\_tmp\_buf<a name="ZH-CN_TOPIC_0000002441678557"></a> TDE temporary buffer address. Must be configured for certain operations. #### Parameter g\_rgb\_truncation\_mode<a name="ZH-CN_TOPIC_0000002408119254"></a> Sets the RGB truncation mode. 0 = truncate low bits (default), 1 = truncate high bits. ## Reference Domain Description<a name="ZH-CN_TOPIC_0000002408279174"></a> ### API Reference Domain<a name="ZH-CN_TOPIC_0000002408119210"></a> The API descriptions use the following reference domains: Purpose, Syntax, Parameters, Description, Return Value, Note, Reference, Related Data Types, Error Code. ### Data Type Reference Domain<a name="ZH-CN_TOPIC_0000002408119290"></a> Data type descriptions use: Definition, Description, Members, Note, Reference, Related Data Types. # API Reference
## API Overview<a name="ZH-CN_TOPIC_0000002408119214"></a> The TDE module provides hardware-accelerated 2D graphics operations. All operations are submitted as jobs that can be processed synchronously or asynchronously. **Figure 1** TDE Software Flow<a name="fig9262165107"></a> ![](figures/TDE Softwarestreamgraph.png "TDE Software Flow Diagram") **Function List:** | Category | Function | Description |
|---|---|---|
| Job Control | ss\_tde\_open | Open TDE device |
| | ss\_tde\_close | Close TDE device |
| | ss\_tde\_begin\_job | Begin a TDE job |
| | ss\_tde\_end\_job | End and submit a TDE job |
| | ss\_tde\_cancel\_job | Cancel a TDE job |
| | ss\_tde\_wait\_for\_done | Wait for a specific job to complete |
| | ss\_tde\_wait\_all\_done | Wait for all jobs to complete |
| | ss\_tde\_reset | Reset TDE hardware |
| Draw Operations | ss\_tde\_quick\_fill | Quick fill a rectangular area with color |
| | ss\_tde\_quick\_draw\_rect | Draw a rectangle outline |
| | ss\_tde\_draw\_multi\_rect | Draw multiple rectangles |
| | ss\_tde\_draw\_line | Draw lines |
| BitBLT Operations | ss\_tde\_quick\_copy | Quick copy image data |
| | ss\_tde\_quick\_resize | Resize image data |
| | ss\_tde\_bit\_blit | Bit block transfer with ROP |
| | ss\_tde\_mb\_blit | Multi-bit block transfer |
| | ss\_tde\_bitmap\_mask\_rop | Bitmap mask ROP operation |
| | ss\_tde\_bitmap\_mask\_blend | Bitmap mask blend operation |
| Special Operations | ss\_tde\_quick\_deflicker | De-flicker filter |
| | ss\_tde\_solid\_draw | Solid drawing with pattern |
| | ss\_tde\_rotate | Image rotation |
| | ss\_tde\_pattern\_fill | Pattern fill |
| Configuration | ss\_tde\_get\_deflicker\_level | Get de-flicker level |
| | ss\_tde\_set\_deflicker\_level | Set de-flicker level |
| | ss\_tde\_get\_alpha\_threshold\_value | Get alpha threshold value |
| | ss\_tde\_set\_alpha\_threshold\_value | Set alpha threshold value |
| | ss\_tde\_get\_alpha\_threshold\_state | Get alpha threshold state |
| | ss\_tde\_set\_alpha\_threshold\_state | Set alpha threshold state |
| | ss\_tde\_enable\_rgn\_deflicker | Enable regional de-flicker | ## Function Reference<a name="ZH-CN_TOPIC_0000002408119286"></a> ### ss\_tde\_open<a name="ZH-CN_TOPIC_0000002408119258"></a> [Purpose]
Open the TDE device and obtain a device handle. [Syntax]
```c
#include "ss_tde.h"
td_s32 ss_tde_open(void);
``` [Parameters]
None. [Description]
Opens the TDE device. Must be called before any other TDE operations. Returns a handle that is used in subsequent TDE operations. [Return Value]
Returns a non-negative handle on success. Returns a negative value on failure. ### ss\_tde\_close<a name="ZH-CN_TOPIC_0000002441718445"></a> [Purpose]
Close the TDE device. [Syntax]
```c
td_s32 ss_tde_close(td_s32 hTde);
``` [Parameters]
- h Tde: TDE device handle obtained from ss\_tde\_open. [Description]
Closes the TDE device and releases related resources. ### ss\_tde\_begin\_job<a name="ZH-CN_TOPIC_0000002408279190"></a> [Purpose]
Begin a new TDE job. [Syntax]
```c
td_s32 ss_tde_begin_job(td_s32 hTde, ot_tde_handle *phJob);
``` [Description]
Creates a new job handle for subsequent TDE operations. Multiple operations can be added to a single job. ### ss\_tde\_end\_job<a name="ZH-CN_TOPIC_0000002408279158"></a> [Purpose]
End and submit a TDE job for execution. [Syntax]
```c
td_s32 ss_tde_end_job(td_s32 hTde, ot_tde_handle hJob, td_bool bSync, td_bool bBlock, td_u32 u32TimeOut);
``` [Parameters]
- h Tde: TDE device handle.
- h Job: Job handle to submit.
- bSync: Synchronous (TD_TRUE) or asynchronous (TD_FALSE) execution.
- b Block: Blocking mode.
- u32Time Out: Timeout in milliseconds for blocking mode. ### ss\_tde\_cancel\_job<a name="ZH-CN_TOPIC_0000002408119222"></a> [Purpose]
Cancel a previously submitted TDE job. ### ss\_tde\_wait\_for\_done<a name="ZH-CN_TOPIC_0000002408279142"></a> [Purpose]
Wait for a specific TDE job to complete. ### ss\_tde\_wait\_all\_done<a name="ZH-CN_TOPIC_0000002408279162"></a> [Purpose]
Wait for all submitted TDE jobs to complete. ### ss\_tde\_reset<a name="ZH-CN_TOPIC_0000002441678533"></a> [Purpose]
Reset the TDE hardware. ### ss\_tde\_quick\_fill<a name="ZH-CN_TOPIC_0000002408279206"></a> [Purpose]
Quickly fill a rectangular area with a solid color. [Syntax]
```c
td_s32 ss_tde_quick_fill(td_s32 hTde, ot_tde_handle hJob, const ot_tde_surface *pstDst, const ot_tde_fill_rect *pstFillRect, td_u32 u32Color);
``` [Description]
Fills the destination rectangle with the specified color. Supports RGB and ARGB color formats. ### ss\_tde\_quick\_draw\_rect<a name="ZH-CN_TOPIC_0000002408279218"></a> [Purpose]
Draw a rectangle outline (border only). ### ss\_tde\_draw\_multi\_rect<a name="ZH-CN_TOPIC_0000002408119278"></a> [Purpose]
Draw multiple rectangles in a single operation. ### ss\_tde\_draw\_line<a name="ZH-CN_TOPIC_0000002408119246"></a> [Purpose]
Draw one or more lines between specified coordinates. ### ss\_tde\_quick\_copy<a name="ZH-CN_TOPIC_0000002441718413"></a> [Purpose]
Quickly copy image data from source to destination surface. ### ss\_tde\_quick\_resize<a name="ZH-CN_TOPIC_0000002408119230"></a> [Purpose]
Resize (scale) an image from source to destination rectangle. [Description]
Supports both upscaling and downscaling with configurable filter options. ### ss\_tde\_quick\_deflicker<a name="ZH-CN_TOPIC_0000002408119250"></a> [Purpose]
Apply de-flicker filter to reduce flickering in interlaced displays. ### ss\_tde\_solid\_draw<a name="ZH-CN_TOPIC_0000002408119234"></a> [Purpose]
Solid drawing operation with configurable pattern and alpha. ### ss\_tde\_rotate<a name="ZH-CN_TOPIC_0000002408279222"></a> [Purpose]
Rotate an image by 0, 90, 180, or 270 degrees. ### ss\_tde\_bit\_blit<a name="ZH-CN_TOPIC_0000002408279150"></a> [Purpose]
Bit block transfer with raster operation (ROP) codes. [Description]
Transfers source image data to destination with programmable ROP codes for combining source and destination pixel data. ### ss\_tde\_pattern\_fill<a name="ZH-CN_TOPIC_0000002408119294"></a> [Purpose]
Fill a rectangle using a pattern image source. ### ss\_tde\_mb\_blit<a name="ZH-CN_TOPIC_0000002441678577"></a> [Purpose]
Multi-block bit block transfer. ### ss\_tde\_bitmap\_mask\_rop<a name="ZH-CN_TOPIC_0000002408279186"></a> [Purpose]
Bit block transfer with bitmap mask and ROP. ### ss\_tde\_bitmap\_mask\_blend<a name="ZH-CN_TOPIC_0000002408279178"></a> [Purpose]
Bit block transfer with bitmap mask and alpha blending. ### ss\_tde\_get\_deflicker\_level / ss\_tde\_set\_deflicker\_level<a name="ZH-CN_TOPIC_0000002408119266"></a> [Purpose]
Get/set the de-flicker filter level. ### ss\_tde\_get\_alpha\_threshold\_value / ss\_tde\_set\_alpha\_threshold\_value<a name="ZH-CN_TOPIC_0000002408279154"></a> [Purpose]
Get/set the alpha threshold value for alpha comparison operations. ### ss\_tde\_get\_alpha\_threshold\_state / ss\_tde\_set\_alpha\_threshold\_state<a name="ZH-CN_TOPIC_0000002441718401"></a> [Purpose]
Get/set the alpha threshold state (enabled/disabled). ### ss\_tde\_enable\_rgn\_deflicker<a name="ZH-CN_TOPIC_0000002408119274"></a> [Purpose]
Enable or disable regional de-flicker for specific regions. # Data Type
## Data Structure Index The TDE module defines the following data types: - **ot\_tde\_handle**: TDE job handle type.
- **ot\_tde\_surface**: Defines a TDE surface, including physical address, virtual address, width, height, stride, and color format.
- **ot\_tde\_color\_format**: Enumeration of supported color formats (RGB565, RGB888, ARGB8888, etc.).
- **ot\_tde\_mb\_color\_format**: Color format for multi-block operations.
- **ot\_tde\_fill\_rect**: Rectangle definition for fill operations.
- **ot\_tde\_rect**: Generic rectangle structure with x, y, w, h.
- **ot\_tde\_point**: Point coordinate structure.
- **ot\_tde\_deflicker\_level**: De-flicker level enumeration.
- **ot\_tde\_alpha\_threshold**: Alpha threshold configuration structure.
- **ot\_tde\_rop\_code**: Raster operation code type. ## Color Format Mapping<a name="ZH-CN_TOPIC_0000002441678613"></a> **Table 1** Color Format Mapping | ot\_tde\_color\_format | Description | Byte Order (in memory) |
|---|---|---|
| OT\_TDE\_COLOR\_FMT\_ARGB1555 | ARGB 1:5:5:5 | A1R5G5B5 |
| OT\_TDE\_COLOR\_FMT\_ARGB4444 | ARGB 4:4:4:4 | A4R4G4B4 |
| OT\_TDE\_COLOR\_FMT\_ARGB8888 | ARGB 8:8:8:8 | B0G0R0A0 |
| OT\_TDE\_COLOR\_FMT\_RGB565 | RGB 5:6:5 | B5G6R5 | (For the complete color format list, refer to the header file ss\_tde.h.) ## Detailed Data Type Descriptions ### ot\_tde\_surface<a name="ZH-CN_TOPIC_0000002408119270"></a> [Definition]
```c
typedef struct { td_u32 phys_addr; td_u32 virt_addr; td_u32 width; td_u32 height; td_u32 stride; ot_tde_color_format color_format; td_bool alpha_enable; td_u8 alpha0; td_u8 alpha1;
} ot_tde_surface;
``` [Description]
Defines a surface (image buffer) for TDE operations. [Members]
- phys_addr: Physical address of the surface buffer.
- virt_addr: Virtual address of the surface buffer.
- width: Width in pixels.
- height: Height in pixels.
- stride: Stride (bytes per line).
- color_format: Color format of the surface.
- alpha_enable: Whether global alpha is enabled.
- alpha0/alpha1: Global alpha values for the surface. ### ot\_tde\_color\_format [Definition]
```c
typedef enum { OT_TDE_COLOR_FMT_RGB565 = 0x0, OT_TDE_COLOR_FMT_ARGB1555, OT_TDE_COLOR_FMT_ARGB4444, OT_TDE_COLOR_FMT_ARGB8888, OT_TDE_COLOR_FMT_ARGB8888, /* ... additional formats */
} ot_tde_color_format;
``` [Description]
Enumeration of supported color formats for TDE surfaces. ### Additional Data Types Refer to the header files for complete definitions of ot\_tde\_fill\_rect, ot\_tde\_rect, ot\_tde\_point, ot\_tde\_deflicker\_level, and other related types. # Proc Debug Information TDE module debug information is available through: - `/proc/umap/tde`: Displays TDE job status, hardware utilization, error counts, and current configuration parameters. The proc output includes:
- TDE version information.
- Job queue status (queued, running, completed).
- Module parameters (resize filter, max node num, tmp buf, truncation mode).
- Per-operation statistics.
