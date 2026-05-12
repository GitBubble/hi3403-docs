---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/音频组件API参考/音频组件 API参考.md
---

# Preface
**Overview<a name="section143mcpsimp"></a>**

This document is written for programmers developing intelligent analysis solutions using the audio functionality of the media processing chip. It is intended to provide reference information supported by audio during development, including protocol descriptions, APIs, error codes, etc.

**Product Version<a name="section146mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table149mcpsimp"></a>
<table><thead align="left"><tr id="row154mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p156mcpsimp"><a name="p156mcpsimp"></a><a name="p156mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p158mcpsimp"><a name="p158mcpsimp"></a><a name="p158mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row160mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p162mcpsimp"><a name="p162mcpsimp"></a><a name="p162mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p164mcpsimp"><a name="p164mcpsimp"></a><a name="p164mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row165mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p167mcpsimp"><a name="p167mcpsimp"></a><a name="p167mcpsimp"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p169mcpsimp"><a name="p169mcpsimp"></a><a name="p169mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row7709132215363"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p881081984715"><a name="p881081984715"></a><a name="p881081984715"></a>SS524</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
<tr id="row8236125812712"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p119117210287"><a name="p119117210287"></a><a name="p119117210287"></a>SS522</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p89152122811"><a name="p89152122811"></a><a name="p89152122811"></a>V100</p>
</td>
</tr>
<tr id="row12260172910419"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p175361749141815"><a name="p175361749141815"></a><a name="p175361749141815"></a>SS528</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13835920181"><a name="p13835920181"></a><a name="p13835920181"></a>V100</p>
</td>
</tr>
<tr id="row151529352446"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p3152113524414"><a name="p3152113524414"></a><a name="p3152113524414"></a>SS625</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p715215356441"><a name="p715215356441"></a><a name="p715215356441"></a>V100</p>
</td>
</tr>
<tr id="row32641658179"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section170mcpsimp"></a>**

This document (guide) is primarily intended for the following engineers:

-   Technical Support Engineers
-   Software Development Engineers

**Symbol Conventions<a name="section176mcpsimp"></a>**

The following symbols may appear in this document, and their meanings are described below.

<a name="table179mcpsimp"></a>
<table><thead align="left"><tr id="row184mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p186mcpsimp"><a name="p186mcpsimp"></a><a name="p186mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p188mcpsimp"><a name="p188mcpsimp"></a><a name="p188mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row190mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p192mcpsimp"><a name="p192mcpsimp"></a><a name="p192mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="figures/zh-cn_image_0000002441714733.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p194mcpsimp"><a name="p194mcpsimp"></a><a name="p194mcpsimp"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row195mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p197mcpsimp"><a name="p197mcpsimp"></a><a name="p197mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="figures/zh-cn_image_0000002441674929.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p199mcpsimp"><a name="p199mcpsimp"></a><a name="p199mcpsimp"></a>Indicates a medium-level hazard which, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row200mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p202mcpsimp"><a name="p202mcpsimp"></a><a name="p202mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="figures/zh-cn_image_0000002441714825.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p204mcpsimp"><a name="p204mcpsimp"></a><a name="p204mcpsimp"></a>Indicates a low-level hazard which, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row205mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p207mcpsimp"><a name="p207mcpsimp"></a><a name="p207mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="figures/zh-cn_image_0000002408275514.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p209mcpsimp"><a name="p209mcpsimp"></a><a name="p209mcpsimp"></a>Used to convey device or environmental safety alert information. If not avoided, it may result in equipment damage, data loss, reduced equipment performance, or other unpredictable consequences.</p>
<p id="p210mcpsimp"><a name="p210mcpsimp"></a><a name="p210mcpsimp"></a>"Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row211mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p213mcpsimp"><a name="p213mcpsimp"></a><a name="p213mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="figures/zh-cn_image_0000002408115650.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>Supplementary explanation of key information in the main text.</p>
<p id="p216mcpsimp"><a name="p216mcpsimp"></a><a name="p216mcpsimp"></a>"Note" is not safety warning information and does not involve personal, equipment, or environmental injury.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section217mcpsimp"></a>**

The revision history summarizes the changes made in each document update. The latest version of the document includes updates from all previous document versions.

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
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1664582017209"><a name="p1664582017209"></a><a name="p1664582017209"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table>

# Audio Component
## Overview<a name="ZH-CN_TOPIC_0000002408275386"></a>

The audio component integrates the AAC codec protocol and provides interfaces to facilitate the integration of third-party codec protocols. Example code for AAC encoding/decoding is located in the sample/audio directory.

>![](public_sys-resources/icon-notice.gif) **Caution:**
>If customers need to use AAC format patents, they must obtain authorization from the copyright holder and pay the Licensing Fee.

## Important Concepts<a name="ZH-CN_TOPIC_0000002441674813"></a>

