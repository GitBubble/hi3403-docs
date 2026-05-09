---
title: "第一章 Ubuntu系统功能测试"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/hi3403/vendor/topeet/docs/iTOP-Hi3403 镜像烧写步骤.md
---

# 第一章 Ubuntu系统功能测试

本小节测试Ubuntu系统。因此需要烧写Ubuntu系统镜像，Ubuntu系统镜像可以通过[网盘链接](https://pan.baidu.com/s/16XKTCPqWIFCNlHM3DNKKFA?pwd=qiif)进行下载。

系统账号密码为：

账号root

密码topeet

## 1.1 系统启动

命令行终端显示如下，进入root用户。

![image-20260327132735420](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271327461.png)

 ## 1.2 系统信息查询 

查看内核和 cpu 信息，输入如下命令： 

~~~shell
uname -a 
~~~

查看操作系统信息： 

~~~bash
cat /etc/issue 
~~~

以上命令操作结果如下图所示。 

![image-20260327132836367](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271328401.png)

 ## 1.3 有线网测试

首先准备一个千兆路由器，一根千兆网线，如下图所示，这俩个网口都可以连接外网，将网口通过网线连接到路由器的千兆口。

![image-20260327132858585](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271329826.png)

可以根据自己的需求选择连接的网口并使用命令查看网口的IP，如下图所示：

~~~shell
ifconfig eth0 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320861.jpg)

~~~shell
 ifconfig eth1 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320859.jpg)

 输入以下命令对网口的连通性测试，俩个网口都支持连接外网。

~~~shell
ping www.baidu.com -I eth0
ping www.baidu.com -I eth1
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320881.jpg)

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320112.jpg)

## 1.4 U盘测试

当插入U盘以后，U盘的格式为FAT32格式（底板上3个USB 接口都可以插入U盘），如下图所示。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320135.jpg)

 1 将U盘(U盘的格式为FAT32格式)插到开发板的usb接口，串口打印信息如下所示，U盘的设备节点是/dev/sda。U盘的设备节点不是固定的，根据实际情况来查看设备节点。

![image-20260327133111270](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271331295.png)

 2 通过mount命令将U盘挂载到/mnt/usb0目录下，然后可以通过“df -h”命令查看挂载路径，如下图所示：

~~~shell
mount /dev/sda1 /mnt/usb0
~~~

![image-20260327133057182](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271330217.png)

 至此U盘测试就完成了。

## 1.5 TF卡测试 

1 将TF卡插到开发板的TF卡插槽，串口打印信息如下图所示，TF盘的设备节点是/dev/mmcblk1p1。

![image-20260327133232560](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271332589.png)

 2 可以通过mount命令将U盘挂载到/mnt/sdcard目录下，然后可以通过“df -h”命令查看挂载路径，如下图所示：

~~~shell
mount /dev/mmcblk1p1 /mnt/sdcard/
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320335.jpg)

## 1.6 Linux 485测试

### 1.6.1 485硬件连接

两个RS485接口位置如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320387.jpg)

RS485接口对应原理图如下图所示：

![image-20260327133501381](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271335433.png)

![image-20260327133511500](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271335544.png)

 RS485使用的分别是串口3和串口4，可以通过/dev/ttyAMA3和/dev/ttyAMA4来控制。接下来使用USB转RS485模块进行测试（需要自行准备）。USB转RS485模块如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320493.jpg)     ![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320554.jpg)

将RS485接口的A、B引脚连接到USB转RS485模块上，A接A，B接B，GND接GND。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320633.jpg)

 USB转RS485模块的usb端口连接到电脑上。

### 1.6.2 测试485    

将测试程序拷贝到开发板上（Ubuntu系统/home/topeet/topeet_test/01_485_test目录下默认预置了该程序，可直接使用），如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320680.jpg)

 在电脑上打开串口助手，选择对应的串口号和波特率，注意：默认波特率为115200！

打开串口，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320717.jpg)

 输入以下命令运行测试程序发送数据，发送的数据为123456789，数据信息可以自定义。

~~~c
./uarttest /dev/ttyAMA3 send 123456789
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320746.jpg)

 电脑端接收到信息，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320812.jpg)

输入以下命令开发板接收数据，如下图所示：

~~~shell
./uarttest /dev/ttyAMA3 recv
~~~



![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320887.jpg)

 电脑端发送数据，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320923.jpg)

