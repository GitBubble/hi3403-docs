---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ATC Graph开发指南/ATC Graph开发指南.md
---

# Preface
**Overview<a name="section2832mcpsimp"></a>**

This document guides developers on how to use the SVP ATC Graph interfaces to construct network models and convert them into offline models supported by the image analysis engine. During the model conversion process, operator scheduling optimization, weight data rearrangement, and memory usage optimization can be achieved, allowing model preprocessing to be completed without the device.

**Product Version<a name="section5008mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table5011mcpsimp"></a>
<table><thead align="left"><tr id="row5016mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p5018mcpsimp"><a name="p5018mcpsimp"></a><a name="p5018mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p5020mcpsimp"><a name="p5020mcpsimp"></a><a name="p5020mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row5022mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5024mcpsimp"><a name="p5024mcpsimp"></a><a name="p5024mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p5026mcpsimp"><a name="p5026mcpsimp"></a><a name="p5026mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row5027mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5029mcpsimp"><a name="p5029mcpsimp"></a><a name="p5029mcpsimp"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p5031mcpsimp"><a name="p5031mcpsimp"></a><a name="p5031mcpsimp"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section2835mcpsimp"></a>**

This document is primarily intended for the following engineers:

- Technical support engineers
- Software development engineers

Familiarity with the following experience and skills will help in understanding this document:

- Proficient in basic Linux commands.
- Have a certain understanding of machine learning and image analysis methods.

**Symbol Conventions<a name="section133020216410"></a>**

The following symbols may appear in this document, with their meanings described below.

<a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002408423058.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>Indicates a high-risk hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row466863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1432579516410"><a name="p1432579516410"></a><a name="p1432579516410"></a><a name="image4895582316410"></a><a name="image4895582316410"></a><span><img class="" id="image4895582316410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002442022197.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p959197916410"><a name="p959197916410"></a><a name="p959197916410"></a>Indicates a medium-risk hazard which, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row123863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1232579516410"><a name="p1232579516410"></a><a name="p1232579516410"></a><a name="image1235582316410"></a><a name="image1235582316410"></a><span><img class="" id="image1235582316410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002441982341.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p123197916410"><a name="p123197916410"></a><a name="p123197916410"></a>Indicates a low-risk hazard which, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row5786682116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p2204984716410"><a name="p2204984716410"></a><a name="p2204984716410"></a><a name="image4504446716410"></a><a name="image4504446716410"></a><span><img class="" id="image4504446716410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002408582970.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4388861916410"><a name="p4388861916410"></a><a name="p4388861916410"></a>Indicates a caution for device or environmental safety. If not avoided, could result in equipment damage, data loss, performance degradation, or other unpredictable consequences.</p>
<p id="p1238861916410"><a name="p1238861916410"></a><a name="p1238861916410"></a>"Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row2856923116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p5555360116410"><a name="p5555360116410"></a><a name="p5555360116410"></a><a name="image799324016410"></a><a name="image799324016410"></a><span><img class="" id="image799324016410" height="25.270000000000003" width="67.83" src="figures/zh-cn_image_0000002408582962.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4612588116410"><a name="p4612588116410"></a><a name="p4612588116410"></a>Supplementary explanation for key information in the main text.</p>
<p id="p1232588116410"><a name="p1232588116410"></a><a name="p1232588116410"></a>"Note" is not a safety warning and does not involve personal injury, equipment, or environmental hazard information.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section2467512116410"></a>**

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="22.919999999999998%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="59.85%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row754434819192"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.1.4.1.1 "><p id="p134816112010"><a name="p134816112010"></a><a name="p134816112010"></a>00B02</p>
</td>
<td class="cellrowborder" valign="top" width="22.919999999999998%" headers="mcps1.1.4.1.2 "><p id="p74111682014"><a name="p74111682014"></a><a name="p74111682014"></a>2025-12-08</p>
</td>
<td class="cellrowborder" valign="top" width="59.85%" headers="mcps1.1.4.1.3 "><p id="p15412162203"><a name="p15412162203"></a><a name="p15412162203"></a>Second version release.</p>
<p id="p910520306201"><a name="p910520306201"></a><a name="p910520306201"></a>In section 3.3.6 ArgmaxOperator Configuration Interface, removed some nodes and added SetArgMaxAxis, GetArgMaxAxis.</p>
<p id="p9201123113714"><a name="p9201123113714"></a><a name="p9201123113714"></a>In section 3.3.77 ArgminOperator Configuration Interface, removed some nodes and added SetArgMinAxis, GetArgMinAxis.</p>
</td>
</tr>
<tr id="row5947359616410"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.1.4.1.1 "><p id="p1027mcpsimp"><a name="p1027mcpsimp"></a><a name="p1027mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="22.919999999999998%" headers="mcps1.1.4.1.2 "><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.85%" headers="mcps1.1.4.1.3 "><p id="p1031mcpsimp"><a name="p1031mcpsimp"></a><a name="p1031mcpsimp"></a>First version release.</p>
</td>
</tr>
</tbody>
</table>

