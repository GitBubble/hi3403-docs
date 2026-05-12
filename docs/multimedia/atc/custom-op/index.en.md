---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ATC自定义算子开发指南/ATC自定义算子开发指南.md
---

# Preface
**Overview<a name="section996mcpsimp"></a>**

This document describes how to use the interfaces provided by ATC (Advanced Tensor Compiler) to develop custom operators in order to improve network runtime efficiency.

**Product Version<a name="section300mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table303mcpsimp"></a>
<table><thead align="left"><tr id="row308mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p310mcpsimp"><a name="p310mcpsimp"></a><a name="p310mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p312mcpsimp"><a name="p312mcpsimp"></a><a name="p312mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row314mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1376073312191"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p5760533111913"><a name="p5760533111913"></a><a name="p5760533111913"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p6760333131918"><a name="p6760333131918"></a><a name="p6760333131918"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section999mcpsimp"></a>**

This document is primarily intended for software development engineers.

Familiarity with the following experience and skills will help in understanding this document:

- Proficient in basic Linux commands.
- Have a certain understanding of machine learning and image analysis methods.

**Symbol Conventions<a name="section133020216410"></a>**

The following symbols may appear in this document, with their meanings described below.

<a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="/multimedia/atc/custom-op/figures/zh-cn_image_0000002441982933.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>Indicates a high-risk hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row466863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1432579516410"><a name="p1432579516410"></a><a name="p1432579516410"></a><a name="image4895582316410"></a><a name="image4895582316410"></a><span><img class="" id="image4895582316410" height="25.270000000000003" width="67.83" src="/multimedia/atc/custom-op/figures/zh-cn_image_0000002408583542.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p959197916410"><a name="p959197916410"></a><a name="p959197916410"></a>Indicates a medium-risk hazard which, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row123863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1232579516410"><a name="p1232579516410"></a><a name="p1232579516410"></a><a name="image1235582316410"></a><a name="image1235582316410"></a><span><img class="" id="image1235582316410" height="25.270000000000003" width="67.83" src="/multimedia/atc/custom-op/figures/zh-cn_image_0000002408423634.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p123197916410"><a name="p123197916410"></a><a name="p123197916410"></a>Indicates a low-risk hazard which, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row5786682116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p2204984716410"><a name="p2204984716410"></a><a name="p2204984716410"></a><a name="image4504446716410"></a><a name="image4504446716410"></a><span><img class="" id="image4504446716410" height="25.270000000000003" width="67.83" src="/multimedia/atc/custom-op/figures/zh-cn_image_0000002442022777.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4388861916410"><a name="p4388861916410"></a><a name="p4388861916410"></a>Indicates a caution for device or environmental safety. If not avoided, could result in equipment damage, data loss, performance degradation, or other unpredictable consequences.</p>
<p id="p1238861916410"><a name="p1238861916410"></a><a name="p1238861916410"></a>"Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row2856923116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p5555360116410"><a name="p5555360116410"></a><a name="p5555360116410"></a><a name="image799324016410"></a><a name="image799324016410"></a><span><img class="" id="image799324016410" height="25.270000000000003" width="67.83" src="/multimedia/atc/custom-op/figures/zh-cn_image_0000002442022785.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4612588116410"><a name="p4612588116410"></a><a name="p4612588116410"></a>Supplementary explanation for key information in the main text.</p>
<p id="p1232588116410"><a name="p1232588116410"></a><a name="p1232588116410"></a>"Note" is not a safety warning and does not involve personal injury, equipment, or environmental hazard information.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section2467512116410"></a>**

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.75%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.53%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p1027mcpsimp"><a name="p1027mcpsimp"></a><a name="p1027mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.1.4.1.2 "><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="54.53%" headers="mcps1.1.4.1.3 "><p id="p1031mcpsimp"><a name="p1031mcpsimp"></a><a name="p1031mcpsimp"></a>First temporary version release.</p>
</td>
</tr>
</tbody>
</table>

# Getting Started
## Introductory Learning<a name="ZH-CN_TOPIC_0000002408423562"></a>

### Basic Operator Concepts<a name="ZH-CN_TOPIC_0000002408423566"></a>

