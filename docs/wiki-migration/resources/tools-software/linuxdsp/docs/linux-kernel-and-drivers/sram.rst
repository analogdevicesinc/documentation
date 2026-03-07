SRAM driver
===========

Introduction
------------

This page introduces the SRAM driver in ADI linux kernel for sc5xx ezkit boards. Users could allocate memory from specified sram pool defined in dts. sram_mmap driver in this page is an example for this. For how to enable the sram_mmap, please see the below sections.

Package Configuration
---------------------

::

   vim conf/local.conf
   IMAGE_INSTALL_append = " sram-mmap-test"

Kernel config
-------------

Disable icc driver
~~~~~~~~~~~~~~~~~~

::

   bitbake linux-adi -c menuconfig
   Device Drivers  --->
          [*] Staging drivers  --->
                [N]   icc driver  ----

Enable sram driver
~~~~~~~~~~~~~~~~~~

::

   bitbake linux-adi -c menuconfig
   Device Drivers  --->
          Misc devices  --->
               [*] Generic on-chip SRAM driver
               [*] MMAP driver for sc5xx onchip SRAM
               [*] /proc/sraminfo support for sc5xx onchip SRAM

Test Example
------------

::

   # sram_mmap /dev/sram_mmap
   sram mmaped 0x20084000 : 0x20085000 successfully!
   mmap pass.
   # cat /proc/sraminfo
   sram-icc@20080000:
   Total size: 4 KB
   Used sram: 0 KB
   Avail sram: 4 KB
   sram-reserved@20084000:
   Total size: 236 KB
   Used sram: 0 KB
   Avail sram: 236 KB

.. _sram-driver-1:

SRAM driver
-----------

There are two main c files under the driver/sram/adi directory.

::

   ; **''sram.c''**
   : will create a /proc/sraminfo in filesytem, control/monitor the sram memory, use the command "#cat /proc/sraminfo"
   ; **''sram_mmap.c''**
   : one example to use the sram framework, allocate memory from the specified pool defined in dts, and then free the memory

Reserved SRAM pools in dts file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These 2 dts part will generate 2 memory pools from sram using "mmio-sram" driver.

::

   sram0: sram-icc@20080000 { /* ICC SRAM 4KB */
       compatible = "mmio-sram";
       #address-cells = <1>;
       #size-cells = <1>;
       reg = <0x20080000 0x1000>;
       ranges = <0 0x20080000 0x1000>;
   };
    
   sram1: sram-reserved@20084000 {
       compatible = "mmio-sram";
       #address-cells = <1>;
       #size-cells = <1>;
       reg = <0x20084000 0x3B000>;
       ranges = <0 0x20084000 0x3B000>;
   };

How to add another device to use the memory in sram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If users want to allocate their own sram memory from sram pool in linux kernel, they should first

-  add below line dts in your own device

::

   adi,sram = <&sram1>;

-  Add below code in your device driver source code

::

   /* Get the sram pool from dts */
   sram_pool = of_gen_pool_get(dev->of_node, "adi,sram", 0);
   if (!sram_pool) {
           pr_err("Unable to get sram pool!\n");
           return -ENODEV;
   }
    
   /* Get the allocated virtual memory from sram pool */
   vaddr = gen_pool_alloc(sram_pool, sram_size);
   if (!vaddr) {
       pr_warn("Faied to alloc sram from sram pool!\n");
   }
    
   /* Remember: When you finish all the operations, free the allocated addr */
   gen_pool_free(sram_pool, vaddr, sram_size);

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
