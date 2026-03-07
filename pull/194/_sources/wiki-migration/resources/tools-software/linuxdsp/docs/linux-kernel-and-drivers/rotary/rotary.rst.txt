Rotary Driver
=============

Introduction
------------

SC5xx processors feature an up/down counter and thumbwheel interface.

A 32-bit up/down counter is provided that can sense 2-bit quadrature or binary codes as typically emitted by industrial drives or manual thumb wheels. The counter can also operate in general-purpose up/down count modes, in which case count direction is either controlled by a level sensitive input pin or by two edge detectors. A third input can provide flexible zero marker support and can alternatively be used to input the push-button signal of thumb wheels. All three pins have a programmable debouncing circuit.

Hardware Setup
--------------

An ADSP-SC5xx EZ-Board: 

-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

The SC589-EZKIT board does not include the rotary input hardware.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/rotary/lkad-rotary_driver-hw_setup.jpg
   :width: 600px

Software Configuration
----------------------

Configure Linux kernel
~~~~~~~~~~~~~~~~~~~~~~

You need to enable the ADI rotary driver in Linux kernel. 

::

   Device Drivers  --->
       Input device support  --->
           <*>   Event interface    
           [*]   Miscellaneous devices  --->
               <*>   ADI Rotary support

Configure Packages
~~~~~~~~~~~~~~~~~~

You should also enable the event test program to assist with testing. Add the event test program in the filesystem images, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "evtest"

ADSP-SC573 EZ-Board
~~~~~~~~~~~~~~~~~~~

As the Rotary hardware pin conflicts with MSI function on the ADSP-SC573 EZ-Board, thumb wheel switch is disabled by default in U-Boot for ADSP-SC573 EZ-Board out of box. To enable thumb wheel hardware switch, you should enable the thumb wheel switch in U-Boot and disable MSI function in Linux kernel. Please refer to ADSP-SC573 EZ-Board schematic and the section Mobile Storage Interface for MMC/SD for more information.

Disable MSI function in Linux kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   Device Drivers
       MMC/SD/SDIO card support  --->
           [*] Synopsys DesignWare Memory Card Interface
             [*]    Synopsys Designware MCI Support as platform device
             <N>    ADI specific extensions for Synopsys DW Memory Card Interface  

ADSP-SC584 EZ-Board
~~~~~~~~~~~~~~~~~~~

As the Rotary hardware pin conflicts with EMAC RESET pin of Ethernet PHY DP83865/BCM89810 on the ADSP-SC584 EZ-Board, you should disable Ethernet function in Linux kernel. Please refer to ADSP-SC584 EZ-Board schematic and the section Ethernet driver and performance for more information.

Disable EMAC driver in Linux kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   Device Drivers  --->
       [*] Network device support  --->
           [*]   Ethernet driver support  --->
               [*]   STMicroelectronics devices
                   <N>     STMicroelectronics 10/100/1000 Ethernet driver
                   <N>       STMMAC Platform bus support

Disable Ethernet PHY device driver in Linux kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   Device Drivers  --->
       [*] Network device support  --->
           -*-   PHY Device support and infrastructure  --->
               <N>  National Semiconductor PHYs 

The driver provides two options. It can either send Key (KEY) or Relative (REL) events.

**Option 1** – send Key events: Provide two KEY Codes for: 

::

   rotary_up_key  =  KEY_PLUS
   rotary_down_key =  KEY_MINUS

**Option 2** – send REL events: Provide one REL event type: 

::

   rotary_rel_code =  REL_WHEEL    

In case your CZM input is connected (push-button signal of thumb wheels) Specify the KEY event – this will enable the CZM input. See include/linux/input.h for a full list of supported events.

::

   rotary_button_key = KEY_ENTER

The debounce prescale value is used to select the noise filtering characteristic of the input pins. Must be in the range of  0..17

::

   debounce = 10

The driver supports various Counter types

::

   cnt_mode =  CNTMODE_QUADENC

Example
-------

 You will get following information when the rotary hardware device is turned left, right or pushed.