Image analysis algorithms consist of computational units called operators (Op). In a network model, operators correspond to the computation logic in layers. For example, a Convolution Layer is an operator, and the weight summation process in a Fully-connected Layer (FC layer) is an operator. The following are basic concepts commonly used in operators.

- **Operator Name**

    The name of the operator, used to identify a specific operator in the network. Operator names in the same network must be unique.

- **Operator Type**

    Each operator in the network is matched to its implementation based on the operator type. Operators of the same type have the same implementation logic. Multiple operators of the same type may exist in one network.

- **Data Layout (Format)**

    In image analysis frameworks, multidimensional data is stored in multidimensional arrays. For example, convolution feature maps in image analysis are stored as four-dimensional arrays: Batch size (N), feature map Height (H), feature map Width (W), and feature map Channels (C). Since data can only be stored linearly, these four dimensions have a corresponding order. Different image analysis frameworks store feature map data in different orders. For example, in Caffe, the order is [Batch, Channels, Height, Width] (NCHW). In TensorFlow, the order is [Batch, Height, Width, Channels] (NHWC).

- **Shape**

    The shape of a tensor, expressed as (D0, D1, ..., Dn-1), where D0 to Dn are arbitrary positive integers.

## Release Mode Usage<a name="ZH-CN_TOPIC_0000002442022577"></a>

### Obtain the ATC Tool<a name="ZH-CN_TOPIC_0000002441982845"></a>

Refer to the section "2.1.1 Obtain the ATC Tool" in the ATC Tool User Guide.

### Obtain the custom Sample Project<a name="ZH-CN_TOPIC_0000002442022697"></a>

The custom sample project includes two implementation samples: Abs (cpu) and Add (_nnn_). The sample project directory structure is as follows:

```
├── build.sh
├── caffe_model
│   ├── scale.caffemodel
│   ├── scale.prototxt
├── CMakeLists.txt
├── custom_common
│   └── operator_desc.sh
├── out
├── package.config
├── sample_abs
│   ├── caffe_proto
│   ├── custom
│   └── test
└── sample_add
    ├── caffe_proto
    ├── custom
    └── test
```

[The source document describes the directory structure and contents in detail, including the build scripts, model files, operator implementation code, and test files for both the Abs and Add samples.]

### Set Environment Variables<a name="ZH-CN_TOPIC_0000002442022709"></a>

Set the environment variables required for compiling custom operator projects, including paths to the ATC toolkit, compiler toolchain, and dependencies.

### Compile the custom Sample Project<a name="ZH-CN_TOPIC_0000002441982757"></a>

Run the build.sh script to compile the custom operator sample project, generating the operator implementation shared libraries.

### Run ATC<a name="ZH-CN_TOPIC_0000002408423442"></a>

Use the ATC tool to convert the model containing custom operators, specifying the custom operator library path via the --plugin\_path parameter.

## Debug Mode Usage<a name="ZH-CN_TOPIC_0000002442022605"></a>

### Obtain the test Sample Project<a name="ZH-CN_TOPIC_0000002442022657"></a>

The test sample project includes simulation test code for verifying custom operator functionality on the x86 server before deployment.

### Compile the test Sample Project<a name="ZH-CN_TOPIC_0000002408423590"></a>

Compile the test project using CMake to generate the simulation test executable.

### Run the test Sample Project<a name="ZH-CN_TOPIC_0000002408583386"></a>

Run the compiled test executable to verify the correctness of custom operator implementations.

# Operator Development Process
## Operator Op Definition<a name="ZH-CN_TOPIC_0000002408423542"></a>

### Principles<a name="ZH-CN_TOPIC_0000002441982749"></a>

Describes the fundamental concepts of operator definition, including the three core components:
- **OpNode**: Defines the operator's properties, inputs, outputs, and parameters
- **Parser**: Parses the operator parameters from the framework-specific model format
- **Propagation**: Performs shape inference and propagation through the network

### Operator Analysis<a name="ZH-CN_TOPIC_0000002441982797"></a>

Guidelines for analyzing an operator before development, including understanding the computation formula, determining input/output tensor shapes and data types, and identifying parameters.

### Project Creation<a name="ZH-CN_TOPIC_0000002441982813"></a>

Steps to create the custom operator project directory structure, including header files, source files, CMake configuration, and build scripts.

### Operator Code Implementation<a name="ZH-CN_TOPIC_0000002442022669"></a>