-   Audio Codec Protocol

    The encoding/decoding functions provided by the audio component are based on an independently packaged AAC codec library. The core codec operates in user mode and uses CPU software for encoding/decoding.

    The AAC codec protocol is described in [Table 1](#_Ref224548251).

**Table 1**  Audio codec protocol description

<a name="_Ref224548251"></a>
<table><thead align="left"><tr id="row261mcpsimp"><th class="cellrowborder" valign="top" width="10.341034103410342%" id="mcps1.2.8.1.1"><p id="p263mcpsimp"><a name="p263mcpsimp"></a><a name="p263mcpsimp"></a>Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="9.86098609860986%" id="mcps1.2.8.1.2"><p id="p265mcpsimp"><a name="p265mcpsimp"></a><a name="p265mcpsimp"></a>Sample Rate</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.8.1.3"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a>Frame Length (samples)</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.8.1.4"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a>Bitrate (kbps)</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.8.1.5"><p id="p272mcpsimp"><a name="p272mcpsimp"></a><a name="p272mcpsimp"></a>Compression Ratio</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.8.1.6"><p id="p274mcpsimp"><a name="p274mcpsimp"></a><a name="p274mcpsimp"></a>CPU Consumption</p>
</th>
<th class="cellrowborder" valign="top" width="31.313131313131308%" id="mcps1.2.8.1.7"><p id="p276mcpsimp"><a name="p276mcpsimp"></a><a name="p276mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row278mcpsimp"><td class="cellrowborder" valign="top" width="10.341034103410342%" headers="mcps1.2.8.1.1 "><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>AAC Encoder</p>
</td>
<td class="cellrowborder" valign="top" width="9.86098609860986%" headers="mcps1.2.8.1.2 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>8kHz, 16kHz, 22.05kHz, 24kHz, 32kHz,</p>
<p id="p283mcpsimp"><a name="p283mcpsimp"></a><a name="p283mcpsimp"></a>44.1kHz, 48kHz</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.8.1.3 "><a name="ul285mcpsimp"></a><a name="ul285mcpsimp"></a><ul id="ul285mcpsimp"><li>AACLC supports 1024;</li><li>EAAC and EAACPLUS support 2048;</li><li>AACLD and AACELD support 512.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.4 "><p id="p290mcpsimp"><a name="p290mcpsimp"></a><a name="p290mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.5 "><p id="p292mcpsimp"><a name="p292mcpsimp"></a><a name="p292mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.6 "><p id="p294mcpsimp"><a name="p294mcpsimp"></a><a name="p294mcpsimp"></a>50 MHz</p>
</td>
<td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.2.8.1.7 "><p id="p296mcpsimp"><a name="p296mcpsimp"></a><a name="p296mcpsimp"></a>AAC has undergone two breakthrough technology upgrades:</p>
<a name="ul297mcpsimp"></a><a name="ul297mcpsimp"></a><ul id="ul297mcpsimp"><li>aacPlus1 (i.e., EAAC), adds SBR (Spectral Band Replication) technology, enabling the codec to achieve the same audio quality at half the bitrate.</li><li>aacPlus2 (i.e., EAACPLUS), adds PS (Parametric Stereo) technology, providing excellent audio quality at low bitrates. aacPlus2 can achieve CD quality at 48 kbit/s.</li><li>AAC-LD and AAC-ELD are low-delay voice codec processing solutions. AAC-LD is a public safety industry standard requirement, and AAC-ELD is the encoding format for future communications.</li></ul>
<p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>Bitstream ranges and recommended bitrate settings are shown in <a href="#_Ref342555172">Table 2</a> and <a href="#_Ref224621074">Table 3</a>.</p>
</td>
</tr>
<tr id="row305mcpsimp"><td class="cellrowborder" valign="top" width="10.341034103410342%" headers="mcps1.2.8.1.1 "><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>AAC Decoder</p>
</td>
<td class="cellrowborder" valign="top" width="9.86098609860986%" headers="mcps1.2.8.1.2 "><p id="p309mcpsimp"><a name="p309mcpsimp"></a><a name="p309mcpsimp"></a>Compatible with all rates</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.8.1.3 "><p id="p311mcpsimp"><a name="p311mcpsimp"></a><a name="p311mcpsimp"></a>512, 1024, 2048</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.4 "><p id="p313mcpsimp"><a name="p313mcpsimp"></a><a name="p313mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.8.1.5 "><p id="p315mcpsimp"><a name="p315mcpsimp"></a><a name="p315mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.8.1.6 "><p id="p317mcpsimp"><a name="p317mcpsimp"></a><a name="p317mcpsimp"></a>25 MHz</p>
</td>
<td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.2.8.1.7 "><p id="p319mcpsimp"><a name="p319mcpsimp"></a><a name="p319mcpsimp"></a>Backward compatible. Traditional AAC decoders only decode low-frequency information of aacPlus v1 streams, while aacPlus decoders can restore high-frequency information as well. AAC decoders that do not support PS will only obtain mono information when decoding aacPlus v2 streams, while aacPlus2 decoders can produce stereo sound. Note: The decoding mode should use ADEC_MODE_STREAM.</p>
</td>
</tr>
</tbody>
</table>

Note: The "CPU consumption" result values are based on an ARM9 288 MHz environment. 2/2 MHz indicates that encoding and decoding each consume 2M and 2M CPU, respectively.

**Table 2**  AAC Encoder bitrate settings for each protocol (bitrate unit: kbps)

<a name="_Ref342555172"></a>
<table><thead align="left"><tr id="row332mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.9.1.1"><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>Sample Rate</p>
</th>
<th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.9.1.2"><p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>Channel</p>
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
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p363mcpsimp"><a name="p363mcpsimp"></a><a name="p363mcpsimp"></a>16 to 48</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p365mcpsimp"><a name="p365mcpsimp"></a><a name="p365mcpsimp"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p367mcpsimp"><a name="p367mcpsimp"></a><a name="p367mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p371mcpsimp"><a name="p371mcpsimp"></a><a name="p371mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p373mcpsimp"><a name="p373mcpsimp"></a><a name="p373mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row374mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p376mcpsimp"><a name="p376mcpsimp"></a><a name="p376mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p378mcpsimp"><a name="p378mcpsimp"></a><a name="p378mcpsimp"></a>16 to 96</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p380mcpsimp"><a name="p380mcpsimp"></a><a name="p380mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p386mcpsimp"><a name="p386mcpsimp"></a><a name="p386mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row389mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p391mcpsimp"><a name="p391mcpsimp"></a><a name="p391mcpsimp"></a>16kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p393mcpsimp"><a name="p393mcpsimp"></a><a name="p393mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p395mcpsimp"><a name="p395mcpsimp"></a><a name="p395mcpsimp"></a>24 to 96</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>24 to 48</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p405mcpsimp"><a name="p405mcpsimp"></a><a name="p405mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row406mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>24 to 192</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p412mcpsimp"><a name="p412mcpsimp"></a><a name="p412mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p414mcpsimp"><a name="p414mcpsimp"></a><a name="p414mcpsimp"></a>24 to 96</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p416mcpsimp"><a name="p416mcpsimp"></a><a name="p416mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p418mcpsimp"><a name="p418mcpsimp"></a><a name="p418mcpsimp"></a>16 to 48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p420mcpsimp"><a name="p420mcpsimp"></a><a name="p420mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row421mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p423mcpsimp"><a name="p423mcpsimp"></a><a name="p423mcpsimp"></a>22.05kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p425mcpsimp"><a name="p425mcpsimp"></a><a name="p425mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>32 to 132</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p429mcpsimp"><a name="p429mcpsimp"></a><a name="p429mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p431mcpsimp"><a name="p431mcpsimp"></a><a name="p431mcpsimp"></a>32 to 64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p433mcpsimp"><a name="p433mcpsimp"></a><a name="p433mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p435mcpsimp"><a name="p435mcpsimp"></a><a name="p435mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row438mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p440mcpsimp"><a name="p440mcpsimp"></a><a name="p440mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p442mcpsimp"><a name="p442mcpsimp"></a><a name="p442mcpsimp"></a>32 to 265</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p444mcpsimp"><a name="p444mcpsimp"></a><a name="p444mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p446mcpsimp"><a name="p446mcpsimp"></a><a name="p446mcpsimp"></a>32 to 128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p448mcpsimp"><a name="p448mcpsimp"></a><a name="p448mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p450mcpsimp"><a name="p450mcpsimp"></a><a name="p450mcpsimp"></a>16 to 64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p452mcpsimp"><a name="p452mcpsimp"></a><a name="p452mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row453mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p455mcpsimp"><a name="p455mcpsimp"></a><a name="p455mcpsimp"></a>24kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p457mcpsimp"><a name="p457mcpsimp"></a><a name="p457mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p459mcpsimp"><a name="p459mcpsimp"></a><a name="p459mcpsimp"></a>32 to 144</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p461mcpsimp"><a name="p461mcpsimp"></a><a name="p461mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p463mcpsimp"><a name="p463mcpsimp"></a><a name="p463mcpsimp"></a>32 to 64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p465mcpsimp"><a name="p465mcpsimp"></a><a name="p465mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row470mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p472mcpsimp"><a name="p472mcpsimp"></a><a name="p472mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p474mcpsimp"><a name="p474mcpsimp"></a><a name="p474mcpsimp"></a>32 to 288</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p476mcpsimp"><a name="p476mcpsimp"></a><a name="p476mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p478mcpsimp"><a name="p478mcpsimp"></a><a name="p478mcpsimp"></a>32 to 128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p480mcpsimp"><a name="p480mcpsimp"></a><a name="p480mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p482mcpsimp"><a name="p482mcpsimp"></a><a name="p482mcpsimp"></a>16 to 64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p484mcpsimp"><a name="p484mcpsimp"></a><a name="p484mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row485mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p487mcpsimp"><a name="p487mcpsimp"></a><a name="p487mcpsimp"></a>32kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p489mcpsimp"><a name="p489mcpsimp"></a><a name="p489mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p491mcpsimp"><a name="p491mcpsimp"></a><a name="p491mcpsimp"></a>32 to 192</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p493mcpsimp"><a name="p493mcpsimp"></a><a name="p493mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p495mcpsimp"><a name="p495mcpsimp"></a><a name="p495mcpsimp"></a>32 to 64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p499mcpsimp"><a name="p499mcpsimp"></a><a name="p499mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p501mcpsimp"><a name="p501mcpsimp"></a><a name="p501mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row502mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p504mcpsimp"><a name="p504mcpsimp"></a><a name="p504mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p506mcpsimp"><a name="p506mcpsimp"></a><a name="p506mcpsimp"></a>32 to 320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p508mcpsimp"><a name="p508mcpsimp"></a><a name="p508mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p510mcpsimp"><a name="p510mcpsimp"></a><a name="p510mcpsimp"></a>32 to 128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p512mcpsimp"><a name="p512mcpsimp"></a><a name="p512mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p514mcpsimp"><a name="p514mcpsimp"></a><a name="p514mcpsimp"></a>16 to 64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p516mcpsimp"><a name="p516mcpsimp"></a><a name="p516mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row517mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>44.1kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p521mcpsimp"><a name="p521mcpsimp"></a><a name="p521mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p523mcpsimp"><a name="p523mcpsimp"></a><a name="p523mcpsimp"></a>48 to 265</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p525mcpsimp"><a name="p525mcpsimp"></a><a name="p525mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p527mcpsimp"><a name="p527mcpsimp"></a><a name="p527mcpsimp"></a>32 to 64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p529mcpsimp"><a name="p529mcpsimp"></a><a name="p529mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p531mcpsimp"><a name="p531mcpsimp"></a><a name="p531mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p533mcpsimp"><a name="p533mcpsimp"></a><a name="p533mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row534mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p536mcpsimp"><a name="p536mcpsimp"></a><a name="p536mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p538mcpsimp"><a name="p538mcpsimp"></a><a name="p538mcpsimp"></a>48 to 320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p540mcpsimp"><a name="p540mcpsimp"></a><a name="p540mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>32 to 128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p546mcpsimp"><a name="p546mcpsimp"></a><a name="p546mcpsimp"></a>16 to 64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p548mcpsimp"><a name="p548mcpsimp"></a><a name="p548mcpsimp"></a>48</p>
</td>
</tr>
<tr id="row549mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="10.891089108910892%" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p551mcpsimp"><a name="p551mcpsimp"></a><a name="p551mcpsimp"></a>48kHz</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p553mcpsimp"><a name="p553mcpsimp"></a><a name="p553mcpsimp"></a>Mono</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p555mcpsimp"><a name="p555mcpsimp"></a><a name="p555mcpsimp"></a>48 to 288</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p559mcpsimp"><a name="p559mcpsimp"></a><a name="p559mcpsimp"></a>32 to 64</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p561mcpsimp"><a name="p561mcpsimp"></a><a name="p561mcpsimp"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.9.1.5 "><p id="p563mcpsimp"><a name="p563mcpsimp"></a><a name="p563mcpsimp"></a>--</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.9.1.5 "><p id="p565mcpsimp"><a name="p565mcpsimp"></a><a name="p565mcpsimp"></a>--</p>
</td>
</tr>
<tr id="row566mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.9.1.1 mcps1.2.9.2.1 "><p id="p568mcpsimp"><a name="p568mcpsimp"></a><a name="p568mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.2 mcps1.2.9.2.2 "><p id="p570mcpsimp"><a name="p570mcpsimp"></a><a name="p570mcpsimp"></a>48 to 320</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.3 "><p id="p572mcpsimp"><a name="p572mcpsimp"></a><a name="p572mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.3 mcps1.2.9.2.4 "><p id="p574mcpsimp"><a name="p574mcpsimp"></a><a name="p574mcpsimp"></a>32 to 128</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.5 "><p id="p576mcpsimp"><a name="p576mcpsimp"></a><a name="p576mcpsimp"></a>64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.4 mcps1.2.9.2.6 "><p id="p578mcpsimp"><a name="p578mcpsimp"></a><a name="p578mcpsimp"></a>16 to 64</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.9.1.5 "><p id="p580mcpsimp"><a name="p580mcpsimp"></a><a name="p580mcpsimp"></a>48</p>
</td>
</tr>
</tbody>
</table>

Note: "--" indicates this scenario is not supported.

**Table 3**  AAC Encoder Low Delay protocol bitrate settings (bitrate unit: kbps)

<a name="_Ref224621074"></a>
<table><thead align="left"><tr id="row592mcpsimp"><th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.7.1.1"><p id="p594mcpsimp"><a name="p594mcpsimp"></a><a name="p594mcpsimp"></a>Sample Rate</p>
</th>
<th class="cellrowborder" rowspan="2" valign="top" id="mcps1.2.7.1.2"><p id="p596mcpsimp"><a name="p596mcpsimp"></a><a name="p596mcpsimp"></a>Channel</p>
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
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p617mcpsimp"><a name="p617mcpsimp"></a><a name="p617mcpsimp"></a>16 to 96</p>
</td>
<td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.7.1.3 mcps1.2.7.2.4 "><p id="p619mcpsimp"><a name="p619mcpsimp"></a><a name="p619mcpsimp"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.4 "><p id="p621mcpsimp"><a name="p621mcpsimp"></a><a name="p621mcpsimp"></a>32 to 96</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.7.1.4 "><p id="p623mcpsimp"><a name="p623mcpsimp"></a><a name="p623mcpsimp"></a>32</p>
</td>
</tr>
<tr id="row624mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.2.1 "><p id="p626mcpsimp"><a name="p626mcpsimp"></a><a name="p626mcpsimp"></a>Stereo</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 mcps1.2.7.2.2 "><p id="p628mcpsimp"><a name="p628mcpsimp"></a><a name="p628mcpsimp"></a>16 to 192</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 mcps1.2.7.2.3 "><p id="p630mcpsimp"><a name="p630mcpsimp"></a><a name="p630mcpsimp"></a>48</p>
</td></tr></tbody></table>

Note: "--" indicates this scenario is not supported.

(remaining AAC Encoder Low Delay bitrate table data continues with similar rows for 16kHz, 22.05kHz, 24kHz, 32kHz, 44.1kHz, and 48kHz sample rates for both Mono and Stereo channels, following the same pattern)

## API Reference<a name="ZH-CN_TOPIC_0000002441714649"></a>

The following APIs in the SDK release package are used for registering and unregistering encoders and decoders.

-   [ss\_mpi\_aenc\_register\_encoder](#ZH-CN_TOPIC_0000002408115490): Registers an encoder.
-   [ss\_mpi\_aenc\_unregister\_encoder](#ZH-CN_TOPIC_0000002441714653): Unregisters an encoder.
-   [ss\_mpi\_adec\_register\_decoder](#ZH-CN_TOPIC_0000002408115474): Registers a decoder.
-   [ss\_mpi\_adec\_unregister\_decoder](#ZH-CN_TOPIC_0000002408275418): Unregisters a decoder.

Registration examples provided in the audio component:

-   [ss\_mpi\_aenc\_aac\_init](#ZH-CN_TOPIC_0000002408275398): Registers the AAC encoder.
-   [ss\_mpi\_adec\_aac\_init](#ZH-CN_TOPIC_0000002441714637): Registers the AAC decoder.

### ss\_mpi\_aenc\_register\_encoder<a name="ZH-CN_TOPIC_0000002408115490"></a>

[Description]

Registers an encoder.

[Syntax]

```
td_s32 ss_mpi_aenc_register_encoder(td_s32 *handle, const ot_aenc_encoder *encoder);
```

[Parameters]

<a name="table837mcpsimp"></a>
<table><thead align="left"><tr id="row843mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.1.4.1.2"><p id="p847mcpsimp"><a name="p847mcpsimp"></a><a name="p847mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.4.1.3"><p id="p849mcpsimp"><a name="p849mcpsimp"></a><a name="p849mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row851mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p853mcpsimp"><a name="p853mcpsimp"></a><a name="p853mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.4.1.2 "><p id="p855mcpsimp"><a name="p855mcpsimp"></a><a name="p855mcpsimp"></a>Registration handle.</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p857mcpsimp"><a name="p857mcpsimp"></a><a name="p857mcpsimp"></a>Output</p>
</td>
</tr>
<tr id="row858mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p860mcpsimp"><a name="p860mcpsimp"></a><a name="p860mcpsimp"></a>encoder</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.1.4.1.2 "><p id="p862mcpsimp"><a name="p862mcpsimp"></a><a name="p862mcpsimp"></a>Encoder attribute structure.</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.4.1.3 "><p id="p864mcpsimp"><a name="p864mcpsimp"></a><a name="p864mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table866mcpsimp"></a>
<table><thead align="left"><tr id="row871mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p873mcpsimp"><a name="p873mcpsimp"></a><a name="p873mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p875mcpsimp"><a name="p875mcpsimp"></a><a name="p875mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row877mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p879mcpsimp"><a name="p879mcpsimp"></a><a name="p879mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p881mcpsimp"><a name="p881mcpsimp"></a><a name="p881mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row882mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p884mcpsimp"><a name="p884mcpsimp"></a><a name="p884mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p886mcpsimp"><a name="p886mcpsimp"></a><a name="p886mcpsimp"></a>Failed. See <a href="#ZH-CN_TOPIC_0000002408115506">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_comm\_aenc.h, ss\_mpi\_audio.h
-   Library file: libss\_mpi.a

[Notes]

-   Users register an encoder with the AENC module by passing the encoder attribute structure, and a registration handle is returned. Users can later unregister the encoder using this handle.
-   The AENC module can register up to 20 encoders and already has LPCM, G711a, G711u, G726, and ADPCM encoders pre-registered.
-   The same encoding protocol cannot be registered multiple times. For example, if an AAC encoder has already been registered, another AAC encoder cannot be registered.
-   Encoder attributes include the encoder type, maximum stream length, encoder name, function pointers for opening the encoder, encoding, and closing the encoder.
    -   Encoder type
        The SDK uses enums to identify encoding protocols. The corresponding encoder type for the protocol should be selected during registration.
    -   Maximum stream length
        The maximum length of the encoded stream per frame. The AENC module will allocate memory based on the registered maximum stream length.
    -   Encoder name
        The encoder name is represented as a string and is used for display in proc information.
    -   Function pointer for opening the encoder
        A function pointer encapsulated by the SDK, with the prototype:
        td\_s32  (*func\_open\_encoder)(td\_void \*encoder\_attr, td\_void \*\*encoder);
        The first parameter is the encoder attribute for passing specific attributes of different encoder types; the second parameter is the encoder handle for returning a handle that can operate the encoder. Both parameters are encapsulated by the user. When encapsulating the second parameter, memory allocation should be considered, as the encoder handle will also be used for encoding and closing the encoder.
    -   Function pointer for encoding
        A function pointer encapsulated by the SDK, with the prototype:
        td\_s32  (*func\_enc\_frame)(td\_void \*encoder, const ot\_audio\_frame \*data, td\_u8 \*out\_buf, td\_u32 \*out\_len);
        The first parameter is the encoder handle returned when the encoder was opened; the second parameter is a pointer to the SDK's audio frame data structure for passing audio frame data; the third parameter is the output buffer pointer; the fourth parameter is the output buffer length.
    -   Function pointer for closing the encoder
        A function pointer encapsulated by the SDK, with the prototype:
        td\_s32  (*func\_close\_encoder)(td\_void \*encoder);
        The parameter is the encoder handle returned when the encoder was opened.
    -   Users need to encapsulate third-party encoders based on these function prototypes and register them with the AENC module through the encoder attribute structure, thereby integrating third-party encoders.
-   The relevant encoder type must be registered before creating an encoding channel. Encoders do not need to be registered repeatedly.

[Example]

The following code illustrates the registration of an AAC encoder:

```
td_s32 handle, ret;
aenc_encoder aac;
 
ret = aac_init_enc_lib();
if (ret) {
    return ret;
}
 
aac.type = OT_PT_AAC;
snprintf(aac.name, sizeof(aac.name), "aac");
aac.max_frame_len = MAX_AAC_MAINBUF_SIZE;
aac.func_open_encoder = open_aac_encoder;
aac.func_enc_frame = encode_aac_frm;
aac.func_close_encoder = close_aac_encoder;
ret = ss_mpi_aenc_register_encoder(&handle, &aac);
if (ret) {
    return ret;
}
    
 return TD_SUCCESS;
```

[Related Topics]

None.

### ss\_mpi\_aenc\_unregister\_encoder<a name="ZH-CN_TOPIC_0000002441714653"></a>

[Description]

Unregisters an encoder.

[Syntax]

```
td_s32 ss_mpi_aenc_unregister_encoder(td_s32 handle);
```

[Parameters]

<a name="table947mcpsimp"></a>
<table><thead align="left"><tr id="row953mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p955mcpsimp"><a name="p955mcpsimp"></a><a name="p955mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="66.34%" id="mcps1.1.4.1.2"><p id="p957mcpsimp"><a name="p957mcpsimp"></a><a name="p957mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.1.4.1.3"><p id="p959mcpsimp"><a name="p959mcpsimp"></a><a name="p959mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row961mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p xml:lang="it-IT" id="p963mcpsimp"><a name="p963mcpsimp"></a><a name="p963mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="66.34%" headers="mcps1.1.4.1.2 "><p id="p965mcpsimp"><a name="p965mcpsimp"></a><a name="p965mcpsimp"></a>Registration handle (obtained when registering the encoder).</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.1.4.1.3 "><p id="p967mcpsimp"><a name="p967mcpsimp"></a><a name="p967mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

(Standard return value table - 0 for success, non-0 for failure referring to Error Codes)

[Requirements]

-   Header files: ot\_comm\_aenc.h, ss\_mpi\_audio.h
-   Library file: libss\_mpi.a

[Notes]

Unregistering an encoder is generally not necessary.

### ss\_mpi\_adec\_register\_decoder<a name="ZH-CN_TOPIC_0000002408115474"></a>

[Description]

Registers a decoder.

[Syntax]

```
td_s32 ss_mpi_adec_register_decoder(td_s32 *handle, const ot_adec_decoder *decoder);
```

[Parameters]

(Standard parameter table - handle is the registration handle output, decoder is the decoder attribute structure input)

[Requirements]

-   Header files: ot\_comm\_adec.h, ss\_mpi\_audio.h
-   Library file: libss\_mpi.a

[Notes]

-   Users register a decoder with the ADEC module by passing the decoder attribute structure, and a registration handle is returned.
-   The ADEC module can register up to 20 decoders and already has LPCM, G711a, G711u, G726, and ADPCM decoders pre-registered.
-   Decoder attributes include the decoder type, decoder name, function pointers for opening the decoder, decoding, getting frame info, and closing the decoder.
-   The relevant decoder type must be registered before creating a decoding channel.

### ss\_mpi\_adec\_unregister\_decoder<a name="ZH-CN_TOPIC_0000002408275418"></a>

[Description]

Unregisters a decoder. Generally not necessary.

### ss\_mpi\_aenc\_aac\_init<a name="ZH-CN_TOPIC_0000002408275398"></a>

[Description]

Registers the AAC encoder.

[Syntax]

```
td_s32 ss_mpi_aenc_aac_init(td_void);
```

[Parameters]

None.

[Requirements]

-   Source file: audio\_aac\_adp.c
-   Header file: audio\_aac\_adp.h
-   Library files: libaac\_comm.so, libaac\_enc.so

[Notes]

This interface is implemented in audio\_aac\_adp.c, which is not packaged as a library. Therefore, when using this interface, audio\_aac\_adp.c and audio\_aac\_adp.h must be included for compilation. These two files are placed in the sample/audio/adp folder by default. Additionally, when SBRENC functionality is needed, the libaac\_sbr\_enc.so library must be added.

### ss\_mpi\_adec\_aac\_init<a name="ZH-CN_TOPIC_0000002441714637"></a>

[Description]

Registers the AAC decoder. (Similar structure to the encoder init)

# Data Types<a name="ZH-CN_TOPIC_0000002441674769"></a>

The audio component related data types and data structures are defined as follows:

-   [ot\_aenc\_encoder](#ZH-CN_TOPIC_0000002408275394): Defines the encoder attribute structure.
-   [ot\_adec\_decoder](#ZH-CN_TOPIC_0000002441714629): Defines the decoder attribute structure.
-   [ot\_aac\_type](#ZH-CN_TOPIC_0000002441674777): Defines the AAC audio codec protocol type.
-   [ot\_aac\_bps](#ZH-CN_TOPIC_0000002408275382): Defines the AAC audio encoding bitrate.
-   [ot\_aac\_transport\_type](#ZH-CN_TOPIC_0000002408115466): Defines the AAC audio codec protocol transport encapsulation type.
-   [ot\_aenc\_attr\_aac](#ZH-CN_TOPIC_0000002408115470): Defines the AAC encoding protocol attribute structure.
-   [ot\_adec\_attr\_aac](#ZH-CN_TOPIC_0000002441714625): Defines the AAC decoding protocol attribute structure.

## ot\_aenc\_encoder<a name="ZH-CN_TOPIC_0000002408275394"></a>

[Description]

Defines the encoder attribute structure.

[Definition]

```
typedef struct {
    ot_payload_type type;
    td_u32          max_frame_len;
    ot_char         name[OT_MAX_ENCODER_NAME_LEN];
    td_s32          (*func_open_encoder)(td_void *encoder_attr, td_void **encoder);
    td_s32          (*func_enc_frame)(td_void *encoder, const ot_audio_frame *data, td_u8 *out_buf, td_u32 *out_len);
    td_s32          (*func_close_encoder)(td_void *encoder);
} ot_aenc_encoder;
```

[Members]

<a name="table1290mcpsimp"></a>
<table><thead align="left"><tr id="row1295mcpsimp"><th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.1"><p id="p1297mcpsimp"><a name="p1297mcpsimp"></a><a name="p1297mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.2"><p id="p1299mcpsimp"><a name="p1299mcpsimp"></a><a name="p1299mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1301mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1303mcpsimp"><a name="p1303mcpsimp"></a><a name="p1303mcpsimp"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1305mcpsimp"><a name="p1305mcpsimp"></a><a name="p1305mcpsimp"></a>Encoding protocol type. See the "System Control" chapter of the "MPP Media Processing Software V5.0 Development Reference".</p>
</td>
</tr>
<tr id="row1306mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1308mcpsimp"><a name="p1308mcpsimp"></a><a name="p1308mcpsimp"></a>max_frame_len</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1310mcpsimp"><a name="p1310mcpsimp"></a><a name="p1310mcpsimp"></a>Maximum stream length.</p>
</td>
</tr>
<tr id="row1311mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1313mcpsimp"><a name="p1313mcpsimp"></a><a name="p1313mcpsimp"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1315mcpsimp"><a name="p1315mcpsimp"></a><a name="p1315mcpsimp"></a>Encoder name. OT_MAX_ENCODER_NAME_LEN is defined in the "Audio" chapter of the "MPP Media Processing Software V5.0 Development Reference".</p>
</td>
</tr>
<tr id="row1322mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1324mcpsimp"><a name="p1324mcpsimp"></a><a name="p1324mcpsimp"></a>func_open_encoder</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1326mcpsimp"><a name="p1326mcpsimp"></a><a name="p1326mcpsimp"></a>Function pointer for opening the encoder.</p>
</td>
</tr>
<tr id="row1327mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1329mcpsimp"><a name="p1329mcpsimp"></a><a name="p1329mcpsimp"></a>func_enc_frame</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1331mcpsimp"><a name="p1331mcpsimp"></a><a name="p1331mcpsimp"></a>Function pointer for encoding. For detailed description, see the "Audio" chapter of the "MPP Media Processing Software V5.0 Development Reference".</p>
</td>
</tr>
<tr id="row1334mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p xml:lang="fr-FR" id="p1336mcpsimp"><a name="p1336mcpsimp"></a><a name="p1336mcpsimp"></a>func_close_encoder</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p1338mcpsimp"><a name="p1338mcpsimp"></a><a name="p1338mcpsimp"></a>Function pointer for closing the encoder.</p>
</td>
</tr>
</tbody>
</table>

## ot\_adec\_decoder<a name="ZH-CN_TOPIC_0000002441714629"></a>

[Description]

Defines the decoder attribute structure.

[Definition]

```
typedef struct {
    ot_payload_type type;
    ot_char name[OT_MAX_DECODER_NAME_LEN];
    td_s32 (*func_open_decoder)(td_void *decoder_attr, td_void **decoder);
    td_s32 (*func_dec_frame)(td_void *decoder, td_u8 **in_buf, td_s32 *left_byte, td_u16 *out_buf, td_u32 *out_len, td_u32 *chns);
    td_s32 (*func_get_frame_info)(td_void *decoder, td_void *info);
    td_s32 (*func_close_decoder)(td_void *decoder);
    td_s32 (*func_reset_decoder)(td_void *decoder);
} ot_adec_decoder;
```

## ot\_aac\_type<a name="ZH-CN_TOPIC_0000002441674777"></a>

[Description]

Defines the AAC audio codec protocol type.

[Definition]

```
typedef enum {
    OT_AAC_TYPE_AACLC       = 0,
    OT_AAC_TYPE_EAAC        = 1,   /* eAAC format (also known as HEAAC, AAC+, or aacPlusV1) */
    OT_AAC_TYPE_EAACPLUS   = 2,   /* eAACPLUS format (also known as AAC++ or aacPlusV2) */
    OT_AAC_TYPE_AACLD       = 3,
    OT_AAC_TYPE_AACELD     = 4,
    OT_AAC_TYPE_BUTT,
} ot_aac_type;
```

## ot\_aac\_bps<a name="ZH-CN_TOPIC_0000002408275382"></a>

[Description]

Defines the AAC audio encoding bitrate.

[Definition]

```
typedef enum {
    OT_AAC_BPS_8K      = 8000,
    OT_AAC_BPS_16K     = 16000,
    OT_AAC_BPS_22K     = 22000,
    OT_AAC_BPS_24K     = 24000,
    OT_AAC_BPS_32K     = 32000,
    OT_AAC_BPS_48K     = 48000,
    OT_AAC_BPS_64K     = 64000,
    OT_AAC_BPS_96K     = 96000,
    OT_AAC_BPS_128K    = 128000,
    OT_AAC_BPS_256K    = 256000,
    OT_AAC_BPS_320K    = 320000,
    OT_AAC_BPS_BUTT
} ot_aac_bps;
```

## ot\_aac\_transport\_type<a name="ZH-CN_TOPIC_0000002408115466"></a>

[Description]

Defines the AAC audio codec protocol transport encapsulation type.

[Definition]

```
typedef enum {
    OT_AAC_TRANSPORT_TYPE_ADTS = 0,
    OT_AAC_TRANSPORT_TYPE_LOAS = 1,
    OT_AAC_TRANSPORT_TYPE_LATM_MCP1 = 2,
    OT_AAC_TRANSPORT_TYPE_BUTT
} ot_aac_transport_type;
```

[Notes]

The LATM1 format does not have a sync frame header mechanism. If stream issues occur, it cannot recover quickly. **Not recommended**.

## ot\_aenc\_attr\_aac<a name="ZH-CN_TOPIC_0000002408115470"></a>

[Description]

Defines the AAC encoding protocol attribute structure.

[Definition]

```
typedef struct {
    ot_aac_type          aac_type;
    ot_aac_bps           bit_rate;
    ot_audio_sample_rate sample_rate;
    ot_audio_bit_width   bit_width;
    ot_audio_snd_mode  snd_mode;
    ot_aac_transport_type    transport_type;
    td_s16              band_width;
} ot_aenc_attr_aac;
```

## ot\_adec\_attr\_aac<a name="ZH-CN_TOPIC_0000002441714625"></a>

[Description]

Defines the AAC decoding protocol attribute structure.

[Definition]

```
typedef struct {
     ot_aac_transport_type  transport_type;
} ot_adec_attr_aac;
```

# Error Codes<a name="ZH-CN_TOPIC_0000002408115506"></a>

## Audio Encoding Error Codes<a name="ZH-CN_TOPIC_0000002441674781"></a>

**Table 1**  Audio encoding API error codes

<a name="_Ref268526472"></a>
<table><thead align="left"><tr id="row1727mcpsimp"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p1729mcpsimp"><a name="p1729mcpsimp"></a><a name="p1729mcpsimp"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.4.1.2"><p id="p1731mcpsimp"><a name="p1731mcpsimp"></a><a name="p1731mcpsimp"></a>Macro Definition</p>
</th>
<th class="cellrowborder" valign="top" width="33.663366336633665%" id="mcps1.2.4.1.3"><p id="p1733mcpsimp"><a name="p1733mcpsimp"></a><a name="p1733mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1735mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1737mcpsimp"><a name="p1737mcpsimp"></a><a name="p1737mcpsimp"></a>0xa0178001</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1739mcpsimp"><a name="p1739mcpsimp"></a><a name="p1739mcpsimp"></a>OT_ERR_AENC_INVALID_DEV_ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1741mcpsimp"><a name="p1741mcpsimp"></a><a name="p1741mcpsimp"></a>Invalid audio device ID</p>
</td>
</tr>
<tr id="row1742mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1744mcpsimp"><a name="p1744mcpsimp"></a><a name="p1744mcpsimp"></a>0xa0178003</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1746mcpsimp"><a name="p1746mcpsimp"></a><a name="p1746mcpsimp"></a>OT_ERR_AENC_INVALID_CHN_ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1748mcpsimp"><a name="p1748mcpsimp"></a><a name="p1748mcpsimp"></a>Invalid audio encoding channel number</p>
</td>
</tr>
<tr id="row1749mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1751mcpsimp"><a name="p1751mcpsimp"></a><a name="p1751mcpsimp"></a>0xa0178007</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1753mcpsimp"><a name="p1753mcpsimp"></a><a name="p1753mcpsimp"></a>OT_ERR_AENC_ILLEGAL_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1755mcpsimp"><a name="p1755mcpsimp"></a><a name="p1755mcpsimp"></a>Invalid audio encoding parameter</p>
</td>
</tr>
<tr id="row1756mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1758mcpsimp"><a name="p1758mcpsimp"></a><a name="p1758mcpsimp"></a>0xa0178008</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1760mcpsimp"><a name="p1760mcpsimp"></a><a name="p1760mcpsimp"></a>OT_ERR_AENC_EXIST</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1762mcpsimp"><a name="p1762mcpsimp"></a><a name="p1762mcpsimp"></a>Audio encoding channel already created</p>
</td>
</tr>
<tr id="row1763mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1765mcpsimp"><a name="p1765mcpsimp"></a><a name="p1765mcpsimp"></a>0xa0178009</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1767mcpsimp"><a name="p1767mcpsimp"></a><a name="p1767mcpsimp"></a>OT_ERR_AENC_UNEXIST</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1769mcpsimp"><a name="p1769mcpsimp"></a><a name="p1769mcpsimp"></a>Audio encoding channel not created</p>
</td>
</tr>
<tr id="row1770mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1772mcpsimp"><a name="p1772mcpsimp"></a><a name="p1772mcpsimp"></a>0xa017800a</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1774mcpsimp"><a name="p1774mcpsimp"></a><a name="p1774mcpsimp"></a>OT_ERR_AENC_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1776mcpsimp"><a name="p1776mcpsimp"></a><a name="p1776mcpsimp"></a>NULL pointer in input parameters</p>
</td>
</tr>
<tr id="row1777mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1779mcpsimp"><a name="p1779mcpsimp"></a><a name="p1779mcpsimp"></a>0xa017800b</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1781mcpsimp"><a name="p1781mcpsimp"></a><a name="p1781mcpsimp"></a>OT_ERR_AENC_NOT_CFG</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1783mcpsimp"><a name="p1783mcpsimp"></a><a name="p1783mcpsimp"></a>Encoding channel not configured</p>
</td>
</tr>
<tr id="row1784mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1786mcpsimp"><a name="p1786mcpsimp"></a><a name="p1786mcpsimp"></a>0xa017800c</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1788mcpsimp"><a name="p1788mcpsimp"></a><a name="p1788mcpsimp"></a>OT_ERR_AENC_NOT_SUPPORT</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1790mcpsimp"><a name="p1790mcpsimp"></a><a name="p1790mcpsimp"></a>Operation not supported</p>
</td>
</tr>
<tr id="row1791mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1793mcpsimp"><a name="p1793mcpsimp"></a><a name="p1793mcpsimp"></a>0xa017800d</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1795mcpsimp"><a name="p1795mcpsimp"></a><a name="p1795mcpsimp"></a>OT_ERR_AENC_NOT_PERM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1797mcpsimp"><a name="p1797mcpsimp"></a><a name="p1797mcpsimp"></a>Operation not permitted</p>
</td>
</tr>
<tr id="row1798mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1800mcpsimp"><a name="p1800mcpsimp"></a><a name="p1800mcpsimp"></a>0xa0178014</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1802mcpsimp"><a name="p1802mcpsimp"></a><a name="p1802mcpsimp"></a>OT_ERR_AENC_NO_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1804mcpsimp"><a name="p1804mcpsimp"></a><a name="p1804mcpsimp"></a>Insufficient system memory</p>
</td>
</tr>
<tr id="row1805mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1807mcpsimp"><a name="p1807mcpsimp"></a><a name="p1807mcpsimp"></a>0xa0178015</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1809mcpsimp"><a name="p1809mcpsimp"></a><a name="p1809mcpsimp"></a>OT_ERR_AENC_NO_BUF</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1811mcpsimp"><a name="p1811mcpsimp"></a><a name="p1811mcpsimp"></a>Encoding channel buffer allocation failed</p>
</td>
</tr>
<tr id="row1812mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1814mcpsimp"><a name="p1814mcpsimp"></a><a name="p1814mcpsimp"></a>0xa0178016</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1816mcpsimp"><a name="p1816mcpsimp"></a><a name="p1816mcpsimp"></a>OT_ERR_AENC_BUF_EMPTY</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1818mcpsimp"><a name="p1818mcpsimp"></a><a name="p1818mcpsimp"></a>Encoding channel buffer empty</p>
</td>
</tr>
<tr id="row1819mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1821mcpsimp"><a name="p1821mcpsimp"></a><a name="p1821mcpsimp"></a>0xa0178017</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1823mcpsimp"><a name="p1823mcpsimp"></a><a name="p1823mcpsimp"></a>OT_ERR_AENC_BUF_FULL</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1825mcpsimp"><a name="p1825mcpsimp"></a><a name="p1825mcpsimp"></a>Encoding channel buffer full</p>
</td>
</tr>
<tr id="row1826mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1828mcpsimp"><a name="p1828mcpsimp"></a><a name="p1828mcpsimp"></a>0xa0178018</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1830mcpsimp"><a name="p1830mcpsimp"></a><a name="p1830mcpsimp"></a>OT_ERR_AENC_NOT_READY</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1832mcpsimp"><a name="p1832mcpsimp"></a><a name="p1832mcpsimp"></a>System not initialized</p>
</td>
</tr>
<tr id="row1833mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1835mcpsimp"><a name="p1835mcpsimp"></a><a name="p1835mcpsimp"></a>0xa0178040</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1837mcpsimp"><a name="p1837mcpsimp"></a><a name="p1837mcpsimp"></a>OT_ERR_AENC_ENCODER_ERR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1839mcpsimp"><a name="p1839mcpsimp"></a><a name="p1839mcpsimp"></a>Audio encoding data error</p>
</td>
</tr>
<tr id="row1840mcpsimp"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p1842mcpsimp"><a name="p1842mcpsimp"></a><a name="p1842mcpsimp"></a>0xa0178041</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.4.1.2 "><p xml:lang="de-DE" id="p1844mcpsimp"><a name="p1844mcpsimp"></a><a name="p1844mcpsimp"></a>OT_ERR_AENC_VQE_ERR</p>
</td>
<td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.4.1.3 "><p xml:lang="de-DE" id="p1846mcpsimp"><a name="p1846mcpsimp"></a><a name="p1846mcpsimp"></a>AENC VQE processing error</p>
</td>
</tr>
</tbody>
</table>

## Audio Decoding Error Codes<a name="ZH-CN_TOPIC_0000002408275374"></a>

(The audio decoding error codes follow a similar pattern with the prefix OT_ERR_ADEC_ and corresponding descriptions.)
