---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/Peripheral Device Driver Operation Guide/Peripheral Device Driver Operation Guide.md
---

# Preface
**Overview<a name="section15117166194219"></a>**

This document guides personnel using driver modules such as GMAC, USB, and eMMC to control peripheral devices connected to these driver modules through specific steps and methods. It mainly includes operation preparation, operation procedures, issues to note during operation, and operation examples.

>![](public_sys-resources/icon-note.gif) **Note:** 
>This document uses the SS928V100 description as an example. Unless otherwise specified, the content for SS927V100 is consistent with SS928V100.

**Product Version<a name="section10120166104220"></a>**

The product versions corresponding to this document are as follows.

<a name="table1612713694220"></a>
<table><thead align="left"><tr id="row13191136144220"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p41918612421"><a name="p41918612421"></a><a name="p41918612421"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p14191663422"><a name="p14191663422"></a><a name="p14191663422"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row1819118616425"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p81911613425"><a name="p81911613425"></a><a name="p81911613425"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p91911617427"><a name="p91911617427"></a><a name="p91911617427"></a>V100</p>
</td>
</tr>
<tr id="row64983499368"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p182829527361"><a name="p182829527361"></a><a name="p182829527361"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p4282165214366"><a name="p4282165214366"></a><a name="p4282165214366"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Target Audience<a name="section81264620425"></a>**

This document (guide) is primarily applicable to the following engineers:

-   Technical Support Engineer
-   Software Development Engineer

**Revision History<a name="section2467512116410"></a>**

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p18213152074216"><a name="p18213152074216"></a><a name="p18213152074216"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p87086249422"><a name="p87086249422"></a><a name="p87086249422"></a>2025-11-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p492913284427"><a name="p492913284427"></a><a name="p492913284427"></a>First interim version release</p>
</td>
</tr>
</tbody>
</table>

# Linux
## GMAC Operation Guide<a name="ZH-CN_TOPIC_0000002512063505"></a>

### Operation Examples<a name="ZH-CN_TOPIC_0000002479903676"></a>

>![](public_sys-resources/icon-note.gif) **Note:** 
>By default, all related GMAC modules are compiled into the kernel, so no loading operation is required. Please skip directly to the step for configuring the IP address.

Under the kernel, using the network interface involves the following aspects:

-   The GMAC module supports TSO and it is enabled by default. If the user wishes to disable TSO, it can be turned off using the ethtool tool. The methods for toggling TSO are as follows:

    -   Disable TSO: ./ethtool -K eth0 tx off
    -   Enable TSO: ./ethtool -K eth0 tx on

    TSO (TCP Segment Offload) overview:

    -   TSO (TCP Segmentation Offload) is a technology that uses the network card to segment large data packets, reducing CPU load. It is also known as LSO (Large Segment Offload). If the data packet type is only TCP, it is called TSO. If the hardware supports TSO, it must also support hardware TCP checksum calculation and Scatter Gather functionality. TSO is implemented through a combination of software and hardware. Specifically, the hardware can fragment large data packets and attach relevant headers to each fragment.
    -   When the chip uses TSO, part of the processing work originally handled by the CPU is transferred to the network card, reducing CPU pressure and improving performance.

-   Configure IP address and subnet mask

    ```
    ifconfig eth0 xxx.xxx.xxx.xxx netmask xxx.xxx.xxx.xxx up
    ```

-   Set default gateway

    ```
    route add default gw xxx.xxx.xxx.xxx
    ```

-   Mount NFS

    ```
    mount -t nfs -o nolock xxx.xxx.xxx.xxx:/your/path /mount-dir
    ```

-   Upload/download files via tftp in the shell

    Prerequisite is that the tftp service software is running on the server side.

    -   Download file: tftp -r XX.file serverip -g

        Where: XX.file is the file to download, serverip is the IP address of the server where the file resides.

    -   Upload file: tftp -l xx.file remoteip -p

        Where: xx.file is the file to upload, remoteip is the IP address of the server to which the file is uploaded.

### IPv6 Description<a name="ZH-CN_TOPIC_0000002479903632"></a>

IPv6 is disabled by default in the release package. To support IPv6, you need to modify kernel options and recompile the kernel. The specific steps are as follows:

```
cd open_source/linux/linux-4.19.y
cp arch/arm64/configs/ss928v100_defconfig .config
make ARCH=arm64 CROSS_COMPILE=aarch64-mix210-linux- menuconfig
```

