---
title: 在 30 分钟内启动 Hi3403
description: 从空板子到登录界面 —— 最短路径的入门
---

# 在 30 分钟内启动 Hi3403

如果你刚拿到一块 Hi3403V100 开发板，本指南是最短的点亮路径：
**烧录预编译镜像 → 接串口和 HDMI → 登录系统**。

不需要编译、不需要 SDK、不需要交叉工具链。

## 你需要的东西

!!! tip "先准备这些"

    - 一块 Hi3403V100 开发板（[选板子帮助](board-picker.md)）
    - USB-A 转 Micro USB（或 USB Type-C，看板子）数据线 —— 烧录用
    - HDMI 线 + 显示器（看 GUI 的话）或 USB-串口转换器（命令行的话）
    - 一台 Linux / macOS / Windows 主机
    - 5V 充电器或 12V DC 电源（看板子）

时间预算：

| 步骤 | 用时 |
|---|---|
| 下载预编译镜像 | 5 分钟（依赖网速） |
| 烧录镜像 | 10–15 分钟 |
| 上电 + 等系统启动 | 1–2 分钟 |
| 配置网络 / 登录 | 5 分钟 |
| **总计** | **~30 分钟** |

## 步骤 1 — 下载预编译镜像

最简单的方式：用社区的
[`hi3403-build`](../tools/hi3403-build.md) 脚本一条命令产出镜像。

如果你只想拿到 `.img` 文件而不想自己编：可以直接从开发板厂商的发布页
下载预制镜像。每家板子的下载位置不同，看
[开发板](../boards/index.md) 页面里你的板子那一行。

预编译镜像的命名一般是：

```
hi3403-ubuntu-xfce-ss928v100.img    # 8 GB，带 XFCE 桌面
hi3403-ubuntu-lite-ss928v100.img    # 1.5 GB，纯命令行
```

## 步骤 2 — 烧录镜像

=== "用 BurnTool（推荐，海思官方工具）"

    BurnTool 是海思提供的图形化烧录工具，跨平台。

    1. 下载 BurnTool（详见 [BurnTool 工具使用指南](../tools/burntool.md)）。
    2. 把开发板进入烧录模式（一般是按住 BOOT 键再上电；具体看你板子的文档）。
    3. 用 USB 数据线连接电脑和开发板。
    4. 在 BurnTool 里选择 `.img` 文件，点 "Burn"。

=== "用 dd（macOS / Linux 写 SD 卡）"

    部分开发板支持从 SD 卡启动。把 `.img` 写到 SD 卡：

    ``` bash
    # ⚠️ 先确认 /dev/sdX 是 SD 卡，不是你的硬盘！
    sudo dd if=hi3403-ubuntu-xfce-ss928v100.img of=/dev/sdX bs=4M status=progress
    sudo sync
    ```

    macOS 上设备路径形如 `/dev/rdiskN`（带 `r` 前缀的更快）。

=== "用 Etcher（GUI，最适合新手）"

    1. 安装 [balenaEtcher](https://www.balena.io/etcher/)。
    2. 选择 `.img` 文件 → 选择 SD 卡 → 写入。

## 步骤 3 — 接线 + 上电

接线顺序：

1. **HDMI 线**（用桌面）或 **USB 串口线**（用命令行）—— 接显示器/电脑
2. **网线**（可选，要 SSH 时方便）
3. **键盘**（用桌面时）
4. **电源** —— 最后才插，避免误操作

上电后大概 30–60 秒能看到 Linux 启动信息（串口）或 XFCE 桌面（HDMI）。

!!! tip "看不到画面？"

    - 串口波特率 115200 8N1
    - HDMI 没信号 → 检查 DTB 是否对应你的板子（大部分镜像默认 Topeet）
    - 详见 [外围设备驱动](../soc-linux/peripherals.md) 里的常见排错

## 步骤 4 — 登录

XFCE 镜像自带的默认账户：

| 用户名 | 密码 |
|---|---|
| `hi` | `hi` |
| `root` | `hi` |

第一次登录后请马上 `passwd` 改密码。

## 你做到了 ✓

恭喜！下一步可以：

<div class="grid cards" markdown>

-   :material-wrench:{ .lg .middle } __自己编一个镜像__

    ---

    用 `hi3403-build` 一键脚本，定制内核配置或预装的软件包。

    [:octicons-arrow-right-24: hi3403-build](../tools/hi3403-build.md)

-   :material-application-cog:{ .lg .middle } __在 Hi3403 上写程序__

    ---

    交叉编译、调试、性能分析。

    [:octicons-arrow-right-24: 应用开发指南](../soc-linux/app-dev/index.md)

-   :material-video-vintage:{ .lg .middle } __玩多媒体功能__

    ---

    跑 MPP sample，验证摄像头、编解码、ISP 链路。

    [:octicons-arrow-right-24: MPP 概览](../multimedia/mpp/index.md)

-   :material-brain:{ .lg .middle } __跑一个 AI 模型__

    ---

    用 ATC 把 PyTorch / Caffe 模型转成 SVP 可执行格式，板端推理。

    [:octicons-arrow-right-24: SVP 开发](../multimedia/svp/index.md)

</div>
