Altera SOC Quick Start Guide
============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. A better and more concise version of this page can be found at https://analogdevicesinc.github.io/hdl/user_guide/build_intel_boot_image.html\


Download Prebuild Images
------------------------

.. admonition:: Download
   :class: download

   
   -  :doc:`Download Release Images </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>`
   


Now, depending if you are using Linux or Windows, follow these instructions to write the file to your SD card.

-  :doc:`linux_hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`
-  :doc:`windows_hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

ADRV9371 + Arria 10 SoC Development Kit
---------------------------------------

Download Links
~~~~~~~~~~~~~~

HDL Project: |:git-hdl:`projects/adrv9371x/a10soc|`

Linux Kernel:


|https://github.com/analogdevicesinc/linux|

Building the Linux Kernel image and the Devicetree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the kernel tree, point environment to an arm architecture cross compiler, build the configuration file, build the image, and lastly build the project and board specific device tree. See :doc:`socfpga </wiki-migration/resources/tools-software/linux-build/generic/socfpga>` for a more detailed explanation.

::

   $ git clone https:%%//%%github.com/analogdevicesinc/linux.git
   $ cd linux
   /linux$ export ARCH=arm
   /linux$ export CROSS_COMPILE=/path/to/your/arm/cross-compiler
   /linux$ make socfpga_adi_defconfig
   /linux$ make zImage -j4
   /linux$ make socfpga_arria10_socdk_adrv9371.dtb

Building the Hardware Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you skipped the instruction on "Building the Linux Kernel image and the Devicetree" above, it is still necessary to do the step regarding cross compilers.

-  Change directory to where the project is located. Clone the HDL repository if it does not exist yet in local directory.

::

   $ git clone https://github.com/analogdevicesinc/hdl.git //
   $ cd ~/Workspace/hdl/projects/adrv9371x/a10soc

-  Build the project

::

   $ make

-  After the design was built, the resulted *\*\* SRAM Object File (.sof)*\** file shall be converted to a **Raw Binary File (.rbf)**

::

   $ quartus_cpf -c --hps -o bitstream_compression=on ./adrv9371x_a10soc.sof soc_system.rbf

Building the Preloader and Bootloader Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This flow applies starting with release 2021_R1 / Quartus Pro version 20.1. For older versions of the flow see previous versions of this page.

-  Change directory to where the project is located:

::

   $ cd ~/Workspace/hdl/projects/adrv9371x/a10soc

-  create the software/bootloader folder

::

   $ mkdir -p software/bootloader

-  Clone u-boot-socfpga

::

   $ cd software/bootloader
   $ git clone https:%%//%%github.com/altera-opensource/u-boot-socfpga.git

-  Run the qts filter

::

   $ cd u-boot-socfpga
   $ git checkout rel_socfpga_v2021.07_22.02.02_pr
   $ ./arch/arm/mach-socfpga/qts-filter-a10.sh ../../../hps_isw_handoff/hps.xml arch/arm/dts/socfpga_arria10_socdk_sdmmc_handoff.h

-  Build the preloader and bootloader images

::

   make socfpga_arria10_defconfig
   make -j4

-  Create SPL images

::

   $ ln -s ../../../soc_system.core.rbf .
   $ ln -s ../../../soc_system.periph.rbf .
   $ sed -i 's/ghrd_10as066n2/soc_system/g' board/altera/arria10-socdk/fit_spl_fpga.its
   $ tools/mkimage -E -f board/altera/arria10-socdk/fit_spl_fpga.its fit_spl_fpga.itb

-  Make extlinux.conf linux configuration file - this extlinux folder shall be copied to /BOOT partition of the SD Card

::

   $ mkdir extlinux
   $ echo "    LABEL Linux Default" > extlinux/extlinux.conf
   $ echo "    KERNEL ../zImage" >> extlinux/extlinux.conf
   $ echo "    FDT ../socfpga_arria10_socdk_sdmmc.dtb" >> extlinux/extlinux.conf
   $ echo "    APPEND root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8" >> extlinux/extlinux.conf

Creating the Preloader and Bootloader partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   dragos@debian:~$ time sudo dd if=2022-07-08-ADI-Kuiper-full.img of=/dev/mmcblk0 bs=4194304
   1895+0 records in
   1895+0 records out
   7948206080 bytes (7.9 GB) copied, 503.909 s, 15.8 MB/s

   real    8m23.919s
   user    0m0.020s
   sys 0m6.376s
   dragos@debian:~$ sync
   dragos@debian:~$ sudo fdisk /dev/mmcblk0 

   Welcome to fdisk (util-linux 2.25.2).

   Command (m for help): p
   Disk /dev/mmcblk0: 14.9 GiB, 15931539456 bytes, 31116288 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0x00096174

   Device         Boot    Start      End  Sectors  Size Id Type
   /dev/mmcblk0p1          8192  1056767  1048576  2.0G c W95 FAT32 (LBA)
   /dev/mmcblk0p2       1056768 14497791 13441024  6.4G 83 Linux
   /dev/mmcblk0p3      14497792 14499839     2048    1M a2 unknown


   Command (m for help): d
   Partition number (1-3, default 3): 3

   Partition 3 has been deleted.

   Command (m for help): n
   Partition type
      p   primary (2 primary, 0 extended, 2 free)
      e   extended (container for logical partitions)
   Select (default p): p
   Partition number (3,4, default 3): 3
   First sector (2048-31116287, default 2048): 4096
   Last sector, +sectors or +size{K,M,G,T,P} (4096-8191, default 8191): +1M

   Created a new partition 3 of type 'Linux' and of size 1 MiB.

   Command (m for help): t
   Partition number (1-3, default 3): 3
   Hex code (type L to list all codes): a2

   Changed type of partition 'Linux' to 'unknown'.

   Command (m for help): p
   Disk /dev/mmcblk0: 14.9 GiB, 15931539456 bytes, 31116288 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0x00096174

   Device         Boot   Start      End  Sectors  Size Id Type
   /dev/mmcblk0p1         8192  1056767  1048576  2.0G  c W95 FAT32 (LBA)
   /dev/mmcblk0p2      1056768 14497791 13441024  6.4G 83 Linux
   /dev/mmcblk0p3         4096     6143     2048    1M a2 unknown

   Partition table entries are not in disk order.

   Command (m for help): w
   The partition table has been altered.

   The kernel still uses the old table. The new table will be used at the next reboot or after you run partprobe(8) or kpartx(8).

   dragos@debian:~$ sync
   dragos@debian:~$ time sudo dd if=uboot_w_dtb-mkpimage.bin of=/dev/mmcblk0p3
   2048+0 records in
   2048+0 records out
   1048576 bytes (1.0 MB) copied, 0.199898 s, 5.2 MB/s

   real    0m0.206s
   user    0m0.000s
   sys 0m0.004s
   dragos@debian:~$ sync

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/a10soc_adrv9371x.png
   :width: 800px

ARRADIO + Terasic SoCkit Development Kit
----------------------------------------

.. _download-links-1:

Download Links
~~~~~~~~~~~~~~

HDL Project: |:git-hdl:`projects/arradio/c5soc|`

Linux Kernel:


|https://github.com/analogdevicesinc/linux|

`ad9361.tar.gz <https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/ad9361.tar.gz>`_

.. _building-the-linux-kernel-image-and-the-devicetree-1:

Building the Linux Kernel image and the Devicetree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the kernel tree, point environment to an arm architecture cross compiler, build the configuration file, build the image, and lastly build the project and board specific device tree. See :doc:`socfpga </wiki-migration/resources/tools-software/linux-build/generic/socfpga>` for a more detailed explanation.

::

   $ git clone https:%%//%%github.com/analogdevicesinc/linux.git
   $ cd linux
   /linux$ export ARCH=arm
   /linux$ export CROSS_COMPILE=/path/to/your/arm/cross-compiler
   /linux$ make socfpga_adi_defconfig
   /linux$ make zImage -j4
   /linux$ make socfpga_cyclone5_sockit_arradio.dtb

.. _building-the-hardware-design-1:

Building the Hardware Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you skipped the instruction on "Building the Linux Kernel image and the Devicetree" above, it is still necessary to do the step regarding cross compilers.

-  Change directory to where the project is located. Clone the HDL repository if it does not exist yet in local directory.

::

   $ git clone https://github.com/analogdevicesinc/hdl.git //
   $ cd ~/Workspace/hdl/projects/arradio/c5soc

-  Build the project

::

   $ make

-  After the design was built, the resulted *\*\* SRAM Object File (.sof)*\** file shall be converted to a **Raw Binary File (.rbf)**

::

   $ quartus_cpf -c -o bitstream_compression=on ./arradio_c5soc.sof soc_system.rbf

.. _building-the-preloader-and-bootloader-image-1:

Building the Preloader and Bootloader Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This flow applies starting with release 2021_R1 / Quartus Standard version 20.1. For older versions of the flow see previous versions of this page.

-  Change directory to where the project is located

::

   $ cd ~/Workspace/hdl/projects/arradio/c5soc

-  create the software/bootloader folder

::

   $ mkdir -p software/bootloader

-  Create a new BSP settings file

::

   $ embedded_command_shell.sh bsp-create-settings --type spl --bsp-dir software/bootloader --preloader-settings-dir "hps_isw_handoff/system_bd_sys_hps" --settings software/bootloader/settings.bsp

-  Clone u-boot-socfpga

::

   $ cd software/bootloader
   $ git clone https:%%//%%github.com/altera-opensource/u-boot-socfpga.git

-  Run the qts filter

::

   $ cd u-boot-socfpga
   $ ./arch/arm/mach-socfpga/qts-filter.sh cyclone5 ../../../ ../ ./board/altera/cyclone5-socdk/qts/

-  Build the preloader and bootloader images

::

   make socfpga_cyclone5_defconfig
   make -j4

-  Make u-boot.scr file - this file shall be copied to /BOOT partition of the SD Card

::

   $ echo "load mmc 0:1 \${loadaddr} soc_system.rbf;" > u-boot.txt
   $ echo "fpga load 0 \${loadaddr} \$filesize;" >> u-boot.txt
   $ ./tools/mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "Cyclone V script" -d u-boot.txt u-boot.scr

-  Make extlinux.conf linux configuration file - this extlinux folder shall be copied to /BOOT partition of the SD Card

::

   $ mkdir extlinux
   $ echo "LABEL Linux Cyclone V Default" > extlinux/extlinux.conf
   $ echo "    KERNEL ../zImage" >> extlinux/extlinux.conf
   $ echo "    FDT ../socfpga.dtb" >> extlinux/extlinux.conf
   $ echo "    APPEND root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8" >> extlinux/extlinux.conf

Terasic SoCkit Jumper Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= ========= ========= ======== ======== ========
\       CLOCKSEL0 CLOCKSEL1 BOOTSEL0 BOOTSEL1 BOOTSEL2
======= ========= ========= ======== ======== ========
**POS** 2-3       2-3       2-3      2-3      1-2
======= ========= ========= ======== ======== ========

+--------------+


| JP2          |

+==============+

| 2.5V or 1.8V |

+--------------+

======= ===== ===== ===== ===== ===== =========
\       MSEL0 MSEL1 MSEL2 MSEL3 MSEL4 CODEC_SEL
======= ===== ===== ===== ===== ===== =========
**POS** 0     1     0     1     0     0
======= ===== ===== ===== ===== ===== =========

.. _creating-the-preloader-and-bootloader-partition-1:

Creating the Preloader and Bootloader partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   dragos@dragos-debian:~$ sudo fdisk /dev/sdb

   Command (m for help): p

   Disk /dev/sdb: 7948 MB, 7948206080 bytes
   245 heads, 62 sectors/track, 1021 cylinders, total 15523840 sectors
   Units = sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disk identifier: 0x00096174

      Device Boot      Start         End      Blocks   Id  System
   /dev/sdb1            8192      532479      262144    b  W95 FAT32
   /dev/sdb2          532480    15521791     7494656   83  Linux

   Command (m for help): n
   Partition type:
      p   primary (2 primary, 0 extended, 2 free)
      e   extended
   Select (default p): p
   Partition number (1-4, default 3): 3
   First sector (2048-15523839, default 2048): 15521792
   Last sector, +sectors or +size{K,M,G} (15521792-15523839, default 15523839): 15523839

   Command (m for help): t
   Partition number (1-4): 3
   Hex code (type L to list codes): a2
   Changed system type of partition 3 to a2 (Unknown)

   Command (m for help): p

   Disk /dev/sdb: 7948 MB, 7948206080 bytes
   245 heads, 62 sectors/track, 1021 cylinders, total 15523840 sectors
   Units = sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disk identifier: 0x00096174

      Device Boot      Start         End      Blocks   Id  System
   /dev/sdb1            8192      532479      262144    b  W95 FAT32
   /dev/sdb2          532480    15521791     7494656   83  Linux
   /dev/sdb3        15521792    15523839        1024   a2  Unknown

   Command (m for help): w
   The partition table has been altered!

   Calling ioctl() to re-read partition table.

   WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
   The kernel still uses the old table. The new table will be used at
   the next reboot or after you run partprobe(8) or kpartx(8)
   Syncing disks.

   dragos@dragos-debian:~$ sudo dd of=/dev/sdb3 bs=512 if=boot-partition.img
   949+1 records in
   949+1 records out
   486376 bytes (486 kB) copied, 1.2313 s, 395 kB/s
   dragos@dragos-debian:~$ sync

.. _iio-oscilloscope-1:

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/altera_soc.png
   :width: 800px

Building the no-OS project using DS-5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open **Eclipse for DS-5**
-  Import the existing **ad9361.tar.gz** project (**File** -> **Import** -> **General** -> **Existing Projects into Workspace**):

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/ds5_import.png
   :align: center
   :width: 300px

-  Copy all the source files and the **u-boot-spl**:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/ds5_copy_source_files.png
   :align: center
   :width: 300px

-  Build the project
-  Use the **ad9361** debug configuration for programming and debugging the project:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/ds5_debug_configuration.png
   :align: center
   :width: 300px

-  Watch on the **App Console** the printed messages:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/altera_soc/ds5_app_console.png
   :align: center
   :width: 300px

CN0540 + DE10Nano Development Kit
---------------------------------

.. _download-links-2:

Download Links
~~~~~~~~~~~~~~

HDL Project: |:git-hdl:`projects/cn0540/de10nano|`

Linux Kernel:


|https://github.com/analogdevicesinc/linux|

Cross_compiler:


|https://developer.arm.com/-/media/Files/downloads/gnu-a/10.2-2020.11/binrel/gcc-arm-10.2-2020.11-x86_64-arm-none-linux-gnueabihf.tar.xz|

SD Card Image:


|https://wiki.analog.com/resources/tools-software/linux-software/adi-kuiper_images/release_notes|

.. _building-the-linux-kernel-image-and-the-devicetree-2:

Building the Linux Kernel image and the Devicetree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the kernel tree, point environment to an arm architecture cross compiler, build the configuration file, build the image, and lastly build the project and board specific device tree. See :doc:`socfpga </wiki-migration/resources/tools-software/linux-build/generic/socfpga>` for a more detailed explanation.

::

   $ git clone https:%%//%%github.com/analogdevicesinc/linux.git
   $ cd linux
   /linux$ export ARCH=arm
   /linux$ export CROSS_COMPILE=/path/to/your/arm/cross-compiler
   /linux$ make socfpga_adi_defconfig
   /linux$ make zImage -j4
   /linux$ make socfpga_cyclone5_de10_nano_cn0540.dtb

.. _building-the-hardware-design-2:

Building the Hardware Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you skipped the instruction on "Building the Linux Kernel image and the Devicetree" above, it is still necessary to do the step regarding cross compilers.

-  Change directory to where the project is located. Clone the HDL repository if it does not exist yet in local directory.

::

   $ git clone https:%%//%%github.com/analogdevicesinc/hdl.git
   $ cd ~/Workspace/hdl/projects/cn0540/de10nano

-  Build the project

::

   $ make

-  After the design was built, the resulted *\*\* SRAM Object File (.sof)*\** file shall be converted to a **Raw Binary File (.rbf)**

::

   $ quartus_cpf -c -o bitstream_compression=on ./cn0540_de10nano.sof soc_system.rbf

.. _building-the-preloader-and-bootloader-image-2:

Building the Preloader and Bootloader Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This flow applies starting with release 2021_R1 / Quartus Standard version 20.1. For older versions of the flow see previous versions of this page.

-  Change directory to where the project is located

::

   $ cd ~/Workspace/hdl/projects/cn0540/de10nano

-  create the software/bootloader folder

::

   $ mkdir -p software/bootloader

-  Create a new BSP settings file

::

   $ embedded_command_shell.sh bsp-create-settings --type spl --bsp-dir software/bootloader --preloader-settings-dir "hps_isw_handoff/system_bd_sys_hps" --settings software/bootloader/settings.bsp

-  Clone u-boot-socfpga

::

   $ cd software/bootloader
   $ git clone https:%%//%%github.com/altera-opensource/u-boot-socfpga.git

-  Run the qts filter

::

   $ cd u-boot-socfpga
   $ git checkout socfpga_v2021.10
   $ ./arch/arm/mach-socfpga/qts-filter.sh cyclone5 ../../../ ../ ./board/altera/cyclone5-socdk/qts/

-  Make extlinux.conf linux configuration file - this extlinux folder shall be copied to /BOOT partition of the SD Card

::

   $ mkdir extlinux
   $ echo "LABEL Linux Cyclone V Default" > extlinux/extlinux.conf
   $ echo "    KERNEL ../zImage" >> extlinux/extlinux.conf
   $ echo "    FDT ../socfpga.dtb" >> extlinux/extlinux.conf
   $ echo "    APPEND root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8" >> extlinux/extlinux.conf

-  Build the preloader and bootloader images

::

   make socfpga_cyclone5_defconfig
   make -j4

-  Make u-boot.scr file - this file shall be copied to /BOOT partition of the SD Card

::

   $ echo "load mmc 0:1 \${loadaddr} soc_system.rbf;" > u-boot.txt
   $ echo "fpga load 0 \${loadaddr} \$filesize;" >> u-boot.txt
   $ ./tools/mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "Cyclone V script" -d u-boot.txt u-boot.scr

Creating the Micro-SD Card
--------------------------

.. tip::

   \ :doc:`Create SD Image for DE10Nano SoCkit board. (it is a single image for all boards). </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`\


::

   user@debian:~$ time sudo dd if=2023-12-13-ADI-Kuiper-full.img of=/dev/sdd bs=4194304
   2952+0 records in
   2952+0 records out
   12381585408 bytes (12 GB, 12 GiB) copied, 838.353 s, 14.8 MB/s

   real    14m7.938s
   user    0m0.006s
   sys 0m0.009s
   user@debian:~$ sync
   user@debian:~$ lsblk

   NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   sdd           8:48   1  29.1G  0 disk 
   ├─sdd1        8:49   1     2G  0 part 
   ├─sdd2        8:50   1  27.1G  0 part 
   └─sdd3        8:51   1     8M  0 part 

Configuring the Micro-SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::


   user@debian:~$ sudo mount /dev/sdd1 /media/data/BOOT/
   user@debian:~$ lsblk

   NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   sdd           8:48   1  29.1G  0 disk 
   ├─sdd1        8:49   1     2G  0 part /media/data/BOOT
   ├─sdd2        8:50   1  27.1G  0 part 
   └─sdd3        8:51   1     8M  0 part 


   user@debian:~/Workspace/hdl/projects/cn0540/de10nano$ sudo cp soc_system.rbf /media/data/BOOT/
   user@debian:~/Workspace/hdl/projects/cn0540/de10nano/software/bootloader/u-boot-socfpga$ sudo cp u-boot.scr /media/data/BOOT/
   user@debian:~/Workspace/linux/arch/arm/boot/dts$ sudo cp socfpga_cyclone5_de10_nano_cn0540.dtb /media/data/BOOT/socfpga.dtb
   user@debian:~/Workspace/linux/arch/arm/boot$ sudo cp zImage /media/data/BOOT
   user@debian:/media/data/BOOT$ sudo mkdir extlinux
   user@debian:~/Workspace/hdl/projects/cn0540/de10nano/software/bootloader/u-boot-socfpga/extlinux$ sudo cp extlinux.conf /media/data/BOOT/extlinux/
   user@debian:~/Workspace/hdl/projects/cn0540/de10nano/software/bootloader/u-boot-socfpga$ sudo dd if=u-boot-with-spl.sfp of=/dev/sdd3

   1697+1 records in
   1697+1 records out
   868996 bytes (869 kB, 849 KiB) copied, 0.21262 s, 4.1 MB/s

   user@debian:~$ sudo umount /dev/sdd1
   user@debian:~$ lsblk 
    
   NAME        MAJ:MIN RM  SIZE  RO TYPE MOUNTPOINT
   sdd           8:48  1   29.1G  0 disk 
   ├─sdd1        8:49  1      2G  0 part 
   ├─sdd2        8:50  1   27.1G  0 part 
   └─sdd3        8:51  1      8M  0 part 

The root of 'BOOT' should contain:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   *''socfpga.dtb file''
   *''zImage file''
   *''extlinux.conf''
   *''u-boot.scr file''
   *''soc_system.rbf file''

The root of preloader partition should contain:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   *''u-boot-with-spl.sfp file''

Setting up the hardware (DE10-Nano)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to:

-  Get the `DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_.


