## LubanCat-Hi3404功能验证说明

本文档对LubanCat-Hi3404板卡的一些硬件外设的使用方法和功能验证进行简略说明

本文档使用基于hispark/pegasus项目构建的buildroot镜像，镜像构建流程请查看文档 [基于Pegasus构建Buildroot系统镜像](基于Hi3403构建Buildroot系统镜像.md) 

### 引脚复用说明

由于Hi3403的引脚存在功能复用，当我们使用某一片上外设或外部模块前，需要先对该外设的引脚或模块所连的引脚配置适当的复用功能。

Hi3403完整的引脚复用配置可查看表格 [Hi3403V100_PINOUT_CN.xlsx](#)

在hispark/pegasus中，对芯片引脚复用功能的配置在两个位置：

- platform/Hi3403V100_gcc/osdrv/tools/pc/uboot_tools文件夹内编译boot时对应的xlsm表格：用于定义芯片初始化早期部分寄存器的值，u-boot或linux kernel初始化时使用的引脚需要在这里定义。
- platform/Hi3403V100_gcc/smp/a55_linux/interdrv/sysconfig: 内核外部模块，用于linux系统启动后，在引脚使用前对引脚复用功能进行配置。

一般情况下只需要修改sysconfig即可。修改完成后在sysconfig目录运行`make sysconfig`命令编译得到sys_config.ko，将sys_config.ko传输到板卡，使用`insmo sys_config.ko`加载模块就可以完成引脚复用功能配置。

以下是pin_mux.c中对LubanCat-Hi3403的特殊功能引脚进行配置的函数。
```
void lubancat_hi3403_pin_mux(void)
{
    void *iocfg2_base = sys_config_get_reg_iocfg2(); 

    sys_writel(iocfg2_base + 0x0030, 0x1200); /* SYS_LED GPIO4_2 */
    sys_writel(iocfg2_base + 0x005C, 0x1200); /* WIFI_PWR_EN GPIO0_1 */

#if FAN_CTRL_PWM
    sys_writel(iocfg2_base + 0x0100, 0x1205); /* FAN_CTRL PWM0_OUT14 */
#else
    sys_writel(iocfg2_base + 0x0100, 0x1201); /* FAN_CTRL GPIO10_1 */
#endif

    sys_writel(iocfg2_base + 0x0110, 0x1201); /* TP_INT GPIO10_5 */
    sys_writel(iocfg2_base + 0x0104, 0x1201); /* TP_RST GPIO10_2 */
    sys_writel(iocfg2_base + 0x0108, 0x1101); /* LCD_PWR_EN GPIO10_3 */
    sys_writel(iocfg2_base + 0x010C, 0x1101); /* LCD_RST GPIO10_4 */
    // sys_writel(iocfg2_base + 0x01EC, 0x1201); /* LCD_BL PWM0_OUT1 */
}
```
除此之外还有视频输入输出、音频、i2c、uart等接口的引脚配置，这些功能对于使用同一个芯片的不同板卡差异不大，一般不需要去修改。

### 功能验证及说明

以下外设功能验证时如果需要先进行引脚复用功能配置，会在标题下注明 **使用前需要先加载sys_config.ko**

#### USB接口

| USB接口 | 接口数量 | USB版本 |
| ------- | -------- | ------- |
| USB蓝色 | 1        | USB3.0  |
| USB黑色 | 1        | USB2.0  |
| USB白色 | 2        | USB2.0  |

蓝色USB接口还可作为镜像烧录接口，使用双公头USB线连接电脑，镜像下载工具传输方式选择USB(ToolPlatform v5.6.58版本可支持USB烧录)

```
# 查看USB设备
lsusb
```

#### 4G网卡

| 型号 | 规格     | 通信接口 | 通信协议  |
| ---- | -------- | -------- | --------- |
| EC20 | LTE Cat4 | USB2.0   | USB RNDIS |

支持Mini-PCIe接口的4G/5G网卡，使用Mini-PCIe插槽的USB数据线通信。

RNDIS是一种USB网络共享协议，无线网卡被配置为RNDIS模式时，4G网卡会被识别为一个USB网络设备，理论上所有能被配置为RNDIS模式的无线网卡都可以使用。

##### EC20使用说明

使用EC20前，还需要在LubanCat-Hi3404板卡的SIM卡接口插入SIM卡。

以下命令用于确认4G网卡和SIM卡状态，当4G网卡状态和SIM卡状态正常才具备拨号上网的条件。
```
# 关闭回显
echo -e "ATE0\r" > /dev/ttyUSB2

# 打印串口输出
cat /dev/ttyUSB2 &

# 查询产品型号和固件信息，没有应答的话，检查4G模块是否开机
echo -e "ATI\r\n" >  /dev/ttyUSB2

# 查询SIM卡号，没有返回ICCID卡号的话，检查SIM卡是否接好
echo -e "AT+ICCID\r\n" >  /dev/ttyUSB2

# 查看当前SIM卡状态，需要返回状态为 7
echo -e "AT+QINISTAT\r\n" >  /dev/ttyUSB2
SIM卡初始化状态。实际值为以下四种任意几种的数字和（例如： 7 = 1 + 2 + 4表示CPIN已就绪、SMS初始化完成且电话簿初始化完成）。
0 未初始化状态
1 CPIN已就绪，可执行锁定/解锁PIN操作
2 SMS初始化完成
4 电话簿初始化完成

# 查询网络信息，需要注册状态为 1 已注册
echo -e "AT+CGREG?\r\n" >  /dev/ttyUSB2
<n>,<stat> 
<stat> 整型。 GPRS 注册状态。
0 未注册。MT当前未搜索注册业务的运营商。
1 已注册，归属地网络。
2 未注册，但MT当前正尝试附着或搜索网络以进行注册。
3 注册被拒绝。
4 未知
5 已注册，漫游状态
```

如果EC20没有被配置为RNDIS模式，需要使用以下命令配置
```
#查询当前网卡的模式
echo -e "AT+QCFG=\"usbnet\"\r\n" >  /dev/ttyUSB2

+QCFG: "usbnet",3 : RNDIS模式
+QCFG: "usbnet",2 : MBIM模式
+QCFG: "usbnet",1 : ECM模式
+QCFG: "usbnet",0 : rmnet模式

#配置为RNDIS模式(返回：OK 代表配置成功)
echo -e "AT+QCFG=\"usbnet\",3\r\n" >  /dev/ttyUSB2

#重启模块（重启模块才能生效）
echo -e "AT+CFUN=1,1\r\n" >  /dev/ttyUSB2
```

完成模式配置后，会新增一个网络节点，并且自动拨号
```
# ifconfig

usb0      Link encap:Ethernet  HWaddr B6:4E:ED:C3:06:1C
          inet addr:192.168.225.28  Bcast:192.168.225.255  Mask:255.255.255.0
          inet6 addr: fe80::6f7b:6d02:a0fc:fcf8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:26 errors:0 dropped:0 overruns:0 frame:0
          TX packets:29 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:2283 (2.2 KiB)  TX bytes:2354 (2.2 KiB)

# ping baidu.com
PING baidu.com (220.181.7.203): 56 data bytes
64 bytes from 220.181.7.203: seq=0 ttl=47 time=72.739 ms
64 bytes from 220.181.7.203: seq=1 ttl=48 time=76.307 ms
64 bytes from 220.181.7.203: seq=2 ttl=48 time=75.195 ms
```

#### PCIe无线网卡

支持使用Mini-PCIe接口的无线网卡，其中WiFi使用PCIe协议通信，Bluetooth使用USB协议通信。

| 型号      | WiFi             | Bluetooth | WiFi实测速率            |
| --------- | ---------------- | --------- | ----------------------- |
| RTL8852BE | 80211AX 1200Mbps | BT5.2     | TX:604 RX:648 Mbits/sec |
| RTL8822CE | 80211AC 866Mbps  | BT5.0     | TX:817 RX:841 Mbits/sec |

上表为测试验证过的模块，理论上支持rtw88/rtw89驱动的RTL无线网卡都支持。WIFI实测速率为使用无线网卡连接redmi_ax6000无线路由器使用iperf3测试获得。

##### 查看设备信息

```
# 查看pcie设备
lspci

# 查看usb设备
lsusb
```

##### WIFI

```
# 打开wlan0接口
ifconfig wlan0 up

# 扫描无线网络
iw dev wlan0 scan 

# 修改wpa_supplicant配置文件中的无线SSID和密码
vi /etc/wpa_supplicant.conf

# 使用wpa_supplicant连接网络
wpa_supplicant -D nl80211 -i wlan0 -c /etc/wpa_supplicant.conf -B -d

# 查看无线物理连接状态
iw dev wlan0 link

# 查看网络连接状态
ifconfig wlan0
```
##### Bluetooth

```
# 查看hci蓝牙接口
hciconfig

# 使用bluetoochctl工具
bluetoochctl
# 开启蓝牙电源
[bluetooth]# power on
# 开启注册代理
[bluetooth]# agent on
# 扫描蓝牙设备
[bluetooth]# scan on
# 与蓝牙设备配对
[bluetooth]# pair xx:xx:xx:xx:xx:xx
# 信任蓝牙设备
[bluetooth]# trust xx:xx:xx:xx:xx:xx
# 连接蓝牙设备
[bluetooth]# connect xx:xx:xx:xx:xx:xx
```

需要注意，如果没有适配的Profile(上层功能)，蓝牙在连接后会自动断开。

#### USB无线网卡

LubanCat-Hi3404板载一个USB接口的AIC8800D40L无线网卡，支持单频2.4Ghz 802.11ac WIFI和BLE5.2低功耗蓝牙

使用前要先使能WIFI模块供电
```
gpioset gpiochip0 1=1
```
##### WIFI

与PCIe无线网卡连接方法一致

##### Bluetooth

由于AIC8800D40L仅支持BLE低功耗蓝牙，使用方法与经典蓝牙有差异，更多功能请自行学习

#### RTC

LubanCat-Hi3404板载一个i2c接口的RTC芯片，在板卡掉电后可以继续使用电池为RTC芯片供电，实现关机后保持系统时间。

```
# 查看日期
cat /sys/class/rtc/rtc0/date
# 查看时间
cat /sys/class/rtc/rtc0/time
# 查看rtc配置
cat /proc/driver/rtc

date -s "2026-08-08 08:00:00"  #手动设置时间
hwclock -w    #系统时间同步到硬件rtc
hwclock -s    #硬件rtc同步到系统
```

#### FAN

**使用前需要先加载sys_config.ko**

使用GPIO或PWM控制风扇，要修改pin_mux.c中FAN_CTRL_PWM的定义去切换
```
# 使用GPIO控制风扇
# 开启风扇
gpioset gpiochip10 1=1
# 关闭风扇
gpioset gpiochip10 1=0

# 使用PWM控制风扇
echo 14 > /sys/class/pwm/pwmchip0/export
echo 5000000 > /sys/class/pwm/pwmchip0/pwm14/period
echo 2500000 > /sys/class/pwm/pwmchip0/pwm14/duty_cycle
echo 1 > /sys/class/pwm/pwmchip0/pwm14/enable
# 修改占空比对风扇进行调速
echo 4000000 > /sys/class/pwm/pwmchip0/pwm14/duty_cycle
```
#### 触摸屏
**使用前需要先加载sys_config.ko**

首先加载触摸IC驱动。如果使用野火7寸MIPI屏(EBF410655)，需要在加载驱动时传入触摸坐标翻转参数：
```
modprobe goodix_ts.ko invert_x=1 invert_y=1
```
驱动加载完成后可以使用命令`evtest`选择 Goodix Capacitive TouchScreen 进行触摸测试

### MPP媒体处理平台功能验证

有关MPP媒体处理平台的介绍可以参考文档 [MPP媒体处理软件V5.0开发参考](/multimedia/mpp/)

#### 编译和运行环境搭建

在进行功能验证前，要先在SDK中对示例程序、相关的ko驱动模块和lib文件进行编译。然后在板卡端设置运行环境，才能运行示例程序对音视频输入输出接口进行测试。

##### 编译库文件和驱动模块

进入platform/Hi3403V100_gcc/smp/a55_linux/mpp/out/目录

在obj目录下执行`make`命令，编译得到的ko模块和lib文件分别保存在out目录的ko和lib目录

查看ko目录内的文件，已经包含了sys_config.ko、ot_hdmi.ko、ot_mipi_rx.ko等驱动模块，用于设置芯片的引脚功能和硬件接口配置。

查看ko目录内的load_Hi3403V100_user脚本，这是一个用于加载和卸载模块的脚本。其参数介绍如下：

- -i                       加载模块
- -r                       卸载模块
- -a                       卸载模块后重新加载
- -sensor0~3 sensor_name   设置摄像头名称
- -total mem_size          总物理内存
- -osmem os_mem_size       Linux系统占用内存，/proc/cmdline中mem对应的大小

通过设置mem_size和os_mem_size，可以计算得出MPP可使用的内存大小。

具体计算及调整方法查看文档 [内存布局调整指南.md](../../../soc-linux/memory-layout/index.md)

将lib文件和驱动模块传输到板卡中。以通过网络使用scp命令为例，在platform/Hi3403V100_gcc/smp/a55_linux/mpp/out/目录中执行下面的命令：

```
# 将lib下的所有文件传输到板卡/lib目录下
scp -r ./lib/*  root@192.168.5.53:/lib/

# 将ko目录传输到板卡/root目录下
scp -r ./ko/  root@192.168.5.53:/root/
```
执行上面命令时将ip地址替换为板卡在局域网内的ip

如果提升空间不足，可以运行`resize2fs /dev/mmcblk0p3`命令，可将rootfs分区扩展到eMMC的剩余空间。

##### 编译示例程序

进入platform/Hi3403V100_gcc/smp/a55_linux/mpp/sample目录，使用`make`命令一次性编译所有示例程序，编译生成的可执行文件保存在示例程序对应目录中。

也可以进入sample目录下示例程序单独的目录，使用`make`命令编译当前示例程序。

将编译得到的可执行文件传输到板卡中。

如果修改后要重新编译，要先`make clean`后再`make`

##### 板端运行环境搭建

lib文件在之前的步骤中已经传输到了板卡的/lib目录下，还需要加载模块。

进入板卡/root/ko目录下，执行`./load_Hi3403V100_user -i`命令，运行脚本加载模块。

#### HDMI

使用HDMI线连接板卡和显示器的HDMI接口。

将编译好的hdmi示例程序传输到板卡。由于还需要一些资源文件，直接将整个hdmi文件夹传输到板卡。

```
scp -r hdmi/ root@192.168.5.53:/root
```

进入板卡/root/hdmi目录下，执行`sample_hdmi`后，屏幕会播放视频和音频

#### MIPI-CSI

LubanCat-Hi3403板卡的MIPI-CSI接口引脚电平为1.8V，需要搭配1.8V电平的MIPI-CSI摄像头，在使用时请注意区分。

以适配的IMX415为例，板卡断电后使用FPC排线连接板卡的CAM接口和摄像头模块，注意排线方向，摄像头接口1-30脚要与板卡CAM接口1-30脚顺序相连。

在编译示例程序前要确认配置文件：

- sample/Makefile.param中SENSOR{0,1,2,3}_TYPE设置为将要使用的摄像头SONY_IMX415_MIPI_8M_30FPS_12BIT

- sample/vio/sample_vio.c中可通过修改g_vo_cfg的配置来修改hdmi屏幕的显示参数，参数与屏幕不符可能无法显示。默认HDMI、1080P60、YVU420。

修改配置后重新编译，将编译好的vio示例程序传输到板卡。

```
scp -r vio/ root@192.168.5.53:/root
```

在执行sample_vio前还要确认，在加载模块执行load_Hi3403V100_user脚本时打会打印sensors型号，如果不是imx415则要在加载模块时添加sensor参数，如果是imx415则可以忽略。
```
./load_Hi3403V100_user -i -sensor0 imx415 -sensor1 imx415 -sensor2 imx415 -sensor3 imx415
```

进入板卡/root/vio目录下，执行`./sample_vio 0`，稍后的vpss mode选择0，继续执行会初始化摄像头，然后将摄像头画面显示在hdmi屏幕上。同时将视频进行编码，保存到文件stream_chn0.h265。

如果要验证双摄，则可以执行`./sample_vio 0`，会将两路摄像头CAM0和CAM1的画面都显示在屏幕上

#### MIPI-DSI

LubanCat-Hi3403板卡的MIPI-DSI接口引脚电平为1.8V，需要搭配1.8V电平的MIPI-DSI屏幕使用，在使用时请注意区分。

以适配的野火7寸MIPI屏幕EBF410655为例，板卡断电后使用FPC排线连接板卡的DSI接口和屏幕，注意排线方向，屏幕接口1-30脚要与板卡DSI接口1-30脚顺序相连。

```
scp vo/sample_vo root@192.168.5.53:/root
```

由于sample_vo示例是将摄像头获取的图像显示到屏幕上，所以运行示例前要确保摄像头连接正确，摄像头配置正确。

进入板卡/root目录下，执行`./sample_vio 1`将会使用EBF410655的参数去初始化屏幕，然后将摄像头获取的图像显示到MIPI屏幕上。

#### 音频

使用耳机或音响连接板卡的耳机接口。

将编译好的audio示例程序传输到板卡。

```
scp audio/sample_audio root@192.168.5.53:/root
```
进入板卡/root目录下，执行`sample_audio 0`，对着耳机麦克风说话，会在耳机中听到声音。

sample_audio的参数如下：

```
# 回环模式 麦克风 -> 喇叭
0:  start AI to AO loop

# 录音并编码保存文件
1:  send audio frame to AENC channel from AI, save them

# 读取音频文件并播放
2:  read audio stream from file, decode and send AO

# 回环模式(质量增强处理) 麦克风 -> 喇叭
3:  start AI(VQE process), then send to AO

# 回环模式 麦克风 -> HDMI
4:  start AI to AO(HDMI) loop

# 回环模式 麦克风 -> sys_chn
5:  start AI to AO(sys_chn) loop

# 录音重采样后保存文件
6:  start AI, then send to resample, save it
```
