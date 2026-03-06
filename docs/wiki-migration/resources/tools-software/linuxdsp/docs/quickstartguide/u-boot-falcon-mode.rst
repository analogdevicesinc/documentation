U-Boot Falcon Mode
==================

This page provides instructions for using U-Boot Falcon Mode on ADSP-SC59X boards.

.. note::

   The Falcon Mode feature is supported on versions :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>` and later and on SC59x.


What is Falcon Mode?
--------------------

It is described in the upstream repo of U-Boot: `U-Boot Falcon Mode <https://github.com/u-boot/u-boot/blob/master/doc/README.falcon>`__. In short, it's a way to shorten the boot time by allowing the SPL (Secondary Program Loader) to boot the kernel directly, without loading the full bootloader.

Requirements
------------

You must use :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>` or later on an SC59x board.

Build U-Boot with Falcon Mode support
-------------------------------------

When following the Quickstart guides and specifically right after sourcing the setup script, i.e.

.. code:: bash

   $ source setup-environment -m adsp-sc598-som-ezkit

a build folder along with a local build configuration file is created, under ``$PROJECT_DIR/build/conf/local.conf``. Edit this file with your favourite text editor, and append the following two lines to it:

.. code:: bash

   MACHINE_FEATURES:remove = " spl"
   MACHINE_FEATURES:append = " falcon"

and proceed to building and flashing the image, as usual and as seen on the Quickstart guides.

Booting with Falcon Mode
------------------------

When U-Boot with Falcon Mode support has been built and flashed onto the board, the default behaviour will be booting the default mode (SPI boot, if unchanged) straight from the SPL, e.g.:

.. code:: bash

   U-Boot SPL 2020.10 (Apr 12 2023 - 18:48:14 +0000)
   ADI Boot Mode: 0x1 (QSPI Master)
   Trying to boot from SPI
   ## Loading kernel from FIT Image at 96000000 ...
      Using 'conf-1' configuration
      Verifying Hash Integrity ... OK
      Trying 'kernel-1' kernel subimage
   Verifying Hash Integrity ... sha1+ sha1,rsa2048:dev- OK
      Loading kernel from 0x960000e0 to 0x9a200000
      Uncompressing Kernel Image
   ## Loading ramdisk from FIT Image at 96000000 ...
      Using 'conf-1' configuration
      Verifying Hash Integrity ... OK
      Trying 'ramdisk-3' ramdisk subimage
      Verifying Hash Integrity ... sha1+ sha1,rsa2048:dev- OK
      Loading ramdisk from 0x965a1e50 to 0x9c000000
   ## Loading fdt from FIT Image at 96000000 ...
      Using 'conf-1' configuration 
      Verifying Hash Integrity ... OK
      Trying 'fdt-2' fdt subimage  
      Verifying Hash Integrity ... sha1+ sha1,rsa2048:dev- OK
      Loading fdt from 0x9659ac00 to 0x99000000
   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    0.000000] Linux version 5.15.78-yocto-standard (oe-user@oe-host) (aarch64-poky-linux-musl-gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.38.20220313) #1 SMP PREEMPT Wed Apr 12 17:53:07 UTC 2023
   [    0.000000] Machine model: ADI 64-bit SC598 SOM EZ Kit
   [    0.000000] earlycon: adi_uart0 at MMIO 0x0000000031003000 (options '')
   [    0.000000] printk: bootconsole [adi_uart0] enabled
   [    0.000000] efi: UEFI not found.

You can still fall back to U-Boot Proper by holding down the push button ``PB1`` on the target (carrier) board during reset/booting:


|image1|

You will then be able to use the full U-Boot:

.. code:: bash

   U-Boot SPL 2020.10 (Apr 12 2023 - 18:48:14 +0000)
   Pushbutton helding during boot -- entering U-Boot ProperADI Boot Mode: 0x1 (QSPI Master)
   Trying to boot from BOOTROM


   U-Boot 2020.10 (Apr 12 2023 - 18:48:14 +0000)

   CPU:   ADSP ADSP-SC598-0.0 (spi slave boot)
   Model: ADI sc598-som-ezkit
   DRAM:  224 MiB
   WDT:   Not found!
   MMC:   mmc@310C7000: 0
   Loading Environment from SPIFlash... SF: Detected is25lp512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   OK
   In:    serial@0x31003000
   Out:   serial@0x31003000
   Err:   serial@0x31003000
   Net:   eth0: eth0
   Hit any key to stop autoboot:  0

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/sc598_pb1.jpg
   :width: 400px
