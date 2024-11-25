# 功耗

功耗，通俗的理解即电流通过导体使设备运行，导体本身的电阻将电能转换为热能的过程，因此，通常**功耗测试也叫电量测试**。

## 移动设备耗电场景

由于移动设备的电池容量限制，所以对于App的功耗也是需要考虑的一个方面。Android的很多特性都比较耗电(如屏幕、GPS、sensor传感器、唤醒机制wakelock、CPU、连网等等)，我们必须要慎重检查APP的电量使用，以免导致用户手机过度耗电发热，带来不良体验。

主要的耗电场景有:

screen：屏幕显示画面会耗电。

cpu：复杂的运算逻辑、死循环等会直接导致CPU负载过高，会导致耗电;

wake lock：唤醒锁,只要有应用拿到wakelock这个锁，系统就无法进入睡眠状态。频繁wake lock或者申请了wakelock没有释放，会导致耗电:

wifiscan和wif lock：wifiscan和wif lock也会导致手机的wifi模块处于激活状态，频繁的wifiscan或者wifi lock不释放，会导致耗电;

sensor：传感器打开后会导致系统持续监听设备外围环境的数据变化，使用后不及时关闭，会导致耗电:

network：大量的数据传输，或者长时间的移动网络数据传输会导致耗电;

gps：gps也是一种传感器，定位中完成后没有及时关闭，会导致耗电。

## Android App的功耗

目前很多定制Android系统支持查看App耗电量查看。

## Android 电量测试

### batterystats

使用dumpsys batterystats命令可用来生成关于设备电池使用情况的统计数据，这些数据按唯一用户ID(UID)进行整理。

统计信息包括以下内容:

电池相关事件的历史记录

设备的全局统计信息

每个UID和系统组件的大致用电量

单个应用的每个数据包占用的移动网络毫秒数

系统UID汇总统计信息

应用UID汇总统计信息

### bugreport

Android为了方便开发人员分析整个系统平台和某个App在运行一段时间之内的所有信息，专门开发了bugreport工具。输入命令

adb bugreport [mepath]/即可执行信息采集，并生成zip或者txt文件格式的数据文件。

### Battery Historian

Batterystats是包含在Android框架中的一种工具，用于收集设备上的电池数据。您可以使用adb将收集的电池数据转储到PC，并创建一份可使用分析的报告。Battery Historian会将报告从Batterystats转换为可在浏览器中查看的HTML报告。

**要使用Batterystats和BatteryHistorian，需要一台搭载Android5.0或更高版本且启用了USB调试功能的移动设备**

## 电量数据收集

1、收集电池的历史数据

>adb shell dumpsys batterystats -enable full-wake-history

Enabled: full-wake-history

2、重置电池数据

>adb shell dumpsys batterystats -reset

Battery stats reset.

3、.断开设备与电脑的连接，以便只从设备的电池中消耗电流，然后执行指定的APP进行相关操作。（去除边充电边消耗的影响）。

4、使用命令adb bugreport导出电量信息结果，这里需要注意的是Android7.0以上系统版本和Android7.0以下命令不同。

Android7.0以上系统版本:

>adb bugreport bugreport.zip

Android7.0以下系统版本:

获取bugreport信息(记录了从开机之后详细的dumpsys,dumpstate和logcat信息)

>adb bugreport > [path] bugreport.txt

获取dumpsys信息(获取系统信息:比如内存CPU，accounts，activities，wifi等信息)

>adb shell dumpsys batterystats >存放的电脑地址/batterystats.txt

或者获取指足的应用程序的dumpsys信息

>adb shelldumpsys batterystats>包名>存放的电脑地址/batterystats.txt

## 电量数据解析

Battery Historian一款由Google提供的Android系统电量分析工具，从手机中导出bugreport文件上传至页面，在网页中生成详细的图表数据来展示手机上各模块电量消耗过程，最后通过App数据的分析制定出相关的电量优化的方法。

### 安装Battery Historian

1、使用Battery Historian需要在本地安装，最简单的方法使用docker安装然后执行如下命令：

>docker run -d -p 9999:9999 bhaavanbattery-historian

执行完成后使用浏览器打开链接:http://ocalhost(IP):9999 即可看到BatteryHistorian界面。

上传生成的报告文件然后点击submit提交即可，如果上传后没有显示submit按钮，则需要科学上网。原因是因为web某些资源没有加载出来，其中的一些资源需要访问Google服务器，但是这些资源被墙了，无法访问。只要解决了墙的问题，submit的问题也就迎刃而解了。如果不想在本地搭建环境，那么可以访问在线的解析平台:https://bathgist.ef.lc/

## 功耗的符合标准

**电量不能消耗过多**，具体数值可以参考竞品


