---
title: "Graphics Development User Guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/图形开发用户指南/图形开发用户指南.md
---

# Preface
**Overview<a name="section143mcpsimp"></a>**

This document presents one recommended solution for graphics development, covering the solution overview, derived variants, development workflow, applicable scenarios, and the associated advantages and limitations. It serves as a reference for users developing graphics applications.

>![](../../../multimedia/graphics/dev/public_sys-resources/icon-note.gif) **Note:** 
>-   Unless otherwise stated, SS528V100, SS625V100, SS524V100, SS522V101, and SS626V100 are fully identical.
>-   Unless otherwise stated, SS927V100 and SS928V100, and SS522V100 and SS524V100 are fully identical.

**Product Versions<a name="section147mcpsimp"></a>**

The product versions corresponding to this document are listed below.

<a name="table150mcpsimp"></a>
<table><thead align="left"><tr id="row155mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p159mcpsimp"><a name="p159mcpsimp"></a><a name="p159mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row161mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p165mcpsimp"><a name="p165mcpsimp"></a><a name="p165mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row166mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p168mcpsimp"><a name="p168mcpsimp"></a><a name="p168mcpsimp"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p170mcpsimp"><a name="p170mcpsimp"></a><a name="p170mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1159710223415"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p881081984715"><a name="p881081984715"></a><a name="p881081984715"></a>SS524</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
<tr id="row3806135719163"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p327216178"><a name="p327216178"></a><a name="p327216178"></a>SS522</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1927181171714"><a name="p1927181171714"></a><a name="p1927181171714"></a>V100</p>
</td>
</tr>
<tr id="row1154655371615"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p21174601717"><a name="p21174601717"></a><a name="p21174601717"></a>SS522</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1211713611717"><a name="p1211713611717"></a><a name="p1211713611717"></a>V101</p>
</td>
</tr>
<tr id="row13305165014598"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p175361749141815"><a name="p175361749141815"></a><a name="p175361749141815"></a>SS528</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13835920181"><a name="p13835920181"></a><a name="p13835920181"></a>V100</p>
</td>
</tr>
<tr id="row14441920446"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p544495443"><a name="p544495443"></a><a name="p544495443"></a>SS625</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1844992446"><a name="p1844992446"></a><a name="p1844992446"></a>V100</p>
</td>
</tr>
<tr id="row124425241073"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section171mcpsimp"></a>**

This document is primarily intended for:

-   Technical support engineers
-   Software development engineers

**Symbol Conventions<a name="section177mcpsimp"></a>**

The following symbols may appear in this document with the meanings described below.

<a name="table180mcpsimp"></a>
<table><thead align="left"><tr id="row185mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p189mcpsimp"><a name="p189mcpsimp"></a><a name="p189mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row191mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="/multimedia/graphics/dev/figures/zh-cn_image_0000002441674969.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p195mcpsimp"><a name="p195mcpsimp"></a><a name="p195mcpsimp"></a>Indicates a high-risk hazard that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row196mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="/multimedia/graphics/dev/figures/zh-cn_image_0000002441714837.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p200mcpsimp"><a name="p200mcpsimp"></a><a name="p200mcpsimp"></a>Indicates a medium-risk hazard that, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row201mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="/multimedia/graphics/dev/figures/zh-cn_image_0000002408275562.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p205mcpsimp"><a name="p205mcpsimp"></a><a name="p205mcpsimp"></a>Indicates a low-risk hazard that, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row206mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p208mcpsimp"><a name="p208mcpsimp"></a><a name="p208mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="/multimedia/graphics/dev/figures/zh-cn_image_0000002408115618.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p210mcpsimp"><a name="p210mcpsimp"></a><a name="p210mcpsimp"></a>Conveys device or environmental safety warnings. Failure to follow this guidance may result in equipment damage, data loss, performance degradation, or other unpredictable outcomes.</p>
<p id="p211mcpsimp"><a name="p211mcpsimp"></a><a name="p211mcpsimp"></a>"Notice" does not involve personal injury.</p>
</td>
</tr>
<tr id="row212mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="/multimedia/graphics/dev/figures/zh-cn_image_0000002441674901.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p216mcpsimp"><a name="p216mcpsimp"></a><a name="p216mcpsimp"></a>Provides supplementary information for key content in the text.</p>
<p id="p217mcpsimp"><a name="p217mcpsimp"></a><a name="p217mcpsimp"></a>"Note" is not a safety warning and does not involve personal, equipment, or environmental hazards.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section218mcpsimp"></a>**

