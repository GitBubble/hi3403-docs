---
title: "iTOP-Hi3403 — peripheral test guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/vendor/topeet/docs/iTOP-Hi3403 开发板外设测试步骤.md
--- # Chapter 1 · Flashing firmware via Tool Platform This document walks through flashing an image to the Topeet
i TOP-Hi3403 board. ## 1.1 Steps Before you flash, you need an image. Two ways to get one: **(1)** While building the Linux source, each component image is copied
into the source-tree's `output/` directory — pick yours up from there. **(2)** Topeet provide pre-built images on
[their pan.baidu.com share](https:/pan.baidu.com/s/1vvG St YG5wx Cj7UA Gza7UsQ?pwd=rgci),
split into three folders for Buildroot, Ubuntu lite (headless), and
Ubuntu XFCE (desktop). ![image-20260327105156899](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271051933.png) ![image-20260327105220806](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271052841.png) You also need the **Tool Platform** flashing tool. Download
[ToolPlatform-1.0.11-win32-x86_64.zip](https:/pan.baidu.com/s/1zh2z6p Rpk MhabB1JYHY-jg?pwd=t9wm),
unzip it anywhere on Windows. ![image-20260327105257769](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271052788.png) Copy the image folder into the unzipped Tool Platform directory: ![image-20260327105313363](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271053399.png) Run `Tool Platform.exe`: ![image-20260327105327160](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271053191.png) The chip selector lists only **Hi3403V100** — confirm: ![image-20260327110244623](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271102651.png) On the welcome screen, click **Burn Tool** in the menu bar: ![image-20260327110259857](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271102892.png) You're now in the Burn Tool window: ![image-20260327110315635](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271103689.png) Subsequent flashing uses both the serial line and the network — make
sure you have an Ethernet cable connected (it must be **eth0**) and
the serial cable connected: ![img](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271041327.png) Configure the local-PC side: pick the COM port your USB-serial cable
shows up as (make sure no other app is holding it — for example, a
serial terminal would block it), and set the server IP to a NIC that
can ping the board: ![image-20260327110352707](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271103762.png) Since we're flashing to e MMC, click **Burn e MMC**: ![image-20260327110655315](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271106367.png) Click *Browse*, pick `parttable.xml` from your image folder: ![image-20260327110714598](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271107649.png) The partitions are pre-populated. Verify the per-partition address is
right; fix any path that's off, then click **Burn**. If the serial
port is good and not in use, you'll see "Serial port connected,
please power-cycle the board": ![image-20260327110939615](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271109672.png) Hold the **BOOT** button on the board and apply power. The `#####`
progress means flashing is underway: ![image-20260327110954200](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271109259.png) Buildroot images take ~3 minutes; Ubuntu images take ~10. When done
you'll see a "burn successful" pop-up: ![image-20260327111205738](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112760.png) That covers the Hi3403 image flashing. > Note: serial-only flashing is supported but **much** slower — not recommended. ## 1.2 Common flashing problems ### 1.2.1 Serial port is in use Tool Platform needs the serial port for itself. Since the same UART is
also the debug console, it's easy to leave a debug terminal holding it. Symptom: clicking *Burn* yields **"Open serial port failed."** plus
a "download failed" dialog: ![image-20260327111225033](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112086.png) Fix: close any other software holding the port, then retry. ### 1.2.2 Network plugged into eth1 instead of eth0 After the U-Boot stage, Tool Platform pushes the larger kernel + rootfs
images over Ethernet. Only **eth0** can run the TFTP transfer; if you
plug into eth1, the TFTP download times out: ![](https:/chai-1301855619.cos.ap-beijing.myqcloud.com/202603271112977.png) Fix: move the cable to eth0 and retry.
