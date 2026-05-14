---
title: "Boot Screen User Guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/开机画面使用指南/开机画面使用指南.md
---

# Preface
**Overview<a name="section142mcpsimp"></a>**

This document provides basic functional functions and boot command-line instructions for implementing a boot screen. Users can configure these according to their specific application requirements.

>![](public_sys-resources/icon-note.gif) **Note:** 
>Unless otherwise stated, SS927V100 and SS928V100, and SS522V100 and SS524V100 are fully identical.

**Product Versions<a name="section145mcpsimp"></a>**

The product versions corresponding to this document are listed below.

<a name="table148mcpsimp"></a>
<table><thead align="left"><tr id="row153mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row159mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row164mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p166mcpsimp"><a name="p166mcpsimp"></a><a name="p166mcpsimp"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p168mcpsimp"><a name="p168mcpsimp"></a><a name="p168mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row147881056162014"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p881081984715"><a name="p881081984715"></a><a name="p881081984715"></a>SS524</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
<tr id="row15713193911010"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p20713739105"><a name="p20713739105"></a><a name="p20713739105"></a>SS522</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p271323916019"><a name="p271323916019"></a><a name="p271323916019"></a>V100</p>
</td>
</tr>
<tr id="row89631008112"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p064712218110"><a name="p064712218110"></a><a name="p064712218110"></a>SS522</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p19647921118"><a name="p19647921118"></a><a name="p19647921118"></a>V101</p>
</td>
</tr>
<tr id="row67291124323"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p175361749141815"><a name="p175361749141815"></a><a name="p175361749141815"></a>SS528</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13835920181"><a name="p13835920181"></a><a name="p13835920181"></a>V100</p>
</td>
</tr>
<tr id="row8100161813432"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p16101181884320"><a name="p16101181884320"></a><a name="p16101181884320"></a>SS625</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p91011518114310"><a name="p91011518114310"></a><a name="p91011518114310"></a>V100</p>
</td>
</tr>
<tr id="row2044258578"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section169mcpsimp"></a>**

This document is primarily intended for:

-   Technical support engineers
-   Software development engineers

**Symbol Conventions<a name="section175mcpsimp"></a>**

The following symbols may appear in this document with the meanings described below.

<a name="table178mcpsimp"></a>
<table><thead align="left"><tr id="row183mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p185mcpsimp"><a name="p185mcpsimp"></a><a name="p185mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row189mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="figures/zh-cn_image_0000002441674941.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a>Indicates a high-risk hazard that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row194mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="figures/zh-cn_image_0000002408275526.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a>Indicates a medium-risk hazard that, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row199mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="figures/zh-cn_image_0000002408115658.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>Indicates a low-risk hazard that, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row204mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p206mcpsimp"><a name="p206mcpsimp"></a><a name="p206mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="figures/zh-cn_image_0000002408115554.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p208mcpsimp"><a name="p208mcpsimp"></a><a name="p208mcpsimp"></a>Conveys device or environmental safety warnings. Failure to follow this guidance may result in equipment damage, data loss, performance degradation, or other unpredictable outcomes.</p>
<p id="p209mcpsimp"><a name="p209mcpsimp"></a><a name="p209mcpsimp"></a>"Notice" does not involve personal injury.</p>
</td>
</tr>
<tr id="row210mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="figures/zh-cn_image_0000002441714741.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a>Provides supplementary information for key content in the text.</p>
<p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>"Note" is not a safety warning and does not involve personal, equipment, or environmental hazards.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section216mcpsimp"></a>**

The revision history accumulates descriptions of each document update. The latest version of this document incorporates all updates from previous versions.

<a name="table1557726816410"></a>
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
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First preliminary release.</p>
</td>
</tr>
</tbody>
</table>

# Boot Screen User Guide
## Feature Overview<a name="ZH-CN_TOPIC_0000002441714657"></a>

The Uboot code provides the following capabilities:

-   Enabling and disabling VO devices in the boot environment, covering typical VO interfaces and timings.
-   Enabling and disabling VO graphics layers in the boot environment.
-   Enabling and disabling VO video layers in the boot environment.
-   Hardware JPEG decoding to output YVU SEMI-PLANAR420 format images in the boot environment, for display via the VO video layer.
-   The VO graphics layer supports ARGB1555 format or 16-bit-depth BMP format. The default video layer display format is YVU SEMI-PLANAR420.