Detailed implementation guide for the three core classes:
- **OpNode class**: Operator node definition with attributes, input/output specifications
- **Parser class**: Parameter parsing from prototxt or other framework formats
- **Propagation class**: Shape inference for forward propagation

### Operator Project Compilation and Deployment<a name="ZH-CN_TOPIC_0000002442022689"></a>

#### Introduction<a name="ZH-CN_TOPIC_0000002441982833"></a>

The compilation process generates shared libraries (.so) for the custom operator.

#### Operator Project Compilation<a name="ZH-CN_TOPIC_0000002441982825"></a>

Steps to compile the operator project using CMake and Make.

# API Reference
## Common Parameters<a name="ZH-CN_TOPIC_0000002408583482"></a>

### ExtendedAttr Class<a name="ZH-CN_TOPIC_0000002442022733"></a>

#### ExtendedAttr Constructor and Destructor<a name="ZH-CN_TOPIC_0000002408583390"></a>

#### GetExtendedParam<a name="ZH-CN_TOPIC_0000002408423506"></a>

### AttributeType<a name="ZH-CN_TOPIC_0000002408583458"></a>

Enumerated type for operator attribute types.

### AttributeType<a name="ZH-CN_TOPIC_0000002408583462"></a>

Additional attribute type definitions.

### Propagation Inference Parameters<a name="ZH-CN_TOPIC_0000002408423518"></a>

#### ExtendedBuffer<a name="ZH-CN_TOPIC_0000002408423538"></a>

#### ExtendedDataInfo<a name="ZH-CN_TOPIC_0000002408583450"></a>

#### ExtendedDataInfoContainer<a name="ZH-CN_TOPIC_0000002442022613"></a>

#### ExtendedForwardParam<a name="ZH-CN_TOPIC_0000002408423522"></a>

## Common Interfaces<a name="ZH-CN_TOPIC_0000002408583354"></a>

### ExtendedOpNodeBase Class<a name="ZH-CN_TOPIC_0000002408423574"></a>

The base class for all custom operator node definitions.

#### ExtendedOpNodeBase Constructor and Destructor<a name="ZH-CN_TOPIC_0000002441982873"></a>

#### Parser<a name="ZH-CN_TOPIC_0000002442022693"></a>

Parses operator parameters from the framework model file.

#### CalcDataShape<a name="ZH-CN_TOPIC_0000002408423558"></a>

Calculates the output data shape based on input shapes and operator parameters.

#### CheckSpecification<a name="ZH-CN_TOPIC_0000002408583470"></a>

Validates operator specifications and constraints.

#### SetIsAacpuOp<a name="ZH-CN_TOPIC_0000002408423514"></a>

Sets whether this operator is an AICPU (AI CPU) operator.

#### GetIsAAcpuOp<a name="ZH-CN_TOPIC_0000002408423462"></a>

Gets whether this operator is an AICPU operator.

#### SetOpName<a name="ZH-CN_TOPIC_0000002408583346"></a>

Sets the operator name.

#### GetOpName<a name="ZH-CN_TOPIC_0000002408423546"></a>

Gets the operator name.

### ExtendedParserBase Class<a name="ZH-CN_TOPIC_0000002441982869"></a>

Base class for operator parameter parsing.

#### ExtendedParserBase Constructor and Destructor<a name="ZH-CN_TOPIC_0000002441982877"></a>

#### ParseParam<a name="ZH-CN_TOPIC_0000002441982885"></a>

Parses operator parameters from the framework-specific parameter format.

### ExtendedPropagationBase Class<a name="ZH-CN_TOPIC_0000002408423454"></a>

Base class for shape propagation inference.

#### ExtendedPropagationBase Constructor and Destructor<a name="ZH-CN_TOPIC_0000002408583410"></a>

#### Forward<a name="ZH-CN_TOPIC_0000002442022665"></a>

Performs shape propagation forward inference.

#### Init<a name="ZH-CN_TOPIC_0000002408423482"></a>

Initializes the propagation parameters.

#### Prepare<a name="ZH-CN_TOPIC_0000002442022629"></a>

Prepares the propagation context.

#### ForwardCpu<a name="ZH-CN_TOPIC_0000002408583446"></a>

