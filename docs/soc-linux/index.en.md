---
description: Hi3403V100 chip hardware, U-Boot, Linux kernel, peripheral drivers, secure
  boot
title: SoC & Linux
---

# SoC & Linux

Everything that has nothing to do with the specific distribution, but is strongly related to the hardware and underlying software: the capabilities of the chip itself,
Boot link (U-Boot → ATF → Kernel), various peripherals, memory layout, and security.

<div class="grid cards" markdown>

-   :material-chip:{ .lg .middle } __Hi3403V100 Overview__

    ---

    Chip architecture, capabilities, and typical application scenarios.

    [:octicons-arrow-right-24: Enter](soc-overview/index.md)

-   :material-rocket-launch:{ .lg .middle } __U-Boot porting__

    ---

    Porting and customization guide starting with U-Boot 2020.01.

    [:octicons-arrow-right-24: Enter](uboot/index.md)

-   :material-shield-key:{ .lg .middle } __Secure Boot__

    ---

    Hi3403V100/Hi3519AV200 secure boot key, signature, and burning process.

    [:octicons-arrow-right-24: Enter](secure-boot/index.md)

-   :material-power-plug:{ .lg .middle } __Peripheral device driver__

    ---

    Operation guide for UART, SPI, I2C, GPIO, USB, network port, SD/eMMC and other peripherals.

    [:octicons-arrow-right-24: Enter](peripherals/index.md)

-   :material-memory:{ .lg .middle } __Memory Layout__

    ---

    DDR allocation, MMZ media memory zone, NMA, secure/non-secure zone partitioning.

    [:octicons-arrow-right-24: Enter](memory-layout/index.md)

-   :material-camera:{ .lg .middle } __MIPI configuration__

    ---

    Hardware wiring and software configuration of MIPI CSI/DSI interface.

    [:octicons-arrow-right-24: Enter](mipi/index.md)

-   :material-tune:{ .lg .middle } __DDR tuning__

    ---

    DDR miniaturization, timing, power consumption and stability tuning.

    [:octicons-arrow-right-24: Enter](ddr-tuning/index.md)

-   :material-link-variant:{ .lg .middle } __PCIE cascade__

    ---

    Multi-chip Hi3403V100 PCIE cascade networking application.

    [:octicons-arrow-right-24: Enter](pcie/index.md)

-   :material-security:{ .lg .middle } __Security Subsystem__

    ---

    Collaborative use of the three subsystems KLAD, CIPHER and OTP.

    [:octicons-arrow-right-24: Enter](security/index.md)

-   :material-application-cog-outline:{ .lg .middle } __Application Development__

    ---

    Write a Linux user mode program on Hi3403: construction, debugging, and performance analysis.

    [:octicons-arrow-right-24: Enter](app-dev/index.md)

</div>

<div class="related" markdown>

## Related resources

<div class="grid cards" markdown>

-   :material-cog:{ .lg .middle } __SYS_CONFIG__

    ---

    Hi3403 system-level configuration file format and all configurable items.

    [:octicons-arrow-right-24: Enter](../reference/sys-config/index.md)

-   :material-help-circle:{ .lg .middle } __BSP FAQ__

    ---

    FAQs about BSP.

    [:octicons-arrow-right-24: Enter](../reference/faq/bsp/index.md)

</div>

</div>