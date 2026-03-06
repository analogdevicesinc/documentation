How to Boot Linux From SD Card
==============================

To boot Linux from SD Card, users should put the kernel image and dtb file along with a file system located on the SD Card.

Generate the Filesystem for SD Card Boot
----------------------------------------

For users want to use ``run ramboot_emmc`` boot method, do the following commands to prepare the ramdisk filesystem file.

::

   $ bitbake adsp-sc5xx-ramdisk

| 
| For users want to use ``run sdcardboot`` boot method, ADI provides two kinds of images to allow users to boot from SD Card using sdcardboot boot command.

-  adsp-sc5xx-full
-  adsp-sc5xx-minimal

The minimal image is a subset of the full image which has less packages than full image. There is no difference for the Linux kernel in the minimal and full image.

Run "**bitbake <TARGET>**" to generate the images you want.

::

   $ bitbake adsp-sc5xx-full

or

::

   $ bitbake adspsc5xx-minimal

.. note::

   If you want to compile and deploy the images at your second time, run the command "**bitbake <TARGET> -C compile**".

   
   | 
   | If you want to add packages to filesystem, you could add package to **IMAGE_INSTALL_append = "<PACKAGE_NAME>"** in build/conf/local.conf file.
   
   |


SD Card Set Up
--------------

Formatting the SD Card
~~~~~~~~~~~~~~~~~~~~~~

In order to use an SD Card with Linux we need to prepare it by formatting it in the correct format. This section of instructions requires you to correctly identify the SD Card and format the card. If you select the wrong drive you may cause irreversible damage to you Host PC. To format the SD Card, follow the commands below. The example code in this section assumes that the SD Card device is reported to be /dev/sdb. Ensure that you change these commands to use your device.

::

   $ sudo fdisk /dev/sdb
   /* Create primary partition 1, 256M size*/
   Command (m for help): n
   Select (default p): p
   Partition number (1-4, default 1): 1
   First sector (2048-3887103, default 2048): PRESS ENTER
   Last sector, +sectors or +size{K,M,G} (2048-3887103, default 3887103): PRESS ENTER

   /* Save partition */
   Command (m for help): w

**Format the SD card to EXT filesystem**

::

   $ sudo mkfs.ext2 /dev/sdb1

| 
| ==== Writing the file system to the SD Card ==== Next, we need to copy the Linux file system and kernel image to the SD Card. We install this on to the SD Card by mounting the file system on to the local Host PC and copying the contents on to the SD Card.

::

   $ sudo mount -t ext2 /dev/sdb1 /mnt

For users want to use ``run ramboot_emmc`` boot method, users copy the following files into SD card.

::

   $ sudo cp build/tmp/deploy/images/<MACHINE>/<RAMDISK_FILE> /mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp build/tmp/deploy/images/<MACHINE>/<DTB_FILE> /mnt/boot/
   $ sudo cp build/tmp/deploy/images/<MACHINE>/zImage /mnt/boot/
   $ sudo umount /mnt

For users want to use ``run sdcardboot`` boot method, users copy the following files into SD card.

::

   $ sudo tar -xf build/tmp/deploy/images/<MACHINE>/<FULL/MINIMAL_FS_IMAGE> -C /mnt
   $ sudo cp build/tmp/deploy/images/<MACHINE>/<DTB_FILE> /mnt/boot/
   $ sudo cp build/tmp/deploy/images/<MACHINE>/zImage /mnt/boot/
   $ sudo umount /mnt

The file system and kernel image are now installed on to the SD Card. The SD Card can now be safely removed from the Host PC.

Booting Linux From SD Card
--------------------------

Insert the SD card to target board, and reset the board and enter into U-Boot

::

   U-Boot 2015.01 ADI-YOCTO-1.0.0 (May 14 2020 - 19:26:23)

   CPU:   ADSP ADSP-SC589-0.1 (Detected Rev: 1.1) (spi flash boot)
   VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 450 MHz
   OCLK: 150 MHz
          Watchdog enabled
   I2C:   ready
   DRAM:  224 MiB
   MMC:   SC5XX SDH: 0                                                                                                        
   SF: Detected IS25LP512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB                                           
   In:    serial                                                                                                              
   Out:   serial                                                                                                              
   Err:   serial                                                                                                              
   other init                                                                                                                 
   Net:   dwmac.3100c000                                                                                                      
   Hit any key to stop autoboot:  0                                                                                           
   sc # run sdcardboot
   or 
   sc # run ramboot_emmc

The linux kernel would then boot up and the file system stored in SD card.

::

   ......
   Starting syslogd/klogd: done
     * Starting Avahi mDNS/DNS-SD Daemon: avahi-daemon
      ...done.


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
        
   adsp-sc589-mini login: root
   Password: adi

The default username is **root** and the password is **adi**.

| 
| ====== Appendix: Macro Definition ======

+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| ``MACHINE``      | ``DTB_FILE``    | ``FULL_FS_IMAGE``                       | ``MINIMAL_FS_IMAGE``                       | '' RAMDISK_FILE''                                  |
+==================+=================+=========================================+============================================+====================================================+
| adsp-sc589-mini  | sc589-mini.dtb  | adsp-sc5xx-full-adsp-sc589-mini.tar.xz  | adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz  | adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz.u-boot  |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| adsp-sc589-ezkit | sc589-ezkit.dtb | adsp-sc5xx-full-adsp-sc589-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz | adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz.u-boot |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| adsp-sc584-ezkit | sc584-ezkit.dtb | adsp-sc5xx-full-adsp-sc584-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc584-ezkit.tar.xz | adsp-sc5xx-ramdisk-adsp-sc584-ezkit.cpio.xz.u-boot |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| adsp-sc573-ezkit | sc573-ezkit.dtb | adsp-sc5xx-full-adsp-sc573-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc573-ezkit.tar.xz | adsp-sc5xx-ramdisk-adsp-sc573-ezkit.cpio.xz.u-boot |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+

| 
| ---- \**BACK TO: \*\* :doc:`Installing Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>` \**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
