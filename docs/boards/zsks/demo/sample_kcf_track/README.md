## 2.4、sample_kcf_track操作指导

### 2.4.1、sample_kcf_track程序简介

* sample_kcf_track 基于Hi3403V100平台开发，以EulerPi套件为例，sample_kcf_track 基于KCF+Track模型，通过USB Camera，将采集到的图片送到KCF+trak模型，实现对目标的实时跟踪效果。

### 2.4.2、目录

```shell
pegasus/vendor/zsks/demo/sample_kcf_track 
|── main.c               # sample_kcf_track的主入口
|── Makefile             # 编译脚本
|── sample_kcf_track.c   # sample_kcf_track业务代码
|── sample_kcf_track.h   # sample_kcf_track业务代码头文件
|── sample_svp_npu_process.c   # 调用SVP_NPU的业务代码
└── sample_svp_npu_process.c   # 调用SVP_NPU的头文件
```

![image-20250919184816530](pic/image-20250919184816530.png)

* 根据外接显示屏的输出参数进行配置，比如说我的外接显示屏的输出是1080P60，如果smp/a55_linux/mpp/sample/svp/common/sample_common_svp.c sample_common_svp_get_def_vo_cfg函数的intf_sync为OT_VO_OUT_1080P30，则需要把他修改为OT_VO_OUT_1080P60。

![image-20251023102053075](pic/image-20251023102053075.png)

### 2.4.3、编译

* **注意：在编译zsks的demo之前，请确保你已经按照[开发指南中的步骤](../../../index.md#2开发指南)把补丁打入对应目录下了**。

* 步骤1：先根据自己选择的操作系统，进入到对应的Pegasus所在目录下。

* 步骤2：使用Makefile的方式进行单编

* 在Ubuntu的命令行终端，分步执行下面的命令，单编 sample_kcf_track 

* 编译命令添加LLVM=1参数可使用clang工具链编译，而LLVM=0参数可使用gcc工具链编译，不使用LLVM参数默认使用gcc工具链编译，当前开发板系统对应clang，所以本教程统一使用LLVM=1参数编译。

  ```
  cd pegasus/vendor/zsks/demo/sample_kcf_track
  
  make LLVM=1 clean && make LLVM=1
  ```

  * 在sample_kcf_track/out目录下，生成一个名为main的可执行文件，如下图所示：

  ![image-20251231155023771](pic/image-20251231155023771.png)
  
  ![image-20251231155047164](pic/image-20251231155047164.png)

### 2.4.4、拷贝可执行程序和依赖文件至开发板的mnt目录下

**方式一：使用SD卡进行资料文件的拷贝**

* 首先需要自己准备一张Micro sd卡(16G 左右即可)，还得有一个Micro sd卡的读卡器。

<img src="pic/image-20221114150205685.png" alt="image-20221114150205685" style="zoom:50%;" />

* 步骤1：将编译后生成的可执行文件main，拷贝到SD卡中。

![image-20251023100505047](pic/image-20251023100505047.png)

* 步骤2：可执行文件拷贝成功后，将内存卡插入开发板的SD卡槽中，可通过挂载的方式挂载到板端，可选择SD卡 mount指令进行挂载。

<img src="pic/image-20250210161601541.png" alt="image-20250210161601541" style="zoom:67%;" />

* 在开发板的终端，执行下面的命令进行SD卡的挂载
  * 如果挂载失败，可以参考[这个issue尝试解决](https://gitee.com/HiSpark/HiSpark_NICU2022/issues/I54932?from=project-issue)


```shell
mount -t vfat /dev/mmcblk1p1 /mnt
# 其中/dev/mmcblk1p1需要根据实际块设备号修改
```

* 挂载成功后，如下图所示：

![image-20251023114317633](pic/image-20251023114317633.png)

**方式二：使用NFS挂载的方式进行资料文件的拷贝**

* 首先需要自己准备一根网线
* 步骤1：参考[博客链接](https://blog.csdn.net/Wu_GuiMing/article/details/115872995?spm=1001.2014.3001.5501)中的内容，进行nfs的环境搭建
* 步骤2：将编译后生成的可执行文件main，拷贝到Windows的nfs共享路径下

![image-20251023100536744](pic/image-20251023100536744.png)

* 步骤3：在开发板的终端执行下面的命令，将Windows的nfs共享路径挂载至开发板的mnt目录下	
  * 注意：这里IP地址请根据你开发板和电脑主机的实际IP地址进行填写


```
ifconfig eth0 192.168.100.100

mount -o nolock,addr=192.168.100.10 -t nfs 192.168.100.10:/d/nfs /mnt
```

![image-20251023114345977](pic/image-20251023114345977.png)

### 2.4.5、硬件连接

* 准备一个外接显示器和HDMI数据线，将HDMI的一头接在开发板的HDMI输出口，将HDMI的另外一头接在外接显示器的HDMI输入口。

![image-20250213112932380](pic/image-20250213112932380.png)

* 将USB 摄像头接在EulerPi开发板的USB接口上。

<img src="pic/image-20250919150630870.png" alt="image-20250919150630870" style="zoom: 25%;" />

### 2.4.6、功能验证

* 在开发板的终端执行下面的命令，运行可执行文件

```
cd /mnt

chmod +x main

./main
```

![image-20251023114430657](pic/image-20251023114430657.png)

* 此时，在HDMI的外接显示屏上即可出现实时码流，如下图所示：

<img src="pic/image-20250210170027454.png" alt="image-20250210170027454" style="zoom:50%;" />

* 如果您看到的现象和下图现象不一致，可以确认一下USB摄像头是否插入到开发板的USB口，并且在开发板的/dev目录下能够看到video0 和 video1两个设备节点。如果没有这两个设备节点，请确保镜像烧录正常。

![image-20250919151018659](pic/image-20250919151018659.png)

* 正常情况下，我们会在外接显示屏上看到USB Camera采集到的画面。
* 步骤1：按下键盘的空格键，会在屏幕的正中间显示一个红色的框框。

![image-20250919192349341](pic/image-20250919192349341.png)

* 步骤2：把需要跟踪的目标放在红色框框内，然后再按一下空格键，此时红色框会变绿，如果没有变，可以重复一次。
* 步骤3：移动需要跟踪的目标，绿色框会跟着目标一起移动。

![image-20250919192115350](pic/image-20250919192137187.png)

* 当目标不在sensor视野范围内，绿框会变成黄色。

![image-20250919192243361](pic/image-20250919192243361.png)

* 输入Q键，即可关闭程序

![image-20250919151519310](pic/image-20250919151519310.png)