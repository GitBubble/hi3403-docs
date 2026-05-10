---
title: "OpenHarmony — HiSilicon-chip adaptation"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/os/OpenHarmony/README_zh.md
---

# OpenHarmony — HiSilicon-chip adaptation

## Release scope

This patchset adapts **OpenHarmony 5.1.0 Release** to the
**Hi3403V100 / Hi3519AV200** chips:

1. The OpenHarmony 5.1.0 Small-system runs on Hi3403V100 / Hi3519AV200
2. Linux 6.6.86 kernel
3. Inherits the OpenHarmony native llvm/clang toolchain
4. Passes the L1 device XTS compatibility tests, with and without a display
5. Inherits the OpenHarmony graphics, media, and enhancement features —
   the media + graphics samples run end-to-end
6. Runs the SS928V100 SDK's native samples

## Repository layout

```
pegasus/
├── os/OpenHarmony
│   ├── device
│   │   └── soc/hisilicon/patches   # OpenHarmony source patches by subsystem (customizations on top of the upstream)
│   ├── kernel                      # Kernel config + patches (linux-6.6)
│   ├── vendor                      # HiSilicon product configurations (hispark_aifly_linux, hispark_aiflylite_linux)
│   └── manifest
│       ├── devboard_hispark_aifly_5.1.0.xml  # repo manifest (lists code repos)
│       └── prebuilts_setup.sh                # pre-build environment setup
├── platform/ss928v100_clang        # SDK source + binaries (kernel drivers, samples, OSS)
└── vendor
    └── rkh/patches                 # 润开鸿 (RKH) OpenHarmony patches by subsystem (extra features + driver support)
```

## Directory guide

### `device/` — board-specific code

#### `device/board/hisilicon` — board configurations

**Supported boards:**

1. **`hispark_aifly`** (Hi3403V100 chip)
   - System type: Small system
   - Domain: smart-vision, AI compute
   - Key files:
     - `kernel/BUILD.gn` — GN build file
     - `kernel/build.sh` — kernel build script
     - `liteos_a_display.config` / `liteos_a_no_display.config` — LiteOS-A configs
     - `linux_no_display.config` / `linux_display.config` — Linux configs
2. **`hispark_aiflylite`** (Hi3403V100 chip)
   - Lower-tier configuration of the same SoC

#### `device/soc/hisilicon` — SoC-specific code

Patches are organised by subsystem:

```
device/soc/hisilicon/patches/
├── ai/                      # AI / ATC / SVP
├── communication/           # Wi-Fi, BT
├── distributedhardware/     # Distributed-hardware framework
├── graphic/                 # 2D / 3D graphics
├── multimedia/              # MPP layer
├── powermgr/                # Power-management
├── security/                # Cipher / KLAD / OTP
└── ...
```

Each patch tracks an upstream OpenHarmony commit and adds
HiSilicon-specific changes (driver hooks, MMZ allocator, ISP bring-up,
NPU integration).

### `kernel/` — kernel config + patches

- **`config/`** — hispark-board-specific `defconfig` files
- **`patches/`** — kernel patches that aren't yet upstream

The kernel base is **Linux 6.6** — patches sit on top.

### `vendor/` — HiSilicon product configurations

Two product variants:

- `hispark_aifly_linux` — full Hi3403V100 (4-core A55 + NPU)
- `hispark_aiflylite_linux` — light variant (fewer cores or capped NPU)

### `manifest/` — repo manifest

- `devboard_hispark_aifly_5.1.0.xml` — `repo init -m` points at this
  to bring all the relevant OpenHarmony repos in
- `prebuilts_setup.sh` — pre-build environment prep (toolchain
  download, Python deps, etc.)

## Build flow (high level)

1. `repo init` against the manifest
2. Clone `pegasus` and `vendor/rkh` (if you need RKH-specific changes)
3. Run `prebuilts_setup.sh` to bring down the LLVM toolchain
4. Apply the `os/OpenHarmony/patches/` patches into your OpenHarmony tree
5. `./build.sh hispark_aifly`

For full step-by-step instructions see the dedicated
[OpenHarmony Small-system usage guide](usage/index.md) and the
[Hi3403V100 OpenHarmony porting case-study](porting/index.md).

## Patches and customizations

`os/OpenHarmony/device/soc/hisilicon/patches/` contains 40+ patches
sliced by subsystem. Each patch carries:

- A short description (e.g. `add Hi3403V100 ISP driver`)
- The OpenHarmony component it targets
- The upstream commit it's based on

When OpenHarmony moves, these are the patches you re-base to bring up
a newer release.

## Vendor: 润开鸿 (RKH)

`vendor/rkh/patches/` adds OpenHarmony tweaks specific to the RKH
desktop image — extended driver support, more GUI components, and
desktop-friendly defaults. See the
[RKH board page](../../boards/rkh/index.md) for the full feature list.

## Related docs

- [OpenHarmony Small-system usage guide](usage/index.md) — boots, sample apps, day-to-day usage
- [Porting case-study: integrating OpenHarmony Small on Hi3403V100](porting/index.md) — step-by-step migration walkthrough
- Upstream OpenHarmony documentation: <https://gitee.com/openharmony/docs>
