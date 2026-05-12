#!/usr/bin/env python3
"""
Translate Chinese MPP documentation .md files to English .en.md files.
Preserves all HTML, code blocks, API names, struct names, file paths, anchors.
Uses full-sentence translation tables for known content and phrase-level
translation for prose, avoiding naive word-by-word replacement.
"""

import re
import os
import sys

# ═══════════════════════════════════════════════════════════════
#  1. API section headers (bracketed labels)
# ═══════════════════════════════════════════════════════════════
SECTION_MAP = {
    "【描述】": "【Description】",
    "【语法】": "【Syntax】",
    "【参数】": "【Parameters】",
    "【返回值】": "【Return Value】",
    "【需求】": "【Requirements】",
    "【注意】": "【Notes】",
    "【举例】": "【Example】",
    "【相关主题】": "【Related Topics】",
}

# ═══════════════════════════════════════════════════════════════
#  2. Full-sentence / full-phrase translations (longest first)
# ═══════════════════════════════════════════════════════════════
SENTENCE_MAP = {
    # ── File / section titles ──
    "系统控制": "System Control",
    "视频输入": "Video Input",
    "视频输出": "Video Output",
    "视频处理子系统": "Video Processing Subsystem",
    "概述": "Overview",
    "功能描述": "Functional Description",
    "重要概念": "Important Concepts",
    "低延时": "Low Latency",
    "视频缓存池": "Video Buffer Pool",
    "系统绑定": "System Binding",
    "强制销毁VB功能": "Forced VB Destruction",
    "VI和VPSS工作模式": "VI and VPSS Working Modes",
    "VI视频模式": "VI Video Mode",
    "logmpp日志": "logmpp Log",
    "API参考": "API Reference",
    "功能框图": "Functional Block Diagram",
    "视频输入设备": "Video Input Device",
    "视频输入物理PIPE": "Video Input Physical PIPE",
    "视频输入虚拟PIPE": "Video Input Virtual PIPE",
    "视频物理通道": "Video Physical Channel",
    "PIPE的工作模式": "PIPE Working Mode",
    "掩码": "MASK",
    "镜头畸变校正（LDC）": "Lens Distortion Correction (LDC)",
    "DIS": "DIS",
    "BAS": "BAS",
    "提前上报中断": "Early Interrupt Reporting",
    "VO基本概念": "VO Basic Concepts",
    "VO显示设备": "VO Display Device",
    "VO视频层": "VO Video Layer",
    "VO图形层": "VO Graphics Layer",
    "VO回写设备": "VO Writeback Device",
    "VO显示通路": "VO Display Pipeline",
    "HDMI物理像素时钟设置": "HDMI Physical Pixel Clock Setting",
    "基本处理流程": "Basic Processing Flow",
    "VO与VDAC时序": "VO and VDAC Timing",
    "HDMI时序配置": "HDMI Timing Configuration",
    "显示通路配置": "Display Pipeline Configuration",
    "ZOOM模式": "ZOOM Mode",
    "压缩与解压缩": "Compression and Decompression",
    "vpss基本概念": "VPSS Basic Concepts",
    "MCF（多目融合）": "MCF (Multi-Camera Fusion)",
    "基本概念": "Basic Concepts",
    "JPEG解码": "JPEG Decode",
    "VGS": "VGS",
    "AVS": "AVS",
    "AVS基本概念": "AVS Basic Concepts",
    "AVS功能描述": "AVS Functional Description",
    "VPSS基本概念": "VPSS Basic Concepts",
    "vpss region": "VPSS Region",

    # ── Table header cells ──
    "参数名称": "Parameter Name",
    "输入/输出": "Input/Output",
    "输入": "Input",
    "输出": "Output",
    "返回值": "Return Value",
    "成功。": "Success.",
    "成功": "Success",
    "失败，其值参见错误码": "Failure, see Error Code",
    "失败，其值参见": "Failure, see ",
    "失败": "Failure",
    "错误码": "Error Code",
    "非0": "Non-zero",
    "解决方案": "Solution",
    "备注": "Remarks",
    "数据源": "Data Source",
    "数据接收者": "Data Receiver",
    "模式": "Mode",
    "在线模式": "Online Mode",
    "离线模式": "Offline Mode",
    "在线": "Online",
    "离线": "Offline",
    "支持低延时的模块": "Modules Supporting Low Latency",
    "支持输出低延时": "Supports output low latency",
    "支持输入、输出低延时": "Supports input and output low latency",
    "支持输入低延时": "Supports input low latency",
    "模式分布1": "Mode Distribution 1",
    "模式分布2": "Mode Distribution 2",
    "PIPE ID": "PIPE ID",
    "视频缓存池大小计算接口": "Video Buffer Pool Size Calculation Interface",
    "接口简介": "Interface Description",
    "MPP支持的绑定关系": "MPP Supported Bindings",
    "设备/PIPE/通道的个数": "Device/PIPE/Channel Counts",
    "VI在软件层次划分的4个部分": "Four software-level partitions of VI",
    "DDR内存分配": "DDR Memory Allocation",
    "帧buffer计算": "Frame Buffer Calculation",
    "视频层VHD0": "Video Layer VHD0",
    "视频层VHD1": "Video Layer VHD1",
    "视频层VHD2": "Video Layer VHD2",
    "图形层G0": "Graphics Layer G0",
    "图形层G1": "Graphics Layer G1",
    "图形层G2": "Graphics Layer G2",
    "图形层G3": "Graphics Layer G3",
    "设备级回写自DHD0/DHD1": "Device-level writeback from DHD0/DHD1",
    "视频层回写自VHD0/VHD1": "Video layer writeback from VHD0/VHD1",
    "超高清显示设备DHD0": "Ultra-HD Display Device DHD0",
    "高清显示设备DHD1": "HD Display Device DHD1",
    "标清显示设备DSD0": "SD Display Device DSD0",
    "回写设备WD": "Writeback Device WD",
    "显示/回写设备": "Display/Writeback Device",
    "视频层": "Video Layer",
    "图形层": "Graphics Layer",
    "层类型": "Layer Type",
    "预乘Alpha": "Premultiplied Alpha",
    "独立Alpha": "Independent Alpha",
    "无Alpha": "No Alpha",
    "边界值/饱和值": "Clamp/Saturate",
    "边界值": "Clamp",
    "饱和值": "Saturate",
    "直接丢弃（整帧）": "Discard (Whole Frame)",
    "丢弃模式": "Discard Mode",
    "帧率转换": "Frame Rate Conversion",
    "显示buffer个数": "Display Buffer Count",
    "缓冲模式": "Buffer Mode",
    "优先显示": "Priority Display",
    "显示画面质量": "Display Quality",
    "显示帧存压缩": "Display Frame Buffer Compression",
    "视频层压缩": "Video Layer Compression",
    "去隔行": "De-interlacing",
    "显示层分辨率": "Display Layer Resolution",
    "行数错误丢弃": "Line Count Error Discard",
    "层级": "Level",
    "坐标": "Coordinates",
    "图像处理": "Image Processing",
    "WBMS": "WBMS",
    "VIPP": "VIPP",
    "层属性": "Layer Attribute",
    "深度": "Depth",
    "层使能": "Layer Enable",
    "显示buffer": "Display Buffer",
    "回写buffer": "Writeback Buffer",
    "回写深度": "Writeback Depth",
    "回写压缩": "Writeback Compression",
    "音视频同步": "Audio/Video Sync",
    "同步模式": "Sync Mode",
    "参考时钟源": "Reference Clock Source",
    "用户模式": "User Mode",
    "自动模式": "Auto Mode",
    "PTS模式": "PTS Mode",
    "VPSS模式": "VPSS Mode",
    "WB模式": "WB Mode",
    "在线模式": "Online Mode",
    "VPSS 4.1": "VPSS 4.1",
    "VPSS 4.2": "VPSS 4.2",
    "物理通道": "Physical Channel",
    "扩展通道": "Extension Channel",
    "VPSS缩放": "VPSS Scaling",
    "VPSS裁剪": "VPSS Crop",
    "VPSS镜像": "VPSS Mirror",
    "VPSS旋转": "VPSS Rotation",
    "VPSS帧率控制": "VPSS Frame Rate Control",
    "VPSS压缩": "VPSS Compression",
    "VPSS低延时": "VPSS Low Latency",
    "VPSS调试信息": "VPSS Debug Information",
    "SP图像": "SP Image",
    "低通滤波": "Low-Pass Filter",
    "3D降噪": "3D Noise Reduction",
    "2D降噪": "2D Noise Reduction",
    "细节增强": "Detail Enhancement",
    "边缘增强": "Edge Enhancement",
    "亮度对比度": "Brightness/Contrast",
    "饱和度": "Saturation",
    "色调": "Hue",
    "Gamma校正": "Gamma Correction",
    "动态对比度": "Dynamic Contrast",
    "肤色校正": "Skin Tone Correction",
    "色温": "Color Temperature",
    "镜头阴影校正": "Lens Shading Correction",
    "坏点校正": "Bad Pixel Correction",
    "数字增益": "Digital Gain",
    "黑电平": "Black Level",
    "去雾": "Dehaze",
    "场景模式": "Scene Mode",
    "AE": "AE",
    "AWB": "AWB",
    "AF": "AF",
    "AI": "AI",
    "AO": "AO",
    "AENC": "AENC",
    "ADEC": "ADEC",
    "TDE": "TDE",

    # ── API descriptions (complete sentences) ──
    "配置系统控制参数。": "Configures system control parameters.",
    "获取系统控制参数。": "Gets system control parameters.",
    "初始化MPP系统。包括音频输入输出、视频输入输出、视频编解码、视频叠加区域、视频处理、图形处理等模块都会被初始化。": "Initializes the MPP system. This includes modules such as audio input/output, video input/output, video encoding/decoding, video overlay region, video processing, and graphics processing.",
    "初始化MPP系统。": "Initializes the MPP system.",
    "去初始化MPP系统。包括音频输入输出、视频输入输出、视频编解码、视频叠加区域、视频处理、图形处理等模块都会被销毁或者禁用。": "Deinitializes the MPP system. This includes destroying or disabling modules such as audio input/output, video input/output, video encoding/decoding, video overlay region, video processing, and graphics processing.",
    "去初始化MPP系统。": "Deinitializes the MPP system.",
    "数据源到数据接收者绑定接口。": "Binds a data source to a data receiver.",
    "数据源到数据接收者解绑定接口。": "Unbinds a data source from a data receiver.",
    "获取此通道上绑定的源通道的信息。": "Gets the bound source channel information for this channel.",
    "根据源获取绑定的目标。": "Gets the bound destination based on the source.",
    "获取MPP的版本号。": "Gets the MPP version number.",
    "获取当前芯片的ID。": "Gets the current chip ID.",
    "获取当前芯片的unique ID（芯片唯一码）。": "Gets the current chip unique ID.",
    "获取当前芯片的custom code。": "Gets the current chip custom code.",
    "获取当前时间戳。": "Gets the current timestamp.",
    "初始化MPP时间戳。": "Initializes the MPP timestamp.",
    "同步MPP时间戳。": "Synchronizes the MPP timestamp.",
    "memory存储映射接口。": "Memory storage mapping interface.",
    "存储带Cache映射接口。": "Memory mapping interface with Cache.",
    "存储反映射接口。": "Memory unmapping interface.",
    "刷新cache里的内容到内存并且使cache里的内容无效。": "Flushes cache content to memory and invalidates cache content.",
    "在用户态分配MMZ内存。": "Allocates MMZ memory in user space.",
    "在用户态分配MMZ内存，该内存支持cache缓存。": "Allocates MMZ memory in user space, which supports cache.",
    "在用户态释放MMZ内存。": "Releases MMZ memory in user space.",
    "设置模块设备通道使用内存的DDR名。": "Sets the DDR name for memory used by the module device channel.",
    "获取模块设备通道使用的MMZ区域名称。": "Gets the MMZ zone name used by the module device channel.",
    "关闭所有SYS打开的日志、系统Fd。": "Closes all SYS-opened logs and system file descriptors.",
    "根据虚拟地址获取对应的内存信息。": "Gets corresponding memory information based on the virtual address.",
    "设置VPSS模块和VGS模块的缩放系数等级。": "Sets the scaling coefficient level for VPSS and VGS modules.",
    "获取VPSS和VGS缩放系数等级。": "Gets the VPSS and VGS scaling coefficient level.",
    "设置时区信息。": "Sets the time zone information.",
    "获取时区信息。": "Gets the time zone information.",
    "设置GPS信息。": "Sets GPS information.",
    "获取GPS信息。": "Gets GPS information.",
    "设置系统调度模式。": "Sets the system scheduling mode.",
    "获取系统调度模式。": "Gets the system scheduling mode.",
    "设置VI，VPSS的工作模式。": "Sets the VI and VPSS working modes.",
    "获取VI，VPSS的工作模式。": "Gets the VI and VPSS working modes.",
    "设置VI视频模式。": "Sets the VI video mode.",
    "获取VI视频模式。": "Gets the VI video mode.",
    "设置RAW帧压缩参数。": "Sets RAW frame compression parameters.",
    "获取RAW帧压缩参数。": "Gets RAW frame compression parameters.",
    "设置Tuning工具连接。": "Sets the Tuning tool connection.",
    "获取Tuning工具连接。": "Gets the Tuning tool connection.",
    "将handle对应的mmz buffer共享给特定的进程ID。": "Shares the MMZ buffer corresponding to the handle with a specific process ID.",
    "解除handle对应的mmz buffer对进程ID的共享。": "Removes the share of the MMZ buffer corresponding to the handle from a process ID.",
    "将handle对应的mmz buffer以不限进程ID的方式共享给所有进程。": "Shares the MMZ buffer corresponding to the handle with all processes without process ID restriction.",
    "解除handle对应的mmz buffer对所有进程的共享。": "Removes the share of the MMZ buffer corresponding to the handle from all processes.",
    "通过handle获取mmz buffer的内存描述信息。": "Gets MMZ buffer memory description information via the handle.",
    "通过物理地址获取mmz buffer的内存描述信息。": "Gets MMZ buffer memory description information via the physical address.",
    "通过用户态虚拟地址获取mmz buffer的内存描述信息。": "Gets MMZ buffer memory description information via the user-space virtual address.",
    "设置MPP视频缓存池属性。": "Sets MPP video buffer pool attributes.",
    "获取MPP视频缓存池属性。": "Gets MPP video buffer pool attributes.",
    "初始化MPP视频缓存池。": "Initializes the MPP video buffer pool.",
    "去初始化MPP视频缓存池。": "Deinitializes the MPP video buffer pool.",
    "创建一个用户视频缓存池。": "Creates a user video buffer pool.",
    "创建一个虚拟视频缓存池。": "Creates a virtual video buffer pool.",
    "销毁一个视频缓存池。": "Destroys a video buffer pool.",
    "获取一个缓存块。": "Gets a buffer block.",
    "释放一个已经获取的缓存块。": "Releases an acquired buffer block.",
    "添加一个缓存块到虚拟视频缓存池。": "Adds a buffer block to the virtual video buffer pool.",
    "从虚拟视频缓存池中删除一个缓存块。": "Deletes a buffer block from the virtual video buffer pool.",
    "用户态通过缓存块的物理地址获取其句柄。": "Gets the handle of a buffer block via its physical address in user space.",
    "获取一个缓存块的物理地址。": "Gets the physical address of a buffer block.",
    "获取一个缓存块所在缓存池的ID。": "Gets the pool ID of a buffer block.",
    "获取一个视频缓存池的信息。": "Gets the information of a video buffer pool.",
    "初始化模块公共视频缓冲池。": "Initializes the module common video buffer pool.",
    "注销模块公共视频缓冲池。": "Unregisters the module common video buffer pool.",
    "设置模块公共视频缓冲池属性。": "Sets the module common video buffer pool attributes.",
    "获取模块公共视频缓冲池属性。": "Gets the module common video buffer pool attributes.",
    "查询缓存块使用计数信息。": "Queries buffer block usage count information.",
    "获取VB block内存的辅助信息。": "Gets the auxiliary information of the VB block memory.",
    "设置VB内存的附加信息。": "Sets the supplementary information of VB memory.",
    "获取VB内存的附加信息。": "Gets the supplementary information of VB memory.",
    "获取公共VB池的pool ID。": "Gets the pool ID of the common VB pool.",
    "获取模块公共VB池的pool ID。": "Gets the pool ID of the module common VB pool.",
    "将pool ID对应的VB池共享给特定的进程ID。": "Shares the VB pool corresponding to the pool ID with a specific process ID.",
    "解除pool ID对应的VB池对进程ID的共享。": "Removes the share of the VB pool corresponding to the pool ID from a process ID.",
    "将pool ID对应的VB池以不限进程ID的方式共享给所有进程。": "Shares the VB pool corresponding to the pool ID with all processes without process ID restriction.",
    "解除pool ID对应的VB池对所有进程的共享。": "Removes the share of the VB pool corresponding to the pool ID from all processes.",
    "设置日志等级。": "Sets the log level.",
    "获取日志等级。": "Gets the log level.",
    "设置读取日志时等待标志。": "Sets the wait flag when reading logs.",
    "读取日志。": "Reads the log.",
    "关闭日志文件。": "Closes the log file.",

    # ── Parameter descriptions ──
    "系统控制参数指针。": "Pointer to the system control parameters.",
    "系统控制参数指针。静态属性（指只能在系统未初始化、未启用设备或通道时，才能设置的属性）。": "Pointer to the system control parameters. Static attribute (can only be set when the system is not initialized and devices or channels are not enabled).",
    "源通道指针。": "Pointer to the source channel.",
    "目的通道指针。": "Pointer to the destination channel.",
    "版本号描述指针。": "Pointer to the version number description.",
    "版本号描述指针。动态属性（指在任何时刻都可以设置的属性）。": "Pointer to the version number description. Dynamic attribute (can be set at any time).",
    "芯片ID指针。": "Pointer to the chip ID.",
    "芯片unique ID数据结构体指针。": "Pointer to the chip unique ID data structure.",
    "custom code指针。": "Pointer to the custom code.",
    "静态属性。": "Static attribute.",
    "静态属性（指只能在系统未初始化、未启用设备或通道时，才能设置的属性）。": "Static attribute (can only be set when the system is not initialized and devices or channels are not enabled).",
    "动态属性（指在任何时刻都可以设置的属性）。": "Dynamic attribute (can be set at any time).",
    "绑定的目的指针。": "Pointer to the bound destination.",
    "无。": "None.",
    "无": "None",

    # ── Callout / note translations ──
    "须知：": "**Note:** ",
    "说明：": "**Note:** ",
    "注意：": "**Caution:** ",
    "警告：": "**Warning:** ",

    # ── Notes section content ──
    "只有在MPP整个系统处于未初始化状态，才可调用此函数配置MPP系统，否则会配置失败。": "This function can only be called to configure the MPP system when the entire MPP system is in an uninitialized state; otherwise, the configuration will fail.",
    "此接口功能暂时无效。": "This interface is currently not functional.",
    "必须先调用ss_mpi_sys_set_cfg成功后才能获取配置。": "ss_mpi_sys_set_cfg must be called successfully before getting the configuration.",
    "由于MPP系统的正常运行依赖于缓存池，因此需要先调用ss_mpi_vb_init初始化缓存池，再初始化MPP系统，否则会导致业务运行异常。": "Since the normal operation of the MPP system depends on the buffer pool, ss_mpi_vb_init must be called first to initialize the buffer pool before initializing the MPP system; otherwise, the business operation may be abnormal.",
    "如果多次初始化，仍会返回成功，但实际上系统不会对MPP的运行状态有任何影响。": "If initialized multiple times, it will still return success, but the system state will not be affected.",
    "只要有一个进程进行初始化即可，不需要所有的进程都做系统初始化的操作。": "Only one process needs to perform initialization; not all processes need to do so.",
    "由于音频模块依赖用户态属性，故音频不支持多进程操作。用户需要保证音频的相关操作和ss_mpi_vb_init在同一个进程中。": "As the audio module depends on user-space attributes, audio does not support multi-process operations. Users must ensure audio-related operations and ss_mpi_vb_init are in the same process.",
    "去初始化时，如果有阻塞在MPI上的用户进程，调用ss_mpi_sys_exit会唤醒该阻塞进程，如果没有成功唤醒，则去初始化会失败。如果所有阻塞在MPI上的调用都返回，则可以成功去初始化。": "During deinitialization, if there are user processes blocked on MPI, calling ss_mpi_sys_exit will wake up the blocked process. If the wake-up is unsuccessful, deinitialization will fail. If all blocked MPI calls return, deinitialization can succeed.",
    "可以反复去初始化，不返回失败。": "Deinitialization can be called repeatedly without returning failure.",
    "由于系统去初始化不会销毁音频的编解码通道，因此这些通道的销毁需要用户主动进行。如果创建这些通道的进程退出，则通道随之被销毁。": "Since system deinitialization does not destroy audio encoding/decoding channels, users must destroy these channels actively. If the process that created these channels exits, the channels will be destroyed accordingly.",
    "系统目前支持的绑定关系，请参见表1。": "For the currently supported bindings, see Table 1.",
    "同一个数据接收者只能绑定一个数据源。": "The same data receiver can only bind to one data source.",
    "绑定是指数据源和数据接收者建立关联关系。绑定后，数据源生成的数据将自动发送给接收者。": "Binding establishes an association between a data source and a data receiver. After binding, data generated by the source is automatically sent to the receiver.",
    "dst_chn如果找不到绑定的源通道，则直接返回成功。如果找到了绑定的源通道，但是绑定的源通道和src_chn不匹配，则返回失败。": "If dst_chn cannot find a bound source channel, it returns success. If a bound source channel is found but does not match src_chn, it returns failure.",
    "VDEC作为数据源，是以通道为发送者，向其他模块发送数据，用户将设备号置为0，SDK不检查输入的设备号。": "When VDEC acts as a data source, the channel serves as the sender to transmit data to other modules. Users should set the device number to 0; the SDK does not check the input device number.",
    "SS528V100/SS625V100/SS524V100/SS522V101/SS626V100 VI作为数据源，是以通道为发送者，向其他模块发送数据，用户将设备号置为0，SDK不检查输入的设备号。": "For SS528V100/SS625V100/SS524V100/SS522V101/SS626V100, when VI acts as a data source, the channel serves as the sender to transmit data to other modules. Users should set the device number to 0; the SDK does not check the input device number.",
    "Hi3403V100 VI作为数据源，是以设备（pipe）、通道（chn）为发送者，向其他模块发送数据；作为数据接收者时，以设备（pipe）、通道（chn）为接收者。": "For Hi3403V100, when VI acts as a data source, the device (pipe) and channel (chn) serve as the sender to transmit data to other modules; when acting as a data receiver, the device (pipe) and channel (chn) serve as the receiver.",
    "VO作为数据源发送回写（WBC）数据时，是以设备为发送者，向其他模块发送数据，用户将通道号置为0，SDK不检查输入的通道号。": "When VO sends writeback (WBC) data as a data source, the device serves as the sender. Users should set the channel number to 0; the SDK does not check the input channel number.",
    "VPSS作为数据接收者时，是以设备（GROUP）为接收者，接收其他模块发来的数据，用户将通道号置为0。": "When VPSS acts as a data receiver, the device (GROUP) serves as the receiver. Users should set the channel number to 0.",
    "VENC作为数据接收者时，是以通道号为接收者，接收其他模块发过来的数据，用户将设备号置为0，SDK不检查输入的设备号。若VENC工作在OT_VENC_PIC_RECV_MULTI模式下，用户需要配置设备号，此时设备号实际用于指定输入源，可以使用OT_VENC_RECV_SRC0、OT_VENC_RECV_SRC1、OT_VENC_RECV_SRC2、OT_VENC_RECV_SRC3宏进行输入源指定。": "When VENC acts as a data receiver, the channel number serves as the receiver. Users should set the device number to 0; the SDK does not check the input device number. If VENC works in OT_VENC_PIC_RECV_MULTI mode, users need to configure the device number, which is then used to specify the input source. Macros OT_VENC_RECV_SRC0, OT_VENC_RECV_SRC1, OT_VENC_RECV_SRC2, and OT_VENC_RECV_SRC3 can be used for input source specification.",
    "AVS作为数据接收者，是以设备（GROUP）、通道（PIPE）为接收者。": "When AVS acts as a data receiver, the device (GROUP) and channel (PIPE) serve as the receiver.",
    "MCF作为数据接收者，是以设备（GROUP）、通道（PIPE）为接收者。": "When MCF acts as a data receiver, the device (GROUP) and channel (PIPE) serve as the receiver.",
    "其他情况均需指定设备号和通道号。": "In other cases, both the device number and channel number must be specified.",

    # ── Video buffer pool descriptions ──
    "一般linear格式的YUV或者raw数据缓存池配置，VI/VPSS模块紧凑段压缩格式需使用单独计算接口": "General linear format YUV or RAW data buffer pool configuration. VI/VPSS module compact segment compression format requires a separate calculation interface.",
    "一般linear格式的YUV或者raw数据缓存池大小，VI/VPSS模块紧凑段压缩格式需使用单独计算接口": "General linear format YUV or RAW data buffer pool size. VI/VPSS module compact segment compression format requires a separate calculation interface.",
    "HNR使用的帧数据缓存池，仅Hi3403V100支持": "Frame data buffer pool used by HNR, only supported on Hi3403V100.",
    "raw数据根据压缩率获取缓存池配置，仅Hi3403V100支持": "Obtains buffer pool configuration for RAW data based on compression ratio, only supported on Hi3403V100.",
    "VDEC输出的YUV帧存缓存池": "YUV frame buffer pool for VDEC output.",
    "VDEC输出的Tmv数据缓存池": "Tmv data buffer pool for VDEC output.",
    "VENC Picture信息VB大小，支持帧节省模式计算": "VENC Picture information VB size, supports frame saving mode calculation.",
    "VENC Picture VB大小，支持帧节省模式计算": "VENC Picture VB size, supports frame saving mode calculation.",
    "VENC参考帧大小，Hi3403V100/SS626V100不支持": "VENC reference frame size, not supported on Hi3403V100/SS626V100.",
    "VENC参考帧信息（pme、pmeinfo、tmv）大小": "VENC reference frame information (pme, pmeinfo, tmv) size.",
    "Hi3403V100/SS626V100不支持": "Not supported on Hi3403V100/SS626V100.",
    "qpmap映射表大小": "qpmap mapping table size.",
    "qpmap映射表stride": "qpmap mapping table stride.",
    "roi map映射表大小": "roi map mapping table size.",
    "roi map映射表stride": "roi map mapping table stride.",
    "skip weight映射表大小": "skip weight mapping table size.",
    "skip weight映射表stride": "skip weight mapping table stride.",
    "AVS输入的YUV数据缓存池，仅Hi3403V100支持": "YUV data buffer pool for AVS input, only supported on Hi3403V100.",
    "MCF场景彩色通路VPSS通道VB大小，仅Hi3403V100支持": "VPSS channel VB size for MCF scene color path, only supported on Hi3403V100.",
    "MCF场景黑白通路VPSS通道VB大小，仅Hi3403V100支持": "VPSS channel VB size for MCF scene monochrome path, only supported on Hi3403V100.",
    "VI输出的YUV数据缓存池大小，仅Hi3403V100支持": "YUV data buffer pool size for VI output, only supported on Hi3403V100.",
    "VPSS输出的YUV数据缓存池大小，仅Hi3403V100支持": "YUV data buffer pool size for VPSS output, only supported on Hi3403V100.",

    # ── VI/VPSS mode descriptions ──
    "VI_CAP与VI_PROC之间在线数据流传输，此模式下VI_CAP不会写出RAW数据到DDR，而是直接把数据流送给VI_PROC。": "Online data flow transmission between VI_CAP and VI_PROC. In this mode, VI_CAP does not write RAW data to DDR; instead, it directly sends the data stream to VI_PROC.",
    "VI_PROC与VPSS之间的在线数据流传输，在此模式下VI_PROC不会写出YUV数据到DDR，而是直接把数据流送给VPSS。": "Online data flow transmission between VI_PROC and VPSS. In this mode, VI_PROC does not write YUV data to DDR; instead, it directly sends the data stream to VPSS.",
    "VI_CAP写出RAW数据到DDR，然后VI_PROC从DDR读取RAW数据进行后处理。": "VI_CAP writes RAW data to DDR, then VI_PROC reads RAW data from DDR for post-processing.",
    "VI_PROC写出YUV数据到DDR，然后VPSS从DDR读取YUV数据进行后处理。": "VI_PROC writes YUV data to DDR, then VPSS reads YUV data from DDR for post-processing.",

    # ── Requirements lines ──
    "头文件：ot_common_sys.h、ss_mpi_sys.h": "Header file: ot_common_sys.h, ss_mpi_sys.h",
    "库文件：libss_mpi.a": "Library file: libss_mpi.a",

    # ── VB forced destruction ──
    "VB在占用状态时无法被销毁，插入xx_base.ko时加上模块参数g_vb_force_exit=1，即使VB正在被使用也可强制销毁，因此请谨慎使用此功能，需保证业务正常运行时不可主动销毁VB，必须待所有业务完全退出之后才能主动销毁VB。": "VB cannot be destroyed while in use. By adding the module parameter g_vb_force_exit=1 when inserting xx_base.ko, VB can be forcibly destroyed even while in use. Use this feature with caution. Ensure that VB is not actively destroyed during normal operation; it must only be actively destroyed after all services have fully exited.",

    "强制销毁VB功能是为了应用程序异常崩溃之后方便业务重启而设计的：用户态应用程序异常崩溃之后，应用程序已经无法按正常的业务退出流程操作，此时重启业务前须先进行ss_mpi_sys_exit和ss_mpi_vb_exit把上次应用程序异常崩溃之后无法销毁的VB资源先销毁，然后再进行正常的业务重启流程。": "The forced VB destruction feature is designed to facilitate service restart after an application crash: After a user-space application crashes abnormally, the application can no longer follow the normal service exit procedure. Before restarting the service, ss_mpi_sys_exit and ss_mpi_vb_exit must be called first to destroy the VB resources that could not be destroyed after the previous abnormal crash, and then the normal service restart procedure can be followed.",

    "无特殊说明，SS625V100/SS626V100的描述与SS528V100一致，SS524V100的描述与SS522V100一致。": "Unless otherwise specified, the descriptions for SS625V100/SS626V100 are the same as SS528V100, and the descriptions for SS524V100 are the same as SS522V100.",
    "SS528V100、SS625V100和SS524V100不支持低延时、拼接和MCF": "SS528V100, SS625V100, and SS524V100 do not support low latency, stitching, and MCF.",
    "各模块低延时开启会与一些特定功能组合存在冲突，具体开启的方法及对应的限制参考各模块章节中相关的低延时描述。": "Enabling low latency on each module may conflict with certain specific feature combinations. For the specific enabling method and corresponding restrictions, refer to the low latency description in each module chapter.",
    "Hi3403V100/SS626V100支持低延时，支持的模块分别见表1和表2，未在列表中的模块不支持低延时。": "Hi3403V100/SS626V100 support low latency. See Table 1 and Table 2 for supported modules; modules not listed do not support low latency.",

    # ── VI overview ──
    "视频输入（VI）模块实现的功能：通过MIPI Rx（含MIPI接口、LVDS接口和HISPI接口），BT.1120，BT.656，BT.601，DC等接口接收视频数据。VI将接收到的数据存入到指定的内存区域，在此过程中，VI可以对接收到的原始视频图像数据进行处理，实现视频数据的采集。": "The Video Input (VI) module receives video data through MIPI Rx (including MIPI, LVDS, and HISPI interfaces), BT.1120, BT.656, BT.601, DC, and other interfaces. VI stores the received data into the specified memory area. During this process, VI can process the received raw video image data to achieve video data capture.",

    "详情请参考\"系统控制\"章节的\"VI和VPSS\"的工作模式描述。": "For details, refer to the \"VI and VPSS\" working mode description in the \"System Control\" chapter.",

    # ── VO overview ──
    "VO（Video Output，视频输出）模块主动从内存相应位置读取视频和图形数据，并通过相应的显示设备输出视频和图形。解决方案支持的显示/回写设备、视频层和图形层情况如表1所示。": "The VO (Video Output) module actively reads video and graphics data from the corresponding memory locations and outputs video and graphics through the corresponding display devices. The display/writeback devices, video layers, and graphics layers supported by each solution are shown in Table 1.",

    # ── VPSS overview etc. ──
    "VPSS（Video Process SubSystem，视频处理子系统）支持对输入视频图像进行缩放、锐化、裁剪、旋转、镜像等多种处理。同时VPSS提供多种处理算法，如去噪、去隔行等。支持内插（interlace）和逐行（progressive）两种扫描格式视频源的处理。": "The VPSS (Video Process SubSystem) supports various processing operations on input video images, including scaling, sharpening, cropping, rotation, and mirroring. It also provides multiple processing algorithms such as denoising and de-interlacing. It supports processing of both interlaced and progressive scan format video sources.",

    "MCF（Multi-Camera Fusion，多目融合，仅Hi3403V100支持）模块支持多路视频拼接融合，实现全景监控的功能，支持对ISP输入的多路RAW数据做图像融合，得到合成图像。": "The MCF (Multi-Camera Fusion, only supported on Hi3403V100) module supports multi-channel video stitching and fusion to achieve panoramic monitoring. It supports image fusion of multi-channel RAW data from ISP input to produce a composite image.",

    "AVS（Anti-Vibration System，电子防抖，仅Hi3403V100支持）模块通过陀螺仪数据和图像数据融合处理以实现电子防抖功能。": "The AVS (Anti-Vibration System, only supported on Hi3403V100) module achieves electronic image stabilization through fusion processing of gyroscope data and image data.",

    "本章主要包括以下内容：": "This chapter mainly includes the following:",
    "芯片解决方案与业务模块的映射关系": "Mapping between chip solutions and service modules",

    # ── Image figure/table captions ──
    "典型的公共视频缓存池数据流图": "Typical Video Buffer Pool Data Flow Diagram",
    "VI在软件层次划分的4个部分": "Four software-level partitions of VI",

    # ═══════════════════════════════════════════════════════════════
    #  File 1: 06-视频编码-61-63.md  (VENC Overview + API Reference)
    # ═══════════════════════════════════════════════════════════════
    "VENC模块，即视频编码模块。本模块支持多路实时编码，且每路编码独立，编码协议和编码profile可以不同。本模块支持视频编码同时，调度Region模块对编码图像内容进行叠加和遮挡。":
        "The VENC module is the video encoding module. It supports multi-channel real-time encoding, with each channel operating independently and supporting different encoding protocols and profiles. It supports video encoding while scheduling the Region module to overlay and cover encoded image content.",
    "不同型号的解决方案支持不同的编码规格，解决方案支持的编码规格如[表1](#_Ref322704612)所示。":
        "Different solution models support different encoding specifications, as shown in [Table 1](#_Ref322704612).",
    "典型的编码流程包括了输入图像的接收、图像内容的遮挡和覆盖、图像的编码、以及码流的输出等过程。":
        "A typical encoding process includes receiving input images, covering and overlaying image content, encoding images, and outputting the encoded stream.",
    "VENC模块由编码通道子模块（VENC）和编码协议子模块（H.264/H.265/JPEG/MJPEG）组成。":
        "The VENC module consists of the encoding channel sub-module (VENC) and the encoding protocol sub-modules (H.264/H.265/JPEG/MJPEG).",
    "通道接收到图像之后，比较图像尺寸和编码通道尺寸：":
        "After receiving an image, the channel compares the image size with the encoding channel size:",
    "如果输入图像比编码通道尺寸大，VENC将按照编码通道尺寸大小，调用VGS对源图像进行缩小，然后对缩小之后的图像进行编码。":
        "If the input image is larger than the encoding channel size, VENC calls VGS to downscale the source image to the encoding channel size, then encodes the downscaled image.",
    "如果输入图像比编码通道尺寸小，VENC丢弃源图像。VENC不支持放大输入图像编码。":
        "If the input image is smaller than the encoding channel size, VENC discards the source image. VENC does not support encoding upscaled input images.",
    "如果输入图像与编码通道尺寸相当，VENC直接接收源图像，进行编码。":
        "If the input image matches the encoding channel size, VENC directly receives the source image for encoding.",
    "REGION模块支持提供对图像内容的遮挡/叠加信息，编码前先完成遮挡/叠加，再进行编码，输出码流。":
        "The REGION module provides cover/overlay information for image content. Cover/overlay is applied before encoding, and then the encoded stream is output.",
    "编码通道作为基本容器，保存编码通道的多种用户设置和管理编码通道的多种内部资源。编码通道完成图像转化为码流的功能，具体由码率控制器和编码器协同完成。这里的编码器指的是狭义上的编码器，只完成编码功能。码率控制器提供了对编码参数的控制和调整，从而对输出码率进行控制。":
        "The encoding channel serves as a basic container, storing various user settings and managing various internal resources of the encoding channel. It converts images into streams through the collaboration of the rate controller and the encoder. The encoder here refers to the encoder in the narrow sense, which only performs encoding. The rate controller provides control and adjustment of encoding parameters, thereby controlling the output bitrate.",
    "码率控制器实现对编码码率进行控制。":
        "The rate controller controls the encoding bitrate.",
    "从信息学的角度分析，图像的压缩比越低，压缩图像的质量越高；图像压缩比例越高，压缩图像的质量越低。在场景变化的情况下，追求图像质量稳定，则编码码率会波动较大；如追求编码码率稳定，则图像质量会波动较大。以H.264编码为例，通常图像Qp越低，图像的质量越好，码率越高；图像Qp越高，图像质量越差，码率越低。":
        "From an information theory perspective, the lower the compression ratio, the higher the compressed image quality; the higher the compression ratio, the lower the compressed image quality. When scene changes occur, pursuing stable image quality results in larger bitrate fluctuations, while pursuing stable bitrate results in larger image quality fluctuations. For H.264 encoding, generally the lower the Qp, the better the image quality and the higher the bitrate; the higher the Qp, the worse the image quality and the lower the bitrate.",
    "码率控制是针对连续的编码码流而言，所以，JPEG协议编码通道不包括码率控制功能。":
        "Rate control targets continuous encoded streams, so JPEG protocol encoding channels do not include rate control functionality.",
    "CBR（Constant Bit Rate）固定比特率。即在码率统计时间内保证编码码率平稳。码率稳定主要由两个量来评估。":
        "CBR (Constant Bit Rate) ensures a stable encoding bitrate within the bitrate statistics time. Bitrate stability is mainly evaluated by two parameters.",
    "码率统计时间stats_time": "Bitrate statistics time stats_time",
    "行级码率控制调节幅度row_qp_delta": "Row-level rate control adjustment range row_qp_delta",
    "VBR（Variable Bit Rate）可变比特率，即允许在码率统计时间内编码码率波动，从而保证编码图像质量平稳。":
        "VBR (Variable Bit Rate) allows the encoding bitrate to fluctuate within the bitrate statistics time, ensuring stable encoded image quality.",
    "AVBR（Adaptive Variable Bit Rate）自适应可变比特率，即允许在码率统计时间内编码码率波动，从而保证编码图像质量平稳。码率控制内部会检测当前场景的运动静止状态，在运动时用较高码率编码，在静止时主动降低目标码率。":
        "AVBR (Adaptive Variable Bit Rate) allows the encoding bitrate to fluctuate within the bitrate statistics time to ensure stable image quality. The rate controller internally detects motion/static states, using higher bitrate for motion and reducing target bitrate for static scenes.",
    "CVBR (Constrained Variable Bit Rate) 是以VBR为基础，旨在提供平稳的图像质量的码控算法，同时对VBR的码率进行限制，以满足传输带宽以及存储空间的要求。":
        "CVBR (Constrained Variable Bit Rate) is built upon VBR, aiming to provide stable image quality rate control while limiting the VBR bitrate to meet transmission bandwidth and storage space requirements.",
    "FIXQP固定QP值。在码率统计时间内，编码图像所有宏块QP值相同，采用用户设定的图像QP值，I帧和P帧的QP值可以分别设置。":
        "FIXQP uses a fixed QP value. Within the bitrate statistics time, all macroblocks have the same QP value specified by the user. I-frame and P-frame QP values can be set separately.",
    "QPMAP 模式下允许用户自由决定码控的策略。":
        "QPMAP mode allows users to freely determine the rate control strategy.",
    "ROI（Region Of Interest）编码：感兴趣区域编码。":
        "ROI (Region Of Interest) encoding.",
    "用户可以通过配置ROI区域，对该区域的图像Qp进行限制，从而实现图像中该区域的Qp与其他图像区域的差异化。系统现仅支持对H.264/H.265通道进行ROI设置。系统提供了8个感兴趣区域，可供用户同时使用。":
        "Users can configure ROI regions to limit the image Qp in those regions, achieving Qp differentiation between ROI and non-ROI areas. The system currently only supports ROI for H.264/H.265 channels and provides 8 regions of interest for simultaneous use.",
    "JPEG编码抓拍模式有两种工作模式：全部抓拍模式和抓拍模式。":
        "JPEG encoding snapshot mode has two working modes: all-snapshot mode and snapshot mode.",
    "全部抓拍模式：通道启动接收图像后，编码所有接收的图像。":
        "All-snapshot mode: After the channel starts receiving images, all received images are encoded.",
    "抓拍模式：通道启动接收图像后，只编码标记为抓拍帧的图像。":
        "Snapshot mode: After the channel starts receiving images, only images marked as snapshot frames are encoded.",
    "P帧刷新ISlice，可以为客户提供码率非常平滑的编码方式，每个I帧和P帧的大小可以非常接近。":
        "P-frame refresh ISlice provides a very smooth bitrate encoding method, where I-frame and P-frame sizes can be very close.",
    "编码码流帧配置支持两种模式：单包模式和多包模式（在不调用slice分割接口及其插入用户数据接口的情况下），如[图1](#fig175464472117)所示。":
        "The encoded stream frame configuration supports two modes: single-packet mode and multi-packet mode (when the slice split and user data insertion interfaces are not called), as shown in [Figure 1](#fig175464472117).",
    "编码码流buffer配置支持两种模式：一般模式和省内存模式。":
        "The encoded stream buffer configuration supports two modes: normal mode and memory-saving mode.",
    "视频编码模块主要提供视频编码通道的创建和销毁、视频编码通道的复位、开启和停止接收图像、设置和获取编码通道属性、获取和释放码流等功能。":
        "The video encoding module provides functions for creating and destroying encoding channels, resetting channels, starting and stopping image reception, setting and getting encoding channel attributes, and acquiring and releasing encoded streams.",
    "该功能模块提供以下MPI：":
        "This module provides the following MPIs:",
    "创建编码通道。": "Creates an encoding channel.",
    "销毁编码通道。": "Destroys an encoding channel.",
    "复位编码通道。": "Resets the encoding channel.",
    "复位通道。": "Resets the channel.",
    "开启编码通道接收输入图像，允许指定接收帧数，超出指定的帧数后自动停止接收图像。":
        "Starts the encoding channel to receive input images. Allows specifying the number of frames to receive. Automatically stops after exceeding the specified number.",
    "停止编码通道接收输入图像。": "Stops the encoding channel from receiving input images.",
    "查询编码通道状态。": "Queries the encoding channel status.",
    "设置编码通道的编码属性。": "Sets the encoding attributes of the encoding channel.",
    "获取编码通道的编码属性。": "Gets the encoding attributes of the encoding channel.",
    "获取编码码流。": "Gets the encoded stream.",
    "释放码流缓存。": "Releases the stream buffer.",
    "获取码流buffer的物理地址和大小。": "Gets the physical address and size of the stream buffer.",
    "插入用户数据。": "Inserts user data.",
    "支持用户发送原始图像进行编码。": "Supports users sending raw images for encoding.",
    "设置编码通道属性。": "Sets encoding channel attributes.",
    "获取编码通道属性。": "Gets encoding channel attributes.",
    "编码通道号。": "Encoding channel number.",
    "通道号。": "Channel number.",
    "编码通道属性。": "Encoding channel attributes.",
    "编码通道的状态。": "Encoding channel status.",
    "接收图像参数结构体，用于指定需要接收的图像帧数。":
        "Receive parameter structure used to specify the number of image frames to receive.",

    # API function descriptions
    "支持用户发送原始图像及该图的QpMap表信息进行编码。": "Supports sending raw images with their QpMap table information for encoding.",
    "支持用户对于H.264/H.265编码通路发送外部码率控制信息进行编码。": "Supports sending external rate control information for H.264/H.265 encoding paths.",
    "用户发送2个图像及马赛克区域信息进行编码": "Sends 2 images and mosaic area information for encoding.",
    "设置编码通道复合编码配置": "Sets the composite encoding configuration of the encoding channel.",
    "获取编码通道复合编码配置": "Gets the composite encoding configuration of the encoding channel.",
    "请求VI(虚拟I帧)帧。": "Requests a VI (Virtual I-frame) frame.",
    "请求IDR帧。": "Requests an IDR frame.",
    "使能IDR帧。": "Enables an IDR frame.",
    "获取编码通道对应的设备文件句柄。": "Gets the device file handle of the encoding channel.",
    "关闭编码通道对应的设备文件句柄。": "Closes the device file handle of the encoding channel.",
    "设置编码通道的感兴趣区域编码配置。": "Sets the ROI encoding configuration of the encoding channel.",
    "获取编码通道的感兴趣区域编码配置。": "Gets the ROI encoding configuration of the encoding channel.",
    "设置编码通道的感兴趣区域编码高级配置。": "Sets the advanced ROI encoding configuration of the encoding channel.",
    "获取编码通道的感兴趣区域编码高级配置。": "Gets the advanced ROI encoding configuration of the encoding channel.",
    "设置编码通道非感兴趣区域的帧率配置。": "Sets the frame rate configuration for non-ROI regions.",
    "获取编码通道非感兴趣区域的帧率配置。": "Gets the frame rate configuration for non-ROI regions.",
    "设置H.264编码的帧内预测配置。": "Sets the intra prediction configuration for H.264 encoding.",
    "获取H.264编码的帧内预测配置。": "Gets the intra prediction configuration for H.264 encoding.",
    "设置H.264编码的变换、量化配置。": "Sets the transform and quantization configuration for H.264 encoding.",
    "获取H.264编码的变换、量化配置。": "Gets the transform and quantization configuration for H.264 encoding.",
    "设置H.264编码的熵编码配置。": "Sets the entropy coding configuration for H.264 encoding.",
    "获取H.264编码的熵编码配置。": "Gets the entropy coding configuration for H.264 encoding.",
    "设置H.264编码的deblocking配置。": "Sets the deblocking configuration for H.264 encoding.",
    "获取H.264编码的deblocking配置。": "Gets the deblocking configuration for H.264 encoding.",
    "设置H.264编码的VUI配置。": "Sets the VUI configuration for H.264 encoding.",
    "获取H.264编码的VUI配置。": "Gets the VUI configuration for H.264 encoding.",
    "设置H.265协议编码通道的VUI参数。": "Sets the VUI parameters for the H.265 encoding channel.",
    "获取H.265协议编码通道的VUI配置": "Gets the VUI configuration for the H.265 encoding channel.",
    "设置JPEG编码的参数集合。": "Sets the JPEG encoding parameter set.",
    "获取JPEG编码的参数集合。": "Gets the JPEG encoding parameter set.",
    "设置MJPEG协议编码通道的高级参数。": "Sets the advanced parameters for the MJPEG encoding channel.",
    "获取MJPEG协议编码通道的高级参数。": "Gets the advanced parameters for the MJPEG encoding channel.",
    "设置通道码率控制高级参数。": "Sets the channel rate control advanced parameters.",
    "获取通道码率控制高级参数。": "Gets the channel rate control advanced parameters.",
    "设置H.264/H.265编码通道高级跳帧参考参数。": "Sets the advanced skip frame reference parameters for H.264/H.265 channels.",
    "获取H.264/H.265编码通道高级跳帧参考参数。": "Gets the advanced skip frame reference parameters for H.264/H.265 channels.",
    "设置JPEG抓拍通道的抓拍模式。": "Sets the snapshot mode for the JPEG snapshot channel.",
    "获取JPEG抓拍通道的抓拍模式。": "Gets the snapshot mode for the JPEG snapshot channel.",
    "设置H.264/H.265编码的slice分割配置。": "Sets the slice split configuration for H.264/H.265 encoding.",
    "获取H.264/H.265编码的slice分割配置。": "Gets the slice split configuration for H.264/H.265 encoding.",
    "设置H.264/H.265通道的搜索窗范围。": "Sets the search window range for H.264/H.265 channels.",
    "获取H.264/H.265通道的搜索窗范围。": "Gets the search window range for H.264/H.265 channels.",
    "设置H.265编码的PU配置。": "Sets the PU configuration for H.265 encoding.",
    "获取H.265编码的PU配置。": "Gets the PU configuration for H.265 encoding.",
    "设置H.265编码的变换、量化配置。": "Sets the transform and quantization configuration for H.265 encoding.",
    "获取H.265编码的变换、量化配置。": "Gets the transform and quantization configuration for H.265 encoding.",
    "设置H.265通道的熵编码属性。": "Sets the entropy coding attributes for the H.265 channel.",
    "获取H.265通道的熵编码属性。": "Gets the entropy coding attributes for the H.265 channel.",
    "设置H.265编码的deblocking配置。": "Sets the deblocking configuration for H.265 encoding.",
    "获取H.265编码的deblocking配置。": "Gets the deblocking configuration for H.265 encoding.",
    "设置H.265编码的SAO配置。": "Sets the SAO configuration for H.265 encoding.",
    "获取H.265编码的SAO配置。": "Gets the SAO configuration for H.265 encoding.",
    "设置瞬时码率超出阈值时丢帧策略的配置。": "Sets the frame drop strategy when the instantaneous bitrate exceeds the threshold.",
    "获取瞬时码率超出阈值时丢帧策略的配置。": "Gets the frame drop strategy when the instantaneous bitrate exceeds the threshold.",
    "设置超大帧处理配置。": "Sets the super frame processing configuration.",
    "获取超大帧处理配置。": "Gets the super frame processing configuration.",
    "获取P帧刷Islice的设置参数。": "Gets the P-frame refresh ISlice parameters.",
    "设置P帧刷Islice的参数。": "Sets the P-frame refresh ISlice parameters.",
    "设置编码相关的模块参数。": "Sets encoding-related module parameters.",
    "获取编码相关的模块参数。": "Gets encoding-related module parameters.",
    "设置H.264/H.265通道的SSE属性。": "Sets the SSE attributes for H.264/H.265 channels.",
    "获取H.264/H.265通道的SSE属性。": "Gets the SSE attributes for H.264/H.265 channels.",
    "设置Venc通道参数。": "Sets the VENC channel parameters.",
    "获取Venc通道参数。": "Gets the VENC channel parameters.",
    "设置通道的前景保护参数。": "Sets the channel foreground protection parameters.",
    "获取通道的前景保护参数。": "Gets the channel foreground protection parameters.",
    "设置编码场景模式。": "Sets the encoding scene mode.",
    "获取编码场景模式。": "Gets the encoding scene mode.",
    "将编码通道绑定到某个视频缓存VB池中。": "Binds the encoding channel to a video buffer VB pool.",
    "将编码通道从某个视频缓存VB池中解绑定。": "Unbinds the encoding channel from a video buffer VB pool.",
    "设置CU模式的倾向性。": "Sets the CU mode tendency.",
    "获取CU模式的倾向性配置。": "Gets the CU mode tendency configuration.",
    "设置cu/mb选择Skip模式的倾向性。": "Sets the tendency for cu/mb to select Skip mode.",
    "获取cu/mb选择Skip模式的倾向性配置。": "Gets the tendency for cu/mb to select Skip mode.",
    "设置去除呼吸效应参数。": "Sets the de-breathing effect parameters.",
    "获取去除呼吸效应参数。": "Gets the de-breathing effect parameters.",
    "设置分层qp参数。": "Sets the hierarchical QP parameters.",
    "获取分层qp参数。": "Gets the hierarchical QP parameters.",
    "设置RC模块的高级参数。": "Sets the RC module advanced parameters.",
    "获取RC模块的高级参数。": "Gets the RC module advanced parameters.",
    "设置jpeg ROI属性。": "Sets the JPEG ROI attributes.",
    "获取jpeg ROI属性。": "Gets the JPEG ROI attributes.",
    "开启/关闭智能编码。": "Enables/disables smart video coding.",
    "获取智能编码相关参数。": "Gets smart video coding parameters.",
    "设置智能编码相关参数。": "Sets smart video coding parameters.",
    "发送智能检测目标框属性信息。": "Sends smart detection target rectangle attribute information.",
    "获取编码器md检测信息。": "Gets encoder MD detection information.",
    "设置编码器md检测区域控制信息。": "Sets encoder MD detection area control information.",
    "获取背景去模糊算法相关参数。": "Gets background deblurring algorithm parameters.",
    "设置背景去模糊算法相关参数。": "Sets background deblurring algorithm parameters.",
    "获取H.264/H.265参数集ID。": "Gets the H.264/H.265 parameter set ID.",
    "设置H.264/H.265参数集ID。": "Sets the H.264/H.265 parameter set ID.",
    "获取H.264协议编码通道的POC类型。": "Gets the POC type of the H.264 encoding channel.",
    "设置H.264协议编码通道的POC类型。": "Sets the POC type of the H.264 encoding channel.",
    "获取JPEG编码通道的强边去Ring效应强度等级。": "Gets the strong edge dering level for the JPEG encoding channel.",
    "设置JPEG编码通道的强边去Ring效应强度等级。": "Sets the strong edge dering level for the JPEG encoding channel.",
    "是否使能JPEG编码通道的Block效应。": "Enables/disables the block effect for the JPEG encoding channel.",
    "获取运动物体区域拖尾和残留区域检测参数。": "Gets detection parameters for motion object trailing and residual areas.",
    "设置运动物体区域拖尾和残留区域检测参数。": "Sets detection parameters for motion object trailing and residual areas.",
    "获取JPEG和MJPEG编码通道的ROI高级属性。": "Gets the advanced ROI attributes for JPEG and MJPEG channels.",
    "设置JPEG和MJPEG编码通道的ROI高级属性。": "Sets the advanced ROI attributes for JPEG and MJPEG channels.",
    "**注意：SS528V100/SS625V100/SS524V100/SS522V101/Hi3403V100/SS626V100不支持PRORES相关接口。**":
        "**Note: SS528V100/SS625V100/SS524V100/SS522V101/Hi3403V100/SS626V100 do not support PRORES-related interfaces.**",

    # Encoding prose translations
    "1. 通道的帧率控制默认不打开，需要用户调用接口设置。RC中也具有帧率控制功能。推荐使用RC的帧率控制，这样不会对码率控制造成过大的冲击。":
        "1. Channel frame rate control is disabled by default and must be set via the API. RC also has frame rate control functionality. It is recommended to use RC frame rate control to avoid excessive impact on bitrate control.",
    "2. 对于H.264/ H.265编码，输入图像格式由非单分量切换为单分量时，由于存在帧间预测量化误差，在编码出下一个I帧之前图像会存有色度残留。建议客户在切换单分量时调用接口[ss_mpi_venc_reset_chn](#ZH-CN_TOPIC_0000002408258510)进行通道复位。":
        "2. For H.264/H.265 encoding, when switching from non-single-component to single-component input format, chroma residuals may persist until the next I-frame due to inter-frame prediction quantization errors. It is recommended to call [ss_mpi_venc_reset_chn](#ZH-CN_TOPIC_0000002408258510) to reset the channel when switching to single-component mode.",
    "彩转灰：即VENC支持把彩色图像转换成灰度图像进行编码。具体功能请参考相关API：ss_mpi_venc_set_chn_param中彩转灰部分。":
        "Color-to-grayscale: VENC supports converting color images to grayscale images for encoding. See the color-to-grayscale section of ss_mpi_venc_set_chn_param for details.",
    "裁剪编码：即VENC从图像中裁剪出一部分进行编码，用户可以设置裁剪的起始点X、Y和裁剪的宽度width和高度height，具体功能请参考相关[ss_mpi_venc_set_chn_param](#ZH-CN_TOPIC_0000002441698329)和[图1](#fig1953319321786)等。":
        "Crop encoding: VENC crops a portion of the image for encoding. Users can set the crop start point X, Y and the crop width and height. See [ss_mpi_venc_set_chn_param](#ZH-CN_TOPIC_0000002441698329) and [Figure 1](#fig1953319321786) for details.",

    # ═══════════════════════════════════════════════════════════════
    #  File 2: 06-视频编码-64-65.md  (Data Types)
    # ═══════════════════════════════════════════════════════════════
    "相关数据类型、数据结构定义如下：": "The related data types and data structures are defined as follows:",

    # ═══════════════════════════════════════════════════════════════
    #  File 3: 13-proc调试信息-131-1315.md  (Proc Debug Overview + SYS)
    # ═══════════════════════════════════════════════════════════════
    "调试信息采用了Linux下的proc文件系统，可实时反映当前系统的运行状态，所记录的信息可供问题定位及分析时使用。":
        "The debug information uses the Linux proc file system to reflect current system runtime status in real time. The recorded information can be used for problem location and analysis.",
    "记录当前SYS模块的使用情况。": "Records the current SYS module usage.",
    "记录当前VB模块的buffer使用情况。": "Records the current VB module buffer usage.",
    "记录当前各个模块的调试级别，内部调试用。": "Records the current debug level of each module, for internal debugging.",
    "CHNL模块状态。": "CHNL module status.",
    "视频缩放处理单元状态信息。": "Video scaling processing unit status information.",
    "H.265编码过程中，各通道的编码属性、状态以及历史信息统计。": "Statistics of encoding attributes, status, and historical info during H.265 encoding.",
    "H.264编码过程中，各通道的编码属性、状态以及历史信息统计。": "Statistics of encoding attributes, status, and historical info during H.264 encoding.",
    "JPEG编码过程中，各通道的编码属性、状态以及历史信息统计。": "Statistics of encoding attributes, status, and historical info during JPEG encoding.",
    "编码通道的码流控制属性、状态以及历史信息统计。": "Statistics of stream control attributes, status, and history for encoding channels.",
    "视频叠加OSD的区域管理信息。": "Video overlay OSD region management information.",
    "视频编码器信息。": "Video encoder information.",
    "视频解码器信息。": "Video decoder information.",
    "视频解码过程中各通道的公共信息。": "Common information for each channel during video decoding.",
    "视频解码过程中各通道的码流信息。": "Stream information for each channel during video decoding.",
    "视频解码过程中各通道的语法信息。": "Syntax information for each channel during video decoding.",
    "视频解码过程中各通道的硬件配置信息。": "Hardware configuration info for each channel during video decoding.",
    "视频输入模块信息。": "Video input module information.",
    "视频输出模块信息。": "Video output module information.",
    "视频预处理模块信息。": "Video preprocessing module information.",
    "音频输入信息。": "Audio input information.",
    "音频输出信息。": "Audio output information.",
    "音频编码信息。": "Audio encoding information.",
    "音频解码信息。": "Audio decoding information.",
    "Acodec音量信息。": "Acodec volume information.",
    "视频侦测分析模块信息。": "Video detection analysis module information.",
    "拼接处理模块信息": "Stitching processing module information.",
    "在控制台上可以使用cat命令查看信息，例如cat /proc/umap/venc；也可以使用其他常用的文件操作命令，例如 cp /proc/umap/ ./ -rf，将所有umap下的proc文件拷贝到当前目录。":
        "Information can be viewed on the console using the cat command, e.g., cat /proc/umap/venc. Other common file operation commands can also be used, e.g., cp /proc/umap/ ./ -rf.",
    "在应用程序中可以将上述文件当作普通只读文件进行读操作，例如fopen、fread等。":
        "In applications, these files can be read as ordinary read-only files using functions such as fopen, fread, etc.",
    "参数在描述时有以下2种情况需要注意：": "Two cases should be noted when describing parameters:",
    "取值为{0, 1}的参数，如未列出具体取值和含义的对应关系，则参数为1时表示肯定，为0时表示否定。":
        "For parameters with values {0, 1}, if the mapping is not listed, 1 indicates affirmative and 0 indicates negative.",
    "取值为{aaa, bbb, ccc}的参数，未列出具体取值和含义的对应关系，但可直接根据取值aaa、bbb或ccc判断参数含义。":
        "For parameters with values {aaa, bbb, ccc}, the meaning can be directly inferred from the values.",

    # ═══════════════════════════════════════════════════════════════
    #  File 4: 13-proc调试信息-1316-1329.md  (VPSS Debug)
    # ═══════════════════════════════════════════════════════════════
    "记录当前VPSS属性配置以及状态信息。": "Records the current VPSS attribute configuration and status information.",
    "分块节点数量。取值范围为[1,16]，默认值为3，通过模块参数接口修改。": "Number of split nodes. Range: [1, 16]. Default: 3. Modified via the module parameter interface.",
    "是否支持Coverex相对坐标。": "Whether Coverex relative coordinates are supported.",
    "Y：使能；": "Y: Enabled;",
    "N：关闭。": "N: Disabled.",
    "N：不使能；": "N: Disabled;",
    "Y：使能。": "Y: Enabled.",
    "调度模式，通过SYS接口设置。": "Scheduling mode, set via the SYS interface.",
    "NORMAL：正常调度模式。": "NORMAL: Normal scheduling mode.",
    "QUICK：快速调度模式。": "QUICK: Quick scheduling mode.",
    "3DNR延时模式使能。": "3DNR delay mode enable.",
    "组的多任务使能。": "Group multi-task enable.",
    "VPSS模块高性开关，仅Hi3403V100支持。": "VPSS module high-performance switch, only supported by Hi3403V100.",
    "VPSS组链阈值。": "VPSS group chain threshold.",
    "有效范围：[40, 160]。": "Valid range: [40, 160].",
    "VPSS支持输出低延时开关。": "VPSS output low-delay switch.",
    "VPSS proc统计处理时间数据开关。": "VPSS proc processing time statistics switch.",
    "关闭时VPSS proc中的cost_time、max_cost_time、proc_time、中断工作时间等信息不进行统计。": "When disabled, cost_time, max_cost_time, proc_time, etc. are not counted in VPSS proc.",

    # ═══════════════════════════════════════════════════════════════
    #  File 5: isp-开发参考-1-2.md  (ISP Dev Reference)
    # ═══════════════════════════════════════════════════════════════
    "前言": "Preface",
    "本文为使用ISP开发的程序员而写，目的是为您在开发过程中遇到的问题提供解决办法和帮助。":
        "This document is written for programmers developing with ISP, aiming to provide solutions and assistance for issues encountered during development.",
    "本文以Hi3403V100描述为例，未有特殊说明，Hi3519AV200与Hi3403V100内容一致。":
        "This document uses Hi3403V100 as an example. Unless otherwise specified, Hi3519AV200 and Hi3403V100 have the same content.",
    "本文档（本指南）主要适用于以下工程师：": "This document (guide) mainly applies to the following engineers:",
    "技术支持工程师": "Technical Support Engineer",
    "软件开发工程师": "Software Development Engineer",
    "在本文中可能出现下列标志，它们所代表的含义如下。": "The following symbols may appear in this document. Their meanings are as follows.",
    "表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。": "Indicates a high-level risk hazard that, if not avoided, will result in death or serious injury.",
    "表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。": "Indicates a medium-level risk hazard that, if not avoided, could result in death or serious injury.",
    "表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。": "Indicates a low-level risk hazard that, if not avoided, could result in minor or moderate injury.",
    "用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。":
        "Used to convey device or environmental safety warnings. If not avoided, it may result in equipment damage, data loss, performance degradation, or other unpredictable consequences.",
    "须知\"不涉及人身伤害。": "\"Notice\" does not involve personal injury.",
    "对正文中重点信息的补充说明。": "Supplementary explanation of key information in the text.",
    "说明\"不是安全警示信息，不涉及人身、设备及环境伤害信息。": "\"Note\" is not a safety warning and does not involve personal injury, equipment damage, or environmental harm.",
    "\"须知\"不涉及人身伤害。": "\"Notice\" does not involve personal injury.",
    "\"说明\"不是安全警示信息，不涉及人身、设备及环境伤害信息。": "\"Note\" is not a safety warning and does not involve personal injury, equipment damage, or environmental harm.",
    "修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。":
        "The revision history accumulates descriptions of each document update. The latest version contains updates from all previous versions.",
    "第1次临时版本发布。": "First provisional release.",
    "ISP通过一系列数字图像处理算法完成对数字图像的效果处理。主要包括3A、坏点校正、去噪、强光抑制、背光补偿、色彩增强、镜头阴影校正等处理。ISP包括逻辑部分以及运行在其上的firmware。这里主要介绍ISP的用户接口。":
        "ISP performs image processing through a series of digital image processing algorithms. It mainly includes 3A, bad pixel correction, denoising, highlight suppression, backlight compensation, color enhancement, lens shading correction, etc. ISP consists of the logic part and the firmware running on it. This section mainly introduces the ISP user interface.",
    "ISP由ISP逻辑及运行在其上的Firmware组成，逻辑单元除了完成一部分算法处理外，还可以统计出当前图像的实时信息。Firmware通过获取ISP逻辑的图像统计信息，重新计算，反馈控制lens、sensor和ISP逻辑，以达到自动调节图像质量的目的。":
        "ISP consists of ISP logic and the firmware running on it. The logic unit can also collect real-time image information. The firmware obtains image statistics from ISP logic, recalculates, and provides feedback to control the lens, sensor, and ISP logic, achieving automatic image quality adjustment.",
    "ISP逻辑主要流程、具体概念和功能点请参见芯片手册。": "For the main ISP logic flow, specific concepts, and features, please refer to the chip manual.",
    "SDK支持用户使用多种开发模式：": "The SDK supports multiple development modes:",
    "2. 用户根据ISP库提供的3A算法注册接口，实现自己的3A算法库开发。这时用户需要根据ISP基础算法库和用户的3A算法库给出的sensor适配接口去适配不同的sensor。":
        "2. Users implement their own 3A algorithm library based on the 3A registration interface. Users need to adapt different sensors according to the sensor adaptation interfaces from the ISP basic library and their own 3A library.",
    "3. 用户部分使用SDK中3A算法库，部分实现自己的3A算法库。例如AE使用libot_ae.a，AWB使用自己的3A算法库。SDK提供了灵活多变的支持方式。":
        "3. Users partially use the SDK 3A algorithm library and partially implement their own. For example, AE uses libot_ae.a while AWB uses the user's own 3A library. The SDK provides flexible support methods.",
    "PQ Tools工具主要完成在PC端进行动态图像质量调节，可以调节多个影响图像质量的因子，如去噪强度、色彩转换矩阵、饱和度等。":
        "The PQ Tools tool performs dynamic image quality adjustment on the PC side, adjusting multiple factors such as denoising strength, color conversion matrix, saturation, etc.",
    "如果用户调试好图像效果后，可以使用PQ Tools工具提供的配置文件保存功能进行配置参数保存。在下次启动时系统可以使用PQ Tools工具提供的配置文件加载功能加载已经调节好的图像参数。":
        "After debugging image effects, users can save configuration parameters using the PQ Tools configuration save function. On the next startup, the system can load the adjusted parameters using the PQ Tools configuration load function.",
    "/* 注册sensor库 */": "/* Register sensor library */",
    "/* 注册AE算法库 */": "/* Register AE algorithm library */",
    "/* 注册AWB算法库 */": "/* Register AWB algorithm library */",

    # ISP notes
    "> **说明：**": "> **Note:**",
    ">![](public_sys-resources/icon-note.gif) **说明：**": "> **Note:**",
    ">![](public_sys-resources/icon-note.gif) **说明：** ": "> **Note:** ",
    ">![](public_sys-resources/icon-notice.gif) **须知：**": "> **Notice:**",
    ">![](public_sys-resources/icon-warning.gif) **警告：**": "> **Warning:**",
}

