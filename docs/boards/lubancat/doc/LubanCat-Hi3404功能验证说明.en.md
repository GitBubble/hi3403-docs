## LubanCat-Hi3404 Functional Verification Guide

This document provides a brief description of the usage and functional verification of some hardware peripherals on the LubanCat-Hi3404 board.

This document uses a Buildroot image built based on the hispark/pegasus project. For the image build process, please refer to the document [Building Buildroot System Image Based on Pegasus](基于Hi3403构建Buildroot系统镜像.md).

### Pin Multiplexing Description

Since Hi3403 pins have function multiplexing, before using a particular on-chip peripheral or external module, the corresponding pin or module pins must be configured with the appropriate multiplexing function.

The complete Hi3403 pin multiplexing configuration can be found in the table [Hi3403V100_PINOUT_CN.xlsx](#).

In hispark/pegasus, the chip pin multiplexing function is configured in two locations:

- The xlsm table corresponding to the compiled boot in the platform/Hi3403V100_gcc/osdrv/tools/pc/uboot_tools folder: used to define the values of some registers in the early chip initialization phase. Pins used by u-boot or linux kernel initialization need to be defined here.
- platform/Hi3403V100_gcc/smp/a55_linux/interdrv/sysconfig: kernel external module, used to configure pin multiplexing functions after the linux system starts, before pins are used.

Generally, only sysconfig needs to be modified. After modification, run the `make sysconfig` command in the sysconfig directory to compile sys_config.ko. Transfer sys_config.ko to the board and load the module with `insmod sys_config.ko` to complete the pin multiplexing configuration.

Below is the function in pin_mux.c that configures the special function pins of the LubanCat-Hi3403.
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
Additionally, there are pin configurations for video input/output, audio, i2c, uart, and other interfaces. These functions have little difference between different boards using the same chip and generally do not need modification.

### Functional Verification and Description

If the following peripheral functional verification requires pin multiplexing configuration first, it will be noted under the title as **sys_config.ko must be loaded before use**.

#### USB Interface

| USB Port | Quantity | USB Version |
| -------- | -------- | ----------- |
| Blue USB | 1        | USB 3.0     |
| Black USB | 1        | USB 2.0     |
| White USB | 2        | USB 2.0     |

The blue USB port can also be used as an image Flashing interface. Connect it to a computer using a dual male USB cable, and select USB as the transmission method in the image flashing tool (ToolPlatform v5.6.58 supports USB Flashing).

```
# View USB devices
lsusb
```

#### 4G Modem

| Model | Specification | Communication Interface | Communication Protocol |
| ----- | ------------- | --------------------- | --------------------- |
| EC20  | LTE Cat4      | USB 2.0               | USB RNDIS             |

Supports Mini-PCIe interface 4G/5G modems, using the Mini-PCIe slot's USB data lines for communication.

RNDIS is a USB network sharing protocol. When the wireless modem is configured in RNDIS mode, the 4G modem is recognized as a USB network device. In theory, any wireless modem that can be configured to RNDIS mode can be used.

##### EC20 Usage Instructions

Before using EC20, insert a SIM card into the SIM card slot of the LubanCat-Hi3404 board.

The following commands are used to confirm the 4G modem and SIM card status. Dial-up internet access is only possible when both the 4G modem and SIM card status are normal.
```
# Disable echo
echo -e "ATE0\r" > /dev/ttyUSB2

# Print serial output
cat /dev/ttyUSB2 &

# Query product model and firmware information; if no response, check if the 4G module is powered on
echo -e "ATI\r\n" >  /dev/ttyUSB2

# Query SIM card number; if no ICCID is returned, check if the SIM card is properly inserted
echo -e "AT+ICCID\r\n" >  /dev/ttyUSB2

# View current SIM card status; the returned status must be 7
echo -e "AT+QINISTAT\r\n" >  /dev/ttyUSB2
SIM card initialization status. The actual value is the sum of any combination of the following four numbers (e.g., 7 = 1 + 2 + 4 means CPIN ready, SMS initialization complete, and phonebook initialization complete).
0 Not initialized
1 CPIN ready, PIN lock/unlock operations can be performed
2 SMS initialization complete
4 Phonebook initialization complete

# Query network information; registration status must be 1 (registered)
echo -e "AT+CGREG?\r\n" >  /dev/ttyUSB2
<n>,<stat> 
<stat> Integer. GPRS registration status.
0 Not registered. MT is not currently searching for an operator to register with.
1 Registered, home network.
2 Not registered, but MT is currently attempting to attach or searching for a network to register with.
3 Registration denied.
4 Unknown
5 Registered, roaming
```

If the EC20 is not configured in RNDIS mode, use the following commands to configure it.
```
# Query current modem mode
echo -e "AT+QCFG=\"usbnet\"\r\n" >  /dev/ttyUSB2

+QCFG: "usbnet",3 : RNDIS mode
+QCFG: "usbnet",2 : MBIM mode
+QCFG: "usbnet",1 : ECM mode
+QCFG: "usbnet",0 : rmnet mode

# Configure to RNDIS mode (return: OK means configuration successful)
echo -e "AT+QCFG=\"usbnet\",3\r\n" >  /dev/ttyUSB2

# Restart the module (must restart for the configuration to take effect)
echo -e "AT+CFUN=1,1\r\n" >  /dev/ttyUSB2
```

After completing the mode configuration, a new network node will appear and automatically dial up.
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

#### PCIe Wireless Network Card

Supports Mini-PCIe interface wireless network cards, where WiFi communicates using the PCIe protocol and Bluetooth communicates using the USB protocol.

| Model     | WiFi             | Bluetooth | Measured WiFi Throughput        |
| --------- | ---------------- | --------- | ------------------------------- |
| RTL8852BE | 802.11AX 1200Mbps | BT 5.2    | TX:604 RX:648 Mbits/sec         |
| RTL8822CE | 802.11AC 866Mbps  | BT 5.0    | TX:817 RX:841 Mbits/sec         |

The table above shows tested and verified modules. In theory, RTL wireless network cards with rtw88/rtw89 drivers are supported. Measured WiFi throughput was obtained using iperf3 with the wireless network card connected to a redmi_ax6000 wireless router.

##### View Device Information

```
# View PCIe devices
lspci

# View USB devices
lsusb
```

##### WiFi

```
# Bring up wlan0 interface
ifconfig wlan0 up

# Scan for wireless networks
iw dev wlan0 scan 

# Modify the wireless SSID and password in the wpa_supplicant configuration file
vi /etc/wpa_supplicant.conf

# Connect to the network using wpa_supplicant
wpa_supplicant -D nl80211 -i wlan0 -c /etc/wpa_supplicant.conf -B -d

# View wireless physical connection status
iw dev wlan0 link

# View network connection status
ifconfig wlan0
```
##### Bluetooth

```
# View hci Bluetooth interface
hciconfig

# Use the bluetoothctl tool
bluetoothctl
# Enable Bluetooth power
[bluetooth]# power on
# Enable registration agent
[bluetooth]# agent on
# Scan for Bluetooth devices
[bluetooth]# scan on
# Pair with a Bluetooth device
[bluetooth]# pair xx:xx:xx:xx:xx:xx
# Trust a Bluetooth device
[bluetooth]# trust xx:xx:xx:xx:xx:xx
# Connect to a Bluetooth device
[bluetooth]# connect xx:xx:xx:xx:xx:xx
```

Note that without an appropriate Profile (upper-layer function), Bluetooth will disconnect automatically after connecting.

#### USB Wireless Network Card

The LubanCat-Hi3404 has a built-in USB interface AIC8800D40L wireless network card, supporting single-band 2.4 GHz 802.11ac WiFi and BLE 5.2 low-power Bluetooth.

Before use, enable the WiFi module power supply.
```
gpioset gpiochip0 1=1
```
##### WiFi

Same connection method as PCIe wireless network card.

##### Bluetooth

Since the AIC8800D40L only supports BLE low-power Bluetooth, the usage method differs from classic Bluetooth. Please study further for more features.

#### RTC

The LubanCat-Hi3404 has an onboard i2c interface RTC chip. After the board loses power, a battery can continue to power the RTC chip, maintaining the system time after shutdown.

```
# View date
cat /sys/class/rtc/rtc0/date
# View time
cat /sys/class/rtc/rtc0/time
# View RTC configuration
cat /proc/driver/rtc

date -s "2026-08-08 08:00:00"  # Manually set the time
hwclock -w    # Sync system time to hardware RTC
hwclock -s    # Sync hardware RTC to system
```

#### FAN

**sys_config.ko must be loaded before use**

Use GPIO or PWM to control the fan. Modify the FAN_CTRL_PWM definition in pin_mux.c to switch.
```
# Use GPIO to control the fan
# Turn on the fan
gpioset gpiochip10 1=1
# Turn off the fan
gpioset gpiochip10 1=0

# Use PWM to control the fan
echo 14 > /sys/class/pwm/pwmchip0/export
echo 5000000 > /sys/class/pwm/pwmchip0/pwm14/period
echo 2500000 > /sys/class/pwm/pwmchip0/pwm14/duty_cycle
echo 1 > /sys/class/pwm/pwmchip0/pwm14/enable
# Adjust fan speed by modifying the duty cycle
echo 4000000 > /sys/class/pwm/pwmchip0/pwm14/duty_cycle
```
#### Touchscreen
**sys_config.ko must be loaded before use**

First, load the touch IC driver. If using a Wildfire 7-inch MIPI screen (EBF410655), pass touch coordinate inversion parameters when loading the driver:
```
modprobe goodix_ts.ko invert_x=1 invert_y=1
```
After the driver is loaded, use the `evtest` command and select Goodix Capacitive TouchScreen for touch testing.

### MPP Media Processing Platform Functional Verification

For an introduction to the MPP media processing platform, refer to the document [MPP Media Processing Software V5.0 Development Reference](/multimedia/mpp/).

#### Compilation and Runtime Environment Setup

Before functional verification, compile the sample programs, related ko driver modules, and lib files in the SDK. Then configure the runtime environment on the board side to test the audio/video input/output interfaces with the sample programs.

##### Compile Library Files and Driver Modules

Navigate to the platform/Hi3403V100_gcc/smp/a55_linux/mpp/out/ directory.

Run the `make` command in the obj directory. The compiled ko modules and lib files are saved in the ko and lib directories of the out directory respectively.

Check the files in the ko directory — they already include sys_config.ko, ot_hdmi.ko, ot_mipi_rx.ko, and other driver modules for setting the chip's pin functions and hardware interface configuration.

Check the load_Hi3403V100_user script in the ko directory. This is a script for loading and unloading modules. Its parameters are as follows:

- -i                       Load modules
- -r                       Unload modules
- -a                       Unload and then reload modules
- -sensor0~3 sensor_name   Set the camera name
- -total mem_size          Total physical memory
- -osmem os_mem_size       Linux system memory, corresponding to the mem size in /proc/cmdline

By setting mem_size and os_mem_size, the memory size available for MPP can be calculated.

For specific calculation and adjustment methods, refer to the document [Memory Layout Adjustment Guide.md](../../../soc-linux/memory-layout/index.md).

Transfer the lib files and driver modules to the board. For example, using the scp command over the network, execute the following command from the platform/Hi3403V100_gcc/smp/a55_linux/mpp/out/ directory:

```
# Transfer all files in lib to the board's /lib directory
scp -r ./lib/*  root@192.168.5.53:/lib/

# Transfer the ko directory to the board's /root directory
scp -r ./ko/  root@192.168.5.53:/root/
```
Replace the IP address with the board's local IP address when executing the above command.

If insufficient space is reported, run the `resize2fs /dev/mmcblk0p3` command to expand the rootfs partition to the remaining eMMC space.

##### Compile Sample Programs

Navigate to the platform/Hi3403V100_gcc/smp/a55_linux/mpp/sample directory. Use the `make` command to compile all sample programs at once. The compiled executable files are saved in the corresponding sample program directories.

You can also enter a specific sample program directory under the sample directory and use the `make` command to compile only that sample program.

Transfer the compiled executable files to the board.

If modifications are made and recompilation is needed, first run `make clean` then `make`.

##### Board-Side Runtime Environment Setup

The lib files have already been transferred to the board's /lib directory in the previous steps. Now the modules need to be loaded.

Navigate to the /root/ko directory on the board and run the `./load_Hi3403V100_user -i` command to load the modules.

#### HDMI

Connect the board and monitor's HDMI port using an HDMI cable.

Transfer the compiled hdmi sample program to the board. Since resource files are also needed, transfer the entire hdmi folder to the board.

```
scp -r hdmi/ root@192.168.5.53:/root
```

Navigate to the /root/hdmi directory on the board and run `sample_hdmi`. Video and audio will start playing on the screen.

#### MIPI-CSI

The MIPI-CSI interface pin level on the LubanCat-Hi3403 board is 1.8V and requires a 1.8V level MIPI-CSI camera. Please pay attention when using.

Using the adapted IMX415 as an example: after powering off the board, connect the board's CAM interface and the camera module using an FPC cable, paying attention to the cable direction. Pins 1-30 of the camera interface must connect in order to pins 1-30 of the board's CAM interface.

Before compiling the sample program, confirm the configuration file:

- Set SENSOR{0,1,2,3}_TYPE in sample/Makefile.param to the camera to be used: SONY_IMX415_MIPI_8M_30FPS_12BIT

- In sample/vio/sample_vio.c, modify the g_vo_cfg configuration to adjust the hdmi screen display parameters. Parameters that do not match the screen may cause no display. Default: HDMI, 1080P60, YVU420.

After modifying the configuration, recompile and transfer the compiled vio sample program to the board.

```
scp -r vio/ root@192.168.5.53:/root
```

Before running sample_vio, confirm that when executing the load_Hi3403V100_user script to load modules, it prints the sensor model. If it is not imx415, add the sensor parameter when loading the module. If it is imx415, this can be ignored.
```
./load_Hi3403V100_user -i -sensor0 imx415 -sensor1 imx415 -sensor2 imx415 -sensor3 imx415
```

Navigate to the /root/vio directory on the board. Run `./sample_vio 0`. When prompted for vpss mode, select 0. The camera will initialize and display on the hdmi screen. The video will also be encoded and saved to stream_chn0.h265.

To verify dual cameras, run `./sample_vio 0`. Both CAM0 and CAM1 camera feeds will be displayed on the screen.

#### MIPI-DSI

The MIPI-DSI interface pin level on the LubanCat-Hi3403 board is 1.8V and requires a 1.8V level MIPI-DSI screen. Please pay attention when using.

Using the adapted Wildfire 7-inch MIPI screen EBF410655 as an example: after powering off the board, connect the board's DSI interface and the screen using an FPC cable, paying attention to the cable direction. Pins 1-30 of the screen interface must connect in order to pins 1-30 of the board's DSI interface.

```
scp vo/sample_vo root@192.168.5.53:/root
```

Since the sample_vo sample displays images from the camera on the screen, ensure the camera is properly connected and configured before running the sample.

Navigate to the /root directory on the board. Run `./sample_vio 1`. This will use EBF410655 parameters to initialize the screen and display images from the camera on the MIPI screen.

#### Audio

Connect headphones or speakers to the board's headphone jack.

Transfer the compiled audio sample program to the board.

```
scp audio/sample_audio root@192.168.5.53:/root
```
Navigate to the /root directory on the board. Run `sample_audio 0` and speak into the headset microphone. You will hear the sound through the headphones.

The sample_audio parameters are as follows:

```
# Loopback mode: microphone -> speaker
0:  start AI to AO loop

# Record and encode, save to file
1:  send audio frame to AENC channel from AI, save them

# Read audio file and play
2:  read audio stream from file, decode and send AO

# Loopback mode (quality enhancement): microphone -> speaker
3:  start AI(VQE process), then send to AO

# Loopback mode: microphone -> HDMI
4:  start AI to AO(HDMI) loop

# Loopback mode: microphone -> sys_chn
5:  start AI to AO(sys_chn) loop

# Record, resample, and save to file
6:  start AI, then send to resample, save it
```
