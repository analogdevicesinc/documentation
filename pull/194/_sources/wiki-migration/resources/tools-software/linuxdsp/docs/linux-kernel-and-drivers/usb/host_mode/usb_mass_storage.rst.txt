USB Mass Storage
================

Hardware Configuration
----------------------

Connect the USB micro-A plug to A receptacle adaptor cable (found in the EZ-Board box) to the OTG port, below photo shows when it acts as Host and connected to a USB memory stick.


|image1|

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Host only mode, and enable the USB Mass Storage support. check the directory of "yocto/build" and Clean up and setup the linux-kernel configuration with commands:

.. code:: c++

   $ bitbake linux-adi -c cleansstate
   $ bitbake linux-adi -c menuconfig

And In the pop-up window of linux-kenel configuration, configure as follows Configure the USB drivers to host mode

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
           <*>   Support for Host-side USB
                   [*]   Enable USB persist by default 
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Host only mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra 

Configure to use the USB storage for host mode demonstrate

.. code:: shell

   Device Drivers  --->
           SCSI device support  --->
           <*> SCSI device support
           <*> SCSI disk support
       [*] USB support  --->
                   <*>   USB Mass Storage support

Then Save the linux-kernel configuration and build the target images:

.. code:: shell

   $ bitbake adsp-sc5xx-full

Example Usage
-------------

Boot the generated Images and connect the USB memory storage, kernel outputs messages looks like below:

.. code:: c++

   root@adsp-sc589-ezkit:~# usb 1-1: new high-speed USB device number 2 using musb-hdrc
   usb-storage 1-1:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1:1.0
   scsi 0:0:0:0: Direct-Access     SanDisk  Cruzer           8.02 PQ: 0 ANSI: 0 CCS
   sd 0:0:0:0: [sda] 3907583 512-byte logical blocks: (2.00 GB/1.86 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
    sda: sda1 sda2 sda3 sda4
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   root@adsp-sc589-ezkit:~# mke2fs /dev/sda1
   mke2fs 1.44.3 (10-July-2018)
   /dev/sda1 contains a vfat file system
   Creating filesystem with 409600 1k blocks and 102400 inodes
   Filesystem UUID: 10a5af3b-dd29-4eac-bbc8-80e1622a34a7
   Superblock backups stored on blocks:
           8193, 24577, 40961, 57345, 73729, 204801, 221185, 401409

   Allocating group tables: done
   Writing inode tables: done
   Writing superblocks and filesystem accounting information: done
   root@adsp-sc589-ezkit:~ # mount -t ext2 /dev/sda1 /mnt
   EXT4-fs (sda1): mounting ext2 file system using the ext4 subsystem
   EXT4-fs (sda1): mounted filesystem without journal. Opts: (null)
   root@adsp-sc589-ezkit:~# mount
   10.99.24.127:/romfs on / type nfs (rw,relatime,vers=3,rsize=4096,wsize=4096,namlen=255,hard,)
   devtmpfs on /dev type devtmpfs (rw,relatime,size=108844k,nr_inodes=27211,mode=755)
   proc on /proc type proc (rw,relatime)
   sysfs on /sys type sysfs (rw,relatime)
   debugfs on /sys/kernel/debug type debugfs (rw,relatime)
   tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
   tmpfs on /var/volatile type tmpfs (rw,relatime)
   devpts on /dev/pts type devpts (rw,relatime,gid=5,mode=620,ptmxmode=000)
   /dev/sda1 on /mnt type ext2 (rw,relatime,block_validity,barrier,user_xattr)
   root@adsp-sc589-ezkit:~# echo teststring > /mnt/usbhost_testfile; cat /mnt/usbhost_testfile
   teststring
   root@adsp-sc589-ezkit:~# date > /mnt/date_file; cat /mnt/date_file
   Thu Jul  2 09:09:08 UTC 2020
   root@adsp-sc589-ezkit:~# time dd conv=fsync if=/dev/zero of=/mnt/10m.bin bs=1M count=10
   10+0 records in
   10+0 records out

   real    0m6.440s
   user    0m0.004s
   sys     0m0.408s
   root@adsp-sc589-ezkit:~# ls /mnt/
   10m.bin           date_file         lost+found        usbhost_testfile
   root@adsp-sc589-ezkit:~# rm /mnt/usbhost_testfile; rm /mnt/*.bin;
   root@adsp-sc589-ezkit:~# ls /mnt/
   date_file   lost+found
   root@adsp-sc589-ezkit:~# umount /mnt
   root@adsp-sc589-ezkit:~# mount
   10.99.24.127:/romfs on / type nfs (rw,relatime,vers=3,rsize=4096,wsize=4096,namlen=255,hard,)
   devtmpfs on /dev type devtmpfs (rw,relatime,size=108844k,nr_inodes=27211,mode=755)
   proc on /proc type proc (rw,relatime)
   sysfs on /sys type sysfs (rw,relatime)
   debugfs on /sys/kernel/debug type debugfs (rw,relatime)
   tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
   tmpfs on /var/volatile type tmpfs (rw,relatime)
   devpts on /dev/pts type devpts (rw,relatime,gid=5,mode=620,ptmxmode=000)

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/001_usb_interface-host_application.jpg
