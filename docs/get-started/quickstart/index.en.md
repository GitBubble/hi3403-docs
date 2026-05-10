---
description: Record of steps from getting the board to logging into Linux
title: Quick start
---

# Quick start

Complete the following 5 steps in order to start Hi3403V100. Links at the end of each step lead to more detailed documentation.

## Preparation

- Hi3403V100 (SS928V100) development board
- Linux / macOS host (WSL2 for Windows)
- USB-TTL serial port cable (3.3V)
- SD card or USB data cable (depending on the burning method)
- 5V/3A power supply

## 1. Select boards and systems

|  | Options | Details |
|---|---|---|
| Board | Xunwei/Wildfire/Ibaina/Run Kaihong | [Board comparison](../board-picker.md) |
| OS | Ubuntu 22.04 / OpenHarmony / OpenEuler / Buildroot | [OS comparison](../os-picker.md) |

It is recommended to use Ubuntu 22.04 + the manufacturer's pre-compiled image for the first time, and then consider self-compiling after the hardware verification is passed.

## 2. Wiring

```text
USB-TTL  ──  UART0 (TX/RX/GND)     # 115200 8N1
DC IN    ──  5V/3A
HDMI ── Monitor # XFCE Desktop Variant
ETH ── Router # Optional
```

Host-side serial port tools: `minicom`, `picocom`, `screen /dev/ttyUSB0 115200`, PuTTY.

## 3. Burn the image

### Vendor-provided images

| Manufacturer | Tools | medium |
|---|---|---|
| Topeet | HiTool / BurnTool | eMMC over USB |
| Wildfire (LubanCat) | balenaEtcher / dd | SD card |
| Ebaina | HiBurn | eMMC |

For download links, see each manufacturer’s [Boards](../../boards/index.md) page.

### Build it yourself

```bash
git clone --recurse-submodules https://github.com/GitBubble/hi3403-build.git
cd hi3403-build
./build.sh ubuntu_xfce_all
```

Product `output/hi3403-ubuntu-xfce-ss928v100.img`, `dd` to eMMC or SD card.

See [Ubuntu build guide](../../os/ubuntu/porting.md) for details.

## 4. Power on and log in

After powering on, the serial port prints U-Boot → kernel → systemd logs in sequence, and finally a login prompt appears:

```text
hi3403 login: hi
Password: hi
```

After connecting the network cable, `ip a` checks the IP, and the host `ssh hi@<IP>`.

??? failure "No output from serial port"
    - TX/RX connection reversed (USB-TTL’s TX is connected to the board’s RX)
    - The baud rate is not 115200
    - Wrong device node selection (macOS is `/dev/tty.usbserial-*`)
    - The board is not actually powered

??? failure "Kernel panic after U-Boot starts"
    - DTB does not match the board (eMMC and SPI flash use different DTB)
    - The image writing is incomplete or the media is damaged.

## 5. Host development environment

Only required when compiling by yourself.

```bash
# Linux
sudo apt install -y build-essential gcc-aarch64-linux-gnu git make python3 docker.io

# macOS
brew install --cask docker
```

See [Development environment](../environment/index.md) · [SDK installation](../sdk-install/index.md) · [Driver installation](../driver-install/index.md) for details.

## Next

| Target | document |
|---|---|
| NPU inference (YOLO) | [SVP first inference](../../tutorials/svp-first-inference.md) |
| Camera capture + H.264 encoding | [Collection code](../../tutorials/capture-encode-stream.md) |
| ISP / white balance | [ISP color correction](../../tutorials/isp-color-tuning.md) |
| Full SDK workflow | [Upstream SDK quick start](../upstream-quickstart/index.md) |
| Build script parameters | [hi3403-build](https://github.com/GitBubble/hi3403-build) |