开发板收到数据，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320951.jpg)

 /dev/ttyAMA4测试方法同上。

## 1.7 4G模块测试

iTOP-Hi3403开发板上预留了一个4G/5G接口，可以连接迅为提供的EM05-CE模块（4G模块）和RM500U-CN（5G模块）。将4G/5G模块连接到iTOP-Hi3403开发板对应接口上，接好天线（4G模块三根天线，5G模块四根天线），然后插入一张能联网的SIM卡。

将quectel-CM脚本拷贝到开发板上（Ubuntu系统/home/topeet/topeet_test/02_4g目录下默认预置了该程序，可直接使用），如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320082.jpg)

 然后执行以下命令运行连接脚本，如下图所示：

~~~shell
./quectel-CM &
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320108.jpg)

 输入命令“ifconfig”会有 wwan0 出现，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320140.jpg)

 然后输入以下命令，ping一下百度的ip，可以看到已经能上网了，如下图所示：

~~~shell
ping www.baidu.com
~~~

![image-20260327153108942](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271531989.png)

 ## 1.8 5G模块AT拨号上网测试

iTOP-Hi3403开发板上预留了一个4G/5G接口，可以连接迅为提供的EM05-CE模块（4G模块）和RM500U-CN（5G模块）。将4G/5G模块连接到iTOP-Hi3403开发板对应接口上，接好天线（4G模块三根天线，5G模块四根天线），然后插入一张能联网的SIM卡。

启动开发板识别到5G模块节点如下图所示：

~~~shell
ls /dev/ttyUSB*
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320228.jpg)

 其中/dev/ttyUSB2为AT命令通道。

使用以下命令查看/dev/ttyUSB2的输出打印，如下图所示：

~~~shell
cat /dev/ttyUSB2 &
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320253.jpg)

检查SIM卡状态

~~~shell
echo -e "AT+CPIN?\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320337.jpg)

 返回READY说明SIM卡已经识别成功。

查询信号强度

~~~shell
echo -e "AT+CSQ\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320378.jpg)

 返回+CSQ: <rssi>,<ber>，rssi在10~30之间才算正常。

自动注册网络

~~~shell
echo -e "AT+COPS=0\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320406.jpg)

 返回OK，并能用AT+COPS? 查询到运营商（如CHINA MOBILE）。

~~~shell
echo -e "AT+COPS?\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320504.jpg)

 设置APN

~~~shell
echo -e "AT+CGDCONT=1,\"IP\",\"CMNET\"\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320524.jpg)

移动用 "CMNET"，联通用 "3GNET"，电信用 "CTNET"。

附着数据网络

~~~shell
echo -e "AT+CGATT=1\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320546.jpg) 

返回OK表示已附着。

打开虚拟网卡-使能网卡并分配IP

~~~shell
echo -e "AT+QCFG=\"ethernet\",1\r\n" > /dev/ttyUSB2
echo -e "AT+QCFG=\"nat\",0\r\n" > /dev/ttyUSB2
echo -e "AT+QNETDEVCTL=1,3,1\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320628.jpg)

 查询分配的IP地址

~~~shell
echo -e "AT+CGPADDR=1\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320664.jpg)

 可知分配的IP为10.167.148.251。

使用以下命令查看5G节点，如下图所示：

~~~shell
ifconfig  
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320688.jpg)

 测试网络

~~~shell
ping www.baidu.com -I usb0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320767.jpg)

 ## 1.9 M2接口固态硬盘测试

iTOP-Hi3403开发板支持M.2接口的固态硬盘，启动前将固态硬盘插入M.2接口，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320811.jpg)

 pci是一种总线，而通过pci总线连接的设备就是pci设备。PC上常用的设备很多都是采用pci总线，如：网卡、存储等。输入以下命令显示所有的pci设备信息。

~~~shell
lspci
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320848.jpg)

 

输入以下命令查看生成的设备节点

~~~shell
ls /dev/nvme0*
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320874.jpg)

 输入以下命令挂载固态，将固态硬盘挂载到nvme目录下，挂载目录可以随意指定，如下图所示：

~~~shell
mkdir nvme
mount /dev/nvme0n1p1 nvme/
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320939.jpg)

 挂载完，如下图所示:

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320010.jpg)

 ## 1.10耳机/麦克风测试

