---
title: "Hi3403V100 Ubuntu Image Builder"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/README.md
---

# Hi3403V100 Ubuntu Image Builder

Build Ubuntu 22.04 ARM64 images for Hi3403V100 (SS928V100) boards using the open-source [Hi3403](https://gitee.com/HiSpark/pegasus) repository.

## Supported Boards

- Topeet iTOP-Hi3403V100 (default)
- Add other boards via vendor patches in `hi3403/vendor/`

## Prerequisites

- **Docker** (required for cross-compilation)
- **git** (to clone hi3403)
- **macOS / Linux** host

## Quick Start

```bash
# Full build with XFCE desktop (one command)
./build.sh ubuntu_xfce_all

# Full build without desktop
./build.sh ubuntu_lite_all
```

## All Commands

### Full Builds

| Command | Description |
|---|---|
| `ubuntu_xfce_all` | Everything: boot + MPP + XFCE rootfs + package image |
| `ubuntu_lite_all` | Everything: boot + MPP + lite rootfs + package image |
| `all` | Same as `ubuntu_xfce_all` |

### Individual Components

| Command | Description | Output |
|---|---|---|
| `uboot` | U-Boot bootloader | `output/boot/u-boot.bin` |
| `atf` | ARM Trusted Firmware | `output/boot/bl31.bin` |
| `kernel` | Linux kernel + DTBs | `output/boot/Image.gz` + `*.dtb` |
| `kernel-image` | Linux kernel only | `output/boot/Image.gz` |
| `dtb` | Device tree blobs only | `output/boot/*.dtb` |
| `boot` | All boot components | uboot + atf + kernel + dtbs |
| `mpp` | MPP kernel modules | `output/mpp/ko/*.ko` |

### Rootfs & Packaging

| Command | Description |
|---|---|
| `ubuntu_xfce` | Build XFCE desktop rootfs only |
| `ubuntu_lite` | Build lite rootfs only (no desktop) |
| `rootfs` | Build rootfs (default: xfce) |
| `integrate` | Copy MPP modules into existing rootfs |
| `package` | Package rootfs into ext4 image |

### Utilities

| Command | Description |
|---|---|
| `setup` | Clone repos + download sources + apply patches |
| `sources` | Download source tarballs only |
| `clean` | Remove all build artifacts |
| `shell` | Enter Docker build environment interactively |
| `--help` | Show this help |

## Options

```bash
./build.sh ubuntu_xfce_all -j 8         # Use 8 parallel jobs
./build.sh rootfs ROOTFS_TYPE=lite      # Build lite rootfs
./build.sh all BOOT_MEDIA=spi CHIP=ss928v100   # Custom build params
```

| Option | Description | Default |
|---|---|---|
| `-j N` | Parallel make jobs | `nproc` |
| `ROOTFS_TYPE=` | `xfce` or `lite` | `xfce` |
| `BOOT_MEDIA=` | `emmc`, `spi`, `nand` | `emmc` |
| `CHIP=` | `ss928v100` or `ss927v100` | `ss928v100` |

## Output

```
output/
├── hi3403-ubuntu-xfce-ss928v100.img    # Rootfs ext4 image
├── boot/
│   ├── u-boot.bin                      # U-Boot 2020.01
│   ├── bl31.bin                        # ATF BL31
│   ├── Image.gz                        # Linux 6.6.86 ARM64
│   ├── ss928v100-demb-emmc.dtb         # eMMC variant DTB
│   └── ss928v100-demb-flash.dtb        # Flash variant DTB
└── mpp/
    ├── ko/                              # Kernel modules
    └── lib/                             # MPP shared libraries
```

## Flashing

```
1. Write u-boot.bin → eMMC boot partition
2. Write Image.gz + DTB → boot partition
3. Write rootfs.img → root partition
```

## Default Login

- **User:** `hi`
- **Password:** `hi`

## Build Details

- **Kernel:** Linux 6.6.86 with HiSilicon BSP + Topeet vendor patches
- **Toolchain:** GCC 11.4.0 (aarch64-linux-gnu-gcc)
- **Rootfs:** Ubuntu 22.04.5 ARM64
- **Desktop:** XFCE4 (xfce variant)
- **MPP:** HiSilicon media processing platform (89 userspace libs + 8 kernel modules)

## Directory Layout

```
hi3403-build/
├── build.sh            # Main build script
├── README.md           # This file
├── docker/
│   └── Dockerfile      # Ubuntu 22.04 build environment
├── hi3403/            # HiSilicon Hi3403 SDK (cloned from Gitee)
├── downloads/          # Source tarballs cache
├── scripts/            # Helper scripts
└── output/             # Build artifacts
    ├── boot/
    ├── mpp/
    └── rootfs/
```

## Troubleshooting

**"Docker image not found"** — First run will auto-build the Docker image (~5 min).

**"mount: permission denied"** — Docker needs `--privileged` for rootfs creation (build.sh handles this).

**Slow apt downloads** — build.sh auto-configures USTC mirror for China users.

**"E: Sub-process dpkg returned an error"** — Rootfs is built on ext4 inside Docker, avoiding macOS filesystem issues.
