---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/GFBG 开发指南/GFBG 开发指南.md
--- # Preface
**Overview<a name="section151mcpsimp"></a>** Graphic Framebuffer Group (hereinafter referred to as GFBG) is a module provided by the digital media processing platform for managing graphics overlay layers. It is implemented based on the Linux Framebuffer, providing basic Linux Framebuffer functionality while extending additional graphics layer control features such as inter-layer Alpha and origin setting. This document primarily introduces how to load the GFBG module and develop applications for the first time. >![](public_sys-resources/icon-note.gif) **Note:** >- Unless otherwise specified, and Hi3403V100, and have completely identical content. **Product Version<a name="section155mcpsimp"></a>** The product versions corresponding to this document are as follows. <a name="table158mcpsimp"></a>
<table><thead align="left"><tr id="row163mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p165mcpsimp"><a name="p165mcpsimp"></a><a name="p165mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p167mcpsimp"><a name="p167mcpsimp"></a><a name="p167mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row169mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p171mcpsimp"><a name="p171mcpsimp"></a><a name="p171mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p173mcpsimp"><a name="p173mcpsimp"></a><a name="p173mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p178mcpsimp"><a name="p178mcpsimp"></a><a name="p178mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p165835179263"><a name="p165835179263"></a><a name="p165835179263"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1212383017264"><a name="p1212383017264"></a><a name="p1212383017264"></a>V101</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p982018196301"><a name="p982018196301"></a><a name="p982018196301"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9879931201010"><a name="p9879931201010"></a><a name="p9879931201010"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Intended Audience<a name="section179mcpsimp"></a>** This document (this guide) is primarily intended for the following engineers: - Technical support engineers
- Software development engineers **Symbol Conventions<a name="section185mcpsimp"></a>** The following symbols may appear in this document. Their meanings are as follows. <a name="table188mcpsimp"></a>
<table><thead align="left"><tr id="row193mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p195mcpsimp"><a name="p195mcpsimp"></a><a name="p195mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p197mcpsimp"><a name="p197mcpsimp"></a><a name="p197mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row199mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a><a name="image111"></a><a name="image111"></a><span><img id="image111" src="figures/zh-cn_image_0000002441655037.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>Indicates a hazard with a high level of risk that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section226mcpsimp"></a>** The revision history accumulates the description of each document update. The latest version of the document contains all update content from previous versions. <a name="table2161mcpsimp"></a>
<table><thead align="left"><tr id="row2167mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2169mcpsimp"><a name="p2169mcpsimp"></a><a name="p2169mcpsimp"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p2171mcpsimp"><a name="p2171mcpsimp"></a><a name="p2171mcpsimp"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p2173mcpsimp"><a name="p2173mcpsimp"></a><a name="p2173mcpsimp"></a>Modification Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2175mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2177mcpsimp"><a name="p2177mcpsimp"></a><a name="p2177mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p2179mcpsimp"><a name="p2179mcpsimp"></a><a name="p2179mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p2181mcpsimp"><a name="p2181mcpsimp"></a><a name="p2181mcpsimp"></a>First temporary version release.</p>
</td>
</tr>
</tbody>
</table> # Overview
## GFBG Introduction<a name="ZH-CN_TOPIC_0000002408095650"></a> Framebuffer (hereinafter referred to as GFBG) is a module provided by the digital media processing platform for managing overlay graphics layers. It not only provides basic Linux Framebuffer functionality, but also adds extended features on top of Linux Framebuffer, such as inter-layer colorkey, inter-layer colorkey mask, inter-layer Alpha, and origin offset. ### Architecture<a name="ZH-CN_TOPIC_0000002408255614"></a> Applications use GFBG based on the Linux filesystem. The architecture of GFBG is shown in [Figure 1](#fig103731568718). **Figure 1** GFBG architecture<a name="fig103731568718"></a> ![](figures/GFBG.png "GFBG")
### Application Scenarios<a name="ZH-CN_TOPIC_0000002441655009"></a> GFBG can be applied in the following scenarios: - Mini GUI window system Mini GUI supports Linux Framebuffer. With minor modifications to Mini GUI, it can be ported to the chip, enabling rapid porting. - Other Linux Framebuffer-based applications Applications based on Linux Framebuffer can be ported to the chip with no or minor modifications, enabling rapid porting. ## Comparison Between GFBG and Linux Framebuffer<a name="ZH-CN_TOPIC_0000002441694837"></a> ### Overlay Graphics Layer Management<a name="ZH-CN_TOPIC_0000002441655017"></a> In Linux Framebuffer, a sub-device number corresponds to a graphics card. In GFBG, a sub-device number corresponds to an overlay graphics layer. GFBG can manage multiple overlay graphics layers; the specific number is chip-dependent. >![](public_sys-resources/icon-note.gif) **Note:** >- For Hi3403V100, GFBG can manage up to 3 overlay graphics layers: graphics layers 0, 1, 3 (G0, G1, G3), with corresponding device files /dev/fb0, /dev/fb1, /dev/fb2 respectively.
> Hi3403V100 supports graphics layer overlay on 2 output devices: high-definition output device 0 (abbreviated as HD0) and standard-definition output device 0 (abbreviated as SD0). The relationship between the 3 graphics layers and the output devices is shown in [Table 3](#_Ref49523598). **Table 1** Correspondence between FB device files, graphics layers, and output devices <a name="_Toc363726513"></a>
<table><thead align="left"><tr id="row797mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p799mcpsimp"><a name="p799mcpsimp"></a><a name="p799mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p801mcpsimp"><a name="p801mcpsimp"></a><a name="p801mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="p803mcpsimp"><a name="p803mcpsimp"></a><a name="p803mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row805mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p807mcpsimp"><a name="p807mcpsimp"></a><a name="p807mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p809mcpsimp"><a name="p809mcpsimp"></a><a name="p809mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p811mcpsimp"><a name="p811mcpsimp"></a><a name="p811mcpsimp"></a>Can only be displayed on the HD0 device.</p>
</td>
</tr>
<tr id="row812mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p814mcpsimp"><a name="p814mcpsimp"></a><a name="p814mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p816mcpsimp"><a name="p816mcpsimp"></a><a name="p816mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p818mcpsimp"><a name="p818mcpsimp"></a><a name="p818mcpsimp"></a>Can only be displayed on the HD1 device.</p>
</td>
</tr>
<tr id="row819mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p821mcpsimp"><a name="p821mcpsimp"></a><a name="p821mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p823mcpsimp"><a name="p823mcpsimp"></a><a name="p823mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p825mcpsimp"><a name="p825mcpsimp"></a><a name="p825mcpsimp"></a>Can be dynamically bound to HD0, HD1, SD0 displays. G2 is the hardware cursor layer, and it is always at the highest layer of the display device overlay. If HD0 has a video layer, G0, and G2, the overlay order from bottom to top is: video layer, G0, G2.</p>
</td>
</tr>
<tr id="row826mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p828mcpsimp"><a name="p828mcpsimp"></a><a name="p828mcpsimp"></a>/dev/fb3</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p830mcpsimp"><a name="p830mcpsimp"></a><a name="p830mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p832mcpsimp"><a name="p832mcpsimp"></a><a name="p832mcpsimp"></a>Can be dynamically bound to HD0, HD1, SD0 displays. G3 is used as the smart frame layer.</p>
</td>
</tr>
</tbody>
</table> **Table 2** Correspondence between FB device files, graphics layers, and output devices <a name="_Ref49523582"></a>
<table><thead align="left"><tr id="row839mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p841mcpsimp"><a name="p841mcpsimp"></a><a name="p841mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p843mcpsimp"><a name="p843mcpsimp"></a><a name="p843mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row846mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p848mcpsimp"><a name="p848mcpsimp"></a><a name="p848mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p850mcpsimp"><a name="p850mcpsimp"></a><a name="p850mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p852mcpsimp"><a name="p852mcpsimp"></a><a name="p852mcpsimp"></a>Can only be displayed on the HD0 device.</p>
</td>
</tr>
<tr id="row853mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p855mcpsimp"><a name="p855mcpsimp"></a><a name="p855mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p857mcpsimp"><a name="p857mcpsimp"></a><a name="p857mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p859mcpsimp"><a name="p859mcpsimp"></a><a name="p859mcpsimp"></a>Can be dynamically bound to HD0, HD1, SD0 displays. G2 is the hardware cursor layer, and it is always at the highest layer of the display device overlay. If HD0 has a video layer, G0, and G2, the overlay order from bottom to top is: video layer, G0, G2.</p>
</td>
</tr>
<tr id="row860mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p862mcpsimp"><a name="p862mcpsimp"></a><a name="p862mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p864mcpsimp"><a name="p864mcpsimp"></a><a name="p864mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p866mcpsimp"><a name="p866mcpsimp"></a><a name="p866mcpsimp"></a>Can be dynamically bound to HD0, HD1, SD0 displays. G3 is used as the smart frame layer.</p>
</td>
</tr>
</tbody>
</table> **Table 3** Correspondence between FB device files, graphics layers, and output devices <a name="_Ref49523598"></a>
<table><thead align="left"><tr id="row873mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p875mcpsimp"><a name="p875mcpsimp"></a><a name="p875mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p877mcpsimp"><a name="p877mcpsimp"></a><a name="p877mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p879mcpsimp"><a name="p879mcpsimp"></a><a name="p879mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row880mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p882mcpsimp"><a name="p882mcpsimp"></a><a name="p882mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p884mcpsimp"><a name="p884mcpsimp"></a><a name="p884mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p886mcpsimp"><a name="p886mcpsimp"></a><a name="p886mcpsimp"></a>Can only be displayed on the HD0 device.</p>
</td>
</tr>
<tr id="row887mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p889mcpsimp"><a name="p889mcpsimp"></a><a name="p889mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p891mcpsimp"><a name="p891mcpsimp"></a><a name="p891mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p893mcpsimp"><a name="p893mcpsimp"></a><a name="p893mcpsimp"></a>Can only be displayed on the HD1 device.</p>
</td>
</tr>
<tr id="row894mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p896mcpsimp"><a name="p896mcpsimp"></a><a name="p896mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p898mcpsimp"><a name="p898mcpsimp"></a><a name="p898mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p900mcpsimp"><a name="p900mcpsimp"></a><a name="p900mcpsimp"></a>Can be dynamically bound to HD0, HD1, SD0 displays. G3 is used as the smart frame layer.</p>
</td>
</tr>
</tbody>
</table> **Table 4** Correspondence between FB device files, graphics layers, and output devices <a name="_Ref57989656"></a>
<table><thead align="left"><tr id="row907mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p909mcpsimp"><a name="p909mcpsimp"></a><a name="p909mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p911mcpsimp"><a name="p911mcpsimp"></a><a name="p911mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="p913mcpsimp"><a name="p913mcpsimp"></a><a name="p913mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row915mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p917mcpsimp"><a name="p917mcpsimp"></a><a name="p917mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p919mcpsimp"><a name="p919mcpsimp"></a><a name="p919mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p921mcpsimp"><a name="p921mcpsimp"></a><a name="p921mcpsimp"></a>Can only be displayed on the HD0 device.</p>
</td>
</tr>
<tr id="row922mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p924mcpsimp"><a name="p924mcpsimp"></a><a name="p924mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p926mcpsimp"><a name="p926mcpsimp"></a><a name="p926mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p928mcpsimp"><a name="p928mcpsimp"></a><a name="p928mcpsimp"></a>Can only be displayed on the HD1 device.</p>
</td>
</tr>
<tr id="row929mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p931mcpsimp"><a name="p931mcpsimp"></a><a name="p931mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p933mcpsimp"><a name="p933mcpsimp"></a><a name="p933mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p935mcpsimp"><a name="p935mcpsimp"></a><a name="p935mcpsimp"></a>Can be dynamically bound to HD0, HD1, SD0 displays. G2 is the hardware cursor layer, and it is always at the highest layer of the display device overlay. If HD0 has a video layer, G0, and G2, the overlay order from bottom to top is: video layer, G0, G2.</p>
</td>
</tr>
<tr id="row936mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p938mcpsimp"><a name="p938mcpsimp"></a><a name="p938mcpsimp"></a>/dev/fb3</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p940mcpsimp"><a name="p940mcpsimp"></a><a name="p940mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p942mcpsimp"><a name="p942mcpsimp"></a><a name="p942mcpsimp"></a>Can be dynamically bound to HD0, HD1 displays. G3 can be used as the smart frame layer.</p>
</td>
</tr>
<tr id="row943mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p945mcpsimp"><a name="p945mcpsimp"></a><a name="p945mcpsimp"></a>/dev/fb4</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p947mcpsimp"><a name="p947mcpsimp"></a><a name="p947mcpsimp"></a>G4</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p949mcpsimp"><a name="p949mcpsimp"></a><a name="p949mcpsimp"></a>Can be dynamically bound to HD1, SD0 displays. G4 can be used as the smart frame layer and as the standard-definition layer.</p>
</td>
</tr>
</tbody>
</table> Through module load parameters, GFBG can be controlled to manage one or multiple overlay graphics layers, and the overlay graphics layers can be operated like ordinary files. ### Solution Differences<a name="ZH-CN_TOPIC_0000002408255606"></a> <a name="table261mcpsimp"></a>
<table><thead align="left"><tr id="row270mcpsimp"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.7.1.1"><p id="p272mcpsimp"><a name="p272mcpsimp"></a><a name="p272mcpsimp"></a>Solution Name</p>
</th>
<th class="cellrowborder" valign="top" width="10.09100910091009%" id="mcps1.1.7.1.2"><p id="p274mcpsimp"><a name="p274mcpsimp"></a><a name="p274mcpsimp"></a>Supported Graphics Layers</p>
</th>
<th class="cellrowborder" valign="top" width="17.18171817181718%" id="mcps1.1.7.1.3"><p id="p276mcpsimp"><a name="p276mcpsimp"></a><a name="p276mcpsimp"></a>Compression Support</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.7.1.4"><p id="p278mcpsimp"><a name="p278mcpsimp"></a><a name="p278mcpsimp"></a>Scaling Support</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.1.7.1.5"><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>Binding Relationship</p>
</th>
<th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.1.7.1.6"><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>Soft Cursor</p>
</th>
</tr>
</thead>
</td>
<td class="cellrowborder" valign="top" width="10.09100910091009%" headers="mcps1.1.7.1.2 "><p id="p288mcpsimp"><a name="p288mcpsimp"></a><a name="p288mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="17.18171817181718%" headers="mcps1.1.7.1.3 "><p id="p290mcpsimp"><a name="p290mcpsimp"></a><a name="p290mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.7.1.4 "><p id="p292mcpsimp"><a name="p292mcpsimp"></a><a name="p292mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.7.1.5 "><p id="p294mcpsimp"><a name="p294mcpsimp"></a><a name="p294mcpsimp"></a>G0 is fixedly bound to HD0</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.7.1.6 "><p id="p296mcpsimp"><a name="p296mcpsimp"></a><a name="p296mcpsimp"></a>Not supported</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="10.09100910091009%" headers="mcps1.1.7.1.2 "><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="17.18171817181718%" headers="mcps1.1.7.1.3 "><p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.7.1.4 "><p id="p338mcpsimp"><a name="p338mcpsimp"></a><a name="p338mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.7.1.5 "><p id="p340mcpsimp"><a name="p340mcpsimp"></a><a name="p340mcpsimp"></a>G0 is fixedly bound to HD0</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.7.1.6 "><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>Not supported</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="10.09100910091009%" headers="mcps1.1.7.1.2 "><p id="p380mcpsimp"><a name="p380mcpsimp"></a><a name="p380mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="17.18171817181718%" headers="mcps1.1.7.1.3 "><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.7.1.4 "><p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.7.1.5 "><p id="p386mcpsimp"><a name="p386mcpsimp"></a><a name="p386mcpsimp"></a>G0 is fixedly bound to HD0</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.7.1.6 "><p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>Not supported</p>
</td>
</tr>
<tr id="row411mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="17.17171717171717%" headers="mcps1.1.7.1.1 "><p id="p413mcpsimp"><a name="p413mcpsimp"></a><a name="p413mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="10.09100910091009%" headers="mcps1.1.7.1.2 "><p id="p415mcpsimp"><a name="p415mcpsimp"></a><a name="p415mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="17.18171817181718%" headers="mcps1.1.7.1.3 "><p id="p417mcpsimp"><a name="p417mcpsimp"></a><a name="p417mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.7.1.4 "><p id="p419mcpsimp"><a name="p419mcpsimp"></a><a name="p419mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.7.1.5 "><p id="p421mcpsimp"><a name="p421mcpsimp"></a><a name="p421mcpsimp"></a>G0 is fixedly bound to HD0</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.7.1.6 "><p id="p423mcpsimp"><a name="p423mcpsimp"></a><a name="p423mcpsimp"></a>Not supported</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="10.09100910091009%" headers="mcps1.1.7.1.2 "><p id="p450mcpsimp"><a name="p450mcpsimp"></a><a name="p450mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="17.18171817181718%" headers="mcps1.1.7.1.3 "><p id="p452mcpsimp"><a name="p452mcpsimp"></a><a name="p452mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.7.1.4 "><p id="p454mcpsimp"><a name="p454mcpsimp"></a><a name="p454mcpsimp"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.7.1.5 "><p id="p456mcpsimp"><a name="p456mcpsimp"></a><a name="p456mcpsimp"></a>G0 is fixedly bound to HD0</p>
</td>
<td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.7.1.6 "><p id="p458mcpsimp"><a name="p458mcpsimp"></a><a name="p458mcpsimp"></a>Not supported</p>
</td>
</tr>
</tbody>
</table> ### Timing Control<a name="ZH-CN_TOPIC_0000002408095654"></a> Linux Framebuffer provides control methods such as synchronous timing, scan mode, and sync signal organization (requires hardware support) to display the contents of physical video memory on different output devices (such as PC monitors, T Vs, LC Ds, etc.). Currently, GFBG does not support control methods such as synchronous timing, scan mode, and sync signal organization. ### Standard and Extended Features<a name="ZH-CN_TOPIC_0000002408255602"></a> GFBG supports the following Linux Framebuffer standard features: - Mapping (or unmapping) physical video memory to virtual memory space.
- Operating physical video memory like ordinary files.
- Setting hardware display resolution and pixel format. The maximum resolution and pixel format supported by each overlay graphics layer can be obtained through the capability interface.
- Reading, writing, and displaying from any position in physical video memory.
- Setting and obtaining a 256-color palette when the overlay graphics layer supports indexed format. GFBG adds the following extended features: - Setting and obtaining the Alpha value of an overlay graphics layer.
- Setting and obtaining the colorkey value of an overlay graphics layer.
- Setting the starting position of the current overlay graphics layer (offset relative to the screen origin).
- Setting and obtaining the display state (show/hide) of the current overlay graphics layer.
- Configuring the physical video memory size of GFBG and the number of managed overlay graphics layers through module load parameters.
- Setting and obtaining the anti-flicker function state.
- Setting and obtaining premultiplied mode.
- Setting and obtaining the compression mode state.
- Setting/obtaining the graphics layer refresh type (0 buffer, 1 buffer, and 2 buffer). GFBG does not support the following Linux Framebuffer standard features: - Setting and obtaining the Linux Framebuffer corresponding to the console.
- Obtaining real-time hardware scan information.
- Obtaining hardware-related information.
- Setting hardware synchronous timing.
- Setting hardware sync signal mechanisms. ### Graphics Layer Refresh Types — FB Extended Mode<a name="ZH-CN_TOPIC_0000002441694841"></a> GFBG provides a complete refresh solution for upper-layer users, called the FB extended mode. Based on a comprehensive balance of system performance, memory, and graphics display effects, users can select an appropriate refresh solution according to their needs. The currently provided refresh types are: - 0 buffer (i.e., OT_FB_LAYER_BUF_NONE) The upper-layer user's drawing buffer is also the display buffer. This refresh type saves memory consumption and is the fastest, but the user will see the drawing process of the graphics. The illustration is shown in [Figure 1](#fig194946465118). - 1 buffer (i.e., OT_FB_LAYER_BUF_ONE) The display buffer is provided by GFBG, so it requires a certain amount of memory. This refresh type is a compromise between display effect and memory requirements. However, there will be tearing. The illustration is shown in [Figure 2](#fig76714267123). - 2 buffer The display buffer is provided by GFBG. Compared to the previous refresh types, it requires the most memory but has the best graphics display effect. The illustration is shown in [Figure 3](#fig1270123631220). It includes the following: - OT_FB_LAYER_BUF_DOUBLE - OT_FB_LAYER_BUF_DOUBLE_IMMEDIATE The difference between the two is that in the latter, each subsequent refresh operation waits until the drawn content is actually displayed before returning. **Figure 1** 0 buffer illustration<a name="fig194946465118"></a> ![](figures/0-buffershownmeaninggraph.png "0-buffershownmeaninggraph") **Figure 2** 1 buffer illustration<a name="fig76714267123"></a> ![](figures/1-buffershownmeaninggraph.png "1-buffershownmeaninggraph") **Figure 3** 2 buffer illustration<a name="fig1270123631220"></a> ![](figures/2-buffershownmeaninggraph.png "2-buffershownmeaninggraph")
>![](public_sys-resources/icon-note.gif) **Note:** >The three resolutions mentioned above: canvas resolution (i.e., the resolution of the user drawing buffer), video memory resolution, and screen display resolution. The process of drawing content from the user drawing buffer to the display buffer supports scaling and anti-flicker; while the process from the display buffer to the display device supports scaling but not anti-flicker. The video memory resolution and screen display resolution are the same by default; the screen resolution can be set via the FBIOPUT_SCREEN_SIZE interface. ### Graphics Layer Compression<a name="ZH-CN_TOPIC_0000002441694853"></a> The graphics layer compression function means that the graphics layer receives data compressed by TDE and then performs decompression display based on the compressed data. When the display buffer data does not change, the graphics layer loads the compressed data each time for decompression display. For graphics layers with compression enabled, the bus load bandwidth can be effectively reduced, but an additional frame of compressed data memory space needs to be allocated. A typical graphics layer compression buffer illustration is shown in [Figure 1](#fig1764612121513). **Figure 1** Compression buffer illustration<a name="fig1764612121513"></a> ![](figures/Compression-buffershownmeaninggraph.png "Compression-buffershownmeaninggraph") The compression function is only supported in FB extended refresh mode, under the OT_FB_LAYER_BUF_DOUBLE and OT_FB_LAYER_BUF_DOUBLE_IMMEDIATE refresh modes. ## Related Documents<a name="ZH-CN_TOPIC_0000002408255610"></a> Documents related to this guide: GFBG API Reference # Module Loading
## Principle Introduction<a name="ZH-CN_TOPIC_0000002408095666"></a> Some Linux Framebuffer drivers (such as versa) do not support changing display attributes such as resolution, color depth, and timing during runtime. For this, the Linux system provides a mechanism that allows corresponding options to be passed to the Linux Framebuffer through parameters during kernel boot or module loading. Kernel boot parameters can be configured in the kernel loader. When the GFBG driver is loaded, only the size of the physical video memory can be set; other options are not allowed. When loading the GFBG driver gfbg.ko, it must be ensured that the standard Framebuffer driver fb.ko is already loaded in the kernel. If it is not loaded, you can first load fb.ko using "modprobe fb", and then load gfbg.ko. ## Parameter Settings<a name="ZH-CN_TOPIC_0000002441694845"></a> GFBG can configure the size of the physical video memory for the overlay graphics layers it manages. The physical video memory size determines the maximum physical video memory that GFBG can use and the settable virtual resolution of the system. The physical video memory size is set through parameter passing when loading the GFBG driver, and once set, the physical video memory size will not change. ### Parameter video<a name="ZH-CN_TOPIC_0000002408095662"></a> ```
video="gfbg:vram0_size:xxx, vram1_size:xxx,…"
``` >![](public_sys-resources/icon-note.gif) **Note:** >- Options are separated by commas ",".
>- Options and option values are separated by colons ":".
>- If a graphics layer is not configured with a physical video memory size, the system defaults it to 0.
>- vram0_size to vram3_size correspond to overlay graphics layer 0 to overlay graphics layer 3 respectively. Where vramn_size:xxx indicates allocating xxx K bytes of physical video memory for overlay graphics layer n. (1) For FB standard mode, the relationship between vramn_size and virtual resolution is as follows: ```
Vramn_size * 1024 >= xres_virtual * yres_virtual * bpp;
``` Where: xres_virtual * yres_virtual is the virtual resolution, and bpp is the number of bytes per pixel. (2) For FB extended mode, the memory size required for each graphics layer depends on the display size, the layer pixel format, and the refresh mode. The specific relationship is as follows: ```
vramn_size * 1024 >= displaywidth * display Height * bpp * Buffer Mode;
``` For example: In 2 buffer mode with a resolution of 1280×720 and ARGB8888 format, the memory required for graphics layer 0 is vram0_size = 1280×720×4×2 = 7200 K. >![](public_sys-resources/icon-note.gif) **Note:** >vramn_size must be a multiple of PAGE_SIZE (4 K bytes); otherwise, the GFBG driver forces it to be a multiple of PAGE_SIZE, rounding up. ### Parameter softcursor<a name="ZH-CN_TOPIC_0000002441655013"></a> This parameter determines whether to enable the soft cursor function. When its value is "off", the soft cursor function is disabled (i.e., the hardware cursor function is available); otherwise, the soft cursor function is enabled. Once the module is loaded, whether the soft cursor function is enabled is determined. >![](public_sys-resources/icon-note.gif) **Note:** >Hi3403V100 do not support the soft cursor. ### Parameter g_layer_mmz_names<a name="ZH-CN_TOPIC_0000002441655021"></a> This parameter determines from which MMZ the memory to be used by each graphics layer will be allocated. This parameter is a string array, allowing a maximum of 4 values, corresponding to fb0–fb3 in order. Once the module is loaded, from which MMZ the memory to be used by each graphics layer is allocated is determined. If no value is specified, the system defaults that the memory to be used by the corresponding layer will be allocated from an unnamed MMZ. - insmod gfbg.ko g_layer_mmz_names=xxxx,xxxx,xxxx,xxxx video="gfbg:vram0_size:32400, vram1_size:32400, vram2_size:256, vram3_size:4052"
- The above 4 xxxx strings correspond to the MMZ partition names to be specified for fb0–fb3 respectively. The partition name must actually exist for it to take effect; otherwise, the memory will be allocated from an unnamed MMZ. No customer has used this yet; this module parameter function is retained. ### Default Parameter Values<a name="ZH-CN_TOPIC_0000002408255598"></a> If the GFBG driver is loaded without any parameters, the system's default configured parameter values are as follows. video="gfbg:vram0_size: 32400, vram1_size: 16200, vram2_size:256, vram3_size: 4052 " video="gfbg:vram0_size: 32400, vram1_size: 16200, vram2_size:256, vram3_size: 4052 " - Hi3403V100 video="gfbg:vram0_size: 32400, vram1_size: 16200, vram3_size: 3240 " video=" gfbg:vram0_size:32400, vram1_size:16200, vram2_size:256,vram3_size:4052, vram4_size:4052 " Users need to configure, from a global perspective, the overlay graphics layers that GFBG needs to manage and from which MMZ the corresponding storage space should be allocated, and allocate appropriate video memory for each overlay graphics layer. ## Configuration Examples<a name="ZH-CN_TOPIC_0000002441694849"></a> Examples of configuring GFBG to manage overlay graphics layers are as follows: >![](public_sys-resources/icon-note.gif) **Note:** >The module file of the GFBG driver is gfbg.ko. - Configuring GFBG to manage one overlay graphics layer. If you only need GFBG to manage overlay graphics layer 0, and the maximum virtual resolution is 720 × 576, using the ARGB1555 pixel format, then the minimum video memory required for overlay graphics layer 0 is 720 × 576 × 2 = 829440 = 810 K. The configuration parameter is as follows: insmod gfbg.ko video="gfbg:vram0_size:810, vram2_size:0". If using double buffer mode, multiply by 2, i.e.: insmod gfbg.ko video="gfbg:vram0_size:1620, vram2_size:0". - Configuring GFBG to manage multiple overlay graphics layers. If you need GFBG to manage two overlay layers, overlay graphics layer 0 and overlay graphics layer 1, and the maximum virtual resolution is 720 × 576, using the ARGB1555 pixel format, then the minimum video memory required for both overlay layers is 720 × 576 × 2 = 829440 = 810 K. The configuration parameter is as follows: insmod gfbg.ko video="gfbg:vram0_size:810, vram1_size: 810" ## Abnormal Situations<a name="ZH-CN_TOPIC_0000002408255618"></a> The following abnormal situation may occur when configuring GFBG: if the configured overlay graphics layer physical video memory data is incorrect, GFBG will not manage the corresponding overlay graphics layer. # First Application Development
## Development Process<a name="ZH-CN_TOPIC_0000002441655025"></a> GFBG is primarily used for displaying 2D graphics (by directly operating physical video memory). The development process of GFBG is shown in [Figure 1](#fig031318474168). **Figure 1** GFBG development process<a name="fig031318474168"></a> ![](figures/GFB Gopenstream.png "GFB Gopenstream") The development steps for GFBG are as follows: 1. Call the VO initialization interface to open the VO device.
2. Call the open function to open the specified GFBG device.
3. Call the ioctl function to set GFBG parameters such as pixel format and screen width/height (for details, please refer to the GFBG API Reference).
4. Call the ioctl function to obtain fixed information such as the physical video memory size and stride allocated by GFBG. The ioctl function can also be used to access GFBG-provided features such as inter-layer colorkey, inter-layer colorkey mask, inter-layer alpha, and origin offset.
5. Call the mmap function to map the physical video memory to the virtual memory space.
6. Operate the virtual memory to complete specific drawing tasks. At this step, GFBG-provided features such as double-buffer page flipping can be used to achieve certain rendering effects.
7. Call munmap to unmap the video memory.
8. Call the close function to close the device. >![](public_sys-resources/icon-note.gif) **Note:** >Since modifying the virtual resolution will change the fixed information of GFBG, fb_fix_screeninfo::line_length (stride), to ensure that the drawing program executes correctly, it is recommended to first set the variable information fb_var_screeninfo of GFBG, and then obtain the fixed information fb_fix_screeninfo::line_length of GFBG. The tasks completed in each development stage of GFBG are shown in [Table 1](#table3584165011503). **Table 1** GFBG development stage task list <a name="table3584165011503"></a>
<table><thead align="left"><tr id="row11633165055016"><th class="cellrowborder" valign="top" width="32.769999999999996%" id="mcps1.2.3.1.1"><p id="p1633850195013"><a name="p1633850195013"></a><a name="p1633850195013"></a>Stage</p>
</th>
<th class="cellrowborder" valign="top" width="67.23%" id="mcps1.2.3.1.2"><p id="p13633145019505"><a name="p13633145019505"></a><a name="p13633145019505"></a>Task</p>
</th>
</tr>
</thead>
<tbody><tr id="row66341750185015"><td class="cellrowborder" valign="top" width="32.769999999999996%" headers="mcps1.2.3.1.1 "><p id="p106341050105012"><a name="p106341050105012"></a><a name="p106341050105012"></a>Initialization stage</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.3.1.2 "><p id="p563495055017"><a name="p563495055017"></a><a name="p563495055017"></a>Complete the setting of display attributes and the mapping of physical video memory.</p>
</td>
</tr>
<tr id="row1163418504507"><td class="cellrowborder" valign="top" width="32.769999999999996%" headers="mcps1.2.3.1.1 "><p id="p7634150115015"><a name="p7634150115015"></a><a name="p7634150115015"></a>Drawing stage</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.3.1.2 "><p id="p26341750195014"><a name="p26341750195014"></a><a name="p26341750195014"></a>Complete specific drawing work.</p>
</td>
</tr>
<tr id="row1563445095016"><td class="cellrowborder" valign="top" width="32.769999999999996%" headers="mcps1.2.3.1.1 "><p id="p563416504501"><a name="p563416504501"></a><a name="p563416504501"></a>Termination stage</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.3.1.2 "><p id="p19634750105020"><a name="p19634750105020"></a><a name="p19634750105020"></a>Complete resource cleanup (steps 6, 7).</p>
<p id="p13634450115016"><a name="p13634450115016"></a><a name="p13634450115016"></a><strong id="b14634135045010"><a name="b14634135045010"></a><a name="b14634135045010"></a>Note: This operation must be performed before ss_mpi_sys_exit, because fb depends on sys resources.</strong></p>
</td>
</tr>
</tbody>
</table> ## Example Introduction<a name="ZH-CN_TOPIC_0000002408095646"></a> This example uses PAN_DISPLAY to continuously display 15 images with a resolution of 640×352 to achieve a dynamic display effect. Each file stores raw data in the ARGB1555 pixel format (image data without additional header information). [Reference Code] ```
#include <stdio.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <linux/fb.h>
#include "gfbg.h" #define IMAGE_WIDTH 640
#define IMAGE_HEIGHT 352
#define IMAGE_SIZE (640*352*2)
#define IMAGE_NUM 14
#define IMAGE_PATH "./res/%d.bits" static struct fb_bitfield g_r16 = {10, 5, 0};
static struct fb_bitfield g_g16 = {5, 5, 0};
static struct fb_bitfield g_b16 = {0, 5, 0};
static struct fb_bitfield g_a16 = {15, 1, 0}; int main
{ int fd; int i; struct fb_fix_screeninfo fix; struct fb_var_screeninfo var; unsigned char *show_screen; unsigned char *hide_screen; ot_fb_point point = {40, 112};
FILE *fp;
ot_vo_pub_attr stPubAttr = {0}; char image_name[128]; /*0. open VO device 0 */
/* …… initialize the attributes for st Pub Attr */ ss_mpi_vo_set_pub_attr(0, &stPubAttr);
ss_mpi_vo_enable(0); /*1. open Framebuffer device overlay 0*/ fd = open("/dev/fb0", O_RDWR); if(fd < 0) { printf("open fb0 failed!\n"); return -1; } /*2. set the screen original position*/ if (ioctl(fd, FBIOPUT_SCREEN_ORIGIN_GFBG, &point) < 0) { printf("set screen original show position failed!\n"); return -1; } /*3. get the variable screen info*/ if (ioctl(fd, FBIOGET_VSCREENINFO, &var) < 0) { printf("Get variable screen info failed!\n"); close(fd); return -1; } /*4. modify the variable screen info the screen size: IMAGE_WIDTH*IMAGE_HEIGHT the virtual screen size: IMAGE_WIDTH*(IMAGE_HEIGHT*2) the pixel format: ARGB1555 */ var.xres = var.xres_virtual = IMAGE_WIDTH; var.yres = IMAGE_HEIGHT; var.yres_virtual = IMAGE_HEIGHT*2; var.transp= g_a16; var.red = g_r16; var.green = g_g16; var.blue = g_b16; var.bits_per_pixel = 16; /*5. set the variable screeninfo*/ if (ioctl(fd, FBIOPUT_VSCREENINFO, &var) < 0) { printf("Put variable screen info failed!\n"); close(fd); return -1; } /*6. get the fix screen info*/ if (ioctl(fd, FBIOGET_FSCREENINFO, &fix) < 0) { printf("Get fix screen info failed!\n"); close(fd); return -1; } /*7. map the physical video memory for user use*/ show_screen = mmap(NULL, fix.smem_len, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0); hide_screen = show_screen + IMAGE_SIZE; memset(show_screen, 0, IMAGE_SIZE); /*8. load the bitmaps from file to hide screen and set pan display the hide screen*/ for(i = 0; i < IMAGE_NUM; i++) { sprintf(image_name, IMAGE_PATH, i); fp = fopen(image_name, "rb"); if(NULL == fp) { printf("Load %s failed!\n", image_name); close(fd); return -1; } fread(hide_screen, 1, IMAGE_SIZE, fp); fclose(fp); usleep(10); if(i%2) { var.yoffset = 0; hide_screen = show_screen + IMAGE_SIZE; } else { var.yoffset = IMAGE_HEIGHT; hide_screen = show_screen; } if (ioctl(fd, FBIOPAN_DISPLAY, &var) < 0) { printf("FBIOPAN_DISPLAY failed!\n"); close(fd); return -1; } } printf("Enter to quit!\n");
getchar; /*9. close the devices*/ close(fd);
ss_mpi_vo_disable(0); return 0;
```
