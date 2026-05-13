---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/MPP 媒体处理软件 V5.0 FAQ/MPP 媒体处理软件 V5.0 FAQ.md
--- # Preface
**Overview<a name="section102mcpsimp"></a>** This document is written for programmers developing with the MPP media processing software. Its purpose is to provide solutions and assistance for problems encountered during development. >![](public_sys-resources/icon-note.gif) **Note:**
>Unless otherwise specified, the content for is identical to Hi3403V100. **Product Version<a name="section105mcpsimp"></a>** The product version corresponding to this document is as follows. <a name="table108mcpsimp"></a>
<table><thead align="left"><tr id="row113mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p115mcpsimp"><a name="p115mcpsimp"></a><a name="p115mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p117mcpsimp"><a name="p117mcpsimp"></a><a name="p117mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row119mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p121mcpsimp"><a name="p121mcpsimp"></a><a name="p121mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p123mcpsimp"><a name="p123mcpsimp"></a><a name="p123mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p128mcpsimp"><a name="p128mcpsimp"></a><a name="p128mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p34921898474"><a name="p34921898474"></a><a name="p34921898474"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p143761152041"><a name="p143761152041"></a><a name="p143761152041"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p64271955205915"><a name="p64271955205915"></a><a name="p64271955205915"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p107354154419"><a name="p107354154419"></a><a name="p107354154419"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Target Audience<a name="section129mcpsimp"></a>** This document is mainly intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions<a name="section135mcpsimp"></a>** The following symbols may appear in this document. Their meanings are as follows. <a name="table138mcpsimp"></a>
<table><thead align="left"><tr id="row143mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p145mcpsimp"><a name="p145mcpsimp"></a><a name="p145mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p147mcpsimp"><a name="p147mcpsimp"></a><a name="p147mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row149mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p151mcpsimp"><a name="p151mcpsimp"></a><a name="p151mcpsimp"></a><a name="image102"></a><a name="image102"></a><span><img id="image102" src="figures/zh-cn_image_0000002408115790.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p153mcpsimp"><a name="p153mcpsimp"></a><a name="p153mcpsimp"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Register Access Type Conventions<a name="section176mcpsimp"></a>** <a name="table178mcpsimp"></a>
<table><thead align="left"><tr id="row185mcpsimp"><th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.1"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.1.5.1.2"><p id="p189mcpsimp"><a name="p189mcpsimp"></a><a name="p189mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.3"><p id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.5.1.4"><p id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row195mcpsimp"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.1 "><p id="p197mcpsimp"><a name="p197mcpsimp"></a><a name="p197mcpsimp"></a>RO</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.5.1.2 "><p id="p199mcpsimp"><a name="p199mcpsimp"></a><a name="p199mcpsimp"></a>Read only, not writable.</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a>RW</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>Readable and writable.</p>
</td>
</tr>
</tbody>
</table> **Numeric Unit Conventions<a name="section219mcpsimp"></a>** The representation of data capacity, frequency, data rate, etc., is described as follows. <a name="table222mcpsimp"></a>
<table><thead align="left"><tr id="row228mcpsimp"><th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.1.4.1.1"><p id="p230mcpsimp"><a name="p230mcpsimp"></a><a name="p230mcpsimp"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.4.1.2"><p id="p232mcpsimp"><a name="p232mcpsimp"></a><a name="p232mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="40.40404040404041%" id="mcps1.1.4.1.3"><p id="p234mcpsimp"><a name="p234mcpsimp"></a><a name="p234mcpsimp"></a>Corresponding Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row236mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="39.39393939393939%" headers="mcps1.1.4.1.1 "><p id="p238mcpsimp"><a name="p238mcpsimp"></a><a name="p238mcpsimp"></a>Data capacity (e.g., RAM capacity)</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.4.1.2 "><p id="p240mcpsimp"><a name="p240mcpsimp"></a><a name="p240mcpsimp"></a>1K</p>
</td>
<td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.1.4.1.3 "><p id="p242mcpsimp"><a name="p242mcpsimp"></a><a name="p242mcpsimp"></a>1024</p>
</td>
</tr>
<tr id="row253mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="39.39393939393939%" headers="mcps1.1.4.1.1 "><p id="p255mcpsimp"><a name="p255mcpsimp"></a><a name="p255mcpsimp"></a>Frequency, data rate, etc.</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.4.1.2 "><p id="p257mcpsimp"><a name="p257mcpsimp"></a><a name="p257mcpsimp"></a>1k</p>
</td>
<td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.1.4.1.3 "><p id="p259mcpsimp"><a name="p259mcpsimp"></a><a name="p259mcpsimp"></a>1000</p>
</td>
</tr>
</tbody>
</table> Address and data representations are described as follows. <a name="table271mcpsimp"></a>
<table><thead align="left"><tr id="row277mcpsimp"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.1"><p id="p279mcpsimp"><a name="p279mcpsimp"></a><a name="p279mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.1.4.1.2"><p id="p281mcpsimp"><a name="p281mcpsimp"></a><a name="p281mcpsimp"></a>Example</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.1.4.1.3"><p id="p283mcpsimp"><a name="p283mcpsimp"></a><a name="p283mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row285mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.1 "><p id="p287mcpsimp"><a name="p287mcpsimp"></a><a name="p287mcpsimp"></a>0x</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.4.1.2 "><p id="p289mcpsimp"><a name="p289mcpsimp"></a><a name="p289mcpsimp"></a>0x FE04, 0x18</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.4.1.3 "><p id="p291mcpsimp"><a name="p291mcpsimp"></a><a name="p291mcpsimp"></a>Hexadecimal data values and address values.</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section342mcpsimp"></a>** The revision history accumulates update descriptions for each document version. The latest version of this document contains updates from all previous versions. <a name="table2674mcpsimp"></a>
<table><thead align="left"><tr id="row2680mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2682mcpsimp"><a name="p2682mcpsimp"></a><a name="p2682mcpsimp"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p2685mcpsimp"><a name="p2685mcpsimp"></a><a name="p2685mcpsimp"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p2688mcpsimp"><a name="p2688mcpsimp"></a><a name="p2688mcpsimp"></a>Revision Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2699mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2701mcpsimp"><a name="p2701mcpsimp"></a><a name="p2701mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p2703mcpsimp"><a name="p2703mcpsimp"></a><a name="p2703mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p2705mcpsimp"><a name="p2705mcpsimp"></a><a name="p2705mcpsimp"></a>First interim release.</p>
</td>
</tr>
</tbody>
</table> # System Control
## Log Information<a name="ZH-CN_TOPIC_0000002408115570"></a> ### How to View MPP Log Information<a name="ZH-CN_TOPIC_0000002408275458"></a> [Phenomenon] Need to view logs and adjust log levels. [Analysis] Log records record the causes of SDK runtime errors, approximate locations, and some system running status information. Therefore, viewing logs can assist in error localization. Currently, logs have 7 levels. The default setting is level 3. The higher the level setting, the more information is recorded in the log. When the level is 7, the entire system running status is recorded in real time. The amount of information at this level is very large and will significantly reduce overall system performance. Therefore, under normal circumstances, level 3 is recommended, because at this level, information is only recorded when an error occurs, helping to locate most errors. [Solution] Commands for obtaining logs or modifying log levels are as follows: - To view the log level of each module, use **cat /proc/umap/logmpp**. This command lists all module log levels.
- To modify the log level of a specific module, use **echo "venc=4" > /proc/umap/logmpp**, where venc is the module name, matching the module names listed by the cat command.
- To modify the log level of all modules, use **echo "all=4" > /proc/umap/logmpp**.
- To obtain log records, use **cat /dev/logmpp**. This command prints all log information. If the logs have been read, the command blocks and waits for new log information. Use Ctrl+C to exit. To avoid blocking and waiting, use **echo wait=0 > /proc/umap/logmpp** to cancel blocking wait. You can also use system calls such as open and read to operate the /dev/logmpp device node. ## Memory Usage<a name="ZH-CN_TOPIC_0000002441714813"></a> ### OS Reserved Memory and Thread Stack Size Adjustment<a name="ZH-CN_TOPIC_0000002408115550"></a> [Phenomenon] Linux system running business programs shows oom-killer. [Analysis] Possible causes include: - Insufficient OS memory
- System reserved memory too small [Solution] - Increase OS memory
- Increase system reserved memory. Add the following commands to /etc/profile to set the system reserved memory to 4MB (adjustable): echo 2 > /proc/sys/kernel/randomize\_va\_space echo 4096 > /proc/sys/vm/min\_free\_kbytes [Phenomenon] The system shows thread creation failure with error: pthread\_create: Resource temporarily unavailable. [Analysis] Possible causes include: - Insufficient OS memory
- Thread stack space too large [Solution] - Increase OS memory
- Adjust the maximum thread stack space size. There are 2 methods: - Use `ulimit -s` to modify the thread stack size in Linux, e.g., set to 1MB: `ulimit -s 1024`. Add this command to /etc/profile to set the stack size at boot. - Use `pthread_attr_setstacksize` to change the thread stack size in the program. ### How to Adjust Media Business Memory Based on Specific Products<a name="ZH-CN_TOPIC_0000002408275686"></a> [Phenomenon] Media services require a certain amount of memory (mainly MMZ memory) to support normal operation. The MPP platform allocates memory based on typical business patterns. When product memory usage is tight, users can try related strategies to adjust memory allocation based on actual conditions. [Analysis] For products with tight memory usage, the SDK software in the delivery package provides some methods to adjust memory allocation. This section only briefly describes memory reduction measures. Refer to related documents for specific usage. [Solution] 1. Confirm OS and MMZ memory allocation. See the "Address Space Allocation and Usage" section in the document "S Sxxxx SDK Installation and Upgrade Instructions". 2. Adjust SDK-related business memory usage based on actual conditions. - All resolution image sizes should be integer multiples of each other. For example, 1080P is 1920x1080, 960H is 960x480. Situations like 960H being 960x756 should not occur. Also, the case where VI captures 1920x1088 images but VENC encodes 1920x1080 should not occur. - Minimum buffer configuration for each module: refer to "MPP Media Processing Software V5.0 Development Reference". - Public VB pool should be exactly sufficient. Related interface: ss\_mpi\_vb\_set\_cfg. Refer to the "System Control" chapter of "MPP Media Processing Software V5.0 Development Reference". **Special note: the calculation of VB size for each module's output data is complex. Refer to the ot\_buffer.h code for specific formulas.** How to confirm sufficiency: In the VB proc information, pools with "is\_comm =1" are public VB pools. Ensure min\_free = 0 for the public VB pool and no module prints that VB cannot be obtained in logmpp. - Use compact segment compression to save memory and bandwidth. For example, VI and VPSS channels can use compact segment compression for writing. - DDR miniaturization measures per module. Refer to the "DDR Miniaturization Guide". ### MMZ Information<a name="ZH-CN_TOPIC_0000002408115714"></a> Customers can use `cat /proc/umap/media-mem` to view current system MMZ information and usage: ---ZONE: PHYS(0x64100000, 0x BFFFFFFF), GFP=0, n BYTES=1506304KB, NAME="anonymous" This indicates MMZ zone 0, named anonymous, MMZ range (0x64100000, 0x BFFFFFFF), size 1506304KB. If MMZ is divided into multiple ranges, there will be multiple ZON Es. ---MMZ\_USE\_INFO: total size=1512448KB(1477MB), used=86564KB(84MB + 548KB), remain=1425884KB(1392MB + 476KB), zone\_number=2, block\_number=16 This indicates overall MMZ statistics, including total MMZ size, used size, remaining size, number of ZON Es, etc. ### CMA Related<a name="ZH-CN_TOPIC_0000002441714865"></a> In projects such as Hi3403V100, CMA is enabled by default. When CMA is enabled, the system reserves a portion of memory by default. Only part of this reserved memory may be used. Therefore, to save memory, customers can use the following two methods: 1. Adjust the system reserved memory. Use `cat /proc/meminfo` to view the current system reserved CMA memory and its usage. Cma Total is the total reserved CMA memory, and Cma Free is the remaining memory: Cma Total: 16384 kB Cma Free: 16068 kB Customers can adjust the reserved memory size by modifying the kernel configuration: Device Drivers -> Generic Driver Options -> Size in Mega Bytes After modifying the kernel configuration, please recompile the kernel. 2. Disable CMA. If customers do not need the CMA feature, they can disable it by modifying the kernel configuration: Kernel Features -> Contiguous Memory Allocator After modifying the kernel configuration, please recompile the kernel and ot\_osal.ko. ## Performance Related<a name="ZH-CN_TOPIC_0000002441714777"></a> ### Effect and Impact of Adjusting USB Priority<a name="ZH-CN_TOPIC_0000002441714773"></a> On XVR platforms, if the mouse cursor drifts automatically, this can be resolved by increasing the USB module priority. The method for adjusting USB module priority is as follows: ### CPU Performance Top Statistics Fluctuation Issue<a name="ZH-CN_TOPIC_0000002408275498"></a> [Phenomenon] Using top for CPU utilization statistics is not very accurate and may show fluctuations, especially in low-load scenarios where top CPU utilization can fluctuate significantly. [Analysis] The Linux kernel version defaults to HZ=100 (10ms scheduling statistics). The statistical time granularity is coarse, resulting in insufficient accuracy and larger fluctuations. [Solution] For more accurate CPU utilization statistics, modify kernel HZ to 1000 to improve statistical precision. ### Precautions for Binding Interrupts to Different CPUs<a name="ZH-CN_TOPIC_0000002441714917"></a> The following recommendations apply to binding interrupts to CP Us: - Bind CP Us before business operations start, do not dynamically switch during operation.
- Multiple cores of the same module should be bound to the same CPU.
- VPSS and VGS modules should be bound to the same CPU, because VPSS may call VGS for rotation, overlayex, coverex, mosaicex, line, brightness, and other functions.
- Identify modules with many interrupts and bind them to different CP Us. For example, if network interrupts are numerous, separate them from media services. ## Miniaturization<a name="ZH-CN_TOPIC_0000002408275506"></a> ### Static Library Usage<a name="ZH-CN_TOPIC_0000002441675041"></a> [Phenomenon] Applications only use a small portion of functions from libss\_mpi.a, but need to link library files such as vqev2 in addition to the mpi library, resulting in excessively large application files. [Analysis] By default, the linker needs to link all defined function tables in the library, thus referencing other libraries associated with the mpi library. [Solution] When generating the MPP version library, add the -ffunction-sections compilation option to Makefile.param. When the customer links to generate the application, add -Wl,--gc-sections. This effectively reduces the application size by removing unused functions. ## Where to Configure Pin Multiplexing, Clock Gating, and System Control?<a name="ZH-CN_TOPIC_0000002441714889"></a> In the single Linux multi-core solution, pinmux, pin drive capability, clock gating (clk), and system control (sysctl) configurations are concentrated in interdrv/sysconfig/sys\_config.c. Users can modify them based on their product needs, compile them into sys\_config.ko, and the configuration takes effect after loading the ko. ## Video Cascade Configuration Precautions<a name="ZH-CN_TOPIC_0000002408275626"></a> - During video cascading, VO outputs standard timing signals, and VI parses the timing, thus completing data transmission.
- When VI parses BT.1120 standard timing, it uses 0xff 00 00 as the sync header signal data. When VO generates timing signals, it writes status information in the blanking area for software management of cascade status. Note that during data transmission, sync header values should not appear in the blanking area, otherwise VI will parse the timing incorrectly, ultimately causing transmission failure.
- When calling ss\_mpi\_vo\_set\_cas\_pattern, users should avoid using pattern=0x7f, as it may cause the 0xff 00 00 sync header to appear. ## Fast Frame Buffer Rotation Scheme Usage<a name="ZH-CN_TOPIC_0000002408275574"></a> [Phenomenon] For all self-encoded streams, implement fast frame buffer rotation, saving one VB per decoding channel. [Usage Notes] - Call ss\_mpi\_vdec\_set\_chn\_param to set display frame count to 0.
- Call ss\_mpi\_vpss\_disable\_backup\_frame to disable backup frames. ## Recompiling KO Process After Modifying Kernel Options<a name="ZH-CN_TOPIC_0000002408115654"></a> [Phenomenon] Customers need to modify kernel options. After recompiling the kernel, driver K Os need to be recompiled. [Solution] - Modify kernel options and recompile the kernel. Refer to the readme\_cn.txt/readme\_en.txt files in the osdrv directory of the delivery package.
- After changing kernel options, all business drivers need to be recompiled and relinked. - For Hi3403V100, enter the mpp/out/obj directory, run: make clean; make. ipcm.ko and virt-tty.ko need to be compiled in osdrv to be updated. [Precautions] - The generated driver ko is automatically copied to the mpp/ko (Hi3403V100 copies to mpp/out/ko) directory, overwriting the old driver ko.
- The default kernel source path is open\_source/linux/linux-4.x.y in the delivery package (x is the kernel version). To specify a kernel path, use: make clean; make KERNEL\_ROOT=<kernel source path>. ## Quick Schedule Precautions<a name="ZH-CN_TOPIC_0000002408115634"></a> Quick schedule is an overall optimization scheme for VDEC-VPSS-VO, requiring end-to-end coordination to achieve optimal memory savings. The specific operations are as follows: 1. Use ss\_mpi\_vb\_set\_mod\_pool\_cfg and ss\_mpi\_vb\_init\_mod\_common\_pool to create VDEC VB (supports module VB and user VB, module VB recommended).
2. Use ss\_mpi\_sys\_set\_schedule\_mode to set system schedule mode to OT\_SCHEDULE\_QUICK.
3. Use ss\_mpi\_vdec\_set\_mod\_param to set vb\_src to OT\_VB\_SRC\_MOD (module VB recommended).
4. Set VDEC mark mode to fast mark mode via ss\_mpi\_vdec\_set\_chn\_param (quick\_mark\_mode = OT\_QUICK\_MARK\_ADAPT or OT\_QUICK\_MARK\_FORCE).
5. Set VDEC display frame count to 0 via ss\_mpi\_vdec\_set\_chn\_param (display\_frame\_num = 0).
6. Use ss\_mpi\_vpss\_enable\_quick\_send to enable channel fast send mode. Disable backup frames, and set channel mode to auto mode.
7. Use ss\_mpi\_vo\_set\_less\_buf\_attr to enable VO buffer saving (enable = TD\_TRUE). Set the vtth value based on different customer scenarios. See the VO section for details.
8. Use ss\_mpi\_vo\_set\_video\_layer\_attr to set display\_buf\_len to 2 buffers, partition\_mode to OT\_VO\_PARTITION\_MODE\_MULTI (MULTI mode recommended). ### VDEC<a name="ZH-CN_TOPIC_0000002441674829"></a> - VDEC fast schedule only takes effect in VDEC-VO and VDEC-VPSS-VO binding relationships.
- When mixing bound and unbound channels, user VB mode is recommended. Unbound channels should attach to a different pool than bound channels to avoid VB starvation.
- Fast reference frame release defaults to adaptive mode (OT\_QUICK\_MARK\_ADAPT).
- Force mode (OT\_QUICK\_MARK\_FORCE) supports normalP and SmartP streams without skip-frame reference for fast frame release saving VB. However, if the encoder sets skip-frame reference or reference frame count > 2, there is a decoding compatibility risk causing decoding artifacts.
- When compound decoding of enhancement layer is enabled, fast reference frame release does not take effect.
- After enabling fast schedule, display order output, IPB decode mode, and private VB mode are not supported.
- With fast schedule enabled, if a single VDEC channel binds to multiple VO channels, playback control is disabled.
- With fast schedule and dynamic bind/unbind scenarios, to avoid stuttering, call ss\_mpi\_vpss\_reset\_grp and ss\_mpi\_vo\_clear\_chn\_buf to reset before rebinding.
- With fast schedule and skip-frame reference streams in playback control scenarios, set display frame count to 1 to avoid stuttering. ### VPSS<a name="ZH-CN_TOPIC_0000002408115642"></a> - With fast schedule, VPSS prioritizes VO-bound Groups, affecting real-time performance of non-VO-bound Groups.
- The VPSS proc info's old undo count may increase. Multiple Groups may have uneven old undo counts, which is normal.
- VPSS fast send mode interface does not support dynamic configuration; set it before enabling the channel.
- Various platform-specific limitations exist for VPSS fast send mode (Aspect Ratio, Flip, overscaling, channel post-processing, rotation, low latency, etc.). Refer to the original Chinese documentation for the complete platform-specific details. ### VO<a name="ZH-CN_TOPIC_0000002408275662"></a> - VO buffer saving vtth2 value range is [2, vtth1], where vtth1 is set by ss\_mpi\_vo\_set\_vtth.
- If vtth2 is close to 2, no screen tearing risk, but may cause insufficient frame rate or frame drops. If close to vtth1, frame rate is sufficient but there is screen tearing risk.
- For fewer channels with larger resolutions, set vtth2 = vtth1-1. For more channels with smaller resolutions, set vtth2 close to 2.
- MULTI mode is recommended over SINGLE mode in buffer-saving fast schedule scenarios.
- Use hide/show for screen switching, not disable/enable. If using disable/enable, destroy the disabled front-end channels to ensure sufficient VB.
- If VDEC/VPSS performance is near the bottleneck with VO 2-buf, configure 3-buf to guarantee no frame drops. ## Low Latency<a name="ZH-CN_TOPIC_0000002441674849"></a> Low latency features reduce delay between pipeline modules (e.g., VPSS->VO/VENC), including input low latency and output low latency. Module support varies by product. See the "Low Latency" section in "MPP Media Processing Software V5.0 Development Reference". ### VDEC<a name="ZH-CN_TOPIC_0000002441674957"></a> - H264/H265 decode channels support output low latency via ss\_mpi\_vdec\_set\_low\_delay\_attr.
- H264/H265 decode supports slice input low latency via ss\_mpi\_vdec\_set\_chn\_param (slice\_input\_en). ### VPSS<a name="ZH-CN_TOPIC_0000002441674993"></a> - Configure output low latency via ss\_mpi\_vpss\_set\_low\_delay\_attr.
- Disable channel post-processing features (see "VPSS Data Processing Flow").
- Enable fast schedule via ss\_mpi\_vpss\_enable\_quick\_send.
- Adjust VPSS online interrupt type via ss\_mpi\_vpss\_set\_grp\_frame\_interrupt\_attr. ### VO<a name="ZH-CN_TOPIC_0000002441714745"></a> - Configure VO as single-screen direct mode. Refer to the "Video Output" chapter in the Development Reference.
- Set the channel receive threshold. Smaller values mean lower preview latency.
- Adjust the vertical timing interrupt threshold. Smaller values reduce latency.
- For non-direct SINGLE mode low latency, enable video layer early display. ### VENC<a name="ZH-CN_TOPIC_0000002441714861"></a> - Input low latency is only supported on Hi3403V100.
- Output low latency includes H.264/H.265 slice interrupt output and JPEGE/MJPEGE ECS interrupt output.
- Hi3403V100 support slice low latency output (ss\_mpi\_venc\_set\_slice\_split).
- Hi3403V100 support ECS interrupt output (ss\_mpi\_venc\_set\_mjpeg\_param). ### VI<a name="ZH-CN_TOPIC_0000002441674889"></a> - Input/output low latency is only supported on Hi3403V100.
- Configure pipe output low latency via ss\_mpi\_vi\_set\_pipe\_low\_delay\_attr.
- Configure channel/channel post-processing output low latency via ss\_mpi\_vi\_set\_chn\_low\_delay\_attr.
- Adjust VI interrupt type via ss\_mpi\_vi\_set\_pipe\_frame\_interrupt\_attr. ## Pixel Format Description<a name="ZH-CN_TOPIC_0000002408115646"></a> The byte ordering for VGS module reading and writing YUV PACKAGE 422 format is as follows. 32-bit data byte-to-memory mapping: a7~0 = Byte0 bits, b7~0 = Byte1 bits, etc. **Figure 1** 32-bit Data to Memory Byte Mapping<a name="fig867601481414"></a> ![](figures/32bit Data To Memoryeachsave Corresponding Relationship.png "32-bit Data to Memory Byte Mapping") YUV PACKAGE 422 format component-to-memory byte mapping (using YUYV as example): **Figure 2** YUV PACKAGE 422 Component to Memory Byte Mapping<a name="fig317111362520"></a> ![](figures/YUV-PACKAGE-422Formateach And Memoryeachsave Corresponding Relationship.png "YUV PACKAGE 422 Component to Memory Byte Mapping") All YUV PACKAGE 422 formats mapping: **Table 1** Pixel Format Component to Memory Byte Mapping <a name="table257201417382"></a>
<table><thead align="left"><tr id="row195751493811"><th class="cellrowborder" valign="top" width="44.48555144485552%" id="mcps1.2.6.1.1"><p id="p257151413813"><a name="p257151413813"></a><a name="p257151413813"></a>Pixel Format</p>
</th>
<th class="cellrowborder" valign="top" width="13.578642135786422%" id="mcps1.2.6.1.2"><p id="p7571414143813"><a name="p7571414143813"></a><a name="p7571414143813"></a>Byte3[7:0]</p>
</th>
<th class="cellrowborder" valign="top" width="13.878612138786123%" id="mcps1.2.6.1.3"><p id="p185731463810"><a name="p185731463810"></a><a name="p185731463810"></a>Byte2[7:0]</p>
</th>
<th class="cellrowborder" valign="top" width="14.638536146385361%" id="mcps1.2.6.1.4"><p id="p05712143389"><a name="p05712143389"></a><a name="p05712143389"></a>Byte1[7:0]</p>
</th>
<th class="cellrowborder" valign="top" width="13.418658134186584%" id="mcps1.2.6.1.5"><p id="p957131433817"><a name="p957131433817"></a><a name="p957131433817"></a>Byte0[7:0]</p>
</th>
</tr>
</thead>
<tbody><tr id="row1957131420388"><td class="cellrowborder" valign="top" width="44.48555144485552%" headers="mcps1.2.6.1.1 "><p id="p15574145386"><a name="p15574145386"></a><a name="p15574145386"></a>OT_PIXEL_FORMAT_YUYV_PACKAGE_422</p>
</td>
<td class="cellrowborder" valign="top" width="13.578642135786422%" headers="mcps1.2.6.1.2 "><p id="p115721413819"><a name="p115721413819"></a><a name="p115721413819"></a>Y0</p>
</td>
<td class="cellrowborder" valign="top" width="13.878612138786123%" headers="mcps1.2.6.1.3 "><p id="p1057314173812"><a name="p1057314173812"></a><a name="p1057314173812"></a>U0</p>
</td>
<td class="cellrowborder" valign="top" width="14.638536146385361%" headers="mcps1.2.6.1.4 "><p id="p1257191412382"><a name="p1257191412382"></a><a name="p1257191412382"></a>Y1</p>
</td>
<td class="cellrowborder" valign="top" width="13.418658134186584%" headers="mcps1.2.6.1.5 "><p id="p14577146380"><a name="p14577146380"></a><a name="p14577146380"></a>V0</p>
</td>
</tr>
<tr id="row05721416385"><td class="cellrowborder" valign="top" width="44.48555144485552%" headers="mcps1.2.6.1.1 "><p id="p16571714133816"><a name="p16571714133816"></a><a name="p16571714133816"></a>OT_PIXEL_FORMAT_YVYU_PACKAGE_422</p>
</td>
<td class="cellrowborder" valign="top" width="13.578642135786422%" headers="mcps1.2.6.1.2 "><p id="p12571014133817"><a name="p12571014133817"></a><a name="p12571014133817"></a>Y0</p>
</td>
<td class="cellrowborder" valign="top" width="13.878612138786123%" headers="mcps1.2.6.1.3 "><p id="p658101415386"><a name="p658101415386"></a><a name="p658101415386"></a>V0</p>
</td>
<td class="cellrowborder" valign="top" width="14.638536146385361%" headers="mcps1.2.6.1.4 "><p id="p1258121417389"><a name="p1258121417389"></a><a name="p1258121417389"></a>Y1</p>
</td>
<td class="cellrowborder" valign="top" width="13.418658134186584%" headers="mcps1.2.6.1.5 "><p id="p1581114173820"><a name="p1581114173820"></a><a name="p1581114173820"></a>U0</p>
</td>
</tr>
<tr id="row158514133818"><td class="cellrowborder" valign="top" width="44.48555144485552%" headers="mcps1.2.6.1.1 "><p id="p185871413818"><a name="p185871413818"></a><a name="p185871413818"></a>OT_PIXEL_FORMAT_UYVY_PACKAGE_422</p>
</td>
<td class="cellrowborder" valign="top" width="13.578642135786422%" headers="mcps1.2.6.1.2 "><p id="p258141463812"><a name="p258141463812"></a><a name="p258141463812"></a>U0</p>
</td>
<td class="cellrowborder" valign="top" width="13.878612138786123%" headers="mcps1.2.6.1.3 "><p id="p6589149382"><a name="p6589149382"></a><a name="p6589149382"></a>Y0</p>
</td>
<td class="cellrowborder" valign="top" width="14.638536146385361%" headers="mcps1.2.6.1.4 "><p id="p1758141413811"><a name="p1758141413811"></a><a name="p1758141413811"></a>V0</p>
</td>
<td class="cellrowborder" valign="top" width="13.418658134186584%" headers="mcps1.2.6.1.5 "><p id="p758161416387"><a name="p758161416387"></a><a name="p758161416387"></a>Y1</p>
</td>
</tr>
<tr id="row1558161414388"><td class="cellrowborder" valign="top" width="44.48555144485552%" headers="mcps1.2.6.1.1 "><p id="p1958101403817"><a name="p1958101403817"></a><a name="p1958101403817"></a>OT_PIXEL_FORMAT_VYUY_PACKAGE_422</p>
</td>
<td class="cellrowborder" valign="top" width="13.578642135786422%" headers="mcps1.2.6.1.2 "><p id="p165811413386"><a name="p165811413386"></a><a name="p165811413386"></a>V0</p>
</td>
<td class="cellrowborder" valign="top" width="13.878612138786123%" headers="mcps1.2.6.1.3 "><p id="p458171423811"><a name="p458171423811"></a><a name="p458171423811"></a>Y0</p>
</td>
<td class="cellrowborder" valign="top" width="14.638536146385361%" headers="mcps1.2.6.1.4 "><p id="p158131473816"><a name="p158131473816"></a><a name="p158131473816"></a>U0</p>
</td>
<td class="cellrowborder" valign="top" width="13.418658134186584%" headers="mcps1.2.6.1.5 "><p id="p145841416384"><a name="p145841416384"></a><a name="p145841416384"></a>Y1</p>
</td>
</tr>
</tbody>
</table> (Additional pixel format byte mappings follow the same pattern. See the original Chinese document for the complete list of 8 YUV PACKAGE 422 formats.) # VI
## Thermal Detector Interface<a name="ZH-CN_TOPIC_0000002408115738"></a> ### T0 Type Detector Configuration<a name="ZH-CN_TOPIC_0000002408275594"></a> #### CRG and Pin Multiplexing Configuration<a name="ZH-CN_TOPIC_0000002408275590"></a> When loading the ko, use: load\_Hi3403V100 -a --sensor1 t0. Adjust pin multiplexing in sysconfig as needed, referring to functions thermo\_clock\_config and thermo\_sensor\_pin\_mux. #### MIPI Configuration<a name="ZH-CN_TOPIC_0000002441674977"></a> No configuration required. #### VI Configuration<a name="ZH-CN_TOPIC_0000002441714721"></a> #### VI DEV Attribute Configuration<a name="ZH-CN_TOPIC_0000002408115674"></a> Only Dev1 can be used. Set intf\_mode to OT\_VI\_INTF\_MODE\_THERMO. Other configurations are the same as raw data input. Resolution set to 656x520. #### Thermal Attribute Configuration<a name="ZH-CN_TOPIC_0000002408275678"></a> - work\_mode set to OT\_VI\_THERMO\_WORK\_MODE\_T0.
- ooc\_frame\_info set to 328x520, 16-bit raw data input.
- cfg\_num set to 60.
- sns\_cfg configuration (60-byte data array, see original document).
- frame\_rate set to 50 (currently invalid).
- sd\_mux set based on actual hardware routing. ### T1 Type Detector Configuration<a name="ZH-CN_TOPIC_0000002441714833"></a> #### CRG and Pin Multiplexing Configuration<a name="ZH-CN_TOPIC_0000002441674965"></a> Use: load\_Hi3403V100 -a -sensor0 t1. Adjust pin multiplexing as needed. #### MIPI Configuration (LVDS Configuration)<a name="ZH-CN_TOPIC_0000002408115534"></a> 1. Configure LVDS attributes with combo\_dev\_attr\_t THERMO\_T1\_LVDS\_ATTR (devno=0, INPUT\_MODE\_LVDS, DATA\_TYPE\_RAW\_8BIT, etc.). See the original document for the full structure with sync codes and lane mapping. 2. Configure LVDS VBPLL. #### VI Configuration<a name="ZH-CN_TOPIC_0000002441714785"></a> Set intf\_mode to OT\_VI\_INTF\_MODE\_THERMO. Resolution 164x123. #### Thermal Attribute Configuration<a name="ZH-CN_TOPIC_0000002441675053"></a> - work\_mode set to OT\_VI\_THERMO\_WORK\_MODE\_T1.
- ooc\_frame\_info set to 82x123, 16-bit raw data.
- cfg\_num set to 60.
- frame\_rate set to 50.
- sd\_mux etc. configured based on hardware. ### T1 Aitemp Type Detector Configuration<a name="ZH-CN_TOPIC_0000002441674941"></a> Similar to T1 LVDS but with different sync codes and register configurations. ### T1 ISC Type Detector Configuration<a name="ZH-CN_TOPIC_0000002441714945"></a> Uses INPUT\_MODE\_MIPI with RAW data type. Similar to T1 but with MIPI instead of LVDS. ### T2 Type Detector Configuration<a name="ZH-CN_TOPIC_0000002441714929"></a> Uses LVDS interface. Notable attributes include 160x120 resolution image rectangle. ## VI Frame Rate Readback Description<a name="ZH-CN_TOPIC_0000002441714741"></a> The frame rate readback interface provides VICAP's internal frame rate statistics. See ss\_mpi\_vi\_get\_pipe\_fps and ss\_mpi\_vi\_get\_chn\_fps. ## VI Channel Offline Crop Invalid Issue<a name="ZH-CN_TOPIC_0000002408115706"></a> [Phenomenon] VI channel offline crop may not take effect.
[Solution] Ensure that the pipe's first enable is online mode. ## VI Channel Pipe Bind and Unbind<a name="ZH-CN_TOPIC_0000002408115746"></a> VI supports dynamic bind/unbind. For different modes (online/offline), follow specific sequences for create, bind, start, and stop operations. ## VI Pipe Dynamic Frame Rate Setting Function<a name="ZH-CN_TOPIC_0000002441714717"></a> Supports dynamic frame rate changes via ss\_mpi\_vi\_set\_pipe\_frame\_rate. Must stop dev/pipe first. ## VI Bind VPSS in Offline Mode - Scaler Performance Issue<a name="ZH-CN_TOPIC_0000002441675081"></a> - Scale-down factor >= 16x is not supported in offline mode.
- Scale-down factor >= 8x may cause performance bottlenecks. ## VI Intf Sync Horizontal Pixel Count Not Aligned to 16<a name="ZH-CN_TOPIC_0000002441675057"></a> For BT.1120/BT.656 interfaces, ensure horizontal pixel count is aligned to 16 to avoid image shift. ## VI Ringing Green Border Issue<a name="ZH-CN_TOPIC_0000002441674901"></a> [Phenomenon] Green border ringing on images.
[Solution] Adjust VI module filter coefficients. # VO ## Static Logo Loading Flicker Issue<a name="ZH-CN_TOPIC_0000002441675029"></a> [Phenomenon] Static logo loading causes flicker.
[Solution] Set the channel layer to VGS layer before sending the logo. Logo configuration timing differs between HD and SD. ## Hi3403V100 Cascade VO Part Screen Flicker<a name="ZH-CN_TOPIC_0000002441674877"></a> [Phenomenon] Flicker on cascaded VO partial screens.
[Solution] Enable BTA for BT.1120 output. ## VO BT.1120 Clock Phase Setting<a name="ZH-CN_TOPIC_0000002441714873"></a> [Phenomenon] Data sampling errors due to BT.1120 clock phase.
[Solution] Use the debug register or sample delay interface ss\_mpi\_vo\_set\_sample\_delay to adjust delay. ## VO Compositing Graphical Layers and Video Layers<a name="ZH-CN_TOPIC_0000002408115734"></a> [Phenomenon] Composited display of graphical layers over video layers may show only the graphical layer.
[Analysis] Graphical layers have higher overlay priority and may completely cover the video layer if alpha transparency is not properly configured.
[Solution] Set proper alpha values for the overlay operation. ## VO Channel Does Not Display Images<a name="ZH-CN_TOPIC_0000002408275682"></a> [Phenomenon] After configuring all VO parameters per the document, no image is displayed.
[Analysis] Possible issues with device enable timing and channel enable sequence.
[Solution] - Enable the device before enabling channels.
- After enabling channels, delay at least 2 frames before sending images. ## VO Crop Feature Does Not Cover Entire Screen After Configuring Compositing Parameters<a name="ZH-CN_TOPIC_0000002441714761"></a> [Phenomenon] After setting VO compositing parameters, configuring crop overlay area results in incomplete screen coverage.
[Solution] Configure the compositing attribute bord\_en to set a border area and ensure the crop area dimensions are correct. ## VO Layer Extended Configuration Method<a name="ZH-CN_TOPIC_0000002441674845"></a> Use ss\_mpi\_vo\_set\_video\_layer\_ext\_para to set custom timing parameters for the video layer. ## MIPI DSI Read Data Register Check Method<a name="ZH-CN_TOPIC_0000002441714881"></a> [Phenomenon] Need to check MIPI DSI register data.
[Solution] Use 'himdL' to read registers at mipi\_tx\_base + specific offsets for command packet, RX DATA, and payload. ## VO Cascading Common Issues<a name="ZH-CN_TOPIC_0000002441674885"></a> - Confirm VO BT.1120 is outputting correct timing.
- Confirm VI can lock onto BT.1120 timing.
- Check for MIPI\_TX signal using an oscilloscope.
- Check cascade register configuration. # VENC ## JPEG Quantization Table Configuration Precautions<a name="ZH-CN_TOPIC_0000002441675061"></a> Use ss\_mpi\_venc\_set\_jpeg\_param to set quantization tables. The luminance and chrominance tables should be configured separately. ## JPEG Dull/Gray Issue<a name="ZH-CN_TOPIC_0000002441674909"></a> [Phenomenon] JPEG images appear dull or gray.
[Solution] Adjust quantization tables and enable JPEG quality enhancement features. ## P-frame Intra Refresh Causes Visible Screen Scrolling<a name="ZH-CN_TOPIC_0000002408275474"></a> [Phenomenon] P-frame intra refresh produces a visible scrolling effect.
[Solution] Reduce the intra refresh cycle or use a different refresh mode. ## H.264 AVBR Bitrate Differences Compared to Other Platforms<a name="ZH-CN_TOPIC_0000002408115726"></a> [Phenomenon] H.264 AVBR bitrates differ from other platforms.
[Solution] Use VBV buffer size adjustment to fine-tune bitrate control. # VDEC ## MDC Decode Memory Usage When DDR > 3GB<a name="ZH-CN_TOPIC_0000002408115774"></a> Configure VB pool properly for MDC decode mode. Memory mapping differs for DDR configurations exceeding 3GB. ## MDC Decode Module VB Usage Precautions<a name="ZH-CN_TOPIC_0000002408275578"></a> Use module VB pool for MDC decode. Ensure VB size meets MDC requirements. ## VO Display Differences When Destroying VDEC Channels in Different Scenarios<a name="ZH-CN_TOPIC_0000002441674937"></a> Destroying VDEC channels may cause different VO display behaviors depending on the pipeline configuration (direct display vs. VPSS processing). ## Decode Timeliness Optimization<a name="ZH-CN_TOPIC_0000002441714921"></a> Optimize decode latency by adjusting decode buffer count and thread priority. # Pipeline Debugging Guide
## VI Pipeline Debugging<a name="ZH-CN_TOPIC_0000002441714801"></a> ### I2C Errors<a name="ZH-CN_TOPIC_0000002408115598"></a> Check I2C communication: verify pull-up resistors, clock frequency, and device address. Use i2c-tools for debugging. ### No Output Image or Black Screen<a name="ZH-CN_TOPIC_0000002441714729"></a> [Phenomenon] No image output or black screen.
[Analysis] Possible causes: incorrect sensor configuration, MIPI/LVDS setup issues, clock problems.
[Solution] Check sensor initialization, verify MIPI/LVDS configuration, check clock signals. ### CC Error<a name="ZH-CN_TOPIC_0000002408115666"></a> [Phenomenon] CC (Code Correction) errors reported by VI.
[Solution] Check signal integrity and adjust equalizer settings. ### Lost Interrupts<a name="ZH-CN_TOPIC_0000002441714817"></a> [Phenomenon] VI interrupts being lost.
[Solution] Check interrupt binding, CPU load, and interrupt priority settings. ### Color Bar Debug<a name="ZH-CN_TOPIC_0000002441714897"></a> Use built-in color bar to verify video pipeline without an external sensor. ## VO Pipeline Debugging<a name="ZH-CN_TOPIC_0000002408115702"></a> ### VO Color Bar Usage<a name="ZH-CN_TOPIC_0000002441714809"></a> Enable built-in VO color bar to verify output timing. ### VO Color Bar Configuration<a name="ZH-CN_TOPIC_0000002408275582"></a> Configure specific color bar patterns and modes via the VO color bar interface. ## HDMI Pipeline Debugging<a name="ZH-CN_TOPIC_0000002441674949"></a> ### Color Bar Usage<a name="ZH-CN_TOPIC_0000002408275534"></a> Enable HDMI color bar to verify the HDMI output path. ### HDMI Color Bar<a name="ZH-CN_TOPIC_0000002441714849"></a> HDMI color bar configuration details. # Other
## Dynamic Library<a name="ZH-CN_TOPIC_0000002408115754"></a> ### Why Can't Static Compilation Applications Use Dynamic Libraries<a name="ZH-CN_TOPIC_0000002441675021"></a> [Phenomenon] Statically compiled applications cannot link dynamic libraries.
[Solution] Use dynamic linking or ensure all required libraries are statically linked. ### Why Does Dynamic Compilation with libss\_upvqe.a and libss\_dnvqe.a Cause Redefinition<a name="ZH-CN_TOPIC_0000002441714841"></a> [Phenomenon] Redefinition errors when linking both upvqe and dnvqe libraries.
[Solution] Use --allow-multiple-definition or ensure only one VQE library is linked. ## Encoding Block Effect in IR Mode<a name="ZH-CN_TOPIC_0000002441714853"></a> [Phenomenon] Visible block artifacts in IR mode encoding.
[Solution] Adjust encoding parameters for IR-specific noise characteristics. ## DVR Front-end 3840x480 Interlaced Scene Performance Optimization<a name="ZH-CN_TOPIC_0000002441674981"></a> Optimize performance for interlaced 3840x480 capture on DVR front-end. ### Module KO Dependencies<a name="ZH-CN_TOPIC_0000002408115662"></a> List of module driver dependencies and correct loading order. ## HDMI Hot Plug and Power Consumption<a name="ZH-CN_TOPIC_0000002441714697"></a> HDMI hot plug detection may affect power consumption. Optimize by managing HDMI PHY power states. ## OSD Transparency and Color Issues<a name="ZH-CN_TOPIC_0000002441714685"></a> OSD overlay transparency and color configuration guidelines. ## Partial VI Channel Startup Black Screen<a name="ZH-CN_TOPIC_0000002408115766"></a> [Phenomenon] Starting some VI channels results in black screen.
[Solution] Check channel enable sequence and VB allocation. ## VDEC Backpressure Failure in Playback Mode<a name="ZH-CN_TOPIC_0000002441714893"></a> [Phenomenon] Backpressure to VDEC fails during playback.
[Solution] Adjust buffer pool sizes or use alternative flow control. ## MIPI\_RX Pin Multiplexing Configuration Issue<a name="ZH-CN_TOPIC_0000002441714857"></a> [Phenomenon] Incorrect MIPI\_RX pin multiplexing.
[Solution] Verify pinmux configuration for specific MIPI lanes in sysconfig. ## Hardware Timer Used for VI User Image Modification<a name="ZH-CN_TOPIC_0000002441675017"></a> Using hardware timers to control VI user image update timing. ## EARLY/EARLY\_END Mode Early\_Line Configuration Suggestions<a name="ZH-CN_TOPIC_0000002408115694"></a> Recommendations for configuring early\_line in EARLY and EARLY\_END modes for latency optimization. ## HNR/Smart Business Switching Process<a name="ZH-CN_TOPIC_0000002408275658"></a> Switching between HNR (High Noise Reduction) and smart business modes. Follow the documented sequence to avoid configuration conflicts. ## VO Interrupt Delay Issue<a name="ZH-CN_TOPIC_0000002441714789"></a> [Phenomenon] VO interrupt delays causing display issues.
[Solution] Check interrupt handling and CPU affinity settings. ## Hi3403V100 VI Buffer Overflow Interrupt Frame Drop Issue<a name="ZH-CN_TOPIC_0000002408275630"></a> [Phenomenon] VI reporting buffer overflow interrupt and dropping frames.
[Solution] Increase VB pool size or reduce VI input load.
