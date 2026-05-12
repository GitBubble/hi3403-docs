---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/MotionFusion 开发参考/MotionFusion 开发参考.md
---

# 前言
**产品版本<a name="section2174mcpsimp"></a>**

与本文档相对应的产品版本如下。

<a name="table2177mcpsimp"></a>
<table><thead align="left"><tr id="row2182mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p2184mcpsimp"><a name="p2184mcpsimp"></a><a name="p2184mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p2186mcpsimp"><a name="p2186mcpsimp"></a><a name="p2186mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row2188mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p2190mcpsimp"><a name="p2190mcpsimp"></a><a name="p2190mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p2192mcpsimp"><a name="p2192mcpsimp"></a><a name="p2192mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1450412425144"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1937114619148"><a name="p1937114619148"></a><a name="p1937114619148"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p937114671412"><a name="p937114671412"></a><a name="p937114671412"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**修订记录<a name="section2193mcpsimp"></a>**

修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。

<a name="table2674mcpsimp"></a>
<table><thead align="left"><tr id="row2680mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2682mcpsimp"><a name="p2682mcpsimp"></a><a name="p2682mcpsimp"></a>文档版本</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p2685mcpsimp"><a name="p2685mcpsimp"></a><a name="p2685mcpsimp"></a>发布日期</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p2688mcpsimp"><a name="p2688mcpsimp"></a><a name="p2688mcpsimp"></a>修改说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row2699mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2701mcpsimp"><a name="p2701mcpsimp"></a><a name="p2701mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p2703mcpsimp"><a name="p2703mcpsimp"></a><a name="p2703mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p2705mcpsimp"><a name="p2705mcpsimp"></a><a name="p2705mcpsimp"></a>第1次临时版本发布。</p>
</td>
</tr>
</tbody>
</table>

# 概述
## 概述<a name="ZH-CN_TOPIC_0000002408262102"></a>

MotionFusion即运动传感器的融合补偿，对陀螺仪、加速度计等运动测量器件的数据进行预处理，通过标定和补偿，为防抖提供校准后的陀螺仪数据。

## 基本概念<a name="ZH-CN_TOPIC_0000002441661609"></a>

-   零偏

    静止状态下，Gyro的角速度和ACC的加速度预期的值应该是0，但因为设备器件的工艺等问题或系统误差，在静止状态下仍然有非0的值，这个值我们称之为零偏。

-   温飘

    不同温度下，设备器件的零偏值可能不同。不同温度下对应的零偏我们称之为温飘。

-   标定

    使用标准的计量方法对陀螺仪或加速度计的准确度或精度进行校准的过程。标定可以消除工艺等问题引起的系统误差，改善设备的准确度或精确度，确定设备或测量系统的静态特性指标。

-   六面标定及校准

    标定及校准陀螺仪或加速度计设备由于自身特性或者是安装引起的Sensitivity Scale Factor Error\(灵敏度误差\)及Crosstalk（轴间串扰）问题。

-   在线标定及校准

    设备自标定的过程。设备在正常工作过程中，对自身计量误差的自动校准或者补偿的过程。

# API参考
该功能模块为用户提供以下MPI：

