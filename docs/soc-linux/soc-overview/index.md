---
title: "总体介绍"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/SS928V100 超高清智能网络录像机 SoC 产品简介/SS928V100 超高清智能网络录像机 SoC 产品简介.md
---

# 总体介绍
SS928V100是一颗面向市场推出的专业超高清智能网络录像机SoC。该芯片最高支持四路sensor输入，支持最高4K60的ISP图像处理能力，支持3F WDR、多级降噪、六轴防抖、硬件拼接等多种图像增强和处理算法，为用户提供了卓越的图像处理能力。

SS928V100内置四核A55，提供高效且丰富和灵活的CPU资源，以满足客户计算和控制需求。集成单核MCU，以满足某些低延时要求较高场景。

SS928V100集成了高效的图像分析工具推理单元，最高10.4Tops INT8，并支持业界主流的图像分析工具框架。并内置双核Vision DSP，以满足客户一些差异化的CV计算需求。

SS928V100采用先进的12nm低功耗工艺和0.65pitch封装，同时支持LPDDR4/LPDDR4x/DDR4颗粒，满足客户应用的产品小型化设计和快速量产。

SS928V100配套提供的稳定、易用的SDK设计，能够支撑客户快速产品量产。

# 关键特性
-   智能加速
    -   10.4Tops INT8 双NN加速引擎
    -   双核Vision Q6的DSP处理

-   4K60 编解码
    -   支持4K60的H.265/H.264编码。
    -   支持10路1080p30的H.265/H.264解码。

-   支持四路4M实时拼接

    支持4路4Mp30机内实时硬化拼接。

-   高速接口

    支持USB3.0和PCIe2.0高速接口。

-   小型化封装

    采用23mm x 23mm FC-BGA封装形式。

# 主要特点
## 处理器内核<a name="ZH-CN_TOPIC_0000002494991445"></a>

-   四核ARM Cortex A55@1.4GHz
    -   32KB I-Cache，32KB D-Cache /512KB L3 cache
    -   支持Neon加速，集成FPU处理单元

-   内置32bit MCU@500MHz
    -   32KB I-Cache，32KB D-Cache /64KB TCM

## 智能视频分析<a name="ZH-CN_TOPIC_0000002461672396"></a>

-   图像分析加速引擎，高达10.4Tops@INT8算力
    -   双内核异构引擎
    -   引擎1 支持4.8Tops算力，支持INT4/INT8/FP16
    -   引擎2 支持5.6Tops算力，支持INT8/INT16
    -   支持完整的API和工具链，易于客户开发

-   双核Vision Q6 DSP
    -   32K I-Cache /32K D-Cache /32K IRAM/320K DRAM

-   内置智能计算加速引擎
-   内置双目深度加速单元
-   内置矩阵计算加速单元

## 视频编解码<a name="ZH-CN_TOPIC_0000002494871485"></a>

-   H.264 BP/MP/HP
-   H.265 Main Profile
-   H.264/H.265编解码最大分辨率为8192 x 8192
-   H.264/H.265 编码支持I/P帧
-   H.264/H.265多码流编码能力：
    -   3840 x 2160@60fps + 1280x720@30fps
    -   7680 x 4320@15fps

-   H.264/H.265/MPEG-4多码流解码能力：
    -   3840 x 2160@60fps + 1920x1080@60fps

-   支持最多8个区域的编码前OSD叠加
-   支持CBR/VBR/AVBR/FIXQP/QPMAP等多种码率控制模式
-   输出码率最大值160Mbps
-   支持8个感兴趣区域（ROI）编码
-   支持JPEG Baseline编解码
-   JPEG编解码最大分辨率16384x16384
-   JPEG最大性能
    -   编码：3840 x 2160@60fps \(YUV420\)
    -   解码：3840 x 2160@75fps \(YUV420\)

## 视频输入接口<a name="ZH-CN_TOPIC_0000002461831988"></a>

