---
title: "iTOP-Hi3403 SDK Build Steps"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/vendor/topeet/docs/iTOP-Hi3403 SDK编译步骤.md
---

# iTOP-Hi3403 SDK Build Steps

This document provides detailed instructions for building the iTOP-Hi3403 SDK.

## 1.1 Obtaining the Linux Source Package

**Build environment notes**:

This guide uses the [Ubuntu 20.04](https://pan.baidu.com/s/1duDPKS2fDyGVL1AXBQkbbg?pwd=g8cf) build environment provided by Topeet, which can be downloaded from Baidu Netdisk. Because there are many Ubuntu versions and it is not practical to test all of them, you may need to troubleshoot issues yourself if you use a different development environment.

The [iTOP-Hi3403 SDK source code](https://pan.baidu.com/s/1rba7oNkDRKBTI8UAe4a5Rg?pwd=ppv1) is also available on Baidu Netdisk. Note that the source code is updated incrementally, so the release date shown in the filename may vary; use the actual filename in the Netdisk as the reference.

1. Download the Linux source package from Baidu Netdisk, as shown below:

![image-20260326163839192](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261638213.png)

2. In the Topeet-provided Ubuntu 20.04 virtual machine, create a new directory `/home/topeet/Linux`. Copy `Hi3403_SDK_XXXXXXX.tar.xz` (where XX... is an abbreviated name) into the Linux directory, then extract it with `tar -vxf Hi3403_SDK_XXXXXXX.tar.xz`. After extraction, a `Hi3403_SDK` directory will be created, as shown below:

![image-20260326164321492](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261643522.png)

## 1.2 Building Buildroot

Buildroot is an integrated build system that solves the complexity of cross-compilation and package porting. This section covers the buildroot image build process, including both individual component builds and a full automated build.

### 1.2.1 Individual Component Build

#### **1.2.1.1 Graphical UI**

The build order for individual components in this section is:

Build U-Boot -> Build kernel -> Build buildroot

**Step 1: Build U-Boot**

From the Linux source directory, run the following command to launch the build UI:

~~~bash
./build.sh 
~~~

![image-20260326164720535](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261647565.png)

![image-20260326164754401](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261647435.png)

The cursor defaults to uboot, so press Enter to start the U-Boot build. The build process is shown below:

![image-20260326164812070](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261648104.png)

U-Boot build complete:

![image-20260326164825839](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261648892.png)

After the build, the `u-boot.bin` image is placed in the `output` directory, as shown below:

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701348.png)

**Step 2: Build kernel**

From the Linux source directory, run the following command to launch the build UI:

~~~bash
./build.sh 
~~~

![image-20260326164720535](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701805.png)

![image-20260326164754401](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261706847.png)

Move the cursor to the second item, kernel, and press Enter to start the kernel build. The build process is shown below:

![image-20260326170838515](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261708555.png)

![image-20260326171339964](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261713005.png)

Kernel build complete:

![image-20260326171605701](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716750.png)

The resulting image file `uImage_Hi3403V100` is copied to the `output` directory, as shown below:

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716987.png)

**Step 3: Build buildroot**

From the Linux source directory, run the following command to launch the build UI:

~~~
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701483.png)

![image-20260326170943985](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261709018.png)

Move the cursor to the third item, rootfs, and press Enter to enter the filesystem image selection screen:

![image-20260326170925272](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261709310.png)

![image-20260326171020818](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261710851.png)

There are three image types to choose from. Since this section builds buildroot, move the cursor to buildroot and press Enter to start the build. The build process is shown below:

![image-20260326172127448](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261721527.png)

After the build completes, the generated `rootfs.img` image is copied to the `output` directory, as shown below:

![image-20260327102243499](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271022530.png)

All Hi3403-related images are now built.

#### **1.2.1.2 Command Line**

The build order for individual components in this section is:

Build U-Boot -> Build kernel -> Build buildroot

**Step 1: Build U-Boot**

From the Linux source directory, run the following command to build U-Boot:

~~~bash
./build.sh uboot 
~~~

![image-20260326172815706](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261728748.png)

U-Boot build complete:

![image-20260326164825839](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261648892.png)

After the build, the `u-boot.bin` image is placed in the `output` directory, as shown below:

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701348.png)

**Step 2: Build kernel**

From the Linux source directory, run the following command to build the kernel:

~~~bash
./build.sh kernel 
~~~

![image-20260326173123812](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261731852.png)

Kernel build complete:

![image-20260326171605701](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716750.png)

The resulting image file `uImage_Hi3403V100` is copied to the `output` directory, as shown below:

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716987.png)

**Step 3: Build buildroot**

From the source root directory, run the following command to automatically build and package the rootfs:

~~~
./build.sh buildroot
~~~

![image-20260326173447627](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261734674.png)

After the build completes, the generated `rootfs.img` image is copied to the `output` directory, as shown below:

![image-20260326174743275](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261747303.png)

All Hi3403-related images are now built.

### 1.2.2 Full Automated Build

#### **1.2.2.1 Graphical UI**

From the Linux source directory, run the following command to launch the build UI:

~~~bash
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261735932.png)

![image-20260326174812953](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261748990.png)

Select the fourth item, all, to enter the filesystem type selection screen:

![image-20260326174829699](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261748738.png)

![image-20260326174851998](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261748035.png)