The revision history accumulates descriptions of each document update. The latest version of this document incorporates all updates from previous versions.

<a name="table126443203200"></a>
<table><thead align="left"><tr id="row264516207203"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p146456203200"><a name="p146456203200"></a><a name="p146456203200"></a><strong id="b8645172022010"><a name="b8645172022010"></a><a name="b8645172022010"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p364512062019"><a name="p364512062019"></a><a name="p364512062019"></a><strong id="b1464512200200"><a name="b1464512200200"></a><a name="b1464512200200"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p664522018206"><a name="p664522018206"></a><a name="p664522018206"></a><strong id="b156451420152010"><a name="b156451420152010"></a><a name="b156451420152010"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row56451520182017"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p1564572014209"><a name="p1564572014209"></a><a name="p1564572014209"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p126451920132014"><a name="p126451920132014"></a><a name="p126451920132014"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1664582017209"><a name="p1664582017209"></a><a name="p1664582017209"></a>First preliminary release.</p>
</td>
</tr>
</tbody>
</table>

# Graphics Layer Overview
## Overview<a name="ZH-CN_TOPIC_0000002408275422"></a>

The digital media processing platform provides a complete set of mechanisms for developing graphical interfaces. The main components are:

-   Two Dimensional Engine (TDE): a hardware-accelerated engine for processing graphics and images.
-   Graphic Framebuffer Group (GFBG): manages overlapping graphics layers. In addition to the standard Linux Framebuffer functionality, GFBG adds extended features such as inter-layer colorkey and inter-layer alpha blending.

>![](../../../multimedia/graphics/dev/public_sys-resources/icon-note.gif) **Note:** 
>-   For TDE usage, refer to the *TDE API Reference*.
>-   For GFBG usage, refer to the *GFBG Developer Guide* and *GFBG API Reference*.

## Graphics Layer Architecture<a name="ZH-CN_TOPIC_0000002441674809"></a>

-   SS528V100/SS625V100/SS524V100 support 2 HD display outputs (HD0, HD1) and 1 SD display output (SD0), along with 4 graphics layers: G0, G1, G2, and G3.
-   SS522V101 supports 1 HD display output (HD0) and 1 SD display output (SD0), along with 3 graphics layers: G0, G2, and G3.
-   SS928V100 supports 2 HD display outputs (HD0, HD1) and 1 SD display output (SD0), along with 3 graphics layers: G0, G1, and G3.
-   SS626V100 supports 2 HD display outputs (HD0, HD1) and 1 SD display output (SD0), along with 5 graphics layers: G0, G1, G2, G3, and G4.

>![](../../../multimedia/graphics/dev/public_sys-resources/icon-note.gif) **Note:** 
>For the interface types and timing supported by each output device, refer to the VDP chapter of the corresponding chip manual.

