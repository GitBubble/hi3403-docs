---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/开机画面使用指南/开机画面使用指南.md
---

# 前言
**概述<a name="section142mcpsimp"></a>**

本文为实现开机画面提供了基本的功能函数和boot命令行，用户可以根据具体应用进行配置。

>![](public_sys-resources/icon-note.gif) **说明：** 
>未有特殊说明，Hi3519AV200与Hi3403V100，SS522V100与SS524V100内容完全一致。

**产品版本<a name="section145mcpsimp"></a>**

与本文档相对应的产品版本如下。

<a name="table148mcpsimp"></a>
<table><thead align="left"><tr id="row153mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row159mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>Hi3403V100</p>
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
<tr id="row2044258578"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**读者对象<a name="section169mcpsimp"></a>**

本文档（本指南）主要适用于以下工程师：

-   技术支持工程师
-   软件开发工程师

**符号约定<a name="section175mcpsimp"></a>**

在本文中可能出现下列标志，它们所代表的含义如下。

<a name="table178mcpsimp"></a>
<table><thead align="left"><tr id="row183mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p185mcpsimp"><a name="p185mcpsimp"></a><a name="p185mcpsimp"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row189mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="/multimedia/splash/figures/zh-cn_image_0000002441674941.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
<tr id="row194mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="/multimedia/splash/figures/zh-cn_image_0000002408275526.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a>表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。</p>
</td>
</tr>
<tr id="row199mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="/multimedia/splash/figures/zh-cn_image_0000002408115658.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。</p>
</td>
</tr>
<tr id="row204mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p206mcpsimp"><a name="p206mcpsimp"></a><a name="p206mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="/multimedia/splash/figures/zh-cn_image_0000002408115554.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p208mcpsimp"><a name="p208mcpsimp"></a><a name="p208mcpsimp"></a>用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。</p>
<p id="p209mcpsimp"><a name="p209mcpsimp"></a><a name="p209mcpsimp"></a>“须知”不涉及人身伤害。</p>
</td>
</tr>
<tr id="row210mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="/multimedia/splash/figures/zh-cn_image_0000002441714741.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a>对正文中重点信息的补充说明。</p>
<p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>“说明”不是安全警示信息，不涉及人身、设备及环境伤害信息。</p>
</td>
</tr>
</tbody>
</table>

**修订记录<a name="section216mcpsimp"></a>**

修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>文档版本</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>发布日期</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>修改说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>第1次临时版本发布。</p>
</td>
</tr>
</tbody>
</table>

# 开机画面使用指南
## 功能简介<a name="ZH-CN_TOPIC_0000002441714657"></a>

Uboot代码提供功能如下：

-   提供boot环境下VO设备的开启和关闭，涵盖VO典型接口和时序。
-   提供boot环境下VO图形层的开启和关闭。
-   提供boot环境下VO视频层的开启和关闭。
-   提供boot环境下JPEG硬件解码输出YVU SEMI-PLANAR420格式图像，配合VO视频层显示。
-   VO图形层支持显示格式为ARGB1555或16位深BMP格式，视频层默认显示格式为YVU SEMI-PLANAR420。

## boot命令行<a name="ZH-CN_TOPIC_0000002408275410"></a>

