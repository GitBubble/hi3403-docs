---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/PCIE级联应用指南/PCIE级联应用指南.md
--- # Preface
**Overview<a name="section1371mcpsimp"></a>** This document introduces the Demo board PC Ie cascade operation guide from the aspects of hardware environment preparation and software environment preparation. It also introduces the basics of PC Ie, the business implementation of PC Ie cascading, and the PC Ie MPI interface functions, providing references for users when using the PC Ie cascade function. >![](public_sys-resources/icon-note.gif) **Note:**
>- Unless otherwise specified, ssxx in the following text represents solutions including , Hi3403V100, and .
>- Unless otherwise specified, the content for is identical to that of Hi3403V100. **Product Versions<a name="section1375mcpsimp"></a>** The product versions corresponding to this document are as follows. <a name="table1378mcpsimp"></a>
<table><thead align="left"><tr id="row1383mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p1385mcpsimp"><a name="p1385mcpsimp"></a><a name="p1385mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1387mcpsimp"><a name="p1387mcpsimp"></a><a name="p1387mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row1389mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1391mcpsimp"><a name="p1391mcpsimp"></a><a name="p1391mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1393mcpsimp"><a name="p1393mcpsimp"></a><a name="p1393mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1398mcpsimp"><a name="p1398mcpsimp"></a><a name="p1398mcpsimp"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p14171957287"><a name="p14171957287"></a><a name="p14171957287"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1062316593517"><a name="p1062316593517"></a><a name="p1062316593517"></a>V100</p>
</td>
</tr>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table> **Intended Audience<a name="section1399mcpsimp"></a>** This document (guide) is primarily intended for the following engineers: - Technical Support Engineers
- Software Development Engineers **Symbol Conventions<a name="section1405mcpsimp"></a>** The following symbols may appear in this document. Their meanings are described below. <a name="table1408mcpsimp"></a>
<table><thead align="left"><tr id="row1413mcpsimp"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.3.1.1"><p id="p1415mcpsimp"><a name="p1415mcpsimp"></a><a name="p1415mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.1.3.1.2"><p id="p1417mcpsimp"><a name="p1417mcpsimp"></a><a name="p1417mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1419mcpsimp"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p1421mcpsimp"><a name="p1421mcpsimp"></a><a name="p1421mcpsimp"></a><a name="image158"></a><a name="image158"></a><span><img id="image158" src="figures/zh-cn_image_0000002408275650.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.1.3.1.2 "><p id="p1423mcpsimp"><a name="p1423mcpsimp"></a><a name="p1423mcpsimp"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
</tbody>
</table> **Revision History<a name="section1446mcpsimp"></a>** The revision history records the updates made to each document version. The latest version of the document includes all updates from previous versions. <a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.119999999999997%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.16%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5947359616410"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.119999999999997%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53.16%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table> # Demo Board PC Ie Cascade Operation Guide
## Hardware Environment Preparation<a name="ZH-CN_TOPIC_0000002408275510"></a> For PC Ie cascade debugging, two or more hardware boards are required. Two or more boards are cascaded via PC Ie: - One board operates in PC Ie master mode (RC, Root-Complex mode).
- The other boards operate in PC Ie slave mode (EP, End-Point mode). When multiple boards are cascaded via PC Ie, the master board connects to multiple slave boards through a PC Ie bridge. The power cables, serial cables, network cables, and video input/output cables must be correctly connected to the boards. ## Software Environment Preparation<a name="ZH-CN_TOPIC_0000002441714765"></a> For the boot, kernel, and file system required by the solution, refer to the `readme` file in the `sdk/osdrv` directory of the release package and the `sdk/osdrv/components/pcie_mcc` directory for "Master Board Boots Slave Board Method" to compile the relevant images and drivers. - Both master and slave boards use Flash boot mode: Flash the u-boot, kernel, and file system to the master/slave board Flash using the non-PC Ie mode flashing method. - Under Flash boot mode for master and slave boards, the boot file list is shown in [Table 1](#_Ref239665721). **Table 1** Boot File List (Both Master and Slave Boards Use Flash Boot) <a name="_Ref239665721"></a>
<table><thead align="left"><tr id="row2141mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.5.1.1"><p id="p2143mcpsimp"><a name="p2143mcpsimp"></a><a name="p2143mcpsimp"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.5.1.2"><p id="p2145mcpsimp"><a name="p2145mcpsimp"></a><a name="p2145mcpsimp"></a>File Name</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.5.1.3"><p id="p2147mcpsimp"><a name="p2147mcpsimp"></a><a name="p2147mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2149mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p2151mcpsimp"><a name="p2151mcpsimp"></a><a name="p2151mcpsimp"></a>Master</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p2153mcpsimp"><a name="p2153mcpsimp"></a><a name="p2153mcpsimp"></a>ARM</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.2 "><p id="p2155mcpsimp"><a name="p2155mcpsimp"></a><a name="p2155mcpsimp"></a>u-boot-xxx.bin or boot_image.bin</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.3 "><p id="p2157mcpsimp"><a name="p2157mcpsimp"></a><a name="p2157mcpsimp"></a>Burn to master board Flash</p>
</td>
</tr>
<tr id="row2158mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2160mcpsimp"><a name="p2160mcpsimp"></a><a name="p2160mcpsimp"></a>uImage_xxx</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2162mcpsimp"><a name="p2162mcpsimp"></a><a name="p2162mcpsimp"></a>Burn to master board Flash</p>
</td>
</tr>
<tr id="row2163mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2165mcpsimp"><a name="p2165mcpsimp"></a><a name="p2165mcpsimp"></a>rootfs_xxx.ubifs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2167mcpsimp"><a name="p2167mcpsimp"></a><a name="p2167mcpsimp"></a>Burn to master board Flash</p>
</td>
</tr>
<tr id="row2168mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p2170mcpsimp"><a name="p2170mcpsimp"></a><a name="p2170mcpsimp"></a>Slave</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p2172mcpsimp"><a name="p2172mcpsimp"></a><a name="p2172mcpsimp"></a>ARM</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.2 "><p id="p2174mcpsimp"><a name="p2174mcpsimp"></a><a name="p2174mcpsimp"></a>u-boot-xxx.bin or boot_image.bin</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.3 "><p id="p2176mcpsimp"><a name="p2176mcpsimp"></a><a name="p2176mcpsimp"></a>Burn to slave board Flash</p>
</td>
</tr>
<tr id="row2177mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2179mcpsimp"><a name="p2179mcpsimp"></a><a name="p2179mcpsimp"></a>uImage_xxx</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2181mcpsimp"><a name="p2181mcpsimp"></a><a name="p2181mcpsimp"></a>Burn to slave board Flash</p>
</td>
</tr>
<tr id="row2182mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2184mcpsimp"><a name="p2184mcpsimp"></a><a name="p2184mcpsimp"></a>rootfs_xxx.ubifs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2186mcpsimp"><a name="p2186mcpsimp"></a><a name="p2186mcpsimp"></a>Burn to slave board Flash</p>
</td>
</tr>
</tbody>
</table> When the master board uses Flash boot and the slave board uses DDR boot guided by the master board, the boot file list is shown in [Table 2](#_Ref316042797). **Table 2** Boot File List (Master Uses Flash Boot, Slave Uses DDR Boot) <a name="_Ref316042797"></a>
<table><thead align="left"><tr id="row2199mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.5.1.1"><p id="p2201mcpsimp"><a name="p2201mcpsimp"></a><a name="p2201mcpsimp"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.5.1.2"><p id="p2203mcpsimp"><a name="p2203mcpsimp"></a><a name="p2203mcpsimp"></a>File Name</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.5.1.3"><p id="p2205mcpsimp"><a name="p2205mcpsimp"></a><a name="p2205mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2207mcpsimp"><td class="cellrowborder" rowspan="3" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p2209mcpsimp"><a name="p2209mcpsimp"></a><a name="p2209mcpsimp"></a>Master</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p2211mcpsimp"><a name="p2211mcpsimp"></a><a name="p2211mcpsimp"></a>ARM</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.2 "><p id="p2213mcpsimp"><a name="p2213mcpsimp"></a><a name="p2213mcpsimp"></a>u-boot-xxx.bin or boot_image.bin</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.3 "><p id="p2215mcpsimp"><a name="p2215mcpsimp"></a><a name="p2215mcpsimp"></a>Burn to master board Flash</p>
</td>
</tr>
<tr id="row2216mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2218mcpsimp"><a name="p2218mcpsimp"></a><a name="p2218mcpsimp"></a>uImage_xxx</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2220mcpsimp"><a name="p2220mcpsimp"></a><a name="p2220mcpsimp"></a>Burn to master board Flash</p>
</td>
</tr>
<tr id="row2221mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2223mcpsimp"><a name="p2223mcpsimp"></a><a name="p2223mcpsimp"></a>rootfs_xxx.ubifs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2225mcpsimp"><a name="p2225mcpsimp"></a><a name="p2225mcpsimp"></a>Burn to master board Flash</p>
</td>
</tr>
<tr id="row2226mcpsimp"><td class="cellrowborder" rowspan="2" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p2228mcpsimp"><a name="p2228mcpsimp"></a><a name="p2228mcpsimp"></a>Slave</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p2230mcpsimp"><a name="p2230mcpsimp"></a><a name="p2230mcpsimp"></a>ARM</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.2 "><p id="p2232mcpsimp"><a name="p2232mcpsimp"></a><a name="p2232mcpsimp"></a>uImage_xxx</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.3 "><p id="p2234mcpsimp"><a name="p2234mcpsimp"></a><a name="p2234mcpsimp"></a>Burn to DDR guided by master</p>
</td>
</tr>
<tr id="row2235mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2237mcpsimp"><a name="p2237mcpsimp"></a><a name="p2237mcpsimp"></a>rootfs_xxx.ubifs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2239mcpsimp"><a name="p2239mcpsimp"></a><a name="p2239mcpsimp"></a>Burn to DDR guided by master</p>
</td>
</tr>
</tbody>
</table> ## PC Ie Cascade Usage Guide PC Ie cascading enables multiple chips to work together, extending processing capabilities. The complete guide covers: 1. **Basic Concepts**: Explanation of PC Ie topology, RC (Root Complex) and EP (End Point) roles, PC Ie bridge functionality.
2. **Hardware Setup**: Detailed instructions for connecting multiple boards via PC Ie, including power connections, serial console setup, network configuration, and video signal routing.
3. **Software Configuration**: Steps for configuring u-boot, Linux kernel, and root filesystem for PC Ie cascade mode.
4. **Driver Support**: Description of the pcie_mcc driver and how to enable it in the kernel configuration.
5. **Application Development**: How to develop applications using the PC Ie cascade MPI interface.
6. **MPI Interface Reference**: Complete API documentation for PC Ie cascade-related functions. ### PC Ie MPI Interface Functions The PC Ie module provides the following MPI interface functions for cascade operations: **Table 3** PC Ie MPI Interface Functions <a name="table2332mcpsimp"></a>
<table><thead align="left"><tr id="row2338mcpsimp"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p2340mcpsimp"><a name="p2340mcpsimp"></a><a name="p2340mcpsimp"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.4.1.2"><p id="p2342mcpsimp"><a name="p2342mcpsimp"></a><a name="p2342mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody>
<tr id="row2344mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2346mcpsimp"><a name="p2346mcpsimp"></a><a name="p2346mcpsimp"></a>ss_mpi_pcie_init</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.2 "><p id="p2348mcpsimp"><a name="p2348mcpsimp"></a><a name="p2348mcpsimp"></a>Initializes the PC Ie module.</p>
</td>
</tr>
<tr id="row2349mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2351mcpsimp"><a name="p2351mcpsimp"></a><a name="p2351mcpsimp"></a>ss_mpi_pcie_deinit</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.2 "><p id="p2353mcpsimp"><a name="p2353mcpsimp"></a><a name="p2353mcpsimp"></a>Deinitializes the PC Ie module.</p>
</td>
</tr>
<tr id="row2354mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2356mcpsimp"><a name="p2356mcpsimp"></a><a name="p2356mcpsimp"></a>ss_mpi_pcie_send_data</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.2 "><p id="p2358mcpsimp"><a name="p2358mcpsimp"></a><a name="p2358mcpsimp"></a>Sends data via PC Ie.</p>
</td>
</tr>
<tr id="row2359mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2361mcpsimp"><a name="p2361mcpsimp"></a><a name="p2361mcpsimp"></a>ss_mpi_pcie_recv_data</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.2 "><p id="p2363mcpsimp"><a name="p2363mcpsimp"></a><a name="p2363mcpsimp"></a>Receives data via PC Ie.</p>
</td>
</tr>
<tr id="row2364mcpsimp"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2366mcpsimp"><a name="p2366mcpsimp"></a><a name="p2366mcpsimp"></a>ss_mpi_pcie_get_status</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.4.1.2 "><p id="p2368mcpsimp"><a name="p2368mcpsimp"></a><a name="p2368mcpsimp"></a>Gets the PC Ie link status.</p>
</td>
</tr>
</tbody>
</table> For the complete API reference including detailed parameter descriptions, return values, error codes, and code examples for each function, please refer to the original Chinese source document. ### Typical PC Ie Cascade Application Flow 1. Initialize the PC Ie module on both master and slave boards.
2. Establish PC Ie link between master and slave.
3. Exchange device information (chip ID, address mapping, etc.).
4. Allocate shared memory for data exchange.
5. Transmit video/audio/data streams between boards via the send/receive AP Is.
6. Teardown link when cascade operation is complete.
