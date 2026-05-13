---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/DDR 小型化指南/DDR 小型化指南.md
--- # Preface
**Overview<a name="section4537382116410"></a>** This document is written for programmers developing miniaturization, with the aim of introducing Linux development, tailoring, optimization, and usage precautions on a single board. >![](public_sys-resources/icon-note.gif) **Note:**
>Unless otherwise specified, the content for is identical to that of Hi3403V100. **Product Version<a name="section25718263411"></a>** The product versions corresponding to this document are as follows. <a name="table1233317181949"></a>
<table><thead align="left"><tr id="row103955189411"><th class="cellrowborder" valign="top" width="31.759999999999998%" id="mcps1.1.3.1.1"><p id="p13395161815412"><a name="p13395161815412"></a><a name="p13395161815412"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68.24%" id="mcps1.1.3.1.2"><p id="p33951518144"><a name="p33951518144"></a><a name="p33951518144"></a>Product Version</p>
</th>
</tr>
</thead>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p93951718242"><a name="p93951718242"></a><a name="p93951718242"></a>V100</p>
</td>
</tr>
<tr id="row188062423511"><td class="cellrowborder" valign="top" width="31.759999999999998%" headers="mcps1.1.3.1.1 "><p id="p208065421519"><a name="p208065421519"></a><a name="p208065421519"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p168061342157"><a name="p168061342157"></a><a name="p168061342157"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68.24%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Intended Audience<a name="section51625422047"></a>** This document (guide) is mainly applicable to the following engineers: - Technical Support Engineer
- Software Development Engineer **Revision History<a name="section2467512116410"></a>** <a name="table126443203200"></a>
<table><thead align="left"><tr id="row264516207203"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p146456203200"><a name="p146456203200"></a><a name="p146456203200"></a><strong id="b8645172022010"><a name="b8645172022010"></a><a name="b8645172022010"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p364512062019"><a name="p364512062019"></a><a name="p364512062019"></a><strong id="b1464512200200"><a name="b1464512200200"></a><a name="b1464512200200"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p664522018206"><a name="p664522018206"></a><a name="p664522018206"></a><strong id="b156451420152010"><a name="b156451420152010"></a><a name="b156451420152010"></a>Revision Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row56451520182017"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p1564572014209"><a name="p1564572014209"></a><a name="p1564572014209"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p126451920132014"><a name="p126451920132014"></a><a name="p126451920132014"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1664582017209"><a name="p1664582017209"></a><a name="p1664582017209"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table> # Overview
DDR miniaturization can be approached from multiple directions: uboot, kernel, filesys, SDK, and APP can all be optimized to a certain extent in memory usage. This document mainly provides a brief explanation of miniaturization for SDK and APP. The SDK based on currently supports running both Linux and Lite OS dual systems or a single Linux system. If the business scenario only requires running a single Linux system, please refer to Section 3.2 of the "Memory Layout Adjustment Guide" to trim MMZ occupancy related to the liteos system. This document is based on the Linux and Lite OS dual-system configuration by default. The system miniaturization of is implemented on the DEMO board, using 2GB DDR memory as an example. **Figure 1** Linux System Memory Allocation Diagram on DEMO Board (for reference only)<a name="fig58516719710"></a>
![](figures/DEMO Linux System Memoryallocategraph（Only Reference）.png "DEMO Linux System Memoryallocategraph（Only Reference）")") For MMZ memory usage data in typical business scenarios, please refer to the " Memory Usage Statistics Report". Additionally, specific memory usage for customer applications needs to be analyzed in conjunction with specific scenarios. The following sections describe the MMZ memory usage of each module and optimization methods for miniaturization. # MMZ Occupancy of Main Modules During Operation
In general business scenarios, MMZ occupancy often accounts for a large portion of memory consumption. This chapter mainly describes the MMZ occupancy of several major modules during operation in typical business scenarios. ## VI<a name="ZH-CN_TOPIC_0000002424361046"></a> In the VI capture state, a maximum of three video frame V Bs will be occupied. One is used for current frame capture, one is prepared for the next frame capture, and one is in the rotation flow (mainly occupied by downstream modules). MMZ occupancy in Hi3403V100: - vi\(%d\)\_model\_%d: Each pipe needs to occupy two template MMZ memories of a certain size. The size is related to the channel width. When the width is less than or equal to 4096, the size is 16KB.
- vi\(%d\)\_lmf: Occupies MMZ memory when LMF function is enabled on each pipe, used to store LMF coefficients, fixed at 4K.
- vi\(%d\)\_bnr\_mot: Motion buffer memory required when Bayer NR function is enabled on each pipe. Size is determined by the width and height of the processed image.
- vi\(0\)\_bnr\_rnt: RNT memory required when Bayer NR function is enabled on each pipe. Size is determined by the width and height of the processed image. When offline, the count is set by ss\_mpi\_vi\_set\_pipe\_bnr\_buf\_num.
- Interface setting, default is 40 blocks.
- vi\(0\)\_bnr\_ref%d: Temporal reference memory required when Bayer NR function is enabled on each pipe. Size is determined by the width and height of the processed image. ## VDEC<a name="ZH-CN_TOPIC_0000002424201210"></a> VDEC MMZ occupancy is divided into buffer occupancy, rotation occupancy, and device occupancy. **Buffer Occupancy<a name="section389732110912"></a>** - vfmw\(%d\)\_usd\_buf: User data buffer memory, allocated based on the size specified by the user.
- vdec\(%d\)\_adp\_ref: Used to store vb-related information for the channel.
- vdec\(%d\)\_adp\_event: Used to store event information generated during decoding.
- vfmw\(%d\)\_shr\_img: Used to store information related to decoded images.
- vdec\_adp\_proc: Used to store proc information generated by vdec on the MDC side.
- vfmw\_mdc\_shr: Used to store proc information generated by vfmw on the MDC side. **Device Occupancy<a name="section172822554102"></a>** - vfmw\(%d\)\_seg\_buf: Memory for storing data after SCD stream slicing. Related to resolution, independent of protocol.
- vfmw\_scd\_msg: Memory required for SCD logic operation, fixed at 44KB.
- vfmw\_mdma\_msg: Memory required for VDH logic operation, fixed at 44KB. **Rotation Occupancy<a name="section32020161117"></a>** - vdec\(%d\)\_pic\_vb: Both the VB size and count are configured by the user. In private VB mode, the size is determined by frame\_buf\_size in the user-configured channel attributes, and the count is determined by frame\_buf\_cnt in the user-configured channel attributes.
- vdec\(%d\)\_tmv\_vb: Both the VB size and count are configured by the user. In private VB mode, the size is determined by tmv\_buf\_size in the user-configured channel attributes, and the count is "reference frames + 1", where the reference frame count is determined by ref\_frame\_num in the user-configured channel attributes. ## VPSS<a name="ZH-CN_TOPIC_0000002457879933"></a> - vb\_pool: The Group occupies two VBs (sent from the upstream module: current working VB + Backup frame). Each enabled channel will obtain a channel-sized VB (in Auto mode for the channel, it is obtained for the downstream module). After hardware processing, it is sent to the bound downstream module. If rotation/secondary scaling is needed, intermediate temporary V Bs (public V Bs) also need to be allocated.
- vpss\(%d\)\_src: Each group needs to occupy luminance and MMZ memory resources, approximately 4K.
- vpss\(%d\)\_dci: Occupies MMZ memory when DCI function is enabled on each group, approximately 4K.
- vpss\(%d\)\_model: Each group needs to occupy a certain size of template MMZ memory. The size is related to split\_node\_num in the module parameters and the max\_width of the group. The larger split\_node\_num and max\_width are, the larger the occupancy.
- vpss\(%d\)\_lmf: Occupies MMZ memory when LMF function is enabled on each group, used to store LMF coefficients, fixed at 4K.
- vpss\(%d\)\_rgn\_luma: Occupies MMZ memory when the channel luminance sum function is enabled on each group, used to store luminance statistical information, fixed at 4K.
- vmallocinfo: Each group context needs to occupy a certain amount of OS memory. The total size is related to the number of groups; more groups mean larger occupancy. ## VGS<a name="ZH-CN_TOPIC_0000002457879973"></a> The VGS module allocates fixed MMZ memory based on the number of jobs, nodes, and tasks. - vmallocinfo: Occupies OS memory based on the number of jobs, tasks, and context. More items mean larger occupancy.
- vgs\_node\_buf: Occupies a certain amount of MMZ memory based on the number of nodes. More nodes mean larger occupancy. ## VENC<a name="ZH-CN_TOPIC_0000002457879945"></a> - Hardware-related: vedu\_hal\_\(%d\): Memory required by the hardware, related to the number of I Ps. - Channel-related memory (using H264 as an example; H265 uses the h265e prefix): - h264e\(%d\)\_node: Register node configuration memory, one per channel. - h264e\(%d\)\_str0: Stream buffer, one per channel. - h264e\(%d\)\_rcn\(%d\): Reference frame reconstruction frame memory. The count is related to the number of encoding reference frames. - h264e\(%d\)\_info\(%d\): Reference frame reconstruction frame information memory. The count is related to the number of encoding reference frames. - h264e\(%d\)\_deblur: After enabling deblur via ss\_mpi\_venc\_set\_deblur, corresponding deblur processing memory is required. - h264e\(%d\)\_md: After enabling MD detection via ss\_mpi\_venc\_set\_md, corresponding MD detection memory is required. - venc\(%d\)\_svc: After enabling SVC via ss\_mpi\_venc\_enable\_svc, corresponding SVC memory is required. - jpege\(%d\)\_stm: jpege stream buffer, one per channel. - jpege\(%d\)\_roi\_map: When enabling roi\_map via ss\_mpi\_venc\_set\_jpeg\_roi\_attr, memory is allocated for the jpege roi\_map. - vmallocinfo: Channel context memory for each channel; User Data data; bitrate control related memory. ## VO<a name="ZH-CN_TOPIC_0000002424201194"></a> VO MMZ occupancy is divided into coefficient MMZ occupancy, luminance sum MMZ occupancy, and VB rotation MMZ occupancy. - Coefficient MMZ occupancy: vo\_coef\_buf: Memory for storing write-back scaling coefficients (128KB) and multi-region configuration coefficients (8KB), totaling 136KB. If the chip does not support write-back scaling, the corresponding coefficients will not be allocated. One multi-region occupies 4KB of memory, and two multi-regions occupy 8KB. - Luminance sum MMZ occupancy: vo\(%d,%d\)\_luma: MMZ memory dynamically allocated when the VO module obtains the video layer and channel luminance sum. A specific channel always occupies 4KB. If the chip does not support obtaining the luminance sum, this memory is not allocated. - VB rotation MMZ occupancy: vo\(%d\)\_disp\_buf: Both the VB size and count are configured by the user. The size is determined by img\_size in the user-configured video layer attribute, and the count is determined by display\_buf\_len in the user-configured video layer attribute. In Single mode, VO occupies 3 private V Bs for display rotation. In Multi mode, if the upstream VPSS is in auto mode, VO occupies 4 private V Bs for display rotation; if the upstream is in User mode, VO may not allocate V Bs, instead occupying V Bs sent from the upstream module and releasing them after display. ## GFBG<a name="ZH-CN_TOPIC_0000002457839817"></a> When loading the ko, the user specifies the display buffer size for the graphics layer and mouse layer. All supported layers can be specified, and the layer ID must match the vram ID. For example: `insmod gfbg.ko video="gfbg:vram0_size:32400,vram1_size:32400,vram2_size:256,vram3_size:4052"`. - vram0\_size: Corresponds to the gfbg0 graphics layer memory size, in KB, mmz name= gfbg\_layer0.
- vram1\_size: Corresponds to the gfbg1 graphics layer memory size, in KB, mmz name= gfbg\_layer1.
- vram2\_size: Corresponds to the gfbg2 graphics layer memory size, in KB, mmz name= gfbg\_layer2.
- vram3\_size: Corresponds to the gfbg3 graphics layer memory size, in KB, mmz name= gfbg\_layer3. ## AUDIO<a name="ZH-CN_TOPIC_0000002424201218"></a> **AI<a name="section1478714716237"></a>** - ai\(%d\)\_frm: AI channel buffer allocated based on chn\_cnt, frame\_num, and point\_num\_per\_frame.
- ai\(%d\)\_dma: AI DMA buffer allocated based on chn\_cnt and point\_num\_per\_frame. **AO<a name="section20436157192318"></a>** - ao\(%d\)\_dma&frm: AO DMA buffer and channel buffer allocated based on chn\_cnt, frame\_num, and point\_num\_per\_frame.
- ao\(%d, %d\)\_cir: Audio frame buffer allocated based on frame\_num and point\_num\_per\_frame. **AENC<a name="section339816212241"></a>** - aenc\(%d\)\_strm: Stream buffer allocated based on buf\_size.
- aenc\(%d\)\_cir: Ring buffer allocated based on the number of encoding channels. ## REGION<a name="ZH-CN_TOPIC_0000002457879941"></a> **Region Information Context Nodes<a name="section15813751132413"></a>** Removing unnecessary modules can reduce memory usage, for example: - 1024 region information context nodes allocated when loading the module, consuming 4KB of OS memory. Region information context is dynamically allocated when creating regions.
- If it is an overlay or overlayex type region, ping-pong buffers will also be allocated for storing bitmap data.
- rgn\_pin\_pon\_\(%d\): The size of the ping-pong buffer is determined by the width, height, canvas\_num, and color format set by the user, occupying MMZ memory. **Channel Management Information Nodes<a name="section16571145662413"></a>** When other modules call REGION functions to register information with REGION, they are dynamically allocated, occupying MMZ memory. ## TDE<a name="ZH-CN_TOPIC_0000002457839825"></a> The channel uses MMZ memory with a fixed total size: \(OT\_TDE\_CMD\_NUM\) \* 64 + \(OT\_TDE\_JOB\_NUM\) \* 96 + \(OT\_TDE\_NODE\_NUM\) \* 256 + \(OT\_TDE\_FILTER\_NUM\) \* 1024. ## SVP<a name="ZH-CN_TOPIC_0000002457839801"></a> **SVP\_NNN<a name="section14631148142915"></a>** SVP\_NNN memory usage is divided into MMZ memory and OS memory. MMZ memory includes task nodes and inference content memory. - Node MMZ occupancy: Kernel-mode node size, default 100KB; User-mode node size, default 80KB. - Inference MMZ occupancy (Resnet50 Batch 1 typical scenario): OM memory size, 50828KB; Input/output data memory size, 8596KB; Model information memory size, 12KB. - OS memory occupancy: OS memory mainly includes two parts: static global variable memory, approximately 5.6KB; dynamic memory, approximately 0.594KB. >![](public_sys-resources/icon-note.gif) **Note:** **IVE<a name="section8594155332913"></a>** IVE memory usage is divided into MMZ memory and OS memory. MMZ memory includes the task list and auxiliary memory. - Task list MMZ occupancy: ive\_queue: IVE task list size, default 212KB. - Auxiliary MMZ memory occupancy: - ive\_tmp\_node: Temporary node needed for IVE multi-operator combined tasks, fixed at 4KB. - Md\_proc: MMZ memory needed for MD proc information, fixed at 8KB. - ive\_resize\_param: Auxiliary memory needed for resize operator calculation, fixed at 9264 bytes. - ive\_yuv\_to\_hsv\_table: Auxiliary memory for storing IVE color space conversion table, fixed at 2048 bytes. - ive\_yuv\_to\_lab\_table: Auxiliary memory for storing IVE color space conversion table, fixed at 6656 bytes. - OS memory occupancy: IVE OS memory mainly consists of memory allocated by kmalloc and static global variable memory. OS memory plus MMZ memory does not exceed 235KB. **KCF<a name="section1226215919298"></a>** KCF memory usage is divided into MMZ memory and OS memory. MMZ memory includes the task list and auxiliary memory. - Task list MMZ occupancy: kcf\_queue: KCF task list size, fixed at 106688 bytes. - Auxiliary MMZ memory occupancy: kcf\_param: Auxiliary memory needed for KCF calculation, fixed at 45328 bytes. - OS memory occupancy: KCF OS memory mainly consists of memory allocated by kmalloc and static global variable memory. OS memory plus MMZ memory does not exceed 150KB. **MAU<a name="section4581452303"></a>** MAU memory is mainly divided into MMZ memory and OS memory. MMZ memory is the task list memory. - Task list occupancy: svp\_mau\_queue: MAU task list size, default 160KB. - OS memory occupancy: MAU OS memory mainly consists of mem\_info linked list memory using OS memory (40 \* mau\_max\_mem\_info\_num bytes), and memory used by mau context static global variables. OS memory plus MMZ memory totals no more than 163KB. ## PCIV<a name="ZH-CN_TOPIC_0000002457839793"></a> PCIV MMZ occupancy is divided into pcie-mcc message pool occupancy, window occupancy, and VB rotation occupancy. - pcie-mcc message pool occupancy: Used for pcie-mcc message communication. The location and size are specified when loading the slave chip pcie driver, fixed at 1M. - Window occupancy: When the master chip initiates a DMA operation, the slave chip space can only be read and written through the window. When loading the osal driver, the MMZ name is specified as window, the default size is 7M, and the starting position immediately follows the pcie-mcc message pool (pcie-mcc message pool + window continuous space has a maximum of 8M). - VB rotation occupancy: - Master chip rotation VB: VB size and count are configured by the user. The size must be sufficient to receive a complete image, generally determined by the image width, height, format attributes, etc., in the channel attributes. Allocation and release are controlled by user-called interfaces. When receiving slave chip images, the rotation VB is passed downstream, and whether to accept the next rotation is determined by checking the downstream occupancy status. - Slave chip rotation VB: The slave chip receives the upstream image. If VPSS uses auto mode to send frames, PCIV obtains the VB; in other modes, the VB is occupied when receiving the image. In pass-through mode (PCIV transparent transmission), the VB is released after DMA transmission completes. In non-pass-through mode (OSD, scaling, etc.), VGS needs to obtain a write VB and release the received image VB. After DMA transmission completes, the VGS write VB is released. ## GDC<a name="ZH-CN_TOPIC_0000002424361082"></a> The GDC module allocates fixed MMZ memory based on the number of jobs, nodes, and tasks. - vmallocinfo: Occupies OS memory based on job count, task count, and context. More items mean larger occupancy.
- gdc\_node\_buf: Occupies a certain amount of MMZ memory based on the number of nodes. More nodes mean larger occupancy.
- gdc\_int\_pole\_coef: MMZ memory needed for storing interpolation coefficients, fixed at 4KB. ## CIPHER<a name="ZH-CN_TOPIC_0000002457879957"></a> Fixed size (the length of MMZ memory allocated is determined internally by the driver): - Hash initialization: Allocates memory for the SHA node linked list, fixed at 28 \* 255 \* 1 = 7KB; 255 is the maximum depth of the linked list, with a minimum depth of 2. HASH message DMA memory: logic only recognizes physical memory, so a maximum of 64KB of physical memory needs to be allocated to store hash messages.
- Cipher driver module initialization: Allocates memory for the CIPHER node linked list, entry list size (20KB), used to store the CCM GCM aad physical memory padding buffer (2KB) for each of the 16 channels, fixed at 22KB. Non-fixed size (the length of MMZ memory allocated is passed in by the user-layer interface): cipher encryption/decryption: Depends on the byte\_len parameter of the virtual address/physical address encryption/decryption interface. ## DCC<a name="ZH-CN_TOPIC_0000002424361058"></a> dcc\_msg\_buf: Used on for dual-core communication tasks. ## VDA<a name="ZH-CN_TOPIC_0000002457879965"></a> vda\(%d\): Memory related to internal channel calculation result storage, mainly including SAD result memory, RGN motion region information memory, and background. ## ISP<a name="ZH-CN_TOPIC_0000002457839813"></a> - isp\[%d\].vreg\[%d\]: External virtual register memory.
- isp\[%d\].proc: User-mode algorithm proc debug information.
- isp\[%d\].trans: dng, dcf, colorgamut and other information memory.
- isp\[%d\].ldci: ldci algorithm memory.
- isp\[%d\].clut: clut algorithm memory.
- be\_lut\_stt\[%d\]: be lut information memory.
- pre\_on\_lut\_stt\[%d\]: Online channel ADVANCED mode be lut information memory.
- isp\[%d\].stat: Statistical information (FE, BE) memory.
- isp\[%d\].fe\_stat: FE statistical information memory.
- isp\[%d\].wdr: wdr algorithm memory.
- isp\[%d\].drc: drc algorithm memory.
- isp\[%d\].be\_cfg: Offline channel be config buffer.
- isp\[%d\].be\_stt\_on: Online channel be statistical information memory.
- isp\[%d\].fe\_stt: fe statistical information memory.
- isp\[%d\].be\_stt: Offline channel be statistical information memory.
- isp\[%d\].stit\_fe: Stitching channel fe statistical information memory.
- isp\[%d\].stit\_be: Stitching channel be statistical information memory. ## HNR<a name="ZH-CN_TOPIC_0000002424201214"></a> - hnr\_pqp\_buf\[%d\]: HNR model file memory.
- hnr\_ping\_pong\_buf: Working memory used for HNR model inference. When the HNR function reference frame mode is enabled, 4-6 additional video frame V Bs are needed. In non-reference frame mode, 1 additional video frame VB is needed. # Module Memory Optimization Configurations
## VB<a name="ZH-CN_TOPIC_0000002424201202"></a> <a name="table626mcpsimp"></a>
<table><thead align="left"><tr id="row635mcpsimp"><th class="cellrowborder" valign="top" width="10.80897348742352%" id="mcps1.1.7.1.1"><p id="p637mcpsimp"><a name="p637mcpsimp"></a><a name="p637mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="11.197436146450421%" id="mcps1.1.7.1.2"><p id="p639mcpsimp"><a name="p639mcpsimp"></a><a name="p639mcpsimp"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="17.568223754491598%" id="mcps1.1.7.1.3"><p id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="6.798096532970768%" id="mcps1.1.7.1.4"><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="34.26240652617267%" id="mcps1.1.7.1.5"><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="19.364863552491016%" id="mcps1.1.7.1.6"><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row672311199166"><td class="cellrowborder" valign="top" width="10.80897348742352%" headers="mcps1.1.7.1.1 "><p id="p045852610166"><a name="p045852610166"></a><a name="p045852610166"></a>Check if the VB count in vb pools is set too high</p>
</td>
<td class="cellrowborder" valign="top" width="11.197436146450421%" headers="mcps1.1.7.1.2 "><p id="p238171916718"><a name="p238171916718"></a><a name="p238171916718"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.568223754491598%" headers="mcps1.1.7.1.3 "><p id="p9100754101120"><a name="p9100754101120"></a><a name="p9100754101120"></a>If the number of VB blocks in a pool with non-zero mini_free is set too high, you can subtract mini_free.</p>
</td>
<td class="cellrowborder" valign="top" width="6.798096532970768%" headers="mcps1.1.7.1.4 "><p id="p67241519151610"><a name="p67241519151610"></a><a name="p67241519151610"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="34.26240652617267%" headers="mcps1.1.7.1.5 "><p id="p572411981616"><a name="p572411981616"></a><a name="p572411981616"></a>For setting VB count in public VB pool, module VB pool, and User VB pool, refer to the VB-related interfaces in the "System Control" chapter of the "MPP Media Processing Software V5.0 Development Reference".</p>
<p id="p187074211157"><a name="p187074211157"></a><a name="p187074211157"></a>For setting Private VB pool count, find the corresponding parameters in the relevant module interfaces.</p>
</td>
<td class="cellrowborder" valign="top" width="19.364863552491016%" headers="mcps1.1.7.1.6 "><p id="p1372417193163"><a name="p1372417193163"></a><a name="p1372417193163"></a>mini_free: historical minimum remaining VB count</p>
</td>
</tr>
<tr id="row66990531976"><td class="cellrowborder" valign="top" width="10.80897348742352%" headers="mcps1.1.7.1.1 "><p id="p166994531176"><a name="p166994531176"></a><a name="p166994531176"></a>Check if any VB block size is set too large</p>
</td>
<td class="cellrowborder" valign="top" width="11.197436146450421%" headers="mcps1.1.7.1.2 "><p id="p176991153275"><a name="p176991153275"></a><a name="p176991153275"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="17.568223754491598%" headers="mcps1.1.7.1.3 "><p id="p116994536714"><a name="p116994536714"></a><a name="p116994536714"></a>If a VB block with non-zero free_bytes is oversized, you can subtract free_bytes.</p>
</td>
<td class="cellrowborder" valign="top" width="6.798096532970768%" headers="mcps1.1.7.1.4 "><p id="p12699753174"><a name="p12699753174"></a><a name="p12699753174"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="34.26240652617267%" headers="mcps1.1.7.1.5 "><p id="p4276361092"><a name="p4276361092"></a><a name="p4276361092"></a>For setting VB block size in public VB pool, module VB pool, and User VB pool, refer to the VB-related interfaces in the "System Control" chapter of the "MPP Media Processing Software V5.0 FAQ".</p>
<p id="p162712362916"><a name="p162712362916"></a><a name="p162712362916"></a>For setting Private VB pool count, find the corresponding parameters in the relevant module interfaces.</p>
</td>
<td class="cellrowborder" valign="top" width="19.364863552491016%" headers="mcps1.1.7.1.6 "><p id="p869916538718"><a name="p869916538718"></a><a name="p869916538718"></a>free_bytes: real-time remaining bytes in VB block</p>
<p id="p109046282137"><a name="p109046282137"></a><a name="p109046282137"></a>get: the module that obtained the VB block; this information can help determine which module's VB block size is oversized</p>
</td>
</tr>
</tbody>
</table> ## SYS<a name="ZH-CN_TOPIC_0000002457879949"></a> <a name="table626mcpsimp"></a>
<table><thead align="left"><tr id="row635mcpsimp"><th class="cellrowborder" valign="top" width="16.6016601660166%" id="mcps1.1.7.1.1"><p id="p637mcpsimp"><a name="p637mcpsimp"></a><a name="p637mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="16.56165616561656%" id="mcps1.1.7.1.2"><p id="p639mcpsimp"><a name="p639mcpsimp"></a><a name="p639mcpsimp"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="18.55185518551855%" id="mcps1.1.7.1.3"><p id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="5.5205520552055205%" id="mcps1.1.7.1.4"><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="33.913391339133916%" id="mcps1.1.7.1.5"><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="8.85088508850885%" id="mcps1.1.7.1.6"><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row672311199166"><td class="cellrowborder" valign="top" width="16.6016601660166%" headers="mcps1.1.7.1.1 "><p id="p045852610166"><a name="p045852610166"></a><a name="p045852610166"></a>Set scheduling mode to OT_SCHEDULE_QUICK</p>
</td>
<td class="cellrowborder" valign="top" width="16.56165616561656%" headers="mcps1.1.7.1.2 "><p id="p272461951613"><a name="p272461951613"></a><a name="p272461951613"></a>ss_mpi_sys_set_schedule_mode</p>
</td>
<td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.1.7.1.3 "><p id="p472411991616"><a name="p472411991616"></a><a name="p472411991616"></a>Accelerates VB rotation, can reduce VB allocation</p>
</td>
<td class="cellrowborder" valign="top" width="5.5205520552055205%" headers="mcps1.1.7.1.4 "><p id="p67241519151610"><a name="p67241519151610"></a><a name="p67241519151610"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="33.913391339133916%" headers="mcps1.1.7.1.5 "><p id="p572411981616"><a name="p572411981616"></a><a name="p572411981616"></a>For specific operations and precautions, refer to "1.9 Quick schedule" notes in the "MPP Media Processing Software V5.0 FAQ".</p>
</td>
<td class="cellrowborder" valign="top" width="8.85088508850885%" headers="mcps1.1.7.1.6 "><p id="p1372417193163"><a name="p1372417193163"></a><a name="p1372417193163"></a>-</p>
</td>
</tr>
<tr id="row1245111561610"><td class="cellrowborder" valign="top" width="16.6016601660166%" headers="mcps1.1.7.1.1 "><p id="p19934174519167"><a name="p19934174519167"></a><a name="p19934174519167"></a>Disable logmpp_mdc</p>
</td>
<td class="cellrowborder" valign="top" width="16.56165616561656%" headers="mcps1.1.7.1.2 "><p id="p10952769391"><a name="p10952769391"></a><a name="p10952769391"></a>g_mdc_log_enable</p>
</td>
<td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.1.7.1.3 "><p id="p11931645141616"><a name="p11931645141616"></a><a name="p11931645141616"></a>Saves 68K of logmpp_mdc log</p>
</td>
<td class="cellrowborder" valign="top" width="5.5205520552055205%" headers="mcps1.1.7.1.4 "><p id="p15930184513162"><a name="p15930184513162"></a><a name="p15930184513162"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="33.913391339133916%" headers="mcps1.1.7.1.5 "><a name="ul5953174413428"></a><a name="ul5953174413428"></a><ul id="ul5953174413428"><li>Set module parameter g_mdc_log_enable=0 when inserting xx_base.ko</li><li>Supported by </li></ul>
</td>
<td class="cellrowborder" valign="top" width="8.85088508850885%" headers="mcps1.1.7.1.6 "><p id="p1592917457166"><a name="p1592917457166"></a><a name="p1592917457166"></a>-</p>
</td>
</tr>
<tr id="row14135125317368"><td class="cellrowborder" valign="top" width="16.6016601660166%" headers="mcps1.1.7.1.1 "><p id="p8928154571619"><a name="p8928154571619"></a><a name="p8928154571619"></a>Remove MDC-side memory allocation</p>
</td>
<td class="cellrowborder" valign="top" width="16.56165616561656%" headers="mcps1.1.7.1.2 "><p id="p1616120012812"><a name="p1616120012812"></a><a name="p1616120012812"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.55185518551855%" headers="mcps1.1.7.1.3 "><p id="p119414588245"><a name="p119414588245"></a><a name="p119414588245"></a>No need to load: xx_dcc.ko, xx_vdec_adapt.ko</p>
</td>
<td class="cellrowborder" valign="top" width="5.5205520552055205%" headers="mcps1.1.7.1.4 "><p id="p2819188142613"><a name="p2819188142613"></a><a name="p2819188142613"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="33.913391339133916%" headers="mcps1.1.7.1.5 "><a name="ul07781240164419"></a><a name="ul07781240164419"></a><ul id="ul07781240164419"><li>Refer to document "Memory Layout Adjustment Guide"</li><li>ss_mpi_vdec_set_chn_config: set deployment_mode to OT_VDEC_DEPLOYMENT_MODE0</li><li>Supported by </li></ul>
</td>
<td class="cellrowborder" valign="top" width="8.85088508850885%" headers="mcps1.1.7.1.6 "><p id="p179233459165"><a name="p179233459165"></a><a name="p179233459165"></a>-</p>
</td>
</tr>
</tbody>
</table> ## VI<a name="ZH-CN_TOPIC_0000002457879929"></a> <a name="table131881116404"></a>
<table><thead align="left"><tr id="row1118913161008"><th class="cellrowborder" valign="top" width="17.39%" id="mcps1.1.7.1.1"><p id="p171891516307"><a name="p171891516307"></a><a name="p171891516307"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="16.259999999999998%" id="mcps1.1.7.1.2"><p id="p181891616508"><a name="p181891616508"></a><a name="p181891616508"></a>Related Interface</p>
</th>
<th class="cellrowborder" valign="top" width="18.96%" id="mcps1.1.7.1.3"><p id="p171897165014"><a name="p171897165014"></a><a name="p171897165014"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="15.28%" id="mcps1.1.7.1.4"><p id="p6189111610012"><a name="p6189111610012"></a><a name="p6189111610012"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="11.88%" id="mcps1.1.7.1.5"><p id="p18189161613018"><a name="p18189161613018"></a><a name="p18189161613018"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="20.23%" id="mcps1.1.7.1.6"><p id="p1189111619018"><a name="p1189111619018"></a><a name="p1189111619018"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row121893162017"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p101895160012"><a name="p101895160012"></a><a name="p101895160012"></a>Enable Early/Early_end mechanism</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p35557121739"><a name="p35557121739"></a><a name="p35557121739"></a>ss_mpi_vi_set_pipe_frame_interrupt_attr</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p41899164014"><a name="p41899164014"></a><a name="p41899164014"></a>Linear or online WDR, saves one VB; offline WDR (2 channels), saves two V Bs</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p61891216901"><a name="p61891216901"></a><a name="p61891216901"></a>Number of VI capture response interrupts doubles</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p0189111610018"><a name="p0189111610018"></a><a name="p0189111610018"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p181897164011"><a name="p181897164011"></a><a name="p181897164011"></a>vi pipe frame interrupt attr:</p>
<p id="p52761528981"><a name="p52761528981"></a><a name="p52761528981"></a>interrupt_type</p>
</td>
</tr>
<tr id="row79767550392"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p1797714558391"><a name="p1797714558391"></a><a name="p1797714558391"></a>Set chn output compression</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p3977755123917"><a name="p3977755123917"></a><a name="p3977755123917"></a>ss_mpi_vi_set_chn_attr</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p850653417418"><a name="p850653417418"></a><a name="p850653417418"></a>Compression saves more memory and bandwidth than uncompressed</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p697714553393"><a name="p697714553393"></a><a name="p697714553393"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p497735543915"><a name="p497735543915"></a><a name="p497735543915"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><a name="ul14706112944616"></a><a name="ul14706112944616"></a><ul id="ul14706112944616"><li>Hi3403V100: vi phys chn attr1:<p id="p9429133620436"><a name="p9429133620436"></a><a name="p9429133620436"></a>compress_mode</p>
</li><li>Others: vi phychn attr 2:<p id="p13774436174218"><a name="p13774436174218"></a><a name="p13774436174218"></a>compress_mode</p>
</li></ul>
</td>
</tr>
<tr id="row418971615018"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p51891116706"><a name="p51891116706"></a><a name="p51891116706"></a>Online WDR line mode wrapping</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p91906168018"><a name="p91906168018"></a><a name="p91906168018"></a>ss_mpi_vi_set_wdr_fusion_grp_attr</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p131901916309"><a name="p131901916309"></a><a name="p131901916309"></a>Default no wrapping, saves memory based on configured cache_line</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p1619017161701"><a name="p1619017161701"></a><a name="p1619017161701"></a>If cache_line is configured too small, image layering may occur</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p191902161105"><a name="p191902161105"></a><a name="p191902161105"></a>Supported by Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p219011617015"><a name="p219011617015"></a><a name="p219011617015"></a>vi wdr fusion grp attr: cache_line</p>
</td>
</tr>
<tr id="row425112112382"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p17261021143819"><a name="p17261021143819"></a><a name="p17261021143819"></a>Set pipe compressed output</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p19261821133820"><a name="p19261821133820"></a><a name="p19261821133820"></a>ss_mpi_vi_set_pipe_attr</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p326221143810"><a name="p326221143810"></a><a name="p326221143810"></a>Compression saves more memory and bandwidth than uncompressed</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p1426102114386"><a name="p1426102114386"></a><a name="p1426102114386"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p1226122111388"><a name="p1226122111388"></a><a name="p1226122111388"></a>Supported by Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p126921113816"><a name="p126921113816"></a><a name="p126921113816"></a>vi pipe attr1:</p>
<p id="p1112971894317"><a name="p1112971894317"></a><a name="p1112971894317"></a>compress_mode</p>
</td>
</tr>
<tr id="row61901164019"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p201903161102"><a name="p201903161102"></a><a name="p201903161102"></a>Adjust VI_VPSS to online/offline mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p1685912519133"><a name="p1685912519133"></a><a name="p1685912519133"></a>ss_mpi_sys_set_vi_vpss_mode</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p819016162012"><a name="p819016162012"></a><a name="p819016162012"></a>Online/online-offline/offline-online paths save 1-2 V Bs compared to fully offline paths</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p619018161605"><a name="p619018161605"></a><a name="p619018161605"></a>VI online can only process one path; VPSS online cannot perform channel post-processing functions at VI_CHN</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p2019001618011"><a name="p2019001618011"></a><a name="p2019001618011"></a>Supported by Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p61901416900"><a name="p61901416900"></a><a name="p61901416900"></a>vi vpss mode &amp; vi video mode: vi_vpss_mode</p>
</td>
</tr>
<tr id="row1391410280361"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p189141628173617"><a name="p189141628173617"></a><a name="p189141628173617"></a>Adjust VI_VIDEO mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p4914172816364"><a name="p4914172816364"></a><a name="p4914172816364"></a>ss_mpi_sys_set_vi_video_mode</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p8914162833615"><a name="p8914162833615"></a><a name="p8914162833615"></a>Normal mode saves 2 V Bs compared to advanced mode</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p2914152810361"><a name="p2914152810361"></a><a name="p2914152810361"></a>In normal mode, HNR function is before BE</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p1427543315374"><a name="p1427543315374"></a><a name="p1427543315374"></a>Supported by Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p1791492823613"><a name="p1791492823613"></a><a name="p1791492823613"></a>vi vpss mode &amp; vi video mode: vi_vpss_mode</p>
</td>
</tr>
<tr id="row194021932153015"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p11403532113017"><a name="p11403532113017"></a><a name="p11403532113017"></a>Adjust BayerNR buf_num count</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p1845374033616"><a name="p1845374033616"></a><a name="p1845374033616"></a>ss_mpi_vi_set_pipe_bnr_buf_num</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p16403132193015"><a name="p16403132193015"></a><a name="p16403132193015"></a>Default count is 40; can adjust count based on offline cached YUV requirements to save some memory</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p240323223019"><a name="p240323223019"></a><a name="p240323223019"></a>bnr_buf_num mainly affects the number of YUV frames that VI continuously caches without releasing</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p5176194463810"><a name="p5176194463810"></a><a name="p5176194463810"></a>Supported by Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p1240383233018"><a name="p1240383233018"></a><a name="p1240383233018"></a>vi pipe bnr buf num:</p>
<p id="p250319140392"><a name="p250319140392"></a><a name="p250319140392"></a>bnr_buf_num</p>
</td>
</tr>
<tr id="row1794717217459"><td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.7.1.1 "><p id="p119471121134513"><a name="p119471121134513"></a><a name="p119471121134513"></a>Manually disable ISP Bayer NR function</p>
</td>
<td class="cellrowborder" valign="top" width="16.259999999999998%" headers="mcps1.1.7.1.2 "><p id="p20607134462"><a name="p20607134462"></a><a name="p20607134462"></a>ss_mpi_isp_set_nr_attr</p>
</td>
<td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.7.1.3 "><p id="p49471821174517"><a name="p49471821174517"></a><a name="p49471821174517"></a>Disabling Bayer NR can save reference frame memory and bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.4 "><p id="p189471921174513"><a name="p189471921174513"></a><a name="p189471921174513"></a>Affects image quality</p>
</td>
<td class="cellrowborder" valign="top" width="11.88%" headers="mcps1.1.7.1.5 "><p id="p12469112194717"><a name="p12469112194717"></a><a name="p12469112194717"></a>Supported by Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="20.23%" headers="mcps1.1.7.1.6 "><p id="p1094782144512"><a name="p1094782144512"></a><a name="p1094782144512"></a>bayernr info: enable</p>
</td>
</tr>
</tbody>
</table> ## VDEC<a name="ZH-CN_TOPIC_0000002457839809"></a> <a name="table626mcpsimp"></a>
<table><thead align="left"><tr id="row635mcpsimp"><th class="cellrowborder" valign="top" width="15.521552155215524%" id="mcps1.1.7.1.1"><p id="p637mcpsimp"><a name="p637mcpsimp"></a><a name="p637mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="19.061906190619062%" id="mcps1.1.7.1.2"><p id="p639mcpsimp"><a name="p639mcpsimp"></a><a name="p639mcpsimp"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="17.851785178517854%" id="mcps1.1.7.1.3"><p id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="16.261626162616263%" id="mcps1.1.7.1.4"><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="11.211121112111213%" id="mcps1.1.7.1.5"><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="20.092009200920096%" id="mcps1.1.7.1.6"><p id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row649mcpsimp"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p651mcpsimp"><a name="p651mcpsimp"></a><a name="p651mcpsimp"></a>Allocate decoded stream buffer in memory-saving mode</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p653mcpsimp"><a name="p653mcpsimp"></a><a name="p653mcpsimp"></a>ss_mpi_vdec_set_mod_param: mini_buf_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><a name="ol068582510497"></a><a name="ol068582510497"></a><ol id="ol068582510497"><li>Can reduce the stream buffer size.</li><li>Can reduce vfmw(%d)_seg_buf memory</li></ol>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p661mcpsimp"><a name="p661mcpsimp"></a><a name="p661mcpsimp"></a>module param: mini_buf_mode</p>
</td>
</tr>
<tr id="row14135125317368"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p1513515353610"><a name="p1513515353610"></a><a name="p1513515353610"></a>Control user data buffer size</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p191358537368"><a name="p191358537368"></a><a name="p191358537368"></a>ss_mpi_vdec_set_user_data_attr:</p>
<a name="ul1314929113618"></a><a name="ul1314929113618"></a><ul id="ul1314929113618"><li>enable</li><li>max_user_data_len</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p15136135314361"><a name="p15136135314361"></a><a name="p15136135314361"></a>Do not allocate or allocate fewer user data buffers</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p20136175313620"><a name="p20136175313620"></a><a name="p20136175313620"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p17136135323616"><a name="p17136135323616"></a><a name="p17136135323616"></a>detail user_data state:</p>
<a name="ul1382325010495"></a><a name="ul1382325010495"></a><ul id="ul1382325010495"><li>enable</li><li>max_user_data_len</li></ul>
</td>
</tr>
<tr id="row9783124223915"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p4784194210391"><a name="p4784194210391"></a><a name="p4784194210391"></a>Control jpeg decoding progressive_buffer</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p10784442123910"><a name="p10784442123910"></a><a name="p10784442123910"></a>ss_mpi_vdec_set_mod_param:</p>
<p id="p1184225315461"><a name="p1184225315461"></a><a name="p1184225315461"></a>progressive_en</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p078410427393"><a name="p078410427393"></a><a name="p078410427393"></a>Do not allocate progressive_buffer</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p16441457194013"><a name="p16441457194013"></a><a name="p16441457194013"></a>When using JPEGD progressive function, setting dynamic_alloc_en to TD_TRUE allows dynamic allocation of progressive_buffer, reducing progressive_buffer memory usage</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p3785042183915"><a name="p3785042183915"></a><a name="p3785042183915"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p1878512420393"><a name="p1878512420393"></a><a name="p1878512420393"></a>module param: progressive_en</p>
</td>
</tr>
<tr id="row662mcpsimp"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p664mcpsimp"><a name="p664mcpsimp"></a><a name="p664mcpsimp"></a>Set maximum decoder capability set per scenario</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p856962512367"><a name="p856962512367"></a><a name="p856962512367"></a>ss_mpi_vdec_set_mod_param:</p>
<a name="ul116082983617"></a><a name="ul116082983617"></a><ul id="ul116082983617"><li>video_mod_param</li><li>pic_mod_param</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>Can save some MMZ and OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p670mcpsimp"><a name="p670mcpsimp"></a><a name="p670mcpsimp"></a>Reducing VDH-related memory allocation may decrease decoding performance, but does not affect functionality. JPEGD configuration can save OS memory.</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p672mcpsimp"><a name="p672mcpsimp"></a><a name="p672mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p17332182416509"><a name="p17332182416509"></a><a name="p17332182416509"></a>module param:</p>
<a name="ul8861295508"></a><a name="ul8861295508"></a><ul id="ul8861295508"><li>max_video_width</li><li>max_video_height</li><li>max_slice_num</li><li>vdh_msg_num</li><li>max_pic_width</li><li>max_pic_height</li><li>progressive_en</li><li>dynamic_alloc_en</li><li>capacity_strategy</li></ul>
</td>
</tr>
<tr id="row675mcpsimp"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p677mcpsimp"><a name="p677mcpsimp"></a><a name="p677mcpsimp"></a>Set decoding channel capability set per scenario</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p679mcpsimp"><a name="p679mcpsimp"></a><a name="p679mcpsimp"></a>ss_mpi_vdec_set_protocol_param</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p681mcpsimp"><a name="p681mcpsimp"></a><a name="p681mcpsimp"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p683mcpsimp"><a name="p683mcpsimp"></a><a name="p683mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p685mcpsimp"><a name="p685mcpsimp"></a><a name="p685mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p1732172845117"><a name="p1732172845117"></a><a name="p1732172845117"></a>chn video attr &amp; params:</p>
<a name="ul6698163135110"></a><a name="ul6698163135110"></a><ul id="ul6698163135110"><li>max_vps_num</li><li>max_sps_num</li><li>max_pps_num</li><li>max_slice_segment_num</li></ul>
</td>
</tr>
<tr id="row688mcpsimp"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p690mcpsimp"><a name="p690mcpsimp"></a><a name="p690mcpsimp"></a>Can disable Tmv switch when decoding H264 streams without B frames</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p692mcpsimp"><a name="p692mcpsimp"></a><a name="p692mcpsimp"></a>ss_mpi_vdec_create_chn: temporal_mvp_en</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p694mcpsimp"><a name="p694mcpsimp"></a><a name="p694mcpsimp"></a>Can save Tmv buffer</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p696mcpsimp"><a name="p696mcpsimp"></a><a name="p696mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p698mcpsimp"><a name="p698mcpsimp"></a><a name="p698mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p700mcpsimp"><a name="p700mcpsimp"></a><a name="p700mcpsimp"></a>chn video attr &amp; params: tmv_en</p>
</td>
</tr>
<tr id="row701mcpsimp"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p703mcpsimp"><a name="p703mcpsimp"></a><a name="p703mcpsimp"></a>Maximum number of channels supported by the decoding module</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p705mcpsimp"><a name="p705mcpsimp"></a><a name="p705mcpsimp"></a>g_vdec_max_chn_num g_vfmw_max_chn_num</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p707mcpsimp"><a name="p707mcpsimp"></a><a name="p707mcpsimp"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p709mcpsimp"><a name="p709mcpsimp"></a><a name="p709mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p711mcpsimp"><a name="p711mcpsimp"></a><a name="p711mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p713mcpsimp"><a name="p713mcpsimp"></a><a name="p713mcpsimp"></a>module param: g_vdec_max_chn_num</p>
</td>
</tr>
<tr id="row714mcpsimp"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p716mcpsimp"><a name="p716mcpsimp"></a><a name="p716mcpsimp"></a>Set reference frames to 0 for I-frame-only decoding channels</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p718mcpsimp"><a name="p718mcpsimp"></a><a name="p718mcpsimp"></a>ss_mpi_vdec_create_chn:</p>
<p id="p719mcpsimp"><a name="p719mcpsimp"></a><a name="p719mcpsimp"></a>ref_frame_num</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p13664518479"><a name="p13664518479"></a><a name="p13664518479"></a>Reduces pic_vb and tmv_vb allocation count</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p723mcpsimp"><a name="p723mcpsimp"></a><a name="p723mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p725mcpsimp"><a name="p725mcpsimp"></a><a name="p725mcpsimp"></a>Set the channel decoding mode to I mode, otherwise logmpp will report an error.</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p727mcpsimp"><a name="p727mcpsimp"></a><a name="p727mcpsimp"></a>chn video attr &amp; params: ref_num</p>
</td>
</tr>
<tr id="row152423017415"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p492842274410"><a name="p492842274410"></a><a name="p492842274410"></a>Set quick release reference frame mode to adaptive or forced mode</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p109271722164410"><a name="p109271722164410"></a><a name="p109271722164410"></a>ss_mpi_vdec_set_chn_param:</p>
<p id="p14976199523"><a name="p14976199523"></a><a name="p14976199523"></a>quick_mark_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p1755935204417"><a name="p1755935204417"></a><a name="p1755935204417"></a>Accelerates VB rotation, can reduce pic_vb and tmv_vb allocation count</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p18243170154115"><a name="p18243170154115"></a><a name="p18243170154115"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p16243150114111"><a name="p16243150114111"></a><a name="p16243150114111"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p1724310114118"><a name="p1724310114118"></a><a name="p1724310114118"></a>chn video attr &amp; params:</p>
<p id="p85881976531"><a name="p85881976531"></a><a name="p85881976531"></a>quick_mark_mode</p>
</td>
</tr>
<tr id="row161151734125414"><td class="cellrowborder" valign="top" width="15.521552155215524%" headers="mcps1.1.7.1.1 "><p id="p18574312549"><a name="p18574312549"></a><a name="p18574312549"></a>Create channels with the smallest possible width and height for the actual application</p>
</td>
<td class="cellrowborder" valign="top" width="19.061906190619062%" headers="mcps1.1.7.1.2 "><p id="p13115193413548"><a name="p13115193413548"></a><a name="p13115193413548"></a>ss_mpi_vdec_create_chn</p>
</td>
<td class="cellrowborder" valign="top" width="17.851785178517854%" headers="mcps1.1.7.1.3 "><p id="p161159340548"><a name="p161159340548"></a><a name="p161159340548"></a>Can reduce vfmw(%d)_seg_buf memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.261626162616263%" headers="mcps1.1.7.1.4 "><p id="p1111593410549"><a name="p1111593410549"></a><a name="p1111593410549"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.211121112111213%" headers="mcps1.1.7.1.5 "><p id="p17115123415547"><a name="p17115123415547"></a><a name="p17115123415547"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20.092009200920096%" headers="mcps1.1.7.1.6 "><p id="p121151434185418"><a name="p121151434185418"></a><a name="p121151434185418"></a>chn comm attr &amp; params:</p>
<a name="ul177476443519"></a><a name="ul177476443519"></a><ul id="ul177476443519"><li>max_w</li><li>max_h</li></ul>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **Note:**
>For details, see the "Video Decoding" chapter of the "MPP Media Processing Software V5.0 Development Reference". ## VPSS<a name="ZH-CN_TOPIC_0000002424201190"></a> <a name="table451mcpsimp"></a>
<table><thead align="left"><tr id="row460mcpsimp"><th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.1.7.1.1"><p id="p462mcpsimp"><a name="p462mcpsimp"></a><a name="p462mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="21.842184218421842%" id="mcps1.1.7.1.2"><p id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="17.75177517751775%" id="mcps1.1.7.1.3"><p id="p466mcpsimp"><a name="p466mcpsimp"></a><a name="p466mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="14.951495149514951%" id="mcps1.1.7.1.4"><p id="p468mcpsimp"><a name="p468mcpsimp"></a><a name="p468mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="16.251625162516252%" id="mcps1.1.7.1.5"><p id="p470mcpsimp"><a name="p470mcpsimp"></a><a name="p470mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18.09180918091809%" id="mcps1.1.7.1.6"><p id="p472mcpsimp"><a name="p472mcpsimp"></a><a name="p472mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row474mcpsimp"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.7.1.1 "><p id="p476mcpsimp"><a name="p476mcpsimp"></a><a name="p476mcpsimp"></a>Disable backup frame</p>
</td>
<td class="cellrowborder" valign="top" width="21.842184218421842%" headers="mcps1.1.7.1.2 "><a name="ul1224620538532"></a><a name="ul1224620538532"></a><ul id="ul1224620538532"><li>ss_mpi_vpss_enable_backup_frame</li><li>ss_mpi_vpss_disable_backup_frame</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.1.7.1.3 "><p id="p481mcpsimp"><a name="p481mcpsimp"></a><a name="p481mcpsimp"></a>Each VPSS GROUP uses 1 less input source buffer.</p>
</td>
<td class="cellrowborder" valign="top" width="14.951495149514951%" headers="mcps1.1.7.1.4 "><p id="p483mcpsimp"><a name="p483mcpsimp"></a><a name="p483mcpsimp"></a>When VO is paused, the display device shows the background color during zoom or scene switching.</p>
</td>
<td class="cellrowborder" valign="top" width="16.251625162516252%" headers="mcps1.1.7.1.5 "><p id="p485mcpsimp"><a name="p485mcpsimp"></a><a name="p485mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.09180918091809%" headers="mcps1.1.7.1.6 "><p id="p487mcpsimp"><a name="p487mcpsimp"></a><a name="p487mcpsimp"></a>vpss grp attr1: backup</p>
</td>
</tr>
<tr id="row488mcpsimp"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.7.1.1 "><p id="p490mcpsimp"><a name="p490mcpsimp"></a><a name="p490mcpsimp"></a>Do not enable nr and dei functions simultaneously</p>
</td>
<td class="cellrowborder" valign="top" width="21.842184218421842%" headers="mcps1.1.7.1.2 "><p id="p492mcpsimp"><a name="p492mcpsimp"></a><a name="p492mcpsimp"></a>ss_mpi_vpss_create_grp</p>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.1.7.1.3 "><p id="p494mcpsimp"><a name="p494mcpsimp"></a><a name="p494mcpsimp"></a>Each VPSS GROUP allocates 2 fewer frame buffers (reference frame and reconstructed frame).</p>
</td>
<td class="cellrowborder" valign="top" width="14.951495149514951%" headers="mcps1.1.7.1.4 "><p id="p496mcpsimp"><a name="p496mcpsimp"></a><a name="p496mcpsimp"></a>Affects image quality.</p>
</td>
<td class="cellrowborder" valign="top" width="16.251625162516252%" headers="mcps1.1.7.1.5 "><p id="p498mcpsimp"><a name="p498mcpsimp"></a><a name="p498mcpsimp"></a>If either nr or dei function is enabled, reference frame and reconstructed frame buffers will be allocated.</p>
</td>
<td class="cellrowborder" valign="top" width="18.09180918091809%" headers="mcps1.1.7.1.6 "><p id="p1526981212547"><a name="p1526981212547"></a><a name="p1526981212547"></a>vpss grp attr:</p>
<a name="ul1993443710547"></a><a name="ul1993443710547"></a><ul id="ul1993443710547"><li>nr</li><li>dei_mode</li></ul>
</td>
</tr>
<tr id="row501mcpsimp"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.7.1.1 "><p id="p503mcpsimp"><a name="p503mcpsimp"></a><a name="p503mcpsimp"></a>CH0 output YUV compression</p>
</td>
<td class="cellrowborder" valign="top" width="21.842184218421842%" headers="mcps1.1.7.1.2 "><p id="p505mcpsimp"><a name="p505mcpsimp"></a><a name="p505mcpsimp"></a>ss_mpi_vpss_set_chn_attr: compress_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.1.7.1.3 "><p id="p507mcpsimp"><a name="p507mcpsimp"></a><a name="p507mcpsimp"></a>Saves more memory and bandwidth than uncompressed</p>
</td>
<td class="cellrowborder" valign="top" width="14.951495149514951%" headers="mcps1.1.7.1.4 "><p id="p509mcpsimp"><a name="p509mcpsimp"></a><a name="p509mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.251625162516252%" headers="mcps1.1.7.1.5 "><p id="p511mcpsimp"><a name="p511mcpsimp"></a><a name="p511mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.09180918091809%" headers="mcps1.1.7.1.6 "><p id="p513mcpsimp"><a name="p513mcpsimp"></a><a name="p513mcpsimp"></a>vpss chn output status: compress_mode</p>
</td>
</tr>
<tr id="row128135520520"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.7.1.1 "><p id="p18139521659"><a name="p18139521659"></a><a name="p18139521659"></a>Enable Early/Early_end mechanism</p>
</td>
<td class="cellrowborder" valign="top" width="21.842184218421842%" headers="mcps1.1.7.1.2 "><p id="p1381316525513"><a name="p1381316525513"></a><a name="p1381316525513"></a>ss_mpi_vpss_set_grp_frame_interrupt_attr</p>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.1.7.1.3 "><p id="p198131252554"><a name="p198131252554"></a><a name="p198131252554"></a>In full online mode, each channel saves one frame buffer</p>
</td>
<td class="cellrowborder" valign="top" width="14.951495149514951%" headers="mcps1.1.7.1.4 "><p id="p1481305216514"><a name="p1481305216514"></a><a name="p1481305216514"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.251625162516252%" headers="mcps1.1.7.1.5 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="18.09180918091809%" headers="mcps1.1.7.1.6 "><p id="p14813252553"><a name="p14813252553"></a><a name="p14813252553"></a>frame interrupt attr: int_type</p>
</td>
</tr>
<tr id="row57851237113914"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.7.1.1 "><p id="p8786173783912"><a name="p8786173783912"></a><a name="p8786173783912"></a>Reduce module parameter split_node_num</p>
</td>
<td class="cellrowborder" valign="top" width="21.842184218421842%" headers="mcps1.1.7.1.2 "><p id="p952841515511"><a name="p952841515511"></a><a name="p952841515511"></a>ss_mpi_vpss_set_mod_param</p>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.1.7.1.3 "><p id="p18786203719390"><a name="p18786203719390"></a><a name="p18786203719390"></a>Reduces the mmz memory occupied by register templates for each group</p>
</td>
<td class="cellrowborder" valign="top" width="14.951495149514951%" headers="mcps1.1.7.1.4 "><p id="p17861237153917"><a name="p17861237153917"></a><a name="p17861237153917"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="16.251625162516252%" headers="mcps1.1.7.1.5 "><p id="p1678633763910"><a name="p1678633763910"></a><a name="p1678633763910"></a>split_node_num is proportional to the input resolution width, default is 3. When the scene is fixed with small resolution, the value can be reduced; for very large resolutions, choose an appropriate value to avoid wasting memory.</p>
</td>
<td class="cellrowborder" valign="top" width="18.09180918091809%" headers="mcps1.1.7.1.6 "><p id="p1378620377390"><a name="p1378620377390"></a><a name="p1378620377390"></a>vpss module param:</p>
<p id="p13318205816215"><a name="p13318205816215"></a><a name="p13318205816215"></a>split_node_num</p>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **Note:**
>For specific usage and limitations, see the "Video Processing Subsystem" chapter of the "MPP Media Processing Software V5.0 Development Reference". ## VGS<a name="ZH-CN_TOPIC_0000002424361078"></a> <a name="table830mcpsimp"></a>
<table><thead align="left"><tr id="row839mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.7.1.1"><p id="p841mcpsimp"><a name="p841mcpsimp"></a><a name="p841mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.7.1.2"><p id="p843mcpsimp"><a name="p843mcpsimp"></a><a name="p843mcpsimp"></a>Related Module Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.7.1.3"><p id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="15.989999999999998%" id="mcps1.1.7.1.4"><p id="p847mcpsimp"><a name="p847mcpsimp"></a><a name="p847mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="10.26%" id="mcps1.1.7.1.5"><p id="p849mcpsimp"><a name="p849mcpsimp"></a><a name="p849mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18.75%" id="mcps1.1.7.1.6"><p id="p851mcpsimp"><a name="p851mcpsimp"></a><a name="p851mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row853mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.7.1.1 "><p id="p855mcpsimp"><a name="p855mcpsimp"></a><a name="p855mcpsimp"></a>Set the maximum number of VGS jobs</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.7.1.2 "><p id="p857mcpsimp"><a name="p857mcpsimp"></a><a name="p857mcpsimp"></a>g_max_vgs_job</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.7.1.3 "><p id="p859mcpsimp"><a name="p859mcpsimp"></a><a name="p859mcpsimp"></a>Default 128; reducing as needed can save memory</p>
</td>
<td class="cellrowborder" valign="top" width="15.989999999999998%" headers="mcps1.1.7.1.4 "><p id="p861mcpsimp"><a name="p861mcpsimp"></a><a name="p861mcpsimp"></a>Too few jobs will limit VGS performance.</p>
</td>
<td class="cellrowborder" valign="top" width="10.26%" headers="mcps1.1.7.1.5 "><p id="p863mcpsimp"><a name="p863mcpsimp"></a><a name="p863mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.7.1.6 "><p id="p865mcpsimp"><a name="p865mcpsimp"></a><a name="p865mcpsimp"></a>module params: g_max_job_num</p>
</td>
</tr>
<tr id="row866mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.7.1.1 "><p id="p868mcpsimp"><a name="p868mcpsimp"></a><a name="p868mcpsimp"></a>Set the maximum number of VGS tasks</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.7.1.2 "><p id="p870mcpsimp"><a name="p870mcpsimp"></a><a name="p870mcpsimp"></a>g_max_vgs_task</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.7.1.3 "><p id="p872mcpsimp"><a name="p872mcpsimp"></a><a name="p872mcpsimp"></a>Default 200; reducing as needed can save memory</p>
</td>
<td class="cellrowborder" valign="top" width="15.989999999999998%" headers="mcps1.1.7.1.4 "><p id="p874mcpsimp"><a name="p874mcpsimp"></a><a name="p874mcpsimp"></a>Too few tasks will limit VGS performance</p>
</td>
<td class="cellrowborder" valign="top" width="10.26%" headers="mcps1.1.7.1.5 "><p id="p876mcpsimp"><a name="p876mcpsimp"></a><a name="p876mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.7.1.6 "><p id="p878mcpsimp"><a name="p878mcpsimp"></a><a name="p878mcpsimp"></a>module params: g_max_task_num</p>
</td>
</tr>
<tr id="row879mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.7.1.1 "><p id="p881mcpsimp"><a name="p881mcpsimp"></a><a name="p881mcpsimp"></a>Set the maximum number of VGS nodes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.7.1.2 "><p id="p883mcpsimp"><a name="p883mcpsimp"></a><a name="p883mcpsimp"></a>g_max_vgs_node</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.7.1.3 "><p id="p885mcpsimp"><a name="p885mcpsimp"></a><a name="p885mcpsimp"></a>Default 200; reducing as needed can save memory</p>
</td>
<td class="cellrowborder" valign="top" width="15.989999999999998%" headers="mcps1.1.7.1.4 "><p id="p887mcpsimp"><a name="p887mcpsimp"></a><a name="p887mcpsimp"></a>Too few nodes will limit VGS performance</p>
</td>
<td class="cellrowborder" valign="top" width="10.26%" headers="mcps1.1.7.1.5 "><p id="p889mcpsimp"><a name="p889mcpsimp"></a><a name="p889mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.75%" headers="mcps1.1.7.1.6 "><p id="p891mcpsimp"><a name="p891mcpsimp"></a><a name="p891mcpsimp"></a>module params: g_max_node_num</p>
</td>
</tr>
</tbody>
</table> The VGS module mainly uses OS memory and node mmz. Considering the scenario, reducing the maximum job count, maximum task count, and maximum node count can reduce OS memory usage and node-occupied MMZ memory. >![](public_sys-resources/icon-note.gif) **Note:**
>For specific usage and limitations, see the "Video Graphics Subsystem" chapter of the "MPP Media Processing Software V5.0 Development Reference". ## VENC<a name="ZH-CN_TOPIC_0000002424361070"></a> <a name="table97611421161513"></a>
<table><thead align="left"><tr id="row127617214151"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.7.1.1"><p id="p117611621171511"><a name="p117611621171511"></a><a name="p117611621171511"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="20.18%" id="mcps1.1.7.1.2"><p id="p1676192171517"><a name="p1676192171517"></a><a name="p1676192171517"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.7.1.3"><p id="p47611821101518"><a name="p47611821101518"></a><a name="p47611821101518"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="22.52%" id="mcps1.1.7.1.4"><p id="p4761821121510"><a name="p4761821121510"></a><a name="p4761821121510"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.7.1.5"><p id="p187611521101518"><a name="p187611521101518"></a><a name="p187611521101518"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.7.1.6"><p id="p2761202120150"><a name="p2761202120150"></a><a name="p2761202120150"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row776213215151"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p8762821131520"><a name="p8762821131520"></a><a name="p8762821131520"></a>Dynamically switch encoding resolution</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><a name="ul332553461517"></a><a name="ul332553461517"></a><ul id="ul332553461517"><li>ss_mpi_venc_set_chn_attr</li><li>ss_mpi_venc_get_chn_attr</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p6762122151518"><a name="p6762122151518"></a><a name="p6762122151518"></a>Switching encoding resolution without destroying the channel reduces memory fragmentation. For example, using NormalP can reduce the total size of reference frame/reconstructed frame buffer memory compared to SmartP and DualP.</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><p id="p1876282141516"><a name="p1876282141516"></a><a name="p1876282141516"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 "><p id="p1676210214151"><a name="p1676210214151"></a><a name="p1676210214151"></a>After switching resolution, all parameters return to default values.</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p1476242131511"><a name="p1476242131511"></a><a name="p1476242131511"></a>-</p>
</td>
</tr>
<tr id="row1776242119151"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p27622021191510"><a name="p27622021191510"></a><a name="p27622021191510"></a>Allocate encoded stream buffer in memory-saving mode</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><p id="p676218214157"><a name="p676218214157"></a><a name="p676218214157"></a>ss_mpi_venc_set_mod_param: mini_buf_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p1676242116159"><a name="p1676242116159"></a><a name="p1676242116159"></a>Can reduce the stream buffer size.</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><p id="p2762172110156"><a name="p2762172110156"></a><a name="p2762172110156"></a>This mode requires the user to ensure that the stream buffer size is set appropriately. If the bitrate is high or the user does not retrieve the stream in time, stream buffer insufficiency may lead to continuous re-encoding or frame dropping.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 "><p id="p1076215216155"><a name="p1076215216155"></a><a name="p1076215216155"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p1476220218153"><a name="p1476220218153"></a><a name="p1476220218153"></a>The h265e/h264e/jpege modules all have module param: mini_buf_mode</p>
</td>
</tr>
<tr id="row13762162111151"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p97621218158"><a name="p97621218158"></a><a name="p97621218158"></a>Reference frame/reconstructed frame buffer reuse</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><p id="p147621721171511"><a name="p147621721171511"></a><a name="p147621721171511"></a>ss_mpi_venc_create_chn: rcn_ref_share_buf_en</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p14762821201517"><a name="p14762821201517"></a><a name="p14762821201517"></a>Approximately saves (ref_num+1-1.2* ref_num) frame buffers</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><p id="p167621521181517"><a name="p167621521181517"></a><a name="p167621521181517"></a>In abnormal situations such as oversized frames, bitrate overshoot, or bitrate buffer full leading to frame dropping or re-encoding, the next frame can only be inserted as an I frame.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 "><p id="p276252141516"><a name="p276252141516"></a><a name="p276252141516"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p4762132101513"><a name="p4762132101513"></a><a name="p4762132101513"></a>h265e/h264e module ref_param info: rcn_ref_share_buf_en</p>
</td>
</tr>
<tr id="row127622211155"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p376232111518"><a name="p376232111518"></a><a name="p376232111518"></a>Reference frame/reconstructed frame buffer ratio adjustment</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><a name="ul9454134811156"></a><a name="ul9454134811156"></a><ul id="ul9454134811156"><li>ss_mpi_venc_set_chn_attr</li><li>ss_mpi_venc_get_chn_attr<p id="p8762121121510"><a name="p8762121121510"></a><a name="p8762121121510"></a>frame_buf_ratio</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p12762621131513"><a name="p12762621131513"></a><a name="p12762621131513"></a>If set to 80, the frame buffer is 80% of the original size.</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><a name="ol11762122111153"></a><a name="ol11762122111153"></a><ol id="ol11762122111153"><li>When P frames flush I slices, the entire frame may be flushed as I blocks and the I slice flushing may end early;</li><li>Anti-breathing effect may fail on certain frames;</li><li>The QPMAP table cannot force-specify skip blocks, and the Skip Weight table cannot force-specify skip blocks;</li><li>ROI background low-frame-rate encoding may result in some frames' non-ROI areas not being encoded as p_skip blocks;</li><li>In certain scenarios, specifying p_skip frames may fail, such as the frame-dropping strategy when the instantaneous encoding bitrate exceeds the threshold;</li><li>Skip tendency may fail.</li></ol>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p2763121161519"><a name="p2763121161519"></a><a name="p2763121161519"></a>h265e/h264e module ref_param info: frame_buf_ratio</p>
</td>
</tr>
<tr id="row13763921201510"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p27631217155"><a name="p27631217155"></a><a name="p27631217155"></a>Dynamically recycle reference frame buffers</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><p id="p67635212156"><a name="p67635212156"></a><a name="p67635212156"></a>ss_mpi_venc_set_mod_param: frame_buf_recycle</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p11763421161513"><a name="p11763421161513"></a><a name="p11763421161513"></a>When the encoding switches GOP mode and reference frames decrease, excess reference frame buffers can be dynamically released.</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><p id="p3763172111520"><a name="p3763172111520"></a><a name="p3763172111520"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 "><p id="p776342171513"><a name="p776342171513"></a><a name="p776342171513"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p17763221121516"><a name="p17763221121516"></a><a name="p17763221121516"></a>venc module param: frame_buf_recycle</p>
</td>
</tr>
<tr id="row11763121101512"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p7763112171513"><a name="p7763112171513"></a><a name="p7763112171513"></a>Maximum number of channels supported by the encoding module</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><p id="p87635216158"><a name="p87635216158"></a><a name="p87635216158"></a>Module parameter: g_venc_max_chn_num</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p1576372121511"><a name="p1576372121511"></a><a name="p1576372121511"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><p id="p8763172121515"><a name="p8763172121515"></a><a name="p8763172121515"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 "><p id="p147637212157"><a name="p147637212157"></a><a name="p147637212157"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p167632217151"><a name="p167632217151"></a><a name="p167632217151"></a>venc module param: venc_max_chn_num</p>
</td>
</tr>
<tr id="row876392181520"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.1 "><p id="p57631221171510"><a name="p57631221171510"></a><a name="p57631221171510"></a>Multi-channel encoding with same resolution uses User VB mode to save memory</p>
</td>
<td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.7.1.2 "><p id="p187631721161519"><a name="p187631721161519"></a><a name="p187631721161519"></a>ss_mpi_venc_set_mod_param: vb_src</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.7.1.3 "><p id="p37634212157"><a name="p37634212157"></a><a name="p37634212157"></a>Saves more frame buffer memory than Private VB mode</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.7.1.4 "><p id="p27637210154"><a name="p27637210154"></a><a name="p27637210154"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.5 "><p id="p67644211156"><a name="p67644211156"></a><a name="p67644211156"></a>Only supported by h265e/h264e</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.7.1.6 "><p id="p1764132111155"><a name="p1764132111155"></a><a name="p1764132111155"></a>h265e module param: h265_vb_src;</p>
<p id="p77647219155"><a name="p77647219155"></a><a name="p77647219155"></a>h264e module param: h264_vb_src</p>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **Note:**
>For details, see the "Video Encoding" chapter of the "MPP Media Processing Software V5.0 Development Reference". ## VO<a name="ZH-CN_TOPIC_0000002424361042"></a> <a name="table16803153016127"></a>
<table><thead align="left"><tr id="row4803153012125"><th class="cellrowborder" valign="top" width="13.171317131713172%" id="mcps1.1.7.1.1"><p id="p98031130121217"><a name="p98031130121217"></a><a name="p98031130121217"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="22.472247224722473%" id="mcps1.1.7.1.2"><p id="p8803173016125"><a name="p8803173016125"></a><a name="p8803173016125"></a>Related Interface</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.7.1.3"><p id="p1680319306124"><a name="p1680319306124"></a><a name="p1680319306124"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811883%" id="mcps1.1.7.1.4"><p id="p108032307127"><a name="p108032307127"></a><a name="p108032307127"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="13.251325132513253%" id="mcps1.1.7.1.5"><p id="p480413015127"><a name="p480413015127"></a><a name="p480413015127"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="23.382338233823383%" id="mcps1.1.7.1.6"><p id="p1680463091215"><a name="p1680463091215"></a><a name="p1680463091215"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row2080411309124"><td class="cellrowborder" valign="top" width="13.171317131713172%" headers="mcps1.1.7.1.1 "><p id="p1180443020128"><a name="p1180443020128"></a><a name="p1180443020128"></a>Set VO watermark to 2</p>
</td>
<td class="cellrowborder" valign="top" width="22.472247224722473%" headers="mcps1.1.7.1.2 "><p id="p1804143061213"><a name="p1804143061213"></a><a name="p1804143061213"></a>ss_mpi_vo_set_chn_recv_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.7.1.3 "><p id="p18804830181213"><a name="p18804830181213"></a><a name="p18804830181213"></a>Reduces channel VB accumulation</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.1.7.1.4 "><p id="p1080453071219"><a name="p1080453071219"></a><a name="p1080453071219"></a>May cause slight frame dropping</p>
</td>
<td class="cellrowborder" valign="top" width="13.251325132513253%" headers="mcps1.1.7.1.5 "><p id="p19804930111210"><a name="p19804930111210"></a><a name="p19804930111210"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.382338233823383%" headers="mcps1.1.7.1.6 "><p id="p188041530141213"><a name="p188041530141213"></a><a name="p188041530141213"></a>vo chn play info 1: threshold</p>
</td>
</tr>
<tr id="row13804133081219"><td class="cellrowborder" valign="top" width="13.171317131713172%" headers="mcps1.1.7.1.1 "><p id="p1280410309122"><a name="p1280410309122"></a><a name="p1280410309122"></a>Set display queue length to minimum 3 in playback mode</p>
</td>
<td class="cellrowborder" valign="top" width="22.472247224722473%" headers="mcps1.1.7.1.2 "><p id="p98041730131219"><a name="p98041730131219"></a><a name="p98041730131219"></a>ss_mpi_vo_set_video_layer_attr</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.7.1.3 "><p id="p3804103051215"><a name="p3804103051215"></a><a name="p3804103051215"></a>HD devices can save 1 frame buffer.</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.1.7.1.4 "><p id="p48041930201212"><a name="p48041930201212"></a><a name="p48041930201212"></a>Affects VO display smoothness.</p>
</td>
<td class="cellrowborder" valign="top" width="13.251325132513253%" headers="mcps1.1.7.1.5 "><p id="p18041430141217"><a name="p18041430141217"></a><a name="p18041430141217"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.382338233823383%" headers="mcps1.1.7.1.6 "><p id="p68041830111220"><a name="p68041830111220"></a><a name="p68041830111220"></a>vo video layer status 2: disp_buf_len</p>
</td>
</tr>
<tr id="row78041830121212"><td class="cellrowborder" valign="top" width="13.171317131713172%" headers="mcps1.1.7.1.1 "><p id="p1680473011125"><a name="p1680473011125"></a><a name="p1680473011125"></a>In pass-through mode, Disp Buf Len can be set to 0</p>
</td>
<td class="cellrowborder" valign="top" width="22.472247224722473%" headers="mcps1.1.7.1.2 "><p id="p2080483011129"><a name="p2080483011129"></a><a name="p2080483011129"></a>ss_mpi_vo_set_video_layer_attr</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.7.1.3 "><p id="p58041030141218"><a name="p58041030141218"></a><a name="p58041030141218"></a>No need to allocate Display Buffer</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.1.7.1.4 "><p id="p16804143010129"><a name="p16804143010129"></a><a name="p16804143010129"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="13.251325132513253%" headers="mcps1.1.7.1.5 "><p id="p19804930191218"><a name="p19804930191218"></a><a name="p19804930191218"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.382338233823383%" headers="mcps1.1.7.1.6 "><p id="p13804530141215"><a name="p13804530141215"></a><a name="p13804530141215"></a>vo video layer status 2: disp_buf_len</p>
</td>
</tr>
<tr id="row1980443019128"><td class="cellrowborder" valign="top" width="13.171317131713172%" headers="mcps1.1.7.1.1 "><p id="p880473016122"><a name="p880473016122"></a><a name="p880473016122"></a>Multi-region cluster mode</p>
</td>
<td class="cellrowborder" valign="top" width="22.472247224722473%" headers="mcps1.1.7.1.2 "><a name="ul68049306129"></a><a name="ul68049306129"></a><ul id="ul68049306129"><li>ss_mpi_vo_set_video_layer_attr</li><li>ss_mpi_vo_set_chn_display_pos</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.7.1.3 "><p id="p7805103071218"><a name="p7805103071218"></a><a name="p7805103071218"></a>Can save some MMZ memory</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.1.7.1.4 "><p id="p580573021218"><a name="p580573021218"></a><a name="p580573021218"></a>Cluster mode VO does not support scaling</p>
</td>
<td class="cellrowborder" valign="top" width="13.251325132513253%" headers="mcps1.1.7.1.5 "><p id="p580583071220"><a name="p580583071220"></a><a name="p580583071220"></a>Supported by </p>
</td>
<td class="cellrowborder" valign="top" width="23.382338233823383%" headers="mcps1.1.7.1.6 "><a name="ul58051130111211"></a><a name="ul58051130111211"></a><ul id="ul58051130111211"><li>vo video layer status 2: cluster_mode_en</li><li>vo chn basic info: disp_x disp_y</li></ul>
</td>
</tr>
<tr id="row3805163018128"><td class="cellrowborder" valign="top" width="13.171317131713172%" headers="mcps1.1.7.1.1 "><p id="p88058309121"><a name="p88058309121"></a><a name="p88058309121"></a>Single-region mode VO buffer-saving solution</p>
</td>
<td class="cellrowborder" valign="top" width="22.472247224722473%" headers="mcps1.1.7.1.2 "><a name="ul480573016127"></a><a name="ul480573016127"></a><ul id="ul480573016127"><li>ss_mpi_vo_set_video_layer_attr</li><li>ss_mpi_vo_set_vtth</li><li>ss_mpi_vo_set_less_buf_attr</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.7.1.3 "><p id="p14805430111216"><a name="p14805430111216"></a><a name="p14805430111216"></a>In single-region non-pass-through mode, the minimum display buffer can be set to 2.</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.1.7.1.4 "><p id="p19805143091213"><a name="p19805143091213"></a><a name="p19805143091213"></a>Reduces one display buffer</p>
</td>
<td class="cellrowborder" valign="top" width="13.251325132513253%" headers="mcps1.1.7.1.5 "><p id="p198051630101210"><a name="p198051630101210"></a><a name="p198051630101210"></a>Supported by </p>
</td>
<td class="cellrowborder" valign="top" width="23.382338233823383%" headers="mcps1.1.7.1.6 "><a name="ul7805230171213"></a><a name="ul7805230171213"></a><ul id="ul7805230171213"><li>vo video layer status 2: disp_buf_len</li><li>vo interface status:<a name="ul7805103031214"></a><a name="ul7805103031214"></a><ul id="ul7805103031214"><li>vtth less_buf_enable</li><li>less_buf_vtth</li></ul>
</li></ul>
</td>
</tr>
<tr id="row12805103081214"><td class="cellrowborder" valign="top" width="13.171317131713172%" headers="mcps1.1.7.1.1 "><p id="p138052302125"><a name="p138052302125"></a><a name="p138052302125"></a>Multi-region mode VO buffer-saving solution</p>
</td>
<td class="cellrowborder" valign="top" width="22.472247224722473%" headers="mcps1.1.7.1.2 "><a name="ul880510305120"></a><a name="ul880510305120"></a><ul id="ul880510305120"><li>ss_mpi_vo_set_video_layer_attr</li><li>ss_mpi_vo_set_vtth</li><li>ss_mpi_vo_set_less_buf_attr</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.7.1.3 "><p id="p13806930171214"><a name="p13806930171214"></a><a name="p13806930171214"></a>Reduces one display buffer in multi-region mode</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.1.7.1.4 "><p id="p7806630101210"><a name="p7806630101210"></a><a name="p7806630101210"></a>May cause display stuttering</p>
</td>
<td class="cellrowborder" valign="top" width="13.251325132513253%" headers="mcps1.1.7.1.5 "><p id="p38061330201212"><a name="p38061330201212"></a><a name="p38061330201212"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.382338233823383%" headers="mcps1.1.7.1.6 "><a name="ul17806230151216"></a><a name="ul17806230151216"></a><ul id="ul17806230151216"><li>vo video layer status 2: disp_buf_len</li><li>vo interface status:<a name="ul208061230171217"></a><a name="ul208061230171217"></a><ul id="ul208061230171217"><li>vtth less_buf_enable</li><li>less_buf_vtth</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **Note:**
>For details, see the "Video Output" chapter of the "MPP Media Processing Software V5.0 Development Reference". ## GFBG<a name="ZH-CN_TOPIC_0000002457839797"></a> When loading the ko, the video memory size for the overlay graphics layer is calculated based on pixel format, resolution, and buffer mode. The user can determine the required video memory size based on the actual usage scenario. Uncompressed: Allocated by calculating based on actual UI size, pixel format, and single/double BUF. Example: 1080P argb8888 double buf mode, ```
buf_size = 1920 * 4 * 1080 * 2 / 1024 = 16200KB
``` Compressed: For argb8888 pixel format with width >= 320, memory savings of 45% compared to uncompressed: Example: 1080P argb8888 double buf mode, ```
buf_size = (1920 * 4 * 1080 * 2 / 1024) * 55% = 8910KB
``` online drawing can save G3 MMZ memory. If G3 is only used for online drawing, G3 MMZ may not be allocated. The same applies for G4 when used for online drawing. <a name="table950mcpsimp"></a>
<table><thead align="left"><tr id="row959mcpsimp"><th class="cellrowborder" valign="top" width="13%" id="mcps1.1.7.1.1"><p id="p961mcpsimp"><a name="p961mcpsimp"></a><a name="p961mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="19.63%" id="mcps1.1.7.1.2"><p id="p963mcpsimp"><a name="p963mcpsimp"></a><a name="p963mcpsimp"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="19.66%" id="mcps1.1.7.1.3"><p id="p965mcpsimp"><a name="p965mcpsimp"></a><a name="p965mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="16.76%" id="mcps1.1.7.1.4"><p id="p967mcpsimp"><a name="p967mcpsimp"></a><a name="p967mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="18.95%" id="mcps1.1.7.1.5"><p id="p969mcpsimp"><a name="p969mcpsimp"></a><a name="p969mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.7.1.6"><p id="p971mcpsimp"><a name="p971mcpsimp"></a><a name="p971mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row973mcpsimp"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.1 "><p id="p975mcpsimp"><a name="p975mcpsimp"></a><a name="p975mcpsimp"></a>Set appropriate graphics layer physical video memory</p>
</td>
<td class="cellrowborder" valign="top" width="19.63%" headers="mcps1.1.7.1.2 "><p id="p977mcpsimp"><a name="p977mcpsimp"></a><a name="p977mcpsimp"></a>video</p>
</td>
<td class="cellrowborder" valign="top" width="19.66%" headers="mcps1.1.7.1.3 "><p id="p979mcpsimp"><a name="p979mcpsimp"></a><a name="p979mcpsimp"></a>Set the appropriate graphics layer physical video memory based on the actual resolution to avoid memory waste.</p>
</td>
<td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.1.7.1.4 "><p id="p981mcpsimp"><a name="p981mcpsimp"></a><a name="p981mcpsimp"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="18.95%" headers="mcps1.1.7.1.5 "><p id="p983mcpsimp"><a name="p983mcpsimp"></a><a name="p983mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.6 "><p xml:lang="es-ES" id="p985mcpsimp"><a name="p985mcpsimp"></a><a name="p985mcpsimp"></a>mem_size</p>
</td>
</tr>
<tr id="row986mcpsimp"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.1 "><p id="p988mcpsimp"><a name="p988mcpsimp"></a><a name="p988mcpsimp"></a>Graphics layer scaling</p>
</td>
<td class="cellrowborder" valign="top" width="19.63%" headers="mcps1.1.7.1.2 "><p id="p990mcpsimp"><a name="p990mcpsimp"></a><a name="p990mcpsimp"></a>FBIOPUT_SCREENSIZE</p>
</td>
<td class="cellrowborder" valign="top" width="19.66%" headers="mcps1.1.7.1.3 "><p id="p992mcpsimp"><a name="p992mcpsimp"></a><a name="p992mcpsimp"></a>Can save some MMZ memory.</p>
</td>
<td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.1.7.1.4 "><p id="p994mcpsimp"><a name="p994mcpsimp"></a><a name="p994mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.95%" headers="mcps1.1.7.1.5 "><p id="p996mcpsimp"><a name="p996mcpsimp"></a><a name="p996mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.6 "><p id="entry997mcpsimpp0"><a name="entry997mcpsimpp0"></a><a name="entry997mcpsimpp0"></a>-</p>
</td>
</tr>
<tr id="row998mcpsimp"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.1 "><p id="p1000mcpsimp"><a name="p1000mcpsimp"></a><a name="p1000mcpsimp"></a>Online drawing</p>
</td>
<td class="cellrowborder" valign="top" width="19.63%" headers="mcps1.1.7.1.2 "><p id="p1002mcpsimp"><a name="p1002mcpsimp"></a><a name="p1002mcpsimp"></a>FBIO_DRAW_SMART_RECT</p>
</td>
<td class="cellrowborder" valign="top" width="19.66%" headers="mcps1.1.7.1.3 "><p id="p1004mcpsimp"><a name="p1004mcpsimp"></a><a name="p1004mcpsimp"></a>Can save G3 MMZ memory.</p>
</td>
<td class="cellrowborder" valign="top" width="16.76%" headers="mcps1.1.7.1.4 "><p id="p1006mcpsimp"><a name="p1006mcpsimp"></a><a name="p1006mcpsimp"></a>If G3 is used for SD layer display, the KO needs to be reloaded with sufficient memory allocated.</p>
</td>
<td class="cellrowborder" valign="top" width="18.95%" headers="mcps1.1.7.1.5 "><a name="ul49726222180"></a><a name="ul49726222180"></a><ul id="ul49726222180"><li>If G3 is only used for online drawing, G3 MMZ memory may not be allocated;</li><li>Supported by </li></ul>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.6 "><p id="p1010mcpsimp"><a name="p1010mcpsimp"></a><a name="p1010mcpsimp"></a>mem_size</p>
</td>
</tr>
</tbody>
</table> ## AUDIO<a name="ZH-CN_TOPIC_0000002457879961"></a> <a name="table1014mcpsimp"></a>
<table><thead align="left"><tr id="row1023mcpsimp"><th class="cellrowborder" valign="top" width="21.84%" id="mcps1.1.7.1.1"><p id="p1025mcpsimp"><a name="p1025mcpsimp"></a><a name="p1025mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="18.16%" id="mcps1.1.7.1.2"><p id="p1027mcpsimp"><a name="p1027mcpsimp"></a><a name="p1027mcpsimp"></a>Related Interface/Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.7.1.3"><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="22.71%" id="mcps1.1.7.1.4"><p id="p1031mcpsimp"><a name="p1031mcpsimp"></a><a name="p1031mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="5.83%" id="mcps1.1.7.1.5"><p id="p1033mcpsimp"><a name="p1033mcpsimp"></a><a name="p1033mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18.459999999999997%" id="mcps1.1.7.1.6"><p id="p1035mcpsimp"><a name="p1035mcpsimp"></a><a name="p1035mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row1037mcpsimp"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.7.1.1 "><p id="p1039mcpsimp"><a name="p1039mcpsimp"></a><a name="p1039mcpsimp"></a>Reasonable setting of channel count, AI cached audio frame count, and samples per frame per scenario.</p>
</td>
<td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.1.7.1.2 "><p id="p1838405575410"><a name="p1838405575410"></a><a name="p1838405575410"></a>ss_mpi_ai_set_pub_attr: chn_cnt, frame_num, point_num_per_frame</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.3 "><p id="p1043mcpsimp"><a name="p1043mcpsimp"></a><a name="p1043mcpsimp"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="22.71%" headers="mcps1.1.7.1.4 "><p id="p1045mcpsimp"><a name="p1045mcpsimp"></a><a name="p1045mcpsimp"></a>The user must ensure the buffer size is set appropriately; otherwise, anomalies such as capture frame dropping may occur.</p>
</td>
<td class="cellrowborder" valign="top" width="5.83%" headers="mcps1.1.7.1.5 "><p id="p1047mcpsimp"><a name="p1047mcpsimp"></a><a name="p1047mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.1.7.1.6 "><p id="p1049mcpsimp"><a name="p1049mcpsimp"></a><a name="p1049mcpsimp"></a>cat /proc/umap/ai</p>
<p id="p1050mcpsimp"><a name="p1050mcpsimp"></a><a name="p1050mcpsimp"></a>ai dev attr: chn_cnt, frame_num, point_num</p>
</td>
</tr>
<tr id="row1051mcpsimp"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.7.1.1 "><p id="p1053mcpsimp"><a name="p1053mcpsimp"></a><a name="p1053mcpsimp"></a>Reasonable setting of AENC cached audio frame size per scenario</p>
</td>
<td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.1.7.1.2 "><p id="p1055mcpsimp"><a name="p1055mcpsimp"></a><a name="p1055mcpsimp"></a>ss_mpi_aenc_create_chn: buf_size</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.3 "><p id="p1057mcpsimp"><a name="p1057mcpsimp"></a><a name="p1057mcpsimp"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="22.71%" headers="mcps1.1.7.1.4 "><p id="p1059mcpsimp"><a name="p1059mcpsimp"></a><a name="p1059mcpsimp"></a>The user must ensure the buffer size is set appropriately; otherwise, anomalies such as capture frame dropping may occur.</p>
</td>
<td class="cellrowborder" valign="top" width="5.83%" headers="mcps1.1.7.1.5 "><p id="p1061mcpsimp"><a name="p1061mcpsimp"></a><a name="p1061mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.1.7.1.6 "><p id="p1063mcpsimp"><a name="p1063mcpsimp"></a><a name="p1063mcpsimp"></a>cat /proc/umap/aenc</p>
<p id="p1064mcpsimp"><a name="p1064mcpsimp"></a><a name="p1064mcpsimp"></a>aenc chn attr: buf_size</p>
</td>
</tr>
<tr id="row1065mcpsimp"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.7.1.1 "><p id="p1067mcpsimp"><a name="p1067mcpsimp"></a><a name="p1067mcpsimp"></a>Reasonable setting of ADEC cached audio frame size per scenario</p>
</td>
<td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.1.7.1.2 "><p id="p1069mcpsimp"><a name="p1069mcpsimp"></a><a name="p1069mcpsimp"></a>ss_mpi_adec_create_chn: buf_size</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.3 "><p id="p1071mcpsimp"><a name="p1071mcpsimp"></a><a name="p1071mcpsimp"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="22.71%" headers="mcps1.1.7.1.4 "><p id="p1073mcpsimp"><a name="p1073mcpsimp"></a><a name="p1073mcpsimp"></a>The user must ensure the buffer size is set appropriately; otherwise, anomalies such as capture frame dropping may occur.</p>
</td>
<td class="cellrowborder" valign="top" width="5.83%" headers="mcps1.1.7.1.5 "><p id="p1075mcpsimp"><a name="p1075mcpsimp"></a><a name="p1075mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.1.7.1.6 "><p id="p1077mcpsimp"><a name="p1077mcpsimp"></a><a name="p1077mcpsimp"></a>cat /proc/umap/adec</p>
<p id="p1078mcpsimp"><a name="p1078mcpsimp"></a><a name="p1078mcpsimp"></a>adec chn attr: buf_size</p>
</td>
</tr>
<tr id="row1079mcpsimp"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.7.1.1 "><p id="p1081mcpsimp"><a name="p1081mcpsimp"></a><a name="p1081mcpsimp"></a>Reasonable setting of channel count, AO cached audio frame count, and samples per frame per scenario.</p>
</td>
<td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.1.7.1.2 "><p id="p1083mcpsimp"><a name="p1083mcpsimp"></a><a name="p1083mcpsimp"></a>ss_mpi_ao_set_pub_attr: chn_cnt, frame_num, point_num_per_frame</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.3 "><p id="p1085mcpsimp"><a name="p1085mcpsimp"></a><a name="p1085mcpsimp"></a>Can save some OS memory</p>
</td>
<td class="cellrowborder" valign="top" width="22.71%" headers="mcps1.1.7.1.4 "><p id="p1087mcpsimp"><a name="p1087mcpsimp"></a><a name="p1087mcpsimp"></a>The user must ensure the buffer size is set appropriately; otherwise, anomalies such as capture frame dropping may occur.</p>
</td>
<td class="cellrowborder" valign="top" width="5.83%" headers="mcps1.1.7.1.5 "><p id="p1089mcpsimp"><a name="p1089mcpsimp"></a><a name="p1089mcpsimp"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.1.7.1.6 "><p id="p1091mcpsimp"><a name="p1091mcpsimp"></a><a name="p1091mcpsimp"></a>cat /proc/umap/ao</p>
<p id="p14811853289"><a name="p14811853289"></a><a name="p14811853289"></a>ao dev attr: chn_cnt,</p>
<p id="p1092mcpsimp"><a name="p1092mcpsimp"></a><a name="p1092mcpsimp"></a>frame_num, point_num</p>
</td>
</tr>
</tbody>
</table> >![](public_sys-resources/icon-note.gif) **Note:**
>Refer to the "Audio" chapter of the "MPP Media Processing Software V5.0 Development Reference". ## REGION<a name="ZH-CN_TOPIC_0000002457879937"></a> - Set the width and height specified by the user for the ping-pong buffer as small as possible based on requirements.
- When the region type is overlay/overlayex, pixel\_format can be set to CLUT2/CLUT4. CLUT2 can save 7/8 memory compared to ARGB1555, and CLUT4 can save 3/4 memory compared to 1555. This method will reduce image quality.
- overlay/overlayex can use single-buff mode by setting canvas\_num in the region attribute to 1. When the image needs frequent refreshing, tearing effects may occur.
- Refer to the "Region Management" chapter of the "MPP Media Processing Software V5.0 Development Reference". Use the command cat /proc/umap/rgn to view proc information. <a name="table895mcpsimp"></a>
<table><thead align="left"><tr id="row904mcpsimp"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.7.1.1"><p id="p906mcpsimp"><a name="p906mcpsimp"></a><a name="p906mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="18.5%" id="mcps1.1.7.1.2"><p id="p908mcpsimp"><a name="p908mcpsimp"></a><a name="p908mcpsimp"></a>Related Module Parameter/Interface</p>
</th>
<th class="cellrowborder" valign="top" width="19.580000000000002%" id="mcps1.1.7.1.3"><p id="p910mcpsimp"><a name="p910mcpsimp"></a><a name="p910mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="9.87%" id="mcps1.1.7.1.4"><p id="p912mcpsimp"><a name="p912mcpsimp"></a><a name="p912mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="18.509999999999998%" id="mcps1.1.7.1.5"><p id="p914mcpsimp"><a name="p914mcpsimp"></a><a name="p914mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18.54%" id="mcps1.1.7.1.6"><p id="p916mcpsimp"><a name="p916mcpsimp"></a><a name="p916mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row917mcpsimp"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.7.1.1 "><p id="p919mcpsimp"><a name="p919mcpsimp"></a><a name="p919mcpsimp"></a>Use ARGB CLUT2 OVERLAY and OVERLAYEX_RGN</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.7.1.2 "><p id="p921mcpsimp"><a name="p921mcpsimp"></a><a name="p921mcpsimp"></a>ss_mpi_rgn_create: set pixel_format to OT_PIXEL_FORMAT_ARGB_CLUT2</p>
</td>
<td class="cellrowborder" valign="top" width="19.580000000000002%" headers="mcps1.1.7.1.3 "><p id="p923mcpsimp"><a name="p923mcpsimp"></a><a name="p923mcpsimp"></a>ARGB CLUT2 is 1/8 of ARGB 1555 and 1/16 of ARGB 8888.</p>
</td>
<td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.1.7.1.4 "><p id="p925mcpsimp"><a name="p925mcpsimp"></a><a name="p925mcpsimp"></a>Can only display 4 colors</p>
</td>
<td class="cellrowborder" valign="top" width="18.509999999999998%" headers="mcps1.1.7.1.5 "><p id="p927mcpsimp"><a name="p927mcpsimp"></a><a name="p927mcpsimp"></a>When multiple OS Ds overlap, the higher-layer OSD will cover the lower-layer OSD.</p>
</td>
<td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.7.1.6 "><p id="p929mcpsimp"><a name="p929mcpsimp"></a><a name="p929mcpsimp"></a>region status of overlay: pixel_format;</p>
<p id="p930mcpsimp"><a name="p930mcpsimp"></a><a name="p930mcpsimp"></a>region status of overlayex: pixel_format</p>
</td>
</tr>
<tr id="row931mcpsimp"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.7.1.1 "><p id="p933mcpsimp"><a name="p933mcpsimp"></a><a name="p933mcpsimp"></a>Use ARGB CLUT4 OVERLAY and OVERLAYEX_RGN</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.7.1.2 "><p id="p935mcpsimp"><a name="p935mcpsimp"></a><a name="p935mcpsimp"></a>ss_mpi_rgn_create: set pixel_format to OT_PIXEL_FORMAT_ARGB_CLUT4</p>
</td>
<td class="cellrowborder" valign="top" width="19.580000000000002%" headers="mcps1.1.7.1.3 "><p id="p937mcpsimp"><a name="p937mcpsimp"></a><a name="p937mcpsimp"></a>ARGB CLUT4 is 1/4 of ARGB 1555 and 1/8 of ARGB 8888.</p>
</td>
<td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.1.7.1.4 "><p id="p939mcpsimp"><a name="p939mcpsimp"></a><a name="p939mcpsimp"></a>Can only display 16 colors</p>
</td>
<td class="cellrowborder" valign="top" width="18.509999999999998%" headers="mcps1.1.7.1.5 "><p id="p941mcpsimp"><a name="p941mcpsimp"></a><a name="p941mcpsimp"></a>When multiple OS Ds overlap, the higher-layer OSD will cover the lower-layer OSD.</p>
</td>
<td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.7.1.6 "><p id="p943mcpsimp"><a name="p943mcpsimp"></a><a name="p943mcpsimp"></a>region status of overlay: pixel_format;</p>
<p id="p944mcpsimp"><a name="p944mcpsimp"></a><a name="p944mcpsimp"></a>region status of overlayex: pixel_format</p>
</td>
</tr>
</tbody>
</table> ## SVP<a name="ZH-CN_TOPIC_0000002457839821"></a> **SVP\_NNN<a name="section72111374332"></a>** 1. Configuration parameters during model conversion - ATC --batch\_num parameter set to 1 to reduce input/output and workbuf memory usage. - ATC --online\_model\_type parameter set to 0. This configuration prevents the converted model from carrying debug-related information, reducing model memory usage. 2. Quantization parameter configuration - activation\_quant\_params - num\_bits set to 8 - weight\_quant\_params - num\_bits set to 4 Note: This configuration will affect model accuracy. 3. KO module parameters The number of task nodes can be changed via the module parameter svp\_nnn\_max\_task\_node\_num, thereby reducing the mmz memory occupied by task nodes. 4. Workbuf sharing Multiple models on the same stream can share the same workbuf, thereby reducing mmz memory usage. >![](public_sys-resources/icon-note.gif) **Note:** **NNN<a name="section1727814121310"></a>** 1. Configuration parameter during model conversion: ATC -enable\_single\_stream=true, enabling one model to use one stream.
2. When multiple models perform inference sequentially, use aclmdl Load From File With Mem or aclmdl Load From Mem With Mem loading methods to manually allocate workbuf memory, and then have multiple models share the same working memory, thereby reducing mmz memory usage. **IVE<a name="section151011750183319"></a>** 1. MD proc information memory is only allocated when MD is supported.
2. If the user does not call IVE's resize, kcf, and csc operators, the corresponding auxiliary memory for resize, kcf, and csc will not be allocated.
3. The number of linked list nodes can be controlled by configuring the module parameter max\_node\_num, reducing the MMZ memory occupied by linked list nodes. **KCF<a name="section1668375619333"></a>** Reducing the number of cores used can reduce memory usage. **MAU<a name="section15117207183413"></a>** 1. If the user does not call the ss\_mpi\_svp\_mau\_add\_mem\_info interface to record mem\_info, the mem\_info linked list memory will not be allocated. If the user needs to call the ss\_mpi\_svp\_mau\_add\_mem\_info interface to record mem\_info, the memory size for storing mem\_info can be controlled by configuring the module parameter mau\_max\_mem\_info\_num.
2. The number of linked list nodes can be controlled by configuring the module parameter mau\_max\_node\_num, reducing the MMZ memory occupied by linked list nodes. ## VDA<a name="ZH-CN_TOPIC_0000002424361054"></a> When loading the vda module ko, set the module parameter for the maximum channel count g\_vda\_max\_chn\_num to save OS memory. ## PCIV<a name="ZH-CN_TOPIC_0000002424201186"></a> - Window occupancy: If no DMA tasks initiated by the master chip are involved, the window space does not need to be allocated. Note that if the window space is not allocated, care must be taken regarding mmz space integrity so that it is not split by pcie\_mcc space.
- VB rotation occupancy: - Master chip rotation VB: Used for receiving bound images. If only DMA functionality is used, it may not be allocated. If transmission efficiency is sufficient (small images, low frame rate), single-buff can be used with only one allocation. - Slave chip rotation VB: When receiving bound images, use pass-through mode if possible. When only using DMA transmission, rotation V Bs are not occupied or allocated. ## GDC<a name="ZH-CN_TOPIC_0000002424201222"></a> The GDC module mainly uses OS memory and node mmz. Considering the scenario, reducing the maximum job count, maximum task count, and maximum node count can reduce OS memory usage and node-occupied MMZ memory. ## CIPHER<a name="ZH-CN_TOPIC_0000002424361050"></a> <a name="table830mcpsimp"></a>
<table><thead align="left"><tr id="row839mcpsimp"><th class="cellrowborder" valign="top" width="17.419999999999998%" id="mcps1.1.7.1.1"><p id="p841mcpsimp"><a name="p841mcpsimp"></a><a name="p841mcpsimp"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="22.3%" id="mcps1.1.7.1.2"><p id="p843mcpsimp"><a name="p843mcpsimp"></a><a name="p843mcpsimp"></a>Related Module Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.28%" id="mcps1.1.7.1.3"><p id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="20.77%" id="mcps1.1.7.1.4"><p id="p847mcpsimp"><a name="p847mcpsimp"></a><a name="p847mcpsimp"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="6.22%" id="mcps1.1.7.1.5"><p id="p849mcpsimp"><a name="p849mcpsimp"></a><a name="p849mcpsimp"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18.01%" id="mcps1.1.7.1.6"><p id="p851mcpsimp"><a name="p851mcpsimp"></a><a name="p851mcpsimp"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row853mcpsimp"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.1.7.1.1 "><p id="p984254755612"><a name="p984254755612"></a><a name="p984254755612"></a>Configure internal fixed memory size for Hash initialization</p>
</td>
<td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.1.7.1.2 "><p id="p12945124118249"><a name="p12945124118249"></a><a name="p12945124118249"></a>HASH_MAX_DEPTH;</p>
<a name="ul118251049224"></a><a name="ul118251049224"></a><ul id="ul118251049224"><li>ss_mpi_cipher_hash_updata/in_data_len</li><li>ss_mpi_cipher_hash_final/out_hash_len</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.3 "><p id="p1284115478563"><a name="p1284115478563"></a><a name="p1284115478563"></a>Reduces the length of MMZ memory allocated internally by the driver</p>
</td>
<td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.1.7.1.4 "><p id="p48401647185612"><a name="p48401647185612"></a><a name="p48401647185612"></a>Can reduce linked list depth to decrease total linked list memory size; or modify the HASH message length based on the actual scenario to reduce allocated physical memory.</p>
</td>
<td class="cellrowborder" valign="top" width="6.22%" headers="mcps1.1.7.1.5 "><p id="p11840154735613"><a name="p11840154735613"></a><a name="p11840154735613"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.1.7.1.6 "><p id="p12841158984"><a name="p12841158984"></a><a name="p12841158984"></a>cat /proc/umap/cipher</p>
</td>
</tr>
<tr id="row866mcpsimp"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.1.7.1.1 "><p id="p783944795612"><a name="p783944795612"></a><a name="p783944795612"></a>Configure internal fixed memory size for Cipher driver module initialization</p>
</td>
<td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.1.7.1.2 "><p id="p185517264245"><a name="p185517264245"></a><a name="p185517264245"></a>SYMC_MAX_LIST_NUM;</p>
<p id="p99571310132316"><a name="p99571310132316"></a><a name="p99571310132316"></a>Disable CHIP_AES_CCM_GCM_SUPPORT macro</p>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.3 "><p id="p1582234675918"><a name="p1582234675918"></a><a name="p1582234675918"></a>Reduces the length of MMZ memory allocated internally by the driver</p>
</td>
<td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.1.7.1.4 "><p id="p0838124714568"><a name="p0838124714568"></a><a name="p0838124714568"></a>Can reduce linked list depth to decrease total linked list memory size; can remove the padding buffer allocated for CCM/GCM if not used in the actual scenario.</p>
</td>
<td class="cellrowborder" valign="top" width="6.22%" headers="mcps1.1.7.1.5 "><p id="p983644711566"><a name="p983644711566"></a><a name="p983644711566"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.1.7.1.6 "><p id="p8556357584"><a name="p8556357584"></a><a name="p8556357584"></a>cat /proc/umap/cipher</p>
</td>
</tr>
<tr id="row879mcpsimp"><td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.1.7.1.1 "><p id="p18835174710564"><a name="p18835174710564"></a><a name="p18835174710564"></a>Reasonable design of cipher encryption/decryption memory length per scenario</p>
</td>
<td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.1.7.1.2 "><a name="ul171531719152213"></a><a name="ul171531719152213"></a><ul id="ul171531719152213"><li>ss_mpi_cipher_encrypt/byte_len</li><li>ss_mpi_cipher_decrypt/byte_len</li></ul>
</td>
<td class="cellrowborder" valign="top" width="15.28%" headers="mcps1.1.7.1.3 "><p id="p3270357175918"><a name="p3270357175918"></a><a name="p3270357175918"></a>Reduces the length of MMZ memory passed in by the user-layer interface</p>
</td>
<td class="cellrowborder" valign="top" width="20.77%" headers="mcps1.1.7.1.4 "><p id="p1583310471568"><a name="p1583310471568"></a><a name="p1583310471568"></a>Passing an appropriate MMZ memory allocation length from the user-layer interface based on the actual scenario can save some MMZ memory.</p>
</td>
<td class="cellrowborder" valign="top" width="6.22%" headers="mcps1.1.7.1.5 "><p id="p88331847135614"><a name="p88331847135614"></a><a name="p88331847135614"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.1.7.1.6 "><p id="p10415503816"><a name="p10415503816"></a><a name="p10415503816"></a>cat /proc/umap/cipher</p>
</td>
</tr>
</tbody>
</table> ## ISP<a name="ZH-CN_TOPIC_0000002457839833"></a> <a name="table1014mcpsimp"></a>
<table><thead align="left"><tr id="row1023mcpsimp"><th class="cellrowborder" valign="top" width="18.85%" id="mcps1.1.7.1.1"><p id="p149138502109"><a name="p149138502109"></a><a name="p149138502109"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="21.15%" id="mcps1.1.7.1.2"><p id="p791315018106"><a name="p791315018106"></a><a name="p791315018106"></a>Related Interface/Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.7.1.3"><p id="p1091311503101"><a name="p1091311503101"></a><a name="p1091311503101"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.1.7.1.4"><p id="p19131450171012"><a name="p19131450171012"></a><a name="p19131450171012"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="7.000000000000001%" id="mcps1.1.7.1.5"><p id="p1891335012102"><a name="p1891335012102"></a><a name="p1891335012102"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.7.1.6"><p id="p13913195017105"><a name="p13913195017105"></a><a name="p13913195017105"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row1037mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.1.7.1.1 "><p id="p1291355081015"><a name="p1291355081015"></a><a name="p1291355081015"></a>For offline channels, reasonably set the number of be config buffers per scenario.</p>
</td>
<td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.7.1.2 "><p id="p5913250161013"><a name="p5913250161013"></a><a name="p5913250161013"></a>ss_mpi_isp_set_ctrl_param: be_buf_num</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.3 "><p id="p169131950131013"><a name="p169131950131013"></a><a name="p169131950131013"></a>Can save some MMZ memory</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.7.1.4 "><p id="p11914450181013"><a name="p11914450181013"></a><a name="p11914450181013"></a>The user must ensure the buffer size is set appropriately; otherwise, anomalies in obtaining the be config buffer may occur.</p>
</td>
<td class="cellrowborder" valign="top" width="7.000000000000001%" headers="mcps1.1.7.1.5 "><p id="p291416504107"><a name="p291416504107"></a><a name="p291416504107"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.7.1.6 "><p id="p19145507107"><a name="p19145507107"></a><a name="p19145507107"></a>cat /proc/umap/isp</p>
<p id="p791435061019"><a name="p791435061019"></a><a name="p791435061019"></a>module/control param: be_buf_num</p>
</td>
</tr>
</tbody>
</table> ## HNR<a name="ZH-CN_TOPIC_0000002457879953"></a> <a name="table779695811439"></a>
<table><thead align="left"><tr id="row12796125817436"><th class="cellrowborder" valign="top" width="18.85%" id="mcps1.1.7.1.1"><p id="p19796115817439"><a name="p19796115817439"></a><a name="p19796115817439"></a>Measure</p>
</th>
<th class="cellrowborder" valign="top" width="21.15%" id="mcps1.1.7.1.2"><p id="p12796135814312"><a name="p12796135814312"></a><a name="p12796135814312"></a>Related Interface/Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.7.1.3"><p id="p479615589438"><a name="p479615589438"></a><a name="p479615589438"></a>Benefit</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.1.7.1.4"><p id="p8796125824310"><a name="p8796125824310"></a><a name="p8796125824310"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="7.000000000000001%" id="mcps1.1.7.1.5"><p id="p279685864318"><a name="p279685864318"></a><a name="p279685864318"></a>Note</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.7.1.6"><p id="p2796458184319"><a name="p2796458184319"></a><a name="p2796458184319"></a>Proc Info</p>
</th>
</tr>
</thead>
<tbody><tr id="row2079611581437"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.1.7.1.1 "><p id="p1179775812433"><a name="p1179775812433"></a><a name="p1179775812433"></a>In VI stagger input scenario and VI video mode is OT_VI_VIDEO_MODE_NORM</p>
</td>
<td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.7.1.2 "><p id="p17960913104414"><a name="p17960913104414"></a><a name="p17960913104414"></a>ss_mpi_hnr_attach_out_vb_pool: ot_vb_pool</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.7.1.3 "><p id="p11797165815432"><a name="p11797165815432"></a><a name="p11797165815432"></a>Can save MMZ memory</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.7.1.4 "><p id="p5797558174319"><a name="p5797558174319"></a><a name="p5797558174319"></a>The user must ensure VB size and count are set appropriately.</p>
</td>
<td class="cellrowborder" valign="top" width="7.000000000000001%" headers="mcps1.1.7.1.5 "><p id="p079715824315"><a name="p079715824315"></a><a name="p079715824315"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.7.1.6 "><p id="p4797858184315"><a name="p4797858184315"></a><a name="p4797858184315"></a>cat /proc/umap/vb</p>
</td>
</tr>
</tbody>
</table> # Other Measures
## Limit Stack Size<a name="ZH-CN_TOPIC_0000002457879969"></a> The default stack size is 8192KB. If memory is limited, thread creation may fail. Based on the actual stack space required by the application, modify the stack size limit to 1024KB. If the application uses even less, it can be changed to 512KB or smaller. There are two methods to modify the stack size: - Use the `ulimit -s 1024` command, called once before the application starts;
- Call the `pthread_attr_setstacksize` function at the beginning of the main function to modify the stack space for a single application. ## Optimize Memory Usage in Code<a name="ZH-CN_TOPIC_0000002457839805"></a> Optimize memory usage in code, especially for stack, heap, constants, and global variables. Key points to note: - Avoid declaring variables that are not used after allocation in application code;
- Do not arbitrarily allocate large blocks of memory; allocate only as much as needed;
- Redundant memory usage also includes initialization of unused functional modules. ## Disable Process Creation Functions like fork and system in Applications<a name="ZH-CN_TOPIC_0000002457839829"></a> Since the main process data segment already occupies significant memory, forking a child process will certainly consume substantial memory and has a high probability of failure. Therefore, process creation functions such as fork and system should be disabled in applications: for example, bspmm calls, mkfs.vfat calls, etc. ## Remove Unnecessary Modules Based on the Scenario<a name="ZH-CN_TOPIC_0000002424361062"></a> Removing unnecessary modules can reduce memory usage, for example: - When using gfbg 0buffer or standard mode, TDE may not be loaded. If TDE is not loaded, REGION uses memcpy for Overlay/Overlay Ex copying.
- When audio input and encoding are not needed, AI and VENC may not be loaded.
- When REGION functions are not needed, REGION may not be loaded.
- When JPEGE is not needed, the jpege module may not be loaded.
