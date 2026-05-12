---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/图像分析引擎2与图像分析引擎1使用差异说明/图像分析引擎2与图像分析引擎1使用差异说明.md
---

# Preface
**Overview<a name="section145mcpsimp"></a>**

This document describes the development differences between Image Analysis Engine 2 and Image Analysis Engine 1.

**Product Versions<a name="section300mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table303mcpsimp"></a>
<table><thead align="left"><tr id="row308mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p310mcpsimp"><a name="p310mcpsimp"></a><a name="p310mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p312mcpsimp"><a name="p312mcpsimp"></a><a name="p312mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row314mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1376073312191"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p5760533111913"><a name="p5760533111913"></a><a name="p5760533111913"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p6760333131918"><a name="p6760333131918"></a><a name="p6760333131918"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section150mcpsimp"></a>**

This document is primarily intended for the following engineers:

-   Technical Support Engineers
-   Software Development Engineers

**Revision History<a name="section156mcpsimp"></a>**

The revision history records the updates made to each document version. The latest version of the document includes all updates from previous versions.

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.06%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.06%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table>

# SDK Interface Differences
## Style Differences<a name="ZH-CN_TOPIC_0000002441980521"></a>

Image Analysis Engine 1 uses the ACL interface, and Image Analysis Engine 2 uses the SVP ACL interface.

