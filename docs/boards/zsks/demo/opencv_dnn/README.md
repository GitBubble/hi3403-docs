## 2.1、opencv_dnn操作指导

### 2.1.1、opencv_dnn程序简介

* opencv_dnn sample基于SS928V100平台开发，以EulerPi套件为例，opencv_dnn sample是通过USB camera采集到的图片送到人脸检测模型进行推理，将得到的结果通过HDMI，显示在外接显示屏上面。
* opencv_dnn案例，模型推理是在CPU上实现了，没有调用svp_npu的接口，都是调用opencv的接口来实现。

### 2.1.2、目录

```shell
pegasus/vendor/zsks/demo/opencv_dnn 
|── media_vdec.c         # 主要是将推理的结果在HDMI外接显示器上显示
|── media_vdec.h          
|── Makefile             # 编译脚本
|── main.cpp             # opencv_dnn sample业务代码
|── host_uvc.c           #参考海思SDK的host_uvc代码
└── host_uvc.h       
```

![image-20250919181207847](pic/image-20250919181207847.png)

* 请在opencv_dnn目录下创建一个onnx的文件夹，然后访问链接下载[onnx模型](https://github.com/opencv/opencv_zoo/blob/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx)，并放入onnx目录下

![image-20251015164912907](pic/image-20251015164912907.png)

![image-20251015165024778](pic/image-20251015165024778.png)

### 2.1.3、编译

* **注意：在编译zsks的demo之前，请确保你已经按照[开发指南中的步骤](../../../index.md#2开发指南)把补丁打入对应目录下了**。

* 步骤1：先根据自己选择的操作系统，进入到对应的Pegasus所在目录下。

* 步骤2：使用Makefile的方式进行单编

* 在Ubuntu的命令行终端，分步执行下面的命令，单编 opencv_dnn sample

* 编译命令添加LLVM=1参数可使用clang工具链编译，而LLVM=0参数可使用gcc工具链编译，不使用LLVM参数默认使用gcc工具链编译，当前开发板系统对应clang，所以本教程统一使用LLVM=1参数编译。

  ```
  cd pegasus/vendor/zsks/demo/opencv_dnn
  
  make LLVM=1 clean && make LLVM=1
  ```

  * 在opencv_dnn/out目录下，生成一个名为main的可执行文件，如下图所示：

  ![image-20251231154118407](pic/image-20251231154118407.png)

![image-20251231154144577](pic/image-20251231154144577.png)

### 2.1.4、拷贝可执行程序和依赖文件至开发板的mnt目录下

**方式一：使用SD卡进行资料文件的拷贝**

* 首先需要自己准备一张Micro sd卡(16G 左右即可)，还得有一个Micro sd卡的读卡器。

<img src="/boards/zsks/demo/opencv_dnn/pic/image-20221114150205685.png" alt="image-20221114150205685" style="zoom:50%;" />

* 步骤1：将编译后生成的可执行文件、onnx模型文件、opencv的lib文件都拷贝到SD卡中。

![image-20251023112130092](pic/image-20251023112130092.png)

* 步骤2：可执行文件拷贝成功后，将内存卡插入开发板的SD卡槽中，可通过挂载的方式挂载到板端，可选择SD卡 mount指令进行挂载。

<img src="/boards/zsks/demo/opencv_dnn/pic/image-20250210161601541.png" alt="image-20250210161601541" style="zoom:67%;" />

* 在开发板的终端，执行下面的命令进行SD卡的挂载
  * 如果挂载失败，可以参考[这个issue尝试解决](https://gitee.com/HiSpark/HiSpark_NICU2022/issues/I54932?from=project-issue)


```shell
mount -t vfat /dev/mmcblk1p1 /mnt
# 其中/dev/mmcblk1p1需要根据实际块设备号修改
```

* 挂载成功后，如下图所示：

![image-20251023112228717](pic/image-20251023112228717.png)

**方式二：使用NFS挂载的方式进行资料文件的拷贝**

* 首先需要自己准备一根网线
* 步骤1：参考[博客链接](https://blog.csdn.net/Wu_GuiMing/article/details/115872995?spm=1001.2014.3001.5501)中的内容，进行nfs的环境搭建
* 步骤2：将编译后生成的可执行文件、onnx模型文件、opencv库（在pegasus/vendor/opensource/opencv/lib目录下）都拷贝到Windows的nfs共享路径下

![image-20251023112328619](pic/image-20251023112328619.png)

* 步骤3：在开发板的终端执行下面的命令，将Windows的nfs共享路径挂载至开发板的mnt目录下	
  * 注意：这里IP地址请根据你开发板和电脑主机的实际IP地址进行填写


```
ifconfig eth0 192.168.100.100

mount -o nolock,addr=192.168.100.10 -t nfs 192.168.100.10:/d/nfs /mnt
```

![image-20251023112352692](pic/image-20251023112352692.png)

### 2.1.5、硬件连接

* 准备一个外接显示器和HDMI数据线，将HDMI的一头接在开发板的HDMI输出口，将HDMI的另外一头接在外接显示器的HDMI输入口。

![image-20250213112932380](pic/image-20250213112932380.png)

* 将USB 摄像头接在EulerPi开发板的USB接口上。

<img src="/boards/zsks/demo/opencv_dnn/pic/image-20250919150630870.png" alt="image-20250919150630870" style="zoom: 25%;" />

### 2.1.6、功能验证

* 在开发板的终端执行下面的命令，运行可执行文件

```c
# 把opencv的库添加到环境变量中
export LD_LIBRARY_PATH=/mnt/lib:$LD_LIBRARY_PATH

cd /mnt/lib/  
    
ln -s libopencv_world.so  libopencv_world.so.413

cd /mnt

    
chmod +x main

./main  /dev/media0  -fMJPEG -s1920x1080 -Ftest.mjpg
```

![image-20251023112451423](pic/image-20251023112451423.png)

* 此时，在HDMI的外接显示屏上即可出现实时码流，如下图所示：

<img src="/boards/zsks/demo/opencv_dnn/pic/image-20250210170027454.png" alt="image-20250210170027454" style="zoom:50%;" />

* 如果您看到的现象和下图现象不一致，可以确认一下USB摄像头是否插入到开发板的USB口，并且在开发板的/dev目录下能够看到video0 和 video1两个设备节点。如果没有这两个设备节点，请确保镜像烧录正常。

![image-20250919151018659](pic/image-20250919151018659.png)

* 正常情况下，我们会在外接显示屏上看到有人脸的区域被框出来，且在框框的左上角显示置信度。

![image-20250919183224310](pic/image-20250919183224310.png)

* Ctrl + C，然后回车即可关闭程序

![image-20250919151519310](pic/image-20250919151519310.png)