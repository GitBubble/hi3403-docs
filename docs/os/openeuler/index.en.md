---
title: "Hi3403V100 OpenEuler porting guide"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/os/OpenEuler/README_zh.md
--- # Hi3403V100 OpenEuler porting guide - **Development platform**: - Host server: Ubuntu 22.04 - Hardware: Euler Pi
- **Two paths to a usable image**: - [§ 2.1 Download a pre-built image](#21-download-a-pre-built-image) — fastest, skips the build - [§ 2.2 Build the image yourself](#22-build-the-image-yourself) — slower but better understanding
- **References used while writing this guide**: - [oebridge — openEuler Embedded online docs (24.03)](https:/pages.openeuler.openatom.cn/embedded/docs/build/html/master/features/oebridge.html) - [Euler Pi image build & usage — openEuler Embedded online docs (24.03)](https:/pages.openeuler.openatom.cn/embedded/docs/build/html/master/bsp/arm64/hisilicon/hieulerpi/hieulerpi.html) - [openEuler ROS user / development manual](https:/openeuler-ros-docs.readthedocs.io/en/latest/) - [Booting XFCE without a GPU — issue ICVB82](https:/gitee.com/openeuler/yocto-meta-openeuler/issues/ICVB82?from=project-issue) - [hieulerpi1-xfce-systemd daily builds](http:/121.36.84.172/dailybuild/EBS-openEuler-Mainline/embedded_img/aarch64/hieulerpi1-xfce-systemd/20251026041019/) ## 1. Hardware - This guide uses the EBaina Euler Pi (4 GB / 32 GB) for screenshots. ## 2. Get the image Pick whichever path fits your needs. U-Boot is **not** included in
either — build it yourself per the board guide. ### 2.1 Download a pre-built image - Visit the [hieulerpi1-xfce-systemd daily-build directory](http:/121.36.84.172/dailybuild/EBS-openEuler-Mainline/embedded_img/aarch64/hieulerpi1-xfce-systemd/20251026041019/) and download both the kernel image and the rootfs image. ### 2.2 Build the image yourself #### 2.2.1 Install dependencies OpenEuler builds with `docker` + `oebuild`: ```bash
sudo apt-get install git python3 python3-pip docker docker.io
pip install oebuild
``` Configure Docker (the `daemon-reload && restart docker` step takes a moment): ```bash
sudo systemctl daemon-reload && sudo systemctl restart docker
sudo usermod -aG docker $USER
newgrp docker
``` #### 2.2.2 Initialize and build Follow the upstream openEuler-Embedded
[Euler Pi build guide](https:/pages.openeuler.openatom.cn/embedded/docs/build/html/master/bsp/arm64/hisilicon/hieulerpi/hieulerpi.html)
for the precise `oebuild` invocation — the recipe paths shift from
release to release. The output is a `kernel.bin` plus an ext4 rootfs
image. ## 3. Flash the image Use the same flashing procedure described in
[Quickstart — Step 2](../../get-started/quickstart.md#step-2-burn-the-image)
(BurnTool / `dd` / Etcher), pointing at the `.img` files you just
obtained. ## 4. First boot - Plug in HDMI + USB keyboard + power → XFCE desktop appears.
- Open a terminal — DNF is preconfigured to the openEuler mirrors. ## 5. Notes - This guide only covers the EBaina Euler Pi 4 GB / 32 GB board. Other variants need additional patches (RAM size, NPU clocks).
- The upstream Chinese README has more screenshots and step-by-step troubleshooting; switch the language toggle in the top-right to read it.
