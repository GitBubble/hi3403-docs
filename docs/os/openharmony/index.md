---
title: "OpenHarmony 海思芯片适配"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/os/OpenHarmony/README_zh.md
--- # OpenHarmony 海思芯片适配 ## 版本描述 本文档基于 OpenHarmony 5.1.0 Release 版本适配 Hi3403V100 芯片补丁包： 1. 支持 OpenHarmony 5.1.0 Small 型系统运行在 Hi3403V100 芯片上
2. 支持 Linux 6.6.86 内核
3. 继承 OpenHarmony 源生 llvm-clang 编译工具链
4. 支持 L1 设备带屏和不带屏的 XTS 兼容性测试
5. 支持继承 OpenHarmony 图形、媒体和增强特性开发，满足运行媒体和图形的 Sample 功能
6. 支持运行 Hi3403V100 的 SDK 源生 Sample ## 目录结构 ```
pegasus/
├── os/OpenHarmony
│ ├── device
│ │ └── soc/hisilicon/patches # OpenHarmony源码补丁（按子系统分类，对原生代码的定制化修改）
│ ├── kernel # 内核配置和补丁（linux-6.6）
│ ├── vendor # 海思产品配置（hispark_aifly_linux、hispark_aiflylite_linux）
│ └── manifest
│ ├── devboard_hispark_aifly_5.1.0.xml # repo清单文件（定义代码仓库列表）
│ └── prebuilts_setup.sh # 预编译环境准备脚本
├── platform/Hi3403V100_clang # SDK源码和二进制库（内核驱动、Sample、开源软件包）
└── vendor └── rkh/patches # 润开鸿OpenHarmony源码补丁（按子系统分类，增强系统功能和驱动支持）
``` ## 目录说明 ### device - 设备相关代码 #### device/board/hisilicon - 开发板配置 存放基于海思芯片的开发板相关内容，包括内核编译配置、构建脚本等。 **支持的开发板：** 1. **hispark_aifly** (Hi3403V100 芯片) - 系统类型：小型系统 - 应用领域：智慧视觉、AI 计算 - 关键文件： - `kernel/BUILD.gn` - 编译框架 GN 文件 - `kernel/kernel.mk` - 内核编译配置 - `kernel/kernel_module_build.sh` - 内核编译入口脚本 - `linux/config.gni` - 产品配置信息 2. **hispark_aiflylite** ( 芯片) - 系统类型：小型系统 - 应用领域：智慧视觉、AI 计算 #### device/soc/hisilicon - SoC 芯片相关 存放芯片相关内容，包括 HDI 实现、芯片软件、驱动源码、补丁等。 **主要子目录：**
- **common** - 公共代码（HAL 层实现、平台驱动）
- **hi3403v100** - Hi3403V100 芯片 SDK（Linux SDK、U-Boot）
- **patches** - OpenHarmony 补丁（按子系统分类，对原生代码的定制化修改） **patches 目录结构：** ```
patches
├── applications/sample # 应用示例补丁
├── base # 基础子系统补丁
│ ├── security # 安全子系统补丁
│ └── startup # 启动子系统补丁
├── build # 构建系统补丁
├── commonlibrary # 公共库补丁
│ └── c_utils # C 工具库补丁
├── developtools # 开发工具补丁
│ └── syscap_codec # Syscap 编码工具补丁
├── drivers # 驱动补丁
│ ├── hdf_core # HDF 核心补丁
│ └── peripheral # 外设驱动补丁
├── foundation # 基础框架补丁
│ ├── arkui # ArkUI 补丁
│ ├── distributedhardware # 分布式硬件补丁
│ ├── graphic # 图形子系统补丁
│ ├── multimedia # 媒体子系统补丁
│ └── window # 窗口管理补丁
├── test # 测试补丁
│ └── xts # XTS 兼容性测试补丁
├── third_party # 第三方组件补丁
│ ├── musl # Musl libc 补丁
│ └── openssl # OpenSSL 补丁
├── make_linux_patch.sh # 补丁制作脚本
└── README.md # 补丁说明文档
``` **关键功能：**
- **HAL 层**：提供显示、媒体、音频等硬件抽象层实现
- **平台驱动**：ADC、GPIO、I2C、I2S、SPI、UART、WiFi 等驱动
- **Hi3403V100 SDK**：包含媒体处理平台(MPP)、外设驱动、OS 适配层
- **补丁系统**：对 OpenHarmony 原生代码的定制化修改 ### kernel - 内核配置和补丁 #### kernel/linux/config - 内核配置 内核配置文件采用分层设计，通过合并多个配置文件生成最终的 defconfig。 **目录结构：** ```
kernel/linux/config
├── LICENSE
├── OAT.xml
├── README.md
├── README_zh.md
└── linux-6.6 ├── base_defconfig # 基础必选配置 ├── type # 系统类型配置 │ ├── small_defconfig # 小型系统配置 │ └── standard_defconfig # 标准系统配置 ├── hispark_aifly # Hi3403V100 配置 │ └── arch │ ├── arm64_defconfig # ARM64 架构配置 │ └── support_defconfig # OpenHarmony 支持配置 └── hispark_aiflylite # 配置 └── arch ├── arm64_defconfig └── support_defconfig
``` **配置文件组成：** 1. **base_defconfig** - 基础必选配置 - OpenHarmony 特性依赖的内核必选模块 - 安全红线特性配置 - 包含：FUTEX、EPOLL、EVENTFD、安全特性等 2. **type/small_defconfig** - 小型系统配置 - 小型系统常用内核配置 3. **type/standard_defconfig** - 标准系统配置 - 标准系统常用内核配置 4. **arch/arm64_defconfig** - 芯片特性配置 - 芯片单板 64 位版本相关配置 5. **arch/support_defconfig** - OpenHarmony 支持配置 - 适配 OpenHarmony 内核的专用配置 **配置合并流程：** ```bash
# 合并多个配置文件生成最终 defconfig
bash scripts/kconfig/merge_config.sh -O arch/arm64/configs/ \ -m type/small_defconfig \ hispark_aifly/arch/arm64_defconfig \ hispark_aifly/arch/support_defconfig \ base_defconfig
``` #### kernel/linux/patches - 内核补丁 **目录结构：** ```
kernel/linux/patches
└── linux-6.6 ├── common_patch # 通用补丁 │ └── hdf.patch # HDF 驱动框架补丁 ├── hispark_aifly_patch # Hi3403V100 芯片补丁 │ ├── 0001-kernel-hispark_aifly.patch │ ├── 0002-kernel-compile-support.patch │ ├── 0003-support-eulerpi-uvc-and-ethernet.patch │ ├── 0004-kernel-drm-support.patch │ ├── 0005-kernel-dhcp-support.patch │ └── patch_hispark_aifly.sh # 补丁应用脚本 └── hispark_aiflylite_patch # 芯片补丁 └── patch_hispark_aiflylite.sh
``` **补丁说明：** - **common_patch**：HDF 等通用补丁
- **hispark_aifly_patch**：Hi3403V100 芯片专用补丁 1. `0001-kernel-hispark_aifly.patch` - 芯片基础支持 2. `0002-kernel-compile-support.patch` - 编译支持 3. `0003-support-eulerpi-uvc-and-ethernet.patch` - UVC 和以太网支持 4. `0004-kernel-drm-support.patch` - DHCP 支持 5. `0005-kernel-dhcp-support.patch` - DRM 显示支持 ### manifest - 仓库清单 基于 OpenHarmony 5.1.0 Release 版本的仓库清单文件，用于 repo 工具同步代码。 **文件：**
- `devboard_hispark_aifly_5.1.0.xml` - repo 清单文件
- `prebuilts_setup.sh` - 预编译环境准备脚本（修复脚本bug、拷贝SDK、下载mbedtls/trusted-firmware-a、下载编译工具链、配置Clang环境变量） **清单特点：** 1. **剔除 Small 系统无需的代码仓** - 注释掉 LiteOS-A、LiteOS-M、Uniproton 等内核仓库 - 注释掉部分标准系统专用组件（如 NFC、DLP 管理器等） - 注释掉部分 Rust 第三方库 2. **常用修改的代码仓** - **kernel_linux_config** - 内核配置（已注释，使用本地版本） - **kernel_linux_patches** - 内核补丁（已注释，使用本地版本） - **device_soc_hisilicon** - 海思 SoC 支持（已注释，使用本地版本） - **device_board_hisilicon** - 海思开发板配置（已注释，使用本地版本） - **vendor_hisilicon** - 海思产品配置（已注释，使用本地版本） 3. **主要子系统组件** - **systemabilitymgr** - 系统能力管理（samgr_lite、safwk_lite） - **hiviewdfx** - 日志和诊断（hilog_lite、faultloggerd） - **security** - 安全子系统（permission_lite、appverify、device_auth、huks） - **startup** - 启动子系统（bootstrap_lite、init、appspawn） - **hdf** - 驱动框架（hdf_core、drivers_peripheral_display、drivers_peripheral_input） - **ability** - 能力框架（ability_lite、dmsfwk_lite） - **bundlemanager** - 包管理（bundle_framework_lite） - **xts** - 兼容性测试（acts、tools、device_attest_lite） - **communication** - 通信子系统（dhcp、ipc） - **arkui** - UI 框架（ace_engine_lite、ui_lite） - **graphic** - 图形子系统（graphic_utils_lite、surface_lite） - **window** - 窗口管理（window_manager_lite） - **multimedia** - 媒体子系统（camera_lite、media_lite、audio_lite、media_service） - **powermgr** - 电源管理（powermgr_lite） - **applications** - 应用示例（camera_sample_app、camera_screensaver_app） **使用方法：** ```bash
# 1. 进入 os/OpenHarmony 目录
cd os/OpenHarmony # 2. 初始化并同步代码
repo init -u https:/gitee.com/HiSpark/pegasus.git -m manifest/devboard_hispark_aifly_5.1.0.xml
repo sync -c
repo forall -c 'git lfs pull'
``` ### vendor - 厂商产品配置 存放产品定义配置、HDF 配置、文件系统配置等。 **主要子目录：**
- **hispark_aifly_linux** - Hi3403V100 产品配置 **关键配置文件：** 1. **config.json** - 产品定义 ```json { "product_name": "ipcamera_hispark_aifly_linux", "version": "3.0", "type": "small", "ohos_version": "OpenHarmony 5.1", "device_company": "hisilicon", "board": "hispark_aifly", "kernel_type": "linux", "kernel_version": "6.6", "target_cpu": "arm64", "subsystems": [...] } ``` 2. **patch.yml** - 补丁配置 - 定义需要应用的 OpenHarmony 源码补丁 - 包含海思和润开鸿的补丁 - 涵盖应用、安全、启动、构建、驱动等模块 3. **fs.yml** - 文件系统配置 - 定义 rootfs、userfs、userdata 分区 - 指定文件和目录的打包规则 - 设置文件权限和符号链接 - 生成 ext4 文件系统镜像 4. **hdf_config** - HDF 配置 - 支持的设备配置：GPIO、I2C、UART、SPI、ADC - Watchdog、PWM、MMC/SDIO、eMMC - LCD 显示、Input 输入 - WiFi、Sensor 传感器 - Vibrator 振动器 ## 支持的产品 | 产品名称 | 芯片 | 内核版本 | 系统类型 | 应用领域 |
|---------|------|---------|---------|---------|
| ipcamera_hispark_aifly_linux | Hi3403V100 | Linux 6.6 | Small | 智慧视觉、AI 计算 |
| ipcamera_hispark_aiflylite_linux | | Linux 6.6 | Small | 智慧视觉、AI 计算 | ## 关键技术特性 - **内核**：Linux 6.6.86，支持 ARM64 架构
- **编译工具链**：继承 OpenHarmony 源生 llvm-clang
- **驱动框架**：HDF (Hardware Driver Foundation)
- **文件系统**：ext4，支持 rootfs/userfs/userdata 分区
- **安全**：支持 HUKS、设备认证、应用验证
- **媒体**：支持音视频采集、编解码、输出
- **图形**：支持 DRM 显示、UI 引擎
- **测试**：支持 XTS 兼容性测试 ## 快速入手 请参考 [OpenHarmony Small版本使用指南](usage/index.md) 快速开始。 ### 相关文档 | **文档路径** | **用途介绍** |
|-------------|-------------|
| [OpenHarmony Small版本使用指南](usage/index.md) | Hi3403V100 上运行 OpenHarmony Small 系统，rootfs 打包文件系统，配置代码开发环境、编译、烧写；鸿蒙内核选项修改；XTS 测试说明；媒体功能使用；图形功能使用 |
| [OpenHarmony Small系统集成Hi3403V100移植案例](porting/index.md) | Hi3403V100 芯片解决方案集成案例：产品配置添加，内核移植适配、编译，XTS 认证，图形增强特性，媒体增强特性的适配案例总结 | ## 许可证 本项目遵循 OpenHarmony 开源许可证，具体请参考各目录下的 LICENSE 文件。
