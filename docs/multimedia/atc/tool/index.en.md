---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/ATC工具使用指南/ATC工具使用指南.md
--- # Preface
**Overview<a name="section236mcpsimp"></a>** This document describes how to convert network models from open-source frameworks (such as Caffe, Onnx, etc.) into offline models supported by the image analysis engine using ATC (Advanced Tensor Compiler). During the model conversion process, operator scheduling optimization, weight data rearrangement, and memory usage optimization can be achieved. The preprocessing of the model can be completed without a device. **Product Version<a name="section300mcpsimp"></a>** The product versions corresponding to this document are as follows. <a name="table303mcpsimp"></a>
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
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p6760333131918"><a name="p6760333131918"></a><a name="p6760333131918"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Target Audience<a name="section239mcpsimp"></a>** This document is primarily intended for the following engineers: - Technical support engineers
- Software development engineers The following experience and skills are helpful for understanding this document: - Familiarity with basic Linux commands.
- Basic understanding of machine learning and image analysis methods. **Symbol Conventions<a name="section133020216410"></a>** The following symbols may appear in this document, with their meanings described below. **Change History<a name="section19186024461"></a>** <a name="table203mcpsimp"></a>
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
<td class="cellrowborder" valign="top" width="22.919999999999998%" headers="mcps1.1.4.1.2 "><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.85%" headers="mcps1.1.4.1.3 "><p id="p1031mcpsimp"><a name="p1031mcpsimp"></a><a name="p1031mcpsimp"></a>First release.</p>
</td>
</tr>
</tbody>
</table> # Introduction
## Tool Functional Architecture<a name="ZH-CN_TOPIC_0000002442020833"></a> The functional architecture of the ATC tool is shown in [Figure 1](#fig16910569311). As shown in [Figure 1](#fig16910569311), users can convert open-source framework network models into offline models suitable for the image analysis engine using the ATC tool. They can also convert the converted offline model into a json file for easy viewing. Users can also directly convert open-source framework network model files into json files through the ATC tool. **Figure 1** ATC Tool Functional Architecture<a name="fig16910569311"></a> ![](figures/AT Chas Function.png "ATC Tool Functional Architecture") ## Tool Running Flow<a name="ZH-CN_TOPIC_0000002408581678"></a> The overall flow of model conversion using the ATC tool is shown in [Figure 1](#fig125822392014). **Figure 1** Running Flow<a name="fig125822392014"></a> ![](figures/Rowstream.png "Running Flow") The detailed flow is described as follows: - Before using the ATC tool, install ATC in the development environment and locate the ATC tool in the relevant path. For details, see the environment preparation in [Getting the ATC Tool](#ZH-CN_TOPIC_0000002441981281).
- Prepare the model to be converted and upload it to the development environment. For details, see [Conversion Example](#ZH-CN_TOPIC_0000002442021333).
- Use the ATC tool for model conversion. When configuring related parameters, choose whether to perform [Quantization Options](#ZH-CN_TOPIC_0000002441981037) based on the actual situation. Image preprocessing is a hardware image preprocessing module provided by the image analysis engine, including color gamut conversion and image normalization (mean subtraction/coefficient multiplication). # Getting Started
## Preparations<a name="ZH-CN_TOPIC_0000002408422174"></a> ### Getting the ATC Tool<a name="ZH-CN_TOPIC_0000002441981281"></a> Install the CANN package independently. For details, see "2.3.4 Software Package Installation" in the Driver and Development Environment Installation Guide. This manual takes the independent installation of the CANN package for ATC as an example. ### Setting Environment Variables<a name="ZH-CN_TOPIC_0000002408422110"></a> > ![](public_sys-resources/icon-notice.gif) **Note:** > - Environment variables set using the export method are only valid in the current window. If users have previously set ATC installation path environment variables in the .bashrc file, they need to manually delete the originally set ATC installation path environment variables before executing the above commands.
> - If users have previously set ATC installation path environment variables for a previous version in the .bashrc file, they need to manually delete the originally set ATC installation path environment variables before executing the atc command, then set the following environment variables. After setting, switch to a new window to execute the atc model conversion command. **Mandatory Environment Variables** (In the following environment variables, ${install_path} uses the default installation path of the software package as an example) ```
export PATH=${install_path}/Ascend/ascend-toolkit/{software version}/atc/bin:$PATH export LD_LIBRARY_PATH=${install_path}/Ascend/ascend-toolkit/{software version}/atc/third_party_lib:$LD_LIBRARY_PATH
``` Or execute the following command to configure environment variables: ```
source ${install_path}/Ascend/ascend-toolkit/{software version}/x86_64-linux/script/setenv.sh
``` ### Conversion Example<a name="ZH-CN_TOPIC_0000002442021333"></a> This section provides an example of model conversion using the ATC tool, including the basic command format and usage. ### Output File Description<a name="ZH-CN_TOPIC_0000002408582014"></a> After model conversion, the ATC tool outputs the following files: - Offline model file (*.om): The converted offline model file.
- JSON file (*.json): A description file for the model structure (optional, generated when the --output_type=JSON parameter is specified). # Parameter Description
## Overview<a name="ZH-CN_TOPIC_0000002408421822"></a> This section describes the parameters supported by the ATC tool. The ATC tool parameters are categorized into basic functions, quantization options, and image preprocessing configurations. ## Basic Functions<a name="ZH-CN_TOPIC_0000002408422094"></a> The basic function parameters of the ATC tool include model input/output specification, framework type selection, operator configuration, and precision mode settings. **Model Conversion Parameters** <a name="table394mcpsimp"></a>
<table><thead align="left"><tr id="row399mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.1"><p id="p401mcpsimp"><a name="p401mcpsimp"></a><a name="p401mcpsimp"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.4.1.2"><p id="p403mcpsimp"><a name="p403mcpsimp"></a><a name="p403mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.3"><p id="p405mcpsimp"><a name="p405mcpsimp"></a><a name="p405mcpsimp"></a>Mandatory/Optional</p>
</th>
</tr>
</thead>
<tbody><tr id="row406mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>--model</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p410mcpsimp"><a name="p410mcpsimp"></a><a name="p410mcpsimp"></a>Specifies the input model file path.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.3 "><p id="p412mcpsimp"><a name="p412mcpsimp"></a><a name="p412mcpsimp"></a>Mandatory</p>
</td>
</tr>
<tr id="row413mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p415mcpsimp"><a name="p415mcpsimp"></a><a name="p415mcpsimp"></a>--framework</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p417mcpsimp"><a name="p417mcpsimp"></a><a name="p417mcpsimp"></a>Specifies the framework type of the input model.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.3 "><p id="p419mcpsimp"><a name="p419mcpsimp"></a><a name="p419mcpsimp"></a>Mandatory</p>
</td>
</tr>
<tr id="row420mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p422mcpsimp"><a name="p422mcpsimp"></a><a name="p422mcpsimp"></a>--output</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p424mcpsimp"><a name="p424mcpsimp"></a><a name="p424mcpsimp"></a>Specifies the output model file path and name.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.3 "><p id="p426mcpsimp"><a name="p426mcpsimp"></a><a name="p426mcpsimp"></a>Mandatory</p>
</td>
</tr>
<tr id="row427mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p429mcpsimp"><a name="p429mcpsimp"></a><a name="p429mcpsimp"></a>--soc_version</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p431mcpsimp"><a name="p431mcpsimp"></a><a name="p431mcpsimp"></a>Specifies the chip version.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.3 "><p id="p433mcpsimp"><a name="p433mcpsimp"></a><a name="p433mcpsimp"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table> ### Image Preprocessing Configuration<a name="ZH-CN_TOPIC_0000002442020965"></a> Image preprocessing is configured starting with the `--aapp_op` parameter, which identifies the AAPP (Advanced Application Pre-Processing) operator configuration. All input configurations are described within the aapp_op. - `related_input_rank` parameter (optional): Identifies which input of the model to apply image preprocessing to, starting from 0. Default is 0. For example, if the model has two inputs and preprocessing needs to be applied to the second input, configure related_input_rank as 1. - Type: Integer - Range: >= 0 - Input image format when running on the device side (mandatory): - Type: enum - Range: YUV420SP, YVU420SP, YUV422SP, YVU422SP, YUV400, BGR_PLANAR, RGB_PLANAR, RGB_PACKAGE, BGR_PACKAGE, XRGB_PLANAR, ARGB_PLANAR, XBGR_PLANAR, ABGR_PLANAR, RGBX_PLANAR, RGBA_PLANAR, BGRX_PLANAR, BGRA_PLANAR, XRGB_PACKAGE, ARGB_PACKAGE, XBGR_PACKAGE, ABGR_PACKAGE, RGBX_PACKAGE, RGBA_PACKAGE, BGRX_PACKAGE, BGRA_PACKAGE, RAW_RGGB, RAW_GRBG, RAW_GBRG, RAW_BGGR - Original model training image format (channel data order, optional): - Type: enum ### Quantization Options<a name="ZH-CN_TOPIC_0000002441981037"></a> The ATC tool provides quantization options to convert float32 models into lower-precision (such as int8 or float16) models for improved inference performance.
