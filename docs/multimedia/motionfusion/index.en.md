---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/en/MotionFusion Development Reference/MotionFusion Development Reference.md
--- # Preface
**Product Version<a name="section2174mcpsimp"></a>** The product versions corresponding to this document are as follows. <a name="table2177mcpsimp"></a>
<table><thead align="left"><tr id="row2182mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p2184mcpsimp"><a name="p2184mcpsimp"></a><a name="p2184mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p2186mcpsimp"><a name="p2186mcpsimp"></a><a name="p2186mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row2188mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p2190mcpsimp"><a name="p2190mcpsimp"></a><a name="p2190mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p2192mcpsimp"><a name="p2192mcpsimp"></a><a name="p2192mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p937114671412"><a name="p937114671412"></a><a name="p937114671412"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section2193mcpsimp"></a>** The revision history cumulates documentation changes for each document update. The latest version of the document contains all updates from previous versions. <a name="table2674mcpsimp"></a>
<table><thead align="left"><tr id="row2680mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2682mcpsimp"><a name="p2682mcpsimp"></a><a name="p2682mcpsimp"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p2685mcpsimp"><a name="p2685mcpsimp"></a><a name="p2685mcpsimp"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p2688mcpsimp"><a name="p2688mcpsimp"></a><a name="p2688mcpsimp"></a>Change Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2699mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2701mcpsimp"><a name="p2701mcpsimp"></a><a name="p2701mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p2703mcpsimp"><a name="p2703mcpsimp"></a><a name="p2703mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p2705mcpsimp"><a name="p2705mcpsimp"></a><a name="p2705mcpsimp"></a>First temporary version release.</p>
</td>
</tr>
</tbody>
</table> # Overview
## Overview<a name="ZH-CN_TOPIC_0000002408262102"></a> MotionFusion refers to motion sensor fusion and compensation. It preprocesses data from motion measurement devices such as gyroscopes and accelerometers, and provides calibrated gyroscope data for image stabilization through calibration and compensation. ## Basic Concepts<a name="ZH-CN_TOPIC_0000002441661609"></a> - **Zero Bias** In a stationary state, the expected values of Gyro angular velocity and ACC acceleration should be 0. However, due to device manufacturing process issues or system errors, there may still be non-zero values in a stationary state. This value is called zero bias. - **Temperature Drift** The zero bias value of a device may vary at different temperatures. The zero bias values corresponding to different temperatures are called temperature drift. - **Calibration** The process of calibrating the accuracy or precision of a gyroscope or accelerometer using standard measurement methods. Calibration can eliminate systematic errors caused by manufacturing processes, improve device accuracy or precision, and determine the static characteristic indicators of the device or measurement system. - **Six-Side Calibration** Calibrating Sensitivity Scale Factor Error and Crosstalk (axis crosstalk) issues of a gyroscope or accelerometer device caused by its own characteristics or installation. - **Online Calibration** The process of a device self-calibrating. During normal operation, the device automatically calibrates or compensates for its own measurement errors. # API Reference
This functional module provides the following MPIs to the user: - [ss\_mpi\_mfusion\_set\_attr](#ZH-CN_TOPIC_0000002441701417): Sets the motionfusion attributes.
- [ss\_mpi\_mfusion\_get\_attr](#ZH-CN_TOPIC_0000002408102330): Gets the motionfusion attributes.
- [ss\_mpi\_mfusion\_set\_gyro\_drift](#ZH-CN_TOPIC_0000002408102362): Sets the Gyro zero bias.
- [ss\_mpi\_mfusion\_get\_gyro\_drift](#ZH-CN_TOPIC_0000002441701377): Gets the Gyro zero bias.
- [ss\_mpi\_mfusion\_set\_gyro\_six\_side\_calibration](#ZH-CN_TOPIC_0000002441701473): Sets the Gyro six-side calibration.
- [ss\_mpi\_mfusion\_get\_gyro\_six\_side\_calibration](#ZH-CN_TOPIC_0000002408262182): Gets the Gyro six-side calibration.
- [ss\_mpi\_mfusion\_set\_gyro\_temperature\_drift](#ZH-CN_TOPIC_0000002408262230): Sets the Gyro temperature drift parameters.
- [ss\_mpi\_mfusion\_get\_gyro\_temperature\_drift](#ZH-CN_TOPIC_0000002441701449): Gets the Gyro temperature drift parameters.
- [ss\_mpi\_mfusion\_set\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441661621): Sets the Gyro online temperature drift.
- [ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441701513): Gets the Gyro online temperature drift.
- [ss\_mpi\_mfusion\_set\_gyro\_online\_drift](#ZH-CN_TOPIC_0000002408102190): Sets the Gyro online zero bias.
- [ss\_mpi\_mfusion\_get\_gyro\_online\_drift](#ZH-CN_TOPIC_0000002408102286): Gets the Gyro online zero bias.
- [ss\_mpi\_mfusion\_bind\_vi](#ZH-CN_TOPIC_0000002408262258): Binds the fusion and pipe, chn.
- [ss\_mpi\_mfusion\_unbind\_vi](#ZH-CN_TOPIC_0000002408102254): Unbinds the fusion and pipe, chn. ## ss\_mpi\_mfusion\_set\_attr<a name="ZH-CN_TOPIC_0000002441701417"></a> 【Description】 Sets the motionfusion attributes. 【Syntax】 ```
td_s32 ss_mpi_mfusion_set_attr(const td_u32 fusion_id, const ot_mfusion_attr *mfusion_attr);
``` 【Parameters】 <a name="table2225mcpsimp"></a>
<table><thead align="left"><tr id="row2231mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p2233mcpsimp"><a name="p2233mcpsimp"></a><a name="p2233mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.4.1.2"><p id="p2235mcpsimp"><a name="p2235mcpsimp"></a><a name="p2235mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2237mcpsimp"><a name="p2237mcpsimp"></a><a name="p2237mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row2239mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p2241mcpsimp"><a name="p2241mcpsimp"></a><a name="p2241mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p2243mcpsimp"><a name="p2243mcpsimp"></a><a name="p2243mcpsimp"></a>Fusion device ID number. Range: [0, 1].</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2245mcpsimp"><a name="p2245mcpsimp"></a><a name="p2245mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row2246mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p2248mcpsimp"><a name="p2248mcpsimp"></a><a name="p2248mcpsimp"></a>mfusion_attr</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p2250mcpsimp"><a name="p2250mcpsimp"></a><a name="p2250mcpsimp"></a>Pointer to motionfusion attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2252mcpsimp"><a name="p2252mcpsimp"></a><a name="p2252mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table2254mcpsimp"></a>
<table><thead align="left"><tr id="row2259mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2261mcpsimp"><a name="p2261mcpsimp"></a><a name="p2261mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2263mcpsimp"><a name="p2263mcpsimp"></a><a name="p2263mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2265mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2267mcpsimp"><a name="p2267mcpsimp"></a><a name="p2267mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2269mcpsimp"><a name="p2269mcpsimp"></a><a name="p2269mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row2270mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2272mcpsimp"><a name="p2272mcpsimp"></a><a name="p2272mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2274mcpsimp"><a name="p2274mcpsimp"></a><a name="p2274mcpsimp"></a>Failure. See <a href="#ZH-CN_TOPIC_0000002441701493">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header files: ot\_common\_motionfusion.h, ss\_mpi\_motionfusion.h
- Library file: libss\_motionfusion.a 【Notes】 Magnetometer attribute settings are not currently supported. 【Example】 None. 【Related Topics】 None. ## ss\_mpi\_mfusion\_get\_attr<a name="ZH-CN_TOPIC_0000002408102330"></a> 【Description】 Gets the motionfusion attributes. 【Syntax】 ```
td_s32 ss_mpi_mfusion_get_attr(const td_u32 fusion_id, ot_mfusion_attr *mfusion_attr);
``` 【Parameters】 <a name="table2293mcpsimp"></a>
<table><thead align="left"><tr id="row2299mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2301mcpsimp"><a name="p2301mcpsimp"></a><a name="p2301mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p2303mcpsimp"><a name="p2303mcpsimp"></a><a name="p2303mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2305mcpsimp"><a name="p2305mcpsimp"></a><a name="p2305mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row2307mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2309mcpsimp"><a name="p2309mcpsimp"></a><a name="p2309mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2311mcpsimp"><a name="p2311mcpsimp"></a><a name="p2311mcpsimp"></a>Fusion device ID number. Range: [0, 1].</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2313mcpsimp"><a name="p2313mcpsimp"></a><a name="p2313mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row2314mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2316mcpsimp"><a name="p2316mcpsimp"></a><a name="p2316mcpsimp"></a>mfusion_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2318mcpsimp"><a name="p2318mcpsimp"></a><a name="p2318mcpsimp"></a>Pointer to motionfusion attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2320mcpsimp"><a name="p2320mcpsimp"></a><a name="p2320mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table2322mcpsimp"></a>
<table><thead align="left"><tr id="row2327mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2329mcpsimp"><a name="p2329mcpsimp"></a><a name="p2329mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2331mcpsimp"><a name="p2331mcpsimp"></a><a name="p2331mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2333mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2335mcpsimp"><a name="p2335mcpsimp"></a><a name="p2335mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2337mcpsimp"><a name="p2337mcpsimp"></a><a name="p2337mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row2338mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2340mcpsimp"><a name="p2340mcpsimp"></a><a name="p2340mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2274mcpsimp"><a name="p2274mcpsimp"></a><a name="p2274mcpsimp"></a>Failure. See <a href="#ZH-CN_TOPIC_0000002441701493">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header files: ot\_common\_motionfusion.h, ss\_mpi\_motionfusion.h
- Library file: libss\_motionfusion.a 【Notes】 None. 【Example】 None. 【Related Topics】 None. ## ss\_mpi\_mfusion\_set\_gyro\_drift<a name="ZH-CN_TOPIC_0000002408102362"></a> 【Description】 Sets the Gyro zero bias. 【Syntax】 ```
td_s32 ss_mpi_mfusion_set_gyro_drift(const td_u32 fusion_id, const ot_mfusion_drift *gyro_drift);
``` 【Parameters】 <a name="table2362mcpsimp"></a>
<table><thead align="left"><tr id="row2368mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2370mcpsimp"><a name="p2370mcpsimp"></a><a name="p2370mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p2372mcpsimp"><a name="p2372mcpsimp"></a><a name="p2372mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2374mcpsimp"><a name="p2374mcpsimp"></a><a name="p2374mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row2376mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2378mcpsimp"><a name="p2378mcpsimp"></a><a name="p2378mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2380mcpsimp"><a name="p2380mcpsimp"></a><a name="p2380mcpsimp"></a>Fusion device ID number. Range: [0, 1].</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2382mcpsimp"><a name="p2382mcpsimp"></a><a name="p2382mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row2383mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2385mcpsimp"><a name="p2385mcpsimp"></a><a name="p2385mcpsimp"></a>gyro_drift</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2387mcpsimp"><a name="p2387mcpsimp"></a><a name="p2387mcpsimp"></a>Gyroscope zero bias enable switch; gyroscope zero bias parameter array including zero bias values for x, y, and z axes.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2389mcpsimp"><a name="p2389mcpsimp"></a><a name="p2389mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table> 【Return Values】 <a name="table2391mcpsimp"></a>
<table><thead align="left"><tr id="row2396mcpsimp"><th class="cellrowborder" valign="top" width="46%" id="mcps1.1.3.1.1"><p id="p2398mcpsimp"><a name="p2398mcpsimp"></a><a name="p2398mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.1.3.1.2"><p id="p2400mcpsimp"><a name="p2400mcpsimp"></a><a name="p2400mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2402mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p2404mcpsimp"><a name="p2404mcpsimp"></a><a name="p2404mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p2406mcpsimp"><a name="p2406mcpsimp"></a><a name="p2406mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row2407mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p2409mcpsimp"><a name="p2409mcpsimp"></a><a name="p2409mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p2411mcpsimp"><a name="p2411mcpsimp"></a><a name="p2411mcpsimp"></a>Failure. See <a href="#ZH-CN_TOPIC_0000002441701493">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table> 【Requirements】 - Header files: ot\_common\_motionfusion.h, ss\_mpi\_motionfusion.h
- Library file: libss\_motionfusion.a 【Notes】 - To maintain zero bias stability unaffected by any range, the configured zero bias parameter is the product of the gyroscope raw reading zero bias multiplied by the range.
- The zero bias calibration process is: at a typical operating temperature, the gyroscope is stationary. The readings for the x, y, and z axes are obtained and averaged. The average is then multiplied by the range to obtain the final zero bias.
- The Gyro zero bias function is mutually exclusive with the Gyro online zero bias, Gyro temperature drift parameters, and Gyro online temperature drift parameters. Once one function is enabled, the others cannot be enabled. 【Example】 None. 【Related Topics】 None. ## ss\_mpi\_mfusion\_get\_gyro\_drift<a name="ZH-CN_TOPIC_0000002441701377"></a> 【Description】 Gets the Gyro zero bias. ... ## ss\_mpi\_mfusion\_set\_gyro\_six\_side\_calibration<a name="ZH-CN_TOPIC_0000002441701473"></a> 【Description】 Sets the Gyro six-side calibration. ... ## ss\_mpi\_mfusion\_get\_gyro\_six\_side\_calibration<a name="ZH-CN_TOPIC_0000002408262182"></a> 【Description】 Gets the Gyro six-side calibration. ... ## ss\_mpi\_mfusion\_set\_gyro\_temperature\_drift<a name="ZH-CN_TOPIC_0000002408262230"></a> 【Description】 Sets the Gyro temperature drift parameters. ... ## ss\_mpi\_mfusion\_get\_gyro\_temperature\_drift<a name="ZH-CN_TOPIC_0000002441701449"></a> 【Description】 Gets the Gyro temperature drift parameters. ... ## ss\_mpi\_mfusion\_set\_gyro\_online\_temperature\_drift<a name="ZH-CN_TOPIC_0000002441661621"></a> 【Description】 Sets the Gyro online temperature drift parameters. ... ## ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift<a name="ZH-CN_TOPIC_0000002441701513"></a> 【Description】 Gets the Gyro online temperature drift parameters. ... ## ss\_mpi\_mfusion\_set\_gyro\_online\_drift<a name="ZH-CN_TOPIC_0000002408102190"></a> 【Description】 Sets the Gyro online zero bias. ... ## ss\_mpi\_mfusion\_get\_gyro\_online\_drift<a name="ZH-CN_TOPIC_0000002408102286"></a> 【Description】 Gets the Gyro online zero bias. ... ## ss\_mpi\_mfusion\_bind\_vi<a name="ZH-CN_TOPIC_0000002408262258"></a> 【Description】 Binds the fusion and pipe, chn. ... ## ss\_mpi\_mfusion\_unbind\_vi<a name="ZH-CN_TOPIC_0000002408102254"></a> 【Description】 Unbinds the fusion and pipe, chn. ... ## Data Types<a name="ZH-CN_TOPIC_0000002441661617"></a> ... ## Error Codes<a name="ZH-CN_TOPIC_0000002441701493"></a> ...
