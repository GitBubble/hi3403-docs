---
title: "iTOP-Hi3403 SDK编译步骤"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/vendor/topeet/docs/iTOP-Hi3403 SDK编译步骤.md
---

# iTOP-Hi3403 SDK编译步骤

本文档对使用iTOP-Hi3403 SDK 的编译步骤进行详细的说明。

## 1.1 获取Linux源码包

**编译环境说明**：

本手册使用的是迅为提供 的编译环境[Ubuntu20.04](https://pan.baidu.com/s/1duDPKS2fDyGVL1AXBQkbbg?pwd=g8cf )，可通过百度网盘链接进行下载，因Ubuntu版本众多，无法将所有版本Ubuntu全部测试通过，如使用其他开发环境，在开发过程中遇到问题，需自行研究解决。

 [iTOP-Hi3403 SDK源码](https://pan.baidu.com/s/1rba7oNkDRKBTI8UAe4a5Rg?pwd=ppv1)也可通过百度网盘链接进行下载，需要注意的源码会逐渐更新，发布的源码日期会有所不同，具体以网盘中实际名称为准。

1 从百度网盘中下载Linux源码包，如下图所示：

![image-20260326163839192](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261638213.png)

2然后在迅为提供的虚拟机Ubuntu20.04中，新建一个/home/topeet/Linux文件夹，我们将Hi3403_SDK_XXXXXXX.tar.xz（XX...为名称的简写）拷贝到Linux文件夹中，使用命令“tar -vxf Hi3403_SDK_XXXXXXX.tar.xz（XX...为名称的简写）”解压压缩包。解压后会生成一个Hi3403_SDK文件夹，如下图所示:

![image-20260326164321492](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261643522.png)

 ##  1.2 编译 buildroot 

Buildroot是一款集成的编译集合包，解决了软件包移植和交叉编译麻烦的问题，本小节将介绍buildroot镜像的编译流程，分为单独编译和完整全自动编译。

### 1.2.1 单独编译

#### **1.2.1.1 图形化界面**

本小节单独编译镜像的顺序如下所示：

单独编译uboot ->单独编译kernel ->单独编译buildroot

第一步：编译uboot

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~bash
./build.sh 
~~~

![image-20260326164720535](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261647565.png)

![image-20260326164754401](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261647435.png)

 光标默认就在uboot，所以直接回车即可开始uboot的编译，编译过程如下所示：

![image-20260326164812070](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261648104.png)

 Uboot编译完成如下图所示：

![image-20260326164825839](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261648892.png)

 编译完成后会生成u-boot.bin镜像，存放在output目录下，如下图所示：

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701348.png)

 第二步：编译kernel

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~bash
./build.sh 
~~~

![image-20260326164720535](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701805.png)

![image-20260326164754401](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261706847.png)

 然后将光标移动到第二个kernel，点击回车即可开始kernel内核的编译，编译过程如下所示：

![image-20260326170838515](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261708555.png)

![image-20260326171339964](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261713005.png)

 内核编译完如下图所示：

![image-20260326171605701](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716750.png)

 编译完成后的镜像文件uImage_ss928v100会放到output目录，如下图所示

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716987.png)

 第三步：编译buildroot

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701483.png)

![image-20260326170943985](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261709018.png)

 然后将光标移动到第三个rootfs，点击回车会进入到文件系统镜像选择界面，如下图所示：
![image-20260326170925272](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261709310.png)

![image-20260326171020818](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261710851.png)

 这里总共有三种镜像供编译选择，由于本小节要编译的是buildroot，所以将光标移动到buildroot按下回车即可开始buildroot镜像的构建，构建过程如下所示：

![image-20260326172127448](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261721527.png)

 构建完成之后，生成的镜像rootfs.img会拷贝到output目录下，如下图所示：

![image-20260327102243499](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271022530.png)

 至此，关于Hi3403的相关镜像就编译完成了。

#### **1.2.1.2 命令行**

本小节单独编译镜像的顺序如下所示：

单独编译uboot ->单独编译kernel ->单独编译buildroot

第一步：编译uboot

在linux源码目录下输入以下命令编译U-Boot

~~~bash
./build.sh uboot 
~~~

![image-20260326172815706](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261728748.png)

  Uboot编译完成如下图所示：

![image-20260326164825839](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261648892.png)

 编译完成后会生成u-boot.bin镜像，存放在output目录下，如下图所示：

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261701348.png)

 第二步：编译kernel

在linux源码目录下输入以下命令编译 Kernel

~~~bash
./build.sh kernel 
~~~

![image-20260326173123812](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261731852.png)

  内核编译完如下图所示：

![image-20260326171605701](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716750.png)

 编译完成后的镜像文件uImage_ss928v100会放到output目录，如下图所示

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261716987.png)

 第三步：编译buildroot

进入源码根目录执行以下命令自动完成 Rootfs 的编译及打包，编译过程如下所示：

~~~
./build.sh buildroot
~~~

![image-20260326173447627](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261734674.png)

 构建完成之后，生成的镜像rootfs.img会拷贝到output目录下，如下图所示：

![image-20260326174743275](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261747303.png)

 至此，关于Hi3403的相关镜像就编译完成了。

### 1.2.2 全自动编译

#### **1.2.2.1 图形化界面**

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~bash
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261735932.png)

![image-20260326174812953](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261748990.png)

  然后选择第四个all，就会进入到文件系统类型选择页面，如下所示：
![image-20260326174829699](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261748738.png) 

![image-20260326174851998](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261748035.png)

由于本小节全自动编译的是buildroot系统，所以这里选择buildroot，然后回车，等待编译完成即可，脚本会自动编译uboot kernel buildroot,编译完成之后如下所示：
![image-20260326174626433](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261746473.png)	在output目录就生成了烧写所需要的各个镜像，如下图所示：
![image-20260326174610020](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261746053.png)

