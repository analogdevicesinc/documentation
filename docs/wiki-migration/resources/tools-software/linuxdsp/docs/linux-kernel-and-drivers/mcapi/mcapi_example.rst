Run Linux on ARM and bare-metal application on SHARC
====================================================

Introduction
------------

This document introduces steps to run Linux on ARM core and SHARC baremetal application on SHARC+ cores(Core 1 & 2) by CrossCore Embedded Studio (**CCES**). Take the Linux MCAPI inter-operability demo example as a SHARC baremetal application.

Get the Hardware Ready
----------------------

MCAPI support the the ADSP-SC5xx series product:

-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above
-  ADSP-SC584 Ezkit v1.0 and above
-  ADSP-SC589 Ezkit v1.1 and above
-  ADSP-SC589 Mini Board
-  ICE1000 or ICE2000 JTAG board

Here we take ADSP-SC589 EZ-kit as our example.

Get the Source Code Ready
-------------------------

The MCAPI example for ARM core (Running Linux) is included in the YOCTO, and you can get the MCAPI example for SHARC+ Cores from the gitbub `lnxdsp-examples <https://github.com/analogdevicesinc/lnxdsp-examples.git>`__

- MCAPI Examples for SHARC Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   ; name : lnxdsp-exmaples/mcapi/mcapi-message-example
   ; version : ''v1.0.0''
   ; branch : remotes/origin/release/yocto-''1.0.0''

**Git Usage**

.. code:: bash

   git clone https://github.com/analogdevicesinc/lnxdsp-examples.git
   cd lnxdsp-examples
   git branch -a 
   git checkout -b release/yocto-1.0.0 origin/release/yocto-1.0.0
   git pull

- MCAPI Examples for ARM Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  sources/meta-adi/meta-adi-adsp-sc5xx/recipes-icc/libmcapi/libmcapi.bb
-  sources/meta-adi/meta-adi-adsp-sc5xx/recipes-icc/sc5xx-corecontrol/sc5xx-corecontrol.bb

- CCES
~~~~~~

