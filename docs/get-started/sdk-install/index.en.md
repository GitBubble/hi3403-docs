---
title: "SS928V100 SDK Installation and Upgrade Guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/SS928V100╱SS927V100 SDK 安装以及升级使用说明/SS928V100╱SS927V100 SDK 安装以及升级使用说明.md
---

# Preface
**Overview<a name="section142mcpsimp"></a>**

This document describes the installation and upgrade procedures for the SS928V100 SDK, enabling users to quickly set up the SDK runtime environment on the corresponding chip's DEMB board.

>![](public_sys-resources/icon-note.gif) **Note:** 
>This document uses SS928V100 as the reference. Unless otherwise specified, the content applies equally to SS927V100.

**Product Versions<a name="section145mcpsimp"></a>**

The product versions corresponding to this document are listed below.

<a name="table148mcpsimp"></a>
<table><thead align="left"><tr id="row153mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row159mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1127814474269"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p632375032618"><a name="p632375032618"></a><a name="p632375032618"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13236502265"><a name="p13236502265"></a><a name="p13236502265"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section164mcpsimp"></a>**

This document is primarily intended for the following engineers:

-   Technical support engineers
-   Software development engineers

**Symbol Conventions<a name="section133020216410"></a>**

The following symbols may appear in this document with the meanings described below.

<a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="/get-started/sdk-install/figures/zh-cn_image_0000002424357674.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>Indicates a high-risk hazard that, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row466863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1432579516410"><a name="p1432579516410"></a><a name="p1432579516410"></a><a name="image4895582316410"></a><a name="image4895582316410"></a><span><img class="" id="image4895582316410" height="25.270000000000003" width="67.83" src="/get-started/sdk-install/figures/zh-cn_image_0000002457876557.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p959197916410"><a name="p959197916410"></a><a name="p959197916410"></a>Indicates a medium-risk hazard that, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row123863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1232579516410"><a name="p1232579516410"></a><a name="p1232579516410"></a><a name="image1235582316410"></a><a name="image1235582316410"></a><span><img class="" id="image1235582316410" height="25.270000000000003" width="67.83" src="/get-started/sdk-install/figures/zh-cn_image_0000002424197818.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p123197916410"><a name="p123197916410"></a><a name="p123197916410"></a>Indicates a low-risk hazard that, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row5786682116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p2204984716410"><a name="p2204984716410"></a><a name="p2204984716410"></a><a name="image4504446716410"></a><a name="image4504446716410"></a><span><img class="" id="image4504446716410" height="25.270000000000003" width="67.83" src="/get-started/sdk-install/figures/zh-cn_image_0000002457836413.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4388861916410"><a name="p4388861916410"></a><a name="p4388861916410"></a>Conveys device or environment safety warnings. Failure to comply may result in device damage, data loss, degraded performance, or other unpredictable outcomes.</p>
<p id="p1238861916410"><a name="p1238861916410"></a><a name="p1238861916410"></a>"Notice" does not involve personal injury.</p>
</td>
</tr>
<tr id="row2856923116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p5555360116410"><a name="p5555360116410"></a><a name="p5555360116410"></a><a name="image799324016410"></a><a name="image799324016410"></a><span><img class="" id="image799324016410" height="25.270000000000003" width="67.83" src="/get-started/sdk-install/figures/zh-cn_image_0000002424197822.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4612588116410"><a name="p4612588116410"></a><a name="p4612588116410"></a>Supplementary information for key points in the main text.</p>
<p id="p1232588116410"><a name="p1232588116410"></a><a name="p1232588116410"></a>"Note" is not a safety warning and does not involve personal, device, or environmental hazards.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section2467512116410"></a>**

