Installing Linux On The Hardware
================================

Linux on the ADSP-SC5xx can be configured to boot from various sources (flash, network, SD Card, USB). For the Getting Started Guide we will configure the system so that the U-Boot bootloader is installed into flash on the development board. Linux and the filesystem will be downloaded at boot time via **TFTP** from your host PC, and copied into RAM. This method of **network boot** is convenient when developing Linux as it provides an easy method to update the image that is booted onto the board.

.. important::

   The steps on this page require multiple terminal windows to be active. Take care to use the correct window for each step


Booting into U-Boot
-------------------

First you should make sure the U-boot has been written into the flash. You should see the outputs after powering up the board

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
   sc #

If no output please refer this page :doc:`Installing U-boot </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing_uboot>` to build and write the U-Boot onto flash.

| 
| ==== Boot Commands in U-Boot Environemt ==== When you run **printenv** in u-Boot console, there will be 4 boot methods in the U-boot.

-  nfsboot=tftp ${loadaddr} ${nfsfile};tftp ${dtbaddr} ${dtbfile};run nfsargs;run addip;bootz ${loadaddr} - ${dtbaddr}
-  norboot=tftp ${loadaddr} ${ramfile};tftp ${dtbaddr} ${dtbfile};run ramargs;run addip;bootz ${loadaddr} - ${dtbaddr}
-  ramboot=tftp ${loadaddr} ${ramfile};tftp ${dtbaddr} ${dtbfile};tftp ${initramaddr} ${initramfile};run ramargs;run addip;bootz ${loadaddr} ${initramaddr} ${dtbaddr}
-  ramboot_emmc=mmc rescan;mmc dev 0 0;ext2load mmc 0:1 :math:`{loadaddr} /boot/`\ {ramfile};ext2load mmc 0:1 :math:`{dtbaddr} /boot/`\ {dtbfile};ext2load mmc 0:1 :math:`{initramaddr} /boot/`\ {initramfile};run sdcardargs;run addi}
-  sdcardboot=mmc rescan;mmc dev 0 0;ext2load mmc 0:1 :math:`{loadaddr} /boot/`\ {ramfile};ext2load mmc 0:1 :math:`{dtbaddr} /boot/`\ {dtbfile};run sdcardargs;bootz ${loadaddr} - ${dtbaddr}

The default boot command is **run ramboot**.

| 
| ===== Booting Linux ===== Currently ADI provides some deploy methods to load linux kernel and boot into console. The default deploy method is ramboot.

| 
| ==== RAM Boot ==== In order to boot Linux, a copy of the **image file** should be copied into the **/tftpboot** directory. This file will be downloaded by U-Boot when the board begins to boot. In a console, in the **build** directory of your workspace issue the following commands:

::

   $ cp tmp/deploy/images/<MACHINE>/zImage /tftpboot
   $ cp tmp/deploy/images/<MACHINE>/<DTB_FILE> /tftpboot
   $ cp tmp/deploy/images/<MACHINE>/<RAMDISK_FILE> /tftpboot/ramdisk.cpio.xz.u-boot

Where the macros in the above command are listed at the bottom of this page in **Appendix**.

| 
| Next, reboot the board and Linux will be downloaded to the target board and boot. When boot is successful you will be presented by the ADI logo and the login prompt:

::

   sc # set serverip <SERVERIP>
   sc # set ipaddr <BOARD_IP>
   or
   sc # dhcp
   sc #
   sc # boot 
   or 
   sc # run ramboot
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
| ==== NFS Boot ==== This boot method would finally use the Network File System which is stored in local Ubuntu Host. This is suggested when you do application development. For how to boot Linux via NFS, please refer to ":doc:`How to Boot Linux From NFS </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing/installing_nfsboot>`".

| 
| ==== SD Card Boot ==== There are two kinds of boot commands for booting Linux from SD card.

::

   ;''ramboot_emmc''  : Booting Linux using zImage, dtb file and ramdisk file which are stored in SD card
   ;''sdcardboot''  : Booting Linux using zImage, dtb file and file system file which are stored in SD card

And please make sure there are 500 MB at least in SD card to store zImge, dtb and system file.

For how to boot Linux via SD card, please refer to ":doc:`How to Boot Linux From SD Card </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing/installing_sdcardboot>`"

| 
| ==== NOR Boot ==== Due to the limited flash size, currently we can only support NOR boot the Linux kernel image(zImage) and device tree file(dtb). Put the filesystem in local HOST or SD Card is suggested.

| 
| ====== Appendix: Macro Definition ======

+------------------+-----------------+----------------------------------------------------+
| ``MACHINE``      | ``DTB_FILE``    | ``RAMDISK_FILE``                                   |
+==================+=================+====================================================+
| adsp-sc589-mini  | sc589-mini.dtb  | adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz.u-boot  |
+------------------+-----------------+----------------------------------------------------+
| adsp-sc589-ezkit | sc589-ezkit.dtb | adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz.u-boot |
+------------------+-----------------+----------------------------------------------------+
| adsp-sc584-ezkit | sc584-ezkit.dtb | adsp-sc5xx-ramdisk-adsp-sc584-ezkit.cpio.xz.u-boot |
+------------------+-----------------+----------------------------------------------------+
| adsp-sc573-ezkit | sc573-ezkit.dtb | adsp-sc5xx-ramdisk-adsp-sc573-ezkit.cpio.xz.u-boot |
+------------------+-----------------+----------------------------------------------------+

| 
| ---- \*\* PREV::doc:`Building The Components </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building>`\ HOME PAGE:\*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