::

   # evtest /dev/input/event0 
   Input driver version is 1.0.1
   Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
   Input device name: "3100b000.cnt"
   Supported events:
     Event type 0 (Sync)
     Event type 1 (Key)
       Event code 28 (Enter)
     Event type 3 (Absolute)
       Event code 8 (Wheel)
         Value      0
         Min     -256
         Max      256
   Testing ... (interrupt to exit)
   Event: time 172.195518, type 3 (Absolute), code 8 (Wheel), value 1
   Event: time 172.195518, -------------- Report Sync ------------
   Event: time 172.206199, type 3 (Absolute), code 8 (Wheel), value 2
   Event: time 172.206199, -------------- Report Sync ------------
   Event: time 172.211954, type 3 (Absolute), code 8 (Wheel), value 3
   Event: time 172.211954, -------------- Report Sync ------------
   Event: time 172.218301, type 3 (Absolute), code 8 (Wheel), value 4
   Event: time 172.218301, -------------- Report Sync ------------
   Event: time 172.401334, type 3 (Absolute), code 8 (Wheel), value 5
   Event: time 172.401334, -------------- Report Sync ------------
   Event: time 172.485123, type 3 (Absolute), code 8 (Wheel), value 4
   Event: time 172.485123, -------------- Report Sync ------------
   Event: time 173.511092, type 3 (Absolute), code 8 (Wheel), value 3
   Event: time 173.511092, -------------- Report Sync ------------
   Event: time 173.565120, type 3 (Absolute), code 8 (Wheel), value 2
   Event: time 173.565120, -------------- Report Sync ------------
   Event: time 173.582020, type 3 (Absolute), code 8 (Wheel), value 1
   Event: time 173.582020, -------------- Report Sync ------------
   Event: time 173.600967, type 3 (Absolute), code 8 (Wheel), value 0
   Event: time 173.600967, -------------- Report Sync ------------
   Event: time 175.609542, type 3 (Absolute), code 8 (Wheel), value 1
   Event: time 175.609542, -------------- Report Sync ------------
   Event: time 175.624487, type 3 (Absolute), code 8 (Wheel), value 2
   Event: time 175.624487, -------------- Report Sync ------------
   Event: time 175.629124, type 3 (Absolute), code 8 (Wheel), value 3
   Event: time 175.629124, -------------- Report Sync ------------
   Event: time 175.633278, type 3 (Absolute), code 8 (Wheel), value 4
   Event: time 175.633278, -------------- Report Sync ------------
   Event: time 176.719340, type 3 (Absolute), code 8 (Wheel), value 5
   Event: time 176.719340, -------------- Report Sync ------------
   Event: time 176.741497, type 3 (Absolute), code 8 (Wheel), value 6
   Event: time 176.741497, -------------- Report Sync ------------
   Event: time 176.748370, type 3 (Absolute), code 8 (Wheel), value 7
   Event: time 176.748370, -------------- Report Sync ------------
   Event: time 176.754401, type 3 (Absolute), code 8 (Wheel), value 8
   Event: time 176.754401, -------------- Report Sync ------------
   Event: time 177.670738, type 3 (Absolute), code 8 (Wheel), value 9
   Event: time 177.670738, -------------- Report Sync ------------
   Event: time 177.691486, type 3 (Absolute), code 8 (Wheel), value 10
   Event: time 177.691486, -------------- Report Sync ------------
   Event: time 177.698444, type 3 (Absolute), code 8 (Wheel), value 11
   Event: time 177.698444, -------------- Report Sync ------------
   Event: time 177.705056, type 3 (Absolute), code 8 (Wheel), value 12
   Event: time 177.705056, -------------- Report Sync ------------
   Event: time 178.598188, type 3 (Absolute), code 8 (Wheel), value 11
   Event: time 178.598188, -------------- Report Sync ------------
   Event: time 178.700345, type 3 (Absolute), code 8 (Wheel), value 10
   Event: time 178.700345, -------------- Report Sync ------------
   Event: time 178.710039, type 3 (Absolute), code 8 (Wheel), value 9
   Event: time 178.710039, -------------- Report Sync ------------
   Event: time 178.716659, type 3 (Absolute), code 8 (Wheel), value 8
   Event: time 178.716659, -------------- Report Sync ------------
   Event: time 179.628879, type 3 (Absolute), code 8 (Wheel), value 7
   Event: time 179.628879, -------------- Report Sync ------------
   Event: time 179.705605, type 3 (Absolute), code 8 (Wheel), value 6
   Event: time 179.705605, -------------- Report Sync ------------
   Event: time 179.714243, type 3 (Absolute), code 8 (Wheel), value 5
   Event: time 179.714243, -------------- Report Sync ------------
   Event: time 179.719841, type 3 (Absolute), code 8 (Wheel), value 4
   Event: time 179.719841, -------------- Report Sync ------------

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
