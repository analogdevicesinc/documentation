CPU Frequency utility
=====================

Introduction
------------

CPU frequency scaling enables the operating system to scale the CPU frequency up or down in order to save power. Clock scaling allows you to change the clock speed of the CPUs on the fly.

Hardware Setup
--------------

-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above, or,
-  ADSP-SC589 MINI v1.4 and above

The ADSP-SC5xx processors have Clock Generation Unit (CGU) support. The CGU allows program to change the PLL clock frequency and the CCLKn, SYSCLK, SCLKn, and OUTCLK clock scaling.

| 
| ===== Software Configuration =====

Enabling CPU Frequency Driver in Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run "**bitbake linux-adi -c menuconfig**" and configure the kernel as follows:

::

   CPU Power Management  --->      
           CPU Frequency scaling  --->   
           [*] CPU Frequency scaling  
           <*>   CPU frequency translation statistics 
           [*]   CPU frequency translation statistics details      
                 Default CPUFreq governor (performance)  --->
           -*-   'performance' governor 
           < >   'powersave' governor     
           <*>   'userspace' governor for userspace frequency scaling     
           < >   'ondemand' cpufreq policy governor  
           < >   'conservative' cpufreq governor
                 *** CPU frequency scaling drivers ***
           < >   Generic DT based cpufreq driver
           [*]   SC58X CPUFreq support   

| 
| ===== How to Change the CPU Frequency =====

Preferred Interface: sysfs
~~~~~~~~~~~~~~~~~~~~~~~~~~

The preferred interface is located in the sysfs filesystem. If you mounted it at /sys, the cpufreq interface is located in a subdirectory “cpufreq” within the cpu-device directory (e.g. /sys/devices/system/cpu/cpu0/cpufreq/ for the first CPU).

::

   cpuinfo_min_freq :      This file shows the minimum operating frequency the processor can run at (in kHz) 

   cpuinfo_max_freq :      This file shows the maximum operating frequency the processor can run at (in kHz) 

   scaling_driver :        This file shows what cpufreq driver is used to set the frequency on this CPU

   scaling_available_governors :
                   This file shows the CPUfreq governors available in this kernel. You can see the
                   currently activated governor inscaling_governor, and by "echoing" the name of another
                   governor you can change it. Please note that some governors won't load - they only
                   work on some specific architectures or processors.

   scaling_min_freq and scaling_max_freq :
                   These files show the current "policy limits" (in kHz). By echoing new values into these
                   files, you can change these limits. NOTE: when setting a policy you need to
                   first set scaling_max_freq, then scaling_min_freq.

   scaling_setspeed :
                   By "echoing" a new frequency into this file you can change the speed of the CPU,
                   but only within the limits of scaling_min_freq and scaling_max_freq.
    

| 
| ===== What Is A CPUFreq Governor? =====

Governors In the Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Performance
^^^^^^^^^^^

The CPUfreq governor “performance” sets the CPU statically to the highest frequency within the borders of scaling_min_freq and scaling_max_freq.

Powersave
^^^^^^^^^

The CPUfreq governor “powersave” sets the CPU statically to the lowest frequency within the borders of scaling_min_freq and scaling_max_freq.

Userspace
^^^^^^^^^

The CPUfreq governor “userspace” allows the user, or any userspace program running with UID “root”, to set the CPU to a specific frequency by making a sysfs file “scaling_setspeed” available in the CPU-device directory.

Ondemand
^^^^^^^^

The CPUfreq governor “ondemand” sets the CPU depending on the current usage. To do this the CPU must have the capability to switch the frequency very quickly. There are a number of sysfs file accessible parameters:

sampling_rate: Measured in uS (10^-6 seconds), this is how often you want the kernel to look at the CPU usage and to make decisions on what to do about the frequency. Typically this is set to values of around '10000' or more.

show_sampling_rate\_(min|max): The minimum and maximum sampling rates available that you may set 'sampling_rate' to.

