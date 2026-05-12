---
description: From empty board to login interface - an introduction to the shortest
  path
title: Boot Hi3403 in 30 minutes
---

# Boot Hi3403 in 30 minutes

If you just got a Hi3403V100 development board, this guide is the shortest path to lighting it up:
**Burn the precompiled image → Connect the serial port and HDMI → Log in to the system**.

No compilation, no SDK, no cross toolchain required.

## what you need

!!! tip "Prepare these first"

    - A Hi3403V100 development board ([Palette help](board-picker.md))
    - USB-A to Micro USB (or USB Type-C, see the board) data cable - for programming
    - HDMI cable + monitor (for GUI) or USB-to-serial converter (for command line)
    - A Linux / macOS / Windows host
    - 5V charger or 12V DC power supply (see the board)

Time budget:

| step | time |
|---|---|
| Download precompiled image | 5 minutes (depends on internet speed) |
| Flash the image | 10–15 minutes |
| Power on + wait for system startup | 1–2 minutes |
| Configure network/login | 5 minutes |
| **total** | **~30 minutes** |

## Step 1 — Download the precompiled image

The easiest way: use the community
[`hi3403-build`](../tools/hi3403-build.md) script produces an image with one command.

If you just want to get the `.img` file without editing it yourself: You can directly download it from the development board manufacturer's release page
Download the pre-made image. The download location of each board is different, see
[Boards](../boards/index.md) The row of your board on the page.

The naming of precompiled images is generally:

```
hi3403-ubuntu-xfce-Hi3403V100.img # 8 GB with XFCE desktop
hi3403-ubuntu-lite-Hi3403V100.img # 1.5 GB, pure command line
```

## Step 2 — Burn the image

=== "Use BurnTool (recommended, HiSilicon official tool)"

    BurnTool is a graphical burning tool provided by HiSilicon and is cross-platform.

    1. Download BurnTool (see [the BurnTool user guide](../tools/burntool/index.md)).
    2. Put the development board into programming mode (usually press and hold the BOOT key before powering on; see your board's documentation for details).
    3. Connect the computer and development board with a USB data cable.
    4. Select the `.img` file in BurnTool and click "Burn".

=== "Write to SD card using dd (macOS/Linux)"

    Some development boards support booting from the SD card. Write `.img` to SD card:

    ``` bash
    # ⚠️ First make sure /dev/sdX is an SD card, not your hard drive!
    sudo dd if=hi3403-ubuntu-xfce-Hi3403V100.img of=/dev/sdX bs=4M status=progress
    sudo sync
    ```

    The device path on macOS looks like `/dev/rdiskN` (prefixed with `r` is faster).

=== "Use Etcher (GUI, best for newbies)"

    1. Install [balenaEtcher](https://www.balena.io/etcher/).
    2. Select `.img` file → select SD card → Write.

## Step 3 — Wire + Power Up

Wiring sequence:

1. **HDMI cable** (using desktop) or **USB serial cable** (using command line) - connect to monitor/computer
2. **Network cable** (optional, convenient when you need SSH)
3. **Keyboard** (when using desktop)
4. **Power supply** - plug in last to avoid misoperation

It takes about 30-60 seconds after powering on to see the Linux boot information (serial port) or XFCE desktop (HDMI).

!!! tip "Can't see the screen?"

    - Serial port baud rate 115200 8N1
    - HDMI has no signal → Check if DTB corresponds to your board (most images default to Topeet)
    - For more troubleshooting, see [Peripheral drivers](../soc-linux/peripherals/index.md)

## Step 4 — Login

Default accounts on the `hi3403-build` image:

| Username | Password | Notes |
|---|---|---|
| `hi` | `hi` | Already in the `sudo` group |
| `root` | (locked) | Disabled by default; run `sudo passwd root` to set one |

Run `sudo passwd hi` to change the password as soon as you log in.
Other vendors' images (OpenHarmony, OpenEuler, various Buildroot
builds) use different defaults — check the download page for your image.

## You did it ✓

Congratulations! Next steps can be:

<div class="grid cards" markdown>

-   :material-wrench:{ .lg .middle } __Create a mirror yourself__

    ---

    Use `hi3403-build` one-click script to customize kernel configuration or pre-installed software packages.

    [:octicons-arrow-right-24: hi3403-build](../tools/hi3403-build.md)

-   :material-application-cog:{ .lg .middle } __Write a program on Hi3403__

    ---

    Cross-compilation, debugging, performance analysis.

    [:octicons-arrow-right-24: Application Development Guide](../soc-linux/app-dev/index.md)

-   :material-video-vintage:{ .lg .middle } __Play multimedia functions__

    ---

    Run MPP sample to verify the camera, codec, and ISP link.

    [:octicons-arrow-right-24: MPP Overview](../multimedia/mpp/index.md)

-   :material-brain:{ .lg .middle } __Run an AI model__

    ---

    Use ATC to convert PyTorch/Caffe models into SVP executable format for board-side inference.

    [:octicons-arrow-right-24: SVP Development](../multimedia/svp/index.md)

</div>