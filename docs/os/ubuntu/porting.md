---
title: Ubuntu 移植与构建指南
description: 使用 hi3403-build 一键构建 Hi3403V100 (Hi3403V100) 的 Ubuntu 22.04 ARM64 镜像
---

# Ubuntu 移植与构建指南

本指南介绍如何使用 [`hi3403-build`](https://github.com/GitBubble/hi3403-build) 项目，
基于开源 [Pegasus](https://gitee.com/HiSpark/pegasus) 仓库为 Hi3403V100 (Hi3403V100) 开发板
构建 Ubuntu 22.04 ARM64 镜像（含 boot、内核、MPP 与 rootfs）。

!!! tip "源码仓库"
    本指南配套代码托管于 GitHub：[**GitBubble/hi3403-build**](https://github.com/GitBubble/hi3403-build)

    ```bash
    git clone --recurse-submodules https://github.com/GitBubble/hi3403-build.git
    cd hi3403-build
    ```

## 支持的开发板

- Topeet iTOP-Hi3403V100（默认）
- 其它开发板可通过 `pegasus/vendor/` 下的厂商补丁扩展

## 环境要求

- **Docker**（用于交叉编译，必需）
- **git**（克隆 pegasus 子模块）
- **macOS / Linux** 主机

## 快速开始

```bash
# 一键构建带 XFCE 桌面的完整镜像
./build.sh ubuntu_xfce_all

# 一键构建无桌面的精简镜像
./build.sh ubuntu_lite_all
```

## 全部命令

### 一键构建

| 命令 | 说明 |
|---|---|
| `ubuntu_xfce_all` | 完整流程：boot + MPP + XFCE rootfs + 打包镜像 |
| `ubuntu_lite_all` | 完整流程：boot + MPP + lite rootfs + 打包镜像 |
| `all` | 同 `ubuntu_xfce_all` |

### 单独组件

| 命令 | 说明 | 输出 |
|---|---|---|
| `uboot` | U-Boot 引导加载程序 | `output/boot/u-boot.bin` |
| `atf` | ARM Trusted Firmware | `output/boot/bl31.bin` |
| `kernel` | Linux 内核 + DTB | `output/boot/Image.gz` + `*.dtb` |
| `kernel-image` | 仅 Linux 内核 | `output/boot/Image.gz` |
| `dtb` | 仅设备树 | `output/boot/*.dtb` |
| `boot` | 全部 boot 组件 | uboot + atf + kernel + dtbs |
| `mpp` | MPP 内核模块 | `output/mpp/ko/*.ko` |

### Rootfs 与打包

| 命令 | 说明 |
|---|---|
| `ubuntu_xfce` | 仅构建 XFCE 桌面 rootfs |
| `ubuntu_lite` | 仅构建精简 rootfs（无桌面） |
| `rootfs` | 构建 rootfs（默认 xfce） |
| `integrate` | 将 MPP 模块复制到现有 rootfs |
| `package` | 将 rootfs 打包为 ext4 镜像 |

### 工具

| 命令 | 说明 |
|---|---|
| `setup` | 克隆仓库 + 下载源码 + 应用补丁 |
| `sources` | 仅下载源码压缩包 |
| `clean` | 清除所有构建产物 |
| `shell` | 交互式进入 Docker 构建环境 |
| `--help` | 显示帮助信息 |

## 选项

```bash
./build.sh ubuntu_xfce_all -j 8                # 使用 8 个并行任务
./build.sh rootfs ROOTFS_TYPE=lite             # 构建精简 rootfs
./build.sh all BOOT_MEDIA=spi CHIP=Hi3403V100   # 自定义构建参数
```

| 选项 | 说明 | 默认值 |
|---|---|---|
| `-j N` | 并行 make 任务数 | `nproc` |
| `ROOTFS_TYPE=` | `xfce` 或 `lite` | `xfce` |
| `BOOT_MEDIA=` | `emmc`、`spi`、`nand` | `emmc` |
| `CHIP=` | `Hi3403V100` 或 `Hi3519AV200` | `Hi3403V100` |

## 输出产物

```text
output/
├── hi3403-ubuntu-xfce-Hi3403V100.img    # Rootfs ext4 镜像
├── boot/
│   ├── u-boot.bin                      # U-Boot 2020.01
│   ├── bl31.bin                        # ATF BL31
│   ├── Image.gz                        # Linux 6.6.86 ARM64
│   ├── Hi3403V100-demb-emmc.dtb         # eMMC 变体 DTB
│   └── Hi3403V100-demb-flash.dtb        # Flash 变体 DTB
└── mpp/
    ├── ko/                              # 内核模块
    └── lib/                             # MPP 用户态库
```

## 烧录

```text
1. 将 u-boot.bin 写入 eMMC boot 分区
2. 将 Image.gz + DTB 写入 boot 分区
3. 将 rootfs.img 写入 root 分区
```

## 默认登录

- **用户名：** `hi`
- **密码：** `hi`

## 构建详情

- **内核：** Linux 6.6.86，含 HiSilicon BSP 与 Topeet 厂商补丁
- **工具链：** GCC 11.4.0 (`aarch64-linux-gnu-gcc`)
- **Rootfs：** Ubuntu 22.04.5 ARM64
- **桌面：** XFCE4（xfce 变体）
- **MPP：** HiSilicon 媒体处理平台（89 个用户态库 + 8 个内核模块）

## 目录结构

```text
hi3403-build/
├── build.sh            # 主构建脚本
├── README.md           # 项目说明
├── docker/
│   └── Dockerfile      # Ubuntu 22.04 构建环境
├── pegasus/            # HiSilicon Pegasus SDK（Gitee 子模块）
├── hi3403-docs/        # 本文档站（GitHub 子模块）
├── downloads/          # 源码压缩包缓存
├── scripts/            # 辅助脚本
└── output/             # 构建产物
    ├── boot/
    ├── mpp/
    └── rootfs/
```

## 故障排查

**“Docker image not found”**
首次运行会自动构建 Docker 镜像（约 5 分钟）。

**“mount: permission denied”**
Docker 创建 rootfs 需要 `--privileged`，`build.sh` 已处理。

**apt 下载缓慢**
`build.sh` 会自动配置中科大 (USTC) 镜像源。

**“E: Sub-process dpkg returned an error”**
Rootfs 在 Docker 内的 ext4 上构建，规避了 macOS 文件系统的兼容问题。

## 相关链接

- 源码与 Issue：[GitHub · GitBubble/hi3403-build](https://github.com/GitBubble/hi3403-build)
- Pegasus SDK：[Gitee · HiSpark/pegasus](https://gitee.com/HiSpark/pegasus)
- 文档源码：[GitHub · GitBubble/hi3403-docs](https://github.com/GitBubble/hi3403-docs)
