Mobile Storage Interface for MMC/SD
===================================

The ADSP-SC5xx processors provide a mobile storage interface (MSI). MSI is a fast, synchronous controller that uses various protocols to communicate with MMC, SD, and SDIO cards to address the growing storage need in embedded systems, handheld and consumer electronics applications requiring low power. The MSI is compatible with the following protocols.

-  MMC (Multimedia Card) bus protocol
-  SD (Secure Digital) bus protocol
-  SDIO (Secure Digital Input Output) bus protocol

All of these storage solutions use similar interface protocols. The main difference between MMC and SD support is the initialization sequence. The main difference between SD and SDIO support is the use of interrupt and read wait signals for SDIO.

Hardware Setup
--------------

An ADSP-SC5xx EZ-Board:

-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above or,
-  ADSP-SC589 MINI v1.3 and above
-  SC584 processor does not include MMC/SD controller

The SD/MMC card slot is **J18** on the SC589/SC573 EZKIT board and is **J6** on the SC589 MINI board. This slot accepts full-size SD and MMC cards, or microSD cards with an adapter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mmc/lkad-mobile_storage_interface_for_mmc-hw_setup.jpg
   :width: 400px

| 
| ===== Software Configuration =====

Package Configuration
~~~~~~~~~~~~~~~~~~~~~

Add Bonnie++ package in the filesystem. Bonnie++ is a program for testing filesystem throughput, see www.coker.com.au/bonnie++ for details.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = " dosfstools e2fsprogs bonnie++"

| 
| ==== Configure Linux Kernel ==== Run “\ **bitbake linux-adi -c menuconfig**\ ” to configure the linux kernel.

Enable MSI Support
^^^^^^^^^^^^^^^^^^

::

   Device Drivers
       MMC/SD/SDIO card support  --->
           <*> Synopsys DesignWare Memory Card Interface
           -*-   Synopsys Designware MCI Support as platform device
           <*>   ADI specific extensions for Synopsys DW Memory Card Interface  

File System Support
^^^^^^^^^^^^^^^^^^^

If you want to mount an SD card in a particular format, you should compile the Linux kernel with the corresponding file-system first.

**Example1**\ ：FAT32 SD card, corresponding filesystem is VFAT.  Configuration is shown below:

::

   File systems --->
       DOS/FAT/NT Filesystems  --->
               [*] VFAT (Windows-95) fs support
           (437) Default codepage for FAT
           (iso8859-1) Default iocharset for FAT

**Example2**: ext2 SD card, corresponding filesystem is ext2.  Configuration is shown below:

::

   File systems --->
       <*> Second extended fs support
       [*]   Ext2 extended attributes
       [*]     Ext2 POSIX Access Control Lists
       [*]     Ext2 Security Labels 

Build and Load Linux Kernel
---------------------------

Run “\ **bitbake linux-adi -C compile**\ ” to compile the linux kernel to generate the zImage and dtb file.

A kernel image and dtb file can now be built and loaded onto the target board.  See SC5xx ezkit Linux quick start guide for details.

| 
| ===== Usage of MSI ===== The most typical use of an SD Card in embedded applications is as a removable storage device (disk) that can be easily taken from the embedded target board. In such contexts, the SD Card installed to the embedded target board is typically already formatted with an MS-DOS file system. The Linux kernel must be specially configured to allow mounting the MS-DOS file system. See part 2 in section 2.1 for details. The mount utility is also needed. Typically,  mount will already be enabled in your busybox configuration.

Formatting the SD Card
~~~~~~~~~~~~~~~~~~~~~~

In order to use an SD Card with Linux we need to prepare it by formatting it in the correct format.

This section of instructions requires you to correctly identify the SD Card and format the card. If you select the wrong drive you may cause irreversible damage to you Host PC.

To format the SD Card, follow the commands below. The example code in this section assumes that the SD Card device is reported to be /dev/sdb. Ensure that you change these commands to use your device.

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

\*\* Format the SD card to MS-DOS (FAT) filesystem \*\*

::

   # mkfs.vfat -F 32 /dev/mmcblk0p1

\*\* Format the SD card to EXT filesystem \*\*

::

   # mkfs.ext3 /dev/mmcblk0p1

| 
| === Insert a pre-formatted card with an MS-DOS (FAT) file system to the SD Card slot on the ADSP-SC5xx === When you boot the zImage on the ADSP-SC5xx, there should be messages similar to the ones shown below. In the below example, Linux has detected an SD Card with a single partition on it:

::

   mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 25000000Hz, actual 25000000HZ div = 1)
   mmc0: new SD card at address b368
   mmcblk0: mmc0:b368 FFFFF 1.85 GiB   

