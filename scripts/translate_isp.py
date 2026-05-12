#!/usr/bin/env python3
"""Translate ISP sections 1-2 from Chinese to English."""
import os, re

SRC = "/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/isp/dev-ref/isp-开发参考-1-2.md"
DST = "/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/isp/dev-ref/isp-开发参考-1-2.en.md"

with open(SRC, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Frontmatter
text = text.replace('title: "前言"', 'title: "Foreword"', 1)
text = text.replace("# 前言\n", "# Foreword\n", 1)

# 2. Chinese labels in brackets
LABELS = {
    "【说明】": "【Description】",
    "【描述】": "【Description】",
    "【语法】": "【Syntax】",
    "【参数】": "【Parameters】",
    "【返回值】": "【Return Value】",
    "【需求】": "【Requirements】",
    "【注意】": "【Notice】",
    "【举例】": "【Example】",
    "【相关主题】": "【Related Topics】",
    "【定义】": "【Definition】",
    "【成员】": "【Members】",
    "【注意事项】": "【Notice】",
    "【相关数据类型及接口】": "【Related Data Types and Interfaces】",
}
for cn, en in LABELS.items():
    text = text.replace(cn, en)

# 3. Table headers
TABLE_HEADERS = {
    "参数名称": "Parameter Name",
    "输入/输出": "Input/Output",
    "描述": "Description",
    "返回值": "Return Value",
    "成员名称": "Member Name",
    "产品名称": "Product Name",
    "产品版本": "Product Version",
    "符号": "Symbol",
    "文档版本": "Document Version",
    "发布日期": "Release Date",
    "修改说明": "Change Description",
}
for cn, en in TABLE_HEADERS.items():
    text = text.replace(cn, en)

# 4. Headings
HEADINGS = {
    "# 概述\n": "# Overview\n",
    "## 概述\n": "## Overview\n",
    "## 概述<a": "## Overview<a",
    "## 功能描述": "## Function Description",
    "### 架构": "### Architecture",
    "### 开发模式": "### Development Mode",
    "### 内部流程": "### Internal Flow",
    "### 软件流程": "### Software Flow",
    "### 文件组织": "### File Organization",
    "# 系统控制\n": "# System Control\n",
    "## 功能概述": "## Function Overview",
    "## API参考": "## API Reference",
    "# 数据类型\n": "# Data Types\n",
}
for cn, en in HEADINGS.items():
    text = text.replace(cn, en)

# 5. Bold labels in foreword
BOLD_LABELS = {
    "**概述**": "**Overview**",
    "**产品版本**": "**Product Version**",
    "**读者对象**": "**Audience**",
    "**符号约定**": "**Symbol Conventions**",
    "**修订记录**": "**Change History**",
    '**概述<a name="section102mcpsimp"></a>**': '**Overview<a name="section102mcpsimp"></a>**',
}
for cn, en in BOLD_LABELS.items():
    text = text.replace(cn, en)

# 6. Note icon
text = text.replace('>![](public_sys-resources/icon-note.gif) **说明：**', '>![](public_sys-resources/icon-note.gif) **Note:**')

# 7. Foreword paragraphs
FOREWORD = {
    '本文为使用ISP开发的程序员而写，目的是为您在开发过程中遇到的问题提供解决办法和帮助。': 'This document is written for engineers developing with ISP. It provides solutions and assistance for issues encountered during development.',
    '>**说明：** 本文以SS928V100描述为例，未有特殊说明，SS927V100与SS928V100内容一致。': '> **Note:** Unless otherwise stated, the SS927V100 and SS928V100 content is identical.',
    '与本文档相对应的产品版本如下。': 'The product versions corresponding to this document are as follows.',
    '本文档（本指南）主要适用于以下工程师：': 'This document (guide) is primarily intended for the following engineers:',
    '-   技术支持工程师': '-   Technical Support Engineers',
    '-   软件开发工程师': '-   Software Development Engineers',
    '在本文中可能出现下列标志，它们所代表的含义如下。': 'The following symbols may appear in this document. Their meanings are as follows.',
}
for cn, en in FOREWORD.items():
    text = text.replace(cn, en)

# 8. Symbol table
SYMBOLS = {
    '表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。': 'Indicates a hazard with a high level of risk which, if not avoided, will result in death or serious injury.',
    '表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。': 'Indicates a hazard with a medium level of risk which, if not avoided, could result in death or serious injury.',
    '表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。': 'Indicates a hazard with a low level of risk which, if not avoided, could result in minor or moderate injury.',
    '用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。': 'Indicates a potentially hazardous situation which, if not avoided, could result in equipment damage, data loss, performance deterioration, or unanticipated results.',
    '"须知"不涉及人身伤害。': '"NOTICE" is used to address practices not related to personal injury.',
    '对正文中重点信息的补充说明。': 'Calls attention to important information.',
    '"说明"不是安全警示信息，不涉及人身、设备及环境伤害信息。': '"NOTE" is used to convey information unrelated to personal injury, equipment damage, or environmental damage.',
}
for cn, en in SYMBOLS.items():
    text = text.replace(cn, en)

# 9. Change history
CHANGE = {
    '修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。': 'The revision record accumulates the description of each document update. The latest version of the document contains all updates from previous document versions.',
    '第1次临时版本发布。': 'First temporary version release.',
}
for cn, en in CHANGE.items():
    text = text.replace(cn, en)

# 10. Overview section
OVERVIEW = {
    'ISP通过一系列数字图像处理算法完成对数字图像的效果处理。主要包括3A、坏点校正、去噪、强光抑制、背光补偿、色彩增强、镜头阴影校正等处理。ISP包括逻辑部分以及运行在其上的firmware。这里主要介绍ISP的用户接口。': 'ISP completes digital image processing through a series of digital image processing algorithms. It mainly includes 3A, dead pixel correction, noise reduction, highlight suppression, backlight compensation, color enhancement, lens shading correction, and other processing. ISP consists of the logic part and the firmware running on it. This document mainly introduces the user interface of ISP.',
    'ISP的控制结构如[图1](#fig19534124782113)所示，lens将光信号投射到sensor的感光区域后，sensor经过光电转换，将Bayer格式的原始图像送给ISP，ISP经过算法处理，输出RGB空间域的图像给后端的视频采集单元。在这个过程中，ISP通过运行在其上的firmware对ISP逻辑，lens和sensor进行相应控制，进而完成自动光圈、自动曝光、自动白平衡等功能。其中，firmware的运转靠视频采集单元的中断驱动。PQ Tools工具通过网口或者串口完成对ISP的在线图像质量调节。': 'The ISP control structure is shown in [Figure 1](#fig19534124782113). After the lens projects the optical signal onto the photosensitive area of the sensor, the sensor undergoes photoelectric conversion and sends the Bayer format raw image to the ISP. The ISP processes it through algorithms and outputs an RGB space domain image to the backend video capture unit. During this process, the ISP controls the ISP logic, lens, and sensor through the firmware running on it, thereby completing functions such as auto iris, auto exposure, and auto white balance. The firmware is driven by interrupts from the video capture unit. The PQ Tools tool completes online image quality adjustment of ISP through the network port or serial port.',
    'ISP由ISP逻辑及运行在其上的Firmware组成，逻辑单元除了完成一部分算法处理外，还可以统计出当前图像的实时信息。Firmware通过获取ISP逻辑的图像统计信息，重新计算，反馈控制lens、sensor和ISP逻辑，以达到自动调节图像质量的目的。': 'ISP consists of ISP logic and the firmware running on it. In addition to completing part of the algorithm processing, the logic unit can also collect real-time statistics of the current image. The firmware obtains image statistics from the ISP logic, recalculates, and provides feedback control to the lens, sensor, and ISP logic to achieve automatic image quality adjustment.',
    'ISP逻辑主要流程、具体概念和功能点请参见芯片手册。': 'For the main flow, specific concepts, and function points of ISP logic, please refer to the chip manual.',
    'ISP的Firmware包含三部分，一部分是ISP控制单元和基础算法库，一部分是AE/AWB算法库，一部分是sensor库。Firmware设计的基本思想是单独提供3A算法库，由ISP控制单元调度基础算法库和3A算法库，同时sensor库分别向ISP基础算法库和3A算法库注册函数回调，以实现差异化的sensor适配。ISP firmware架构如[图1](#fig1959110622411)所示。': 'The ISP firmware consists of three parts: the ISP control unit and basic algorithm library, the AE/AWB algorithm library, and the sensor library. The basic design idea of the firmware is to provide the 3A algorithm library separately, with the ISP control unit scheduling the basic algorithm library and the 3A algorithm library. At the same time, the sensor library registers function callbacks to the ISP basic algorithm library and the 3A algorithm library respectively to achieve differentiated sensor adaptation. The ISP firmware architecture is shown in [Figure 1](#fig1959110622411).',
    '不同的sensor都以回调函数的形式，向ISP算法库注册控制函数。ISP控制单元调度基础算法库和3A算法库时，将通过这些回调函数获取初始化参数，并控制sensor，如调节曝光时间、模拟增益、数字增益，控制lens步进聚焦或旋转光圈等。': 'Different sensors register control functions with the ISP algorithm library in the form of callback functions. When the ISP control unit schedules the basic algorithm library and the 3A algorithm library, it will obtain initialization parameters through these callback functions and control the sensor, such as adjusting exposure time, analog gain, digital gain, controlling lens step focus or iris rotation, etc.',
}
for cn, en in OVERVIEW.items():
    text = text.replace(cn, en)

# 11. Development mode
DEV_MODE = {
    'SDK支持用户使用多种开发模式：': 'The SDK supports multiple development modes:',
    '1.  用户使用SDK的3A算法库。这时用户需要根据ISP基础算法库和3A算法库给出的sensor适配接口去适配不同的sensor。每款sensor对应一个文件夹，文件夹中包含两个主要文件：': '1.  The user uses the SDK\'s 3A algorithm library. In this case, the user needs to adapt different sensors according to the sensor adaptation interfaces provided by the ISP basic algorithm library and the 3A algorithm library. Each sensor corresponds to a folder containing two main files:',
    '该文件中主要实现ISP需要的回调函数，这些回调函数中包含了sensor的适配算法，不同的sensor可能有所不同。': 'This file mainly implements the callback functions required by ISP. These callback functions contain the sensor adaptation algorithm, which may vary for different sensors.',
    'sensor的底层控制驱动，主要实现sensor的读写和初始化动作。用户可以根据sensor的datasheet进行这两个文件的开发，必要的时候可以向sensor厂家寻求支持。': 'The underlying control driver for the sensor, mainly implementing sensor read/write and initialization operations. Users can develop these two files based on the sensor datasheet and may seek support from the sensor manufacturer when necessary.',
    '2.  用户根据ISP库提供的3A算法注册接口，实现自己的3A算法库开发。这时用户需要根据ISP基础算法库和用户的3A算法库给出的sensor适配接口去适配不同的sensor。': '2.  The user implements their own 3A algorithm library development based on the 3A algorithm registration interface provided by the ISP library. In this case, the user needs to adapt different sensors according to the sensor adaptation interfaces provided by the ISP basic algorithm library and the user\'s 3A algorithm library.',
    '3.  用户部分使用SDK中3A算法库，部分实现自己的3A算法库。例如AE使用libot\\_ae.a，AWB使用自己的3A算法库。SDK提供了灵活多变的支持方式。': '3.  The user partially uses the 3A algorithm library from the SDK and partially implements their own 3A algorithm library. For example, AE uses libot\\_ae.a, and AWB uses its own 3A algorithm library. The SDK provides flexible and diverse support methods.',
}
for cn, en in DEV_MODE.items():
    text = text.replace(cn, en)

# 12. Internal flow
text = text.replace(
    'Firmware内部流程分两部分，如[图1](#fig39021449132613)所示。一部分是初始化任务，主要完成ISP控制单元的初始化、ISP基础算法库的初始化、3A算法库的初始化，包括调用sensor的回调获取sensor差异化的初始化参数；另一部分是动态调节过程，在这个过程中，firmware中的ISP控制单元调度ISP基础算法库和3A算法库，实时计算并进行相应控制。Firmware的软件结构如[图2](#fig81434122714)所示。',
    'The firmware internal flow is divided into two parts, as shown in [Figure 1](#fig39021449132613). One part is the initialization task, which mainly completes the initialization of the ISP control unit, the ISP basic algorithm library, and the 3A algorithm library, including calling sensor callbacks to obtain differentiated sensor initialization parameters. The other part is the dynamic adjustment process, during which the ISP control unit in the firmware schedules the ISP basic algorithm library and the 3A algorithm library to perform real-time calculation and corresponding control. The firmware software structure is shown in [Figure 2](#fig81434122714).'
)

# 13. Software flow
text = text.replace(
    'ISP作为前端采集部分，需要和视频采集单元（VIU）协同工作。ISP初始化和基本配置完成后，需要VIU进行接口时序匹配。一是为了匹配不同sensor的输入时序，二是为ISP配置正确的输入时序。待时序配置完成后，ISP就可以启动Run来进行动态图像质量调节。此时输出的图像被VIU采集，进而送去显示或编码。软件使用流程如[图1](#fig796617213110)所示。',
    'As the front-end capture part, ISP needs to work together with the Video Capture Unit (VIU). After ISP initialization and basic configuration are completed, the VIU needs to perform interface timing matching. One is to match the input timing of different sensors, and the other is to configure the correct input timing for ISP. After the timing configuration is completed, the ISP can start Run to perform dynamic image quality adjustment. At this point, the output image is captured by the VIU and then sent for display or encoding. The software usage flow is shown in [Figure 1](#fig796617213110).'
)
text = text.replace(
    'PQ Tools工具主要完成在PC端进行动态图像质量调节，可以调节多个影响图像质量的因子，如去噪强度、色彩转换矩阵、饱和度等。',
    'The PQ Tools tool mainly performs dynamic image quality adjustment on the PC side and can adjust multiple factors affecting image quality, such as noise reduction strength, color conversion matrix, saturation, etc.'
)
text = text.replace(
    '如果用户调试好图像效果后，可以使用PQ Tools工具提供的配置文件保存功能进行配置参数保存。在下次启动时系统可以使用PQ Tools工具提供的配置文件加载功能加载已经调节好的图像参数。',
    'After the user has debugged the image effect, they can use the configuration file save function provided by the PQ Tools tool to save the configuration parameters. On the next startup, the system can use the configuration file load function provided by the PQ Tools tool to load the already adjusted image parameters.'
)
text = text.replace(
    'AE库有用到标准C库的数学库，请使用者在Makefile中增加 –lm 编译条件。',
    'The AE library uses the math library of the standard C library. Users should add the -lm compilation flag in the Makefile.'
)

# 14. File organization
text = text.replace(
    'ISP Firmware的文件组织结构如[图1](#fig142122515335)所示，ISP库和3A库、sensor库、dehaze库、ldci库、drc库分别独立。Firmware中的drv生成的驱动程序向用户态上报ISP中断，并以该中断驱动Firmware的ISP控制单元运转。ISP控制单元从驱动程序中获取统计信息，并调度基础算法单元和3A算法库，最后通过驱动程序配置寄存器。',
    'The file organization structure of ISP firmware is shown in [Figure 1](#fig142122515335). The ISP library, 3A library, sensor library, dehaze library, ldci library, and drc library are independent of each other. The driver program generated by drv in the firmware reports ISP interrupts to the user space and drives the operation of the ISP control unit of the firmware with these interrupts. The ISP control unit obtains statistical information from the driver program, schedules the basic algorithm unit and the 3A algorithm library, and finally configures registers through the driver program.'
)
text = text.replace(
    'Src文件夹中包含ISP控制单元和基础算法单元，编译后生成libss\\_isp.a、libot\\_isp.a，即ISP库。3a文件夹中包含AE/AWB算法库，用户也可以基于统一的接口界面开发自己的3a算法。Sensor文件夹中包含了各个sensor的驱动程序，该部分代码开源。dehaze文件夹对应去雾算法程序，ldci文件夹对应局域自动对比度增强算法程序，drc文件夹对应动态范围压缩算法程序，该部分代码不开源。',
    'The Src folder contains the ISP control unit and the basic algorithm unit, which compile to generate libss\\_isp.a and libot\\_isp.a, i.e., the ISP library. The 3a folder contains the AE/AWB algorithm library. Users can also develop their own 3a algorithms based on the unified interface. The Sensor folder contains the driver programs for each sensor, and this part of the code is open source. The dehaze folder corresponds to the dehaze algorithm program, the ldci folder corresponds to the local automatic contrast enhancement algorithm program, and the drc folder corresponds to the dynamic range compression algorithm program. This part of the code is not open source.'
)

# 15. System Control
text = text.replace(
    '系统控制部分包含了ISP公共属性配置，初始化ISP Firmware、运行ISP firmware、退出ISP firmware，设置ISP各模块等功能。',
    'The system control section includes ISP public attribute configuration, initializing ISP firmware, running ISP firmware, exiting ISP firmware, and setting ISP modules.'
)
text = text.replace(
    '本文档中接口，如无特殊说明，支持多进程。',
    'Unless otherwise specified, the interfaces in this document support multi-process.'
)

# 16. API descriptions
API_DESCS = {
    '初始化ISP外部寄存器。': 'Initialize the ISP external registers.',
    '初始化ISP firmware。': 'Initialize the ISP firmware.',
    '运行ISP firmware。': 'Run the ISP firmware.',
    '运行ISP firmware 一次。': 'Run the ISP firmware once.',
    '退出ISP firmware。': 'Exit the ISP firmware.',
    '设置ISP公共属性。': 'Set the ISP public attributes.',
    '获取ISP公共属性。': 'Get the ISP public attributes.',
    '设置ISP firmware状态。': 'Set the ISP firmware state.',
    '获取 ISP firmware状态。': 'Get the ISP firmware state.',
    '获取 ISP firmware状态。': 'Get the ISP firmware state.',
    '设置从模式sensor行场同步信号。': 'Set the slave mode sensor line/field sync signal.',
    '获取从模式sensor行场同步信号。': 'Get the slave mode sensor line/field sync signal.',
    '设定ISP功能模块的控制。': 'Set the ISP function module control.',
    '获取ISP功能模块的控制。': 'Get the ISP function module control.',
    '获取ISP中断信息。': 'Get the ISP interrupt information.',
    'ISP提供的sensor注册的回调接口。': 'Sensor registration callback interface provided by ISP.',
    'ISP提供的sensor反注册的回调接口。': 'Sensor unregistration callback interface provided by ISP.',
    'ISP提供的AE库注册的回调接口。': 'AE library registration callback interface provided by ISP.',
    'ISP提供的AE库反注册的回调接口。': 'AE library unregistration callback interface provided by ISP.',
    'ISP提供的AWB库注册的回调接口。': 'AWB library registration callback interface provided by ISP.',
    'ISP提供的AWB库反注册的回调接口。': 'AWB library unregistration callback interface provided by ISP.',
    '设置ISP库与3A库、sensor的绑定关系。': 'Set the binding relationship between the ISP library, 3A library, and sensor.',
    '获取ISP库与3A库、sensor的绑定关系。': 'Get the binding relationship between the ISP library, 3A library, and sensor.',
    '设置DCF参数。': 'Set the DCF parameters.',
    '获取DCF参数。': 'Get the DCF parameters.',
    '设置多路ISP Pipe差异属性。': 'Set the multi-channel ISP pipe differential attributes.',
    '获取多路ISP Pipe差异属性。': 'Get the multi-channel ISP pipe differential attributes.',
    '设置ISP控制参数。': 'Set the ISP control parameters.',
    '获取ISP控制参数。': 'Get the ISP control parameters.',
    '设置ISP模块参数。': 'Set the ISP module parameters.',
    '获取ISP模块参数。': 'Get the ISP module parameters.',
    '设置ISP模块智能信息。': 'Set the ISP module smart information.',
    '获取ISP模块智能信息。': 'Get the ISP module smart information.',
    '获取AWB在线标定得到的增益结构体。': 'Get the gain structure obtained from AWB online calibration.',
    '运行红外自动切换功能。': 'Run the infrared auto-switch function.',
    '设置be frame属性。': 'Set the BE frame attributes.',
    '获取be frame 属性。': 'Get the BE frame attributes.',
    '获取噪声模型标定参数。': 'Get the noise model calibration parameters.',
    '设置ISP实时信息。': 'Set the ISP real-time frame information.',
    '获取ISP实时信息。': 'Get the ISP real-time frame information.',
    '将ISP相关mmz buffer共享给特定的进程id。': 'Share the ISP-related MMZ buffer to a specific process ID.',
    '解除ISP相关mmz buffer对进程id的共享。': 'Unshare the ISP-related MMZ buffer from a process ID.',
    '共享ISP相关mmz buffer以不限进程id的方式共享给所有进程。': 'Share the ISP-related MMZ buffer to all processes without limiting by process ID.',
    '取消共享ISP相关mmz buffer对所有进程的共享。': 'Cancel the sharing of the ISP-related MMZ buffer to all processes.',
}
for cn, en in API_DESCS.items():
    text = text.replace(cn, en)

# 17. Figure captions
FIGURES = {
    '**图 1**  ISP控制结构示意图': '**Figure 1** ISP Control Structure Diagram',
    '**图 1**  ISP firmware 架构': '**Figure 1** ISP Firmware Architecture',
    '**图 1**  ISP firmware 内部流程': '**Figure 1** ISP Firmware Internal Flow',
    '**图 2**  ISP firmware 软件结构': '**Figure 2** ISP Firmware Software Structure',
    '**图 1**  ISP firmware使用流程': '**Figure 1** ISP Firmware Usage Flow',
    '**图 1**  ISP firmware 文件组织': '**Figure 1** ISP Firmware File Organization',
    '**图 1**  ISP库与sensor库间的接口': '**Figure 1** Interface Between ISP Library and Sensor Library',
    '**图 1**  ISP库与AE库间的接口': '**Figure 1** Interface Between ISP Library and AE Library',
    '**图 1**  ISP库与AWB库间的接口': '**Figure 1** Interface Between ISP Library and AWB Library',
    '**图 1**  同步信号配置时序图': '**Figure 1** Sync Signal Configuration Timing Diagram',
    '**图 2**  同步信号极性翻转': '**Figure 2** Sync Signal Polarity Inversion',
    '**图 3**  同步信号使能': '**Figure 3** Sync Signal Enable',
}
for cn, en in FIGURES.items():
    text = text.replace(cn, en)

# 18. Common value strings
text = text.replace('\n无\n', '\nNone\n')
text = text.replace('成功。', 'Success.')
text = text.replace('失败，其值为错误码。', 'Failure, the value is the error code.')
text = text.replace('失败，其值为<span xml:lang="sv-SE" id="ph5133152619495"><a name="ph5133152619495"></a><a name="ph5133152619495"></a>错误码</span>。',
    'Failure, the value is the <span xml:lang="sv-SE" id="ph5133152619495"><a name="ph5133152619495"></a><a name="ph5133152619495"></a>error code</span>.')
text = text.replace('输入', 'Input')
text = text.replace('输出', 'Output')
text = text.replace('非0', 'Non-0')

# 19. Requirements
text = text.replace('-   头文件：ot\\_common\\_isp.h、ss\\_mpi\\_isp.h', '-   Header file: ot\\_common\\_isp.h, ss\\_mpi\\_isp.h')
text = text.replace('-   库文件：libss\\_isp.a、libot\\_isp.a', '-   Library file: libss\\_isp.a, libot\\_isp.a')

# 20. Data types intro
text = text.replace(
    '本文档中变量，如未明确指定取值范围，则默认是数据类型对应的取值范围。例如td_u8数据类型的变量取值范围为[0, 255]。本文档中变量，如未明确指定数据精度，则默认是1。',
    'For variables in this document, if the value range is not explicitly specified, the default is the value range corresponding to the data type. For example, the value range of a td_u8 data type variable is [0, 255]. For variables in this document, if the data precision is not explicitly specified, the default is 1.'
)

# 21. Data type descriptions
DATA_DESCS = {
    '定义bayer数据的通道数目。': 'Defines the number of Bayer data channels.',
    '定义ISP 支持的PIPE数目的最大值。': 'Defines the maximum number of PIPE instances supported by ISP.',
    '定义WDR合成的最大帧数。': 'Defines the maximum number of frames for WDR composition.',
    '定义WDR曝光比的数目。': 'Defines the number of WDR exposure ratios.',
    '定义ISO档位数。': 'Defines the number of ISO steps.',
    '定义ISP BE离线分块数目的最大值。': 'Defines the maximum number of ISP BE offline stripes.',
    '定义ISP拼接组的最大个数。': 'Defines the maximum number of ISP stitching groups.',
    '定义3A算法库名称的最大字符数。': 'Defines the maximum number of characters in the 3A algorithm library name.',
    '曝光结果写到sensor时需要配置的寄存器个数的最大值。': 'Defines the maximum number of registers to configure when writing exposure results to the sensor.',
    '定义人形、人脸检测类型的最大数目。': 'Defines the maximum number of human body and face detection types.',
    '定义隧道检测类型的最大数目。': 'Defines the maximum number of tunnel detection types.',
    'AE水平方向的分区间数目。': 'Number of AE horizontal zone partitions.',
    'AE垂直方向的分区间数目。': 'Number of AE vertical zone partitions.',
    'MG水平方向的分区间数目。': 'Number of MG horizontal zone partitions.',
    'MG垂直方向的分区间数目。': 'Number of MG vertical zone partitions.',
    'AE ROUTE节点的最大数目。': 'Maximum number of AE ROUTE nodes.',
    '扩展AE ROUTE节点的最大数目。': 'Maximum number of extended AE ROUTE nodes.',
    '定义标定噪声模型参数的iso档位个数的最大值。': 'Defines the maximum number of ISO steps for calibrating noise model parameters.',
    '定义标定噪声模型参数的最大个数。': 'Defines the maximum number of calibration noise model parameters.',
    'CCM矩阵参数个数。': 'Number of CCM matrix parameters.',
    '定义DCF描述信息的深度。': 'Defines the depth of DCF description information.',
    '定义记录sensor info的最大帧数。': 'Defines the maximum number of frames for recording sensor info.',
    'Mesh Shading在x方向上划分的分块所需点的数量。': 'Number of points required for mesh shading partitions in the x direction.',
    'Mesh Shading在y方向上划分的分块所需点的数量。': 'Number of points required for mesh shading partitions in the y direction.',
    'Mesh Shading LUT表增益点的数量。': 'Number of gain points in the Mesh Shading LUT table.',
    'ACS划分的光源数量。': 'Number of ACS light source divisions.',
    '表示ACS标定的R和B通道分量。': 'Indicates the R and B channel components of ACS calibration.',
    '表示拍照pro模式下最大支持的帧数。': 'Indicates the maximum number of frames supported in photo pro mode.',
    '定义裁剪窗口起始位置和图像宽高。': 'Defines the crop window start position and image width/height.',
    '定义坐标信息。': 'Defines coordinate information.',
    '定义输入Bayer图像数据格式。': 'Defines the input Bayer image data format.',
    'mipi裁剪参数。': 'MIPI crop attributes.',
    '定义输入Bayer图像数据位宽。': 'Defines the input Bayer image data bit width.',
    '定义sensor输出的宽高。': 'Defines the sensor output width and height.',
    '定义通道色域属性。': 'Defines the channel color gamut attribute.',
    '定义ISP公共属性。': 'Defines the ISP public attributes.',
    '定义模块运行状态。': 'Defines the module operation mode.',
    '定义ISPfirmware状态。': 'Defines the ISP firmware state.',
    '定义从模式sensor同步信号配置。': 'Defines the slave mode sensor sync signal configuration.',
    '定义ISP宽动态模式。': 'Defines the ISP WDR mode.',
    '定义宽动态模式。': 'Defines the WDR mode.',
    '定义ISP功能模块的控制。': 'Defines the ISP function module control.',
    '定义获取的帧数据在ISP BE中的位置。': 'Defines the position of the obtained frame data in the ISP BE.',
    '定义be frame的相关配置信息。': 'Defines the relevant configuration information for the BE frame.',
    '定义ISP场同步信号。': 'Defines the ISP field sync signal.',
    '定义ISP sensor属性。': 'Defines the ISP sensor attributes.',
    '定义sensor注册结构体。': 'Defines the sensor registration structure.',
    '定义sensor回调函数结构体。': 'Defines the sensor callback function structure.',
    '定义sensor输出的宽高和帧率属性。': 'Defines the sensor output width, height, and frame rate attributes.',
    '定义LSC 参数。': 'Defines the LSC parameters.',
    '定义Auto Color Shading亮度分量上的校正强度表，也就是Gr/Gb分量的校正强度，用标定工具生成。': 'Defines the correction intensity table on the Auto Color Shading luminance component, i.e., the correction intensity of the Gr/Gb component, generated by the calibration tool.',
    '定义Auto Color Shading颜色分量上的Lut表，用标定工具生成，算法会根据R/B分量上的Lut表，动态生成适合当前场景的Lut表。': 'Defines the LUT table for the Auto Color Shading color component, generated by the calibration tool. The algorithm dynamically generates a LUT table suitable for the current scene based on the R/B component LUT tables.',
    '定义Auto Color Shading的标定参数，用标定工具生成。': 'Defines the calibration parameters for Auto Color Shading, generated by the calibration tool.',
    '定义Auto Color Shading的CMOS参数。': 'Defines the CMOS parameters for Auto Color Shading.',
    '定义NOISE 校正参数。': 'Defines the noise calibration parameters.',
    '定义sensor最大分辨率结构体。': 'Defines the sensor maximum resolution structure.',
    '定义CLUT结构体。': 'Defines the CLUT structure.',
    '定义sensor模式寄存器。': 'Defines the sensor mode registers.',
    '定义DNG白平衡校正系数。': 'Defines the DNG white balance correction coefficients.',
    '定义WDR切换属性。': 'Defines the WDR switch attributes.',
    '定义ISP的各算法是否采用cmos中的默认配置的标志位。': 'Defines the flag indicating whether each ISP algorithm uses the default configuration in CMOS.',
}
for cn, en in DATA_DESCS.items():
    text = text.replace(cn, en)

# 22. vi_pipe number
text = text.replace('vi_pipe号。', 'vi_pipe number.')
text = text.replace('vi_pipe号。\n', 'vi_pipe number.\n')

# 23. Misc member descriptions
MISC = {
    '水平方向起始位置, 取值范围：[0, 8072]': 'Horizontal start position, range: [0, 8072]',
    '垂直方向起始位置，取值范围：[0, 8072]': 'Vertical start position, range: [0, 8072]',
    '图像宽度，4对齐。使用shading功能时4对齐，否则shading功能会不正常。取值范围：[120, 8192]': 'Image width, 4-aligned. Must be 4-aligned when using the shading function, otherwise the shading function will not work correctly. Range: [120, 8192]',
    '图像高度，4对齐。使用shading功能时4对齐，否则shading功能会不正常。取值范围：[120, 8192]': 'Image height, 4-aligned. Must be 4-aligned when using the shading function, otherwise the shading function will not work correctly. Range: [120, 8192]',
    '横坐标信息。': 'X-coordinate information.',
    '纵坐标信息。': 'Y-coordinate information.',
    'RGGB排列方式。': 'RGGB arrangement.',
    'GRBG排列方式。': 'GRBG arrangement.',
    'GBRG排列方式。': 'GBRG arrangement.',
    'BGGR排列方式。': 'BGGR arrangement.',
    '保留字段。': 'Reserved field.',
    '保留位。': 'Reserved bits.',
    '线性模式。': 'Linear mode.',
    'Sensor合成WDR模式。': 'Sensor-composed WDR mode.',
    'Qudra模式': 'Qudra mode',
    '2帧合成行WDR模式。': '2-frame line WDR mode.',
    '2帧合成帧WDR模式。': '2-frame frame WDR mode.',
    '3帧合成行WDR模式。': '3-frame line WDR mode.',
    '3帧合成帧WDR模式。': '3-frame frame WDR mode.',
    '4帧合成行WDR模式。': '4-frame line WDR mode.',
    '4帧合成帧WDR模式。': '4-frame frame WDR mode.',
    'Bayer数据位宽：8bit。': 'Bayer data bit width: 8-bit.',
    'Bayer数据位宽：10bit。': 'Bayer data bit width: 10-bit.',
    'Bayer数据位宽：12bit。': 'Bayer data bit width: 12-bit.',
    'Bayer数据位宽：14bit。': 'Bayer data bit width: 14-bit.',
    'Bayer数据位宽：16bit。': 'Bayer data bit width: 16-bit.',
    'Firmware正常运行状态。': 'Firmware normal running state.',
    'Firmware冻结状态。': 'Firmware frozen state.',
    '运行在自动模式下。': 'Runs in auto mode.',
    '运行在手动模式下。': 'Runs in manual mode.',
    '色域范围为BT.601。': 'Color gamut range is BT.601.',
    '色域范围为BT.709。': 'Color gamut range is BT.709.',
    '色域范围为BT.2020。': 'Color gamut range is BT.2020.',
    '用户自定义色域范围。': 'User-defined color gamut range.',
    'FE帧起始。': 'FE frame start.',
    'FE帧结束。': 'FE frame end.',
    'BE帧结束。': 'BE frame end.',
    '获取经过ISP BE所有模块处理后的数据': 'Get data processed by all ISP BE modules',
    '获取WDR合成后的raw数据': 'Get raw data after WDR composition',
    '智能信息，包括人脸、人形信息。': 'Smart information, including face and human body information.',
    'Sensor输出的宽度。': 'Sensor output width.',
    'Sensor输出的高度。': 'Sensor output height.',
    'Sensor输出的帧率。': 'Sensor output frame rate.',
}
for cn, en in MISC.items():
    text = text.replace(cn, en)

with open(DST, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Done. Output: {DST}")
print(f"Size: {os.path.getsize(DST)} bytes")
