Remoteproc Drivers
==================

Introduction
------------

This page introduces the remoteproc support in linux kernel on ADI sc5xx platforms. The remoteproc framework allows users to control(load firmware, start and stop) remote processors from ARM side.

Hardware Setup
--------------

-  ADSP-SC589 Ezkit or,
-  ADSP-SC584 Ezkit or,
-  ADSP-SC573 Ezkit or,
-  ADSP-SC589 MINI

No connections are required except the uart, ethernet and power connections.

Software Configuration
----------------------

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

::

   $ bitbake linux-adi -c menuconfig
   Device Drivers  --->
      Remoteproc drivers  --->
         <*> Support for Remote Processor subsystem
         <*>   ADI remoteproc support

Then run **bitbake linux-adi -C compile** to generate kernel image zImage and dtb file.

Package Configuration
~~~~~~~~~~~~~~~~~~~~~

Add the firmware package in the filesystem, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "linux-firmware-adau1761"

Then run "**bitbake adsp-sc5xx-minimal -C compile**" or "**bitbake adsp-sc5xx-full -C compile**" to generate the filesystem.

| 
| ===== How to Use the Remoteproc Framework =====

Remote Processor Start
~~~~~~~~~~~~~~~~~~~~~~

Firmware Path
^^^^^^^^^^^^^

The firmware components are stored in the **/lib/firmware/** folder by default in the file system. Optionally another location can be set. Below the command for adding a new path for firmware parsing:

::

   root@adsp-sc589-ezkit:~# echo -n <firmware_path> > /sys/module/firmware_class/parameters/path

Set the firmware name through sysfs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   root@adsp-sc589-ezkit:~# echo blinky_Core1_sc589.ldr > /sys/class/remoteproc/remoteproc0/firmware

.. note::

   The blinky_Core1_sc589.ldr is one SHARC LED blinking application generated through ADI :adi:`CrossCore® Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>`. Refer this page for ``How to generate remoteproc LDR file in CCES``.


Start the SHARC Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   root@adsp-sc589-ezkit:~# echo start > /sys/class/remoteproc/remoteproc0/state

The LED will start blinking on sc589-ezkit board.

Remote Processor Stop
~~~~~~~~~~~~~~~~~~~~~

Run the below command, one SOFT irq would be raised through SEC interface to SHARC core, SHARC core will release all related resources(interrupts, hardwares, etc) and set itself to IDLE state once receiving the interrupt.

::

   root@adsp-sc589-ezkit:~# echo stop > /sys/class/remoteproc/remoteproc0/state

Remote Processor Auto Boot
~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI sets a specified name called adi_adsp_core1_fw.ldr or adi_adsp_core2_fw.ldr to auto boot when kernel starts. If you want to auto boot the remote processor, rename your own ldr file to **adi_adsp_core1_fw.ldr** or **adi_adsp_core1_fw.ldr** and put it in **/lib/firmware** directory.

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