Since this section performs a full automated buildroot build, select buildroot and press Enter. The script will automatically build U-Boot, kernel, and buildroot. Once complete:

![image-20260326174626433](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261746473.png)

All images required for flashing are generated in the `output` directory, as shown below:

![image-20260326174610020](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261746053.png)

#### **1.2.2.2 Command Line**

From the source root directory, run the following command to automatically build everything. To build all components with the buildroot filesystem:

~~~bash
./build.sh buildroot_all
~~~

This command automatically builds U-Boot, kernel, and buildroot. All images required for flashing are generated in the `output` directory, as shown below:

![image-20260326174610020](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261749745.png)

## 1.3 Building Ubuntu

This section covers the Ubuntu image build process, including both individual component builds and a full automated build.

### 1.3.1 Individual Component Build

#### **1.3.1.1 Graphical UI**

The build order for individual components in this section is:

Build U-Boot -> Build kernel -> Build Ubuntu

**Step 1: Build U-Boot**

From the Linux source directory, run the following command to launch the build UI:

~~~bash
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261704299.png)

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261737539.png)

The cursor defaults to uboot, so press Enter to start the U-Boot build. The build process is shown below:

![image-20260326175117352](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261751393.png)

U-Boot build complete:

![image-20260326175138946](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261751000.png)

After the build, the `u-boot.bin` image is placed in the `output` directory, as shown below:

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261752845.png)

**Step 2: Build kernel**

From the Linux source directory, run the following command to launch the build UI:

~~~bash
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261704729.png)

![image-20260326173706882](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261737926.png)

Move the cursor to the second item, kernel, and press Enter to start the kernel build. The build process is shown below:

![image-20260326175352195](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261753238.png)

![image-20260326175413006](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261754041.png)

Kernel build complete:

![image-20260326175431735](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261754781.png)

The resulting image file `uImage_Hi3403V100` is copied to the `output` directory, as shown below:

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261754696.png)

**Step 3: Build Ubuntu**

Move the cursor to the third item, rootfs, and press Enter to enter the filesystem image selection screen:

![image-20260326175511224](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261755262.png)

![image-20260326175528925](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261755964.png)

There are three image types to choose from. Since this section builds Ubuntu, and Ubuntu has two variants — `ubuntu_lite` (desktop-free) and `ubuntu_xfce` (with XFCE desktop) — this guide demonstrates the desktop-free lite variant. Move the cursor to ubuntu_lite and press Enter to start the build. The build process is shown below:

![image-20260326175557743](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261755780.png)

![image-20260326175637317](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261756371.png)

After the build completes, the generated `rootfs.img` image is copied to the `output` directory, as shown below:

![image-20260326175704246](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261757276.png)

All Hi3403-related images are now built.

#### **1.3.1.2 Command Line**

The build order for individual components in this section is:

Build U-Boot -> Build kernel -> Build Ubuntu

**Step 1: Build U-Boot**

From the Linux source directory, run the following command to build U-Boot:

~~~bash
./build.sh uboot 
~~~

![image-20260326175834341](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261758378.png)

U-Boot build complete:

![image-20260326175851461](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261758510.png)

After the build, the `u-boot.bin` image is placed in the `output` directory, as shown below:

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261759160.png)

**Step 2: Build kernel**

From the Linux source directory, run the following command to build the kernel:

~~~bash
./build.sh kernel 
~~~

![image-20260326175947179](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261759217.png)

Kernel build complete:

![image-20260326180002420](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261800457.png)

The resulting image file `uImage_Hi3403V100` is copied to the `output` directory, as shown below:

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261800423.png)

**Step 3: Build Ubuntu**

Ubuntu has two variants: `ubuntu_lite` (desktop-free) and `ubuntu_xfce` (with XFCE desktop). The build commands for each are shown below. This guide demonstrates the desktop-free lite variant:

~~~bash
./build.sh ubuntu_lite
./build.sh ubuntu_xfce
~~~

![image-20260327094931810](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270949879.png)

After the build completes, the generated `rootfs.img` image is copied to the `output` directory, as shown below:

![image-20260327095009919](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270950948.png)

All Hi3403-related images are now built.

### 1.3.2 Full Automated Build

#### **1.3.2.1 Graphical UI**

From the Linux source directory, run the following command to launch the build UI:

~~~c
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270951199.png)

![image-20260327095228807](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270952843.png)

Select the fourth item, all, to enter the filesystem type selection screen:

![image-20260327095335690](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270953729.png)

![image-20260327095349051](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270953087.png)

There are three image types to choose from. Since this section builds Ubuntu, and Ubuntu has two variants — `ubuntu_lite` (desktop-free) and `ubuntu_xfce` (with XFCE desktop) — this guide demonstrates the desktop-free lite variant. Move the cursor to ubuntu_lite and press Enter to start the build. The build process is shown below:

![image-20260327095646998](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270956032.png)

All images required for flashing are generated in the `output` directory, as shown below:

![image-20260327095715932](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270957962.png)

#### **1.3.2.2 Command Line**

Ubuntu has two variants: `ubuntu_lite` (desktop-free) and `ubuntu_xfce` (with XFCE desktop). The full automated build commands for each are:

~~~bash
./build.sh ubuntu_lite_all
./build.sh ubuntu_xfce_all
~~~

These commands automatically build U-Boot, kernel, and Ubuntu. All images required for flashing are generated in the `output` directory, as shown below:

![image-20260327095715932](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271002849.png)