iTOP-Hi3403开发板板载耳机麦克风接口，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320060.jpg)

 接入三段式耳机和麦克风，使用/sameple/sample_audio例程进行测试，运行例程打印如下：

~~~shell
./sample_audio 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320087.jpg)

 其中功能0是从音频输入通道（AI）采集声音信号，直接回放到音频输出（AO）。输入以下命令进行环回测试，如下图所示：

~~~shell
./sample_audio 0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320133.jpg)

 此时，对着麦克风说话，耳机能实时听到自己的声音。使用Ctrl + C停止测试。

功能1是从AI采集音频数据，经过音频编码器压缩，保存成音频文件。输入以下命令进行录音测试，如下图所示：

~~~shell
./sample_audio 1
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320154.jpg)

 对着麦克风讲话，程序会录制音频并生成文件，使用Ctrl + C停止录音后，生成文件为audio_chn0.aac，如下图所：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320239.jpg)

 功能2是从本地音频文件读取音频流，经解码后输出到耳机，输入以下命令播放刚刚录制的音频，如下图所示：

~~~shell
./sample_audio 2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320286.jpg)

此时耳机里会一直播放录制的audio_chn0.aac文件内容，使用Ctrl + C停止播放。

## 1.11蜂鸣器测试

将底板拨码开关1和2拨到ON位置，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320347.jpg)

 PWM提供了用户层的接口，在/sys/class/pwm/节点下面：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320391.jpg)

 蜂鸣器使用PWM0的12通道，查看pwmchip0目录下文件，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320412.jpg)

 使用以下命令测试蜂鸣器：

~~~shell
echo 12 > /sys/class/pwm/pwmchip0/export 

echo 366300 > /sys/class/pwm/pwmchip0/pwm12/period 

echo 260000 > /sys/class/pwm/pwmchip0/pwm12/duty_cycle 

echo 1 > /sys/class/pwm/pwmchip0/pwm12/enable  //开启

echo 0 > /sys/class/pwm/pwmchip0/pwm12/enable  //关闭
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320453.jpg)

 修改第二句和第三句命令中的参数以修改pwm的占空比来控制蜂鸣器发出声音的大小。

## 1.12 温湿度测试

iTOP-Hi3403开发板板载DHT11模块，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320497.jpg)

 使用以下命令查看当前温度，如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device1/in_temp_input 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320544.jpg)

 使用以下命令查看当前湿度，如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device1/in_humidityrelative_input 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320594.jpg)

 ## 1.13 ADC电位器测试

iTOP-Hi3403开发板板载了一路电位器，原理图如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320663.jpg)

 电位器对应原理图如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320704.jpg)

 从上图可以看到电位器（R244）的原理很简单，使用1.8V供电，输出引脚通过IR_CUT_0_CONTROL1链接到Hi3403的LSADC_CH0引脚上了。这样就能够实现电位器的电压采集了，我们调节电位器上的旋钮，ADC采集到的电压会在0~1.8V范围内变化。

使用以下命令查看LSADC_CH0通道原始数据，如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320729.jpg)

 使用以下命令查看电压缩放因子（将原始采样值转换为实际电压值），如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device0/in_voltage0_scale
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320758.jpg)

 将读取到的in_voltage0_raw原始值511乘以in_voltage0_scale缩放因子1.757812500即可获得该通道的当前实际电压约为898mV（即0.9V）。

## 1.14 EMMC测试

下面简单测试EMMC的读写速度，以读写ext4文件系统为例。注意：为确保数据准确，请重启开发板后测试读取速度。 

~~~shell
dd if=/dev/zero of=/test bs=1M count=500 conv=fsync//写入测试 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320820.jpg)

 ~~~shell
 dd if=/test of=/dev/null bs=100M //读取测试 
 ~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320846.jpg)

 ## 1.15 OS08A20摄像头测试

开发板默认支持摄像头接口。底板提供2个摄像头接口，默认提供的镜像可以使用***\*J1\****接口。迅为提供的OS08A20摄像头模块如下图所示。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320967.jpg)

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320991.jpg)

 使用系统/sameple目录下的sample_vo例程进行测试，如下图所示：

~~~shell
./sample_vo 0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320027.jpg)

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320094.jpg)

## 1.16 RTC时钟测试

Linux系统下分为系统时钟和硬件时钟。分别使用 date 和 hwclock 命令查看。系统时钟在系统断电以后会丢失，硬件时钟在有纽扣电池的情况下，系统断电，时钟不会丢失。在系统每次启动的时候，系统时钟会和硬件时钟进行同步。

