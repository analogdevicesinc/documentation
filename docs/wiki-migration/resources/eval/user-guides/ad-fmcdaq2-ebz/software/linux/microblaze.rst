AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ on Microblaze
===========================================

Linux on the Xilinx FPGA development Board
==========================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/linux/kernel/microblaze.html


.. note::

   This content is purely informational, and the best place for questions about this content is normally `Xilinx <https://forums.xilinx.com/t5/Embedded-Linux/bd-p/ELINUX>`_, or a friendly consultant (who you will pay), or `trainer <https://training.linuxfoundation.org/training/embedded-linux-development/>`_. These instructions work for us. That does not mean they are complete, accurate, or supported.


20

This guide provides some step-by-step instructions on how to build a Microblaze Linux Kernel image for the FMC board connected to an

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `VC707 <https://www.xilinx.com/VC707>`_
-  `VCU118 <https://www.xilinx.com/VCU118>`_
-  `VCU128 <https://www.xilinx.com/VCU128>`_

Required Software
-----------------

-  `Linux Kernel Source <http://github.com/analogdevicesinc/linux>`_
-  `rootfs.cpio.gz <https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz>`_
-  `Xilinx Vivado Design Suite (Microblaze GNU Tools) <https://www.xilinx.com/products/design-tools/vivado.html>`_
-  `Microblaze GNU Toolchain <http://xilinx.wikidot.com/mb-gnu-tools>`_ (See note below)

Microblaze gnu toolchain from Xilinx is no longer available on git. Please use gnu tools from Vitis installation as below:

| ~/linux$ export PATH=/opt/Xilinx/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin/::math:`PATH\\ ~/linux` export ARCH=microblaze
| ~/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-

.. tip::

   Latest released files can be downloaded from :doc:`here </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>`


Build Linux - Step by Step instructions
---------------------------------------

Get Microblaze Little Endian Toolchain from Xilinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the Vivado Vitis from here `Download <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_ And make sure you followed the instructions for `Microblaze GNU Toolchain <http://xilinx.wikidot.com/mb-gnu-tools>`_

Get Linux kernel source
~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   
      $ git clone https://github.com/analogdevicesinc/linux.git
      Cloning into 'linux'...
      remote: Counting objects: 2757163, done.
      remote: Compressing objects: 100% (495484/495484), done.
      remote: Total 2757163 (delta 2296596), reused 2687337 (delta 2234506)
      Receiving objects: 100% (2757163/2757163), 782.04 MiB

      | 1.39 MiB/s, done.
      Resolving deltas: 100% (2296596/2296596), done.
   


Checkout main branch
~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   
      $ cd linux/
      ~/linux$ git checkout main
      Checking out files: 100% (16412/16412), done.
      Branch main set up to track remote branch main from origin.
      Switched to a new branch 'main'
   


Set Environmental Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   
      ~/linux$ source /opt/Xilinx/Vivado/2023.2/settings64.sh
      ~/linux$ export ARCH=microblaze
      ~/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-
   


|

.. tip::

   Instead of sourcing the Vivado settings64.sh script you can alternatively add your microblaze gcc toolchain directly to your PATH variable:

   | ``~/linux$ export PATH=/opt/Xilinx/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin/:$PATH``


Configure Kernel
~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   
      ~/linux$ make adi_mb_defconfig
      #
      # configuration written to .config
      #
   


Get Root File-System
~~~~~~~~~~~~~~~~~~~~

The root file system or rootfs contains everything (besides the Linux kernel itself) needed to support a full Linux system. It contains all the (user) applications, configurations, services, data, etc. Without the rootfs your Linux system cannot run. You can either just download the pre-build image or build it yourself. Instructions can be found here: :doc:`Building with buildroot </wiki-migration/resources/tools-software/linux-build/generic/buildroot>`

`rootfs.cpio.gz <https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz>`_

.. tip::

   rootfs.cpio.gz must be placed in the root of your kernel tree. (~/linux/rootfs.cpio.gz)


