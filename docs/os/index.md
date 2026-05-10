---
title: 操作系统
description: 在 Hi3403 上运行 Ubuntu、OpenHarmony、OpenEuler、Buildroot
---

# 操作系统

Hi3403V100 可以运行多种操作系统。每种系统都有各自的取舍 —— 桌面体验、
软件包数量、实时性、镜像大小。下面是各自的移植指南与使用说明。

<div class="grid cards" markdown>

-   :simple-ubuntu:{ .lg .middle } __Ubuntu 22.04__

    ---

    XFCE4 桌面，apt 包生态完整，开发体验最接近普通 PC。
    用 `hi3403-build` 一条命令产出可烧录镜像。

    [:octicons-arrow-right-24: 进入](ubuntu/index.md)

-   :simple-harmonyos:{ .lg .middle } __OpenHarmony Small__

    ---

    OpenHarmony 5.1.0 Release 版本，小型系统。
    支持 XTS 认证，适合做 OpenHarmony 设备。

    [:octicons-arrow-right-24: 进入](openharmony/index.md)

-   :material-open-source-initiative:{ .lg .middle } __OpenEuler__

    ---

    国产 Linux 发行版，海鸥派 Euler Pi 默认搭配。

    [:octicons-arrow-right-24: 进入](openeuler/index.md)

-   :material-cog-box:{ .lg .middle } __Buildroot__

    ---

    极简系统镜像，可定制性最强、体积最小，野火 LubanCat 默认方案。

    [:octicons-arrow-right-24: 进入](buildroot/index.md)

</div>

## 怎么挑？

跟着 [选择操作系统](../get-started/os-picker.md) 里的决策树走，根据
"要不要图形界面"、"要不要 apt"、"实时性需求" 几个问题就能定下来。

<div class="related" markdown>

## 相关资源

<div class="grid cards" markdown>

-   :material-package-variant:{ .lg .middle } __hi3403-build__

    ---

    构建 Ubuntu 镜像最简单的方式。

    [:octicons-arrow-right-24: 进入](../tools/hi3403-build.md)

-   :material-chip:{ .lg .middle } __SoC 与 Linux__

    ---

    内核配置、U-Boot、外设驱动 —— 跟具体发行版无关。

    [:octicons-arrow-right-24: 进入](../soc-linux/index.md)

</div>

</div>