| 
| ==== Mount the MS-DOS file system on the SD Card ==== This is done as follows:

::


   # mount -t vfat -o sync /dev/mmcblk0p1 /mnt 

Check that the file system has indeed been mounted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the last line in the below output:

::

   # mount 
   rootfs on / type rootfs (rw) 
   devtmpfs on /dev type devtmpfs (rw,relatime,size=42740k,nr_inodes=10685,mode=755) 
   proc on /proc type proc (rw,relatime) 
   devpts on /dev/pts type devpts (rw,relatime,gid=5,mode=620) 
   tmpfs on /dev/shm type tmpfs (rw,relatime,mode=777) 
   tmpfs on /tmp type tmpfs (rw,relatime,mode=777) 
   sysfs on /sys type sysfs (rw,relatime) 
   debugfs on /sys/kernel/debug type 
   debugfs (rw,relatime) 
   /dev/mmcblk0p1 on /mnt type vfat (rw,sync,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro)  

Write something to the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the below example, we store the current date and time to a log file, although in real-life applications you will probably want to do something more meaningful:

::

   # date > /mnt/log.file 

Verify the written content by reading the log file back
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   # cat /mnt/log.file
   Fri Jul 17 05:31:49 UTC 2020

Unmount the file system and then extract the card from the SD card slot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can remove the card the from the embedded target board.

::

   # umount /mnt
   mmc0: card b368 removed

| 
| ===== Test MSI Performance with Bonnie++ =====

1) Test Case 1: Bonnie++ on Ext2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input the following command on the target board console

::

   root@adsp-sc589-ezkit:~# mkfs.ext2 /dev/mmcblk0p1
   root@adsp-sc589-ezkit:~# mount /dev/mmcblk0p1 /mnt/
   root@adsp-sc589-ezkit:~# bonnie++ -u root -d /mnt/ 

Result
^^^^^^

::

   Using uid:0, gid:0.
   Writing with putc()...done
   Writing intelligently...done
   Rewriting...done
   Reading with getc()...done
   Reading intelligently...done
   start 'em...done...done...done...
   Create files in sequential order...done.
   Stat files in sequential order...done.
   Delete files in sequential order...done.
   Create files in random order...done.
   Stat files in random order...done.
   Delete files in random order...done.
   Version  1.04       ------Sequential Output------ --Sequential Input- --Random-
                       -Per Chr- --Block-- -Rewrite- -Per Chr- --Block-- --Seeks--
   Machine        Size K/sec %CP K/sec %CP K/sec %CP K/sec %CP K/sec %CP  /sec %CP
   adsp-sc589-ezk 424M  7985  77  8227   8  3920   6  8538  90  8660   6  1220  18
                       ------Sequential Create------ --------Random Create--------
                       -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
                 files  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
                    16  6513  92 16713  84 10240  97   149  98 +++++ +++ 12912  98
   adsp-sc589-ezkit,424M,7985,77,8227,8,3920,6,8538,90,8660,6,1220.4,18,16,6513,92,16713,84,10240,97,149,98,+++++,+++,12912,98

| 
| ==== 2) Test Case 2: Bonnie++ on FAT32 ==== Input the following command on the target board console

::

   root@adsp-sc589-ezkit:~# mkfs.vfat -F 32 /dev/mmcblk0p1
   root@adsp-sc589-ezkit:~# mount /dev/mmcblk0p1 /mnt/
   root@adsp-sc589-ezkit:~# bonnie++ -u root -d /mnt/ 
   Using uid:0, gid:0.
   Writing with putc()...done
   Writing intelligently...done
   Rewriting...done
   Reading with getc()...done
   Reading intelligently...done
   start 'em...done...done...done...
   Create files in sequential order...done.
   Stat files in sequential order...done.
   Delete files in sequential order...done.
   Create files in random order...done.
   Stat files in random order...done.
   Delete files in random order...done.
   Version  1.04       ------Sequential Output------ --Sequential Input- --Random-
                       -Per Chr- --Block-- -Rewrite- -Per Chr- --Block-- --Seeks--
   Machine        Size K/sec %CP K/sec %CP K/sec %CP K/sec %CP K/sec %CP  /sec %CP
   adsp-sc589-ezk 424M  4405  44  6886  10  4026   7  8360  89  8658   6 803.4  12
                       ------Sequential Create------ --------Random Create--------
                       -Create-- --Read--- -Delete-- -Create-- --Read--- -Delete--
                 files  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP  /sec %CP
                    16     9  99 +++++ +++   147  99    17  99 +++++ +++    39  98
   adsp-sc589-ezkit,424M,4405,44,6886,10,4026,7,8360,89,8658,6,803.4,12,16,9,99,+++++,+++,147,99,17,99,+++++,+++,39,98

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
