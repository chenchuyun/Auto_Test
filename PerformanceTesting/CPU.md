## CPU及Android下的CPU

cpu：中央处理器，运算数据、发送数据；相当于人体的大脑

### CPU的组成

CPU右运算器、控制器和寄存器及实现它们之间练习的数据线、控制线及状态的总线构成

### CPU使用率/利用率

CPU占用过高会使得设备运行程序出现宽发热，设置出现应用程序Crash,影响用户体验，在排除硬件环境的限制下，应用程序应该尽可能少的占用CPU，所以，设备的发热很大功劳是CPU

### Android CPU三大状态
用户态：CPU处于用户态执行的时间

系统态：CPU处于系统内核执行的时间

空闲态：CPU处于空闲系统进程执行的时间

CPU利用率是指：CPU执行非系统空闲进程的时间/CPU总的执行时间

HZ：Linux核心每隔固定周期会发出timerinterrupt（时间中断），HZ是用来定义每一秒有几次时钟中断。

例如：HZ为1000，就代表每秒有1000次时钟中断

Jiffies：在Linux内核中，有一个全局变量：Jiffies。Jiffies代表时间，它的单位随硬件平台的不同而不同。Jiffies的单位就是1/HZ

那么CPU利用率计算公式如下：

CPU使用率=（用户态Jiffies+系统态Jiffies）/总Jiffies

### CPU使用率的测试方法

cmd或windowsShell窗口中输入命令
>adb shell top

### adb shell top输出内容解释

![image](https://github.com/user-attachments/assets/597244c4-a135-423f-a83c-0673dfde56c0)


**Tasks：858 total,   1 running, 857 sleeping,   0 stopped,   0 zombie**

任务（进程）：系统现在总共有858个进程，其中处于运行中的有1个，857个在休眠，stoped状态的有0个，僵尸状态的有0个。

Mem:  7797364K total,  7675152K used,   122212K free,   2891776 buffers

内存状态：物理内存总量（9979364K），使用中的内存总量（7675152K），空闲内存总量（122212K），缓存内存量（2891776）

Swap:  4145148K total,  1489508K used,  2655640K free,  3193308K cached

Swap交换分区：交换区总量（4145148K），使用的交换区总量（1489508K），空闲交换区总量（2655640K），缓冲的交换区总量（3193308K）

**计算当前计算机可用内存公式**

Mem的free + Mem的buffers + Swap的cached

**800%cpu   4%user   0%nice   7%sys 787%idle   0%iow   2%irq   0%sirq   0%host**

800%cpu：CPU的总量--八核

4%user：用户空间占用CPU的百分比

0%nice：改变过优先级的进程占用CPU的百分比

7%sys：内核空间占用CPU的百分比

787%idle：空闲CPU百分比

0%iow：10等待占用CPU的百分比

2%irq：硬中断(Hardware IRQ)占用CPU的百分比

0%sirq：软中断(Software Intemupts)占用CPU的百分比

硬中断和软中断是整个中断过程中的两个不同的部分

 **PID USER         PR  NI VIRT  RES  SHR S[%CPU] %MEM     TIME+ ARGS**

 PID-进程id

 USER-进程所有者

 PR -进程优先级

 NI- nice值。负值表示高优先级，正值表示低优先级

 VIRT-进程使用的虚拟内存总量，单位kb。VIRT=SWAP+RES

 RES -进程使用的、未被换出的物理内存大小，单位kb。RES=CODE+DATA

SHR -共享内存大小，单位kb

S -进程状态。D=不可中断的睡眠状态 R=运行 S=睡眠 T=跟踪/停止 Z=僵尸进程

%CPU-上次更新到现在的CPU时间占用百分比

%MEM -进程使用的物理内存百分比

TIME+- 进程使用的CPU时间总计，单位1/100秒

ARGS- 进程名称(命令名/命令行)