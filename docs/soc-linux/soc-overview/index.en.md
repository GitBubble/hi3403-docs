---
title: "SS928V100 Ultra-HD Intelligent NVR SoC Product Overview"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/SS928V100 超高清智能网络录像机 SoC 产品简介/SS928V100 超高清智能网络录像机 SoC 产品简介.md
---

# General Introduction
SS928V100 is a professional ultra-HD intelligent network video recorder (NVR) SoC. The chip supports up to four sensor inputs and up to 4K60 ISP image processing, along with 3-frame WDR, multi-level noise reduction, 6-axis electronic image stabilization, hardware stitching, and other image enhancement algorithms, delivering exceptional image processing capability.

SS928V100 integrates a quad-core A55 processor, providing efficient and flexible CPU resources for compute and control requirements. An embedded single-core MCU meets the needs of low-latency scenarios.

SS928V100 integrates a high-efficiency AI inference engine with up to 10.4 TOPS INT8, supporting mainstream AI frameworks. Dual-core Vision DSP is embedded to address differentiated CV compute requirements.

SS928V100 is manufactured on an advanced 12 nm low-power process with a 0.65 mm pitch package, and supports LPDDR4/LPDDR4x/DDR4 memory, enabling compact product designs and rapid mass production.

SS928V100 comes with a stable, easy-to-use SDK to support rapid customer product deployment.

# Key Features
-   AI Acceleration
    -   10.4 TOPS INT8 dual NN acceleration engines
    -   Dual-core Vision Q6 DSP processing

-   4K60 Encode/Decode
    -   H.265/H.264 encoding at 4K60.
    -   10-channel 1080p30 H.265/H.264 decoding.

-   4-Channel 4M Real-Time Stitching

    Supports 4-channel 4 Mp30 in-device real-time hardware stitching.

-   High-Speed Interfaces

    Supports USB 3.0 and PCIe 2.0 high-speed interfaces.

-   Compact Package

    23 mm x 23 mm FC-BGA package.

# Key Specifications
## Processor Core<a name="ZH-CN_TOPIC_0000002494991445"></a>

-   Quad-core ARM Cortex-A55 @ 1.4 GHz
    -   32 KB I-Cache, 32 KB D-Cache / 512 KB L3 cache
    -   NEON acceleration, integrated FPU

-   Embedded 32-bit MCU @ 500 MHz
    -   32 KB I-Cache, 32 KB D-Cache / 64 KB TCM

## Intelligent Video Analytics<a name="ZH-CN_TOPIC_0000002461672396"></a>

-   AI acceleration engine, up to 10.4 TOPS @ INT8
    -   Dual-core heterogeneous engine
    -   Engine 1: 4.8 TOPS, supports INT4/INT8/FP16
    -   Engine 2: 5.6 TOPS, supports INT8/INT16
    -   Full API and toolchain support for easy development

-   Dual-core Vision Q6 DSP
    -   32 KB I-Cache / 32 KB D-Cache / 32 KB IRAM / 320 KB DRAM

-   Embedded intelligent compute acceleration engine
-   Embedded binocular depth acceleration unit
-   Embedded matrix compute acceleration unit

## Video Codec<a name="ZH-CN_TOPIC_0000002494871485"></a>

-   H.264 BP/MP/HP
-   H.265 Main Profile
-   H.264/H.265 maximum encode/decode resolution: 8192 x 8192
-   H.264/H.265 encoding supports I/P frames
-   H.264/H.265 multi-stream encoding capability:
    -   3840 x 2160 @ 60 fps + 1280 x 720 @ 30 fps
    -   7680 x 4320 @ 15 fps

-   H.264/H.265/MPEG-4 multi-stream decoding capability:
    -   3840 x 2160 @ 60 fps + 1920 x 1080 @ 60 fps

-   Supports up to 8-region pre-encoding OSD overlay
-   Supports CBR/VBR/AVBR/FIXQP/QPMAP bitrate control modes
-   Maximum output bitrate: 160 Mbps
-   Supports 8 regions of interest (ROI) encoding
-   Supports JPEG Baseline encode/decode
-   JPEG maximum resolution: 16384 x 16384
-   JPEG maximum performance:
    -   Encode: 3840 x 2160 @ 60 fps (YUV420)
    -   Decode: 3840 x 2160 @ 75 fps (YUV420)

## Video Input Interface<a name="ZH-CN_TOPIC_0000002461831988"></a>

-   8-lane image sensor serial input; supports MIPI/LVDS/Sub-LVDS/HiSPi interfaces
-   Supports 2x4-lane or 4x2-lane combinations; up to 4 sensor serial inputs
-   Maximum resolution: 8192 x 8192
-   Supports 8/10/12/14-bit RGB Bayer DC timing video input at up to 150 MHz
-   Supports BT.601, BT.656, BT.1120 video input interfaces
-   Supports mainstream CMOS-level thermal imaging sensors

## Digital Image Processing (ISP)<a name="ZH-CN_TOPIC_0000002494991449"></a>

