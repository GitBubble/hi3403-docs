---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/hi3403/docs/zh-CN/BurnTool 工具使用指南/BurnTool 工具使用指南.md
---

# 前言
**概述<a name="section94015722114"></a>**

本文档主要介绍BurnTool烧写工具的使用方法，适用于一键烧写所有程序镜像到单板flash上的场景、单板已有boot可按地址烧写其他程序镜像到单板flash上的场景，以及在空板上只烧写boot到单板flash上的场景。

**产品版本<a name="section1241074213"></a>**

与本文档相对应的产品版本如下。

<a name="table16437719210"></a>
<table><thead align="left"><tr id="row75927132112"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p135997202113"><a name="p135997202113"></a><a name="p135997202113"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p145917742113"><a name="p145917742113"></a><a name="p145917742113"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row155916713213"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p13591471219"><a name="p13591471219"></a><a name="p13591471219"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p18594716219"><a name="p18594716219"></a><a name="p18594716219"></a>V100</p>
</td>
</tr>
<tr id="row113583017224"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p1083151018221"><a name="p1083151018221"></a><a name="p1083151018221"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p583114100228"><a name="p583114100228"></a><a name="p583114100228"></a>V100</p>
</td>
</tr>
<tr id="row165411745144415"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p881081984715"><a name="p881081984715"></a><a name="p881081984715"></a>SS524</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
<tr id="row131881816202318"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p61881616162312"><a name="p61881616162312"></a><a name="p61881616162312"></a>SS522</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p11189616192320"><a name="p11189616192320"></a><a name="p11189616192320"></a>V100</p>
</td>
</tr>
<tr id="row11407191494813"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p6427175519594"><a name="p6427175519594"></a><a name="p6427175519594"></a>SS528</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p64271955205915"><a name="p64271955205915"></a><a name="p64271955205915"></a>V100</p>
</td>
</tr>
<tr id="row20945431175910"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p1945203185916"><a name="p1945203185916"></a><a name="p1945203185916"></a>SS625</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p10945163175913"><a name="p10945163175913"></a><a name="p10945163175913"></a>V100</p>
</td>
</tr>
<tr id="row56503143253"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**读者对象<a name="section18436710211"></a>**

本文档（本指南）主要适用于以下工程师：

-   技术支持工程师
-   硬件开发工程师

**修订记录<a name="section1530582391712"></a>**

修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>文档版本</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>发布日期</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.06%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>修改说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.06%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>第1次临时版本发布。</p>
</td>
</tr>
</tbody>
</table>

# 概述
## 工具概述<a name="ZH-CN_TOPIC_0000002441889113"></a>

BurnTool工具主要是用于镜像烧写、镜像上载与烧片器镜像制作的多功能工具。

>![](public_sys-resources/icon-note.gif) **说明：**  当前工具只支持在64位操作系统上使用。

## 应用场景<a name="ZH-CN_TOPIC_0000002408329736"></a>

BurnTool工具三大主要功能的应用场景如下：

-   镜像烧写：应用于将镜像通过串口、网口或USB口烧写到对应Flash地址上；
-   镜像上载：应用于将Flash地址上数据通过DDR导出到PC上的文件中；
-   烧片器镜像制作：应用于将分区表中的镜像按照烧片器工具要求的格式打包成对应的镜像文件以供烧片器量产烧写。

## 烧写原理<a name="ZH-CN_TOPIC_0000002441768981"></a>

uboot烧写原理：BurnTool工具在开始烧写后，首选与bootrom进行交互，工具DDR参数传送到传到bootrom，即为uboot下载阶段5%处，然后初始化DDR，再把uboot传输到DDR中，uboot下载阶段100%处表示传输完毕，再从DDR启动uboot，uboot启动完成后，工具开始与uboot进行交互，发送烧写命令，将DDR中的uboot烧写到Flash对应地址中。

其他镜像分区烧写原理：其他镜像分区，如kernel，rootfs等分区，工具默认采用网口传输的方式，客户可选择裸烧和非裸烧两种方式进行烧写，裸烧即为在按分区烧写或按Emmc烧写中勾选uboot进行烧写，此时uboot会被烧写到Flash中，非裸烧即为不勾选uboot，仅勾选其他分区进行烧写，此时需要保证当前单板上已经存在uboot，烧写时工具会启动uboot，与其交互，通过向uboot发送TFTP命令与Write命令，完成烧写。

## 工具与单板器件匹配关系说明<a name="ZH-CN_TOPIC_0000002408169824"></a>

