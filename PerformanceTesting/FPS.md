# FPS

无论是手机端还是PC端，**画面的流畅度一直被用户视为衡量应用视觉体验的重要标准。而对开发者来说，帧率(FPS)通常作为衡量应用是否流畅的标准。**

一帧就是一副静止的画面连续的帧就形成动画,我们通常说帧数，简单地说，就是在1秒钟时间里传输的图片的数量也可以理解为图形处理器每秒钟能够刷新几次。**每一帧都是静止的图象，快速连续地显示帧便形成了运动的假象**。

我们看到的早期动画片其实就是用一张张手绘图片连贯翻页制作而成的。当一张张独立图片切换速度足够快时，我们的眼睛就会以为这是连续的动作，这个就是视觉暂留现象。

**FPS即FramesPerSecond(每秒显示的帧数)，用于测量显示帧数的度量。帧数为0说明页面处于静止**，只要画面动起来，这个帧数就会有变化。

## 何为帧延迟?卡顿如何造成的?

**卡顿本质其实就是操作过程中的丢帧**,本来一秒中画面需要更新60帧,但是如果这期间只更新了30帧,那么在用户看来就是丢帧了,主观感觉就是卡了,尤其是帧率波动,用户的感知会更明显。

引起丢帧的原因非常多,有硬件层面的,有软件层面的,也有App自身的问题.帧延迟的高低可以通过帧时间(FrameTime)来判定。

## Android获取FPS帧率

### 环境准备

1、将设备连接到PC,输入adb devices查看到设备信息。

2、在设置-开发者选项-监控-GPU呈现模式分析-勾选上“In adb shelldumpsys gfxinfo”

### 执行测试

1、使用如下命令可以获取设备当前打开的应用包名。

mac系统使用：

>adb shell dumpsys window | grep mCurrentFocus

windows系统使用：

>adb shell dumpsys window | findstr mCurrentFocus

使用后会出现类似如下输出：

![image](https://github.com/user-attachments/assets/b24acded-c6e7-47c8-a744-a2d9f87210c7)


2、在App上执行操作，操作完成之后。输入命令

>adb shell dumpsys gfxinfo{包名} > {PC存储位置}

如下图

![image](https://github.com/user-attachments/assets/88b31e6c-293d-4df5-9259-34d41f5b9dc0)


打开PC存储文件;可以看到采集的原始数据如下所示:

![image](https://github.com/user-attachments/assets/bdb270a6-50e2-4887-9aaf-18a9f54edab3)


### 数据分析



Total frames rendered:2388 //本次dump搜集了2388帧的信息

**Janky frames: 265 (11.10%)// 有265 帧超过了16.67ms.卡帧率是11.1%**

Draw:表示在Java中创建显示列表部分中OnDraw()方法占用的时间。(单位:毫秒)

Prepared:代表的时间就是UIThread传送数据给RenderThread所用的时间。

Process:表示渲染引警执行显示列表所花的时间，view越多，时间就越长

Execute:表示把一帧数据发送到屏幕上排版显示实际花费的时间

**Draw+Prepared+Execute=完整显示一帧的时间，这个时间要小于16ms才能保证每秒60帧**

