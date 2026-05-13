## 2.5. face_detection Operation Guide

### 2.5.1. face_detection Program Introduction

* The face_detection sample is developed based on the Hi3403V100 platform, using the EulerPi kit as an example. The face_detection sample captures images via a USB camera and feeds them into a face detection model for inference. When a face is detected, a rectangle is drawn around the face area and displayed in real-time on an external display via an HDMI cable.
* The face_detection case primarily uses the PyTorch framework, based on the YoloV8 network, using open-source datasets such as widerface, FDDB, and UFDD — a total of over 13,000 images — to train a face detection model that works under strong light, backlight, and low light conditions.

### 2.5.2. Directory Structure

```shell
pegasus/vendor/zsks/demo/face_detection
|── data                 # model files
|── Makefile             # compilation script
└── face_detection.c     # face_detection sample application code
```

![image-20250919144926220](pic/image-20250919144926220.png)

* Configure according to the output parameters of the external display. For example, if the external display outputs 1080P60, and the intf_sync in the sample_common_svp_get_def_vo_cfg function in smp/a55_linux/mpp/sample/svp/common/sample_common_svp.c is OT_VO_OUT_1080P30, change it to OT_VO_OUT_1080P60.

![image-20251023102053075](pic/image-20251023102053075.png)

### 2.5.3. Compilation

* **Note: Before compiling ZSKS demos, ensure you have applied the patches to the corresponding directories as described in [the development guide](../../../index.md#2-development-guide)**.

* Step 1: Navigate to the corresponding Pegasus directory based on your chosen operating system.

* Step 2: Use the Makefile for individual compilation.

* In the Ubuntu command line terminal, execute the following commands step by step to individually compile the face_detection sample.

* Adding the LLVM=1 parameter to the compilation command uses the clang toolchain, while LLVM=0 uses the gcc toolchain. Without the LLVM parameter, the gcc toolchain is used by default. The current development board system uses clang, so this guide uniformly uses the LLVM=1 parameter for compilation.

  ```
  cd pegasus/vendor/zsks/demo/face_detection
  
  make LLVM=1 clean && make LLVM=1
  ```

  * An executable named main is generated in the face_detection/out directory, as shown below:

  ![image-20251231153903404](pic/image-20251231153903404.png)
  
  ![image-20251231153931716](pic/image-20251231153931716.png)

### 2.5.4. Copying Executable and Dependency Files to the Development Board's mnt Directory

**Method 1: Using an SD Card for File Copying**

* First, prepare a Micro SD card (about 16GB) and a Micro SD card reader.

<img src="pic/image-20221114150205685.png" alt="image-20221114150205685" style="zoom:50%;" />

* Step 1: Copy the compiled executable main and resource file data to the SD card.

![image-20251023100347550](pic/image-20251023100347550.png)

* Step 2: After the executable is successfully copied, insert the SD card into the development board's SD card slot and mount it on the board using the SD card mount command.

<img src="pic/image-20250210161601541.png" alt="image-20250210161601541" style="zoom:67%;" />

* In the development board's terminal, execute the following command to mount the SD card:
  * If mounting fails, refer to [this issue for resolution](https://gitee.com/HiSpark/HiSpark_NICU2022/issues/I54932?from=project-issue)


```shell
mount -t vfat /dev/mmcblk1p1 /mnt
# where /dev/mmcblk1p1 should be modified according to the actual block device number
```

* After successful mounting, the result is shown below:

![image-20251023102549783](pic/image-20251023102549783.png)

**Method 2: Using NFS Mount for File Copying**

* First, prepare a network cable.
* Step 1: Refer to the [blog link](https://blog.csdn.net/Wu_GuiMing/article/details/115872995?spm=1001.2014.3001.5501) for setting up the NFS environment.
* Step 2: Copy the compiled executable main and resource file data to the Windows NFS shared path.

![image-20251023100136196](pic/image-20251023100136196.png)

* Step 3: In the development board's terminal, execute the following command to mount the Windows NFS shared path to the development board's mnt directory:
  * Note: Fill in the IP address according to the actual IP addresses of your development board and host PC.


```
ifconfig eth0 192.168.100.100

mount -o nolock,addr=192.168.100.10 -t nfs 192.168.100.10:/d/nfs /mnt
```

![image-20251023101210815](pic/image-20251023101210815.png)

### 2.5.5. Hardware Connection

* Prepare an external display and an HDMI cable. Connect one end of the HDMI cable to the development board's HDMI output port and the other end to the external display's HDMI input port.

![image-20250213112932380](pic/image-20250213112932380.png)

* Connect the USB camera to the USB port of the EulerPi development board.

<img src="pic/image-20250919150630870.png" alt="image-20250919150630870"  />

### 2.5.6. Functional Verification

* In the development board's terminal, execute the following command to run the executable:

```
cd /mnt

chmod +x main

./main
```

![image-20251023101503216](pic/image-20251023101503216.png)

* At this point, a real-time video stream will appear on the external HDMI display, as shown below:

<img src="pic/image-20250210170027454.png" alt="image-20250210170027454" style="zoom:50%;" />

* If you see a different result from the image below, verify that the USB camera is connected to the development board's USB port and that video0 and video1 device nodes are visible in the /dev directory on the development board. If these two device nodes are not present, ensure that the image has been flashed correctly.

![image-20250919151018659](pic/image-20250919151018659.png)

* Under normal conditions, you will see face areas framed on the external display, and faces can be detected well even in dark or strong backlight conditions. ![image-20250919151605632](pic/image-20250919151605632.png)

* Press Enter twice to exit the program.

![image-20250919151519310](pic/image-20250919151519310.png)
