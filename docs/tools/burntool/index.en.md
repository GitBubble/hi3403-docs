---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/BurnTool 工具使用指南/BurnTool 工具使用指南.md
---

# Preface
**Overview<a name="section94015722114"></a>**

This document primarily introduces the usage of the BurnTool burning tool, applicable to scenarios including one-click burning of all program images to the board flash, burning other program images to the board flash by address when the board already has boot, and burning only boot to the board flash on an empty board.

**Product Version<a name="section1241074213"></a>**

The product versions corresponding to this document are as follows.

<a name="table16437719210"></a>
<table><thead align="left"><tr id="row75927132112"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p135997202113"><a name="p135997202113"></a><a name="p135997202113"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p145917742113"><a name="p145917742113"></a><a name="p145917742113"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row155916713213"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p13591471219"><a name="p13591471219"></a><a name="p13591471219"></a>Hi3403V100</p>
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
<tr id="row56503143253"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section18436710211"></a>**

This document (this guide) is primarily intended for the following engineers:

- Technical support engineers
- Hardware development engineers

**Revision History<a name="section1530582391712"></a>**

The revision history accumulates the description of each document update. The latest version of the document contains all update content from previous versions.

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.06%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Modification Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.06%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First temporary version release.</p>
</td>
</tr>
</tbody>
</table>

# Overview
## Tool Overview<a name="ZH-CN_TOPIC_0000002441889113"></a>

The BurnTool is a multifunctional tool primarily used for image burning, image uploading, and burner image creation.

>![](public_sys-resources/icon-note.gif) **Note:**  The current tool only supports use on 64-bit operating systems.

## Application Scenarios<a name="ZH-CN_TOPIC_0000002408329736"></a>

The application scenarios of the three main functions of the BurnTool are as follows:

- Image burning: used to burn images to the corresponding Flash addresses via serial port, network port, or USB port.
- Image uploading: used to export data from Flash addresses to files on the PC via DDR.
- Burner image creation: used to package images from the partition table into corresponding image files according to the format required by the burner tool for mass production burning.

## Burning Principle<a name="ZH-CN_TOPIC_0000002441768981"></a>

U-Boot burning principle: After the BurnTool starts burning, it first interacts with bootrom. The tool transmits DDR parameters to bootrom (this is the U-Boot download stage at 5%). It then initializes DDR and transfers U-Boot to DDR (the U-Boot download stage at 100% indicates transfer completion). U-Boot is then started from DDR. After U-Boot startup is complete, the tool begins interacting with U-Boot, sending burning commands to burn U-Boot from DDR to the corresponding Flash address.

Burning principle for other image partitions: For other image partitions, such as kernel, rootfs, etc., the tool defaults to network port transmission. Customers can choose between bare burning and non-bare burning methods. Bare burning means selecting U-Boot for burning in Burn by Partition or Burn by eMMC — at this time U-Boot will be burned to Flash. Non-bare burning means not selecting U-Boot and only selecting other partitions for burning. In this case, U-Boot must already exist on the current board. During burning, the tool will start U-Boot, interact with it, and complete burning by sending TFTP commands and Write commands to U-Boot.

## Tool and Board Device Matching Relationship<a name="ZH-CN_TOPIC_0000002408169824"></a>

