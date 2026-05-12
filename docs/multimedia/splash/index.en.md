---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/开机画面使用指南/开机画面使用指南.md
---

# Preface
**Overview<a name="section142mcpsimp"></a>**

This document provides basic function calls and boot command lines for implementing a boot splash screen. Users can configure them according to their specific applications.

>![](../../multimedia/splash/public_sys-resources/icon-note.gif) **Note:** 
>Unless otherwise specified, SS927V100 and SS928V100, and SS522V100 and SS524V100, have identical content.

**Product Versions<a name="section145mcpsimp"></a>**

The product versions corresponding to this document are as follows.

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

This document (this guide) is primarily intended for the following engineers:

- Technical support engineers
- Software development engineers

**Symbol Conventions<a name="section175mcpsimp"></a>**

The following symbols may appear in this document. Their meanings are as follows.

<a name="table178mcpsimp"></a>
<table><thead align="left"><tr id="row183mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p185mcpsimp"><a name="p185mcpsimp"></a><a name="p185mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row189mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="/multimedia/splash/figures/zh-cn_image_0000002441674941.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a>Indicates a high-risk hazard that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row194mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="/multimedia/splash/figures/zh-cn_image_0000002408275526.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a>Indicates a medium-risk hazard that, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row199mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="/multimedia/splash/figures/zh-cn_image_0000002408115658.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>Indicates a low-risk hazard that, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row204mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p206mcpsimp"><a name="p206mcpsimp"></a><a name="p206mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="/multimedia/splash/figures/zh-cn_image_0000002408115554.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p208mcpsimp"><a name="p208mcpsimp"></a><a name="p208mcpsimp"></a>Used to convey equipment or environmental safety warning information. If not avoided, it may result in equipment damage, data loss, performance degradation, or other unpredictable results.</p>
<p id="p209mcpsimp"><a name="p209mcpsimp"></a><a name="p209mcpsimp"></a>"Notice" does not involve personal injury.</p>
</td>
</tr>
<tr id="row210mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="/multimedia/splash/figures/zh-cn_image_0000002441714741.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a>Supplementary explanation of key information in the main text.</p>
<p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>"Note" is not a safety warning and does not involve personal, equipment, or environmental harm.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section216mcpsimp"></a>**

The revision history accumulates descriptions of each document update. The latest version of the document contains the updates from all previous versions.

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Modification Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First provisional release.</p>
</td>
</tr>
</tbody>
</table>

# Boot Splash Screen User Guide
## Feature Overview<a name="ZH-CN_TOPIC_0000002441714657"></a>

The Uboot code provides the following features:

-   Starting and stopping VO devices in the boot environment, covering typical VO interfaces and timings.
-   Starting and stopping VO graphics layers in the boot environment.
-   Starting and stopping VO video layers in the boot environment.
-   JPEG hardware decoding in the boot environment to output YVU SEMI-PLANAR420 format images, displayed via the VO video layer.
-   The VO graphics layer supports display in ARGB1555 or 16-bit BMP format, and the video layer defaults to YVU SEMI-PLANAR420 display format.

## Boot Command Lines<a name="ZH-CN_TOPIC_0000002408275410"></a>