首先启动开发板，通过调试串口登录到开发板上，如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320129.jpg)

查看系统时钟在串口终端输入“date”命令，运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320196.jpg)

查看硬件时钟，在串口输入“hwclock -u”命令查看硬件时钟，运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320221.jpg)

 也可以使用date命令来设置系统时间，例如置系统时间为2025年9月11号14:30:00，在串口终端输入命令“date -s "2025-9-11 14:30:00"”，设运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320336.jpg)

 

然后使用“hwclock --systohc -u”命令把当前系统的时间同步到硬件时钟里面，然后使用“hwclock -u”命令查看硬件时钟。运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320357.jpg)

## 1.17 HDMI测试

使用系统/sample目录下的sample_hdmi进行测试，sample_hdmi例程是解析H265格式视频文件通过HDMI接口输出到显示屏。如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320391.jpg)

 使用以下命令运行sample_hdmi进行测试，如下图所示：

~~~shell
./sample_hdmi
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320479.jpg)

 当前例程播放文件为/sample/source_file/3840x2160_8bit.h265，运行后HDMI屏显示视频文件，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320503.jpg)

 进入例程终端输入h查看帮助信息如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320537.jpg)

 输入q结束例程，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320581.jpg)

## 1.18 UVC摄像头测试

使用系统/sample目录下的sample_uvc进行测试，sample_uvc例程是一路usb摄像头输入到HDMI TX输出显示。如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320607.jpg)

 使用以下命令运行例程查看帮助信息，如下图所示：

~~~shell
./sample_uvc -h 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320639.jpg)

 将USB摄像头插入开发板，将自动安装uvc驱动，使用以下命令检查识别摄像头，如下图所示：

~~~shell
v4l2-ctl --list-devices 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320730.jpg)

 由上图可知，USB摄像头节点为/dev/video0。

首先查看USB摄像头设备可支持的格式，如下图所示：

~~~shell
./sample_uvc /dev/video0 --enum-formats 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320784.jpg)

 使用以下命令运行例程查看摄像头画面（可根据自己实际打印，修改例程参数），如下图所示：

~~~shell
./sample_uvc /dev/video0 -fYUYV -s640x480 -Ftest.yuv
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320821.jpg)

运行后HDMI屏显示摄像头画面，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320881.jpg)

# 第二章 buildroot系统功能测试

本小节测试buildroot系统。因此需要烧写buildroot系统镜像，buildroot系统镜像可以通过[网盘链接](https://pan.baidu.com/s/1CdzFZy7BRA-eMSfGNEZloQ?pwd=f4aa)进行下载。

## 2.1 系统启动

命令行终端显示如下，进入root用户

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320911.jpg)

 ## 2.2 系统信息查询

查看内核和 cpu 信息，输入如下命令： 

~~~bash
uname -a 
~~~

查看操作系统信息： 

~~~shell
cat /etc/issue 
~~~

以上命令操作结果如下图所示。 

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320970.jpg)

 ## 2.3 有线网测试

首先准备一个千兆路由器，一根千兆网线，如下图所示，这俩个网口都可以连接外网，将网口通过网线连接到路由器的千兆口。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320032.jpg)

 可以根据自己的需求选择连接的网口并使用命令查看网口的IP，如下图所示：

~~~shell
ifconfig eth0 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320065.jpg)

 ~~~shell
 ifconfig eth1 
 ~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320112.jpg)

 输入以下命令对网口的连通性测试，俩个网口都支持连接外网。

~~~shell
ping www.baidu.com -I eth0

ping www.baidu.com -I eth1
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320146.jpg)

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320210.jpg)

## 2.4 U盘测试

当插入U盘以后，U盘的格式为FAT32格式（底板上3个USB 接口都可以插入U盘），如下图所示。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320253.jpg)

 1 将U盘(U盘的格式为FAT32格式)插到开发板的usb接口，串口打印信息如下所示，U盘的设备节点是/dev/sda。U盘的设备节点不是固定的，根据实际情况来查看设备节点。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320303.jpg)

 2 通过mount命令将U盘挂载到/mnt/usb0目录下，然后可以通过“df -h”命令查看挂载路径，如下图所示：

~~~shell
mount /dev/sda1 /mnt/usb0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320345.jpg)

 至此U盘测试就完成了。

