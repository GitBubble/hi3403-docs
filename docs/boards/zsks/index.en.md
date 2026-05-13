---
title: "ZSKS (Zhongshan Kuangshi) — README"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/vendor/zsks/README.md
--- ## 1. About the project - This directory is a deep-collaboration open-source project between **Zhongshan Kuangshi (ZSKS) Microelectronics** and HiSilicon. The aim is to ship convenient, efficient, easy-to-use third-party software and tools for developers, growing the HiSilicon ecosystem.
- The `demo/` directory holds practical examples ZSKS built on the Hi3403V100 platform, including: - OpenCV face detection - HNR-based extreme low-light night-vision - YOLOv8 fruit recognition + voice announcement - KCF object tracking - YOLOv8 face detection under strong backlight - OpenCV hardware-accelerated through IVE — lets OpenCV-fluent developers use the Hi3403V100 hardware accelerator with minimal learning curve
- ZSKS has ported common third-party software to Hi3403V100 — Python, NumPy, OpenCV, libv4l2, alsa-lib, ffmpeg, libcamera. The `doc/` directory contains the porting and dev documentation. They have also Python-bound the Hi3403V100 MPP modules so a few lines of Python suffice to drive a HiSilicon use-case.
- The `patch/` directory ships ZSKS' SDK patches that the demos depend on. ## 2. Developer guide ### Step 1: Set up the environment First follow the official
[Hi3403V100 environment-setup guide](https:/gitee.com/HiSpark/pegasus/blob/master/docs/Hi3403V100%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA%E6%8C%87%E5%8D%97/Hi3403V100%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA%E6%8C%87%E5%8D%97.md). ### Step 2: Apply patches On your build host, apply the ZSKS patches into the Hi3403 tree: ```sh
cd pegasus/vendor/zsks ./patch_build.sh
``` Apply the matching RKH patches: ```sh
cd pegasus/os/OpenHarmony cp ../../vendor/rkh/rkh_patch* . -rf sudo apt-get update sudo apt-get install dos2unix dos2unix ohos/foundation/systemabilitymgr/samgr_lite/samgr/source/service.c dos2unix ohos/vendor/hisilicon/hispark_Hi3403V100_linux/config.json dos2unix ohos/vendor/hisilicon/hispark_Hi3403V100_linux/init_configs/init_linux_openharmony.cfg chmod +x rkh_patch_build.sh ./rkh_patch_build.sh
``` Apply the UVC + Ethernet OpenHarmony kernel patches: ```sh
cd pegasus/os/OpenHarmony cp ../../vendor/zsks/patch/0001-support-eulerpi-uvc-and-ethernet.patch \ ohos/kernel/linux/patches/linux-6.6/hispark_Hi3403V100_patch/
``` ### Step 3: Build & flash Follow the upstream OpenHarmony build instructions; the patched tree
will produce a flashable image that includes the ZSKS demos and ported
third-party software. ## 3. Demos | Demo | What it shows |
|---|---|
| `face_detection` | OpenCV-based face detection |
| `hnr_auto` | Heterogeneous noise reduction for low-light |
| `fruit_identify` | YOLOv8 fruit classification with audio output |
| `sample_kcf_track` | KCF tracking on live video |
| `opencv_dnn` | YOLOv8 face detection in strong backlight | Each demo's own `demo/<name>/README.md` walks through running it on
hardware. ## 4. Third-party software Available through the ZSKS port: - **Python** + standard library
- **NumPy**
- **OpenCV** (hardware-accelerated via IVE)
- **libv4l2** for V4L2 capture
- **ALSA libraries** for audio
- **ffmpeg** for media processing
- **libcamera** for camera abstraction Per-package porting notes live under `doc/` — `python/`, `opencv/`,
`numpy/`, `libv4l2/`, `libcamera/`, `ffmpeg/`, `alsa-lib/`. ## 5. Python-friendly MPP ZSKS exposes the MPP subsystems through Python bindings, so a few
lines of Python set up VI / VPSS / VENC pipelines, OSD, and AI
inference. See the demos for the calling style.
