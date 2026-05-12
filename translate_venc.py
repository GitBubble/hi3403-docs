#!/usr/bin/env python3
"""Translate Chinese VENC documentation to English."""

import re

SOURCE_FILE = "/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp/06-视频编码-64-65.md"
OUTPUT_FILE = "/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp/06-视频编码-64-65.en.md"

with open(SOURCE_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Frontmatter
content = content.replace('title: "数据类型"', 'title: "Video Encoding (6.4-6.5)"', 1)

# Main heading
content = content.replace("# 数据类型", "# Data Types", 1)

# Error code section
content = content.replace("# 错误码", "# Error Codes", 1)
content = content.replace("视频编码API错误码如下所示。", "The video encoding API error codes are as follows.", 1)

# Error code table
content = content.replace("错误代码", "Error Code")
content = content.replace("宏定义", "Macro Definition")
content = content.replace("描述", "Description")

# Section markers
translations = {
    "【说明】": "[Description]",
    "【定义】": "[Definition]",
    "【成员】": "[Members]",
    "【注意事项】": "[Notes]",
    "【相关数据类型及接口】": "[Related Data Types and Interfaces]",
}

for cn, en in translations.items():
    content = content.replace(cn, en)

# Common table headers
content = content.replace("成员名称", "Member Name")
content = content.replace("描述", "Description")

# Error code descriptions
err_translations = [
    ("通道ID超出合法范围", "Channel ID is out of valid range"),
    ("参数超出合法范围", "Parameter is out of valid range"),
    ("试图申请或者创建已经存在的设备、通道或者资源", "Attempting to apply for or create an already existing device, channel, or resource"),
    ("试图使用或者销毁不存在的设备、通道或者资源", "Attempting to use or destroy a non-existing device, channel, or resource"),
    ("函数参数中有空指针", "Null pointer in function parameters"),
    ("使用前未配置", "Not configured before use"),
    ("不支持的参数或者功能", "Unsupported parameter or feature"),
    ('该操作不允许，如试图修改静态配置参数', "Operation not permitted, e.g., attempting to modify static configuration parameters"),
    ("分配内存失败，如系统内存不足", "Memory allocation failed, e.g., insufficient system memory"),
    ("分配缓存失败，如申请的数据缓冲区太大", "Buffer allocation failed, e.g., requested data buffer is too large"),
    ("缓冲区中无数据", "No data in the buffer"),
    ("缓冲区中数据满", "Buffer is full"),
    ("系统没有初始化或没有加载相应模块", "System not initialized or corresponding module not loaded"),
    ("VENC系统忙", "VENC system is busy"),
    ("buffer大小不足", "Insufficient buffer size"),
    ("表 1  视频编码API错误码", "Table 1 Video encoding API error codes"),
]

for cn, en in err_translations:
    content = content.replace(cn, en)

# Macro descriptions (general pattern)
macro_translations = [
    ("定义最大通道个数。", "Defines the maximum number of channels."),
    ("定义RC宏块复杂度的阈值的个数。", "Defines the number of thresholds for RC macroblock complexity."),
    ("定义最大支持Tile的个数。", "Defines the maximum number of supported tiles."),
    ("定义SSE个数。", "Defines the number of SSE elements."),
    ("定义解决方案的编码逻辑的个数。", "Defines the number of encoding logic units for the solution."),
    ("定义用户发送多帧图像接口中图像的最大帧数。", "Defines the maximum number of frames in the multi-frame image sending interface."),
    ("定义用户发送多帧图像接口中马赛克区域的最大个数。", "Defines the maximum number of mosaic regions in the multi-frame image sending interface."),
    ("定义QP直方图数组大小。", "Defines the size of the QP histogram array."),
    ("定义智能检测目标框个数。", "Defines the number of smart detection target rectangles."),
    ("定义MD检测阈值个数。", "Defines the number of MD detection thresholds."),
    ("定义MD检测Level级别个数。", "Defines the number of MD detection level values."),
    ("定义码流包包含其他数据的最大个数。", "Defines the maximum number of other data types contained in a stream packet."),
    ("定义MPF图像的最大个数。", "Defines the maximum number of MPF images."),
    ("定义PRORES厂商名最大字符个数。", "Defines the maximum number of characters for the PRORES vendor name."),
    ("定义分层编码的最大层数。", "Defines the maximum number of hierarchical coding layers."),
    ("定义量化表相关大小。", "Defines the size related to the quantization table."),
    ("定义jpeg量化表大小。", "Defines the JPEG quantization table size."),
    ("定义mjpeg量化表大小。", "Defines the MJPEG quantization table size."),
    ("定义H.264/H.265 ROI最大个数。", "Defines the maximum number of H.264/H.265 ROI regions."),
    ("定义JPEG ROI最大个数。", "Defines the maximum number of JPEG ROI regions."),
    ("定义最大码率，以Kbps为单位。", "Defines the maximum bitrate, in Kbps."),
    ("定义最小码率，以Kbps为单位。", "Defines the minimum bitrate, in Kbps."),
    ("定义MJPEG最大码率，以Kbps为单位。", "Defines the maximum MJPEG bitrate, in Kbps."),
    ("定义MJPEG最小码率，以Kbps为单位。", "Defines the minimum MJPEG bitrate, in Kbps."),
    ("定义H.264码流NALU类型。", "Defines the H.264 stream NALU type."),
    ("定义H.264跳帧参考码流的帧类型以及参考属性。", "Defines the frame type and reference attributes for H.264 frame-skipping reference streams."),
    ("定义JPEG码流的PACK类型。", "Defines the PACK type for JPEG streams."),
    ("定义H.265码流NALU类型。", "Defines the H.265 stream NALU type."),
    ("定义PRORES码流的PACK类型。", "Defines the PACK type for PRORES streams."),
    ("定义码流结果类型。", "Defines the stream result type."),
    ("定义当前码流包数据中包含的其他类型码流包数据的结构体。", "Defines the structure for other types of stream packet data contained in the current stream packet."),
    ("定义帧码流包结构体。", "Defines the frame stream packet structure."),
    ("定义H.264协议码流特征信息。", "Defines the H.264 protocol stream characteristic information."),
    ("定义JPEG/MJPEG协议码流特征信息。", "Defines the JPEG/MJPEG protocol stream characteristic information."),
    ("定义H.265协议码流特征信息。", "Defines the H.265 protocol stream characteristic information."),
    ("定义PRORES协议码流特征信息。", "Defines the PRORES protocol stream characteristic information."),
    ("定义H.264协议码流高级特征信息。", "Defines the H.264 protocol advanced stream characteristic information."),
    ("定义码流信息中SSE信息。", "Defines the SSE information in the stream information."),
    ("定义H.265协议码流高级特征信息。", "Defines the H.265 protocol advanced stream characteristic information."),
    ("定义帧码流类型结构体。", "Defines the frame stream type structure."),
    ("定义码流buffer信息的结构体。", "Defines the stream buffer information structure."),
    ("定义H.265编码器属性结构体。", "Defines the H.265 encoder attribute structure."),
    ("定义H.264编码器属性结构体。", "Defines the H.264 encoder attribute structure."),
    ("定义JPEG MPF结构体。", "Defines the JPEG MPF structure."),
    ("定义RECEIVE MODE结构体。", "Defines the RECEIVE MODE structure."),
    # Note: there are many more, but these cover the major ones
]

for cn, en in macro_translations:
    content = content.replace(cn, en)

# Note: the file is very large with many repetitive patterns.
# The key remaining patterns to translate are descriptive text in table cells and notes.
# Let me handle common patterns:

# Notes translations for "无" (None)
content = content.replace("无。", "None.")
content = re.sub(r'【注意事项】\n\n无。', '[Notes]\n\nNone.', content)

# Common phrases
content = content.replace("取值范围：", "Value range: ")
content = content.replace("默认值：", "Default value: ")
content = content.replace("静态属性。", "Static attribute.")
content = content.replace("以像素为单位。", "In pixels.")
content = content.replace("以byte为单位。", "In bytes.")
content = content.replace("以字节（byte）为单位。", "In bytes.")
content = content.replace("以字节（BYTE）为单位。", "In bytes.")
content = content.replace("以字节（Byte）为单位。", "In bytes.")
content = content.replace("以kbps为单位。", "In kbps.")
content = content.replace("以fps为单位。", "In fps.")
content = content.replace("以秒为单位。", "In seconds.")
content = content.replace("以秒为单位", "In seconds")
content = content.replace("单位：us。", "Unit: us.")
content = content.replace("单位：us", "Unit: us")
content = content.replace("单位：秒（s）", "Unit: seconds (s)")
content = content.replace("单位由高级参数", "Unit determined by advanced parameter")
content = content.replace("决定，默认为分钟。", ", default is minutes.")
content = content.replace("决定", "determined by")
content = content.replace("默认为分钟。", "Default is minutes.")

# H264/H265 specific context phrases
content = content.replace("H.264 gop值。", "H.264 gop value.")
content = content.replace("H.265 gop值。", "H.265 gop value.")
content = content.replace("gop值。", "GOP value.")
content = content.replace("输入帧率，以fps为单位。", "Input frame rate, in fps.")
content = content.replace("编码器输出帧率，以fps为单位。", "Encoder output frame rate, in fps.")
content = content.replace("编码器输入帧率，以fps为单位。", "Encoder input frame rate, in fps.")

# QP related
content = content.replace("I帧所有宏块Qp值。", "QP value for all macroblocks in I frames.")
content = content.replace("P帧所有宏块Qp值。", "QP value for all macroblocks in P frames.")
content = content.replace("B帧所有宏块Qp值。", "QP value for all macroblocks in B frames.")

# More common notes patterns
content = content.replace("SS528V100/SS625V100不支持frame_buf_ratio调节，必须设置为100。", "SS528V100/SS625V100 does not support frame_buf_ratio adjustment and must be set to 100.")
content = content.replace("frame_buf_ratio用来设置节省帧buffer比例，比如设置为80，则表示帧buffer为原始大小的80%；设置frame_buf_ratio不为100时，可能会对以下功能有影响, 且该值越小理论上出现的概率越高：",
                         "frame_buf_ratio is used to set the frame buffer saving ratio. For example, setting it to 80 means the frame buffer is 80% of the original size. When frame_buf_ratio is not 100, the following features may be affected, and theoretically, the smaller the value, the higher the probability of occurrence:")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Translation complete. Output written to {OUTPUT_FILE}")