#### **1.2.2.2 命令行**

进入源码根目录执行以下命令自动完成所有的编译。如果想自动全编译buildroot文件系统，输入以下命令：

~~~bash
./build.sh buildroot_all
~~~

输入上面的命令后，会自动编译uboot kernel buildroot,编译完成之后会在output目录生成烧写所需要的各个镜像，如下图所示：

![image-20260326174610020](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261749745.png)

 ##  1.3 编译 Ubuntu

本小节将介绍ubuntu镜像的编译流程，分为单独编译和完整全自动编译。

### 1.3.1 单独编译

#### **1.3.1.1 图形化界面**

本小节单独编译镜像的顺序如下所示：

单独编译uboot ->单独编译kernel ->单独编译ubuntu

第一步：编译uboot

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~bash
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261704299.png)

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261737539.png)

 光标默认就在uboot，所以直接回车即可开始uboot的编译，编译过程如下所示：

![image-20260326175117352](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261751393.png)

 Uboot编译完成如下图所示：

![image-20260326175138946](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261751000.png)

 编译完成后会生成u-boot.bin镜像，存放在output目录下，如下图所示：

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261752845.png)

第二步：编译kernel

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~bash
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261704729.png)

![image-20260326173706882](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261737926.png)

 然后将光标移动到第二个kernel，点击回车即可开始kernel内核的编译，编译过程如下所示：

![image-20260326175352195](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261753238.png)

![image-20260326175413006](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261754041.png)

 内核编译完如下图所示：

![image-20260326175431735](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261754781.png)

 编译完成后的镜像文件uImage_ss928v100会放到output目录，如下图所示

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261754696.png)

 第三步：构建Ubuntu

然后将光标移动到第三个rootfs，点击回车会进入到文件系统镜像选择界面，如下图所示：
![image-20260326175511224](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261755262.png) 

![image-20260326175528925](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261755964.png)

这里总共有三种镜像供编译选择，由于本小节要编译的是ubuntu，ubuntu有两个版本，分别是无桌面的lite版本和有桌面的xfce版本，本小节以编译无桌面的lite版本为例进行演示，所以将光标移动到ubuntu_lite,然后按下回车即可开始ubuntu镜像的构建，构建过程如下所示：

![image-20260326175557743](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261755780.png)

![image-20260326175637317](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261756371.png)

 构建完成之后，生成的镜像rootfs.img会拷贝到output目录下，如下图所示：

![image-20260326175704246](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261757276.png)

 至此，关于Hi3403的相关镜像就编译完成了。

#### **1.3.1.2 命令行**

本小节单独编译镜像的顺序如下所示：

单独编译uboot ->单独编译kernel ->单独编译buildroot

第一步：编译uboot

在linux源码目录下输入以下命令编译U-Boot

~~~bash
./build.sh uboot 
~~~

![image-20260326175834341](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261758378.png)

 Uboot编译完成如下图所示：

![image-20260326175851461](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261758510.png)

 编译完成后会生成u-boot.bin镜像，存放在output目录下，如下图所示：

![image-20260326170129316](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261759160.png)

  第二步：编译kernel

在linux源码目录下输入以下命令编译 Kernel

~~~bash
./build.sh kernel 
~~~

![image-20260326175947179](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261759217.png)

 内核编译完如下图所示：

![image-20260326180002420](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261800457.png)

 编译完成后的镜像文件uImage_ss928v100会放到output目录，如下图所示

![image-20260326171629958](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603261800423.png)

 第三步：编译ubuntu

ubuntu有两个版本，分别是无桌面的lite版本和有桌面的xfce版本，两个版本ubuntu的编译命令如下所示，本小节以lite无桌面版本镜像的编译为例进行演示，编译过程如下图所示： 

~~~bash
./build.sh ubuntu_lite
./build.sh ubuntu_xfce
~~~

![image-20260327094931810](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270949879.png)

 构建完成之后，生成的镜像rootfs.img会拷贝到output目录下，如下图所示：

![image-20260327095009919](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270950948.png)

 至此，关于Hi3403的相关镜像就编译完成了。

### 1.3.2 全自动编译

#### **1.3.2.1 图形化界面**

首先在linux源码目录下输入以下命令进入编译的UI界面，进入之后如下所示：

~~~c
./build.sh 
~~~

![](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270951199.png)

![image-20260327095228807](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270952843.png)

  然后选择第四个all，就会进入到文件系统类型选择页面，如下所示：
![image-20260327095335690](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270953729.png)

![image-20260327095349051](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270953087.png)

 这里总共有三种镜像供编译选择，由于本小节要编译的是ubuntu，ubuntu有两个版本，分别是无桌面的lite版本和有桌面的xfce版本，本小节以编译无桌面的lite版本为例进行演示，所以将光标移动到ubuntu_lite,然后按下回车即可开始ubuntu镜像的构建，构建过程如下所示：
![image-20260327095646998](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270956032.png)

​	在output目录就生成了烧写所需要的各个镜像，如下图所示：
![image-20260327095715932](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603270957962.png)

#### **1.3.2.2 命令行**

ubuntu有两个版本，分别是无桌面的lite版本和有桌面的xfce版本，两个版本ubuntu镜像的整体编译命令如下所示：

~~~bash
./build.sh ubuntu_lite_all
./build.sh ubuntu_xfce_all
~~~

输入上面的命令后，会自动编译uboot kernel ubuntu,编译完成之后会在output目录生成烧写所需要的各个镜像，如下图所示：

![image-20260327095715932](https://chai-1301855619.cos.ap-beijing.myqcloud.com/202603271002849.png)

 