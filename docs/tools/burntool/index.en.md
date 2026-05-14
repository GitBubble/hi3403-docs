---
title: "BurnTool User Guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/BurnTool 工具使用指南/BurnTool 工具使用指南.md
---

# Preface
**Overview<a name="section94015722114"></a>**

This document describes the usage of the BurnTool flashing utility. It covers three scenarios: one-click flashing of all program images to board flash, address-based flashing of other program images to board flash when a boot image is already present, and flashing only the boot image to an empty board.

**Product Versions<a name="section1241074213"></a>**

The product versions corresponding to this document are listed below.

<a name="table16437719210"></a>
<table><thead align="left"><tr id="row75927132112"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p135997202113"><a name="p135997202113"></a><a name="p135997202113"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p145917742113"><a name="p145917742113"></a><a name="p145917742113"></a>Product Version</p>
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

**Intended Audience<a name="section18436710211"></a>**

This document is intended for the following engineers:

-   Technical support engineers
-   Hardware development engineers

**Revision History<a name="section1530582391712"></a>**

The revision history accumulates the description of each document update. The latest version of this document incorporates all updates from previous versions.

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.06%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.06%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First interim release.</p>
</td>
</tr>
</tbody>
</table>

# Overview
## Tool Overview<a name="ZH-CN_TOPIC_0000002441889113"></a>

BurnTool is a multi-function utility for image flashing, image upload, and programmer image creation.

>![](public_sys-resources/icon-note.gif) **Note:**  This tool only supports 64-bit operating systems.

## Use Cases<a name="ZH-CN_TOPIC_0000002408329736"></a>

The three main use cases for BurnTool are:

-   Image flashing: Flash images to the corresponding flash address on the board via serial port, network port, or USB.
-   Image upload: Export data from a flash address on the board to a file on the PC via DDR.
-   Programmer image creation: Package images from the partition table into the format required by the programmer tool for mass production flashing.

## Flashing Principles<a name="ZH-CN_TOPIC_0000002441768981"></a>

**uboot flashing principle:** After BurnTool starts the flashing process, it first communicates with the bootrom. The tool sends DDR parameters to the bootrom (this is the 5% stage of the uboot download phase), which then initializes the DDR. Next, the tool transfers uboot to DDR — the 100% stage indicates the transfer is complete. uboot then boots from DDR. Once uboot is running, BurnTool communicates with uboot, sends flashing commands, and flashes the uboot image from DDR to the corresponding flash address.

**Other partition flashing principle:** For other image partitions such as kernel and rootfs, the tool uses the network port by default. Customers can choose between bare flashing and non-bare flashing. Bare flashing means selecting uboot in the partition flashing or eMMC flashing mode, which burns uboot to flash. Non-bare flashing means not selecting uboot — only other partitions — which requires an existing uboot on the board. In this case, the tool boots uboot and interacts with it, sending TFTP and write commands to complete the flash operation.

## Tool and Board Device Compatibility<a name="ZH-CN_TOPIC_0000002408169824"></a>

