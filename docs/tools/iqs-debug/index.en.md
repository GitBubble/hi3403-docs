---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/Image Quality Debugging Tool User Guide/Image Quality Debugging Tool User Guide.md
---

# Preface
**Overview<a name="section5622mcpsimp"></a>**

The PQ Tools Image Quality Debugging Tool User Guide mainly assists debuggers in image effect adjustment and differentiation. This document focuses on explaining the relevant debugging operation methods.

>![](public_sys-resources/icon-note.gif) **Note:** 
>This document uses the Hi3403V100 description as an example. Unless otherwise specified, the content for Hi3519AV200 is consistent with Hi3403V100.

**Product Version<a name="section5625mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table5628mcpsimp"></a>
<table><thead align="left"><tr id="row5633mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p5635mcpsimp"><a name="p5635mcpsimp"></a><a name="p5635mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p5637mcpsimp"><a name="p5637mcpsimp"></a><a name="p5637mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row5639mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5641mcpsimp"><a name="p5641mcpsimp"></a><a name="p5641mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p5643mcpsimp"><a name="p5643mcpsimp"></a><a name="p5643mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row4477135110273"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p17797185342716"><a name="p17797185342716"></a><a name="p17797185342716"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1879775352710"><a name="p1879775352710"></a><a name="p1879775352710"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Target Audience<a name="section5644mcpsimp"></a>**

This document (guide) is primarily applicable to the following engineers:

-   Technical Support Engineer
-   Software Development Engineer

**Revision History<a name="section5650mcpsimp"></a>**

<a name="table5652mcpsimp"></a>
<table><thead align="left"><tr id="row5658mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p5660mcpsimp"><a name="p5660mcpsimp"></a><a name="p5660mcpsimp"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p5663mcpsimp"><a name="p5663mcpsimp"></a><a name="p5663mcpsimp"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p5666mcpsimp"><a name="p5666mcpsimp"></a><a name="p5666mcpsimp"></a>Change Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9157117152013"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p14523111518206"><a name="p14523111518206"></a><a name="p14523111518206"></a>00B02</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p1052321511203"><a name="p1052321511203"></a><a name="p1052321511203"></a>2025-12-25</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p15523171512209"><a name="p15523171512209"></a><a name="p15523171512209"></a>Second interim version release.</p>
<p id="p10140193052014"><a name="p10140193052014"></a><a name="p10140193052014"></a>Modified sections: "Installation and Operation of Board-Side Software under Linux" and "Fisheye Lens Calibration Steps"</p>
</td>
</tr>
<tr id="row5669mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p5671mcpsimp"><a name="p5671mcpsimp"></a><a name="p5671mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p5673mcpsimp"><a name="p5673mcpsimp"></a><a name="p5673mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p5675mcpsimp"><a name="p5675mcpsimp"></a><a name="p5675mcpsimp"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table>

# Overview
## Tool Overview<a name="ZH-CN_TOPIC_0000002530061733"></a>

PQ provides customers with a series of professional image quality debugging tools (hereinafter referred to as PQT). These include a convenient online debugging tool (Tuning Tool) that allows direct parameter adjustment of ISP and other modules after connecting to the board, while viewing the effect of parameter settings through real-time preview/ondemand (Stream). It also provides various data analysis tools (Analysis Tool) for common debugging scenarios, offering more objective analysis for customer adjustments.

