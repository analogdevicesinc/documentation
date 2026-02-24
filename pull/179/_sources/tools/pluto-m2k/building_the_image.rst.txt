.. _pluto-m2k building_the_image:

Building the Firmware Image
"""""""""""""""""""""""""""

It is recommenced to use the pre-build images, which can be
found at :git-plutosdr-fw:`PlutoSDR Firmware releases <releases/latest+>`.
found at :git-m2k-fw:`M2k Firmware releases <releases/latest+>`.
These are build and tested by Analog Devices, and should work on your PlutoSDR
without issues.

If you want to change functionality, you will need to follow
these instructions. To test your image, it is recommended to use the
:ref:`RAM Boot <pluto-m2k reboot dfu-ram>` rather than
writing to flash the first time. This keep the default firmware while you are
testing your image, so if something goes wrong - its a quick power cycle to fix
things.

Prerequisites
=============

#. Make sure to download, or upgrade your
   :ref:`Sources <pluto-m2k obtaining_the_sources>`

   -  Make sure you have the recommended/required Vivado versions. It's likely
      listed in the *archive* section of the Xilinx web site. To check out what
      you need, look at the following tcl file (which was checked out in the
      sources link above).

      .. shell::

         ~/github/temp/plutosdr-fw
         $grep -i REQUIRED_VIVADO_VERSION $(find ./ -name "adi*.tcl") | grep set
          set required_vivado_version "2021.1"

#. You need :xilinx:`Xilinx Vivado Design Suite <support/download.html>` to
   compile the Verilog into the FPGA bit file.
#. You need :xilinx:`Xilinx Vivado Vitis <support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`
   to compile C code for the ARM inside the AMD Zynq.

   -  If you are using very old versions of Xilinx tools, you need to make sure
      that you have the 32-bit libraries (the Xilinx tools are distributed as
      32-bit binaries).

.. shell::

   ~/github/temp/plutosdr-fw
   $find /opt/Xilinx/ -name vivado -executable -type f | xargs file | grep ELF
    /opt/Xilinx/Vivado/2021.2/bin/unwrapped/lnx64.o/vivado: ELF 64-bit LSB executable,
    x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
    for GNU/Linux 2.6.18, not stripped

If it reports as a 32-bit binary (which the above did not), and you are running
on a 64-bit system, do:

.. shell::

   ~/devel
   $dpkg --add-architecture i386
   $apt-get update
   $sudo apt-get install libc6:i386 libstdc++6:i386

There are a few other tools that are necessary in order to build your own
Firmware Image.

.. shell::

   ~/devel
   $sudo apt-get install git build-essential ccache device-tree-compiler \
   $    dfu-util fakeroot help2man libncurses5-dev libssl1.0-dev mtools rsync \
   $    u-boot-tools bc python cpio zip unzip file wget

Building
========

.. hint::

   It is recommended that if you are building in a Virtual Machine
   (which is totally fine), the Base Memory be set to at least 4096 MBytes. The
   AMD Xilinx :xilinx:`Vivado <products/design-tools/vivado/memory.html>` tools
   require at least 1.6 Gig of memory when compile for the ``XC7Z010``. It has been
   reported that 2048 Mbytes is not enough, and will cause the tools to hang.

Starting the build process is just a matter of typing ``make`` within the
firmware repository. The Makefile requires a few environmental variables being
set, and of course the ARM GCC toolchain in the PATH. Some paths maybe adjusted
to match your Xilinx Vivado and Vitis install folders.

.. shell::

   ~/devel
   $cd plutosdr-fw # or m2k-fw
   $export CROSS_COMPILE=arm-linux-gnueabihf-
   $export PATH=$PATH:/opt/Xilinx/Vitis/2021.2/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin
   $export VIVADO_SETTINGS=/opt/Xilinx/Vivado/2021.2/settings64.sh
   $make

The initial build takes some time to complete, and also requires an INTERNET
connection, since `buildroot <https://buildroot.org/>`__ downloads the source
packages from the WEB.

.. hint::

   Depending on your distribution, you may need to force Vivado to use
   Gtk2. You can do that by adding:

   .. shell::

      ~/devel/plutosdr-fw
      $export SWT_GTK3=0

before you type ``make``.

Build Artifacts
---------------

.. shell::

         ~/devel/plutosdr-fw
         $ls -AGhl build
          total 52M
          -rw-rw-r-- 1 michael   69 Apr 19 17:45 boot.bif
          -rw-rw-r-- 1 michael 446K Apr 19 17:45 boot.bin
          -rw-rw-r-- 1 michael 446K Apr 19 17:45 boot.dfu
          -rw-rw-r-- 1 michael 575K Apr 19 17:45 boot.frm
          -rw-rw-r-- 1 michael 8,3M Apr 19 17:45 pluto.dfu
          -rw-rw-r-- 1 michael 8,3M Apr 19 17:45 pluto.frm
          -rw-rw-r-- 1 michael   33 Apr 19 17:45 pluto.frm.md5
          -rw-rw-r-- 1 michael 8,3M Apr 19 17:45 pluto.itb
          -rw-rw-r-- 1 michael  16M Apr 19 17:45 plutosdr-fw-v0.20.zip
          -rw-rw-r-- 1 michael 471K Apr 19 17:45 plutosdr-jtag-bootstrap-v0.20.zip
          -rw-r--r-- 1 michael 4,2M Apr 19 17:39 rootfs.cpio.gz
          drwxrwxr-x 6 michael 4,0K Apr 19 17:45 sdk
          -rw-rw-r-- 1 michael 940K Apr 19 17:45 system_top.bit
          -rw-rw-r-- 1 michael 362K Apr 19 17:45 system_top.hdf
          -rwxrwxr-x 1 michael 409K Apr 19 17:45 u-boot.elf
          -rw-rw---- 1 michael 128K Apr 19 17:45 uboot-env.bin
          -rw-rw---- 1 michael 129K Apr 19 17:45 uboot-env.dfu
          -rw-rw-r-- 1 michael 4,6K Apr 19 17:45 uboot-env.txt
          -rwxrwxr-x 1 michael 3,2M Apr 19 17:33 zImage
          -rw-rw-r-- 1 michael  16K Apr 19 17:39 zynq-pluto-sdr.dtb
          -rw-rw-r-- 1 michael  16K Apr 19 17:39 zynq-pluto-sdr-revb.dtb

Testing on the target
---------------------

There is a script in the :git-plutosdr_scripts:`plutosdr_scripts <+>` repo
that will quickly download a build artifact (the ``pluto.dfu`` file) to an USB
attached PlutoSDR. This will load the image into RAM, and not write to flash,
enabling easy testing of images. However, since it is loading into RAM, it is
not a persistent update over power cycles or further reboots.

.. shell::

   ~/github/plutosdr-fw
   $sudo ../plutosdr_scripts/pluto_ramboot
    Found Pluto SDR at IP 192.168.3.1, running kernel:
        Linux pluto 5.4.0-00535-g9c04de11ae53 #1 SMP PREEMPT Fri Aug 20 13:01:03 CEST 2021 armv7l GNU/Linux
    Found Pluto SDR in dfu mode and downloading ./build/pluto.dfu
    successfully downloaded
    Found new PlutoSDR at 192.168.3.1, running kernel:
        Linux pluto 5.4.0-00535-g9c04de11ae53 #1 SMP PREEMPT Tue Feb 15 16:17:50 EST 2022 armv7l GNU/Linux

Main targets
------------

.. list-table::
   :header-rows: 1

   - - File
     - Comment
   - - pluto.frm
     - Main PlutoSDR firmware file used with the USB Mass Storage Device
   - - pluto.dfu
     - Main PlutoSDR firmware file used in DFU mode
   - - boot.frm
     - First and Second Stage Bootloader (u-boot + fsbl + uEnv) used with the
       USB Mass Storage Device
   - - boot.dfu
     - First and Second Stage Bootloader (u-boot + fsbl) used in DFU mode
   - - uboot-env.dfu
     - u-boot default environment used in DFU mode
   - - plutosdr-fw-vX.XX.zip
     - ZIP archive containg all of the files above
   - - plutosdr-jtag-bootstrap-vX.XX.zip
     - ZIP archive containg u-boot and Vivao TCL used for JATG bootstrapping

Other intermediate targets
--------------------------

.. list-table::
   :header-rows: 1

   - - File
     - Comment
   - - boot.bif
     - Boot Image Format file used to generate the Boot Image
   - - boot.bin
     - Final Boot Image
   - - pluto.frm.md5
     - md5sum of the pluto.frm file
   - - pluto.itb
     - u-boot Flattened Image Tree
   - - rootfs.cpio.gz
     - The Root Filesystem archive
   - - sdk
     - Vivado/XSDK Build folder including the FSBL
   - - system_top.bit
     - FPGA Bitstream (from HDF)
   - - system_top.hdf
     - FPGA Hardware Description File exported by Vivado
   - - u-boot.elf
     - u-boot ELF Binary
   - - uboot-env.bin
     - u-boot default environment in binary format created form uboot-env.txt
   - - uboot-env.txt
     - u-boot default environment in human readable text format
   - - zImage
     - Compressed Linux Kernel Image
   - - zynq-pluto-sdr.dtb
     - Device Tree Blob for Rev.A
   - - zynq-pluto-sdr-revb.dtb
     - Device Tree Blob for Rev.B

How does it work
----------------

.. warning::

   All these steps are automatically handled by make. They are just
   explained here, for those who are interested.

Build Linux kernel
------------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - PlutoSDR Linux Kernel Config
     - :git-linux:`zynq_pluto_defconfig <arch/arm/configs/zynq_pluto_defconfig>`

.. shell::
   :no-path:

   $make -C linux ARCH=arm zynq_pluto_defconfig
   $make -C linux -j 8 \
   $    UIMAGE_LOADADDR=0x8000 \
   $    ARCH=arm CROSS_COMPILE=arm-xilinx-linux-gnueabi- \
   $    zImage
   $cp linux/arch/arm/boot/zImage build/zImage

Making custom kernel changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attention::

   Normal users should not need to change their kernel, and this is
   only described for advanced users, or developers who periodically forget things

The command

.. shell::
   :no-path:

   $make -C linux ARCH=arm zynq_pluto_defconfig

copies the file from ``arch/arm/configs/zynq_pluto_defconfig`` to ``.config``
and

.. shell::
   :no-path:

   $make -C linux -j 8 \
   $    ARCH=arm \
   $    CROSS_COMPILE=arm-xilinx-linux-gnueabi- \
   $    UIMAGE_LOADADDR=0x8000 \
   $    zImage

builds it.

If you want to make a custom kernel, the easiest thing to do, is modify the
``.config`` with

.. shell::
   :no-path:

   $make -C linux ARCH=arm zynq_pluto_defconfig
   $make -C linux ARCH=arm menuconfig

and then make changes, save them, and then create the ``defconfig``.

.. shell::
   :no-path:

   $make -C linux ARCH=arm savedefconfig

Check your changes against the default image

.. shell::
   :no-path:

   $diff -u ./linux/arch/arm/configs/zynq_pluto_defconfig linux/defconfig | less

And if you are sure things are what you want, store them to the default file.

.. shell::
   :no-path:

   $cp ./linux/defconfig ./linux/arch/arm/configs/zynq_pluto_defconfig

then this will work next time you type ``make`` to build the firmware image.

Build Devicetrees
-----------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - PlutoSDR Rev.A Device Tree
     - :git-linux:`zynq-pluto-sdr.dts <arch/arm/boot/dts/xilinx/zynq-pluto-sdr.dts>`
   - - PlutoSDR Rev.B Device Tree
     - :git-linux:`zynq-pluto-sdr-revb.dts <arch/arm/boot/dts/xilinx/zynq-pluto-sdr-revb.dts>`

.. shell::
   :no-path:

   $make -C linux -j 8 ARCH=arm CROSS_COMPILE=arm-xilinx-linux-gnueabi- zynq-pluto-sdr.dtb
   $cp linux/arch/arm/boot/dts/zynq-pluto-sdr.dtb build/zynq-pluto-sdr.dtb
   $make -C linux -j 8 ARCH=arm CROSS_COMPILE=arm-xilinx-linux-gnueabi- zynq-pluto-sdr-revb.dtb
   $cp linux/arch/arm/boot/dts/zynq-pluto-sdr-revb.dtb build/zynq-pluto-sdr-revb.dtb

Build Buildroot User Space
--------------------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - PlutoSDR Buildroot Config
     - :git-buildroot:`zynq_pluto_defconfig <master:configs/zynq_pluto_defconfig>`

.. shell::
   :no-path:

   $make -C buildroot ARCH=arm zynq_pluto_defconfig
   $make -C buildroot TOOLCHAIN_EXTERNAL_INSTALL_DIR= \
   $    ARCH=arm CROSS_COMPILE=arm-xilinx-linux-gnueabi- \
   $    BUSYBOX_CONFIG_FILE=/home/michael/devel/pluto/plutosdr-fw/buildroot/board/pluto/busybox-1.25.0.config all
   $cp buildroot/output/images/rootfs.cpio.gz build/rootfs.cpio.gz

Configuring Buildroot
~~~~~~~~~~~~~~~~~~~~~

You need to copy over the correct file, to the ``.config``, edit it (with
``menuconfig``), and then save it to the right place so that the main build
system will use the new file.

.. shell::
   :no-path:

   $make -C buildroot ARCH=arm zynq_pluto_defconfig
   $make -C buildroot ARCH=arm menuconfig
   $make -C buildroot ARCH=arm savedefconfig
   $make

Build FPGA Hardware Description File
------------------------------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - Pluto HDL Project
     - :git-hdl:`Files <projects/pluto>`

.. shell::
   :no-path:

   $source /opt/Xilinx/Vivado/2021.2/settings64.sh
   $make -C hdl/projects/pluto
   $cp hdl/projects/pluto/pluto.sdk/system_top.hdf build/system_top.hdf

Build FPGA First Stage Bootloader (FSBL)
----------------------------------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - Create FSBL TCL script
     - :git-plutosdr-fw:`create_fsbl_project.tcl <master:scripts/create_fsbl_project.tcl>`

.. shell::
   :no-path:

   $source /opt/Xilinx/Vivado/2021.2/settings64.sh
   $xsdk -batch -source scripts/create_fsbl_project.tcl
   $cp build/sdk/hw_0/system_top.bit build/system_top.bit

Build multi component FIT image (Flattened Image Tree)
------------------------------------------------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - PlutoSDR Image Tree Source
     - :git-plutosdr-fw:`pluto.its <master:scripts/pluto.its>`

.. shell::
   :no-path:

   $u-boot-xlnx/tools/mkimage -f scripts/pluto.its build/pluto.itb

Build Firmware DFU image
------------------------

.. shell::
   :no-path:

   $cp build/pluto.itb build/pluto.itb.tmp
   $dfu-suffix -a build/pluto.itb.tmp -v 0x0456 -p 0xb673
   $mv build/pluto.itb.tmp build/pluto.dfu

Build Firmware FRM image
------------------------

.. shell::
   :no-path:

   $md5sum build/pluto.itb | cut -d ' ' -f 1 > build/pluto.frm.md5
   $cat build/pluto.itb build/pluto.frm.md5 > build/pluto.frm

Build u-boot
------------

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - PlutoSDR u-boot Config
     - :git-u-boot-xlnx:`zynq_pluto_defconfig <pluto:configs/zynq_pluto_defconfig>`
   - - PlutoSDR u-boot Device Tree
     - :git-u-boot-xlnx:`zynq-pluto-sdr.dts <pluto:arch/arm/dts/zynq-pluto-sdr.dts>`

.. shell::
   :no-path:

   $make -C u-boot-xlnx ARCH=arm zynq_pluto_defconfig
   $make -C u-boot-xlnx ARCH=arm CROSS_COMPILE=arm-xilinx-linux-gnueabi- UBOOTVERSION="PlutoSDR v0.20-PlutoSDR"
   $cp u-boot-xlnx/u-boot build/u-boot.elf

Build Zynq Boot Image
---------------------

.. shell::
   :no-path:

   $echo img:{[bootloader] build/sdk/fsbl/Release/fsbl.elf build/u-boot.elf } > build/boot.bif
   $source /opt/Xilinx/Vivado/2021.2/settings64.sh
   $bootgen -image build/boot.bif -w -o build/boot.bin

Build Boot DFU Image
--------------------

.. shell::
   :no-path:

   $cp build/boot.bin build/boot.bin.tmp
   $dfu-suffix -a build/boot.bin.tmp -v 0x0456 -p 0xb673
   $mv build/boot.bin.tmp build/boot.dfu

Build u-boot default environment Image
--------------------------------------

.. shell::
   :no-path:

   $CROSS_COMPILE=arm-xilinx-linux-gnueabi- scripts/get_default_envs.sh > build/uboot-env.txt
   $u-boot-xlnx/tools/mkenvimage -s 0x20000 -o build/uboot-env.bin build/uboot-env.txt

Build u-boot default environment DFU Image
------------------------------------------

.. shell::
   :no-path:

   $cp build/uboot-env.bin build/uboot-env.bin.tmp
   $dfu-suffix -a build/uboot-env.bin.tmp -v 0x0456 -p 0xb673
   $mv build/uboot-env.bin.tmp build/uboot-env.dfu

Build Boot FRM image
--------------------

.. shell::
   :no-path:

   $cat build/boot.bin build/uboot-env.bin scripts/target_mtd_info.key | \
   $    tee build/boot.frm | md5sum | cut -d ' ' -f1 | tee -a build/boot.frm
