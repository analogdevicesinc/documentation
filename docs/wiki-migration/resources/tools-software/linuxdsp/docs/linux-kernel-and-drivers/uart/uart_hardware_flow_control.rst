User manual for uart hardware flow control in linux kernel
==========================================================

Introduction
------------

This section describes the steps required to enable UART hardware flow control on ADSP-SC5xx board.

Hardware Setup
--------------

-  An ADSP-SC5xx EZ-Board:
-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

The UART interface is the **USB to UART** port on the ADSP-SC5xx EZ-board.

| 
| ===== Software Configuration =====

Configure Linux kernel
~~~~~~~~~~~~~~~~~~~~~~

::

   Device Drivers  --->
         Character devices  --->
               Serial drivers  --->
                     <*> ADI uart4 serial port support
                     [*]   Console on ADI uart4 serial port

Configure Device tree
~~~~~~~~~~~~~~~~~~~~~

Run “bitbake linux-adi -c devshell” to enter into the kernel source code and then change the device tree files.

Add in uart0 node of **'linux source code directory'/arch/arm/boot/dts/sc58x.dtsi** or **'linux source code directory'/arch/arm/boot/dts/sc57x.dtsi**

::

   uart0: uart@0x31003000 {
   ...
   adi,uart-has-rtscts;
   ...
   }; 

Then run bitbake linux-adi -C compile to generate kernel image zImage and dtb file.

Package Configuration
~~~~~~~~~~~~~~~~~~~~~

Add the rtscts-test package in the filesystem, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "rtscts-test"

Then run “bitbake adsp-sc5xx-minimal -C compile” or “bitbake adsp-sc5xx-full -C compile” to generate the filesystem.

Example
-------

Preliminary setup
~~~~~~~~~~~~~~~~~

Setting serial port parameter

::

   # minicom -s
   Select "Serial port setup"
   Select "F - Hardware Flow Control: Yes"

Test
~~~~

.. note::

   SD CARD shouldn't be in the card slot due to the pin signal interference.


**1) Input invalid before Linux boot up**

After powering-off and restarting the board you will find that UBoot doesn't accept the input from the serial console. Instead it automatically boot up kernel according to its predefined parameters. Once the Linux kernel has been booted it will accept input..

**2) run rtscts_test case**

::

   # rtscts_test ttySC0 -t

.. note::

   In the above command the serial device is given as an example, and will not necessarily be ttySC0.


--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
