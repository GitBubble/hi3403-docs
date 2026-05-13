---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/音频组件API参考/音频组件 API参考.md
--- # 前言
**概述<a name="section143mcpsimp"></a>** 本文档为使用媒体处理芯片的音频进行智能分析方案开发的程序员而写，目的是供您在开发过程中查阅音频支持的各种参考信息，包括各项协议说明、API、错误码等。 **产品版本<a name="section146mcpsimp"></a>** 与本文档相对应的产品版本如下。 <a name="table149mcpsimp"></a>
<table><thead align="left"><tr id="row154mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p156mcpsimp"><a name="p156mcpsimp"></a><a name="p156mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p158mcpsimp"><a name="p158mcpsimp"></a><a name="p158mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row160mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p162mcpsimp"><a name="p162mcpsimp"></a><a name="p162mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p164mcpsimp"><a name="p164mcpsimp"></a><a name="p164mcpsimp"></a>V100</p>
</td>
</tr>
</tbody>
</table> **读者对象<a name="section170mcpsimp"></a>** 本文档（本指南）主要适用于以下工程师： - 技术支持工程师
- 软件开发工程师 **符号约定<a name="section176mcpsimp"></a>** 在本文中可能出现下列标志，它们所代表的含义如下。 <a name="table179mcpsimp"></a>
<table><thead align="left"><tr id="row184mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p186mcpsimp"><a name="p186mcpsimp"></a><a name="p186mcpsimp"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p188mcpsimp"><a name="p188mcpsimp"></a><a name="p188mcpsimp"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row190mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p192mcpsimp"><a name="p192mcpsimp"></a><a name="p192mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="figures/zh-cn_image_0000002441714733.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p194mcpsimp"><a name="p194mcpsimp"></a><a name="p194mcpsimp"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
</tbody>
</table> **修订记录<a name="section217mcpsimp"></a>** 修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。 <a name="table126443203200"></a>
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
</table> # 音频组件
## 概述<a name="ZH-CN_TOPIC_0000002408275386"></a> 音频组件集成了AAC编解码协议，并开放接口，以便于用户集成第三方提供的编解码协议。AAC编解码使用示例代码在sample/audio目录。 >![](public_sys-resources/icon-notice.gif) **须知：** >客户如果需要使用AAC格式的专利，必须从版权权利人处获取授权，并缴纳Licensing Fee。 ## 重要概念<a name="ZH-CN_TOPIC_0000002441674813"></a> - 音频编解码协议 音频组件提供的编解码功能基于独立封装的AAC编解码库，核心编解码器工作在用户态，使用CPU软件编解码。 AAC编解码协议说明如[表1](#_Ref224548251)所示。 **表 1** 音频编解码协议说明 <a name="_Ref224548251"></a>
<table><thead align="left"><tr id="row261mcpsimp"><th class="cellrowborder" valign="top" width="10.341034103410342%" id="mcps1.2.8.1.1"><p id="p263mcpsimp"><a name="p263mcpsimp"></a><a name="p263mcpsimp"></a>协议</p>
</th>
<th class="cellrowborder" valign="top" width="9.86098609860986%" id="mcps1.2.8.1.2"><p id="p265mcpsimp"><a name="p265mcpsimp"></a><a name="p265mcpsimp"></a>采样率</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.8.1.3"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a>帧长（采样点）</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.8.1.4"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a>码率（kbps）</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.8.1.5"><p id="p272mcpsimp"><a name="p272mcpsimp"></a><a name="p272mcpsimp"></a>压缩率</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.8.1.6"><p id="p274mcpsimp"><a name="p274mcpsimp"></a><a name="p274mcpsimp"></a>CPU消耗</p>
</th>
<th class="cellrowborder" valign="top" width="31.313131313131308%" id="mcps1.2.8.1.7"><p id="p276mcpsimp"><a name="p276mcpsimp"></a><a name="p276mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row278mcpsimp"><td class="cellrowborder" valign="top" width="10.341034103410342%" headers="mcps1.2.8.1.1 "><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>AAC Encoder</p>
</td>
<td class="cellrowborder" valign="top" width="9.86098609860986%" headers="mcps1.2.8.1.2 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>8kHz，16kHz,22.05kHz,24kHz,32kHZ,</p>
<p id="p283mcpsimp"><a name="p283mcpsimp"></a><a name="p283mcpsimp"></a>44.1kHz,48kHz</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.8.1.3 "><a name="ul285mcpsimp"></a><a name="ul285mcpsimp"></a><ul id="ul285mcpsimp"><li>AACLC支持1024；</li><li>EAAC和EAACPLUS支持2048；</li><li>AACLD和AACELD支持512。</li></ul>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.4 "><p id="p290mcpsimp"><a name="p290mcpsimp"></a><a name="p290mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.5 "><p id="p292mcpsimp"><a name="p292mcpsimp"></a><a name="p292mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.6 "><p id="p294mcpsimp"><a name="p294mcpsimp"></a><a name="p294mcpsimp"></a>50 MHz</p>
</td>
<td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.2.8.1.7 "><p id="p296mcpsimp"><a name="p296mcpsimp"></a><a name="p296mcpsimp"></a>AAC有两次突破性的技术升级：</p>
<a name="ul297mcpsimp"></a><a name="ul297mcpsimp"></a><ul id="ul297mcpsimp"><li>aacPlus1（即EAAC），增加SBR(带宽扩展)技术，使得编解码器可以在比原来少一半的码率的条件下达到相同的音质。</li><li>aacPlus2（即EAACPLUS），增加PS(参数立体声)技术，在低码率情况下得到极佳的音质效果，aacPlus2可以在48kbit/s的速率下得到CD音质。</li><li>AAC-LD和AAC-ELD都为低时延语音编解码处理方案，其中AAC-LD为<em id="i301mcpsimp"><a name="i301mcpsimp"></a><a name="i301mcpsimp"></a>公共安全</em>行业标准需求，AAC-ELD为未来通讯使用编码格式。</li></ul>
<p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>码流范围与推荐码率设置如<a href="#_Ref342555172">表2</a>、<a href="#_Ref224621074">表3</a>所示。</p>
</td>
</tr>
<tr id="row305mcpsimp"><td class="cellrowborder" valign="top" width="10.341034103410342%" headers="mcps1.2.8.1.1 "><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>AAC Decoder</p>
</td>
<td class="cellrowborder" valign="top" width="9.86098609860986%" headers="mcps1.2.8.1.2 "><p id="p309mcpsimp"><a name="p309mcpsimp"></a><a name="p309mcpsimp"></a>兼容全部速率</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.8.1.3 "><p id="p311mcpsimp"><a name="p311mcpsimp"></a><a name="p311mcpsimp"></a>512、1024、2048</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.4 "><p id="p313mcpsimp"><a name="p313mcpsimp"></a><a name="p313mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.5 "><p id="p315mcpsimp"><a name="p315mcpsimp"></a><a name="p315mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.6 "><p id="p317mcpsimp"><a name="p317mcpsimp"></a><a name="p317mcpsimp"></a>25 MHz</p>
</td>
<td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.2.8.1.7 "><p id="p319mcpsimp"><a name="p319mcpsimp"></a><a name="p319mcpsimp"></a>后向兼容。传统AAC解码器，仅解码aac Plus v1码流低频信息，而aacPlus解码器则可以同时还原高频信息。不支持PS的AAC解码器，解码aac Plus v2码流时，仅能得到单声道信息，而aacPlus2解码器则可以得到立体声声音。注意：解码方式需要选用ADEC_MODE_STREAM。</p>
</td>
</tr>
</tbody>
</table> 注：“cpu消耗”的结果值基于ARM9 288MHz环境，2/2 MHz表示编码和解码分别占有2M和2M CPU。 **表 2** AAC Encoder各协议码率设置（码率单位为kbps） <a name="_Ref342555172"></a>
<table><thead align="left"><tr id="row332mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.9.1.1"><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>采样率</p>
</th>
<th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.9.1.2"><p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>声道</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.9.1.3"><p id="p338mcpsimp"><a name="p338mcpsimp"></a><a name="p338mcpsimp"></a>LC BitRate</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.9.1.4"><p id="p340mcpsimp"><a name="p340mcpsimp"></a><a name="p340mcpsimp"></a>Plus v1 BitRate</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.9.1.5"><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>Plus v2 BitRate</p>
</th>
</tr>
<tr id="row343mcpsimp"><th class="cellrowborder" valign="top" id="mcps1.2.9.2.1"><p id="p345mcpsimp"><a name="p345mcpsimp"></a><a name="p345mcpsimp"></a>Supported</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.2.2"><p id="p347mcpsimp"><a name="p347mcpsimp"></a><a name="p347mcpsimp"></a>Preferred</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.2.3"><p id="p349mcpsimp"><a name="p349mcpsimp"></a><a name="p349mcpsimp"></a>Supported</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.2.4"><p id="p351mcpsimp"><a name="p351mcpsimp"></a><a name="p351mcpsimp"></a>Preferred</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.2.5"><p id="p353mcpsimp"><a name="p353mcpsimp"></a><a name="p353mcpsimp"></a>Supported</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.2.6"><p id="p355mcpsimp"><a name="p355mcpsimp"></a><a name="p355mcpsimp"></a>Preferred</p>
</th>
</tr>
</thead>
<tbody><tr id="row357mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>8kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p361mcpsimp"><a name="p361mcpsimp"></a><a name="p361mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p363mcpsimp"><a name="p363mcpsimp"></a><a name="p363mcpsimp"></a>16～48</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p365mcpsimp"><a name="p365mcpsimp"></a><a name="p365mcpsimp"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p367mcpsimp"><a name="p367mcpsimp"></a><a name="p367mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p371mcpsimp"><a name="p371mcpsimp"></a><a name="p371mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p373mcpsimp"><a name="p373mcpsimp"></a><a name="p373mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row374mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p376mcpsimp"><a name="p376mcpsimp"></a><a name="p376mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p378mcpsimp"><a name="p378mcpsimp"></a><a name="p378mcpsimp"></a>16～96</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p380mcpsimp"><a name="p380mcpsimp"></a><a name="p380mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p386mcpsimp"><a name="p386mcpsimp"></a><a name="p386mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row389mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p391mcpsimp"><a name="p391mcpsimp"></a><a name="p391mcpsimp"></a>16kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p393mcpsimp"><a name="p393mcpsimp"></a><a name="p393mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p395mcpsimp"><a name="p395mcpsimp"></a><a name="p395mcpsimp"></a>24～96</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>24～48</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p405mcpsimp"><a name="p405mcpsimp"></a><a name="p405mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row406mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>24～192</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p412mcpsimp"><a name="p412mcpsimp"></a><a name="p412mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p414mcpsimp"><a name="p414mcpsimp"></a><a name="p414mcpsimp"></a>24～96</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p416mcpsimp"><a name="p416mcpsimp"></a><a name="p416mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p418mcpsimp"><a name="p418mcpsimp"></a><a name="p418mcpsimp"></a>16～48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p420mcpsimp"><a name="p420mcpsimp"></a><a name="p420mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row421mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p423mcpsimp"><a name="p423mcpsimp"></a><a name="p423mcpsimp"></a>22.05kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p425mcpsimp"><a name="p425mcpsimp"></a><a name="p425mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>32～132</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p429mcpsimp"><a name="p429mcpsimp"></a><a name="p429mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p431mcpsimp"><a name="p431mcpsimp"></a><a name="p431mcpsimp"></a>32～64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p433mcpsimp"><a name="p433mcpsimp"></a><a name="p433mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p435mcpsimp"><a name="p435mcpsimp"></a><a name="p435mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row438mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p440mcpsimp"><a name="p440mcpsimp"></a><a name="p440mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p442mcpsimp"><a name="p442mcpsimp"></a><a name="p442mcpsimp"></a>32～265</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p444mcpsimp"><a name="p444mcpsimp"></a><a name="p444mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p446mcpsimp"><a name="p446mcpsimp"></a><a name="p446mcpsimp"></a>32～128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p448mcpsimp"><a name="p448mcpsimp"></a><a name="p448mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p450mcpsimp"><a name="p450mcpsimp"></a><a name="p450mcpsimp"></a>16～64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p452mcpsimp"><a name="p452mcpsimp"></a><a name="p452mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row453mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p455mcpsimp"><a name="p455mcpsimp"></a><a name="p455mcpsimp"></a>24kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p457mcpsimp"><a name="p457mcpsimp"></a><a name="p457mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p459mcpsimp"><a name="p459mcpsimp"></a><a name="p459mcpsimp"></a>32～144</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p461mcpsimp"><a name="p461mcpsimp"></a><a name="p461mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p463mcpsimp"><a name="p463mcpsimp"></a><a name="p463mcpsimp"></a>32～64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p465mcpsimp"><a name="p465mcpsimp"></a><a name="p465mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row470mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p472mcpsimp"><a name="p472mcpsimp"></a><a name="p472mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p474mcpsimp"><a name="p474mcpsimp"></a><a name="p474mcpsimp"></a>32～288</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p476mcpsimp"><a name="p476mcpsimp"></a><a name="p476mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p478mcpsimp"><a name="p478mcpsimp"></a><a name="p478mcpsimp"></a>32～128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p480mcpsimp"><a name="p480mcpsimp"></a><a name="p480mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p482mcpsimp"><a name="p482mcpsimp"></a><a name="p482mcpsimp"></a>16～64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p484mcpsimp"><a name="p484mcpsimp"></a><a name="p484mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row485mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p487mcpsimp"><a name="p487mcpsimp"></a><a name="p487mcpsimp"></a>32kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p489mcpsimp"><a name="p489mcpsimp"></a><a name="p489mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p491mcpsimp"><a name="p491mcpsimp"></a><a name="p491mcpsimp"></a>32～192</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p493mcpsimp"><a name="p493mcpsimp"></a><a name="p493mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p495mcpsimp"><a name="p495mcpsimp"></a><a name="p495mcpsimp"></a>32～64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p499mcpsimp"><a name="p499mcpsimp"></a><a name="p499mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p501mcpsimp"><a name="p501mcpsimp"></a><a name="p501mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row502mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p504mcpsimp"><a name="p504mcpsimp"></a><a name="p504mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p506mcpsimp"><a name="p506mcpsimp"></a><a name="p506mcpsimp"></a>32～320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p508mcpsimp"><a name="p508mcpsimp"></a><a name="p508mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p510mcpsimp"><a name="p510mcpsimp"></a><a name="p510mcpsimp"></a>32～128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p512mcpsimp"><a name="p512mcpsimp"></a><a name="p512mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p514mcpsimp"><a name="p514mcpsimp"></a><a name="p514mcpsimp"></a>16～64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p516mcpsimp"><a name="p516mcpsimp"></a><a name="p516mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row517mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>44.1kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p521mcpsimp"><a name="p521mcpsimp"></a><a name="p521mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p523mcpsimp"><a name="p523mcpsimp"></a><a name="p523mcpsimp"></a>48～265</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p525mcpsimp"><a name="p525mcpsimp"></a><a name="p525mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p527mcpsimp"><a name="p527mcpsimp"></a><a name="p527mcpsimp"></a>32～64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p529mcpsimp"><a name="p529mcpsimp"></a><a name="p529mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p531mcpsimp"><a name="p531mcpsimp"></a><a name="p531mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p533mcpsimp"><a name="p533mcpsimp"></a><a name="p533mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row534mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p536mcpsimp"><a name="p536mcpsimp"></a><a name="p536mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p538mcpsimp"><a name="p538mcpsimp"></a><a name="p538mcpsimp"></a>48～320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p540mcpsimp"><a name="p540mcpsimp"></a><a name="p540mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>32～128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p546mcpsimp"><a name="p546mcpsimp"></a><a name="p546mcpsimp"></a>16～64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p548mcpsimp"><a name="p548mcpsimp"></a><a name="p548mcpsimp"></a>48</p>
</td>
</tr>
<tr id="row549mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p551mcpsimp"><a name="p551mcpsimp"></a><a name="p551mcpsimp"></a>48kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p553mcpsimp"><a name="p553mcpsimp"></a><a name="p553mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p555mcpsimp"><a name="p555mcpsimp"></a><a name="p555mcpsimp"></a>48～288</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p559mcpsimp"><a name="p559mcpsimp"></a><a name="p559mcpsimp"></a>32～64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p561mcpsimp"><a name="p561mcpsimp"></a><a name="p561mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p563mcpsimp"><a name="p563mcpsimp"></a><a name="p563mcpsimp"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p565mcpsimp"><a name="p565mcpsimp"></a><a name="p565mcpsimp"></a>—</p>
</td>
</tr>
<tr id="row566mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p568mcpsimp"><a name="p568mcpsimp"></a><a name="p568mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p570mcpsimp"><a name="p570mcpsimp"></a><a name="p570mcpsimp"></a>48～320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p572mcpsimp"><a name="p572mcpsimp"></a><a name="p572mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p574mcpsimp"><a name="p574mcpsimp"></a><a name="p574mcpsimp"></a>32～128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p576mcpsimp"><a name="p576mcpsimp"></a><a name="p576mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p578mcpsimp"><a name="p578mcpsimp"></a><a name="p578mcpsimp"></a>16～64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p580mcpsimp"><a name="p580mcpsimp"></a><a name="p580mcpsimp"></a>48</p>
</td>
</tr>
</tbody>
</table> 注：“—”表示不支持这种情况。 **表 3** AAC Encoder Low Delay协议码率设置（码率单位为kbps） <a name="_Ref224621074"></a>
<table><thead align="left"><tr id="row592mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.7.1.1"><p id="p594mcpsimp"><a name="p594mcpsimp"></a><a name="p594mcpsimp"></a>采样率</p>
</th>
<th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.7.1.2"><p id="p596mcpsimp"><a name="p596mcpsimp"></a><a name="p596mcpsimp"></a>声道</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.7.1.3"><p id="p598mcpsimp"><a name="p598mcpsimp"></a><a name="p598mcpsimp"></a>LD BitRate</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.7.1.4"><p id="p600mcpsimp"><a name="p600mcpsimp"></a><a name="p600mcpsimp"></a>ELD BitRate</p>
</th>
</tr>
<tr id="row601mcpsimp"><th class="cellrowborder" valign="top" id="mcps1.2.7.2.1"><p id="p603mcpsimp"><a name="p603mcpsimp"></a><a name="p603mcpsimp"></a>Supported</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.7.2.2"><p id="p605mcpsimp"><a name="p605mcpsimp"></a><a name="p605mcpsimp"></a>Preferred</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.7.2.3"><p id="p607mcpsimp"><a name="p607mcpsimp"></a><a name="p607mcpsimp"></a>Supported</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.7.2.4"><p id="p609mcpsimp"><a name="p609mcpsimp"></a><a name="p609mcpsimp"></a>Preferred</p>
</th>
</tr>
</thead>
<tbody><tr id="row611mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p613mcpsimp"><a name="p613mcpsimp"></a><a name="p613mcpsimp"></a>8kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p615mcpsimp"><a name="p615mcpsimp"></a><a name="p615mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p617mcpsimp"><a name="p617mcpsimp"></a><a name="p617mcpsimp"></a>16~96</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p619mcpsimp"><a name="p619mcpsimp"></a><a name="p619mcpsimp"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p621mcpsimp"><a name="p621mcpsimp"></a><a name="p621mcpsimp"></a>32~96</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p623mcpsimp"><a name="p623mcpsimp"></a><a name="p623mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row624mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p626mcpsimp"><a name="p626mcpsimp"></a><a name="p626mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p628mcpsimp"><a name="p628mcpsimp"></a><a name="p628mcpsimp"></a>16~192</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p630mcpsimp"><a name="p630mcpsimp"></a><a name="p630mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p632mcpsimp"><a name="p632mcpsimp"></a><a name="p632mcpsimp"></a>64~192</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p634mcpsimp"><a name="p634mcpsimp"></a><a name="p634mcpsimp"></a>64</p>
</td>
</tr>
<tr id="row635mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p637mcpsimp"><a name="p637mcpsimp"></a><a name="p637mcpsimp"></a>16kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p639mcpsimp"><a name="p639mcpsimp"></a><a name="p639mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a>24~192</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>16~256</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>48</p>
</td>
</tr>
<tr id="row648mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p650mcpsimp"><a name="p650mcpsimp"></a><a name="p650mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p652mcpsimp"><a name="p652mcpsimp"></a><a name="p652mcpsimp"></a>32~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p654mcpsimp"><a name="p654mcpsimp"></a><a name="p654mcpsimp"></a>96</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p656mcpsimp"><a name="p656mcpsimp"></a><a name="p656mcpsimp"></a>32~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p658mcpsimp"><a name="p658mcpsimp"></a><a name="p658mcpsimp"></a>96</p>
</td>
</tr>
<tr id="row659mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p661mcpsimp"><a name="p661mcpsimp"></a><a name="p661mcpsimp"></a>22.05kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p663mcpsimp"><a name="p663mcpsimp"></a><a name="p663mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p665mcpsimp"><a name="p665mcpsimp"></a><a name="p665mcpsimp"></a>32~256</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p667mcpsimp"><a name="p667mcpsimp"></a><a name="p667mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p669mcpsimp"><a name="p669mcpsimp"></a><a name="p669mcpsimp"></a>24~256</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p671mcpsimp"><a name="p671mcpsimp"></a><a name="p671mcpsimp"></a>48</p>
</td>
</tr>
<tr id="row672mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p674mcpsimp"><a name="p674mcpsimp"></a><a name="p674mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p676mcpsimp"><a name="p676mcpsimp"></a><a name="p676mcpsimp"></a>48~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p678mcpsimp"><a name="p678mcpsimp"></a><a name="p678mcpsimp"></a>96</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p680mcpsimp"><a name="p680mcpsimp"></a><a name="p680mcpsimp"></a>32~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p682mcpsimp"><a name="p682mcpsimp"></a><a name="p682mcpsimp"></a>96</p>
</td>
</tr>
<tr id="row683mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p685mcpsimp"><a name="p685mcpsimp"></a><a name="p685mcpsimp"></a>24kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p687mcpsimp"><a name="p687mcpsimp"></a><a name="p687mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p689mcpsimp"><a name="p689mcpsimp"></a><a name="p689mcpsimp"></a>32~256</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p691mcpsimp"><a name="p691mcpsimp"></a><a name="p691mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p693mcpsimp"><a name="p693mcpsimp"></a><a name="p693mcpsimp"></a>24~256</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p695mcpsimp"><a name="p695mcpsimp"></a><a name="p695mcpsimp"></a>64</p>
</td>
</tr>
<tr id="row696mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p698mcpsimp"><a name="p698mcpsimp"></a><a name="p698mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p700mcpsimp"><a name="p700mcpsimp"></a><a name="p700mcpsimp"></a>48~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p702mcpsimp"><a name="p702mcpsimp"></a><a name="p702mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p704mcpsimp"><a name="p704mcpsimp"></a><a name="p704mcpsimp"></a>32~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p706mcpsimp"><a name="p706mcpsimp"></a><a name="p706mcpsimp"></a>128</p>
</td>
</tr>
<tr id="row707mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p709mcpsimp"><a name="p709mcpsimp"></a><a name="p709mcpsimp"></a>32kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p711mcpsimp"><a name="p711mcpsimp"></a><a name="p711mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p713mcpsimp"><a name="p713mcpsimp"></a><a name="p713mcpsimp"></a>48~320</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p715mcpsimp"><a name="p715mcpsimp"></a><a name="p715mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p717mcpsimp"><a name="p717mcpsimp"></a><a name="p717mcpsimp"></a>32~320</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p719mcpsimp"><a name="p719mcpsimp"></a><a name="p719mcpsimp"></a>64</p>
</td>
</tr>
<tr id="row720mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p722mcpsimp"><a name="p722mcpsimp"></a><a name="p722mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p724mcpsimp"><a name="p724mcpsimp"></a><a name="p724mcpsimp"></a>64~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p726mcpsimp"><a name="p726mcpsimp"></a><a name="p726mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p728mcpsimp"><a name="p728mcpsimp"></a><a name="p728mcpsimp"></a>64~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p730mcpsimp"><a name="p730mcpsimp"></a><a name="p730mcpsimp"></a>128</p>
</td>
</tr>
<tr id="row731mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p733mcpsimp"><a name="p733mcpsimp"></a><a name="p733mcpsimp"></a>44.1kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p735mcpsimp"><a name="p735mcpsimp"></a><a name="p735mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p737mcpsimp"><a name="p737mcpsimp"></a><a name="p737mcpsimp"></a>64~320</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p739mcpsimp"><a name="p739mcpsimp"></a><a name="p739mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p741mcpsimp"><a name="p741mcpsimp"></a><a name="p741mcpsimp"></a>96~320</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p743mcpsimp"><a name="p743mcpsimp"></a><a name="p743mcpsimp"></a>128</p>
</td>
</tr>
<tr id="row744mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p746mcpsimp"><a name="p746mcpsimp"></a><a name="p746mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>44~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p750mcpsimp"><a name="p750mcpsimp"></a><a name="p750mcpsimp"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p752mcpsimp"><a name="p752mcpsimp"></a><a name="p752mcpsimp"></a>192~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p754mcpsimp"><a name="p754mcpsimp"></a><a name="p754mcpsimp"></a>256</p>
</td>
</tr>
<tr id="row755mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11.111111111111112%" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p757mcpsimp"><a name="p757mcpsimp"></a><a name="p757mcpsimp"></a>48kHz</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p759mcpsimp"><a name="p759mcpsimp"></a><a name="p759mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p761mcpsimp"><a name="p761mcpsimp"></a><a name="p761mcpsimp"></a>64~320</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p763mcpsimp"><a name="p763mcpsimp"></a><a name="p763mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p765mcpsimp"><a name="p765mcpsimp"></a><a name="p765mcpsimp"></a>96~320</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p767mcpsimp"><a name="p767mcpsimp"></a><a name="p767mcpsimp"></a>128</p>
</td>
</tr>
<tr id="row768mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p770mcpsimp"><a name="p770mcpsimp"></a><a name="p770mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p772mcpsimp"><a name="p772mcpsimp"></a><a name="p772mcpsimp"></a>64~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p774mcpsimp"><a name="p774mcpsimp"></a><a name="p774mcpsimp"></a>256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p776mcpsimp"><a name="p776mcpsimp"></a><a name="p776mcpsimp"></a>192~320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p778mcpsimp"><a name="p778mcpsimp"></a><a name="p778mcpsimp"></a>256</p>
</td>
</tr>
</tbody>
</table> - 音频编解码集成接口 SDK发布包中开放接口用于注册和注销编码器和解码器，音频组件根据这些接口，提供了注册AAC编解码器的示例。用户既可以参考示例，注册自有的第三方编解码器，也可直接使用音频组件提供的示例来注册并使用组件中的AAC编解码器。 【注意】 - AAC编解码器的使用支持静态库注册的形式，相关库包括libaac\_comm.a、libaac\_enc.a、libaac\_sbr\_enc.a、libaac\_dec.a、libaac\_sbr\_dec.a。其中，libaac\_sbr\_enc.a在AAC编码器不使用EAAC、EAACPLUS、AACELD类型编码时可裁剪；libaac\_sbr\_dec.a在AAC解码器不使用EAAC、EAACPLUS、AACELD类型解码时可裁剪。当使用EAAC、EAACPLUS、AACELD编解码类型时，须在注册编解码器之前进行SBRENC、SBRDEC功能模块的静态注册。
- AAC编解码器的使用还支持动态库调用的形式，相关库包括libaac\_comm.so、libaac\_enc.so、libaac\_sbr\_enc.so、libaac\_dec.so、libaac\_sbr\_dec.so。其中，libaac\_sbr\_enc.so在AAC编码器不使用EAAC、EAACPLUS、AACELD类型编码时可裁剪；libaac\_sbr\_dec.so在AAC解码器不使用EAAC、EAACPLUS、AACELD类型解码时可裁剪。
- AAC编解码器不支持同时使用静态库注册和动态库调用。
- AAC编解码器的静态库注册只允许成功调用一次，不支持重复注册。 【举例】 下面的代码实现静态注册AAC的SBRENC和SBRDEC模块。 ```
td_s32 ret; td_void* sbr_enc_handle = ss_aac_sbrenc_get_handle;
/* register SBRENC module. */
ret = ss_aacenc_register_mod(sbr_enc_handle); if (ret != TD_SUCCESS) { printf("[func]:%s [line]:%d [info]:%s\n", __FUNCTION__, __LINE__, "init sbr_enc lib fail!\n"); return OT_ERR_AENC_NOT_SUPPORT;
} td_void* sbr_dec_handle = ss_aac_sbrdec_get_handle;
/* register SBRDEC module. */
ret = ss_aacdec_register_mod(sbr_dec_handle); if (ret != TD_SUCCESS) { printf("[func]:%s [line]:%d [info]:%s\n", __FUNCTION__, __LINE__, "init sbr_dec lib fail!\n"); return OT_ERR_ADEC_NOT_SUPPORT;
}
``` ## API参考<a name="ZH-CN_TOPIC_0000002441714649"></a> SDK发布包中的以下API用于注册和注销编码器和解码器。 - [ss\_mpi\_aenc\_register\_encoder](#ZH-CN_TOPIC_0000002408115490)：注册编码器。
- [ss\_mpi\_aenc\_unregister\_encoder](#ZH-CN_TOPIC_0000002441714653)：注销编码器。
- [ss\_mpi\_adec\_register\_decoder](#ZH-CN_TOPIC_0000002408115474)：注册解码器。
- [ss\_mpi\_adec\_unregister\_decoder](#ZH-CN_TOPIC_0000002408275418)：注销解码器。 音频组件中提供的注册示例： - [ss\_mpi\_aenc\_aac\_init](#ZH-CN_TOPIC_0000002408275398)：注册AAC编码器。
- [ss\_mpi\_adec\_aac\_init](#ZH-CN_TOPIC_0000002441714637)：注册AAC解码器。 ### ss\_mpi\_aenc\_register\_encoder<a name="ZH-CN_TOPIC_0000002408115490"></a> 【描述】 注册编码器。 【语法】 ```
td_s32 ss_mpi_aenc_register_encoder(td_s32 *handle, const ot_aenc_encoder *encoder);
``` 【参数】 <a name="table837mcpsimp"></a>
<table><thead align="left"><tr id="row843mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.1.4.1.2"><p id="p847mcpsimp"><a name="p847mcpsimp"></a><a name="p847mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.4.1.3"><p id="p849mcpsimp"><a name="p849mcpsimp"></a><a name="p849mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row851mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p853mcpsimp"><a name="p853mcpsimp"></a><a name="p853mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.4.1.2 "><p id="p855mcpsimp"><a name="p855mcpsimp"></a><a name="p855mcpsimp"></a>注册句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p857mcpsimp"><a name="p857mcpsimp"></a><a name="p857mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row858mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p860mcpsimp"><a name="p860mcpsimp"></a><a name="p860mcpsimp"></a>encoder</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.4.1.2 "><p id="p862mcpsimp"><a name="p862mcpsimp"></a><a name="p862mcpsimp"></a>编码器属性结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p864mcpsimp"><a name="p864mcpsimp"></a><a name="p864mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table> 【返回值】 <a name="table866mcpsimp"></a>
<table><thead align="left"><tr id="row871mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p873mcpsimp"><a name="p873mcpsimp"></a><a name="p873mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p875mcpsimp"><a name="p875mcpsimp"></a><a name="p875mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row877mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p879mcpsimp"><a name="p879mcpsimp"></a><a name="p879mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p881mcpsimp"><a name="p881mcpsimp"></a><a name="p881mcpsimp"></a>成功。</p>
</td>
</tr>
</tbody>
</table> 【需求】 - 头文件：ot\_comm\_aenc.h、ss\_mpi\_audio.h
- 库文件：libss\_mpi.a 【注意】 - 用户通过传入编码器属性结构体，向AENC模块注册一个编码器，并返回注册句柄，用户可以最后通过注册句柄来注销该编码器。
- AENC模块最大可注册20个编码器，且自身已注册LPCM、G711a、G711u、G726、ADPCM五个编码器。
- 同一种编码协议不允许重复注册编码器，例如假如已注册AAC编码器，不允许另外再注册一个AAC编码器。
- 编码器属性包括编码器类型、最大码流长度、编码器名称、打开编码器的函数指针、进行编码的函数指针、关闭编码器的函数指针。 - 编码器类型 SDK以枚举标识编码协议，注册时应选择相关协议的编码器类型。 - 最大码流长度 每帧编码后码流的最大长度，AENC模块将根据注册的最大码流长度分配内存大小。 - 编码器名称 编码器名称用字符串表示，用于在proc信息中显示。 - 打开编码器的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_open\_encoder\)\(td\_void \*encoder\_attr, td\_void \*\*encoder\); 其中第一个参数是编码器属性，用于传入不同类型的编码器的特定属性；第二个参数是编码器句柄，用于返回可用于操作编码器的句柄。这两个参数均由用户封装，用户封装第二个参数时需要注意分配内存，因为编码器句柄还将用于编码和关闭编码器。 - 进行编码的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_enc\_frame\)\(td\_void \*encoder, const ot\_audio\_frame \*data, td\_u8 \*out\_buf, td\_u32 \*out\_len\); 第一个参数是上一个函数打开编码器时返回的编码器句柄；第二个参数是SDK的音频帧数据结构体的指针，用于传入音频帧数据；第三个参数是输出缓存指针；第四个参数是输出缓存长度。 - 关闭编码器的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_close\_encoder\)\(td\_void \*encoder\); 参数是打开编码器时返回的编码器句柄。 - 用户需根据这几个函数原型封装第三方编码器，并通过编码器属性结构体注册给AENC模块，从而实现第三方编码器的集成。 - 必须在创建编码通道前注册相关类型的编码器，编码器不需要重复注册。 【举例】 下面的代码举例AAC编码器的注册： ```
td_s32 handle, ret;
aenc_encoder aac; ret = aac_init_enc_lib;
if (ret) { return ret;
} aac.type = OT_PT_AAC;
snprintf(aac.name, sizeof(aac.name), "aac");
aac.max_frame_len = MAX_AAC_MAINBUF_SIZE;
aac.func_open_encoder = open_aac_encoder;
aac.func_enc_frame = encode_aac_frm;
aac.func_close_encoder = close_aac_encoder;
ret = ss_mpi_aenc_register_encoder(&handle, &aac);
if (ret) { return ret;
} return TD_SUCCESS;
``` 【相关主题】 无。 ### ss\_mpi\_aenc\_unregister\_encoder<a name="ZH-CN_TOPIC_0000002441714653"></a> 【描述】 注销解码器。 【语法】 ```
td_s32 ss_mpi_aenc_unregister_encoder(td_s32 handle);
``` 【参数】 <a name="table947mcpsimp"></a>
<table><thead align="left"><tr id="row953mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p955mcpsimp"><a name="p955mcpsimp"></a><a name="p955mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="66.34%" id="mcps1.1.4.1.2"><p id="p957mcpsimp"><a name="p957mcpsimp"></a><a name="p957mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.1.4.1.3"><p id="p959mcpsimp"><a name="p959mcpsimp"></a><a name="p959mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row961mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p963mcpsimp"><a name="p963mcpsimp"></a><a name="p963mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="66.34%" headers="mcps1.1.4.1.2 "><p id="p965mcpsimp"><a name="p965mcpsimp"></a><a name="p965mcpsimp"></a>注册句柄（注册编码器时获得的句柄）。</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.1.4.1.3 "><p id="p967mcpsimp"><a name="p967mcpsimp"></a><a name="p967mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table> 【返回值】 <a name="table969mcpsimp"></a>
<table><thead align="left"><tr id="row974mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p976mcpsimp"><a name="p976mcpsimp"></a><a name="p976mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p978mcpsimp"><a name="p978mcpsimp"></a><a name="p978mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row980mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p982mcpsimp"><a name="p982mcpsimp"></a><a name="p982mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p984mcpsimp"><a name="p984mcpsimp"></a><a name="p984mcpsimp"></a>成功。</p>
</td>
</tr>
</tbody>
</table> 【需求】 - 头文件：ot\_comm\_aenc.h、ss\_mpi\_audio.h
- 库文件：libss\_mpi.a 【注意】 通常不需要注销编码器。 【举例】 无 【相关主题】 无 ### ss\_mpi\_adec\_register\_decoder<a name="ZH-CN_TOPIC_0000002408115474"></a> 【描述】 注册解码器。 【语法】 ```
td_s32 ss_mpi_adec_register_decoder(td_s32 *handle, const ot_adec_decoder *decoder);
``` 【参数】 <a name="table1010mcpsimp"></a>
<table><thead align="left"><tr id="row1016mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.1"><p id="p1018mcpsimp"><a name="p1018mcpsimp"></a><a name="p1018mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.4.1.2"><p id="p1020mcpsimp"><a name="p1020mcpsimp"></a><a name="p1020mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p1022mcpsimp"><a name="p1022mcpsimp"></a><a name="p1022mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1024mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p1026mcpsimp"><a name="p1026mcpsimp"></a><a name="p1026mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p1028mcpsimp"><a name="p1028mcpsimp"></a><a name="p1028mcpsimp"></a>注册句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p1030mcpsimp"><a name="p1030mcpsimp"></a><a name="p1030mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row1031mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p1033mcpsimp"><a name="p1033mcpsimp"></a><a name="p1033mcpsimp"></a>decoder</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p1035mcpsimp"><a name="p1035mcpsimp"></a><a name="p1035mcpsimp"></a>解码器属性结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p1037mcpsimp"><a name="p1037mcpsimp"></a><a name="p1037mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table> 【返回值】 <a name="table1039mcpsimp"></a>
<table><thead align="left"><tr id="row1044mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1046mcpsimp"><a name="p1046mcpsimp"></a><a name="p1046mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1048mcpsimp"><a name="p1048mcpsimp"></a><a name="p1048mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1050mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1052mcpsimp"><a name="p1052mcpsimp"></a><a name="p1052mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1054mcpsimp"><a name="p1054mcpsimp"></a><a name="p1054mcpsimp"></a>成功。</p>
</td>
</tr>
</tbody>
</table> 【需求】 - 头文件：ot\_comm\_adec.h、ss\_mpi\_audio.h
- 库文件：libss\_mpi.a 【注意】 - 用户通过传入解码器属性结构体，向ADEC模块注册一个解码器，并返回注册句柄，用户可以最后通过注册句柄来注销该解码器。
- ADEC模块最大可注册20个解码器，且自身已注册LPCM、G711a、G711u、G726、ADPCM五个解码器。
- 同一种解码协议不允许重复注册解码器，例如假如已注册AAC解码器，不允许另外再注册一个AAC解码器。
- 解码器属性包括解码器类型、解码器名称、打开解码器的函数指针、进行解码的函数指针、获取音频帧信息的函数指针、关闭解码器的函数指针。 - 解码器类型 SDK以枚举标识解码协议，注册时应选择相关协议的解码器类型。 - 解码器名称 解码器名称用字符串表示，用于在proc信息中显示。 - 打开解码器的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_open\_decoder\)\(td\_void \*decoder\_attr, td\_void \*\*decoder\)；其中第一个参数是解码器属性，用于传入不同类型的解码器的特定属性；第二个参数是解码器句柄，用于返回可用于操作解码器的句柄。这两个参数均由用户封装，用户封装第二个参数时需要注意分配内存，因为解码器句柄还将用于解码和关闭解码器。 - 进行解码的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_dec\_frame\)\(td\_void \*decoder, td\_u8 \*\*in\_buf, td\_s32 \*left\_byte, td\_u16 \*out\_buf, td\_u32 \*out\_len, td\_u32 \*chns\)；第一个参数是上一个函数打开解码器时返回的解码器句柄；第二个参数是输入缓存，用于传入音频帧数据；第三个参数用于返回剩余字节数，用于流式解码，即每次送入的音频帧数据不是完整的一帧的情形；第四个参数是输出缓存；第五个参数是输出数据的单声道长度；第六个参数是输出的通道数，码流数据经解码后，可能输出单声道，也可能输出立体声。 - 获取音频帧信息的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_get\_frame\_info\)\(td\_void \*decoder, td\_void \*info\)；第一个参数是打开解码器时返回的解码器句柄；第二个参数是用户封装的音频帧信息，有的解码器解析码流时会获取解码后音频数据的采样点、采样率等信息；如果用户解码器不需要此函数，可以为该函数原型封装一个空函数。 - 关闭解码器的函数指针 SDK封装的一个函数指针，其函数原型为： td\_s32 \(\*func\_close\_decoder\)\(td\_void \*decoder\)；参数是打开解码器时返回的解码器句柄。 - 用户需根据这几个函数原型封装第三方解码器，并通过解码器属性结构体注册给ADEC模块，从而实现第三方解码器的集成。 - 必须在创建解码通道前注册相关类型的解码器，解码器不需要重复注册。 【举例】 下面的代码举例AAC解码器的注册： ```
td_s32 handle, ret;
adec_decoder aac; ret = aac_init_dec_lib;
if (ret) { return ret;
} aac.type = OT_PT_AAC;
snprintf(aac.name, sizeof(aac.name), "aac");
aac.func_open_decoder = open_aac_decoder;
aac.func_dec_frame = decode_aac_frm;
aac.func_get_frame_info = get_aac_frm_info;
aac.func_close_decoder = close_aac_decoder;
aac.func_reset_decoder = reset_aac_decoder;
ret = ss_mpi_adec_register_decoder(&handle, &aac);
if (ret) { return ret;
} return TD_SUCCESS;
``` 【相关主题】 无。 ### ss\_mpi\_adec\_unregister\_decoder<a name="ZH-CN_TOPIC_0000002408275418"></a> 【描述】 注销解码器。 【语法】 ```
td_s32 ss_mpi_adec_unregister_decoder(td_s32 handle);
``` 【参数】 <a name="table1119mcpsimp"></a>
<table><thead align="left"><tr id="row1125mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p1127mcpsimp"><a name="p1127mcpsimp"></a><a name="p1127mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="66.34%" id="mcps1.1.4.1.2"><p id="p1129mcpsimp"><a name="p1129mcpsimp"></a><a name="p1129mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.1.4.1.3"><p id="p1131mcpsimp"><a name="p1131mcpsimp"></a><a name="p1131mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1133mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p1135mcpsimp"><a name="p1135mcpsimp"></a><a name="p1135mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="66.34%" headers="mcps1.1.4.1.2 "><p id="p1137mcpsimp"><a name="p1137mcpsimp"></a><a name="p1137mcpsimp"></a>注册句柄（注册解码器时获得的句柄）。</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.1.4.1.3 "><p id="p1139mcpsimp"><a name="p1139mcpsimp"></a><a name="p1139mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table> 【返回值】 <a name="table1141mcpsimp"></a>
<table><thead align="left"><tr id="row1146mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1148mcpsimp"><a name="p1148mcpsimp"></a><a name="p1148mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1150mcpsimp"><a name="p1150mcpsimp"></a><a name="p1150mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1152mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1154mcpsimp"><a name="p1154mcpsimp"></a><a name="p1154mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1156mcpsimp"><a name="p1156mcpsimp"></a><a name="p1156mcpsimp"></a>成功。</p>
</td>
</tr>
</tbody>
</table> 【需求】 - 头文件：ot\_comm\_adec.h、ss\_mpi\_audio.h
- 库文件：libss\_mpi.a 【注意】 通常不需要注销解码器。 【举例】 无 【相关主题】 无。 ### ss\_mpi\_aenc\_aac\_init<a name="ZH-CN_TOPIC_0000002408275398"></a> 【描述】 注册AAC编码器。 【语法】 ```
td_s32 ss_mpi_aenc_aac_init(td_void);
``` 【参数】 无 【返回值】 <a name="table1182mcpsimp"></a>
<table><thead align="left"><tr id="row1187mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1189mcpsimp"><a name="p1189mcpsimp"></a><a name="p1189mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1191mcpsimp"><a name="p1191mcpsimp"></a><a name="p1191mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1193mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1195mcpsimp"><a name="p1195mcpsimp"></a><a name="p1195mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1197mcpsimp"><a name="p1197mcpsimp"></a><a name="p1197mcpsimp"></a>成功。</p>
</td>
</tr>
</tbody>
</table> 【需求】 - 源文件：audio\_aac\_adp.c
- 头文件：audio\_aac\_adp.h
- 库文件：libaac\_comm.so、libaac\_enc.so 【注意】 此接口在audio\_aac\_adp.c里实现，而audio\_aac\_adp.c并没有封装成库，所以在使用此接口时，需要包含audio\_aac\_adp.c和audio\_aac\_adp.h才能编译通过。这两个文件默认放置在sample/audio/adp文件夹中。此外，在需要使用到SBRENC功能时，需要添加libaac\_sbr\_enc.so库。 【举例】 无。 【相关主题】 无。 ### ss\_mpi\_adec\_aac\_init<a name="ZH-CN_TOPIC_0000002441714637"></a> 【描述】 注册AAC解码器。 【语法】 ```
td_s32 ss_mpi_adec_aac_init(td_void);
``` 【参数】 无 【返回值】 <a name="table1224mcpsimp"></a>
<table><thead align="left"><tr id="row1229mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1231mcpsimp"><a name="p1231mcpsimp"></a><a name="p1231mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1233mcpsimp"><a name="p1233mcpsimp"></a><a name="p1233mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1235mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1237mcpsimp"><a name="p1237mcpsimp"></a><a name="p1237mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1239mcpsimp"><a name="p1239mcpsimp"></a><a name="p1239mcpsimp"></a>成功。</p>
</td>
</tr>
</tbody>
</table> 【需求】 - 源文件：aduio\_aac\_adp.h
- 头文件：audio\_aac\_adp.h
- 库文件：libaac\_comm.so、libaac\_dec.so 【注意】 请参考ss\_mpi\_aenc\_aac\_init接口注意项的说明。此外，在需要使用到SBRDEC功能时，需要添加libaac\_sbr\_dec.so库。 【举例】 无。 【相关主题】 无。 ## 数据类型<a name="ZH-CN_TOPIC_0000002441674769"></a> 音频组件相关数据类型、数据结构定义如下： - [ot\_aenc\_encoder](#ZH-CN_TOPIC_0000002408275394)：定义编码器属性结构体。
- [ot\_adec\_decoder](#ZH-CN_TOPIC_0000002441714629)：定义解码器属性结构体。
- [ot\_aac\_type](#ZH-CN_TOPIC_0000002441674777)：定义AAC音频编解码协议类型。
- [ot\_aac\_bps](#ZH-CN_TOPIC_0000002408275382)：定义AAC音频编码码率。
- [ot\_aac\_transport\_type](#ZH-CN_TOPIC_0000002408115466)：定义AAC音频编解码协议传输封装类型。
- [ot\_aenc\_attr\_aac](#ZH-CN_TOPIC_0000002408115470)：定义AAC编码协议属性结构体。
- [ot\_adec\_attr\_aac](#ZH-CN_TOPIC_0000002441714625)：定义AAC解码协议属性结构体。 ### ot\_aenc\_encoder<a name="ZH-CN_TOPIC_0000002408275394"></a> 【说明】 定义编码器属性结构体。 【定义】 ```
typedef struct { ot_payload_type type; td_u32 max_frame_len; ot_char name[OT_MAX_ENCODER_NAME_LEN]; /* encoder type,be used to print proc information */ td_s32 (*func_open_encoder)(td_void *encoder_attr, td_void **encoder); /* encoder is the handle to control the encoder */ td_s32 (*func_enc_frame)(td_void *encoder, const ot_audio_frame *data, td_u8 *out_buf, td_u32 *out_len); td_s32 (*func_close_encoder)(td_void *encoder);
} ot_aenc_encoder;
``` 【成员】 <a name="table1290mcpsimp"></a>
<table><thead align="left"><tr id="row1295mcpsimp"><th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.1"><p id="p1297mcpsimp"><a name="p1297mcpsimp"></a><a name="p1297mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.2"><p id="p1299mcpsimp"><a name="p1299mcpsimp"></a><a name="p1299mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1301mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1303mcpsimp"><a name="p1303mcpsimp"></a><a name="p1303mcpsimp"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1305mcpsimp"><a name="p1305mcpsimp"></a><a name="p1305mcpsimp"></a>编码协议类型，见《MPP 媒体处理软件V5.0 开发参考》“2.系统控制”章节。</p>
</td>
</tr>
<tr id="row1306mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1308mcpsimp"><a name="p1308mcpsimp"></a><a name="p1308mcpsimp"></a>max_frame_len</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1310mcpsimp"><a name="p1310mcpsimp"></a><a name="p1310mcpsimp"></a>最大码流长度。</p>
</td>
</tr>
<tr id="row1311mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1313mcpsimp"><a name="p1313mcpsimp"></a><a name="p1313mcpsimp"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="fr-FR" id="p1315mcpsimp"><a name="p1315mcpsimp"></a><a name="p1315mcpsimp"></a><span xml:lang="en-US" id="ph1316mcpsimp"><a name="ph1316mcpsimp"></a><a name="ph1316mcpsimp"></a>编码器名称。</span>OT_MAX_ENCODER_NAME_LEN定义<span xml:lang="en-US" id="ph1317mcpsimp"><a name="ph1317mcpsimp"></a><a name="ph1317mcpsimp"></a>见《</span>MPP <span xml:lang="en-US" id="ph1318mcpsimp"><a name="ph1318mcpsimp"></a><a name="ph1318mcpsimp"></a>媒体处理软件</span>V5.0 <span xml:lang="en-US" id="ph1319mcpsimp"><a name="ph1319mcpsimp"></a><a name="ph1319mcpsimp"></a>开发参考》</span>“<span xml:lang="en-US" id="ph1320mcpsimp"><a name="ph1320mcpsimp"></a><a name="ph1320mcpsimp"></a>音频</span>”<span xml:lang="en-US" id="ph1321mcpsimp"><a name="ph1321mcpsimp"></a><a name="ph1321mcpsimp"></a>章节。</span></p>
</td>
</tr>
<tr id="row1322mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1324mcpsimp"><a name="p1324mcpsimp"></a><a name="p1324mcpsimp"></a>func_open_encoder</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1326mcpsimp"><a name="p1326mcpsimp"></a><a name="p1326mcpsimp"></a>打开编码器的函数指针。</p>
</td>
</tr>
<tr id="row1327mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1329mcpsimp"><a name="p1329mcpsimp"></a><a name="p1329mcpsimp"></a>func_enc_frame</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1331mcpsimp"><a name="p1331mcpsimp"></a><a name="p1331mcpsimp"></a>进行编码的函数指针<span xml:lang="fr-FR" id="ph1332mcpsimp"><a name="ph1332mcpsimp"></a><a name="ph1332mcpsimp"></a>。详细描述请参</span>见《MPP 媒体处理软件V5.0 开发参考》<span xml:lang="fr-FR" id="ph1333mcpsimp"><a name="ph1333mcpsimp"></a><a name="ph1333mcpsimp"></a>“音频”</span>章节。</p>
</td>
</tr>
<tr id="row1334mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1336mcpsimp"><a name="p1336mcpsimp"></a><a name="p1336mcpsimp"></a>func_close_encoder</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1338mcpsimp"><a name="p1338mcpsimp"></a><a name="p1338mcpsimp"></a>关闭编码器的函数指针。</p>
</td>
</tr>
</tbody>
</table> 【注意事项】 无。 【相关数据类型及接口】 [ss\_mpi\_aenc\_register\_encoder](#ZH-CN_TOPIC_0000002408115490) ### ot\_adec\_decoder<a name="ZH-CN_TOPIC_0000002441714629"></a> 【说明】 定义解码器属性结构体。 **【**定义**】** ```
typedef struct { ot_payload_type type; ot_char name[OT_MAX_DECODER_NAME_LEN]; td_s32 (*func_open_decoder)(td_void *decoder_attr, td_void **decoder); /* struct decoder is packed by user, user malloc and free memory for this struct */ td_s32 (*func_dec_frame)(td_void *decoder, td_u8 **in_buf, td_s32 *left_byte, td_u16 *out_buf, td_u32 *out_len, td_u32 *chns); td_s32 (*func_get_frame_info)(td_void *decoder, td_void *info); td_s32 (*func_close_decoder)(td_void *decoder); td_s32 (*func_reset_decoder)(td_void *decoder);
} ot_adec_decoder;
``` 【成员】 <a name="table1360mcpsimp"></a>
<table><thead align="left"><tr id="row1365mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p1367mcpsimp"><a name="p1367mcpsimp"></a><a name="p1367mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p1369mcpsimp"><a name="p1369mcpsimp"></a><a name="p1369mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1371mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1373mcpsimp"><a name="p1373mcpsimp"></a><a name="p1373mcpsimp"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1375mcpsimp"><a name="p1375mcpsimp"></a><a name="p1375mcpsimp"></a>解码协议类型，见《MPP 媒体处理软件V5.0 开发参考》“系统控制”章节。</p>
</td>
</tr>
<tr id="row1376mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1378mcpsimp"><a name="p1378mcpsimp"></a><a name="p1378mcpsimp"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1380mcpsimp"><a name="p1380mcpsimp"></a><a name="p1380mcpsimp"></a>解码器名称。<span xml:lang="fr-FR" id="ph1381mcpsimp"><a name="ph1381mcpsimp"></a><a name="ph1381mcpsimp"></a>OT_MAX_DECODER_NAME_LEN定义</span>见《MPP 媒体处理软件V5.0 开发参考》“音频”章节。</p>
</td>
</tr>
<tr id="row1382mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1384mcpsimp"><a name="p1384mcpsimp"></a><a name="p1384mcpsimp"></a>func_open_decoder</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1386mcpsimp"><a name="p1386mcpsimp"></a><a name="p1386mcpsimp"></a>打开解码器的函数指针。</p>
</td>
</tr>
<tr id="row1387mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1389mcpsimp"><a name="p1389mcpsimp"></a><a name="p1389mcpsimp"></a>func_dec_frame</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1391mcpsimp"><a name="p1391mcpsimp"></a><a name="p1391mcpsimp"></a>进行解码的函数指针。</p>
</td>
</tr>
<tr id="row1392mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1394mcpsimp"><a name="p1394mcpsimp"></a><a name="p1394mcpsimp"></a>func_get_frame_info</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1396mcpsimp"><a name="p1396mcpsimp"></a><a name="p1396mcpsimp"></a>获取音频帧信息的函数指针</p>
</td>
</tr>
<tr id="row1397mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1399mcpsimp"><a name="p1399mcpsimp"></a><a name="p1399mcpsimp"></a>func_close_decoder</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1401mcpsimp"><a name="p1401mcpsimp"></a><a name="p1401mcpsimp"></a>关闭解码器的函数指针。</p>
</td>
</tr>
<tr id="row1402mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1404mcpsimp"><a name="p1404mcpsimp"></a><a name="p1404mcpsimp"></a>func_reset_decoder</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p1406mcpsimp"><a name="p1406mcpsimp"></a><a name="p1406mcpsimp"></a>重启解码器的函数指针。</p>
</td>
</tr>
</tbody>
</table> 【注意事项】 无。 【相关数据类型及接口】 [ss\_mpi\_adec\_register\_decoder](#ZH-CN_TOPIC_0000002408115474) ### ot\_aac\_type<a name="ZH-CN_TOPIC_0000002441674777"></a> 【说明】 定义AAC音频编解码协议类型。 【定义】 ```
typedef enum { OT_AAC_TYPE_AACLC = 0, OT_AAC_TYPE_EAAC = 1, OT_AAC_TYPE_EAACPLUS = 2, OT_AAC_TYPE_AACLD = 3, OT_AAC_TYPE_AACELD = 4, OT_AAC_TYPE_BUTT,
} ot_aac_type;
``` 【成员】 <a name="table1425mcpsimp"></a>
<table><thead align="left"><tr id="row1430mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p1432mcpsimp"><a name="p1432mcpsimp"></a><a name="p1432mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p1434mcpsimp"><a name="p1434mcpsimp"></a><a name="p1434mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1436mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1438mcpsimp"><a name="p1438mcpsimp"></a><a name="p1438mcpsimp"></a>OT_AAC_TYPE_AACLC</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1440mcpsimp"><a name="p1440mcpsimp"></a><a name="p1440mcpsimp"></a>AACLC格式。</p>
</td>
</tr>
<tr id="row1441mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1443mcpsimp"><a name="p1443mcpsimp"></a><a name="p1443mcpsimp"></a>OT_AAC_TYPE_EAAC</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1445mcpsimp"><a name="p1445mcpsimp"></a><a name="p1445mcpsimp"></a>eAAC格式（也称为HEAAC、AAC+或aacPlusV1）。</p>
</td>
</tr>
<tr id="row1446mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1448mcpsimp"><a name="p1448mcpsimp"></a><a name="p1448mcpsimp"></a>OT_AAC_TYPE_EAACPLUS</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1450mcpsimp"><a name="p1450mcpsimp"></a><a name="p1450mcpsimp"></a>eAACPLUS格式（也称为AAC++或aacPlusV2）。</p>
</td>
</tr>
<tr id="row1451mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1453mcpsimp"><a name="p1453mcpsimp"></a><a name="p1453mcpsimp"></a>OT_AAC_TYPE_AACLD</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1455mcpsimp"><a name="p1455mcpsimp"></a><a name="p1455mcpsimp"></a>AACLD格式。</p>
</td>
</tr>
<tr id="row1456mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1458mcpsimp"><a name="p1458mcpsimp"></a><a name="p1458mcpsimp"></a>OT_AAC_TYPE_AACELD</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1460mcpsimp"><a name="p1460mcpsimp"></a><a name="p1460mcpsimp"></a>AACELD格式。</p>
</td>
</tr>
</tbody>
</table> 【注意事项】 无。 【相关数据类型及接口】 无。 ### ot\_aac\_bps<a name="ZH-CN_TOPIC_0000002408275382"></a> 【说明】 定义AAC音频编码码率。 【定义】 ```
typedef enum { OT_AAC_BPS_8K = 8000, OT_AAC_BPS_16K = 16000, OT_AAC_BPS_22K = 22000, OT_AAC_BPS_24K = 24000, OT_AAC_BPS_32K = 32000, OT_AAC_BPS_48K = 48000, OT_AAC_BPS_64K = 64000, OT_AAC_BPS_96K = 96000, OT_AAC_BPS_128K = 128000, OT_AAC_BPS_256K = 256000, OT_AAC_BPS_320K = 320000, OT_AAC_BPS_BUTT
} ot_aac_bps;
``` 【成员】 <a name="table1484mcpsimp"></a>
<table><thead align="left"><tr id="row1489mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p1491mcpsimp"><a name="p1491mcpsimp"></a><a name="p1491mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p1493mcpsimp"><a name="p1493mcpsimp"></a><a name="p1493mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1495mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1497mcpsimp"><a name="p1497mcpsimp"></a><a name="p1497mcpsimp"></a>OT_AAC_BPS_8K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1499mcpsimp"><a name="p1499mcpsimp"></a><a name="p1499mcpsimp"></a>8kbit/s</p>
</td>
</tr>
<tr id="row1500mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1502mcpsimp"><a name="p1502mcpsimp"></a><a name="p1502mcpsimp"></a>OT_AAC_BPS_16K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1504mcpsimp"><a name="p1504mcpsimp"></a><a name="p1504mcpsimp"></a>16kbit/s</p>
</td>
</tr>
<tr id="row1505mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1507mcpsimp"><a name="p1507mcpsimp"></a><a name="p1507mcpsimp"></a>OT_AAC_BPS_22K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1509mcpsimp"><a name="p1509mcpsimp"></a><a name="p1509mcpsimp"></a>22kbit/s</p>
</td>
</tr>
<tr id="row1510mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1512mcpsimp"><a name="p1512mcpsimp"></a><a name="p1512mcpsimp"></a>OT_AAC_BPS_24K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1514mcpsimp"><a name="p1514mcpsimp"></a><a name="p1514mcpsimp"></a>24kbit/s</p>
</td>
</tr>
<tr id="row1515mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1517mcpsimp"><a name="p1517mcpsimp"></a><a name="p1517mcpsimp"></a>OT_AAC_BPS_32K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1519mcpsimp"><a name="p1519mcpsimp"></a><a name="p1519mcpsimp"></a>32kbit/s</p>
</td>
</tr>
<tr id="row1520mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1522mcpsimp"><a name="p1522mcpsimp"></a><a name="p1522mcpsimp"></a>OT_AAC_BPS_48K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1524mcpsimp"><a name="p1524mcpsimp"></a><a name="p1524mcpsimp"></a>48kbit/s</p>
</td>
</tr>
<tr id="row1525mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1527mcpsimp"><a name="p1527mcpsimp"></a><a name="p1527mcpsimp"></a>OT_AAC_BPS_64K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1529mcpsimp"><a name="p1529mcpsimp"></a><a name="p1529mcpsimp"></a>64kbit/s</p>
</td>
</tr>
<tr id="row1530mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1532mcpsimp"><a name="p1532mcpsimp"></a><a name="p1532mcpsimp"></a>OT_AAC_BPS_96K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1534mcpsimp"><a name="p1534mcpsimp"></a><a name="p1534mcpsimp"></a>96kbit/s</p>
</td>
</tr>
<tr id="row1535mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1537mcpsimp"><a name="p1537mcpsimp"></a><a name="p1537mcpsimp"></a>OT_AAC_BPS_128K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1539mcpsimp"><a name="p1539mcpsimp"></a><a name="p1539mcpsimp"></a>128kbit/s</p>
</td>
</tr>
<tr id="row1540mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1542mcpsimp"><a name="p1542mcpsimp"></a><a name="p1542mcpsimp"></a>OT_AAC_BPS_256K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1544mcpsimp"><a name="p1544mcpsimp"></a><a name="p1544mcpsimp"></a>256kbit/s</p>
</td>
</tr>
<tr id="row1545mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1547mcpsimp"><a name="p1547mcpsimp"></a><a name="p1547mcpsimp"></a>OT_AAC_BPS_320K</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1549mcpsimp"><a name="p1549mcpsimp"></a><a name="p1549mcpsimp"></a>320kbit/s</p>
</td>
</tr>
</tbody>
</table> 【注意事项】 无。 【相关数据类型及接口】 无。 ### ot\_aac\_transport\_type<a name="ZH-CN_TOPIC_0000002408115466"></a> 【说明】 定义AAC音频编解码协议传输封装类型。 【定义】 ```
typedef enum { OT_AAC_TRANSPORT_TYPE_ADTS = 0, OT_AAC_TRANSPORT_TYPE_LOAS = 1, OT_AAC_TRANSPORT_TYPE_LATM_MCP1 = 2, OT_AAC_TRANSPORT_TYPE_BUTT
} ot_aac_transport_type;
``` 【成员】 <a name="table1565mcpsimp"></a>
<table><thead align="left"><tr id="row1570mcpsimp"><th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.1"><p id="p1572mcpsimp"><a name="p1572mcpsimp"></a><a name="p1572mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.2"><p id="p1574mcpsimp"><a name="p1574mcpsimp"></a><a name="p1574mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1576mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p id="p1578mcpsimp"><a name="p1578mcpsimp"></a><a name="p1578mcpsimp"></a>OT_AAC_TRANSPORT_TYPE_ADTS</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p id="p1580mcpsimp"><a name="p1580mcpsimp"></a><a name="p1580mcpsimp"></a>ADTS封装格式。AACLC/EAAC/EAACPLUS支持。</p>
</td>
</tr>
<tr id="row1581mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p id="p1583mcpsimp"><a name="p1583mcpsimp"></a><a name="p1583mcpsimp"></a>OT_AAC_TRANSPORT_TYPE_LOAS</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p id="p1585mcpsimp"><a name="p1585mcpsimp"></a><a name="p1585mcpsimp"></a>LOAS封装格式。AACLC/EAAC/EAACPLUS/AACLD/AACELD支持。</p>
</td>
</tr>
<tr id="row1586mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p id="p1588mcpsimp"><a name="p1588mcpsimp"></a><a name="p1588mcpsimp"></a>OT_AAC_TRANSPORT_TYPE_LATM_MCP1</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p id="p1590mcpsimp"><a name="p1590mcpsimp"></a><a name="p1590mcpsimp"></a>LATM1封装格式。AACLC/EAAC/EAACPLUS/AACLD/AACELD支持。</p>
</td>
</tr>
</tbody>
</table> 【注意事项】 LATM1格式由于不具备同步帧头机制，在码流出现问题时无法快速恢复，**不推荐使用**。 【相关数据类型及接口】 无。 ### ot\_aenc\_attr\_aac<a name="ZH-CN_TOPIC_0000002408115470"></a> 【说明】 定义AAC编码协议属性结构体。 【定义】 ```
typedef struct { ot_aac_type aac_type; ot_aac_bps bit_rate; ot_audio_sample_rate sample_rate; ot_audio_bit_width bit_width; ot_audio_snd_mode snd_mode; ot_aac_transport_type transport_type; td_s16 band_width;;
} ot_aenc_attr_aac;
``` 【成员】 <a name="table1611mcpsimp"></a>
<table><thead align="left"><tr id="row1616mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.3.1.1"><p id="p1618mcpsimp"><a name="p1618mcpsimp"></a><a name="p1618mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="79%" id="mcps1.1.3.1.2"><p id="p1620mcpsimp"><a name="p1620mcpsimp"></a><a name="p1620mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1622mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1624mcpsimp"><a name="p1624mcpsimp"></a><a name="p1624mcpsimp"></a>aac_type</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1626mcpsimp"><a name="p1626mcpsimp"></a><a name="p1626mcpsimp"></a>AAC编码类型（Profile）。</p>
</td>
</tr>
<tr id="row1627mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1629mcpsimp"><a name="p1629mcpsimp"></a><a name="p1629mcpsimp"></a>bit_rate</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1631mcpsimp"><a name="p1631mcpsimp"></a><a name="p1631mcpsimp"></a>编码码率。</p>
<p id="p1632mcpsimp"><a name="p1632mcpsimp"></a><a name="p1632mcpsimp"></a>取值范围：</p>
<p id="p1633mcpsimp"><a name="p1633mcpsimp"></a><a name="p1633mcpsimp"></a>LC：16～320；</p>
<p id="p1634mcpsimp"><a name="p1634mcpsimp"></a><a name="p1634mcpsimp"></a>EAAC：24～128；</p>
<p id="p1635mcpsimp"><a name="p1635mcpsimp"></a><a name="p1635mcpsimp"></a>EAAC+：16～64；</p>
<p id="p1636mcpsimp"><a name="p1636mcpsimp"></a><a name="p1636mcpsimp"></a>AACLD：16～320；</p>
<p id="p1637mcpsimp"><a name="p1637mcpsimp"></a><a name="p1637mcpsimp"></a>AACELD：32～320；</p>
<p id="p1638mcpsimp"><a name="p1638mcpsimp"></a><a name="p1638mcpsimp"></a>以kbit/s为单位。</p>
</td>
</tr>
<tr id="row1639mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1641mcpsimp"><a name="p1641mcpsimp"></a><a name="p1641mcpsimp"></a>sample_rate</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1643mcpsimp"><a name="p1643mcpsimp"></a><a name="p1643mcpsimp"></a>音频数据的采样率。</p>
<p id="p1644mcpsimp"><a name="p1644mcpsimp"></a><a name="p1644mcpsimp"></a>取值范围：</p>
<p id="p1645mcpsimp"><a name="p1645mcpsimp"></a><a name="p1645mcpsimp"></a>LC：8～48；</p>
<p id="p1646mcpsimp"><a name="p1646mcpsimp"></a><a name="p1646mcpsimp"></a>EAAC：16～48；</p>
<p id="p1647mcpsimp"><a name="p1647mcpsimp"></a><a name="p1647mcpsimp"></a>EAAC+：16～48。</p>
<p id="p1648mcpsimp"><a name="p1648mcpsimp"></a><a name="p1648mcpsimp"></a>AACLD：8～48；</p>
<p id="p1649mcpsimp"><a name="p1649mcpsimp"></a><a name="p1649mcpsimp"></a>AACELD：8～48；</p>
<p id="p1650mcpsimp"><a name="p1650mcpsimp"></a><a name="p1650mcpsimp"></a>以kHz为单位。</p>
<p id="p1651mcpsimp"><a name="p1651mcpsimp"></a><a name="p1651mcpsimp"></a>ot_audio_sample_rate请参见《MPP 媒体处理软件V5.0 开发参考》“音频”章节。</p>
</td>
</tr>
<tr id="row1652mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1654mcpsimp"><a name="p1654mcpsimp"></a><a name="p1654mcpsimp"></a>bit_width</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1656mcpsimp"><a name="p1656mcpsimp"></a><a name="p1656mcpsimp"></a>音频数据采样精度，只支持16bit。</p>
<p id="p1657mcpsimp"><a name="p1657mcpsimp"></a><a name="p1657mcpsimp"></a>ot_audio_bit_width请参见《MPP 媒体处理软件V5.0 开发参考》“音频”章节。</p>
</td>
</tr>
<tr id="row1658mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1660mcpsimp"><a name="p1660mcpsimp"></a><a name="p1660mcpsimp"></a>snd_mode</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1662mcpsimp"><a name="p1662mcpsimp"></a><a name="p1662mcpsimp"></a>输入数据的声道模式。支持输入为单声道或双声道。</p>
<p id="p1663mcpsimp"><a name="p1663mcpsimp"></a><a name="p1663mcpsimp"></a>ot_audio_snd_mode请参见《MPP 媒体处理软件V5.0 开发参考》“音频”章节。</p>
</td>
</tr>
<tr id="row1664mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1666mcpsimp"><a name="p1666mcpsimp"></a><a name="p1666mcpsimp"></a>transport_type</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1668mcpsimp"><a name="p1668mcpsimp"></a><a name="p1668mcpsimp"></a>AAC传输封装类型。</p>
<p id="p1669mcpsimp"><a name="p1669mcpsimp"></a><a name="p1669mcpsimp"></a>取值范围：</p>
<a name="ul1670mcpsimp"></a><a name="ul1670mcpsimp"></a><ul id="ul1670mcpsimp"><li>OT_AAC_TRANSPORT_TYPE_ADTS：0</li><li>OT_AAC_TRANSPORT_TYPE_LOAS：1</li><li>OT_AAC_TRANSPORT_TYPE_LATM_MCP1：2</li></ul>
</td>
</tr>
<tr id="row1674mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1676mcpsimp"><a name="p1676mcpsimp"></a><a name="p1676mcpsimp"></a>band_width</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1678mcpsimp"><a name="p1678mcpsimp"></a><a name="p1678mcpsimp"></a>目标频段范围。取值范围是，0或1000~sample_rate/2，单位Hz</p>
</td>
</tr>
</tbody>
</table> 【注意事项】 无。 【相关数据类型及接口】 无。 ### ot\_adec\_attr\_aac<a name="ZH-CN_TOPIC_0000002441714625"></a> 【说明】 定义AAC解码协议属性结构体。 【定义】 ```
typedef struct { ot_aac_transport_type transport_type;
} ot_adec_attr_aac;
``` 【成员】 <a name="table1692mcpsimp"></a>
<table><thead align="left"><tr id="row1697mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.3.1.1"><p id="p1699mcpsimp"><a name="p1699mcpsimp"></a><a name="p1699mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="79%" id="mcps1.1.3.1.2"><p id="p1701mcpsimp"><a name="p1701mcpsimp"></a><a name="p1701mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1703mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.3.1.1 "><p id="p1705mcpsimp"><a name="p1705mcpsimp"></a><a name="p1705mcpsimp"></a>trans_type</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.1.3.1.2 "><p id="p1707mcpsimp"><a name="p1707mcpsimp"></a><a name="p1707mcpsimp"></a>AAC传输封装类型。</p>
<p id="p1708mcpsimp"><a name="p1708mcpsimp"></a><a name="p1708mcpsimp"></a>取值范围：</p>
<a name="ul1709mcpsimp"></a><a name="ul1709mcpsimp"></a><ul id="ul1709mcpsimp"><li>OT_AAC_TRANSPORT_TYPE_ADTS：0</li><li>OT_AAC_TRANSPORT_TYPE_LOAS：1</li><li>OT_AAC_TRANSPORT_TYPE_LATM_MCP1：2</li></ul>
</td>
</tr>
</tbody>
</table> 【注意事项】 无。 【相关数据类型及接口】 无。 ## 错误码<a name="ZH-CN_TOPIC_0000002408115506"></a> ### 音频编码错误码<a name="ZH-CN_TOPIC_0000002441674781"></a> 音频编码API错误码如下所示。 **表 1** 音频编码API错误码 <a name="_Ref268526472"></a>
<table><thead align="left"><tr id="row1727mcpsimp"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p1729mcpsimp"><a name="p1729mcpsimp"></a><a name="p1729mcpsimp"></a>错误代码</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.4.1.2"><p id="p1731mcpsimp"><a name="p1731mcpsimp"></a><a name="p1731mcpsimp"></a>宏定义</p>
</th>
<th class="cellrowborder" valign="top" width="33.663366336633665%" id="mcps1.2.4.1.3"><p id="p1733mcpsimp"><a name="p1733mcpsimp"></a><a name="p1733mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1735mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1737mcpsimp"><a name="p1737mcpsimp"></a><a name="p1737mcpsimp"></a>0xa0178001</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1739mcpsimp"><a name="p1739mcpsimp"></a><a name="p1739mcpsimp"></a>OT_ERR_AENC_INVALID_DEV_ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1741mcpsimp"><a name="p1741mcpsimp"></a><a name="p1741mcpsimp"></a>音频设备号无效</p>
</td>
</tr>
<tr id="row1742mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1744mcpsimp"><a name="p1744mcpsimp"></a><a name="p1744mcpsimp"></a>0xa0178003</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1746mcpsimp"><a name="p1746mcpsimp"></a><a name="p1746mcpsimp"></a>OT_ERR_AENC_INVALID_CHN_ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1748mcpsimp"><a name="p1748mcpsimp"></a><a name="p1748mcpsimp"></a>音频编码通道号无效</p>
</td>
</tr>
<tr id="row1749mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1751mcpsimp"><a name="p1751mcpsimp"></a><a name="p1751mcpsimp"></a>0xa0178007</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1753mcpsimp"><a name="p1753mcpsimp"></a><a name="p1753mcpsimp"></a>OT_ERR_AENC_ILLEGAL_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1755mcpsimp"><a name="p1755mcpsimp"></a><a name="p1755mcpsimp"></a>音频编码参数设置无效</p>
</td>
</tr>
<tr id="row1756mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1758mcpsimp"><a name="p1758mcpsimp"></a><a name="p1758mcpsimp"></a>0xa0178008</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1760mcpsimp"><a name="p1760mcpsimp"></a><a name="p1760mcpsimp"></a>OT_ERR_AENC_EXIST</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1762mcpsimp"><a name="p1762mcpsimp"></a><a name="p1762mcpsimp"></a>音频编码通道已经创建</p>
</td>
</tr>
<tr id="row1763mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1765mcpsimp"><a name="p1765mcpsimp"></a><a name="p1765mcpsimp"></a>0xa0178009</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1767mcpsimp"><a name="p1767mcpsimp"></a><a name="p1767mcpsimp"></a>OT_ERR_AENC_UNEXIST</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1769mcpsimp"><a name="p1769mcpsimp"></a><a name="p1769mcpsimp"></a>音频编码通道未创建</p>
</td>
</tr>
<tr id="row1770mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1772mcpsimp"><a name="p1772mcpsimp"></a><a name="p1772mcpsimp"></a>0xa017800a</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1774mcpsimp"><a name="p1774mcpsimp"></a><a name="p1774mcpsimp"></a>OT_ERR_AENC_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1776mcpsimp"><a name="p1776mcpsimp"></a><a name="p1776mcpsimp"></a>输入参数空指针错误</p>
</td>
</tr>
<tr id="row1777mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1779mcpsimp"><a name="p1779mcpsimp"></a><a name="p1779mcpsimp"></a>0xa017800b</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1781mcpsimp"><a name="p1781mcpsimp"></a><a name="p1781mcpsimp"></a>OT_ERR_AENC_NOT_CFG</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1783mcpsimp"><a name="p1783mcpsimp"></a><a name="p1783mcpsimp"></a>编码通道未配置</p>
</td>
</tr>
<tr id="row1784mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1786mcpsimp"><a name="p1786mcpsimp"></a><a name="p1786mcpsimp"></a>0xa017800c</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1788mcpsimp"><a name="p1788mcpsimp"></a><a name="p1788mcpsimp"></a>OT_ERR_AENC_NOT_SUPPORT</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1790mcpsimp"><a name="p1790mcpsimp"></a><a name="p1790mcpsimp"></a>操作不被支持</p>
</td>
</tr>
<tr id="row1791mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1793mcpsimp"><a name="p1793mcpsimp"></a><a name="p1793mcpsimp"></a>0xa017800d</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1795mcpsimp"><a name="p1795mcpsimp"></a><a name="p1795mcpsimp"></a>OT_ERR_AENC_NOT_PERM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1797mcpsimp"><a name="p1797mcpsimp"></a><a name="p1797mcpsimp"></a>操作不允许</p>
</td>
</tr>
<tr id="row1798mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1800mcpsimp"><a name="p1800mcpsimp"></a><a name="p1800mcpsimp"></a>0xa0178014</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1802mcpsimp"><a name="p1802mcpsimp"></a><a name="p1802mcpsimp"></a>OT_ERR_AENC_NO_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1804mcpsimp"><a name="p1804mcpsimp"></a><a name="p1804mcpsimp"></a>系统内存不足</p>
</td>
</tr>
<tr id="row1805mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1807mcpsimp"><a name="p1807mcpsimp"></a><a name="p1807mcpsimp"></a>0xa0178015</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1809mcpsimp"><a name="p1809mcpsimp"></a><a name="p1809mcpsimp"></a>OT_ERR_AENC_NO_BUF</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1811mcpsimp"><a name="p1811mcpsimp"></a><a name="p1811mcpsimp"></a>编码通道缓存分配失败</p>
</td>
</tr>
<tr id="row1812mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1814mcpsimp"><a name="p1814mcpsimp"></a><a name="p1814mcpsimp"></a>0xa0178016</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1816mcpsimp"><a name="p1816mcpsimp"></a><a name="p1816mcpsimp"></a>OT_ERR_AENC_BUF_EMPTY</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1818mcpsimp"><a name="p1818mcpsimp"></a><a name="p1818mcpsimp"></a>编码通道缓存空</p>
</td>
</tr>
<tr id="row1819mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1821mcpsimp"><a name="p1821mcpsimp"></a><a name="p1821mcpsimp"></a>0xa0178017</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1823mcpsimp"><a name="p1823mcpsimp"></a><a name="p1823mcpsimp"></a>OT_ERR_AENC_BUF_FULL</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1825mcpsimp"><a name="p1825mcpsimp"></a><a name="p1825mcpsimp"></a>编码通道缓存满</p>
</td>
</tr>
<tr id="row1826mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1828mcpsimp"><a name="p1828mcpsimp"></a><a name="p1828mcpsimp"></a>0xa0178018</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1830mcpsimp"><a name="p1830mcpsimp"></a><a name="p1830mcpsimp"></a>OT_ERR_AENC_NOT_READY</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1832mcpsimp"><a name="p1832mcpsimp"></a><a name="p1832mcpsimp"></a>系统没有初始化</p>
</td>
</tr>
<tr id="row1833mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1835mcpsimp"><a name="p1835mcpsimp"></a><a name="p1835mcpsimp"></a>0xa0178040</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1837mcpsimp"><a name="p1837mcpsimp"></a><a name="p1837mcpsimp"></a>OT_ERR_AENC_ENCODER_ERR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1839mcpsimp"><a name="p1839mcpsimp"></a><a name="p1839mcpsimp"></a>音频编码数据错误</p>
</td>
</tr>
<tr id="row1840mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1842mcpsimp"><a name="p1842mcpsimp"></a><a name="p1842mcpsimp"></a>0xa0178041</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1844mcpsimp"><a name="p1844mcpsimp"></a><a name="p1844mcpsimp"></a>OT_ERR_AENC_VQE_ERR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1846mcpsimp"><a name="p1846mcpsimp"></a><a name="p1846mcpsimp"></a>AENC VQE处理错误</p>
</td>
</tr>
</tbody>
</table> ### 音频解码错误码<a name="ZH-CN_TOPIC_0000002408275374"></a> 音频解码API错误码如下所示。 **表 1** 音频解码API错误码 <a name="_Ref268526500"></a>
<table><thead align="left"><tr id="row1856mcpsimp"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p1858mcpsimp"><a name="p1858mcpsimp"></a><a name="p1858mcpsimp"></a>错误代码</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.4.1.2"><p id="p1860mcpsimp"><a name="p1860mcpsimp"></a><a name="p1860mcpsimp"></a>宏定义</p>
</th>
<th class="cellrowborder" valign="top" width="33.663366336633665%" id="mcps1.2.4.1.3"><p id="p1862mcpsimp"><a name="p1862mcpsimp"></a><a name="p1862mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1864mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1866mcpsimp"><a name="p1866mcpsimp"></a><a name="p1866mcpsimp"></a>0xa0188001</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1868mcpsimp"><a name="p1868mcpsimp"></a><a name="p1868mcpsimp"></a>OT_ERR_ADEC_INVALID_DEV_ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1870mcpsimp"><a name="p1870mcpsimp"></a><a name="p1870mcpsimp"></a>音频解码设备号无效</p>
</td>
</tr>
<tr id="row1871mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1873mcpsimp"><a name="p1873mcpsimp"></a><a name="p1873mcpsimp"></a>0xa0188002</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1875mcpsimp"><a name="p1875mcpsimp"></a><a name="p1875mcpsimp"></a>OT_ERR_ADEC_INVALID_CHN_ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1877mcpsimp"><a name="p1877mcpsimp"></a><a name="p1877mcpsimp"></a>音频解码通道号无效</p>
</td>
</tr>
<tr id="row1878mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1880mcpsimp"><a name="p1880mcpsimp"></a><a name="p1880mcpsimp"></a>0xa0188007</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1882mcpsimp"><a name="p1882mcpsimp"></a><a name="p1882mcpsimp"></a>OT_ERR_ADEC_ILLEGAL_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1884mcpsimp"><a name="p1884mcpsimp"></a><a name="p1884mcpsimp"></a>音频解码参数设置无效</p>
</td>
</tr>
<tr id="row1885mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1887mcpsimp"><a name="p1887mcpsimp"></a><a name="p1887mcpsimp"></a>0xa0188008</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1889mcpsimp"><a name="p1889mcpsimp"></a><a name="p1889mcpsimp"></a>OT_ERR_ADEC_EXIST</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1891mcpsimp"><a name="p1891mcpsimp"></a><a name="p1891mcpsimp"></a>音频解码通道已经创建</p>
</td>
</tr>
<tr id="row1892mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1894mcpsimp"><a name="p1894mcpsimp"></a><a name="p1894mcpsimp"></a>0xa0188009</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1896mcpsimp"><a name="p1896mcpsimp"></a><a name="p1896mcpsimp"></a>OT_ERR_ADEC_UNEXIST</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1898mcpsimp"><a name="p1898mcpsimp"></a><a name="p1898mcpsimp"></a>音频解码通道未创建</p>
</td>
</tr>
<tr id="row1899mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1901mcpsimp"><a name="p1901mcpsimp"></a><a name="p1901mcpsimp"></a>0xa018800a</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1903mcpsimp"><a name="p1903mcpsimp"></a><a name="p1903mcpsimp"></a>OT_ERR_ADEC_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1905mcpsimp"><a name="p1905mcpsimp"></a><a name="p1905mcpsimp"></a>输入参数空指针错误</p>
</td>
</tr>
<tr id="row1906mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1908mcpsimp"><a name="p1908mcpsimp"></a><a name="p1908mcpsimp"></a>0xa018800b</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1910mcpsimp"><a name="p1910mcpsimp"></a><a name="p1910mcpsimp"></a>OT_ERR_ADEC_NOT_CFG</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1912mcpsimp"><a name="p1912mcpsimp"></a><a name="p1912mcpsimp"></a>解码通道属性未配置</p>
</td>
</tr>
<tr id="row1913mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1915mcpsimp"><a name="p1915mcpsimp"></a><a name="p1915mcpsimp"></a>0xa018800c</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1917mcpsimp"><a name="p1917mcpsimp"></a><a name="p1917mcpsimp"></a>OT_ERR_ADEC_NOT_SUPPORT</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1919mcpsimp"><a name="p1919mcpsimp"></a><a name="p1919mcpsimp"></a>操作不被支持</p>
</td>
</tr>
<tr id="row1920mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1922mcpsimp"><a name="p1922mcpsimp"></a><a name="p1922mcpsimp"></a>0xa018800d</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1924mcpsimp"><a name="p1924mcpsimp"></a><a name="p1924mcpsimp"></a>OT_ERR_ADEC_NOT_PERM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1926mcpsimp"><a name="p1926mcpsimp"></a><a name="p1926mcpsimp"></a>操作不允许</p>
</td>
</tr>
<tr id="row1927mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1929mcpsimp"><a name="p1929mcpsimp"></a><a name="p1929mcpsimp"></a>0xa0188014</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1931mcpsimp"><a name="p1931mcpsimp"></a><a name="p1931mcpsimp"></a>OT_ERR_ADEC_NO_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1933mcpsimp"><a name="p1933mcpsimp"></a><a name="p1933mcpsimp"></a>系统内存不足</p>
</td>
</tr>
<tr id="row1934mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1936mcpsimp"><a name="p1936mcpsimp"></a><a name="p1936mcpsimp"></a>0xa0188015</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1938mcpsimp"><a name="p1938mcpsimp"></a><a name="p1938mcpsimp"></a>OT_ERR_ADEC_NO_BUF</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1940mcpsimp"><a name="p1940mcpsimp"></a><a name="p1940mcpsimp"></a>解码通道缓存分配失败</p>
</td>
</tr>
<tr id="row1941mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1943mcpsimp"><a name="p1943mcpsimp"></a><a name="p1943mcpsimp"></a>0xa0188016</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1945mcpsimp"><a name="p1945mcpsimp"></a><a name="p1945mcpsimp"></a>OT_ERR_ADEC_BUF_EMPTY</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1947mcpsimp"><a name="p1947mcpsimp"></a><a name="p1947mcpsimp"></a>解码通道缓存空</p>
</td>
</tr>
<tr id="row1948mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1950mcpsimp"><a name="p1950mcpsimp"></a><a name="p1950mcpsimp"></a>0xa0188017</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1952mcpsimp"><a name="p1952mcpsimp"></a><a name="p1952mcpsimp"></a>OT_ERR_ADEC_BUF_FULL</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1954mcpsimp"><a name="p1954mcpsimp"></a><a name="p1954mcpsimp"></a>解码通道缓存满</p>
</td>
</tr>
<tr id="row1955mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1957mcpsimp"><a name="p1957mcpsimp"></a><a name="p1957mcpsimp"></a>0xa0188018</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1959mcpsimp"><a name="p1959mcpsimp"></a><a name="p1959mcpsimp"></a>OT_ERR_ADEC_NOT_READY</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1961mcpsimp"><a name="p1961mcpsimp"></a><a name="p1961mcpsimp"></a>系统没有初始化</p>
</td>
</tr>
<tr id="row1962mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1964mcpsimp"><a name="p1964mcpsimp"></a><a name="p1964mcpsimp"></a>0xa0188040</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1966mcpsimp"><a name="p1966mcpsimp"></a><a name="p1966mcpsimp"></a>OT_ERR_ADEC_DECODER_ERR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1968mcpsimp"><a name="p1968mcpsimp"></a><a name="p1968mcpsimp"></a>音频解码数据错误</p>
</td>
</tr>
<tr id="row1969mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1971mcpsimp"><a name="p1971mcpsimp"></a><a name="p1971mcpsimp"></a>0xa0188041</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1973mcpsimp"><a name="p1973mcpsimp"></a><a name="p1973mcpsimp"></a>OT_ERR_ADEC_BUF_LACK</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p id="p1975mcpsimp"><a name="p1975mcpsimp"></a><a name="p1975mcpsimp"></a>解码输入缓存空间不够</p>
</td>
</tr>
</tbody>
</table>
