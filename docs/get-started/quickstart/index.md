---
title: 30 分钟启动 Hi3403
description: 最短路径 —— 从拿到开发板到看到 Linux 登录提示符
---

# 30 分钟启动 Hi3403

这是“**最短可行路径**”：跳过原理，按步骤走完，半小时内你就能看到 `hi@hi3403:~$` 登录提示符。

如果某一步想深入，每一步末尾都有跳转链接到详细页面。

!!! tip "你需要先准备"
    - 一块 Hi3403V100 (SS928V100) 开发板（任意厂家）
    - 一台 Linux 或 macOS 主机（Windows 用 WSL2）
    - USB-TTL 串口线（板子大多用 3.3V）
    - SD 卡或 USB 线（用于烧录）
    - 5V/3A 以上电源

---

## 第 0 步 · 决策（5 分钟）

| 问题 | 推荐 | 详细 |
|---|---|---|
| 我有哪块板子？ | 找出厂商：迅为 / 野火 / 易百纳 / 润开鸿 | [选择开发板](../board-picker.md) |
| 跑什么系统？ | 第一次 → **Ubuntu 22.04 (XFCE)** | [选择操作系统](../os-picker.md) |
| 用预编译镜像还是自己编？ | 第一次 → **预编译** | 见下方第 2 步 |

> :material-lightbulb-on: 第一次摸板子，**别**先编译 SDK。先用厂商或社区提供的镜像点亮，确认硬件没问题，再回头研究构建。

---

## 第 1 步 · 硬件接线（5 分钟）

```text
        ┌─────────────────────────────┐
        │   Hi3403V100 开发板          │
        │                              │
[USB-TTL]──── UART0 (TX/RX/GND) ──→ 串口调试
        │                              │
[5V 电源]──── DC IN                    │
        │                              │
[HDMI]──── HDMI OUT (XFCE 桌面)        │
        │                              │
[网线/USB]── ETH / OTG (可选)         │
        └─────────────────────────────┘
```

- 串口波特率：**115200 8N1**
- 主机端可用 `minicom`、`picocom`、`screen /dev/ttyUSB0 115200`、PuTTY

---

## 第 2 步 · 烧录镜像（10 分钟）

### 路径 A：用厂商现成镜像（推荐第一次）

每家板子的烧录工具不同：

| 厂商 | 工具 | 媒介 |
|---|---|---|
| 迅为 (Topeet) | HiTool / BurnTool | eMMC（USB） |
| 野火 (LubanCat) | balenaEtcher / dd | SD 卡 |
| 易百纳 (Ebaina) | HiBurn | eMMC |

镜像下载链接见各厂商 [开发板](../../boards/index.md) 页面。

### 路径 B：自己构建 Ubuntu 镜像

```bash
git clone --recurse-submodules https://github.com/GitBubble/hi3403-build.git
cd hi3403-build
./build.sh ubuntu_xfce_all     # 一键构建（约 30-60 分钟，取决于网速）
```

产物：`output/hi3403-ubuntu-xfce-ss928v100.img` —— 直接 `dd` 到 eMMC/SD 即可。

[:octicons-arrow-right-24: Ubuntu 构建详解](../../os/ubuntu/porting.md)

---

## 第 3 步 · 上电 + 登录（5 分钟）

1. 接好串口、电源
2. 上电后串口应输出 U-Boot → kernel → systemd 启动日志
3. 看到登录提示符后输入：

   ```text
   login: hi
   password: hi
   ```

4. 联网（如果接了网线）：`ip a` 确认拿到 IP
5. SSH 登录：`ssh hi@<板子IP>`

??? failure "看不到任何串口输出？"
    - TX/RX 接反（USB-TTL 的 TX 接板子的 RX）
    - 波特率不对（必须 115200）
    - 选错串口设备（macOS 是 `/dev/tty.usbserial-*`）
    - 板子没真正上电（看电源 LED）

??? failure "U-Boot 启动但内核挂掉？"
    - 烧录的镜像和你的板子型号不匹配（eMMC vs SPI flash 的 DTB 不同）
    - 镜像没烧完整（`dd` 时被中断 / SD 卡损坏）

---

## 第 4 步 · 装开发环境（PC 侧，5 分钟）

只在你想自己编译代码时才需要。

```bash
# Ubuntu/Debian 主机
sudo apt install -y build-essential gcc-aarch64-linux-gnu \
                    git make python3 docker.io

# macOS 主机（用 Docker 跑交叉编译）
brew install --cask docker
```

[:octicons-arrow-right-24: 安装开发环境（详细）](../environment/index.md) ·
[:octicons-arrow-right-24: 安装 SDK](../sdk-install/index.md) ·
[:octicons-arrow-right-24: 驱动安装](../driver-install/index.md)

---

## 接下来读什么？

| 你想做什么 | 跳转 |
|---|---|
| 用 NPU 跑 YOLO | [SVP 首次推理](../../tutorials/svp-first-inference.md) |
| 摄像头 → H.264 推流 | [采集编码教程](../../tutorials/capture-encode-stream.md) |
| 调 ISP / 白平衡 | [ISP 调色教程](../../tutorials/isp-color-tuning.md) |
| 看完整 SDK 文档 | [上游 SDK 快速开始](../upstream-quickstart/index.md) |
| 一键构建脚本细节 | [hi3403-build](https://github.com/GitBubble/hi3403-build) |

---

??? note "为什么这页这么短？"
    早期版本塞了 1000+ 行 SVP 模型转换内容，对刚拿到板子的人没用。
    Quickstart 的目标就是 **让人最短时间看到 shell**，所有细节都拆到子页面里。
    如果你在某一步卡住，请打开右边那一栏的 “详细” 链接。