-   startvo: Start VO device

    Parameters: device number, interface type, timing

    ```
    # help startvo 
    startvo   - open vo device with a certain output interface. 
              - startvo [dev intftype sync]
    ```

    -   <dev\>: Device number, see [Table 1](#_table48496300)
    -   <intftype\>: Interface type, see [Table 1](#_table48496300)
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

    If the device is already enabled, calling this command will fail; repeated enabling is not supported.

-   stopvo: Stop VO device

    Parameter: device number

    ```
    # help stopvo 
         stopvo - stopvo   - close interface of vo device.
                - stopvo [dev]
    ```

    <dev\>: Device number, see [Table 1](#_table48496300)

    [Note]

    The video layer on the device must be disabled before the device itself.

-   startvl: Start video layer

    Parameters: video layer number, image address (after decoding), stride, display position and size (x,y,w,h)

    ```
    # help startvl
    startvl - startvl   - open video layer.
               - startvl [layer addr stride x y w h]
    ```

    -   <layer\>: Video layer number, see [Table 1](#_table48496300)
    -   <addr\>: Image address
    -   <stride\>: Image storage stride
    -   <x,y,w,h\>: Display position and size

    [Note]

    The device bound to the video layer must be in an enabled state before the video layer is enabled.

-   stopvl: Stop video layer

    Parameter: video layer number

    ```
    # help stopvl 
    stopvl - stopvl   - close video layer. 
                      - stopvl [layer]
    ```

    -   <layer\>: Video layer number, see [Table 1](#_table48496300)

-   startgx: Start graphics layer

    Parameters: graphics layer number, image address, stride, display position and size (x,y,w,h), image type

    ```
    # help startgx 
    startgx - open graphics layer. 
    - startgx [layer addr stride x y w h type]
    ```

    -   <layer\>: Graphics layer number, see [Table 1](#_table48496300)
    -   <addr\>: Image address
    -   <stride\>: Image storage stride
    -   <x,y,w,h\>: Display position and size
    -   <type\>: Image type, 0: ARGB1555 format, 1: 16-bit BMP format

    [Note]

    The device bound to the graphics layer must be in an enabled state before the graphics layer is enabled.

-   stopgx: Stop graphics layer

    Parameter: graphics layer number

    ```
    # help stopgx 
    stopgx   - close graphics layer. 
             - stopgx [layer]
    ```

    -   <layer\>: Graphics layer number, see [Table 1](#_table48496300)

-   setvobg: Set device background color

    Parameter: device number, color

    ```
    # help setvobg 
    setvobg - setvobg   - set vo background color. 
            - setvobg [dev color]
    ```

    -   <dev\>: Device number, see [Table 1](#_table48496300)
    -   <color\>: RGB color space

-   decjpg: Start JPEG decoding

    Parameter: decode output format

    ```
    # help decjpg 
    decjpg - jpgd   - decode jpeg picture. 
    - decjpg [format]
    ```

    -   <format\> : 0: semi-planar yvu420

        Using decjpg requires setting the environment variables jpeg_addr, jpeg_size, jpeg_emar_buf, and vobuf.

        jpeg_addr is the address where the raw JPEG image bitstream is stored;

        jpeg_size is the size of the raw JPEG image bitstream;

        jpeg_emar_buf is the buffer address used during JPEG decoding, with a size of 256 KB.

        vobuf is the storage address for the output image after JPEG decoding.

        Example:

        ```
        #setenv jpeg_addr 0x90000000  
        #setenv jpeg_size 0xb85f9 
        #setenv jpeg_emar_buf 0x96000000 
        #setenv vobuf 0xa0000000
        ```

**Table 1**  Solution differences

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

>![](../../multimedia/splash/public_sys-resources/icon-note.gif) **Note:** 
>-   If using user-defined timing, you need to modify the file: product\\ot_osd\\vo\\arch\\xxx\\hal\\drv_vo_dev.c or product\\ot_osd\\vo\\arch\\xxx\\hal\\drv_vo_dev.c. The global variable g_vo_user_sync_timing in this file is used to configure the timing structure, and g_vo_user_sync_info is used to configure clock-related information. For the configuration method of each member in this structure, see the ot_vo_user_sync_info data item in the "4 Video Output" chapter of the *MPP Media Processing Software V5.0 Development Reference*.
>-   HDMI interface does not support user-defined timing.
>-   If using BT.1120 interface output, the user needs to develop the BT.1120 driver themselves.
>-   Same-source output: For configuring same-source output across different interfaces and supported timings for same-source output, see the "ot_vo_pub_attr" data item in the "4 Video Output" chapter of the *MPP Media Processing Software V5.0 Development Reference*.
>-   Device and interface timing: For device- and interface-supported timings, see the "ot_vo_pub_attr" data item in the "4 Video Output" chapter of the *MPP Media Processing Software V5.0 Development Reference*.
>-   Pin multiplexing: Users need to configure pin multiplexing relationships themselves for interfaces such as BT.1120, BT.656, VGA, and RGB.
>-   If using MIPI or MIPI_SLAVE interface output, the "device configuration" for MIPI is as follows: When VO is in non-user-timing mode, the system matches a corresponding device configuration based on the second parameter sync of the function do_start_mipi_tx in cmd/cmd_vo.c (this value defaults to the VO timing value). This configuration is stored as a global variable (e.g., g_sample_comm_mipi_tx_1920x1080_60_config). Users can modify the device configuration as needed. When VO is in user-timing mode, users need to fill in the device configuration themselves in the mipi_tx_display function of product\\ot_osd\\mipi_tx\\xxx\\sample_comm_mipi_tx.c — filling the combo_dev_cfg member of the sample_mipi_tx_config structure.
>-   If using MIPI or MIPI_SLAVE interface output, the "peripheral configuration" for MIPI is as follows: When the peripheral does not need to be configured via MIPI (e.g., adapter devices), the system defaults to not sending any commands to the peripheral. When the peripheral needs to be configured via MIPI (e.g., MIPI screens), users need to fill in the screen configuration themselves in the mipi_tx_display function of product\\ot_osd\\mipi_tx\\xxx\\sample_comm_mipi_tx.c — filling the cmd_count and cmd_info members of the sample_mipi_tx_config structure.
>-   The default VO and MIPI configurations under user-defined timing are for reference only. In actual business use with user-defined timing, VO and MIPI configurations need to be modified and adapted according to actual conditions.
>-   Binding relationships: For the default device binding relationships between video layers and graphics layers, see the ss_mpi_vo_bind_layer interface in the "4 Video Output" chapter of the *MPP Media Processing Software V5.0 Development Reference*.

## Boot Functions<a name="ZH-CN_TOPIC_0000002441714633"></a>

The following functions are available for user coding in the boot environment:

-   startvo

    ```
    int start_vo(unsigned int dev, unsigned int type, unsigned int sync);
    ```

    **Note: For supported VO device numbers, see **[Table 1](#ZH-CN_TOPIC_0000002408275410)**.**

-   stopvo

    ```
    int stop_vo(unsigned int dev);
    ```

-   startvl

    ```
    int start_videolayer(unsigned int layer, unsigned long addr, unsigned int strd, ot_rect layer_rect);
    ```

    **Note**:

    -   **JPEG decoding uses hardware decoding, with output format: semi-planar yvu 420.**
    -   **strd can be obtained from JPEG decoding; after executing decjpg (command), stride is printed.**
    -   **stride must be 16-byte aligned; otherwise, the image will display incorrectly.**
    -   **addr is the address of a semi-planar yvu 420 format image (obtained via decoding or other means). When the image is obtained via decoding, the value of addr can be obtained from the environment variable vobuf. When the video layer displays, the Y component address defaults to addr, and the C component address is calculated as: c_addr = addr + stride * align(rect.height, 16). addr must be 16-byte aligned.**
    -   **Only Baseline bitstream decoding is supported.**
    -   **If the stride, width, or height of the image at address addr does not match the configured parameters strd, layer_rect.width, and layer_rect.height, the image will display incorrectly.**
    -   **The video layer display area must not exceed the device display area; otherwise, the image will display incorrectly.**
    -   **When the video layer display area width exceeds 3840, semi-planar yvu 420 is constrained and not supported. Currently, the boot splash screen only supports semi-planar yvu 420, so the maximum supported boot splash display area width is 3840.**

-   stopvl

    ```
    int stop_videolayer(unsigned int layer);
    ```

-   startgx

    ```
    int start_gx(unsigned int layer, unsigned long addr, unsigned int strd, ot_rect gx_rect, unsigned int type);
    ```

    **Note:**

    -   **The graphics layer supports displaying ARGB1555 format and 16-bit BMP format data. type 0 loads ARGB1555 format, type 1 loads 16-bit BMP format. If ARGB8888 format display is needed, users must modify the code themselves. When loading BMP format images, for normal display, the image width must be 8-aligned and the image must be vertically flipped beforehand.**
    -   **strd is the number of bytes occupied by one row of image data, i.e., stride.**
    -   **stride must be 16-byte aligned; otherwise, the image will display incorrectly.**
    -   **When type is 0, addr is the memory address of the image and must be 16-byte aligned; otherwise, the image will display incorrectly.**
    -   **When type is 1, addr is the memory address of the image (including file header and bitmap info header) and must satisfy (addr + bfOffBits) % 16 = 0 — addr + bfOffBits offsets the address addr by bfOffBits bytes (where bfOffBits refers to the bfOffBits member of the BMP file header information, at offset 0xA), to skip the file header and info header and obtain the actual image data address. The offset address must be 16-byte aligned.**
    -   **If the stride, width, or height of the image at address addr does not match the configured parameters strd, gx_rect.width, and gx_rect.height, the image will display incorrectly.**
    -   **The graphics layer display area must not exceed the device display area; otherwise, the image will display incorrectly.**

-   stopgx

    ```
    int stop_gx(unsigned int layer);
    ```

-   setvobg

    ```
    int set_vobg(unsigned int dev, unsigned int rgb);
    ```

    **Note:**

    -   **This interface takes effect only when set before startvo; if set after startvo, it takes effect on the next startvo call.**
    -   **It is recommended to express rgb in 0xRRGGBB format for clarity.**

-   decjpg

    ```
    int jpeg_decode(unsigned int format);
    ```

    **Note:**

    -   **jpeg_decode is used to decode images to memory.**
    -   **This call requires four parameters: jpeg_addr is the memory address where the source image is stored; jpeg_size is the image size in bytes; jpeg_emar_buf is the buffer address used during decoding; and vobuf is the address where the decoded image is stored, which is also the starting position for VO video layer display. These four parameters only support hexadecimal input.**

## Involved Code<a name="ZH-CN_TOPIC_0000002408275390"></a>

The boot splash screen only provides basic function calls. Users can configure according to specific applications, especially the decoding part which can be made more flexible.

```
u-boot-2020.01
Makefile
Makefile-otproduct include/configs/xxx.h (or include/configs/xxx.h)  cmd/cmd_vo.c  cmd/cmd_dec.c  cmd/Makefile
cmd/Makefile-otproduct
u-boot-2020.01/product/ot_osd/include
ot_common.h  ot_common_video.h  ot_debug.h  ot_errno.h  ot_math.h  ot_type.h u-boot-2020.01/product/ot_osd/vo (only one level of directory content listed)
Makefile include/
mkp/
ext_inc/
arch/
u-boot-2020.01/product/ot_osd/dec (only one level of directory content listed)  ot_type.h
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

>![](../../multimedia/splash/public_sys-resources/icon-note.gif) **Note:** 
>-   For SS528V100, replace the above "xxx" with "ss528v100", and mipi_tx configuration under product/ot_osd is not supported.
>-   For SS625V100, replace the above "xxx" with "ss625v100", and mipi_tx configuration under product/ot_osd is not supported.
>-   For SS524V100, replace the above "xxx" with "ss524v100", and mipi_tx configuration under product/ot_osd is not supported.
>-   For SS522V101, replace the above "xxx" with "ss522v101", and mipi_tx configuration under product/ot_osd is not supported.
>-   For SS928V100, replace the above "xxx" with "ss928v100".
>-   For SS626V100, replace the above "xxx" with "ss626v100", and mipi_tx configuration under product/ot_osd is not supported.

## Command Line Example<a name="ZH-CN_TOPIC_0000002408115478"></a>

The following example uses SS528V100 configuring device DHD0 with HDMI interface timing 1080p@60 output.

Special note: DDR download addresses vary by solution; use the DDR address appropriate for your solution.

-   Set environment variables for JPEG decoding parameters

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

-   Configure DHD0 device startup

    ```
    startvo 0 16 24
    ```

-   Configure V0 startup

    ```
    startvl 0 0xa0000000 1920 0 0 1920 1080
    ```

-   Stop V0

    ```
    stopvl 0
    ```

-   Stop DHD0 device

    ```
    stopvo 0
    ```

## Hardware Decoding Support<a name="ZH-CN_TOPIC_0000002441674797"></a>

The boot splash screen in uboot supports hardware decoding. After hardware decoding outputs **semi-planar yvu 420** format, it can be configured for VO video layer display.

## Smooth Transition<a name="ZH-CN_TOPIC_0000002408115494"></a>

Smooth transition refers to the seamless switch from the boot splash screen to the service screen without turning off the display output. Smooth transition requires the boot splash screen and the service screen to use the same interface and timing.

>![](../../multimedia/splash/public_sys-resources/icon-notice.gif) **Notice:** 
>-   HDMI smooth transition requires that after entering the system, the HDMI-related attribute configuration is consistent with the boot splash screen configuration in uboot.
>-   HDMI only supports smooth transition for CEA (Consumer Electronics Association) timings.

For the HDMI interface, the supported smooth transition timings are the intersection of the solution-supported timings and CEA timings. Some CEA timings are listed as follows:

```
5(480P60), 6(576P50), 9(720P50), 10(720P60), 18(1080P24), 19(1080P25),
20(1080P30), 23(1080P50), 24(1080P60), 30(3840x2160_24),
31(3840x2160_25), 32(3840x2160_30), 33(3840x2160_50), 34(3840x2160_60),
35(4096x2160_24), 36(4096x2160_25), 37(4096x2160_30), 38(4096x2160_50),
39(4096x2160_60)
```

## Precautions<a name="ZH-CN_TOPIC_0000002441714641"></a>

-   After the boot splash screen starts and drivers are loaded during system operation, it may be affected by the sys_config.ko driver that configures CRG. If affected, sys_config.ko needs to be modified.
-   When configuring the boot splash screen for display via BT.1120 interface, users need to port and implement the BT.1120-to-HDMI peripheral driver themselves.
-   When configuring the boot splash screen for display via BT.656 interface, users need to port and implement the BT.656 peripheral driver themselves.
-   When configuring the boot splash screen for display via RGB interface, users need to port and implement the RGB peripheral driver themselves.
-   When configuring the boot splash screen for display via MIPI or MIPI_SLAVE interface, users need to port and implement the MIPI or MIPI_SLAVE peripheral driver themselves.
-   If the boot splash screen is displayed via HDMI interface, after entering the system, to continue displaying video content while maintaining the boot splash screen format, the step of setting HDMI attributes (ss_mpi_hdmi_set_attr) must be removed from the normal HDMI startup flow.
-   If after system startup, the user manually configures HDMI hardware specification parameters instead of using the defaults, please use the relevant functions (ss_mpi_hdmi_set_hw_spec, ss_mpi_hdmi_set_mod_param) in the boot splash screen scenario to set the same HDMI hardware specification parameters.
-   When outputting via BT.1120, BT.656, RGB6/8/16/18/24-bit, or MIPI_TX interfaces, due to the large number of pins used by these interfaces, their pin multiplexing relationships may be complex. Certain pins of these interfaces may conflict with pins of some kernel modules. Users need to analyze and resolve these conflicts in advance, such as disabling kernel modules that conflict with the interface. Otherwise, the boot splash screen may display abnormally due to kernel boot process interference.