up_threshold: Defines what the average CPU usage between the samplings of 'sampling_rate' needs to be for the kernel to make a decision on whether it should increase the frequency. For example when it is set to its default value of '80' it means that between the checking intervals the CPU needs to be on average more than 80% in use to then decide that the CPU frequency needs to be increased.

sampling_down_factor: This parameter controls the rate that the CPU makes a decision on when to decrease the frequency.  When set to its default value of '5' it means that at 1/5 the sampling_rate the kernel makes a decision to lower the frequency. Five “lower rate” decisions have to be made in a row before the CPU frequency is actually lowered. If set to '1' then the frequency decreases as quickly as it increases, if set to '2' it decreases at half the rate of the increase.

ignore_nice_load: This parameter takes a value of '0' or '1'. When set to '0' (its default), all processes are counted towards the 'cpu utilisation' value. When set to '1', the processes that are run with a 'nice' value will not count (and thus are ignored) in the overall usage calculation. This is useful if you are running a CPU intensive calculation on your laptop that you do not care how long it takes to complete, as you can 'nice' it and prevent it from taking part in the deciding process of whether to increase your CPU frequency.

Conservative
^^^^^^^^^^^^

The CPUfreq governor “conservative”, much like the “ondemand” governor, sets the CPU depending on the current usage. It differs in behaviour in that it gracefully increases and decreases the CPU speed rather than jumping to max speed the moment there is any load on the CPU. This behaviour is more suitable in a battery powered environment. The governor is tweaked in the same manner as the “ondemand” governor through sysfs with the addition of:

freq_step: This describes what percentage steps the cpu freq should be increased and decreased smoothly by. By default the cpu frequency will increase in 5% chunks of your maximum CPU frequency. You can change this value to anywhere between 0 and 100 where '0' will effectively lock your CPU at a speed regardless of its load whilst '100' will, in theory, make it behave identically to the “ondemand” governor.

down_threshold: Same as the 'up_threshold' found for the “ondemand” governor but for the opposite direction. For example when set to its default value of '20' it means that if the CPU usage needs to be below 20% between samples to have the frequency decreased.

 

Change Core Clock Frequency via cpufreq-utils
---------------------------------------------

In order to modify frequency settings with cpufreq-utils, you need to have the userspace governor enabled.

::

   # cpufreq-info 
   cpufrequtils 005: cpufreq-info (C) Dominik Brodowski 2004-2006
   Report errors and bugs to cpufreq@vger.kernel.org, please.
   analyzing CPU 0:
     driver: sc58x cpufreq
     CPUs which need to switch frequency at the same time: 0
     hardware limits: 113 MHz - 450 MHz
     available frequency steps: 450 MHz, 225 MHz, 113 MHz
     available cpufreq governors: performance
     current policy: frequency should be within 113 MHz and 450 MHz.
                     The governor "performance" may decide which speed to use
                     within this range.
     current CPU frequency is 450 MHz (asserted by call to hardware).
     cpufreq stats: 450 MHz:0.00%, 225 MHz:0.00%, 113 MHz:0.00%
   # 


   # cpufreq-set -f 225000
   # cpufreq-info 
   cpufrequtils 005: cpufreq-info (C) Dominik Brodowski 2004-2006
   Report errors and bugs to cpufreq@vger.kernel.org, please.
   analyzing CPU 0:
     driver: sc58x cpufreq
     CPUs which need to switch frequency at the same time: 0
     hardware limits: 113 MHz - 450 MHz
     available frequency steps: 450 MHz, 225 MHz, 113 MHz
     available cpufreq governors: userspace, performance
     current policy: frequency should be within 113 MHz and 450 MHz.
                     The governor "userspace" may decide which speed to use
                     within this range.
     current CPU frequency is 225 MHz (asserted by call to hardware).
     cpufreq stats: 450 MHz:0.00%, 225 MHz:0.00%, 113 MHz:0.00%  (1)

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
