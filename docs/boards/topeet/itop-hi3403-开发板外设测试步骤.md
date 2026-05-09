---
title: "第1章 ToolPlatform固件烧录"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/hi3403/vendor/topeet/docs/iTOP-Hi3403 开发板外设测试步骤.md
---

# 第1章 ToolPlatform固件烧录

本文档对使用iTOP-Hi3403 开发板的镜像烧录进行详细的说明。

## 1.1 烧写步骤

在烧录之前需要先获取到要烧写的镜像，获取镜像有以下两种方式： 

(1)获取方式一

在编译Linux源码时，各部分镜像会拷贝到Linux源码的output目录下，可以从output输出目录获取到要烧写的镜像。

(2)获取方式二

迅为已经将编译好的镜像放到了[网盘链接](https://pan.baidu.com/s/1vvGStYG5wxCj7UAGza7UsQ?pwd=rgci)对应的目录下，分为buildroot镜像、ubuntu_lite镜像(无桌面)、ubuntu_xfce镜像(有桌面)镜像两个文件夹，用来区分不同的文件系统，每个文件夹内容如下图所示：

![image-20260327105156899](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271051933.png)

![image-20260327105220806](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271052841.png)

 烧写镜像确定之后，还需要烧写工具ToolPlatform，[烧写工具]( https://pan.baidu.com/s/1zh2z6pRpkMhabB1JYHY-jg?pwd=t9wm)可以从网盘链接进行下载，将ToolPlatform-1.0.11-win32-x86_64.zip压缩包拷贝到windows的任意路径，然后解压压缩包会得到ToolPlatform文件夹，如下图所示：

![image-20260327105257769](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271052788.png)

 然后进入ToolPlatform文件夹，将要烧写的镜像文件夹拷贝到该目录中，拷贝完成如下图所示：

![image-20260327105313363](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271053399.png)

 然后点击ToolPlatform.exe运行烧写工具，如下图所示：

![image-20260327105327160](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271053191.png)

 烧写工具打开之后会进入芯片选择界面，这里只有SS928V100，所以直接点击确认即可，如下图所示：

![image-20260327110244623](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271102651.png)

 点击确认之后会进入欢迎界面，然后点击菜单栏下方的BurnTool按钮，如下图所示：

![image-20260327110259857](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271102892.png)

 点击之后就进入烧写工具界面了，如下图所示：

![image-20260327110315635](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271103689.png)

 由于后续的烧写需要用到串口和网络，所以在烧写之前需要确保开发板已连接好了网线(必须接eth0)和串口线，连接完成如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271041327.png)

 然后修改烧写软件的本地PC配置，将串口修改为连接开发板对应的COM口(需要时注意串口不能在其他地方使用，例如在串口终端软件查看打印)，服务器IP设置为可以与开发板ping通的网卡IP，设置完成如下图所示：

![image-20260327110352707](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271103762.png)

 由于要将镜像烧写到EMMC对应的分区，所以这里点击“烧写eMMC”按钮如下图所示：

![image-20260327110655315](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271106367.png)

 然后点击浏览按钮，选择烧写镜像文件夹里的parttable.xml，选择之后烧写界面如下图所示：

![image-20260327110714598](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271107649.png)

 分区默认已经设置完成，这里需要注意的是每个镜像对应的地址是否正确，如果不正确需要改为匹配的地址路径，然后点击烧写按钮，如果串口正常连接，且未在其他地方使用，会出现“串口已连接，请给单板上电，若已经上电，请断电后重新上电”的打印，如下图所示：

![image-20260327110939615](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271109672.png)

 然后在开发板端，按着boot按键上电，出现########################打印就证明镜像正在烧写，如下图所示：

![image-20260327110954200](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271109259.png)

 buildroot镜像烧写时间大约是3分钟左右，ubuntu镜像大约是10分钟左右，烧写完成之后会有烧写成功的弹窗，如下图所示：

![image-20260327111205738](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112760.png)

 至此，关于Hi3403镜像的烧写就讲解完成了。

注意：可以完全通过串口进行烧写，但由于串口的烧写速率太低，所以并不推荐使用该方法。

## 1.2常见烧写问题

### 1.2.1串口占用问题

在使用ToolPlatform工具进行烧写时，需要确保连接的串口没有在其他地方使用，因为该串口也被用作调试串口，所以在进行烧写时，难免会遇到未关闭调试串口就进行烧写的情况。

在串口被占用的情况下，点击烧写会遇到“Open serial port failed.”的打印，并弹出下载失败的弹窗，如下图所示：

![image-20260327111225033](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112086.png)

 这时候需要检查串口的使用情况，关闭其他占用串口的软件，然后重新烧写。

### 1.2.2网口接到了eth1

ToolPlatform工具在通过串口将uboot烧写到emmc之后，会通过网络烧写体积较大的内核和文件系统镜像，而在开发板上有两个网口分别是eth0和eth1，需要注意只有eth0可以进行后续的tftp烧写，如果接入eth1会出现网络下载tftp超时的弹窗，如下图所示：

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112977.png)

 这时需要检查是不是接错了网口，在连接正常之后，重新进行烧写。