The tool architecture is shown in [Figure 1](#fig12895245195817).

**Figure 1** Tool Architecture Diagram<a name="fig12895245195817"></a>  
![](figures/Tool architecture diagram.png "Tool architecture diagram")

The tools are mainly divided by usage scenario into:

-   Calibration Tool: Used to automatically generate algorithm parameters for each supported ISP module. Currently, this tool is an independent tool.
-   Online Debugging Tool (Tuning Tool): Used for fine and differentiated adjustment of various parameters, taking effect in real time, with the image quality effect viewable through preview.
-   Analysis Tool: Assists the online debugging tool by providing commonly used data and charts, enabling real-time analysis alongside real-time adjustment.
-   Capture Tool: Supports capturing YUV, RAW, and JPEG files.
-   From a delivery perspective, the tools are divided into two parts: PC side and board side. The PC side includes the online debugging tool and various analysis tools and calibration tools provided as plugins. The board side is the ittb_control process, mainly responsible for online parameter adjustment.

## Environment Preparation Description<a name="ZH-CN_TOPIC_0000002530221735"></a>

### Hardware and Software Requirements<a name="ZH-CN_TOPIC_0000002498141768"></a>

-   Hardware Requirements
    -   A board with the chip listed in the product version of the preface and a network port.
    -   Desktop or laptop computer.
    -   Network cables (if using a LAN, a router or other network switching equipment is also required) or serial cables.
    -   Monitor resolution for running the PQTools tool: width not less than 1024, height not less than 768.

-   Software Requirements

    The computer running the PQTools tool must have Windows 10 or later 64-bit Windows OS installed.

    Before using ISP calibration, autofocus parameter simulation, or the PQTools Stitching Tool, please download the Python 3.9.2 installation package (64-bit) from:

    [https://www.python.org/downloads/release/python-392/](https://www.python.org/downloads/release/python-392/). Windows users should select the option indicated by the red box in [Figure 1](#fig1216734547).

    **Figure 1** Download Prompt<a name="fig1216734547"></a>  
    ![](figures/Download prompt.png "Download prompt")

    Install and configure the system path as shown in [Figure 2](#fig18802134119314).

    This path is only an example. Configure the environment variables according to the actual Python installation path.

    **Figure 2** System Path Configuration<a name="fig18802134119314"></a>  
    ![](figures/System path configuration.png "System path configuration")

    After Python is installed successfully, use `pip install` to install the numpy, scipy, and csaps packages.

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>Some functions of the PQTools tool do not support Chinese paths. When using the tool and loading files, avoid file paths containing Chinese characters. **Currently, the tool path is restricted within the algorithm due to the algorithm calling tool python directory content:**
>-   **Desktop and paths under the desktop**
>-   **Chinese paths**
>-   **Paths starting with digits**

### Physical Link Connection<a name="ZH-CN_TOPIC_0000002530221609"></a>

The PQTools tool is divided into a client side (PC software) and a server side (board software), communicating via network or serial port. Any of the following three connection methods can be used to establish the physical link.

-   Direct connection between computer and board

    Connect the two ends of the network cable to the network ports of the board and the computer respectively.

-   Using a local area network (LAN)
    -   Connect the two ends of the network cable to the board network port and the router client port respectively.
    -   If the computer uses a wired network, connect the two ends of another network cable to the computer network port and the router client port respectively. If using a wireless network, refer to the current router settings (or the network settings assigned to you by the network administrator) to connect the computer to the wireless hotspot.

-   Serial connection between computer and board

    Connect the two ends of the serial cable to the board serial port and the computer serial port respectively.

### PQTools Release Package Directory Description<a name="ZH-CN_TOPIC_0000002498141840"></a>

#### Hi3403V100\_PQ\_Vx.x.x.x.tgz<a name="ZH-CN_TOPIC_0000002498301738"></a>

For this version, please refer to the "[Installation and Operation of Board-Side Software under Linux](#ZH-CN_TOPIC_0000002530221763)" chapter. The directory structure after decompression is shown in [Figure 1](#_ref513797864).

**Figure 1** Directory Structure After Decompression<a name="_ref513797864"></a>  
![](figures/Directory structure after decompression.png "Directory structure after decompression")

-   The configs directory contains sensor configuration files for various business scenarios for ittb_stream (if ittb_stream is not needed, this directory can be deleted to save board space; if only specific scenarios are used, sensor configuration files for other scenarios in this directory can be deleted to save board space)
-   The libs directory contains dynamic library files required for ittb_control and ittb_stream (by default, sensor libraries for all supported scenarios are provided; if only specific scenarios are used, sensor libraries for other scenarios in this directory can be deleted to save board space)
-   config.cfg is the configuration file required for ittb_control and ittb_stream operation
-   PQTools.sh is the script file for running ittb_control and ittb_stream
-   ittb_control and ittb_stream are the business program files
-   StartControl.sh is the script file for quickly restarting ittb_control

#### Hi3403V100\_ext\_api\_Vx.x.x.x.tgz<a name="ZH-CN_TOPIC_0000002530221767"></a>

This release package is used for miniaturized scenarios where some PQTools tool functions are compiled into user applications. The directory structure after decompression is shown in [Figure 1](#_toc51692445).

**Figure 1** Directory Structure After Decompression<a name="_toc51692445"></a>  
![](figures/Directory structure after decompression-0.png "Directory structure after decompression-0")

-   The libbin directory contains header files and library files for the BIN function, along with compiled sample code for user reference.
-   The libcontrol directory contains header files and library files for the control function, along with compiled sample code for user reference.
-   Before compiling the samples for libbin and libcontrol, modify the SDK\_DIR variable in the corresponding Makefile.
-   config.cfg is the configuration file required for control function operation (if libcontrol is compiled into a user application, this file needs to be placed in the runtime directory).

### Installation and Operation of Board-Side Software under Linux<a name="ZH-CN_TOPIC_0000002530221763"></a>

For the steps to burn the chip SDK and configure the board-side tool runtime environment, please refer to the "SSXX SDK Installation and Upgrade Instructions". Burn the image file to the board and configure the network.

1.  Decompress the SSXX\_SDK\_VX.X.X.X.tgz from the release package and place the mpp/ko directory into the file system, or NFS mount the mpp directory from the server to the board file system.
2.  Run the loadXXXX script in the ko directory.
3.  Decompress the SSXX\_PQ\_VX.X.X.X.tgz from the release package. Refer to readme.txt to compile and generate test\_pqt in the sample directory, then copy the files from the sample directory to the file system, or NFS mount them to the board file system.
4.  On the board side, use ./test\_pqt to run a single process that supports both stream and control functions.

## PC Software Installation<a name="ZH-CN_TOPIC_0000002498301772"></a>

The PQTools PC software is a green software. Simply use a decompression tool (such as WinRAR, WinZip, etc.) to extract the PQTools tool archive (zip format) to any writable directory to use it.

## Quick Start<a name="ZH-CN_TOPIC_0000002498301786"></a>

### Welcome Screen<a name="ZH-CN_TOPIC_0000002498301740"></a>

Each time the user launches the tool by running PQTools.exe, a welcome screen will pop up to guide the user in quickly creating a new debugging table and connecting to the board, as shown in [Figure 1](#fig1611913543).

**Figure 1** Welcome Screen Example<a name="fig1611913543"></a>  
![](figures/Welcome screen example.png "Welcome screen example")

To quickly start image quality debugging from this screen, perform the following steps:

1.  Select the correct debugging table template. In the "Load Template" dropdown, select a template that matches the chip name and version number being debugged.
2.  Connect to the board: If using a network connection, select "Network" in the "Connection Type" dropdown, enter the board's IP address in the "IP Address" field, and enter the port number specified when running the board-side program in the "Port" field (default is 4321).

    If using a serial connection to the board, perform the following steps:

    -   First, modify the \[Default\] UartEn field in the config.cfg file of the board-side release package from 0 to 1.
    -   Modify the \[Default\] UartDev field in config.cfg. The default is /dev/ttyAMA0. To switch to serial communication, disable the serial console using the following method (Note: After disabling, you will no longer be able to operate the board via the serial terminal. Make sure that the board's startup script includes the startup process for media services and ittb_control):

        Single Linux system:

        Use the following command to comment out the console initialization action in /etc/inittab, then reboot:

        ```
        sed -i "s/^::respawn:\/sbin\/getty/#::respawn:\/sbin\/getty/g" /etc/inittab 
        reboot
        ```

    -   Select "Serial Port" in the "Connection Type" dropdown on the tool interface, and select the corresponding COM port to connect to the board.

After performing the above operations, click the "OK" button. The tool will read the selected template to generate a debugging table and automatically establish a network connection between the computer and the board. If the network connection is successful, the tool will also automatically read the values of all debugging items from the board. If the serial port opens successfully, the tool will only automatically read the values of the debugging items on the currently displayed page.

>![](public_sys-resources/icon-note.gif) **Note:** 
>-   By default, the tool remembers all information entered by the user each time. If the parameters are only for a one-time temporary debug session and the user does not want the tool to remember them, uncheck the "Remember the selections" checkbox.
>-   If the user does not want the welcome window to appear each time the tool is launched, check "Do not show this dialog when start PQ Tools". If checked, the welcome window will not appear the next time the user starts the tool, and the main tool interface will be displayed directly.

### Tool Main Interface<a name="ZH-CN_TOPIC_0000002530061641"></a>

The tool main interface is shown in [Figure 1](#fig4429101745518).

**Figure 1** Tool Main Interface Example<a name="fig4429101745518"></a>  
![](figures/Tool main interface example.png "Tool main interface example")

The PQTools tool main interface is divided into the following areas by function:

-   (1) Toolbar: Provides shortcut buttons for common operations
-   (2) Debugging table panel: Displays all debuggable items contained in the currently opened debugging table file
-   (3) Debugging area: Clicking a tree node on the left will display the debugging page corresponding to the selected node in this area
-   (4) Advanced function area: Displays communication logs
-   (5) Status bar: Displays prompt text for certain operations

### Common Operations<a name="ZH-CN_TOPIC_0000002530061749"></a>

#### Creating a New Debugging Table<a name="ZH-CN_TOPIC_0000002498301748"></a>

Click the "New" button (![](figures/zh-cn_image_0000002498301892.png)) on the toolbar to create a debugging table for image quality debugging. Clicking the "New" button will bring up the "Create a new PQ table" dialog, as shown in [Figure 1](#fig10817881288).

**Figure 1** Create Debugging Table Dialog<a name="fig10817881288"></a>  
![](figures/Create debugging table dialog.png "Create debugging table dialog")

Select the corresponding debugging table template from the dropdown and click the "OK" button. The tool will create the debugging table. After creation, the tree structure of the current debugging table will be displayed in the debugging table panel area of the main interface (for a detailed description, please refer to "[Interface and Function Description](#ZH-CN_TOPIC_0000002498141848)").

#### Saving Debug Data Files<a name="ZH-CN_TOPIC_0000002498301818"></a>

To save the current debugging table and the debug data read from the board to a file, click the "Save" button (![](figures/zh-cn_image_0000002498141996.png)) on the toolbar. The tool will pop up a path selection dialog. After the user selects a path, the tool will save the current debugging table data.

The saved file format is \*.xml. The debug data file will also include the structure of the debugging table used.

#### Opening Debug Data Files<a name="ZH-CN_TOPIC_0000002498141846"></a>

To load a saved debug data file, click the "Open" button (![](figures/zh-cn_image_0000002498301970.png)) on the toolbar. The tool will pop up a dialog for the user to select the data file to open.

When the tool opens a debug data file, it reads the debugging table structure saved in the file and displays it in the debugging table panel.

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>-   After importing an xml file, switching the adjustable item interface will not automatically fetch board-side data. The adjustable item interface displays the data from the imported file.
>-   After importing an xml file, click the main interface ![](figures/zh-cn_image_0000002530061945.jpg) or ![](figures/zh-cn_image_0000002530221919.jpg) to set the parameters to the board. Alternatively, switch to the adjustable item interface and click ![](figures/zh-cn_image_0000002530061953.jpg) on the debug page to set this set of data to the board.
>-   The data file format exported by the current PQTools version is .xml.
>-   When opening a file, you can choose through the popup whether to only load data or create a new debugging table. Loading data only refreshes the data on the debugging table interface, while creating a new debugging table is equivalent to restarting the tool, simultaneously refreshing external plugins and restoring to the initial state.

#### Undo and Redo<a name="ZH-CN_TOPIC_0000002530221717"></a>

If a debug operation needs to be undone, click the "Undo" button (![](figures/zh-cn_image_0000002498141934.png)) on the toolbar. To redo an undone operation, click the "Redo" button (![](figures/zh-cn_image_0000002530221853.png)) on the toolbar.

#### Opening External Plugins/Programs<a name="ZH-CN_TOPIC_0000002498301780"></a>

The dropdown list (![](figures/zh-cn_image_0000002498301942.png)) on the toolbar lists all currently available external plugins and programs. Click the dropdown and select the plugin/program to use.

The tool only loads plugins supported by the current chip.

>![](public_sys-resources/icon-notice.gif) **Notice:** 
>-   When the tool exits, opened plugins will be closed simultaneously.
>-   Since some external programs depend on connection parameters, if the tool does not have a network connection established with the board, the open operation for external applications will be blocked.

#### Connecting to the Board<a name="ZH-CN_TOPIC_0000002498141806"></a>

Click the "Connect" button (![](figures/zh-cn_image_0000002498301940.png)) on the toolbar. The tool will pop up the board connection wizard dialog, as shown in [Figure 1](#fig611801919308).

**Figure 1** Board Connection Wizard<a name="fig611801919308"></a>  
