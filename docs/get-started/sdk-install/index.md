---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/Hi3403V100╱ SDK 安装以及升级使用说明/Hi3403V100╱ SDK 安装以及升级使用说明.md
--- # 前言
**概述<a name="section142mcpsimp"></a>** 本文为Hi3403V100 SDK的安装及升级使用说明，方便使用者能快速在对应芯片的DEMB板上搭建好SDK运行环境。 >![](public_sys-resources/icon-note.gif) **说明：** >本文以Hi3403V100描述为例，未有特殊说明，与Hi3403V100内容一致。 **产品版本<a name="section145mcpsimp"></a>** 与本文档相对应的产品版本如下。 <a name="table148mcpsimp"></a>
<table><thead align="left"><tr id="row153mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row159mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>V100</p>
</td>
</tr>
</tbody>
</table> **读者对象<a name="section164mcpsimp"></a>** 本文档（本指南）主要适用于以下工程师： - 技术支持工程师
- 软件开发工程师 **符号约定<a name="section133020216410"></a>** 在本文中可能出现下列标志，它们所代表的含义如下。 <a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>符号</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002424357674.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
</tbody>
</table> **修改记录<a name="section2467512116410"></a>** <a name="table256mcpsimp"></a>
<table><thead align="left"><tr id="row262mcpsimp"><th class="cellrowborder" valign="top" width="20.97%" id="mcps1.1.4.1.1"><p id="p264mcpsimp"><a name="p264mcpsimp"></a><a name="p264mcpsimp"></a><strong id="b265mcpsimp"><a name="b265mcpsimp"></a><a name="b265mcpsimp"></a>文档版本</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.029999999999998%" id="mcps1.1.4.1.2"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a><strong id="b268mcpsimp"><a name="b268mcpsimp"></a><a name="b268mcpsimp"></a>发布日期</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a><strong id="b271mcpsimp"><a name="b271mcpsimp"></a><a name="b271mcpsimp"></a>修改说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row280mcpsimp"><td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.1.4.1.1 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.1.4.1.2 "><p id="p284mcpsimp"><a name="p284mcpsimp"></a><a name="p284mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p286mcpsimp"><a name="p286mcpsimp"></a><a name="p286mcpsimp"></a>第1次临时版本发布。</p>
</td>
</tr>
</tbody>
</table> # 首次安装SDK
如果您已安装过SDK，可以直接参看[安装、升级Hi3403V100 DEMO板开发环境](#ZH-CN_TOPIC_0000002457836393)。 ## Hi3403V100 SDK包位置<a name="ZH-CN_TOPIC_0000002457876545"></a> 在"Hi3403V100R001\*\*\*/01.software/board"目录下，您可以看到一个 Hi3403V100\_SDK\_Vx.x.x.x.tgz 的文件，该文件就是Hi3403V100的软件开发包。 ## 解压缩SDK包<a name="ZH-CN_TOPIC_0000002457836397"></a> 在linux服务器上（或者一台装有linux的PC上，主流的linux发行版本均可以），使用命令：tar -zxf Hi3403V100\_SDK\_Vx.x.x.x.tgz，解压缩该文件，可以得到一个Hi3403V100\_SDK\_Vx.x.x.x目录。 ## 展开SDK包内容<a name="ZH-CN_TOPIC_0000002424197802"></a> 返回Hi3403V100\_SDK\_Vx.x.x.x目录，运行./sdk.unpack\(请用root或sudo权限执行\)将会展开SDK包打包压缩存放的内容，请按照提示完成操作。 如果您需要通过WINDOWS操作系统中转拷贝SDK包，请先运行./sdk.cleanup，收起SDK包的内容，拷贝到新的目录后再展开。 ## 在linux服务器上搭建开发环境<a name="ZH-CN_TOPIC_0000002457876549"></a> 请参考《OpenHarmony Small版本使用指南》。 ## 编译osdrv<a name="ZH-CN_TOPIC_0000002457836389"></a> 参见osdrv目录下readme ## SDK目录介绍<a name="ZH-CN_TOPIC_0000002457876533"></a> Hi3403V100\_SDK\_Vx.x.x.x 目录结构如下： ├── smp \#smp目录 │ ├── a55\_linux │ ├── interdrv \#mipitx等驱动源代码 │ ├── vendor \#外围驱动源代码 │ ├── mpp │ │ ├── component │ │ │ ├── gfbg \#gfbg源代码 │ │ │ ├── security\_subsys \#安全子系统源代码 │ │ │ └── pciv \#pciv源代码 │ │ ├── cbb │ │ │ └── isp \#isp源代码 │ │ ├── out \#mpp编译目标目录 │ │ ├── ko \#内核ko │ │ ├── lib \#用户lib库 │ │ ├── include \#头文件 │ │ ├── init \#内核模块初始化源代码 │ │ └── obj \#内核模块obj文件 │ └── osal \#操作系统适配层源代码 │ ├── include \#操作系统适配层头文件 │ └── linux \#linux系统适配层源文件 │ ├── dsp\_liteos \#dsp驱动 ├── open\_source \#开源第三方源代码 │ ├── u-boot \#uboot源代码 │ ├── linux \#kernel源代码 │ ├── eigen \#eigen源代码 │ ... ├── platform \#平台代码 │ ├── liteos \#LiteOS代码包 ├── osdrv \#操作系统相关目录 │ ├── components \#自研组件源代码 │ ├── pub \#编译好的镜像等 │ ├── rootfs\_scripts \#文件系统初始目录和脚本 │ ├── tools \#系统工具源代码 ├── package \#SDK的压缩包 │ ├── smp.tgz \#媒体处理平台软件压缩包 │ ├── osdrv.tgz \#操作系统相关压缩包 │ ├── platform.tgz \#平台代码压缩包 │ └── open\_source.tgz \#第三方开源软件压缩包 ├── scripts \#shell脚本目录 ├── sdk.cleanup \#SDK清理脚本 └── sdk.unpack \#SDK展开脚本 # 安装、升级Hi3403V100 DEMO板开发环境
如果您使用的Hi3403V100的DEMO板，可以按照以下操作烧写uboot、内核以及文件系统，以下操作均使用网络来更新: - 如果您拿到的单板没有uboot的话，就需要使用01.software/pc/ToolPlatform进行烧写。更详细的烧写操作步骤及说明，请参见01.software/pc/ToolPlatform目录下的《BurnTool 工具使用指南》。
- 如果您拿到的单板中已经有uboot，可以按照以下步骤使用网口烧写uboot、kernel及rootfs到Flash中。DEMO板默认为从SPI Flash启动。 ## 配置tftp服务器<a name="ZH-CN_TOPIC_0000002424197806"></a> 可以使用任意的tftp服务器，先编译好uboot、kernel和rootfs。将编译好的相关文件拷贝到tftp服务器目录下。 ## 参数配置<a name="ZH-CN_TOPIC_0000002424197814"></a> 单板上电后，敲任意键进入u-boot。设置serverip（即tftp服务器的ip）、ipaddr（单板ip）和ethaddr（单板的MAC地址）。 ```
setenv serverip xx.xx.xx.xx
setenv ipaddr xx.xx.xx.xx
setenv ethaddr xx:xx:xx:xx:xx:xx
setenv netmask xx.xx.xx.xx
setenv gatewayip xx.xx.xx.xx
ping serverip (确保网络畅通)
``` >![](public_sys-resources/icon-notice.gif) **须知：** >- Hi3403V100启动方案分快速启动（使用u-boot-Hi3403V100.bin）和非快速启动（非安全启动/安全启动，使用boot\_image.bin），详见《Hi3403V100 安全启动使用指南》文档第二章节 “启动方案”。
>- 其启动方案可通过读取0x10122090寄存器查看确认，如值为0x5为快速启动，其余值为非快速启动。
>- 默认出厂单板为“非安全启动”，下文以该模式为例烧写镜像。 ## 烧写映像文件到SPI Nor Flash<a name="ZH-CN_TOPIC_0000002424357662"></a> 以32MB SPI Nor Flash为例。地址空间说明： <a name="table252mcpsimp"></a>
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
</table> 以下的操作均基于图示的地址空间分配，您也可以根据实际情况进行调整。 1. 烧写u-boot ``` sf probe 0 mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 boot_image.bin sf probe 0 sf erase 0 0x100000 sf write 0x42000000 0 0x100000 reset ``` 2. 烧写内核 ``` mw.b 0x42000000 0xff 0xb00000 tftp 0x42000000 uImage_Hi3403V100 sf probe 0 sf erase 0x100000 0xb00000 sf write 0x42000000 0x100000 0xb00000 ``` 3. 烧写文件系统 ``` mw.b 0x42000000 0xff 0x1300000 tftp 0x42000000 rootfs_Hi3403V100_64k.jffs2 sf probe 0 sf erase 0xc00000 0x1300000 sf write 0x42000000 0xc00000 0x1300000 ``` 4. 烧写LiteOS 镜像\(可选\) ``` mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 sample.bin sf probe 0 sf erase 0x1f00000 0x100000 sf write 0x42000000 0x1f00000 0x100000 ``` 5. 设置启动参数 ``` setenv bootargs 'mem=512M console=ttyAMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),11M(kernel),19M(rootfs),1M(sample.bin)';sa setenv bootcmd 'sf probe 0;sf read 0x44000000 0x1f00000 0x100000;go_riscv 0x44000000; sf read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa 无LiteOS时: setenv bootargs 'mem=512M console=ttyAMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),11M(kernel),19M(rootfs) ';sa setenv bootcmd 'sf probe 0; sf read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa ``` ## 烧写映像文件到NAND Flash<a name="ZH-CN_TOPIC_0000002457836401"></a> 以64MB NAND Flash为例。地址空间说明： <a name="table312mcpsimp"></a>
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
</table> 以下的操作均基于图示的地址空间分配，您也可以根据实际情况进行调整。 1. 烧写u-boot ``` mw.b 0x42000000 0xff 0x100000 tftp 42000000 boot_image.bin nand erase 0 0x100000 nand write 0x42000000 0 0x100000 reset ``` 1. 烧写内核 ``` mw.b 0x42000000 0xff 0xb00000 tftp 0x42000000 uImage_Hi3403V100 nand erase 0x100000 0xb00000 nand write 0x42000000 0x100000 0xb00000 ``` 2. 烧写文件系统 ``` mw.b 0x42000000 0xff 0x2000000 tftp 0x42000000 rootfs_Hi3403V100_2k_128k_32M.ubifs nand erase 0xc00000 0x2000000 nand write 0x42000000 0xc00000 0x2000000 ``` 3. 烧写LiteOS镜像\(可选\) ``` mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 sample.bin nand erase 0x2c00000 0x100000 nand write 0x42000000 0x2c00000 0x100000 ``` 4. 设置启动参数 ``` setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),11M(kernel),32M(rootfs.ubifs),1M(sample)';sa setenv bootcmd 'nand read 0x44000000 0x2c00000 0x100000;go_riscv 0x44000000;nand read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa 无LiteOS时: setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),11M(kernel),32M(rootfs.ubifs) ';sa setenv bootcmd 'nand read 0x50000000 0x100000 0xb00000;bootm 0x50000000';sa ``` ## 烧写镜像文件到EMMC<a name="ZH-CN_TOPIC_0000002457876529"></a> 地址空间： <a name="table367mcpsimp"></a>
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
</table> 以下的操作均基于图示的地址空间分配，您也可以根据实际情况进行调整。 1. 烧写u-boot ``` mw.b 0x42000000 0xff 0x100000 tftp 42000000 boot_image.bin mmc write 0 0x42000000 0 0x800 reset ``` 2. 烧写内核 ``` mw.b 0x42000000 0xff 0xb00000 tftp 0x42000000 uImage_Hi3403V100 mmc write 0 0x42000000 0x800 0x5800 ``` 3. 烧写文件系统 ``` mw.b 0x42000000 0xff 0x6000000 tftp 0x42000000 rootfs_Hi3403V100_96M.ext4 mmc write 0 0x42000000 0x6000 0x30000 ``` 4. 烧写LiteOS 镜像\(可选\) ``` mw.b 0x42000000 0xff 0x100000 tftp 0x42000000 sample.bin mmc write 0 0x42000000 0x36000 0x800 ``` 5. 设置启动参数 ``` setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(uboot.bin),11M(kernel),96M(rootfs.ext4),1M(sample)';sa setenv bootcmd ' mmc read 0 0x44000000 0x36000 0x800;go_riscv 0x44000000;mmc read 0 0x50000000 0x800 0x5800; bootm 50000000';sa 无 LiteOS 时: setenv bootargs 'mem=512M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(uboot.bin),11M(kernel),96M(rootfs.ext4)';sa setenv bootcmd 'mmc read 0 0x50000000 0x800 0x5800; bootm 50000000';sa ``` >![](public_sys-resources/icon-notice.gif) **须知：** >上述[烧写映像文件到SPI Nor Flash](#ZH-CN_TOPIC_0000002424357662)-[烧写镜像文件到EMMC](#ZH-CN_TOPIC_0000002457876529) 镜像请按照实际大小调整，LiteOS的默认启动地址是 0x44000000，若客户内存布局有调整，请调整LiteOS的启动地址；若无LiteOS时客户可调整 linux 启动地址。 ## 启动新系统<a name="ZH-CN_TOPIC_0000002457876541"></a> reset	\# 重启进入新系统。 # 开发前环境准备
## 管脚复用<a name="ZH-CN_TOPIC_0000002424357658"></a> 与媒体业务相关的管脚复用、DDR优先级配置等在interdrv/sys\_config开源驱动中配置（使用linux DTS进行管理），如果与实际情况不符可直接修改，sys\_config.ko驱动被load\_Hi3403V100调用，在加载mpp内核模块之前被执行。 MPP之外的其他管脚复用统一在uboot中配置，详细说明请参见《Hi3403V100 U-boot 移植应用开发指南》。 # 使用SDK和DEMO板进行开发
## 开启Linux下的网络<a name="ZH-CN_TOPIC_0000002424197794"></a> 1. 设置网络 ``` ifconfig eth0 hw ether xx:xx:xx:xx:xx:xx; ifconfig eth0 xx.xx.xx.xx netmask xx.xx.xx.xx; route add default gw xx.xx.xx.xx ``` 2. 然后ping一下其他机器，如无意外，网络将能正常工作。 ## 使用NFS文件系统进行开发<a name="ZH-CN_TOPIC_0000002424357642"></a> 1. 在开发阶段，推荐使用NFS作为开发环境，可以省去重新制作和烧写根文件系统的工作。
2. 挂载NFS文件系统的操作命令： ``` mount -t nfs -o nolock -o tcp -o rsize=32768,wsize=32768 xx.xx.xx.xx:/your-nfs-path /mnt ``` 3. 然后就可以在/mnt目录下访问服务器上的文件，并进行开发工作。 ## 开启telnet服务<a name="ZH-CN_TOPIC_0000002424357666"></a> \# 网络正常后，运行命令 telnetd & 就可以启动单板telnet服务，然后才能使用telnet登录到单板。 ## 运行MPP业务<a name="ZH-CN_TOPIC_0000002424357646"></a> 在单板linux系统下，进入mpp/out/ko目录，加载ko ```
cd mpp/ko
./load_Hi3403V100 -a
``` ## Linux和LiteOS 切换<a name="ZH-CN_TOPIC_0000002424197810"></a> 将编译好的sample.bin和load\_riscv工具拷贝到linux系统下，然后执行如下命令。 ```
cp load_riscv /bin
chmod +x /bin/load_riscv
load_riscv 0x44000000 sample.bin
``` 注：load\_riscv工具在osdrv/tools/board/load\_riscv/bin路径下 在Linux系统下使用 telnet服务登录单板并进入komod目录，加载ko ```
cd /komod
insmod ipcm.ko
insmod virt-tty.ko
``` 执行如下指令进入 LiteOS ```
virt-tty riscv
``` 在 LiteOS 可通过 “ctrl + c”键切换到 Linux 系统 # 地址空间分配与使用
## DDR内存管理说明<a name="ZH-CN_TOPIC_0000002457876553"></a> - 所有DDR内存中，一部分由操作系统管理，称为OS内存；另一部分由MMZ模块管理，供媒体业务单独使用，称为MMZ内存。
- OS内存起始地址为0x50000000，内存大小可通过bootargs进行配置，例如第三章中的setenv bootargs 'mem=512M ... ',表示分配给操作系统内存为512M，您可以根据实际情况进行调整。
- MMZ内存由osal内核模块管理（mpp/out/ko目录下的ot\_osal.ko），加载osal模块时，通过模块参数指定其起始地址及大小，load脚本中根据MMZ的起始地址mmz\_start及大小mmz\_size。
- 请注意MMZ内存地址范围不能与OS内存重叠。 ## DEMO板DDR内存管理示意<a name="ZH-CN_TOPIC_0000002457836385"></a> 以容量为4G Bytes的DDR内存为例，以下为根据本文档和SDK默认配置得到的内存管理示意图： DDR: ```
|-------------|--------------------| 0x40000000 # Memory managed by IPCM.
| 2MB | IPCM |
|-------------|--------------------| 0x40200000 # Memory managed by DSP LiteOS.
| 62MB | DSP |
|-------------|--------------------| 0x44000000 # Memory managed by RISC-V LiteOS.
| 192MB | RISV-V |
|-------------|--------------------| 0x50000000 # Memory managed by Linux OS.
| 512MB | Linux OS |
|-------------|--------------------| 0x70000000 # Memory managed by MMZ block anonymous.
| 3328MB | MMZ |
|-------------|--------------------| 0xFFFFFFFF # End of memory managed by MMZ.
``` 注意： 1. 用户在配置启动参数时需要设置OS的管理内存为512MB，“setenv bootargs 'mem=512M...”。
2. 如果有特殊应用，可以自行修改load\_Hi3403V100脚本，进行mmz区域划分，如“insmod ot\_osal.ko anony=1 mmz\_allocator=ot mmz=anonymous,0,0x70000000,1786M:jpeg,0,0xDFA00000,6M”。 