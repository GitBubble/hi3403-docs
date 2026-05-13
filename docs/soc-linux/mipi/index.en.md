---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/MIPI User Guide/MIPI User Guide.md
--- # Preface
**Product Version<a name="section178mcpsimp"></a>** The product versions corresponding to this document are as follows. <a name="table181mcpsimp"></a>
<table><thead align="left"><tr id="row186mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p188mcpsimp"><a name="p188mcpsimp"></a><a name="p188mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p190mcpsimp"><a name="p190mcpsimp"></a><a name="p190mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row192mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p194mcpsimp"><a name="p194mcpsimp"></a><a name="p194mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p119201326520"><a name="p119201326520"></a><a name="p119201326520"></a>V100</p>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **Note:** >This document uses the Hi3403V100 description as an example. Unless otherwise specified, the content for is consistent with Hi3403V100. **Target Audience<a name="section197mcpsimp"></a>** This document (guide) is primarily applicable to the following engineers: - Technical Support Engineer
- Software Development Engineer **Symbol Conventions<a name="section203mcpsimp"></a>** The following symbols may appear in this document, and their meanings are as follows. <a name="table206mcpsimp"></a>
<table><thead align="left"><tr id="row211mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p213mcpsimp"><a name="p213mcpsimp"></a><a name="p213mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row217mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p219mcpsimp"><a name="p219mcpsimp"></a><a name="p219mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="figures/zh-cn_image_0000002441661733.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p221mcpsimp"><a name="p221mcpsimp"></a><a name="p221mcpsimp"></a>Indicates a high-level risk hazard that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section244mcpsimp"></a>** The revision history accumulates descriptions of each document update. The latest version of the document includes updates from all previous document versions. <a name="table2674mcpsimp"></a>
<table><thead align="left"><tr id="row2680mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2682mcpsimp"><a name="p2682mcpsimp"></a><a name="p2682mcpsimp"></a><strong id="b2683mcpsimp"><a name="b2683mcpsimp"></a><a name="b2683mcpsimp"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p2685mcpsimp"><a name="p2685mcpsimp"></a><a name="p2685mcpsimp"></a><strong id="b2686mcpsimp"><a name="b2686mcpsimp"></a><a name="b2686mcpsimp"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p2688mcpsimp"><a name="p2688mcpsimp"></a><a name="p2688mcpsimp"></a><strong id="b2689mcpsimp"><a name="b2689mcpsimp"></a><a name="b2689mcpsimp"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2699mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2701mcpsimp"><a name="p2701mcpsimp"></a><a name="p2701mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p2703mcpsimp"><a name="p2703mcpsimp"></a><a name="p2703mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p2705mcpsimp"><a name="p2705mcpsimp"></a><a name="p2705mcpsimp"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table> # MIPI User Guide
## Overview<a name="ZH-CN_TOPIC_0000002408262262"></a> MIPI Rx receives raw video data through low-voltage differential signals, converts the received serial differential signal into DC (Digital Camera) timing, and then passes it to the next-level module VICAP (Video Capture). MIPI Rx supports serial video signal inputs such as MIPI D-PHY, LVDS (Low-Voltage Differential Signal), HiSPi (High-Speed Serial Pixel Interface), and is also compatible with the DC video interface. ## Important Concepts<a name="ZH-CN_TOPIC_0000002441701413"></a> - MIPI MIPI stands for Mobile Industry Processor Interface. The MIPI interface described in this document specifically refers to a communication interface that uses D-PHY transmission specification at the physical layer and CSI-2 at the protocol layer. - LVDS LVDS stands for Low-Voltage Differential Signaling. It uses synchronization codes to distinguish between blanking intervals and valid data. - Lane A pair of high-speed differential lines used to connect the transmitter and receiver. It can be either a clock Lane or a data Lane. - Synchronization Code The MIPI interface uses short packets within CSI-2 for synchronization. LVDS uses synchronization codes to distinguish valid data from blanking intervals. LVDS has two synchronization methods: - Using SOF/EOF to indicate frame start and end, and SOL/EOL to indicate line start and end. The synchronization method is shown in [Figure 1](#fig9405124663417). **Figure 1** SOF/EOF/SOL/EOL Synchronization Method<a name="fig9405124663417"></a> ![](figures/SOF-EOF-SOL-EOL synchronization method.png "SOF-EOF-SOL-EOL synchronization method") - Using SAV(invalid) EAV(invalid) to indicate the start and end of invalid data in the blanking interval, and SAV(valid) EAV(valid) to indicate the start and end of valid pixel data. Each synchronization code consists of 4 fields, each with a bit width consistent with the pixel data bit width. The first 3 fields are fixed reference code words, and the 4th field is determined by the sensor manufacturer. Since different sensors may have different synchronization codes, the synchronization code must be configured according to the sensor. The synchronization method is shown in [Figure 2](#fig1737184853619). **Figure 2** SAV/EAV Synchronization Method<a name="fig1737184853619"></a> ![](figures/SAV-EAV synchronization method.png "SAV-EAV synchronization method") ## Functional Description<a name="ZH-CN_TOPIC_0000002408262130"></a> MIPI Rx is a capture unit that supports multiple differential video input interfaces. It receives data from MIPI/LVDS/sub-LVDS/HiSPi/DC interfaces through combo-PHY. By configuring different functional modes, MIPI Rx can support data transmission at various speeds and resolutions, and support multiple external input devices. The maximum number of supported Lanes is shown in [Table 1](#_Ref484179711). **Table 1** Maximum Number of Supported Lanes <a name="_Ref484179711"></a>
<table><thead align="left"><tr id="row472mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.3.1.1"><p id="p474mcpsimp"><a name="p474mcpsimp"></a><a name="p474mcpsimp"></a>Solution</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.3.1.2"><p id="p476mcpsimp"><a name="p476mcpsimp"></a><a name="p476mcpsimp"></a>Maximum Number of Lanes</p>
</th>
</tr>
</thead>
<tbody><tr id="row477mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="p479mcpsimp"><a name="p479mcpsimp"></a><a name="p479mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><p id="p481mcpsimp"><a name="p481mcpsimp"></a><a name="p481mcpsimp"></a>MIPI Rx supports up to 8-Lane MIPI input or 8-Lane LVDS input.</p>
</td>
</tr>
</tbody>
</table> MIPI Rx can interface with multiple sensors simultaneously. The maximum number of sensors is shown in [Table 2](#_Ref502909111). **Table 2** Maximum Number of Connected Sensors <a name="_Ref502909111"></a>
<table><thead align="left"><tr id="row489mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.3.1.1"><p id="p491mcpsimp"><a name="p491mcpsimp"></a><a name="p491mcpsimp"></a>Solution</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.3.1.2"><p id="p493mcpsimp"><a name="p493mcpsimp"></a><a name="p493mcpsimp"></a>Number of Sensors</p>
</th>
</tr>
</thead>
<tbody><tr id="row495mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><p id="p499mcpsimp"><a name="p499mcpsimp"></a><a name="p499mcpsimp"></a>4</p>
</td>
</tr>
</tbody>
</table> MIPI Rx can interface with different numbers of sensors simultaneously, and each sensor may require a different number of Lanes. Therefore, users need to determine the LANE distribution mode of MIPI Rx. For specific Lane distribution modes, please refer to [Table 3](#_Toc468799631). **Table 3** MIPI Rx Lane Distribution Mode <a name="_Toc468799631"></a>
<table><thead align="left"><tr id="row511mcpsimp"><th class="cellrowborder" valign="top" width="26.732673267326735%" id="mcps1.2.7.1.1"><p id="p513mcpsimp"><a name="p513mcpsimp"></a><a name="p513mcpsimp"></a>Solution</p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811883%" id="mcps1.2.7.1.2"><p id="p515mcpsimp"><a name="p515mcpsimp"></a><a name="p515mcpsimp"></a>Mode</p>
</th>
<th class="cellrowborder" valign="top" width="14.851485148514854%" id="mcps1.2.7.1.3"><p id="p517mcpsimp"><a name="p517mcpsimp"></a><a name="p517mcpsimp"></a>DEV0</p>
</th>
<th class="cellrowborder" valign="top" width="14.851485148514854%" id="mcps1.2.7.1.4"><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>DEV1</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415845%" id="mcps1.2.7.1.5"><p id="p521mcpsimp"><a name="p521mcpsimp"></a><a name="p521mcpsimp"></a>DEV2</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415845%" id="mcps1.2.7.1.6"><p id="p523mcpsimp"><a name="p523mcpsimp"></a><a name="p523mcpsimp"></a>DEV3</p>
</th>
</tr>
</thead>
<tbody><tr id="row525mcpsimp"><td class="cellrowborder" rowspan="4" valign="top" width="26.732673267326735%" headers="mcps1.2.7.1.1 "><p id="p527mcpsimp"><a name="p527mcpsimp"></a><a name="p527mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.7.1.2 "><p id="p529mcpsimp"><a name="p529mcpsimp"></a><a name="p529mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.7.1.3 "><p id="p531mcpsimp"><a name="p531mcpsimp"></a><a name="p531mcpsimp"></a>L0~L7</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.7.1.4 "><p id="p533mcpsimp"><a name="p533mcpsimp"></a><a name="p533mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415845%" headers="mcps1.2.7.1.5 "><p id="p535mcpsimp"><a name="p535mcpsimp"></a><a name="p535mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415845%" headers="mcps1.2.7.1.6 "><p id="p537mcpsimp"><a name="p537mcpsimp"></a><a name="p537mcpsimp"></a>N</p>
</td>
</tr>
</tbody>
</table> For detailed MIPI Rx Lane pin connections, please refer to [Table 4](#_Ref484014656). **Table 4** MIPI Rx Lane Pin Relationship <a name="_Ref484014656"></a>
<table><thead align="left"><tr id="row582mcpsimp"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.7.1.1"><p id="p584mcpsimp"><a name="p584mcpsimp"></a><a name="p584mcpsimp"></a>Solution</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.7.1.2"><p id="p586mcpsimp"><a name="p586mcpsimp"></a><a name="p586mcpsimp"></a>LANE</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415845%" id="mcps1.2.7.1.3"><p id="p588mcpsimp"><a name="p588mcpsimp"></a><a name="p588mcpsimp"></a>MIPI0</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415845%" id="mcps1.2.7.1.4"><p id="p590mcpsimp"><a name="p590mcpsimp"></a><a name="p590mcpsimp"></a>MIPI1</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415845%" id="mcps1.2.7.1.5"><p id="p592mcpsimp"><a name="p592mcpsimp"></a><a name="p592mcpsimp"></a>MIPI2</p>
</th>
<th class="cellrowborder" valign="top" width="14.851485148514854%" id="mcps1.2.7.1.6"><p id="p594mcpsimp"><a name="p594mcpsimp"></a><a name="p594mcpsimp"></a>MIPI3</p>
</th>
</tr>
</thead>
<tbody><tr id="row596mcpsimp"><td class="cellrowborder" rowspan="8" valign="top" width="18.81188118811881%" headers="mcps1.2.7.1.1 "><p id="p598mcpsimp"><a name="p598mcpsimp"></a><a name="p598mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.7.1.2 "><p id="p600mcpsimp"><a name="p600mcpsimp"></a><a name="p600mcpsimp"></a>Lane0</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415845%" headers="mcps1.2.7.1.3 "><p id="p602mcpsimp"><a name="p602mcpsimp"></a><a name="p602mcpsimp"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415845%" headers="mcps1.2.7.1.4 "><p id="entry603mcpsimpp0"><a name="entry603mcpsimpp0"></a><a name="entry603mcpsimpp0"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415845%" headers="mcps1.2.7.1.5 "><p id="entry604mcpsimpp0"><a name="entry604mcpsimpp0"></a><a name="entry604mcpsimpp0"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.7.1.6 "><p id="entry605mcpsimpp0"><a name="entry605mcpsimpp0"></a><a name="entry605mcpsimpp0"></a>-</p>
</td>
</tr>
<tr id="row606mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p608mcpsimp"><a name="p608mcpsimp"></a><a name="p608mcpsimp"></a>Lane1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p610mcpsimp"><a name="p610mcpsimp"></a><a name="p610mcpsimp"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p612mcpsimp"><a name="p612mcpsimp"></a><a name="p612mcpsimp"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="entry613mcpsimpp0"><a name="entry613mcpsimpp0"></a><a name="entry613mcpsimpp0"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="entry614mcpsimpp0"><a name="entry614mcpsimpp0"></a><a name="entry614mcpsimpp0"></a>-</p>
</td>
</tr>
</tbody>
</table>