# Build a regex that matches any multi-character sentence/phrase
_sentence_pattern = re.compile(
    "|".join(re.escape(s) for s in sorted(SENTENCE_MAP.keys(), key=lambda x: -len(x)))
)

# ═══════════════════════════════════════════════════════════════
#  3. Helper functions
# ═══════════════════════════════════════════════════════════════

def has_cjk(s: str) -> bool:
    """Check if string contains CJK Unified Ideographs."""
    for ch in s:
        if '一' <= ch <= '鿿' or '　' <= ch <= '〿':
            return True
    return False


def is_code_block_line(line: str) -> bool:
    return line.strip().startswith("```")


def apply_sentence_map(text: str) -> str:
    """Replace known full sentences/phrases in text, longest first."""
    def repl(m):
        return SENTENCE_MAP[m.group(0)]
    return _sentence_pattern.sub(repl, text)


def translate_html_text(line: str) -> str:
    """Translate Chinese text inside HTML tags, preserving tag structure."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '<':
            j = line.index('>', i) + 1 if '>' in line[i:] else len(line)
            result.append(line[i:j])
            i = j
        else:
            text_start = i
            while i < len(line) and line[i] != '<':
                i += 1
            text_content = line[text_start:i]
            if has_cjk(text_content):
                text_content = apply_sentence_map(text_content)
            result.append(text_content)
    return ''.join(result)


def translate_plain_line(stripped: str) -> str:
    """Translate a plain text line (no HTML tags)."""
    if has_cjk(stripped):
        return apply_sentence_map(stripped)
    return stripped


# ═══════════════════════════════════════════════════════════════
#  4. Main translation function
# ═══════════════════════════════════════════════════════════════

def translate_file(src_path: str, dst_path: str) -> None:
    """Translate a Chinese .md file to English .en.md."""
    print(f"Processing: {src_path}")
    print(f"       =>  {dst_path}")

    with open(src_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_code_block = False
    in_frontmatter = False

    out_lines = []
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')

        # ── Code block tracking ──
        if is_code_block_line(line):
            in_code_block = not in_code_block
            out_lines.append(line)
            continue

        if in_code_block:
            out_lines.append(line)
            continue

        # ── Frontmatter ──
        if i == 0 and stripped == '---':
            in_frontmatter = True
            out_lines.append(line)
            continue

        if in_frontmatter and stripped == '---':
            in_frontmatter = False
            out_lines.append(line)
            continue

        if in_frontmatter:
            if stripped.startswith("title:"):
                m = re.match(r'title:\s*["\']?(.*?)["\']?\s*$', stripped)
                if m:
                    title_val = m.group(1)
                    translated = apply_sentence_map(title_val)
                    out_lines.append(stripped.replace(title_val, translated) + '\n')
                    continue
            out_lines.append(line)
            continue

        # ── Section headers 【...】 ──
        if '【' in stripped:
            for cn, en in SECTION_MAP.items():
                if cn in stripped:
                    stripped = stripped.replace(cn, en)
                    break

        # ── HTML lines (tables, <p> tags, etc.) ──
        if '<' in stripped and '>' in stripped:
            stripped = translate_html_text(stripped)
            out_lines.append(stripped + '\n')
            continue

        # ── Headings ──
        heading_match = re.match(r'^(#+)\s+(.+)$', stripped)
        if heading_match:
            heading_text = heading_match.group(2)
            # Check for heading with anchor
            anchor_match = re.match(r'^(.+?)(<a\s+name=.*)$', heading_text)
            if anchor_match:
                translated = apply_sentence_map(anchor_match.group(1))
                out_lines.append(heading_match.group(1) + ' ' + translated + anchor_match.group(2) + '\n')
            else:
                translated = apply_sentence_map(heading_text)
                out_lines.append(heading_match.group(1) + ' ' + translated + '\n')
            continue

        # ── Plain text ──
        translated = translate_plain_line(stripped)
        out_lines.append(translated + '\n')

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

    print(f"  Done. {len(out_lines)} lines written.")


# ═══════════════════════════════════════════════════════════════
#  5. Entry point
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    files_to_translate = sys.argv[1:] if len(sys.argv) > 1 else []
    if not files_to_translate:
        docs = '/Users/arthurbetter/hi3403-build/hi3403-docs/docs'
        mpp = os.path.join(docs, 'multimedia/mpp')
        isp = os.path.join(docs, 'multimedia/isp/dev-ref')
        files_to_translate = [
            os.path.join(mpp, '02-系统控制.md'),
            os.path.join(mpp, '03-视频输入.md'),
            os.path.join(mpp, '04-视频输出-41-43.md'),
            os.path.join(mpp, '04-视频输出-44-45.md'),
            os.path.join(mpp, '05-视频处理子系统.md'),
            # New files to translate
            os.path.join(mpp, '06-视频编码-61-63.md'),
            os.path.join(mpp, '06-视频编码-64-65.md'),
            os.path.join(mpp, '13-proc调试信息-131-1315.md'),
            os.path.join(mpp, '13-proc调试信息-1316-1329.md'),
            os.path.join(isp, 'isp-开发参考-1-2.md'),
        ]

    for src_path in files_to_translate:
        if not src_path.endswith('.md') or src_path.endswith('.en.md'):
            print(f"Skipping non-.md or .en.md file: {src_path}")
            continue

        dst_path = src_path[:-3] + '.en.md'
        if os.path.exists(dst_path):
            print(f"SKIP: {dst_path} already exists")
            continue

        translate_file(src_path, dst_path)
