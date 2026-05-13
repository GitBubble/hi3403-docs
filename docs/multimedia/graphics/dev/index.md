---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/图形开发用户指南/图形开发用户指南.md
--- # 前言
**概述<a name="section143mcpsimp"></a>** 本文为图形开发推荐了1个方案，分别从方案介绍、衍生方案、开发流程、应用场景及优点和限制介绍，为用户在进行图形开发时提供参考。 >![](public_sys-resources/icon-note.gif) **说明：** >- 未有特殊说明，与Hi3403V100，与内容完全一致。 **产品版本<a name="section147mcpsimp"></a>** 与本文档相对应的产品版本如下。 <a name="table150mcpsimp"></a>
<table><thead align="left"><tr id="row155mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p159mcpsimp"><a name="p159mcpsimp"></a><a name="p159mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row161mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p165mcpsimp"><a name="p165mcpsimp"></a><a name="p165mcpsimp"></a>V100</p>
</td>
</tr>
</tbody>
</table> **读者对象<a name="section171mcpsimp"></a>** 本文档（本指南）主要适用于以下工程师： - 技术支持工程师
- 软件开发工程师 **符号约定<a name="section177mcpsimp"></a>** 在本文中可能出现下列标志，它们所代表的含义如下。 <a name="table180mcpsimp"></a>
<table><thead align="left"><tr id="row185mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p189mcpsimp"><a name="p189mcpsimp"></a><a name="p189mcpsimp"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row191mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="figures/zh-cn_image_0000002441674969.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p195mcpsimp"><a name="p195mcpsimp"></a><a name="p195mcpsimp"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
</tbody>
</table> **修订记录<a name="section218mcpsimp"></a>** 修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。 <a name="table126443203200"></a>
<table><thead align="left"><tr id="row264516207203"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p146456203200"><a name="p146456203200"></a><a name="p146456203200"></a><strong id="b8645172022010"><a name="b8645172022010"></a><a name="b8645172022010"></a>文档版本</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p364512062019"><a name="p364512062019"></a><a name="p364512062019"></a><strong id="b1464512200200"><a name="b1464512200200"></a><a name="b1464512200200"></a>发布日期</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p664522018206"><a name="p664522018206"></a><a name="p664522018206"></a><strong id="b156451420152010"><a name="b156451420152010"></a><a name="b156451420152010"></a>修改说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row56451520182017"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p1564572014209"><a name="p1564572014209"></a><a name="p1564572014209"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p126451920132014"><a name="p126451920132014"></a><a name="p126451920132014"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1664582017209"><a name="p1664582017209"></a><a name="p1664582017209"></a>第1次临时版本发布。</p>
</td>
</tr>
</tbody>
</table> # 图形层介绍
## 概述<a name="ZH-CN_TOPIC_0000002408275422"></a> 数字媒体处理平台提供一整套机制支持图形界面的开发，主要包括： - 图形二维加速引擎（Two Dimensional Engine，简称TDE），它利用硬件加速对图形图像进行处理。
- Graphic Framebuffer Group（以下简称GFBG）用于管理叠加图形层，它不仅提供Linux Framebuffer的基本功能，还在Linux Framebuffer的基础上增加层间colorkey、层间Alpha等扩展功能。 >![](public_sys-resources/icon-note.gif) **说明：** >- TDE相关使用方法请参见《TDE API参考》
>- GFBG相关使用方法请参见《GFBG 开发指南》和《GFBG API参考》 ## 图形层体系结构<a name="ZH-CN_TOPIC_0000002441674809"></a> - Hi3403V100支持2路高清HD0和HD1显示设备，1路标清SD0显示设备，同时支持3个图形层G0、G1、G3。 >![](public_sys-resources/icon-note.gif) **说明：** >每个输出设备支持的接口类型和时序请参见对应芯片手册的VDP章节。 各个图形层与各设备有一定的约束关系，如[表1](#_Ref391716435)\~[表4](#_Ref57990861)所示。 **表 1** FB设备文件、图形层以及输出设备的对应关系 \(\) <a name="_Ref391716435"></a>
<table><thead align="left"><tr id="row254mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p256mcpsimp"><a name="p256mcpsimp"></a><a name="p256mcpsimp"></a>FB设备文件</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p258mcpsimp"><a name="p258mcpsimp"></a><a name="p258mcpsimp"></a>图形层</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p260mcpsimp"><a name="p260mcpsimp"></a><a name="p260mcpsimp"></a>对应显示设备</p>
</th>
</tr>
</thead>
<tbody><tr id="row262mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p264mcpsimp"><a name="p264mcpsimp"></a><a name="p264mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p266mcpsimp"><a name="p266mcpsimp"></a><a name="p266mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p268mcpsimp"><a name="p268mcpsimp"></a><a name="p268mcpsimp"></a>G0在HD0设备上显示。</p>
</td>
</tr>
<tr id="row269mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p271mcpsimp"><a name="p271mcpsimp"></a><a name="p271mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p273mcpsimp"><a name="p273mcpsimp"></a><a name="p273mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p275mcpsimp"><a name="p275mcpsimp"></a><a name="p275mcpsimp"></a>G1在HD1设备上显示。</p>
</td>
</tr>
<tr id="row276mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p278mcpsimp"><a name="p278mcpsimp"></a><a name="p278mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>G2在HD0、HD1、SD0设备上显示。</p>
</td>
</tr>
<tr id="row283mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p285mcpsimp"><a name="p285mcpsimp"></a><a name="p285mcpsimp"></a>/dev/fb3</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p287mcpsimp"><a name="p287mcpsimp"></a><a name="p287mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p289mcpsimp"><a name="p289mcpsimp"></a><a name="p289mcpsimp"></a>G3在HD0、HD1、SD0设备上显示。</p>
</td>
</tr>
</tbody>
</table> **表 2** FB设备文件、图形层以及输出设备的对应关系 \(\) <a name="table290mcpsimp"></a>
<table><thead align="left"><tr id="row297mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p299mcpsimp"><a name="p299mcpsimp"></a><a name="p299mcpsimp"></a>FB设备文件</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p301mcpsimp"><a name="p301mcpsimp"></a><a name="p301mcpsimp"></a>图形层</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p303mcpsimp"><a name="p303mcpsimp"></a><a name="p303mcpsimp"></a>对应显示设备</p>
</th>
</tr>
</thead>
<tbody><tr id="row305mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p309mcpsimp"><a name="p309mcpsimp"></a><a name="p309mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p311mcpsimp"><a name="p311mcpsimp"></a><a name="p311mcpsimp"></a>G0在HD0设备上显示。</p>
</td>
</tr>
<tr id="row312mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p314mcpsimp"><a name="p314mcpsimp"></a><a name="p314mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>G2在HD0、HD1、SD0设备上显示。</p>
</td>
</tr>
<tr id="row319mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p321mcpsimp"><a name="p321mcpsimp"></a><a name="p321mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p323mcpsimp"><a name="p323mcpsimp"></a><a name="p323mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p325mcpsimp"><a name="p325mcpsimp"></a><a name="p325mcpsimp"></a>G3在HD0、HD1、SD0设备上显示。</p>
</td>
</tr>
</tbody>
</table> **表 3** FB设备文件、图形层以及输出设备的对应关系 \(Hi3403V100\) <a name="table326mcpsimp"></a>
<table><thead align="left"><tr id="row333mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p335mcpsimp"><a name="p335mcpsimp"></a><a name="p335mcpsimp"></a>FB设备文件</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p337mcpsimp"><a name="p337mcpsimp"></a><a name="p337mcpsimp"></a>图形层</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p339mcpsimp"><a name="p339mcpsimp"></a><a name="p339mcpsimp"></a>对应显示设备</p>
</th>
</tr>
</thead>
<tbody><tr id="row341mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p343mcpsimp"><a name="p343mcpsimp"></a><a name="p343mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p345mcpsimp"><a name="p345mcpsimp"></a><a name="p345mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p347mcpsimp"><a name="p347mcpsimp"></a><a name="p347mcpsimp"></a>G0在HD0设备上显示。</p>
</td>
</tr>
<tr id="row348mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p350mcpsimp"><a name="p350mcpsimp"></a><a name="p350mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p352mcpsimp"><a name="p352mcpsimp"></a><a name="p352mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p354mcpsimp"><a name="p354mcpsimp"></a><a name="p354mcpsimp"></a>G1在HD1设备上显示。</p>
</td>
</tr>
<tr id="row355mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p357mcpsimp"><a name="p357mcpsimp"></a><a name="p357mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p361mcpsimp"><a name="p361mcpsimp"></a><a name="p361mcpsimp"></a>G3在HD0、HD1、SD0设备上显示。</p>
</td>
</tr>
</tbody>
</table> **表 4** FB设备文件、图形层以及输出设备的对应关系 \(\) <a name="_Ref57990861"></a>
<table><thead align="left"><tr id="row368mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p370mcpsimp"><a name="p370mcpsimp"></a><a name="p370mcpsimp"></a>FB设备文件</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>图形层</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p374mcpsimp"><a name="p374mcpsimp"></a><a name="p374mcpsimp"></a>对应显示设备</p>
</th>
</tr>
</thead>
<tbody><tr id="row376mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p378mcpsimp"><a name="p378mcpsimp"></a><a name="p378mcpsimp"></a>/dev/fb0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p380mcpsimp"><a name="p380mcpsimp"></a><a name="p380mcpsimp"></a>G0</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>G0在HD0设备上显示。</p>
</td>
</tr>
<tr id="row383mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p385mcpsimp"><a name="p385mcpsimp"></a><a name="p385mcpsimp"></a>/dev/fb1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>G1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>G1在HD1设备上显示。</p>
</td>
</tr>
<tr id="row390mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p392mcpsimp"><a name="p392mcpsimp"></a><a name="p392mcpsimp"></a>/dev/fb2</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p394mcpsimp"><a name="p394mcpsimp"></a><a name="p394mcpsimp"></a>G2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p396mcpsimp"><a name="p396mcpsimp"></a><a name="p396mcpsimp"></a>G2在HD0、HD1、SD0设备上显示。</p>
</td>
</tr>
<tr id="row397mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>/dev/fb3</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>G3</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>G3在HD0、HD1设备上显示。</p>
</td>
</tr>
<tr id="row404mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p406mcpsimp"><a name="p406mcpsimp"></a><a name="p406mcpsimp"></a>/dev/fb4</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>G4</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>G4在HD1、SD0设备上显示。</p>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **说明：** >为了显示图形层，使用芯片的用户必须先配置并启动输出设备，最后通过GFBG模块接口操作图像层使之显示。 # 图形开发推荐方案
## 概述<a name="ZH-CN_TOPIC_0000002408275414"></a> 在视频采集领域中，一般输出设备的图形用户界面内容包括： - 后端OSD：显示画面分割线、通道号、时间等信息，用以界定多画面显示布局。
- GUI界面：包括各种菜单、进度条等元素，用户通过操作GUI界面进行设备配置。
- 鼠标：提供更方便易用的界面菜单操作方式。 以上3类图形内容可以通过1个图形层实现，也可以通过多个图形层实现。对于提供多个图形层的芯片，指导用户正确、合理、有效地利用这些图形层，以满足不同的输出界面应用场景。下面推荐几种方案供参考。 ## 单图层实现用户界面方案<a name="ZH-CN_TOPIC_0000002441714645"></a> ### 方案介绍<a name="ZH-CN_TOPIC_0000002408275406"></a> 该方案总体思路是：每个设备都只使用1层图形层来完成本设备的后端OSD、GUI和鼠标的显示，鼠标也可以使用独立的鼠标层实现。 可具体描述为：每个输出设备使用一个图形层来完成本设备的后端OSD、GUI；GUI画在独立的缓存上，后端OSD直接画在FB显存中，再通过TDE进行alpha混合；鼠标可以使用单独的鼠标图形层，也可以跟OSD、GUI共用一个图层，共用图层的时候，可以画在GUI缓存上。 该方案使用了以下机制： - 每个设备的后端OSD直接绘制在各自的FB显存中。 例如在每个图形层对应的FB显存中绘制分割布局、通道号或者时间。 - 每个设备一块GUI画布，GUI变更时局部刷新。 每个设备使用一块独立的缓存绘制GUI（称该块缓存为GUI画布），当GUI变更时仅需要进行局部刷新。 - GUI画布整体搬移至相应图层的FB显存中 将绘制好的画布整体搬移到相应的FB缓冲中，在此过程中可利用TDE实现GUI和OSD的叠加透明效果。每次GUI或OSD有变动时，由于是对画布和OSD整体做叠加，故不需要针对局部信息计算GUI和OSD的叠加区域。 - FB双缓冲 为防止一块FB缓冲被边绘制边显示而导致绘制过程可见，推荐使用FB双缓冲机制或是GFBG实现的扩展模式中的GFBG\_LAYER\_BUF\_DOUBLE / GFBG\_LAYER\_BUF\_DOUBLE\_IMMEDIATE机制。它们的原理都是为FB分配2块大小相同的缓冲作为显存交替绘制和显示。如VO正在显示缓冲2，则本次绘制的对象为缓冲1，然后对于FB标准模式可通过FB的PAN\_DISPLAY或FBIOFLIP\_SURFACE调用通知VO显示缓冲1，而对于FB扩展模式可通过FB的FBIO\_REFRESH调用通知VO显示缓冲1。 方案的结构如[图1](#fig116691737132)所示。 **图 1** 单图层方案的结构示意图<a name="fig116691737132"></a> ![](figures/单图层方案的结构示意图.png "单图层方案的结构示意图") 该方案在后端OSD或者GUI界面变动时，都需要重新绘制FB缓存： - 本设备的后端OSD改变时，如16通道分割线切换到9通道分割线：先清空FB缓存，再绘制新的OSD，再将GUI界面整体搬移到FB缓存中。
- GUI界面每次变动时，都需要先清空FB缓存，再绘制OSD，然后将新的GUI界面整体搬移到FB缓存中。 ### 衍生方案<a name="ZH-CN_TOPIC_0000002441714661"></a> 当SD0和HD0设备上想同时显示同样的GUI界面时，该方案可简化仅有一块GUI画布缓存： - 画布大小与HD0的GUI层大小相同（800x600），用户可按照HD0的GUI规格（如800x600）准备一套图片，每次GUI变更时仅局部绘制画布，而SD0的GUI则是将画布整体经过缩放、抗闪得到，其效果略差于HD上的GUI。
- 每次更新画布后，对于HD设备，由于画布大小与GUI界面大小相同，故利用TDE做整体搬移操作即可；对于SD0设备，需要利用TDE对画布整体进行缩放至和SD0绑定的图形层对应的FB显存中，同时进行抗闪烁处理（因SD0是隔行设备）。 该衍生方案的结构如[图1](#fig16738132531813)所示。 **图 1** 衍生方案的结构图<a name="fig16738132531813"></a> ![](figures/衍生方案的结构图.png "衍生方案的结构图")
### 开发流程<a name="ZH-CN_TOPIC_0000002441674801"></a> #### 方案1的开发流程<a name="ZH-CN_TOPIC_0000002441674817"></a> 以HD0和SD0设备上的GUI和OSD为例：HD0设备上16画面等分分割线，SD0设备上4画面等分分割线，且HD0和SD0同时显示同样的GUI。 若此时GUI界面有变化，则该方案的实现过程为： 1. 清空HD0和SD0对应图形层的FB的空闲缓冲（假设为缓冲1，缓冲2正在被VO显示）。
2. 在HD0对应图形层的FB缓冲1中绘制16通道分割线。
3. 在SD0对应图形层的FB缓冲1中绘制4通道分割线。
4. 局部更新画布。
5. 用TDE将画布整体搬移到HD0对应图形层的FB缓冲1的合适位置，此过程可以做alpha透明度叠加以实现GUI半透明效果。
6. 用TDE将画布整体缩放到SD0对应图形层的FB缓冲1的合适位置，此过程可以做抗闪、alpha透明度叠加（以实现GUI半透明效果）。
7. 通过FB接口调用PAN\_DISPLAY通知HD0显示和本设备绑定图形层已准备好的FB的缓冲1。
8. 通过FB接口调用PAN\_DISPLAY通知SD0显示本设备绑定图形层已准备好的FB的缓冲1。 ### 应用场景<a name="ZH-CN_TOPIC_0000002441714669"></a> 应用场景如下： - 每个设备上有各自的后端OSD（如HD0为16画面分割布局，HD1为8画面分割布局，SD0为4画面分割布局）。
- 2或多个输出设备上同时有GUI界面（相同或者不同）。 ### 优点和限制<a name="ZH-CN_TOPIC_0000002408115502"></a> 该方案具有以下优点： - 可同时在多个设备上显示GUI界面。
- GUI画布可局部刷新，节省总线带宽和TDE性能。
- 可实现GUI和OSD的叠加透明效果，且用户控制流程简单。每次GUI或OSD有变动时，由于是对画布和OSD整体做叠加，故不需要针对局部信息计算GUI和OSD的叠加区域。
- 对于衍生方案，用户仅需要一套GUI界面的图片，就可适应不同分辨率设备的GUI需求，节省Flash空间。 该方案具有以下约束： 对于衍生方案：标清设备上的GUI是画布缩放得到的，故效果略差于高清设备上的GUI。 