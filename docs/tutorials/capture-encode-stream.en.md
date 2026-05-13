---
title: Capture → encode → stream
description: Use a MIPI camera to capture, H.264-encode, and push the stream over RTSP to your LAN
--- # Tutorial: capture → encode → stream **Goal**: continuously capture 1080p@30fps from a MIPI camera, encode it
to H.264, and push to an RTSP stream. Open VLC on a phone or laptop and
see the live picture. **Time**: ~45 minutes (after first-time image flash) !!! info "Assumed runtime environment" This tutorial assumes the Ubuntu 22.04 image produced by [`hi3403-build`](../tools/hi3403-build.md). In that image, MPP user-space libraries live in `/usr/lib/`, kernel modules in `/ko/`, and `/etc/init.d/topeet-start.sh` `insmod`s them at boot. Other images (OpenHarmony, Buildroot, custom builds) put things elsewhere — adapt the paths below to your install layout. **Prerequisites**: - Hi3403 booted via [quickstart](../get-started/quickstart.md)
- A MIPI camera module attached (IMX415 / IMX385 / SC4210, etc.)
- Phone or laptop on the same LAN as the board ## High-level flow ```mermaid
flowchart LR sensor[MIPI Sensor] --> VI[VI<br>video input] VI --> ISP[ISP<br>image processing] ISP --> VPSS[VPSS<br>scale / format] VPSS --> VENC[VENC<br>H.264 encode] VENC --> bitstream[H.264 bitstream] bitstream -.RTSP push.-> Client[VLC<br>phone / laptop]
``` ## Step 1 — Verify MPP is loaded The `hi3403-build` image runs `topeet-start.sh` on first boot to
`insmod` the MPP modules. Check: ``` bash
lsmod | grep -E 'sys_|isp|venc|vi_|vo_'
``` You should see a set of `ot_*` / `Hi3403V100_*` modules. If empty, run the
loader by hand: ``` bash
cd /ko
sudo bash load_Hi3403V100_ubuntu -i
``` ## Step 2 — Cross-build a sample (optional) Pegasus SDK ships sample source code. **On the PC host**, cross-compile: ``` bash
# In your SDK checkout (set OSDRV_CROSS / toolchain per the README first)
cd pegasus/platform/Hi3403V100_gcc/smp/a55_linux/mpp/sample/ # What samples are there?
ls
# audio cipher common composite dis fisheye gfbg hdmi
# hnr host_uvc hy_s0603 pqtool region snap ... # Pick one that demonstrates capture + encode (the exact name varies
# by SDK version — `composite` is closest to a full IPC pipeline)
make -C composite
``` The build produces `mpp/sample/composite/sample_composite` (or similar
— check the sample's own README). Copy it to the board: ``` bash
scp sample_composite hi@<board-IP>:~/
``` ## Step 3 — Run on the board SSH in: ``` bash
ssh hi@<board-IP>
chmod +x sample_composite
sudo ./sample_composite # interactive menu by default
``` Pick sensor type, resolution, bitrate from the prompts. The sample
starts a VI → ISP → VPSS → VENC pipeline and writes the H.264 bitstream
to a `.h264` file in the current directory, or pushes RTSP — depending
on what the sample supports. !!! tip "Use hnr / snap / dis for focused samples" The Pegasus SDK ships a directory per capability: - `hnr` — Heterogeneous Noise Reduction + encode - `snap` — snapshot + JPEG encode - `dis` — digital image stabilization + encode - `composite` — multi-channel pipelines (closest to a full IPC) Read the one nearest to your goal — much easier than starting from scratch. ## Step 4 — Push RTSP for VLC The Pegasus SDK does not include an RTSP server. Push the H.264
bitstream out using `live555` or `mediamtx`. The fastest way is the
`mediamtx` Go single-binary: ``` bash
# On the board
wget https:/github.com/bluenviron/mediamtx/releases/latest/download/mediamtx_linux_arm64.tar.gz
tar -xzf mediamtx_linux_arm64.tar.gz
./mediamtx & # Once your sample is producing output.h264, push to mediamtx
ffmpeg -re -i output.h264 -c copy -f rtsp rtsp:/localhost:8554/live
``` In VLC on your phone or laptop: ```
rtsp:/<board-IP>:8554/live
``` 200–500 ms latency is normal (`-re` reads at 1× realtime; remove for
lower latency at the cost of dropped frames). ## Step 5 — Roll your own: drive MPP API directly Skipping the sample, the core call sequence is: ``` c
#include "ot_common.h"
#include "ot_common_vi.h"
#include "ot_common_venc.h"
#include "ss_mpi_sys.h"
#include "ss_mpi_vi.h"
#include "ss_mpi_venc.h" int main(void) { / 1. Init MMZ memory pool ss_mpi_sys_init; / 2. Create VI pipe + chn (frames in from sensor) ot_vi_pipe_attr pipe_attr = { /* ... fill per your sensor */ }; ss_mpi_vi_create_pipe(0, &pipe_attr); ss_mpi_vi_set_chn_attr(0, 0, &chn_attr); ss_mpi_vi_enable_chn(0, 0); / 3. Create VENC chn (H.264 encoder) ot_venc_chn_attr venc_attr = { .venc_attr = { .type = OT_PT_H264, .pic_width = 1920, .pic_height = 1080, /* ... */ }, .rc_attr = { .rc_mode = OT_VENC_RC_MODE_H264_CBR, /* ... */ }, }; ss_mpi_venc_create_chn(0, &venc_attr); / 4. Bind VI output → VENC input ot_mpp_chn vi_chn = { OT_ID_VI, 0, 0 }; ot_mpp_chn venc_chn = { OT_ID_VENC, 0, 0 }; ss_mpi_sys_bind(&vi_chn, &venc_chn); / 5. Start the receiver ot_venc_recv_pic_param recv = { .recv_pic_num = -1 }; ss_mpi_venc_start_recv_frame(0, &recv); / 6. Pull bitstream (ideally on a separate thread that pushes RTSP) ot_venc_stream stream; while (running) { ss_mpi_venc_get_stream(0, &stream, -1); / → push to RTSP / write to file / ... ss_mpi_venc_release_stream(0, &stream); } /* cleanup ... */ return 0;
}
``` A complete buildable example lives in
`pegasus/platform/Hi3403V100_gcc/smp/a55_linux/mpp/sample/composite/`. ## Tuning — common issues | Symptom | Try |
|---|---|
| **Tinted picture** | Run [ISP color tuning](isp-color-tuning.md) |
| **High latency** | Switch VENC to `OT_VENC_RC_MODE_H264_VBR`, GOP=15 |
| **Bitrate too high** | Lower `rc_attr.target_bitrate` |
| **Client CPU pegged** | Use a hardware-decoded player (VLC defaults to software) |
| **Sensor not detected** | See [Sensor debugging guide](../multimedia/isp/sensor/index.md) | ## Next <div class="grid cards" markdown> - :material-brain:{ .lg .middle } __Add AI inference to the pipeline__ --- Plug an SVP inference stage in front of VENC, draw boxes, then encode. [:octicons-arrow-right-24: First SVP inference](svp-first-inference.md) - :material-bookshelf:{ .lg .middle } __MPP video-input reference__ --- [:octicons-arrow-right-24: MPP 03 · Video Input](../multimedia/mpp/03-VideoInput.md) </div>