-   支持8-Lane image sensor串行输入，支持 MIPI/LVDS/Sub-LVDS/HiSPi多种接口
-   支持2x4-Lane或4x2-Lane等多种组合，最高支持4路sensor串行输入
-   最大分辨率8192 x 8192
-   支持8/10/12/14 Bit RGB Bayer DC时序视频输入，时钟频率最高150MHz
-   支持BT.601、BT.656、BT.1120视频输入接口
-   支持主流CMOS电平热成像传感器

## 数字图像处理（ISP）<a name="ZH-CN_TOPIC_0000002494991449"></a>

-   ISP支持分时复用处理多路sensor输入视频
-   支持3A（AE/AWB/AF）功能，3A的控制用户可调节
-   支持去固定模式噪声（FPN）
-   支持坏点校正、镜头阴影校正；
-   最高支持三帧WDR及Advanced Local Tone Mapping
-   支持多级3D去噪、图像边缘增强、去雾、动态对比度增强等处理功能
-   支持3D-LUT色彩调节
-   支持镜头畸变校正，支持鱼眼矫正
-   支持6-DoF数字防抖及Rolling-Shutter校正
-   支持图像Mirror、Flip、90度/270度旋转
-   提供 PC端ISP 调节工具
-   支持超感光去噪（HNR）

## 视频与图形处理<a name="ZH-CN_TOPIC_0000002461672400"></a>

-   支持图形和图像1/15.5～16x缩放功能
-   支持多达4路视频全景拼接
    -   输入2路3840x2160@30fps，输出4320x3840@30fps
    -   输入4路2688x1520@30fps，输出6080x2688@30fps

-   支持视频层、图形层叠加
-   支持色彩空间转换

## 视频输出<a name="ZH-CN_TOPIC_0000002494871489"></a>

-   支持HDMI2.0接口输出
-   支持4-Lane Mipi DSI/CSI接口输出，最高2.5Gbps/lane
-   内置模拟标清CVBS输出
-   支持8/16/24 bit RGB、BT.656、BT.1120等数字接口
-   同时支持2个独立高清视频输出
    -   支持任意两种接口非同源输出
    -   其中一路可支持PIP\(Picture In Picture\)

-   最大输出能力3840x2160@60fps + 1920x1080@60fps

## 音频接口与处理<a name="ZH-CN_TOPIC_0000002461831992"></a>

-   内置Audio codec，支持16bit 语音输入和输出
-   支持I2S接口
    -   支持多声道时分复用传输模式（TDM）

-   支持HDMI Audio输出
-   通过软件实现多协议语音编解码
-   支持音频3A（AEC/ANR/ALC）处理
-   支持G.711/G.726/AAC/等音频编码格式

## 安全隔离与引擎<a name="ZH-CN_TOPIC_0000002494991453"></a>

-   支持安全启动
-   支持基于TrustZone的REE/TEE硬件隔离方案
-   硬件实现AES对称加密算法
-   硬件实现RSA2048/3072/4096签名校验算法
-   硬件实现基于HASH的SHA/256/384/512、HMAC\_SHA256/384/512算法
-   硬件实现随机数发生器
-   集成30Kbit OTP存储空间供客户使用

## 网络接口<a name="ZH-CN_TOPIC_0000002461672404"></a>

-   2个千兆以太网接口
    -   支持RGMII、RMII两种接口模式
    -   支持TSO、UFO、COE等加速单元
    -   支持Jumbo Frame

## 外围接口<a name="ZH-CN_TOPIC_0000002494871493"></a>

-   支持上电复位（POR）和外部输入复位
-   集成4通道LSADC
-   多个UART、I<sup>2</sup>C、SPI、GPIO接口
-   2个SDIO3.0接口
    -   SDIO0支持SDXC卡，最大容量2TB
    -   SDIO1支持对接wifi模组

-   2个USB3.0/USB2.0接口
    -   USB0 仅Host接口
    -   USB1 Host/Device可切换

-   2-Lane PCIe2.0高速接口
    -   支持RC/EP模式
    -   可配置为2-Lane PCIe2.0
    -   可配置为1-Lane PCIe2.0 + USB3.0

