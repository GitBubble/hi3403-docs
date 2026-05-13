---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ISP 颜色调优说明/ISP 颜色调优说明.md
--- # 前言
**概述<a name="section302mcpsimp"></a>** 本文为AWB，CCM，CLUT算法调试、问题定位而写，详细介绍了标定、参数调优等使用说明，目的是为用户在开发过程中遇到的问题提供解决办法和帮助。 >![](public_sys-resources/icon-note.gif) **说明：** >本文以Hi3403V100描述为例，未有特殊说明，与Hi3403V100内容一致。 **产品版本<a name="section306mcpsimp"></a>** 与本文档相对应的产品版本如下。 <a name="table309mcpsimp"></a>
<table><thead align="left"><tr id="row314mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row320mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p322mcpsimp"><a name="p322mcpsimp"></a><a name="p322mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p324mcpsimp"><a name="p324mcpsimp"></a><a name="p324mcpsimp"></a>V100</p>
</td>
</tr>
</tbody>
</table> **读者对象<a name="section325mcpsimp"></a>** 本文档（本指南）主要适用于以下工程师： - 技术支持工程师
- 软件开发工程师 **符号约定<a name="section331mcpsimp"></a>** 在本文中可能出现下列标志，它们所代表的含义如下。 <a name="table334mcpsimp"></a>
<table><thead align="left"><tr id="row339mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p341mcpsimp"><a name="p341mcpsimp"></a><a name="p341mcpsimp"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p343mcpsimp"><a name="p343mcpsimp"></a><a name="p343mcpsimp"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row345mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p347mcpsimp"><a name="p347mcpsimp"></a><a name="p347mcpsimp"></a><a name="image138"></a><a name="image138"></a><span><img id="image138" src="figures/zh-cn_image_0000002424362258.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p349mcpsimp"><a name="p349mcpsimp"></a><a name="p349mcpsimp"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
</tbody>
</table> **修订记录<a name="section372mcpsimp"></a>** 修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。 <a name="table126443203200"></a>
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
</table> # 原理简介
## 色彩调试综述<a name="ZH-CN_TOPIC_0000002457840885"></a> ISP系统支持两种层次的调色方案。 第一种是基础调色方案。系统的颜色主要由AWB+CCM+GAMMA控制，颜色风格为整个色域内一致的风格，指的是由CCM的3x3矩阵将sensor的native色彩空间（设备相关的色彩）转换到sRGB标准定义的色彩空间（设备无关的色彩）。特点是Sensor的响应被线性扩展到目标空间，即各种颜色获得同样的线性扩展。颜色的呈现随着sensor的光谱响应特性的不同而变化。 **图 1** 基础调色流程图<a name="fig135251247917"></a> ![](figures/基础调色流程图.png "基础调色流程图") 所有颜色的饱和度会随着CCM变大和变小，不同的色调之间可能发生一些冲突，即优先调节某些色调会导致相邻的色调无法调整到位。由于3x3矩阵的原因，暗处，中间亮度，高亮区域的颜色的调节是一致的，如果需要对三个亮度区域做不同的颜色调整，那么就不能满足需求。 第二种是高级调色方案。系统的颜色主要由AWB+CCM+CLUT+GAMMA+CA控制，颜色风格可以按需调节。 **图 2** 高级调色流程图<a name="fig11753153218217"></a> ![](figures/高级调色流程图.png "高级调色流程图") 使用高级调色方案可以调试出不同的颜色风格，比如对于饱和度高的颜色处理方法的不同可以产生不同的效果。 色域边缘的颜色向色域内映射的风格，指的是在CCM达到的颜色的基础上，将饱和度高的区域的颜色向色域内映射。特点是饱和度高的颜色的饱和度会降低，避免RGB中有值发生小于0或者大于1的现象。能将更多的高饱和颜色的变化保留下来，达到色域扩展的效果。适用于光谱响应比较好的sensor。这种调试目标会让饱和度中低的颜色在CCM的作用下得到很好的表现，优先保留饱和度中低的颜色层次。 **图 3** 色域边缘向内映射<a name="fig390mcpsimp"></a> ![](figures/色域边缘向内映射.png "色域边缘向内映射") 色域边缘的颜色向色域外映射的风格，指的是在CCM达到的颜色的基础上，将饱和度高的区域的颜色向色域外映射。特点是饱和度高的颜色的饱和度会增加，会更容易发生RGB中有值小于0或者大于1的现象。可以让颜色更鲜艳，突出画面中的主体。适用于光谱响应比较差的sensor，饱和度由CLUT补足，可以避免CCM的系数过大。这种调试目标会让饱和度中低的颜色在CCM的作用下不过于鲜艳，优先保留饱和度高的颜色层次。 **图 4** 色域边缘向外映射<a name="fig393mcpsimp"></a> ![](figures/色域边缘向外映射.png "色域边缘向外映射")
## AWB模块工作原理<a name="ZH-CN_TOPIC_0000002424202166"></a> AWB模块由硬件WB信息统计模块及Firmware AWB策略控制算法两部分组成。 WB统计模块计算Raw图像满足灰点条件的像素点的R, G, B三个颜色通道平均值。统计输出整幅图像的RGB均值和整幅图像分成M\*N区块的每个区块的RGB均值。 ![](figures/zh-cn_formulaimage_0000002457881137.png) ![](figures/zh-cn_formulaimage_0000002424202422.png) 其中θ指示当前点是否灰点，其取值为0或1；![](figures/zh-cn_formulaimage_0000002424202338.png)是区块内灰点个数；R是像素的红色通道值，![](figures/zh-cn_formulaimage_0000002424362282.png)是R通道均值。 同理计算绿色、蓝色分量均值。 根据AWB统计模块提供的R、G、B三分量均值，计算G/R、G/B，得到AWB增益系数。FW算法会根据各个分块的统计信息，判断环境色温，计算最佳AWB系数。 **图 1** AWB工作原理图<a name="fig633531718246"></a> ![](figures/AWB工作原理图.png "AWB工作原理图")
## CCM模块工作原理<a name="ZH-CN_TOPIC_0000002424202130"></a> sensor对光谱的响应，在RGB各分量上与人眼对光谱的响应通常是有偏差的，通常通过一个色彩校正矩阵校正光谱响应的交叉效应和响应强度，使前端捕获的图片与人眼视觉在色彩上保持一致。 CCM标定工具支持对24色卡进行3x3 Color Correction Matrix的预校正。支持至少三组，最多七组不同色温的CCM，在ISP运行时，FW根据当前的光照强度即ISO，调整饱和度系数。动态色温校正系数（基于标定的多组CCM插值）与饱和度调整系数一起，实现CCM（Color Correction Matrix）矩阵系数的动态调整。CCM矩阵如[图1](#fig11377163510281)所示。 **图 1** CCM矩阵<a name="fig11377163510281"></a> ![](figures/CCM矩阵.png "CCM矩阵")
# AWB调试
## 统计模块调试<a name="ZH-CN_TOPIC_0000002457880949"></a> WB仅统计灰点的RGB三通道均值，准确地配置灰点条件，可提高FirmWare算法的准确度。 ### 色差限制示意图<a name="ZH-CN_TOPIC_0000002457880897"></a> **图 1** 灰点色差限制图<a name="fig414mcpsimp"></a> ![](figures/灰点色差限制图.png "灰点色差限制图")
### 灰点条件参数说明及差异<a name="ZH-CN_TOPIC_0000002424202114"></a> **表 1** Bayer域WB统计灰点条件参数 <a name="table417mcpsimp"></a>
<table><thead align="left"><tr id="row424mcpsimp"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p426mcpsimp"><a name="p426mcpsimp"></a><a name="p426mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="42.57425742574258%" id="mcps1.2.4.1.2"><p id="p428mcpsimp"><a name="p428mcpsimp"></a><a name="p428mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="36.633663366336634%" id="mcps1.2.4.1.3"><p id="p430mcpsimp"><a name="p430mcpsimp"></a><a name="p430mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row432mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p434mcpsimp"><a name="p434mcpsimp"></a><a name="p434mcpsimp"></a>white_level</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.2 "><p id="p436mcpsimp"><a name="p436mcpsimp"></a><a name="p436mcpsimp"></a>灰点的亮度上限。</p>
<p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>取值范围：[0x0, 0xFFFF]，默认值0xFFFF。存在解决方案差异，见<a href="#_Ref505764692">表2</a>。</p>
</td>
<td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.2.4.1.3 "><p id="p440mcpsimp"><a name="p440mcpsimp"></a><a name="p440mcpsimp"></a>sensor在接近饱和时，灰点的线性比例会被破坏，可适当减小该值。</p>
</td>
</tr>
<tr id="row441mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p443mcpsimp"><a name="p443mcpsimp"></a><a name="p443mcpsimp"></a>black_level</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.2 "><p id="p445mcpsimp"><a name="p445mcpsimp"></a><a name="p445mcpsimp"></a>灰点的亮度下限。</p>
<p id="p446mcpsimp"><a name="p446mcpsimp"></a><a name="p446mcpsimp"></a>取值范围：[0x0, 0xFFFF]，默认值0x0。</p>
<p id="p447mcpsimp"><a name="p447mcpsimp"></a><a name="p447mcpsimp"></a>存在解决方案差异，见<a href="#_Ref505764692">表2</a>。</p>
</td>
<td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.2.4.1.3 "><p id="p450mcpsimp"><a name="p450mcpsimp"></a><a name="p450mcpsimp"></a>WDR模式下该门限应设置为统计模块输入Raw数据的最小值；</p>
<p id="p451mcpsimp"><a name="p451mcpsimp"></a><a name="p451mcpsimp"></a>Linear模式下，可在统计模块输入Raw数据的最小值基础上加一个&lt;=0x10的Offset，保证AWB还原以亮区优先。</p>
</td>
</tr>
<tr id="row452mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p454mcpsimp"><a name="p454mcpsimp"></a><a name="p454mcpsimp"></a>cr_max</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.2 "><p id="p456mcpsimp"><a name="p456mcpsimp"></a><a name="p456mcpsimp"></a>灰点红色色差R/G的最大值，8bit精度，取值范围：[0x0, 0xFFF]，默认值0x200（等价浮点2.0）。</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="36.633663366336634%" headers="mcps1.2.4.1.3 "><p id="p458mcpsimp"><a name="p458mcpsimp"></a><a name="p458mcpsimp"></a>色差参数和sensor、光学器件强相关，建议用户对参数进行精调。</p>
<p id="p459mcpsimp"><a name="p459mcpsimp"></a><a name="p459mcpsimp"></a>AWB Firmware将cr_max、cr_min、cb_max、cb_min四个参数和色温、ISO建立了联动，每个参数用户需要配置长度为16的数组。在标定部分说明怎样检查灰点条件配置是否合理。</p>
</td>
</tr>
<tr id="row460mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p462mcpsimp"><a name="p462mcpsimp"></a><a name="p462mcpsimp"></a>cr_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a>灰点红色色差R/G的最小值，8bit精度，取值范围：[0x0, 0xFFF]，默认值0x80（等价浮点0.5）。</p>
</td>
</tr>
<tr id="row465mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>cb_max</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>灰点蓝色色差B/G的最大值，8bit精度，取值范围：[0x0, 0xFFF]，默认值0x200（等价浮点2.0）。</p>
</td>
</tr>
<tr id="row470mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p472mcpsimp"><a name="p472mcpsimp"></a><a name="p472mcpsimp"></a>cb_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p474mcpsimp"><a name="p474mcpsimp"></a><a name="p474mcpsimp"></a>灰点蓝色色差B/G的最小值，8bit精度，取值范围：[0x0, 0xFFF]，默认值0x80（等价浮点0.5）。</p>
</td>
</tr>
</tbody>
</table> **表 2** Bayer域统计控制参数差异说明 <a name="_Ref505764692"></a>
<table><thead align="left"><tr id="row482mcpsimp"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.1"><p id="p484mcpsimp"><a name="p484mcpsimp"></a><a name="p484mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="23.762376237623766%" id="mcps1.2.5.1.2"><p id="p486mcpsimp"><a name="p486mcpsimp"></a><a name="p486mcpsimp"></a>统计输入格式</p>
</th>
<th class="cellrowborder" valign="top" width="40.5940594059406%" id="mcps1.2.5.1.3"><p id="p488mcpsimp"><a name="p488mcpsimp"></a><a name="p488mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="14.851485148514854%" id="mcps1.2.5.1.4"><p id="p490mcpsimp"><a name="p490mcpsimp"></a><a name="p490mcpsimp"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row492mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p494mcpsimp"><a name="p494mcpsimp"></a><a name="p494mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="23.762376237623766%" headers="mcps1.2.5.1.2 "><p id="p496mcpsimp"><a name="p496mcpsimp"></a><a name="p496mcpsimp"></a>16bit，不带黑电平；WDR模式和Linear模式一致</p>
</td>
<td class="cellrowborder" valign="top" width="40.5940594059406%" headers="mcps1.2.5.1.3 "><p id="p498mcpsimp"><a name="p498mcpsimp"></a><a name="p498mcpsimp"></a>不区分Linear模式和WDR模式：</p>
<a name="ul499mcpsimp"></a><a name="ul499mcpsimp"></a><ul id="ul499mcpsimp"><li>black_level取值范围：[0x0, 0xFFFF]</li><li>white_level取值范围：[0x0, 0xFFFF]</li></ul>
</td>
<td class="cellrowborder" valign="top" width="14.851485148514854%" headers="mcps1.2.5.1.4 "><p id="p503mcpsimp"><a name="p503mcpsimp"></a><a name="p503mcpsimp"></a>-</p>
</td>
</tr>
</tbody>
</table> ### 统计输出说明及差异<a name="ZH-CN_TOPIC_0000002457840793"></a> **表 1** Bayer域统计结果说明 <a name="table505mcpsimp"></a>
<table><thead align="left"><tr id="row512mcpsimp"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p514mcpsimp"><a name="p514mcpsimp"></a><a name="p514mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.4.1.2"><p id="p516mcpsimp"><a name="p516mcpsimp"></a><a name="p516mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.3"><p id="p518mcpsimp"><a name="p518mcpsimp"></a><a name="p518mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row520mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p522mcpsimp"><a name="p522mcpsimp"></a><a name="p522mcpsimp"></a>global_r</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p524mcpsimp"><a name="p524mcpsimp"></a><a name="p524mcpsimp"></a>全局统计信息中灰点的R分量平均值。</p>
<p id="p525mcpsimp"><a name="p525mcpsimp"></a><a name="p525mcpsimp"></a>取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p527mcpsimp"><a name="p527mcpsimp"></a><a name="p527mcpsimp"></a>RGB三分量均值的数据位宽存在解决方案差异，见<a href="#_Ref505764721">表2</a>。</p>
</td>
</tr>
<tr id="row529mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p531mcpsimp"><a name="p531mcpsimp"></a><a name="p531mcpsimp"></a>global_g</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p533mcpsimp"><a name="p533mcpsimp"></a><a name="p533mcpsimp"></a>全局统计信息中灰点的G分量平均值。</p>
<p id="p534mcpsimp"><a name="p534mcpsimp"></a><a name="p534mcpsimp"></a>取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p536mcpsimp"><a name="p536mcpsimp"></a><a name="p536mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row537mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p539mcpsimp"><a name="p539mcpsimp"></a><a name="p539mcpsimp"></a>global_b</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p541mcpsimp"><a name="p541mcpsimp"></a><a name="p541mcpsimp"></a>全局统计信息中灰点的B分量平均值。</p>
<p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row545mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p547mcpsimp"><a name="p547mcpsimp"></a><a name="p547mcpsimp"></a>count_all</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p549mcpsimp"><a name="p549mcpsimp"></a><a name="p549mcpsimp"></a>全局统计信息中灰点的个数。</p>
<p id="p550mcpsimp"><a name="p550mcpsimp"></a><a name="p550mcpsimp"></a>已做归一化，取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p552mcpsimp"><a name="p552mcpsimp"></a><a name="p552mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row553mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p555mcpsimp"><a name="p555mcpsimp"></a><a name="p555mcpsimp"></a>zone_avg_r[]</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>分区间统计信息中灰点的R分量平均值。</p>
<p id="p558mcpsimp"><a name="p558mcpsimp"></a><a name="p558mcpsimp"></a>取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p560mcpsimp"><a name="p560mcpsimp"></a><a name="p560mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row561mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p563mcpsimp"><a name="p563mcpsimp"></a><a name="p563mcpsimp"></a>zone_avg_g[]</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p565mcpsimp"><a name="p565mcpsimp"></a><a name="p565mcpsimp"></a>分区间统计信息中灰点的G分量平均值。</p>
<p id="p566mcpsimp"><a name="p566mcpsimp"></a><a name="p566mcpsimp"></a>取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p568mcpsimp"><a name="p568mcpsimp"></a><a name="p568mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row569mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p571mcpsimp"><a name="p571mcpsimp"></a><a name="p571mcpsimp"></a>zone_avg_b[]</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p573mcpsimp"><a name="p573mcpsimp"></a><a name="p573mcpsimp"></a>分区间统计信息中灰点的B分量平均值。</p>
<p id="p574mcpsimp"><a name="p574mcpsimp"></a><a name="p574mcpsimp"></a>取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p576mcpsimp"><a name="p576mcpsimp"></a><a name="p576mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row577mcpsimp"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p579mcpsimp"><a name="p579mcpsimp"></a><a name="p579mcpsimp"></a>zone_count_all[]</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.2 "><p id="p581mcpsimp"><a name="p581mcpsimp"></a><a name="p581mcpsimp"></a>分区间统计信息中灰点的个数。</p>
<p id="p582mcpsimp"><a name="p582mcpsimp"></a><a name="p582mcpsimp"></a>已做归一化，取值范围：[0, 0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.3 "><p id="p584mcpsimp"><a name="p584mcpsimp"></a><a name="p584mcpsimp"></a>-</p>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-notice.gif) **须知：** >像素个数做归一化是为了消除分辨率差异对灰点个数的影响。
>归一化公式：CountAll = \(Count of Gray Pixels << 16\) / \(Count of All Pixels\). **表 2** Bayer域统计结果差异说明 <a name="_Ref505764721"></a>
<table><thead align="left"><tr id="row593mcpsimp"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p595mcpsimp"><a name="p595mcpsimp"></a><a name="p595mcpsimp"></a>解决方案</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.2"><p id="p597mcpsimp"><a name="p597mcpsimp"></a><a name="p597mcpsimp"></a>统计输出格式描述</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.3"><p id="p599mcpsimp"><a name="p599mcpsimp"></a><a name="p599mcpsimp"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row601mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p603mcpsimp"><a name="p603mcpsimp"></a><a name="p603mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p605mcpsimp"><a name="p605mcpsimp"></a><a name="p605mcpsimp"></a>统计输出RGB均值数据位宽是16bit，取值范围：[0, 0xFFFF]</p>
<p id="p606mcpsimp"><a name="p606mcpsimp"></a><a name="p606mcpsimp"></a>其中16bit整数位，无小数位。</p>
<p id="p607mcpsimp"><a name="p607mcpsimp"></a><a name="p607mcpsimp"></a>Linear模式和WDR模式无差异，RGain=G/R。</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p609mcpsimp"><a name="p609mcpsimp"></a><a name="p609mcpsimp"></a>-</p>
</td>
</tr>
</tbody>
</table> ### 统计自适应<a name="ZH-CN_TOPIC_0000002424202138"></a> #### 统计参数自动调整的原因（AWB）<a name="ZH-CN_TOPIC_0000002457880937"></a> 随着环境照度的降低，sensor和isp的增益增大，sensor输出Raw数据的噪声增大。同一光源，白色块的色差分布变化如[图1](#_Ref505767834)所示。 **图 1** 5000K白色块Cr在不同照度的分布图<a name="_Ref505767834"></a> ![](figures/5000K白色块Cr在不同照度的分布图.png "5000K白色块Cr在不同照度的分布图") 因此需要建立统计参数和ISO的互动，以保证尽量多的灰色点参与统计。 ## AWB标定<a name="ZH-CN_TOPIC_0000002424362006"></a> ### AWB标定参数说明<a name="ZH-CN_TOPIC_0000002457840769"></a> 确定sensor和滤光片后，用户需要先进行AWB标定，以保证AWB算法正常工作。标定原理是：提取sensor在多个标准光源下的灰点特征\(R/G，B/G\)，计算普朗克拟合曲线和色温拟合曲线。 **表 1** AWB标定参数 <a name="table620mcpsimp"></a>
<table><thead align="left"><tr id="row627mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p629mcpsimp"><a name="p629mcpsimp"></a><a name="p629mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.4.1.2"><p id="p631mcpsimp"><a name="p631mcpsimp"></a><a name="p631mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.3"><p id="p633mcpsimp"><a name="p633mcpsimp"></a><a name="p633mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row635mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p637mcpsimp"><a name="p637mcpsimp"></a><a name="p637mcpsimp"></a>ref_color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p639mcpsimp"><a name="p639mcpsimp"></a><a name="p639mcpsimp"></a>静态白平衡系数标定的环境色温，AWB标定3个KI光源的中间光源色温，单位Kelvin。</p>
<p id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>取值范围：[0-0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p642mcpsimp"><a name="p642mcpsimp"></a><a name="p642mcpsimp"></a>推荐在Macbeth D50标准光源环境或室外5000k-5500K光源捕获24色卡Raw数据进行标定。</p>
</td>
</tr>
<tr id="row643mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>static_wb[4]</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>静态白平衡系数，由AWB标定工具给出。</p>
<p id="p648mcpsimp"><a name="p648mcpsimp"></a><a name="p648mcpsimp"></a>取值范围：[0-0xFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p650mcpsimp"><a name="p650mcpsimp"></a><a name="p650mcpsimp"></a>8bit定点数，G通道系数固定为0x100(浮点1.0)。</p>
</td>
</tr>
<tr id="row651mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p653mcpsimp"><a name="p653mcpsimp"></a><a name="p653mcpsimp"></a>curve_para[0-2]</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p655mcpsimp"><a name="p655mcpsimp"></a><a name="p655mcpsimp"></a><span xml:lang="sv-SE" id="ph656mcpsimp"><a name="ph656mcpsimp"></a><a name="ph656mcpsimp"></a>普朗克曲线系数，</span>由AWB标定工具给出。</p>
<p xml:lang="sv-SE" id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>普朗克曲线描绘白色块在不同色温的标准光源下的颜色表现。</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row660mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p662mcpsimp"><a name="p662mcpsimp"></a><a name="p662mcpsimp"></a>curve_para[3-5]</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p664mcpsimp"><a name="p664mcpsimp"></a><a name="p664mcpsimp"></a><span xml:lang="sv-SE" id="ph665mcpsimp"><a name="ph665mcpsimp"></a><a name="ph665mcpsimp"></a>色温曲线系数，</span>由AWB标定工具给出。</p>
<p xml:lang="sv-SE" id="p666mcpsimp"><a name="p666mcpsimp"></a><a name="p666mcpsimp"></a>色温曲线描绘白色块的颜色表现与色温的对应关系。</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>-</p>
</td>
</tr>
</tbody>
</table> ### Raw数据采集<a name="ZH-CN_TOPIC_0000002424362074"></a> #### 标定光源选择<a name="ZH-CN_TOPIC_0000002424362050"></a> - 5000K-5500K之间的自然光源
- D50人工光源
- A光源
- D75人工光源或7000K以上自然光源。 以上四组光源是必须的。补充更多的光源数据，如：CWF、TL84、D65、3500K-6500K自然光源等可提高标定的准确性。 #### 采集步骤<a name="ZH-CN_TOPIC_0000002424362002"></a> 1. 采集设备准备：标准X-Rite 24色卡、照度为600Lux均匀光源（左右两侧双光源，光源与色卡平面的夹角在25°- 45°），录像机、色温计。在室外自然光环境采集5000K附近的24色卡Raw，可提高标定的准确性。
2. 调整AE目标亮度，最亮灰阶\(Block 19\)的G分量亮度在饱和值的0.8倍左右（以12bit RAW数据为例，G分量数值在0xC00-0xD80之间）。
3. 采集中性灰RAW图像，检查录像机的镜头阴影程度。Shading较严重时，需要先标定Shading系数，24色卡图像需要先进行Shading校正后，再进行AWB标定。 ### 标定<a name="ZH-CN_TOPIC_0000002424362026"></a> #### 自动AWB标定步骤（AWB）<a name="ZH-CN_TOPIC_0000002457840801"></a> 1. RAW数据导入部分请参考《图像质量调试工具使用指南》。
2. 确认Raw数据导入配置是否合理。图像亮度合理，色卡颜色正确，说明Raw数据位宽和RGGB顺序是正确的；打开任意一幅图像，选择色卡的灰阶区域，计算R/G, B/G的值，如[图1](#_Ref492399771)红色框所示，如果不同灰阶的R/G, B/G基本一致，说明黑电平配置正确。
3. 准确配置每幅Raw图的色温，计算每幅图灰点的R/G, B/G值。对于24色卡场景，一般选择20-22色块计算R/G, B/G，如果是实际场景，避免选择过曝，过暗的灰色块参与计算。
4. 选择3个RAW为关键光源 \(KI\)，做为标定起始点。推荐选择A、D50、D75三个光源为KI。中间色温的D50光源选择非常关键，推荐用5000K-5500K之间的自然光源替代，可优化室外AWB表现。选择的中间光源色温偏高时，图像偏暖色调，选择的中间光源色温偏低时，图像偏冷色调如图 Auto AWB 标定所示。
5. 标定工具最多支持32组光源参与AWB标定。室外应用产品，建议采集傍晚或清晨的高色温场景加入标定，如图 Auto AWB 标定所示。 **Figure 1** 验验证黑电平配置是否正确<a name="_Ref492399771"></a> ![](figures/验验证黑电平配置是否正确.png "验验证黑电平配置是否正确") KI的中间色温光源分别选择4500K, 5500K, 6500K的效果对比图 ![](figures/2-3A.png) #### 手动调整AWB标定结果<a name="ZH-CN_TOPIC_0000002457880965"></a> AWB标定中间光源KI色温会影响色调。客户在6000K色温采集了室外数据，但希望AWB的中间色温在5200K附近，以达到色调轻微偏冷的效果。可以按照以下步骤手动计算，避免重复的数据采集（如果能够采集到室外多个色温段的数据，标定结果会更可靠）。 1. 利用现有数据进行Auto AWB标定，标定步骤参考 "[自动AWB标定步骤（AWB）](#ZH-CN_TOPIC_0000002457840801)"。因为仅采集到6000K的室外数据，因此，指定A、10K\(也可以是D75\)、6000K室外数据为KI光源进行标定，得到的标定结果如图 Auto AWB 标定所示。
2. 将以上标定结果通过MPI接口或者PQTools配置到ISP。
3. 调用ot\_mpi\_isp\_cal\_gain\_by\_temp\(\)计算5200K光源对应的增益。上图中5200K对应的增益是\[487, 256, 256, 479\]。关闭GainNorm功能以确保G分量的增益是256。
4. 半自动模式，校正得到期望的以5200K为中心的AWB参数。请参考图 Semi-Auto AWB 标定所示。
5. 图 Auto与Semi-Auto AWB 效果验证效果对比验证，左图是6000K效果，右图是5200K效果。 **Figure 1** Auto AWB 标定<a name="_Ref492400038"></a> ![](figures/Auto-AWB-标定.png "Auto-AWB-标定") **Figure 2** Semi-Auto AWB 标定<a name="_Ref492400242"></a> ![](figures/Semi-Auto-AWB-标定.png "Semi-Auto-AWB-标定") **Figure 3** Auto与Semi-Auto AWB 效果验证<a name="_Ref492400244"></a> ![](figures/Auto与Semi-Auto-AWB-效果验证.png "Auto与Semi-Auto-AWB-效果验证")
#### 标定结果的确认\(AWB\)<a name="ZH-CN_TOPIC_0000002424202186"></a> 标定完成，观察Planckian Curve，是否光源分布在曲线两侧，是否有光源点距离普朗克曲线较远，估计的色温是否准确。如果某些光源的误差较大，可调整其权重值，再次进行标定。 也可以用3A分析工具的AWB功能在线验证标定的准确性，多个光源下灰色块都落在Planckian曲线的附近，说明标定是可靠的。 **图 1** AWB标定完成的Planckian Curve<a name="fig705mcpsimp"></a> ![](figures/AWB标定完成的Planckian-Curve.png "AWB标定完成的Planckian-Curve") **图 2** AWB标定结果确认<a name="_Ref492403568"></a> ![](figures/AWB标定结果确认.png "AWB标定结果确认") 如[图2](#_Ref492403568)所示，Shift的绝对值小于32，6500K以下光源估计色温值和测量值误差小于500K，确认标定结果正确。 >![](public_sys-resources/icon-notice.gif) **AVIS:** >[Figure 2](#_Ref492403568)中4768.raw的测量色温是4768K，估计色温是5328K，色温误差值较大。但因为4768.raw的B/G比4508.raw，4871.raw都大，说明光源的蓝色分量较强，因此色温偏高是合理的。 ### 根据标定信息调整统计参数配置<a name="ZH-CN_TOPIC_0000002457840797"></a> #### 借助标定工具，判断灰点色差条件设置是否合理<a name="ZH-CN_TOPIC_0000002424361946"></a> 1. 计算最低色温下灰色块的R/G, B/G。比如图 低色温下灰点的色差信息A光源下R/G=1.66, B/G=0.47，8bit定点化R/G=round\(1.66\*256\)=0x1A9，B/G=round\(0.47\*256\)=0x78。因此，灰点条件cr\_max\>= 0x1A9，cb\_min<=0x78，才能保证该场景下WB统计模块获取到正确的灰点信息。考虑到光源照度的变化带来光谱改变，且低照度下噪声增大，用户应该进一步增大cr\_max取值，缩小cb\_min取值。
2. 计算最高色温下灰色块的R/G, B/G。比如图 高色温下灰点的色差信息室外高色温光源下R/G=0.41, B/G=1.13，8bit定点化R/G=round\(0.41\*256\)=0x69，B/G=round\(1.13\*256\)=0x122。因此，灰点条件cr\_min<= 0x69，cb\_max\>=0x122，才能保证该场景下WB统计模块获取到正确的灰点信息。用户应该进一步增大cb\_max取值，缩小cr\_min取值。
3. 完成了正常照度下cr\_max，cr\_min，cb\_max，cb\_min的调整，可以采集不同ISO下的Raw，计算灰点的色差信息，完成自适应表格的调整。 **Figure 1** 低色温下灰点的色差信息<a name="_Ref492400250"></a> ![](figures/低色温下灰点的色差信息.png "低色温下灰点的色差信息") **Figure 2** 高色温下灰点的色差信息<a name="_Ref492400251"></a> ![](figures/高色温下灰点的色差信息.png "高色温下灰点的色差信息")
## AWB FW<a name="ZH-CN_TOPIC_0000002457840861"></a> ### ot\_isp\_awb\_attr<a name="ZH-CN_TOPIC_0000002457880921"></a> ot\_isp\_awb\_attr结构体定义了AWB FW算法的基本可调节参数，包括色温限制、灰点范围限制条件等。该结构体引用了以下子结构体： - ot\_isp\_awb\_ct\_limit\_attr
- ot\_isp\_awb\_cbcr\_track\_attr
- ot\_isp\_awb\_lum\_histgram\_attr **表 1** ot\_isp\_awb\_attr参数 <a name="table727mcpsimp"></a>
<table><thead align="left"><tr id="row734mcpsimp"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.4.1.1"><p id="p736mcpsimp"><a name="p736mcpsimp"></a><a name="p736mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="35.64356435643564%" id="mcps1.2.4.1.2"><p id="p738mcpsimp"><a name="p738mcpsimp"></a><a name="p738mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="42.57425742574258%" id="mcps1.2.4.1.3"><p id="p740mcpsimp"><a name="p740mcpsimp"></a><a name="p740mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row742mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p744mcpsimp"><a name="p744mcpsimp"></a><a name="p744mcpsimp"></a>alg_type</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p746mcpsimp"><a name="p746mcpsimp"></a><a name="p746mcpsimp"></a>白平衡的算法类型属性，支持</p>
<p id="p747mcpsimp"><a name="p747mcpsimp"></a><a name="p747mcpsimp"></a>OT_ISP_AWB_ALG_LOWCOST和</p>
<p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>OT_ISP_AWB_ALG_ADVANCE、OT_ISP_AWB_ALG_NATURA可选。</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p750mcpsimp"><a name="p750mcpsimp"></a><a name="p750mcpsimp"></a>LOWCOST CPU占用较少，对光源的适应性较好。ADVANCE提升了AWB精度。NATURA适用于无人机、运动DV等室外应用产品。</p>
<p id="p751mcpsimp"><a name="p751mcpsimp"></a><a name="p751mcpsimp"></a>按照标定要求完成标定，推荐采用ADVANCE，简单标定推荐采用LOWCOST。</p>
</td>
</tr>
<tr id="row752mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p754mcpsimp"><a name="p754mcpsimp"></a><a name="p754mcpsimp"></a>zone_sel</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p756mcpsimp"><a name="p756mcpsimp"></a><a name="p756mcpsimp"></a>设置zone_sel=0，AWB采用灰度世界算法。</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p758mcpsimp"><a name="p758mcpsimp"></a><a name="p758mcpsimp"></a>该功能主要用来定位问题，不推荐修改。</p>
<p id="p759mcpsimp"><a name="p759mcpsimp"></a><a name="p759mcpsimp"></a>红外灯应用时需要使能AWB，建议设置zone_sel=0。</p>
</td>
</tr>
<tr id="row760mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p762mcpsimp"><a name="p762mcpsimp"></a><a name="p762mcpsimp"></a>speed</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p764mcpsimp"><a name="p764mcpsimp"></a><a name="p764mcpsimp"></a>AWB收敛速度，值越大，AWB收敛越快。</p>
<p id="p765mcpsimp"><a name="p765mcpsimp"></a><a name="p765mcpsimp"></a>取值范围：[0x0, 0xFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p767mcpsimp"><a name="p767mcpsimp"></a><a name="p767mcpsimp"></a>speed设置为0xFFF时，AWB增益不参考历史信息。speed设置为0时，AWB Freeze。</p>
</td>
</tr>
<tr id="row768mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p770mcpsimp"><a name="p770mcpsimp"></a><a name="p770mcpsimp"></a>high_color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p772mcpsimp"><a name="p772mcpsimp"></a><a name="p772mcpsimp"></a>AWB支持的色温上限，推荐取值：[10000, 15000]</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p774mcpsimp"><a name="p774mcpsimp"></a><a name="p774mcpsimp"></a>高色温下出现偏色时，优先调整色温上限。</p>
</td>
</tr>
<tr id="row775mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p777mcpsimp"><a name="p777mcpsimp"></a><a name="p777mcpsimp"></a>low_color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p779mcpsimp"><a name="p779mcpsimp"></a><a name="p779mcpsimp"></a>AWB支持的色温下限，推荐取值：[1500, 2500]</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p781mcpsimp"><a name="p781mcpsimp"></a><a name="p781mcpsimp"></a>低色温下出现偏色时，优先调整色温下限。色温下限太低时，低色温的机动车道路<em id="i782mcpsimp"><a name="i782mcpsimp"></a><a name="i782mcpsimp"></a>视频采集</em>场景容易出现震荡。</p>
</td>
</tr>
<tr id="row783mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p785mcpsimp"><a name="p785mcpsimp"></a><a name="p785mcpsimp"></a>ct_limit</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p787mcpsimp"><a name="p787mcpsimp"></a><a name="p787mcpsimp"></a>检测色温超出色温范围时，AWB算法的动作。仅在检测色温超出色温范围时生效。</p>
<p id="p788mcpsimp"><a name="p788mcpsimp"></a><a name="p788mcpsimp"></a>推荐采用Auto模式。</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p790mcpsimp"><a name="p790mcpsimp"></a><a name="p790mcpsimp"></a>支持Manual和Auto两种方式。</p>
<a name="ul791mcpsimp"></a><a name="ul791mcpsimp"></a><ul id="ul791mcpsimp"><li>Manual模式下，由用户定义色温超限时AWB的增益；</li><li>Auto模式下，根据AWB标定参数，确定色温超限时AWB的增益。</li></ul>
</td>
</tr>
<tr id="row794mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p796mcpsimp"><a name="p796mcpsimp"></a><a name="p796mcpsimp"></a>shift_limit</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p798mcpsimp"><a name="p798mcpsimp"></a><a name="p798mcpsimp"></a>以普朗克曲线为中心点，shift_limit为半径确定AWB支持的光源范围。</p>
<p id="p799mcpsimp"><a name="p799mcpsimp"></a><a name="p799mcpsimp"></a>推荐取值：[0x30-0x50]</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p801mcpsimp"><a name="p801mcpsimp"></a><a name="p801mcpsimp"></a>取值越大，对光源的支持越广，会降低大面积单色场景AWB精度。</p>
</td>
</tr>
<tr id="row802mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p804mcpsimp"><a name="p804mcpsimp"></a><a name="p804mcpsimp"></a>gain_norm_en</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p806mcpsimp"><a name="p806mcpsimp"></a><a name="p806mcpsimp"></a>AWB最终增益是否做归一化。</p>
<p id="p807mcpsimp"><a name="p807mcpsimp"></a><a name="p807mcpsimp"></a>默认打开</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p809mcpsimp"><a name="p809mcpsimp"></a><a name="p809mcpsimp"></a>使能后，可提高低照、低色温下的信噪比。</p>
</td>
</tr>
<tr id="row810mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p812mcpsimp"><a name="p812mcpsimp"></a><a name="p812mcpsimp"></a>natural_cast_en</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p814mcpsimp"><a name="p814mcpsimp"></a><a name="p814mcpsimp"></a>低色温下AWB风格喜好开关。</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p816mcpsimp"><a name="p816mcpsimp"></a><a name="p816mcpsimp"></a>natural_cast_en使能，低色温下AWB保留光源色，图像颜色更自然。</p>
</td>
</tr>
<tr id="row817mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p819mcpsimp"><a name="p819mcpsimp"></a><a name="p819mcpsimp"></a>rg_strength</p>
<p id="p820mcpsimp"><a name="p820mcpsimp"></a><a name="p820mcpsimp"></a>bg_strength</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p822mcpsimp"><a name="p822mcpsimp"></a><a name="p822mcpsimp"></a>AWB校正强度。</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p824mcpsimp"><a name="p824mcpsimp"></a><a name="p824mcpsimp"></a>AWB校正强度分为以下三种情况。（推荐rg_strength = bg_strength，且&lt;=0x80）</p>
<a name="ul825mcpsimp"></a><a name="ul825mcpsimp"></a><ul id="ul825mcpsimp"><li>rg_strength =0x80时，白色恢复为白色；</li><li>rg_strength &gt;0x80时，白色与光源反向，低色温偏蓝，高色温偏红；</li><li>rg_strength &lt;0x80时，白色与光源同向，低色温偏红，高色温偏蓝。颜色表现更符合人眼感观。</li></ul>
</td>
</tr>
<tr id="row829mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p831mcpsimp"><a name="p831mcpsimp"></a><a name="p831mcpsimp"></a>cb_cr_track</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p833mcpsimp"><a name="p833mcpsimp"></a><a name="p833mcpsimp"></a>不同ISO下灰点条件，cr_max, cr_min, cb_max, cb_min等四组查找表。</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p835mcpsimp"><a name="p835mcpsimp"></a><a name="p835mcpsimp"></a>推荐用户针对sensor调整以上参数，可优化低照度效果。</p>
</td>
</tr>
<tr id="row836mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p id="p838mcpsimp"><a name="p838mcpsimp"></a><a name="p838mcpsimp"></a>luma_hist</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p840mcpsimp"><a name="p840mcpsimp"></a><a name="p840mcpsimp"></a>亮度权重配置相关参数</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p842mcpsimp"><a name="p842mcpsimp"></a><a name="p842mcpsimp"></a>Auto模式下，FW自动计算亮度分组门限，支持用户配置不同亮度灰点的权重。</p>
<p id="p843mcpsimp"><a name="p843mcpsimp"></a><a name="p843mcpsimp"></a>Manual模式下，支持用户配置亮度分组门限和不同亮度灰点的权重。</p>
</td>
</tr>
<tr id="row844mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p846mcpsimp"><a name="p846mcpsimp"></a><a name="p846mcpsimp"></a>awb_zone_wt_en</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p848mcpsimp"><a name="p848mcpsimp"></a><a name="p848mcpsimp"></a>白平衡的分块权重使能开关，<span xml:lang="sv-SE" id="ph849mcpsimp"><a name="ph849mcpsimp"></a><a name="ph849mcpsimp"></a>默认TD_FALSE。</span></p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p id="p851mcpsimp"><a name="p851mcpsimp"></a><a name="p851mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row852mcpsimp"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p854mcpsimp"><a name="p854mcpsimp"></a><a name="p854mcpsimp"></a>zone_wt</p>
</td>
<td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.2.4.1.2 "><p id="p856mcpsimp"><a name="p856mcpsimp"></a><a name="p856mcpsimp"></a>白平衡的1024分块权重表<span xml:lang="sv-SE" id="ph857mcpsimp"><a name="ph857mcpsimp"></a><a name="ph857mcpsimp"></a>，</span>取值范围：[0x0, 0xFF]</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574258%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p859mcpsimp"><a name="p859mcpsimp"></a><a name="p859mcpsimp"></a>特定应用产品，客户使能awb_zone_wt_en后，可通过设置权重表改变每个区域的权重，优化AWB表现。</p>
<p xml:lang="sv-SE" id="p860mcpsimp"><a name="p860mcpsimp"></a><a name="p860mcpsimp"></a>在Shading较严重时，可加大中心区域的权重，保证中间区域AWB准确还原，降低Shading对AWB的影响。</p>
<p xml:lang="sv-SE" id="p861mcpsimp"><a name="p861mcpsimp"></a><a name="p861mcpsimp"></a>在行车记录仪应用，感兴趣区域一般在画面的中心偏下区域，可加大此区域的权重，降低天空、树木等区域对AWB的干扰。</p>
</td>
</tr>
</tbody>
</table> #### ot\_isp\_awb\_ct\_limit\_attr<a name="ZH-CN_TOPIC_0000002457880869"></a> **表 1** ot\_isp\_awb\_ct\_limit\_attr参数说明 <a name="table123911857881"></a>
<table><thead align="left"><tr id="row12391165719818"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p1139135711812"><a name="p1139135711812"></a><a name="p1139135711812"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.2"><p id="p19392115718817"><a name="p19392115718817"></a><a name="p19392115718817"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.4.1.3"><p id="p1339225718816"><a name="p1339225718816"></a><a name="p1339225718816"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row03923571181"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p16392857688"><a name="p16392857688"></a><a name="p16392857688"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><p id="p1139295710817"><a name="p1139295710817"></a><a name="p1139295710817"></a>环境色温超出色温上下限范围时，最终生效的AWB增益是否做Clip处理。</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.3 "><p id="p1439275710820"><a name="p1439275710820"></a><a name="p1439275710820"></a>夜晚，室外道路<em id="i339219571812"><a name="i339219571812"></a><a name="i339219571812"></a>视频采集</em>场景的光源在车灯、路灯间切换，打开该功能保证颜色的一致性。</p>
</td>
</tr>
<tr id="row239211573820"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p19393175715819"><a name="p19393175715819"></a><a name="p19393175715819"></a>op_type</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><p id="p1839325719811"><a name="p1839325719811"></a><a name="p1839325719811"></a>环境色温超出色温上下限范围时<span xml:lang="sv-SE" id="ph1939316571812"><a name="ph1939316571812"></a><a name="ph1939316571812"></a>：</span></p>
<a name="ul153934578818"></a><a name="ul153934578818"></a><ul id="ul153934578818"><li xml:lang="sv-SE">Auto模式下，AWB增益由色温曲线计算；</li><li xml:lang="sv-SE">Manual模式下，AWB增益由用户配置。</li></ul>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p2039318577814"><a name="p2039318577814"></a><a name="p2039318577814"></a>推荐Auto模式。</p>
</td>
</tr>
<tr id="row153931457083"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p73930576815"><a name="p73930576815"></a><a name="p73930576815"></a>high_rg_limit</p>
<p id="p14393157981"><a name="p14393157981"></a><a name="p14393157981"></a>high_bg_limit</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><p id="p8393115717813"><a name="p8393115717813"></a><a name="p8393115717813"></a>Manual模式下有效。环境色温超出色温上限范围时，用户配置高色温的R, B增益。</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.3 "><p id="p1639315720817"><a name="p1639315720817"></a><a name="p1639315720817"></a>-</p>
</td>
</tr>
<tr id="row639317571786"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p15393157289"><a name="p15393157289"></a><a name="p15393157289"></a>low_rg_limit</p>
<p id="p10393457881"><a name="p10393457881"></a><a name="p10393457881"></a>low_bg_limit</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><p id="p839316577817"><a name="p839316577817"></a><a name="p839316577817"></a>Manual模式下有效。环境色温超出色温下限范围时，用户配置低色温的R, B增益。</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p739316571386"><a name="p739316571386"></a><a name="p739316571386"></a>-</p>
</td>
</tr>
</tbody>
</table> #### ot\_isp\_awb\_cbcr\_track\_attr<a name="ZH-CN_TOPIC_0000002424202162"></a> **表 1** ot\_isp\_awb\_cbcr\_track\_attr参数说明 <a name="table75153411891"></a>
<table><thead align="left"><tr id="row185151841895"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p1051594112919"><a name="p1051594112919"></a><a name="p1051594112919"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.2.4.1.2"><p id="p95156413915"><a name="p95156413915"></a><a name="p95156413915"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p13515204111919"><a name="p13515204111919"></a><a name="p13515204111919"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row35161411691"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1516134116918"><a name="p1516134116918"></a><a name="p1516134116918"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.2 "><p id="p851616414914"><a name="p851616414914"></a><a name="p851616414914"></a>是否使能灰点条件和ISO联动功能</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p185161241892"><a name="p185161241892"></a><a name="p185161241892"></a>打开该功能，用户可通过cr_max等参数配置，控制低照度下的颜色表现。</p>
</td>
</tr>
<tr id="row1351619418918"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p18516841995"><a name="p18516841995"></a><a name="p18516841995"></a>cr_max[]</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.2 "><p id="p19516184111911"><a name="p19516184111911"></a><a name="p19516184111911"></a>低色温下R/G和ISO的联动数组。</p>
<p id="p13516134114916"><a name="p13516134114916"></a><a name="p13516134114916"></a>要求为单调递增序列。</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p4516134117920"><a name="p4516134117920"></a><a name="p4516134117920"></a>请参考“<a href="#ZH-CN_TOPIC_0000002424361946">借助标定工具，判断灰点色差条件设置是否合理</a>”进行标定。</p>
<p id="p251644117919"><a name="p251644117919"></a><a name="p251644117919"></a>相同ISO下，通常cr_max比cb_max稍大，cr_min和cb_min取值基本相同。</p>
</td>
</tr>
<tr id="row1451614411896"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p151610411697"><a name="p151610411697"></a><a name="p151610411697"></a>cr_min[]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p17516204111916"><a name="p17516204111916"></a><a name="p17516204111916"></a>高色温下R/G<span xml:lang="en-US" id="ph65160411196"><a name="ph65160411196"></a><a name="ph65160411196"></a>和</span>ISO的联动数组。</p>
<p xml:lang="sv-SE" id="p85165411090"><a name="p85165411090"></a><a name="p85165411090"></a>要求为单调递减序列。</p>
</td>
</tr>
<tr id="row11516154115915"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1751614419918"><a name="p1751614419918"></a><a name="p1751614419918"></a>cb_max[]</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p751618410917"><a name="p751618410917"></a><a name="p751618410917"></a>高色温下B/G和ISO的联动数组。</p>
<p xml:lang="sv-SE" id="p7516164115910"><a name="p7516164115910"></a><a name="p7516164115910"></a>要求为单调递增序列。</p>
</td>
</tr>
<tr id="row251654110914"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1251634118910"><a name="p1251634118910"></a><a name="p1251634118910"></a>cb_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p205161141797"><a name="p205161141797"></a><a name="p205161141797"></a>低色温下B/G和ISO的联动数组。</p>
<p xml:lang="sv-SE" id="p45163411297"><a name="p45163411297"></a><a name="p45163411297"></a>要求为单调递减序列。</p>
</td>
</tr>
</tbody>
</table> #### ot\_isp\_awb\_lum\_histgram\_attr<a name="ZH-CN_TOPIC_0000002457840821"></a> **表 1** ot\_isp\_awb\_lum\_histgram\_attr参数说明 <a name="table57545591912"></a>
<table><thead align="left"><tr id="row157541759496"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p187543591493"><a name="p187543591493"></a><a name="p187543591493"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.4.1.2"><p id="p13754115919912"><a name="p13754115919912"></a><a name="p13754115919912"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.2.4.1.3"><p id="p475445912911"><a name="p475445912911"></a><a name="p475445912911"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row475418591891"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1175414591910"><a name="p1175414591910"></a><a name="p1175414591910"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.2 "><p id="p07543591593"><a name="p07543591593"></a><a name="p07543591593"></a>是否使能亮度调整AWB权重功能。</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p17754059591"><a name="p17754059591"></a><a name="p17754059591"></a>建议打开</p>
</td>
</tr>
<tr id="row67544599913"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p167546591293"><a name="p167546591293"></a><a name="p167546591293"></a>op_type</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.2 "><a name="ul27541359899"></a><a name="ul27541359899"></a><ul id="ul27541359899"><li xml:lang="sv-SE">Auto模式下，AWB自动完成亮度直方图统计，但支持用户手动配置亮度权重；</li><li xml:lang="sv-SE">Manual模式下，支持用户配置亮度直方图统计的门限和亮度权重。</li></ul>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p075511591991"><a name="p075511591991"></a><a name="p075511591991"></a>建议设置为Auto模式，用户手动配置亮区、暗区权重，达到亮区优先or暗区优先的效果。</p>
</td>
</tr>
<tr id="row9755959393"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1575510591597"><a name="p1575510591597"></a><a name="p1575510591597"></a>hist_thresh[]</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p775575911917"><a name="p775575911917"></a><a name="p775575911917"></a>用户设置亮度直方图的门限，仅手动模式有效。</p>
<p xml:lang="sv-SE" id="p1775519592910"><a name="p1775519592910"></a><a name="p1775519592910"></a>取值范围：[0x0, 0xFF]，要求为单调递增序列。</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.3 "><p id="p1755135913918"><a name="p1755135913918"></a><a name="p1755135913918"></a>-</p>
</td>
</tr>
<tr id="row16755659394"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p475514591992"><a name="p475514591992"></a><a name="p475514591992"></a>hist_wt[]</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p3755185919912"><a name="p3755185919912"></a><a name="p3755185919912"></a>用户设置亮度直方图的权重，自动、手动模式下均有效。8bit小数精度，取值范围：<span xml:lang="en-US" id="ph16755125916911"><a name="ph16755125916911"></a><a name="ph16755125916911"></a>[0x0, 0xFFFF]</span></p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1975513591398"><a name="p1975513591398"></a><a name="p1975513591398"></a>亮度权重的影响公式：</p>
<p class="msonormal" id="p3755759493"><a name="p3755759493"></a><a name="p3755759493"></a><a name="image137551059699"></a><a name="image137551059699"></a><span><img class="mathml" id="image137551059699" src="figures/zh-cn_formulaimage_0000002457881109.png" width="159.60000000000002" height="22.453991000000002"></span></p>
</td>
</tr>
</tbody>
</table> ### ot\_isp\_awb\_attr\_ex<a name="ZH-CN_TOPIC_0000002424202214"></a> ot\_isp\_awb\_attr\_ex结构体定义了Advance算法的可调节参数，包括独立光源点定义、混合光源权重配置等。该结构体引用了以下子结构体： - ot\_isp\_awb\_in\_out\_attr
- ot\_isp\_awb\_extra\_light\_source\_info **表 1** ot\_isp\_awb\_attr\_ex参数说明 <a name="table1020mcpsimp"></a>
<table><thead align="left"><tr id="row1027mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.2"><p id="p1031mcpsimp"><a name="p1031mcpsimp"></a><a name="p1031mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.4.1.3"><p id="p1033mcpsimp"><a name="p1033mcpsimp"></a><a name="p1033mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1035mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1037mcpsimp"><a name="p1037mcpsimp"></a><a name="p1037mcpsimp"></a>tolerance</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1039mcpsimp"><a name="p1039mcpsimp"></a><a name="p1039mcpsimp"></a>帧间相关的容忍度。设置为0时，AWB每2帧刷新AWB增益；设置为非0值时，AWB仅在检测到场景变化大于容忍值时刷新AWB增益。</p>
<p id="p1040mcpsimp"><a name="p1040mcpsimp"></a><a name="p1040mcpsimp"></a>默认值 0x2。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p1042mcpsimp"><a name="p1042mcpsimp"></a><a name="p1042mcpsimp"></a>FW在判断为室外场景时，自动关闭帧间相关，每2帧重新计算AWB增益。</p>
<p id="p1043mcpsimp"><a name="p1043mcpsimp"></a><a name="p1043mcpsimp"></a>tolerance取值较大时，AWB稳定性增强，灵敏度降低，光源色温变化时AWB不能做出及时调整。</p>
<p id="p1044mcpsimp"><a name="p1044mcpsimp"></a><a name="p1044mcpsimp"></a>推荐取值范围：[0x2, 0x4]</p>
</td>
</tr>
<tr id="row1045mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1047mcpsimp"><a name="p1047mcpsimp"></a><a name="p1047mcpsimp"></a>zone_radius</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1049mcpsimp"><a name="p1049mcpsimp"></a><a name="p1049mcpsimp"></a>分块统计信息分类的半径。</p>
<p id="p1050mcpsimp"><a name="p1050mcpsimp"></a><a name="p1050mcpsimp"></a>默认值 0x10。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p1052mcpsimp"><a name="p1052mcpsimp"></a><a name="p1052mcpsimp"></a>sensor不同亮度灰色块感光一致性较差时，可适当放大该参数。WDR模式下，可适当放大该参数。</p>
</td>
</tr>
<tr id="row1053mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1055mcpsimp"><a name="p1055mcpsimp"></a><a name="p1055mcpsimp"></a>curve_l_limit</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1057mcpsimp"><a name="p1057mcpsimp"></a><a name="p1057mcpsimp"></a>普朗克曲线的左<span xml:lang="en-US" id="ph1058mcpsimp"><a name="ph1058mcpsimp"></a><a name="ph1058mcpsimp"></a>侧边界。</span></p>
<p xml:lang="sv-SE" id="p1059mcpsimp"><a name="p1059mcpsimp"></a><a name="p1059mcpsimp"></a>取值范围：[0x0, 0x100]</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p1061mcpsimp"><a name="p1061mcpsimp"></a><a name="p1061mcpsimp"></a>排除场景中的绿色块。大面积绿色场景偏色时，可以修改curve_l_limit来优化。</p>
</td>
</tr>
<tr id="row1062mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1064mcpsimp"><a name="p1064mcpsimp"></a><a name="p1064mcpsimp"></a>curve_r_limit</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1066mcpsimp"><a name="p1066mcpsimp"></a><a name="p1066mcpsimp"></a>普朗克曲线的右侧边界。</p>
<p xml:lang="sv-SE" id="p1067mcpsimp"><a name="p1067mcpsimp"></a><a name="p1067mcpsimp"></a>取值范围：[0x100, 0xFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p1069mcpsimp"><a name="p1069mcpsimp"></a><a name="p1069mcpsimp"></a>排除场景中的紫色块。如果sensor在低照度下的黑电平漂移较严重时，需要修改curve_r_limit参数来优化。通常不需要修改。</p>
</td>
</tr>
<tr id="row1070mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1072mcpsimp"><a name="p1072mcpsimp"></a><a name="p1072mcpsimp"></a>extra_light_en</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1074mcpsimp"><a name="p1074mcpsimp"></a><a name="p1074mcpsimp"></a>是否使能独立光源点功能</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p1076mcpsimp"><a name="p1076mcpsimp"></a><a name="p1076mcpsimp"></a>独立光源点功能可优化固定场景的偏色问题。</p>
</td>
</tr>
<tr id="row1077mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1079mcpsimp"><a name="p1079mcpsimp"></a><a name="p1079mcpsimp"></a>light_info[]</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1081mcpsimp"><a name="p1081mcpsimp"></a><a name="p1081mcpsimp"></a>独立光源点或干扰色的颜色信息。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1083mcpsimp"><a name="p1083mcpsimp"></a><a name="p1083mcpsimp"></a>用户可通过PQTools的3A分析工具界面添加光源点或删除干扰色。</p>
</td>
</tr>
<tr id="row1084mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1086mcpsimp"><a name="p1086mcpsimp"></a><a name="p1086mcpsimp"></a>in_or_out</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1088mcpsimp"><a name="p1088mcpsimp"></a><a name="p1088mcpsimp"></a>室内外检测参数。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1090mcpsimp"><a name="p1090mcpsimp"></a><a name="p1090mcpsimp"></a>推荐打开室内外检测功能，以优化室外树木、草地、天空等场景AWB表现。用户可通过参数配置达到偏暖或偏冷等颜色风格</p>
</td>
</tr>
<tr id="row1091mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1093mcpsimp"><a name="p1093mcpsimp"></a><a name="p1093mcpsimp"></a>multi_light_source_en</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1095mcpsimp"><a name="p1095mcpsimp"></a><a name="p1095mcpsimp"></a>混合光源下特殊策略。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1097mcpsimp"><a name="p1097mcpsimp"></a><a name="p1097mcpsimp"></a>使能后，FW自动检测混合光源程度，调整饱和度或CCM，从而改善偏色。</p>
</td>
</tr>
<tr id="row1098mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1100mcpsimp"><a name="p1100mcpsimp"></a><a name="p1100mcpsimp"></a>multi_ls_type</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1102mcpsimp"><a name="p1102mcpsimp"></a><a name="p1102mcpsimp"></a>混合光源调整策略选择，支持调整饱和度或CCM。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1104mcpsimp"><a name="p1104mcpsimp"></a><a name="p1104mcpsimp"></a>选择饱和度策略，整幅图像的饱和度降低；选择CCM策略，绿色的饱和度影响微弱，红色、蓝色的色调会有改变。</p>
</td>
</tr>
<tr id="row1105mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1107mcpsimp"><a name="p1107mcpsimp"></a><a name="p1107mcpsimp"></a>multi_ls_scaler</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1109mcpsimp"><a name="p1109mcpsimp"></a><a name="p1109mcpsimp"></a>混合光源下，饱和度或CCM最大调整幅度。实际调整幅度还和场景混合光源程度有关。</p>
<p xml:lang="sv-SE" id="p1110mcpsimp"><a name="p1110mcpsimp"></a><a name="p1110mcpsimp"></a>取值范围：[0x0, 0x100]</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1112mcpsimp"><a name="p1112mcpsimp"></a><a name="p1112mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row1113mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1115mcpsimp"><a name="p1115mcpsimp"></a><a name="p1115mcpsimp"></a>multi_ct_bin[]</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1117mcpsimp"><a name="p1117mcpsimp"></a><a name="p1117mcpsimp"></a>混合光源下的色温分段参数。</p>
<p xml:lang="sv-SE" id="p1118mcpsimp"><a name="p1118mcpsimp"></a><a name="p1118mcpsimp"></a>取值范围：[0x0, 0xFFFF]</p>
<p xml:lang="sv-SE" id="p1119mcpsimp"><a name="p1119mcpsimp"></a><a name="p1119mcpsimp"></a>要求为单调递增序列。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p1121mcpsimp"><a name="p1121mcpsimp"></a><a name="p1121mcpsimp"></a><span xml:lang="sv-SE" id="ph1122mcpsimp"><a name="ph1122mcpsimp"></a><a name="ph1122mcpsimp"></a>推荐值：</span>[2300, 2800, 3500, 4800, 5500, 6300, 7000, 8500]</p>
</td>
</tr>
<tr id="row1123mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1125mcpsimp"><a name="p1125mcpsimp"></a><a name="p1125mcpsimp"></a>multi_ct_wt[]</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1127mcpsimp"><a name="p1127mcpsimp"></a><a name="p1127mcpsimp"></a>混合光源下的色温权重参数。</p>
<p xml:lang="sv-SE" id="p1128mcpsimp"><a name="p1128mcpsimp"></a><a name="p1128mcpsimp"></a>取值范围：[0x0, 0x400]</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1130mcpsimp"><a name="p1130mcpsimp"></a><a name="p1130mcpsimp"></a>推荐值：[0x20, 0x40, 0x100, 0x200, 0x200, 0x100, 0x40, 0x20]</p>
<p xml:lang="sv-SE" id="p1131mcpsimp"><a name="p1131mcpsimp"></a><a name="p1131mcpsimp"></a>4800K-5500K色温权重高，低色温、高色温权重降低，混合光源下颜色表现更自然。</p>
</td>
</tr>
<tr id="row1132mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1134mcpsimp"><a name="p1134mcpsimp"></a><a name="p1134mcpsimp"></a>fine_tune_en</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1136mcpsimp"><a name="p1136mcpsimp"></a><a name="p1136mcpsimp"></a>肤色检测等特殊处理。</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1138mcpsimp"><a name="p1138mcpsimp"></a><a name="p1138mcpsimp"></a>仅在室内模式打开，室外模式自动关闭。</p>
</td>
</tr>
</tbody>
</table> #### ot\_isp\_awb\_in\_out\_attr<a name="ZH-CN_TOPIC_0000002457840837"></a> **表 1** ot\_isp\_awb\_in\_out\_attr参数说明 <a name="table1140mcpsimp"></a>
<table><thead align="left"><tr id="row1147mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p1149mcpsimp"><a name="p1149mcpsimp"></a><a name="p1149mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p1151mcpsimp"><a name="p1151mcpsimp"></a><a name="p1151mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p1153mcpsimp"><a name="p1153mcpsimp"></a><a name="p1153mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1155mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1157mcpsimp"><a name="p1157mcpsimp"></a><a name="p1157mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1159mcpsimp"><a name="p1159mcpsimp"></a><a name="p1159mcpsimp"></a>室内外模式判决开关。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1161mcpsimp"><a name="p1161mcpsimp"></a><a name="p1161mcpsimp"></a>AWB根据曝光信息判断当前场景是室内或室外。</p>
</td>
</tr>
<tr id="row1162mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1164mcpsimp"><a name="p1164mcpsimp"></a><a name="p1164mcpsimp"></a>op_type</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1166mcpsimp"><a name="p1166mcpsimp"></a><a name="p1166mcpsimp"></a>自动或手动判决模式。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1168mcpsimp"><a name="p1168mcpsimp"></a><a name="p1168mcpsimp"></a>手动模式下，用户输入室内外状态；自动模式下，FW根据环境亮度和亮度门限值，判断当前是室内或室外。</p>
</td>
</tr>
<tr id="row1169mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1171mcpsimp"><a name="p1171mcpsimp"></a><a name="p1171mcpsimp"></a>outdoor_status</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1173mcpsimp"><a name="p1173mcpsimp"></a><a name="p1173mcpsimp"></a>室内外模式判决结果；</p>
<p xml:lang="sv-SE" id="p1174mcpsimp"><a name="p1174mcpsimp"></a><a name="p1174mcpsimp"></a>1表示室外，0表示室内。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p1176mcpsimp"><a name="p1176mcpsimp"></a><a name="p1176mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row1177mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1179mcpsimp"><a name="p1179mcpsimp"></a><a name="p1179mcpsimp"></a>out_thresh</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1181mcpsimp"><a name="p1181mcpsimp"></a><a name="p1181mcpsimp"></a>室内外场景判定设置的亮度门限阈值，以单位为us的曝光时间，小于该阈值则认为是室外。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1183mcpsimp"><a name="p1183mcpsimp"></a><a name="p1183mcpsimp"></a>非SDK提供的AE库的应用，请将曝光信息传递给AWB库。</p>
<p xml:lang="sv-SE" id="p1184mcpsimp"><a name="p1184mcpsimp"></a><a name="p1184mcpsimp"></a>用户需要根据录像机的感光强度、产品形态调整亮度门限。DV等产品建议调大该门限值，录像机建议调小该门限值。</p>
</td>
</tr>
<tr id="row1187mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1189mcpsimp"><a name="p1189mcpsimp"></a><a name="p1189mcpsimp"></a>low_stop</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1191mcpsimp"><a name="p1191mcpsimp"></a><a name="p1191mcpsimp"></a>自然光源色温起点的扩展，建议4500K。</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1193mcpsimp"><a name="p1193mcpsimp"></a><a name="p1193mcpsimp"></a>判断为室外模式后，[low_start，high_start]色温范围内的灰色块权重最大，[low_stop，low_start]和[high_start，high_stop]两个色温区间是过渡带，保证平滑过渡。</p>
<p xml:lang="sv-SE" id="p1194mcpsimp"><a name="p1194mcpsimp"></a><a name="p1194mcpsimp"></a>四个色温门限值都增大，图像偏暖色；四个色温门限值都减小，图像偏冷色。</p>
</td>
</tr>
<tr id="row1195mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1197mcpsimp"><a name="p1197mcpsimp"></a><a name="p1197mcpsimp"></a>low_start</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1199mcpsimp"><a name="p1199mcpsimp"></a><a name="p1199mcpsimp"></a>自然光源色温范围的起点，建议5000K。</p>
</td>
</tr>
<tr id="row1200mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1202mcpsimp"><a name="p1202mcpsimp"></a><a name="p1202mcpsimp"></a>high_start</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1204mcpsimp"><a name="p1204mcpsimp"></a><a name="p1204mcpsimp"></a>自然光源色温范围的终点，建议6500K。</p>
</td>
</tr>
<tr id="row1205mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1207mcpsimp"><a name="p1207mcpsimp"></a><a name="p1207mcpsimp"></a>high_stop</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1209mcpsimp"><a name="p1209mcpsimp"></a><a name="p1209mcpsimp"></a>自然光源色温终点的扩展，建议7500K。</p>
</td>
</tr>
<tr id="row1210mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1212mcpsimp"><a name="p1212mcpsimp"></a><a name="p1212mcpsimp"></a>green_enhance_en</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1214mcpsimp"><a name="p1214mcpsimp"></a><a name="p1214mcpsimp"></a>在绿色植物场景下是否对绿色通道增强。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1216mcpsimp"><a name="p1216mcpsimp"></a><a name="p1216mcpsimp"></a>仅在大面积灰绿色草地等场景才有效，其他场景无效。</p>
</td>
</tr>
<tr id="row1217mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1219mcpsimp"><a name="p1219mcpsimp"></a><a name="p1219mcpsimp"></a>out_shift_limit</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1221mcpsimp"><a name="p1221mcpsimp"></a><a name="p1221mcpsimp"></a>室外模式支持的光源范围，建议0x20。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1223mcpsimp"><a name="p1223mcpsimp"></a><a name="p1223mcpsimp"></a>-</p>
</td>
</tr>
</tbody>
</table> #### ot\_isp\_awb\_extra\_light\_source\_info<a name="ZH-CN_TOPIC_0000002424202170"></a> **表 1** ot\_isp\_awb\_extra\_light\_source\_info参数说明 <a name="table1225mcpsimp"></a>
<table><thead align="left"><tr id="row1232mcpsimp"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p1234mcpsimp"><a name="p1234mcpsimp"></a><a name="p1234mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.2.4.1.2"><p id="p1236mcpsimp"><a name="p1236mcpsimp"></a><a name="p1236mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p1238mcpsimp"><a name="p1238mcpsimp"></a><a name="p1238mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1240mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1242mcpsimp"><a name="p1242mcpsimp"></a><a name="p1242mcpsimp"></a>white_r_gain</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1244mcpsimp"><a name="p1244mcpsimp"></a><a name="p1244mcpsimp"></a>增加或删除区域的中心Cr坐标。</p>
<p xml:lang="sv-SE" id="p1245mcpsimp"><a name="p1245mcpsimp"></a><a name="p1245mcpsimp"></a>取值范围：[0x0, 0xFFF]，8bit精度。</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1247mcpsimp"><a name="p1247mcpsimp"></a><a name="p1247mcpsimp"></a>可通过PQTools的3A分析工具配置这两个参数。</p>
</td>
</tr>
<tr id="row1248mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1250mcpsimp"><a name="p1250mcpsimp"></a><a name="p1250mcpsimp"></a>white_b_gain</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1252mcpsimp"><a name="p1252mcpsimp"></a><a name="p1252mcpsimp"></a>增加或删除区域的中心Cb坐标。取值范围：[0x0, 0xFFF]，8bit精度。</p>
</td>
</tr>
<tr id="row1253mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1255mcpsimp"><a name="p1255mcpsimp"></a><a name="p1255mcpsimp"></a>exp_quant</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1257mcpsimp"><a name="p1257mcpsimp"></a><a name="p1257mcpsimp"></a>对外界环境亮度做判断，暂不支持，不需要配置。</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1259mcpsimp"><a name="p1259mcpsimp"></a><a name="p1259mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row1260mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1262mcpsimp"><a name="p1262mcpsimp"></a><a name="p1262mcpsimp"></a>light_status</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1264mcpsimp"><a name="p1264mcpsimp"></a><a name="p1264mcpsimp"></a>光源点状态。</p>
<p xml:lang="sv-SE" id="p1265mcpsimp"><a name="p1265mcpsimp"></a><a name="p1265mcpsimp"></a>0：不使能；</p>
<p xml:lang="sv-SE" id="p1266mcpsimp"><a name="p1266mcpsimp"></a><a name="p1266mcpsimp"></a>1：增加光源点；</p>
<p xml:lang="sv-SE" id="p1267mcpsimp"><a name="p1267mcpsimp"></a><a name="p1267mcpsimp"></a>2：删除干扰色；</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p1269mcpsimp"><a name="p1269mcpsimp"></a><a name="p1269mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row1270mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1272mcpsimp"><a name="p1272mcpsimp"></a><a name="p1272mcpsimp"></a>raius</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p1274mcpsimp"><a name="p1274mcpsimp"></a><a name="p1274mcpsimp"></a>增加或删除区域的半径。取值范围：[0x0, 0xFF]</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p xml:lang="sv-SE" id="p1276mcpsimp"><a name="p1276mcpsimp"></a><a name="p1276mcpsimp"></a>尽量避免[white_r_gain、white_b_gain]为中心，u8radius为半径的圆形区域与Plankcian曲线重合，避免光源点重合。</p>
</td>
</tr>
</tbody>
</table> ## 问题定位<a name="ZH-CN_TOPIC_0000002424362042"></a> ### Raw数据分析\(AWB\)<a name="ZH-CN_TOPIC_0000002424362094"></a> 局部偏色问题首先要分析Raw数据，确认是采集端引入还是后续算法处理引入。推荐灌Raw数据到ISP单板，操作PQTools定位问题原因。 1. 确认黑电平和RGGB顺序正确。 **图 1** 黑电平配置参数确认<a name="fig1281mcpsimp"></a> ![](figures/黑电平配置参数确认.png "黑电平配置参数确认") 2. Bypass 或Disable CCM、Gamma、ACM等影响颜色的模块，将AWB问题和其他模块问题分开。 **图 2** 关闭其他颜色模块<a name="fig1284mcpsimp"></a> ![](figures/关闭其他颜色模块.png "关闭其他颜色模块") 3. 打开3A分析工具，手动配置白平衡系数。选择左图中的灰色块，右键选择Apply Result to Global，当前灰色块期望的AWB增益生效。 **图 3** 选择灰色块，配置手动AWB<a name="fig1287mcpsimp"></a> ![](figures/选择灰色块-配置手动AWB.png "选择灰色块-配置手动AWB") 4. 观察图像中灰色区域颜色是否正常。示例图像仅做了Manual AWB，已经出现了局部区域偏粉，说明Raw数据有问题，请向前端追溯。 **图 4** 手动AWB<a name="fig1290mcpsimp"></a> ![](figures/手动AWB.png "手动AWB") 5. 如果以上步骤确认Raw数据是正常的，那么需要检查Gamma曲线是否合理。可以在板端配置Manual AWB，仅使能BLC、AWB、Demosaic和Gamma几个模块，开关Gamma对比偏色问题。
6. 局部偏色问题，还要确认是否混合光源场景。可以用3A分析工具分别选不同的区域手动计算白平衡系数，如果不同区域期望的白平衡增益差异大，说明是混合光源场景。只能通过降低饱和度或者色温权重调整等方式优化颜色表现。 ### 3A分析工具看白色区域是否合理（AWB）<a name="ZH-CN_TOPIC_0000002424362066"></a> 1. 从统计结果确认统计参数配置是否合理。选择白色块，正常情况CountAll应接近0xFFFF。下图中的CountAll为0，说明统计模块未找到灰点。 **图 1** 统计结果确认<a name="fig1296mcpsimp"></a> ![](figures/统计结果确认.png "统计结果确认") 2. 关闭CrMax等灰点条件自适应功能。 **图 2** 关闭统计参数自动调整功能<a name="fig1299mcpsimp"></a> ![](figures/关闭统计参数自动调整功能.png "关闭统计参数自动调整功能") 3. 调整灰点配置参数，调试原则是：上限调大，下限调小，到3A分析工具显示的统计结果，count\_all接近0xFFFF为止。确认是哪个参数引入问题后，white\_level和black\_level修改默认参数，Cr等需要调整数组。 **图 3** 手动配置统计参数<a name="fig1302mcpsimp"></a> ![](figures/手动配置统计参数.png "手动配置统计参数") 4. 统计模块OK后，确认室内外检测是否正确，如果室内外检测错误，先用Manual的方式配置正确的室内外模式。 **图 4** 检查室内外配置参数<a name="fig1305mcpsimp"></a> ![](figures/检查室内外配置参数.png "检查室内外配置参数") ![](figures/2-18b.png) 5. 确认检测色温有没有超出色温的上下限。将色温的上限调大，下限调小，观察问题是否有改善。
6. 确认灰色块有没有在白色区域范围内。 影响白色区域范围的参数有：high\_color\_temp、low\_color\_temp、shift\_limit、curve\_l\_limit、curve\_r\_limit。观察是否有参数将灰色块排除在白色区域范围外。如[图5](#_Toc74749328)可以看到灰色块落在shift\_limit参数外，调大shift\_limit参数可解决问题如[图6](#_Toc74749329)。 **图 5** Shift参数调整前效果<a name="_Toc74749328"></a> ![](figures/Shift参数调整前效果.png "Shift参数调整前效果") **图 6** Shift参数调整后效果<a name="_Toc74749329"></a> ![](figures/Shift参数调整后效果.png "Shift参数调整后效果") 7. 场景内有多个光源点时，需要排除肤色检测模块对算法的影响。
8. 仍然不能确定偏色原因时，将算法由Advance设置为LowCost，看能否解决；若不能解决，将Attr的zone\_sel设置为0，看能否解决；若还不能解决，就需要从滤光片、黑电平等模块系统分析。 # 基础调色方案
## 基础调色方案概述<a name="ZH-CN_TOPIC_0000002457840781"></a> 本章主要介绍的是与基础调色方案相关的模块，包括CCM等模块的调试指导。进行完CCM等模块的调试以后，产品的颜色能达到常规使用的效果需求。 ## CCM调试<a name="ZH-CN_TOPIC_0000002457880853"></a> ### CCM标定参数说明<a name="ZH-CN_TOPIC_0000002457880957"></a> CCM标定的原理是，使用sensor抓拍到的24色卡场景下前18个色块的实际颜色信息和其期望值，计算3x3的CCM矩阵。输入颜色经CCM矩阵处理得到的颜色与其期望值差距越小，则CCM矩阵就越理想。 **表 1** CCM标定参数 <a name="table1323mcpsimp"></a>
<table><thead align="left"><tr id="row1330mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p1332mcpsimp"><a name="p1332mcpsimp"></a><a name="p1332mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="39%" id="mcps1.2.4.1.2"><p id="p1334mcpsimp"><a name="p1334mcpsimp"></a><a name="p1334mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.2.4.1.3"><p id="p1336mcpsimp"><a name="p1336mcpsimp"></a><a name="p1336mcpsimp"></a>场景说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1338mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p xml:lang="sv-SE" id="p1340mcpsimp"><a name="p1340mcpsimp"></a><a name="p1340mcpsimp"></a>color_temp</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p1342mcpsimp"><a name="p1342mcpsimp"></a><a name="p1342mcpsimp"></a>当前配置的CCM对应的色温。</p>
<p id="p1343mcpsimp"><a name="p1343mcpsimp"></a><a name="p1343mcpsimp"></a>取值范围：[500, 30000]</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p1345mcpsimp"><a name="p1345mcpsimp"></a><a name="p1345mcpsimp"></a>-</p>
</td>
</tr>
<tr id="row1346mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1348mcpsimp"><a name="p1348mcpsimp"></a><a name="p1348mcpsimp"></a>ccm[]</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p1350mcpsimp"><a name="p1350mcpsimp"></a><a name="p1350mcpsimp"></a>不同色温下的颜色校正矩阵，<span xml:lang="sv-SE" id="ph1351mcpsimp"><a name="ph1351mcpsimp"></a><a name="ph1351mcpsimp"></a>8bit</span>小数精度。bit 15是符号位，0表示正数，1表示负数，例如0x8010表示-16。</p>
<p id="p1352mcpsimp"><a name="p1352mcpsimp"></a><a name="p1352mcpsimp"></a>取值范围：[0x0,0xFFFF]</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p1354mcpsimp"><a name="p1354mcpsimp"></a><a name="p1354mcpsimp"></a>支持最大七个最小三个不同色温下的色彩还原矩阵，要按照色温递减的方式配置CCM。典型的三组CCM为D50，TL84，A三个光源下的CCM。典型的五组CCM为10K，D65，D50，TL84，A五个光源下的CCM。前一组的色温值与后一组的色温值需符合如下规则：Tpre * (15/16) &gt; Tpost * (17/16)。最终ISP将根据实际色温，将颜色校正矩阵通过插值的方法得到实际的颜色校正矩阵。</p>
</td>
</tr>
</tbody>
</table> ### RAW数据采集<a name="ZH-CN_TOPIC_0000002424362086"></a> #### 标定光源选择<a name="ZH-CN_TOPIC_0000002424202222"></a> - D50人工光源或5000K-5500K之间的自然光源
- TL84光源
- A光源 #### 采集步骤<a name="ZH-CN_TOPIC_0000002457880881"></a> 1. 采集设备准备：标准X-Rite 24色卡，照度为600Lux均匀光源（左右两侧双光源，光源与色卡平面的夹角在25°- 45°），录像机。
2. 调整AE目标亮度，最亮灰阶\(Block 19\)的G分量亮度在饱和值的0.8倍左右（以12bit RAW数据为例，G分量数值在0xC00-0xD80之间）。
3. 采集中性灰RAW图像，检查录像机的镜头阴影程度。Shading较严重时，需要先标定Shading系数，24色卡图像需要先进行Shading校正后，再进行CCM标定。 ### 标定<a name="ZH-CN_TOPIC_0000002457840873"></a> #### 标定步骤<a name="ZH-CN_TOPIC_0000002457840853"></a> 1. RAW数据导入部分请参考《图像质量调试工具使用指南》。
2. 选取24色区域。 拖动四角色块中央的红色手柄，即可改变24色框的排布，将24个方框对准RAW图像的24色区域即可。如[图1](#_Ref426711119)所示。 **图 1** 24色选框<a name="_Ref426711119"></a> ![](figures/24色选框.png "24色选框") 3. 配置标定参数（GAMMA，参考LAB，色块权重，差异标准）。 - 设置ISP GAMMA：在ISP Gamma的下拉框中选择需要的Gamma预设值（目前支持sRGB和Rec709），也支持自定义。请用户输入ISP当前生效的Gamma表。 **注意：当用户自定义ISP Gamma值时，需注意匹配相对应的LAB参考值，防止由于ISP Gamma和LAB Reference不匹配，导致作为线性变化的AWB和CCM共同作用无法达到目标图片的效果**。 - 设置显示GAMMA：在Display Gamma的下拉框中选择需要的Gamma预设值（目前支持sRGB和Rec709）。 - 设置LAB参考值：在LAB Reference的下拉框中选择需要的LAB预设值（目前支持D65条件下的Xrite标准值），也支持自定义。 **注意：当用户自定义LAB值时，需注意匹配相对应的ISP Gamma，防止由于ISP Gamma和LAB Reference不匹配，导致作为线性变化的AWB和CCM共同作用无法达到目标图片的效果**。 - 设置色块权重：在6x4的表格中配置色块的权重。色块的位置与表格中的位置对应。取值范围为0.0到16.0的浮点数，保留一位小数。 - 选择差异标准：选择差异衡量的标准（支持CIE76、CIE94和CIE2000）以及差异矩阵（Delta C\*ab与Delta E\*ab）。推荐使用“CIE76 Delta E\*ab”和“CIE2000 Delta C\*ab”两种组合进行标定。 - 选择是否autoGain。 - 当选择autoGain时，会对RAW的值和目标值做亮度补偿。默认是勾选。在采集RAW的时候，通过控制曝光，使采集到的RAW数据在Gamma后接近目标图片的亮度。autoGain的作用是使用数字增益让RAW数据达到亮度最佳，减少采集RAW的难度。 - 不选择autoGain时，用户可以通过完全控制RAW数据的亮度来得到不同的CCM的参数。 - 选择是否BT.2020。 - 当选择BT.2020时，ISP的输出符合BT.2020的标准。ISP Gamma可以是用户自定义的Gamma。显示GAMMA，LAB参考值，这两项和目标图片保持一致。当目标图片为sRGB标准时，设置显示GAMMA为sRGB。当目标图片为BT.2020标准时，设置显示GAMMA为Rec709。 - 不选择BT.2020时，ISP的输出符合sRGB的标准。 4. 点击“Calibrate”按钮进行标定，获得结果CCM。在Result页面进行手动色调/饱和度调整，直到获取的CCM满足要求。 #### 手动调整CCM标定结果<a name="ZH-CN_TOPIC_0000002424362018"></a> 如果查看校正后的图像发现效果不理想，还可以进行手动调整。在“Result”页面调整色调（Hue Corr）和饱和度（Sat Corr）修正值，并点击“Manual Adjust”，可以重新计算CCM并进行图像校正。重复上述操作，直到获得满意图像即可。 ### 手动修改CCM<a name="ZH-CN_TOPIC_0000002424202154"></a> 颜色校正矩阵的公式如下： ![](figures/zh-cn_formulaimage_0000002424202514.png) 为了保证白平衡不受破坏，参数必须满足条件： ![](figures/zh-cn_formulaimage_0000002457881253.png) **R’中主要应该还是R分量的部分居多，因此必须满足条件：** ![](figures/zh-cn_formulaimage_0000002457841157.png) 在满足以上条件的情况下，就可以微调颜色校正矩阵而不致产生破坏性影响。 将PQ ISP Calibration Tool校正出来的颜色校正矩阵配置到硬件寄存器后，抓取一副自己的24色卡图像和一副标杆的24色卡图像，在Photoshop中进行颜色对比： **图 1** 捕获图片和目标图片的对比<a name="fig113mcpsimp"></a> ![](figures/捕获图片和目标图片的对比.png "捕获图片和目标图片的对比") 在右侧的info框中可以对比查看两幅图像的同样色块的R/G/B分量值，通常我们会更注重肤色、红色、绿色的校正。也可以对比标准色卡的R/G/B分量值进行对比。 **图 2** 24色卡标准值<a name="fig116mcpsimp"></a> ![](figures/24色卡标准值.jpg "24色卡标准值") 这时需要对比公式来调节参数。例如： 如果对比发现的红色块的B分量偏大，导致红色块偏水红色，那么根据公式![](figures/zh-cn_formulaimage_0000002424202526.png)，且a<sub>20，</sub>a<sub>21，</sub>a<sub>22 </sub>的正负性分别为负，负，正，**当前水红色的R，G，B值的大小顺序为R\>B\>G**，且已知目标标准是\(175,54,60\)，而且a<sub>20</sub> + a<sub>21</sub> + a<sub>22</sub> = 256，因此可以通过三种方式来实现B’减小的目的： - 增大a<sub>20 </sub>的绝对值，同时等量减小a<sub>21 </sub>的绝对值；
- 增大a<sub>21 </sub>的绝对值，同时等量增大a<sub>22 </sub>的绝对值；
- 增大a<sub>20 </sub>的绝对值，同时等量增大a<sub>22 </sub>的绝对值。 通过这种方式，减小最终红色块的B’分量的值，从而将水红色的红色块校正回来。**注意：在修改红色块的B分量时，由于其他颜色的RGB大小顺序可能和红色块的冲突会导致其他色块的最终结果受到影响，所以要注意兼顾其他颜色，尤其是绿色块，肤色块，防止由于修改CCM矩阵带来的其他典型色块的偏色问题。** 对于深肤色和浅肤色这种三个颜色分量的值都差不多的色块，不是特别好单独调节。建议还是将红、绿、蓝这三个单色块的颜色校准确，其他颜色才会准确，因为其他颜色都是这三种颜色的混合色。 由于参与CCM标定的样本的影响，CCM的标定结果可能接近最佳而不是最佳。对CCM标定的结果进行手动调节，可以参考下面的几种做法。 - CCM主对角线以外元素均为负值会较好。如果a02为正数，会导致饱和度高的红色偏紫，如果a20为正数，会导致饱和度高的蓝色偏紫。如果遇到这类偏紫的问题时，可以考虑手动将a02或a20从接近0的正数改为比较小的负数。
- a10为负值时，a10绝对值越大，CCM后红色的G通道值越小，红色的饱和度越高；a12为负值时，a12绝对值越大，CCM后蓝色的G通道值越小，蓝色的饱和度越高。如果遇到红色或蓝色的饱和度过高的问题时，可以考虑减小a10或a12的绝对值。 ### WDR 模式下标定CCM<a name="ZH-CN_TOPIC_0000002457880981"></a> 对于WDR模式，因为CCM容易受到DRC的影响，容易造成颜色难以矫正。所以对于WDR模式来说，调整颜色需注意以下三点： - 在标准光源下（一般是三组光源，分别是D50，TL84，A光源）拍标准24色卡，曝光比手动最大，同时也要调整亮度值，避免长帧过曝，采集长帧的RAW数据进行CCM的标定。标定过程中可以适当的降低饱和度，不能选择开启autoGain功能。
- 适当减少DRC曲线对图像亮度的大幅度提升，这样DRC对颜色的改变会较弱。此时，图像的亮度会有所降低达不到想要的亮度，这时，可以用gamma对亮度进行适当的提升。这样联调DRC和gamma模块，可以让整体的颜色调节更准确一些。
- 对于WDR模式，因为大多场景是混合光源场景，容易出现亮处颜色偏色，人脸颜色偏红等问题，除了可以降低饱和度值以外，还可以使用CA模块对这些区域适当的降低饱和度。 ### 影响CCM标定的因素<a name="ZH-CN_TOPIC_0000002457840757"></a> CCM前的色卡数据的颜色特点如[图1](#_Ref505766663)所示。 **图 1** CCM前24色卡值二维图<a name="_Ref505766663"></a> ![](figures/CCM前24色卡值二维图.png "CCM前24色卡值二维图") **图 2** CCM前24色卡值三维图<a name="fig157mcpsimp"></a> ![](figures/CCM前24色卡值三维图.png "CCM前24色卡值三维图") 从二维图中可以看出CCM前数据饱和度低，亮度低。 如果拍摄的raw数据亮度不符合要求，Gamma也为自定义，那么参与运算CCM时建议选择误差评价Cie2000，LCAB。尽量使误差分布在亮度的方向上，而不是分布在饱和度和色度上。侧重保证饱和度低的颜色的准确。如果觉得某些颜色不好看，那就需要调整CCM计算时色块的权重参数，重新计算，反复确认。 调试好的CCM后，ISP最终输出色卡图片的颜色特点如[图3](#_Ref504385923)所示。 **图 3** ISP最终24色卡值二维图<a name="_Ref504385923"></a> ![](figures/ISP最终24色卡值二维图.png "ISP最终24色卡值二维图") **图 4** ISP最终24色卡值三维图<a name="_Ref504385924"></a> ![](figures/ISP最终24色卡值三维图.png "ISP最终24色卡值三维图") 从[图4](#_Ref504385924)可以看出蓝色红色的误差最好分布在亮度维度上，因为如果红色和蓝色的误差分布在饱和度上，容易过饱和而超出色域。黄色的误差不用在意，因为在色卡中黄色属于这个画面亮度最高的色块，如果这张图片降低一个亮度等级，那么黄色块的颜色误差自然会好一些。 色卡做标定的要点如下： - 光源均匀照射色卡，在色卡表面不能有阴影或者光源的变化。
- 色卡的色块RGB值不能发生clip。
- 灰块的亮度必须在70-95 IRE范围内。
- 需要知道目标图片的gamma曲线。
- 采集的raw需要在符合黑体辐射的光源下，所以最好是在阳光下。
- 拍摄的raw不能有混合色温，如果色卡的色温和背景的色温差别很大，那么不用关心标定后的背景的颜色表现。 对于CCM标定结果的影响因素： - 源gamma
- 目标gamma
- 目标色彩空间：srgb，2020
- 源和目标图片的白平衡
- 源的亮度增益ispdgain 源gamma和目标gamma很重要，因为颜色的达到主要是依赖CCM和gamma共同作用达到。通俗的理解CCM更多的是起到微调颜色方向的作用，而gamma才是颜色调节到位的主力。根本原因是端到端系统对于ISP的要求。显示设备会对ISP传来的数据按照协议做Degamma的运算，还原出线性RGB数据，然后再做处理后显示在屏上。在HDR时代，这样的遵守协议的要求就更高了。源gamma和目标gamma的不匹配会直接造成颜色的误差。 源和目标图片的白平衡很重要，是因为标杆的颜色风格的一个决定性因素是标杆的AWB的增益。AWB可以偏向光源色，也可以完全还原到D65光源。 源的亮度增益ispdgain很重要，因为CCM的3x3矩阵的求解需要尽可能的让矩阵不包括亮度调节的成分。过亮或者是过暗的RAW标定出的CCM的饱和度特性就和亮度合适的不同。过亮的RAW标定出的CCM会偏向饱和度低，过暗的RAW标定出的CCM会偏向饱和度高。 上面5点因素主要影响CCM标定结果，不是说必须将某个因素调节到某个点就不能变化。更重要的是，需要用改变输入变量的方法来控制或者引导CCM最优解的求解，以达到想要的结果。 # 高级调色方案
## 高级调色方案概述<a name="ZH-CN_TOPIC_0000002424362010"></a> 当完成基础调色方案相关的模块调节后，再进行高级调色方案相关的模块调节。在大部分颜色都满足需求的基础上，可以对于系统的颜色进行一个更加精细和个性化的调节。本章介绍与高级调色方案相关的CLUT等模块。 ### 典型应用模式<a name="ZH-CN_TOPIC_0000002424361978"></a> #### 普通模式<a name="ZH-CN_TOPIC_0000002424202246"></a> 普通模式下系统的颜色调节相对简单。 - 系统的颜色主要由AWB+CCM+GAMMA达到。
- 通过使用CA模块，可以在CCM确定的颜色的基础上，根据亮度做饱和度的调节，可以使画面更有层次。 #### 喜好色增强模式<a name="ZH-CN_TOPIC_0000002424202206"></a> 喜好色增强模式下系统的颜色调节策略： - CCM的调节目标侧重于兼顾所有颜色，即让各种颜色的误差都相当，不偏向于某种颜色。
- CLUT在CCM调试稳定的基础上，针对喜好色做特定的增强，或者针对CCM不满足需求的颜色做单独调节。 #### 色彩风格复制模式<a name="ZH-CN_TOPIC_0000002457840813"></a> 色彩风格复制模式下系统的颜色调节策略： - 系统的曝光策略接近目标设备。
- GAMMA通过使用灰阶卡，或者140色卡中的15个灰阶标定的方式接近目标。
- CCM的调节目标侧重于达到目标设备拍摄的色卡的颜色。
- CLUT在CCM调试基本接近目标设备的基础上，针对CCM后仍有误差的颜色做补充调节。 ## CLUT调试<a name="ZH-CN_TOPIC_0000002424361966"></a> ### CLUT标定参数说明<a name="ZH-CN_TOPIC_0000002457880901"></a> CLUT是一个改变线性RGB值的模块，这个模块把用户的颜色调节需求，转化为源和目标RGB对的数据映射关系。ISP内的CLUT调节目标是可生长完善的，用于所有场景的表。通过交互工具调节后能导出和颜色调节需求等价的CLUT表，在生成CLUT的时候会把有矛盾的需求消除。 ### 需求输入的方式<a name="ZH-CN_TOPIC_0000002457880913"></a> 详细的操作过程请参考《图像质量调试工具使用指南》。 #### 色卡对<a name="ZH-CN_TOPIC_0000002424202194"></a> 使用源设备和目标设备同时拍摄色卡，可以很容易的获得广泛的颜色样本，指导CLUT表的生成。使用X-Rite的ColorChecker色卡可以获得24个颜色样本对，使用X-Rite的ColorChecker SG色卡可以获得140个颜色样本对。 **图 1** 色卡对<a name="fig216mcpsimp"></a> ![](figures/色卡对.png "色卡对")
#### 任意颜色对<a name="ZH-CN_TOPIC_0000002424362034"></a> 使用源设备和目标设备同时拍摄同一场景，可以从场景中选择对应的物体表面，可以获得任意颜色对，指导CLUT表的生成。 **图 1** 任意颜色对<a name="fig220mcpsimp"></a> ![](figures/任意颜色对.png "任意颜色对")
#### HSL参数调节<a name="ZH-CN_TOPIC_0000002457880905"></a> 在没有目标设备的情况下，用源设备拍摄场景后，可以选择想调节的颜色表面，然后通过调整HSL参数来获得目标RGB值，指导CLUT表的生成。hue范围+-20，sat范围0.4-1.6倍，light范围0.6-1.4倍。 **图 1** HSL参数调节<a name="fig224mcpsimp"></a> ![](figures/HSL参数调节.png "HSL参数调节")
### CLUT应用举例<a name="ZH-CN_TOPIC_0000002457840737"></a> #### 利用色卡调节<a name="ZH-CN_TOPIC_0000002457840845"></a> 利用色卡可以快速调节CLUT。 用户可以使用源设备和目标设备，在室外拍摄多个不同亮度下的色卡，源设备采集RAW，目标设备采集JPG。 在板端灌入采集到的RAW，将亮度，白平衡调到和目标图片一致，CCM和Gamma使用当前希望使用的参数，抓取ISP输出的图片。 通过Color Check Free功能可以生成2-3组不同亮度下的色卡色块的RGB对。如图 使用含色卡的JPG图片所示。 **图 1** 使用含色卡的JPG图片<a name="_Ref510010720"></a> ![](figures/使用含色卡的JPG图片.png "使用含色卡的JPG图片") **图 2** 生成色卡RGB对<a name="_Ref515525361"></a> ![](figures/生成色卡RGB对.png "生成色卡RGB对") 如图图 生成色卡RGB对所示，经过多次操作可以得到2-3组不同亮度下的色卡的RGB对。如果经过确认颜色都符合调节需求，那么这些RGB对生成的CLUT就可以看做是一个基本的调节表。将这个RGB对导出，后续调节可以在这个基础上进一步进行。 #### 利用颜色值调节<a name="ZH-CN_TOPIC_0000002424202178"></a> CLUT可以直接使用颜色值进行颜色的调节。下面以肤色调节为例。 在源图和目标图都导入同一个含有颜色分布的图片。这里导入的是含有各种肤色值的图片。 通过Color Check Free功能可以将颜色调节趋势的需求转换到RGB对。如图 使用颜色值调节所示。 **图 1** 使用颜色值调节<a name="_Ref515525385"></a> ![](figures/使用颜色值调节.png "使用颜色值调节") 生成的RGB对如[图2](#_Ref515525411)所示。 **图 2** 生成肤色RGB对<a name="_Ref515525411"></a> ![](figures/生成肤色RGB对.png "生成肤色RGB对") 这些RGB对生成的CLUT，需要加载到板端，通过灌入含有肤色的真实图片的RAW进行进一步的确认。 