.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      ~/linux$ wget https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
      --2022-01-18 09:52:08--  https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
      Resolving swdownloads.analog.com (swdownloads.analog.com)... 23.63.205.142
      Connecting to swdownloads.analog.com (swdownloads.analog.com)|23.63.205.142|:443... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 6772207 (6,5M) [application/x-gzip]
      Saving to: ‘rootfs.cpio.gz’
   
      rootfs.cpio.gz                                     100%[===============================================================================================================>]   6,46M  3,32MB/s    in 1,9s    
   
      2022-01-18 09:52:12 (3,32 MB/s) - ‘rootfs.cpio.gz’ saved [6772207/6772207]
   


Build kernel
~~~~~~~~~~~~

The result of building the kernel is an elf file in arch/microblaze/boot named simpleImage.<dts file name> based on the dts specified.

The build process for the kernel searches in the arch/microblaze/boot/dts directory for a specified device tree file and then builds the device tree into the kernel image.

The following command shows the general format for the build target name. Note that the <dts file name> does not include the file extension ".dts".

::

   ~/linux$ make simpleImage.<dts file name>

To see what device-trees for the different FPGA carrier and FMC module combination exist type:

::

   ~/linux$ ls -l arch/microblaze/boot/dts

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      ~/linux$ make -j4 simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
        SYNC    include/config/auto.conf.cmd
        CC      scripts/mod/empty.o
        CC      scripts/mod/devicetable-offsets.s
        MKELF   scripts/mod/elfconfig.h
        HOSTCC  scripts/mod/modpost.o
        HOSTCC  scripts/mod/sumversion.o
        HOSTCC  scripts/mod/file2alias.o
   
      [ --snip-- ]
   
        AR      init/built-in.a
        LD      vmlinux.o
        MODPOST vmlinux.symvers
        MODINFO modules.builtin.modinfo
        GEN     modules.builtin
        LD      .tmp_vmlinux.kallsyms1
        KSYMS   .tmp_vmlinux.kallsyms1.S
        AS      .tmp_vmlinux.kallsyms1.S
        LD      .tmp_vmlinux.kallsyms2
        KSYMS   .tmp_vmlinux.kallsyms2.S
        AS      .tmp_vmlinux.kallsyms2.S
        LD      vmlinux
        SORTTAB vmlinux
        SYSMAP  System.map
        OBJCOPY arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
        SHIPPED arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.unstrip
        STRIP   vmlinux arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.strip
        UIMAGE  arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.ub
      Image Name:   Linux-5.10.0-97916-g513446e488c3
      Created:      Tue Jan 18 12:07:35 2022
      Image Type:   MicroBlaze Linux Kernel Image (uncompressed)
      Data Size:    18398124 Bytes = 17966.92 KiB = 17.55 MiB
      Load Address: 80000000
      Entry Point:  80000000
      Kernel: arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1 is ready  (#3678)
   


.. tip::

   The STRIP image found under arch/microblaze/boot/ is the ELF image which can be loaded via the debugger


Boot Kernel on FPGA Microblaze
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then one method to load the kernel onto the already built and running FPGA which has the Microblaze processor is to launch XMD or XSDB from the Xilinx Vivado toolset from within .../linux/arch/microblaze/boot and run from the XMD or XSDB shell:

.. important::

   XMD has been deprecated and will be removed in the future. XSDB/XSCT replaces XMD and provides additional functionality. Xilinx recommends you switch to XSDB for command line debugging. You can find more information about these tools in the `Embedded System Tools Reference Manual <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2017_4/ug1043-embedded-system-tools.pdf>`_ (UG1043)


For XMD:

::

   xmd> fpga -f system_top.bit
   xmd> connect mb mdm
   xmd> dow simpleImage.vc707_fmcomms2-3
   xmd> run

For XSDB or XSCT:

::

   xsdb> connect
   xsdb> fpga -f system_top.bit
   xsdb> targets
     1  xcku040
        2  MicroBlaze Debug Module at USER2
           3  MicroBlaze #0 (Running)
   xsdb> targets 3
   xsdb> dow simpleImage.kcu105_fmcdaq2
   xsdb> con

Configure and loading using a TCL script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example TCL script:

.. code:: c

   run.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.tcl
   connect
   fpga -f system_top.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc.bit
   after 1000
   target 3
   dow simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.strip
   after 1000
   con
   disconnect

From XSDB or XSCT:

::

   xsdb> source run.tcl

(more details, methods of how to get bit file and kernel on flash and/or boot off SD Card is appreciated)


.. include:: ../../quickstart/microblaze.rst