<a name="table256mcpsimp"></a>
<table><thead align="left"><tr id="row262mcpsimp"><th class="cellrowborder" valign="top" width="20.97%" id="mcps1.1.4.1.1"><p id="p264mcpsimp"><a name="p264mcpsimp"></a><a name="p264mcpsimp"></a><strong id="b265mcpsimp"><a name="b265mcpsimp"></a><a name="b265mcpsimp"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.029999999999998%" id="mcps1.1.4.1.2"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a><strong id="b268mcpsimp"><a name="b268mcpsimp"></a><a name="b268mcpsimp"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a><strong id="b271mcpsimp"><a name="b271mcpsimp"></a><a name="b271mcpsimp"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row280mcpsimp"><td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.1.4.1.1 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.1.4.1.2 "><p id="p284mcpsimp"><a name="p284mcpsimp"></a><a name="p284mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p286mcpsimp"><a name="p286mcpsimp"></a><a name="p286mcpsimp"></a>First preliminary release.</p>
</td>
</tr>
</tbody>
</table>

# First-Time SDK Installation
If you have already installed the SDK, refer directly to [Installing and Upgrading the SS928V100 DEMO Board Development Environment](#ZH-CN_TOPIC_0000002457836393).

## SS928V100 SDK Package Location<a name="ZH-CN_TOPIC_0000002457876545"></a>

Under the `SS928V100R001***/01.software/board` directory, you will find a file named `SS928V100_SDK_Vx.x.x.x.tgz`. This is the software development kit for SS928V100.

## Extracting the SDK Package<a name="ZH-CN_TOPIC_0000002457836397"></a>

On a Linux server (or a PC running Linux — any mainstream distribution is supported), run `tar -zxf SS928V100_SDK_Vx.x.x.x.tgz` to extract the archive. This produces a directory named `SS928V100_SDK_Vx.x.x.x`.

## Unpacking the SDK Contents<a name="ZH-CN_TOPIC_0000002424197802"></a>

Navigate into the `SS928V100_SDK_Vx.x.x.x` directory and run `./sdk.unpack` (as root or with sudo) to expand the compressed contents of the SDK package. Follow the on-screen prompts to complete the operation.

If you need to copy the SDK package via a Windows system, first run `./sdk.cleanup` to repack the contents, copy to the new location, then expand again.

## Setting Up the Development Environment on a Linux Server<a name="ZH-CN_TOPIC_0000002457876549"></a>

Refer to the *OpenHarmony Small Version User Guide*.

## Building osdrv<a name="ZH-CN_TOPIC_0000002457836389"></a>

Refer to the readme file in the osdrv directory.

## SDK Directory Structure<a name="ZH-CN_TOPIC_0000002457876533"></a>

The `SS928V100_SDK_Vx.x.x.x` directory structure is as follows:

├── smp                             \#smp directory

│   ├── a55\_linux

│       ├── interdrv                  \#mipitx and other driver source code

│       ├── vendor                    \#peripheral driver source code

│       ├── mpp

│       │   ├── component

│       │   │   ├── gfbg              \#gfbg source code

│       │   │   ├── security\_subsys   \#security subsystem source code

│       │   │   └── pciv              \#pciv source code

│       │   ├── cbb

│       │   │   └── isp               \#isp source code

│       │   ├── out                   \#mpp build output directory

│       │       ├── ko                \#kernel ko modules

│      │       ├── lib               \#user-space lib libraries

│      │       ├── include           \#header files

│      │       ├── init              \#kernel module initialization source code

│      │       └── obj               \#kernel module obj files

│      └── osal                      \#OS abstraction layer source code

│           ├── include               \#OS abstraction layer header files

│           └── linux                 \#Linux OS adaptation layer source files

│   ├── dsp\_liteos                     \#DSP driver

├── open\_source                       \#open-source third-party source code

│   ├── u-boot                        \#U-Boot source code

│   ├── linux                         \#kernel source code

│   ├── eigen                         \#eigen source code

│   ...

├── platform                          \#platform code

│   ├── liteos                        \#LiteOS code package

├── osdrv                             \#OS-related directory

│   ├── components                    \#proprietary component source code

│   ├── pub                           \#pre-built images and binaries

│   ├── rootfs\_scripts                \#filesystem initialization directories and scripts

│   ├── tools                         \#system tool source code

├── package                           \#SDK compressed packages

│   ├── smp.tgz                       \#media processing platform software package

│   ├── osdrv.tgz                     \#OS-related package

│   ├── platform.tgz                   \#platform code package

│   └── open\_source.tgz               \#third-party open-source software package

├── scripts                           \#shell scripts directory

├── sdk.cleanup                       \#SDK cleanup script

└── sdk.unpack                        \#SDK unpack script

# Installing and Upgrading the SS928V100 DEMO Board Development Environment
If you are using an SS928V100 DEMO board, you can flash U-Boot, the kernel, and the filesystem using the following procedures. All operations below use the network for updates:

-   If the board does not have U-Boot, use the tool at `01.software/pc/ToolPlatform` to flash it. For detailed flashing instructions, refer to the *BurnTool User Guide* located in the `01.software/pc/ToolPlatform` directory.
-   If the board already has U-Boot, follow the steps below to flash U-Boot, kernel, and rootfs to Flash via the network interface. The DEMO board boots from SPI Flash by default.

## Configuring the TFTP Server<a name="ZH-CN_TOPIC_0000002424197806"></a>

You can use any TFTP server. First build U-Boot, kernel, and rootfs, then copy the resulting files to the TFTP server's root directory.

## Parameter Configuration<a name="ZH-CN_TOPIC_0000002424197814"></a>

After powering on the board, press any key to enter U-Boot. Set serverip (the TFTP server IP), ipaddr (the board IP), and ethaddr (the board's MAC address).

```
setenv serverip xx.xx.xx.xx
setenv ipaddr xx.xx.xx.xx
setenv ethaddr xx:xx:xx:xx:xx:xx
setenv netmask xx.xx.xx.xx
setenv gatewayip xx.xx.xx.xx
ping serverip (verify network connectivity)
```

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>-   SS928V100 supports two boot modes: fast boot (using `u-boot-ss928v100.bin`) and non-fast boot (non-secure/secure boot, using `boot_image.bin`). See Chapter 2 "Boot Modes" in the *SS928V100/SS927V100 Secure Boot User Guide*.
>-   The boot mode can be confirmed by reading register `0x10122090`. A value of `0x5` indicates fast boot; any other value indicates non-fast boot.
>-   Boards ship with "non-secure boot" as the default. The following instructions use this mode as the example.

## Flashing Image Files to SPI Nor Flash<a name="ZH-CN_TOPIC_0000002424357662"></a>

Using a 32 MB SPI Nor Flash as an example. Address space layout:

<a name="table252mcpsimp"></a>
<table><tbody><tr id="row259mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p id="p261mcpsimp"><a name="p261mcpsimp"></a><a name="p261mcpsimp"></a>1MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p263mcpsimp"><a name="p263mcpsimp"></a><a name="p263mcpsimp"></a>11MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p265mcpsimp"><a name="p265mcpsimp"></a><a name="p265mcpsimp"></a>19MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a>1MB</p>
</td>
</tr>
<tr id="row268mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a>boot_image.bin</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p272mcpsimp"><a name="p272mcpsimp"></a><a name="p272mcpsimp"></a>kernel</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p274mcpsimp"><a name="p274mcpsimp"></a><a name="p274mcpsimp"></a>rootfs</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p276mcpsimp"><a name="p276mcpsimp"></a><a name="p276mcpsimp"></a>sample.bin</p>
</td>
</tr>
</tbody>
</table>

The following operations are based on the address space layout shown above. Adjust as needed for your actual configuration.

1.  Flash U-Boot

    ```
    sf probe 0
    mw.b 0x42000000 0xff 0x100000
    tftp 0x42000000 boot_image.bin
    sf probe 0
    sf erase 0 0x100000
    sf write 0x42000000 0 0x100000
    reset
    ```

2.  Flash kernel

    ```
    mw.b 0x42000000 0xff 0xb00000
    tftp 0x42000000 uImage_ss928v100
    sf probe 0
    sf erase 0x100000 0xb00000
    sf write 0x42000000 0x100000 0xb00000
    ```

3.  Flash filesystem

    ```
    mw.b 0x42000000 0xff 0x1300000
    tftp 0x42000000 rootfs_ss928v100_64k.jffs2
    sf probe 0
    sf erase 0xc00000 0x1300000
    sf write 0x42000000 0xc00000 0x1300000
    ```

4.  Flash LiteOS image (optional)

    ```
    mw.b 0x42000000 0xff 0x100000
    tftp 0x42000000 sample.bin
    sf probe 0
    sf erase 0x1f00000 0x100000
    sf write 0x42000000 0x1f00000 0x100000
    ```

5.  Set boot parameters

    ```
    setenv bootargs 'mem=512M console=ttyAMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),11M(kernel),19M(rootfs),1M(sample.bin)';sa
    setenv bootcmd 'sf probe 0;sf read 0x44000000 0x1f00000 0x100000;go_riscv 0x44000000; sf read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa
    Without LiteOS:
    setenv bootargs 'mem=512M console=ttyAMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),11M(kernel),19M(rootfs) ';sa
    setenv bootcmd 'sf probe 0; sf read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa
    ```

## Flashing Image Files to NAND Flash<a name="ZH-CN_TOPIC_0000002457836401"></a>

Using a 64 MB NAND Flash as an example. Address space layout:

<a name="table312mcpsimp"></a>
<table><tbody><tr id="row319mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p id="p321mcpsimp"><a name="p321mcpsimp"></a><a name="p321mcpsimp"></a>1MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p323mcpsimp"><a name="p323mcpsimp"></a><a name="p323mcpsimp"></a>11MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p325mcpsimp"><a name="p325mcpsimp"></a><a name="p325mcpsimp"></a>32MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p327mcpsimp"><a name="p327mcpsimp"></a><a name="p327mcpsimp"></a>1MB</p>
</td>
</tr>
<tr id="row328mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p id="p330mcpsimp"><a name="p330mcpsimp"></a><a name="p330mcpsimp"></a>boot_image.bin</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p332mcpsimp"><a name="p332mcpsimp"></a><a name="p332mcpsimp"></a>kernel</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p334mcpsimp"><a name="p334mcpsimp"></a><a name="p334mcpsimp"></a>rootfs</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p336mcpsimp"><a name="p336mcpsimp"></a><a name="p336mcpsimp"></a>sample.bin</p>
</td>
</tr>
</tbody>
</table>

The following operations are based on the address space layout shown above. Adjust as needed for your actual configuration.

1.  Flash U-Boot

    ```
    mw.b 0x42000000 0xff 0x100000
    tftp 42000000 boot_image.bin
    nand erase 0 0x100000
    nand write 0x42000000 0 0x100000
    reset
    ```

1.  Flash kernel

    ```
    mw.b 0x42000000 0xff 0xb00000
    tftp 0x42000000 uImage_ss928v100
    nand erase 0x100000 0xb00000
    nand write 0x42000000 0x100000 0xb00000
    ```

2.  Flash filesystem

    ```
    mw.b 0x42000000 0xff 0x2000000
    tftp 0x42000000 rootfs_ss928v100_2k_128k_32M.ubifs
    nand erase 0xc00000 0x2000000
    nand write 0x42000000 0xc00000 0x2000000
    ```

3.  Flash LiteOS image (optional)

    ```
    mw.b 0x42000000 0xff 0x100000
    tftp 0x42000000 sample.bin
    nand erase 0x2c00000 0x100000
    nand write 0x42000000 0x2c00000 0x100000
    ```

4.  Set boot parameters

    ```
    setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),11M(kernel),32M(rootfs.ubifs),1M(sample)';sa
    setenv bootcmd 'nand read 0x44000000 0x2c00000 0x100000;go_riscv 0x44000000;nand read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa
    Without LiteOS:
    setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),11M(kernel),32M(rootfs.ubifs) ';sa
    setenv bootcmd 'nand read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa
    ```

## Flashing Image Files to EMMC<a name="ZH-CN_TOPIC_0000002457876529"></a>

Address space layout:

<a name="table367mcpsimp"></a>
<table><tbody><tr id="row374mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p id="p376mcpsimp"><a name="p376mcpsimp"></a><a name="p376mcpsimp"></a>1MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p378mcpsimp"><a name="p378mcpsimp"></a><a name="p378mcpsimp"></a>11MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p380mcpsimp"><a name="p380mcpsimp"></a><a name="p380mcpsimp"></a>96MB</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p382mcpsimp"><a name="p382mcpsimp"></a><a name="p382mcpsimp"></a>1MB</p>
</td>
</tr>
<tr id="row383mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p id="p385mcpsimp"><a name="p385mcpsimp"></a><a name="p385mcpsimp"></a>boot_image.bin</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>kernel</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>rootfs</p>
</td>
<td class="cellrowborder" valign="top" width="25%"><p id="p391mcpsimp"><a name="p391mcpsimp"></a><a name="p391mcpsimp"></a>sample.bin</p>
</td>
</tr>
</tbody>
</table>

The following operations are based on the address space layout shown above. Adjust as needed for your actual configuration.

1.  Flash U-Boot

    ```
    mw.b 0x42000000 0xff 0x100000
    tftp 42000000 boot_image.bin
    mmc write 0 0x42000000 0 0x800
    reset
    ```

2.  Flash kernel

    ```
    mw.b 0x42000000 0xff 0xb00000
    tftp 0x42000000 uImage_ss928v100
    mmc write 0 0x42000000 0x800 0x5800
    ```

3.  Flash filesystem

    ```
    mw.b 0x42000000 0xff 0x6000000
    tftp 0x42000000 rootfs_ss928v100_96M.ext4
    mmc write 0 0x42000000 0x6000 0x30000
    ```

4.  Flash LiteOS image (optional)

    ```
    mw.b 0x42000000 0xff 0x100000
    tftp 0x42000000 sample.bin
    mmc write 0 0x42000000 0x36000 0x800
    ```

5.  Set boot parameters

    ```
    setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(uboot.bin),11M(kernel),96M(rootfs.ext4),1M(sample)';sa
    setenv bootcmd ' mmc read 0 0x44000000 0x36000 0x800;go_riscv 0x44000000;mmc read 0 0x50000000 0x800 0x5800; bootm 50000000';sa
    Without LiteOS:
    setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(uboot.bin),11M(kernel),96M(rootfs.ext4)';sa
    setenv bootcmd 'mmc read 0 0x50000000 0x800 0x5800; bootm 50000000';sa
    ```

    >![](public_sys-resources/icon-notice.gif) **Notice:** 
    >Adjust the image sizes in the commands for [Flashing Image Files to SPI Nor Flash](#ZH-CN_TOPIC_0000002424357662) through [Flashing Image Files to EMMC](#ZH-CN_TOPIC_0000002457876529) to match the actual image sizes. The default LiteOS boot address is `0x44000000`. If the customer's memory layout differs, adjust the LiteOS boot address accordingly. If LiteOS is not used, customers can adjust the Linux boot address instead.

## Booting the New System<a name="ZH-CN_TOPIC_0000002457876541"></a>

reset	\# Reboot to enter the new system.

# Pre-Development Environment Setup
## Pin Multiplexing<a name="ZH-CN_TOPIC_0000002424357658"></a>

Pin multiplexing related to media services, DDR priority configuration, and similar settings are configured in the `interdrv/sys_config` open-source driver (managed via Linux DTS). If the configuration does not match your hardware, you can modify it directly. The `sys_config.ko` driver is called by `load_ss928v100` and is executed before MPP kernel modules are loaded.

Pin multiplexing for non-MPP peripherals is configured uniformly in U-Boot. For details, refer to the *SS928V100/SS927V100 U-Boot Porting and Application Development Guide*.

# Development Using the SDK and DEMO Board
## Enabling Linux Networking<a name="ZH-CN_TOPIC_0000002424197794"></a>

1.  Configure the network

    ```
    ifconfig eth0 hw ether xx:xx:xx:xx:xx:xx;
    ifconfig eth0 xx.xx.xx.xx netmask xx.xx.xx.xx;
    route add default gw xx.xx.xx.xx
    ```

2.  Ping another machine to verify network connectivity.

## Using NFS for Development<a name="ZH-CN_TOPIC_0000002424357642"></a>

1.  During development, NFS is the recommended file system, as it eliminates the need to rebuild and reflash the root filesystem.
2.  Mount the NFS filesystem with:

    ```
    mount -t nfs -o nolock -o tcp -o rsize=32768,wsize=32768 xx.xx.xx.xx:/your-nfs-path /mnt
    ```

3.  Files on the server are then accessible under `/mnt` for development.

## Enabling the Telnet Service<a name="ZH-CN_TOPIC_0000002424357666"></a>

\# Once the network is working, run `telnetd &` to start the board's telnet service. You can then log in to the board via telnet.

## Running MPP Services<a name="ZH-CN_TOPIC_0000002424357646"></a>

On the board's Linux system, navigate to the `mpp/out/ko` directory and load the kernel modules:

```
cd mpp/ko
./load_ss928v100 -a
```

## Switching Between Linux and LiteOS<a name="ZH-CN_TOPIC_0000002424197810"></a>

Copy the compiled `sample.bin` and the `load_riscv` tool to the Linux system, then run the following commands:

```
cp load_riscv /bin
chmod +x /bin/load_riscv
load_riscv 0x44000000 sample.bin
```

Note: The `load_riscv` tool is located at `osdrv/tools/board/load_riscv/bin`.

Log in to the board via telnet under Linux and navigate to the komod directory, then load the kernel modules:

```
cd /komod
insmod ipcm.ko
insmod virt-tty.ko
```

Run the following command to enter LiteOS:

```
virt-tty riscv
```

To switch back to Linux from LiteOS, press `Ctrl + C`.

# Address Space Allocation and Usage
## DDR Memory Management<a name="ZH-CN_TOPIC_0000002457876553"></a>

-   All DDR memory is divided into two pools: OS memory, managed by the operating system; and MMZ memory, reserved exclusively for media services and managed by the MMZ module.
-   OS memory starts at `0x50000000`. The size is configurable via bootargs (e.g., `setenv bootargs 'mem=512M ...'` allocates 512 MB to the OS). Adjust as needed.
-   MMZ memory is managed by the `ot_osal.ko` kernel module (in `mpp/out/ko`). The MMZ start address and size are specified as module parameters when loading the osal module, via `mmz_start` and `mmz_size` in the load script.
-   Ensure the MMZ memory address range does not overlap with OS memory.

## DEMO Board DDR Memory Layout<a name="ZH-CN_TOPIC_0000002457836385"></a>

Using a 4 GB DDR configuration as an example, the memory layout based on this document and the SDK default configuration is:

DDR:

```
|-------------|--------------------|  0x40000000   # Memory managed by IPCM.
|      2MB    |        IPCM        |
|-------------|--------------------|  0x40200000   # Memory managed by DSP LiteOS.
|      62MB   |        DSP         |
|-------------|--------------------|  0x44000000   # Memory managed by RISC-V LiteOS.
|     192MB   |       RISV-V       |
|-------------|--------------------|  0x50000000   # Memory managed by Linux OS.
|    512MB    |      Linux OS      |
|-------------|--------------------|  0x70000000   # Memory managed by MMZ block anonymous.
|    3328MB   |         MMZ        |
|-------------|--------------------|  0xFFFFFFFF   # End of memory managed by MMZ.
```

Notes:

1.  When configuring boot parameters, set the OS managed memory to 512 MB: `setenv bootargs 'mem=512M...'`.
2.  For special use cases, the `load_ss928v100` script can be modified to customize MMZ partitioning, for example: `insmod ot_osal.ko anony=1 mmz_allocator=ot mmz=anonymous,0,0x70000000,1786M:jpeg,0,0xDFA00000,6M`.