To avoid symbol conflicts during compilation, SVP ACL uses the Linux style, with macro definitions and enums prefixed with SVP_ACL_. ACL uses the camelCase style, with macro definitions and enums prefixed with ACL_. See [Table 1](#table183mcpsimp) for detailed differences in functions, macro definitions, enums, and structures.

**Table 1** Style Difference Examples

<a name="table183mcpsimp"></a>
<table><thead align="left"><tr id="row190mcpsimp"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.1"><p id="p192mcpsimp"><a name="p192mcpsimp"></a><a name="p192mcpsimp"></a>Difference</p>
</th>
<th class="cellrowborder" valign="top" width="39.18%" id="mcps1.2.4.1.2"><p id="p194mcpsimp"><a name="p194mcpsimp"></a><a name="p194mcpsimp"></a>ACL Interface</p>
</th>
<th class="cellrowborder" valign="top" width="49.82%" id="mcps1.2.4.1.3"><p id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a>SVP_ACL Interface</p>
</th>
</tr>
</thead>
<tbody><tr id="row198mcpsimp"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.1 "><p id="p200mcpsimp"><a name="p200mcpsimp"></a><a name="p200mcpsimp"></a>Function</p>
</td>
<td class="cellrowborder" valign="top" width="39.18%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock15403587314"><a name="codeblock15403587314"></a><a name="codeblock15403587314"></a>aclInit(const char *configPath)</pre>
</td>
<td class="cellrowborder" valign="top" width="49.82%" headers="mcps1.2.4.1.3 "><pre class="codeblock" id="codeblock181561342"><a name="codeblock181561342"></a><a name="codeblock181561342"></a>svp_acl_init(const char *config_path)</pre>
</td>
</tr>
<tr id="row205mcpsimp"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.1 "><p id="p207mcpsimp"><a name="p207mcpsimp"></a><a name="p207mcpsimp"></a>Macro</p>
</td>
<td class="cellrowborder" valign="top" width="39.18%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock16299115212210"><a name="codeblock16299115212210"></a><a name="codeblock16299115212210"></a>#define ACL_MAX_DIM_CNT          128</pre>
</td>
<td class="cellrowborder" valign="top" width="49.82%" headers="mcps1.2.4.1.3 "><pre class="codeblock" id="codeblock5354175511212"><a name="codeblock5354175511212"></a><a name="codeblock5354175511212"></a>#define SVP_ACL_MAX_DIM_CNT          128</pre>
</td>
</tr>
<tr id="row212mcpsimp"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.1 "><p id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a>Enum</p>
</td>
<td class="cellrowborder" valign="top" width="39.18%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock45217611210"><a name="codeblock45217611210"></a><a name="codeblock45217611210"></a>typedef enum aclrtRunMode {
    ACL_DEVICE,
    ACL_HOST,
} aclrtRunMode;</pre>
</td>
<td class="cellrowborder" valign="top" width="49.82%" headers="mcps1.2.4.1.3 "><pre class="codeblock" id="codeblock1566414105212"><a name="codeblock1566414105212"></a><a name="codeblock1566414105212"></a>typedef enum svp_acl_rt_run_mode {
    SVP_ACL_DEVICE,
    SVP_ACL_HOST,
} svp_acl_rt_run_mode;</pre>
</td>
</tr>
<tr id="row225mcpsimp"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.1 "><p id="p227mcpsimp"><a name="p227mcpsimp"></a><a name="p227mcpsimp"></a>Struct</p>
</td>
<td class="cellrowborder" valign="top" width="39.18%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock141280435318"><a name="codeblock141280435318"></a><a name="codeblock141280435318"></a>typedef struct aclmdlIODims {
    char name[ACL_MAX_TENSOR_NAME_LEN];
    size_t dimCount;
    int64_t dims[ACL_MAX_DIM_CNT];
} aclmdlIODims;</pre>
</td>
<td class="cellrowborder" valign="top" width="49.82%" headers="mcps1.2.4.1.3 "><pre class="codeblock" id="codeblock54308261337"><a name="codeblock54308261337"></a><a name="codeblock54308261337"></a>typedef struct svp_acl_mdl_io_dims {
    char name[SVP_ACL_MAX_TENSOR_NAME_LEN];
    size_t dim_count;
    int64_t dims[SVP_ACL_MAX_DIM_CNT];
} svp_acl_mdl_io_dims;</pre>
</td>
</tr>
</tbody>
</table>

## Usage Differences<a name="ZH-CN_TOPIC_0000002442020361"></a>

### Create Data Buffer Function<a name="ZH-CN_TOPIC_0000002442020401"></a>

Since the Image Analysis Engine 2 logic requires stride information for input/output data to quickly jump to the next row during read/write operations, a stride parameter is added when creating and updating data buffers.

**Table 1** Create Data Buffer Function Differences

<a name="table244mcpsimp"></a>
<table><thead align="left"><tr id="row251mcpsimp"><th class="cellrowborder" valign="top" width="9.01%" id="mcps1.2.4.1.1"><p id="p253mcpsimp"><a name="p253mcpsimp"></a><a name="p253mcpsimp"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="44.99%" id="mcps1.2.4.1.2"><p id="p255mcpsimp"><a name="p255mcpsimp"></a><a name="p255mcpsimp"></a>ACL Function</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p257mcpsimp"><a name="p257mcpsimp"></a><a name="p257mcpsimp"></a>SVP_ACL Function</p>
</th>
</tr>
</thead>
<tbody><tr id="row259mcpsimp"><td class="cellrowborder" valign="top" width="9.01%" headers="mcps1.2.4.1.1 "><p id="p261mcpsimp"><a name="p261mcpsimp"></a><a name="p261mcpsimp"></a>Create</p>
</td>
<td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock10935184052"><a name="codeblock10935184052"></a><a name="codeblock10935184052"></a>aclCreateDataBuffer(void *data, size_t size);</pre>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><pre class="codeblock" id="codeblock392181515514"><a name="codeblock392181515514"></a><a name="codeblock392181515514"></a>svp_acl_data_buffer *svp_acl_create_data_buffer(void *data, size_t size, size_t stride)</pre>
</td>
</tr>
<tr id="row266mcpsimp"><td class="cellrowborder" valign="top" width="9.01%" headers="mcps1.2.4.1.1 "><p id="p268mcpsimp"><a name="p268mcpsimp"></a><a name="p268mcpsimp"></a>Update</p>
</td>
<td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock5290177652"><a name="codeblock5290177652"></a><a name="codeblock5290177652"></a>aclUpdateDataBuffer(aclDataBuffer *dataBuffer, void *data, size_t size);</pre>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><pre class="codeblock" id="codeblock1939412173518"><a name="codeblock1939412173518"></a><a name="codeblock1939412173518"></a>svp_acl_update_data_buffer(svp_acl_data_buffer *data_buffer, void *data, size_t size, size_t stride);</pre>
</td>
</tr>
</tbody>
</table>

Due to the introduction of stride, the input/output sizes returned by SVP_ACL interfaces are memory sizes aligned to the stride. To facilitate obtaining the stride, the SVP_ACL interface adds new functions related to stride operations, as shown in the table below:

**Table 2** New Stride-Related Functions

<a name="table274mcpsimp"></a>
<table><thead align="left"><tr id="row281mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p283mcpsimp"><a name="p283mcpsimp"></a><a name="p283mcpsimp"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.2"><p id="p285mcpsimp"><a name="p285mcpsimp"></a><a name="p285mcpsimp"></a>SVP_ACL Function</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.3"><p id="p287mcpsimp"><a name="p287mcpsimp"></a><a name="p287mcpsimp"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row289mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p291mcpsimp"><a name="p291mcpsimp"></a><a name="p291mcpsimp"></a>Get the configured stride from a data buffer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock12578131955"><a name="codeblock12578131955"></a><a name="codeblock12578131955"></a>size_t svp_acl_get_data_buffer_stride(const svp_acl_data_buffer *data_buffer);</pre>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.3 "><p id="p295mcpsimp"><a name="p295mcpsimp"></a><a name="p295mcpsimp"></a>None.</p>
</td>
</tr>
<tr id="row296mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p298mcpsimp"><a name="p298mcpsimp"></a><a name="p298mcpsimp"></a>Get the default stride for model input data</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock24281834953"><a name="codeblock24281834953"></a><a name="codeblock24281834953"></a>size_t svp_acl_mdl_get_input_default_stride(const svp_acl_mdl_desc *model_desc, size_t index);</pre>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.3 "><p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>Stride is aligned to the last dimension of the input shape.</p>
</td>
</tr>
<tr id="row303mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p305mcpsimp"><a name="p305mcpsimp"></a><a name="p305mcpsimp"></a>Get the default stride for model output data</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.2 "><pre class="codeblock" id="codeblock17781162120"><a name="codeblock17781162120"></a><a name="codeblock17781162120"></a>size_t svp_acl_mdl_get_output_default_stride(const svp_acl_mdl_desc *model_desc, size_t index);</pre>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.3 "><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>Stride is aligned to the last dimension of the output shape.</p>
</td>
</tr>
</tbody>
</table>

### Additional API Differences

In addition to the data buffer and stride-related changes, the following sections in the original Chinese document detail additional API differences between ACL (Engine 1) and SVP_ACL (Engine 2), including changes to:

- Context management functions (aclrtSetDevice -> svp_acl_rt_set_device, etc.)
- Stream management functions
- Memory management functions
- Model management functions (model loading, execution, unloading)
- Dataset management functions
- Inference execution functions

For the complete list of all API differences, including all function prototypes, enum definitions, macro definitions, and struct definitions, please refer to the original Chinese source document. All code snippets are included there in full detail, organized by functional category.

The key differences can be summarized as:
- All function names follow the pattern: camelCase (ACL) -> snake_case (SVP_ACL)
- All prefix changes: ACL_ -> SVP_ACL_
- All struct/type changes: aclXxx -> svp_acl_xxx
- The data buffer create/update functions add a stride parameter
- New stride query functions are introduced in the SVP_ACL interface