CPU forward implementation for shape inference.

#### GetStride<a name="ZH-CN_TOPIC_0000002408423550"></a>

Gets the stride information.

#### GetactivateProp<a name="ZH-CN_TOPIC_0000002408423470"></a>

Gets the activation propagation information.

### UTILS API<a name="ZH-CN_TOPIC_0000002408423494"></a>

#### CreateOpNode<a name="ZH-CN_TOPIC_0000002442022581"></a>

Creates a new operator node instance.

#### GetLibVersion<a name="ZH-CN_TOPIC_0000002408583374"></a>

Gets the library version.

## CPU Inference Parameters<a name="ZH-CN_TOPIC_0000002408583426"></a>

### ExtendedAAcpuBuffer<a name="ZH-CN_TOPIC_0000002408583438"></a>

### ExtendedAAcpuDataInfo<a name="ZH-CN_TOPIC_0000002408583466"></a>

### ExtendedAAcpuDataInfoContainer<a name="ZH-CN_TOPIC_0000002408583478"></a>

### ExtendedAAcpuForwardParam<a name="ZH-CN_TOPIC_0000002441982805"></a>

## _NNN_ Parameters and Interfaces<a name="ZH-CN_TOPIC_0000002442022673"></a>

### Data Structure Definitions<a name="ZH-CN_TOPIC_0000002441982781"></a>

#### Scalar<a name="ZH-CN_TOPIC_0000002442022645"></a>

##### Function Description<a name="ZH-CN_TOPIC_0000002442022597"></a>

##### Data Type Definition<a name="ZH-CN_TOPIC_0000002441982769"></a>

##### Function Prototype<a name="ZH-CN_TOPIC_0000002442022725"></a>

##### Constraints<a name="ZH-CN_TOPIC_0000002442022681"></a>

##### Scalar Operations<a name="ZH-CN_TOPIC_0000002442022589"></a>

##### Debug Interfaces<a name="ZH-CN_TOPIC_0000002408583382"></a>

##### Call Example<a name="ZH-CN_TOPIC_0000002442022661"></a>

#### Tensor<a name="ZH-CN_TOPIC_0000002441982745"></a>

##### Function Description<a name="ZH-CN_TOPIC_0000002408423502"></a>

##### Data Type Definition<a name="ZH-CN_TOPIC_0000002408583418"></a>

##### Function Prototype<a name="ZH-CN_TOPIC_0000002441982753"></a>

##### Parameter Description<a name="ZH-CN_TOPIC_0000002442022701"></a>

##### Supported Operations<a name="ZH-CN_TOPIC_0000002408423490"></a>

##### Debug Interfaces<a name="ZH-CN_TOPIC_0000002442022653"></a>

##### Call Example<a name="ZH-CN_TOPIC_0000002442022601"></a>

### Program Control<a name="ZH-CN_TOPIC_0000002408583394"></a>

#### Introduction<a name="ZH-CN_TOPIC_0000002441982737"></a>

#### if<a name="ZH-CN_TOPIC_0000002408583358"></a>

##### if<a name="ZH-CN_TOPIC_0000002408583406"></a>

##### if-else if<a name="ZH-CN_TOPIC_0000002408423582"></a>

##### if-else<a name="ZH-CN_TOPIC_0000002408423530"></a>

##### if-elseif-..-else<a name="ZH-CN_TOPIC_0000002442022593"></a>

#### while<a name="ZH-CN_TOPIC_0000002441982801"></a>

##### while<a name="ZH-CN_TOPIC_0000002408583434"></a>

##### while-break<a name="ZH-CN_TOPIC_0000002442022621"></a>

### Interface Definitions<a name="ZH-CN_TOPIC_0000002408583398"></a>

#### Data Type Definition<a name="ZH-CN_TOPIC_0000002441982837"></a>

#### Offline Data Interface<a name="ZH-CN_TOPIC_0000002408583362"></a>

##### GetOfflineParamAddr<a name="ZH-CN_TOPIC_0000002442022609"></a>

#### Data Load Interface<a name="ZH-CN_TOPIC_0000002442022633"></a>

##### Load<a name="ZH-CN_TOPIC_0000002408583350"></a>

#### Data Store Interface<a name="ZH-CN_TOPIC_0000002441982765"></a>

