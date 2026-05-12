## 2.3、fruit_identify操作指导

### 2.3.1、fruit_identify程序简介

* fruit_identify sample基于Hi3403V100平台开发，以EulerPi套件为例，fruit_identify sample是通过USB Camera，将采集到的图片送到水果检测模型中进行推理，当检测到特定水果时，会通过外接显示屏实时显示水果的种类以及执行度，并框住水果的具体位置，并通过耳机播放出此时识别到的水果类别。
* fruit_identify案例主要是使用pytorch框架，基于YoloV8网络，使用自行标注的水果数据集训练出来的水果分类模型。

### 2.3.2、目录

```shell
pegasus/vendor/zsks/demo/fruit_identify 
|── common               # 基于海思mpp/sample中的svp/common/目录下修改的代码，新增了OSD部分的内容
|── data                 # 模型文件和汉字库
|── fruit_audio          # 不同水果的音频文件
|── Makefile             # 编译脚本
|── fruit_identify.c     # fruit_identif sample业务代码
|── sample_audio.c       # 音频播放的业务代码
└── sample_audio.h       # 音频播放的头文件
```

![image-20250919173612332](pic/image-20250919173612332.png)

### 2.3.3、编译

* **注意：在编译zsks的demo之前，请确保你已经按照[开发指南中的步骤](../../../index.md#2开发指南)把补丁打入对应目录下了**。

* 步骤1：先根据自己选择的操作系统，进入到对应的Pegasus所在目录下。

* 步骤2：使用Makefile的方式进行单编

* 在Ubuntu的命令行终端，分步执行下面的命令，单编 fruit_identify sample

* 编译命令添加LLVM=1参数可使用clang工具链编译，而LLVM=0参数可使用gcc工具链编译，不使用LLVM参数默认使用gcc工具链编译，当前开发板系统对应clang，所以本教程统一使用LLVM=1参数编译。

  ```
  cd pegasus/vendor/zsks/demo/fruit_identify
  
  make LLVM=1 clean && make LLVM=1
  ```

  * 在fruit_identify/out目录下，生成一个名为main的 可执行文件，如下图所示：

  ![image-20251231154526977](pic/image-20251231154526977.png)

![image-20251231154554388](pic/image-20251231154554388.png)

### 2.3.4、拷贝可执行程序和依赖文件至开发板的mnt目录下

**方式一：使用SD卡进行资料文件的拷贝**

* 首先需要自己准备一张Micro sd卡(16G 左右即可)，还得有一个Micro sd卡的读卡器。

<img src="pic/image-20221114150205685.png" alt="image-20221114150205685" style="zoom:50%;" />

* 步骤1：将编译后生成的可执行文件、data目录（里面有模型和字库），音频文件都拷贝到SD卡中。

![image-20251023103623167](pic/image-20251023103623167.png)

* 步骤2：可执行文件拷贝成功后，将内存卡插入开发板的SD卡槽中，可通过挂载的方式挂载到板端，可选择SD卡 mount指令进行挂载。

<img src="pic/image-20250210161601541.png" alt="image-20250210161601541" style="zoom:67%;" />

* 在开发板的终端，执行下面的命令进行SD卡的挂载
  * 如果挂载失败，可以参考[这个issue尝试解决](https://gitee.com/HiSpark/HiSpark_NICU2022/issues/I54932?from=project-issue)


```shell
mount -t vfat /dev/mmcblk1p1 /mnt
# 其中/dev/mmcblk1p1需要根据实际块设备号修改
```

* 挂载成功后，如下图所示：

![image-20251023103850695](pic/image-20251023103850695.png)

**方式二：使用NFS挂载的方式进行资料文件的拷贝**

* 首先需要自己准备一根网线
* 步骤1：参考[博客链接](https://blog.csdn.net/Wu_GuiMing/article/details/115872995?spm=1001.2014.3001.5501)中的内容，进行nfs的环境搭建
* 步骤2：将编译后生成的可执行文件、data目录（里面有模型和字库），音频文件都拷贝到Windows的nfs共享路径下

![image-20251023103700404](pic/image-20251023103700404.png)

* 步骤3：在开发板的终端执行下面的命令，将Windows的nfs共享路径挂载至开发板的mnt目录下	
  * 注意：这里IP地址请根据你开发板和电脑主机的实际IP地址进行填写


```
ifconfig eth0 192.168.100.100

mount -o nolock,addr=192.168.100.10 -t nfs 192.168.100.10:/d/nfs /mnt
```

![image-20251023103944837](pic/image-20251023103944837.png)

### 2.3.5、硬件连接

* 准备一个外接显示器和HDMI数据线，将HDMI的一头接在开发板的HDMI输出口，将HDMI的另外一头接在外接显示器的HDMI输入口。

![image-20250213112932380](pic/image-20250213112932380.png)

* 将USB 摄像头接在EulerPi开发板的USB接口上。

<img src="pic/image-20250919150630870.png" alt="image-20250919150630870" style="zoom: 25%;" />

### 2.3.6、功能验证

* 在开发板的终端执行下面的命令，运行可执行文件

```
cd /mnt

chmod +x main

./main
```

![image-20251023110809454](pic/image-20251023110809454.png)

* 此时，在HDMI的外接显示屏上即可出现实时码流，如下图所示：

<img src="pic/image-20250210170027454.png" alt="image-20250210170027454" style="zoom:50%;" />

* 如果您看到的现象和下图现象不一致，可以确认一下USB摄像头是否插入到开发板的USB口，并且在开发板的/dev目录下能够看到video0 和 video1两个设备节点。如果没有这两个设备节点，请确保镜像烧录正常。

![image-20250919151018659](pic/image-20250919151018659.png)

* 正常情况下，我们会在外接显示屏上看到有水果的区域被框出来。且在框框的左上角显示水果的种类和置信度，并且你可以在开发板上面接上耳机，可以听到检测到的水果的具体语音播报。

![image-20250919180706355](pic/image-20250919180706355.png)

* 敲两下回车即可关闭程序

![image-20250919151519310](pic/image-20250919151519310.png)