## 2.5 TF卡测试 

1 将TF卡插到开发板的TF卡插槽，串口打印信息如下图所示，TF盘的设备节点是/dev/mmcblk1p1。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320400.jpg)

 

2 可以通过mount命令将U盘挂载到/mnt/sdcard目录下，然后可以通过“df -h”命令查看挂载路径，如下图所示：

~~~shell
mount /dev/mmcblk1p1 /mnt/sdcard/
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320442.jpg)

 

## 2.6 Linux 485测试

### 2.6.1 485硬件连接

两个RS485接口位置如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320473.jpg)

 

RS485接口对应原理图如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320568.jpg)

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320596.jpg)

 RS485使用的分别是串口3和串口4，可以通过/dev/ttyAMA3和/dev/ttyAMA4来控制。接下来使用USB转RS485模块进行测试（需要自行准备）。USB转RS485模块如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320652.jpg)     ![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320674.jpg)

将RS485接口的A、B引脚连接到USB转RS485模块上，A接A，B接B，GND接GND。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320764.jpg)

 USB转RS485模块的usb端口连接到电脑上。

### 2.6.2 测试485    

将测试程序拷贝到开发板上（buildroot系统/topeet_test/01_485_test目录下默认预置了该程序，可直接使用），如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320808.jpg)

 在电脑上打开串口助手，选择对应的串口号和波特率，注意：默认波特率为115200！

打开串口，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320838.jpg)

 输入以下命令运行测试程序发送数据，发送的数据为123456789，数据信息可以自定义。

~~~shell
./uarttest /dev/ttyAMA3 send 123456789
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320908.jpg)

 电脑端接收到信息，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320960.jpg)

 输入以下命令开发板接收数据，如下图所示：

~~~shell
./uarttest /dev/ttyAMA3 recv
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320988.jpg)

 电脑端发送数据，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320040.jpg)

 开发板收到数据，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320078.jpg)

 /dev/ttyAMA4测试方法同上。

## 2.7 4G模块测试

iTOP-Hi3403开发板上预留了一个4G/5G接口，可以连接迅为提供的EM05-CE模块（4G模块）和RM500U-CN（5G模块）。将4G/5G模块连接到iTOP-Hi3403开发板对应接口上，接好天线（4G模块三根天线，5G模块四根天线），然后插入一张能联网的SIM卡。

将quectel-CM脚本拷贝到开发板上（buildroot系统/topeet_test/02_4g目录下默认预置了该程序，可直接使用），如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320101.jpg)

然后执行以下命令运行连接脚本，如下图所示：

~~~shell
./quectel-CM &
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320189.jpg)

 输入命令“ifconfig wlan0”查看4G节点，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320234.jpg)

 然后输入以下命令，ping一下百度的ip，可以看到已经能上网了，如下图所示：

ping www.baidu.com -I wwan0

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320261.jpg)

 ## 2.8 5G模块AT拨号上网测试

iTOP-Hi3403开发板上预留了一个4G/5G接口，可以连接迅为提供的EM05-CE模块（4G模块）和RM500U-CN（5G模块）。将4G/5G模块连接到iTOP-Hi3403开发板对应接口上，接好天线（4G模块三根天线，5G模块四根天线），然后插入一张能联网的SIM卡。

启动开发板识别到5G模块节点如下图所示：

~~~shell
ls /dev/ttyUSB*
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320312.jpg)

其中/dev/ttyUSB2为AT命令通道。

使用以下命令查看/dev/ttyUSB2的输出打印，如下图所示：

~~~shell
cat /dev/ttyUSB2 &
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320358.jpg)

检查SIM卡状态

~~~shell
echo -e "AT+CPIN?\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320410.jpg)

 

返回READY说明SIM卡已经识别成功。

查询信号强度

~~~shell
echo -e "AT+CSQ\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320458.jpg)

 返回+CSQ: <rssi>,<ber>，rssi在10~30之间才算正常。

自动注册网络

~~~shell
echo -e "AT+COPS=0\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320503.jpg)

 返回OK，并能用AT+COPS? 查询到运营商（如CHINA MOBILE）。

~~~shell
echo -e "AT+COPS?\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320546.jpg)

 设置APN

~~~shell
echo -e "AT+CGDCONT=1,\"IP\",\"CMNET\"\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320572.jpg)

 移动用 "CMNET"，联通用 "3GNET"，电信用 "CTNET"。

