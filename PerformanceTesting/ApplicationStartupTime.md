# 启动时间

# app启动流程

开发应用的时候,一般会指定一个mainActivity，可以使用命令

>aapt dumpbadging [pkgname]|findstr launchable-activity

用户在桌面上点击这个Activity的时候,系统会直接起这个Activity.Activity在启动的时候会走onCreate/onStart/onResume三个方法

onCreate()在活动第一次创建时被调用，主要用于加载布局。

onStart()这个方法在活动由不可见变为可见的时候调用。

onResume这个方法在活动准备好和用户进行交互的时候调用。