-  Analog Devices :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>` version ``2.9.1`` or later.

--------------

Software Configuration
----------------------

Configure Device Tree
^^^^^^^^^^^^^^^^^^^^^

Make sure the icc has been enabled by from the device tree file sc589-ezkit.dts/sc584-ezkit.dts/sc573-ezkit.dts/sc589-mini.dts under arch/arm/boot/dts.

::

   &icc0 {
       status = "okay";
   };

Kernel Configuration
^^^^^^^^^^^^^^^^^^^^

MCAPI lib is built on top of the ICC (Inter-Core Communications) device driver. Enable the ICC driver relevant operations in Linux kernel:

.. code:: shell

   # bitbake linux-adi -c menuconfig

.. code:: shell

   Device Drivers  --->
          [*] Staging drivers  --->
             [*]   icc driver  --->
                [*]   icc core control  
                [*]   icc protocol
                [ ]   icc debug

Then run **bitbake linux-adi -C compile** to generate kernel image zImage and dtb file.

Package Configuration
^^^^^^^^^^^^^^^^^^^^^

Add the mcapi package in the filesystem, it's enabled in adsp-sc5xx-full image by default.

.. code:: shell

   vim build/conf/local.conf
   IMAGE_INSTALL_append = " libmcapi sc5xx-corecontrol"

Then run **bitbake adsp-sc5xx-minimal -C compile** or **bitbake adsp-sc5xx-full -C compile** to generate the filesystem.

--------------

Load Linux on ARM and SHARC applications on SHARC by CCES
---------------------------------------------------------

A **brief step** to run multicore on the EZ-Kit board is showing as follows:

-  Boot u-boot to console and stop at u-boot;
-  Start CCES to load application to SHARC cores and wait;

   -  Build baremetal example in CCES;
   -  Remove the program of Device 0[Core 0];
   -  Uncheck automaticlly setted breakpoints and disable semihosting in "Automatic Breakpoints" view of debug configuration;
   -  Uncheck "Halt core after connecting to target" for ARM core in debug configuration and start debug;
   -  Click the debug button, it will load the dxe file then waiting for linux to start Core 1 & 2;

-  Enable SHARC cores in Linux
-  Resume Core 1 & 2 Application running in CCES

| 
| ==== Step 1: Boot into Linux console ==== Please refer to the :doc:`Installing Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>` to load the built Linux into the target board:

.. code:: c++


        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
        @@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@            @@@@@@@@@@@@@@@@@@@
        @@@@@@@@               @@@@@@@@@@@@@@@@
        @@@@@@@@                   @@@@@@@@@@@@
        @@@@@@@@                     @@@@@@@@@@
        @@@@@@@@                        @@@@@@@
        @@@@@@@@                     @@@@@@@@@@
        @@@@@@@@                   @@@@@@@@@@@@
        @@@@@@@@               @@@@@@@@@@@@@@@@
        @@@@@@@@            @@@@@@@@@@@@@@@@@@@
        @@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

           Analog Devices Yocto Distribution
                    www.analog.com
                 www.yoctoproject.org
   adsp-sc589-ezkit login: root
   Password: adi

| 
| ==== Step2: Build MCAPI Example in CCES ==== Before running the mcapi example in CrossCore Embedded Studio, please follow the steps below to import and build it, now we take ADSP-SC589-EzKit as the example to demonstrate.

Import the mcapi example into CCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   ; **''Step 1''**
   : Select the **File** menu and then select the **Import** option from the menu
   : When the **Import** project window appears:
   : Click on the **General** folder, then click on the **Existing Projects into Workspace** entry, and click **Next**
   ; **''Step 2''**
   : Click the **Select root directory** radio button and then click the **Browse** button
   : Browse the root folder where you previously cloned the lnxdsp-example and then browse down into the **__//lnxdsp-examples\mcapi\mcapi-message-example\adsp-sc589-ezkit//__** folder
   : Click **OK** to close the file browser dialog
   ; **''Step 3''**
   : The mcapi example projects should appear in the **projects** pane of the **Import** window
   : Check the entry in the **projects** pane and click **Finish**

   |image1|

.. container:: centeralign

   **Diagram 1** Import the MCAPI Example


Build Mode Selection
~~~~~~~~~~~~~~~~~~~~

Select the "Build Tool" to choose Debug/Release mode for building the target projects:


|image2|

.. container:: centeralign

   **Diagram 2** Build Action - Build Mode Selection


Build the projects
~~~~~~~~~~~~~~~~~~

-  In the **Project Explorer** right click on the **mcapi_send_recv_sc589_Core1** and **mcapi_send_recv_sc589_Core2** projects to select the **Build Project** option from the menu


|image3|

.. container:: centeralign

   **Diagram 3** Build Action - Build Projects


| 
| ==== Step3: Load MCAPI Example for SHARC Cores ==== Please follow the steps below to do debug configuration, download and run the built binary for SHARC Cores.

1. Connect ICE-1000/2000 JTAG emulator between the SC589-EZKIT and your PC

2. In the Project Explorer right click **mcapi_send_recv_sc589_Core1** on the project and select the **Debug As** option from the menu.

3. From the popup menu select **Debug Configurations** option to create a new debug configuration that matches your emulator and target board

4. Remove the ARM core project from the debug configuration

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/debug_remove_core0.png

5. Uncheck automaticlly setted breakpoints and disable semihosting in "Automatic Breakpoints" view of debug configuration.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/debug_config_uncheck1.jpg

6. Uncheck the debug target option "Halt core after connecting to target" for ARM core.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/debug_config_uncheck2.jpg

7. Start debug and wait for Linux to start core1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/debug_config_start_debug.jpg

| 
| ==== Step4: Enable SHARC cores in Linux ==== In u-boot, enable SHARC core then boot linux

::

   sc # icc enable 1

Or boot Linux, and then in Linux use the corecontrol utility to start the SHARC core:

::

   # corecontrol --start 1

After running SHARC core, CCES halts in the first line of the application code on SHARC core 1.


|image4|

| 
| ==== Step5: Resume Core 1 & 2 Application running in CCES ==== Resume(F5) core 1 and continue running the application in CCES.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/debug_config_resume_success.jpg

Now Linux is running on ARM core 0 while SHARC baremetal application is running on core 1.

| 
| ==== Step6: Run Linux MCAPI MSG Demo Test ==== Run 'arm_sharc_msg_demo' and 'arm_sharc_msg_test' command in Linux and the passed log in linux is showing as below.

.. code:: c++

   root@adsp-sc589-ezkit:~# corecontrol --start 1
   Test core 1 start
   Test core 1 end: 0
   root@adsp-sc589-ezkit:~# corecontrol --start 2
   Test core 2 start
   Test core 2 end: 0
   root@adsp-sc589-ezkit:~# arm_sharc_msg_demo -h
   Usage: arm_sharc_msg_demo <options>

   Available options:
           -h,--help               this help
           -m,--mode               select the mode:
                                   0 --- nonblocking mode0(default)
                                   1 --- nonblocking mode1
                                   2 --- nonblocking mode2
                                   3 --- blocking mode
           -t,--timeout            timeout value in jiffies(default:10,000)
           -r,--round              number of test round(default:100)
           -i,--remote_core_id     number of remote core id:
                                   0 ----- specify to use the two SHARC cores(default)
                                   1 ----- specify the remote core is SHARC Core 1
                                   2 ----- specify the remote core is SHARC Core 2
                                   
   root@adsp-sc589-ezkit:~# arm_sharc_msg_demo -r 3
   semget
   Thread [0] CHECK_STATUS---initialize:MCAPI_SUCCESS
    node=0, port=200
   Thread [2] CHECK_STATUS---create_ep:MCAPI_SUCCESS
   Thread [2] local endpoint: c8
   Thread [2] CHECK_STATUS---get_ep_i:MCAPI_PENDING
    node=2, port=6
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] remote endpoint: 20006
   Thread [2] send() start......
   Thread [2] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of send() - endpoint=200 has sent: [hello core 2 messag from core 0 - 0]
   Thread [2] core0: mode(0) message send. The 0 time sending
   Thread [2] recv() start......
   Thread [2] CHECK_STATUS---available:MCAPI_SUCCESS
    node=2, port=6
   Thread [2] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of recv() - endpoint=200 size 0x48 has received: [hello core 0 message from core 2 - 1]
   Thread [2] core0: mode(0) message recv. The 0 time receiving
   Thread [2] send() start......
   Thread [2] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of send() - endpoint=200 has sent: [hello core 2 messag from core 0 - 1]
   Thread [2] core0: mode(0) message send. The 1 time sending
   Thread [2] recv() start......
   Thread [2] CHECK_STATUS---available:MCAPI_SUCCESS
    node=2, port=6
   Thread [2] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of recv() - endpoint=200 size 0x48 has received: [hello core 0 message from core 2 - 2]
   Thread [2] core0: mode(0) message recv. The 1 time receiving
   Thread [2] send() start......
    node=0, port=101
   Thread [1] CHECK_STATUS---create_ep:MCAPI_SUCCESS
   Thread [1] local endpoint: 65
   Thread [1] CHECK_STATUS---get_ep_i:MCAPI_PENDING
    node=1, port=5
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] remote endpoint: 10005
   Thread [1] send() start......
   Thread [1] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of send() - endpoint=101 has sent: [hello core 1 messag from core 0 - 0]
   Thread [1] core0: mode(0) message send. The 0 time sending
   Thread [1] recv() start......
   Thread [1] CHECK_STATUS---available:MCAPI_SUCCESS
    node=1, port=5
   Thread [1] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of recv() - endpoint=101 size 0x48 has received: [hello core 0 message from core 1 - 1]
   Thread [1] core0: mode(0) message recv. The 0 time receiving
   Thread [1] send() start......
   Thread [2] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of send() - endpoint=200 has sent: [hello core 2 messag from core 0 - 2]
   Thread [2] core0: mode(0) message send. The 2 time sending
   Thread [2] recv() start......
   Thread [2] CHECK_STATUS---available:MCAPI_SUCCESS
    node=2, port=6
   Thread [2] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of recv() - endpoint=200 size 0x48 has received: [hello core 0 message from core 2 - 3]
   Thread [2] core0: mode(0) message recv. The 2 time receiving
   Thread [2] CHECK_STATUS---del_ep:MCAPI_SUCCESS
   Thread [2] core0 3 rounds mode(0) demo Test PASSED!!
   Thread [2] test success
   Thread [1] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of send() - endpoint=101 has sent: [hello core 1 messag from core 0 - 1]
   Thread [1] core0: mode(0) message send. The 1 time sending
   Thread [1] recv() start......
   Thread [1] CHECK_STATUS---available:MCAPI_SUCCESS
    node=1, port=5
   Thread [1] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of recv() - endpoint=101 size 0x48 has received: [hello core 0 message from core 1 - 2]
   Thread [1] core0: mode(0) message recv. The 1 time receiving
   Thread [1] send() start......
   Thread [1] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of send() - endpoint=101 has sent: [hello core 1 messag from core 0 - 2]
   Thread [1] core0: mode(0) message send. The 2 time sending
   Thread [1] recv() start......
   Thread [1] CHECK_STATUS---available:MCAPI_SUCCESS
    node=1, port=5
   Thread [1] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of recv() - endpoint=101 size 0x48 has received: [hello core 0 message from core 1 - 3]
   Thread [1] core0: mode(0) message recv. The 2 time receiving
   Thread [1] CHECK_STATUS---del_ep:MCAPI_SUCCESS
   Thread [1] core0 3 rounds mode(0) demo Test PASSED!!
   Thread [1] test success
   mcapi_finalize 322

   root@adsp-sc589-ezkit:~# arm_sharc_msg_test -h
   Usage: arm_sharc_msg_test <options>

   Available options:
           -h,--help               this help
           -t,--timeout            timeout value in jiffies(default:10,000)
           -r,--round              number of test round(default:100)
   root@adsp-sc589-ezkit:~# arm_sharc_msg_test -r 3
   semget
   Thread [0] CHECK_STATUS---initialize:MCAPI_SUCCESS
    node=0, port=200
   Thread [2] CHECK_STATUS---create_ep:MCAPI_SUCCESS
   Thread [2] local endpoint: c8
    node=2, port=6
   Thread [2] CHECK_STATUS---get_ep:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---get_ep_i:MCAPI_PENDING
    node=2, port=6
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] remote endpoint: 20006
   Thread [2] send() start......
   Thread [2] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of send() - endpoint=200 has sent: [hello core 2 messag from core 0 - 0]
   Thread [2] core0: mode(0) message send. The 0 time sending
   Thread [2] recv() start......
   Thread [2] CHECK_STATUS---available:MCAPI_SUCCESS
    node=2, port=6
   Thread [2] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of recv() - endpoint=200 size 0x48 has received: [hello core 0 message from core 2 - 1]
   Thread [2] core0: mode(0) message recv. The 0 time receiving
   Thread [2] send() start......
    node=0, port=101
   Thread [1] CHECK_STATUS---create_ep:MCAPI_SUCCESS
   Thread [1] local endpoint: 65
   Thread [2] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of send() - endpoint=200 has sent: [hello core 2 messag from core 0 - 1]
   Thread [2] core0: mode(1) message send. The 1 time sending
   Thread [2] recv() start......
    node=2, port=6
   Thread [2] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of recv() - endpoint=200 size 0x48 has received: [hello core 0 message from core 2 - 2]
   Thread [2] core0: mode(1) message recv. The 1 time receiving
   Thread [2] send() start......
    node=1, port=5
   Thread [1] CHECK_STATUS---get_ep:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---get_ep_i:MCAPI_PENDING
    node=1, port=5
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] remote endpoint: 10005
   Thread [1] send() start......
   Thread [1] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of send() - endpoint=101 has sent: [hello core 1 messag from core 0 - 0]
   Thread [1] core0: mode(0) message send. The 0 time sending
   Thread [1] recv() start......
   Thread [1] CHECK_STATUS---available:MCAPI_SUCCESS
    node=1, port=5
   Thread [1] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of recv() - endpoint=101 size 0x48 has received: [hello core 0 message from core 1 - 1]
   Thread [1] core0: mode(0) message recv. The 0 time receiving
   Thread [1] send() start......
   Thread [2] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of send() - endpoint=200 has sent: [hello core 2 messag from core 0 - 2]
   Thread [2] core0: mode(2) message send. The 2 time sending
   Thread [2] recv() start......
    node=2, port=6
   Thread [2] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [2] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [2] end of recv() - endpoint=200 size 0x48 has received: [hello core 0 message from core 2 - 3]
   Thread [2] core0: mode(2) message recv. The 2 time receiving
   Thread [2] CHECK_STATUS---del_ep:MCAPI_SUCCESS
   Thread [2] core0 3 rounds mode(2) Test PASSED!!
   Thread [2] test success
   Thread [1] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of send() - endpoint=101 has sent: [hello core 1 messag from core 0 - 1]
   Thread [1] core0: mode(1) message send. The 1 time sending
   Thread [1] recv() start......
    node=1, port=5
   Thread [1] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---test:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of recv() - endpoint=101 size 0x48 has received: [hello core 0 message from core 1 - 2]
   Thread [1] core0: mode(1) message recv. The 1 time receiving
   Thread [1] send() start......
   Thread [1] CHECK_STATUS---send_i:MCAPI_PENDING
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of send() - endpoint=101 has sent: [hello core 1 messag from core 0 - 2]
   Thread [1] core0: mode(2) message send. The 2 time sending
   Thread [1] recv() start......
    node=1, port=5
   Thread [1] CHECK_STATUS---recv_i:MCAPI_SUCCESS
   Thread [1] CHECK_STATUS---wait:MCAPI_SUCCESS
   Thread [1] end of recv() - endpoint=101 size 0x48 has received: [hello core 0 message from core 1 - 3]
   Thread [1] core0: mode(2) message recv. The 2 time receiving
   Thread [1] CHECK_STATUS---del_ep:MCAPI_SUCCESS
   Thread [1] core0 3 rounds mode(2) Test PASSED!!
   Thread [1] test success
   mcapi_finalize 322

| 
| ---- **BACK TO** :doc:`Multi-Core Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/001_import_mcapi_example_into_cces.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/002_debug_or_release_mode_choosing.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/003_build_the_projects_in_cces.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/multicore/cces_debug_config_resume.jpg