For different boards, the BurnTool has differences in function and device support. The specific support situation is shown in [Table 1](#_Ref382475342).

**Table 1**  Tool and board device matching relationship

<a name="_Ref382475342"></a>
<table><thead align="left"><tr id="row630mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.16.1.1"><p id="p632mcpsimp"><a name="p632mcpsimp"></a><a name="p632mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" colspan="4" valign="top" id="mcps1.2.16.1.2"><p id="p634mcpsimp"><a name="p634mcpsimp"></a><a name="p634mcpsimp"></a>Flash Type</p>
</th>
<th class="cellrowborder" colspan="5" valign="top" id="mcps1.2.16.1.3"><p id="p636mcpsimp"><a name="p636mcpsimp"></a><a name="p636mcpsimp"></a>File System</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.16.1.4"><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>Advanced Features</p>
</th>
<th class="cellrowborder" colspan="3" valign="top" id="mcps1.2.16.1.5"><p id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>Common Interfaces</p>
</th>
</tr>
<tr id="row641mcpsimp"><th class="cellrowborder" valign="top" id="mcps1.2.16.2.1"><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>Spi nor</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.2"><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>Spi Nand/Nand</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.3"><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>eMMC</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.4"><p id="p649mcpsimp"><a name="p649mcpsimp"></a><a name="p649mcpsimp"></a>UFS</p>
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
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.12"><p id="p665mcpsimp"><a name="p665mcpsimp"></a><a name="p665mcpsimp"></a>Serial</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.13"><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>Network</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.14"><p id="p671mcpsimp"><a name="p671mcpsimp"></a><a name="p671mcpsimp"></a>USB</p>
</th>
</tr>
</thead>
<tbody><tr id="row673mcpsimp"><td class="cellrowborder" valign="top" width="11.917614816045177%" headers="mcps1.2.16.1.1 mcps1.2.16.2.1 "><p id="p675mcpsimp"><a name="p675mcpsimp"></a><a name="p675mcpsimp"></a>Hi3403V100/Hi3519AV200</p>
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

Note: ● indicates supported; ○ indicates not supported.

## Environment Preparation<a name="ZH-CN_TOPIC_0000002408169800"></a>

The environment preparation for BurnTool burning is as follows:

1.  Connect the serial port and network cable between the PC and the board. Since tool burning involves interaction with bootrom, the bootrom_sel on the board hardware must be set to 1 to boot from bootrom.
2.  Copy ToolPlatform-X.X.X.zip located in the SDK release package (path: $SDK_DIR/tools/windows/ToolPlatform) to a local hard drive on the PC (the PC requires Win7 or Win10 operating system).
3.  Extract ToolPlatform-X.X.X.zip, double-click ToolPlatform.exe in the tool directory to open the ToolPlatform tool, as shown in [Figure 1](#_Ref427762404).

    **Figure 1**  Opening the ToolPlatform tool from the ToolPlatform tool directory<a name="_Ref427762404"></a>  
    ![](figures/从ToolPlatform工具目录打开ToolPlatform工具.png "从ToolPlatform工具目录打开ToolPlatform工具")

4.  Select the BurnTool in the welcome page, as shown in [Figure 2](#_Ref427762422).

    **Figure 2**  Selecting the BurnTool<a name="_Ref427762422"></a>  
    ![](figures/选择BurnTool工具.png "选择BurnTool工具")

5.  Parameter configuration: select the serial port used to connect to the board, select the network IP address used by the PC, and configure the board's MAC address, IP address, subnet mask, and gateway, as shown in [Figure 3](#fig58684616564).

    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >The selected PC server IP must be in the same network segment as the board's network configuration; otherwise, images other than fastboot cannot be burned via the network port (the fastboot image is burned via the serial port).

    **Figure 3**  Parameter settings<a name="fig58684616564"></a>  
    ![](figures/参数设置.png "参数设置")
# Burn by Partition
## Applicable Scenarios<a name="ZH-CN_TOPIC_0000002408329724"></a>

The Burn by Partition function is applicable to all boards, regardless of whether boot is present on the board.

## Burning Steps<a name="ZH-CN_TOPIC_0000002441889129"></a>

The specific burning steps are as follows:

1.  After opening the BurnTool, switch to the "Burn by Partition" tab, as shown in [Figure 1](#fig1560862365516).

    **Figure 1**  BurnTool Burn by Partition<a name="fig1560862365516"></a>  
    ![](figures/BurnTool按分区烧写.png "BurnTool按分区烧写")
    >![](public_sys-resources/icon-note.gif) **Note:** 
    >-   When the software is first opened, it will automatically generate default parameters. When these parameter configuration information is changed, the software will automatically record the latest changed values. When the software exits normally, the configuration parameters are automatically saved. Upon next startup, the latest configuration parameters are used. If the software encounters an abnormal exit, the software's configuration parameters may not be correctly saved, meaning the most recent parameter modifications will be lost.
    >-   Click the Save button to save the current board-side network configuration. Click the Load button to select a set of configurations from the saved results as the current configuration.
    >-   Toggle the "Use XML path by default" checkbox state. If checked, the partition file is searched for in the XML path first. If unchecked, the absolute path is used to search for the file first. If the file is not found, the tool then tries to find it in the XML directory.
    >-   **XML is a configuration file used to save partition table information. The edited partition table can be saved as an XML file using the Save button on the tool. The next time the tool is opened, import the XML and the partition table information will be directly loaded.**

2.  Configure the board partition information. Click the browse button ![](figures/zh-cn_image_0000002408330452.png) to select an XML file with pre-configured partition table information and load it into the tool. The partition information will be loaded, as shown in [Figure 2](#fig62556341).

    **Figure 2**  Configuring board partition information<a name="fig62556341"></a>  
    ![](figures/配置单板分区信息.png "配置单板分区信息")
    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >-   The partition information is only used for burning and does not determine the actual partition layout of the board. The actual partition layout of the board is determined by the board's bootargs. Please ensure that the partition information here corresponds to the partition information specified by the board's bootargs; otherwise, errors may occur.
    >-   BurnTool supports inconsistent partition paths and remote burning, meaning the images to be burned can be images on remote paths.
    >-   If a partition is selected but no burning file is chosen, the partition will be erased during the burning process.
    >-   If all partition files need to be packaged into a single image for burning (for NAND flash, due to its special characteristics, if the file system partition is a read-write file system, they cannot be packaged together), the packaged file must be loaded into the fastboot partition for burning, and the image must contain fastboot to burn correctly. Since burning the fastboot partition uses the serial port method, which has a slower burning speed, this method is not recommended for burning.

    To modify partition information, you can directly modify the xml-format partition information file, or modify it in the tool by clicking on the column of the partition you want to modify, as shown in [Figure 3](#fig1406152918013).

    **Figure 3**  Editing board partition information<a name="fig1406152918013"></a>  
    ![](figures/编辑单板分区信息.png "编辑单板分区信息")

    Click the button ![](figures/zh-cn_image_0000002441769937.jpg) to add a row of partition. In this row, you can modify the partition name, select the flash type, whether a file system is needed and the file system type, and modify the partition start address and partition size.

    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >-   The partition start address and partition size are in KB or MB units and must be integer multiples of the flash block size; otherwise, errors may occur.
    >-   For the jffs2 file system in a partition, it is not a special format — simply select none.

    -   Click the button ![](figures/zh-cn_image_0000002408330584.jpg) to select or change the burning file for this partition.
    -   Click the button ![](figures/zh-cn_image_0000002441769729.jpg) to delete this partition information.

    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >The fastboot partition cannot be deleted here, and the fastboot partition name cannot be modified, because if the fastboot partition is deleted or its name is modified, one-click burning cannot be achieved.

    -   Click the button ![](figures/zh-cn_image_0000002441890057.jpg) to select all partitions to be burned for one-click burning of all partitions. Click the button again ![](figures/zh-cn_image_0000002441890145.jpg) to deselect all partitions to be burned. You can also click the checkbox ![](figures/zh-cn_image_0000002441889885.jpg) to select the corresponding partitions for burning.
    -   Click the save button ![](figures/zh-cn_image_0000002441769905.png) to save the edited partition table as a file.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >-   When the tool is first opened, there may not be an xml-format partition information file for the board partition information. In this case, you can directly fill in or modify the board partition information in the tool interface to create it. After creation, when closing the ToolPlatform tool, the dialog shown in [Figure 4](#Figure2.5) will appear, reminding you whether to save the partition information. Click "OK", and in the dialog that appears, select the path to save the partition information, enter the filename to save, and it will be saved as xml-format partition information. Click "Cancel" to close the tool without saving the partition information.
    >-   After creation, when switching tools, the dialog shown in [Figure 5](#Figure2.6) appears. Click "OK", and in the dialog that appears, select the path to save the partition information, enter the filename to save, and it will be saved as xml-format partition information. Click "Cancel" to switch views without saving the partition information. Note that the filename suffix for saving partition information must be .xml format; otherwise, the partition information may not be correctly loaded the next time. Saving partition information is shown in [Figure 6](#Figure2.7).

    **Figure 4**  Dialog reminding whether to save partition information when closing the ToolPlatform tool<a name="Figure2.5"></a>  
    ![](figures/关闭ToolPlatform工具时提醒是否保存分区信息界面.png "关闭ToolPlatform工具时提醒是否保存分区信息界面")

    **Figure 5**  Dialog reminding whether to save partition information when switching views<a name="Figure2.6"></a>  
    ![](figures/切换视图时提醒是否保存分区信息界面.png "切换视图时提醒是否保存分区信息界面")

    **Figure 6**  Partition information save interface<a name="Figure2.7"></a>  
    ![](figures/分区信息保存界面.png "分区信息保存界面")

    Select the current last row, click New ![](figures/zh-cn_image_0000002441769857.jpg) to get a new last row, then enter "-" in the length column of that row, add the partition name, file system, and file reference path for that row. During subsequent burning, the length of this row can be calculated as the remaining length of the entire device. This is shown in [Figure 7](#fig99064111119).

    **Figure 7**  Setting length to "-" after creating new board partition information<a name="fig99064111119"></a>  
    ![](figures/新建单板分区信息后设置长度为--.png "新建单板分区信息后设置长度为--")
    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >If the user does not select the current last partition when creating a new partition row, the newly created partition may not be the new last partition, and "-" cannot be used to represent the remaining length.

3.  Prepare the board environment, select a transmission method, as shown in [Figure 8](#fig15452338171518). If the board is powered on, power it off.

    **Figure 8**  Selecting the transmission method<a name="fig15452338171518"></a>  
    ![](figures/选择传输方式.png "选择传输方式")
    -   If selecting the network port, connect the board's serial port and network port.
    -   If selecting the serial port, connect the board's serial port.

4.  Burn the board. Click the burn button ![](figures/zh-cn_image_0000002441889961.png), as shown in [Figure 9](#fig1659555711617).

    **Figure 9**  Clicking Burn<a name="fig1659555711617"></a>  
    ![](figures/点击烧写.png "点击烧写")

5.  Power on the board, enter the burning process, and wait for burning to complete. The burning process is shown in [Figure 10](#fig297215536181).

    **Figure 10**  Burning process<a name="fig297215536181"></a>  
    ![](figures/烧写过程.png "烧写过程")

    Information about the burning process will be displayed in the console above. If a burning error is found, please check the board again:

    -   Whether the serial port selection is correct.
    -   Whether the IP address is correct and whether it is occupied.
    -   Whether the bootstrap jumper on the board is shorted.

6.  After burning is complete, connect the terminal tool and restart the board.

## Creating NAND Burner Images<a name="ZH-CN_TOPIC_0000002408169740"></a>

BurnTool provides the function of creating NAND burner images. After configuring the partition list, click the Create NAND Burner Image button ![](figures/zh-cn_image_0000002408329812.png), and the NAND Burner Image Creation interface will appear, as shown in [Figure 1](#fig106441654201914).

**Figure 1**  NAND Burner Image Creation interface<a name="fig106441654201914"></a>  
![](figures/制作Nand烧片器镜像界面.png "制作Nand烧片器镜像界面")

After selecting the various data in the dialog box (the Randomization function is available for devices with 8K and above Page Size), click the "Make" button to generate the NAND burner image.

>![](public_sys-resources/icon-notice.gif) **Important:** 
>-   The parameters entered or selected must be consistent with the corresponding item values in the board boot information (which can be captured and viewed using terminal software such as HyperTerminal) or match the actual device parameters installed.
>-   If the user does not select a partition, or does not specify a burning file for a selected partition, the image file for that partition cannot be created.
>-   If creating an image for a non-yaffs partition, the file system item in the partition table must not be specified as yaffs. When creating an image for a yaffs partition, the file system must be specified as yaffs. Otherwise, the resulting image will be incorrect.

## Selecting a Single Row in the Partition Table to Jump to the Burn by Address Interface<a name="ZH-CN_TOPIC_0000002441768853"></a>

Burn by Partition provides the ability to carry sub-partition information, i.e., the partition name, file system, file reference path, start address, and partition length, to jump to the Burn by Address interface, and use the partition's information to directly populate the Burn by Address information fields for user convenience. In the Burn by Partition interface, select a row in the partition table and click the jump button ![](figures/zh-cn_image_0000002441769277.jpg) to jump to the Burn by Address interface. This is shown in [Figure 1](#fig19742104082116) and [Figure 2](#fig1241812821916).

**Figure 1**  Selecting a single row and clicking jump<a name="fig19742104082116"></a>  
![](figures/选中单行-点击跳转.png "选中单行-点击跳转")

**Figure 2**  Entering the Burn by Address interface<a name="fig1241812821916"></a>  
![](figures/进入按地址烧写界面.png "进入按地址烧写界面")
>![](public_sys-resources/icon-notice.gif) **Important:** 
>Before jumping, the user must select the partition row that needs to jump to the Burn by Address page; only then will the jump button appear.

# Burn by Address
## Applicable Scenarios<a name="ZH-CN_TOPIC_0000002408329660"></a>

The board already has boot.

## Burning Steps<a name="ZH-CN_TOPIC_0000002441889077"></a>

The specific burning steps are as follows:

1.  Switch to the "Burn by Address" tab, as shown in [Figure 1](#fig77356229246).

    **Figure 1**  Burn by Address interface<a name="fig77356229246"></a>  
    ![](figures/地址烧写界面.png "地址烧写界面")

1.  Configure the board burning information: select the flash type to burn, set the burning start address and length, and select the file to burn, as shown in [Figure 2](#fig1355103942610).

    **Figure 2**  Configuring board burning information<a name="fig1355103942610"></a>  
    ![](figures/配置单板烧写信息.png "配置单板烧写信息")

2.  Same as section 2.2 step [3](#ZH-CN_TOPIC_0000002441889129).
3.  Click the burn button ![](figures/zh-cn_image_0000002441769249.png), as shown in [Figure 3](#_Ref416783621).

    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >When burning by address, the user does not need to select a file type — just select the file you want to burn. Since yaffs files (with OOB data) and other types of files (without OOB data) have different formats, the tool will automatically distinguish the file type in the background based on the selected file (the tool distinguishes between yaffs type and None type). It then executes the corresponding burning according to the different types. Power on the board, enter the burning process, and wait for burning to complete. For Burn by Address, only the first time the burn button is clicked does the board need to be powered on again. For subsequent image burns, the board does not need to be powered on again.

    **Figure 3**  Clicking Burn<a name="_Ref416783621"></a>  
    ![](figures/单击烧写.png "单击烧写")

4.  Power on the board, enter the burning process, and wait for burning to complete. The burning process is shown in [Figure 4](#_Ref416783705).

    **Figure 4**  Burning process<a name="_Ref416783705"></a>  
    ![](figures/烧写过程-0.png "烧写过程-0")

    Information about the burning process will be printed in the "Console" above. If a burning error is found, please check the board again:

    -   Whether the serial port selection is correct
    -   Whether the IP address setting is correct and whether it is occupied
    -   Whether the bootstrap jumper on the board is shorted

    The Erase operation is similar to the Burn operation and will not be elaborated here.

5.  After burning is complete, connect the terminal tool and restart the board.

## Upload Steps<a name="ZH-CN_TOPIC_0000002408329648"></a>

Burning and uploading are two inverse operations. The burning function writes image files to the board, while the upload function uploads the content of a region to the PC according to the start address and length set by the user. The specific steps for uploading can fully reference the burning steps. Two differences from the burning steps are listed here; repetitive parts will not be reiterated.

1.  Same as section 3.2 step [1](#ZH-CN_TOPIC_0000002441889077).
2.  Same as section 3.2 step [2](#ZH-CN_TOPIC_0000002441889077).
3.  Configure the board upload information: select the flash type to upload, set the start address and length to be uploaded in the storage device, and set the save file after uploading, as shown in [Figure 1](#fig12876191611389).

    **Figure 1**  Upload information<a name="fig12876191611389"></a>  
    ![](figures/上载信息.png "上载信息")

4.  Same as section 3.2 step [3](#ZH-CN_TOPIC_0000002441889077).
5.  Click "upload". If the image in the region to be uploaded is fastboot, kernel, ubifs, etc., please select Data without OOB. If the image is yaffs, please select Data with OOB, as shown in [Figure 2](#_Ref416783742).

    **Figure 2**  Selecting the data type<a name="_Ref416783742"></a>  
    ![](figures/选择数据类型.png "选择数据类型")
    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >When uploading by address, the user needs to explicitly specify the data type to upload. This step is completed in the pop-up dialog after the user clicks the "Upload" button. If the user makes an incorrect selection at this step, the uploaded data will not match the original file. When partially uploading a yaffs file system, the length should be a multiple of pagesize + oobsize.

## Erase Steps<a name="ZH-CN_TOPIC_0000002441889041"></a>

The erase function erases content of a specified length starting from a specified address on the board side. The erase steps are similar to the burning steps. Two differences from the burning steps are listed here; repetitive parts will not be reiterated.

1.  Same as section 3.2 step [1](#ZH-CN_TOPIC_0000002441889077).
2.  Same as section 3.2 step [2](#ZH-CN_TOPIC_0000002441889077).
3.  Configure the board erase information: select the flash type to erase, set the start address and length to be erased in the storage device, as shown in [Figure 1](#fig10547163316314).

    **Figure 1**  Erase information<a name="fig10547163316314"></a>  
    ![](figures/擦除信息.png "擦除信息")

4.  Same as section 3.2 step [3](#ZH-CN_TOPIC_0000002441889077).
5.  Click "erase", power on the board, enter the erase process, and wait for erasure to complete, as shown in [Figure 2](#_Ref416783804).

    **Figure 2**  Erase process<a name="_Ref416783804"></a>  
    ![](figures/擦除过程.png "擦除过程")
    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >When erasing, the length should be a multiple of the blocksize.

# Boot Burning
## Applicable Scenarios<a name="ZH-CN_TOPIC_0000002408169760"></a>

The board does not have boot. Used in conjunction with Burn by Address, it can complete burning of all images on the board.

## Burning Steps<a name="ZH-CN_TOPIC_0000002408329636"></a>

The specific burning steps are as follows:

1.  Switch to the "Burn Fastboot" tab, as shown in [Figure 1](#_Ref416783832).

    **Figure 1**  Fastboot burning interface<a name="_Ref416783832"></a>  
    ![](figures/Fastboot烧写界面.png "Fastboot烧写界面")

2.  Configure the serial port: select the serial port used to connect to the board, as shown in [Figure 2](#_Ref416783851).

    **Figure 2**  Serial port selection<a name="_Ref416783851"></a>  
    ![](figures/串口选择.png "串口选择")

3.  Configure the Boot burning information, as shown in [Figure 3](#fig6981215103111).

    **Figure 3**  Configuring boot burning information<a name="fig6981215103111"></a>  
    ![](figures/配置boot-烧写信息.png "配置boot-烧写信息")

4.  Prepare the board environment. If the board is powered on, power it off.
5.  Click the burn button ![](figures/zh-cn_image_0000002408170424.png), as shown in [Figure 4](#fig1999382113211).

    **Figure 4**  Clicking Burn<a name="fig1999382113211"></a>  
    ![](figures/点击Burn.png "点击Burn")

6.  Power on the board, enter the burning process, and wait for burning to complete. The burning process is shown in [Figure 5](#_Ref416783918).

    **Figure 5**  Burning process<a name="_Ref416783918"></a>  
    ![](figures/烧写过程-1.png "烧写过程-1")

    Information about the burning process will be printed in the "Console" above. If a burning error is found, please check again whether the serial port selection is correct.

7.  After burning is complete, connect the terminal tool and restart the board.

# eMMC Burning
## Applicable Scenarios<a name="ZH-CN_TOPIC_0000002441889025"></a>

The applicable scenarios are as follows: only applicable to eMMC burning, regardless of whether boot is present on the board, enabling one-click burning of all images.

## Burning Steps<a name="ZH-CN_TOPIC_0000002408329704"></a>

The specific burning steps are as follows:

1.  Switch to the "Burn eMMC" tab, as shown in [Figure 1](#fig10733727164915).

    **Figure 1**  eMMC burning interface<a name="fig10733727164915"></a>  
    ![](figures/eMMC-烧写界面.png "eMMC-烧写界面")
    >![](public_sys-resources/icon-note.gif) **Note:** 
    >-   Toggle the "Use XML path by default" checkbox state. If checked, the partition file is searched for in the XML path first. If unchecked, the absolute path is used to search for the file first. If the file is not found, the tool then tries to find it in the XML directory. This state is checked by default.
    >-   **XML is a configuration file used to save partition table information. The edited partition table can be saved as an XML file using the Save button on the tool. The next time the tool is opened, import the XML and the partition table information will be directly loaded.**

1.  Configure the board partition information. Click "Browse" to select pre-configured partition table information and load it into the tool, as shown in [Figure 2](#fig19253651205117). When the device type of the boot partition is emmc or emmc0, boot will be burned into the default partition. emmc will not switch the boot partition, while emmc0 will switch the boot partition to the default partition. When the device type of the boot partition is emmc1 or emmc2, boot will be burned into the corresponding boot1 or boot2 partition, and the boot partition will be switched to the corresponding boot1 or boot2 partition.

    **Figure 2**  Configuring board partition information<a name="fig19253651205117"></a>  
    ![](figures/配置单板分区信息-2.png "配置单板分区信息-2")
    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >If all partition files are packaged into a single image for burning (since eMMC file system partitions need to create a partition table, if the file system partitions are different, they cannot be packaged together; this issue does not exist for Android versions), this image must be placed in the fastboot partition, and the image must contain fastboot. Additionally, since burning at this time uses the serial port method, the burning speed is relatively slow — please be patient.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >eMMC uses the DOS partition format. For Ext3/4 file system partitions, partition table information needs to be created for the kernel to correctly recognize the Ext3/4 file system partitions.

    To modify the information of a partition, you can directly modify the partition information file saved in xml format, or modify it in the tool. To modify the information of a partition in the tool, click on the row where that partition is located, and it will appear as shown in [Figure 3](#fig05531290513).

    **Figure 3**  Editing board partition information<a name="fig05531290513"></a>  
    ![](figures/编辑单板分区信息-3.png "编辑单板分区信息-3")
    >![](public_sys-resources/icon-notice.gif) **Important:** 
    >The partition start size and partition size are in KB or MB units and must be integer multiples of the eMMC sector size; otherwise, errors may occur.

    -   Click the button ![](figures/zh-cn_image_0000002408170740.jpg) to add a row of partition. In this row, you can modify the partition name, select whether a file system is needed and the file system type, and modify the partition start size and partition size.
    -   Click the button ![](figures/zh-cn_image_0000002408170832.jpg) to select or change the burning file for this partition.
    -   Click the button ![](figures/zh-cn_image_0000002408330712.jpg) to delete this partition information. Note: the fastboot partition cannot be deleted here, and the fastboot partition name cannot be modified, because if the fastboot partition is deleted or its name is modified, one-click burning cannot be achieved.
    -   Click the button ![](figures/zh-cn_image_0000002441889837.jpg) to select all partitions for one-click burning of all partitions. Click the button again ![](figures/zh-cn_image_0000002408170596.jpg) to deselect all partitions to be burned. You can also click the checkbox ![](figures/zh-cn_image_0000002408330496.jpg) to select the corresponding partitions for burning.
    -   Click the button ![](figures/zh-cn_image_0000002441769909.jpg) to save the edited partition table as a file.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >After creation, when switching perspectives, a dialog as shown will pop up. Click "OK", and in the dialog that appears, select the path to save the partition information, enter the filename to save, and it will be saved as xml-format partition information. Click "Cancel" to switch views without saving the partition information. Note that the filename suffix for saving partition information must be .xml format; otherwise, the partition information may not be correctly loaded the next time. Saving information is shown in [Figure 6](#fig196451156109).

    **Figure 4**  Dialog reminding whether to save partition information when closing the BurnTool<a name="fig0725202195510"></a>  
    ![](figures/关闭BurnTool工具时提醒是否保存分区信息界.png "关闭BurnTool工具时提醒是否保存分区信息界")

    **Figure 5**  Dialog reminding whether to save partition information when switching views<a name="fig13640113718555"></a>  
    ![](figures/切换视图时提醒是否保存分区信息界面-4.png "切换视图时提醒是否保存分区信息界面-4")

    Saving information is shown in [Figure 6](#fig196451156109).

    **Figure 6**  Partition information save interface<a name="fig196451156109"></a>  
    ![](figures/分区信息保存界面-5.png "分区信息保存界面-5")

1.  Same as [2.2 step 3](#ZH-CN_TOPIC_0000002441889129).
2.  Burn the board. Click the burn button ![](figures/zh-cn_image_0000002408170564.png), as shown in [Figure 7](#fig79197461111).

    **Figure 7**  Clicking Burn<a name="fig79197461111"></a>  
    ![](figures/点击烧写-6.png "点击烧写-6")

1.  Power on the board, enter the burning process, and wait for burning to complete.

    Information about the burning process will be displayed in the console.

    -   Whether the serial port selection is correct.
    -   Whether the IP address setting is correct and whether the address is occupied.
    -   Whether the bootstrap jumper on the board is shorted.

2.  After burning is complete, connect the terminal tool and restart the board.

## Creating Burner Images<a name="ZH-CN_TOPIC_0000002441768929"></a>

The Create Burner Image function can create the files selected in the current partition list as a burner image file. After configuring the partition list, click the Create Burner Image button ![](figures/zh-cn_image_0000002441890077.png), set the file path in the Save dialog that appears, and the burner image creation will begin, as shown in [Figure 1](#fig114434436368).

**Figure 1**  Burner image creation process<a name="fig114434436368"></a>  
![](figures/制作烧片器镜像过程.png "制作烧片器镜像过程")
## Upload Steps<a name="ZH-CN_TOPIC_0000002408169712"></a>

The upload function is not available — the board does not support uploading.

## Erase Steps<a name="ZH-CN_TOPIC_0000002408169768"></a>

1.  Switch to the eMMC tab and import the partition table information, as shown in [Figure 1](#fig119011214321).

    **Figure 1**  Importing partition table<a name="fig119011214321"></a>  
    ![](figures/导入分区表.png "导入分区表")

2.  Edit the boot device type, as shown in [Figure 2](#fig151791728173710). If the device type is emmc, only the default partition will be erased. If the device type is emmc0, 1, or 2, the default partition, boot1, and boot2 partitions will all be erased.

    **Figure 2**  Editing boot device type<a name="fig151791728173710"></a>  
    ![](figures/编辑boot器件类型.png "编辑boot器件类型")

3.  Click Erase, as shown in [Figure 3](#fig17109141184016).

    **Figure 3**  Clicking Erase<a name="fig17109141184016"></a>  
    ![](figures/点击擦除.png "点击擦除")
# Merging Images
## Applicable Scenarios<a name="ZH-CN_TOPIC_0000002408329680"></a>

The applicable scenarios are as follows: applicable to SPI Flash scenarios where storage space is small and users need to merge multiple small images into a single image and then burn them into the same block to save flash space. Also applicable to merging images of other Flash types into a single image.

For example, if there are two images, fastboot and kernel, each 500K, and the SPI block size is 1M, then if these two images are burned as two partitions, the board-side burning command will use 2 blocks. If the images are merged, only a single block is needed, thus saving 1M of Flash space.

## Operation Steps<a name="ZH-CN_TOPIC_0000002408329692"></a>

The specific merging steps are as follows:

1.  Switch to the "Merge Image" tab, as shown in [Figure 1](#_Ref416784461).

    **Figure 1**  BurnTool Merge Image interface<a name="_Ref416784461"></a>  
    ![](figures/BurnTool合并镜像界面.png "BurnTool合并镜像界面")

2.  Click the Browse button to load a partition table, or click the ![](figures/zh-cn_image_0000002408329860.png) button to manually create a new partition table, as shown in [Figure 2](#fig1195161117453).

    **Figure 2**  Loading partition table<a name="fig1195161117453"></a>  
    ![](figures/加载分区表.png "加载分区表")

3.  Click the Merging Image button to merge images, as shown in [Figure 3](#_Ref416784524).

    **Figure 3**  Merging images<a name="_Ref416784524"></a>  
    ![](figures/合并镜像.png "合并镜像")
# Preferences Settings
## Command Settings<a name="ZH-CN_TOPIC_0000002441889057"></a>

The BurnTool's serial port command send timeout can be set through Preferences. Click "Window" → "Preferences" in the menu bar to enter the Preferences dialog, and go to the "Command Settings" page under "BurnTool", as shown in [Figure 1](#_Ref416784561).

**Figure 1**  Command Settings page<a name="_Ref416784561"></a>  
![](figures/命令设置页面.png "命令设置页面")

Note: Timeout (ms): used for serial port command send response timeout. Unit: ms.

## TFTP Settings<a name="ZH-CN_TOPIC_0000002441768913"></a>

The BurnTool's TFTP can be set through Preferences. Click "Window" → "Preferences" in the menu bar to enter the Preferences dialog, and go to the "TFTP Settings" page under "BurnTool", as shown in [Figure 1](#_Ref416784544).

**Figure 1**  TFTP Settings page<a name="_Ref416784544"></a>  
![](figures/TFTP设置页面.png "TFTP设置页面")

Settings items:

-   TFTP Rate: used to calculate timeout. The timeout is calculated based on the length of the transferred file and the set TFTP rate. Unit: byte/s.
-   Handle Packet Loss: check the "Handle Packet Loss" button. The consecutive packet loss count item becomes configurable. During transmission, if the consecutive lost packets reach the maximum consecutive packet loss count, the transmission is judged as failed. If the "Handle Packet Loss" button is not checked, the consecutive packet loss count item is not configurable, and packet loss during transmission is ignored.
-   Consecutive Packet Loss Count: sets the maximum consecutive packet loss count.
-   TFTP Retry Count: sets the TFTP retry count. If transmission fails, it will retry. After reaching the set retry count without success, it will stop.
-   TFTP No Response Timeout: sets the TFTP no response timeout. If there is no response within the set time during transmission, the transmission is judged as failed. Unit: seconds, default value: 10 seconds.

## Other Settings<a name="ZH-CN_TOPIC_0000002441889101"></a>



### BurnTool-Debug Console Settings<a name="ZH-CN_TOPIC_0000002441768885"></a>

The BurnTool's Debug console can be set through Preferences.

1.  Click "Window" → "Preferences" in the menu bar to enter the Preferences dialog, go to the "BurnTool" page, and select the "Open Debug Mode" button to enable the Debug console, as shown in [Figure 1](#_Ref410048637).

    **Figure 1**  Selecting to enable the Debug console<a name="_Ref410048637"></a>  
    ![](figures/选中开启Debug控制台.png "选中开启Debug控制台")

2.  After starting burning, the tool will automatically create a Debug console. Click the console switch button in the upper right corner of the console and select the "BurnTool-Debug" console to switch. The current console will then display as the Debug console, as shown in [Figure 2](#_Ref410048738).

    **Figure 2**  Switching to the BurnTool-Debug console<a name="_Ref410048738"></a>  
    ![](figures/切换BurnTool-Debug控制台.png "切换BurnTool-Debug控制台")
### Check Same Network Segment Settings<a name="ZH-CN_TOPIC_0000002441768921"></a>

Click "Window" → "Preferences" in the menu bar to enter the Preferences dialog, go to the "BurnTool" page, and select the "Check whether the PC and Board IP addresses are in the same network segment" button, as shown in [Figure 1](#_Ref410048821). This enables checking whether the PC and board IPs are in the same gateway before burning. Deselecting it means this check will not be performed before burning.

**Figure 1**  Check Same Network Segment Settings page<a name="_Ref410048821"></a>  
![](figures/检查同一网段设置页面.png "检查同一网段设置页面")
# FAQ
## Solution for TFTP Timeout Prompt During BurnTool Burning<a name="ZH-CN_TOPIC_0000002408169704"></a>

**Problem Description<a name="section9846741144918"></a>**

When the following TFTP error occurs, as shown in [Figure 1](#_Ref386011440), how should it be resolved?

**Figure 1**  TFTP timeout problem<a name="_Ref386011440"></a>  
![](figures/TFTP超时问题.png "TFTP超时问题")

**Solution<a name="section05094512502"></a>**

Resolving this issue involves the following four aspects:

-   Check whether the network configuration in the BurnTool is correct, as shown in [Figure 2](#_Ref386011442). First, check whether the server IP is correct. If not, click Reload to load the latest PC-side IP address. Then check whether the subnet mask and gateway are correctly configured. If correct, check whether the board-side IP address is occupied (use the ping command to check whether the current board IP can be pinged; if not, it indicates that the current network is unreachable). After ensuring all the above parameters are correct, try burning again.

    **Figure 2**  Checking whether the network configuration is correct<a name="_Ref386011442"></a>  
    ![](figures/检查网络配置是否正确.png "检查网络配置是否正确")
-   Use an external tftpd32 tool instead of the built-in TFTP in the tool for download operations (see "[How to Use an External tftpd32 for Image Download?](#ZH-CN_TOPIC_0000002441889093)"). If tftpd32 also shows a timeout, check whether the current network environment is normal.
-   Modify the TFTP parameter settings in the tool to match the current network environment. Through the menu bar, click "Window" → "Preferences" → "BurnTool" → "TFTP Setting", as shown in [Figure 3](#_Ref386007685). Set the "The number of consecutive packet loss" and "TFTP no response timeout" parameters larger, then perform burning to check whether it is normal.
-   Check whether the firewall is disabled. If not, disable the firewall.

    **Figure 3**  Modifying TFTP settings<a name="_Ref386007685"></a>  
    ![](figures/修改TFTP设置.png "修改TFTP设置")
## How to Use an External tftpd32 for Image Download?<a name="ZH-CN_TOPIC_0000002441889093"></a>

**Problem Description<a name="section43891210195218"></a>**

How to use an external tftpd32 for image download and what should be noted?

**Solution<a name="section9229816115214"></a>**

The steps for using the external tftpd32 are:

1.  Before burning, open the tftpd32 tool and select the correct PC-side IP address and the directory where the images to be burned are located, as shown in [Figure 1](#_Ref386011451).

    **Figure 1**  Configuring the tftpd32 tool<a name="_Ref386011451"></a>  
    ![](figures/配置tftpd32工具.png "配置tftpd32工具")

1.  Click the burn button normally in the BurnTool. A prompt box will appear, as shown in [Figure 2](#_Ref386011453). Click Confirm to start burning. The external tftpd32 will then be used for image download, as shown in [Figure 3](#_Ref386011454).

    **Figure 2**  Prompt indicating built-in TFTP startup failed, port occupied by external tftpd32 tool<a name="_Ref386011453"></a>  
    ![](figures/提示内置TFTP启动失败-端口被外置tftpd32工具占.png "提示内置TFTP启动失败-端口被外置tftpd32工具占")

    **Figure 3**  External tftpd32 tool downloading image<a name="_Ref386011454"></a>  
    ![](figures/外置tftpd32工具正在下载镜像.png "外置tftpd32工具正在下载镜像")
## Solution for "Failed to Send Start Frame" Error When Burning the Fastboot Partition with BurnTool<a name="ZH-CN_TOPIC_0000002408329668"></a>

**Problem Description<a name="section17113181011420"></a>**

When the following "Failed to send start frame" error occurs while burning the Fastboot partition, as shown in [Figure 1](#_Ref386011456), what should I do?

**Figure 1**  "Failed to send start frame" error message<a name="_Ref386011456"></a>  
![](figures/Failed-to-send-start-frame-报错信息.png "Failed-to-send-start-frame-报错信息")Failed to send start frame\" error message")

**Solution<a name="section1951334642"></a>**

First, confirm whether the board was powered on again within 15 seconds after the last burn was clicked. If it has already been powered on again, check whether the serial port is making good contact with the board. If the connection is normal, check whether the correct serial port number is selected in the BurnTool, as shown in [Figure 2](#_Ref386011460). After ensuring everything is correct, try burning again.

**Figure 2**  Checking whether the serial port number is correctly selected<a name="_Ref386011460"></a>  
![](figures/检查串口号是否选择正确.png "检查串口号是否选择正确")
## Solution When the Console Only Prints a Line of "#########" Then Stops, and the Tool Reports "Failed to Send Head Frame" During Fastboot Partition Burning<a name="ZH-CN_TOPIC_0000002408169788"></a>

**Problem Description<a name="section1174175519"></a>**

When burning the Fastboot partition, the console only prints a line of "#########" and then stops, and the tool reports a "Failed to send head frame" error, as shown in [Figure 1](#_Ref386011462), how should it be resolved?

**Figure 1**  "Failed to send head frame" error message<a name="_Ref386011462"></a>  
![](figures/Failed-to-send-head-frame-报错信息.png "Failed-to-send-head-frame-报错信息")Failed to send head frame\" error message")

**Solution<a name="section1286417136513"></a>**

There may be two causes for this error:

-   The Fastboot image being burned does not match the current board model. Directly check the board model marking. After identifying the board model, use the SDK image matching the current chip to burn again.
-   The board DDR has issues and cannot perform DDR initialization normally.

## Solution for "Failed to Send Data Frame" Error When Burning the Fastboot Partition with BurnTool<a name="ZH-CN_TOPIC_0000002441768861"></a>

**Problem Description<a name="section956919507512"></a>**

When the following "Failed to send data frame" error occurs while burning the Fastboot partition, as shown in [Figure 1](#_Ref386011468), what should I do?

**Figure 1**  "Failed to send data frame" error message<a name="_Ref386011468"></a>  
![](figures/Failed-to-send-data-frame-报错信息.png "Failed-to-send-data-frame-报错信息")Failed to send data frame\" error message")

**Solution<a name="section35233257619"></a>**

The cause of this error may be that the serial port connection became loose during Fastboot image burning, causing data transmission failure when the tool interacts with the board. Please check the serial port connection.

## Solution for "Failed to Execute Command" Error When Burning the Fastboot Partition with BurnTool<a name="ZH-CN_TOPIC_0000002408169752"></a>

**Problem Description<a name="section45431947769"></a>**

When the following "Failed to execute command" error occurs while burning the Fastboot partition, as shown in [Figure 1](#_Ref386011469), what should I do?

**Figure 1**  "Failed to execute command" error message<a name="_Ref386011469"></a>  
![](figures/Failed-to-execute-command-报错信息.png "Failed-to-execute-command-报错信息")Failed to execute command\" error message")

**Solution<a name="section1426113619713"></a>**

The cause of this error may be that the Flash type selected for the current Fastboot partition is incorrect, as shown in [Figure 2](#_Ref386011475). Restart the board and check the current "Flash" attribute of the board. If it is currently eMMC, use Burn by eMMC, and select emmc as the Flash type for the Fastboot partition.

**Figure 2**  Viewing board Flash information via the serial port<a name="_Ref386011475"></a>  
![](figures/通过串口查看单板Flash信息.png "通过串口查看单板Flash信息")
## What Should Be Noted When Selecting a File Transfer Method?<a name="ZH-CN_TOPIC_0000002408169696"></a>

**Problem Description<a name="section290917257720"></a>**

When selecting a file transfer method, what are the pros and cons between serial port and network port?

**Solution<a name="section15228123017718"></a>**

The BurnTool's serial port burning function is pure serial port burning. Since the burning process requires transmitting a large amount of data to the board side, and the serial port's own transmission rate is relatively low, burning using the pure serial port method will be relatively inefficient. We recommend using the network port method for burning. The pure serial port method of burning is very stable; if the user's network environment is unstable, serial port burning can be used.

## File Length Requirements in the Burn by Address Interface?<a name="ZH-CN_TOPIC_0000002441889033"></a>

**Problem Description<a name="section129616216810"></a>**

In the Burn by Address interface, what are the file length requirements?

**Solution<a name="section14316972810"></a>**

When erasing, the length should be a multiple of the blocksize. When partially uploading a yaffs file system, the length should be a multiple of pagesize + oobsize.

## Possible Reasons Why Burning Does Not Start After Clicking Burn and Power Cycling?<a name="ZH-CN_TOPIC_0000002441768873"></a>

**Problem Description<a name="section879943317814"></a>**

After clicking Burn and power cycling, but the tool does not start burning — what is the reason?

**Solution<a name="section17459025490"></a>**

It may be that the serial port selection is wrong or the serial port is not properly connected (please use a terminal tool to check). Wait, and the console will print relevant information.

## Reasons Why the Serial Port Cannot Be Found, TFTP Startup Fails, or TFTP Port Occupied Error Occurs?<a name="ZH-CN_TOPIC_0000002408329620"></a>

**Problem Description<a name="section15781328107"></a>**

When using Linux, the serial port cannot be found, TFTP startup fails, or a TFTP port occupied error is reported — what are the possible causes?

**Solution<a name="section481113141014"></a>**

Not logged in as the root user, lacking permission to open the TFTP service or use the serial port. A TFTP port occupied error may also be caused by other software occupying this port.

## When Burning NAND, What Do pure data length and len_incl_bad Printed in the Console Mean?<a name="ZH-CN_TOPIC_0000002408169776"></a>

**Problem Description<a name="section9483135101011"></a>**

When burning NAND, what do pure data length and len_incl_bad printed in the console mean?

**Solution<a name="section15954111011116"></a>**

As shown in [Figure 1](#_Ref386007893), pure data length represents the actual length of data burned, while len incl bad represents the actual length occupied by burning including bad blocks. Neither of the above two lengths includes the oobSize length.

**Figure 1**  Burn length printed by the console as feedback to the burn command<a name="_Ref386007893"></a>  
![](figures/控制台打印烧写命令反馈的烧写长度.png "控制台打印烧写命令反馈的烧写长度")
## What Will the Tool Print When Board DDR Training Fails?<a name="ZH-CN_TOPIC_0000002408329624"></a>

**Problem Description<a name="section1033016544115"></a>**

What will the tool print when board DDR Training fails?

**Solution<a name="section2742102181210"></a>**

When board DDR Training fails, during Fastboot partition burning, the information shown in [Figure 1](#_Ref386011496) will be printed.

**Figure 1**  Printing DDR Training failure information<a name="_Ref386011496"></a>  
![](figures/打印DDR-Training失败信息.png "打印DDR-Training失败信息")
## What Needs to Be Provided When Reporting Issues Encountered During BurnTool Usage?<a name="ZH-CN_TOPIC_0000002408329640"></a>

**Problem Description<a name="section4620102214128"></a>**

What needs to be provided when reporting issues encountered during BurnTool usage?

**Solution<a name="section10510122714124"></a>**

When encountering issues with the BurnTool, export the console print content using the export button in the console toolbar. Providing this along with the issue report will help with problem localization and resolution.

## How to Check Whether a Process Is Occupying TFTP Port 69?<a name="ZH-CN_TOPIC_0000002408329684"></a>

**Problem Description<a name="section1072719116131"></a>**

The tftp command always reports that the file cannot be found, but all settings are actually correct — what is the reason? How to check whether a process is occupying TFTP port 69?

**Solution<a name="section17557141213133"></a>**

There may be a background process occupying port 69. You can use the following method to check whether a process is occupying it.

Enter the following in the cmd command line tool, and the printout will look like [Figure 1](#_Ref413161493).

netstat -ano -p udp

**Figure 1**  Viewing process port occupation<a name="_Ref413161493"></a>  
![](figures/查看进程的端口占用.png "查看进程的端口占用")

Check whether any process is occupying port 69. In the above figure, it can be seen that the process with pid 7696 is occupying port 69. Then use the following command to view the name of the 7696 process, with the printout as shown in [Figure 2](#_Ref413161472).

tasklist|findstr "7696"

**Figure 2**  Viewing the process name for a specified PID<a name="_Ref413161472"></a>  
![](figures/查看指定PID的进程名称.png "查看指定PID的进程名称")

Then kill that process in the process manager.

## What If It Is a 64-bit PC and Only the 64-bit Version of JRE Is Installed?<a name="ZH-CN_TOPIC_0000002441768865"></a>

**Problem Description<a name="section234741210149"></a>**

The PC has the 64-bit version of JRE installed, and an error is reported when opening ToolPlatform — what should be done?

**Solution<a name="section16521321181418"></a>**

Since ToolPlatform depends on the 32-bit JRE version, before using ToolPlatform, please first visit the JRE official website, download and install the Windows x86 version of the corresponding JRE version at the following URL: [http://www.oracle.com/technetwork/java/javase/downloads/](http://www.oracle.com/technetwork/java/javase/downloads/)

Additionally, ToolPlatform-XXX-4.0.15 and later versions already have the JRE program built in, so there is no need to install JRE again.

## Non-Chinese Language Systems Cannot Burn Images with Chinese Paths<a name="ZH-CN_TOPIC_0000002441889049"></a>

**Problem Description<a name="section1999915715158"></a>**

If the system is a non-Chinese system, the tool cannot burn images with Chinese paths in the system. To query the language system, enter the chcp command in cmd. As shown in Figure Querying the Windows Language System Method, 437 represents the US language system, while 936 represents the Chinese language system.

**Figure 1**  Method for querying the Windows language system<a name="_Ref4156611"></a>  
![](figures/查询windows语言系统方法.png "查询windows语言系统方法")

**Solution<a name="section185019199156"></a>**

Non-Chinese language systems do not support images with paths containing Chinese characters. Change the burning path to an English path.

# Acronyms and Abbreviations
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