Enter the following directory and configure the page options as shown in [Figure 1](#_Toc498609228).

```
[*] Networking support  --->
    Networking options  --->
        <*>   The IPv6 protocol  --->
```

**Figure 1** IPv6 Protocol Configuration Diagram<a name="_Toc498609228"></a>  
![](figures/IPv6-Protocol configuration diagram.png "IPv6-Protocol configuration diagram")

IPv6 environment configuration:

-   Configure IP address and default gateway

    ```
    ip -6 addr add <ipv6address>/<ipv6_prefixlen> dev <port>
    ```

    ```
    Example: ip -6 addr add 2001:da8:207::9402/64 dev eth0
    ```

-   Ping an IPv6 address

    ```
    ping -6 <ipv6address>
    Example: ping -6 2001:da8:207::9403
    ```

### PHY Address Configuration<a name="ZH-CN_TOPIC_0000002512063515"></a>

-   Configuration method under U-boot

    Under U-boot, you can configure different PHY addresses by modifying the values of the macros CONFIG\_GMAC\_PHY0\_ADDR and CONFIG\_GMAC\_PHY1\_ADDR in the U-boot configuration file include/configs/ss928v100.h.

-   Configuration method under Kernel

    Under the kernel, you can configure the PHY address by modifying the dts configuration file ss928v100-demb.dts under arch/arm64/boot/dts/vendor. As shown in [Figure 1](#_Toc498609229), the value "1" in "reg = <1>" represents the PHY address.

**Figure 1** PHY Address Configuration Node Diagram<a name="_Toc498609229"></a>  
![](figures/PHY address configuration node diagram.png "PHY address configuration node diagram")

### IEEE 802.3x Flow Control Configuration<a name="ZH-CN_TOPIC_0000002480063688"></a>

#### Flow Control Feature Description<a name="ZH-CN_TOPIC_0000002512103529"></a>

The GMAC network supports the flow control function defined by IEEE 802.3x, capable of sending flow control frames and receiving/processing flow control frames from the peer.

-   Flow control frame transmission:

    On the receiving side, if the current receive descriptor queue becomes strained and may not be able to deliver all received data packets to the software, a flow control frame is sent to the peer, instructing it to pause transmission for a certain period.

-   Flow control frame reception:

    When a flow control frame is received, the GMAC delays transmission based on the flow control time field in the frame. Once the timer reaches the flow control time, transmission resumes. Alternatively, if a flow control frame with a flow control time of 0 is received from the peer during the wait, transmission also resumes.

#### Flow Control Configuration<a name="ZH-CN_TOPIC_0000002512103583"></a>

The flow control configuration method is as follows:

```
cd open_source/linux/linux-4.19.y
cp arch/arm64/configs/ss928v100_defconfig .config
make ARCH=arm64 CROSS_COMPILE=aarch64-mix210-linux- menuconfig
```

The corresponding options are:

```
Device Drivers  --->
  [*] Network device support  --->
    [*]   Ethernet driver support  --->
      [*]    Vendor devices
        <*>     eth gmac family network device support  --->
```

![](figures/zh-cn_image_0000002479903736.png)

User-configurable flow control parameters:

-   CONFIG\_RX\_FLOW\_CTRL\_SUPPORT: Enables or disables reception of flow control frames.
-   CONFIG\_TX\_FLOW\_CTRL\_SUPPORT: Enables or disables transmission of flow control frames.
-   CONFIG\_TX\_FLOW\_CTRL\_ACTIVE\_THRESHOLD: The activation watermark for sending flow control frames. When the number of available descriptors in the receive queue falls below this value, the logic to send flow control frames is initiated.
-   CONFIG\_TX\_FLOW\_CTRL\_DEACTIVE\_THRESHOLD: The deactivation watermark for sending flow control frames. When the number of available descriptors in the receive queue is greater than or equal to this value and the system is currently in a flow control state, the current flow control state is released.

>![](public_sys-resources/icon-note.gif) **Note:** 
>The activation watermark value must be less than the deactivation watermark.

#### ethtool Configuration Interface<a name="ZH-CN_TOPIC_0000002480063656"></a>

Users can enable or disable the flow control function through the standard ethtool tool interface.

Command `ethtool -a eth0` to view the flow control status of the eth0 interface; output:

```
# ./ethtool -a eth0
Pause parameters for eth0:
Autonegotiate:  on
RX:             on
TX:             on
```

Here, RX flow control is enabled, and TX flow control is enabled.

Users can enable or disable TX flow control with the following commands:

```
# ./ethtool -A eth0 tx off (Disable TX flow control)
# ./ethtool -A eth0 tx on (Enable TX flow control)
```

### Ipfrag Parameter Configuration<a name="ZH-CN_TOPIC_0000002512063515"></a>

When receiving UDP data streams with high bandwidth and large packet sizes under unstable network conditions, fragment memory may be exhausted, causing the protocol stack to proactively drop packets. It is recommended to appropriately increase the values of the IP parameters `ipfrag_high_thresh` and `ipfrag_low_thresh`. The current default values are 4194304 and 3145728.

Modification method: xxx is the value to set

```
~ # echo xxx > /proc/sys/net/ipv4/ipfrag_high_thresh
~ # echo xxx > /proc/sys/net/ipv4/ipfrag_low_thresh
```

Parameter descriptions:

`ipfrag_high_thresh` sets the maximum amount of memory in the kernel that can be used for IP fragment reassembly. When this maximum boundary is reached, the handler responsible for fragment reassembly will discard all pending IP fragments until the memory usage falls back to the minimum boundary value `ipfrag_low_thresh`.

### Dual Ethernet Port Configuration<a name="ZH-CN_TOPIC_0000002512063533"></a>

When the application scenario requires dual Ethernet ports, the default SDK and demo board do not support dual ports. Customers need to configure dual ports themselves. The following configuration example uses GMAC0 as a Gigabit Ethernet (rgmii) with PHY address 1, and GMAC1 as a 100-Megabit Ethernet (rmii) with PHY address 3. The specific MAC mode and PHY address depend on the customer's hardware design:

GMAC0 1000M (rgmii) phy 1

GMAC1 100M (rmii) phy 3

U-boot modification points:

Enter the U-boot directory: vim include/configs/ss928v100.h

Modified values:

```
/*Network configuration*/
#define CONFIG_PHY_GIGE
#ifdef CONFIG_GMACV300_ETH
#define CONFIG_GMAC_NUMS        2
#define CONFIG_GMAC_PHY0_ADDR     1
#define CONFIG_GMAC_PHY0_INTERFACE_MODE       2 /* rgmii 2, rmii 1, mii 0 */
#define CONFIG_GMAC_PHY1_ADDR     3
#define CONFIG_GMAC_PHY1_INTERFACE_MODE       1 /* rgmii 2, rmii 1, mii 0 */
#define CONFIG_GMAC_DESC_4_WORD
#define CONFIG_SYS_FAULT_ECHO_LINK_DOWN 1
#endif
```

Linux modification points:

Enter the Linux directory: vim arch/arm64/boot/dts/vendor/ss928v100-demb.dts

Modified values:

```
&mdio {
        ethphy: ethernet-phy@1 {
                reg = <1>;
        };
};
&mdio1 {
        ethphy1: ethernet-phy@3 {
                reg = <3>;
        };
};
 
&gmac {
        phy-handle = <&ethphy>;
        phy-mode = "rgmii";
};
 
&gmac1 {
        phy-handle = <&ethphy1>;
        phy-mode = "rmii";
};
```

## USB Operation Guide<a name="ZH-CN_TOPIC_0000002512063507"></a>

### Preparation<a name="ZH-CN_TOPIC_0000002480063646"></a>

The USB ports on the current product provide up to USB 3.0 speed. Their host/device modes are: USB3\_0 port only supports USB Host mode; USB3\_1 port can be used in either Host mode or Device mode. The default SDK version uses Device mode.

USB preparation steps:

-   U-boot and Linux kernel use the U-boot and kernel released with the SDK.
-   The file system can use a local file system such as jffs2, ext4, or cramfs, or NFS.

### Operation Process<a name="ZH-CN_TOPIC_0000002512063493"></a>

#### USB Host Operation Process under Uboot<a name="ZH-CN_TOPIC_0000002480063630"></a>

>![](public_sys-resources/icon-note.gif) **Note:** 
>Under uboot, only pure storage class devices are supported, such as USB flash drives and hard drives. Devices with CD-ROM partitions are not supported. To check on a PC, look at the device drive letter; if there is a CD-ROM drive letter, it has a CD-ROM partition.

Compile USB-related drivers under uboot.

1.  Enter the following path in menuconfig and confirm that all the following driver configurations are selected. The default configuration selects all.

    ```
    Command line interface  --->
             Device access commands  --->
                  [*] usb
    Device Drivers  --->
             [*] vendor usb phy driver
             [*] USB support  --->
                  [*]   xHCI HCD (USB 3.0) support
                  [*]   USB Mass Storage support
    ```

2.  Compilation commands:

    ```
    make ARCH=arm CROSS_COMPILE=aarch64-mix210-linux- menuconfig
    make ARCH=arm CROSS_COMPILE=aarch64-mix210-linux- -j 20
    cp ../../../osdrv/tools/pc/uboot_tools/reg_info.bin .reg
    make ARCH=arm CROSS_COMPILE=aarch64-mix210-linux- u-boot-z.bin
    ```

    The compiled u-boot-ss928v100.bin is the usable u-boot image.

#### USB Host Operation Process under Kernel<a name="ZH-CN_TOPIC_0000002512103591"></a>

1.  Start the board and load a jffs2, ext4, or cramfs file system, or use NFS.
2.  By default, all USB Host-related modules are compiled into the kernel. No additional loading command is required; you can directly perform operations on a USB flash drive, mouse, or keyboard. For specific operations, please refer to "2.3 Operation Examples". The following lists all USB Host-related drivers:
    -   File system and storage device related modules
        -   vfat
        -   ext4
        -   scsi\_mod
        -   sd\_mod
        -   nls\_ascii
        -   nls\_iso8859-1

    -   Keyboard related modules
        -   evdev
        -   usbhid

    -   Mouse related modules
        -   mousedev
        -   usbhid
        -   evdev

    -   USB Host modules
        -   xhci-hcd
        -   xhci-plat-hcd
        -   usb-storage
        -   phy-vendor-usb3

#### USB Device Operation Process under Kernel<a name="ZH-CN_TOPIC_0000002480063612"></a>

1.  Compile USB Device-related kernel driver modules.

    -   Enter the following path in menuconfig. The configuration for USB device as a virtual USB drive, virtual network interface, virtual serial port, and webcam is as follows.

        ```
        Device Drivers  --->
                 <*> Multimedia support  --->
                          [*]   Cameras/video grabbers support 
                          [*]   Media USB Adapters  --->
                                   <*>   USB Video Class (UVC)
                                   [*]     UVC input events device support
                          [*]   V4L platform devices  ---> 
                 <*> Sound card support  --->
                          <*>   Advanced Linux Sound Architecture  --->
                                   [*]   USB sound devices  --->  
                 [*] USB support  --->
                          <*>  DesignWare USB3 DRD Core Support
                                   DWC3 Mode Selection (Gadget only mode)  --->
                          <*>  USB Gadget Support  --->
                                   <*>   USB Gadget functions configurable through configfs
                                             [*]   Abstract Control Model (CDC ACM)
                                             [*]   RNDIS
                                             [*]   Mass storage
                                             [*]   Audio Class 1.0
                                             [*]   USB Webcam function
                 PHY Subsystem  --->
                          <*>  VENDOR USB support  --->
                                   [*]    Vendor USB PHY driver
                                   [*]    Vendor USB related configuration  --->
                                             [ ] USB DRD0 Mode Select HOST
                                             [*] USB DRD0 Mode Select DEVICE
        ```

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >DRD0 can only select host/device, not both simultaneously. That is, USB DRD0 Mode Select HOST and USB DRD0 Mode Select DEVICE in the configuration above cannot be selected at the same time.
    >Not all chips have device mode. For specific chip specifications, please refer to the chip manual or contact technical support.

    -   Compile kernel modules to generate .ko files.

        ```
        make ARCH=arm64 CROSS_COMPILE=aarch64-mix210-linux- modules -j 32
        ```

        Note: When compiling modules, the kernel must be compiled first. The kernel compilation command is:

        ```
        make ARCH=arm64 CROSS_COMPILE=aarch64-mix210-linux- uImage -j 32
        ```

2.  Start the board and load a jffs2, ext4, or cramfs file system, or use NFS.
3.  When the board acts as a Device, you need to load relevant environment variables and configure related scripts. For specific operations, please refer to "[Operation Examples](#ZH-CN_TOPIC_0000002512103593)".

### Operation Examples<a name="ZH-CN_TOPIC_0000002480063640"></a>

#### USB Flash Drive Operation Example under Uboot<a name="ZH-CN_TOPIC_0000002512103597"></a>

##### Insert the Device Before Powering On<a name="ZH-CN_TOPIC_0000002512063501"></a>

>![](public_sys-resources/icon-note.gif) **Note:** 
>Hot-plugging is not supported under Uboot. The device must be inserted into the USB port before the system is powered on.

Power on the board, enter the uboot command line, and enter the command: usb start. Observe whether the device is recognized successfully.

-   When a high-speed/super-speed USB flash drive is inserted into the USB port, the normal serial output is:

    ```
    # usb start
    USB0:   Register 1000140 NbrPorts 1
    Starting the controller
    USB XHCI 1.10
    scanning bus 0 for devices... 2 USB Device(s) found
    scanning usb for storage devices... 1 Storage Device(s) found
    ```

>![](public_sys-resources/icon-note.gif) **Note:** 
>If enumeration errors occur after usb start, such as "Device not responding to set address", or if the device is not detected at all after usb start, execute the following in the uboot command line: setenv usb_pgood_delay XXX. This setting is for devices that require a longer warm-up time. It increases the timeout to wait for the device to stabilize after power-on. XXX should be set to a reasonable value based on the device's warm-up speed, with a recommended range of 1000-3000.

After recognition is complete, enter the command: usb tree, to view the recognition speed.

-   When a high-speed/super-speed USB flash drive is inserted into the USB port, the normal serial output is:

    ```
    # usb tree
    USB device tree:
    1  Hub (5 Gb/s, 0mA)
    |  U-Boot XHCI Host Controller
    |
    +-2  Mass Storage (480 Mb/s, 250mA)
    Generic Mass Storage Device 121220130416
    ```

##### Initialization and Application<a name="ZH-CN_TOPIC_0000002512103561"></a>

After recognition is complete, perform the following operations.

1.  View device information.

    Execute the Uboot command: usb info [dev], to view information about all devices connected to the current controller. You can add a parameter after the command to view information about a specific device, e.g., usb info 2. Example of a normal view:

    ```
     # usb info 2
    config for device 2
    2: Mass Storage,  USB Revision 2.0
      - Generic Mass Storage B92AAF26
      - Class: (from Interface) Mass Storage
      - PacketSize: 64  Configurations: 1
      - Vendor: 0x058f  Product 0x6387 Version 1.0
        Configuration: 1
        - Interfaces: 1 Bus Powered 200mA
          Interface: 0
          - Alternate Setting 0, Endpoints: 2
          - Class Mass Storage, Transp. SCSI, Bulk only
          - Endpoint 1 Out Bulk MaxPacket 512
          - Endpoint 2 In Bulk MaxPacket 512
    ```

2.  Perform a read operation on the USB flash drive.

    Execute the Uboot command: usb read addr blk# cnt, to read data with a starting address of blk and size of cnt to the DDR address addr. Example of a successful read operation:

    ```
     # usb read 0x82000000 0 2000
    USB read: device 0 block # 0, count 8192 ... 8192 blocks read: OK
    ```

3.  Perform a write operation on the USB flash drive.

    Execute the Uboot command: usb write addr blk# cnt, to write data of size cnt from DDR address addr to the blk position on the USB flash drive. Example of a successful write operation:

    ```
     # usb write 0x82000000 2000 2000
    ```

    ```
    USB write: device 0 block # 8192, count 8192 ... 8192 blocks write: OK
    ```

#### USB Flash Drive Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002512103535"></a>

##### Hot-plug Detection<a name="ZH-CN_TOPIC_0000002480063692"></a>

Directly insert the USB flash drive and observe whether enumeration is successful.

-   Normal serial output when a high-speed USB flash drive is inserted into the USB port:

    ```
    ~ # usb 1-1: new high-speed USB device number 2 using xhci-hcd
    scsi2 : usb-storage 1-1:1.0
    scsi 2:0:0:0: Direct-Access           1.00 PQ: 0 ANSI: 4
    sd 2:0:0:0: [sda] 15131636 512-byte logical blocks: (7.74 GB/7.21 GiB)
    sd 2:0:0:0: [sda] Write Protect is off
    sd 2:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
    sda: sda1
    sd 2:0:0:0: [sda] Attached SCSI removable disk
    ```

-   Normal serial output when a super-speed USB flash drive is inserted into the USB port:

    ```
    ~ # usb 2-1: new SuperSpeed USB device number 3 using xhci-hcd
    scsi2 : usb-storage 2-1:1.0
    scsi 2:0:0:0: Direct-Access           1.00 PQ: 0 ANSI: 4
    sd 2:0:0:0: [sda] 15131636 512-byte logical blocks: (7.74 GB/7.21 GiB)
    sd 2:0:0:0: [sda] Write Protect is off
    sd 2:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
    sda: sda1
    sd 2:0:0:0: [sda] Attached SCSI removable disk
    ```

Where: sda1 represents the first partition on the USB flash drive or external hard drive. When multiple partitions exist, sda1, sda2, sda3, etc., will appear.

##### Initialization and Application<a name="ZH-CN_TOPIC_0000002480063658"></a>

After the module is inserted, perform the following operations:

>![](public_sys-resources/icon-note.gif) **Note:** 
>In sdXY, X represents the disk number and Y represents the partition number. Modify according to the specific system environment.

-   The specific device node for partition command operations is sdX. Example: $ fdisk /dev/sda
-   The specific partition formatted with the mkdosfs tool is sdXY: ~ $ mkdosfs -F 32 /dev/sda1
-   The specific partition to mount is sdXY: ~ $ mount -t vfat /dev/sda1 /mnt

1.  View partition information.
    -   Run the command "ls /dev" to view system device files. If there is no partition information sdXY, the device has not been partitioned yet. Please refer to "[Partitioning with fdisk tool](#ZH-CN_TOPIC_0000002479903638)" to partition, then proceed to step 2.
    -   If partition information sdXY exists, the disk has been detected and partitioned. Proceed to step 2.

2.  View formatting information.
    -   If not formatted, please refer to "[Formatting with mkdosfs tool](#ZH-CN_TOPIC_0000002512103571)" to format, then proceed to step 3.
    -   If already formatted, proceed to step 3.

3.  Mount the directory. Please refer to "[Mounting Directory](#ZH-CN_TOPIC_0000002512103519)".
4.  Read and write to the hard drive. Please refer to "[Reading and Writing Files](#ZH-CN_TOPIC_0000002512103577)".

#### Keyboard Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002512103585"></a>

The keyboard operation process is as follows:

1.  Insert modules.

    After inserting keyboard-related modules, the keyboard will generate an event0 node in the /dev/input directory.

2.  Receive keyboard input.

    Execute the command: cat /dev/input/event0

    Then press keys on the USB keyboard, and you can see output on the screen.

#### Mouse Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002479903684"></a>

The mouse operation process is as follows:

1.  Insert modules.

    After inserting mouse-related modules, the mouse will generate a mouse0 node in the /dev/input directory.

2.  Receive mouse input.

    Execute the command: cat /dev/input/mouse0

3.  Perform mouse operations (click, scroll, etc.). You can see the corresponding code values printed on the serial console.

#### Virtual USB Drive Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002512103525"></a>

When the board acts as a virtual USB drive, using Flash and SD card as storage media as an example, the operation process is as follows:

1.  Configure environment variables and scripts.
    -   Using Flash as the storage medium for the virtual USB drive:

        ```
        export VID="0x1D6B"
        export PID="0x0001"
        export MANUFACTURER="Vendor"
        export PRODUCT="MassStorage"
        export SERIALNUMBER="123456789012"
        export MEMORY=/dev/mtdblockX
        ./Config_Storage.sh
        ```

        Where, mtdblockX is the Xth partition of Flash. Users should select according to their specific situation.

    -   Using SD card as the storage medium for the virtual USB drive:

        ```
        export VID="0x1D6B"
        export PID="0x0001"
        export MANUFACTURER=" Vendor"
        export PRODUCT="MassStorage"
        export SERIALNUMBER="123456789012"
        export MEMORY=/dev/mmcblk0pX
        ./Config_Storage.sh
        ```

        Where, mmcblk0pX is the Xth partition of the SD card. Users should select according to their specific situation.

        >![](public_sys-resources/icon-note.gif) **Note:** 
        >1.  The variables modified by the above export commands can be adapted by the user. The meanings of the variables are as follows:
        >    -   VID: Vendor ID, must be modified when used.
        >    -   PID: Product ID, must be modified when used.
        >    -   MANUFACTURER: Manufacturer name, the default release is Vendor, must be modified when used.
        >    -   PRODUCT: Product name, modify as needed.
        >    -   SERIALNUMBER: Product serial number, modify as needed.
        >2.  Config\_Storage.sh contains the necessary operations to start mass storage. Users do not need to modify it.
        >    Config\_Storage.sh is in the appendix: [Virtual USB Drive](#ZH-CN_TOPIC_0000002512063553).
        >3.  To unload the storage function module, execute Disable\_Storage.sh. Users do not need to modify the script content.
        >    Disable\_Storage.sh is in the appendix: [Virtual USB Drive](#ZH-CN_TOPIC_0000002512063553).

2.  Connect the board to a PC via USB. The PC should then recognize a drive letter. At this point, the board can be used as a real USB drive.

#### Virtual Network Interface Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002480063670"></a>

When the board acts as a virtual network interface device, the operation process is as follows:

1.  Configure environment variables and scripts.

    ```
    export VID="0x1D6B"
    export PID="0x0002"
    export MANUFACTURER="Vendor"
    export PRODUCT="Ethernet"
    export SERIALNUMBER="123456789012"
    ./Config_Ether.sh
    ```

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >1.  The variables modified by the above export commands can be adapted by the user. Their meanings are:
    >    -   VID: Vendor ID, must be modified when used.
    >    -   PID: Product ID, must be modified when used.
    >    -   MANUFACTURER: Manufacturer name, the default is Vendor, must be modified when used.
    >    -   PRODUCT: Product name, must be modified when used.
    >    -   SERIALNUMBER: Product serial number, modify as needed.
    >2.  Config\_Ether.sh contains the necessary operations to start the virtual network interface. Users do not need to modify it.
    >    Config\_Ether.sh is in the appendix: [Virtual Network Interface](#ZH-CN_TOPIC_0000002480063664).
    >3.  To unload the network interface function module, execute Disable\_Ether.sh. Users do not need to modify the script content.
    >    Disable\_Ether.sh is in the appendix: [Virtual Network Interface](#ZH-CN_TOPIC_0000002480063664).

2.  Connect the board to a Host PC via a USB data cable. If the PC system is Win10, the PC will automatically load the driver. You can see a Remote NDIS Compatible Device #x device in the Network Adapters section of Device Manager. However, some PCs may recognize it as a serial device. For the solution, see the note after step 4. If the PC system is Win7, the first attempt may fail and the driver needs to be installed manually. The method is:
    -   Right-click Computer and enter the Management interface.
    -   Open Device Manager.
    -   Click on Other devices and you will see Ethernet. Double-click it.
    -   Open the Driver interface, click Update driver, then select "Browse my computer for driver software".
    -   Point the path to the directory containing linux.inf. Download the following file to a local directory, click Next, and the computer will automatically install the driver. After successful installation, you will see Ethernet Linux USB Ethernet /RNDIS Gadget #x under Network adapters.

        The linux.inf file is located in the release package at: \{SDK\_PATH\}/open\_source/linux/linux-4.19.y/Documentation/usb/

3.  Configure the IP address on the board side with the command: ifconfig usb0 xx.xx.xx.xx netmask 255.255.xxx.0; route add default gw xx.xx.xx.xx.
4.  When the board and PC are connected via a USB data cable, a USB network node will be generated on the PC side. The specific location is: Open Network and Sharing Center -> Change adapter settings -> Linux USB Ethernet /RNDIS Gadget #x. Set the network IP for this node, and the board and PC can ping each other and communicate.

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >The Config\_Ether.sh script has been adapted for Win10 systems. However, it has been found that some Win10 PCs may recognize the network interface device as a serial device. The solution is to place the RNDIS.cat and RNDIS.inf driver files in a local directory and update the driver for the newly added serial device in Device Manager, using the same method as the Win7 PC driver update in the steps. After the update, the network interface device can be used normally.
    >Digital signature verification must be disabled on Win10 PCs before updating the driver. The method to disable it can be found through an online search and is not described here.
    >RNDIS.cat and RNDIS.inf files can be obtained through an online search.

#### Virtual Serial Port Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002512103569"></a>

When the board acts as a virtual serial port device, the operation process is as follows:

1.  Configure environment variables and scripts.

    ```
    export VID="0x1D6B"
    export PID="0x0003"
    export MANUFACTURER="Vendor"
    export PRODUCT="SerialGadget"
    export SERIALNUMBER="123456789012"
    ./Config_Serial.sh
    ```

    >![](public_sys-resources/icon-note.gif) **Note:** 
    >1.  The variables modified by the above export commands can be adapted by the user. Their meanings are:
    >    -   VID: Vendor ID, must be modified when used.
    >    -   PID: Product ID, must be modified when used.
    >    -   MANUFACTURER: Manufacturer name, the default is Vendor, must be modified when used.
    >    -   PRODUCT: Product name, must be modified when used.
    >    -   SERIALNUMBER: Product serial number, modify as needed.
    >2.  Config\_Serial.sh contains the necessary operations to start the virtual serial port. Users do not need to modify it.
    >    Config\_Serial.sh is in the appendix: [Virtual Serial Port](#ZH-CN_TOPIC_0000002479903674).
    >3.  To unload the serial port function module, execute Disable\_Serial.sh. Users do not need to modify the script content.
    >    Disable\_Serial.sh is in the appendix: [Virtual Serial Port](#ZH-CN_TOPIC_0000002479903674).

2.  On the board side, perform the following operations:

    ```
    vi /etc/inittab
    #::respawn:/sbin/getty -L ttyS000 115200 vt100 -n root -I "Auto login as root ..."
    ::respawn:/sbin/getty -L ttyGS0 115200 vt100 -n root -I "Auto login as root ..."
    ```

    Then restart the board.

3.  Connect the board to a Host PC via a USB data cable.

    If the PC system is Win10, the PC will automatically load the driver.

    If the PC system is Win7, the first attempt may fail and the driver needs to be installed manually. The method is:

    -   Right-click Computer and enter the Management interface.
    -   Open Device Manager.
    -   Click on Other devices and you will see a device named the PRODUCT variable (e.g., SerialGadget). Double-click it.
    -   Open the Driver interface, click Update driver, then select "Browse my computer for driver software".
    -   Point the path to the directory containing linux-cdc-acm.inf. Download the following file to a local directory, click Next, and the computer will automatically install the driver. After successful installation, you will see a Gadget Serial (COMx) device under Ports (COM & LPT). If the PC system is Win10, no manual driver installation is required, and you will see a USB Serial Device (COMx) under Ports (COM & LPT).

        The linux-cdc-acm.inf file is located in the release package at: \{SDK\_PATH\}/open\_source/linux/linux-4.19.y/Documentation/usb/

#### Webcam Operation Example under Kernel<a name="ZH-CN_TOPIC_0000002512103551"></a>

**Table 1** UVC Solution Feature Table

<a name="table6465725141113"></a>
<table><thead align="left"><tr id="row124654254114"><th class="cellrowborder" valign="top" width="5.129487051294871%" id="mcps1.2.5.1.1"><p id="p291729201211"><a name="p291729201211"></a><a name="p291729201211"></a>No.</p>
</th>
<th class="cellrowborder" valign="top" width="18.51814818518148%" id="mcps1.2.5.1.2"><p id="p1846572571112"><a name="p1846572571112"></a><a name="p1846572571112"></a>Feature</p>
</th>
<th class="cellrowborder" valign="top" width="33.826617338266175%" id="mcps1.2.5.1.3"><p id="p446516257119"><a name="p446516257119"></a><a name="p446516257119"></a>Usage Instructions</p>
</th>
<th class="cellrowborder" valign="top" width="42.52574742525748%" id="mcps1.2.5.1.4"><p id="p174659259115"><a name="p174659259115"></a><a name="p174659259115"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row123811666122"><td class="cellrowborder" valign="top" width="5.129487051294871%" headers="mcps1.2.5.1.1 "><p id="p2912293126"><a name="p2912293126"></a><a name="p2912293126"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="18.51814818518148%" headers="mcps1.2.5.1.2 "><p id="p11381166111214"><a name="p11381166111214"></a><a name="p11381166111214"></a>Supported Protocol Version (UVC 1.1/1.5)</p>
</td>
<td class="cellrowborder" valign="top" width="33.826617338266175%" headers="mcps1.2.5.1.3 "><p id="p238116141215"><a name="p238116141215"></a><a name="p238116141215"></a>Supports UVC 1.1 and UVC 1.5 protocols, switchable via configuration script parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="42.52574742525748%" headers="mcps1.2.5.1.4 "><p id="p1138444211218"><a name="p1138444211218"></a><a name="p1138444211218"></a>Default uses UVC 1.1 protocol.</p>
</td>
</tr>
<tr id="row19661644141213"><td class="cellrowborder" valign="top" width="5.129487051294871%" headers="mcps1.2.5.1.1 "><p id="p2953612111"><a name="p2953612111"></a><a name="p2953612111"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="18.51814818518148%" headers="mcps1.2.5.1.2 "><p id="p1395315151219"><a name="p1395315151219"></a><a name="p1395315151219"></a>Supported Image Formats</p>
</td>
<td class="cellrowborder" valign="top" width="33.826617338266175%" headers="mcps1.2.5.1.3 "><p id="p1795312151213"><a name="p1795312151213"></a><a name="p1795312151213"></a>Supports input formats: YUYV, MJPEG, H.264. Each format can reach up to 1920x1080 resolution.</p>
</td>
<td class="cellrowborder" valign="top" width="42.52574742525748%" headers="mcps1.2.5.1.4 "><p id="p10953315151215"><a name="p10953315151215"></a><a name="p10953315151215"></a>Configuration script parameters can be adjusted to output different formats and resolutions.</p>
</td>
</tr>
<tr id="row17405203112416"><td class="cellrowborder" valign="top" width="5.129487051294871%" headers="mcps1.2.5.1.1 "><p id="p17405163102411"><a name="p17405163102411"></a><a name="p17405163102411"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="18.51814818518148%" headers="mcps1.2.5.1.2 "><p id="p164055311241"><a name="p164055311241"></a><a name="p164055311241"></a>Frame Rate Configuration</p>
</td>
<td class="cellrowborder" valign="top" width="33.826617338266175%" headers="mcps1.2.5.1.3 "><p id="p54051831112414"><a name="p54051831112414"></a><a name="p54051831112414"></a>Frame rate is configurable.</p>
</td>
<td class="cellrowborder" valign="top" width="42.52574742525748%" headers="mcps1.2.5.1.4 "><p id="p2405631152413"><a name="p2405631152413"></a><a name="p2405631152413"></a>Set according to actual product requirements.</p>
</td>
</tr>
</tbody>
</table>
