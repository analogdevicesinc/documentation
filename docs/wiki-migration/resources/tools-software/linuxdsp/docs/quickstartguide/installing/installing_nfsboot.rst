How to Boot Linux From Network File System
==========================================

To boot Linux from NFS, users should put the kernel image and dtb file in **/tftpboot** directory and put the filesystem in HOST UBUNTU.

Filesystem Setup
----------------

Generate the Filesystem for NFS boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI provides two kinds of images to allow users to boot from NFS.

-  adsp-sc5xx-full
-  adsp-sc5xx-minimal

The minimal image is a subset of the full image which has less packages than full image. There is no difference for the Linux kernel in the minimal and full image.

Run "**bitbake <TARGET>**" to generate the images you want.

::

   $ bitbake adsp-sc5xx-full

or

::

   $ bitbake adsp-sc5xx-minimal

| If you want to compile and deploy the images at your second time, run the command "**bitbake <TARGET> -C compile**".
| If you want to add packages to filesystem, you could add package to **IMAGE_INSTALL_append = "<PACKAGE_NAME>"** in build/conf/local.conf file.

| 
| ==== Setting Up NFS Server ==== First follow the section **Setting Up NFS Server** in :doc:`Setting Up The Host </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/setting_up_your_host_pc>` to set up the nfs server in HOST Ubuntu.

| 
| ==== Unzip Filesystem to NFS root Directory ==== Second unzip the filesystem tar image in deploy directory to NFS root diretory.

::

   $ cd build/tmp/deploy/images/<MACHINE>/
   $ sudo tar -xf <FULL_FS_IMAGE/MINIMAL_FS_IMAGE> -C /romfs
   $ ls /romfs
   bin  boot  dev  etc  home  lib  media  mnt  opt  proc  run  sbin  sys  tmp  usr  var  www

See the **Appendix** at the bottom of this page to expand the <MACHINE> and <FULL_FS_IMAGE>or <MINIMAL_FS_IMAGE>.


| 

Copy zImage and dtb File
------------------------

The kernel image zImage and dtb file are loaded to target board through TFTP, first you should copy them to tftpboot directory.

::

   $ cp build/tmp/deploy/images/<MACHINE>/zImage /tftpboot
   $ cp build/tmp/deploy/images/<MACHINE>/<DTB_FILE> /tftpboot

|

Boot Linux From NFS
-------------------

Boot into U-boot and then run the command "**run nfsboot**":

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
   sc # run nfsboot

The linux kernel would then boot up and the file system stored in HOST Ubuntu is mounted via NFS.

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
| ====== Trouble Shooting ====== If the kernel stuck in the below and cannot enter into the login console, it should be a problem related with NFS server setup, you should run the above section "**Setting Up NFS Server**" again.

::

   ......
   cfg80211: Loading compiled-in X.509 certificates for regulatory database
   cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
   ALSA device list:
     #0: sc5xx-asoc-card
   platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
   cfg80211: failed to load regulatory.db

| 
| ====== Appendix: Macro Definition ======

+------------------+-----------------+-----------------------------------------+--------------------------------------------+
| ``MACHINE``      | ``DTB_FILE``    | ``FULL_FS_IMAGE``                       | ``MINIMAL_FS_IMAGE``                       |
+==================+=================+=========================================+============================================+
| adsp-sc589-mini  | sc589-mini.dtb  | adsp-sc5xx-full-adsp-sc589-mini.tar.xz  | adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz  |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+
| adsp-sc589-ezkit | sc589-ezkit.dtb | adsp-sc5xx-full-adsp-sc589-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+
| adsp-sc584-ezkit | sc584-ezkit.dtb | adsp-sc5xx-full-adsp-sc584-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc584-ezkit.tar.xz |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+
| adsp-sc573-ezkit | sc573-ezkit.dtb | adsp-sc5xx-full-adsp-sc573-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc573-ezkit.tar.xz |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+

| 
| ---- \**BACK TO: \*\* :doc:`Installing Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>` \**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