附着数据网络

~~~shell
echo -e "AT+CGATT=1\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320613.jpg) 

返回OK表示已附着。

打开虚拟网卡-使能网卡并分配IP

~~~shell
echo -e "AT+QCFG=\"ethernet\",1\r\n" > /dev/ttyUSB2

echo -e "AT+QCFG=\"nat\",0\r\n" > /dev/ttyUSB2

echo -e "AT+QNETDEVCTL=1,3,1\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320641.jpg)

 查询分配的IP地址

~~~shell
echo -e "AT+CGPADDR=1\r\n" > /dev/ttyUSB2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320726.jpg)

 可知分配的IP为10.167.148.251。

使用以下命令查看5G节点，如下图所示：

~~~shell
ifconfig  
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320751.jpg)

 

测试网络

~~~shell
ping www.baidu.com -I usb0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320824.jpg)

 ## 2.9 M2接口固态硬盘测试

iTOP-Hi3403开发板支持M.2接口的固态硬盘，启动前将固态硬盘插入M.2接口，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320865.jpg)

 pci是一种总线，而通过pci总线连接的设备就是pci设备。PC上常用的设备很多都是采用pci总线，如：网卡、存储等。输入以下命令显示所有的pci设备信息。

~~~shell
lspci
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320897.jpg)

 输入以下命令查看生成的设备节点

~~~shell
ls /dev/nvme0*
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320937.jpg)

 输入以下命令挂载固态，将固态硬盘挂载到nvme目录下，挂载目录可以随意指定，如下图所示：

~~~shell
mkdir nvme

mount /dev/nvme0n1p1 nvme/
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320959.jpg)

 挂载完，如下图所示:

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320076.jpg)

 ## 2.10耳机/麦克风测试

iTOP-Hi3403开发板板载耳机麦克风接口，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320097.jpg)

 接入三段式耳机和麦克风，使用/sameple/sample_audio例程进行测试，运行例程打印如下：

~~~shell
./sample_audio 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320129.jpg)

 其中功能0是从音频输入通道（AI）采集声音信号，直接回放到音频输出（AO）。输入以下命令进行环回测试，如下图所示：

~~~shell
./sample_audio 0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320157.jpg)

 此时，对着麦克风说话，耳机能实时听到自己的声音。使用Ctrl + C停止测试。

功能1是从AI采集音频数据，经过音频编码器压缩，保存成音频文件。输入以下命令进行录音测试，如下图所示：

~~~shell
./sample_audio 1
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320220.jpg)

 对着麦克风讲话，程序会录制音频并生成文件，使用Ctrl + C停止录音后，生成文件为audio_chn0.aac，如下图所：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320299.jpg)

 功能2是从本地音频文件读取音频流，经解码后输出到耳机，输入以下命令播放刚刚录制的音频，如下图所示：

~~~shell
./sample_audio 2
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320324.jpg)

 此时耳机里会一直播放录制的audio_chn0.aac文件内容，使用Ctrl + C停止播放。

## 2.11蜂鸣器测试

将底板拨码开关1和2拨到ON位置，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320368.jpg)

 PWM提供了用户层的接口，在/sys/class/pwm/节点下面：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320430.jpg)

 蜂鸣器使用PWM0的12通道，查看pwmchip0目录下文件，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320451.jpg)

 使用以下命令测试蜂鸣器：

~~~shell
echo 12 > /sys/class/pwm/pwmchip0/export 

echo 366300 > /sys/class/pwm/pwmchip0/pwm12/period 

echo 260000 > /sys/class/pwm/pwmchip0/pwm12/duty_cycle 

echo 1 > /sys/class/pwm/pwmchip0/pwm12/enable  //开启

echo 0 > /sys/class/pwm/pwmchip0/pwm12/enable  //关闭
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320499.jpg)

 修改第二句和第三句命令中的参数以修改pwm的占空比来控制蜂鸣器发出声音的大小。

## 2.12 温湿度测试

iTOP-Hi3403开发板板载DHT11模块，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320569.jpg)

 使用以下命令查看当前温度，如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device1/in_temp_input 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320627.jpg)

 使用以下命令查看当前湿度，如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device1/in_humidityrelative_input 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320649.jpg)

 ## 2.13 ADC电位器测试

