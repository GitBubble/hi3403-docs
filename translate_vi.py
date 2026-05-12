#!/usr/bin/env python3
"""
Translate remaining Chinese text in 03-视频输入.en.md to English.
Preserves code blocks, function names, anchor links, image paths, HTML tags.
"""
import re
import os

filepath = "/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp/03-视频输入.en.md"
backup_path = filepath + ".bak"

# Read the file
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Save backup
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Original file size: {len(content)} chars")

# Comprehensive translation dictionary
# Organized by: key patterns -> English translation
translations = {
    # Section titles in markdown headings
    "视频输入": "Video Input",
    "## 概述": "## Overview",
    "### 功能框图": "### Functional Block Diagram",
    "### 视频输入设备": "### Video Input Device",
    "### 视频输入PIPE": "### Video Input PIPE",
    "### 视频物理通道": "### Video Physical Channel",
    "### 视频扩展通道": "### Video Extension Channel",
    "### BAS功能区分说明": "### BAS Function Distinction Description",
    "### 绑定关系": "### Binding Relationships",
    "### 从模式": "### Slave Mode",
    "### 掩码配置": "### Mask Configuration",
    "## 功能描述": "## Functional Description",
    "## 重要概念": "## Important Concepts",
    "## API参考": "## API Reference",
    "## 错误码": "## Error Codes",

    # Anchor-linked headings
    "重要概念<a": "Important Concepts<a",
    "功能描述<a": "Functional Description<a",
    "功能框图<a": "Functional Block Diagram<a",
    "视频输入设备<a": "Video Input Device<a",
    "视频输入PIPE<a": "Video Input PIPE<a",
    "视频物理通道<a": "Video Physical Channel<a",
    "视频扩展通道<a": "Video Extension Channel<a",
    "BAS功能区分说明<a": "BAS Function Distinction Description<a",
    "绑定关系<a": "Binding Relationships<a",
    "从模式<a": "Slave Mode<a",
    "掩码配置<a": "Mask Configuration<a",
    "API参考<a": "API Reference<a",
    "错误码<a": "Error Codes<a",

    # Common table headers and cell content
    "参数名称": "Parameter Name",
    "描述": "Description",
    "输入/输出": "Input/Output",
    "返回值": "Return Value",
    "错误码": "Error Code",
    "成功。": "Success.",
    "成功": "Success",
    "非0": "Non-0",
    "需要设置": "Must set",
    "需要先销毁": "Must first destroy",
    "解决方案": "Solution",
    "具体功能描述": "Specific Function Description",
    "功能所属子模块": "Function Submodule",
    "PIPE的工作模式": "PIPE Operating Mode",
    "VIDevice number.": "VI Device number.",
    "取值：0。": "Value: 0.",
    "取值：0": "Value: 0",

    # Parameter attribute descriptions
    "Static Attribute。": "Static Attribute.",
    "Dynamic Attribute。": "Dynamic Attribute.",
    "VI设备属性指针。": "VI device attribute pointer.",
    "VI设备属性": "VI device attribute",
    "VI BayerScale属性指针。": "VI BayerScale attribute pointer.",
    "VI BayerScale属性": "VI BayerScale attribute",
    "热成像探测器的配置属性。": "Thermal imaging detector configuration attribute.",
    "热成像探测器的配置属性": "Thermal imaging detector configuration attribute",
    "设备送帧的帧信息结构体。": "Device frame sending information structure.",
    "设备送帧的帧信息": "Device frame sending frame information",
    "超时参数milli_sec：": "Timeout parameter milli_sec:",
    "-1表示阻塞模式；": "-1 indicates blocking mode;",
    "0表示非阻塞模式；": "0 indicates non-blocking mode;",
    "大于0表示超时模式，超时时间的单位为毫秒（ms）。": "Greater than 0 indicates timeout mode, timeout unit is milliseconds (ms).",
    "See": "See",

    # Note section common text
    "支持1、1/2、1/3的缩放和相位调整。": "Supports scaling of 1, 1/2, 1/3 and phase adjustment.",
    "只支持1/2的缩放，用户可以通过设置dump属性来获取bas帧。": "Only supports 1/2 scaling. Users can obtain bas frames by setting the dump attribute.",
    "wdr模式下不支持bas功能。": "Bas function is not supported in WDR mode.",
    "该接口在": "This interface should be configured after ",
    "之前配置，在": " and before ",
    "之后配置。": ".",
    "启用前必须已经设置设备属性，否则返回失败。": "Device attributes must have been set before enabling, otherwise returns failure.",
    "可重复启用，不返回失败。": "Can be enabled repeatedly, does not return failure.",
    "需先销毁所有与该VI设备绑定的物理PIPE后，再禁用VI设备。": "All physical PIPEs bound to this VI device must be destroyed before disabling the VI device.",
    "可重复禁用，不返回失败。": "Can be disabled repeatedly, does not return failure.",
    "支持低功耗处理，禁用VI设备后将完全关闭该设备，需要重新设置属性，才能启用的VI设备。": "Low-power processing is supported. Disabling the VI device will completely shut it down. Device attributes must be re-configured before the VI device can be re-enabled.",
    "支持低功耗处理，禁用VI设备后将完全关闭该设备，需要重新设置属性，才能启用VI设备。": "Low-power processing is supported. Disabling the VI device will completely shut it down. Device attributes must be re-configured before the VI device can be re-enabled.",
    "调用前必须已经启用设备，否则返回失败。": "The device must have been enabled before calling, otherwise returns failure.",
    "调用前必须先调用了": "The ",
    "接口。": " interface must have been called first.",
    "设置": "Sets the ",
    "属性。": " attribute.",
    "获取": "Gets the ",
    "启用": "Enables ",
    "禁用": "Disables ",
    "功能。": " function.",
    "创建": "Creates a ",
    "销毁": "Destroys a ",
    "启用了": "Enables ",
    "禁用了": "Disables ",

    # Device attribute config note
    "参数dev_attr主要用来配置指定VI设备的视频接口模式，用于与外围camera、sensor或codec对接，支持的接口模式包括MIPI Rx（MIPI/LVDS/HISPI）、SLVS-EC。用户需要配置以下几类信息，具体属性意义参见": "The dev_attr parameter is mainly used to configure the video interface mode of the specified VI device for interfacing with external cameras, sensors, or codecs. Supported interface modes include MIPI Rx (MIPI/LVDS/HISPI), SLVS-EC. Users need to configure the following types of information. See ",
    "接口模式信息：接口模式为MIPI Rx（MIPI/LVDS/HISPI）等模式": "- Interface mode information: Interface modes such as MIPI Rx (MIPI/LVDS/HISPI)",
    "工作模式信息：1路、2路、4路复合模式": "- Operating mode information: 1-channel, 2-channel, 4-channel composite modes",
    "数据布局信息：复合模式下多路数据的排布": "- Data layout information: Multi-channel data arrangement in composite mode",
    "数据信息：逐行输入、YUV数据输入顺序": "- Data information: Progressive input, YUV data input order",
    "同步时序信息：垂直、水平同步信号的属性": "- Synchronization timing information: Vertical and horizontal sync signal attributes",

    # Error code descriptions
    "视频输入设备号无效": "Invalid video input device ID",
    "视频输入PIPE号无效": "Invalid video input PIPE ID",
    "视频输入通道号无效": "Invalid video input channel ID",
    "视频输入组号无效": "Invalid video input group ID",
    "视频输入参数设置无效": "Invalid video input parameter setting",
    "输入参数空指针错误": "Input parameter null pointer error",
    "视频设备或通道属性未配置": "Video device or channel attribute not configured",
    "操作不支持": "Operation not supported",
    "操作不允许": "Operation not permitted",
    "视频输入设备或通道未启用": "Video input device or channel not enabled",
    "视频输入设备或通道未禁用": "Video input device or channel not disabled",
    "分配内存失败": "Memory allocation failed",
    "视频输入缓存为空": "Video input buffer is empty",
    "视频输入缓存为满": "Video input buffer is full",
    "视频输入系统未初始化": "Video input system not initialized",
    "视频配置属性超时": "Video configuration attribute timeout",
    "视频输入系统忙": "Video input system busy",
    "视频通道未绑定": "Video channel not bound",
    "视频通道已绑定": "Video channel already bound",

    # WDR fusion
    "wdr合成组": "WDR fusion group",
    "设置wdr合成组的属性。": "Sets the WDR fusion group attribute.",
    "获取wdr合成组的属性。": "Gets the WDR fusion group attribute.",
    "组属性。": " group attribute.",

    # Pipe-related
    "设置VI PIPE的属性。": "Sets the VI PIPE attribute.",
    "获取VI PIPE的属性。": "Gets the VI PIPE attribute.",
    "创建一个VI PIPE。": "Creates a VI PIPE.",
    "销毁一个VI PIPE。": "Destroys a VI PIPE.",
    "创建一个VI PIPE": "Create a VI PIPE",
    "销毁一个VI PIPE": "Destroy a VI PIPE",
    "设置VI 物理PIPE输入端的裁剪功能属性。": "Sets the crop function attribute at the VI physical PIPE input.",
    "获取VI 物理PIPE输入端的裁剪功能属性。": "Gets the crop function attribute at the VI physical PIPE input.",
    "设置VI 物理PIPE输出端的裁剪功能属性。": "Sets the crop function attribute at the VI physical PIPE output.",
    "获取VI 物理PIPE输出端的裁剪功能属性。": "Gets the crop function attribute at the VI physical PIPE output.",
    "设置VI 物理PIPE dump图像帧属性。": "Sets the VI physical PIPE image frame dump attribute.",
    "获取VI 物理PIPE dump图像帧属性。": "Gets the VI physical PIPE image frame dump attribute.",
    "获取VI物理PIPE图像帧。": "Gets the VI physical PIPE image frame.",
    "释放VI 物理PIPE的图像帧。": "Releases the VI physical PIPE image frame.",
    "设置VI 物理PIPE FE输出 dump图像帧属性。": "Sets the VI physical PIPE FE output image frame dump attribute.",
    "获取VI 物理PIPE FE输出 dump图像帧属性。": "Gets the VI physical PIPE FE output image frame dump attribute.",
    "获取VI物理PIPE FE输出图像帧。": "Gets the VI physical PIPE FE output image frame.",
    "释放VI 物理PIPE FE输出的图像帧。": "Releases the VI physical PIPE FE output image frame.",
    "设置VI物理PIPE dump私有数据的属性。": "Sets the VI physical PIPE private data dump attribute.",
    "获取VI物理PIPE dump私有数据的属性。": "Gets the VI physical PIPE private data dump attribute.",
    "获取VI物理PIPE的私有数据。": "Gets the VI physical PIPE private data.",
    "释放VI物理PIPE的私有数据。": "Releases the VI physical PIPE private data.",
    "设置VI PIPE dump bas图像帧的属性。": "Sets the VI PIPE bas image frame dump attribute.",
    "获取VI PIPE dump bas图像帧的属性。": "Gets the VI PIPE bas image frame dump attribute.",
    "获取VI PIPE bas图像帧。": "Gets the VI PIPE bas image frame.",
    "释放VI PIPE bas图像帧。": "Releases the VI PIPE bas image frame.",
    "设置VI PIPE数据的来源。": "Sets the source of VI PIPE data.",
    "获取VI PIPE数据的来源。": "Gets the source of VI PIPE data.",
    "设置VI PIPE参数。": "Sets the VI PIPE parameter.",
    "获取VI PIPE参数。": "Gets the VI PIPE parameter.",
    "启用VI PIPE STAGGER模式输出拆分。": "Enables VI PIPE STAGGER mode output splitting.",
    "禁用VI PIPE STAGGER模式输出拆分。": "Disables VI PIPE STAGGER mode output splitting.",
    "设置VI PIPE bayernr buffer个数。": "Sets the number of VI PIPE bayernr buffers.",
    "获取VI PIPE bayernr buffer个数。": "Gets the number of VI PIPE bayernr buffers.",
    "通过VI PIPE发送YUV数据。": "Sends YUV data via the VI PIPE.",
    "通过VI PIPE发送RAW数据。": "Sends RAW data via the VI PIPE.",
    "查询VI PIPE状态。": "Queries the VI PIPE status.",
    "启动VI 物理PIPE中断。": "Enables VI physical PIPE interrupt.",
    "禁用VI 物理PIPE中断。": "Disables VI physical PIPE interrupt.",
    "设置VI 物理PIPE对接前端sensor或者AD的VC号。": "Sets the VC number for the VI physical PIPE interfacing with the front-end sensor or AD.",
    "获取VI 物理PIPE对接前端sensor或者AD的VC号。": "Gets the VC number for the VI physical PIPE interfacing with the front-end sensor or AD.",
    "设置VI PIPE低延时属性。": "Sets the VI PIPE low latency attribute.",
    "获取VI PIPE低延时属性。": "Gets the VI PIPE low latency attribute.",
    "设置VI PIPE上报中断属性。": "Sets the VI PIPE interrupt reporting attribute.",
    "获取VI PIPE上报中断属性。": "Gets the VI PIPE interrupt reporting attribute.",
    "设置VI PIPE对应的鱼眼镜头LMF参数配置。": "Sets the fisheye lens LMF parameter configuration for the VI PIPE.",
    "获取VI PIPE对应的鱼眼镜头LMF参数配置。": "Gets the fisheye lens LMF parameter configuration for the VI PIPE.",
    "获取VI物理 PIPE的RAW压缩参数。": "Gets the RAW compression parameter of the VI physical PIPE.",
    "设置用户图片，作为无视频信号时的插入图片。": "Sets the user image to be inserted when there is no video signal.",
    "启用VI PIPE插入用户图片。": "Enables inserting the user image into the VI PIPE.",
    "禁用VI PIPE插入用户图片。": "Disables inserting the user image into the VI PIPE.",
    "设置VI PIPE的VB来源。": "Sets the VB source of the VI PIPE.",
    "获取VI PIPE的VB来源。": "Gets the VB source of the VI PIPE.",
    "将VI的PIPE绑定到某个视频缓存VB池中。": "Binds the VI PIPE to a video buffer VB pool.",
    "将VI的PIPE从某个视频缓存VB池中解绑定。": "Unbinds the VI PIPE from a video buffer VB pool.",
    "获取VI PIPE文件描述符。": "Gets the VI PIPE file descriptor.",
    "获取VI物理PIPE": "Gets the VI physical PIPE",

    # Channel-related
    "设置VI通道属性。": "Sets the VI channel attribute.",
    "获取VI通道属性。": "Gets the VI channel attribute.",
    "设置VI扩展通道属性。": "Sets the VI extension channel attribute.",
    "获取VI扩展通道属性。": "Gets the VI extension channel attribute.",
    "启用VI通道。": "Enables the VI channel.",
    "禁用VI通道。": "Disables the VI channel.",
    "设置VI通道裁剪功能属性。": "Sets the VI channel crop function attribute.",
    "获取VI通道裁剪功能属性。": "Gets the VI channel crop function attribute.",
    "设置VI图像旋转属性。": "Sets the VI image rotation attribute.",
    "获取VI图像旋转属性。": "Gets the VI image rotation attribute.",
    "设置VI镜头畸变校正（LDC）属性。": "Sets the VI Lens Distortion Correction (LDC) attribute.",
    "获取VI镜头畸变校正（LDC）属性。": "Gets the VI Lens Distortion Correction (LDC) attribute.",
    "根据镜头畸变校正（LDC）的输出图像坐标点查找输入图像的坐标点。": "Queries the input image coordinate point based on the output image coordinate point of the Lens Distortion Correction (LDC).",
    "根据镜头畸变校正（LDC）的输入图像坐标点查找输出图像的坐标点。": "Queries the output image coordinate point based on the input image coordinate point of the Lens Distortion Correction (LDC).",
    "设置VI通道展宽属性。": "Sets the VI channel spread attribute.",
    "获取VI通道展宽属性。": "Gets the VI channel spread attribute.",
    "设置VI通道对应的鱼眼属性。": "Sets the fisheye attribute of the VI channel.",
    "获取VI通道对应的鱼眼属性。": "Gets the fisheye attribute of the VI channel.",
    "根据鱼眼校正输出图像坐标点查找源图像坐标点。": "Queries the source image coordinate point based on the fisheye correction output image coordinate point.",
    "获取指定图像区域的亮度总和。": "Gets the luma sum for a specified image region.",
    "设置VI通道的DIS配置信息。": "Sets the VI channel DIS configuration information.",
    "获取VI通道的DIS配置信息。": "Gets the VI channel DIS configuration information.",
    "设置VI通道的DIS属性。": "Sets the VI channel DIS attribute.",
    "获取VI通道的DIS属性。": "Gets the VI channel DIS attribute.",
    "设置VI通道的DIS可选参数。": "Sets the VI channel DIS optional parameters.",
    "获取VI通道的DIS的可选参数。": "Gets the VI channel DIS optional parameters.",
    "设置VI通道的DIS WDR属性。": "Sets the VI channel DIS WDR attribute.",
    "获取VI通道的DIS WDR属性。": "Gets the VI channel DIS WDR attribute.",
    "设置VI通道的视场角矫正属性。": "Sets the VI channel field of view correction attribute.",
    "获取VI通道的视场角矫正属性。": "Gets the VI channel field of view correction attribute.",
    "从VI通道获取采集的图像。": "Gets the captured image from the VI channel.",
    "释放一帧从VI通道获取的图像。": "Releases a frame obtained from the VI channel.",
    "设置VI通道低延时属性。": "Sets the VI channel low latency attribute.",
    "获取VI通道低延时属性。": "Gets the VI channel low latency attribute.",
    "设置VI通道输出YUV数据的行stride对齐。": "Sets the line stride alignment for YUV data output from the VI channel.",
    "获取VI通道输出YUV数据的行stride对齐。": "Gets the line stride alignment for YUV data output from the VI channel.",
    "设置VI通道使用VB的来源。": "Sets the VB source for the VI channel.",
    "获取VI通道使用VB的来源。": "Gets the VB source for the VI channel.",
    "将VI通道绑定到某个视频缓存VB池中。": "Binds the VI channel to a video buffer VB pool.",
    "将VI通道从某个视频缓存VB池中解绑定。": "Unbinds the VI channel from a video buffer VB pool.",
    "查询VI通道的状态。": "Queries the VI channel status.",
    "获取VI通道文件描述符。": "Gets the VI channel file descriptor.",
    "设置VI 的拼接组属性。": "Sets the VI stitch group attribute.",
    "获取VI 的拼接组属性。": "Gets the VI stitch group attribute.",
    "设置VI模块参数。": "Sets the VI module parameter.",
    "获取VI模块参数。": "Gets the VI module parameter.",
    "关闭VI文件描述符。": "Closes the VI file descriptor.",
    "设置vi chn 裁剪放大属性。": "Sets the VI channel crop and zoom attribute.",
    "获取vi chn 裁剪放大属性。": "Gets the VI channel crop and zoom attribute.",

    # Data type descriptions
    "定义VI设备属性。": "Defines the VI device attribute.",
    "定义VI扩展通道属性。": "Defines the VI extension channel attribute.",
    "定义VI BayerScale属性。": "Defines the VI BayerScale attribute.",
    "定义DIS配置信息。": "Defines the DIS configuration information.",
    "定义DIS属性。": "Defines the DIS attribute.",
    "定义DIS可选参数。": "Defines the DIS optional parameters.",
    "定义DIS WDR属性。": "Defines the DIS WDR attribute.",
    "定义视场角矫正属性。": "Defines the field of view correction attribute.",
    "定义VI 拼接组属性。": "Defines the VI stitch group attribute.",
    "定义VI 模块参数。": "Defines the VI module parameter.",
    "定义VI 管道参数。": "Defines the VI pipe parameter.",
    "定义VI模块参数。": "Defines the VI module parameter.",
    "成员名称": "Member Name",

    # Notes about specific APIs
    "该接口在": "This interface must be called before ",
    "之前配置，在": " after ",
    "使用本接口时，需先调用": "Before using this interface, you must first call ",
    "启用送帧。": " to enable frame sending.",
    "必须已经启用设备，才能配置该接口送帧，否则会返回错误。": "The device must have been enabled before configuring this interface to send frames, otherwise an error will be returned.",
    "必须和": "It must be used in pairs with ",
    "成对使用，否则会导致VB泄露。": ", otherwise VB leakage will occur.",
    "dev自产生时序进行wdr模式灌raw时，不能使用pipe帧率控制对wdr长短帧帧率进行控制，否则可能出现wdr长短帧不匹配造成的wdr丢帧。": "When using dev self-generated timing to inject raw in WDR mode, pipe frame rate control cannot be used to control the WDR long/short frame frame rate, otherwise WDR frame loss may occur due to long/short frame mismatch.",
    "使用本接口前，需先配置DEV属性，并启用设备，否则返回失败。": "Before using this interface, configure the DEV attributes and enable the device first, otherwise returns failure.",
    "使用自产生时序功能灌RAW时，需配置DEV的宽高与RAW文件的宽高保持一致。": "When using self-generated timing to inject RAW, the DEV width and height must be configured to match the RAW file width and height.",
    "启用自产生时序后，若不灌RAW，则无图像显示。": "After enabling self-generated timing, no image will be displayed if RAW is not injected.",
    "启用自产生时序后，从DEV灌RAW后VI输出帧率由配置自产生时序产生的有效帧率决定。": "After enabling self-generated timing, the VI output frame rate after injecting RAW from the DEV is determined by the effective frame rate generated by the configured self-generated timing.",
    "DEV配置X2速率时，启用自产生时序会导致时序异常。": "When the DEV is configured with X2 rate, enabling self-generated timing will cause timing anomalies.",
    "如果未设置VI设备属性，该接口将返回失败。": "If the VI device attribute has not been set, this interface will return failure.",

    # Overview / concept text
    "视频输入（VI）模块实现的功能：通过MIPI Rx(含MIPI接口、LVDS接口和HISPI接口)，BT.1120，BT.656，BT.601，DC等接口接收视频数据。VI将接收到的数据存入到指定的内存区域，在此过程中，VI可以对接收到的原始视频图像数据进行处理，实现视频数据的采集。": "The Video Input (VI) module implements the following functions: Receiving video data through MIPI Rx (including MIPI interface, LVDS interface, and HISPI interface), BT.1120, BT.656, BT.601, DC and other interfaces. The VI stores the received data into a specified memory area. During this process, the VI can process the received raw video image data to achieve video data capture.",

    # Important concept items
    "视频输入设备": "Video Input Device",
    "视频输入设备支持若干种时序输入，负责对时序进行解析。": "The video input device supports several types of timing input and is responsible for timing parsing.",
    "视频输入物理PIPE": "Video Input Physical PIPE",
    "视频输入PIPE绑定在设备后端，负责设备解析后的数据再处理。": "The video input PIPE is bound to the device backend and is responsible for reprocessing the data after device parsing.",
    "视频输入虚拟PIPE": "Video Input Virtual PIPE",
    "视频输入虚拟PIPE不绑定设备，负责其他模块或用户发送过来的数据再处理。": "The video input virtual PIPE is not bound to a device and is responsible for reprocessing data sent by other modules or users.",
    "视频物理通道": "Video Physical Channel",
    "物理通道负责将最终处理后的数据输出到DDR，在真正将数据输出到DDR之前，它可以实现裁剪等功能。": "The physical channel is responsible for outputting the final processed data to DDR. Before actually outputting data to DDR, it can perform cropping and other functions.",
    "See": "See",
    "系统控制": "System Control",
    "VI和VPSS": "VI and VPSS",
    "的工作模式描述。": " operating mode description.",
    "掩码": "Mask",
    "掩码用于指示VI设备的视频数据来源。": "The mask is used to indicate the video data source of the VI device.",
    "镜头畸变校正（LDC）": "Lens Distortion Correction (LDC)",
    "镜头畸变校正，一些低端镜头容易产生图像畸变，需要根据畸变程度对其图像进行校正。": "Lens Distortion Correction. Some low-end lenses are prone to image distortion and need to have their images corrected based on the degree of distortion.",
    "DIS模块通过比较当前图像与前两帧图像采用不同自由度的防抖算法计算出当前图像在各个轴方向上的抖动偏移向量，然后根据抖动偏移向量对当前图像进行校正，从而起到防抖的效果。": "The DIS module calculates the jitter offset vector of the current image in each axis direction by comparing the current image with the previous two frames using a stabilization algorithm with different degrees of freedom. It then corrects the current image based on the jitter offset vector to achieve stabilization.",
    "Bayer scaling，即Bayer域缩放。": "Bayer scaling, i.e., Bayer domain scaling.",
    "提前上报中断": "Early Interrupt Reporting",
    "提前上报中断指图像写出指定的行数到DDR后，VI上报中断，把图像发给后端模块处理，可以减少延时，但没有和低延时一样的硬件机制保证后端模块读图像不会出错。": "Early interrupt reporting means that after the image is written to DDR for a specified number of lines, the VI reports an interrupt and sends the image to the backend module for processing. This can reduce latency, but does not have the same hardware mechanism as low latency to ensure that the backend module reads the image without errors.",

    # Overview extended
    "VI从软件上划分了输入设备（DEV），输入PIPE(图示为物理PIPE，虚拟PIPE只包含ISP_BE)、物理通道（PHY_CHN）、扩展通道（EXT_CHN）四个层级。各芯片的设备、PIPE、通道个数差异如": "VI is divided into four layers in software: Input Device (DEV), Input PIPE (illustrated as physical PIPE; virtual PIPE only contains ISP_BE), Physical Channel (PHY_CHN), and Extension Channel (EXT_CHN). The differences in device, PIPE, and channel counts across chips are shown in ",
    "SS928V100视频输入通道功能如": "The SS928V100 video input channel functions are shown in ",
    "所有VI设备都是相互独立的，支持时序解析。": "All VI devices are independent of each other and support timing parsing.",
    "VI的PIPE包含了ISP的相关处理功能，主要是对图像数据进行流水线处理，输出YUV图像格式给通道。": "The VI PIPE includes ISP-related processing functions, mainly for pipeline processing of image data and outputting YUV image format to channels.",
    "PIPE的工作模式请参见": "For the PIPE operating mode, refer to ",
    "章节的": " section for ",
    "SS928V100 VI只有一个物理通道，支持8个扩展通道。": "SS928V100 VI has only one physical channel, supporting 8 extension channels.",
    "SS928V100物理通道支持的典型分辨率如3840x2160@60fps、3840x2160@30fps、1080p@240fps、1080p@120fps、1080p@60fps、1080p@30fps等。": "Typical resolutions supported by the SS928V100 physical channel include 3840x2160@60fps, 3840x2160@30fps, 1080p@240fps, 1080p@120fps, 1080p@60fps, 1080p@30fps, etc.",
    "扩展通道是物理通道的扩展，扩展通道具备缩放、裁剪功能，它通过绑定物理通道，将物理通道输出作为自己的输入，然后输出用户设置的目标图像。": "Extension channels are extensions of the physical channel. Extension channels support scaling and cropping functions. They bind to the physical channel, use the physical channel output as their input, and then output the target image set by the user.",
    "SS928V100有两个子模块支持BAS功能，如": "SS928V100 has two submodules that support BAS functions, as shown in ",
    "DEV和前端时序输入的接口有约束关系。例如SS928V100前端需要接入BT.1120，且选择了第0组BT.1120管脚，PIPE应该和DEV3绑定，才能正常接收数据。": "There are constraints between the DEV and the front-end timing input interface. For example, if the SS928V100 front end needs to connect to BT.1120 and the 0th BT.1120 pin group is selected, the PIPE should be bound to DEV3 to receive data correctly.",
    "SS928V100 DEV和时序输入接口的约束关系如": "The constraints between SS928V100 DEV and timing input interfaces are shown in ",
    "表示无效设备号，数字表示有效的设备ID。": "\"x\" indicates an invalid device number, numbers indicate valid device IDs.",
    "DEV和PIPE的绑定关系：每个PIPE都可以与任意Dev绑定，PIPE销毁后，PIPE可以和DEV解绑定。": "DEV and PIPE binding relationship: Each PIPE can be bound to any Dev. After a PIPE is destroyed, the PIPE can be unbound from the DEV.",
    "从模式SENSOR，需要使用VI的从模式模块。从模式与VI的物理PIPE对应关系是固定的。用户需要根据SENSOR管脚的连线和": "For slave mode SENSOR, the VI slave mode module must be used. The correspondence between slave mode and the VI physical PIPE is fixed. Users need to determine which slave mode module to use based on the SENSOR pin connections and ",
    "确定使用哪个从模式模块，然后选择对应的物理PIPE号创建物理PIPE，否则会没有数据，详细步骤如下：": " to choose the corresponding physical PIPE number to create the physical PIPE, otherwise there will be no data. The detailed steps are as follows:",
    "1. 根据硬件原理图确认SENSOR管脚连接到了SENSOR_HSx/ SENSOR_VSx。": "1. Verify from the hardware schematic that the SENSOR pins are connected to SENSOR_HSx / SENSOR_VSx.",
    "2. 根据": "2. According to ",
    "确定该SENSOR连接到从模式模块x。": ", determine that this SENSOR is connected to slave mode module x.",
    "3. 软件根据": "3. Based on ",
    "确定在采集这个SENSOR的数据时可以使用编号为x的PIPE。": ", the software determines that PIPE number x can be used when capturing data from this SENSOR.",
    "从模式和PIPE的对应关系默认是如": "The default correspondence between slave mode and PIPE is as shown in ",
    "所示，如果需要修改，可以通过修改ISP相关的代码完成。": ". If modification is needed, it can be done by modifying ISP-related code.",
    "掩码的高12bit对应着硬件线路的12个pin脚连接（D0到D15之间的任意连续12个pin脚即可，例如D4～D15），用户需要根据实际连接情况设置恰当的掩码配置，掩码的最高比特位对应的pin为D15，例如10bit输入的Sensor连接的pin为D6~D15，掩码配置为0xFFC00000；同理如果是14bit输入时，对应的掩码配置为0xFFFC0000。": "The high 12 bits of the mask correspond to 12 pin connections on the hardware (any consecutive 12 pins between D0 and D15, for example D4~D15). Users need to set the appropriate mask configuration based on the actual connections. The highest bit of the mask corresponds to pin D15. For example, for a 10-bit input Sensor connected to pins D6~D15, the mask configuration is 0xFFC00000; similarly, for 14-bit input, the corresponding mask configuration is 0xFFFC0000.",
    "VI接入Data线序为由低到高，例如单分量接入时，D0为数据低比特位，D15为数据高比特位。": "The VI data line order is from low to high. For example, in single-component input, D0 is the data low bit and D15 is the data high bit.",
    "路/2路5M或1080p图像输入场景（12bit输入）": "-channel/2-channel 5M or 1080p image input scenario (12-bit input)",
    "路/2路5M或1080p图像输入场景下，设置VI设备属性时，可根据": "-channel/2-channel 5M or 1080p image input scenario, when setting VI device attributes, refer to ",
    "配置掩码。": " for mask configuration.",
    "路、2路5M或1080p场景下的掩码配置（12bit）": "-channel, 2-channel 5M or 1080p scenario mask configuration (12-bit)",
    "设备号": "Device ID",
    "掩码0": "Mask 0",
    "掩码1": "Mask 1",
    "路/2路BT.1120高清输入场景（16bit输入）": "-channel/2-channel BT.1120 high-definition input scenario (16-bit input)",
    "路/2路BT.1120高清图像输入场景下，设置VI设备属性时，可根据": "-channel/2-channel BT.1120 high-definition image input scenario, when setting VI device attributes, refer to ",
    "路/2路BT.1120图像输入场景下的掩码配置（16bit）": "-channel/2-channel BT.1120 image input scenario mask configuration (16-bit)",
    "路/2路D1图像输入场景（8bit输入）": "-channel/2-channel D1 image input scenario (8-bit input)",
    "路 图像输入场景下，设置VI设备属性时，可根据": "-channel image input scenario, when setting VI device attributes, refer to ",
    "路D1图像输入场景下的掩码配置（8bit）": "-channel D1 image input scenario mask configuration (8-bit)",

    # Summary description of VI module
    "VI模块实现Dev配置和启用、Dev和Pipe绑定、Grp配置、Pipe创建和启用、Chn配置和启用等功能。": "The VI module implements functions such as Dev configuration and enabling, Dev and Pipe binding, Grp configuration, Pipe creation and enabling, and Chn configuration and enabling.",
    "该功能模块提供以下MPI：": "This functional module provides the following MPI:",

    # 一对一 binding
    "一对一绑定Dev和Pipe。": "Binds Dev and Pipe one-to-one.",
    "一对一解绑定Dev和Pipe。": "Unbinds Dev and Pipe one-to-one.",
    "获取与Dev绑定的Pipe。": "Gets the Pipe bound to the Dev.",
    "获取与Pipe绑定的Dev。": "Gets the Dev bound to the Pipe.",

    # Solution difference text
    "只有Dev1支持热成像。": "Only Dev1 supports thermal imaging.",
    "支持的Dev ID": "Supported Dev ID",
    "无。": "None.",
    "无": "None",

    # Image related text
    "图 1": "Figure 1",
    "图 2": "Figure 2",
    "表 1": "Table 1",
    "表 2": "Table 2",
    "表 3": "Table 3",

    # Various remaining phrases
    "该接口将返回失败。": "This interface will return failure.",
    "该接口": "This interface",
    "视频输入API错误码如下所示。": "The video input API error codes are shown below.",
    "视频输入API错误码": "Video Input API Error Codes",
    "错误代码": "Error Code",
    "宏定义": "Macro Definition",
    "参数名称": "Parameter Name",

    # Data type section
    "数据类型": "Data Types",
    "### ot_vi_dev_attr<a": "### ot_vi_dev_attr<a",
    "定义VI设备属性。": "Defines the VI device attribute.",
    "定义": "Defines ",
    "成员": "Members",
    "相关数据类型及接口": "Related Data Types and Interfaces",
    "说明": "Description",
    "注意事项": "Precautions",
    "Pipe号": "Pipe ID",
    "通道号": "Channel ID",
    "设备号": "Device ID",
    "解决方案差异": "Solution Differences",
    "### 解决方案": "### Solution",
    "Note：": "Note:",
    "内容": "Content",
    "类型": "Type",
    "系统控制": "System Control",

    # Low delay
    "低延时": "low latency",
    "低延时属性。": "low latency attribute.",
    "设置VI PIPE低延时属性。": "Sets the VI PIPE low latency attribute.",

    # Fish eye
    "鱼眼": "fisheye",
    "对应的鱼眼": " corresponding fisheye",

    # Image direction
    "图像": "image",
    "图像帧": "image frame",
    "图像帧。": " image frame.",

    # Pipe descriptions
    "物理PIPE": "physical PIPE",
    "虚拟PIPE": "virtual PIPE",

    # Crop
    "裁剪": "crop",
    "裁剪功能属性": "crop function attribute",
    "裁剪放大": "crop and zoom",

    # WDR
    "wdr": "WDR",
    "WDR": "WDR",  # already ok

    # Various members descriptions
    "使能LDC功能。": "Enables the LDC function.",
    "LDC的配置信息。": "LDC configuration information.",
    "LDC文件的描述符。": "LDC file descriptor.",
    "表示相机坐标系下图像传感器平面法向量在Z轴方向的分量。": "Indicates the Z-axis component of the image sensor plane normal vector in the camera coordinate system.",
    "表示LDC的参考视角。": "Indicates the reference angle of view for LDC.",
    "表示相机坐标系下图像传感器绕Z轴的旋转角度。": "Indicates the rotation angle of the image sensor around the Z-axis in the camera coordinate system.",
    "LDC校正后的图像，所需的目标尺寸。": "The target size required for the LDC-corrected image.",
    "视场角是否启用。": "Whether the field of view correction is enabled.",
    "视场角矫正PMF系数。": "Field of view correction PMF coefficient.",
    "使能DIS功能。": "Enables the DIS function.",
    "DIS算法的缓存行数。": "Number of cache lines for the DIS algorithm.",

    # DIS mode
    "GYRO模式": "GYRO mode",
    "HYBRID模式": "HYBRID mode",
    "GME模式": "GME mode",
    "DIS算法模式": "DIS algorithm mode",

    # Pipe mode
    "VI间接离线模式": "VI indirect offline mode",
    "VI直接离线模式": "VI direct offline mode",
    "VI在线模式": "VI online mode",
    "VI和VPSS的工作模式": "VI and VPSS operating modes",

    # Pipe source
    "VI PIPE DEIVCE模式": "VI PIPE DEVICE mode",
    "VI PIPE用户模式": "VI PIPE user mode",

    # Stagger
    "STAGGER模式": "STAGGER mode",
    "启用VI PIPE STAGGER模式输出拆分。": "Enables VI PIPE STAGGER mode output splitting.",

    # Bayer NR
    "bayernr": "bayernr",
    "buffer个数": "buffer count",

    # VC number
    "VC号": "VC number",

    # Frame interrupt
    "上报中断": "interrupt reporting",
    "帧中断": "frame interrupt",

    # LMF
    "鱼眼镜头LMF参数": "fisheye lens LMF parameters",

    # RAW compress
    "RAW压缩参数": "RAW compression parameter",

    # User pic
    "用户图片": "user picture",
    "插入图片": "insert picture",
    "无视频信号": "no video signal",

    # VB
    "VB来源": "VB source",
    "VB池": "VB pool",

    # FD
    "文件描述符": "file descriptor",

    # Extension channel
    "扩展通道": "extension channel",

    # Spread
    "展宽": "spread",
    "展宽属性": "spread attribute",

    # Rgn luma
    "亮度总和": "luma sum",
    "图像区域": "image region",

    # FOV correction
    "视场角矫正": "field of view correction",
    "视场角矫正属性": "field of view correction attribute",

    # Stitch
    "拼接组": "stitch group",
    "拼接组属性": "stitch group attribute",

    # Mod param
    "模块参数": "module parameter",

    # Close fd
    "关闭": "Closes ",

    # DIS member descriptions
    "DIS算法模式。": "DIS algorithm mode.",
    "GME：": "GME: ",
    "HYBRID：": "HYBRID: ",
    "GYRO：": "GYRO: ",
    "大幅度运动的防抖衰减参数。取值范围[0, 100]。默认值及具体参数效果参见": "Large motion stabilization attenuation parameter. Value range [0, 100]. For default values and specific parameter effects, refer to ",
    "低频运动的保留程度。取值范围[0, 100]。默认值及具体参数效果参见": "Low frequency motion preservation level. Value range [0, 100]. For default values and specific parameter effects, refer to ",
    "低频运动的截止频率。取值范围[0, 100]。默认值及具体参数效果参见": "Low frequency motion cutoff frequency. Value range [0, 100]. For default values and specific parameter effects, refer to ",
    "《DIS 调试指南》": "the DIS Debugging Guide",
    "自适应查找特征点对数阈值的开关。默认值及具体参数效果参见《DIS 调试指南》。": "Adaptive feature point pair threshold switch. For default values and specific parameter effects, refer to the DIS Debugging Guide.",
    "TD_FALSE：不启用自适应查找特征点阈值功能；": "TD_FALSE: Adaptive feature point threshold function is not enabled;",
    "TD_TRUE：启用自适应查找特征点阈值功能。": "TD_TRUE: Adaptive feature point threshold function is enabled.",

    # DIS Precautions
    "参数只在GME和HYBRID模式下有效，不配置使用默认参数。": "The parameters are only valid in GME and HYBRID modes. If not configured, default parameters are used.",
    "算法特征点对数的阈值默认是30对，fpd_adaptive_en启用后会自适应降低阈值，最低降低到10对，fpd_adaptive_en关闭、enable开关关闭或still_crop开关打开后，特征点阈值都会恢复成默认的30。": "The default threshold for algorithm feature point pairs is 30. When fpd_adaptive_en is enabled, the threshold is adaptively reduced to a minimum of 10. When fpd_adaptive_en is disabled, the enable switch is off, or the still_crop switch is turned on, the feature point threshold returns to the default value of 30.",

    # DIS WDR attr
    "WDR 匹配帧参数。": "WDR matching frame parameter.",
    "WDR模式为2TO1时取值范围[0, 1]，0为匹配短帧，1为匹配长帧；": "When WDR mode is 2TO1, the value range is [0, 1], where 0 matches the short frame and 1 matches the long frame;",
    "WDR模式为3TO1时取值范围[0, 2]，0为匹配短帧，1为匹配中帧，2为匹配长帧。": "When WDR mode is 3TO1, the value range is [0, 2], where 0 matches the short frame, 1 matches the medium frame, and 2 matches the long frame.",
    "参数只在GYRO模式下有效，不配置使用默认参数": "Parameters are only valid in GYRO mode. If not configured, default parameters are used.",

    # ATTR descriptions
    "视场角是否启用。": "Whether the field of view correction is enabled.",
    "视场角矫正PMF系数。": "Field of view correction PMF coefficient.",

    # VI module param
    "定义VI 模块参数。": "Defines the VI module parameter.",

    # WDR fusion grp attr
    "定义wdr合成组属性。": "Defines the WDR fusion group attribute.",
    "WDR合成组ID": "WDR fusion group ID",
    "wdr合成组的pipe数。": "Number of pipes in the WDR fusion group.",

    # Pipe attr descriptions
    "pipe模式": "Pipe mode",
    "pipe数据源": "Pipe data source",

    # Chn attr
    "定义VI通道属性。": "Defines the VI channel attribute.",
    "定义VI扩展通道属性。": "Defines the VI extension channel attribute.",

    # Stagger
    "STAGGER模式输出拆分": "STAGGER mode output splitting",
}

# Helper translations for common patterns
def translate_line(line):
    """Translate a line of text, preserving code, anchors, HTML."""
    # Skip code blocks, anchors, image paths entirely
    # We'll handle this at a higher level

    # Apply translations - sort by length desc to match longest first
    sorted_keys = sorted(translations.keys(), key=len, reverse=True)
    for cn_key in sorted_keys:
        if cn_key in line:
            line = line.replace(cn_key, translations[cn_key])
    return line


# Detect if content is inside a code block or is an anchor/image/html-only line
lines = content.split('\n')
in_code_block = False

for i, line in enumerate(lines):
    stripped = line.strip()

    # Track code blocks
    if stripped.startswith('```'):
        in_code_block = not in_code_block
        continue

    # Skip when inside code block
    if in_code_block:
        continue

    # Translate the line
    lines[i] = translate_line(line)

result = '\n'.join(lines)

# Write the result
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

# Count remaining Chinese characters
remaining = len(re.findall(r'[一-鿿㐀-䶿豈-﫿]', result))
print(f"Remaining Chinese characters: {remaining}")
print(f"Translation complete. Backup saved to: {backup_path}")
