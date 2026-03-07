Linux MTD Driver
================

Introduction
------------

This section describes the steps required to build and use MTD(Memory Technology Device) subsystem on Linux using an ADSP-SC5xx board. The MTD software stack looks like below:

::

            MTD
   ------------------------
       SPI NOR framework
   ------------------------
           m25p80
   ------------------------
        SPI bus driver
   ------------------------
         SPI NOR chip

Hardware Setup
--------------

An ADSP-SC5xx EZ-Board:

::

    *ADSP-SC589 Ezkit v1.1 and above, or,
    *ADSP-SC584 Ezkit v1.0 and above, or,
    *ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above
    *ADSP-SC589 MINI v1.4 and above

Software Configuration
----------------------

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

The following configuration should be done on top of the SC589-ezkit/SC584-ezkit/SC573-ezkit/SC589-mini default configuration. Run bitbake linux-adi -c menuconfig and configure the kernel as follows: Enable MTD and SPI NOR flash w25x driver.

::

   Device Drivers  --->
       <*> Memory Technology Device (MTD) support  ---> 

           <*>   Command line partition table parsing
           <*>   Caching block device access to MTD devices
           <*>   SPI-NOR device support  --->
           Self-contained MTD device drivers  ---> 
               <*> Support most SPI Flash chips (AT26DF, M25P, W25X, ...)

Enable JFFS2 filesystem support.

::

   File systems  --->
       [*] Miscellaneous filesystems  --->
           <*>   Journalling Flash File System v2 (JFFS2) support

Enable Packages
~~~~~~~~~~~~~~~

Enable the mtd-utils and mtd-utils-ubifs support, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "mtd-utils mtd-utils-ubifs"

Example
-------

Get the MTD device info.

::

   # cat /proc/mtd 
   dev:    size   erasesize  name 
   mtd0: 00080000 00001000 "uboot (spi)" 
   mtd1: 00580000 00001000 "kernel (spi)" 
   mtd2: 00a00000 00001000 "root file system (spi)" 
   # mtdinfo 
   Count of MTD devices:           3 
   Present MTD devices:            mtd0, mtd1, mtd2 
   Sysfs interface supported:      yes 
   # mtdinfo /dev/mtd0 
   mtd0 
   Name:                           uboot (spi) 
   Type:                           nor 
   Eraseblock size:                4096 bytes, 4.0 KiB 
   Amount of eraseblocks:          128 (524288 bytes, 512.0 KiB) 
   Minimum input/output unit size: 1 byte 
   Sub-page size:                  1 byte 
   Character device major/minor:   90:0 
   Bad blocks are allowed:         false 
   Device is writable:             true 

Erase the MTD device.

::

   # flash_erase -j -q /dev/mtd1 0 0

Mount the MTD device.

::

   # mount -t jffs2 /dev/mtdblock1 /mnt

Read and Write data to the MTD device.

::

   # echo hello > /mnt/test
   # cat /mnt/test 
   hello

Unmount the MTD device.

::

   # umount /mnt

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