## 外部存储器接口<a name="ZH-CN_TOPIC_0000002461831996"></a>

-   DDR4/LPDDR4/LPDDR4x接口
    -   支持4 x 16bit DDR4
    -   支持2 x 32bit LPDDR4/LPDDR4x
    -   DDR4最高速率3200Mbps
    -   LPDDR4/LPDDR4x最高速率3733Mbps
    -   最大容量8GB

-   SPI Nor/SPI Nand Flash接口
    -   支持1、2、4线模式
    -   SPI Nor Flash支持3Byte、4Byte 地址模式

-   NAND Flash接口
    -   支持SLC、MLC异步接口器件
    -   支持2/4/8/16KB页大小
    -   支持8/16/24/28/40/64bit ECC（以1KB为单位）

-   eMMC5.1接口，最大容量2TB
-   可选择从eMMC、SPI Nor/SPI Nand Flash、NAND Flash或PCIe从片启动

## SDK<a name="ZH-CN_TOPIC_0000002494991457"></a>

-   Arm CPU支持Linux SMP
-   DSP/MCU支持LiteOS

## 芯片物理规格<a name="ZH-CN_TOPIC_0000002461672408"></a>

-   功耗
    -   5.2W典型功耗\(4K30 + 4Tops\)

-   工作电压
    -   内核电压为0.8V
    -   IO电压为1.8/3.3V
    -   DDR4/LPDDR4/LPDDR4x接口电压分别为1.2/1.1/0.6V

-   封装形式
    -   RoHS，FC-BGA 23mm x 23mm封装
    -   管脚间距：0.65mm

# 功能框图
![](figures/zh-cn_image_0000002495024793.png)

# SS928V100专业智能网络摄像机方案
![](figures/zh-cn_image_0000002462025394.png)

