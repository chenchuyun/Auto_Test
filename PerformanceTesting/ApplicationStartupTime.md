# 启动时间

# app启动流程

应用图标被点击后布满整个屏幕的过程，包括加载：控件从不可见到可见等

开发应用的时候,一般会指定一个mainActivity，可以使用命令

>aapt dumpbadging [pkgname]|findstr launchable-activity

用户在桌面上点击这个Activity的时候,系统会直接起这个Activity.Activity在启动的时候会走onCreate/onStart/onResume三个方法

onCreate()在活动第一次创建时被调用，主要用于加载布局。

onStart()这个方法在活动由不可见变为可见的时候调用。

onResume这个方法在活动准备好和用户进行交互的时候调用。

## 通过adb获取启动时间

>adb shell am start -W [PackageName]/[PackageName.MainActivity]

这里面涉及到三个时间，ThisTime、TotalTime和WaitTime。
ThisTime表示启动一连串Activity的最后一个Activity的启动耗时，

TotalTime表示新应用启动的耗时，包括新进程的启动和Activity的启动，但不包括前一个应用Activitypause的耗时。也就是说，开发者一般只要关心TotalTime即可，这个时间才是自己应用真正启动的耗时。

WaitTime就是总的耗时，包括前一个应用Activitypause的时间和新应用启动的时间

**启动时间一般关注冷启动TotalTime**

冷启动：后台无进程；

热启动：后台有进程。