The mapping between graphics layers and display devices is subject to certain constraints, as shown in [Table 1](#_Ref391716435) through [Table 4](#_Ref57990861).

**Table 1** FB device files, graphics layers, and output device mappings (SS528V100/SS625V100/SS524V100)

<a name="_Ref391716435"></a>
<table><thead align="left"><tr id="row254mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p256mcpsimp"><a name="p256mcpsimp"></a><a name="p256mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p258mcpsimp"><a name="p258mcpsimp"></a><a name="p258mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p260mcpsimp"><a name="p260mcpsimp"></a><a name="p260mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row262mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p264mcpsimp"><a name="p264mcpsimp"></a><a name="p264mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p266mcpsimp"><a name="p266mcpsimp"></a><a name="p266mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p268mcpsimp"><a name="p268mcpsimp"></a><a name="p268mcpsimp"></a>G0 displays on the HD0 device.</p>
</td>
</tr>
<tr id="row269mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p271mcpsimp"><a name="p271mcpsimp"></a><a name="p271mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p273mcpsimp"><a name="p273mcpsimp"></a><a name="p273mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p275mcpsimp"><a name="p275mcpsimp"></a><a name="p275mcpsimp"></a>G1 displays on the HD1 device.</p>
</td>
</tr>
<tr id="row276mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p278mcpsimp"><a name="p278mcpsimp"></a><a name="p278mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>G2 displays on HD0, HD1, and SD0 devices.</p>
</td>
</tr>
<tr id="row283mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p285mcpsimp"><a name="p285mcpsimp"></a><a name="p285mcpsimp"></a>/dev/fb3</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p287mcpsimp"><a name="p287mcpsimp"></a><a name="p287mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p289mcpsimp"><a name="p289mcpsimp"></a><a name="p289mcpsimp"></a>G3 displays on HD0, HD1, and SD0 devices.</p>
</td>
</tr>
</tbody>
</table>

**Table 2** FB device files, graphics layers, and output device mappings (SS522V101)

<a name="table290mcpsimp"></a>
<table><thead align="left"><tr id="row297mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p299mcpsimp"><a name="p299mcpsimp"></a><a name="p299mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p301mcpsimp"><a name="p301mcpsimp"></a><a name="p301mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p303mcpsimp"><a name="p303mcpsimp"></a><a name="p303mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row305mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p309mcpsimp"><a name="p309mcpsimp"></a><a name="p309mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p311mcpsimp"><a name="p311mcpsimp"></a><a name="p311mcpsimp"></a>G0 displays on the HD0 device.</p>
</td>
</tr>
<tr id="row312mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p314mcpsimp"><a name="p314mcpsimp"></a><a name="p314mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>G2 displays on HD0, HD1, and SD0 devices.</p>
</td>
</tr>
<tr id="row319mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p321mcpsimp"><a name="p321mcpsimp"></a><a name="p321mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p323mcpsimp"><a name="p323mcpsimp"></a><a name="p323mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p325mcpsimp"><a name="p325mcpsimp"></a><a name="p325mcpsimp"></a>G3 displays on HD0, HD1, and SD0 devices.</p>
</td>
</tr>
</tbody>
</table>

**Table 3** FB device files, graphics layers, and output device mappings (SS928V100)

<a name="table326mcpsimp"></a>
<table><thead align="left"><tr id="row333mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p335mcpsimp"><a name="p335mcpsimp"></a><a name="p335mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p337mcpsimp"><a name="p337mcpsimp"></a><a name="p337mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p339mcpsimp"><a name="p339mcpsimp"></a><a name="p339mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row341mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p343mcpsimp"><a name="p343mcpsimp"></a><a name="p343mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p345mcpsimp"><a name="p345mcpsimp"></a><a name="p345mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p347mcpsimp"><a name="p347mcpsimp"></a><a name="p347mcpsimp"></a>G0 displays on the HD0 device.</p>
</td>
</tr>
<tr id="row348mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p350mcpsimp"><a name="p350mcpsimp"></a><a name="p350mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p352mcpsimp"><a name="p352mcpsimp"></a><a name="p352mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p354mcpsimp"><a name="p354mcpsimp"></a><a name="p354mcpsimp"></a>G1 displays on the HD1 device.</p>
</td>
</tr>
<tr id="row355mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p357mcpsimp"><a name="p357mcpsimp"></a><a name="p357mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p361mcpsimp"><a name="p361mcpsimp"></a><a name="p361mcpsimp"></a>G3 displays on HD0, HD1, and SD0 devices.</p>
</td>
</tr>
</tbody>
</table>

**Table 4** FB device files, graphics layers, and output device mappings (SS626V100)

<a name="_Ref57990861"></a>
<table><thead align="left"><tr id="row368mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p370mcpsimp"><a name="p370mcpsimp"></a><a name="p370mcpsimp"></a>FB Device File</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>Graphics Layer</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p374mcpsimp"><a name="p374mcpsimp"></a><a name="p374mcpsimp"></a>Corresponding Display Device</p>
</th>
</tr>
</thead>
<tbody><tr id="row376mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p378mcpsimp"><a name="p378mcpsimp"></a><a name="p378mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p380mcpsimp"><a name="p380mcpsimp"></a><a name="p380mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>G0 displays on the HD0 device.</p>
</td>
</tr>
<tr id="row383mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p385mcpsimp"><a name="p385mcpsimp"></a><a name="p385mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>G1 displays on the HD1 device.</p>
</td>
</tr>
<tr id="row390mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p392mcpsimp"><a name="p392mcpsimp"></a><a name="p392mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p394mcpsimp"><a name="p394mcpsimp"></a><a name="p394mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p396mcpsimp"><a name="p396mcpsimp"></a><a name="p396mcpsimp"></a>G2 displays on HD0, HD1, and SD0 devices.</p>
</td>
</tr>
<tr id="row397mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>/dev/fb3</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>G3 displays on HD0 and HD1 devices.</p>
</td>
</tr>
<tr id="row404mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p406mcpsimp"><a name="p406mcpsimp"></a><a name="p406mcpsimp"></a>/dev/fb4</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>G4</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>G4 displays on HD1 and SD0 devices.</p>
</td>
</tr>
</tbody>
</table>

>![](../../../multimedia/graphics/dev/public_sys-resources/icon-note.gif) **Note:** 
>To display graphics layers, users must first configure and start the output device, then use the GFBG module interface to enable the graphics layer for display.

# Recommended Graphics Development Solution
## Overview<a name="ZH-CN_TOPIC_0000002408275414"></a>

In the video capture domain, the graphical user interface content on a typical output device generally includes:

-   Back-end OSD: displays split lines, channel numbers, time, and other information to define multi-screen layout.
-   GUI: includes menus, progress bars, and other elements through which users configure the device.
-   Mouse cursor: provides a more convenient way to navigate interface menus.

These three categories of graphical content can be implemented using a single graphics layer or multiple graphics layers. For chips that provide multiple graphics layers, this guide helps users correctly, rationally, and effectively utilize these layers to meet different output interface requirements. The following solutions are provided for reference.

## Single-Layer UI Solution<a name="ZH-CN_TOPIC_0000002441714645"></a>

### Solution Overview<a name="ZH-CN_TOPIC_0000002408275406"></a>

The overall approach of this solution is: each output device uses a single graphics layer to handle the back-end OSD, GUI, and mouse cursor display for that device. The mouse cursor can alternatively be implemented using a dedicated cursor layer.

More specifically: each output device uses one graphics layer for its back-end OSD and GUI; the GUI is drawn onto a separate buffer, while the back-end OSD is drawn directly into the FB framebuffer memory, with alpha blending performed via TDE; the mouse cursor can use a dedicated cursor layer or share a layer with the OSD and GUI — when sharing, it is drawn onto the GUI buffer.

This solution uses the following mechanisms:

-   Each device's back-end OSD is drawn directly into its respective FB framebuffer memory.

    For example, split layout lines, channel numbers, or timestamps are drawn into the FB framebuffer of each graphics layer.

-   Each device has a single GUI canvas buffer; only the changed portions are refreshed when the GUI updates.

    Each device uses a separate buffer for rendering the GUI (referred to as the GUI canvas). Only the modified area needs to be redrawn when the GUI changes.

-   The entire GUI canvas is copied to the FB framebuffer of the corresponding graphics layer.

    The rendered canvas is transferred to the appropriate FB buffer. During this process, TDE can be used to blend the GUI and OSD with alpha transparency. Since the entire canvas and OSD are composited together each time, there is no need to compute the overlapping regions between GUI and OSD updates individually.

-   FB double buffering

    To prevent visible tearing while a buffer is being drawn and displayed simultaneously, it is recommended to use the FB double-buffering mechanism or the GFBG\_LAYER\_BUF\_DOUBLE / GFBG\_LAYER\_BUF\_DOUBLE\_IMMEDIATE mode in GFBG extended mode. Both approaches allocate two equal-sized buffers as framebuffer memory, alternating between drawing and display. For example, if VO is currently displaying buffer 2, the current draw target is buffer 1. In FB standard mode, PAN\_DISPLAY or FBIOFLIP\_SURFACE can be called to notify VO to display buffer 1; in FB extended mode, FBIO\_REFRESH can be used for the same purpose.

The structure of this solution is shown in [Figure 1](#fig116691737132).

**Figure 1** Structure diagram of the single-layer solution<a name="fig116691737132"></a>  
![](../../../multimedia/graphics/dev/figures/单图层方案的结构示意图.png "单图层方案的结构示意图")

When either the back-end OSD or the GUI changes, the FB buffer must be redrawn:

-   When the back-end OSD changes (e.g., switching from a 16-channel split layout to a 9-channel split layout): clear the FB buffer, draw the new OSD, then copy the entire GUI canvas into the FB buffer.
-   Every time the GUI changes: clear the FB buffer, draw the OSD, then copy the new GUI canvas into the FB buffer.

### Derived Variant<a name="ZH-CN_TOPIC_0000002441714661"></a>

When the same GUI content needs to be displayed simultaneously on both SD0 and HD0 devices, this solution can be simplified to use a single GUI canvas buffer:

-   The canvas is sized to match the HD0 GUI layer (e.g., 800x600). The user prepares one set of images at HD0 resolution (e.g., 800x600). Only the changed portion of the canvas is redrawn on each GUI update. The GUI on SD0 is derived by scaling the entire canvas, with anti-flicker applied, resulting in slightly lower quality compared to the HD version.
-   After each canvas update, for the HD device, since the canvas and GUI layer are the same size, TDE performs a direct copy; for SD0, TDE scales the entire canvas into the FB buffer bound to the SD0 graphics layer, applying anti-flicker processing (required because SD0 is an interlaced device).

The structure of this derived variant is shown in [Figure 1](#fig16738132531813).

**Figure 1** Structure diagram of the derived variant<a name="fig16738132531813"></a>  
![](../../../multimedia/graphics/dev/figures/衍生方案的结构图.png "衍生方案的结构图")
### Development Workflow<a name="ZH-CN_TOPIC_0000002441674801"></a>

#### Development Workflow for Solution 1<a name="ZH-CN_TOPIC_0000002441674817"></a>

Using HD0 and SD0 as an example: HD0 displays a 16-channel equal split layout, SD0 displays a 4-channel equal split layout, and both HD0 and SD0 show the same GUI simultaneously.

When the GUI changes, the implementation proceeds as follows:

1.  Clear the idle FB buffer (assumed to be buffer 1; buffer 2 is currently being displayed by VO) for the graphics layers corresponding to HD0 and SD0.
2.  Draw the 16-channel split lines into buffer 1 of the HD0 graphics layer FB.
3.  Draw the 4-channel split lines into buffer 1 of the SD0 graphics layer FB.
4.  Partially update the GUI canvas.
5.  Use TDE to copy the entire canvas into the appropriate position in buffer 1 of the HD0 graphics layer FB, optionally applying alpha blending for a semi-transparent GUI effect.
6.  Use TDE to scale the entire canvas into the appropriate position in buffer 1 of the SD0 graphics layer FB, applying anti-flicker and optional alpha blending (for a semi-transparent GUI effect).
7.  Call PAN\_DISPLAY via the FB interface to notify HD0 to display buffer 1 of the graphics layer bound to that device.
8.  Call PAN\_DISPLAY via the FB interface to notify SD0 to display buffer 1 of the graphics layer bound to that device.

### Applicable Scenarios<a name="ZH-CN_TOPIC_0000002441714669"></a>

This solution applies to the following scenarios:

-   Each device has its own back-end OSD (e.g., HD0 shows a 16-channel split layout, HD1 shows an 8-channel split layout, SD0 shows a 4-channel split layout).
-   Two or more output devices display a GUI simultaneously (same or different GUIs).

### Advantages and Limitations<a name="ZH-CN_TOPIC_0000002408115502"></a>

This solution offers the following advantages:

-   GUI can be displayed on multiple devices simultaneously.
-   The GUI canvas supports partial refresh, reducing bus bandwidth usage and TDE processing load.
-   Supports alpha-blended compositing of the GUI and OSD with a simple control flow. Since the entire canvas and OSD are composited together on each update, there is no need to compute overlapping regions for partial updates.
-   For the derived variant, only one set of GUI images is needed to accommodate devices with different resolutions, saving flash storage.

This solution has the following limitation:

For the derived variant: the GUI displayed on the SD device is obtained by scaling the canvas, so its visual quality is slightly lower than that on the HD device.