-   ISP time-division multiplexed processing for multiple sensor inputs
-   Supports 3A (AE/AWB/AF) with user-adjustable control
-   Fixed pattern noise (FPN) correction
-   Bad pixel correction and lens shading correction
-   Up to 3-frame WDR and Advanced Local Tone Mapping
-   Multi-level 3D noise reduction, image edge enhancement, defog, and dynamic contrast enhancement
-   3D-LUT color adjustment
-   Lens geometric distortion correction and fisheye correction
-   6-DoF digital image stabilization (DIS) and Rolling Shutter correction
-   Image mirror, flip, 90°/270° rotation
-   PC-side ISP tuning tool
-   High-sensitivity noise reduction (HNR)

## Video and Graphics Processing<a name="ZH-CN_TOPIC_0000002461672400"></a>

-   1/15.5 to 16x graphics and image scaling
-   Up to 4-channel panoramic video stitching
    -   Input: 2 channels at 3840 x 2160 @ 30 fps; output: 4320 x 3840 @ 30 fps
    -   Input: 4 channels at 2688 x 1520 @ 30 fps; output: 6080 x 2688 @ 30 fps

-   Video layer and graphics layer compositing
-   Color space conversion

## Video Output<a name="ZH-CN_TOPIC_0000002494871489"></a>

-   HDMI 2.0 output
-   4-lane MIPI DSI/CSI output at up to 2.5 Gbps/lane
-   Built-in analog SD CVBS output
-   Supports 8/16/24-bit RGB, BT.656, BT.1120 digital interfaces
-   Two independent HD video outputs simultaneously
    -   Supports any two interfaces with non-synchronized output
    -   One output supports PIP (Picture in Picture)

-   Maximum output: 3840 x 2160 @ 60 fps + 1920 x 1080 @ 60 fps

## Audio Interface and Processing<a name="ZH-CN_TOPIC_0000002461831992"></a>

-   Built-in audio codec supporting 16-bit audio input and output
-   I2S interface
    -   Supports multi-channel time division multiplexing (TDM)

-   HDMI audio output
-   Software-based multi-protocol audio codec
-   Audio 3A processing (AEC/ANR/ALC)
-   Supports G.711/G.726/AAC and other audio encoding formats

## Security Isolation and Engine<a name="ZH-CN_TOPIC_0000002494991453"></a>

-   Secure boot
-   TrustZone-based REE/TEE hardware isolation
-   Hardware AES symmetric encryption
-   Hardware RSA2048/3072/4096 signature verification
-   Hardware SHA-256/384/512 and HMAC\_SHA256/384/512
-   Hardware random number generator (RNG)
-   30 Kbit OTP storage available to customers

## Network Interface<a name="ZH-CN_TOPIC_0000002461672404"></a>

-   2 Gigabit Ethernet interfaces
    -   Supports RGMII and RMII interface modes
    -   Supports TSO, UFO, COE acceleration units
    -   Supports Jumbo Frames

## Peripheral Interfaces<a name="ZH-CN_TOPIC_0000002494871493"></a>

-   Power-on reset (POR) and external reset input
-   4-channel LSADC
-   Multiple UART, I<sup>2</sup>C, SPI, and GPIO interfaces
-   2 SDIO 3.0 interfaces
    -   SDIO0 supports SDXC cards up to 2 TB
    -   SDIO1 supports Wi-Fi module connection

-   2 USB 3.0/USB 2.0 interfaces
    -   USB0: host only
    -   USB1: switchable between host and device

-   2-lane PCIe 2.0 high-speed interface
    -   Supports RC/EP mode
    -   Configurable as 2-lane PCIe 2.0
    -   Configurable as 1-lane PCIe 2.0 + USB 3.0

## External Memory Interface<a name="ZH-CN_TOPIC_0000002461831996"></a>

-   DDR4/LPDDR4/LPDDR4x interface
    -   Supports 4 x 16-bit DDR4
    -   Supports 2 x 32-bit LPDDR4/LPDDR4x
    -   DDR4 max speed: 3200 Mbps
    -   LPDDR4/LPDDR4x max speed: 3733 Mbps
    -   Maximum capacity: 8 GB

-   SPI Nor/SPI NAND Flash interface
    -   Supports 1, 2, and 4-wire modes
    -   SPI Nor Flash supports 3-byte and 4-byte address modes

-   NAND Flash interface
    -   Supports SLC and MLC asynchronous devices
    -   Supports 2/4/8/16 KB page sizes
    -   Supports 8/16/24/28/40/64-bit ECC (per 1 KB unit)

-   eMMC 5.1 interface, maximum capacity 2 TB
-   Boot from eMMC, SPI Nor/SPI NAND Flash, NAND Flash, or PCIe slave

## SDK<a name="ZH-CN_TOPIC_0000002494991457"></a>

-   ARM CPU supports Linux SMP
-   DSP/MCU supports LiteOS

## Physical Specifications<a name="ZH-CN_TOPIC_0000002461672408"></a>

-   Power consumption
    -   5.2 W typical (4K30 + 4 TOPS)

-   Operating voltage
    -   Core voltage: 0.8 V
    -   IO voltage: 1.8/3.3 V
    -   DDR4/LPDDR4/LPDDR4x interface voltage: 1.2/1.1/0.6 V respectively

-   Package
    -   RoHS, FC-BGA 23 mm x 23 mm
    -   Pin pitch: 0.65 mm

# Block Diagram
![](figures/zh-cn_image_0000002495024793.png)

# SS928V100 Professional Intelligent IP Camera Solution
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