-   [ss\_mpi\_mfusion\_set\_attr](#ZH-CN_TOPIC_0000002441701417)：设置motionfusion属性。
-   [ss\_mpi\_mfusion\_get\_attr](#ZH-CN_TOPIC_0000002408102330)：获取motionfusion属性。
-   [ss\_mpi\_mfusion\_set\_gyro\_drift](#ZH-CN_TOPIC_0000002408102362)：设置Gyro零偏。
-   [ss\_mpi\_mfusion\_get\_gyro\_drift](#ZH-CN_TOPIC_0000002441701377)：获取Gyro零偏。
-   [ss\_mpi\_mfusion\_set\_gyro\_six\_side\_calibration](#ZH-CN_TOPIC_0000002441701473)：设置Gyro六面标定。
-   [ss\_mpi\_mfusion\_get\_gyro\_six\_side\_calibration](#ZH-CN_TOPIC_0000002408262182)：获取Gyro六面标定。
-   [ss\_mpi\_mfusion\_set\_gyro\_temperature\_drift](#ZH-CN_TOPIC_0000002408262230)：设置Gyro温飘参数。
-   [ss\_mpi\_mfusion\_get\_gyro\_temperature\_drift](#ZH-CN_TOPIC_0000002441701449)：获取Gyro温飘参数。
-   [ss\_mpi\_mfusion\_set\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441661621)：设置Gyro在线温飘。
-   [ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441701513)：获取Gyro在线温飘。
-   [ss\_mpi\_mfusion\_set\_gyro\_online\_drift](#ZH-CN_TOPIC_0000002408102190)：设置Gyro在线零偏。
-   [ss\_mpi\_mfusion\_get\_gyro\_online\_drift](#ZH-CN_TOPIC_0000002408102286)：获取Gyro在线零偏。
-   [ss\_mpi\_mfusion\_bind\_vi](#ZH-CN_TOPIC_0000002408262258)：绑定fusion和pipe、chn。
-   [ss\_mpi\_mfusion\_unbind\_vi](#ZH-CN_TOPIC_0000002408102254)：解绑定fusion和pipe、chn。















## ss\_mpi\_mfusion\_set\_attr<a name="ZH-CN_TOPIC_0000002441701417"></a>

【描述】

设置motionfusion属性。

【语法】

```
td_s32 ss_mpi_mfusion_set_attr(const td_u32 fusion_id, const ot_mfusion_attr *mfusion_attr);
```

【参数】

<a name="table2225mcpsimp"></a>
<table><thead align="left"><tr id="row2231mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p2233mcpsimp"><a name="p2233mcpsimp"></a><a name="p2233mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.4.1.2"><p id="p2235mcpsimp"><a name="p2235mcpsimp"></a><a name="p2235mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2237mcpsimp"><a name="p2237mcpsimp"></a><a name="p2237mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2239mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p2241mcpsimp"><a name="p2241mcpsimp"></a><a name="p2241mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p2243mcpsimp"><a name="p2243mcpsimp"></a><a name="p2243mcpsimp"></a>fusion设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2245mcpsimp"><a name="p2245mcpsimp"></a><a name="p2245mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2246mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p2248mcpsimp"><a name="p2248mcpsimp"></a><a name="p2248mcpsimp"></a>mfusion_attr</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.4.1.2 "><p id="p2250mcpsimp"><a name="p2250mcpsimp"></a><a name="p2250mcpsimp"></a>motionfusion属性指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2252mcpsimp"><a name="p2252mcpsimp"></a><a name="p2252mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2254mcpsimp"></a>
<table><thead align="left"><tr id="row2259mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2261mcpsimp"><a name="p2261mcpsimp"></a><a name="p2261mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2263mcpsimp"><a name="p2263mcpsimp"></a><a name="p2263mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2265mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2267mcpsimp"><a name="p2267mcpsimp"></a><a name="p2267mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2269mcpsimp"><a name="p2269mcpsimp"></a><a name="p2269mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2270mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2272mcpsimp"><a name="p2272mcpsimp"></a><a name="p2272mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2274mcpsimp"><a name="p2274mcpsimp"></a><a name="p2274mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

暂时不支持磁力计属性的设置。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_get\_attr<a name="ZH-CN_TOPIC_0000002408102330"></a>

【描述】

获取motionfusion属性。

【语法】

```
td_s32 ss_mpi_mfusion_get_attr(const td_u32 fusion_id, ot_mfusion_attr *mfusion_attr);
```

【参数】

<a name="table2293mcpsimp"></a>
<table><thead align="left"><tr id="row2299mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2301mcpsimp"><a name="p2301mcpsimp"></a><a name="p2301mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p2303mcpsimp"><a name="p2303mcpsimp"></a><a name="p2303mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2305mcpsimp"><a name="p2305mcpsimp"></a><a name="p2305mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2307mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2309mcpsimp"><a name="p2309mcpsimp"></a><a name="p2309mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2311mcpsimp"><a name="p2311mcpsimp"></a><a name="p2311mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2313mcpsimp"><a name="p2313mcpsimp"></a><a name="p2313mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2314mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p2316mcpsimp"><a name="p2316mcpsimp"></a><a name="p2316mcpsimp"></a>mfusion_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2318mcpsimp"><a name="p2318mcpsimp"></a><a name="p2318mcpsimp"></a>motionfusion属性指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2320mcpsimp"><a name="p2320mcpsimp"></a><a name="p2320mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2322mcpsimp"></a>
<table><thead align="left"><tr id="row2327mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2329mcpsimp"><a name="p2329mcpsimp"></a><a name="p2329mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2331mcpsimp"><a name="p2331mcpsimp"></a><a name="p2331mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2333mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2335mcpsimp"><a name="p2335mcpsimp"></a><a name="p2335mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2337mcpsimp"><a name="p2337mcpsimp"></a><a name="p2337mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2338mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2340mcpsimp"><a name="p2340mcpsimp"></a><a name="p2340mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2274mcpsimp"><a name="p2274mcpsimp"></a><a name="p2274mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

无。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_set\_gyro\_drift<a name="ZH-CN_TOPIC_0000002408102362"></a>

【描述】

设置Gyro零偏。

【语法】

```
td_s32 ss_mpi_mfusion_set_gyro_drift(const td_u32 fusion_id, const ot_mfusion_drift *gyro_drift);
```

【参数】

<a name="table2362mcpsimp"></a>
<table><thead align="left"><tr id="row2368mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2370mcpsimp"><a name="p2370mcpsimp"></a><a name="p2370mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p2372mcpsimp"><a name="p2372mcpsimp"></a><a name="p2372mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2374mcpsimp"><a name="p2374mcpsimp"></a><a name="p2374mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2376mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2378mcpsimp"><a name="p2378mcpsimp"></a><a name="p2378mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2380mcpsimp"><a name="p2380mcpsimp"></a><a name="p2380mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2382mcpsimp"><a name="p2382mcpsimp"></a><a name="p2382mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2383mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p2385mcpsimp"><a name="p2385mcpsimp"></a><a name="p2385mcpsimp"></a>gyro_drift</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2387mcpsimp"><a name="p2387mcpsimp"></a><a name="p2387mcpsimp"></a>陀螺仪零偏使能开关；陀螺仪零偏参数数组，包括x、y、z三个轴向的零偏。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2389mcpsimp"><a name="p2389mcpsimp"></a><a name="p2389mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2391mcpsimp"></a>
<table><thead align="left"><tr id="row2396mcpsimp"><th class="cellrowborder" valign="top" width="45.97%" id="mcps1.1.3.1.1"><p id="p2398mcpsimp"><a name="p2398mcpsimp"></a><a name="p2398mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="54.03%" id="mcps1.1.3.1.2"><p id="p2400mcpsimp"><a name="p2400mcpsimp"></a><a name="p2400mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2402mcpsimp"><td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.1.3.1.1 "><p id="p2404mcpsimp"><a name="p2404mcpsimp"></a><a name="p2404mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.3.1.2 "><p id="p2406mcpsimp"><a name="p2406mcpsimp"></a><a name="p2406mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2407mcpsimp"><td class="cellrowborder" valign="top" width="45.97%" headers="mcps1.1.3.1.1 "><p id="p2409mcpsimp"><a name="p2409mcpsimp"></a><a name="p2409mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="54.03%" headers="mcps1.1.3.1.2 "><p id="p2411mcpsimp"><a name="p2411mcpsimp"></a><a name="p2411mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   为了保持零偏的稳定性，不受任何量程的影响。配置的零偏参数为陀螺仪原始读数零偏乘以量程的积。
-   零偏标定的过程是：在典型的工作温度下，陀螺仪设备静止，读取x、y、z三个轴向的读数，然后分别求平均值。最后把求得的平均值乘以量程，所得的积为最终的零偏。
-   设置Gyro零偏功能与设置Gyro在线零偏、设置Gyro温飘参数、设置Gyro在线温飘参数互斥，其中一种功能使能之后，其余功能将使能失败。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_get\_gyro\_drift<a name="ZH-CN_TOPIC_0000002441701377"></a>

【描述】

获取Gyro零偏。

【语法】

```
td_s32 ss_mpi_mfusion_get_gyro_drift(const td_u32 fusion_id, ot_mfusion_drift *gyro_drift);
```

【参数】

<a name="table2433mcpsimp"></a>
<table><thead align="left"><tr id="row2439mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2441mcpsimp"><a name="p2441mcpsimp"></a><a name="p2441mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.4.1.2"><p id="p2443mcpsimp"><a name="p2443mcpsimp"></a><a name="p2443mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2445mcpsimp"><a name="p2445mcpsimp"></a><a name="p2445mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2447mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2449mcpsimp"><a name="p2449mcpsimp"></a><a name="p2449mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2451mcpsimp"><a name="p2451mcpsimp"></a><a name="p2451mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2453mcpsimp"><a name="p2453mcpsimp"></a><a name="p2453mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2454mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2456mcpsimp"><a name="p2456mcpsimp"></a><a name="p2456mcpsimp"></a>drift</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.4.1.2 "><p id="p2458mcpsimp"><a name="p2458mcpsimp"></a><a name="p2458mcpsimp"></a>陀螺仪零偏使能开关指针；陀螺仪零偏参数数组，包括x、y、z三个轴向的零偏。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2460mcpsimp"><a name="p2460mcpsimp"></a><a name="p2460mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2462mcpsimp"></a>
<table><thead align="left"><tr id="row2467mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2469mcpsimp"><a name="p2469mcpsimp"></a><a name="p2469mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2471mcpsimp"><a name="p2471mcpsimp"></a><a name="p2471mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2473mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2475mcpsimp"><a name="p2475mcpsimp"></a><a name="p2475mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2477mcpsimp"><a name="p2477mcpsimp"></a><a name="p2477mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2478mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2480mcpsimp"><a name="p2480mcpsimp"></a><a name="p2480mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2482mcpsimp"><a name="p2482mcpsimp"></a><a name="p2482mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

无。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_set\_gyro\_six\_side\_calibration<a name="ZH-CN_TOPIC_0000002441701473"></a>

【描述】

设置Gyro六面标定

【语法】

```
td_s32 ss_mpi_mfusion_set_gyro_six_side_calibration(const td_u32 fusion_id, const ot_mfusion_six_side_calibration *six_side_calibration);
```

【参数】

<a name="table2502mcpsimp"></a>
<table><thead align="left"><tr id="row2508mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2510mcpsimp"><a name="p2510mcpsimp"></a><a name="p2510mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.4.1.2"><p id="p2512mcpsimp"><a name="p2512mcpsimp"></a><a name="p2512mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2514mcpsimp"><a name="p2514mcpsimp"></a><a name="p2514mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2516mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2518mcpsimp"><a name="p2518mcpsimp"></a><a name="p2518mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p2520mcpsimp"><a name="p2520mcpsimp"></a><a name="p2520mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2522mcpsimp"><a name="p2522mcpsimp"></a><a name="p2522mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2523mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p2525mcpsimp"><a name="p2525mcpsimp"></a><a name="p2525mcpsimp"></a>six_side_calibration</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p2527mcpsimp"><a name="p2527mcpsimp"></a><a name="p2527mcpsimp"></a>陀螺仪六面标定使能开关；陀螺仪六面标定矩阵数组。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2529mcpsimp"><a name="p2529mcpsimp"></a><a name="p2529mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2531mcpsimp"></a>
<table><thead align="left"><tr id="row2536mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2538mcpsimp"><a name="p2538mcpsimp"></a><a name="p2538mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2540mcpsimp"><a name="p2540mcpsimp"></a><a name="p2540mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2542mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2544mcpsimp"><a name="p2544mcpsimp"></a><a name="p2544mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2546mcpsimp"><a name="p2546mcpsimp"></a><a name="p2546mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2547mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2549mcpsimp"><a name="p2549mcpsimp"></a><a name="p2549mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2551mcpsimp"><a name="p2551mcpsimp"></a><a name="p2551mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

六面标定矩阵系数的小数精度为15bit，即原始矩阵系数乘以\(1 <<15\)。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_get\_gyro\_six\_side\_calibration<a name="ZH-CN_TOPIC_0000002408262182"></a>

【描述】

获取Gyro六面标定。

【语法】

```
td_s32 ss_mpi_mfusion_get_gyro_six_side_calibration (const td_u32 fusion_id, ot_mfusion_six_side_calibration *six_side_calibration);
```

【参数】

<a name="table2571mcpsimp"></a>
<table><thead align="left"><tr id="row2577mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2579mcpsimp"><a name="p2579mcpsimp"></a><a name="p2579mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.4.1.2"><p id="p2581mcpsimp"><a name="p2581mcpsimp"></a><a name="p2581mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2583mcpsimp"><a name="p2583mcpsimp"></a><a name="p2583mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2585mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2587mcpsimp"><a name="p2587mcpsimp"></a><a name="p2587mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p2589mcpsimp"><a name="p2589mcpsimp"></a><a name="p2589mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2591mcpsimp"><a name="p2591mcpsimp"></a><a name="p2591mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2592mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p2594mcpsimp"><a name="p2594mcpsimp"></a><a name="p2594mcpsimp"></a>six_side_calibration</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p2596mcpsimp"><a name="p2596mcpsimp"></a><a name="p2596mcpsimp"></a>陀螺仪六面标定使能开关指针；陀螺仪六面标定矩阵数组。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2598mcpsimp"><a name="p2598mcpsimp"></a><a name="p2598mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2600mcpsimp"></a>
<table><thead align="left"><tr id="row2605mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2607mcpsimp"><a name="p2607mcpsimp"></a><a name="p2607mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2609mcpsimp"><a name="p2609mcpsimp"></a><a name="p2609mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2611mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2613mcpsimp"><a name="p2613mcpsimp"></a><a name="p2613mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2615mcpsimp"><a name="p2615mcpsimp"></a><a name="p2615mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2616mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2618mcpsimp"><a name="p2618mcpsimp"></a><a name="p2618mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2620mcpsimp"><a name="p2620mcpsimp"></a><a name="p2620mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

六面标定矩阵系数的小数精度为15bit，即原始矩阵系数乘以\(1 <<15\)。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_set\_gyro\_temperature\_drift<a name="ZH-CN_TOPIC_0000002408262230"></a>

【描述】

设置Gyro温飘参数。

【语法】

```
td_s32 ss_mpi_mfusion_set_gyro_temperature_drift (const td_u32 fusion_id, const ot_mfusion_temperature_drift *temperature_drift);
```

【参数】

<a name="table2640mcpsimp"></a>
<table><thead align="left"><tr id="row2646mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.1"><p id="p2648mcpsimp"><a name="p2648mcpsimp"></a><a name="p2648mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p2650mcpsimp"><a name="p2650mcpsimp"></a><a name="p2650mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2652mcpsimp"><a name="p2652mcpsimp"></a><a name="p2652mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2654mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p2656mcpsimp"><a name="p2656mcpsimp"></a><a name="p2656mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p2658mcpsimp"><a name="p2658mcpsimp"></a><a name="p2658mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2660mcpsimp"><a name="p2660mcpsimp"></a><a name="p2660mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2661mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p2663mcpsimp"><a name="p2663mcpsimp"></a><a name="p2663mcpsimp"></a>temperature_drift</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p2665mcpsimp"><a name="p2665mcpsimp"></a><a name="p2665mcpsimp"></a>陀螺仪温度漂移使能开关；陀螺仪温度漂移参数指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2667mcpsimp"><a name="p2667mcpsimp"></a><a name="p2667mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2669mcpsimp"></a>
<table><thead align="left"><tr id="row2674mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2676mcpsimp"><a name="p2676mcpsimp"></a><a name="p2676mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2678mcpsimp"><a name="p2678mcpsimp"></a><a name="p2678mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2680mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2682mcpsimp"><a name="p2682mcpsimp"></a><a name="p2682mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2684mcpsimp"><a name="p2684mcpsimp"></a><a name="p2684mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2685mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2687mcpsimp"><a name="p2687mcpsimp"></a><a name="p2687mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2689mcpsimp"><a name="p2689mcpsimp"></a><a name="p2689mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   温度漂移包含各个温度下的零偏。
-   陀螺仪温度漂移参数有两种类型，一种是多项式曲线，一种是LUT查找表。
-   设置Gyro温飘参数功能与设置Gyro在线温飘参数、设置Gyro零偏、Gyro在线零偏互斥，其中一种功能使能之后，其余功能将使能失败。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_get\_gyro\_temperature\_drift<a name="ZH-CN_TOPIC_0000002441701449"></a>

【描述】

获取Gyro温飘参数。

【语法】

```
td_s32 ss_mpi_mfusion_get_gyro_temperature_drift (const td_u32 fusion_id, ot_mfusion_temperature_drift *temperature_drift);
```

【参数】

<a name="table2711mcpsimp"></a>
<table><thead align="left"><tr id="row2717mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2719mcpsimp"><a name="p2719mcpsimp"></a><a name="p2719mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.4.1.2"><p id="p2721mcpsimp"><a name="p2721mcpsimp"></a><a name="p2721mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2723mcpsimp"><a name="p2723mcpsimp"></a><a name="p2723mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2725mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2727mcpsimp"><a name="p2727mcpsimp"></a><a name="p2727mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p2729mcpsimp"><a name="p2729mcpsimp"></a><a name="p2729mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2731mcpsimp"><a name="p2731mcpsimp"></a><a name="p2731mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2732mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2734mcpsimp"><a name="p2734mcpsimp"></a><a name="p2734mcpsimp"></a>temperature_drift</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p2736mcpsimp"><a name="p2736mcpsimp"></a><a name="p2736mcpsimp"></a>陀螺仪温度漂移使能开关指针；陀螺仪温度漂移参数指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2738mcpsimp"><a name="p2738mcpsimp"></a><a name="p2738mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2740mcpsimp"></a>
<table><thead align="left"><tr id="row2745mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2747mcpsimp"><a name="p2747mcpsimp"></a><a name="p2747mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2749mcpsimp"><a name="p2749mcpsimp"></a><a name="p2749mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2751mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2753mcpsimp"><a name="p2753mcpsimp"></a><a name="p2753mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2755mcpsimp"><a name="p2755mcpsimp"></a><a name="p2755mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2756mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2758mcpsimp"><a name="p2758mcpsimp"></a><a name="p2758mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2760mcpsimp"><a name="p2760mcpsimp"></a><a name="p2760mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   温度漂移包含各个温度下的零偏。
-   陀螺仪温度漂移参数有两种类型，一种是多项式曲线，一种是LUT查找表。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_set\_gyro\_online\_temperature\_drift<a name="ZH-CN_TOPIC_0000002441661621"></a>

【描述】

设置Gyro在线温飘参数。

【语法】

```
td_s32 ss_mpi_mfusion_set_gyro_online_temperature_drift(const td_u32 fusion_id, const ot_mfusion_temperature_drift *temperature_drift);
```

【参数】

<a name="table2782mcpsimp"></a>
<table><thead align="left"><tr id="row2788mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.4.1.1"><p id="p2790mcpsimp"><a name="p2790mcpsimp"></a><a name="p2790mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.1.4.1.2"><p id="p2792mcpsimp"><a name="p2792mcpsimp"></a><a name="p2792mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p2794mcpsimp"><a name="p2794mcpsimp"></a><a name="p2794mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2796mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p2798mcpsimp"><a name="p2798mcpsimp"></a><a name="p2798mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.4.1.2 "><p id="p2800mcpsimp"><a name="p2800mcpsimp"></a><a name="p2800mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2802mcpsimp"><a name="p2802mcpsimp"></a><a name="p2802mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2803mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p2805mcpsimp"><a name="p2805mcpsimp"></a><a name="p2805mcpsimp"></a>temp_drift</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.4.1.2 "><p id="p2807mcpsimp"><a name="p2807mcpsimp"></a><a name="p2807mcpsimp"></a>陀螺仪在线温度漂移使能开关；陀螺仪温度漂移参数指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p2809mcpsimp"><a name="p2809mcpsimp"></a><a name="p2809mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2811mcpsimp"></a>
<table><thead align="left"><tr id="row2816mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2818mcpsimp"><a name="p2818mcpsimp"></a><a name="p2818mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2820mcpsimp"><a name="p2820mcpsimp"></a><a name="p2820mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2822mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2824mcpsimp"><a name="p2824mcpsimp"></a><a name="p2824mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2826mcpsimp"><a name="p2826mcpsimp"></a><a name="p2826mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2827mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2829mcpsimp"><a name="p2829mcpsimp"></a><a name="p2829mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2831mcpsimp"><a name="p2831mcpsimp"></a><a name="p2831mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   陀螺仪在线温飘功能开启时，需要通过temperature\_drift设置上一次保存的在线温飘参数。
-   陀螺仪在线温飘功能开启后，后台会自动进行在线温飘标定，与防抖业务是否开启无关。
-   系统退出前，陀螺仪在线温飘功能需要保持关闭状态，使相关资源得到释放，并使用[ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift](#ZH-CN_TOPIC_0000002441701513)保存最新的温飘参数。以便下次启动时使用。
-   DV模式，采用陀螺仪在线温飘功能。
-   设置Gyro在线温飘参数功能与设置Gyro温飘参数、设置Gyro零偏、设置Gyro在线零偏互斥，其中一种功能使能之后，其余功能将使能失败。

【举例】

无

【相关主题】

[ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift](#ss_mpi_mfusion_get_gyro_online_temperature_drift)

## ss\_mpi\_mfusion\_get\_gyro\_online\_temperature\_drift<a name="ZH-CN_TOPIC_0000002441701513"></a>

【描述】

获取Gyro在线温飘参数。

【语法】

```
td_s32 ss_mpi_mfusion_get_gyro_online_temperature_drift(const td_u32 fusion_id, ot_mfusion_temperature_drift *temperature_drift);
```

【参数】

<a name="table109mcpsimp"></a>
<table><thead align="left"><tr id="row115mcpsimp"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.4.1.1"><p id="p117mcpsimp"><a name="p117mcpsimp"></a><a name="p117mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.4.1.2"><p id="p119mcpsimp"><a name="p119mcpsimp"></a><a name="p119mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p121mcpsimp"><a name="p121mcpsimp"></a><a name="p121mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row123mcpsimp"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.4.1.1 "><p id="p125mcpsimp"><a name="p125mcpsimp"></a><a name="p125mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p127mcpsimp"><a name="p127mcpsimp"></a><a name="p127mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p129mcpsimp"><a name="p129mcpsimp"></a><a name="p129mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row130mcpsimp"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.4.1.1 "><p id="p132mcpsimp"><a name="p132mcpsimp"></a><a name="p132mcpsimp"></a>temperature_drift</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.4.1.2 "><p id="p134mcpsimp"><a name="p134mcpsimp"></a><a name="p134mcpsimp"></a>陀螺仪在线温度漂移使能开关；陀螺仪温度漂移参数指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p136mcpsimp"><a name="p136mcpsimp"></a><a name="p136mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table138mcpsimp"></a>
<table><thead align="left"><tr id="row143mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p145mcpsimp"><a name="p145mcpsimp"></a><a name="p145mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p147mcpsimp"><a name="p147mcpsimp"></a><a name="p147mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row149mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p151mcpsimp"><a name="p151mcpsimp"></a><a name="p151mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p153mcpsimp"><a name="p153mcpsimp"></a><a name="p153mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row154mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p156mcpsimp"><a name="p156mcpsimp"></a><a name="p156mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p158mcpsimp"><a name="p158mcpsimp"></a><a name="p158mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

无

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_set\_gyro\_online\_drift<a name="ZH-CN_TOPIC_0000002408102190"></a>

【描述】

设置Gyro在线零偏。

【语法】

```
td_s32 ss_mpi_mfusion_set_gyro_online_drift(const td_u32 fusion_id, const ot_mfusion_drift *online_drift);
```

【参数】

<a name="table178mcpsimp"></a>
<table><thead align="left"><tr id="row184mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p186mcpsimp"><a name="p186mcpsimp"></a><a name="p186mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.4.1.2"><p id="p188mcpsimp"><a name="p188mcpsimp"></a><a name="p188mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p190mcpsimp"><a name="p190mcpsimp"></a><a name="p190mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row192mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p194mcpsimp"><a name="p194mcpsimp"></a><a name="p194mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row199mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a>online_<span xml:lang="en-US" id="ph202mcpsimp"><a name="ph202mcpsimp"></a><a name="ph202mcpsimp"></a>drift</span></p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.4.1.2 "><p id="p204mcpsimp"><a name="p204mcpsimp"></a><a name="p204mcpsimp"></a>陀螺仪在线零偏使能开关；零偏参数数组，包括x、y、z三个轴向的零偏。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p206mcpsimp"><a name="p206mcpsimp"></a><a name="p206mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table208mcpsimp"></a>
<table><thead align="left"><tr id="row213mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p215mcpsimp"><a name="p215mcpsimp"></a><a name="p215mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p217mcpsimp"><a name="p217mcpsimp"></a><a name="p217mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row219mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p221mcpsimp"><a name="p221mcpsimp"></a><a name="p221mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p223mcpsimp"><a name="p223mcpsimp"></a><a name="p223mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row224mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p226mcpsimp"><a name="p226mcpsimp"></a><a name="p226mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p228mcpsimp"><a name="p228mcpsimp"></a><a name="p228mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   陀螺仪在线零偏开启后，后台会自动进行在线标定，与防抖业务是否开启无关。
-   陀螺仪在线零偏功能在系统退出前保持关闭状态，使相关资源得到释放。
-   _录像机_产品，并且镜头是固定模式，采用陀螺仪在线零偏功能。
-   陀螺仪在线零偏功能需要在系统启动时的前3秒内保持陀螺仪静止，从而获得陀螺仪的基础零偏值，让零偏校准更快收敛。
-   设置Gyro在线零偏功能与设置Gyro零偏、设置Gyro温飘参数、设置Gyro在线温飘参数互斥，其中一种功能使能之后，其余功能将使能失败。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_get\_gyro\_online\_drift<a name="ZH-CN_TOPIC_0000002408102286"></a>

【描述】

获取Gyro在线零偏。

【语法】

```
td_s32 ss_mpi_mfusion_get_gyro_online_drift(const td_u32 fusion_id, ot_mfusion_drift *online_drift);
```

【参数】

<a name="table253mcpsimp"></a>
<table><thead align="left"><tr id="row259mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.1"><p id="p261mcpsimp"><a name="p261mcpsimp"></a><a name="p261mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p263mcpsimp"><a name="p263mcpsimp"></a><a name="p263mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p265mcpsimp"><a name="p265mcpsimp"></a><a name="p265mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row267mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p269mcpsimp"><a name="p269mcpsimp"></a><a name="p269mcpsimp"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p271mcpsimp"><a name="p271mcpsimp"></a><a name="p271mcpsimp"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p273mcpsimp"><a name="p273mcpsimp"></a><a name="p273mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row274mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p276mcpsimp"><a name="p276mcpsimp"></a><a name="p276mcpsimp"></a>online_drift</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p278mcpsimp"><a name="p278mcpsimp"></a><a name="p278mcpsimp"></a>陀螺仪在线零偏使能开关指针；零偏参数数组，包括x、y、z三个轴向的零偏。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p280mcpsimp"><a name="p280mcpsimp"></a><a name="p280mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table282mcpsimp"></a>
<table><thead align="left"><tr id="row287mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p289mcpsimp"><a name="p289mcpsimp"></a><a name="p289mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p291mcpsimp"><a name="p291mcpsimp"></a><a name="p291mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row293mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p295mcpsimp"><a name="p295mcpsimp"></a><a name="p295mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p297mcpsimp"><a name="p297mcpsimp"></a><a name="p297mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row298mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p300mcpsimp"><a name="p300mcpsimp"></a><a name="p300mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p302mcpsimp"><a name="p302mcpsimp"></a><a name="p302mcpsimp"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

无。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_bind\_vi<a name="ZH-CN_TOPIC_0000002408262258"></a>

【描述】

绑定fusion和pipe、chn。

【语法】

```
td_s32 ss_mpi_mfusion_bind_vi(const td_u32 fusion_id, ot_vi_pipe vi_pipe, ot_vi_chn vi_chn);
```

【参数】

<a name="table1013215531107"></a>
<table><thead align="left"><tr id="row14132145381014"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.1"><p id="p813214538105"><a name="p813214538105"></a><a name="p813214538105"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p513255351016"><a name="p513255351016"></a><a name="p513255351016"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p16132155341013"><a name="p16132155341013"></a><a name="p16132155341013"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1613210537106"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p313295361014"><a name="p313295361014"></a><a name="p313295361014"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p18132953111012"><a name="p18132953111012"></a><a name="p18132953111012"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p18132953171015"><a name="p18132953171015"></a><a name="p18132953171015"></a>输入</p>
</td>
</tr>
<tr id="row14132105314109"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p1013265321012"><a name="p1013265321012"></a><a name="p1013265321012"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p8238mcpsimp"><a name="p8238mcpsimp"></a><a name="p8238mcpsimp"></a>PIPE号。取值范围：[0, OT_VI_MAX_PIPE_NUM)，参考《MPP 媒体处理软件 V5.0 开发参考》“视频输入”章节。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p141331853181016"><a name="p141331853181016"></a><a name="p141331853181016"></a>输入</p>
</td>
</tr>
<tr id="row5436318121418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p643611818148"><a name="p643611818148"></a><a name="p643611818148"></a>vi_chn</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p8249mcpsimp"><a name="p8249mcpsimp"></a><a name="p8249mcpsimp"></a>VI通道号。取值范围：[0, OT_VI_MAX_PHYS_CHN_NUM)，参考《MPP 媒体处理软件 V5.0 开发参考》“视频输入”章节。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p84361818161416"><a name="p84361818161416"></a><a name="p84361818161416"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1213375313105"></a>
<table><thead align="left"><tr id="row18133053191020"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2133353101013"><a name="p2133353101013"></a><a name="p2133353101013"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p813385319109"><a name="p813385319109"></a><a name="p813385319109"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row81337537100"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p613310533102"><a name="p613310533102"></a><a name="p613310533102"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p15133553131012"><a name="p15133553131012"></a><a name="p15133553131012"></a>成功。</p>
</td>
</tr>
<tr id="row413325311104"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p171331153121017"><a name="p171331153121017"></a><a name="p171331153121017"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p913335351010"><a name="p913335351010"></a><a name="p913335351010"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   只有防抖关闭的场景下，才可以调用接口进行绑定。
-   vi\_pipe销毁的时候不会清除绑定关系，更改绑定关系前需要先清除上一次的绑定关系。

【举例】

无。

【相关主题】

无。

## ss\_mpi\_mfusion\_unbind\_vi<a name="ZH-CN_TOPIC_0000002408102254"></a>

【描述】

解绑定fusion和pipe、chn。

【语法】

```
td_s32 ss_mpi_mfusion_unbind_vi(const td_u32 fusion_id, ot_vi_pipe vi_pipe, ot_vi_chn vi_chn);
```

【参数】

<a name="table20499638141820"></a>
<table><thead align="left"><tr id="row94991238121819"><th class="cellrowborder" valign="top" width="18.08%" id="mcps1.1.4.1.1"><p id="p6499173851814"><a name="p6499173851814"></a><a name="p6499173851814"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="65.92%" id="mcps1.1.4.1.2"><p id="p7499103871818"><a name="p7499103871818"></a><a name="p7499103871818"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p7499738111819"><a name="p7499738111819"></a><a name="p7499738111819"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row104990387182"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.4.1.1 "><p id="p1549914381184"><a name="p1549914381184"></a><a name="p1549914381184"></a>fusion_id</p>
</td>
<td class="cellrowborder" valign="top" width="65.92%" headers="mcps1.1.4.1.2 "><p id="p114991838201815"><a name="p114991838201815"></a><a name="p114991838201815"></a>fusion 设备ID号。取值范围：[0, 1]。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p250020389182"><a name="p250020389182"></a><a name="p250020389182"></a>输入</p>
</td>
</tr>
<tr id="row15500163818188"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.4.1.1 "><p xml:lang="sv-SE" id="p1850063818187"><a name="p1850063818187"></a><a name="p1850063818187"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" width="65.92%" headers="mcps1.1.4.1.2 "><p id="p1500738101820"><a name="p1500738101820"></a><a name="p1500738101820"></a>PIPE号。取值范围：[0, OT_VI_MAX_PIPE_NUM)，参考《MPP 媒体处理软件 V5.0 开发参考》“视频输入”章节。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p950014386181"><a name="p950014386181"></a><a name="p950014386181"></a>输入</p>
</td>
</tr>
<tr id="row050053871814"><td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.4.1.1 "><p id="p65001838141813"><a name="p65001838141813"></a><a name="p65001838141813"></a>vi_chn</p>
</td>
<td class="cellrowborder" valign="top" width="65.92%" headers="mcps1.1.4.1.2 "><p id="p13500123821811"><a name="p13500123821811"></a><a name="p13500123821811"></a>VI通道号。取值范围：[0, OT_VI_MAX_PHYS_CHN_NUM)，参考《MPP 媒体处理软件 V5.0 开发参考》“视频输入”章节。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p65001638141813"><a name="p65001638141813"></a><a name="p65001638141813"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table5500143831817"></a>
<table><thead align="left"><tr id="row9500143841811"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p20500103801810"><a name="p20500103801810"></a><a name="p20500103801810"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p250010384180"><a name="p250010384180"></a><a name="p250010384180"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row350073819183"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p75001138161811"><a name="p75001138161811"></a><a name="p75001138161811"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p155003383188"><a name="p155003383188"></a><a name="p155003383188"></a>成功。</p>
</td>
</tr>
<tr id="row55001038191815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3500153871812"><a name="p3500153871812"></a><a name="p3500153871812"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1550093851812"><a name="p1550093851812"></a><a name="p1550093851812"></a>失败，请参见<a href="#ZH-CN_TOPIC_0000002441701493">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_motionfusion.h、ss\_mpi\_motionfusion.h
-   库文件：libss\_motionfusion.a

【注意】

-   只有防抖关闭的场景下，才可以调用接口进行解绑定。
-   vi\_pipe销毁的时候不会清除绑定关系，更改绑定关系前需要先清除上一次的绑定关系。

【举例】

无。

【相关主题】

无。

# 数据类型
motionfusion模块相关数据类型定义如下：

-   [OT\_MFUSION\_MAX\_CHN\_NUM](#ZH-CN_TOPIC_0000002441661637)：定义motionfusion最大通道数。
-   [OT\_MFUSION\_AXIS\_NUM](#ZH-CN_TOPIC_0000002408102346)：定义坐标轴数。
-   [OT\_MFUSION\_MATRIX\_NUM](#ZH-CN_TOPIC_0000002441701485)：定义motionfusion设备旋转矩阵的元素个数。
-   [OT\_MFUSION\_MATRIX\_TEMPERATURE\_NUM](#ZH-CN_TOPIC_0000002408262238)：定义motionfusion设备的温飘系数矩阵的元素个数。
-   [OT\_MFUSION\_TEMPERATURE\_LUT\_SAMPLES](#ZH-CN_TOPIC_0000002441661689)：定义motionfusion设备的温飘查找表的采样个数。
-   [OT\_MFUSION\_TEMPERATURE\_GYRO](#ZH-CN_TOPIC_0000002441661577)：定义Gyro温度计的设备掩码。
-   [OT\_MFUSION\_TEMPERATURE\_ACC](#ZH-CN_TOPIC_0000002408102322)：定义ACC温度计的设备掩码。
-   [OT\_MFUSION\_TEMPERATURE\_MAGN](#ZH-CN_TOPIC_0000002408262266)：定义磁力计温度计的设备掩码。
-   [OT\_MFUSION\_TEMPERATURE\_ALL](#ZH-CN_TOPIC_0000002441701505)：定义所有温度计的设备掩码。
-   [OT\_MFUSION\_DEVICE\_GYRO](#ZH-CN_TOPIC_0000002408262274)：定义Gyro的设备掩码。
-   [OT\_MFUSION\_DEVICE\_ACC](#ZH-CN_TOPIC_0000002441661665)：定义ACC的设备掩码。
-   [OT\_MFUSION\_DEVICE\_MAGN](#ZH-CN_TOPIC_0000002441661673)：定义磁力计的设备掩码。
-   [OT\_MFUSION\_DEVICE\_ALL](#ZH-CN_TOPIC_0000002408262146)：定义所有运动测量器件的设备掩码。
-   [OT\_MFUSION\_SIXSIDE\_MATRIX\_GRADINT](#ZH-CN_TOPIC_0000002408102306)：定义六面标定矩阵元素的精度。
-   [OT\_MFUSION\_ZERO\_OFFSET\_GRADINT](#ZH-CN_TOPIC_0000002408262250)：定义零偏参数的精度。
-   [OT\_MFUSION\_TEMPERATURE\_OFFSET\_GRADINT](#ZH-CN_TOPIC_0000002441701353)：定义温飘参数的精度。
-   [OT\_MFUSION\_COMMON\_BUF\_SIZE](#ZH-CN_TOPIC_0000002441661681)：定义motionfusion采样数据大小。
-   [OT\_MFUSION\_LUT\_STATUS\_NUM](#ZH-CN_TOPIC_0000002441701397)：定义温飘查找表状态数目。
-   [ot\_mfusion\_steady\_detect\_attr](#ZH-CN_TOPIC_0000002441701533)：定义IMU噪声和静止检测灵敏度参数类型。
-   [ot\_mfusion\_attr](#ZH-CN_TOPIC_0000002441661501)：定义Motionfusion属性。
-   [ot\_mfusion\_sample\_data](#ZH-CN_TOPIC_0000002441701465)：定义Motionfusion的采样数据。
-   [ot\_mfusion\_gyro\_buf](#ZH-CN_TOPIC_0000002441661653)：定义Gyro的数据类型。
-   [ot\_mfusion\_acc\_buf](#ZH-CN_TOPIC_0000002408102370)：定义ACC的数据类型。
-   [ot\_mfusion\_temperature\_drift\_mode](#ZH-CN_TOPIC_0000002441701437)：定义温飘模式。
-   [ot\_mfusion\_temperature\_drift\_lut](#ZH-CN_TOPIC_0000002441661517)：定义温飘的查找表数据类型。
-   [ot\_mfusion\_temperature\_drift](#ZH-CN_TOPIC_0000002408102298)：定义温飘属性。
-   [ot\_mfusion\_drift](#ZH-CN_TOPIC_0000002408102230)：定义零偏属性。
-   [ot\_mfusion\_six\_side\_calibration](#ZH-CN_TOPIC_0000002408262162)：定义六面标定属性。





























## OT\_MFUSION\_MAX\_CHN\_NUM<a name="ZH-CN_TOPIC_0000002441661637"></a>

【说明】

定义motionfusion最大通道数。

【定义】

```
#define OT_MFUSION_MAX_CHN_NUM    2
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_AXIS\_NUM<a name="ZH-CN_TOPIC_0000002408102346"></a>

【说明】

定义坐标轴数。

【定义】

```
#define OT_MFUSION_AXIS_NUM         3
```

【注意事项】

无。

【相关数据类型及接口】

[ot\_mfusion\_temperature\_drift\_lut](#ot_mfusion_temperature_drift_lut)

## OT\_MFUSION\_MATRIX\_NUM<a name="ZH-CN_TOPIC_0000002441701485"></a>

【说明】

定义Motionfusion设备旋转矩阵的元素个数。

【定义】

```
#define OT_MFUSION_MATRIX_NUM       9
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_MATRIX\_TEMPERATURE\_NUM<a name="ZH-CN_TOPIC_0000002408262238"></a>

【说明】

定义motionfusion设备的温飘系数矩阵的元素个数。

【定义】

```
#define OT_MFUSION_MATRIX_TEMPERATURE_NUM  9
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_TEMPERATURE\_LUT\_SAMPLES<a name="ZH-CN_TOPIC_0000002441661689"></a>

【说明】

定义motionfusion设备的温飘查找表的采样个数。

【定义】

```
#define OT_MFUSION_TEMPERATURE_LUT_SAMPLES 30
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_TEMPERATURE\_GYRO<a name="ZH-CN_TOPIC_0000002441661577"></a>

【说明】

定义Gyro温度计的设备掩码。

【定义】

```
#define OT_MFUSION_TEMPERATURE_GYRO  0x1
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_TEMPERATURE\_ACC<a name="ZH-CN_TOPIC_0000002408102322"></a>

【说明】

定义ACC温度计的设备掩码。

【定义】

```
#define OT_MFUSION_TEMPERATURE_ACC   0x2
```

【注意事项】

暂不支持ACC的温度设置。

【相关数据类型及接口】

无。

## OT\_MFUSION\_TEMPERATURE\_MAGN<a name="ZH-CN_TOPIC_0000002408262266"></a>

【说明】

定义磁力计温度计的设备掩码。

【定义】

```
#define  OT_MFUSION_TEMPERATURE_MAGN  0x4
```

【注意事项】

暂不支持磁力计。

【相关数据类型及接口】

无。

## OT\_MFUSION\_TEMPERATURE\_ALL<a name="ZH-CN_TOPIC_0000002441701505"></a>

【说明】

定义所有温度计的设备掩码。

【定义】

```
#define OT_MFUSION_TEMPERATURE_ALL  0x7
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_DEVICE\_GYRO<a name="ZH-CN_TOPIC_0000002408262274"></a>

【说明】

定义Gyro的设备掩码。

【定义】

```
#define OT_MFUSION_DEVICE_GYRO 0x1
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_DEVICE\_ACC<a name="ZH-CN_TOPIC_0000002441661665"></a>

【说明】

定义ACC的设备掩码。

【定义】

```
#define OT_MFUSION_DEVICE_ACC   0x2
```

【注意事项】

暂不支持ACC设备。

【相关数据类型及接口】

无。

## OT\_MFUSION\_DEVICE\_MAGN<a name="ZH-CN_TOPIC_0000002441661673"></a>

【说明】

定义磁力计的设备掩码。

【定义】

```
#define OT_MFUSION_DEVICE_MAGN 0x4
```

【注意事项】

暂不支持磁力计。

【相关数据类型及接口】

无。

## OT\_MFUSION\_DEVICE\_ALL<a name="ZH-CN_TOPIC_0000002408262146"></a>

【说明】

定义所有运动测量器件的设备掩码。

【定义】

```
#define OT_MFUSION_DEVICE_ALL  0x7
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_SIXSIDE\_MATRIX\_GRADINT<a name="ZH-CN_TOPIC_0000002408102306"></a>

【说明】

定义六面标定矩阵元素的小数精度。

【定义】

```
#define OT_MFUSION_SIXSIDE_MATRIX_GRADINT  15
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_ZERO\_OFFSET\_GRADINT<a name="ZH-CN_TOPIC_0000002408262250"></a>

【说明】

定义零偏参数的小数精度。

【定义】

```
#define OT_MFUSION_ZERO_OFFSET_GRADINT  15
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_TEMPERATURE\_OFFSET\_GRADINT<a name="ZH-CN_TOPIC_0000002441701353"></a>

【说明】

定义温飘参数的小数精度。

【定义】

```
#define OT_MFUSION_TEMPERATURE_OFFSET_GRADINT  15
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_COMMON\_BUF\_SIZE<a name="ZH-CN_TOPIC_0000002441661681"></a>

【说明】

定义motionfusion采样数据大小。

【定义】

```
#define OT_MFUSION_COMMON_BUF_SIZE  128
```

【注意事项】

无。

【相关数据类型及接口】

无。

## OT\_MFUSION\_LUT\_STATUS\_NUM<a name="ZH-CN_TOPIC_0000002441701397"></a>

【说明】

定义温飘查找表状态数目。

【定义】

```
#define OT_MFUSION_LUT_STATUS_NUM   2
```

【注意事项】

无。

【相关数据类型及接口】

无。

## ot\_mfusion\_steady\_detect\_attr<a name="ZH-CN_TOPIC_0000002441701533"></a>

【说明】

定义IMU噪声和静止检测灵敏度参数类型。

【定义】

```
typedef struct {
    td_u32 steady_time_thr;
    td_s32 gyro_offset;
    td_s32 acc_offset;
    td_s32 gyro_rms;
    td_s32 acc_rms;
    td_s32 gyro_offset_factor;
    td_s32 acc_offset_factor;
    td_s32 gyro_rms_factor;
    td_s32 acc_rms_factor;
} ot_mfusion_steady_detect_attr;<a name="ot_mfusion_steady_detect_attr"></a>
```

【成员】

<a name="table596mcpsimp"></a>
<table><thead align="left"><tr id="row601mcpsimp"><th class="cellrowborder" valign="top" width="42%" id="mcps1.1.3.1.1"><p id="p603mcpsimp"><a name="p603mcpsimp"></a><a name="p603mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.1.3.1.2"><p id="p605mcpsimp"><a name="p605mcpsimp"></a><a name="p605mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row607mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p609mcpsimp"><a name="p609mcpsimp"></a><a name="p609mcpsimp"></a>steady_time_thr</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p611mcpsimp"><a name="p611mcpsimp"></a><a name="p611mcpsimp"></a>静止状态时间阈值，单位为秒。连续检测到超过此配置时长的静止状态才启动在线温飘标定。</p>
<p xml:lang="sv-SE" id="p612mcpsimp"><a name="p612mcpsimp"></a><a name="p612mcpsimp"></a>范围: [0, (1&lt;&lt;16)-1]</p>
<p xml:lang="sv-SE" id="p613mcpsimp"><a name="p613mcpsimp"></a><a name="p613mcpsimp"></a>缺省值：3（<em id="i614mcpsimp"><a name="i614mcpsimp"></a><a name="i614mcpsimp"></a>录像机</em>）或1（DV）</p>
</td>
</tr>
<tr id="row615mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p617mcpsimp"><a name="p617mcpsimp"></a><a name="p617mcpsimp"></a>gyro_offset</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p619mcpsimp"><a name="p619mcpsimp"></a><a name="p619mcpsimp"></a>GYRO零偏典型值（取绝对值，为正数），从数据手册中获取（Max value of Initial ZRO Tolerance）, 单位为dps (degree per second), 精度同GYRO数据精度，即ADC WORD LENGTH -1。</p>
<p xml:lang="sv-SE" id="p620mcpsimp"><a name="p620mcpsimp"></a><a name="p620mcpsimp"></a>范围: [0, 100 * (1&lt;&lt;15)]</p>
<p xml:lang="sv-SE" id="p621mcpsimp"><a name="p621mcpsimp"></a><a name="p621mcpsimp"></a>缺省值：327680</p>
</td>
</tr>
<tr id="row622mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p624mcpsimp"><a name="p624mcpsimp"></a><a name="p624mcpsimp"></a>acc_offset</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p626mcpsimp"><a name="p626mcpsimp"></a><a name="p626mcpsimp"></a>ACC零偏典型值（取绝对值，为正数），从数据手册中获取（Max value of Initial ZRO Tolerance），单位为g（一个重力加速度），精度同ACC数据精度，即ADC WORD LENGTH -1。</p>
<p xml:lang="sv-SE" id="p627mcpsimp"><a name="p627mcpsimp"></a><a name="p627mcpsimp"></a>范围: [0, 0.5 * (1&lt;&lt;15)]</p>
<p xml:lang="sv-SE" id="p628mcpsimp"><a name="p628mcpsimp"></a><a name="p628mcpsimp"></a>缺省值：3276</p>
</td>
</tr>
<tr id="row629mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p631mcpsimp"><a name="p631mcpsimp"></a><a name="p631mcpsimp"></a>gyro_rms</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p633mcpsimp"><a name="p633mcpsimp"></a><a name="p633mcpsimp"></a>GYRO在当前低通滤波带宽下的RMS噪声典型值，可从数据手册中Rate Noise Spectral Density和当前配置低通滤波带宽计算得出。单位为dps-rms, 精度同GYRO数据精度，即ADC WORD LENGTH -1。</p>
<p xml:lang="sv-SE" id="p634mcpsimp"><a name="p634mcpsimp"></a><a name="p634mcpsimp"></a>范围: [0, 0.5 * (1&lt;&lt;15)]</p>
<p xml:lang="sv-SE" id="p635mcpsimp"><a name="p635mcpsimp"></a><a name="p635mcpsimp"></a>缺省值：1769</p>
</td>
</tr>
<tr id="row636mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>acc_rms</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>ACC在当前低通滤波带宽下的RMS噪声典型值，可从数据手册中Rate Noise Spectral Density和当前配置低通滤波带宽计算得出。单位为g-rms, 精度同ACC数据精度，即ADC WORD LENGTH -1。</p>
<p xml:lang="sv-SE" id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a>范围: [0, 0.005 * (1&lt;&lt;15)]</p>
<p xml:lang="sv-SE" id="p642mcpsimp"><a name="p642mcpsimp"></a><a name="p642mcpsimp"></a>缺省值：44</p>
</td>
</tr>
<tr id="row643mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p645mcpsimp"><a name="p645mcpsimp"></a><a name="p645mcpsimp"></a>gyro_offset_factor</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p647mcpsimp"><a name="p647mcpsimp"></a><a name="p647mcpsimp"></a>静止判断使用gyro_offset的灵敏度（放大倍数），值越大，对运动越不敏感。精度为4bit。</p>
<p xml:lang="sv-SE" id="p648mcpsimp"><a name="p648mcpsimp"></a><a name="p648mcpsimp"></a>范围：[0, 1000 * (1&lt;&lt;4)]</p>
<p xml:lang="sv-SE" id="p649mcpsimp"><a name="p649mcpsimp"></a><a name="p649mcpsimp"></a>缺省值：32</p>
</td>
</tr>
<tr id="row650mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p652mcpsimp"><a name="p652mcpsimp"></a><a name="p652mcpsimp"></a>acc_offset_factor</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p654mcpsimp"><a name="p654mcpsimp"></a><a name="p654mcpsimp"></a>静止判断使用<span xml:lang="en-US" id="ph655mcpsimp"><a name="ph655mcpsimp"></a><a name="ph655mcpsimp"></a>acc_offset</span>的灵敏度（放大倍数），值越大，对运动越不敏感。精度为4bit。</p>
<p xml:lang="sv-SE" id="p656mcpsimp"><a name="p656mcpsimp"></a><a name="p656mcpsimp"></a>范围：[0, 1000 * (1&lt;&lt;4)]</p>
<p xml:lang="sv-SE" id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>缺省值：32</p>
</td>
</tr>
<tr id="row658mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p660mcpsimp"><a name="p660mcpsimp"></a><a name="p660mcpsimp"></a>gyro_rms_factor</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p662mcpsimp"><a name="p662mcpsimp"></a><a name="p662mcpsimp"></a>静止判断使用<span xml:lang="en-US" id="ph663mcpsimp"><a name="ph663mcpsimp"></a><a name="ph663mcpsimp"></a>gyro_rms</span>的灵敏度（放大倍数），值越大，对运动越不敏感。精度为4bit。</p>
<p xml:lang="sv-SE" id="p664mcpsimp"><a name="p664mcpsimp"></a><a name="p664mcpsimp"></a>范围：[0, 1000 * (1&lt;&lt;4)]</p>
<p xml:lang="sv-SE" id="p665mcpsimp"><a name="p665mcpsimp"></a><a name="p665mcpsimp"></a>缺省值：128（<em id="i666mcpsimp"><a name="i666mcpsimp"></a><a name="i666mcpsimp"></a>录像机</em>）或 200（DV）</p>
</td>
</tr>
<tr id="row667mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p669mcpsimp"><a name="p669mcpsimp"></a><a name="p669mcpsimp"></a>acc_rms_factor</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p671mcpsimp"><a name="p671mcpsimp"></a><a name="p671mcpsimp"></a>静止判断使用<span xml:lang="en-US" id="ph672mcpsimp"><a name="ph672mcpsimp"></a><a name="ph672mcpsimp"></a>acc_rms</span>的灵敏度（放大倍数），值越大，对运动越不敏感。精度为4bit。</p>
<p xml:lang="sv-SE" id="p673mcpsimp"><a name="p673mcpsimp"></a><a name="p673mcpsimp"></a>范围：[0, 1000 * (1&lt;&lt;4)]</p>
<p xml:lang="sv-SE" id="p674mcpsimp"><a name="p674mcpsimp"></a><a name="p674mcpsimp"></a>缺省值：160（<em id="i675mcpsimp"><a name="i675mcpsimp"></a><a name="i675mcpsimp"></a>录像机</em>）或1600（DV）</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

_录像机_与DV产品有不同的缺省值。该属性参数支持动态设置。

【相关数据类型及接口】

无。

## ot\_mfusion\_attr<a name="ZH-CN_TOPIC_0000002441661501"></a>

【说明】

定义motionfusion属性。

【定义】

```
typedef struct {
    td_u32 device_mask;
    td_u32 temperature_mask;
    ot_mfusion_steady_detect_attr steady_detect_attr;
} ot_mfusion_attr;
```

【成员】

<a name="table693mcpsimp"></a>
<table><thead align="left"><tr id="row698mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p700mcpsimp"><a name="p700mcpsimp"></a><a name="p700mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p702mcpsimp"><a name="p702mcpsimp"></a><a name="p702mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row704mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p706mcpsimp"><a name="p706mcpsimp"></a><a name="p706mcpsimp"></a>device_mask</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p708mcpsimp"><a name="p708mcpsimp"></a><a name="p708mcpsimp"></a>设备属性掩码。包括Gyro和ACC设备。</p>
</td>
</tr>
<tr id="row709mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p711mcpsimp"><a name="p711mcpsimp"></a><a name="p711mcpsimp"></a>temperature_mask</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p713mcpsimp"><a name="p713mcpsimp"></a><a name="p713mcpsimp"></a>温度计掩码。包括陀螺仪温度计和ACC温度计。</p>
</td>
</tr>
<tr id="row714mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p716mcpsimp"><a name="p716mcpsimp"></a><a name="p716mcpsimp"></a>steady_detect_attr</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p718mcpsimp"><a name="p718mcpsimp"></a><a name="p718mcpsimp"></a><span xml:lang="en-US" id="ph719mcpsimp"><a name="ph719mcpsimp"></a><a name="ph719mcpsimp"></a>IMU</span>噪声和静止检测灵敏度参数。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

无。

## ot\_mfusion\_sample\_data<a name="ZH-CN_TOPIC_0000002441701465"></a>

【说明】

定义motionfusion的采样数据。

【定义】

```
typedef struct {
    td_s32 x;
    td_s32 y;
    td_s32 z;
    td_s32 temperature;
    td_u64 pts;
} ot_mfusion_sample_data;
```

【成员】

<a name="table738mcpsimp"></a>
<table><thead align="left"><tr id="row743mcpsimp"><th class="cellrowborder" valign="top" width="42%" id="mcps1.1.3.1.1"><p id="p745mcpsimp"><a name="p745mcpsimp"></a><a name="p745mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.1.3.1.2"><p id="p747mcpsimp"><a name="p747mcpsimp"></a><a name="p747mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row749mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p751mcpsimp"><a name="p751mcpsimp"></a><a name="p751mcpsimp"></a>x</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p753mcpsimp"><a name="p753mcpsimp"></a><a name="p753mcpsimp"></a>X轴数据。</p>
</td>
</tr>
<tr id="row754mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p756mcpsimp"><a name="p756mcpsimp"></a><a name="p756mcpsimp"></a>y</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p758mcpsimp"><a name="p758mcpsimp"></a><a name="p758mcpsimp"></a>Y轴数据。</p>
</td>
</tr>
<tr id="row759mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p761mcpsimp"><a name="p761mcpsimp"></a><a name="p761mcpsimp"></a>z</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p763mcpsimp"><a name="p763mcpsimp"></a><a name="p763mcpsimp"></a>Z轴数据。</p>
</td>
</tr>
<tr id="row764mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p id="p766mcpsimp"><a name="p766mcpsimp"></a><a name="p766mcpsimp"></a>temperature</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p768mcpsimp"><a name="p768mcpsimp"></a><a name="p768mcpsimp"></a>温度值。</p>
</td>
</tr>
<tr id="row769mcpsimp"><td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p771mcpsimp"><a name="p771mcpsimp"></a><a name="p771mcpsimp"></a>pts</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p773mcpsimp"><a name="p773mcpsimp"></a><a name="p773mcpsimp"></a>显示时间戳。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

无。

## ot\_mfusion\_gyro\_buf<a name="ZH-CN_TOPIC_0000002441661653"></a>

【说明】

定义Gyro的数据类型。

【定义】

```
typedef struct {
    ot_mfusion_sample_data gyro_data[OT_MFUSION_COMMON_BUF_SIZE];
    td_u32 buf_data_num;
    td_u32 buf_rep_num;
} ot_mfusion_gyro_buf;
```

【成员】

<a name="table791mcpsimp"></a>
<table><thead align="left"><tr id="row796mcpsimp"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p798mcpsimp"><a name="p798mcpsimp"></a><a name="p798mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p800mcpsimp"><a name="p800mcpsimp"></a><a name="p800mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row802mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p804mcpsimp"><a name="p804mcpsimp"></a><a name="p804mcpsimp"></a>gyro_data</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p806mcpsimp"><a name="p806mcpsimp"></a><a name="p806mcpsimp"></a><span xml:lang="de-DE" id="ph807mcpsimp"><a name="ph807mcpsimp"></a><a name="ph807mcpsimp"></a>Gyro数据数组。数组最大为</span>OT_MFUSION_COMMON_BUF_SIZE</p>
</td>
</tr>
<tr id="row809mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p811mcpsimp"><a name="p811mcpsimp"></a><a name="p811mcpsimp"></a>buf_data_num</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p813mcpsimp"><a name="p813mcpsimp"></a><a name="p813mcpsimp"></a>Gyro数据数组有效个数。</p>
</td>
</tr>
<tr id="row814mcpsimp"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p816mcpsimp"><a name="p816mcpsimp"></a><a name="p816mcpsimp"></a>buf_rep_num</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p818mcpsimp"><a name="p818mcpsimp"></a><a name="p818mcpsimp"></a>pts重叠的数据个数。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [OT\_MFUSION\_COMMON\_BUF\_SIZE](#OT_MFUSION_COMMON_BUF_SIZE)
-   [ot\_mfusion\_sample\_data](#ot_mfusion_sample_data)

## ot\_mfusion\_acc\_buf<a name="ZH-CN_TOPIC_0000002408102370"></a>

【说明】

定义ACC的数据类型。

【定义】

```
typedef struct {
    ot_mfusion_sample_data acc_data[OT_MFUSION_COMMON_BUF_SIZE];
    td_u32 buf_data_num;
    td_u32 buf_rep_num;
} ot_mfusion_acc_buf;
```

【成员】

<a name="table840mcpsimp"></a>
<table><thead align="left"><tr id="row845mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p847mcpsimp"><a name="p847mcpsimp"></a><a name="p847mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p849mcpsimp"><a name="p849mcpsimp"></a><a name="p849mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row851mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p853mcpsimp"><a name="p853mcpsimp"></a><a name="p853mcpsimp"></a>acc_data</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p855mcpsimp"><a name="p855mcpsimp"></a><a name="p855mcpsimp"></a><span xml:lang="de-DE" id="ph856mcpsimp"><a name="ph856mcpsimp"></a><a name="ph856mcpsimp"></a>ACC数据数组。数组最大为</span>OT_MFUSION_COMMON_BUF_SIZE</p>
</td>
</tr>
<tr id="row858mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p860mcpsimp"><a name="p860mcpsimp"></a><a name="p860mcpsimp"></a>buf_data_num</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p862mcpsimp"><a name="p862mcpsimp"></a><a name="p862mcpsimp"></a>Gyro数据数组有效个数。</p>
</td>
</tr>
<tr id="row863mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p865mcpsimp"><a name="p865mcpsimp"></a><a name="p865mcpsimp"></a>buf_data_num</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p867mcpsimp"><a name="p867mcpsimp"></a><a name="p867mcpsimp"></a>pts重叠的数据个数。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [OT\_MFUSION\_COMMON\_BUF\_SIZE](#OT_MFUSION_COMMON_BUF_SIZE)
-   [ot\_mfusion\_sample\_data](#ot_mfusion_sample_data)

## ot\_mfusion\_temperature\_drift\_mode<a name="ZH-CN_TOPIC_0000002441701437"></a>

【说明】

定义温飘模式。

【定义】

```
typedef enum {
    OT_IMU_TEMPERATURE_DRIFT_CURV = 0,
    OT_IMU_TEMPERATURE_DRIFT_LUT,
    OT_IMU_TEMPERATURE_DRIFT_BUTT
} ot_mfusion_temperature_drift_mode;
```

【成员】

<a name="table886mcpsimp"></a>
<table><thead align="left"><tr id="row891mcpsimp"><th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.1"><p id="p893mcpsimp"><a name="p893mcpsimp"></a><a name="p893mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.2"><p id="p895mcpsimp"><a name="p895mcpsimp"></a><a name="p895mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row897mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p899mcpsimp"><a name="p899mcpsimp"></a><a name="p899mcpsimp"></a><span xml:lang="en-US" id="ph900mcpsimp"><a name="ph900mcpsimp"></a><a name="ph900mcpsimp"></a>OT_</span>IMU_TEMP<span xml:lang="en-US" id="ph901mcpsimp"><a name="ph901mcpsimp"></a><a name="ph901mcpsimp"></a>ERATURE</span>_DRIFT_CURV</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p903mcpsimp"><a name="p903mcpsimp"></a><a name="p903mcpsimp"></a>温飘的多项式曲线模式。</p>
</td>
</tr>
<tr id="row904mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="sv-SE" id="p906mcpsimp"><a name="p906mcpsimp"></a><a name="p906mcpsimp"></a><span xml:lang="en-US" id="ph907mcpsimp"><a name="ph907mcpsimp"></a><a name="ph907mcpsimp"></a>OT_</span>IMU_TEMP<span xml:lang="en-US" id="ph908mcpsimp"><a name="ph908mcpsimp"></a><a name="ph908mcpsimp"></a>ERATURE</span>_DRIFT_LUT</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p910mcpsimp"><a name="p910mcpsimp"></a><a name="p910mcpsimp"></a>温飘的查找表模式。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

无。

## ot\_mfusion\_temperature\_drift\_lut<a name="ZH-CN_TOPIC_0000002441661517"></a>

【说明】

定义温飘的查找表数据类型。

```
typedef struct {
    td_s32 imu_lut[OT_MFUSION_TEMPERATURE_LUT_SAMPLES][OT_MFUSION_AXIS_NUM];
    td_s32 gyro_lut_status[OT_MFUSION_TEMPERATURE_LUT_SAMPLES][OT_MFUSION_LUT_STATUS_NUM];
    td_s32 range_min;
    td_s32 range_max;
    td_u32 step;
} ot_mfusion_temperature_drift_lut;
```

【成员】

<a name="table931mcpsimp"></a>
<table><thead align="left"><tr id="row936mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p938mcpsimp"><a name="p938mcpsimp"></a><a name="p938mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p940mcpsimp"><a name="p940mcpsimp"></a><a name="p940mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row942mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p944mcpsimp"><a name="p944mcpsimp"></a><a name="p944mcpsimp"></a>imu_lut</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p946mcpsimp"><a name="p946mcpsimp"></a><a name="p946mcpsimp"></a>设备的温飘查找表数组。每个采样点下记录x、y、z三个轴的温飘数据。</p>
</td>
</tr>
<tr id="row947mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p949mcpsimp"><a name="p949mcpsimp"></a><a name="p949mcpsimp"></a>gyro_lut_status</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p951mcpsimp"><a name="p951mcpsimp"></a><a name="p951mcpsimp"></a>温飘查找表的状态信息。</p>
</td>
</tr>
<tr id="row952mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p954mcpsimp"><a name="p954mcpsimp"></a><a name="p954mcpsimp"></a>range_min</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p956mcpsimp"><a name="p956mcpsimp"></a><a name="p956mcpsimp"></a>温飘查找表的最小温度值。</p>
</td>
</tr>
<tr id="row957mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p959mcpsimp"><a name="p959mcpsimp"></a><a name="p959mcpsimp"></a>range_max</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p961mcpsimp"><a name="p961mcpsimp"></a><a name="p961mcpsimp"></a>温飘查找表的最大温度值。</p>
</td>
</tr>
<tr id="row962mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p964mcpsimp"><a name="p964mcpsimp"></a><a name="p964mcpsimp"></a>step</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p966mcpsimp"><a name="p966mcpsimp"></a><a name="p966mcpsimp"></a>温度采样间隔。单位：1/<span xml:lang="en-US" id="ph967mcpsimp"><a name="ph967mcpsimp"></a><a name="ph967mcpsimp"></a>1024℃。</span></p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   首次初始化时，温飘查找表的状态信息需设置成INT\_MAX（0x7fffffff）。
-   系统下电前需保存结构信息到flash，下次上电时将此信息设置到系统中。

【相关数据类型及接口】

-   [OT\_MFUSION\_TEMPERATURE\_LUT\_SAMPLES](#OT_MFUSION_TEMPERATURE_LUT_SAMPLES)
-   [OT\_MFUSION\_AXIS\_NUM](#OT_MFUSION_AXIS_NUM)

## ot\_mfusion\_temperature\_drift<a name="ZH-CN_TOPIC_0000002408102298"></a>

【说明】

定义温飘属性。

【定义】

```
typedef struct {
    td_bool enable;
    ot_mfusion_temperature_drift_mode mode;
    union {
        td_s32 temperature_matrix[OT_MFUSION_MATRIX_TEMPERATURE_NUM];
        ot_mfusion_temperature_drift_lut temperature_lut;
    };
}ot_mfusion_temperature_drift;
```

【成员】

<a name="table999mcpsimp"></a>
<table><thead align="left"><tr id="row1004mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p1006mcpsimp"><a name="p1006mcpsimp"></a><a name="p1006mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p1008mcpsimp"><a name="p1008mcpsimp"></a><a name="p1008mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1010mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1012mcpsimp"><a name="p1012mcpsimp"></a><a name="p1012mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1014mcpsimp"><a name="p1014mcpsimp"></a><a name="p1014mcpsimp"></a>温飘或在线温飘使能。</p>
</td>
</tr>
<tr id="row1015mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1017mcpsimp"><a name="p1017mcpsimp"></a><a name="p1017mcpsimp"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p1019mcpsimp"><a name="p1019mcpsimp"></a><a name="p1019mcpsimp"></a><span xml:lang="en-US" id="ph1020mcpsimp"><a name="ph1020mcpsimp"></a><a name="ph1020mcpsimp"></a>温飘模式，</span>多项式系数拟合曲线模式或者查找表模式。</p>
</td>
</tr>
<tr id="row1021mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1023mcpsimp"><a name="p1023mcpsimp"></a><a name="p1023mcpsimp"></a>temperature_matrix</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p1025mcpsimp"><a name="p1025mcpsimp"></a><a name="p1025mcpsimp"></a>多项式曲线模式的系数数组。</p>
</td>
</tr>
<tr id="row1026mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1028mcpsimp"><a name="p1028mcpsimp"></a><a name="p1028mcpsimp"></a>temperature_lut</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p1030mcpsimp"><a name="p1030mcpsimp"></a><a name="p1030mcpsimp"></a>查找表结构体类型。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_mfusion\_temperature\_drift\_mode](#ot_mfusion_temperature_drift_mode)
-   [OT\_MFUSION\_MATRIX\_TEMPERATURE\_NUM](#OT_MFUSION_MATRIX_TEMPERATURE_NUM)
-   [ot\_mfusion\_temperature\_drift\_lut](#ot_mfusion_temperature_drift_lut)

## ot\_mfusion\_drift<a name="ZH-CN_TOPIC_0000002408102230"></a>

【说明】

定义零偏属性。

【定义】

```
typedef struct {
    td_bool enable;
    td_s32 drift[OT_MFUSION_AXIS_NUM];
} ot_mfusion_drift;
```

【成员】

<a name="table1054mcpsimp"></a>
<table><thead align="left"><tr id="row1059mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p1061mcpsimp"><a name="p1061mcpsimp"></a><a name="p1061mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p1063mcpsimp"><a name="p1063mcpsimp"></a><a name="p1063mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1065mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1067mcpsimp"><a name="p1067mcpsimp"></a><a name="p1067mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1069mcpsimp"><a name="p1069mcpsimp"></a><a name="p1069mcpsimp"></a>零偏或在线零偏使能。</p>
</td>
</tr>
<tr id="row1070mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1072mcpsimp"><a name="p1072mcpsimp"></a><a name="p1072mcpsimp"></a>drift</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1074mcpsimp"><a name="p1074mcpsimp"></a><a name="p1074mcpsimp"></a>零偏值<span xml:lang="sv-SE" id="ph1075mcpsimp"><a name="ph1075mcpsimp"></a><a name="ph1075mcpsimp"></a>。</span></p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

[OT\_MFUSION\_AXIS\_NUM](#OT_MFUSION_AXIS_NUM)

## ot\_mfusion\_six\_side\_calibration<a name="ZH-CN_TOPIC_0000002408262162"></a>

【说明】

定义六面标定属性。

【定义】

```
typedef struct {
    td_bool enable;
    td_s32 matrix[OT_MFUSION_MATRIX_NUM];
} ot_mfusion_six_side_calibration;
```

【成员】

<a name="table1094mcpsimp"></a>
<table><thead align="left"><tr id="row1099mcpsimp"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p1101mcpsimp"><a name="p1101mcpsimp"></a><a name="p1101mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p1103mcpsimp"><a name="p1103mcpsimp"></a><a name="p1103mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1105mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1107mcpsimp"><a name="p1107mcpsimp"></a><a name="p1107mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p1109mcpsimp"><a name="p1109mcpsimp"></a><a name="p1109mcpsimp"></a>六面标定使能。</p>
</td>
</tr>
<tr id="row1110mcpsimp"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p1112mcpsimp"><a name="p1112mcpsimp"></a><a name="p1112mcpsimp"></a>matrix</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p xml:lang="sv-SE" id="p1114mcpsimp"><a name="p1114mcpsimp"></a><a name="p1114mcpsimp"></a>六面标定值。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

[OT\_MFUSION\_MATRIX\_NUM](#OT_MFUSION_MATRIX_NUM)

# 错误码
motionfusion API错误码如下所示。

**表 1**  motionfusion API错误码

<a name="_Ref248290030"></a>
<table><thead align="left"><tr id="row2013mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p2015mcpsimp"><a name="p2015mcpsimp"></a><a name="p2015mcpsimp"></a>错误代码</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.2"><p id="p2017mcpsimp"><a name="p2017mcpsimp"></a><a name="p2017mcpsimp"></a>宏定义</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.3"><p id="p2019mcpsimp"><a name="p2019mcpsimp"></a><a name="p2019mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2021mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2023mcpsimp"><a name="p2023mcpsimp"></a><a name="p2023mcpsimp"></a>0xa038800b</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2025mcpsimp"><a name="p2025mcpsimp"></a><a name="p2025mcpsimp"></a>OT_ERR_MOTIONFUSION_NOT_CONFIG</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2027mcpsimp"><a name="p2027mcpsimp"></a><a name="p2027mcpsimp"></a>MOTIONFUSION未配置</p>
</td>
</tr>
<tr id="row2028mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2030mcpsimp"><a name="p2030mcpsimp"></a><a name="p2030mcpsimp"></a>0xa0388015</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2032mcpsimp"><a name="p2032mcpsimp"></a><a name="p2032mcpsimp"></a>OT_ERR_MOTIONFUSION_NOBUF</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2034mcpsimp"><a name="p2034mcpsimp"></a><a name="p2034mcpsimp"></a>分配BUF失败</p>
</td>
</tr>
<tr id="row2035mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2037mcpsimp"><a name="p2037mcpsimp"></a><a name="p2037mcpsimp"></a>0xa0388016</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2039mcpsimp"><a name="p2039mcpsimp"></a><a name="p2039mcpsimp"></a>OT_ERR_MOTIONFUSION_BUF_EMPTY</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2041mcpsimp"><a name="p2041mcpsimp"></a><a name="p2041mcpsimp"></a>数据缓存为空</p>
</td>
</tr>
<tr id="row2042mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2044mcpsimp"><a name="p2044mcpsimp"></a><a name="p2044mcpsimp"></a>0xa038800a</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2046mcpsimp"><a name="p2046mcpsimp"></a><a name="p2046mcpsimp"></a>OT_ERR_MOTIONFUSION_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2048mcpsimp"><a name="p2048mcpsimp"></a><a name="p2048mcpsimp"></a>空指针错误</p>
</td>
</tr>
<tr id="row2049mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2051mcpsimp"><a name="p2051mcpsimp"></a><a name="p2051mcpsimp"></a>0xa0388007</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2053mcpsimp"><a name="p2053mcpsimp"></a><a name="p2053mcpsimp"></a>OT_ERR_MOTIONFUSION_ILLEGAL_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2055mcpsimp"><a name="p2055mcpsimp"></a><a name="p2055mcpsimp"></a>MOTIONFUSION参数设置无效</p>
</td>
</tr>
<tr id="row2056mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2058mcpsimp"><a name="p2058mcpsimp"></a><a name="p2058mcpsimp"></a>0xa0388017</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2060mcpsimp"><a name="p2060mcpsimp"></a><a name="p2060mcpsimp"></a>OT_ERR_MOTIONFUSION_BUF_FULL</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2062mcpsimp"><a name="p2062mcpsimp"></a><a name="p2062mcpsimp"></a>数据缓存溢出</p>
</td>
</tr>
<tr id="row2063mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2065mcpsimp"><a name="p2065mcpsimp"></a><a name="p2065mcpsimp"></a>0xa0388018</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2067mcpsimp"><a name="p2067mcpsimp"></a><a name="p2067mcpsimp"></a>OT_ERR_MOTIONFUSION_SYS_NOTREADY</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2069mcpsimp"><a name="p2069mcpsimp"></a><a name="p2069mcpsimp"></a>系统未初始化</p>
</td>
</tr>
<tr id="row2070mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2072mcpsimp"><a name="p2072mcpsimp"></a><a name="p2072mcpsimp"></a>0xa038800c</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2074mcpsimp"><a name="p2074mcpsimp"></a><a name="p2074mcpsimp"></a>OT_ERR_MOTIONFUSION_NOT_SUPPORT</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2076mcpsimp"><a name="p2076mcpsimp"></a><a name="p2076mcpsimp"></a>操作不支持</p>
</td>
</tr>
<tr id="row2077mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2079mcpsimp"><a name="p2079mcpsimp"></a><a name="p2079mcpsimp"></a>0xa038800d</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2081mcpsimp"><a name="p2081mcpsimp"></a><a name="p2081mcpsimp"></a>OT_ERR_MOTIONFUSION_NOT_PERMITTED</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2083mcpsimp"><a name="p2083mcpsimp"></a><a name="p2083mcpsimp"></a>操作被禁止</p>
</td>
</tr>
<tr id="row2084mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2086mcpsimp"><a name="p2086mcpsimp"></a><a name="p2086mcpsimp"></a>0xa0388022</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2088mcpsimp"><a name="p2088mcpsimp"></a><a name="p2088mcpsimp"></a>OT_ERR_MOTIONFUSION_BUSY</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2090mcpsimp"><a name="p2090mcpsimp"></a><a name="p2090mcpsimp"></a>MOTIONFUSION系统忙</p>
</td>
</tr>
<tr id="row2091mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2093mcpsimp"><a name="p2093mcpsimp"></a><a name="p2093mcpsimp"></a>0xa0388003</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2095mcpsimp"><a name="p2095mcpsimp"></a><a name="p2095mcpsimp"></a>OT_ERR_MOTIONFUSION_INVALID_CHNID</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2097mcpsimp"><a name="p2097mcpsimp"></a><a name="p2097mcpsimp"></a>无效的通道ID</p>
</td>
</tr>
<tr id="row2098mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2100mcpsimp"><a name="p2100mcpsimp"></a><a name="p2100mcpsimp"></a>0xa0388009</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2102mcpsimp"><a name="p2102mcpsimp"></a><a name="p2102mcpsimp"></a>OT_ERR_MOTIONFUSION_CHN_UNEXIST</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2104mcpsimp"><a name="p2104mcpsimp"></a><a name="p2104mcpsimp"></a>通道未创建</p>
</td>
</tr>
<tr id="row2105mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2107mcpsimp"><a name="p2107mcpsimp"></a><a name="p2107mcpsimp"></a>0xa0388030</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2109mcpsimp"><a name="p2109mcpsimp"></a><a name="p2109mcpsimp"></a>OT_ERR_MOTIONFUSION_GYRO_NOTWORK</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2111mcpsimp"><a name="p2111mcpsimp"></a><a name="p2111mcpsimp"></a>陀螺仪未工作</p>
</td>
</tr>
<tr id="row2112mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2114mcpsimp"><a name="p2114mcpsimp"></a><a name="p2114mcpsimp"></a>0xa0388031</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2116mcpsimp"><a name="p2116mcpsimp"></a><a name="p2116mcpsimp"></a>OT_ERR_MOTIONFUSION_ACC_NOTWORK</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2118mcpsimp"><a name="p2118mcpsimp"></a><a name="p2118mcpsimp"></a>加速度计未工作</p>
</td>
</tr>
<tr id="row2119mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2121mcpsimp"><a name="p2121mcpsimp"></a><a name="p2121mcpsimp"></a>0xa0388032</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2123mcpsimp"><a name="p2123mcpsimp"></a><a name="p2123mcpsimp"></a>OT_ERR_MOTIONFUSION_INVALID_MODE</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2125mcpsimp"><a name="p2125mcpsimp"></a><a name="p2125mcpsimp"></a>无效的工作模式</p>
</td>
</tr>
<tr id="row2126mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p2128mcpsimp"><a name="p2128mcpsimp"></a><a name="p2128mcpsimp"></a>0xa0388033</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.2 "><p xml:lang="sv-SE" id="p2130mcpsimp"><a name="p2130mcpsimp"></a><a name="p2130mcpsimp"></a>OT_ERR_MOTIONFUSION_INVALID_USECASE</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p2132mcpsimp"><a name="p2132mcpsimp"></a><a name="p2132mcpsimp"></a>无效的使用场景</p>
</td>
</tr>
</tbody>
</table>

# Proc调试信息说明
## motionsensor proc<a name="ZH-CN_TOPIC_0000002408262126"></a>



### motionsensor\_chip proc<a name="ZH-CN_TOPIC_0000002408262222"></a>

【调试信息】

```
[motionsensor] version:[motionsensor_chip debug 0.0.0.1], build time[Aug 17 2021, 14:53:42]
--------------------------common parameter-----------------------------
 trigle_mode                  fifo_en
 TIMER                        1
------------------------------gyro parameter------------------------------
            
sample_rate  full-scale-range    datawidth     max-chip-temperature   min-chip-temperature
1000         1024000             16            85                     -40
------------------------------accelerometer parameter----------------------
            
sample_rate  full-scale-range   datawidth     max-chip-temperature     min-chip-temperature
1000         16384              16             85                      -40
```

【参数说明】

<a name="table1137mcpsimp"></a>
<table><thead align="left"><tr id="row1143mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1145mcpsimp"><a name="p1145mcpsimp"></a><a name="p1145mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1147mcpsimp"><a name="p1147mcpsimp"></a><a name="p1147mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1149mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1151mcpsimp"><a name="p1151mcpsimp"></a><a name="p1151mcpsimp"></a>common parameter</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1153mcpsimp"><a name="p1153mcpsimp"></a><a name="p1153mcpsimp"></a>trigle_mode</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1155mcpsimp"><a name="p1155mcpsimp"></a><a name="p1155mcpsimp"></a>获取陀螺仪数据的触发方式：TRIGER_TIMER：定时器触发。</p>
<p id="p1156mcpsimp"><a name="p1156mcpsimp"></a><a name="p1156mcpsimp"></a>TRIGER_EXTERN_INTERRUPT：外部中断触发。</p>
</td>
</tr>
<tr id="row1157mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1159mcpsimp"><a name="p1159mcpsimp"></a><a name="p1159mcpsimp"></a>fifo_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1161mcpsimp"><a name="p1161mcpsimp"></a><a name="p1161mcpsimp"></a>1：使用陀螺仪内部的fifo</p>
<p id="p1162mcpsimp"><a name="p1162mcpsimp"></a><a name="p1162mcpsimp"></a>0：不使用陀螺仪内部的fifo</p>
</td>
</tr>
<tr id="row1163mcpsimp"><td class="cellrowborder" rowspan="5" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1165mcpsimp"><a name="p1165mcpsimp"></a><a name="p1165mcpsimp"></a>gyro parameter</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1167mcpsimp"><a name="p1167mcpsimp"></a><a name="p1167mcpsimp"></a>sample_rate</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1169mcpsimp"><a name="p1169mcpsimp"></a><a name="p1169mcpsimp"></a>陀螺仪采样率</p>
</td>
</tr>
<tr id="row1170mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1172mcpsimp"><a name="p1172mcpsimp"></a><a name="p1172mcpsimp"></a>full-scale-range</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1174mcpsimp"><a name="p1174mcpsimp"></a><a name="p1174mcpsimp"></a>陀螺仪量程</p>
</td>
</tr>
<tr id="row1175mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1177mcpsimp"><a name="p1177mcpsimp"></a><a name="p1177mcpsimp"></a>datawidth</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1179mcpsimp"><a name="p1179mcpsimp"></a><a name="p1179mcpsimp"></a>陀螺仪数据位宽</p>
</td>
</tr>
<tr id="row1180mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1182mcpsimp"><a name="p1182mcpsimp"></a><a name="p1182mcpsimp"></a>max-chip-temperature</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1184mcpsimp"><a name="p1184mcpsimp"></a><a name="p1184mcpsimp"></a>陀螺仪芯片最大温度</p>
</td>
</tr>
<tr id="row1185mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1187mcpsimp"><a name="p1187mcpsimp"></a><a name="p1187mcpsimp"></a>min-chip-temperature</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1189mcpsimp"><a name="p1189mcpsimp"></a><a name="p1189mcpsimp"></a>陀螺仪芯片最小温度</p>
</td>
</tr>
<tr id="row1190mcpsimp"><td class="cellrowborder" rowspan="5" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1192mcpsimp"><a name="p1192mcpsimp"></a><a name="p1192mcpsimp"></a>accelerometer parameter</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1194mcpsimp"><a name="p1194mcpsimp"></a><a name="p1194mcpsimp"></a>sample_rate</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1196mcpsimp"><a name="p1196mcpsimp"></a><a name="p1196mcpsimp"></a>加速度计采样率</p>
</td>
</tr>
<tr id="row1197mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1199mcpsimp"><a name="p1199mcpsimp"></a><a name="p1199mcpsimp"></a>full-scale-range</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1201mcpsimp"><a name="p1201mcpsimp"></a><a name="p1201mcpsimp"></a>加速度计量程</p>
</td>
</tr>
<tr id="row1202mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1204mcpsimp"><a name="p1204mcpsimp"></a><a name="p1204mcpsimp"></a>datawidth</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1206mcpsimp"><a name="p1206mcpsimp"></a><a name="p1206mcpsimp"></a>加速度计数据位宽</p>
</td>
</tr>
<tr id="row1207mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1209mcpsimp"><a name="p1209mcpsimp"></a><a name="p1209mcpsimp"></a>max-chip-temperature</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1211mcpsimp"><a name="p1211mcpsimp"></a><a name="p1211mcpsimp"></a>加速度计芯片最大温度</p>
</td>
</tr>
<tr id="row1212mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1214mcpsimp"><a name="p1214mcpsimp"></a><a name="p1214mcpsimp"></a>min-chip-temperature</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1216mcpsimp"><a name="p1216mcpsimp"></a><a name="p1216mcpsimp"></a>加速度计芯片最小温度</p>
</td>
</tr>
</tbody>
</table>

### motionsensor\_mng proc<a name="ZH-CN_TOPIC_0000002441661597"></a>

【调试信息】

```
[motionsensor] version:[motionsensor_mng debug V0.0.0.1], build time[Aug 17 2021, 14:53:38]
---------------------gyro sensor name---------------------
            
---------------------gyro sensor param--------------------
            buf_addr        buf_size        overflow    data_unmatch     overflow_id data_unmatch_id
    ffffff8011a00000          999936               0               0               0               0
---------------------gyro sensor addr---------------------
                 start_addr          write_addr
         x    ffffff8011a00000    ffffff8011a014a8
         y    ffffff8011a28b00    ffffff8011a29fa8
         z    ffffff8011a51600    ffffff8011a52aa8
      temp    ffffff8011a7a100    ffffff8011a7b5a8
       pts    ffffff8011aa2c00    ffffff8011aa5550
---------------------acc sensor name---------------------
            
---------------------acc sensor param---------------------
            buf_addr        buf_size        overflow    data_unmatch     overflow_id data_unmatch_id
    ffffff8011af4200          999936               0               0               0               0
---------------------acc sensor addr---------------------
                    start_addr          write_addr
         x    ffffff8011af4200    ffffff8011af56a8
         y    ffffff8011b1cd00    ffffff8011b1e1a8
         z    ffffff8011b45800    ffffff8011b46ca8
      temp    ffffff8011b6e300    ffffff8011b6f7a8
       pts    ffffff8011b96e00    ffffff8011b99750
```

【参数说明】

<a name="table1245mcpsimp"></a>
<table><thead align="left"><tr id="row1251mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1253mcpsimp"><a name="p1253mcpsimp"></a><a name="p1253mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1255mcpsimp"><a name="p1255mcpsimp"></a><a name="p1255mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1257mcpsimp"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1259mcpsimp"><a name="p1259mcpsimp"></a><a name="p1259mcpsimp"></a>gyro sensor name</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1261mcpsimp"><a name="p1261mcpsimp"></a><a name="p1261mcpsimp"></a>gyro sensor name</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1263mcpsimp"><a name="p1263mcpsimp"></a><a name="p1263mcpsimp"></a>陀螺仪传感器名称。</p>
</td>
</tr>
<tr id="row1264mcpsimp"><td class="cellrowborder" rowspan="6" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1266mcpsimp"><a name="p1266mcpsimp"></a><a name="p1266mcpsimp"></a>gyro sensor param</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1268mcpsimp"><a name="p1268mcpsimp"></a><a name="p1268mcpsimp"></a>buf_addr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1270mcpsimp"><a name="p1270mcpsimp"></a><a name="p1270mcpsimp"></a>陀螺仪缓存数据的起始地址。</p>
</td>
</tr>
<tr id="row1271mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1273mcpsimp"><a name="p1273mcpsimp"></a><a name="p1273mcpsimp"></a>buf_size</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1275mcpsimp"><a name="p1275mcpsimp"></a><a name="p1275mcpsimp"></a>陀螺仪缓存大小。</p>
</td>
</tr>
<tr id="row1276mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1278mcpsimp"><a name="p1278mcpsimp"></a><a name="p1278mcpsimp"></a>overflow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1280mcpsimp"><a name="p1280mcpsimp"></a><a name="p1280mcpsimp"></a>陀螺仪缓存溢出次数（write指针追赶上read指针的次数）。</p>
</td>
</tr>
<tr id="row1281mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1283mcpsimp"><a name="p1283mcpsimp"></a><a name="p1283mcpsimp"></a>data_unmatch</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1285mcpsimp"><a name="p1285mcpsimp"></a><a name="p1285mcpsimp"></a>陀螺仪数据不匹配次数（根据begin_pts和end_pts从陀螺仪缓存中未获取到数据的次数）。</p>
</td>
</tr>
<tr id="row1286mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1288mcpsimp"><a name="p1288mcpsimp"></a><a name="p1288mcpsimp"></a>overflow_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1290mcpsimp"><a name="p1290mcpsimp"></a><a name="p1290mcpsimp"></a>陀螺仪缓存溢出的motionsensor用户id。</p>
</td>
</tr>
<tr id="row1291mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1293mcpsimp"><a name="p1293mcpsimp"></a><a name="p1293mcpsimp"></a>data_unmatch_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1295mcpsimp"><a name="p1295mcpsimp"></a><a name="p1295mcpsimp"></a>陀螺仪数据不匹配motionsensor用户id。</p>
</td>
</tr>
<tr id="row1296mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1298mcpsimp"><a name="p1298mcpsimp"></a><a name="p1298mcpsimp"></a>gyro sensor addr</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1300mcpsimp"><a name="p1300mcpsimp"></a><a name="p1300mcpsimp"></a>start_addr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1302mcpsimp"><a name="p1302mcpsimp"></a><a name="p1302mcpsimp"></a>陀螺仪x、y、z、temperature、pts数据在缓存中的起始地址。</p>
</td>
</tr>
<tr id="row1303mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1305mcpsimp"><a name="p1305mcpsimp"></a><a name="p1305mcpsimp"></a>write_addr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1307mcpsimp"><a name="p1307mcpsimp"></a><a name="p1307mcpsimp"></a>陀螺仪x、y、z、temperature、pts数据在缓存中的写地址。</p>
</td>
</tr>
<tr id="row1308mcpsimp"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1310mcpsimp"><a name="p1310mcpsimp"></a><a name="p1310mcpsimp"></a>acc sensor name</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1312mcpsimp"><a name="p1312mcpsimp"></a><a name="p1312mcpsimp"></a>acc sensor name</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1314mcpsimp"><a name="p1314mcpsimp"></a><a name="p1314mcpsimp"></a>加速度计传感器名称。</p>
</td>
</tr>
<tr id="row1315mcpsimp"><td class="cellrowborder" rowspan="6" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1317mcpsimp"><a name="p1317mcpsimp"></a><a name="p1317mcpsimp"></a>acc sensor param</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1319mcpsimp"><a name="p1319mcpsimp"></a><a name="p1319mcpsimp"></a>buf_addr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1321mcpsimp"><a name="p1321mcpsimp"></a><a name="p1321mcpsimp"></a>加速度计缓存数据的起始地址。</p>
</td>
</tr>
<tr id="row1322mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1324mcpsimp"><a name="p1324mcpsimp"></a><a name="p1324mcpsimp"></a>buf_size</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1326mcpsimp"><a name="p1326mcpsimp"></a><a name="p1326mcpsimp"></a>加速度计缓存大小。</p>
</td>
</tr>
<tr id="row1327mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1329mcpsimp"><a name="p1329mcpsimp"></a><a name="p1329mcpsimp"></a>overflow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1331mcpsimp"><a name="p1331mcpsimp"></a><a name="p1331mcpsimp"></a>加速度计缓存溢出次数（write指针追赶上read指针的次数）。</p>
</td>
</tr>
<tr id="row1332mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1334mcpsimp"><a name="p1334mcpsimp"></a><a name="p1334mcpsimp"></a>data_unmatch</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1336mcpsimp"><a name="p1336mcpsimp"></a><a name="p1336mcpsimp"></a>加速度计数据不匹配次数（根据begin_pts和end_pts从加速度计缓存中未获取到数据的次数）。</p>
</td>
</tr>
<tr id="row1337mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1339mcpsimp"><a name="p1339mcpsimp"></a><a name="p1339mcpsimp"></a>overflow_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1341mcpsimp"><a name="p1341mcpsimp"></a><a name="p1341mcpsimp"></a>加速度计缓存溢出的motionsensor用户id。</p>
</td>
</tr>
<tr id="row1342mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1344mcpsimp"><a name="p1344mcpsimp"></a><a name="p1344mcpsimp"></a>data_unmatch_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1346mcpsimp"><a name="p1346mcpsimp"></a><a name="p1346mcpsimp"></a>加速度计数据不匹配motionsensor用户id。</p>
</td>
</tr>
<tr id="row1347mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1349mcpsimp"><a name="p1349mcpsimp"></a><a name="p1349mcpsimp"></a>acc sensor addr</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1351mcpsimp"><a name="p1351mcpsimp"></a><a name="p1351mcpsimp"></a>start_addr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1353mcpsimp"><a name="p1353mcpsimp"></a><a name="p1353mcpsimp"></a>加速度计x、y、z、temperature、pts数据分别在缓存中的起始地址。</p>
</td>
</tr>
<tr id="row1354mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1356mcpsimp"><a name="p1356mcpsimp"></a><a name="p1356mcpsimp"></a>write_addr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1358mcpsimp"><a name="p1358mcpsimp"></a><a name="p1358mcpsimp"></a>加速度计x、y、z、temperature、pts数据分别在缓存中的写地址。</p>
</td>
</tr>
</tbody>
</table>

## motionfusion proc<a name="ZH-CN_TOPIC_0000002441661645"></a>

【调试信息】

```
[MFUSION] Version: [V1.0.0.0 B010 Release]
 
----------------------------------------motionfusion[0] public attr--------------------------------------------------------
       usecase          mode          gyro           acc          magn     temp_gyro      temp_acc     temp_magn
        normal        stable             Y             Y             N             Y             Y             N
     steady_time_thr         gyro_offset          acc_offset            gyro_rms             acc_rms
                   1              327680                3276                1769                  44
  gyro_offset_factor   acc_offset_factor     gyro_rms_factor      acc_rms_factor
                  32                  32                 200                1600
----------------------------------------motionfusion[0] gyro sixside cal status--------------------------------------------
            enable :       Y
   rotation_matrix :  -32768       0       0       0   32768       0       0       0  -32768
----------------------------------------motionfusion[0] gyro drift cal status----------------------------------------------
            enable :       N
----------------------------------------motionfusion[0] gyro online drift cal status---------------------------------------
            enable :       Y (矫正模式仅能开一种，此处仅作演示)
        gyro_drift :      36     -99      41
online_gyro_data_mean :       0       0       0
----------------------------------------motionfusion[0] gyro temp drift cal status-----------------------------------------
            enable :       N
----------------------------------------motionfusion[0] gyro online temp drift cal status----------------------------------
            enable :       Y
              mode :     lut
             param :range_min:20480, range_max:79872, step:2048
         temp_lut :
         x         y         z           time   nearest temp      temp
     -9045    -18540    -10471     2147483647     2147483647        20
     -9045    -18540    -10471     2147483647     2147483647        22
     -9045    -18540    -10471     2147483647     2147483647        24
     -9045    -18540    -10471     2147483647     2147483647        26
     -9045    -18540    -10471           1185           1140        28
     -8996    -21218    -10207           1165              1        30
     -8357    -25524    -10439           1110             36        32
     -8254    -28758    -10248            990              4        34
     -8943    -28658    -10618            645              2        36
     -9246    -27259    -10354             45           1374        38
     -9246    -27259    -10354     2147483647     2147483647        40
     -9246    -27259    -10354     2147483647     2147483647        42
     -9246    -27259    -10354     2147483647     2147483647        44
     -9246    -27259    -10354     2147483647     2147483647        46
     -9246    -27259    -10354     2147483647     2147483647        48
     -9246    -27259    -10354     2147483647     2147483647        50
     -9246    -27259    -10354     2147483647     2147483647        52
     -9246    -27259    -10354     2147483647     2147483647        54
     -9246    -27259    -10354     2147483647     2147483647        56
     -9246    -27259    -10354     2147483647     2147483647        58
     -9246    -27259    -10354     2147483647     2147483647        60
     -9246    -27259    -10354     2147483647     2147483647        62
     -9246    -27259    -10354     2147483647     2147483647        64
     -9246    -27259    -10354     2147483647     2147483647        66
     -9246    -27259    -10354     2147483647     2147483647        68
     -9246    -27259    -10354     2147483647     2147483647        70
     -9246    -27259    -10354     2147483647     2147483647        72
     -9246    -27259    -10354     2147483647     2147483647        74
     -9246    -27259    -10354     2147483647     2147483647        76
     -9246    -27259    -10354     2147483647     2147483647        78
----------------------------------------motionfusion[0] acc sixside cal status---------------------------------------------
            enable :       N
----------------------------------------motionfusion[0] acc drift cal status-----------------------------------------------
            enable :       N
----------------------------------------motionfusion[0] acc temp drift cal status------------------------------------------
            enable :       N
----------------------------------------motionfusion[0] bind status-----------------------------------------------------
        bind_valid          vi_pipe         vi_chn
                 Y                0              0
----------------------------------------motionfusion[0] drv status---------------------------------------------------------
       gyro config :    sample_rate     data_range   data_precbit  temp_data_min  temp_data_max      bit_width
                               1000        1024000             16            -40             85             16
        acc config :    sample_rate     data_range   data_precbit  temp_data_min  temp_data_max      bit_width
                               1000          16384             16            -40             85             16
       magn config :    sample_rate
                                  0
        cam status :         steady
----------------------------------------user 0 gyro_data-----------------------------------------------------------------------
begin_pts:487179113, end_pts:487213746, gyro_data num:35
         x            y            z           temp                 pts
       -30         -168          -50          28611           487179113
       -29         -168          -41          28611           487180111
       -24         -169          -32          28611           487181109
       -16         -168          -25          28611           487182107
        -8         -165          -20          28611           487183105
       -12         -167          -18          28611           487184103
       -14         -167          -22          28611           487185101
        -4         -169          -25          28611           487186099
         4         -175          -28          28611           487187097
         0         -175          -30          28611           487188095
        -6         -169          -36          28611           487189093
        -6         -166          -35          28611           487190091
         5         -172          -35          28611           487191089
        13         -176          -44          28611           487192087
        11         -170          -55          28611           487193085
        -4         -161          -55          28611           487194083
        -3         -164          -35          28611           487195081
        12         -170          -18          28611           487196081
        18         -172          -19          28611           487197081
         5         -166          -24          28611           487198081
        -4         -156          -20          28611           487199081
         2         -155          -28          28611           487200081
        10         -162          -42          28611           487201081
         7         -165          -52          28611           487202081
         0         -160          -50          28611           487203081
        -1         -159          -33          28611           487204081
         2         -163          -19          28611           487205081
        10         -162          -21          28611           487206081
         7         -164          -36          28611           487207081
         8         -168          -43          28611           487208081
        12         -170          -41          28611           487209081
         6         -173          -42          28611           487210081
        -6         -166          -45          28611           487211081
       -17         -156          -52          28611           487212081
       -23         -151          -54          28611           487213081

    x_mean       y_mean       z_mean      temp_mean       pts_step_mean
        -2         -164          -35          28611                 999

x_variance   y_variance   z_variance  temp_variance   pts_step_variance
       152           39          146              0                   1
```

【参数说明】

<a name="table1470mcpsimp"></a>
<table><thead align="left"><tr id="row1476mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1478mcpsimp"><a name="p1478mcpsimp"></a><a name="p1478mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1480mcpsimp"><a name="p1480mcpsimp"></a><a name="p1480mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1482mcpsimp"><td class="cellrowborder" rowspan="17" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1484mcpsimp"><a name="p1484mcpsimp"></a><a name="p1484mcpsimp"></a>motionfusion[0] public attr</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1486mcpsimp"><a name="p1486mcpsimp"></a><a name="p1486mcpsimp"></a>usecase</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1488mcpsimp"><a name="p1488mcpsimp"></a><a name="p1488mcpsimp"></a>使用场景：</p>
<p id="p1489mcpsimp"><a name="p1489mcpsimp"></a><a name="p1489mcpsimp"></a>normal：普通模式。</p>
<p id="p1490mcpsimp"><a name="p1490mcpsimp"></a><a name="p1490mcpsimp"></a>stitch：拼接模式（暂不支持）。</p>
</td>
</tr>
<tr id="row1491mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1493mcpsimp"><a name="p1493mcpsimp"></a><a name="p1493mcpsimp"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1495mcpsimp"><a name="p1495mcpsimp"></a><a name="p1495mcpsimp"></a>防抖模式</p>
<p id="p1496mcpsimp"><a name="p1496mcpsimp"></a><a name="p1496mcpsimp"></a>stable：运动DV模式。</p>
<p id="p1497mcpsimp"><a name="p1497mcpsimp"></a><a name="p1497mcpsimp"></a>camsteady：<em id="i1498mcpsimp"><a name="i1498mcpsimp"></a><a name="i1498mcpsimp"></a>录像机</em>模式。</p>
</td>
</tr>
<tr id="row1499mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1501mcpsimp"><a name="p1501mcpsimp"></a><a name="p1501mcpsimp"></a>gyro</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1503mcpsimp"><a name="p1503mcpsimp"></a><a name="p1503mcpsimp"></a>陀螺仪开关。</p>
</td>
</tr>
<tr id="row1504mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1506mcpsimp"><a name="p1506mcpsimp"></a><a name="p1506mcpsimp"></a>acc</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1508mcpsimp"><a name="p1508mcpsimp"></a><a name="p1508mcpsimp"></a>加速度计开关。</p>
</td>
</tr>
<tr id="row1509mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1511mcpsimp"><a name="p1511mcpsimp"></a><a name="p1511mcpsimp"></a>magn</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1513mcpsimp"><a name="p1513mcpsimp"></a><a name="p1513mcpsimp"></a>磁力计开关（暂不支持）。</p>
</td>
</tr>
<tr id="row1514mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1516mcpsimp"><a name="p1516mcpsimp"></a><a name="p1516mcpsimp"></a>temp_gyro</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1518mcpsimp"><a name="p1518mcpsimp"></a><a name="p1518mcpsimp"></a>陀螺仪温度开关。</p>
</td>
</tr>
<tr id="row1519mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1521mcpsimp"><a name="p1521mcpsimp"></a><a name="p1521mcpsimp"></a>temp_acc</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1523mcpsimp"><a name="p1523mcpsimp"></a><a name="p1523mcpsimp"></a>加速度计温度开关。</p>
</td>
</tr>
<tr id="row1524mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1526mcpsimp"><a name="p1526mcpsimp"></a><a name="p1526mcpsimp"></a>temp_magn</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1528mcpsimp"><a name="p1528mcpsimp"></a><a name="p1528mcpsimp"></a>磁力计温度开关（暂不支持）。</p>
</td>
</tr>
<tr id="row1529mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1531mcpsimp"><a name="p1531mcpsimp"></a><a name="p1531mcpsimp"></a>steady_time_thr</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1533mcpsimp"><a name="p1533mcpsimp"></a><a name="p1533mcpsimp"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1535mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1537mcpsimp"><a name="p1537mcpsimp"></a><a name="p1537mcpsimp"></a>gyro_offset</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p14671245191518"><a name="p14671245191518"></a><a name="p14671245191518"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1541mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1543mcpsimp"><a name="p1543mcpsimp"></a><a name="p1543mcpsimp"></a>acc_offset</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p34733450154"><a name="p34733450154"></a><a name="p34733450154"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1547mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1549mcpsimp"><a name="p1549mcpsimp"></a><a name="p1549mcpsimp"></a>gyro_rms</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1847894551518"><a name="p1847894551518"></a><a name="p1847894551518"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1553mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1555mcpsimp"><a name="p1555mcpsimp"></a><a name="p1555mcpsimp"></a>acc_rms</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p174831445111518"><a name="p174831445111518"></a><a name="p174831445111518"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1559mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1561mcpsimp"><a name="p1561mcpsimp"></a><a name="p1561mcpsimp"></a>gyro_offset_factor</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p14881245171513"><a name="p14881245171513"></a><a name="p14881245171513"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1565mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1567mcpsimp"><a name="p1567mcpsimp"></a><a name="p1567mcpsimp"></a>acc_offset_factor</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1249344515152"><a name="p1249344515152"></a><a name="p1249344515152"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1571mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1573mcpsimp"><a name="p1573mcpsimp"></a><a name="p1573mcpsimp"></a>gyro_rms_factor</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1849810456153"><a name="p1849810456153"></a><a name="p1849810456153"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1577mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1579mcpsimp"><a name="p1579mcpsimp"></a><a name="p1579mcpsimp"></a>acc_rms_factor</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p750212456153"><a name="p750212456153"></a><a name="p750212456153"></a>静止检测参数，参考本文档<a href="#ot_mfusion_steady_detect_attr">ot_mfusion_steady_detect_attr</a>的描述。</p>
</td>
</tr>
<tr id="row1583mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1585mcpsimp"><a name="p1585mcpsimp"></a><a name="p1585mcpsimp"></a>motionfusion[0] gyro sixside cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1587mcpsimp"><a name="p1587mcpsimp"></a><a name="p1587mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1589mcpsimp"><a name="p1589mcpsimp"></a><a name="p1589mcpsimp"></a>陀螺仪六面标定使能开关。</p>
</td>
</tr>
<tr id="row1590mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1592mcpsimp"><a name="p1592mcpsimp"></a><a name="p1592mcpsimp"></a>rotation_matrix</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1594mcpsimp"><a name="p1594mcpsimp"></a><a name="p1594mcpsimp"></a>陀螺仪六面标定矩阵。</p>
</td>
</tr>
<tr id="row1595mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1597mcpsimp"><a name="p1597mcpsimp"></a><a name="p1597mcpsimp"></a>motionfusion[0] gyro drift cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1599mcpsimp"><a name="p1599mcpsimp"></a><a name="p1599mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1601mcpsimp"><a name="p1601mcpsimp"></a><a name="p1601mcpsimp"></a>陀螺仪零偏开关。</p>
</td>
</tr>
<tr id="row1602mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1604mcpsimp"><a name="p1604mcpsimp"></a><a name="p1604mcpsimp"></a>gyro_drift</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1606mcpsimp"><a name="p1606mcpsimp"></a><a name="p1606mcpsimp"></a>陀螺仪零偏值。</p>
</td>
</tr>
<tr id="row1607mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1609mcpsimp"><a name="p1609mcpsimp"></a><a name="p1609mcpsimp"></a>motionfusion[0] gyro online drift cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1611mcpsimp"><a name="p1611mcpsimp"></a><a name="p1611mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1613mcpsimp"><a name="p1613mcpsimp"></a><a name="p1613mcpsimp"></a>陀螺仪在线零偏开关。</p>
</td>
</tr>
<tr id="row1614mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1616mcpsimp"><a name="p1616mcpsimp"></a><a name="p1616mcpsimp"></a>gyro_drift</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1618mcpsimp"><a name="p1618mcpsimp"></a><a name="p1618mcpsimp"></a>陀螺仪在线零偏值。</p>
</td>
</tr>
<tr id="row1619mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1621mcpsimp"><a name="p1621mcpsimp"></a><a name="p1621mcpsimp"></a>online_gyro_data_mean</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1623mcpsimp"><a name="p1623mcpsimp"></a><a name="p1623mcpsimp"></a>陀螺仪的漂移值。</p>
</td>
</tr>
<tr id="row1624mcpsimp"><td class="cellrowborder" rowspan="4" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1626mcpsimp"><a name="p1626mcpsimp"></a><a name="p1626mcpsimp"></a>motionfusion[0] gyro temp drift cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1628mcpsimp"><a name="p1628mcpsimp"></a><a name="p1628mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1630mcpsimp"><a name="p1630mcpsimp"></a><a name="p1630mcpsimp"></a>陀螺仪温飘开关。</p>
</td>
</tr>
<tr id="row1631mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1633mcpsimp"><a name="p1633mcpsimp"></a><a name="p1633mcpsimp"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1635mcpsimp"><a name="p1635mcpsimp"></a><a name="p1635mcpsimp"></a>陀螺仪温飘模式：</p>
<p id="p1636mcpsimp"><a name="p1636mcpsimp"></a><a name="p1636mcpsimp"></a>curv：多项式模式。</p>
<p id="p1637mcpsimp"><a name="p1637mcpsimp"></a><a name="p1637mcpsimp"></a>lut：查找表模式。</p>
</td>
</tr>
<tr id="row1638mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1640mcpsimp"><a name="p1640mcpsimp"></a><a name="p1640mcpsimp"></a>matrix</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1642mcpsimp"><a name="p1642mcpsimp"></a><a name="p1642mcpsimp"></a>多项式系数矩阵（curv模式显示）。</p>
</td>
</tr>
<tr id="row1643mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1645mcpsimp"><a name="p1645mcpsimp"></a><a name="p1645mcpsimp"></a>lut</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1647mcpsimp"><a name="p1647mcpsimp"></a><a name="p1647mcpsimp"></a>温飘表（lut模式显示）。</p>
</td>
</tr>
<tr id="row1648mcpsimp"><td class="cellrowborder" rowspan="7" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1650mcpsimp"><a name="p1650mcpsimp"></a><a name="p1650mcpsimp"></a>motionfusion[0] gyro online temp drift cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1652mcpsimp"><a name="p1652mcpsimp"></a><a name="p1652mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1654mcpsimp"><a name="p1654mcpsimp"></a><a name="p1654mcpsimp"></a>陀螺仪在线温飘开关。</p>
</td>
</tr>
<tr id="row1655mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1657mcpsimp"><a name="p1657mcpsimp"></a><a name="p1657mcpsimp"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1659mcpsimp"><a name="p1659mcpsimp"></a><a name="p1659mcpsimp"></a>陀螺仪在线温飘模式：</p>
<p id="p1660mcpsimp"><a name="p1660mcpsimp"></a><a name="p1660mcpsimp"></a>curv：多项式模式。</p>
<p id="p1661mcpsimp"><a name="p1661mcpsimp"></a><a name="p1661mcpsimp"></a>lut：查找表模式。</p>
</td>
</tr>
<tr id="row1662mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1664mcpsimp"><a name="p1664mcpsimp"></a><a name="p1664mcpsimp"></a>matrix</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1666mcpsimp"><a name="p1666mcpsimp"></a><a name="p1666mcpsimp"></a>多项式系数矩阵（curv模式显示）。</p>
</td>
</tr>
<tr id="row1667mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1669mcpsimp"><a name="p1669mcpsimp"></a><a name="p1669mcpsimp"></a>param: range_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1671mcpsimp"><a name="p1671mcpsimp"></a><a name="p1671mcpsimp"></a>温飘表的最小温度，精度2^10（lut模式显示）。</p>
</td>
</tr>
<tr id="row1672mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1674mcpsimp"><a name="p1674mcpsimp"></a><a name="p1674mcpsimp"></a>param: range_max</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1676mcpsimp"><a name="p1676mcpsimp"></a><a name="p1676mcpsimp"></a>温飘表的最大温度，精度2^10（lut模式显示）。</p>
</td>
</tr>
<tr id="row1677mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1679mcpsimp"><a name="p1679mcpsimp"></a><a name="p1679mcpsimp"></a>param: step</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1681mcpsimp"><a name="p1681mcpsimp"></a><a name="p1681mcpsimp"></a>温飘表的step，精度2^10（lut模式显示）。</p>
</td>
</tr>
<tr id="row1682mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1684mcpsimp"><a name="p1684mcpsimp"></a><a name="p1684mcpsimp"></a>temp_lut</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1686mcpsimp"><a name="p1686mcpsimp"></a><a name="p1686mcpsimp"></a>温飘表（lut模式显示）。</p>
</td>
</tr>
<tr id="row1687mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1689mcpsimp"><a name="p1689mcpsimp"></a><a name="p1689mcpsimp"></a>motionfusion[0] acc sixside cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1691mcpsimp"><a name="p1691mcpsimp"></a><a name="p1691mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1693mcpsimp"><a name="p1693mcpsimp"></a><a name="p1693mcpsimp"></a>加速度计六面标定使能开关。</p>
</td>
</tr>
<tr id="row1694mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1696mcpsimp"><a name="p1696mcpsimp"></a><a name="p1696mcpsimp"></a>rotation_matrix</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1698mcpsimp"><a name="p1698mcpsimp"></a><a name="p1698mcpsimp"></a>加速度计六面标定矩阵。</p>
</td>
</tr>
<tr id="row1699mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1701mcpsimp"><a name="p1701mcpsimp"></a><a name="p1701mcpsimp"></a>motionfusion[0] acc drift cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1703mcpsimp"><a name="p1703mcpsimp"></a><a name="p1703mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1705mcpsimp"><a name="p1705mcpsimp"></a><a name="p1705mcpsimp"></a>加速度计零偏开关。</p>
</td>
</tr>
<tr id="row1706mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1708mcpsimp"><a name="p1708mcpsimp"></a><a name="p1708mcpsimp"></a>acc_drift</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1710mcpsimp"><a name="p1710mcpsimp"></a><a name="p1710mcpsimp"></a>加速度计零偏值。</p>
</td>
</tr>
<tr id="row1711mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1713mcpsimp"><a name="p1713mcpsimp"></a><a name="p1713mcpsimp"></a>motionfusion[0] acc temp drift cal status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1715mcpsimp"><a name="p1715mcpsimp"></a><a name="p1715mcpsimp"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1717mcpsimp"><a name="p1717mcpsimp"></a><a name="p1717mcpsimp"></a>加速度计温飘开关。</p>
</td>
</tr>
<tr id="row1718mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1720mcpsimp"><a name="p1720mcpsimp"></a><a name="p1720mcpsimp"></a>acc_temp_drift</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1722mcpsimp"><a name="p1722mcpsimp"></a><a name="p1722mcpsimp"></a>加速度计温飘值。</p>
</td>
</tr>
<tr id="row194555151315"><td class="cellrowborder" rowspan="3" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p20606142019313"><a name="p20606142019313"></a><a name="p20606142019313"></a>motionfusion[0] bind status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p114561015133113"><a name="p114561015133113"></a><a name="p114561015133113"></a>bind_valid</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p11456181583116"><a name="p11456181583116"></a><a name="p11456181583116"></a>绑定关系有效性。</p>
</td>
</tr>
<tr id="row245651515318"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p19456515153113"><a name="p19456515153113"></a><a name="p19456515153113"></a>vi_pipe</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p2456141520313"><a name="p2456141520313"></a><a name="p2456141520313"></a>VI PIPE号。</p>
</td>
</tr>
<tr id="row16685146133114"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p196852046113111"><a name="p196852046113111"></a><a name="p196852046113111"></a>vi_chn</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p12685204613120"><a name="p12685204613120"></a><a name="p12685204613120"></a>VI通道号。</p>
</td>
</tr>
<tr id="row1723mcpsimp"><td class="cellrowborder" rowspan="14" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1725mcpsimp"><a name="p1725mcpsimp"></a><a name="p1725mcpsimp"></a>motionfusion[0] drv status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1727mcpsimp"><a name="p1727mcpsimp"></a><a name="p1727mcpsimp"></a>gyro config：sample_rate</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1729mcpsimp"><a name="p1729mcpsimp"></a><a name="p1729mcpsimp"></a>陀螺仪采样率。</p>
</td>
</tr>
<tr id="row1730mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1732mcpsimp"><a name="p1732mcpsimp"></a><a name="p1732mcpsimp"></a>gyro config：data_range</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1735mcpsimp"><a name="p1735mcpsimp"></a><a name="p1735mcpsimp"></a>陀螺仪量程。</p>
</td>
</tr>
<tr id="row1736mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1738mcpsimp"><a name="p1738mcpsimp"></a><a name="p1738mcpsimp"></a>gyro config：data_precbit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1741mcpsimp"><a name="p1741mcpsimp"></a><a name="p1741mcpsimp"></a>陀螺仪数据位宽。</p>
</td>
</tr>
<tr id="row1742mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1744mcpsimp"><a name="p1744mcpsimp"></a><a name="p1744mcpsimp"></a>gyro config：temp_data_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1747mcpsimp"><a name="p1747mcpsimp"></a><a name="p1747mcpsimp"></a>陀螺仪芯片温度最小值。</p>
</td>
</tr>
<tr id="row1748mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1750mcpsimp"><a name="p1750mcpsimp"></a><a name="p1750mcpsimp"></a>gyro config：temp_data_max</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1753mcpsimp"><a name="p1753mcpsimp"></a><a name="p1753mcpsimp"></a>陀螺仪芯片温度最大值。</p>
</td>
</tr>
<tr id="row1754mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1756mcpsimp"><a name="p1756mcpsimp"></a><a name="p1756mcpsimp"></a>gyro config：bit_width</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1759mcpsimp"><a name="p1759mcpsimp"></a><a name="p1759mcpsimp"></a>陀螺仪数据位宽。</p>
</td>
</tr>
<tr id="row1760mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1762mcpsimp"><a name="p1762mcpsimp"></a><a name="p1762mcpsimp"></a>acc config：sample_rate</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1764mcpsimp"><a name="p1764mcpsimp"></a><a name="p1764mcpsimp"></a>加速度计采样率。</p>
</td>
</tr>
<tr id="row1765mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1767mcpsimp"><a name="p1767mcpsimp"></a><a name="p1767mcpsimp"></a>acc config：data_range</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1770mcpsimp"><a name="p1770mcpsimp"></a><a name="p1770mcpsimp"></a>加速度计量程。</p>
</td>
</tr>
<tr id="row1771mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1773mcpsimp"><a name="p1773mcpsimp"></a><a name="p1773mcpsimp"></a>acc config：data_precbit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1776mcpsimp"><a name="p1776mcpsimp"></a><a name="p1776mcpsimp"></a>加速度计数据位宽。</p>
</td>
</tr>
<tr id="row1777mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1779mcpsimp"><a name="p1779mcpsimp"></a><a name="p1779mcpsimp"></a>acc config：temp_data_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1782mcpsimp"><a name="p1782mcpsimp"></a><a name="p1782mcpsimp"></a>加速度计芯片温度最小值。</p>
</td>
</tr>
<tr id="row1783mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1785mcpsimp"><a name="p1785mcpsimp"></a><a name="p1785mcpsimp"></a>acc config：temp_data_max</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1788mcpsimp"><a name="p1788mcpsimp"></a><a name="p1788mcpsimp"></a>加速度计芯片温度最大值。</p>
</td>
</tr>
<tr id="row1789mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1791mcpsimp"><a name="p1791mcpsimp"></a><a name="p1791mcpsimp"></a>acc config：bit_width</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1794mcpsimp"><a name="p1794mcpsimp"></a><a name="p1794mcpsimp"></a>加速度计数据位宽。</p>
</td>
</tr>
<tr id="row1795mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1797mcpsimp"><a name="p1797mcpsimp"></a><a name="p1797mcpsimp"></a>magn config：sample_rate</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1799mcpsimp"><a name="p1799mcpsimp"></a><a name="p1799mcpsimp"></a>磁力计采样率。（暂不支持）</p>
</td>
</tr>
<tr id="row1800mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1802mcpsimp"><a name="p1802mcpsimp"></a><a name="p1802mcpsimp"></a>cam status</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1804mcpsimp"><a name="p1804mcpsimp"></a><a name="p1804mcpsimp"></a>陀螺仪静止检测的结果：</p>
<p id="p1805mcpsimp"><a name="p1805mcpsimp"></a><a name="p1805mcpsimp"></a>steady：静止。</p>
<p id="p1806mcpsimp"><a name="p1806mcpsimp"></a><a name="p1806mcpsimp"></a>moving：运动。</p>
</td>
</tr>
<tr id="row1807mcpsimp"><td class="cellrowborder" rowspan="6" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1809mcpsimp"><a name="p1809mcpsimp"></a><a name="p1809mcpsimp"></a>user 0 gyro_data</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1811mcpsimp"><a name="p1811mcpsimp"></a><a name="p1811mcpsimp"></a>begin_pts</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1813mcpsimp"><a name="p1813mcpsimp"></a><a name="p1813mcpsimp"></a>当前帧获取陀螺仪数据的起始时间戳。</p>
</td>
</tr>
<tr id="row1814mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1816mcpsimp"><a name="p1816mcpsimp"></a><a name="p1816mcpsimp"></a>end_pts</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1818mcpsimp"><a name="p1818mcpsimp"></a><a name="p1818mcpsimp"></a>当前帧获取陀螺仪数据的结束时间戳。</p>
</td>
</tr>
<tr id="row1819mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1821mcpsimp"><a name="p1821mcpsimp"></a><a name="p1821mcpsimp"></a>gyro_data num</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1823mcpsimp"><a name="p1823mcpsimp"></a><a name="p1823mcpsimp"></a>当前帧获取陀螺仪数据的数目。</p>
</td>
</tr>
<tr id="row1824mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1826mcpsimp"><a name="p1826mcpsimp"></a><a name="p1826mcpsimp"></a>x，y，z，temp，pts</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1828mcpsimp"><a name="p1828mcpsimp"></a><a name="p1828mcpsimp"></a>当前帧获取陀螺仪数据值。</p>
</td>
</tr>
<tr id="row1884781810376"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p148481618133713"><a name="p148481618133713"></a><a name="p148481618133713"></a>x_mean，y_mean，z_mean，temp_mean，pts_step_mean</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p9848101833716"><a name="p9848101833716"></a><a name="p9848101833716"></a>统计帧获取陀螺仪数据的平均值。</p>
</td>
</tr>
<tr id="row777447113616"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p277847173617"><a name="p277847173617"></a><a name="p277847173617"></a>x_variance，y_variance，z_variance，temp_variance，pts_step_variance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p5775475365"><a name="p5775475365"></a><a name="p5775475365"></a>统计帧获取陀螺仪数据的方差。</p>
</td>
</tr>
</tbody>
</table>

## gyrodis proc<a name="ZH-CN_TOPIC_0000002408262194"></a>

【调试信息】

```
[GYRODIS] version: [V2.0.2.0 B010 Release], build time[May 30 2022, 15:20:24]
----------------------------------------gyrodis public attr of chn[0]---------------------------------------------------

is_remove_distortion    is_stabilization
1                   1

hmax_times          time_delay       exposure_time           mirror_en             flip_en
14405               -2700               33189                   0                   0

valid_dt_var          max_dt_var          vmax
20                    1000                2314

gyro_data_range  gyro_data_precbits
256000                  15

----------------------------------------frame pts info of chn[0]--------------------------------------------------------

frm_pts   frm_pts_after_ave        frm_pts_diff    frm_pts_diff_max    frm_pts_diff_min
12562620897         12562620897               33296               33296               33295
```

【参数说明】

<a name="table1843mcpsimp"></a>
<table><thead align="left"><tr id="row1849mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p1851mcpsimp"><a name="p1851mcpsimp"></a><a name="p1851mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p1853mcpsimp"><a name="p1853mcpsimp"></a><a name="p1853mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1855mcpsimp"><td class="cellrowborder" rowspan="12" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1857mcpsimp"><a name="p1857mcpsimp"></a><a name="p1857mcpsimp"></a>gyrodis public attr of chn[0]</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1859mcpsimp"><a name="p1859mcpsimp"></a><a name="p1859mcpsimp"></a>is_remove_distortion</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1861mcpsimp"><a name="p1861mcpsimp"></a><a name="p1861mcpsimp"></a>是否移除最终防抖LDC效果。</p>
</td>
</tr>
<tr id="row1862mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1864mcpsimp"><a name="p1864mcpsimp"></a><a name="p1864mcpsimp"></a>is_stabilization</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1866mcpsimp"><a name="p1866mcpsimp"></a><a name="p1866mcpsimp"></a>是否使能防抖。</p>
</td>
</tr>
<tr id="row1867mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1869mcpsimp"><a name="p1869mcpsimp"></a><a name="p1869mcpsimp"></a>hmax_times</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1871mcpsimp"><a name="p1871mcpsimp"></a><a name="p1871mcpsimp"></a>Sensor读出一行的时间，相关描述参考《ISP 开发参考》。单位：ns。</p>
</td>
</tr>
<tr id="row1872mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1874mcpsimp"><a name="p1874mcpsimp"></a><a name="p1874mcpsimp"></a>time_delay</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1876mcpsimp"><a name="p1876mcpsimp"></a><a name="p1876mcpsimp"></a>陀螺仪与图像时间差。参考《DIS调试指南》。</p>
</td>
</tr>
<tr id="row1877mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1879mcpsimp"><a name="p1879mcpsimp"></a><a name="p1879mcpsimp"></a>exposure_time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1881mcpsimp"><a name="p1881mcpsimp"></a><a name="p1881mcpsimp"></a>曝光时间。</p>
</td>
</tr>
<tr id="row1882mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1884mcpsimp"><a name="p1884mcpsimp"></a><a name="p1884mcpsimp"></a>mirror_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1886mcpsimp"><a name="p1886mcpsimp"></a><a name="p1886mcpsimp"></a>镜像使能状态。</p>
</td>
</tr>
<tr id="row1887mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1889mcpsimp"><a name="p1889mcpsimp"></a><a name="p1889mcpsimp"></a>flip_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1891mcpsimp"><a name="p1891mcpsimp"></a><a name="p1891mcpsimp"></a>翻转使能状态。</p>
</td>
</tr>
<tr id="row17404137185412"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p14746158195511"><a name="p14746158195511"></a><a name="p14746158195511"></a>valid_dt_var</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p87465815555"><a name="p87465815555"></a><a name="p87465815555"></a>合理的帧时间戳的波动。</p>
</td>
</tr>
<tr id="row7237145025417"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1746168125513"><a name="p1746168125513"></a><a name="p1746168125513"></a>max_dt_var</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1574612805516"><a name="p1574612805516"></a><a name="p1574612805516"></a>允许的最大的帧时间戳的波动。</p>
</td>
</tr>
<tr id="row126413467543"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1874619811554"><a name="p1874619811554"></a><a name="p1874619811554"></a>vmax</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p474620815556"><a name="p474620815556"></a><a name="p474620815556"></a>Sensor每帧实际生效的总行数，相关描述参考《ISP 开发参考》。</p>
</td>
</tr>
<tr id="row1892mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1894mcpsimp"><a name="p1894mcpsimp"></a><a name="p1894mcpsimp"></a>gyro_data_range</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1896mcpsimp"><a name="p1896mcpsimp"></a><a name="p1896mcpsimp"></a>陀螺仪量程。</p>
</td>
</tr>
<tr id="row1897mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1899mcpsimp"><a name="p1899mcpsimp"></a><a name="p1899mcpsimp"></a>gyro_data_precbits</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1901mcpsimp"><a name="p1901mcpsimp"></a><a name="p1901mcpsimp"></a>陀螺仪数据精度。</p>
</td>
</tr>
<tr id="row1917mcpsimp"><td class="cellrowborder" rowspan="5" valign="top" width="17%" headers="mcps1.1.4.1.1 "><p id="p1919mcpsimp"><a name="p1919mcpsimp"></a><a name="p1919mcpsimp"></a>frame pts info of chn[0]</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1921mcpsimp"><a name="p1921mcpsimp"></a><a name="p1921mcpsimp"></a>frm_pts</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1923mcpsimp"><a name="p1923mcpsimp"></a><a name="p1923mcpsimp"></a>输入gyrodis的帧时间戳。</p>
</td>
</tr>
<tr id="row1924mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1926mcpsimp"><a name="p1926mcpsimp"></a><a name="p1926mcpsimp"></a>frm_pts_after_ave</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1928mcpsimp"><a name="p1928mcpsimp"></a><a name="p1928mcpsimp"></a>取平均后的帧时间戳。</p>
</td>
</tr>
<tr id="row1929mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1931mcpsimp"><a name="p1931mcpsimp"></a><a name="p1931mcpsimp"></a>frm_pts_diff</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1933mcpsimp"><a name="p1933mcpsimp"></a><a name="p1933mcpsimp"></a>与上一帧的时间戳间隔。</p>
</td>
</tr>
<tr id="row1934mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1936mcpsimp"><a name="p1936mcpsimp"></a><a name="p1936mcpsimp"></a>frm_pts_diff_max</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1938mcpsimp"><a name="p1938mcpsimp"></a><a name="p1938mcpsimp"></a>与上一帧的时间戳差值最大值。</p>
</td>
</tr>
<tr id="row1939mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1941mcpsimp"><a name="p1941mcpsimp"></a><a name="p1941mcpsimp"></a>frm_pts_diff_min</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p1943mcpsimp"><a name="p1943mcpsimp"></a><a name="p1943mcpsimp"></a>与上一帧的时间戳差值最小值。</p>
</td>
</tr>
</tbody>
</table>

# 缩略语
<a name="table1945mcpsimp"></a>
<table><thead align="left"><tr id="row1950mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p1952mcpsimp"><a name="p1952mcpsimp"></a><a name="p1952mcpsimp"></a>缩略语</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1954mcpsimp"><a name="p1954mcpsimp"></a><a name="p1954mcpsimp"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1956mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1958mcpsimp"><a name="p1958mcpsimp"></a><a name="p1958mcpsimp"></a>Gyro</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1960mcpsimp"><a name="p1960mcpsimp"></a><a name="p1960mcpsimp"></a>Gyroscope 陀螺仪</p>
</td>
</tr>
<tr id="row1961mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1963mcpsimp"><a name="p1963mcpsimp"></a><a name="p1963mcpsimp"></a>ACC</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1965mcpsimp"><a name="p1965mcpsimp"></a><a name="p1965mcpsimp"></a>Accelerometer 加速度计</p>
</td>
</tr>
<tr id="row1966mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1968mcpsimp"><a name="p1968mcpsimp"></a><a name="p1968mcpsimp"></a>PTS</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1970mcpsimp"><a name="p1970mcpsimp"></a><a name="p1970mcpsimp"></a>Presentation Time Stamp 显示时间戳</p>
</td>
</tr>
<tr id="row1971mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1973mcpsimp"><a name="p1973mcpsimp"></a><a name="p1973mcpsimp"></a>IMU</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p xml:lang="en" id="p1975mcpsimp"><a name="p1975mcpsimp"></a><a name="p1975mcpsimp"></a>Inertial Measurement Unit 惯性测量单元</p>
</td>
</tr>
</tbody>
</table>