|zedboard.png|

-  Insert the Micro-SD into the Micro-SD Interface Connector (J11).
   \* Connect the CN0540-ARDZ to the DE10Nano FPGA using the Arduino shield connection.
   \* Connect USB UART J4 (USB Mini B) to your host PC.
   \* Plug your ethernet cable into the RJ45 ethernet connector(J10).
   \* Plug the Power Supply into 5V Power input connector (J14) (DO NOT turn the device on).
   \* Set the jumpers as seen in the below picture:

   |image1|

   \* Turn it on.
   \* Wait ~30 seconds for the “DONE” LED to turn blue.


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


.. _iio-oscilloscope-2:

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/playground/cn0540_de10nano_waveforms_.png

.. |:git-hdl:`projects/adrv9371x/a10soc|` image:: :git-hdl:`projects/adrv9371x/a10soc`
.. |https://github.com/analogdevicesinc/linux| image:: https://github.com/analogdevicesinc/linux
.. |:git-hdl:`projects/arradio/c5soc|` image:: :git-hdl:`projects/arradio/c5soc`
.. |:git-hdl:`projects/cn0540/de10nano|` image:: :git-hdl:`projects/cn0540/de10nano`
.. |https://developer.arm.com/-/media/Files/downloads/gnu-a/10.2-2020.11/binrel/gcc-arm-10.2-2020.11-x86_64-arm-none-linux-gnueabihf.tar.xz| image:: https://developer.arm.com/-/media/Files/downloads/gnu-a/10.2-2020.11/binrel/gcc-arm-10.2-2020.11-x86_64-arm-none-linux-gnueabihf.tar.xz
.. |https://wiki.analog.com/resources/tools-software/linux-software/adi-kuiper_images/release_notes| image:: https://wiki.analog.com/_media/:doc:`/wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes`
.. |zedboard.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/AD777x-ARDZ/zedboard.png
   :width: 600px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/de10-nano_fpga_switch_matrix.png
   :width: 800px
