---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/HNR 开发参考/HNR 开发参考.md
--- # Preface
**Overview<a name="section140mcpsimp"></a>** This document is written for software development engineers and image quality development engineers using HNR, aiming to provide usage guidance and assistance during development. >![](public_sys-resources/icon-note.gif) **Note:**
>This document uses Hi3403V100 as an example. Unless otherwise specified, content is consistent with Hi3403V100. **Product Version<a name="section143mcpsimp"></a>** The product versions corresponding to this document are as follows. <a name="table146mcpsimp"></a>
<table><thead align="left"><tr id="row151mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p153mcpsimp"><a name="p153mcpsimp"></a><a name="p153mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row157mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p159mcpsimp"><a name="p159mcpsimp"></a><a name="p159mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1361913118420"><a name="p1361913118420"></a><a name="p1361913118420"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section162mcpsimp"></a>** The revision history records the descriptions of each document update. The latest version of the document contains updates from all previous document versions. <a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a>Doc Version</p>
</th>
<th class="cellrowborder" valign="top" width="21.27%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="58.01%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a>Change Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16527181025018"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p393381565011"><a name="p393381565011"></a><a name="p393381565011"></a>00B02</p>
</td>
<td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.1.4.1.2 "><p id="p179331115155016"><a name="p179331115155016"></a><a name="p179331115155016"></a>2025-12-25</p>
</td>
<td class="cellrowborder" valign="top" width="58.01%" headers="mcps1.1.4.1.3 "><p id="p1893320150503"><a name="p1893320150503"></a><a name="p1893320150503"></a>The 2nd temporary version release.</p>
<p id="p11117153545011"><a name="p11117153545011"></a><a name="p11117153545011"></a>Modifications involving ot_hnr_ref_mode [Definition] and [Members].</p>
</td>
</tr>
<tr id="row1665351220483"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p10443201017431"><a name="p10443201017431"></a><a name="p10443201017431"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.1.4.1.2 "><p id="p6851917114310"><a name="p6851917114310"></a><a name="p6851917114310"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="58.01%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>The 1st temporary version release.</p>
</td>
</tr>
</tbody>
</table> # Overview
## Overview<a name="ZH-CN_TOPIC_0000002441661549"></a> HNR (hypersensitive noise reduction) is a new type of denoising algorithm that enables imaging devices to remove noise more cleanly and retain more detail at lower illumination levels, thereby improving the sensitivity of imaging devices in extremely low light conditions. This document mainly describes the interface description and usage notes for HNR. HNR reference frame normal mode supports 3840 x 2160@30fps performance, no-reference frame mode supports 3840 x 2160@40fps, and HNR supports a maximum frame rate of 100fps. ## Basic Concepts<a name="ZH-CN_TOPIC_0000002408102234"></a> - sfs (spatial filter strength), the spatial denoising strength.
- tfs (temporal filter strength), the temporal denoising strength. ## Performance<a name="ZH-CN_TOPIC_0000002441701401"></a> Linear OT_HNR_REF_MODE_NORM mode performance data is as follows. <a name="table11488022326"></a>
<table><thead align="left"><tr id="row353517225215"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p195350221520"><a name="p195350221520"></a><a name="p195350221520"></a>Resolution</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p135351522226"><a name="p135351522226"></a><a name="p135351522226"></a>Frame Rate</p>
</th>
</tr>
</thead>
<tbody><tr id="row853513223211"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1753511221526"><a name="p1753511221526"></a><a name="p1753511221526"></a>3840x2160</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7535132215214"><a name="p7535132215214"></a><a name="p7535132215214"></a>Single stream 30fps</p>
</td>
</tr>
<tr id="row1053512226218"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p13535132211219"><a name="p13535132211219"></a><a name="p13535132211219"></a>1920x1080</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p16535132216210"><a name="p16535132216210"></a><a name="p16535132216210"></a>Single stream 96fps</p>
</td>
</tr>
<tr id="row165353221023"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p175358221229"><a name="p175358221229"></a><a name="p175358221229"></a>1920x1080</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p195351922525"><a name="p195351922525"></a><a name="p195351922525"></a>Four streams 25fps</p>
</td>
</tr>
<tr id="row1853514221218"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5535182219215"><a name="p5535182219215"></a><a name="p5535182219215"></a>2688x1520</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7535162214216"><a name="p7535162214216"></a><a name="p7535162214216"></a>Single stream 57fps</p>
</td>
</tr>
<tr id="row1653610221822"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5536152215212"><a name="p5536152215212"></a><a name="p5536152215212"></a>2688x1520</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1753612218214"><a name="p1753612218214"></a><a name="p1753612218214"></a>Four streams 14fps</p>
</td>
</tr>
</tbody>
</table> # API Reference
This functional module provides the following AP Is: - [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525): Initializes the HNR module.
- [ss_mpi_hnr_exit](#ZH-CN_TOPIC_0000002408262170): Deinitializes the HNR module.
- [ss_mpi_hnr_load_cfg](#ZH-CN_TOPIC_0000002441701369): Loads the HNR configuration file.
- [ss_mpi_hnr_unload_cfg](#ZH-CN_TOPIC_0000002441701385): Unloads the HNR configuration file.
- [ss_mpi_hnr_set_alg_cfg](#ZH-CN_TOPIC_0000002441661513): Sets HNR algorithm configuration parameters.
- [ss_mpi_hnr_get_alg_cfg](#ZH-CN_TOPIC_0000002441661465): Gets HNR algorithm configuration parameters.
- [ss_mpi_hnr_enable](#ZH-CN_TOPIC_0000002408102158): Enables the HNR data stream switch.
- [ss_mpi_hnr_disable](#ZH-CN_TOPIC_0000002408102186): Disables the HNR data stream switch.
- [ss_mpi_hnr_set_attr](#ZH-CN_TOPIC_0000002441661457): Sets HNR attributes.
- [ss_mpi_hnr_get_attr](#ZH-CN_TOPIC_0000002408262070): Gets HNR attributes.
- [ss_mpi_hnr_set_input_depth](#ZH-CN_TOPIC_0000002441661493): Sets the buffer depth of the HNR input queue.
- [ss_mpi_hnr_set_thread_attr](#ZH-CN_TOPIC_0000002441661481): Sets HNR thread attributes.
- [ss_mpi_hnr_get_thread_attr](#ZH-CN_TOPIC_0000002408262054): Gets HNR thread attributes.
- [ss_mpi_hnr_attach_out_vb_pool](#ZH-CN_TOPIC_0000002408262098): Binds HNR output to a video buffer VB pool.
- [ss_mpi_hnr_detach_out_vb_pool](#ZH-CN_TOPIC_0000002441701317): Unbinds HNR output from a video buffer VB pool. ## ss_mpi_hnr_init<a name="ZH-CN_TOPIC_0000002441661525"></a> 【Description】 Initializes the HNR module. 【Syntax】 ```
td_s32 ss_mpi_hnr_init(td_void);
``` 【Parameters】 None 【Return Values】 <a name="table194mcpsimp"></a>
<table><thead align="left"><tr id="row199mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row205mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p207mcpsimp"><a name="p207mcpsimp"></a><a name="p207mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p209mcpsimp"><a name="p209mcpsimp"></a><a name="p209mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row210mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p212mcpsimp"><a name="p212mcpsimp"></a><a name="p212mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p214mcpsimp"><a name="p214mcpsimp"></a><a name="p214mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Does not support multi-process calls.
- The VI and ISP modules must be initialized before calling this interface. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_exit<a name="ZH-CN_TOPIC_0000002408262170"></a> 【Description】 Deinitializes the HNR module. 【Syntax】 ```
td_void ss_mpi_hnr_exit(td_void);
``` 【Parameters】 None 【Return Values】 <a name="table234mcpsimp"></a>
<table><thead align="left"><tr id="row239mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p241mcpsimp"><a name="p241mcpsimp"></a><a name="p241mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p243mcpsimp"><a name="p243mcpsimp"></a><a name="p243mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row245mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p247mcpsimp"><a name="p247mcpsimp"></a><a name="p247mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p249mcpsimp"><a name="p249mcpsimp"></a><a name="p249mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row250mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p252mcpsimp"><a name="p252mcpsimp"></a><a name="p252mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p254mcpsimp"><a name="p254mcpsimp"></a><a name="p254mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Does not support multi-process calls.
- Before calling this interface to deinitialize the HNR module, the HNR data stream switch must be disabled. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_load_cfg<a name="ZH-CN_TOPIC_0000002441701369"></a> 【Description】 Loads the HNR configuration file. 【Syntax】 ```
td_s32 ss_mpi_hnr_load_cfg(const ot_hnr_cfg *cfg, td_s32 *cfg_id);
``` 【Parameters】 <a name="table276mcpsimp"></a>
<table><thead align="left"><tr id="row282mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p284mcpsimp"><a name="p284mcpsimp"></a><a name="p284mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.4.1.2"><p id="p286mcpsimp"><a name="p286mcpsimp"></a><a name="p286mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p288mcpsimp"><a name="p288mcpsimp"></a><a name="p288mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row290mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p292mcpsimp"><a name="p292mcpsimp"></a><a name="p292mcpsimp"></a>cfg</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p294mcpsimp"><a name="p294mcpsimp"></a><a name="p294mcpsimp"></a>HNR configuration file pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p297mcpsimp"><a name="p297mcpsimp"></a><a name="p297mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row298mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p300mcpsimp"><a name="p300mcpsimp"></a><a name="p300mcpsimp"></a>cfg_id</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>Returned configuration file ID pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p305mcpsimp"><a name="p305mcpsimp"></a><a name="p305mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table307mcpsimp"></a>
<table><thead align="left"><tr id="row312mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p314mcpsimp"><a name="p314mcpsimp"></a><a name="p314mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row318mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p320mcpsimp"><a name="p320mcpsimp"></a><a name="p320mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p322mcpsimp"><a name="p322mcpsimp"></a><a name="p322mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row323mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p325mcpsimp"><a name="p325mcpsimp"></a><a name="p325mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p327mcpsimp"><a name="p327mcpsimp"></a><a name="p327mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module.
- The HNR data stream must remain disabled before calling this interface.
- Configuration files of the same type with equal image width and height cannot be loaded repeatedly.
- Supports loading multiple configuration files, or loading the same configuration file multiple times with different resolutions.
- Does not support multi-process calls.
- WDR mode does not support loading snapshot models. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_unload_cfg<a name="ZH-CN_TOPIC_0000002441701385"></a> 【Description】 Unloads the HNR configuration file. 【Syntax】 ```
td_s32 ss_mpi_hnr_unload_cfg(td_s32 cfg_id);
``` 【Parameters】 <a name="table351mcpsimp"></a>
<table><thead align="left"><tr id="row357mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p359mcpsimp"><a name="p359mcpsimp"></a><a name="p359mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.4.1.2"><p id="p361mcpsimp"><a name="p361mcpsimp"></a><a name="p361mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p363mcpsimp"><a name="p363mcpsimp"></a><a name="p363mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row365mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p367mcpsimp"><a name="p367mcpsimp"></a><a name="p367mcpsimp"></a>cfg_id</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p369mcpsimp"><a name="p369mcpsimp"></a><a name="p369mcpsimp"></a>The ID of the configuration file.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table374mcpsimp"></a>
<table><thead align="left"><tr id="row379mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p381mcpsimp"><a name="p381mcpsimp"></a><a name="p381mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p383mcpsimp"><a name="p383mcpsimp"></a><a name="p383mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row385mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p387mcpsimp"><a name="p387mcpsimp"></a><a name="p387mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p389mcpsimp"><a name="p389mcpsimp"></a><a name="p389mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row390mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p392mcpsimp"><a name="p392mcpsimp"></a><a name="p392mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p394mcpsimp"><a name="p394mcpsimp"></a><a name="p394mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before the application exits, this interface must be called to release the memory resources of loaded configuration files, or [ss_mpi_hnr_exit](#ZH-CN_TOPIC_0000002408262170) can be called to release all HNR resources.
- Does not support multi-process calls.
- The HNR data stream switch must be disabled before calling this interface. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_set_alg_cfg<a name="ZH-CN_TOPIC_0000002441661513"></a> 【Description】 Sets HNR algorithm configuration parameters. 【Syntax】 ```
td_s32 ss_mpi_hnr_set_alg_cfg(ot_vi_pipe vi_pipe, const ot_hnr_alg_cfg *cfg)
``` 【Parameters】 <a name="table418mcpsimp"></a>
<table><thead align="left"><tr id="row424mcpsimp"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.1"><p id="p426mcpsimp"><a name="p426mcpsimp"></a><a name="p426mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.4.1.2"><p id="p428mcpsimp"><a name="p428mcpsimp"></a><a name="p428mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p430mcpsimp"><a name="p430mcpsimp"></a><a name="p430mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row432mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.1 "><p id="p434mcpsimp"><a name="p434mcpsimp"></a><a name="p434mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.4.1.2 "><p id="p436mcpsimp"><a name="p436mcpsimp"></a><a name="p436mcpsimp"></a>VI module PIPE number.</p>
<p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p440mcpsimp"><a name="p440mcpsimp"></a><a name="p440mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row441mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.1 "><p id="p443mcpsimp"><a name="p443mcpsimp"></a><a name="p443mcpsimp"></a>cfg</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.4.1.2 "><p id="p445mcpsimp"><a name="p445mcpsimp"></a><a name="p445mcpsimp"></a>HNR algorithm parameter configuration structure pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p447mcpsimp"><a name="p447mcpsimp"></a><a name="p447mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table449mcpsimp"></a>
<table><thead align="left"><tr id="row454mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p456mcpsimp"><a name="p456mcpsimp"></a><a name="p456mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p458mcpsimp"><a name="p458mcpsimp"></a><a name="p458mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row460mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p462mcpsimp"><a name="p462mcpsimp"></a><a name="p462mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p464mcpsimp"><a name="p464mcpsimp"></a><a name="p464mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row465mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p467mcpsimp"><a name="p467mcpsimp"></a><a name="p467mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p469mcpsimp"><a name="p469mcpsimp"></a><a name="p469mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module.
- Before calling this interface, the pipe must be created and ISP must be initialized.
- When calling this interface, the HNR data stream must remain disabled.
- If this interface is not called, the default is reference frame mode.
- For photo-taking scenarios, this interface must be called to set no-reference frame mode.
- HNR reference frame normal mode supports a maximum resolution of 4096x4096; HNR no-reference frame mode (OT_HNR_REF_MODE_NONE and OT_HNR_REF_MODE_NONE_ADVANCED) supports a maximum resolution of 8192x8192.
- The current version of HNR no-reference frame mode (OT_HNR_REF_MODE_NONE and OT_HNR_REF_MODE_NONE_ADVANCED) does not support BGGR and GRBG Bayer image data formats.
- WDR mode does not support HNR no-reference frame mode (OT_HNR_REF_MODE_NONE and OT_HNR_REF_MODE_NONE_ADVANCED).
- OT_HNR_REF_MODE_NONE_ADVANCED mode is only supported when the VI video mode is OT_VI_VIDEO_MODE_ADVANCED.
- OT_HNR_REF_MODE_NONE_ADVANCED mode only supports the frame feeding method, with Run Once recommended.
- Input frames for OT_HNR_REF_MODE_NONE_ADVANCED mode only support non-compressed formats.
- If calling this interface from a non-main process, ss_mpi_isp_mem_share or ss_mpi_isp_mem_share_all must be called first to share ISP-related MMZ buffers. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_get_alg_cfg<a name="ZH-CN_TOPIC_0000002441661465"></a> 【Description】 Gets HNR algorithm configuration parameters. 【Syntax】 ```
td_s32 ss_mpi_hnr_get_alg_cfg(ot_vi_pipe vi_pipe, ot_hnr_alg_cfg *cfg);
``` 【Parameters】 <a name="table494mcpsimp"></a>
<table><thead align="left"><tr id="row500mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p502mcpsimp"><a name="p502mcpsimp"></a><a name="p502mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.4.1.2"><p id="p504mcpsimp"><a name="p504mcpsimp"></a><a name="p504mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p506mcpsimp"><a name="p506mcpsimp"></a><a name="p506mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row508mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p510mcpsimp"><a name="p510mcpsimp"></a><a name="p510mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p512mcpsimp"><a name="p512mcpsimp"></a><a name="p512mcpsimp"></a>VI module PIPE number.</p>
<p id="p513mcpsimp"><a name="p513mcpsimp"></a><a name="p513mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p516mcpsimp"><a name="p516mcpsimp"></a><a name="p516mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row517mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>cfg</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p521mcpsimp"><a name="p521mcpsimp"></a><a name="p521mcpsimp"></a>HNR algorithm parameter configuration structure pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p523mcpsimp"><a name="p523mcpsimp"></a><a name="p523mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table525mcpsimp"></a>
<table><thead align="left"><tr id="row530mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p532mcpsimp"><a name="p532mcpsimp"></a><a name="p532mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p534mcpsimp"><a name="p534mcpsimp"></a><a name="p534mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row536mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p538mcpsimp"><a name="p538mcpsimp"></a><a name="p538mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p540mcpsimp"><a name="p540mcpsimp"></a><a name="p540mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row541mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p543mcpsimp"><a name="p543mcpsimp"></a><a name="p543mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p545mcpsimp"><a name="p545mcpsimp"></a><a name="p545mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module.
- Before calling this interface, the pipe must be created and ISP must be initialized.
- If calling this interface from a non-main process, ss_mpi_isp_mem_share or ss_mpi_isp_mem_share_all must be called first to share ISP-related MMZ buffers. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_enable<a name="ZH-CN_TOPIC_0000002408102158"></a> 【Description】 Enables the HNR data stream switch. 【Syntax】 ```
td_s32 ss_mpi_hnr_enable(ot_vi_pipe vi_pipe);
``` 【Parameters】 <a name="table563mcpsimp"></a>
<table><thead align="left"><tr id="row569mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p571mcpsimp"><a name="p571mcpsimp"></a><a name="p571mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.4.1.2"><p id="p573mcpsimp"><a name="p573mcpsimp"></a><a name="p573mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p575mcpsimp"><a name="p575mcpsimp"></a><a name="p575mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row577mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p579mcpsimp"><a name="p579mcpsimp"></a><a name="p579mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p581mcpsimp"><a name="p581mcpsimp"></a><a name="p581mcpsimp"></a>VI module PIPE number.</p>
<p id="p582mcpsimp"><a name="p582mcpsimp"></a><a name="p582mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p585mcpsimp"><a name="p585mcpsimp"></a><a name="p585mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table587mcpsimp"></a>
<table><thead align="left"><tr id="row592mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p594mcpsimp"><a name="p594mcpsimp"></a><a name="p594mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p596mcpsimp"><a name="p596mcpsimp"></a><a name="p596mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row598mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p600mcpsimp"><a name="p600mcpsimp"></a><a name="p600mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p602mcpsimp"><a name="p602mcpsimp"></a><a name="p602mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row603mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p605mcpsimp"><a name="p605mcpsimp"></a><a name="p605mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p607mcpsimp"><a name="p607mcpsimp"></a><a name="p607mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before the main process calls this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module, and [ss_mpi_hnr_load_cfg](#ZH-CN_TOPIC_0000002441701369) must be called to load the HNR configuration file.
- Other non-main processes (e.g., PQ Tools) can use this interface to enable the HNR data stream without initializing HNR, but the main process must initialize the HNR module; otherwise, the data stream cannot actually be opened.
- If calling this interface from a non-main process, ss_mpi_isp_mem_share or ss_mpi_isp_mem_share_all must be called first to share ISP-related MMZ buffers.
- Before enabling hnr, the following constraints apply: - The corresponding pipe must have been created. - The user must call the function to allocate a VB pool. VB size is calculated using the function ot_hnr_get_pic_buf_size (see the "System Control" chapter in the MPP Media Processing Software V5.0 Development Reference). The allocated VB pool needs to be attached to the corresponding PIPE.
- If the data format of the input Bayer image is changed, [ss_mpi_hnr_disable](#ZH-CN_TOPIC_0000002408102186) must be called to disable HNR first, then re-enable the HNR data stream with this interface for the change to take effect.
- After HNR is enabled, reference frame mode takes effect after a 4-frame delay, and no-reference frame mode takes effect after a 2-frame delay.
- HNR only supports 12-bit Bayer image data processing. If the sensor input is not 12-bit Bayer, the VI PIPE output image data format must be set to Bayer 12bit.
- HNR linear mode usage has the following restrictions: - If another stream uses WDR mode, the VI video mode must be set to OT_VI_VIDEO_MODE_NORM; otherwise, the BNR effect on the WDR stream will be affected.
- HNR WDR mode usage has the following restrictions: - Only takes effect when VI is offline. - The VI video mode must be set to OT_VI_VIDEO_MODE_NORM. - HNR is recommended to bind to the long frame pipe, not a virtual pipe. - Compression must not be enabled on the pipe path. - The current version of HNR WDR mode does not support BGGR and GRBG Bayer image data formats. - normal_blend mode is not supported. - In high-performance scenarios, WDR long and short frames may lose sync, leading to abnormal WDR fusion effects. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_disable<a name="ZH-CN_TOPIC_0000002408102186"></a> 【Description】 Disables the HNR data stream switch. 【Syntax】 ```
td_s32 ss_mpi_hnr_disable(ot_vi_pipe vi_pipe);
``` 【Parameters】 <a name="table651mcpsimp"></a>
<table><thead align="left"><tr id="row657mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.4.1.2"><p id="p661mcpsimp"><a name="p661mcpsimp"></a><a name="p661mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p663mcpsimp"><a name="p663mcpsimp"></a><a name="p663mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row665mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p667mcpsimp"><a name="p667mcpsimp"></a><a name="p667mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p669mcpsimp"><a name="p669mcpsimp"></a><a name="p669mcpsimp"></a>VI module PIPE number.</p>
<p id="p670mcpsimp"><a name="p670mcpsimp"></a><a name="p670mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p673mcpsimp"><a name="p673mcpsimp"></a><a name="p673mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table675mcpsimp"></a>
<table><thead align="left"><tr id="row680mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p682mcpsimp"><a name="p682mcpsimp"></a><a name="p682mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p684mcpsimp"><a name="p684mcpsimp"></a><a name="p684mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row686mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p688mcpsimp"><a name="p688mcpsimp"></a><a name="p688mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p690mcpsimp"><a name="p690mcpsimp"></a><a name="p690mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row691mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p693mcpsimp"><a name="p693mcpsimp"></a><a name="p693mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p695mcpsimp"><a name="p695mcpsimp"></a><a name="p695mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before the main process calls this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module, and [ss_mpi_hnr_load_cfg](#ZH-CN_TOPIC_0000002441701369) must be called to load the HNR configuration file.
- Other non-main processes (e.g., PQ Tools) can use this interface to disable the HNR data stream without initializing HNR.
- If calling this interface from a non-main process, ss_mpi_isp_mem_share or ss_mpi_isp_mem_share_all must be called first to share ISP-related MMZ buffers.
- Before destroying the corresponding pipe in the VI module, this interface must be called to disable the HNR function; otherwise, VB leakage may occur. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_set_attr<a name="ZH-CN_TOPIC_0000002441661457"></a> 【Description】 Sets HNR attributes. 【Syntax】 ```
td_s32 ss_mpi_hnr_set_attr(ot_vi_pipe vi_pipe, const ot_hnr_attr *attr);
``` 【Parameters】 <a name="table719mcpsimp"></a>
<table><thead align="left"><tr id="row725mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p727mcpsimp"><a name="p727mcpsimp"></a><a name="p727mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p729mcpsimp"><a name="p729mcpsimp"></a><a name="p729mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p731mcpsimp"><a name="p731mcpsimp"></a><a name="p731mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row733mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p735mcpsimp"><a name="p735mcpsimp"></a><a name="p735mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p737mcpsimp"><a name="p737mcpsimp"></a><a name="p737mcpsimp"></a>VI module PIPE number.</p>
<p id="p738mcpsimp"><a name="p738mcpsimp"></a><a name="p738mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p741mcpsimp"><a name="p741mcpsimp"></a><a name="p741mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row742mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p744mcpsimp"><a name="p744mcpsimp"></a><a name="p744mcpsimp"></a>attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p746mcpsimp"><a name="p746mcpsimp"></a><a name="p746mcpsimp"></a>HNR attribute structure pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table750mcpsimp"></a>
<table><thead align="left"><tr id="row755mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p757mcpsimp"><a name="p757mcpsimp"></a><a name="p757mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p759mcpsimp"><a name="p759mcpsimp"></a><a name="p759mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row761mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p763mcpsimp"><a name="p763mcpsimp"></a><a name="p763mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p765mcpsimp"><a name="p765mcpsimp"></a><a name="p765mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row766mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p768mcpsimp"><a name="p768mcpsimp"></a><a name="p768mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p770mcpsimp"><a name="p770mcpsimp"></a><a name="p770mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module, and [ss_mpi_hnr_load_cfg](#ZH-CN_TOPIC_0000002441701369) must be called to load the HNR configuration file.
- The HNR data stream switch must be enabled before this interface can successfully set HNR attributes.
- When the VI video mode is OT_VI_VIDEO_MODE_NORM, if attr->enable is TD_FALSE, bnr_bypass must be TD_FALSE.
- When the VI video mode is OT_VI_VIDEO_MODE_ADVANCED, bnr_bypass has no effect.
- When the VI video mode is OT_VI_VIDEO_MODE_NORM and bnr_bypass is TD_FALSE, normal_blend can be enabled.
- When the VI video mode is OT_VI_VIDEO_MODE_NORM and normal_blend is enabled, getting HNR-processed RAW is not supported, and ISP Run Once HNR usage is not supported because the BE-fed RAW has not been processed by HNR.
- When the VI video mode is OT_VI_VIDEO_MODE_NORM and normal_blend is disabled, getting HNR-processed RAW is supported, and ISP Run Once HNR usage is supported.
- If calling this interface from a non-main process, ss_mpi_isp_mem_share or ss_mpi_isp_mem_share_all must be called first to share ISP-related MMZ buffers. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_get_attr<a name="ZH-CN_TOPIC_0000002408262070"></a> 【Description】 Gets HNR attributes. 【Syntax】 ```
td_s32 ss_mpi_hnr_get_attr(ot_vi_pipe vi_pipe, ot_hnr_attr *attr);
``` 【Parameters】 <a name="table796mcpsimp"></a>
<table><thead align="left"><tr id="row802mcpsimp"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.4.1.1"><p id="p804mcpsimp"><a name="p804mcpsimp"></a><a name="p804mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.4.1.2"><p id="p806mcpsimp"><a name="p806mcpsimp"></a><a name="p806mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p808mcpsimp"><a name="p808mcpsimp"></a><a name="p808mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row810mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p812mcpsimp"><a name="p812mcpsimp"></a><a name="p812mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.4.1.2 "><p id="p814mcpsimp"><a name="p814mcpsimp"></a><a name="p814mcpsimp"></a>VI module PIPE number.</p>
<p id="p815mcpsimp"><a name="p815mcpsimp"></a><a name="p815mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p818mcpsimp"><a name="p818mcpsimp"></a><a name="p818mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row819mcpsimp"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p821mcpsimp"><a name="p821mcpsimp"></a><a name="p821mcpsimp"></a>attr</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.4.1.2 "><p id="p823mcpsimp"><a name="p823mcpsimp"></a><a name="p823mcpsimp"></a>HNR attribute structure pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p825mcpsimp"><a name="p825mcpsimp"></a><a name="p825mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table827mcpsimp"></a>
<table><thead align="left"><tr id="row832mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p834mcpsimp"><a name="p834mcpsimp"></a><a name="p834mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p836mcpsimp"><a name="p836mcpsimp"></a><a name="p836mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row838mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p840mcpsimp"><a name="p840mcpsimp"></a><a name="p840mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p842mcpsimp"><a name="p842mcpsimp"></a><a name="p842mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row843mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p845mcpsimp"><a name="p845mcpsimp"></a><a name="p845mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p847mcpsimp"><a name="p847mcpsimp"></a><a name="p847mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - The HNR data stream switch must be enabled before this interface can successfully get HNR attributes.
- If calling this interface from a non-main process, ss_mpi_isp_mem_share or ss_mpi_isp_mem_share_all must be called first to share ISP-related MMZ buffers. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_set_input_depth<a name="ZH-CN_TOPIC_0000002441661493"></a> 【Description】 Sets the buffer depth of the HNR input queue. 【Syntax】 ```
td_s32 ss_mpi_hnr_set_input_depth(ot_vi_pipe vi_pipe, td_u32 depth);
``` 【Parameters】 <a name="table865mcpsimp"></a>
<table><thead align="left"><tr id="row871mcpsimp"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.1"><p id="p873mcpsimp"><a name="p873mcpsimp"></a><a name="p873mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.4.1.2"><p id="p875mcpsimp"><a name="p875mcpsimp"></a><a name="p875mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p877mcpsimp"><a name="p877mcpsimp"></a><a name="p877mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row879mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.1 "><p id="p881mcpsimp"><a name="p881mcpsimp"></a><a name="p881mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.4.1.2 "><p id="p883mcpsimp"><a name="p883mcpsimp"></a><a name="p883mcpsimp"></a>VI module PIPE number.</p>
<p id="p884mcpsimp"><a name="p884mcpsimp"></a><a name="p884mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p887mcpsimp"><a name="p887mcpsimp"></a><a name="p887mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row888mcpsimp"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.1 "><p id="p890mcpsimp"><a name="p890mcpsimp"></a><a name="p890mcpsimp"></a>depth</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.4.1.2 "><p id="p892mcpsimp"><a name="p892mcpsimp"></a><a name="p892mcpsimp"></a>Input buffer depth, range: [1, 20]</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p894mcpsimp"><a name="p894mcpsimp"></a><a name="p894mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table896mcpsimp"></a>
<table><thead align="left"><tr id="row901mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p903mcpsimp"><a name="p903mcpsimp"></a><a name="p903mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p905mcpsimp"><a name="p905mcpsimp"></a><a name="p905mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row907mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p909mcpsimp"><a name="p909mcpsimp"></a><a name="p909mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p911mcpsimp"><a name="p911mcpsimp"></a><a name="p911mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row912mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p914mcpsimp"><a name="p914mcpsimp"></a><a name="p914mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p916mcpsimp"><a name="p916mcpsimp"></a><a name="p916mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module, and the corresponding pipe must have been created. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_set_thread_attr<a name="ZH-CN_TOPIC_0000002441661481"></a> 【Description】 Sets HNR thread attributes. 【Syntax】 ```
td_s32 ss_mpi_hnr_set_thread_attr(const ot_hnr_thread_attr *thread_attr);
``` 【Parameters】 <a name="table719mcpsimp"></a>
<table><thead align="left"><tr id="row725mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p727mcpsimp"><a name="p727mcpsimp"></a><a name="p727mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p729mcpsimp"><a name="p729mcpsimp"></a><a name="p729mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p731mcpsimp"><a name="p731mcpsimp"></a><a name="p731mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row742mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p744mcpsimp"><a name="p744mcpsimp"></a><a name="p744mcpsimp"></a>thread_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p746mcpsimp"><a name="p746mcpsimp"></a><a name="p746mcpsimp"></a>HNR thread attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table750mcpsimp"></a>
<table><thead align="left"><tr id="row755mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p757mcpsimp"><a name="p757mcpsimp"></a><a name="p757mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p759mcpsimp"><a name="p759mcpsimp"></a><a name="p759mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row761mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p763mcpsimp"><a name="p763mcpsimp"></a><a name="p763mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p765mcpsimp"><a name="p765mcpsimp"></a><a name="p765mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row766mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p768mcpsimp"><a name="p768mcpsimp"></a><a name="p768mcpsimp"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p770mcpsimp"><a name="p770mcpsimp"></a><a name="p770mcpsimp"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 This interface can be called before [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) initializing the HNR module or after enabling the HNR path for dynamic modification. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_get_thread_attr<a name="ZH-CN_TOPIC_0000002408262054"></a> 【Description】 Gets HNR thread attributes. 【Syntax】 ```
td_s32 ss_mpi_hnr_get_thread_attr(const ot_hnr_thread_attr *thread_attr);
``` 【Parameters】 <a name="table1578315475611"></a>
<table><thead align="left"><tr id="row8783114718618"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p7784144713611"><a name="p7784144713611"></a><a name="p7784144713611"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p3784184719613"><a name="p3784184719613"></a><a name="p3784184719613"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p8784947961"><a name="p8784947961"></a><a name="p8784947961"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row13784647564"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p177843471469"><a name="p177843471469"></a><a name="p177843471469"></a>thread_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p57849476611"><a name="p57849476611"></a><a name="p57849476611"></a>HNR thread attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p278415471565"><a name="p278415471565"></a><a name="p278415471565"></a>Output</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table97841347266"></a>
<table><thead align="left"><tr id="row4784647763"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p378419471264"><a name="p378419471264"></a><a name="p378419471264"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4784047561"><a name="p4784047561"></a><a name="p4784047561"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row177842474614"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p27841647861"><a name="p27841647861"></a><a name="p27841647861"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1578410473614"><a name="p1578410473614"></a><a name="p1578410473614"></a>Success.</p>
</td>
</tr>
<tr id="row57845471368"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p207845470614"><a name="p207845470614"></a><a name="p207845470614"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p77841847464"><a name="p77841847464"></a><a name="p77841847464"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 None 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_attach_out_vb_pool<a name="ZH-CN_TOPIC_0000002408262098"></a> 【Description】 Binds HNR output to a video buffer VB pool. 【Syntax】 ```
td_s32 ss_mpi_hnr_attach_out_vb_pool(ot_vi_pipe vi_pipe, ot_vb_pool vb_pool);
``` 【Parameters】 <a name="table1010413506202"></a>
<table><thead align="left"><tr id="row3104850192012"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p810445072017"><a name="p810445072017"></a><a name="p810445072017"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p191041250122018"><a name="p191041250122018"></a><a name="p191041250122018"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p7104115082014"><a name="p7104115082014"></a><a name="p7104115082014"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row1610435013205"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p881mcpsimp"><a name="p881mcpsimp"></a><a name="p881mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p883mcpsimp"><a name="p883mcpsimp"></a><a name="p883mcpsimp"></a>VI module PIPE number.</p>
<p id="p884mcpsimp"><a name="p884mcpsimp"></a><a name="p884mcpsimp"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p887mcpsimp"><a name="p887mcpsimp"></a><a name="p887mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row11168919162613"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p5168619152615"><a name="p5168619152615"></a><a name="p5168619152615"></a>vb_pool</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p116861915261"><a name="p116861915261"></a><a name="p116861915261"></a>Video buffer VB pool information. See the "System Control" chapter for details.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p81681019122617"><a name="p81681019122617"></a><a name="p81681019122617"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table1810575010201"></a>
<table><thead align="left"><tr id="row13105205052018"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1510595052016"><a name="p1510595052016"></a><a name="p1510595052016"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p710535022013"><a name="p710535022013"></a><a name="p710535022013"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row141051550132017"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p19105205022019"><a name="p19105205022019"></a><a name="p19105205022019"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p910525022014"><a name="p910525022014"></a><a name="p910525022014"></a>Success.</p>
</td>
</tr>
<tr id="row910575013204"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p171056503201"><a name="p171056503201"></a><a name="p171056503201"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1105350112018"><a name="p1105350112018"></a><a name="p1105350112018"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module.
- The HNR data stream must remain disabled before calling this interface.
- Recommended for use only in VI stagger input scenarios when the VI video mode is OT_VI_VIDEO_MODE_NORM; using it in other scenarios may reduce VB utilization. 【Example】 None 【Related Topics】 None ## ss_mpi_hnr_detach_out_vb_pool<a name="ZH-CN_TOPIC_0000002441701317"></a> 【Description】 Unbinds HNR output from a video buffer VB pool. 【Syntax】 ```
td_s32 ss_mpi_hnr_detach_out_vb_pool(ot_vi_pipe vi_pipe);
``` 【Parameters】 <a name="table14616149162819"></a>
<table><thead align="left"><tr id="row86161449132817"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p761615496286"><a name="p761615496286"></a><a name="p761615496286"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p56162492284"><a name="p56162492284"></a><a name="p56162492284"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p20617164911286"><a name="p20617164911286"></a><a name="p20617164911286"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row2617174918282"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p16176495283"><a name="p16176495283"></a><a name="p16176495283"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p186175498281"><a name="p186175498281"></a><a name="p186175498281"></a>VI module PIPE number.</p>
<p id="p12617849142812"><a name="p12617849142812"></a><a name="p12617849142812"></a>Range: [0, OT_VI_MAX_PIPE_NUM). See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p9617149122813"><a name="p9617149122813"></a><a name="p9617149122813"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table461744915286"></a>
<table><thead align="left"><tr id="row13617154902818"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p16617449152814"><a name="p16617449152814"></a><a name="p16617449152814"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p361784992819"><a name="p361784992819"></a><a name="p361784992819"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1661774912811"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p11617104912813"><a name="p11617104912813"></a><a name="p11617104912813"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3617144902818"><a name="p3617144902818"></a><a name="p3617144902818"></a>Success.</p>
</td>
</tr>
<tr id="row361724918281"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p8617154915280"><a name="p8617154915280"></a><a name="p8617154915280"></a>Non-zero</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p196171249172810"><a name="p196171249172810"></a><a name="p196171249172810"></a>Failure, see <a href="#ZH-CN_TOPIC_0000002441701421">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header file: ss_mpi_hnr.h
- Library file: libss_hnr.a 【Notes】 - Before calling this interface, [ss_mpi_hnr_init](#ZH-CN_TOPIC_0000002441661525) must be called to initialize the HNR module.
- The HNR data stream must remain disabled before calling this interface. 【Example】 None 【Related Topics】 None # Data Types
HNR module-related data types are defined as follows: - [OT_HNR_MAX_CFG_NUM](#ZH-CN_TOPIC_0000002408262082): Defines the maximum number of HNR configuration files supported for loading.
- [ot_hnr_mem_info](#ZH-CN_TOPIC_0000002441701333): Defines HNR configuration file memory information.
- [ot_hnr_cfg](#ZH-CN_TOPIC_0000002408102170): Defines HNR configuration file information.
- [ot_hnr_param](#ZH-CN_TOPIC_0000002441701305): Defines HNR image effect parameters.
- [ot_hnr_manual_attr](#ZH-CN_TOPIC_0000002408102146): Defines HNR manual parameters.
- [ot_hnr_attr](#ZH-CN_TOPIC_0000002408102266): Defines HNR attributes.
- [ot_hnr_ref_mode](#ZH-CN_TOPIC_0000002408102250): Defines HNR reference frame mode.
- [ot_hnr_alg_cfg](#ZH-CN_TOPIC_0000002441701357): Defines HNR algorithm configuration parameters.
- [ot_hnr_thread_attr](#ZH-CN_TOPIC_0000002441661533): Defines HNR thread configuration parameters. ## OT_HNR_MAX_CFG_NUM<a name="ZH-CN_TOPIC_0000002408262082"></a> 【Description】 Defines the maximum number of HNR configuration files supported for loading. 【Definition】 ```
#define OT_HNR_MAX_CFG_NUM 32
``` 【Notes】 None 【Related Data Types and Interfaces】 None ## ot_hnr_mem_info<a name="ZH-CN_TOPIC_0000002441701333"></a> 【Description】 HNR configuration file memory information. 【Definition】 ```
typedef struct { td_phys_addr_t phys_addr; td_void *virt_addr; td_u32 size;
} ot_hnr_mem_info;
``` 【Members】 <a name="table976mcpsimp"></a>
<table><thead align="left"><tr id="row981mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p983mcpsimp"><a name="p983mcpsimp"></a><a name="p983mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p985mcpsimp"><a name="p985mcpsimp"></a><a name="p985mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row987mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p989mcpsimp"><a name="p989mcpsimp"></a><a name="p989mcpsimp"></a>phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p991mcpsimp"><a name="p991mcpsimp"></a><a name="p991mcpsimp"></a>Physical memory address of the HNR configuration file.</p>
<p id="p992mcpsimp"><a name="p992mcpsimp"></a><a name="p992mcpsimp"></a>See td_phys_addr_t in the "System Control" chapter of the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
</tr>
<tr id="row994mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p996mcpsimp"><a name="p996mcpsimp"></a><a name="p996mcpsimp"></a>virt_addr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p998mcpsimp"><a name="p998mcpsimp"></a><a name="p998mcpsimp"></a>Virtual memory address of the HNR configuration file.</p>
</td>
</tr>
<tr id="row999mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1001mcpsimp"><a name="p1001mcpsimp"></a><a name="p1001mcpsimp"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1003mcpsimp"><a name="p1003mcpsimp"></a><a name="p1003mcpsimp"></a>Memory size of the HNR configuration file.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 None 【Related Data Types and Interfaces】 [ot_hnr_cfg](#ot_hnr_cfg) ## ot_hnr_cfg<a name="ZH-CN_TOPIC_0000002408102170"></a> 【Description】 HNR configuration file information. 【Definition】 ```
typedef struct { ot_hnr_mem_info mem_info; ot_size image_size; td_bool is_wdr_mode;
} ot_hnr_cfg;
``` 【Members】 <a name="table1020mcpsimp"></a>
<table><thead align="left"><tr id="row1025mcpsimp"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p1027mcpsimp"><a name="p1027mcpsimp"></a><a name="p1027mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1031mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1033mcpsimp"><a name="p1033mcpsimp"></a><a name="p1033mcpsimp"></a>mem_info</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1035mcpsimp"><a name="p1035mcpsimp"></a><a name="p1035mcpsimp"></a>HNR configuration file memory information.</p>
</td>
</tr>
<tr id="row1037mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1039mcpsimp"><a name="p1039mcpsimp"></a><a name="p1039mcpsimp"></a>image_size</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1041mcpsimp"><a name="p1041mcpsimp"></a><a name="p1041mcpsimp"></a>Image resolution supported by the configuration file.</p>
</td>
</tr>
<tr id="row1042mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1044mcpsimp"><a name="p1044mcpsimp"></a><a name="p1044mcpsimp"></a>is_wdr_mode</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1046mcpsimp"><a name="p1046mcpsimp"></a><a name="p1046mcpsimp"></a>Whether the configuration file supports WDR mode; if not, it supports linear mode.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 - The user must ensure the integrity and correctness of the configuration file information stored in memory; otherwise, runtime anomalies may occur.
- When loading a configuration file, the supported image resolution must be specified.
- The width and height of supported image resolutions must be integer multiples of 4.
- The image resolution supported by HNR reference frame mode is consistent with the VI PIPE offline image size range. See the "Video Input" chapter in the MPP Media Processing Software V5.0 Development Reference for details. 【Related Data Types and Interfaces】 None ## ot_hnr_param<a name="ZH-CN_TOPIC_0000002441701305"></a> 【Description】 Defines HNR image effect parameters. 【Definition】 ```
typedef struct { td_u32 sfs; td_u32 tfs;
} ot_hnr_param;
``` 【Members】 <a name="table1064mcpsimp"></a>
<table><thead align="left"><tr id="row1069mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p1071mcpsimp"><a name="p1071mcpsimp"></a><a name="p1071mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p1073mcpsimp"><a name="p1073mcpsimp"></a><a name="p1073mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1075mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1077mcpsimp"><a name="p1077mcpsimp"></a><a name="p1077mcpsimp"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1079mcpsimp"><a name="p1079mcpsimp"></a><a name="p1079mcpsimp"></a>Spatial denoising strength for the overall image. The larger the value, the stronger the denoising.</p>
<p id="p1080mcpsimp"><a name="p1080mcpsimp"></a><a name="p1080mcpsimp"></a>Range: [0, 31]</p>
</td>
</tr>
<tr id="row1081mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1083mcpsimp"><a name="p1083mcpsimp"></a><a name="p1083mcpsimp"></a>tfs</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1085mcpsimp"><a name="p1085mcpsimp"></a><a name="p1085mcpsimp"></a>Temporal denoising strength. The larger the value, the stronger the temporal denoising. This version does not yet support adjustment of this parameter.</p>
<p id="p1086mcpsimp"><a name="p1086mcpsimp"></a><a name="p1086mcpsimp"></a>Range: [0, 31]</p>
</td>
</tr>
</tbody>
</table> 【Notes】 In the current version, the tfs parameter is not yet effective. For parameter adjustment, refer to the HNR Tuning Guide. 【Related Data Types and Interfaces】 [ot_hnr_manual_attr](#ot_hnr_manual_attr) ## ot_hnr_manual_attr<a name="ZH-CN_TOPIC_0000002408102146"></a> 【Description】 Defines HNR manual parameters. 【Definition】 ```
typedef struct { ot_hnr_param param;
} ot_hnr_manual_attr;
``` 【Members】 <a name="table1102mcpsimp"></a>
<table><thead align="left"><tr id="row1107mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p1109mcpsimp"><a name="p1109mcpsimp"></a><a name="p1109mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p1111mcpsimp"><a name="p1111mcpsimp"></a><a name="p1111mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1113mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1115mcpsimp"><a name="p1115mcpsimp"></a><a name="p1115mcpsimp"></a>param</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1117mcpsimp"><a name="p1117mcpsimp"></a><a name="p1117mcpsimp"></a>HNR image effect parameters.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 None 【Related Data Types and Interfaces】 [ot_hnr_attr](#ot_hnr_attr) ## ot_hnr_attr<a name="ZH-CN_TOPIC_0000002408102266"></a> 【Description】 Defines HNR attributes. 【Definition】 ```
typedef struct { td_bool enable; td_bool bnr_bypass; td_bool normal_blend; ot_op_mode op_type; ot_hnr_manual_attr manual_attr; ot_hnr_auto_attr auto_attr;
} ot_hnr_attr;
``` 【Members】 <a name="table1138mcpsimp"></a>
<table><thead align="left"><tr id="row1143mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p1145mcpsimp"><a name="p1145mcpsimp"></a><a name="p1145mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p1147mcpsimp"><a name="p1147mcpsimp"></a><a name="p1147mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1149mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1151mcpsimp"><a name="p1151mcpsimp"></a><a name="p1151mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1153mcpsimp"><a name="p1153mcpsimp"></a><a name="p1153mcpsimp"></a>Image effect enable switch.</p>
</td>
</tr>
<tr id="row1154mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1156mcpsimp"><a name="p1156mcpsimp"></a><a name="p1156mcpsimp"></a>bnr_bypass</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1158mcpsimp"><a name="p1158mcpsimp"></a><a name="p1158mcpsimp"></a>BNR Bypass switch. See the HNR Debugging Guide for HNR and BNR switching.</p>
</td>
</tr>
<tr id="row1796684721119"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1496617478119"><a name="p1496617478119"></a><a name="p1496617478119"></a>normal_blend</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p189661447151113"><a name="p189661447151113"></a><a name="p189661447151113"></a>Normal mode blend switch.</p>
</td>
</tr>
<tr id="row1159mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1161mcpsimp"><a name="p1161mcpsimp"></a><a name="p1161mcpsimp"></a>op_type</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1163mcpsimp"><a name="p1163mcpsimp"></a><a name="p1163mcpsimp"></a>HNR selection mode. See the "System Control" chapter in the MPP Media Processing Software V5.0 Development Reference.</p>
</td>
</tr>
<tr id="row1164mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1166mcpsimp"><a name="p1166mcpsimp"></a><a name="p1166mcpsimp"></a>manual_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1168mcpsimp"><a name="p1168mcpsimp"></a><a name="p1168mcpsimp"></a>HNR manual mode parameters.</p>
</td>
</tr>
<tr id="row1169mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1171mcpsimp"><a name="p1171mcpsimp"></a><a name="p1171mcpsimp"></a>auto_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1173mcpsimp"><a name="p1173mcpsimp"></a><a name="p1173mcpsimp"></a>HNR auto mode standard parameters.</p>
<p id="p1174mcpsimp"><a name="p1174mcpsimp"></a><a name="p1174mcpsimp"></a>The ot_hnr_auto_attr parameter is not yet supported.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 This version only supports manual mode parameters and does not support auto mode parameter configuration. 【Related Data Types and Interfaces】 None ## ot_hnr_ref_mode<a name="ZH-CN_TOPIC_0000002408102250"></a> 【Description】 Defines HNR reference frame mode. 【Definition】 ```
typedef enum { OT_HNR_REF_MODE_NORM = 0, OT_HNR_REF_MODE_NONE, OT_HNR_REF_MODE_NONE_ADVANCED, OT_HNR_REF_MODE_NORM_FACE, OT_HNR_REF_MODE_BUTT
} ot_hnr_ref_mode;
``` 【Members】 <a name="table1190mcpsimp"></a>
<table><thead align="left"><tr id="row1195mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p1197mcpsimp"><a name="p1197mcpsimp"></a><a name="p1197mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p1199mcpsimp"><a name="p1199mcpsimp"></a><a name="p1199mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1201mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p1203mcpsimp"><a name="p1203mcpsimp"></a><a name="p1203mcpsimp"></a>OT_HNR_REF_MODE_NORM</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1205mcpsimp"><a name="p1205mcpsimp"></a><a name="p1205mcpsimp"></a>HNR reference frame normal mode; image processing requires a reference frame. This is the default mode.</p>
</td>
</tr>
<tr id="row1206mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p1208mcpsimp"><a name="p1208mcpsimp"></a><a name="p1208mcpsimp"></a>OT_HNR_REF_MODE_NONE</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1210mcpsimp"><a name="p1210mcpsimp"></a><a name="p1210mcpsimp"></a>HNR no-reference frame mode; image processing does not require a reference frame.</p>
</td>
</tr>
<tr id="row051475832617"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p15514195882619"><a name="p15514195882619"></a><a name="p15514195882619"></a>OT_HNR_REF_MODE_NONE_ADVANCED</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p9514175819262"><a name="p9514175819262"></a><a name="p9514175819262"></a>HNR no-reference frame advanced mode; enhances dark area details in images, no reference frame required.</p>
</td>
</tr>
<tr id="row177621635151412"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p77622035101419"><a name="p77622035101419"></a><a name="p77622035101419"></a>OT_HNR_REF_MODE_NORM_FACE</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p117621135131413"><a name="p117621135131413"></a><a name="p117621135131413"></a>HNR reference frame face mode; enhances moving face details, image processing requires a reference frame.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 For photo-taking scenarios, choose HNR no-reference frame mode or HNR no-reference frame advanced mode. 【Related Data Types and Interfaces】 [ot_hnr_alg_cfg](#ot_hnr_alg_cfg) ## ot_hnr_alg_cfg<a name="ZH-CN_TOPIC_0000002441701357"></a> 【Description】 Defines HNR algorithm configuration parameters. 【Definition】 ```
typedef struct { ot_hnr_ref_mode ref_mode;
} ot_hnr_alg_cfg;
``` 【Members】 <a name="table1225mcpsimp"></a>
<table><thead align="left"><tr id="row1230mcpsimp"><th class="cellrowborder" valign="top" width="49%" id="mcps1.1.3.1.1"><p id="p1232mcpsimp"><a name="p1232mcpsimp"></a><a name="p1232mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.1.3.1.2"><p id="p1234mcpsimp"><a name="p1234mcpsimp"></a><a name="p1234mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1236mcpsimp"><td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.3.1.1 "><p id="p1238mcpsimp"><a name="p1238mcpsimp"></a><a name="p1238mcpsimp"></a>ref_mode</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.3.1.2 "><p id="p1240mcpsimp"><a name="p1240mcpsimp"></a><a name="p1240mcpsimp"></a>HNR reference frame mode.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 None 【Related Data Types and Interfaces】 None ## ot_hnr_thread_attr<a name="ZH-CN_TOPIC_0000002441661533"></a> 【Description】 Defines HNR thread attributes. 【Definition】 ```
typedef struct { td_u32 cpu_id;
} ot_hnr_thread_attr;
``` 【Members】 <a name="table439015344443"></a>
<table><thead align="left"><tr id="row16390173444411"><th class="cellrowborder" valign="top" width="49%" id="mcps1.1.3.1.1"><p id="p7390734124410"><a name="p7390734124410"></a><a name="p7390734124410"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.1.3.1.2"><p id="p3390734174417"><a name="p3390734174417"></a><a name="p3390734174417"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4390173418443"><td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.3.1.1 "><p id="p93905348447"><a name="p93905348447"></a><a name="p93905348447"></a>cpu_id</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.3.1.2 "><p id="p63901434134419"><a name="p63901434134419"></a><a name="p63901434134419"></a>Bound CPU ID, range: [0, 3].</p>
</td>
</tr>
</tbody>
</table> 【Notes】 None 【Related Data Types and Interfaces】 None # Proc Debug Information
## Overview<a name="ZH-CN_TOPIC_0000002408262154"></a> Debug information uses the Linux proc filesystem, which can reflect the current system running status in real time. The recorded information can be used for issue location and analysis. 【File Directory】 /proc/umap 【Information Viewing Method】 - On the console, use the cat command to view information: cat /proc/umap/isp or cat /proc/umap/pqp. Other commonly used file operation commands can also be used, such as cp /proc/umap/isp ./ or cp /proc/umap/pqp ./, to copy the file to the current directory.
- In applications, the above files can be read as ordinary read-only files, such as using fopen, fread, etc. >![](public_sys-resources/icon-note.gif) **Note:**
>There are two cases to note when describing parameters:
>- For parameters with values {0, 1}, if the mapping between specific values and meanings is not listed, 1 indicates affirmative and 0 indicates negative.
>- For parameters with values {aaa, bbb, ccc}, if the mapping between specific values and meanings is not listed, the meaning can be inferred directly from the values aaa, bbb, or ccc. ## Proc Information Description<a name="ZH-CN_TOPIC_0000002441661569"></a> ### HNR Debug Information Description<a name="ZH-CN_TOPIC_0000002408262134"></a> 【Debug Information】 ```
# cat /proc/umap/isp [ISP] Version: [MPP_Vx.x.x.x B0xx Release], Build Time[mm dd yyyy, hh:mm:ss]
----------------------------------------hnr info------------------------------------------------------------------------
hnr_en attr_en sfs set_bnr_bypass bnr_bypass_status long_frame_mode normal_blend normal_blend_status
1 1 31 1 0 N 0 0 cfg_id width height is_wdr ref_mode version_id 0 3840 2160 N norm 2021082801 vi_pipe iso handle busy_node free_node ref_mode input_depth ref_cnt work_time slp_cnt slp_time 0 3521 1 2 1 norm 8 1 12226 26 12231 ``` 【Notes】 HNR-related proc information can be viewed only after the HNR data stream is enabled for the first time. 【Debug Information Analysis】 Records current HNR working status and resource information, mainly including HNR user settings, loaded configuration file information, and task status information. 【Parameter Description】 <a name="table1278mcpsimp"></a>
<table><thead align="left"><tr id="row1284mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1286mcpsimp"><a name="p1286mcpsimp"></a><a name="p1286mcpsimp"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1288mcpsimp"><a name="p1288mcpsimp"></a><a name="p1288mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1290mcpsimp"><td class="cellrowborder" rowspan="8" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p id="p1292mcpsimp"><a name="p1292mcpsimp"></a><a name="p1292mcpsimp"></a>HNR User Settings</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p id="p1294mcpsimp"><a name="p1294mcpsimp"></a><a name="p1294mcpsimp"></a>hnr_en</p>
</td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p id="p1296mcpsimp"><a name="p1296mcpsimp"></a><a name="p1296mcpsimp"></a>HNR data stream switch.</p>
</td>
</tr>
<tr id="row1297mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1299mcpsimp"><a name="p1299mcpsimp"></a><a name="p1299mcpsimp"></a>attr_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1301mcpsimp"><a name="p1301mcpsimp"></a><a name="p1301mcpsimp"></a>HNR effect switch.</p>
</td>
</tr>
<tr id="row1302mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1304mcpsimp"><a name="p1304mcpsimp"></a><a name="p1304mcpsimp"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1306mcpsimp"><a name="p1306mcpsimp"></a><a name="p1306mcpsimp"></a>Spatial denoising strength for the image.</p>
</td>
</tr>
<tr id="row1308mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1310mcpsimp"><a name="p1310mcpsimp"></a><a name="p1310mcpsimp"></a>set_bnr_bypass</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1312mcpsimp"><a name="p1312mcpsimp"></a><a name="p1312mcpsimp"></a>BNR Bypass setting switch.</p>
</td>
</tr>
<tr id="row1313mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1315mcpsimp"><a name="p1315mcpsimp"></a><a name="p1315mcpsimp"></a>bnr_bypass_status</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1317mcpsimp"><a name="p1317mcpsimp"></a><a name="p1317mcpsimp"></a>BNR Bypass active status.</p>
</td>
</tr>
<tr id="row1318mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1320mcpsimp"><a name="p1320mcpsimp"></a><a name="p1320mcpsimp"></a>long_frame_mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1322mcpsimp"><a name="p1322mcpsimp"></a><a name="p1322mcpsimp"></a>Whether in long frame mode.</p>
<p id="p1323mcpsimp"><a name="p1323mcpsimp"></a><a name="p1323mcpsimp"></a>Y: long frame mode;</p>
<p id="p1324mcpsimp"><a name="p1324mcpsimp"></a><a name="p1324mcpsimp"></a>N: not long frame mode.</p>
</td>
</tr>
<tr id="row1174272813719"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p117421828163717"><a name="p117421828163717"></a><a name="p117421828163717"></a>normal_blend</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p87424285371"><a name="p87424285371"></a><a name="p87424285371"></a>normal_blend setting switch.</p>
</td>
</tr>
<tr id="row5318131493719"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p19318181415371"><a name="p19318181415371"></a><a name="p19318181415371"></a>normal_blend_status</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1831851419375"><a name="p1831851419375"></a><a name="p1831851419375"></a>normal_blend active status.</p>
</td>
</tr>
<tr id="row1325mcpsimp"><td class="cellrowborder" rowspan="6" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p id="p1327mcpsimp"><a name="p1327mcpsimp"></a><a name="p1327mcpsimp"></a>HNR Config File Info</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p id="p1329mcpsimp"><a name="p1329mcpsimp"></a><a name="p1329mcpsimp"></a>cfg_id</p>
</td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p id="p1331mcpsimp"><a name="p1331mcpsimp"></a><a name="p1331mcpsimp"></a>Configuration file ID.</p>
</td>
</tr>
<tr id="row1333mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1335mcpsimp"><a name="p1335mcpsimp"></a><a name="p1335mcpsimp"></a>width</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1337mcpsimp"><a name="p1337mcpsimp"></a><a name="p1337mcpsimp"></a>Image width corresponding to the configuration file.</p>
</td>
</tr>
<tr id="row1338mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1340mcpsimp"><a name="p1340mcpsimp"></a><a name="p1340mcpsimp"></a>height</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1342mcpsimp"><a name="p1342mcpsimp"></a><a name="p1342mcpsimp"></a>Image height corresponding to the configuration file.</p>
</td>
</tr>
<tr id="row1343mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1345mcpsimp"><a name="p1345mcpsimp"></a><a name="p1345mcpsimp"></a>is_wdr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1347mcpsimp"><a name="p1347mcpsimp"></a><a name="p1347mcpsimp"></a>Whether the configuration file is in WDR mode.</p>
<p id="p1348mcpsimp"><a name="p1348mcpsimp"></a><a name="p1348mcpsimp"></a>Y: WDR mode;</p>
<p id="p1349mcpsimp"><a name="p1349mcpsimp"></a><a name="p1349mcpsimp"></a>N: linear mode.</p>
</td>
</tr>
<tr id="row1350mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1352mcpsimp"><a name="p1352mcpsimp"></a><a name="p1352mcpsimp"></a>ref_mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1354mcpsimp"><a name="p1354mcpsimp"></a><a name="p1354mcpsimp"></a>Reference frame mode of the configuration file.</p>
<p id="p1355mcpsimp"><a name="p1355mcpsimp"></a><a name="p1355mcpsimp"></a>norm: reference frame normal mode, image processing requires a reference frame;</p>
<p id="p1356mcpsimp"><a name="p1356mcpsimp"></a><a name="p1356mcpsimp"></a>none: no-reference frame mode, image processing does not require a reference frame;</p>
<p id="p17409131362115"><a name="p17409131362115"></a><a name="p17409131362115"></a>advanced: no-reference frame advanced mode.</p>
</td>
</tr>
<tr id="row1357mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1359mcpsimp"><a name="p1359mcpsimp"></a><a name="p1359mcpsimp"></a>version_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1361mcpsimp"><a name="p1361mcpsimp"></a><a name="p1361mcpsimp"></a>Configuration file version ID.</p>
</td>
</tr>
<tr id="row1362mcpsimp"><td class="cellrowborder" rowspan="11" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p id="p1364mcpsimp"><a name="p1364mcpsimp"></a><a name="p1364mcpsimp"></a>HNR Task Status Info</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p id="p1366mcpsimp"><a name="p1366mcpsimp"></a><a name="p1366mcpsimp"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p id="p1368mcpsimp"><a name="p1368mcpsimp"></a><a name="p1368mcpsimp"></a>VI PIPE number corresponding to the HNR enabled path.</p>
</td>
</tr>
<tr id="row1369mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1371mcpsimp"><a name="p1371mcpsimp"></a><a name="p1371mcpsimp"></a>iso</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1373mcpsimp"><a name="p1373mcpsimp"></a><a name="p1373mcpsimp"></a>ISO information used for HNR calculation.</p>
<p id="p128741112132515"><a name="p128741112132515"></a><a name="p128741112132515"></a>The ISO value comes from the iso field in isp_frame_info within the frame supplement information.</p>
<p id="p1374mcpsimp"><a name="p1374mcpsimp"></a><a name="p1374mcpsimp"></a>In WDR non-long frame mode, this iso value equals the ISP iso divided by the ISP gain.</p>
</td>
</tr>
<tr id="row1375mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1377mcpsimp"><a name="p1377mcpsimp"></a><a name="p1377mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1379mcpsimp"><a name="p1379mcpsimp"></a><a name="p1379mcpsimp"></a>HNR current task handle number.</p>
</td>
</tr>
<tr id="row1380mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1382mcpsimp"><a name="p1382mcpsimp"></a><a name="p1382mcpsimp"></a>busy_node</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1384mcpsimp"><a name="p1384mcpsimp"></a><a name="p1384mcpsimp"></a>Number of busy nodes in the HNR task queue.</p>
</td>
</tr>
<tr id="row1385mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1387mcpsimp"><a name="p1387mcpsimp"></a><a name="p1387mcpsimp"></a>free_node</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1389mcpsimp"><a name="p1389mcpsimp"></a><a name="p1389mcpsimp"></a>Number of free nodes in the HNR task queue.</p>
</td>
</tr>
<tr id="row1390mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1392mcpsimp"><a name="p1392mcpsimp"></a><a name="p1392mcpsimp"></a>ref_mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1394mcpsimp"><a name="p1394mcpsimp"></a><a name="p1394mcpsimp"></a>HNR reference frame mode.</p>
<p id="p1121935572210"><a name="p1121935572210"></a><a name="p1121935572210"></a>norm: reference frame normal mode, image processing requires a reference frame;</p>
<p id="p1321935518225"><a name="p1321935518225"></a><a name="p1321935518225"></a>none: no-reference frame mode, image processing does not require a reference frame;</p>
<p id="p7219855162219"><a name="p7219855162219"></a><a name="p7219855162219"></a>advanced: no-reference frame advanced mode.</p>
</td>
</tr>
<tr id="row1398mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1400mcpsimp"><a name="p1400mcpsimp"></a><a name="p1400mcpsimp"></a>input_depth</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1402mcpsimp"><a name="p1402mcpsimp"></a><a name="p1402mcpsimp"></a>Buffer depth of the HNR input queue.</p>
</td>
</tr>
<tr id="row168991915161"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p149091917163"><a name="p149091917163"></a><a name="p149091917163"></a>ref_cnt</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1190819181614"><a name="p1190819181614"></a><a name="p1190819181614"></a>Number of tasks currently submitted.</p>
</td>
</tr>
<tr id="row1282114237166"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p182192312167"><a name="p182192312167"></a><a name="p182192312167"></a>work_time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1682119239162"><a name="p1682119239162"></a><a name="p1682119239162"></a>Maximum time spent on submitted tasks within 10s, in us.</p>
</td>
</tr>
<tr id="row83822541710"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p2038275171714"><a name="p2038275171714"></a><a name="p2038275171714"></a>slp_cnt</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p938212513172"><a name="p938212513172"></a><a name="p938212513172"></a>Number of times the submit thread enters sleep within 10s.</p>
</td>
</tr>
<tr id="row127161928171615"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p671752871615"><a name="p671752871615"></a><a name="p671752871615"></a>slp_time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p15717162816166"><a name="p15717162816166"></a><a name="p15717162816166"></a>Average time per sleep of the submit thread within 10s, in us.</p>
</td>
</tr>
</tbody>
</table> ### PQP Debug Information Description<a name="ZH-CN_TOPIC_0000002441701433"></a> 【Debug Information】 ```
# cat /proc/umap/pqp [PQP] Version: [Vx.x.x.x B0xx Release], Build Time[mm dd yyyy, hh:mm:ss]
----------------------------------------pqp module param------------------------------ dev_id high_profile 0 N -------------------------------- pqp task queue info---------------------------------- dev_id wait_queue_id work_queue_id wait_head_idx wait_tail_idx 0 0 -1 0 0 work_head_idx work_tail_idx 0 0 -------------------------------------- pqp task info ----------------------------------- dev_id handle task_send task_finish last_finish_id start_task_id handle_wrap 0 0 0 0 0 0 0 finish_wrap 0 -------------------------------------- pqp perf info------------------------------------ dev_id irq_num_per_sec last_irq_time max_irq_time last_task_time 0 0 0 0 0 --------------------------------------- pqp err info------------------------------------- dev_id query_timeout_num hw_timeout_num hw_err_num 0 0 0 0 ``` 【Debug Information Analysis】 Records current PQP working status resource information, mainly including PQP queue status information, task status information, performance information, and error information. 【Parameter Description】 <a name="table1426mcpsimp"></a>
<table><thead align="left"><tr id="row1432mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1434mcpsimp"><a name="p1434mcpsimp"></a><a name="p1434mcpsimp"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1436mcpsimp"><a name="p1436mcpsimp"></a><a name="p1436mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody>
<tr><td class="cellrowborder" rowspan="2" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p>pqp module param</p><p>PQP module parameter information</p></td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p>dev_id</p></td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p>Dev ID.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>high_profile</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>High performance switch: only Hi3403V100 supports this.</p><p>Y: enabled;</p><p>N: disabled.</p></td>
</tr>
<tr><td class="cellrowborder" rowspan="7" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p>pqp task queue info</p><p>PQP module task queue information</p></td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p>dev_id</p></td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p>Dev ID.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>wait_queue_id</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Wait queue ID (0 or 1).</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>work_queue_id</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Work queue ID (0, 1, or -1); -1 indicates hardware idle.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>wait_head_idx</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Index of the first valid task in the wait queue.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>wait_tail_idx</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Index of the last valid task in the wait queue.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>work_head_idx</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Index of the first valid task in the work queue.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>work_tail_idx</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Index of the last valid task in the work queue.</p></td>
</tr>
<tr><td class="cellrowborder" rowspan="8" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p>pqp task info</p><p>PQP task related information</p></td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p>dev_id</p></td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p>Dev ID.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>handle</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Currently allocated task handle number.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>task_send</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of tasks currently sent.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>task_finish</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of tasks currently completed.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>last_finish_id</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>ID of the last completed task.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>start_task_id</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>ID of the most recently started hardware task.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>handle_wrap</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of times the handle number allocation wrapped.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>finish_wrap</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of times the completed task count wrapped.</p></td>
</tr>
<tr><td class="cellrowborder" rowspan="5" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p>pqp perf info</p><p>PQP performance related information</p></td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p>dev_id</p></td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p>Dev ID.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>irq_num_per_sec</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of interrupt executions in the most recent 1 second.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>last_irq_time</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Execution time of the most recent interrupt, in us.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>max_irq_time</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Maximum execution time for a single interrupt, in us.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>last_task_time</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Execution time of the most recent task, in us.</p></td>
</tr>
<tr><td class="cellrowborder" rowspan="4" valign="top" width="21.21212121212121%" headers="mcps1.1.4.1.1 "><p>pqp err info</p><p>PQP error information</p></td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.4.1.1 "><p>dev_id</p></td>
<td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.1.4.1.2 "><p>Dev ID.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>query_timeout_num</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of task query timeouts.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>hw_timeout_num</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of hardware execution timeouts.</p></td>
</tr>
<tr><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>hw_err_num</p></td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p>Number of hardware execution errors.</p></td>
</tr>
</tbody>
</table> # Error Codes
HNR error codes are as follows. **Table 1** HNR API error codes <a name="_Ref248290030"></a>
<table><thead align="left"><tr id="row1613mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p1615mcpsimp"><a name="p1615mcpsimp"></a><a name="p1615mcpsimp"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.2"><p id="p1617mcpsimp"><a name="p1617mcpsimp"></a><a name="p1617mcpsimp"></a>Macro Definition</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.3"><p id="p1619mcpsimp"><a name="p1619mcpsimp"></a><a name="p1619mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1621mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1623mcpsimp"><a name="p1623mcpsimp"></a><a name="p1623mcpsimp"></a>0xa0528002</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_INVALID_PIPE_ID</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1627mcpsimp"><a name="p1627mcpsimp"></a><a name="p1627mcpsimp"></a>Invalid PIPE ID</p>
</td>
</tr>
<tr id="row1628mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1630mcpsimp"><a name="p1630mcpsimp"></a><a name="p1630mcpsimp"></a>0xa0528007</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_ILLEGAL_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1634mcpsimp"><a name="p1634mcpsimp"></a><a name="p1634mcpsimp"></a>Invalid parameter</p>
</td>
</tr>
<tr id="row1635mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1637mcpsimp"><a name="p1637mcpsimp"></a><a name="p1637mcpsimp"></a>0xa052800a</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1641mcpsimp"><a name="p1641mcpsimp"></a><a name="p1641mcpsimp"></a>Null pointer error in input parameter</p>
</td>
</tr>
<tr id="row1642mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1644mcpsimp"><a name="p1644mcpsimp"></a><a name="p1644mcpsimp"></a>0xa052800c</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_NOT_SUPPORT</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1648mcpsimp"><a name="p1648mcpsimp"></a><a name="p1648mcpsimp"></a>Operation not supported</p>
</td>
</tr>
<tr id="row1649mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1651mcpsimp"><a name="p1651mcpsimp"></a><a name="p1651mcpsimp"></a>0xa052800d</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_NOT_PERM</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1655mcpsimp"><a name="p1655mcpsimp"></a><a name="p1655mcpsimp"></a>Operation not permitted</p>
</td>
</tr>
<tr id="row1656mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1658mcpsimp"><a name="p1658mcpsimp"></a><a name="p1658mcpsimp"></a>0xa0528014</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_NO_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1662mcpsimp"><a name="p1662mcpsimp"></a><a name="p1662mcpsimp"></a>Data buffer overflow</p>
</td>
</tr>
<tr id="row1663mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1665mcpsimp"><a name="p1665mcpsimp"></a><a name="p1665mcpsimp"></a>0xa0528018</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_NOT_READY</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1669mcpsimp"><a name="p1669mcpsimp"></a><a name="p1669mcpsimp"></a>Not initialized</p>
</td>
</tr>
<tr id="row1670mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1672mcpsimp"><a name="p1672mcpsimp"></a><a name="p1672mcpsimp"></a>0xa0528050</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.2 "><p>OT_ERR_HNR_BIN_NOT_MATACH</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1676mcpsimp"><a name="p1676mcpsimp"></a><a name="p1676mcpsimp"></a>Bin configuration file mismatch</p>
</td>
</tr>
</tbody>
</table>
