Enable and Disable SHARC Cores
==============================

Introduction
------------

This document introduces two kind of core control solutions which support ADSP-SC573, SC584, SC589 EZ-Kits and SC589-MINI. One method is to control SHARC Cores with u-boot ICC command. Other way includes a kernel device driver and a command-line utility, for enabling and disabling the SHARC cores (Core 1 & 2) from the ARM core (Core 0), which have been added to the Yocto Linux distribution for ADSP-SC573, SC584, SC589 and SHARC AUDIO MODULE.

| 
| ===== Method 1: Enable SHARC cores with u-boot ICC command =====

Configure u-boot to Enable Slave Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The slave SHARC core 0 and 1 in SC5xx silicon can be enabled and disabled in u-boot command console. In order to include this ICC command into u-boot, you need to select it in u-boot configuration.

::

   $ bitbake u-boot-adi -c menuconfig
   ARM architecture  --->
       [*] ICC command to enable and disable slave cores
       

After saving the configuration in u-boot, rebuild the u-boot ldr image for sc5xx boards.

::

   $ bitbake u-boot-adi -C compile

Finally, flash the u-boot LDR image into the SPI flash of SC5xx.

U-boot ICC command usage
~~~~~~~~~~~~~~~~~~~~~~~~

The ICC command can enable or disable a specific slave core. The SHARC core ids accepted by this command for SC5xx are 1 and 2, any other id value is ignored. The ICC message queue at the beginning of L2 SRAM is reset before enabling the SHARC cores.

::

   sc # icc
   icc - Inter core communication interface
   Usage:
   icc icc enable <coreid>
     * enable coreid
   icc disable <coreid>
     * disable coreid

| 
| ===== Method 2: Enable SHARC Cores with corecontrol Utility in Linux =====

Linux Core Control Driver
~~~~~~~~~~~~~~~~~~~~~~~~~

The corectrl Device
^^^^^^^^^^^^^^^^^^^

Enable the core control driver by using the below command:

::

   $ bitbake linux-adi -c menuconfig
   CONFIG_CORE_CONTROL:
      ICC core control, control the DSP devices at the side of ARM Core, which 
      provides some commands e.g. Start, Stop, and Set the vector value  
      Symbol: CORE_CONTROL [=y] 
      Type  : bool  
      Prompt: icc core control 
         Location:  
           -> Device Drivers
             -> Staging drivers (STAGING [=y]) 
               -> icc driver (ICC [=y]) 

A new corectrl device would be created to allow Linux user to enable and disable the SHARC cores. See icc.h for macro values. The device, /dev/corectrl, supports the following ioctl requests:

+----------------+---------------------------------------------------------------------+-------------------------------------------+
| Request        | Description                                                         | Format                                    |
+================+=====================================================================+===========================================+
| CMD_CORE_START | Start the specified core running from the programmed SVECT address. | int ioctl(<FD>,CMD_CORE_START, <COREID>); |
+----------------+---------------------------------------------------------------------+-------------------------------------------+
| CMD_CORE_STOP  | Stop the specified core by putting it back in reset.                | int ioctl(<FD>, CMD_CORE_STOP, <COREID>); |
+----------------+---------------------------------------------------------------------+-------------------------------------------+

Both requests return 0 on success and -1 on failure.

::

   ;<FD> 
   :File descriptor of /dev/corectrl
   ;<COREID> 
   :The number of the core to start or stop.  Values accepted are CCTRL_CORE1 and CCTRL_CORE2.

Example: Use corectrl device from source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An example to enable both cores is as follows:

::

   #include <icc.h>
   ...
   int fd = open("/dev/corectrl", O_RDWR);
   if (fd < 0) {
     perror("Unable to open /dev/corectrl");
     exit(1);
   }
   ...
   if (ioctl(fd, CMD_CORE_START, CCTRL_CORE1)) {
     perror("Unable to start Core 1");
     exit(2);
   }
   if (ioctl(fd, CMD_CORE_START, CCTRL_CORE2)) {
     perror("Unable to start Core 2");
     exit(3);
   }

| 
| ==== Package Configuration ==== The SHARC cores can be controlled from the Linux command line using the corecontrol utility. To use corecontrol, first add the package in local.conf:

::

   $ vim /build/conf/local.conf
   IMAGE_INSTALL_append = " sc5xx-corecontrol"

With the corecontrol utility, sharc cores can be controlled to start or stop.

| 
| ==== Example: Use corecontrol from user space ====

::

   # corecontrol -h
   Valid options
   --start CORE_NUM
   --stop CORE_NUM
   # corecontrol --start 1
   # corecontrol --stop 1

| 
| ---- **BACK TO** :doc:`Multi-Core Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/start>`