##### Store<a name="ZH-CN_TOPIC_0000002441982817"></a>

#### Data Computation Interfaces<a name="ZH-CN_TOPIC_0000002441982829"></a>

##### VvAdd, VvSub, VvMul, VvDiv, VvMax, VvMin<a name="ZH-CN_TOPIC_0000002441982857"></a>

Vector-vector arithmetic operations.

##### VDivS, VSEmadS, VSEmadFaSb, VSEmadSaFb<a name="ZH-CN_TOPIC_0000002408583366"></a>

Vector-scalar arithmetic operations.

##### VSigmoid, VTanh, VExp, Vlog, VSqrt<a name="ZH-CN_TOPIC_0000002441982841"></a>

Activation function operations.

##### VDivF, VSEmadF<a name="ZH-CN_TOPIC_0000002441982809"></a>

Floating-point vector operations.

##### VSum, VMax, VMin<a name="ZH-CN_TOPIC_0000002442022617"></a>

Reduction operations.

##### VVMad<a name="ZH-CN_TOPIC_0000002408583370"></a>

Vector-vector multiply-add operation.

#### Utilization Statistics Interface<a name="ZH-CN_TOPIC_0000002442022685"></a>

#### DDR Debug Interface<a name="ZH-CN_TOPIC_0000002408583494"></a>

##### InitSpace<a name="ZH-CN_TOPIC_0000002442022729"></a>

##### GetSpaceSize<a name="ZH-CN_TOPIC_0000002408423586"></a>

##### InitDataRandom<a name="ZH-CN_TOPIC_0000002441982821"></a>

##### InitData<a name="ZH-CN_TOPIC_0000002441982853"></a>

##### SetOfflineParamAddr<a name="ZH-CN_TOPIC_0000002408423446"></a>

##### GetOfflineParamAddr<a name="ZH-CN_TOPIC_0000002408583402"></a>

##### GetDdrSpace<a name="ZH-CN_TOPIC_0000002442022721"></a>

##### SetDdrSpace<a name="ZH-CN_TOPIC_0000002408583454"></a>

##### PrintSpace<a name="ZH-CN_TOPIC_0000002441982849"></a>

##### PrintSpace<a name="ZH-CN_TOPIC_0000002441982761"></a>

# Sample Introduction
## CPU Sample Introduction<a name="ZH-CN_TOPIC_0000002441982789"></a>

### Prototxt Definition<a name="ZH-CN_TOPIC_0000002441982793"></a>

Prototxt definition for the Abs CPU custom operator sample.

### Custom Project Development<a name="ZH-CN_TOPIC_0000002442022625"></a>

#### AbsOpNode<a name="ZH-CN_TOPIC_0000002408583486"></a>

#### AbsParser<a name="ZH-CN_TOPIC_0000002408423466"></a>

#### Propagation<a name="ZH-CN_TOPIC_0000002442022717"></a>

#### AbsCpuForward<a name="ZH-CN_TOPIC_0000002441982865"></a>

### Simulation Project Run Results<a name="ZH-CN_TOPIC_0000002442022585"></a>

#### Simulation Project Test<a name="ZH-CN_TOPIC_0000002408583422"></a>

#### Board-side Project Test<a name="ZH-CN_TOPIC_0000002441982889"></a>

## _NNN_ Sample Introduction<a name="ZH-CN_TOPIC_0000002408583378"></a>

### Prototxt Definition<a name="ZH-CN_TOPIC_0000002408583474"></a>

Prototxt definition for the Add _NNN_ custom operator sample.

### Custom Project Development<a name="ZH-CN_TOPIC_0000002441982741"></a>

#### AddOpNode<a name="ZH-CN_TOPIC_0000002408423554"></a>

#### AddParser<a name="ZH-CN_TOPIC_0000002441982881"></a>

#### Propagation<a name="ZH-CN_TOPIC_0000002408423534"></a>

#### AddProcessLayer<a name="ZH-CN_TOPIC_0000002441982777"></a>

### Simulation Project Run Results<a name="ZH-CN_TOPIC_0000002442022637"></a>

#### Simulation Test Project Test<a name="ZH-CN_TOPIC_0000002442022649"></a>

#### Board-side Project Test<a name="ZH-CN_TOPIC_0000002408583498"></a>
