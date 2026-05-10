---
description: Running Ubuntu, OpenHarmony, OpenEuler, Buildroot on Hi3403
title: OS
---

# OS

Hi3403V100 can run multiple operating systems. Each system has its own trade-offs—desktop experience,
Number of software packages, real-time performance, and image size. Below are the respective porting guides and usage instructions.

<div class="grid cards" markdown>

-   :simple-ubuntu:{ .lg .middle } __Ubuntu 22.04__

    ---

    XFCE4 desktop, apt package ecology is complete, and the development experience is closest to that of an ordinary PC.
    Use `hi3403-build` to generate a burnable image with one command.

    [:octicons-arrow-right-24: Enter](ubuntu/index.md)

-   :simple-harmonyos:{ .lg .middle } __OpenHarmony Small__

    ---

    OpenHarmony 5.1.0 Release version, small system.
    Supports XTS certification and is suitable for OpenHarmony devices.

    [:octicons-arrow-right-24: Enter](openharmony/index.md)

-   :simple-linux:{ .lg .middle } __OpenEuler__

    ---

    Domestic Linux distribution, the default configuration of Euler Pi.

    [:octicons-arrow-right-24: Enter](openeuler/index.md)

-   :material-cog-box:{ .lg .middle } __Buildroot__

    ---

    Minimalist system image, the most customizable and smallest, the default solution of Wildfire LubanCat.

    [:octicons-arrow-right-24: Enter](buildroot/index.md)

</div>

## How to choose?

Follow the decision tree in [Choose an operating system](../get-started/os-picker.md), according to
"Do you need a graphical interface?" "Do you need apt?" and "Real-time requirements" can be decided by just a few questions.

<div class="related" markdown>

## Related resources

<div class="grid cards" markdown>

-   :material-package-variant:{ .lg .middle } __hi3403-build__

    ---

    The easiest way to build an Ubuntu image.

    [:octicons-arrow-right-24: Enter](../tools/hi3403-build.md)

-   :material-chip:{ .lg .middle } __SoC and Linux__

    ---

    Kernel configuration, U-Boot, peripheral drivers - independent of the specific distribution.

    [:octicons-arrow-right-24: Enter](../soc-linux/index.md)

</div>

</div>