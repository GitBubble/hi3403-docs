---
title: 快速启动
description: 从拿到板子到登录 Linux 的步骤记录
---

# 快速启动

按顺序做完下面 5 步即可启动 Hi3403V100。每步末尾的链接指向更详细的文档。

## 准备

- Hi3403V100 (SS928V100) 开发板
- Linux / macOS 主机（Windows 用 WSL2）
- USB-TTL 串口线（3.3V）
- SD 卡或 USB 数据线（视烧录方式）
- 5V/3A 电源

## 1. 选板子和系统

| | 选项 | 详细 |
|---|---|---|
| 板子 | 迅为 / 野火 / 易百纳 / 润开鸿 | [板子对比](../board-picker.md) |
| 系统 | Ubuntu 22.04 / OpenHarmony / OpenEuler / Buildroot | [系统对比](../os-picker.md) |

第一次上手建议 Ubuntu 22.04 + 厂商预编译镜像，硬件验证通过后再考虑自编译。

## 2. 接线

```text
USB-TTL  ──  UART0 (TX/RX/GND)     # 115200 8N1
DC IN    ──  5V/3A
HDMI     ──  显示器                # XFCE 桌面变体
ETH      ──  路由器                # 可选
```

主机端串口工具：`minicom`、`picocom`、`screen /dev/ttyUSB0 115200`、PuTTY。

## 3. 烧录镜像

### 厂商镜像

| 厂商 | 工具 | 介质 |
|---|---|---|
| 迅为 (Topeet) | HiTool / BurnTool | eMMC over USB |
| 野火 (LubanCat) | balenaEtcher / dd | SD 卡 |
| 易百纳 (Ebaina) | HiBurn | eMMC |

下载链接见各厂商 [开发板](../../boards/index.md) 页面。

### 自己构建

```bash
git clone --recurse-submodules https://github.com/GitBubble/hi3403-build.git
cd hi3403-build
./build.sh ubuntu_xfce_all
```

产物 `output/hi3403-ubuntu-xfce-ss928v100.img`，`dd` 到 eMMC 或 SD 卡。

详见 [Ubuntu 构建指南](../../os/ubuntu/porting.md)。

## 4. 上电登录

上电后串口依次打印 U-Boot → kernel → systemd 日志，最后出现登录提示：

```text
hi3403 login: hi
Password: hi
```

接网线后 `ip a` 查 IP，主机 `ssh hi@<IP>`。

??? failure "串口无输出"
    - TX/RX 接反（USB-TTL 的 TX 接板子的 RX）
    - 波特率不是 115200
    - 设备节点选错（macOS 是 `/dev/tty.usbserial-*`）
    - 板子未实际供电

??? failure "U-Boot 启动后内核 panic"
    - DTB 与板子不匹配（eMMC 与 SPI flash 用不同 DTB）
    - 镜像写入不完整或介质损坏

## 5. 主机开发环境

仅在自行编译时需要。

```bash
# Linux
sudo apt install -y build-essential gcc-aarch64-linux-gnu git make python3 docker.io

# macOS
brew install --cask docker
```

详见 [开发环境](../environment/index.md) · [SDK 安装](../sdk-install/index.md) · [驱动安装](../driver-install/index.md)。

## 接下来

| 目标 | 文档 |
|---|---|
| NPU 推理 (YOLO) | [SVP 首次推理](../../tutorials/svp-first-inference.md) |
| 摄像头采集 + H.264 编码 | [采集编码](../../tutorials/capture-encode-stream.md) |
| ISP / 白平衡 | [ISP 调色](../../tutorials/isp-color-tuning.md) |
| 完整 SDK 流程 | [上游 SDK 快速开始](../upstream-quickstart/index.md) |
| 构建脚本参数 | [hi3403-build](https://github.com/GitBubble/hi3403-build) |