对不同的单板，BurnTool工具在功能与器件上的支持有所差异。具体支持情况如[表1](#_Ref382475342)所示。

**表 1**  工具与单板器件匹配关系说明

<a name="_Ref382475342"></a>
<table><thead align="left"><tr id="row630mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.16.1.1"><p id="p632mcpsimp"><a name="p632mcpsimp"></a><a name="p632mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" colspan="4" valign="top" id="mcps1.2.16.1.2"><p id="p634mcpsimp"><a name="p634mcpsimp"></a><a name="p634mcpsimp"></a>Flash类型</p>
</th>
<th class="cellrowborder" colspan="5" valign="top" id="mcps1.2.16.1.3"><p id="p636mcpsimp"><a name="p636mcpsimp"></a><a name="p636mcpsimp"></a>文件系统</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.16.1.4"><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>高级功能</p>
</th>
<th class="cellrowborder" colspan="3" valign="top" id="mcps1.2.16.1.5"><p id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>通用接口</p>
</th>
</tr>
<tr id="row641mcpsimp"><th class="cellrowborder" valign="top" id="mcps1.2.16.2.1"><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>Spi nor</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.2"><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>Spi Nand/Nand</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.3"><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>eMMC</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.4"><p id="p649mcpsimp"><a name="p649mcpsimp"></a><a name="p649mcpsimp"></a>Ufs</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.5"><p id="p651mcpsimp"><a name="p651mcpsimp"></a><a name="p651mcpsimp"></a>Yaffs</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.6"><p id="p653mcpsimp"><a name="p653mcpsimp"></a><a name="p653mcpsimp"></a>Jffs2</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.7"><p id="p655mcpsimp"><a name="p655mcpsimp"></a><a name="p655mcpsimp"></a>SquashFS</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.8"><p id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>UBI</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.9"><p id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>ext3/4</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.10"><p id="p661mcpsimp"><a name="p661mcpsimp"></a><a name="p661mcpsimp"></a>CA</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.11"><p id="p663mcpsimp"><a name="p663mcpsimp"></a><a name="p663mcpsimp"></a>Bad Check</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.12"><p id="p665mcpsimp"><a name="p665mcpsimp"></a><a name="p665mcpsimp"></a>串口</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.13"><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>网口</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.14"><p id="p671mcpsimp"><a name="p671mcpsimp"></a><a name="p671mcpsimp"></a>USB</p>
</th>
</tr>
</thead>
<tbody><tr id="row673mcpsimp"><td class="cellrowborder" valign="top" width="11.917614816045177%" headers="mcps1.2.16.1.1 mcps1.2.16.2.1 "><p id="p675mcpsimp"><a name="p675mcpsimp"></a><a name="p675mcpsimp"></a>SS928V100/SS927V100</p>
</td>
<td class="cellrowborder" valign="top" width="6.286853251391079%" headers="mcps1.2.16.1.2 mcps1.2.16.2.2 "><p id="p677mcpsimp"><a name="p677mcpsimp"></a><a name="p677mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="11.394402458267583%" headers="mcps1.2.16.1.2 mcps1.2.16.2.3 "><p id="p679mcpsimp"><a name="p679mcpsimp"></a><a name="p679mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="4.800265758657918%" headers="mcps1.2.16.1.2 mcps1.2.16.2.4 "><p id="p681mcpsimp"><a name="p681mcpsimp"></a><a name="p681mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.946349970932645%" headers="mcps1.2.16.1.2 mcps1.2.16.2.5 "><p id="p683mcpsimp"><a name="p683mcpsimp"></a><a name="p683mcpsimp"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="4.933145087617307%" headers="mcps1.2.16.1.3 mcps1.2.16.2.6 "><p id="p685mcpsimp"><a name="p685mcpsimp"></a><a name="p685mcpsimp"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.3 mcps1.2.16.2.7 "><p id="p687mcpsimp"><a name="p687mcpsimp"></a><a name="p687mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="7.39971763142596%" headers="mcps1.2.16.1.3 mcps1.2.16.2.8 "><p id="p689mcpsimp"><a name="p689mcpsimp"></a><a name="p689mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="4.3185781911801335%" headers="mcps1.2.16.1.3 mcps1.2.16.2.9 "><p id="p691mcpsimp"><a name="p691mcpsimp"></a><a name="p691mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="6.428037538410431%" headers="mcps1.2.16.1.3 mcps1.2.16.2.10 "><p id="p693mcpsimp"><a name="p693mcpsimp"></a><a name="p693mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.4 mcps1.2.16.2.11 "><p id="p695mcpsimp"><a name="p695mcpsimp"></a><a name="p695mcpsimp"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="7.507682086205462%" headers="mcps1.2.16.1.4 mcps1.2.16.2.12 "><p id="p697mcpsimp"><a name="p697mcpsimp"></a><a name="p697mcpsimp"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.5 mcps1.2.16.2.13 "><p id="p699mcpsimp"><a name="p699mcpsimp"></a><a name="p699mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.5 mcps1.2.16.2.14 "><p id="p701mcpsimp"><a name="p701mcpsimp"></a><a name="p701mcpsimp"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.5 "><p id="p703mcpsimp"><a name="p703mcpsimp"></a><a name="p703mcpsimp"></a>●</p>
</td>
</tr>
<tr id="row1586684215493"><td class="cellrowborder" valign="top" width="11.917614816045177%" headers="mcps1.2.16.1.1 mcps1.2.16.2.1 "><p id="p986704216496"><a name="p986704216496"></a><a name="p986704216496"></a>SS626V100</p>
</td>
<td class="cellrowborder" valign="top" width="6.286853251391079%" headers="mcps1.2.16.1.2 mcps1.2.16.2.2 "><p id="p188673423494"><a name="p188673423494"></a><a name="p188673423494"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="11.394402458267583%" headers="mcps1.2.16.1.2 mcps1.2.16.2.3 "><p id="p88672421494"><a name="p88672421494"></a><a name="p88672421494"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="4.800265758657918%" headers="mcps1.2.16.1.2 mcps1.2.16.2.4 "><p id="p1886774211492"><a name="p1886774211492"></a><a name="p1886774211492"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.946349970932645%" headers="mcps1.2.16.1.2 mcps1.2.16.2.5 "><p id="p1586754254915"><a name="p1586754254915"></a><a name="p1586754254915"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="4.933145087617307%" headers="mcps1.2.16.1.3 mcps1.2.16.2.6 "><p id="p286784264912"><a name="p286784264912"></a><a name="p286784264912"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.3 mcps1.2.16.2.7 "><p id="p14867442184910"><a name="p14867442184910"></a><a name="p14867442184910"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="7.39971763142596%" headers="mcps1.2.16.1.3 mcps1.2.16.2.8 "><p id="p5867242194914"><a name="p5867242194914"></a><a name="p5867242194914"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="4.3185781911801335%" headers="mcps1.2.16.1.3 mcps1.2.16.2.9 "><p id="p148671242104918"><a name="p148671242104918"></a><a name="p148671242104918"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="6.428037538410431%" headers="mcps1.2.16.1.3 mcps1.2.16.2.10 "><p id="p886734220496"><a name="p886734220496"></a><a name="p886734220496"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.4 mcps1.2.16.2.11 "><p id="p1686734264912"><a name="p1686734264912"></a><a name="p1686734264912"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="7.507682086205462%" headers="mcps1.2.16.1.4 mcps1.2.16.2.12 "><p id="p1867184224915"><a name="p1867184224915"></a><a name="p1867184224915"></a>○</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.5 mcps1.2.16.2.13 "><p id="p17867542104910"><a name="p17867542104910"></a><a name="p17867542104910"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.5 mcps1.2.16.2.14 "><p id="p3867942144912"><a name="p3867942144912"></a><a name="p3867942144912"></a>●</p>
</td>
<td class="cellrowborder" valign="top" width="5.813470641973257%" headers="mcps1.2.16.1.5 "><p id="p1586794234914"><a name="p1586794234914"></a><a name="p1586794234914"></a>○</p>
</td>
</tr>
</tbody>
</table>

注：●表示支持；○表示不支持。

## 环境准备<a name="ZH-CN_TOPIC_0000002408169800"></a>

BurnTool工具烧写的环境准备如下：

1.  PC与单板之间连接好串口、网线，且因工具烧写需要涉及到与bootrom交互，故单板硬件上bootrom\_sel需要设置为1，从bootrom启动。
2.  把位于SDK发布包中的ToolPlatform-X.X.X.zip（路径：$SDK\_DIR/ tools/windows/ToolPlatform），拷贝到PC上（PC要求安装Win7、Win10操作系统）的某个本地硬盘。
3.  解压ToolPlatform-X.X.X.zip，双击工具目录下的ToolPlatform.exe，打开ToolPlatform工具，如[图1](#_Ref427762404)所示。

    **图 1**  从ToolPlatform工具目录打开ToolPlatform工具<a name="_Ref427762404"></a>  
    ![](figures/从ToolPlatform工具目录打开ToolPlatform工具.png "从ToolPlatform工具目录打开ToolPlatform工具")

4.  在欢迎页中选择BurnTool工具，如[图2](#_Ref427762422)所示。

    **图 2**  选择BurnTool工具<a name="_Ref427762422"></a>  
    ![](figures/选择BurnTool工具.png "选择BurnTool工具")

5.  参数配置，选择连接单板所用的串口，选择PC端使用的网络IP地址，配置好单板的MAC地址、IP地址、子网掩码以及网关，配置如[图3](#fig58684616564)所示。

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >所选择的PC的服务器IP必须和单板的网络配置在同一个网段内，否则无法通过网口烧写除fastboot以外的其他镜像（fastboot镜像是通过串口烧写的）。

    **图 3**  参数设置<a name="fig58684616564"></a>  
    ![](figures/参数设置.png "参数设置")

# 按分区烧写
## 适用场景<a name="ZH-CN_TOPIC_0000002408329724"></a>

按分区烧写功能，适用于所有的单板，不管单板上有没有boot都适用。

## 烧写步骤<a name="ZH-CN_TOPIC_0000002441889129"></a>

具体烧写步骤如下：

1.  打开BurnTool后，切换到“Burn by Partition”页签，如[图1](#fig1560862365516)所示。

    **图 1**  BurnTool按分区烧写<a name="fig1560862365516"></a>  
    ![](figures/BurnTool按分区烧写.png "BurnTool按分区烧写")

    >![](public_sys-resources/icon-note.gif) **说明：** 
    >-   软件第一次打开时，软件会自动生成默认参数，当这些参数配置信息更改时，软件会自动记录更改后的最新值，在软件正常退出时，自动保存配置参数，下次启动时，使用最新配置参数，如软件遇到非法退出，软件的配置参数可能不会被正确保存，即最近一次的参数修改失效。
    >-   点击保存按钮，可以将当前板端的网络配置保存起来，点击加载按钮，可以从保存的结果中选择一组配置作为当前配置。
    >-   切换“默认采用XML所在路径”的勾选状态，若勾选，则优先在XML路径下查找该分区文件。若不勾选，则优先采用绝对路径查找该文件，若找不到，再尝试以在XML所在目录下查找该文件。
    >-   **XML是一个配置文件用于保存分区表信息的，可以将编辑的分区表使用工具上的Save按钮保存成一个XML文件，下次打开工具时，将XML导入进来，分区表信息就直接加载进来。**

2.  配置单板分区信息，点击浏览按钮![](figures/zh-cn_image_0000002408330452.png)，可选择已设置好的分区表信息的XML，载入到工具中，分区信息被加载，如[图2](#fig62556341)所示。

    **图 2**  配置单板分区信息<a name="fig62556341"></a>  
    ![](figures/配置单板分区信息.png "配置单板分区信息")

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >-   分区信息只用于烧写，并不决定单板真正的分区划分，单板真实的分区划分还是由单板的bootargs决定，请将此处的分区信息与单板bootargs指定的分区信息对应，否则可能会出错。
    >-   BurnTool支持分区路径不一致，支持远程烧写，即为烧写的镜像是远程路径下的镜像。
    >-   分区被选中，但未选择烧写文件时，此分区在烧写过程中将会被擦除。
    >-   如果需要将所有分区的文件打包成一个镜像烧写（对于nandflash，由于其本身特性特殊，如果文件系统分区是可读写的文件系统，则不能一起打包），则打包的文件必须要加载到fastboot分区进行烧写，并且镜像中需要包含fastboot，才可以正常烧写。因烧写fastboot分区是采用串口方式烧写，烧写速度较慢，故不推荐使用此种方法进行烧写。

    修改分区信息可以直接修改xml格式的分区信息文件，也可以在工具中修改，用鼠标点击需修改分区的所在列，即可修改，如[图3](#fig1406152918013)所示。

    **图 3**  编辑单板分区信息<a name="fig1406152918013"></a>  
    ![](figures/编辑单板分区信息.png "编辑单板分区信息")

    单击按钮![](figures/zh-cn_image_0000002441769937.jpg)，可以增加一行分区。可以在这一行修改分区名，选择flash类型以及是否需要文件系统以及文件系统的类型，还可以修改分区的起始地址和分区大小。

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >-   分区的起始地址和分区大小都是以KB或MB为单位，而且必须是flash块大小的整数倍，否则可能会出错。
    >-   分区的文件系统中jffs2不是特殊格式，直接选择none即可。

    -   单击按钮![](figures/zh-cn_image_0000002408330584.jpg)，可选择或改变该分区的烧写文件。
    -   单击按钮![](figures/zh-cn_image_0000002441769729.jpg)，可删除该分区信息。

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >这里fastboot分区无法被删除，而且fastboot分区名不能被修改，因为如果fastboot分区被删除或fastboot分区名被修改则无法实现一键烧写。

    -   单击按钮![](figures/zh-cn_image_0000002441890057.jpg)，选择所有要烧写的分区，进行一键烧写所有分区，再次单击按钮![](figures/zh-cn_image_0000002441890145.jpg)，则取消所有要烧写的分区，也可以点击复选框  ![](figures/zh-cn_image_0000002441889885.jpg)，选择相应的分区进行烧写。
    -   单击保存按钮![](figures/zh-cn_image_0000002441769905.png)，可以将编辑好的分区表保存为文件。

    >![](public_sys-resources/icon-note.gif) **说明：** 
    >-   单板分区信息在第一次打开工具时可能没有xml格式的分区信息文件，此时可以在工具界面中直接填写或修改来创建单板分区信息，创建完成后，在关闭ToolPlatform工具时，弹出如[图2](#fig1241812821916)对话框，会提醒是否保存分区信息，点击“确定”，在弹出的对话框中选择要保存分区信息的路径，输入要保存的文件名，就会保存为xml格式的分区信息，点击“取消”，则关闭工具且不保存分区信息。
    >-   创建完成后在切换工具时，弹出如[图5](#Figure2.6)话框，“确定”，在弹出的对话框中选择要保存分区信息的路径，输入要保存的文件名，就会保存为xml 格式的分区信息，点击“取消”，则切换视图且不保存分区信息。注意保存分区信息的文件名后缀必须为.xml格式，否则下次载入分区信息时可能会出错而无法正确载入分区信息。信息另存为如[图6](#Figure2.7)所示。

    **图 4**  关闭ToolPlatform工具时提醒是否保存分区信息界面<a name="Figure2.5"></a>  
    ![](figures/关闭ToolPlatform工具时提醒是否保存分区信息界面.png "关闭ToolPlatform工具时提醒是否保存分区信息界面")

    **图 5**  切换视图时提醒是否保存分区信息界面<a name="Figure2.6"></a>  
    ![](figures/切换视图时提醒是否保存分区信息界面.png "切换视图时提醒是否保存分区信息界面")

    **图 6**  分区信息保存界面<a name="Figure2.7"></a>  
    ![](figures/分区信息保存界面.png "分区信息保存界面")

    选中当前最后一行，点击新建![](figures/zh-cn_image_0000002441769857.jpg)得到新的最后一行，然后在该行长度一栏中输入“-”，再加入该行的分区名、文件系统以及文件的引用路径，在之后的烧写中即可计算出该行的长度，该长度为整个器件的剩余长度。如[图7](#fig99064111119)所示。

    **图 7**  新建单板分区信息后设置长度为“-”<a name="fig99064111119"></a>  
    ![](figures/新建单板分区信息后设置长度为--.png "新建单板分区信息后设置长度为--")

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >若用户在新建分区行时，未选中当前的最后一个分区，则新建的分区可能不是新的最后一个分区，则无法使用“-”来代表剩余长度。

3.  准备单板环境，选择一种传输方式，如[图8](#fig15452338171518)所示，如果单板处于通电状态，给单板下电。

    **图 8**  选择传输方式<a name="fig15452338171518"></a>  
    ![](figures/选择传输方式.png "选择传输方式")

    -   若选择网口，连接单板的串口和网口。
    -   若选择串口，连接单板的串口。

4.  烧写单板，点击烧写按钮![](figures/zh-cn_image_0000002441889961.png)，如[图9](#fig1659555711617)所示。

    **图 9**  点击烧写<a name="fig1659555711617"></a>  
    ![](figures/点击烧写.png "点击烧写")

5.  给单板上电，进入烧写过程，等待烧写完成。烧写过程如[图10](#fig297215536181)所示。

    **图 10**  烧写过程<a name="fig297215536181"></a>  
    ![](figures/烧写过程.png "烧写过程")

    烧写过程的信息会在如上的控制台中显示。如果发现烧写出错，请再次检查单板：

    -   串口选择是否正确。
    -   IP地址是否正确，是否被占用。
    -   是否有短接单板上的自举跳线。

6.  烧写完成，连接终端工具，重启单板。

## 制作Nand烧片器镜像<a name="ZH-CN_TOPIC_0000002408169740"></a>

BurnTool提供了制作Nand烧片器镜像的功能。配置好分区列表后，点击制作Nand烧片器镜像按钮![](figures/zh-cn_image_0000002408329812.png)，会弹出Nand烧片器镜像制作界面。如[图1](#fig106441654201914)所示。

**图 1**  制作Nand烧片器镜像界面<a name="fig106441654201914"></a>  
![](figures/制作Nand烧片器镜像界面.png "制作Nand烧片器镜像界面")

选择对话框中的各项数据以后（其中Randomization功能对8K及以上Page Size的器件开放），点击“Make”按钮，即可生成Nand烧片器的镜像。

>![](public_sys-resources/icon-notice.gif) **须知：** 
>-   填入或选择的各项参数，必须与单板启动信息（可以使用超级终端类软件捕捉单板的启动信息并查看）中对应项的数值一致或实际贴的器件参数匹配。
>-   若用户不勾选某个分区，或者不为勾选的分区指定烧写文件，则无法制作该分区的镜像文件。
>-   若为非yaffs分区制作镜像，则分区表中的文件系统一项不能指定为yaffs；为yaffs分区制作镜像时，文件系统必须指定为yaffs。否则，会导致做出的镜像不正确。

## 选中分区表单行点击跳转进入按地址烧写界面<a name="ZH-CN_TOPIC_0000002441768853"></a>

按分区烧写提供了携带子分区信息即分区的分区名、文件系统以及文件的引用路径和起始地址以及分区长度跳转到按地址烧写界面，并采用该分区的信息直接录入到按地址烧写信息栏中，方便用户使用。在按分区烧写界面中选中分区表中的一行，点击跳转按钮![](figures/zh-cn_image_0000002441769277.jpg)，即可跳转到按地址烧写界面中。如[图1](#fig19742104082116)与[图2](#fig1241812821916)所示。

**图 1**  选中单行，点击跳转<a name="fig19742104082116"></a>  
![](figures/选中单行-点击跳转.png "选中单行-点击跳转")

**图 2**  进入按地址烧写界面<a name="fig1241812821916"></a>  
![](figures/进入按地址烧写界面.png "进入按地址烧写界面")

>![](public_sys-resources/icon-notice.gif) **须知：** 
>在跳转前，用户必须选中需要跳转到按地址烧写页面的分区行，跳转按钮才会显示。

# 按地址烧写
## 适用场景<a name="ZH-CN_TOPIC_0000002408329660"></a>

单板已有boot。

## 烧写步骤<a name="ZH-CN_TOPIC_0000002441889077"></a>

具体烧写步骤如下：

1.  切换到“Burn by Address”页签，如[图1](#fig77356229246)所示。

    **图 1**  地址烧写界面<a name="fig77356229246"></a>  
    ![](figures/地址烧写界面.png "地址烧写界面")

1.  配置单板烧写信息，选择要烧写的 flash类型，设置烧写起始地址和长度，选择要烧写的文件，如[图2](#fig1355103942610)所示界面。

    **图 2**  配置单板烧写信息<a name="fig1355103942610"></a>  
    ![](figures/配置单板烧写信息.png "配置单板烧写信息")

2.  同2.2章节[3](#ZH-CN_TOPIC_0000002441889129)。
3.  单击烧写按钮![](figures/zh-cn_image_0000002441769249.png)，如[图3](#_Ref416783621)所示。

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >按地址烧写时，用户无需选择文件类型，只要选择自己想要烧写的文件即可。由于yaffs文件（带OOB数据）和其他类型文件（不带OOB数据）的格式不同，工具会根据选定的文件在后台自动区分文件类型（工具中区分为yaffs类型和None类型），然后根据不同的类型来执行相应的烧写，给单板上电，进入烧写过程，等待烧写完成，按地址烧写只有第一次点击烧写按钮时需要重新给单板上电，后续再烧写镜像时不需要重新给单板上电了。

    **图 3**  单击烧写<a name="_Ref416783621"></a>  
    ![](figures/单击烧写.png "单击烧写")

4.  给单板上电，进入烧写过程，等待烧写完成。烧写过程如[图4](#_Ref416783705)所示。

    **图 4**  烧写过程<a name="_Ref416783705"></a>  
    ![](figures/烧写过程-0.png "烧写过程-0")

    烧写过程的信息会在如上的“控制台”中打印输出。如果发现烧写出错，请再次检查单板：

    -   串口选择是否正确
    -   IP地址设置是否正确，是否被占用
    -   是否有短接单板上的自举跳线

    Erase操作和Burn操作类似，这里不再赘述。

5.  烧写完成，连接终端工具，重启单板。

## 上载步骤<a name="ZH-CN_TOPIC_0000002408329648"></a>

烧写和上载是两个逆反操作，烧写功能是将镜像文件烧录到单板上，而上载功能则是按照用户设置的起始地址和长度将这段区域的内容上载至PC。上载的具体步骤完全可以参考烧写步骤。这里列出两个和烧写步骤中不一样的地方，重复的地方不在累述。

1.  同3.2章节[1](#ZH-CN_TOPIC_0000002441889077)。
2.  同3.2章节[2](#ZH-CN_TOPIC_0000002441889077)。
3.  配置单板上载信息，选择要上载的flash类型，设置存储设备中待上载的起始地址及长度，并且设置上载后的保存文件。如[图1](#fig12876191611389)所示。

    **图 1**  上载信息<a name="fig12876191611389"></a>  
    ![](figures/上载信息.png "上载信息")

4.  同3.2章节[3](#ZH-CN_TOPIC_0000002441889077)。
5.  单击“upload”，如果待上载区域的镜像是fastboot，kernel，ubifs等请选择Data whithout OOB，如果镜像是yaffs，请选择Data with OOB。如[图2](#_Ref416783742)所示。

    **图 2**  选择数据类型<a name="_Ref416783742"></a>  
    ![](figures/选择数据类型.png "选择数据类型")

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >按地址上载时，用户需要明确指定要上载的数据类型。这一步操作是在用户点击“上载”按钮后的弹出对话框中完成的。如果用户在这一步选择错误，会导致上载后的数据跟原始的文件无法吻合。yaffs文件系统部分上载时，长度应该为pagesize + oobsize的倍数。

## 擦除步骤<a name="ZH-CN_TOPIC_0000002441889041"></a>

擦除功能是从指定地址开始将指定长度的内容从板端擦除。擦除的步骤同烧写步骤类似，这里列出两个和烧写步骤中不一样的地方，重复的地方不在累述。

1.  同3.2章节[1](#ZH-CN_TOPIC_0000002441889077)。
2.  同3.2章节[2](#ZH-CN_TOPIC_0000002441889077)。
3.  配置单板擦除信息，选择要擦除的flash类型，设置存储设备中待擦除的起始地址及长度。如[图1](#fig10547163316314)所示。

    **图 1**  擦除信息<a name="fig10547163316314"></a>  
    ![](figures/擦除信息.png "擦除信息")

4.  同3.2章节[3](#ZH-CN_TOPIC_0000002441889077)。
5.  单击“erase”，给单板上电，进入擦除过程，等待擦除完成。如[图2](#_Ref416783804)所示。

    **图 2**  擦除过程<a name="_Ref416783804"></a>  
    ![](figures/擦除过程.png "擦除过程")

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >擦除时，长度应该为blocksize的倍数。

# Boot烧写
## 适用场景<a name="ZH-CN_TOPIC_0000002408169760"></a>

单板上没有boot，和按地址烧写配合，可完成单板所有镜像的烧写。

## 烧写步骤<a name="ZH-CN_TOPIC_0000002408329636"></a>

具体烧写步骤如下：

1.  切换到“Burn Fastboot”页签，如[图1](#_Ref416783832)所示。

    **图 1**  Fastboot烧写界面<a name="_Ref416783832"></a>  
    ![](figures/Fastboot烧写界面.png "Fastboot烧写界面")

2.  配置串口，选择连接单板所用的串口，配置如[图2](#_Ref416783851)所示。

    **图 2**  串口选择<a name="_Ref416783851"></a>  
    ![](figures/串口选择.png "串口选择")

3.  配置Boot烧写信息，配置如[图3](#fig6981215103111)所示。

    **图 3**  配置boot 烧写信息<a name="fig6981215103111"></a>  
    ![](figures/配置boot-烧写信息.png "配置boot-烧写信息")

4.  准备单板环境，如果单板处于通电状态，请给单板下电；
5.  点击烧写按钮![](figures/zh-cn_image_0000002408170424.png)，如[图4](#fig1999382113211)所示。

    **图 4**  点击Burn<a name="fig1999382113211"></a>  
    ![](figures/点击Burn.png "点击Burn")

6.  给单板上电，进入烧写过程，等待烧写完成。烧写过程如[图5](#_Ref416783918)所示。

    **图 5**  烧写过程<a name="_Ref416783918"></a>  
    ![](figures/烧写过程-1.png "烧写过程-1")

    烧写过程的信息会在如上的“控制台”打印输出。如果发现烧写出错，请再次检查串口选择是否正确。

7.  烧写完成，连接终端工具，重启单板。

# eMMC烧写
## 适用场景<a name="ZH-CN_TOPIC_0000002441889025"></a>

适用场景如下：只适用于eMMC烧写，不管单板上有没有boot都适用，可实现一键烧写所有镜像。

## 烧写步骤<a name="ZH-CN_TOPIC_0000002408329704"></a>

具体烧写步骤如下：

1.  切换到“烧写eMMC”页签，如[图1](#fig10733727164915)所示。

    **图 1**  eMMC 烧写界面<a name="fig10733727164915"></a>  
    ![](figures/eMMC-烧写界面.png "eMMC-烧写界面")

    >![](public_sys-resources/icon-note.gif) **说明：** 
    >-   切换“默认采用XML所在路径”的勾选状态，若勾选，则优先在XML路径下查找该分区文件。若不勾选，则优先采用绝对路径查找该文件，若找不到，再尝试以在XML所在目录下查找该文件，该状态默认被勾选。
    >-   **XML是一个配置文件用于保存分区表信息的，可以将编辑的分区表使用工具上的Save按钮保存成一个XML文件，下次打开工具时，将XML导入进来，分区表信息就直接加载进来。**

1.  配置单板分区信息，点击“浏览”，可选择已设置好的分区表信息，载入工具中，如[图2](#fig19253651205117)所示界面。其中boot分区的器件类型是emmc和emmc0时，boot会被烧写进默认分区，其中emmc不会切换启动分区，emmc0会切换boot的启动分区为默认分区。boot分区的器件类型是emmc1和emmc2时，boot会被烧写进对应的boot1，boot2分区，会切换boot的启动分区为对应的boot1，boot2分区。

    **图 2**  配置单板分区信息<a name="fig19253651205117"></a>  
    ![](figures/配置单板分区信息-2.png "配置单板分区信息-2")

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >如果所有分区的文件打包成一个镜像烧写时（由于eMMC文件系统分区需要创建分区表，因此文件系统分区不同时，则不能一起打包，Android版本不存在此问题），此镜像必须要放到fastboot分区，而且此镜像中要包含fastboot，另外由于此时是采用串口方式烧写，烧写速度比较慢，要耐心等待。

    >![](public_sys-resources/icon-note.gif) **说明：** 
    >eMMC采用DOS分区格式，对于Ext3/4文件系统分区需要创建分区表信息，内核才可以正确识别Ext3/4 文件系统分区。

    要修改某个分区的信息可以直接修改保存为 xml格式的分区信息文件，也可以直接在工具中修改，如果要在工具中修改某个分区的信息，用鼠标点击这个分区所在的行，则会出现如[图3](#fig05531290513)所示。

    **图 3**  编辑单板分区信息<a name="fig05531290513"></a>  
    ![](figures/编辑单板分区信息-3.png "编辑单板分区信息-3")

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >分区的起始大小和分区大小都是以KB或MB为单位，而且必须是eMMC扇区大小的整数倍，否则可能会出错。

    -   单击按钮![](figures/zh-cn_image_0000002408170740.jpg)，可以增加一行分区。可以在这一行修改分区名、选择是否需要文件系统以及文件系统的类型，还可以修改分区的起始大小和分区大小。
    -   单击按钮![](figures/zh-cn_image_0000002408170832.jpg)，可选择或改变该分区的烧写文件。
    -   单击按钮![](figures/zh-cn_image_0000002408330712.jpg)，可删除改分区信息。注意：这里fastboot 分区无法被删除，而且fastboot 分区名不能被修改，因为如果fastboot 分区被删除或fastboot 分区名被修改则无法实现一键烧写。
    -   单击按钮![](figures/zh-cn_image_0000002441889837.jpg)，选择所有要烧写的分区，进行一键烧写所有分区，再次单击按钮![](figures/zh-cn_image_0000002408170596.jpg)  ，则取消所有要烧写的分区，也可以点击复选框![](figures/zh-cn_image_0000002408330496.jpg)，选择相应的分区进行烧写。
    -   单击按钮![](figures/zh-cn_image_0000002441769909.jpg)，可以将编辑好的分区表保存为文件。

    >![](public_sys-resources/icon-note.gif) **说明：** 
    >创建完成后在切换透视图时，弹出如图话框，“确定”，在弹出的对话框中选择要保存分区信息的路径，输入要保存的文件名，就会保存为xml 格式的分区信息，点击“取消”，则切换视图且不保存分区信息。注意保存分区信息的文件名后缀必须为.xml格式，否则下次载入分区信息时可能会出错而无法正确载入分区信息。信息另存为如[图6](#fig196451156109)所示。

    **图 4**  关闭BurnTool工具时提醒是否保存分区信息界<a name="fig0725202195510"></a>  
    ![](figures/关闭BurnTool工具时提醒是否保存分区信息界.png "关闭BurnTool工具时提醒是否保存分区信息界")

    **图 5**  切换视图时提醒是否保存分区信息界面<a name="fig13640113718555"></a>  
    ![](figures/切换视图时提醒是否保存分区信息界面-4.png "切换视图时提醒是否保存分区信息界面-4")

    信息另存为如[图6](#fig196451156109)所示。

    **图 6**  分区信息保存界面<a name="fig196451156109"></a>  
    ![](figures/分区信息保存界面-5.png "分区信息保存界面-5")

1.  同[2.2-3](#ZH-CN_TOPIC_0000002441889129)一样。
2.  烧写单板，点击烧写按钮![](figures/zh-cn_image_0000002408170564.png)，如[图7](#fig79197461111)所示。

    **图 7**  点击烧写<a name="fig79197461111"></a>  
    ![](figures/点击烧写-6.png "点击烧写-6")

1.  给单板上电，进入烧写过程，等待烧写完成。

    烧写过程的信息会在控制台中显示。

    -   串口选择是否正确。
    -   IP地址设置是否正确，地址是否被占用。
    -   是否有短接单板上的自举跳线。

2.  烧写完成，连接终端工具，重启单板。

## 制作烧片器镜像<a name="ZH-CN_TOPIC_0000002441768929"></a>

制作烧片器镜像功能可以将当前分区列表中选择的文件制作为烧片器镜像文件。配置好分区列表后，点击制作烧片器镜像按钮![](figures/zh-cn_image_0000002441890077.png)，在弹出的保存对话框中设置好文件路径，制作烧片器镜像就开始了，如[图1](#fig114434436368)所示。

**图 1**  制作烧片器镜像过程<a name="fig114434436368"></a>  
![](figures/制作烧片器镜像过程.png "制作烧片器镜像过程")

## 上载步骤<a name="ZH-CN_TOPIC_0000002408169712"></a>

上载功能不可用，单板不支持上载。

## 擦除步骤<a name="ZH-CN_TOPIC_0000002408169768"></a>

1.  切换到emmc页签，导入分区表信息，如[图1](#fig119011214321)。

    **图 1**  导入分区表<a name="fig119011214321"></a>  
    ![](figures/导入分区表.png "导入分区表")

2.  编辑boot器件类型，如[图2](#fig151791728173710)。器件类型是emmc，只会擦除默认分区，器件类型是emmc0，1，2，会将默认分区，boot1，boot2分区擦除。

    **图 2**  编辑boot器件类型<a name="fig151791728173710"></a>  
    ![](figures/编辑boot器件类型.png "编辑boot器件类型")

3.  点击擦除。如[图3](#fig17109141184016)

    **图 3**  点击擦除<a name="fig17109141184016"></a>  
    ![](figures/点击擦除.png "点击擦除")

# 合并镜像
## 适用场景<a name="ZH-CN_TOPIC_0000002408329680"></a>

适用场景如下：适用于SPI Flash中因存储空间较小，用户需要将多个小镜像合并为一个镜像，然后烧录到同一个block块中，从而节省flash空间的场景，也适用于将其他Flash类型的镜像合并为一个镜像。

例如，有fastboot，kernel两个镜像他们分别为500K，而spi的block大小为1M，那么如果将这两个镜像当做两个分区来烧写，板端烧写命令会使用到2个block块来占用，如果合并镜像后，就只需要占用单个block块即可，从而省了1M的Flash空间。

## 操作步骤<a name="ZH-CN_TOPIC_0000002408329692"></a>

具体烧写步骤如下：

1.  切换到“Merge Image”页签，如[图1](#_Ref416784461)所示。

    **图 1**  BurnTool合并镜像界面<a name="_Ref416784461"></a>  
    ![](figures/BurnTool合并镜像界面.png "BurnTool合并镜像界面")

2.  点击Browse按钮，加载分区表或点击![](figures/zh-cn_image_0000002408329860.png)按钮，手动新建分区表，如[图2](#fig1195161117453)所示。

    **图 2**  加载分区表<a name="fig1195161117453"></a>  
    ![](figures/加载分区表.png "加载分区表")

3.  点击Merging Image按钮，合并镜像，如[图3](#_Ref416784524)所示。

    **图 3**  合并镜像<a name="_Ref416784524"></a>  
    ![](figures/合并镜像.png "合并镜像")

# 首选项设置
## 命令设置<a name="ZH-CN_TOPIC_0000002441889057"></a>

BurnTool工具的串口发送命令超时可通过首选项进行设置，点击菜单栏中“窗口”-\>“首选项”进入首选项对话框，进入“BurnTool”下“命令设置”页面，如[图1](#_Ref416784561)所示。

**图 1**  命令设置页面<a name="_Ref416784561"></a>  
![](figures/命令设置页面.png "命令设置页面")

注: Timeout（ms）：用于串口发送命令响应超时。单位为ms。

## TFTP设置<a name="ZH-CN_TOPIC_0000002441768913"></a>

BurnTool工具的TFTP可通过首选项进行设置，点击菜单栏中“窗口”-\>“首选项”进入首选项对话框，进入“BurnTool”下的“TFTP设置”页面，如[图1](#_Ref416784544)所示。

**图 1**  TFTP设置页面<a name="_Ref416784544"></a>  
![](figures/TFTP设置页面.png "TFTP设置页面")

设置项：

-   TFTP速率：用于计算超时，根据传输文件的长度及设置的TFTP速率计算出超时。单位为byte/s。
-   处理丢包：勾选“处理丢包”按钮，连续丢包次数项可配置，在传输过程中若连续丢失的包达到最大连续丢包次数，则判定传输失败。若不勾选“处理丢包”按钮，连续丢包次数项不可配置，且不管传输过程中的丢包情况。
-   连续丢包次数：设置最大连续丢包次数。
-   TFTP重试次数：设置TFTP重试次数，若传输失败，将重试，达到重试设置次数后仍未成功，将停止。
-   TFTP无响应超时：设置TFTP无响应超时，传输过程中若在设置时间内无响应，则判定传输失败，单位为秒，默认值为10秒。

## 其他设置<a name="ZH-CN_TOPIC_0000002441889101"></a>



### BurnTool-Debug控制台设置<a name="ZH-CN_TOPIC_0000002441768885"></a>

BurnTool工具的Debug控制台可通过首选项进行设置。

1.  点击菜单栏中“窗口”-\>“首选项”进入首选项对话框，进入“BurnTool”页面，选中“Open Debug Mode”按钮，表示开启Debug控制台，如[图1](#_Ref410048637)所示。

    **图 1**  选中开启Debug控制台<a name="_Ref410048637"></a>  
    ![](figures/选中开启Debug控制台.png "选中开启Debug控制台")

2.  在开始烧写后，工具会自动创建Debug控制台，点击控制台右上角切换控制台按钮，选择切换控制台为“BurnTool-Debug”控制台，当前控制台就显示为Debug控制台，如[图2](#_Ref410048738)所示。

    **图 2**  切换BurnTool-Debug控制台<a name="_Ref410048738"></a>  
    ![](figures/切换BurnTool-Debug控制台.png "切换BurnTool-Debug控制台")

### 检查同一网段设置<a name="ZH-CN_TOPIC_0000002441768921"></a>

点击菜单栏中“窗口”-\>“首选项”进入首选项对话框，进入“BurnTool”页面，选中“Check whether the PC and Borad IP addresses are in the same network segment”按钮，如[图1](#_Ref410048821)所示，表示开启在烧写前检查PC与板端IP是否在同一网关，取消选中则表示不会在烧写前检查此项。

**图 1**  检查同一网段设置页面<a name="_Ref410048821"></a>  
![](figures/检查同一网段设置页面.png "检查同一网段设置页面")

# FAQ
## BurnTool烧写中出现TFTP超时提示时的解决办法<a name="ZH-CN_TOPIC_0000002408169704"></a>

**问题描述<a name="section9846741144918"></a>**

出现以下TFTP错误时，如[图1](#_Ref386011440)所示，该如何解决？

**图 1**  TFTP超时问题<a name="_Ref386011440"></a>  
![](figures/TFTP超时问题.png "TFTP超时问题")

**解决办法<a name="section05094512502"></a>**

解决此问题分以下四个方面：

-   检查BurnTool中网络配置是否正确，如[图2](#_Ref386011442)所示，首先检查服务器IP是否正确，若不正确点击重新加载，加载最新的PC端IP地址；然后检查子网掩码与网关是否配置正确，若正确，再检查板端IP地址是否被占用（使用ping命令，查看当前单板IP是否能够ping通，若不能则表示当前网络不通），再查看，将以上参数全部保证正确后再尝试重新烧写。

    **图 2**  检查网络配置是否正确<a name="_Ref386011442"></a>  
    ![](figures/检查网络配置是否正确.png "检查网络配置是否正确")

-   使用外置的tftpd32工具代替工具中内置的TFTP进行下载操作（参见“[如何使用外置的tftpd32进行镜像下载？](#ZH-CN_TOPIC_0000002441889093)”），若tftpd32也显示超时，则检查当前网络环境是否正常；
-   修改工具中TFTP参数设置，匹配当前网络环境，通过点击菜单栏上的“Window”-\>“Preferences”-\>“BurnTool”-\>“TFTP Setting”，如[图3](#_Ref386007685)所示，将“The number of consecutive packet loss”与“TFTP no response timeout”两个参数设置大一些，然后在进行烧写，查看是否正常。
-   检查是否关闭防火墙，若未关闭，需要关闭防火墙。

    **图 3**  修改TFTP设置<a name="_Ref386007685"></a>  
    ![](figures/修改TFTP设置.png "修改TFTP设置")

## 如何使用外置的tftpd32进行镜像下载？<a name="ZH-CN_TOPIC_0000002441889093"></a>

**问题描述<a name="section43891210195218"></a>**

如何使用外置的tftpd32进行镜像下载且需要注意什么？

**解决办法<a name="section9229816115214"></a>**

使用外部tftpd32步骤为：

1.  在烧写前打开tftpd32工具，并选择正确的PC端IP地址与将烧写的镜像所在目录，如[图1](#_Ref386011451)所示。

    **图 1**  配置tftpd32工具<a name="_Ref386011451"></a>  
    ![](figures/配置tftpd32工具.png "配置tftpd32工具")

1.  在BurnTool中正常点击烧写按钮，弹出提示框，如[图2](#_Ref386011453)所示，点击确认，开始烧写，当前就会使用外置的tftpd32进行镜像的下载，如[图3](#_Ref386011454)所示。

    **图 2**  提示内置TFTP启动失败，端口被外置tftpd32工具占<a name="_Ref386011453"></a>  
    ![](figures/提示内置TFTP启动失败-端口被外置tftpd32工具占.png "提示内置TFTP启动失败-端口被外置tftpd32工具占")

    **图 3**  外置tftpd32工具正在下载镜像<a name="_Ref386011454"></a>  
    ![](figures/外置tftpd32工具正在下载镜像.png "外置tftpd32工具正在下载镜像")

## BurnTool烧写Fastboot分区时，工具出现报错“Failed to send start frame”的解决办法<a name="ZH-CN_TOPIC_0000002408329668"></a>

**问题描述<a name="section17113181011420"></a>**

烧写Fastboot分区出现以下“Failed to send start frame”错误时，如[图1](#_Ref386011456)所示，我该怎么办？

**图 1**  “Failed to send start frame”报错信息<a name="_Ref386011456"></a>  
![](figures/Failed-to-send-start-frame-报错信息.png "Failed-to-send-start-frame-报错信息")

**解决办法<a name="section1951334642"></a>**

首先确认上一次点击烧写后，是否在15秒内给单板重新上电，若已经重新上电，则查看串口是否与单板接触良好，若连接正常，则检查BurnTool中是否选择了正确的串口号，如[图2](#_Ref386011460)所示，全部保证正确后，请重新进行烧写。

**图 2**  检查串口号是否选择正确<a name="_Ref386011460"></a>  
![](figures/检查串口号是否选择正确.png "检查串口号是否选择正确")

## BurnTool烧写Fastboot分区时，控制台只打印了一段“\#\#\#\#\#\#\#\#\#”后停止打印，且工具出现报错“Failed to send head frame”的解决办法<a name="ZH-CN_TOPIC_0000002408169788"></a>

**问题描述<a name="section1174175519"></a>**

烧写Fastboot分区控制台只打印了一段“\#\#\#\#\#\#\#\#\#”后停止打印，且工具出现报错“Failed to send head frame”时，如[图1](#_Ref386011462)所示，该如何解决？

**图 1**  “Failed to send head frame”报错信息<a name="_Ref386011462"></a>  
![](figures/Failed-to-send-head-frame-报错信息.png "Failed-to-send-head-frame-报错信息")

**解决办法<a name="section1286417136513"></a>**

此报错原因可能有以下两种：

-   烧写的Fastboot镜像与当前单板型号不匹配导致，请直接查看单板标记型号，明确单板型号后，请使用匹配当前芯片的SDK镜像重新进行烧写；
-   单板DDR有问题，无法正常进行DDR初始化操作。

## BurnTool烧写Fastboot分区时，工具出现报错“Failed to send data frame”的解决办法<a name="ZH-CN_TOPIC_0000002441768861"></a>

**问题描述<a name="section956919507512"></a>**

烧写Fastboot分区出现以下“Failed to send data frame”错误时，如[图1](#_Ref386011468)所示，我该怎么办？

**图 1**  “Failed to send data frame”报错信息<a name="_Ref386011468"></a>  
![](figures/Failed-to-send-data-frame-报错信息.png "Failed-to-send-data-frame-报错信息")

**解决办法<a name="section35233257619"></a>**

此报错原因可能是烧写Fastboot镜像时串口连接出现松动导致工具与单板进行交互时数据发送失败，请检查串口连接情况。

## BurnTool烧写Fastboot分区时，工具出现报错“Failed to execute command”的解决办法<a name="ZH-CN_TOPIC_0000002408169752"></a>

**问题描述<a name="section45431947769"></a>**

烧写Fastboot分区出现以下“Failed to execute command”错误时，如[图1](#_Ref386011469)所示，我该怎么办？

**图 1**  “Failed to execute command”报错信息<a name="_Ref386011469"></a>  
![](figures/Failed-to-execute-command-报错信息.png "Failed-to-execute-command-报错信息")

**解决办法<a name="section1426113619713"></a>**

此报错原因可能是当前Fastboot分区的Flash类型选择错误导致的，如[图2](#_Ref386011475)所示，重启单板查看单板当前“Flash”属性，如当前为eMMC，则需要使用按EMMC烧写，且Fastboot分区的Flash类型选择为emmc。

**图 2**  通过串口查看单板Flash信息<a name="_Ref386011475"></a>  
![](figures/通过串口查看单板Flash信息.png "通过串口查看单板Flash信息")

## 对于文件传输方式的选择，需要注意什么？<a name="ZH-CN_TOPIC_0000002408169696"></a>

**问题描述<a name="section290917257720"></a>**

在选择文件传输方式时，串口和网口之间的优缺点是什么？

**解决办法<a name="section15228123017718"></a>**

BurnTool工具的串口烧写功能是纯串口烧写，因烧写过程需给板端传送大量数据。而串口本身的传输速率较低，故用纯串口的方式烧写，效率会比较低，我们推荐用网口的方式进行烧写，纯串口的方式烧写非常稳定，若用户网络环境不稳定，可使用串口烧写。

## 按地址烧写界面，文件的长度要求？<a name="ZH-CN_TOPIC_0000002441889033"></a>

**问题描述<a name="section129616216810"></a>**

按地址烧写界面，文件的长度要求是什么？

**解决办法<a name="section14316972810"></a>**

擦除时，长度应该为blocksize的倍数；yaffs文件系统部分上载时，长度应该为pagesize + oobsize的倍数。

## 遇到点击烧写，断电重启后，不开始烧写，可能原因？<a name="ZH-CN_TOPIC_0000002441768873"></a>

**问题描述<a name="section879943317814"></a>**

在点击烧写，断电重启后，但是工具并没有开始烧写，是什么原因？

**解决办法<a name="section17459025490"></a>**

可能是串口选择错误或没有正常连接串口（请使用终端工具查看），请等待，控制台会打印出相关信息。

## 串口找不到或tftp启动失败或报tftp端口被占用的原因？<a name="ZH-CN_TOPIC_0000002408329620"></a>

**问题描述<a name="section15781328107"></a>**

在linux下使用时，串口找不到或tftp启动失败或报tftp端口被占用，可能的原因什么？

**解决办法<a name="section481113141014"></a>**

没有以root用户登录，无权限打开tftp服务或使用串口。报tftp端口被占用也有可能是其他软件占用了此端口。

## 烧写Nand时控制台打印pure data length和len\_incl\_bad分别是什么含义？<a name="ZH-CN_TOPIC_0000002408169776"></a>

**问题描述<a name="section9483135101011"></a>**

烧写Nand时控制台打印pure data length和len\_incl\_bad分别是什么含义？

**解决办法<a name="section15954111011116"></a>**

如[图1](#_Ref386007893)所示，其中pure data length表示实际烧写的数据长度，而len incl bad表示包含坏块的实际烧写占用的长度，以上两种长度均不包含oobSize长度。

**图 1**  控制台打印烧写命令反馈的烧写长度<a name="_Ref386007893"></a>  
![](figures/控制台打印烧写命令反馈的烧写长度.png "控制台打印烧写命令反馈的烧写长度")

## 单板DDR Training失败的情况下工具会有什么打印？<a name="ZH-CN_TOPIC_0000002408329624"></a>

**问题描述<a name="section1033016544115"></a>**

单板DDR Training失败的情况下工具会有什么打印？

**解决办法<a name="section2742102181210"></a>**

当单板出现DDR Training失败时，在烧写Fastboot分区时，会打印如[图1](#_Ref386011496)所示信息。

**图 1**  打印DDR Training失败信息<a name="_Ref386011496"></a>  
![](figures/打印DDR-Training失败信息.png "打印DDR-Training失败信息")

## 反馈BurnTool使用过程中出现问题时需要提供什么？<a name="ZH-CN_TOPIC_0000002408329640"></a>

**问题描述<a name="section4620102214128"></a>**

反馈BurnTool使用过程中出现问题时需要提供什么？

**解决办法<a name="section10510122714124"></a>**

使用BurnTool工具出现问题时，将控制台中打印内容通过控制台工具栏中导出按钮导出，反馈问题时一并反馈，将有助于问题的定位及解决。

## 如何查看是否有进程占用了tftp的69端口？<a name="ZH-CN_TOPIC_0000002408329684"></a>

**问题描述<a name="section1072719116131"></a>**

tftp命令总是报文件找不到，但实际所有的设置都是好的，原因是什么？如何查看是否有进程占用了tftp的69端口？

**解决办法<a name="section17557141213133"></a>**

可能存在后台进程占用了69端口。可以使用如下方法查看是否有进程占用。

在cmd命令行工具中输入，打印例如[图1](#_Ref413161493)所示。

netstat -ano -p udp

**图 1**  查看进程的端口占用<a name="_Ref413161493"></a>  
![](figures/查看进程的端口占用.png "查看进程的端口占用")

查看是否有进程占用了69端口，上图中可以看到pid为7696的进程占用了69端口。再使用如下命令查看7696进程的名称，打印例如[图2](#_Ref413161472)所示。

tasklist|findstr "7696"

**图 2**  查看指定PID的进程名称<a name="_Ref413161472"></a>  
![](figures/查看指定PID的进程名称.png "查看指定PID的进程名称")

然后在进程管理器中杀掉该进程即可。

## 如果是64位的PC且只安装了64位版本的JRE？<a name="ZH-CN_TOPIC_0000002441768865"></a>

**问题描述<a name="section234741210149"></a>**

PC安装了64位版本的JRE，打开ToolPlatform时报错，该怎么办？

**解决办法<a name="section16521321181418"></a>**

因ToolPlatform依赖32位JRE版本，故在使用ToolPlatform前，请先登录JRE官网，下载并安装对应JRE版本的Windows x86的版本，网址如下：[http://www.oracle.com/technetwork/java/javase/downloads/](http://www.oracle.com/technetwork/java/javase/downloads/)

另，ToolPlatform-XXX-4.0.15以后的版本已经内置JRE程序，无需再次安装JRE。

## 非中文语言系统无法烧写中文路径镜像<a name="ZH-CN_TOPIC_0000002441889049"></a>

**问题描述<a name="section1999915715158"></a>**

如果系统为非中文系统，工具传入中文路径系统是无法进行烧写的，查看语言系统的方法，在cmd下输入chcp命令即可查询，如图 查询windows语言系统方法所示，437表示为美国语言系统，如果是936，则表示中文语言系统。

**图 1**  查询windows语言系统方法<a name="_Ref4156611"></a>  
![](figures/查询windows语言系统方法.png "查询windows语言系统方法")

**解决办法<a name="section185019199156"></a>**

非中文语言系统不支持带中文路径的镜像，将烧写路径修改英文路径。

# 缩略语
<a name="table177mcpsimp"></a>
<table><tbody><tr id="row182mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p184mcpsimp"><a name="p184mcpsimp"></a><a name="p184mcpsimp"></a><strong id="b185mcpsimp"><a name="b185mcpsimp"></a><a name="b185mcpsimp"></a>A</strong></p>
</td>
</tr>
<tr id="row187mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p189mcpsimp"><a name="p189mcpsimp"></a><a name="p189mcpsimp"></a>AXI</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a>Advanced eXtensible Interface</p>
</td>
</tr>
<tr id="row195mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p197mcpsimp"><a name="p197mcpsimp"></a><a name="p197mcpsimp"></a><strong id="b198mcpsimp"><a name="b198mcpsimp"></a><a name="b198mcpsimp"></a>D</strong></p>
</td>
</tr>
<tr id="row200mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p202mcpsimp"><a name="p202mcpsimp"></a><a name="p202mcpsimp"></a>DDR</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p204mcpsimp"><a name="p204mcpsimp"></a><a name="p204mcpsimp"></a>Double Data Rate</p>
</td>
</tr>
<tr id="row208mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p210mcpsimp"><a name="p210mcpsimp"></a><a name="p210mcpsimp"></a><strong id="b211mcpsimp"><a name="b211mcpsimp"></a><a name="b211mcpsimp"></a>E</strong></p>
</td>
</tr>
<tr id="row213mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>eMMC</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p217mcpsimp"><a name="p217mcpsimp"></a><a name="p217mcpsimp"></a>Embedded MultiMediaCard</p>
</td>
</tr>
<tr id="row221mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p223mcpsimp"><a name="p223mcpsimp"></a><a name="p223mcpsimp"></a><strong id="b224mcpsimp"><a name="b224mcpsimp"></a><a name="b224mcpsimp"></a>G</strong></p>
</td>
</tr>
<tr id="row226mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p228mcpsimp"><a name="p228mcpsimp"></a><a name="p228mcpsimp"></a>GPIO</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p230mcpsimp"><a name="p230mcpsimp"></a><a name="p230mcpsimp"></a>General Purpose Input Output</p>
</td>
</tr>
<tr id="row234mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p236mcpsimp"><a name="p236mcpsimp"></a><a name="p236mcpsimp"></a><strong id="b237mcpsimp"><a name="b237mcpsimp"></a><a name="b237mcpsimp"></a>H</strong></p>
</td>
</tr>
<tr id="row239mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p241mcpsimp"><a name="p241mcpsimp"></a><a name="p241mcpsimp"></a>HDMI</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p243mcpsimp"><a name="p243mcpsimp"></a><a name="p243mcpsimp"></a>High Definition Multimedia Interface</p>
</td>
</tr>
<tr id="row247mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p249mcpsimp"><a name="p249mcpsimp"></a><a name="p249mcpsimp"></a><strong id="b250mcpsimp"><a name="b250mcpsimp"></a><a name="b250mcpsimp"></a>N</strong></p>
</td>
</tr>
<tr id="row252mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p254mcpsimp"><a name="p254mcpsimp"></a><a name="p254mcpsimp"></a>NAND</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p256mcpsimp"><a name="p256mcpsimp"></a><a name="p256mcpsimp"></a>NAND</p>
</td>
</tr>
<tr id="row260mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p262mcpsimp"><a name="p262mcpsimp"></a><a name="p262mcpsimp"></a><strong id="b263mcpsimp"><a name="b263mcpsimp"></a><a name="b263mcpsimp"></a>P</strong></p>
</td>
</tr>
<tr id="row265mcpsimp"><td class="cellrowborder" valign="top" width="23%"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a>PID</p>
</td>
<td class="cellrowborder" valign="top" width="77%"><p id="p269mcpsimp"><a name="p269mcpsimp"></a><a name="p269mcpsimp"></a>Process Identification</p>
</td>
</tr>
</tbody>
</table>