## Boot Command Line<a name="ZH-CN_TOPIC_0000002408275410"></a>

-   startvo: Start the VO device

    Parameters: device number, interface type, timing

    ```
    # help startvo 
    startvo   - open vo device with a certain output interface. 
              - startvo [dev intftype sync]
    ```

    -   <dev\>: Device number. See [Table 1](#_table48496300).
    -   <intftype\>: Interface type. See [Table 1](#_table48496300).
    -   <sync\>: Timing type

        ```
        0(PAL),          1(NTSC),         2(960H_PAL),     3(960H_NTSC)
        4(640x480_60),   5(480P60),       6(576P50),       7(800x600_60)
        8(1024x768_60),  9(720P50),       10(720P60),      11(1280x800_60)
        12(1280x1024_60),13(1366x768_60), 14(1400x1050_60),15(1440x900_60)
        16(1680x1050_60),17(1080P24),     18(1080P25),     19(1080P30)
        20(1080I50),     21(1080I60),     22(1080P50),     23(1080P60)
        24(1600x1200_60), 25(1920x1200_60),26(1920x2160_30),27(2560x1440_30)
        28(2560x1440_60),29(2560x1600_60),30(3840x2160_24),31(3840x2160_25)
        32(3840x2160_30),33(3840x2160_50),34(3840x2160_60),35(4096x2160_24)
        36(4096x2160_25),37(4096x2160_30),38(4096x2160_50),39(4096x2160_60)
        40(7680x4320_30),41(240x320_50),  42(320x240_50),  43(240x320_60)
        44(320x240_60),  45(800x600_50),  46(720x1280_60), 47(1080x1920_60)
        48(user)
        ```

    [Note]

    If the device is already enabled, calling this command will fail. Duplicate enabling is not supported.

-   stopvo: Stop the VO device

    Parameters: device number

    ```
    # help stopvo 
         stopvo - stopvo   - close interface of vo device.
                - stopvo [dev]
    ```

    <dev\>: Device number. See [Table 1](#_table48496300).

    [Note]

    All video layers on the device must be disabled before the device can be disabled.

-   startvl: Start the video layer

    Parameters: video layer number, image address (post-decode), stride, display position and size (x, y, w, h)

    ```
    # help startvl
    startvl - startvl   - open video layer.
               - startvl [layer addr stride x y w h]
    ```

    -   <layer\>: Video layer number. See [Table 1](#_table48496300).
    -   <addr\>: Image address.
    -   <stride\>: Image storage row width (stride).
    -   <x,y,w,h\>: Display position and size.

    [Note]

    The device bound to the video layer must be enabled before the video layer can be enabled.

-   stopvl: Stop the video layer

    Parameters: video layer number

    ```
    # help stopvl 
    stopvl - stopvl   - close video layer. 
                      - stopvl [layer]
    ```

    -   <layer\>: Video layer number. See [Table 1](#_table48496300).

-   startgx: Start the graphics layer

    Parameters: graphics layer number, image address, stride, display position and size (x, y, w, h), image type

    ```
    # help startgx 
    startgx - open graphics layer. 
    - startgx [layer addr stride x y w h type]
    ```

    -   <layer\>: Graphics layer number. See [Table 1](#_table48496300).
    -   <addr\>: Image address.
    -   <stride\>: Image storage row width (stride).
    -   <x,y,w,h\>: Display position and dimensions.
    -   <type\>: Image type. 0: ARGB1555 format; 1: 16-bit-depth BMP format.

    [Note]

    The device bound to the graphics layer must be enabled before the graphics layer can be enabled.

-   stopgx: Stop the graphics layer

    Parameters: graphics layer number

    ```
    # help stopgx 
    stopgx   - close graphics layer. 
             - stopgx [layer]
    ```

    -   <layer\>: Graphics layer number. See [Table 1](#_table48496300).

-   setvobg: Set the device background color

    Parameters: graphics layer number

    ```
    # help setvobg 
    setvobg - setvobg   - set vo background color. 
            - setvobg [dev color]
    ```

    -   <dev\>: Device number. See [Table 1](#_table48496300).
    -   <color\>: rgb color space

-   decjpg: Start JPEG decoding

    Parameters: decode output format

    ```
    # help decjpg 
    decjpg - jpgd   - decode jpeg picture. 
    - decjpg [format]
    ```

    -   <format\>: 0: semi-planar yvu420

        Using decjpg requires setting the environment variables `jpeg_addr`, `jpeg_size`, `jpeg_emar_buf`, and `vobuf`.

        `jpeg_addr`: address for storing the JPEG image bitstream;

        `jpeg_size`: size of the JPEG image bitstream;

        `jpeg_emar_buf`: buffer address used during JPEG decoding, size is 256 KB;

        `vobuf`: address where the decoded image output is stored.

        Example:

        ```
        #setenv jpeg_addr 0x90000000  
        #setenv jpeg_size 0xb85f9 
        #setenv jpeg_emar_buf 0x96000000 
        #setenv vobuf 0xa0000000
        ```

**Table 1** Solution differences

<a name="_table48496300"></a>
<table><thead align="left"><tr id="row332mcpsimp"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.1"><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>Solution</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.6.1.2"><p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>Device</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.3"><p id="p338mcpsimp"><a name="p338mcpsimp"></a><a name="p338mcpsimp"></a>Video Layer</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.6.1.4"><p id="p340mcpsimp"><a name="p340mcpsimp"></a><a name="p340mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.6.1.5"><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>Interface Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row344mcpsimp"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.1 "><p id="p346mcpsimp"><a name="p346mcpsimp"></a><a name="p346mcpsimp"></a>SS528V100/SS625V100</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.2 "><p id="p348mcpsimp"><a name="p348mcpsimp"></a><a name="p348mcpsimp"></a>{0,1,2}</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p350mcpsimp"><a name="p350mcpsimp"></a><a name="p350mcpsimp"></a>{0,1,3}</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p352mcpsimp"><a name="p352mcpsimp"></a><a name="p352mcpsimp"></a>{4,5,7}</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.6.1.5 "><p id="p354mcpsimp"><a name="p354mcpsimp"></a><a name="p354mcpsimp"></a>1: CVBS</p>
<p id="p355mcpsimp"><a name="p355mcpsimp"></a><a name="p355mcpsimp"></a>2: VGA</p>
<p id="p356mcpsimp"><a name="p356mcpsimp"></a><a name="p356mcpsimp"></a>8: BT.1120</p>
<p id="p357mcpsimp"><a name="p357mcpsimp"></a><a name="p357mcpsimp"></a>16: HDMI</p>
</td>
</tr>
<tr id="row358mcpsimp"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.1 "><p id="p360mcpsimp"><a name="p360mcpsimp"></a><a name="p360mcpsimp"></a>SS524V100</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.2 "><p id="p362mcpsimp"><a name="p362mcpsimp"></a><a name="p362mcpsimp"></a>{0,1,2}</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p364mcpsimp"><a name="p364mcpsimp"></a><a name="p364mcpsimp"></a>{0,1,3}</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p366mcpsimp"><a name="p366mcpsimp"></a><a name="p366mcpsimp"></a>{4,5,7}</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.6.1.5 "><p id="p368mcpsimp"><a name="p368mcpsimp"></a><a name="p368mcpsimp"></a>1: CVBS</p>
<p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>2: VGA</p>
<p id="p370mcpsimp"><a name="p370mcpsimp"></a><a name="p370mcpsimp"></a>4: BT.656</p>
<p id="p371mcpsimp"><a name="p371mcpsimp"></a><a name="p371mcpsimp"></a>8: BT.1120</p>
<p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>16: HDMI</p>
</td>
</tr>
<tr id="row373mcpsimp"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.1 "><p id="p375mcpsimp"><a name="p375mcpsimp"></a><a name="p375mcpsimp"></a>SS522V101</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.2 "><p id="p377mcpsimp"><a name="p377mcpsimp"></a><a name="p377mcpsimp"></a>{0, 2}</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p379mcpsimp"><a name="p379mcpsimp"></a><a name="p379mcpsimp"></a>{0, 3}</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p381mcpsimp"><a name="p381mcpsimp"></a><a name="p381mcpsimp"></a>{4, 7}</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.6.1.5 "><p id="p383mcpsimp"><a name="p383mcpsimp"></a><a name="p383mcpsimp"></a>1: CVBS</p>
<p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a>2: VGA</p>
<p id="p385mcpsimp"><a name="p385mcpsimp"></a><a name="p385mcpsimp"></a>4: BT.656</p>
<p id="p386mcpsimp"><a name="p386mcpsimp"></a><a name="p386mcpsimp"></a>8: BT.1120</p>
<p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>16: HDMI</p>
<p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>128: RGB_16BIT</p>
<p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>256: RGB_18BIT</p>
<p id="p390mcpsimp"><a name="p390mcpsimp"></a><a name="p390mcpsimp"></a>512: RGB_24BIT</p>
</td>
</tr>
<tr id="row391mcpsimp"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.1 "><p id="p393mcpsimp"><a name="p393mcpsimp"></a><a name="p393mcpsimp"></a>SS928V100</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.2 "><p id="p395mcpsimp"><a name="p395mcpsimp"></a><a name="p395mcpsimp"></a>{0, 1}</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>{0, 1}</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>{3, 4}</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.6.1.5 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>1: CVBS</p>
<p id="p402mcpsimp"><a name="p402mcpsimp"></a><a name="p402mcpsimp"></a>4: BT.656</p>
<p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>8: BT.1120</p>
<p id="p404mcpsimp"><a name="p404mcpsimp"></a><a name="p404mcpsimp"></a>16: HDMI</p>
<p id="p405mcpsimp"><a name="p405mcpsimp"></a><a name="p405mcpsimp"></a>32: RGB_6BIT</p>
<p id="p406mcpsimp"><a name="p406mcpsimp"></a><a name="p406mcpsimp"></a>64: RGB_8BIT</p>
<p id="p407mcpsimp"><a name="p407mcpsimp"></a><a name="p407mcpsimp"></a>128: RGB_16BIT</p>
<p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>256: RGB_18BIT</p>
<p id="p409mcpsimp"><a name="p409mcpsimp"></a><a name="p409mcpsimp"></a>512: RGB_24BIT</p>
<p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>1024: MIPI</p>
<p id="p411mcpsimp"><a name="p411mcpsimp"></a><a name="p411mcpsimp"></a>2048: MIPI_SLAVE</p>
</td>
</tr>
<tr id="row412mcpsimp"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.1 "><p id="p414mcpsimp"><a name="p414mcpsimp"></a><a name="p414mcpsimp"></a>SS626V100</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.2 "><p id="p416mcpsimp"><a name="p416mcpsimp"></a><a name="p416mcpsimp"></a>{0,1,2}</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p418mcpsimp"><a name="p418mcpsimp"></a><a name="p418mcpsimp"></a>{0,1,3}</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p420mcpsimp"><a name="p420mcpsimp"></a><a name="p420mcpsimp"></a>{4,5,8}</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.6.1.5 "><p id="p422mcpsimp"><a name="p422mcpsimp"></a><a name="p422mcpsimp"></a>1: CVBS</p>
<p id="p423mcpsimp"><a name="p423mcpsimp"></a><a name="p423mcpsimp"></a>2: VGA</p>
<p id="p424mcpsimp"><a name="p424mcpsimp"></a><a name="p424mcpsimp"></a>4: BT.656</p>
<p id="p425mcpsimp"><a name="p425mcpsimp"></a><a name="p425mcpsimp"></a>8: BT.1120</p>
<p id="p426mcpsimp"><a name="p426mcpsimp"></a><a name="p426mcpsimp"></a>16: HDMI</p>
<p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>4096: HDMI1</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **Note:** 
>-   For custom timing, modify the file `product\ot_osd\vo\arch\xxx\hal\drv_vo_dev.c`. The global variable `g_vo_user_sync_timing` configures the timing structure, and `g_vo_user_sync_info` configures clock-related information. For the configuration method of each member of this struct, refer to the `ot_vo_user_sync_info` data item in Chapter "4 Video Output" of the *MPP Media Processing Software V5.0 Developer Reference*.
>-   The HDMI interface does not support custom timing.
>-   If the BT.1120 interface is used for output, the user must develop the BT.1120 driver independently.
>-   Same-source output: for the method of configuring multiple interfaces to share the same source, and the timings supported for same-source output, refer to the `ot_vo_pub_attr` data item in Chapter "4 Video Output" of the *MPP Media Processing Software V5.0 Developer Reference*.
>-   Device and interface timings: for the timings supported by each device and interface, refer to the `ot_vo_pub_attr` data item in Chapter "4 Video Output" of the *MPP Media Processing Software V5.0 Developer Reference*.
>-   Pin multiplexing: for interfaces such as BT.1120, BT.656, VGA, and RGB, the user must independently configure the relevant pin multiplexing.
>-   For MIPI or MIPI_SLAVE output, device configuration: in non-custom-timing mode, the system matches a device configuration (stored as a global variable, e.g., `g_sample_comm_mipi_tx_1920x1080_60_config`) based on the second parameter `sync` of `do_start_mipi_tx` in `cmd/cmd_vo.c` (which defaults to the same value as the VO timing). Users can modify the device configuration as needed. In custom-timing mode, the user must populate the device configuration by filling in the `combo_dev_cfg` member of the `sample_mipi_tx_config` struct inside the `mipi_tx_display` function in `product\ot_osd\mipi_tx\xxx\sample_comm_mipi_tx.c`.
>-   For MIPI or MIPI_SLAVE output, peripheral configuration: if the peripheral does not need to be configured via MIPI (e.g., a bridge device), the system does not send any commands to the peripheral by default. If the peripheral must be configured via MIPI (e.g., a MIPI screen), the user must populate the screen configuration by filling in the `cmd_count` and `cmd_info` members of the `sample_mipi_tx_config` struct inside the `mipi_tx_display` function in `product\ot_osd\mipi_tx\xxx\sample_comm_mipi_tx.c`.
>-   The system's default VO and MIPI custom-timing configurations are provided for reference only. When using custom timing in actual applications, the VO and MIPI configurations must be modified and adapted to the actual hardware.
>-   Layer bindings: for the default device binding relationships for video and graphics layers, refer to the `ss_mpi_vo_bind_layer` interface in Chapter "4 Video Output" of the *MPP Media Processing Software V5.0 Developer Reference*.

## Boot Functions<a name="ZH-CN_TOPIC_0000002441714633"></a>

The following functions are available for user code to call in the boot environment:

-   startvo

    ```
    int start_vo(unsigned int dev, unsigned int type, unsigned int sync);
    ```

    **Note: for VO supported device numbers, see** [Table 1](#ZH-CN_TOPIC_0000002408275410).

-   stopvo

    ```
    int stop_vo(unsigned int dev);
    ```

-   startvl

    ```
    int start_videolayer(unsigned int layer, unsigned long addr, unsigned int strd, ot_rect layer_rect);
    ```

    **Notes:**

    -   **JPEG decoding uses hardware decoding; the output format is semi-planar yvu 420.**
    -   **`strd` can be obtained from the JPEG decode output; it is printed after running `decjpg`.**
    -   **`stride` must be 16-byte aligned; otherwise the image will display incorrectly.**
    -   **`addr` is the address of the semi-planar yvu 420 image (obtained by decoding or other means). When obtained by decoding, `addr` can be read from the `vobuf` environment variable. The Y component address defaults to `addr`; the C component address is calculated as: `c_addr = addr + stride * align(rect.height, 16)`. `addr` must be 16-byte aligned.**
    -   **Only Baseline bitstream decoding is supported.**
    -   **If the stride, width, and height of the image at `addr` do not match the parameters `strd`, `layer_rect.width`, and `layer_rect.height`, the image will display incorrectly.**
    -   **The video layer display region must not exceed the device display region; otherwise the image will display incorrectly.**
    -   **When the video layer display region width exceeds 3840, semi-planar yvu 420 cannot be supported. Since the boot screen only supports semi-planar yvu 420, the maximum supported boot screen display width is 3840.**

-   stopvl

    ```
    int stop_videolayer(unsigned int layer);
    ```

-   startgx

    ```
    int start_gx(unsigned int layer, unsigned long addr, unsigned int strd, ot_rect gx_rect, unsigned int type);
    ```

    **Notes:**

    -   **The graphics layer supports ARGB1555 and 16-bit-depth BMP formats. `type=0` loads ARGB1555 format; `type=1` loads 16-bit-depth BMP format. To display ARGB8888 format, the user must modify the code. When loading BMP format images, the image width must be 8-aligned and the image must be flipped vertically beforehand for correct display.**
    -   **`strd` is the number of bytes per row of image data, i.e., the stride.**
    -   **`stride` must be 16-byte aligned; otherwise the image will display incorrectly.**
    -   **When `type=0`, `addr` is the memory address of the image data and must be 16-byte aligned; otherwise the image will display incorrectly.**
    -   **When `type=1`, `addr` is the memory address of the image (including the file header and bitmap info header), and must satisfy `(addr + bfOffBits) % 16 = 0` — where `bfOffBits` is the `bfOffBits` member in the BMP file header (at offset 0xA), which skips the file and info headers to reach the pixel data. The resulting address must be 16-byte aligned.**
    -   **If the stride, width, and height of the image at `addr` do not match the parameters `strd`, `gx_rect.width`, and `gx_rect.height`, the image will display incorrectly.**
    -   **The graphics layer display region must not exceed the device display region; otherwise the image will display incorrectly.**

-   stopgx

    ```
    int stop_gx(unsigned int layer);
    ```

-   setvobg

    ```
    int set_vobg(unsigned int dev, unsigned int rgb);
    ```

    **Notes:**

    -   **This interface takes effect only if called before `startvo`. If called after `startvo`, it takes effect on the next `startvo` call.**
    -   **It is recommended to express `rgb` in 0xRRGGBB format for clarity.**

-   decjpg

    ```
    int jpeg_decode(unsigned int format);
    ```

    **Notes:**

    -   **`jpeg_decode` decodes the image into memory.**
    -   **This call requires four parameters: `jpeg_addr` is the source image memory address; `jpeg_size` is the image size in bytes; `jpeg_emar_buf` is the buffer address used during decoding; `vobuf` is the output address for the decoded image, also used as the starting address for the VO video layer display. All four parameters accept hexadecimal values only.**

## Source Code<a name="ZH-CN_TOPIC_0000002408275390"></a>

The boot screen implementation provides only basic functional functions. Users can configure them further based on their specific applications, especially the decode portion which can be made more flexible.

```
u-boot-2020.01
Makefile
Makefile-otproduct include/configs/xxx.h (or include/configs/xxx.h)  cmd/cmd_vo.c  cmd/cmd_dec.c  cmd/Makefile
cmd/Makefile-otproduct
u-boot-2020.01/product/ot_osd/include
ot_common.h  ot_common_video.h  ot_debug.h  ot_errno.h  ot_math.h  ot_type.h u-boot-2020.01/product/ot_osd/vo（only one level of directory content listed）
Makefile include/
mkp/
ext_inc/
arch/
u-boot-2020.01/product/ot_osd/dec（only one level of directory content listed）  ot_type.h
jpegd.c
jpegd_drv.c
jpegd_drv.h
jpegd_entry.c
jpegd_entry.h
jpegd_error.h
jpegd.h
jpegd_image.c
jpegd_image.h
jpegd_reg.h
mjpeg_func.h
mjpeg_idct.c
mjpeg_image.c
mjpeg_mcu.c
u-boot-2020.01/product/ot_osd/mipi_tx/xxx$ (or u-boot-2020.01/product/ot_osd/mipi_tx/xxx$)
ot_mipi_tx.h
ot_mipi_tx_mod_init.h
Makefile
mipi_tx.c
mipi_tx_def.h
mipi_tx.h
mipi_tx_hal.c
mipi_tx_hal.h
mipi_tx_reg.h
sample_comm_mipi_tx.c
type.h
```

>![](public_sys-resources/icon-note.gif) **Note:** 
>-   For SS528V100, replace "xxx" in the above paths with "ss528v100". MIPI_TX configuration under `product/ot_osd` is not supported.
>-   For SS625V100, replace "xxx" with "ss625v100". MIPI_TX configuration under `product/ot_osd` is not supported.
>-   For SS524V100, replace "xxx" with "ss524v100". MIPI_TX configuration under `product/ot_osd` is not supported.
>-   For SS522V101, replace "xxx" with "ss522v101". MIPI_TX configuration under `product/ot_osd` is not supported.
>-   For SS928V100, replace "xxx" with "ss928v100".
>-   For SS626V100, replace "xxx" with "ss626v100". MIPI_TX configuration under `product/ot_osd` is not supported.

## Command Line Example<a name="ZH-CN_TOPIC_0000002408115478"></a>

The following example uses SS528V100 to configure device DHD0 with HDMI interface and 1080p@60 timing output.

Note: DDR download addresses differ across solutions; use the address appropriate for your solution.

-   Set environment variables and configure JPEG decode parameters

    ```
     setenv jpeg_addr 0x92000000; 
     setenv jpeg_size 0x8f0b8; 
     setenv jpeg_emar_buf 0x96000000; 
     setenv vobuf 0xa0000000; 
     saveenv
    ```

-   Decode JPEG to memory

    ```
    decjpg  0
    ```

-   Configure and start the DHD0 device

    ```
    startvo 0 16 24
    ```

-   Start V0

    ```
    startvl 0 0xa0000000 1920 0 0 1920 1080
    ```

-   Stop V0

    ```
    stopvl 0
    ```

-   Stop the DHD0 device

    ```
    stopvo 0
    ```

## Hardware Decoding Support<a name="ZH-CN_TOPIC_0000002441674797"></a>

The boot screen supports hardware JPEG decoding. After hardware decoding outputs an image in **semi-planar yvu 420** format, the VO video layer can be configured to display it.

## Smooth Transition<a name="ZH-CN_TOPIC_0000002408115494"></a>

A smooth transition means switching from the boot screen to the application display without interrupting the video output. A smooth transition requires that the boot screen and the application display use the same interface and timing.

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>-   For HDMI smooth transitions, the HDMI attributes configured after entering the OS must match those configured for the boot screen in uboot.
>-   HDMI only supports smooth transitions for CEA (Consumer Electronics Association) timings.

For the HDMI interface, the supported smooth-transition timings are the intersection of the solution's supported timings and CEA timings. Some CEA timings are listed below:

```
5(480P60), 6(576P50), 9(720P50), 10(720P60), 18(1080P24), 19(1080P25),
20(1080P30), 23(1080P50), 24(1080P60), 30(3840x2160_24),
31(3840x2160_25), 32(3840x2160_30), 33(3840x2160_50), 34(3840x2160_60),
35(4096x2160_24), 36(4096x2160_25), 37(4096x2160_30), 38(4096x2160_50),
39(4096x2160_60)
```

## Notes<a name="ZH-CN_TOPIC_0000002441714641"></a>

-   After the boot screen starts, loading drivers during system runtime may be affected by `sys_config.ko`, the driver that configures CRG. If interference occurs, `sys_config.ko` must be modified.
-   When configuring the boot screen to display via the BT.1120 interface, a BT.1120-to-HDMI peripheral driver must be ported and implemented independently.
-   When configuring the boot screen to display via the BT.656 interface, a BT.656 peripheral driver must be ported and implemented independently.
-   When configuring the boot screen to display via the RGB interface, an RGB peripheral driver must be ported and implemented independently.
-   When configuring the boot screen to display via MIPI or MIPI_SLAVE interfaces, the corresponding peripheral drivers must be ported and implemented independently.
-   When the boot screen is displayed via HDMI and the system needs to continue displaying video content using the same HDMI format after boot, remove the `ss_mpi_hdmi_set_attr` step from the normal HDMI startup flow.
-   If custom HDMI hardware spec parameters are configured by the user after system startup (rather than using defaults), the same HDMI hardware spec parameters must also be set in the boot screen scenario using the relevant functions (`ss_mpi_hdmi_set_hw_spec`, `ss_mpi_hdmi_set_mod_param`).
-   For BT.1120, BT.656, RGB 6/8/16/18/24-bit, and MIPI_TX interface outputs, these interfaces use a large number of pins, and pin multiplexing may be complex. Some interface pins may conflict with pins used by other kernel modules. Users must analyze and resolve these conflicts in advance (e.g., by disabling the conflicting kernel modules). Otherwise, the boot screen display may be disrupted by the kernel startup process.
