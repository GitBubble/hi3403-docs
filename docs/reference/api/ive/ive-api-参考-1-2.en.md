---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/IVE API Reference/IVE API Reference (1-2).md
--- # Preface
**Overview<a name="section4537382116410"></a>** This document is written for programmers developing recognition and analysis solutions using the IVE co-processor of the media processing chip. It is intended to provide various reference information supported by the IVE co-processor during development, including APIs, header files, error codes, Proc information, etc. > ![](public_sys-resources/icon-note.gif) **Note:** > Unless otherwise specified in this document, the content for and Hi3403V100 is identical. **Product Version<a name="section155321452151615"></a>** The product versions corresponding to this document are as follows. <a name="table10537205211163"></a>
<table><thead align="left"><tr id="row16570155221618"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p6570452161616"><a name="p6570452161616"></a><a name="p6570452161616"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p1157017526160"><a name="p1157017526160"></a><a name="p1157017526160"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row105711852151613"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p125711852121615"><a name="p125711852121615"></a><a name="p125711852121615"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p1557185217161"><a name="p1557185217161"></a><a name="p1557185217161"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Target Audience<a name="section4378592816410"></a>** This document (guide) is primarily intended for the following engineers: - Technical support engineers
- Software development engineers **Symbol Conventions<a name="section133020216410"></a>** The following symbols may appear in this document, with their meanings described below. <a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002474560250.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>Indicates a high-risk hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Change History<a name="section04531529133911"></a>** <a name="table203mcpsimp"></a>
<table><thead align="left"><tr id="row208mcpsimp"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.1.4.1.1"><p id="p210mcpsimp"><a name="p210mcpsimp"></a><a name="p210mcpsimp"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="22.919999999999998%" id="mcps1.1.4.1.2"><p id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a>Date</p>
</th>
<th class="cellrowborder" valign="top" width="59.85%" id="mcps1.1.4.1.3"><p id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.1.4.1.1 "><p id="p1027mcpsimp"><a name="p1027mcpsimp"></a><a name="p1027mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="22.919999999999998%" headers="mcps1.1.4.1.2 "><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>2024-12-27</p>
</td>
<td class="cellrowborder" valign="top" width="59.85%" headers="mcps1.1.4.1.3 "><p id="p1031mcpsimp"><a name="p1031mcpsimp"></a><a name="p1031mcpsimp"></a>First release.</p>
</td>
</tr>
</tbody>
</table> # Overview
## Overview<a name="ZH-CN_TOPIC_0000002470931328"></a> IVE (Identification Video Engine) is a hardware acceleration module in the media processing chip recognition and analysis system. Users developing recognition and analysis solutions based on IVE can accelerate recognition and analysis while reducing CPU usage. The operators currently provided by IVE can support the development of video diagnosis, perimeter prevention, and other recognition and analysis solutions. ## Function Description<a name="ZH-CN_TOPIC_0000002471091280"></a> ### Important Concepts<a name="ZH-CN_TOPIC_0000002503971263"></a> - Handle: When a user calls an operator to create a task, the system assigns a handle to each task to identify different tasks. - Immediate return flag is_instant: After creating a task, if the user wants to be notified promptly when the task is completed, set is_instant to TD_TRUE when creating the task. Otherwise, if the user does not care whether the task is completed, it is recommended to set is_instant to TD_FALSE, allowing chained execution with subsequent tasks, reducing interrupt count and improving performance. - Query: The user calls ss_mpi_ive_query with the handle returned by the system to check whether the corresponding operator task is completed. - Timely cache flush: The IVE hardware can only obtain data from DDR. If the access space is cacheable and the CPU has previously accessed it when calling an IVE task, to prevent IVE input/output data from being interfered with by the CPU cache, the user needs to call the ss_mpi_sys_mmz_flush_cache interface to flush the cache (see the MPP Media Processing Software Vx.y Development Reference for details), flushing data from cache to DDR for IVE use. - Stride: A measure consistent with the width of an image or two-dimensional data, as shown in [Figure 1](#fig1615616519207). - ot_svp_img image data stride: represents the number of units calculated as "pixels" per row of the image. The pixel bit width can be 8bit, 16bit, etc. - ot_svp_data two-dimensional data stride: represents the number of bytes per row of two-dimensional data. ot_svp_img can be viewed as an image where one "pixel" is represented by 8bit, so stride is uniformly expressed as the number of units calculated as "pixels" per row of the image or two-dimensional data. **Figure 1** Stride Diagram<a name="fig1615616519207"></a> ![](figures/Stride Diagram "Stride Diagram") - Alignment: To quickly access memory start addresses or cross-row data, the hardware requires that memory addresses or memory strides must be multiples of the alignment coefficient. - Data memory start address alignment: Current IVE operators have requirements for 1-byte alignment, 2-byte alignment, and 16-byte alignment for their inputs and outputs. Refer to the parameter requirements in each operator's API reference. - Stride alignment: For two-dimensional generalized images, two-dimensional single-component data, and one-dimensional array data, the stride must satisfy 16 "pixel" alignment. > ![](public_sys-resources/icon-notice.gif) **Note:** > When using DDR4, to improve memory access efficiency, it is recommended to use 256-byte alignment for the start address and odd multiples of 256 "pixels" for stride alignment. If using a 64-bit operating system, the MMZ address used must be within a 4GB space, otherwise an exception will occur. - Input/Output Data Types: - Two-dimensional generalized image data: ot_svp_img, ot_svp_src_img, ot_svp_dst_img. Image types refer to ot_svp_img_type. - Two-dimensional single-component data: ot_svp_data, two-dimensional data in bytes, mainly used for DMA, etc. - One-dimensional data: ot_svp_mem_info, ot_svp_src_mem_info, ot_svp_dst_mem_info. # API Reference<a name="ZH-CN_TOPIC_0000002470931302"></a>The IVE module provides basic interfaces for creating tasks and querying tasks. This functional module provides the following MPIs: - [ss_mpi_ive_dma](#ZH-CN_TOPIC_0000002504091099): Create a direct memory access task.
- [ss_mpi_ive_filter](#ZH-CN_TOPIC_0000002470931284): Create a 5x5 template filter task.
- [ss_mpi_ive_csc](#ZH-CN_TOPIC_0000002470931294): Create a color space conversion task.
- [ss_mpi_ive_filter_and_csc](#ZH-CN_TOPIC_0000002470931218): Create a composite filter and color space conversion task.
- [ss_mpi_ive_sobel](#ZH-CN_TOPIC_0000002471091284): Create a 5x5 template sobel-like gradient computation task.
- [ss_mpi_ive_mag_and_ang](#ZH-CN_TOPIC_0000002470931308): Create a 5x5 template gradient magnitude and angle computation task.
- [ss_mpi_ive_dilate](#ZH-CN_TOPIC_0000002503971205): Create a dilation task.
- [ss_mpi_ive_erode](#ZH-CN_TOPIC_0000002503971269): Create an erosion task.
- [ss_mpi_ive_threshold](#ZH-CN_TOPIC_0000002471091326): Create an image binarization task.
- [ss_mpi_ive_and](#ZH-CN_TOPIC_0000002504091087): Create a binary image AND task.
- [ss_mpi_ive_sub](#ZH-CN_TOPIC_0000002503971163): Create a grayscale image subtraction task.
- [ss_mpi_ive_or](#ZH-CN_TOPIC_0000002471091296): Create a binary image OR task.
- [ss_mpi_ive_integ](#ZH-CN_TOPIC_0000002470931322): Create an integral image statistics task.
- [ss_mpi_ive_hist](#ZH-CN_TOPIC_0000002504091123): Create a histogram statistics task.
- [ss_mpi_ive_threshold_s16](#ZH-CN_TOPIC_0000002470931220): Create an s16 to 8-bit data thresholding task.
- [ss_mpi_ive_threshold_u16](#ZH-CN_TOPIC_0000002470931242): Create a u16 to u8 data thresholding task.
- [ss_mpi_ive_16bit_to_8bit](#ZH-CN_TOPIC_0000002471091216): Create a 16-bit to 8-bit linear conversion task.
- [ss_mpi_ive_order_stats_filter](#ZH-CN_TOPIC_0000002504091093): Create a 3x3 template order statistics filter task.
- [ss_mpi_ive_map](#ZH-CN_TOPIC_0000002470931234): Create a Map (mapping u8->u8 / u8->u16 / u8->s16 assignment) task.
- [ss_mpi_ive_equalize_hist](#ZH-CN_TOPIC_0000002471091322): Create a grayscale image histogram equalization task.
- [ss_mpi_ive_add](#ZH-CN_TOPIC_0000002504091171): Create a weighted addition of two grayscale images task.
- [ss_mpi_ive_xor](#ZH-CN_TOPIC_0000002504091203): Create a binary image XOR task.
- [ss_mpi_ive_ncc](#ZH-CN_TOPIC_0000002503971167): Create a normalized cross-correlation computation for two same-resolution images task.
- [ss_mpi_ive_ccl](#ZH-CN_TOPIC_0000002504091151): Create a connected component labeling for binary images task.
- [ss_mpi_ive_gmm](#ZH-CN_TOPIC_0000002503971147): Create a GMM background modeling task.
- [ss_mpi_ive_gmm2](#ZH-CN_TOPIC_0000002504091155): Create a GMM2 background modeling task.
- [ss_mpi_ive_canny_hys_edge](#ZH-CN_TOPIC_0000002503971215): Create a Canny strong/weak edge extraction for grayscale images task.
- [ss_mpi_ive_canny_edge](#ZH-CN_TOPIC_0000002470931286): Create the second half of Canny edge extraction: connect edge points to form a Canny edge map.
- [ss_mpi_ive_lbp](#ZH-CN_TOPIC_0000002503971201): Create an LBP computation task.
- [ss_mpi_ive_norm_grad](#ZH-CN_TOPIC_0000002503971195): Create a normalized gradient computation task, with all gradient components normalized to s8.
- [ss_mpi_ive_lk_optical_flow_pyr](#ZH-CN_TOPIC_0000002504091135): Create a multi-layer pyramid Lucas-Kanade optical flow computation task.
- [ss_mpi_ive_st_cand_corner](#ZH-CN_TOPIC_0000002471091320): Create the first half of Shi-Tomasi-like corner detection: compute candidate corners.
- [ss_mpi_ive_st_corner](#ZH-CN_TOPIC_0000002470931280): Create the second half of Shi-Tomasi-like corner detection: select corners according to rules.
- [ss_mpi_ive_sad](#ZH-CN_TOPIC_0000002471091328): Compute 4x4/8x8/16x16 block-based 16-bit/8-bit SAD images and threshold the SAD output.
- [ss_mpi_ive_resize](#ZH-CN_TOPIC_0000002503971235): Create an image resize task.