# 第2章 使用TF卡烧写固件

使用ToolPlatform工具烧写需要连接串口线和网线，需要的前提条件较多且烧写速度缓慢，从而导致大批量产品升级时效率较低，所以本章节将对TF卡固件烧写步骤进行讲解，通过TF卡升级固件可以做到脱离电脑、提高生产效率。

TF卡升级前提条件如下：

（1）TF卡小于32G

（2）TF卡格式需要格式化为FAT32

（3）开发板已烧写过uboot镜像，非裸板

首先将TF卡通过读卡器或者其他方式连接到电脑上，会出现U盘的盘符，如下图所示：

![image-20260327111256396](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112425.png)

 然后将要烧写的镜像拷贝到TF卡的根目录下，拷贝完成如下所示：

![image-20260327111310055](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271113081.png)

 这里的parttable.xml是ToolPlatform工具烧写时候要用到的分区表，在TF卡烧写时不会用到，所以可以不拷贝该文件，然后将TF卡插到iTOP-Hi3403开发板上，然后启动开发板，TF卡烧写有两种方法，下面进行讲解。

**方式1：**

在uboot倒计时的过程中按下任意按键进入命令行模式，如下图所示：

![image-20260327111326997](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271113058.png)

 然后输入sd_update命令即可开始TF卡向EMMC中烧写各个镜像，烧写过程如下所示：

![image-20260327111337681](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271113727.png)

 烧写完成之后如下图所示，这时候输入reset重启开发板即可进入烧写完成的系统

![image-20260327111347296](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271113320.png)

 进入系统之后如下图所示：

![image-20260327111358220](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271113280.png)

 至此，关于TF卡烧写固件方式1就讲解完成了。

**方式2：**

方式1使用的是命令行的方式进行的系统升级，但当项目已经部署之后，命令行升级的方式就显得有些繁琐了，所以提供了方式2的升级方法。同样是插入拷贝好镜像的TF卡，然后按着开发板的update按键对开发板进行上电，就会自动进入TF卡烧写模式，update按键位置如下所示：

![image-20260327111432293](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271114651.png)

 TF卡升级过程如下所示：

![image-20260327111444333](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271114388.png)

 烧写完成之后会自动重启，进入烧写之后的系统，如下图所示：

![image-20260327111454362](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271114407.png)

![image-20260327111502509](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271115571.png)

 至此，关于TF卡烧写固件方式2就讲解完成了。



# 第3章 TF启动

在上一章节中讲解了TF卡烧写固件，但在一些特殊情况或者日常调试的过程中可能会用到TF卡启动，即启动TF卡中的固件，本章节将对TF卡启动的相关步骤进行讲解。

TF卡启动前提条件如下：

（1）TF卡小于32G

（2）TF卡格式需要格式化为FAT32

（3）开发板已烧写过uboot镜像，非裸板

系统启动的TF卡制作需要对应的脚本，脚本存放在Linux SDK源码中，所以需要先解压Linux SDK,进入SDK根目录如下图所示：

![image-20260327111521453](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271115484.png)

 然后进入Hi3403_SDK/scripts/TF_BOOT目录下，如下图所示：

![image-20260327111530932](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271115961.png)

 这里的image用来存放TF卡要启动的镜像，make_sd.sh为TF卡制作脚本，后面两个目录为临时挂载目录，然后将要启动的镜像放到image目录下，注意这里只需要拷贝内核镜像uImage_ss928v100和文件系统镜像rootfs.img即可，拷贝完成如下所示：

![image-20260327111541182](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271115202.png)

 然后将TF卡通过读卡器连接到虚拟机ubuntu上，这时使用fdsisk命令应该能查看到对应的信息，如下图所示：

![image-20260327111611932](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271116969.png)

 注：这里不同环境可能磁盘的设备节点不同，需要根据实际情况确定，然后使用以下命令进行TF卡的制作，制作过程如下所示：

~~~bash
sudo ./make_sd.sh /dev/sdc
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271115954.png)

 制作完成如下所示：

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271116754.png)

然后将TF卡插到开发板上，在uboot倒计时的过程中按下任意键进入命令行模式，如下图所示：

![image-20260327111954756](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271119814.png)

 然后依次输入以下三条命令将bootmedia参数从默认的emmc切换为tf卡，如下图所示：

~~~bash
setenv bootmedia tf 
saveenv
reset
~~~

![image-20260327112156210](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271121239.png)

 重启就会进入TF卡中的系统，进入系统之后如下所示：

![image-20260327112207245](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271122282.png)

 至此，关于TF卡启动就演示完成了。