USB Gadget Mass storage
=======================

This page provides how to use the USB Gadget mass storage on ADSP-SC5xx board, and it will include the below test:

-  USB gadget mass storage ram test
-  USB Gadget mass storage hd test

--------------

Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS/OTG Device port, as showing below:


|image1|

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Gadget only mode, and enable the USB Gadget Mass Storage relevant options.

.. code:: c++

   $ bitbake linux-adi -c menuconfig

**Configure the USB drivers to Gadget only mode (or Dual role mode )**

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Gadget only mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra
                   <*>   USB Gadget Support  --->

\**Configure the Gadget Mass Storage Support \*\*

.. code:: shell

   Device Drivers  --
   ->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Mass Storage Gadget   

--------------

Example Usage
-------------

**on the target Ez-Kit board**

.. code:: c++

   root@adsp-sc589-ezkit:~# dd if=/dev/zero of=/fsg.block bs=1M count=16
   16+0 records in
   16+0 records out
   root@adsp-sc589-ezkit:~# modprobe g_mass_storage file=/fsg.block stall=0
   Mass Storage Function, version: 2009/09/11
   LUN: removable file: (no medium)
   LUN: file: /fsg.block
   Number of LUNs=1
   g_mass_storage gadget: Mass Storage Gadget, version: 2009/09/11
   g_mass_storage gadget: userspace failed to provide iSerialNumber
   g_mass_storage gadget: g_mass_storage ready
   g_mass_storage gadget: high-speed config #1: Linux File-Backed Storage

**On the Linux-Host PC**

-  **Fdisk and format the usb mass storage**

.. code:: c++

   root@madara:~# sudo su
   root@madara:~# ls /dev/sdb
   /dev/sdb
   root@madara:~#  time fdisk /dev/sdb
   Welcome to fdisk (util-linux 2.31.1).
   Changes will remain in memory only, until you decide to write them.
   Be careful before using the write command.

   Device does not contain a recognized partition table.
   Created a new DOS disklabel with disk identifier 0x7459b8e4.

   Command (m for help): n
   Partition type
      p   primary (0 primary, 0 extended, 4 free)
      e   extended (container for logical partitions)
   Select (default p): p
   Partition number (1-4, default 1): 1
   First sector (2048-32767, default 2048):
   Last sector, +sectors or +size{K,M,G,T,P} (2048-32767, default 32767):

   Created a new partition 1 of type 'Linux' and of size 15 MiB.

   Command (m for help): w
   The partition table has been altered.
   Calling ioctl() to re-read partition table.
   Syncing disks.
   real    0m10.807s
   user    0m0.000s
   sys     0m0.008s

   root@madara:~# mke2fs /dev/sdb1
   mke2fs 1.44.1 (24-Mar-2018)
   Creating filesystem with 15360 1k blocks and 3840 inodes
   Filesystem UUID: 3bd2120b-eca2-4c8f-9eb6-c408f9c1c0d9
   Superblock backups stored on blocks:
           8193

   Allocating group tables: done
   Writing inode tables: done
   Writing superblocks and filesystem accounting information: done

-  **Read/write test**

.. code:: c++

   root@madara:~# mkdir /met/usb
   root@madara:~# mount /dev/sdb1 /mnt/usb/
   root@madara:~# date; time dd if=/dev/zero of=/mnt/usb/10m.bin bs=1M
   Tuesday 14 July 2020 15:09:16 CST
   dd: error writing '/mnt/usb/10m.bin': No space left on device
   15+0 records in
   14+0 records out
   15032320 bytes (15 MB, 14 MiB) copied, 8.89978 s, 1.7 MB/s

   real    0m8.901s
   user    0m0.000s
   sys     0m0.309s
   root@madara:~# ls -lh /mnt/usb
   total 15M
   -rw-r--r-- 1 root root 15M July  14 16:08 10m.bin
   drwx------ 2 root root 12K July 14 15:52 lost+found
   root@madara:~# rm /mnt/usb/10m.bin
   root@madara:~# ls -lh /mnt/usb/
   total 12K
   drwx------ 2 root root 12K July  14 15:52 lost+found
   root@madara:~# umount /mnt/usb

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
