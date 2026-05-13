---
description: Abbreviations, proper nouns and one-sentence explanations in the Hi3403
  platform
title: Glossary
---

# Glossary

Hi3403 documentation is full of abbreviations. This table gives a one-sentence explanation for each term — helping newcomers get up to speed.

## Chips and Subsystems

`Hi3403V100` / `Hi3403V100`
: Two names for the same chip. Hi3403 is the product code name, Hi3403V100 is the chip code name,
Completely equivalent. Comes with Hi3519AV200 (lite version with one less NPU cluster).

`SoC`
: System on Chip. Integrate CPU, NPU, ISP, codecs, and various IO controllers
into a chip.

`A55`
: ARM Cortex-A55 processor core. Hi3403V100 has 4 A55s and runs Linux and
User space program.

`SVP`
: Smart Vision Platform 2.0 - NPU of Hi3403. Run AI model inference.
    [Reference](/multimedia/svp/)

`ISP`
: Image Signal Processor——Image signal processor. Take the RAW output from the sensor
Data is processed into viewable YUV/RGB (Denoising, White Balance, Color, HDR, Gamma…).
    [Reference](../multimedia/isp/index.md)

`MPP`
: Media Processing Platform - HiSilicon's multimedia processing software framework. video collection,
Codec, image processing, audio, and display output are all in MPP.
    [Reference](../multimedia/mpp/index.md)

`MMZ`
: Media Memory Zone——Media memory area. Physical contiguous memory pool used by MPP,
Avoid common Linux memory fragmentation issues.

`NMA`
: Non-cacheable Memory Allocator - non-cacheable memory allocator,
Buffer used for DMA transfers.

## Multimedia Subsystem

`VI`
: Video Input——Video input. Collect images from sensor / MIPI-CSI.

`VO`
: Video Output——Video output. to HDMI/MIPI-DSI/VGA.

`VPSS`
: Video Process SubSystem——Video processing subsystem. Zoom, crop,
Color space conversion.

`VENC` / `VDEC`
: Video Encoder / Decoder - H.264 / H.265 / JPEG encoder/decoder.

`AENC` / `ADEC` / `AI` / `AO`
: Audio encoding/decoding/input/output.

`AEC` / `ANS`
:   Acoustic Echo Cancellation / Acoustic Noise Suppression.

`TDE`
: Two-Dimensional Engine - 2D graphics hardware accelerator.
    [Reference](/reference/api/tde/)

`GFBG`
: Graphics FrameBuffer Group——Graphics framebuffer management.
    [Reference](../multimedia/graphics/gfbg/index.md)

`GDC`
: Geometric Distortion Correction——Geometric distortion correction subsystem.
Straighten the image of the fisheye lens.

## AI/computer vision

`ATC`
: Ascend Tensor Compiler - model converter. Put Caffe / ONNX / PyTorch
The model is converted into an SVP executable `.om` file.
    [Reference](../multimedia/atc/index.md)

`AMCT`
: Ascend Model Compression Tool - model quantification tool. FP32 → INT8/INT16,
The model becomes smaller and runs faster.
    [Reference](../multimedia/amct/index.md)

`IVE`
: Intelligent Video Engine - traditional computer vision hardware accelerator
(Histogram, Canny, Morphology, Optical Flow...).
    [Reference](/reference/api/ive/)

`IVS`
: Intelligent Video System - Video structuring framework.

`DPU`
: Depth Processing Unit——Depth perception module (binocular parallax, etc.).

`HNR`
: Heterogeneous NR (Noise Reduction)——Heterogeneous noise reduction.
    [Reference](../multimedia/cv/hnr/index.md)

`DIS`
: Digital Image Stabilization——Digital image stabilization.
    [Reference](../multimedia/dis/index.md)

`MotionFusion`
: Fusion of motion information (gyroscope/IMU) and image information for electronic image stabilization and super-resolution.
    [Reference](../multimedia/motionfusion/index.md)

## Security and encryption

`KLAD`
: Key Ladder - Key derivation hardware unit.
    [Reference](/reference/api/klad/)

`CIPHER`
: General encryption and decryption hardware accelerator (AES, SM4, SHA, RSA...).
    [Reference](/reference/api/cipher/)

`OTP`
: One-Time Programmable memory - one-time programmable memory, storage device
Keys, Boot configuration, etc.
    [Reference](/reference/api/otp/)

`TBBR`
: Trusted Board Boot Requirements - ARM's Trusted Boot Specification.
The secure boot of Hi3403 is based on TBBR.

`TF-A` / `ATF`
: Trusted Firmware-A - ARM's secure boot firmware, running on EL3.
Hi3403 uses v2.2.

## System startup

`U-Boot`
: Universal Bootloader. Hi3403 uses v2020.01.
    [Reference](../soc-linux/uboot/index.md)

`bl31`
: ATF's Stage 3.1 - the last station running in EL3 in the secure boot link,
Then jump to U-Boot or Linux.

`DTB`
: Device Tree Blob - Device tree binary file. Describe the hardware to the kernel.

`eMMC` / `SPI` / `NAND`
: Three boot media. eMMC is the most commonly used onboard Flash; SPI has small capacity but is cheap;
NAND is an industrial control scenario.

## Tools and Platforms

`hi3403-build`
: Community script to build Ubuntu image with one click.
    [Reference](../tools/hi3403-build.md)

`BurnTool`
: HiSilicon’s official graphics flashing tool.
    [Reference](../tools/burntool/index.md)

`MindCmd`
: Board-side command line debugging tool, including AI one-click inference.
    [Reference](../tools/mindcmd/index.md)

`ToolPlatform`
: HiSilicon visual debugging platform.
    [Reference](../tools/toolplatform/index.md)

`SDK`
: Software Development Kit——Hi3403 development kit, including MPP library,
Kernel driver, sample code. There are two variants: GCC-GLIBC and CLANG-MUSL.

## Other common abbreviations

`Hi3403V100` ↔ `Hi3403V100` - see "Chip and Subsystem" above.

`Topeet` / `LubanCat` / `ebaina` / `rkh` / `zsks`
: Development board OEM. They are Xunwei, Yehuo, Yibaina, Runkaihong, and Zhongshan Kuangshi.
    [Development board comparison](../get-started/board-picker.md)

---

Did you find the term? Welcome [Raise a PR](../community/contributing.md) to add a line.