---
title: Ubuntu porting & build guide
description: Use hi3403-build to one-shot a Hi3403V100 (Hi3403V100) Ubuntu 22.04 ARM64 image
---

# Ubuntu porting & build guide

This guide walks you through building a Hi3403V100 (Hi3403V100) Ubuntu
22.04 ARM64 image — boot, kernel, MPP, and rootfs — using the
[`hi3403-build`](https://github.com/GitBubble/hi3403-build) project on
top of the open-source [Pegasus](https://gitee.com/HiSpark/pegasus) SDK.

!!! tip "Source repo"
    The code that backs this guide is on GitHub:
    [**GitBubble/hi3403-build**](https://github.com/GitBubble/hi3403-build)

    ```bash
    git clone --recurse-submodules https://github.com/GitBubble/hi3403-build.git
    cd hi3403-build
    ```

## Supported boards

- Topeet iTOP-Hi3403V100 (default)
- Other boards through vendor patches under `pegasus/vendor/`

## Requirements

- **Docker** (used for cross-compilation — required)
- **git** (to clone the pegasus submodule)
- **macOS / Linux** host

## Quick start

```bash
# One-shot: full image with XFCE desktop
./build.sh ubuntu_xfce_all

# One-shot: lite (headless) image
./build.sh ubuntu_lite_all
```

## All commands

### One-shot builds

| Command | What it does |
|---|---|
| `ubuntu_xfce_all` | Full pipeline: boot + MPP + XFCE rootfs + image packaging |
| `ubuntu_lite_all` | Full pipeline: boot + MPP + lite rootfs + image packaging |
| `all` | Same as `ubuntu_xfce_all` |

### Individual components

| Command | What it does | Output |
|---|---|---|
| `uboot` | U-Boot bootloader | `output/boot/u-boot.bin` |
| `atf` | ARM Trusted Firmware | `output/boot/bl31.bin` |
| `kernel` | Linux kernel + DTBs | `output/boot/Image.gz` + `*.dtb` |
| `kernel-image` | Linux kernel only | `output/boot/Image.gz` |
| `dtb` | Device trees only | `output/boot/*.dtb` |
| `boot` | All boot components | uboot + atf + kernel + dtbs |
| `mpp` | MPP kernel modules | `output/mpp/ko/*.ko` |

### Rootfs and packaging

| Command | What it does |
|---|---|
| `ubuntu_xfce` | Build the XFCE desktop rootfs only |
| `ubuntu_lite` | Build the lite rootfs only (no desktop) |
| `rootfs` | Build the rootfs (defaults to `xfce`) |
| `integrate` | Copy the MPP modules into an existing rootfs |
| `package` | Package the rootfs into an ext4 image |

### Utilities

| Command | What it does |
|---|---|
| `setup` | Clone repos + download sources + apply patches |
| `sources` | Download source tarballs only |
| `clean` | Remove all build artefacts |
| `shell` | Drop into the Docker build environment interactively |
| `--help` | Show usage |

## Options

```bash
./build.sh ubuntu_xfce_all -j 8                # 8 parallel jobs
./build.sh rootfs ROOTFS_TYPE=lite             # lite rootfs only
./build.sh all BOOT_MEDIA=spi CHIP=Hi3403V100   # custom build params
```

| Option | Meaning | Default |
|---|---|---|
| `-j N` | Parallel make jobs | `nproc` |
| `ROOTFS_TYPE=` | `xfce` or `lite` | `xfce` |
| `BOOT_MEDIA=` | `emmc`, `spi`, `nand` | `emmc` |
| `CHIP=` | `Hi3403V100` or `Hi3519AV200` | `Hi3403V100` |

## Output

```text
output/
├── hi3403-ubuntu-xfce-Hi3403V100.img    # rootfs ext4 image
├── boot/
│   ├── u-boot.bin                      # U-Boot 2020.01
│   ├── bl31.bin                        # ATF BL31
│   ├── Image.gz                        # Linux 6.6.86 ARM64
│   ├── Hi3403V100-demb-emmc.dtb         # eMMC variant DTB
│   └── Hi3403V100-demb-flash.dtb        # Flash variant DTB
└── mpp/
    ├── ko/                              # kernel modules
    └── lib/                             # MPP user-space libraries
```

## Flashing

```text
1. Write u-boot.bin to the eMMC boot partition
2. Write Image.gz + DTB to the boot partition
3. Write rootfs.img to the root partition
```

## Default login

- **Username:** `hi`
- **Password:** `hi`

## Build details

- **Kernel:** Linux 6.6.86 with HiSilicon BSP + Topeet vendor patches
- **Toolchain:** GCC 11.4.0 (`aarch64-linux-gnu-gcc`)
- **Rootfs:** Ubuntu 22.04.5 ARM64
- **Desktop:** XFCE4 (xfce variant)
- **MPP:** HiSilicon Media Process Platform — 89 user-space libraries + 8 kernel modules

## Project layout

```text
hi3403-build/
├── build.sh            # main build script
├── README.md           # project README
├── docker/
│   └── Dockerfile      # Ubuntu 22.04 build environment
├── pegasus/            # HiSilicon Pegasus SDK (Gitee submodule)
├── hi3403-docs/        # this docs site (GitHub submodule)
├── downloads/          # source tarball cache
├── scripts/            # helpers
└── output/             # build artefacts
    ├── boot/
    ├── mpp/
    └── rootfs/
```

## Troubleshooting

**"Docker image not found"**
First run will auto-build the Docker image (~5 minutes).

**"mount: permission denied"**
Docker needs `--privileged` to create the rootfs — `build.sh` already
sets that.

**Slow apt downloads**
`build.sh` configures the USTC mirror automatically.

**"E: Sub-process dpkg returned an error"**
The rootfs is built on ext4 inside Docker, which sidesteps macOS
filesystem incompatibilities.

## Related links

- Source + issue tracker: [GitHub · GitBubble/hi3403-build](https://github.com/GitBubble/hi3403-build)
- Pegasus SDK: [Gitee · HiSpark/pegasus](https://gitee.com/HiSpark/pegasus)
- Docs source: [GitHub · GitBubble/hi3403-docs](https://github.com/GitBubble/hi3403-docs)