-   startvo：启动VO设备

    参数：设备号，接口类型，时序

    ```
    # help startvo 
    startvo   - open vo device with a certain output interface. 
              - startvo [dev intftype sync]
    ```

    -   <dev\>：设备号，请参见[表1](#_table48496300)
    -   <intftype\>：接口类型，请参见[表1](#_table48496300)
    -   <sync\>：时序类型

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

    【注意】

    如果设备已经使能，调用此命令则失败，不支持重复使能。

-   stopvo：关闭VO设备

    参数：设备号

    ```
    # help stopvo 
         stopvo - stopvo   - close interface of vo device.
                - stopvo [dev]
    ```

    <dev\>：设备号，见[表1](#_table48496300)

    【注意】

    设备禁用前必须先禁用该设备上的视频层。

-   startvl：启动视频层

    参数：视频层号，图像地址（解码后），行宽，显示位置和大小（x,y,w,h）

    ```
    # help startvl
    startvl - startvl   - open video layer.
               - startvl [layer addr stride x y w h]
    ```

    -   <layer\>：视频层号，请参见[表1](#_table48496300)
    -   <addr\>：图像地址
    -   <stride\>：图像存储行宽（stride）
    -   <x,y,w,h\>：显示位置和大小

    【注意】

    视频层使能前必须保证该视频层所绑定的设备处于使能状态。

-   stopvl：关闭视频层

    参数：视频层号

    ```
    # help stopvl 
    stopvl - stopvl   - close video layer. 
                      - stopvl [layer]
    ```

    -   <layer\>：视频层号，请参见[表1](#_table48496300)

-   startgx：启动图形层

    参数：图形层号，图像地址，行宽，显示位置和大小（x,y,w,h），图像类型

    ```
    # help startgx 
    startgx - open graphics layer. 
    - startgx [layer addr stride x y w h type]
    ```

    -   <layer\>：图形层号，请参见[表1](#_table48496300)
    -   <addr\>：图像地址
    -   <stride\>：图像存储行宽（stride）
    -   <x,y,w,h\>：显示位置和宽高
    -   <type\>：图像类型，0：ARGB1555格式，1：16位深BMP格式

    【注意】

    图形层使能前必须保证该图形层所绑定的设备处于使能状态。

-   stopgx：关闭图形层

    参数：图形层号

    ```
    # help stopgx 
    stopgx   - close graphics layer. 
             - stopgx [layer]
    ```

    -   <layer\>：图形层号，请参见[表1](#_table48496300)

-   setvobg：设置设备背景色

    参数：图形层号

    ```
    # help setvobg 
    setvobg - setvobg   - set vo background color. 
            - setvobg [dev color]
    ```

    -   <dev\>：设备号，请参见[表1](#_table48496300)
    -   <color\>：rgb color space

-   decjpg：启动JPEG解码

    参数：解码输出格式

    ```
    # help decjpg 
    decjpg - jpgd   - decode jpeg picture. 
    - decjpg [format]
    ```

    -   <format\> : 0: semi-planar yvu420

        使用decjpg需要设置环境变量jpeg\_addr、jpeg\_size、jpeg\_emar\_buf、vobuf。

        jpeg\_addr是用于存放JPEG图片原始码流的地址；

        jpeg\_size是JPEG图片原始码流大小；

        jpeg\_emar\_buf是解码JPEG图片过程中使用到的buffer地址，大小为256KB。

        vobuf是解码JPEG图片后输出图像的存放地址。

        如：

        ```
        #setenv jpeg_addr 0x90000000  
        #setenv jpeg_size 0xb85f9 
        #setenv jpeg_emar_buf 0x96000000 
        #setenv vobuf 0xa0000000
        ```

**表 1**  解决方案差异

<a name="_table48496300"></a>
<table><thead align="left"><tr id="row332mcpsimp"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.6.1.1"><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.6.1.2"><p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>设备</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.3"><p id="p338mcpsimp"><a name="p338mcpsimp"></a><a name="p338mcpsimp"></a>视频层</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.6.1.4"><p id="p340mcpsimp"><a name="p340mcpsimp"></a><a name="p340mcpsimp"></a>图形层</p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.6.1.5"><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>接口类型</p>
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
<tr id="row391mcpsimp"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.6.1.1 "><p id="p393mcpsimp"><a name="p393mcpsimp"></a><a name="p393mcpsimp"></a>Hi3403V100</p>
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

>![](public_sys-resources/icon-note.gif) **说明：** 
>-   如果使用用户时序，则需要自行修改文件: product\\ot\_osd\\vo\\arch\\xxx\\hal\\drv\_vo\_dev.c或product\\ot\_osd\\vo\\arch\\xxx\\hal\\drv\_vo\_dev.c，该文件中全局变量g\_vo\_user\_sync\_timing用于配置时序结构，g\_vo\_user\_sync\_info用于配置时钟相关信息。该结构体中各成员配置方法见《MPP 媒体处理软件V5.0开发参考》中“4 视频输出”章节ot\_vo\_user\_sync\_info数据项。
>-   HDMI接口不支持用户时序。
>-   如果使用BT.1120接口输出，用户需要自行开发BT.1120驱动。
>-   同源输出：不同接口同源输出设置方法，同源输出支持时序见《MPP媒体处理软件V5.0开发参考.pdf》中“4 视频输出”章节“ot\_vo\_pub\_attr”数据项。
>-   设备和接口时序：设备和接口支持的时序见《MPP 媒体处理软件V5.0 开发参考》中“4 视频输出”章节“ot\_vo\_pub\_attr”数据项。
>-   管脚复用：接口BT.1120、BT.656、VGA、RGB等涉及到的管脚及其复用关系，用户需要自行配置。
>-   如果使用MIPI或者MIPI\_SLAVE接口输出，关于MIPI的 “设备配置”说明如下：VO为非用户时序情况下，根据cmd/cmd\_vo.c中函数do\_start\_mipi\_tx的第二个参数sync（该值默认与VO时序值一致），系统将匹配一个对应的设备配置（该配置以全局变量形式存在，如g\_sample\_comm\_mipi\_tx\_1920x1080\_60\_config），用户可根据需要自行修改设备配置；VO为用户时序情况下，需要用户在product\\ot\_osd\\mipi\_tx\\xxx\\ sample\_comm\_mipi\_tx.c文件的mipi\_tx\_display函数中自行填充设备配置——填充sample\_mipi\_tx\_config结构体的combo\_dev\_cfg成员。
>-   如果使用MIPI或者MIPI\_SLAVE接口输出，关于MIPI的 “外设配置”说明如下：外设不需要通过MIPI来配置的情况下（如转接设备），系统默认是不发送任何命令给外设的；外设需要通过MIPI来配置的情况下（如MIPI屏幕），需要用户在product\\ot\_osd\\mipi\_tx\\xxx\\ sample\_comm\_mipi\_tx.c文件的mipi\_tx\_display函数中自行填充屏幕配置——填充sample\_mipi\_tx\_config结构体的cmd\_count和cmd\_info成员。
>-   系统默认的VO和MIPI等用户时序下的配置仅供参考，实际业务中使用用户时序时，VO和MIPI等的配置，需要根据实际情况进行修改和适配。
>-   绑定关系：视频层和图形层的默认设备绑定关系见《MPP 媒体处理软件V5.0 开发参考》中“4 视频输出”章节ss\_mpi\_vo\_bind\_layer接口。

## boot函数<a name="ZH-CN_TOPIC_0000002441714633"></a>

以下函数可供用户在boot下编码调用：

-   startvo

    ```
    int start_vo(unsigned int dev, unsigned int type, unsigned int sync);
    ```

    **注意：vo支持的设备号见**[表1](#ZH-CN_TOPIC_0000002408275410)**。**

-   stopvo

    ```
    int stop_vo(unsigned int dev);
    ```

-   startvl

    ```
    int start_videolayer(unsigned int layer, unsigned long addr, unsigned int strd, ot_rect layer_rect);
    ```

    **注意**：

    -   **jpeg解码采用硬件解码，输出格式有：semi-planar yvu 420。**
    -   **strd可以从解码JPEG中获取，执行decjpg（命令）后有打印，即stride。**
    -   **stride需要16bytes对齐，否则图像将显示错误。**
    -   **addr即semi-planar yvu 420格式图像（通过解码或其他方式获得）的地址，通过解码获得图像时，可以从环境变量vobuf中获取addr的值。视频层显示时，y分量地址默认使用addr，c分量地址默认按照如下公式计算:c\_addr=addr+stride\*align\(rect.height, 16\)。addr需要满足16bytes对齐。**
    -   **仅支持Baseline码流解码**。
    -   **地址addr处图像的stride、宽、高与设置的参数strd、layer\_rect.width、layer\_rect.height不一致时图像将显示错误。**
    -   **视频层显示区域不允许超过设备显示区域，否则图像将显示错误。**
    -   **视频层显示区域宽超过3840时约束无法支持semi-planar yvu 420，目前开机画面只支持semi-planar yvu 420，所以开机画面显示区域宽度最大支持3840。**

-   stopvl

    ```
    int stop_videolayer(unsigned int layer);
    ```

-   startgx

    ```
    int start_gx(unsigned int layer, unsigned long addr, unsigned int strd, ot_rect gx_rect, unsigned int type);
    ```

    **注意：**

    -   **图形层支持显示ARGB1555格式和16位深BMP格式数据，type为0表示载入ARGB1555格式，type为1表示载入16位深BMP格式，需要显示ARGB8888格式时用户需自行修改代码。载入BMP格式图像时，为了正常显示图像，该图像宽度要求8对齐并且需要事先垂直翻转。**
    -   **strd为图像中一行数据占用的字节数，即stride。**
    -   **stride需要16bytes对齐，否则图像将显示错误。**
    -   **当type为0时，addr为图像所在的内存地址，需要满足16bytes对齐，否则图像将显示错误。**
    -   **当type为1时，addr为图像（含文件头和位图信息头）所在的内存地址，需要满足\(addr + bfOffBits\) % 16 = 0——addr+ bfOffBits 是将地址addr偏移bfOffBits个字节（其中bfOffBits表示BMP格式文件头信息中的bfOffBits成员，该成员的偏移是0xA），以跳过文件头和信息头直接得到图像数据所在的地址，偏移后的地址需满足16字节对齐。**
    -   **地址addr处图像的stride、宽、高与设置的参数strd、gx\_rect.width、gx\_rect.height不一致时图像将显示错误。**
    -   **图形层显示区域不允许超过设备显示区域，否则图像将显示错误。**

-   stopgx

    ```
    int stop_gx(unsigned int layer);
    ```

-   setvobg

    ```
    int set_vobg(unsigned int dev, unsigned int rgb);
    ```

    **注意：**

    -   **该接口需要在startvo前设置才生效；如果startvo后设置，则在下一次startvo时生效。**
    -   **建议rgb的表现形式使用0xRRGGBB格式，这样会更清晰。**

-   decjpg

    ```
    int jpeg_decode(unsigned int format);
    ```

    **注意：**

    -   **jpeg\_decode用于图像解码到内存中。**
    -   **这个调用需要用到四个参数，jpeg\_addr是用于存放源图像的内存地址；jpeg\_size是图像的大小，以字节为单位；jpeg\_emar\_buf是解码过程中使用到的buf地址；vobuf用于存放解码后的图像地址，也就是vo视频层用于显示的起始位置。这四个参数仅支持十六进制数输入。**

## 涉及代码<a name="ZH-CN_TOPIC_0000002408275390"></a>

该开机画面只提供了基本的功能函数，用户可以根据具体应用进行配置，尤其是解码部分可以做得更加灵活。

```
u-boot-2020.01
Makefile
Makefile-otproduct include/configs/xxx.h (或include/configs/xxx.h)  cmd/cmd_vo.c  cmd/cmd_dec.c  cmd/Makefile
cmd/Makefile-otproduct
u-boot-2020.01/product/ot_osd/include
ot_common.h  ot_common_video.h  ot_debug.h  ot_errno.h  ot_math.h  ot_type.h u-boot-2020.01/product/ot_osd/vo（仅列举一层目录内容）
Makefile include/
mkp/
ext_inc/
arch/
u-boot-2020.01/product/ot_osd/dec（仅列举一层目录内容）  ot_type.h
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
u-boot-2020.01/product/ot_osd/mipi_tx/xxx$（或u-boot-2020.01/product/ot_osd/mipi_tx/xxx$）
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

>![](public_sys-resources/icon-note.gif) **说明：** 
>-   对于SS528V100，上述“xxx”使用“ss528v100”代替，且不支持product/ot\_osd目录下mipi\_tx配置。
>-   对于SS625V100，上述“xxx”使用“ss625v100”代替，且不支持product/ ot\_osd目录下mipi\_tx配置。
>-   对于SS524V100，上述“xxx”使用“ss524v100”代替，且不支持product/ ot\_osd目录下mipi\_tx配置。
>-   对于SS522V101，上述“xxx”使用“ss522v101”代替，且不支持product/ ot\_osd目录下mipi\_tx配置。
>-   对于Hi3403V100，上述“xxx”使用“Hi3403V100”代替。
>-   对于SS626V100，上述“xxx”使用“ss626v100”代替，且不支持product/ ot\_osd目录下mipi\_tx配置。

## 命令行示例<a name="ZH-CN_TOPIC_0000002408115478"></a>

下面以SS528V100配置设备DHD0 HDMI接口的时序1080p@60输出为例。

特别说明：各解决方案DDR下载地址有所不同，根据解决方案来使用DDR地址。

-   设置环境变量，配置jpeg解码参数

    ```
     setenv jpeg_addr 0x92000000; 
     setenv jpeg_size 0x8f0b8; 
     setenv jpeg_emar_buf 0x96000000; 
     setenv vobuf 0xa0000000; 
     saveenv
    ```

-   解码JPEG到内存

    ```
    decjpg  0
    ```

-   配置DHD0设备启动

    ```
    startvo 0 16 24
    ```

-   配置V0启动

    ```
    startvl 0 0xa0000000 1920 0 0 1920 1080
    ```

-   关闭V0

    ```
    stopvl 0
    ```

-   关闭DHD0设备

    ```
    stopvo 0
    ```

## 支持硬件解码<a name="ZH-CN_TOPIC_0000002441674797"></a>

uboot下开机画面支持硬件解码，硬件解码输出**semi-planar yvu 420**格式后可配置VO视频层显示。

## 平滑过渡<a name="ZH-CN_TOPIC_0000002408115494"></a>

平滑过渡是指开机画面平滑切换至业务画面，期间不关闭显示输出。平滑过渡要求开机画面和业务画面使用相同的接口和时序。

>![](public_sys-resources/icon-notice.gif) **须知：** 
>-   HDMI平滑过渡要求进入系统后，HDMI相关属性配置和uboot中开机画面配置一致。
>-   HDMI只支持CEA（Consumer Electronics Association，消费电子协会）时序的平滑过渡。

对于HDMI接口，HDMI接口支持的平滑过渡时序取解决方案支持时序与CEA时序交集，部分CEA时序列举如下：

```
5(480P60), 6(576P50), 9(720P50), 10(720P60), 18(1080P24), 19(1080P25),
20(1080P30), 23(1080P50), 24(1080P60), 30(3840x2160_24),
31(3840x2160_25), 32(3840x2160_30), 33(3840x2160_50), 34(3840x2160_60),
35(4096x2160_24), 36(4096x2160_25), 37(4096x2160_30), 38(4096x2160_50),
39(4096x2160_60)
```

## 注意事项<a name="ZH-CN_TOPIC_0000002441714641"></a>

-   开机画面启动之后，在系统运行后加载驱动，可能会受到配置crg的驱动sys\_config.ko的影响，如果有影响，则需要修改sys\_config.ko。
-   配置开机画面通过BT.1120接口显示时，需要自行移植实现BT.1120转HDMI的外设驱动。
-   配置开机画面通过BT.656接口显示时，需要自行移植实现BT.656的外设驱动。
-   配置开机画面通过RGB接口显示时，需要自行移植实现RGB的外设驱动。
-   配置开机画面通过MIPI、MIPI\_SLAVE接口显示时，需要自行移植实现MIPI、MIPI\_SLAVE的外设驱动。
-   开机画面如果通过HDMI接口显示时，在进入系统后，如果需要保持开机画面的制式继续显示视频内容，需要在正常开启HDMI的流程中去掉设置hdmi属性（ss\_mpi\_hdmi\_set\_attr）的部分。
-   如果在系统启动后，用户自行配置了HDMI硬件指标参数，而不是使用默认的指标参数，请在开机画面场景下使用相关的函数\(ss\_mpi\_hdmi\_set\_hw\_spec, ss\_mpi \_hdmi\_set\_mod\_param\)设置相同的HDMI硬件指标参数。
-   BT.1120,BT.656,RGB6/8/16/18/24bit，MIPI\_TX接口输出时，由于这些接口使用到的管脚数量较多，管脚的复用关系可能较为复杂，接口的某些管脚可能与内核中某些模块的管脚存在冲突，用户需要提前分析并排除这些冲突，比如关闭内核中与接口存在冲突的模块。否则开机画面可能受内核启动过程的影响而显示异常。