BurnTool support varies by board. The compatibility matrix is shown in [Table 1](#_Ref382475342).

**Table 1**  Tool and board device compatibility

<a name="_Ref382475342"></a>
<table><thead align="left"><tr id="row630mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.16.1.1"><p id="p632mcpsimp"><a name="p632mcpsimp"></a><a name="p632mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" colspan="4" valign="top" id="mcps1.2.16.1.2"><p id="p634mcpsimp"><a name="p634mcpsimp"></a><a name="p634mcpsimp"></a>Flash Type</p>
</th>
<th class="cellrowborder" colspan="5" valign="top" id="mcps1.2.16.1.3"><p id="p636mcpsimp"><a name="p636mcpsimp"></a><a name="p636mcpsimp"></a>File System</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.16.1.4"><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>Advanced Features</p>
</th>
<th class="cellrowborder" colspan="3" valign="top" id="mcps1.2.16.1.5"><p id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>General Interfaces</p>
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
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.12"><p id="p665mcpsimp"><a name="p665mcpsimp"></a><a name="p665mcpsimp"></a>Serial</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.16.2.13"><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>Network</p>
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

Note: ● = Supported; ○ = Not supported.

## Environment Preparation<a name="ZH-CN_TOPIC_0000002408169800"></a>

Prepare the BurnTool flashing environment as follows:

1.  Connect the serial port and network cable between the PC and the board. Since flashing requires interaction with the bootrom, the board's `bootrom_sel` hardware pin must be set to 1 to boot from the bootrom.
2.  Copy `ToolPlatform-X.X.X.zip` from the SDK release package (path: `$SDK_DIR/tools/windows/ToolPlatform`) to a local hard drive on the PC (Windows 7 or Windows 10 required).
3.  Extract `ToolPlatform-X.X.X.zip`, then double-click `ToolPlatform.exe` in the tool directory to launch ToolPlatform, as shown in [Figure 1](#_Ref427762404).

    **Figure 1**  Launching ToolPlatform from its directory<a name="_Ref427762404"></a>  
    ![](figures/从ToolPlatform工具目录打开ToolPlatform工具.png "Launching ToolPlatform from its directory")

4.  On the welcome page, select the BurnTool tool, as shown in [Figure 2](#_Ref427762422).

    **Figure 2**  Selecting BurnTool<a name="_Ref427762422"></a>  
    ![](figures/选择BurnTool工具.png "Selecting BurnTool")

5.  Configure parameters: select the serial port connected to the board, select the PC's network IP address, and configure the board's MAC address, IP address, subnet mask, and gateway, as shown in [Figure 3](#fig58684616564).

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >The selected PC server IP must be on the same subnet as the board's network configuration; otherwise, flashing images other than fastboot via the network port will fail (the fastboot image is flashed via the serial port).

    **Figure 3**  Parameter configuration<a name="fig58684616564"></a>  
    ![](figures/参数设置.png "Parameter configuration")

# Partition-Based Flashing
## Use Case<a name="ZH-CN_TOPIC_0000002408329724"></a>

The partition-based flashing function works for all boards, regardless of whether a boot image is already present.

## Flashing Steps<a name="ZH-CN_TOPIC_0000002441889129"></a>

The flashing steps are as follows:

1.  After opening BurnTool, switch to the **Burn by Partition** tab, as shown in [Figure 1](#fig1560862365516).

    **Figure 1**  BurnTool partition-based flashing<a name="fig1560862365516"></a>  
    ![](figures/BurnTool按分区烧写.png "BurnTool partition-based flashing")

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >-   When the software is first opened, default parameters are automatically generated. When these are changed, the software records the latest values. On normal exit, the configuration is saved automatically. On the next launch, the latest configuration is used. If the software exits abnormally, the most recent parameter changes may not be saved.
    >-   Click the Save button to save the current board network configuration. Click the Load button to select a previously saved configuration as the current configuration.
    >-   Toggling "Default to XML path" changes file lookup behavior: when checked, partition files are searched in the XML directory first; when unchecked, the absolute path is used first, and the XML directory is tried as a fallback.
    >-   **The XML is a configuration file that stores partition table information. Use the Save button on the tool to save the edited partition table as an XML file. On the next launch, import the XML to directly load the partition table.**

2.  Configure board partition information. Click the Browse button ![](figures/zh-cn_image_0000002408330452.png) to select an XML file with pre-configured partition table information and load it into the tool. The partition information is loaded as shown in [Figure 2](#fig62556341).

    **Figure 2**  Configuring board partition information<a name="fig62556341"></a>  
    ![](figures/配置单板分区信息.png "Configuring board partition information")

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >-   Partition information is only used for flashing and does not determine the actual board partition layout. The actual partition layout is determined by the board's bootargs. Ensure the partition information here matches what is specified in the board bootargs, or errors may occur.
    >-   BurnTool supports mismatched partition paths and remote flashing, meaning the images to be flashed can be on a remote path.
    >-   If a partition is selected but no flash file is specified, that partition will be erased during the flashing process.
    >-   If all partition files need to be packaged into a single image for flashing (for nandflash with writable file system partitions, these cannot be packaged together due to nandflash characteristics), the packaged file must be loaded into the fastboot partition for flashing and the image must include fastboot. Since flashing the fastboot partition uses the serial port (which is slow), this approach is not recommended.

    To edit partition information, either directly modify the XML file, or click the row of the partition to edit in the tool, as shown in [Figure 3](#fig1406152918013).

    **Figure 3**  Editing board partition information<a name="fig1406152918013"></a>  
    ![](figures/编辑单板分区信息.png "Editing board partition information")

    Click button ![](figures/zh-cn_image_0000002441769937.jpg) to add a new partition row. In this row, you can modify the partition name, select the flash type, choose whether to use a file system and which type, and set the start address and partition size.

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >-   Partition start address and size are in KB or MB units and must be integer multiples of the flash block size, or errors may occur.
    >-   For jffs2 file systems, no special format is required — select None.

    -   Click button ![](figures/zh-cn_image_0000002408330584.jpg) to select or change the flash file for that partition.
    -   Click button ![](figures/zh-cn_image_0000002441769729.jpg) to delete that partition entry.

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >The fastboot partition cannot be deleted and its name cannot be changed. Deleting or renaming the fastboot partition disables one-click flashing.

    -   Click button ![](figures/zh-cn_image_0000002441890057.jpg) to select all partitions for one-click flashing. Click button ![](figures/zh-cn_image_0000002441890145.jpg) again to deselect all. You can also click individual checkboxes ![](figures/zh-cn_image_0000002441889885.jpg) to select specific partitions.
    -   Click Save button ![](figures/zh-cn_image_0000002441769905.png) to save the edited partition table to a file.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >-   When no XML partition file exists the first time the tool is opened, you can create partition information directly in the tool interface. After creation, when closing ToolPlatform, a dialog as shown in [Figure 2](#fig1241812821916) prompts whether to save the partition information. Click **OK**, then in the dialog select the save path and enter a filename to save as an XML file. Click **Cancel** to close the tool without saving.
    >-   After creation, when switching tools, a dialog as shown in [Figure 5](#Figure2.6) appears. Click **OK** to save the partition table; click **Cancel** to switch views without saving. Note: the filename must have a `.xml` extension, or loading will fail on the next launch. The Save As dialog is shown in [Figure 6](#Figure2.7).

    **Figure 4**  Prompt to save partition information when closing ToolPlatform<a name="Figure2.5"></a>  
    ![](figures/关闭ToolPlatform工具时提醒是否保存分区信息界面.png "Prompt to save partition information when closing ToolPlatform")

    **Figure 5**  Prompt to save partition information when switching views<a name="Figure2.6"></a>  
    ![](figures/切换视图时提醒是否保存分区信息界面.png "Prompt to save partition information when switching views")

    **Figure 6**  Partition information save dialog<a name="Figure2.7"></a>  
    ![](figures/分区信息保存界面.png "Partition information save dialog")

    Select the current last row, click New ![](figures/zh-cn_image_0000002441769857.jpg) to create a new last row, then enter `-` in the Length field of that row. After adding the partition name, file system, and file path, the length is calculated automatically as the remaining space on the device. See [Figure 7](#fig99064111119).

    **Figure 7**  Setting length to "-" for the new partition row<a name="fig99064111119"></a>  
    ![](figures/新建单板分区信息后设置长度为--.png "Setting length to \"-\" for the new partition row")

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >If the current last partition is not selected when creating a new partition row, the new row may not be the actual last row and `-` cannot be used to represent remaining length.

3.  Prepare the board environment. Select a transfer method as shown in [Figure 8](#fig15452338171518). Power off the board if it is currently on.

    **Figure 8**  Selecting transfer method<a name="fig15452338171518"></a>  
    ![](figures/选择传输方式.png "Selecting transfer method")

    -   If using the network port, connect both the serial port and network port to the board.
    -   If using the serial port, connect only the serial port to the board.

4.  Start flashing. Click the Flash button ![](figures/zh-cn_image_0000002441889961.png), as shown in [Figure 9](#fig1659555711617).

    **Figure 9**  Click Flash<a name="fig1659555711617"></a>  
    ![](figures/点击烧写.png "Click Flash")

5.  Power on the board to start the flashing process and wait for it to complete. The flashing process is shown in [Figure 10](#fig297215536181).

    **Figure 10**  Flashing in progress<a name="fig297215536181"></a>  
    ![](figures/烧写过程.png "Flashing in progress")

    Progress information is shown in the console above. If flashing errors occur, check the board:

    -   Whether the serial port is correctly selected.
    -   Whether the IP address is correct and not already in use.
    -   Whether the bootstrap jumper on the board is correctly shorted.

6.  Once flashing is complete, connect a terminal tool and reboot the board.

## Creating Nand Programmer Images<a name="ZH-CN_TOPIC_0000002408169740"></a>

BurnTool provides a Nand programmer image creation function. After configuring the partition list, click the Create Nand Programmer Image button ![](figures/zh-cn_image_0000002408329812.png) to open the Nand programmer image creation dialog, as shown in [Figure 1](#fig106441654201914).

**Figure 1**  Nand programmer image creation dialog<a name="fig106441654201914"></a>  
![](figures/制作Nand烧片器镜像界面.png "Nand programmer image creation dialog")

After selecting all required options in the dialog (the Randomization feature is available for devices with 8K or larger page size), click **Make** to generate the Nand programmer image.

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>-   All entered or selected parameters must match the corresponding values in the board startup information (capturable using a terminal tool) or the actual device parameters on the board.
>-   If a partition is not selected or no flash file is assigned to a selected partition, no image will be created for that partition.
>-   When creating images for non-yaffs partitions, the file system column in the partition table must not be set to yaffs. When creating yaffs partition images, the file system must be set to yaffs. Incorrect settings will produce an invalid image.

## Jump from Partition Table Row to Address-Based Flashing<a name="ZH-CN_TOPIC_0000002441768853"></a>

The partition-based flashing view supports jumping to the address-based flashing view with partition details (partition name, file system, file path, start address, and partition length) pre-populated. In the partition flashing view, select a row in the partition table and click the Jump button ![](figures/zh-cn_image_0000002441769277.jpg) to switch to the address-based flashing view, as shown in [Figure 1](#fig19742104082116) and [Figure 2](#fig1241812821916).

**Figure 1**  Select row and click Jump<a name="fig19742104082116"></a>  
![](figures/选中单行-点击跳转.png "Select row and click Jump")

**Figure 2**  Address-based flashing view<a name="fig1241812821916"></a>  
![](figures/进入按地址烧写界面.png "Address-based flashing view")

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>Before jumping, a partition row must be selected; the Jump button only appears when a row is selected.

# Address-Based Flashing
## Use Case<a name="ZH-CN_TOPIC_0000002408329660"></a>

The board already has a boot image.

## Flashing Steps<a name="ZH-CN_TOPIC_0000002441889077"></a>

The flashing steps are as follows:

1.  Switch to the **Burn by Address** tab, as shown in [Figure 1](#fig77356229246).

    **Figure 1**  Address-based flashing view<a name="fig77356229246"></a>  
    ![](figures/地址烧写界面.png "Address-based flashing view")

1.  Configure board flash information: select the flash type, set the start address and length, and select the file to flash, as shown in [Figure 2](#fig1355103942610).

    **Figure 2**  Configuring board flash information<a name="fig1355103942610"></a>  
    ![](figures/配置单板烧写信息.png "Configuring board flash information")

2.  Same as section 2.2, step [3](#ZH-CN_TOPIC_0000002441889129).
3.  Click the Flash button ![](figures/zh-cn_image_0000002441769249.png), as shown in [Figure 3](#_Ref416783621).

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >For address-based flashing, you do not need to select a file type — simply select the file you want to flash. Since yaffs files (with OOB data) and other file types (without OOB data) have different formats, the tool automatically detects the file type in the background (classified as yaffs or None) and executes the appropriate flashing procedure. Power on the board to start flashing and wait for it to complete. Note that only the first time you click the Flash button is a power cycle required; subsequent flashes do not require a power cycle.

    **Figure 3**  Click Flash<a name="_Ref416783621"></a>  
    ![](figures/单击烧写.png "Click Flash")

4.  Power on the board to start the flashing process and wait for it to complete. The flashing process is shown in [Figure 4](#_Ref416783705).

    **Figure 4**  Flashing in progress<a name="_Ref416783705"></a>  
    ![](figures/烧写过程-0.png "Flashing in progress")

    Progress information is printed in the console. If flashing errors occur, check the board:

    -   Whether the serial port is correctly selected.
    -   Whether the IP address is correct and not already in use.
    -   Whether the bootstrap jumper on the board is correctly shorted.

    The Erase operation follows the same procedure as Flash and is not described separately.

5.  Once flashing is complete, connect a terminal tool and reboot the board.

## Upload Steps<a name="ZH-CN_TOPIC_0000002408329648"></a>

Flashing and uploading are inverse operations: flashing writes an image to the board; uploading reads a specified address range from the board to a file on the PC. The upload steps are essentially the same as flashing. Only the two steps that differ are listed below.

1.  Same as section 3.2, step [1](#ZH-CN_TOPIC_0000002441889077).
2.  Same as section 3.2, step [2](#ZH-CN_TOPIC_0000002441889077).
3.  Configure upload information: select the flash type, set the start address and length of the region to upload from the storage device, and specify the destination file. As shown in [Figure 1](#fig12876191611389).

    **Figure 1**  Upload configuration<a name="fig12876191611389"></a>  
    ![](figures/上载信息.png "Upload configuration")

4.  Same as section 3.2, step [3](#ZH-CN_TOPIC_0000002441889077).
5.  Click **upload**. For fastboot, kernel, ubifs, and similar images, select **Data without OOB**; for yaffs images, select **Data with OOB**. As shown in [Figure 2](#_Ref416783742).

    **Figure 2**  Select data type<a name="_Ref416783742"></a>  
    ![](figures/选择数据类型.png "Select data type")

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >For address-based upload, you must explicitly specify the data type. This is done in the dialog that appears after clicking the Upload button. Selecting incorrectly will cause the uploaded data to not match the original file. For yaffs partial uploads, the length must be a multiple of (pagesize + oobsize).

## Erase Steps<a name="ZH-CN_TOPIC_0000002441889041"></a>

The erase function erases a specified length of content starting from a given address on the board. The erase steps are similar to flashing. Only the two steps that differ are listed.

1.  Same as section 3.2, step [1](#ZH-CN_TOPIC_0000002441889077).
2.  Same as section 3.2, step [2](#ZH-CN_TOPIC_0000002441889077).
3.  Configure erase information: select the flash type and set the start address and length of the region to erase. As shown in [Figure 1](#fig10547163316314).

    **Figure 1**  Erase configuration<a name="fig10547163316314"></a>  
    ![](figures/擦除信息.png "Erase configuration")

4.  Same as section 3.2, step [3](#ZH-CN_TOPIC_0000002441889077).
5.  Click **erase**, power on the board to start the erase process, and wait for it to complete. As shown in [Figure 2](#_Ref416783804).

    **Figure 2**  Erase in progress<a name="_Ref416783804"></a>  
    ![](figures/擦除过程.png "Erase in progress")

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >The erase length must be a multiple of the block size.

# Boot Flashing
## Use Case<a name="ZH-CN_TOPIC_0000002408169760"></a>

The board has no boot image. Used in combination with address-based flashing to complete full board image flashing.

## Flashing Steps<a name="ZH-CN_TOPIC_0000002408329636"></a>

The flashing steps are as follows:

1.  Switch to the **Burn Fastboot** tab, as shown in [Figure 1](#_Ref416783832).

    **Figure 1**  Fastboot flashing view<a name="_Ref416783832"></a>  
    ![](figures/Fastboot烧写界面.png "Fastboot flashing view")

2.  Configure the serial port, as shown in [Figure 2](#_Ref416783851).

    **Figure 2**  Serial port selection<a name="_Ref416783851"></a>  
    ![](figures/串口选择.png "Serial port selection")

3.  Configure boot flashing information, as shown in [Figure 3](#fig6981215103111).

    **Figure 3**  Boot flashing configuration<a name="fig6981215103111"></a>  
    ![](figures/配置boot-烧写信息.png "Boot flashing configuration")

4.  Power off the board if it is currently on.
5.  Click the Flash button ![](figures/zh-cn_image_0000002408170424.png), as shown in [Figure 4](#fig1999382113211).

    **Figure 4**  Click Burn<a name="fig1999382113211"></a>  
    ![](figures/点击Burn.png "Click Burn")

6.  Power on the board to start flashing and wait for it to complete. The flashing process is shown in [Figure 5](#_Ref416783918).

    **Figure 5**  Flashing in progress<a name="_Ref416783918"></a>  
    ![](figures/烧写过程-1.png "Flashing in progress")

    Progress information is printed in the console. If errors occur, check whether the correct serial port is selected.

7.  Once flashing is complete, connect a terminal tool and reboot the board.

# eMMC Flashing
## Use Case<a name="ZH-CN_TOPIC_0000002441889025"></a>

Only applicable to eMMC flashing. Works regardless of whether a boot image is present on the board, enabling one-click flashing of all images.

## Flashing Steps<a name="ZH-CN_TOPIC_0000002408329704"></a>

The flashing steps are as follows:

1.  Switch to the **Burn eMMC** tab, as shown in [Figure 1](#fig10733727164915).

    **Figure 1**  eMMC flashing view<a name="fig10733727164915"></a>  
    ![](figures/eMMC-烧写界面.png "eMMC flashing view")

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >-   Toggling "Default to XML path" changes file lookup behavior: when checked, partition files are searched in the XML directory first (default). When unchecked, absolute paths are used first, falling back to the XML directory.
    >-   **The XML is a configuration file for storing partition table information. Save the edited partition table using the Save button to create an XML file. On the next launch, import the XML to load the partition table directly.**

1.  Configure board partition information. Click **Browse** to select pre-configured partition table information and load it into the tool, as shown in [Figure 2](#fig19253651205117). When the boot partition device type is `emmc` or `emmc0`, boot is flashed to the default partition: `emmc` does not switch the boot partition, while `emmc0` switches the boot partition to the default. When the boot partition device type is `emmc1` or `emmc2`, boot is flashed to the corresponding boot1 or boot2 partition and the boot partition is switched accordingly.

    **Figure 2**  Configuring board partition information<a name="fig19253651205117"></a>  
    ![](figures/配置单板分区信息-2.png "Configuring board partition information")

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >If all partition files are packaged into a single image (eMMC file system partitions require partition table creation, so different file system partitions cannot be packaged together — this restriction does not apply to Android builds), the image must be placed in the fastboot partition and must include fastboot. Since this uses serial port flashing, it is slow — be patient.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >eMMC uses the DOS partition format. Ext3/4 file system partitions require a partition table so the kernel can correctly identify the Ext3/4 file system partitions.

    To modify a partition, either directly edit the saved XML file, or click the row in the tool to display the edit dialog as shown in [Figure 3](#fig05531290513).

    **Figure 3**  Editing board partition information<a name="fig05531290513"></a>  
    ![](figures/编辑单板分区信息-3.png "Editing board partition information")

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >Partition start size and partition size are in KB or MB units and must be integer multiples of the eMMC sector size, or errors may occur.

    -   Click button ![](figures/zh-cn_image_0000002408170740.jpg) to add a partition row. Set the partition name, choose whether to use a file system and which type, and configure the start size and partition size.
    -   Click button ![](figures/zh-cn_image_0000002408170832.jpg) to select or change the flash file for the partition.
    -   Click button ![](figures/zh-cn_image_0000002408330712.jpg) to delete the partition. Note: the fastboot partition cannot be deleted and its name cannot be changed, as this would disable one-click flashing.
    -   Click button ![](figures/zh-cn_image_0000002441889837.jpg) to select all partitions for one-click flashing. Click button ![](figures/zh-cn_image_0000002408170596.jpg) again to deselect all. Click individual checkboxes ![](figures/zh-cn_image_0000002408330496.jpg) to select specific partitions.
    -   Click button ![](figures/zh-cn_image_0000002441769909.jpg) to save the edited partition table to a file.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >When switching perspectives, a dialog appears. Click **OK** to save the partition table; click **Cancel** to switch views without saving. The filename must have a `.xml` extension, or loading will fail on the next launch. The Save As dialog is shown in [Figure 6](#fig196451156109).

    **Figure 4**  Prompt to save partition information when closing BurnTool<a name="fig0725202195510"></a>  
    ![](figures/关闭BurnTool工具时提醒是否保存分区信息界.png "Prompt to save partition information when closing BurnTool")

    **Figure 5**  Prompt to save partition information when switching views<a name="fig13640113718555"></a>  
    ![](figures/切换视图时提醒是否保存分区信息界面-4.png "Prompt to save partition information when switching views")

    The Save As dialog is shown in [Figure 6](#fig196451156109).

    **Figure 6**  Partition information save dialog<a name="fig196451156109"></a>  
    ![](figures/分区信息保存界面-5.png "Partition information save dialog")

1.  Same as [section 2.2, step 3](#ZH-CN_TOPIC_0000002441889129).
2.  Start flashing. Click the Flash button ![](figures/zh-cn_image_0000002408170564.png), as shown in [Figure 7](#fig79197461111).

    **Figure 7**  Click Flash<a name="fig79197461111"></a>  
    ![](figures/点击烧写-6.png "Click Flash")

1.  Power on the board to start flashing and wait for it to complete.

    Progress information is displayed in the console. If errors occur, check:

    -   Whether the serial port is correctly selected.
    -   Whether the IP address is correct and not already in use.
    -   Whether the bootstrap jumper on the board is correctly shorted.

2.  Once flashing is complete, connect a terminal tool and reboot the board.

## Creating Programmer Images<a name="ZH-CN_TOPIC_0000002441768929"></a>

The programmer image creation function packages the selected files in the current partition list into a programmer image file. After configuring the partition list, click the Create Programmer Image button ![](figures/zh-cn_image_0000002441890077.png), set the file path in the save dialog, and the image creation begins, as shown in [Figure 1](#fig114434436368).

**Figure 1**  Programmer image creation in progress<a name="fig114434436368"></a>  
![](figures/制作烧片器镜像过程.png "Programmer image creation in progress")

## Upload Steps<a name="ZH-CN_TOPIC_0000002408169712"></a>

Upload is not supported. The board does not support upload.

## Erase Steps<a name="ZH-CN_TOPIC_0000002408169768"></a>

1.  Switch to the eMMC tab and import the partition table, as shown in [Figure 1](#fig119011214321).

    **Figure 1**  Import partition table<a name="fig119011214321"></a>  
    ![](figures/导入分区表.png "Import partition table")

2.  Edit the boot device type, as shown in [Figure 2](#fig151791728173710). With type `emmc`, only the default partition is erased; with type `emmc0`, `1`, or `2`, the default partition, boot1, and boot2 partitions are all erased.

    **Figure 2**  Edit boot device type<a name="fig151791728173710"></a>  
    ![](figures/编辑boot器件类型.png "Edit boot device type")

3.  Click Erase, as shown in [Figure 3](#fig17109141184016).

    **Figure 3**  Click Erase<a name="fig17109141184016"></a>  
    ![](figures/点击擦除.png "Click Erase")

# Merging Images
## Use Case<a name="ZH-CN_TOPIC_0000002408329680"></a>

This is applicable when SPI Flash storage space is limited and multiple small images need to be merged into one image to be stored in the same block, saving flash space. It also applies to merging images from other flash types.

For example, if fastboot and kernel images are each 500 KB and the SPI block size is 1 MB, flashing them as two separate partitions uses two blocks. Merging them into one image requires only one block, saving 1 MB of flash space.

## Steps<a name="ZH-CN_TOPIC_0000002408329692"></a>

The steps are as follows:

1.  Switch to the **Merge Image** tab, as shown in [Figure 1](#_Ref416784461).

    **Figure 1**  BurnTool merge image view<a name="_Ref416784461"></a>  
    ![](figures/BurnTool合并镜像界面.png "BurnTool merge image view")

2.  Click Browse to load a partition table, or click ![](figures/zh-cn_image_0000002408329860.png) to manually create a new partition table, as shown in [Figure 2](#fig1195161117453).

    **Figure 2**  Load partition table<a name="fig1195161117453"></a>  
    ![](figures/加载分区表.png "Load partition table")

3.  Click the **Merging Image** button to merge the images, as shown in [Figure 3](#_Ref416784524).

    **Figure 3**  Merge images<a name="_Ref416784524"></a>  
    ![](figures/合并镜像.png "Merge images")

# Preferences
## Command Settings<a name="ZH-CN_TOPIC_0000002441889057"></a>

The BurnTool serial port command send timeout can be configured in Preferences. Navigate to **Window** > **Preferences** in the menu bar, then go to **BurnTool** > **Command Settings**, as shown in [Figure 1](#_Ref416784561).

**Figure 1**  Command settings page<a name="_Ref416784561"></a>  
![](figures/命令设置页面.png "Command settings page")

Note: **Timeout (ms)**: Timeout for serial port command response, in milliseconds.

## TFTP Settings<a name="ZH-CN_TOPIC_0000002441768913"></a>

BurnTool TFTP settings can be configured in Preferences. Navigate to **Window** > **Preferences** in the menu bar, then go to **BurnTool** > **TFTP Settings**, as shown in [Figure 1](#_Ref416784544).

**Figure 1**  TFTP settings page<a name="_Ref416784544"></a>  
![](figures/TFTP设置页面.png "TFTP settings page")

Settings:

-   **TFTP rate**: Used to calculate timeout based on the file size and configured rate. Unit: bytes/s.
-   **Handle packet loss**: When checked, the consecutive packet loss count is configurable. If consecutive packet loss reaches the maximum during transfer, the transfer is deemed failed. When unchecked, packet loss is ignored.
-   **Consecutive packet loss count**: Sets the maximum number of consecutive lost packets.
-   **TFTP retry count**: Sets the number of TFTP retries. If transfer fails, it retries until the retry count is reached.
-   **TFTP no-response timeout**: Sets the TFTP no-response timeout. If no response is received within this time during transfer, the transfer is deemed failed. Unit: seconds; default: 10 seconds.

## Other Settings<a name="ZH-CN_TOPIC_0000002441889101"></a>

### BurnTool Debug Console Settings<a name="ZH-CN_TOPIC_0000002441768885"></a>

The BurnTool Debug console can be configured in Preferences.

1.  Navigate to **Window** > **Preferences** in the menu bar, go to the **BurnTool** page, and select the **Open Debug Mode** button to enable the Debug console, as shown in [Figure 1](#_Ref410048637).

    **Figure 1**  Enable Debug console<a name="_Ref410048637"></a>  
    ![](figures/选中开启Debug控制台.png "Enable Debug console")

2.  After flashing starts, the tool automatically creates a Debug console. Click the switch console button in the upper right corner of the console and select **BurnTool-Debug** to display the Debug console, as shown in [Figure 2](#_Ref410048738).

    **Figure 2**  Switch to BurnTool-Debug console<a name="_Ref410048738"></a>  
    ![](figures/切换BurnTool-Debug控制台.png "Switch to BurnTool-Debug console")

### Same Subnet Check Settings<a name="ZH-CN_TOPIC_0000002441768921"></a>

Navigate to **Window** > **Preferences** in the menu bar, go to the **BurnTool** page, and select **Check whether the PC and Board IP addresses are in the same network segment**, as shown in [Figure 1](#_Ref410048821). When selected, BurnTool checks before flashing whether the PC and board IP addresses are on the same subnet. When deselected, this check is skipped.

**Figure 1**  Same subnet check settings<a name="_Ref410048821"></a>  
![](figures/检查同一网段设置页面.png "Same subnet check settings")

# FAQ
## How to Resolve TFTP Timeout Errors During BurnTool Flashing<a name="ZH-CN_TOPIC_0000002408169704"></a>

**Problem Description<a name="section9846741144918"></a>**

A TFTP error appears as shown in [Figure 1](#_Ref386011440). How should this be resolved?

**Figure 1**  TFTP timeout error<a name="_Ref386011440"></a>  
![](figures/TFTP超时问题.png "TFTP timeout error")

**Solution<a name="section05094512502"></a>**

Address this issue from the following four aspects:

-   Verify the BurnTool network configuration as shown in [Figure 2](#_Ref386011442). First, check whether the server IP is correct — if not, click Reload to fetch the latest PC IP address. Then verify the subnet mask and gateway are configured correctly. If they are correct, check whether the board IP address is in use (use the ping command to verify connectivity — if the ping fails, the network is not reachable). Once all parameters are confirmed correct, retry flashing.

    **Figure 2**  Check network configuration<a name="_Ref386011442"></a>  
    ![](figures/检查网络配置是否正确.png "Check network configuration")

-   Use an external tftpd32 tool instead of the built-in TFTP (refer to "[How to Use External tftpd32 for Image Download](#ZH-CN_TOPIC_0000002441889093)"). If tftpd32 also shows a timeout, check whether the network environment is functioning normally.
-   Modify the TFTP settings in the tool to match the current network environment. Navigate to **Window** > **Preferences** > **BurnTool** > **TFTP Setting** as shown in [Figure 3](#_Ref386007685), and increase the values for **The number of consecutive packet loss** and **TFTP no response timeout**, then retry flashing.
-   Verify that the firewall is disabled. If it is not, disable it.

    **Figure 3**  Modify TFTP settings<a name="_Ref386007685"></a>  
    ![](figures/修改TFTP设置.png "Modify TFTP settings")

## How to Use External tftpd32 for Image Download<a name="ZH-CN_TOPIC_0000002441889093"></a>

**Problem Description<a name="section43891210195218"></a>**

How to use an external tftpd32 for image download and what should be noted?

**Solution<a name="section9229816115214"></a>**

Steps to use external tftpd32:

1.  Before flashing, open the tftpd32 tool, select the correct PC IP address, and set the directory containing the images to be flashed, as shown in [Figure 1](#_Ref386011451).

    **Figure 1**  Configure tftpd32<a name="_Ref386011451"></a>  
    ![](figures/配置tftpd32工具.png "Configure tftpd32")

1.  In BurnTool, click the Flash button normally. A prompt dialog appears as shown in [Figure 2](#_Ref386011453). Click **OK** to start flashing — the external tftpd32 will be used for image download, as shown in [Figure 3](#_Ref386011454).

    **Figure 2**  Prompt: built-in TFTP failed to start, port occupied by external tftpd32<a name="_Ref386011453"></a>  
    ![](figures/提示内置TFTP启动失败-端口被外置tftpd32工具占.png "Prompt: built-in TFTP failed, port occupied by tftpd32")

    **Figure 3**  External tftpd32 downloading image<a name="_Ref386011454"></a>  
    ![](figures/外置tftpd32工具正在下载镜像.png "External tftpd32 downloading image")

## How to Resolve "Failed to send start frame" Error When Flashing the Fastboot Partition<a name="ZH-CN_TOPIC_0000002408329668"></a>

**Problem Description<a name="section17113181011420"></a>**

The error "Failed to send start frame" appears when flashing the Fastboot partition, as shown in [Figure 1](#_Ref386011456). What should I do?

**Figure 1**  "Failed to send start frame" error message<a name="_Ref386011456"></a>  
![](figures/Failed-to-send-start-frame-报错信息.png "\"Failed to send start frame\" error message")

**Solution<a name="section1951334642"></a>**

First, confirm whether the board was powered on within 15 seconds after clicking Flash. If the board was powered on in time, check that the serial port connection to the board is secure. If the connection is normal, verify that the correct serial port number is selected in BurnTool, as shown in [Figure 2](#_Ref386011460). Once all issues are confirmed and resolved, retry flashing.

**Figure 2**  Check serial port number selection<a name="_Ref386011460"></a>  
![](figures/检查串口号是否选择正确.png "Check serial port number selection")

## How to Resolve "Failed to send head frame" Error When Flashing the Fastboot Partition<a name="ZH-CN_TOPIC_0000002408169788"></a>

**Problem Description<a name="section1174175519"></a>**

When flashing the Fastboot partition, the console prints a segment of `#########` and then stops, and the error "Failed to send head frame" appears, as shown in [Figure 1](#_Ref386011462). How should this be resolved?

**Figure 1**  "Failed to send head frame" error message<a name="_Ref386011462"></a>  
![](figures/Failed-to-send-head-frame-报错信息.png "\"Failed to send head frame\" error message")

**Solution<a name="section1286417136513"></a>**

This error may be caused by one of the following:

-   The Fastboot image being flashed does not match the current board model. Check the board model label, then use the SDK image matching the correct chip and retry flashing.
-   The board DDR has a hardware issue and DDR initialization cannot be completed.

## How to Resolve "Failed to send data frame" Error When Flashing the Fastboot Partition<a name="ZH-CN_TOPIC_0000002441768861"></a>

**Problem Description<a name="section956919507512"></a>**

The error "Failed to send data frame" appears when flashing the Fastboot partition, as shown in [Figure 1](#_Ref386011468). What should I do?

**Figure 1**  "Failed to send data frame" error message<a name="_Ref386011468"></a>  
![](figures/Failed-to-send-data-frame-报错信息.png "\"Failed to send data frame\" error message")

**Solution<a name="section35233257619"></a>**

This error is likely caused by a loose serial port connection during Fastboot image flashing, preventing successful data transmission. Check the serial port connection.

## How to Resolve "Failed to execute command" Error When Flashing the Fastboot Partition<a name="ZH-CN_TOPIC_0000002408169752"></a>

**Problem Description<a name="section45431947769"></a>**

The error "Failed to execute command" appears when flashing the Fastboot partition, as shown in [Figure 1](#_Ref386011469). What should I do?

**Figure 1**  "Failed to execute command" error message<a name="_Ref386011469"></a>  
![](figures/Failed-to-execute-command-报错信息.png "\"Failed to execute command\" error message")

**Solution<a name="section1426113619713"></a>**

This error is likely caused by an incorrect flash type selection for the Fastboot partition. As shown in [Figure 2](#_Ref386011475), reboot the board and check the Flash type from the board startup log. For example, if the board uses eMMC, use the Burn eMMC flashing method and set the Fastboot partition flash type to emmc.

**Figure 2**  Check board flash information via serial port<a name="_Ref386011475"></a>  
![](figures/通过串口查看单板Flash信息.png "Check board flash information via serial port")

## What to Consider When Choosing the File Transfer Method<a name="ZH-CN_TOPIC_0000002408169696"></a>

**Problem Description<a name="section290917257720"></a>**

What are the advantages and disadvantages of serial port vs. network port for file transfer?

**Solution<a name="section15228123017718"></a>**

BurnTool's serial port flashing mode is pure serial port transfer. Since flashing requires transmitting large amounts of data to the board and serial ports have relatively low transfer rates, pure serial flashing is slow. Network port flashing is recommended. Pure serial flashing is very stable; if the network environment is unreliable, serial port flashing is an acceptable alternative.

## Length Requirement for Address-Based Flashing<a name="ZH-CN_TOPIC_0000002441889033"></a>

**Problem Description<a name="section129616216810"></a>**

What are the length requirements in the address-based flashing view?

**Solution<a name="section14316972810"></a>**

The erase length must be a multiple of the block size. For yaffs file system partial uploads, the length must be a multiple of (pagesize + oobsize).

## Why Does the Board Not Start Flashing After Clicking Flash and Power-Cycling<a name="ZH-CN_TOPIC_0000002441768873"></a>

**Problem Description<a name="section879943317814"></a>**

After clicking Flash and power-cycling the board, the tool does not start flashing. What is the cause?

**Solution<a name="section17459025490"></a>**

The serial port may be selected incorrectly or the serial port connection may be abnormal (verify using a terminal tool). Wait — the console will eventually print relevant diagnostic information.

## Why Is the Serial Port Not Found, or TFTP Fails to Start, or the TFTP Port Is Reported as Occupied on Linux<a name="ZH-CN_TOPIC_0000002408329620"></a>

**Problem Description<a name="section15781328107"></a>**

When using BurnTool on Linux, the serial port is not found, TFTP fails to start, or the TFTP port is reported as occupied. What are the possible causes?

**Solution<a name="section481113141014"></a>**

The tool is not running as root, so it lacks permission to start the TFTP service or access the serial port. The TFTP port occupied error may also be caused by another application occupying that port.

## What Do "pure data length" and "len_incl_bad" Mean in the Console When Flashing Nand<a name="ZH-CN_TOPIC_0000002408169776"></a>

**Problem Description<a name="section9483135101011"></a>**

What do the console outputs "pure data length" and "len_incl_bad" mean when flashing Nand?

**Solution<a name="section15954111011116"></a>**

As shown in [Figure 1](#_Ref386007893): `pure data length` is the actual data length being flashed; `len incl bad` is the actual flash space occupied including bad blocks. Neither length includes the OOB size.

**Figure 1**  Console output of flash length after flashing command<a name="_Ref386007893"></a>  
![](figures/控制台打印烧写命令反馈的烧写长度.png "Console output of flash length after flashing command")

## What Does the Tool Print When DDR Training Fails on the Board<a name="ZH-CN_TOPIC_0000002408329624"></a>

**Problem Description<a name="section1033016544115"></a>**

What output does the tool print when DDR Training fails on the board?

**Solution<a name="section2742102181210"></a>**

When DDR Training fails, the following message is printed during Fastboot partition flashing, as shown in [Figure 1](#_Ref386011496).

**Figure 1**  DDR Training failure message<a name="_Ref386011496"></a>  
![](figures/打印DDR-Training失败信息.png "DDR Training failure message")

## What Information to Provide When Reporting BurnTool Issues<a name="ZH-CN_TOPIC_0000002408329640"></a>

**Problem Description<a name="section4620102214128"></a>**

What information should be provided when reporting a BurnTool issue?

**Solution<a name="section10510122714124"></a>**

When a BurnTool issue occurs, export the console output using the export button in the console toolbar and include it with the issue report. This will greatly assist with issue diagnosis and resolution.

## How to Check Whether a Process Is Occupying TFTP Port 69<a name="ZH-CN_TOPIC_0000002408329684"></a>

**Problem Description<a name="section1072719116131"></a>**

TFTP always reports file not found even though all settings are correct. How can I check whether a process is occupying TFTP port 69?

**Solution<a name="section17557141213133"></a>**

A background process may be occupying port 69. Use the following method to check.

In a cmd window, enter the following command and output similar to [Figure 1](#_Ref413161493) will be printed:

`netstat -ano -p udp`

**Figure 1**  Viewing process port usage<a name="_Ref413161493"></a>  
![](figures/查看进程的端口占用.png "Viewing process port usage")

Check whether any process is occupying port 69. In the example above, the process with PID 7696 is occupying port 69. Use the following command to find the process name, with output similar to [Figure 2](#_Ref413161472):

`tasklist|findstr "7696"`

**Figure 2**  Finding process name by PID<a name="_Ref413161472"></a>  
![](figures/查看指定PID的进程名称.png "Finding process name by PID")

Then terminate that process in Task Manager.

## How to Handle a 64-bit PC with Only a 64-bit JRE Installed<a name="ZH-CN_TOPIC_0000002441768865"></a>

**Problem Description<a name="section234741210149"></a>**

A 64-bit JRE is installed on the PC and opening ToolPlatform produces an error. What should I do?

**Solution<a name="section16521321181418"></a>**

ToolPlatform depends on a 32-bit JRE. Before using ToolPlatform, download and install the Windows x86 version of JRE from the JRE official website: [http://www.oracle.com/technetwork/java/javase/downloads/](http://www.oracle.com/technetwork/java/javase/downloads/)

Note: ToolPlatform-XXX-4.0.15 and later versions include a bundled JRE — no separate JRE installation is required.

## Cannot Flash Images with Chinese Characters in the Path on Non-Chinese Language Systems<a name="ZH-CN_TOPIC_0000002441889049"></a>

**Problem Description<a name="section1999915715158"></a>**

On non-Chinese language systems, the tool cannot flash images with Chinese characters in the path. To check your system language, run the `chcp` command in cmd as shown in Figure 1. Code 437 indicates a US English system; 936 indicates a Chinese system.

**Figure 1**  Checking Windows system language<a name="_Ref4156611"></a>  
![](figures/查询windows语言系统方法.png "Checking Windows system language")

**Solution<a name="section185019199156"></a>**

Non-Chinese language systems do not support Chinese characters in image paths. Change the flash path to an all-English path.

# Abbreviations
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