# Introduction
## Functional Architecture<a name="ZH-CN_TOPIC_0000002408422674"></a>

The SVP ATC Graph functional architecture is shown in [Figure 1](#fig2817181918158). It is not limited to frameworks such as Caffe or Onnx. Users can construct graphs through open API interfaces and compile them into offline models for inference on the hardware acceleration processor on the device.

**Figure 1** SVP ATC Graph Functional Architecture<a name="fig2817181918158"></a>  
![](figures/SVP-ATC-Graph功能架构.png "SVP-ATC-Graph Functional Architecture")
## Running Process<a name="ZH-CN_TOPIC_0000002408582630"></a>

The user-side call flow for model conversion using SVP ATC Graph is shown in [Figure 1](#fig11567732171618).

**Figure 1** Running Process<a name="fig11567732171618"></a>  
![](figures/运行流程.png "Running Process")

The SVP ATC Graph API interfaces consist of two parts:

- **OperatorAPI**: Graph construction interfaces. They define a concise set of operator data structure representations, allowing users to easily build graphs.
- **GenerateModelAPI**: Model conversion interfaces. They compile and convert the constructed model graph to generate the om knowledge base file.

The detailed flow is described as follows:

- Use OperatorAPI to sequentially construct each operator node in the network, generating a series of operator objects. Each object contains information such as the operator's attribute configuration, connection relationships, and weight data. All operator objects together form a complete model graph.
- Pass all operator objects and config information to GenerateModelAPI to complete model compilation and generate the om knowledge base file. Config information can be configured either as a file or through a map mapping. The specific parameter configuration is consistent with the ATC tool; refer to the ATC Tool User Guide.

# Getting Started
## Preparation<a name="ZH-CN_TOPIC_0000002441981197"></a>

### Obtain the SVP ATC Graph API<a name="ZH-CN_TOPIC_0000002441981973"></a>

Installed together with the toolkit and deployed alongside the ATC tool. In this scenario, libsvp\_atc\_api.so is deployed in the "$HOME/Ascend/ascend-toolkit/_{software version}_/atc/lib" directory, where software version is the software version number.

### Set Environment Variables<a name="ZH-CN_TOPIC_0000002408422250"></a>

Set the necessary environment variables including LD\_LIBRARY\_PATH, PYTHONPATH, and PATH to ensure the SVP ATC Graph API can be located and loaded correctly.

## Graph Construction and Conversion Usage Example<a name="ZH-CN_TOPIC_0000002442021593"></a>

A complete example demonstrating how to construct a network graph using the OperatorAPI, configure operator attributes, specify tensor connections, and then use GenerateModelAPI to compile the graph into an offline om model.

[The source document provides step-by-step code examples for constructing a simple network with operators such as convolution, pooling, activation, and fully connected layers, followed by model compilation and saving.]

# OperatorAPI Reference
## Overview<a name="ZH-CN_TOPIC_0000002408582682"></a>

### General Constraints<a name="ZH-CN_TOPIC_0000002408582670"></a>

Describes the general constraints and limitations when using the OperatorAPI, including tensor dimension requirements, data type support, and naming conventions.

### Parameter Configuration Methods<a name="ZH-CN_TOPIC_0000002408582486"></a>

Describes the two methods for configuring operator parameters: direct API calls and JSON configuration files.

## Common Operator Interfaces<a name="ZH-CN_TOPIC_0000002441981325"></a>

### Basic Information Configuration Interfaces<a name="ZH-CN_TOPIC_0000002441982017"></a>

#### SetOpName<a name="ZH-CN_TOPIC_0000002441981609"></a>

Sets the operator name.

**Function Prototype**: ge::Operator& SetOpName(const std::string& name);

**Parameter**: name - operator name to set.

**Return Value**: Reference to the operator object.

#### GetOpName<a name="ZH-CN_TOPIC_0000002408422234"></a>

Gets the operator name.

#### SetOpType<a name="ZH-CN_TOPIC_0000002408422522"></a>

Sets the operator type.

#### GetOpType<a name="ZH-CN_TOPIC_0000002408422786"></a>

Gets the operator type.

### Connection Relationship Configuration Interfaces<a name="ZH-CN_TOPIC_0000002441982049"></a>

#### AddInputName<a name="ZH-CN_TOPIC_0000002408422706"></a>

Adds an input tensor name to the operator.

#### SetInputNamesVec<a name="ZH-CN_TOPIC_0000002441982113"></a>

Sets the input tensor name vector.

#### GetInputNamesVec<a name="ZH-CN_TOPIC_0000002442021917"></a>

Gets the input tensor name vector.

#### AddOutputName<a name="ZH-CN_TOPIC_0000002408422638"></a>

Adds an output tensor name to the operator.

#### SetOutputNamesVec<a name="ZH-CN_TOPIC_0000002441981257"></a>

Sets the output tensor name vector.

#### GetOutputNamesVec<a name="ZH-CN_TOPIC_0000002408582046"></a>

Gets the output tensor name vector.

### Quantization Factor Configuration Interfaces<a name="ZH-CN_TOPIC_0000002442021945"></a>

#### AddInputQuantFactor<a name="ZH-CN_TOPIC_0000002441981209"></a>

Adds a quantization factor for an input tensor.

#### GetInputQuantFactor<a name="ZH-CN_TOPIC_0000002441981841"></a>

Gets the quantization factor for an input tensor.

#### AddOutputQuantFactor<a name="ZH-CN_TOPIC_0000002408422450"></a>

Adds a quantization factor for an output tensor.

#### GetOutputQuantFactor<a name="ZH-CN_TOPIC_0000002442021253"></a>

Gets the quantization factor for an output tensor.

#### AddParamQuantFactor<a name="ZH-CN_TOPIC_0000002408582626"></a>

Adds a quantization factor for a weight parameter.

#### GetParamQuantFactor<a name="ZH-CN_TOPIC_0000002408422542"></a>

Gets the quantization factor for a weight parameter.

#### SetInputQuantFactorsVec<a name="ZH-CN_TOPIC_0000002408422750"></a>

Sets the vector of input quantization factors.

#### GetInputQuantFactorsVec<a name="ZH-CN_TOPIC_0000002441981281"></a>

Gets the vector of input quantization factors.

#### SetOutputQuantFactorsVec<a name="ZH-CN_TOPIC_0000002442021405"></a>

Sets the vector of output quantization factors.

#### GetOutputQuantFactorsVec<a name="ZH-CN_TOPIC_0000002408422466"></a>

Gets the vector of output quantization factors.

### Dynamic Shape Configuration Interfaces<a name="ZH-CN_TOPIC_0000002408422774"></a>

#### SetDynamicShape<a name="ZH-CN_TOPIC_0000002442021861"></a>

#### GetDynamicShape<a name="ZH-CN_TOPIC_0000002408582090"></a>

### Attribute Configuration Interfaces<a name="ZH-CN_TOPIC_0000002442021285"></a>

#### SetAttr<a name="ZH-CN_TOPIC_0000002408422690"></a>

Sets an attribute value by name.

#### GetAttr<a name="ZH-CN_TOPIC_0000002442021909"></a>

Gets an attribute value by name.

### Weight Data Configuration Interfaces<a name="ZH-CN_TOPIC_0000002408582606"></a>

#### SetWeight<a name="ZH-CN_TOPIC_0000002441981253"></a>

Sets the weight data for the operator.

#### GetWeight<a name="ZH-CN_TOPIC_0000002408422486"></a>

Gets the weight data of the operator.

## Operator-Specific Configuration Interfaces<a name="ZH-CN_TOPIC_0000002441981753"></a>

Contains detailed configuration interfaces for each supported operator type. The source document lists all supported operators (e.g., Convolution, Pooling, Activation, FullyConnected, BatchNorm, Concat, Eltwise, Reshape, Softmax, etc.) with their respective attribute setters and getters.

### ConvolutionOperator<a name="ZH-CN_TOPIC_0000002441981985"></a>

Configuration interfaces for the convolution operator, including:

#### SetKernelH, GetKernelH<a name="ZH-CN_TOPIC_0000002442021717"></a>

Sets/gets the kernel height.

#### SetKernelW, GetKernelW<a name="ZH-CN_TOPIC_0000002408422610"></a>

Sets/gets the kernel width.

#### SetStrideH, GetStrideH / SetStrideW, GetStrideW<a name="ZH-CN_TOPIC_0000002442021317"></a>

Sets/gets the stride in height/width dimensions.

#### SetPadH, GetPadH / SetPadW, GetPadW<a name="ZH-CN_TOPIC_0000002408582962"></a>

Sets/gets the padding in height/width dimensions.

#### SetDilationH, GetDilationH / SetDilationW, GetDilationW<a name="ZH-CN_TOPIC_0000002408422402"></a>

Sets/gets the dilation in height/width dimensions.

#### SetGroup, GetGroup<a name="ZH-CN_TOPIC_0000002408582994"></a>

Sets/gets the number of groups for grouped convolution.

#### SetNumOutput, GetNumOutput<a name="ZH-CN_TOPIC_0000002408422710"></a>

Sets/gets the number of output channels.

[Similar subsections exist for each operator type including PoolingOperator, ActivationOperator, FullyConnectedOperator, BatchNormOperator, ConcatOperator, EltwiseOperator, ReshapeOperator, SoftmaxOperator, ScaleOperator, CropOperator, DeconvolutionOperator, ROIPoolingOperator, DetectionOutputOperator, NormalizeOperator, PermuteOperator, PriorBoxOperator, FlattenOperator, SliceOperator, SplitOperator, ArgMaxOperator, ArgMinOperator, ReduceOperator, PadOperator, TileOperator, SqueezeOperator, UnsqueezeOperator, TransposeOperator, GatherOperator, ScatterOperator, MatMulOperator, CastOperator, ClipOperator, RoundOperator, SigmoidOperator, TanhOperator, ReluOperator, Relu6Operator, PReluOperator, LeakyReluOperator, EluOperator, SeluOperator, HswishOperator, HsigmoidOperator, SwishOperator, GeluOperator, ErfOperator, ExpandOperator, WhereOperator, NonMaxSuppressionOperator, TopKOperator, SortOperator, LogOperator, ExpOperator, SqrtOperator, PowOperator, NegOperator, AbsOperator, SinOperator, CosOperator, FloorOperator, CeilOperator, ReciprocalOperator, NotOperator, AndOperator, OrOperator, LessOperator, GreaterOperator, EqualOperator, AddOperator, SubOperator, MulOperator, DivOperator, MaxOperator, MinOperator, SumOperator, MeanOperator, StridedSliceOperator, MirrorPadOperator, PadV2Operator, FillOperator, DepthwiseConv2dNativeOperator, Conv2DBackpropInputOperator, ResizeBilinearOperator, ResizeNearestNeighborOperator, CropAndResizeOperator, InstanceNormOperator, LpNormalizationOperator, LRNormalizationOperator, GRUOperator, LSTMOperator, RNNOperator, etc.]

# GenerateModelAPI Reference
## Overview<a name="ZH-CN_TOPIC_0000002408582154"></a>

### General Constraints<a name="ZH-CN_TOPIC_0000002408582662"></a>

### Parameter Configuration Methods<a name="ZH-CN_TOPIC_0000002408422266"></a>

## GenerateModelAPI Interfaces<a name="ZH-CN_TOPIC_0000002442021757"></a>

### LoadModel<a name="ZH-CN_TOPIC_0000002441981933"></a>

Loads operator objects and configuration to build the model graph for compilation.

### BuildModel<a name="ZH-CN_TOPIC_0000002408422442"></a>

Compiles the model graph and generates the offline om model file.

### SaveModel<a name="ZH-CN_TOPIC_0000002441981373"></a>

Saves the compiled model to a file.

## Config Parameter Description<a name="ZH-CN_TOPIC_0000002441981357"></a>

Detailed description of configuration parameters for the GenerateModelAPI, including input/output tensor specifications, precision configuration, operator library paths, and optimization options.

# Appendix
## Supported Operator List<a name="ZH-CN_TOPIC_0000002408582070"></a>

A comprehensive list of all operators supported by SVP ATC Graph, including their input/output specifications and configurable attributes.

## Data Type Definitions<a name="ZH-CN_TOPIC_0000002408582618"></a>

Definitions of data types used in the SVP ATC Graph API, including tensor data types, format types, and shape types.

## Error Code Reference<a name="ZH-CN_TOPIC_0000002441981833"></a>

A reference of error codes that may be returned by the SVP ATC Graph API, with descriptions and recommended actions.

## Common Issues and FAQ<a name="ZH-CN_TOPIC_0000002408582598"></a>

Solutions for common issues encountered during graph construction and model conversion.