iTOP-Hi3403开发板板载了一路电位器，原理图如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320679.jpg)

 电位器对应原理图如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320775.jpg)

 从上图可以看到电位器（R244）的原理很简单，使用1.8V供电，输出引脚通过IR_CUT_0_CONTROL1链接到Hi3403的LSADC_CH0引脚上了。这样就能够实现电位器的电压采集了，我们调节电位器上的旋钮，ADC采集到的电压会在0~1.8V范围内变化。

使用以下命令查看LSADC_CH0通道原始数据，如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320800.jpg)

 使用以下命令查看电压缩放因子（将原始采样值转换为实际电压值），如下图所示：

~~~shell
cat /sys/bus/iio/devices/iio\:device0/in_voltage0_scale
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320850.jpg)

 将读取到的in_voltage0_raw原始值511乘以in_voltage0_scale缩放因子1.757812500即可获得该通道的当前实际电压约为898mV（即0.9V）。

## 2.14 EMMC测试

下面简单测试EMMC的读写速度，以读写ext4文件系统为例。注意：为确保数据准确，请重启开发板后测试读取速度。 

~~~shell
dd if=/dev/zero of=/test bs=1M count=500 conv=fsync//写入测试 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320908.jpg)

 dd if=/test of=/dev/null bs=100M //读取测试 

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320931.jpg)

 ## 2.15 OS08A20摄像头测试

开发板默认支持摄像头接口。底板提供2个摄像头接口，默认提供的镜像可以使用***\*J1\****接口。迅为提供的OS08A20摄像头模块如下图所示。

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320983.jpg)

 

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320059.jpg)

 使用系统/sameple目录下的sample_vo例程进行测试，如下图所示：

~~~shell
./sample_vo 0
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320120.jpg)

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320148.jpg)

 ## 2.16 RTC时钟测试



Linux系统下分为系统时钟和硬件时钟。分别使用 date 和 hwclock 命令查看。系统时钟在系统断电以后会丢失，硬件时钟在有纽扣电池的情况下，系统断电，时钟不会丢失。在系统每次启动的时候，系统时钟会和硬件时钟进行同步。

首先启动开发板，通过调试串口登录到开发板上，如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320179.jpg)

 查看系统时钟在串口终端输入“date”命令，运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320232.jpg)

 查看硬件时钟，在串口输入“hwclock -u”命令查看硬件时钟，运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320283.jpg)

 也可以使用date命令来设置系统时间，例如置系统时间为2025年9月11号14:30:00，在串口终端输入命令“date -s "2025-9-11 14:30:00"”，设运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320327.jpg)

 然后使用“hwclock --systohc -u”命令把当前系统的时间同步到硬件时钟里面，然后使用“hwclock -u”命令查看硬件时钟。运行结果如图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320430.jpg)

 ## 2.17 HDMI测试

使用系统/sample目录下的sample_hdmi进行测试，sample_hdmi例程是解析H265格式视频文件通过HDMI接口输出到显示屏。如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320451.jpg)

 使用以下命令运行sample_hdmi进行测试，如下图所示：

~~~shell
./sample_hdmi
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320480.jpg)

 当前例程播放文件为/sample/source_file/3840x2160_8bit.h265，运行后HDMI屏显示视频文件，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320509.jpg)

 进入例程终端输入h查看帮助信息如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320600.jpg)

 输入q结束例程，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320626.jpg)

 ## 2.18 UVC摄像头测试

使用系统/sample目录下的sample_uvc进行测试，sample_uvc例程是一路usb摄像头输入到HDMI TX输出显示。如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320675.jpg)

 使用以下命令运行例程查看帮助信息，如下图所示：

~~~shell
./sample_uvc -h 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320714.jpg)

 将USB摄像头插入开发板，将自动安装uvc驱动，使用以下命令检查识别摄像头，如下图所示：

~~~shell
v4l2-ctl --list-devices 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320753.jpg)

 由上图可知，USB摄像头节点为/dev/video0。

首先查看USB摄像头设备可支持的格式，如下图所示：

~~~shell
./sample_uvc /dev/video0 --enum-formats 
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320804.jpg)

 使用以下命令运行例程查看摄像头画面（可根据自己实际打印，修改例程参数），如下图所示：

~~~shell
./sample_uvc /dev/video0 -fYUYV -s640x480 -Ftest.yuv
~~~

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320876.jpg)

运行后HDMI屏显示摄像头画面，如下图所示：

![img](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271320906.jpg)

 