# Acronyms and Abbreviations
<a name="table123mcpsimp"></a>
<table><tbody><tr id="row128mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p130mcpsimp"><a name="p130mcpsimp"></a><a name="p130mcpsimp"></a>3DNR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p132mcpsimp"><a name="p132mcpsimp"></a><a name="p132mcpsimp"></a>three-dimensional noise reduction</p>
</td>
</tr>
<tr id="row133mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p135mcpsimp"><a name="p135mcpsimp"></a><a name="p135mcpsimp"></a>AAC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p137mcpsimp"><a name="p137mcpsimp"></a><a name="p137mcpsimp"></a>advanced audio coding</p>
</td>
</tr>
<tr id="row138mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p140mcpsimp"><a name="p140mcpsimp"></a><a name="p140mcpsimp"></a>AE</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p142mcpsimp"><a name="p142mcpsimp"></a><a name="p142mcpsimp"></a>automatic exposure</p>
</td>
</tr>
<tr id="row143mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p145mcpsimp"><a name="p145mcpsimp"></a><a name="p145mcpsimp"></a>AEC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p147mcpsimp"><a name="p147mcpsimp"></a><a name="p147mcpsimp"></a>acoustic echo control</p>
</td>
</tr>
<tr id="row148mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p150mcpsimp"><a name="p150mcpsimp"></a><a name="p150mcpsimp"></a>AES</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p152mcpsimp"><a name="p152mcpsimp"></a><a name="p152mcpsimp"></a>advanced encryption standard</p>
</td>
</tr>
<tr id="row153mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>AF</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>automatic focus</p>
</td>
</tr>
<tr id="row158mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p160mcpsimp"><a name="p160mcpsimp"></a><a name="p160mcpsimp"></a>ALC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p162mcpsimp"><a name="p162mcpsimp"></a><a name="p162mcpsimp"></a>automatic level control</p>
</td>
</tr>
<tr id="row163mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p165mcpsimp"><a name="p165mcpsimp"></a><a name="p165mcpsimp"></a>ANR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p167mcpsimp"><a name="p167mcpsimp"></a><a name="p167mcpsimp"></a>adaptive noise reduction</p>
</td>
</tr>
<tr id="row168mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p170mcpsimp"><a name="p170mcpsimp"></a><a name="p170mcpsimp"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p172mcpsimp"><a name="p172mcpsimp"></a><a name="p172mcpsimp"></a>application programming interface</p>
</td>
</tr>
<tr id="row173mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p175mcpsimp"><a name="p175mcpsimp"></a><a name="p175mcpsimp"></a>AVBR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p177mcpsimp"><a name="p177mcpsimp"></a><a name="p177mcpsimp"></a>adaptive variable bit rate</p>
</td>
</tr>
<tr id="row178mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p180mcpsimp"><a name="p180mcpsimp"></a><a name="p180mcpsimp"></a>AVS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p182mcpsimp"><a name="p182mcpsimp"></a><a name="p182mcpsimp"></a>any view stitching</p>
</td>
</tr>
<tr id="row183mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p185mcpsimp"><a name="p185mcpsimp"></a><a name="p185mcpsimp"></a>AWB</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>automatic white balance</p>
</td>
</tr>
<tr id="row188mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p190mcpsimp"><a name="p190mcpsimp"></a><a name="p190mcpsimp"></a>CAC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p192mcpsimp"><a name="p192mcpsimp"></a><a name="p192mcpsimp"></a>chromatic aberration correction</p>
</td>
</tr>
<tr id="row193mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p195mcpsimp"><a name="p195mcpsimp"></a><a name="p195mcpsimp"></a>CBR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p197mcpsimp"><a name="p197mcpsimp"></a><a name="p197mcpsimp"></a>constant bit rate</p>
</td>
</tr>
<tr id="row198mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p200mcpsimp"><a name="p200mcpsimp"></a><a name="p200mcpsimp"></a>CMOS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p202mcpsimp"><a name="p202mcpsimp"></a><a name="p202mcpsimp"></a>complementary metal-oxide-semiconductor</p>
</td>
</tr>
<tr id="row203mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p205mcpsimp"><a name="p205mcpsimp"></a><a name="p205mcpsimp"></a>CV</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p207mcpsimp"><a name="p207mcpsimp"></a><a name="p207mcpsimp"></a>computer vision</p>
</td>
</tr>
<tr id="row208mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p210mcpsimp"><a name="p210mcpsimp"></a><a name="p210mcpsimp"></a>codec</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a>coder/decoder</p>
</td>
</tr>
<tr id="row213mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>CSI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p217mcpsimp"><a name="p217mcpsimp"></a><a name="p217mcpsimp"></a>camera serial interface</p>
</td>
</tr>
<tr id="row218mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p220mcpsimp"><a name="p220mcpsimp"></a><a name="p220mcpsimp"></a>DC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p222mcpsimp"><a name="p222mcpsimp"></a><a name="p222mcpsimp"></a>digital camera</p>
</td>
</tr>
<tr id="row223mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p225mcpsimp"><a name="p225mcpsimp"></a><a name="p225mcpsimp"></a>DCI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p227mcpsimp"><a name="p227mcpsimp"></a><a name="p227mcpsimp"></a>dynamic contrast improvement</p>
</td>
</tr>
<tr id="row228mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p230mcpsimp"><a name="p230mcpsimp"></a><a name="p230mcpsimp"></a>DDR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p232mcpsimp"><a name="p232mcpsimp"></a><a name="p232mcpsimp"></a>double data rate</p>
</td>
</tr>
<tr id="row233mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p235mcpsimp"><a name="p235mcpsimp"></a><a name="p235mcpsimp"></a>DDRC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p237mcpsimp"><a name="p237mcpsimp"></a><a name="p237mcpsimp"></a>double data rate controller</p>
</td>
</tr>
<tr id="row238mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p240mcpsimp"><a name="p240mcpsimp"></a><a name="p240mcpsimp"></a>DIS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p242mcpsimp"><a name="p242mcpsimp"></a><a name="p242mcpsimp"></a>digital image stabilization</p>
</td>
</tr>
<tr id="row243mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p245mcpsimp"><a name="p245mcpsimp"></a><a name="p245mcpsimp"></a>DPU</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p247mcpsimp"><a name="p247mcpsimp"></a><a name="p247mcpsimp"></a>depth processing unit</p>
</td>
</tr>
<tr id="row248mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p250mcpsimp"><a name="p250mcpsimp"></a><a name="p250mcpsimp"></a>DSI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p252mcpsimp"><a name="p252mcpsimp"></a><a name="p252mcpsimp"></a>display serial interface</p>
</td>
</tr>
<tr id="row253mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p255mcpsimp"><a name="p255mcpsimp"></a><a name="p255mcpsimp"></a>DSP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p257mcpsimp"><a name="p257mcpsimp"></a><a name="p257mcpsimp"></a>digital signal processor</p>
</td>
</tr>
<tr id="row258mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p260mcpsimp"><a name="p260mcpsimp"></a><a name="p260mcpsimp"></a>ECC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p262mcpsimp"><a name="p262mcpsimp"></a><a name="p262mcpsimp"></a>error-correcting code</p>
</td>
</tr>
<tr id="row263mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p265mcpsimp"><a name="p265mcpsimp"></a><a name="p265mcpsimp"></a>eMMC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a>embedded multimedia card</p>
</td>
</tr>
<tr id="row268mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a>EP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p272mcpsimp"><a name="p272mcpsimp"></a><a name="p272mcpsimp"></a>endpoint</p>
</td>
</tr>
<tr id="row273mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p275mcpsimp"><a name="p275mcpsimp"></a><a name="p275mcpsimp"></a>FCCSP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p277mcpsimp"><a name="p277mcpsimp"></a><a name="p277mcpsimp"></a>flip-chip chip scale package</p>
</td>
</tr>
<tr id="row278mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>FPN</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>fixed pattern noise</p>
</td>
</tr>
<tr id="row283mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p285mcpsimp"><a name="p285mcpsimp"></a><a name="p285mcpsimp"></a>FPU</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p287mcpsimp"><a name="p287mcpsimp"></a><a name="p287mcpsimp"></a>floating-point unit</p>
</td>
</tr>
<tr id="row288mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p290mcpsimp"><a name="p290mcpsimp"></a><a name="p290mcpsimp"></a>GE</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p292mcpsimp"><a name="p292mcpsimp"></a><a name="p292mcpsimp"></a>gigabit Ethernet</p>
</td>
</tr>
<tr id="row293mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p295mcpsimp"><a name="p295mcpsimp"></a><a name="p295mcpsimp"></a>GMAC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p297mcpsimp"><a name="p297mcpsimp"></a><a name="p297mcpsimp"></a>Gigabit Ethernet Media Access Controller</p>
</td>
</tr>
<tr id="row298mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p300mcpsimp"><a name="p300mcpsimp"></a><a name="p300mcpsimp"></a>GPIO</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>general-purpose input/output</p>
</td>
</tr>
<tr id="row303mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p305mcpsimp"><a name="p305mcpsimp"></a><a name="p305mcpsimp"></a>GUI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>graphical user interface</p>
</td>
</tr>
<tr id="row308mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p310mcpsimp"><a name="p310mcpsimp"></a><a name="p310mcpsimp"></a>HD</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p312mcpsimp"><a name="p312mcpsimp"></a><a name="p312mcpsimp"></a>high definition</p>
</td>
</tr>
<tr id="row313mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p315mcpsimp"><a name="p315mcpsimp"></a><a name="p315mcpsimp"></a>HiSPI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p317mcpsimp"><a name="p317mcpsimp"></a><a name="p317mcpsimp"></a>high-speed serial pixel interface</p>
</td>
</tr>
<tr id="row318mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p320mcpsimp"><a name="p320mcpsimp"></a><a name="p320mcpsimp"></a>I<sup id="sup321mcpsimp"><a name="sup321mcpsimp"></a><a name="sup321mcpsimp"></a>2</sup>C</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p323mcpsimp"><a name="p323mcpsimp"></a><a name="p323mcpsimp"></a>inter-integrated circuit</p>
</td>
</tr>
<tr id="row324mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p326mcpsimp"><a name="p326mcpsimp"></a><a name="p326mcpsimp"></a>I<sup id="sup327mcpsimp"><a name="sup327mcpsimp"></a><a name="sup327mcpsimp"></a>2</sup>S</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p329mcpsimp"><a name="p329mcpsimp"></a><a name="p329mcpsimp"></a>inter-IC sound</p>
</td>
</tr>
<tr id="row330mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p332mcpsimp"><a name="p332mcpsimp"></a><a name="p332mcpsimp"></a>ISP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>image signal processor</p>
</td>
</tr>
<tr id="row335mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p337mcpsimp"><a name="p337mcpsimp"></a><a name="p337mcpsimp"></a>IVE</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p339mcpsimp"><a name="p339mcpsimp"></a><a name="p339mcpsimp"></a>intelligent video engine</p>
</td>
</tr>
<tr id="row340mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p342mcpsimp"><a name="p342mcpsimp"></a><a name="p342mcpsimp"></a>LCD</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p344mcpsimp"><a name="p344mcpsimp"></a><a name="p344mcpsimp"></a>liquid crystal display</p>
</td>
</tr>
<tr id="row345mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p347mcpsimp"><a name="p347mcpsimp"></a><a name="p347mcpsimp"></a>LGDC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p349mcpsimp"><a name="p349mcpsimp"></a><a name="p349mcpsimp"></a>lens geometric distortion correction</p>
</td>
</tr>
<tr id="row350mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p352mcpsimp"><a name="p352mcpsimp"></a><a name="p352mcpsimp"></a>LPDDR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p354mcpsimp"><a name="p354mcpsimp"></a><a name="p354mcpsimp"></a>low-power double data rate</p>
</td>
</tr>
<tr id="row355mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p357mcpsimp"><a name="p357mcpsimp"></a><a name="p357mcpsimp"></a>LSADC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>low-speed analog-to-digital converter</p>
</td>
</tr>
<tr id="row360mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p362mcpsimp"><a name="p362mcpsimp"></a><a name="p362mcpsimp"></a>LUT</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p364mcpsimp"><a name="p364mcpsimp"></a><a name="p364mcpsimp"></a>lookup table</p>
</td>
</tr>
<tr id="row365mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p367mcpsimp"><a name="p367mcpsimp"></a><a name="p367mcpsimp"></a>LVDS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>low-voltage differential signaling</p>
</td>
</tr>
<tr id="row370mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>MAU</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p374mcpsimp"><a name="p374mcpsimp"></a><a name="p374mcpsimp"></a>matrix arithmetic unit</p>
</td>
</tr>
<tr id="row375mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p377mcpsimp"><a name="p377mcpsimp"></a><a name="p377mcpsimp"></a>MCU</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p379mcpsimp"><a name="p379mcpsimp"></a><a name="p379mcpsimp"></a>microcontroller unit</p>
</td>
</tr>
<tr id="row380mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>MIC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a>microphone</p>
</td>
</tr>
<tr id="row385mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>MIPI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>mobile industry processor interface</p>
</td>
</tr>
<tr id="row390mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p392mcpsimp"><a name="p392mcpsimp"></a><a name="p392mcpsimp"></a>NR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p394mcpsimp"><a name="p394mcpsimp"></a><a name="p394mcpsimp"></a>noise reduction</p>
</td>
</tr>
<tr id="row395mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>OSD</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>on-screen display</p>
</td>
</tr>
<tr id="row400mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p402mcpsimp"><a name="p402mcpsimp"></a><a name="p402mcpsimp"></a>OTP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p404mcpsimp"><a name="p404mcpsimp"></a><a name="p404mcpsimp"></a>one-time programming</p>
</td>
</tr>
<tr id="row405mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p407mcpsimp"><a name="p407mcpsimp"></a><a name="p407mcpsimp"></a>PCIe</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p409mcpsimp"><a name="p409mcpsimp"></a><a name="p409mcpsimp"></a>peripheral component interconnect express</p>
</td>
</tr>
<tr id="row410mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p412mcpsimp"><a name="p412mcpsimp"></a><a name="p412mcpsimp"></a>PIP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p414mcpsimp"><a name="p414mcpsimp"></a><a name="p414mcpsimp"></a>picture-in-picture</p>
</td>
</tr>
<tr id="row415mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p417mcpsimp"><a name="p417mcpsimp"></a><a name="p417mcpsimp"></a>POR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p419mcpsimp"><a name="p419mcpsimp"></a><a name="p419mcpsimp"></a>power-on reset</p>
</td>
</tr>
<tr id="row420mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p422mcpsimp"><a name="p422mcpsimp"></a><a name="p422mcpsimp"></a>PWM</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p424mcpsimp"><a name="p424mcpsimp"></a><a name="p424mcpsimp"></a>pulse-width modulation</p>
</td>
</tr>
<tr id="row425mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>RAM</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p429mcpsimp"><a name="p429mcpsimp"></a><a name="p429mcpsimp"></a>random access memory</p>
</td>
</tr>
<tr id="row430mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p432mcpsimp"><a name="p432mcpsimp"></a><a name="p432mcpsimp"></a>RC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p434mcpsimp"><a name="p434mcpsimp"></a><a name="p434mcpsimp"></a>root complex</p>
</td>
</tr>
<tr id="row435mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>RGB</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p439mcpsimp"><a name="p439mcpsimp"></a><a name="p439mcpsimp"></a>red-green-blue</p>
</td>
</tr>
<tr id="row440mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p442mcpsimp"><a name="p442mcpsimp"></a><a name="p442mcpsimp"></a>RGMII</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p444mcpsimp"><a name="p444mcpsimp"></a><a name="p444mcpsimp"></a>reduced gigabit media-independent interface</p>
</td>
</tr>
<tr id="row445mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p447mcpsimp"><a name="p447mcpsimp"></a><a name="p447mcpsimp"></a>RMII</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p449mcpsimp"><a name="p449mcpsimp"></a><a name="p449mcpsimp"></a>reduced media-independent interface</p>
</td>
</tr>
<tr id="row450mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p452mcpsimp"><a name="p452mcpsimp"></a><a name="p452mcpsimp"></a>RoHS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p454mcpsimp"><a name="p454mcpsimp"></a><a name="p454mcpsimp"></a>restriction of hazardous substances</p>
</td>
</tr>
<tr id="row455mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p457mcpsimp"><a name="p457mcpsimp"></a><a name="p457mcpsimp"></a>ROI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p459mcpsimp"><a name="p459mcpsimp"></a><a name="p459mcpsimp"></a>region of interest</p>
</td>
</tr>
<tr id="row460mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p462mcpsimp"><a name="p462mcpsimp"></a><a name="p462mcpsimp"></a>RSA</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a>Rivest-Shamir-Adleman</p>
</td>
</tr>
<tr id="row465mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>RNG</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>random number generator</p>
</td>
</tr>
<tr id="row470mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p472mcpsimp"><a name="p472mcpsimp"></a><a name="p472mcpsimp"></a>SD</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p474mcpsimp"><a name="p474mcpsimp"></a><a name="p474mcpsimp"></a>secure digital</p>
</td>
</tr>
<tr id="row475mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p477mcpsimp"><a name="p477mcpsimp"></a><a name="p477mcpsimp"></a>SDIO</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p479mcpsimp"><a name="p479mcpsimp"></a><a name="p479mcpsimp"></a>secure digital input/output</p>
</td>
</tr>
<tr id="row480mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p482mcpsimp"><a name="p482mcpsimp"></a><a name="p482mcpsimp"></a>SDK</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p484mcpsimp"><a name="p484mcpsimp"></a><a name="p484mcpsimp"></a>software development kit</p>
</td>
</tr>
<tr id="row485mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p487mcpsimp"><a name="p487mcpsimp"></a><a name="p487mcpsimp"></a>SDRAM</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p489mcpsimp"><a name="p489mcpsimp"></a><a name="p489mcpsimp"></a>synchronous dynamic random access memory</p>
</td>
</tr>
<tr id="row490mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p492mcpsimp"><a name="p492mcpsimp"></a><a name="p492mcpsimp"></a>SDXC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p494mcpsimp"><a name="p494mcpsimp"></a><a name="p494mcpsimp"></a>secure digital extended capacity</p>
</td>
</tr>
<tr id="row495mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>SMP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p499mcpsimp"><a name="p499mcpsimp"></a><a name="p499mcpsimp"></a>symmetric multiprocessing</p>
</td>
</tr>
<tr id="row500mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p502mcpsimp"><a name="p502mcpsimp"></a><a name="p502mcpsimp"></a>SoC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p504mcpsimp"><a name="p504mcpsimp"></a><a name="p504mcpsimp"></a>system-on-chip</p>
</td>
</tr>
<tr id="row505mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p507mcpsimp"><a name="p507mcpsimp"></a><a name="p507mcpsimp"></a>SPI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p509mcpsimp"><a name="p509mcpsimp"></a><a name="p509mcpsimp"></a>serial peripheral interface</p>
</td>
</tr>
<tr id="row510mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p512mcpsimp"><a name="p512mcpsimp"></a><a name="p512mcpsimp"></a>TDM</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p514mcpsimp"><a name="p514mcpsimp"></a><a name="p514mcpsimp"></a>time division multiplexing</p>
</td>
</tr>
<tr id="row515mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p517mcpsimp"><a name="p517mcpsimp"></a><a name="p517mcpsimp"></a>TOPS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>Tera Operations Per Second</p>
</td>
</tr>
<tr id="row520mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p522mcpsimp"><a name="p522mcpsimp"></a><a name="p522mcpsimp"></a>TSO</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p524mcpsimp"><a name="p524mcpsimp"></a><a name="p524mcpsimp"></a>TCP segmentation offload</p>
</td>
</tr>
<tr id="row525mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p527mcpsimp"><a name="p527mcpsimp"></a><a name="p527mcpsimp"></a>TX</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p529mcpsimp"><a name="p529mcpsimp"></a><a name="p529mcpsimp"></a>transmit</p>
</td>
</tr>
<tr id="row530mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p532mcpsimp"><a name="p532mcpsimp"></a><a name="p532mcpsimp"></a>UART</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p534mcpsimp"><a name="p534mcpsimp"></a><a name="p534mcpsimp"></a>universal asynchronous receiver transmitter</p>
</td>
</tr>
<tr id="row535mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p537mcpsimp"><a name="p537mcpsimp"></a><a name="p537mcpsimp"></a>USB</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p539mcpsimp"><a name="p539mcpsimp"></a><a name="p539mcpsimp"></a>Universal Serial Bus</p>
</td>
</tr>
<tr id="row540mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>VBR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>variable bit rate</p>
</td>
</tr>
<tr id="row545mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p547mcpsimp"><a name="p547mcpsimp"></a><a name="p547mcpsimp"></a>VI</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p549mcpsimp"><a name="p549mcpsimp"></a><a name="p549mcpsimp"></a>video input</p>
</td>
</tr>
<tr id="row550mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p552mcpsimp"><a name="p552mcpsimp"></a><a name="p552mcpsimp"></a>VO</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p554mcpsimp"><a name="p554mcpsimp"></a><a name="p554mcpsimp"></a>video output</p>
</td>
</tr>
<tr id="row555mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>VQE</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p559mcpsimp"><a name="p559mcpsimp"></a><a name="p559mcpsimp"></a>voice quality enhancement</p>
</td>
</tr>
<tr id="row560mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p562mcpsimp"><a name="p562mcpsimp"></a><a name="p562mcpsimp"></a>WDR</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p564mcpsimp"><a name="p564mcpsimp"></a><a name="p564mcpsimp"></a>wide dynamic range</p>
</td>
</tr>
</tbody>
</table>

