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

~/linux$ export PATH=/opt/Xilinx/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin/::math:`PATH ~/linux` export ARCH=microblaze ~/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-

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

   This specifies any shell prompt running on the development host

   
   ::
   
      $ git clone :git-linux:`linux`
      Cloning into 'linux'...
      remote: Counting objects: 2757163, done.
      remote: Compressing objects: 100% (495484/495484), done.
      remote: Total 2757163 (delta 2296596), reused 2687337 (delta 2234506)
      Receiving objects: 100% (2757163/2757163), 782.04 MiB | 1.39 MiB/s, done.
      Resolving deltas: 100% (2296596/2296596), done.
   


Checkout main branch
~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

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

   This specifies any shell prompt running on the development host

   
   ::
   
      ~/linux$ source /opt/Xilinx/Vivado/2023.2/settings64.sh
      ~/linux$ export ARCH=microblaze
      ~/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-
   


.. tip::

   Instead of sourcing the Vivado settings64.sh script you can alternatively add your microblaze gcc toolchain directly to your PATH variable:

   
   ::
   
      ~/linux$ export PATH=/opt/Xilinx/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin/:$PATH
   


Configure Kernel
~~~~~~~~~~~~~~~~

.. container:: box bgblue

   This specifies any shell prompt running on the development host

   
   ::
   
      ~/linux$ make adi_mb_defconfig
      #
      # configuration written to .config
      #
   


Get Root File-System
~~~~~~~~~~~~~~~~~~~~

The root file system or rootfs contains everything (besides the Linux kernel itself) needed to support a full Linux system. It contains all the (user) applications, configurations, services, data, etc. Without the rootfs your Linux system cannot run. You can either just download the pre-build image or build it yourself. Instructions can be found here: :doc:`Building with buildroot </wiki-migration/resources/tools-software/linux-build/generic/buildroot>`

`rootfs.cpio.gz <https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz>`_ rootfs.cpio.gz must be placed in the root of your kernel tree. (~/linux/rootfs.cpio.gz)

.. container:: box bgblue

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




AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ Microblaze Quick Start Guide
==========================================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ on:

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `VC707 <https://www.xilinx.com/VC707>`_

Required Software
-----------------

-  Bitfile and Linux ELF image.
-  Xilinx ISE Microprocessor Debugger (XMD) is sufficient for the demo.
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  Xilinx KC705 or KCU105 or VC707
-  AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ FMC Board.
-  Micro / Mini-USB Cable

Testing
=======

-  Connect the AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ FMC board to the FPGA carrier, on the HPC FMC connector.
-  Connect USB JTAG (Micro USB) to your host PC.
-  Turn on the power switch on the FPGA board.
-  Open XMD console to configure the FPGA and download the elf image.

Loading
-------

Download the pre-build image for you device in question.

.. note::

   **Latest Build: 2024-03-26 - 2023_R2**

   
   | Linux branch: 2023_R2
   | Linux repository: :git-linux:`linux`
   | HDL branch: hdl_2023_r2
   | HDL repository: :git-hdl:`hdl`



+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FPGA Carrier | FMC Card   | Download                                                                                                                                                                           |
+==============+============+====================================================================================================================================================================================+
| KC705        | AD9467_FMC | `2023_r2_kc705_ad9467_fmc.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kc705_ad9467_fmc.zip>`_                                                                        |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2023_r2_kc705_fmcomms2-3.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kc705_fmcomms2-3.zip>`_                                                                        |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS4   | `2023_r2_kc705_fmcomms4.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kc705_fmcomms4.zip>`_                                                                            |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCDAQ2    | `2023_r2_kc705_fmcdaq2.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kc705_fmcdaq2.zip>`_                                                                              |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | ADRV9371X  | `2023_r2_kcu105_adrv9371x.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kcu105_adrv9371x.zip>`_                                                                        |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2023_r2_kcu105_fmcomms2-3.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kcu105_fmcomms2-3.zip>`_                                                                      |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | DAQ2       | `2023_r2_kcu105_daq2.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/kcu105_fmcdaq2.zip>`_                                                                               |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VC707        | AD6676EVB  | `2023_r2_vc707_ad6676evb.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vc707_ad6676evb.zip>`_                                                                          |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2023_r2_vc707_fmcomms2-3.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vc707_fmcomms2-3.zip>`_                                                                        |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS4   | `2023_r2_vc707_fmcomms4.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vc707_fmcomms4.zip>`_                                                                            |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | AD9081     | `2023_r2_vcu118_ad9081_m4_l8.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9081.zip>`_                                                                        |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2023_r2_vcu118_ad9081_m8_l4.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9081_m8_l4.zip>`_                                                                  |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2023_r2_vcu118_ad9081_204c_txmode_10_rxmode_11.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9081_204c_txmode_10_rxmode_11.zip>`_                            |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2023_r2_vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.zip>`_  |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2023_r2_vcu118_ad9081_204c_txmode_23_rxmode_25.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9081_204c_txmode_23_rxmode_25.zip>`_                            |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2023_r2_vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.zip>`_  |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2023_r2_vcu118_ad9081_204c_txmode_11_rxmode_4_revc.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.zip>`_               |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCDAQ3    | `2023_r2_vcu118_daq3.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_fmcdaq3.zip>`_                                                                               |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | AD9082     | `2023_r2_vcu118_ad9082.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_ad9082.zip>`_                                                                              |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | ADRV9025   | `2023_r2_vcu118_adrv9025.zip <http://swdownloads.analog.com/cse/microblaze/2023_r2/vcu118_adrv99025.zip>`_                                                                         |
+--------------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   **Latest Build: 2023-12-08 - 2022_R2**

   
   | Linux branch: 2022_R2
   | Linux repository: :git-linux:`linux`
   | HDL branch: hdl_2022_r2
   | HDL repository: :git-hdl:`hdl`



+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FPGA Carrier | FMC Card   | Download                                                                                                                                                                            |
+==============+============+=====================================================================================================================================================================================+
| KC705        | AD9467_FMC | `2022_r2_kc705_ad9467_fmc.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/kc705_ad9467_fmc.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2022_r2_kc705_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/kc705_fmcomms2-3.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | ADRV9371X  | `2022_r2_kcu105_adrv9371x.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/kcu105_adrv9371x.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2022_r2_kcu105_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/kcu105_fmcomms2-3.zip>`_                                                                      |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | DAQ2       | `2022_r2_kcu105_daq2.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/kcu105_fmcdaq2.zip>`_                                                                               |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | DAQ3       | `2022_r2_kcu105_daq3.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/kcu105_fmcdaq3.zip>`_                                                                               |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VC707        | AD6676EVB  | `2022_r2_vc707_ad6676evb.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vc707_ad6676evb.zip>`_                                                                          |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2022_r2_vc707_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vc707_fmcomms2-3.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS4   | `2022_r2_vc707_fmcomms4.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vc707_fmcomms4.zip>`_                                                                            |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | AD9081     | `2022_r2_vcu118_ad9081_m4_l8.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2022_r2_vcu118_ad9081_m8_l4.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081_m8_l4.zip>`_                                                                  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2022_r2_vcu118_ad9081_204c_txmode_10_rxmode_11.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081_204c_txmode_10_rxmode_11.zip>`_                            |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2022_r2_vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.zip>`_  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2022_r2_vcu118_ad9081_204c_txmode_23_rxmode_25.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081_204c_txmode_23_rxmode_25.zip>`_                            |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2022_r2_vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps.zip>`_  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2022_r2_vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.zip>`_  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | DAQ3       | `2022_r2_vcu118_daq3.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu118_fmcdaq3.zip>`_                                                                               |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCU128       | AD9081     | `2022_r2_vcu128_ad9081_m8_l4.zip <https://swdownloads.analog.com/cse/microblaze/2022_r2/vcu128_ad9081_m8_l4.zip>`_                                                                  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   **Latest Build: 2023-04-02 - 2021_R2**

   
   | Linux branch: 2021_R2
   | Linux repository: :git-linux:`linux`
   | HDL branch: hdl_2021_r2
   | HDL repository: :git-hdl:`hdl`



+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FPGA Carrier | FMC Card   | Download                                                                                                                                                                            |
+==============+============+=====================================================================================================================================================================================+
| KC705        | AD9467_FMC | `2021_r2_kc705_ad9467_fmc.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/kc705_ad9467_fmc.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2021_r2_kc705_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/kc705_fmcomms2-3.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | ADRV9371X  | `2021_r2_kcu105_adrv9371x.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/kcu105_adrv9371x.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2021_r2_kcu105_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/kcu105_fmcomms2-3.zip>`_                                                                      |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VC707        | AD6676EVB  | `2021_r2_vc707_ad6676evb.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vc707_ad6676evb.zip>`_                                                                          |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCADC2    | `2021_r2_vc707_fmcadc2.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vc707_fmcadc2.zip>`_                                                                              |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCADC5    | `2021_r2_vc707_fmcadc5.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vc707_fmcadc5.zip>`_                                                                              |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | FMCOMMS2-3 | `2021_r2_vc707_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vc707_fmcomms2-3.zip>`_                                                                        |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | AD9081     | `2021_r2_vcu118_ad9081_204c_txmode_10_rxmode_11.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vcu118_ad9081_204c_txmode_10_rxmode_11.zip>`_                            |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2021_r2_vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.zip>`_  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2021_r2_vcu118_ad9081_204c_txmode_23_rxmode_25.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vcu118_ad9081_204c_txmode_23_rxmode_25.zip>`_                            |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2021_r2_vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps.zip>`_  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              |            | `2021_r2_vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.zip>`_  |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCU128       | AD9081     | `2021_r2_vcu128_ad9081_m8_l4.zip.zip <https://swdownloads.analog.com/cse/microblaze/2021_r2/vcu128_ad9081_m8_l4.zip>`_                                                              |
+--------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   **Latest Build: 2022_08_05 - 2021_R1**

   
   | Linux branch: 2021_R1
   | Linux repository: :git-linux:`linux`
   | HDL branch: hdl_2021_r1
   | HDL repository: :git-hdl:`hdl`



+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| FPGA Carrier | FMC Card   | Download                                                                                                        |
+==============+============+=================================================================================================================+
| KC705        | AD9467_FMC | `2021_r1_kc705_ad9467_fmc.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/kc705_ad9467_fmc.zip>`_    |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| KC705        | FMCOMMS2-3 | `2021_r1_kc705_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/kc705_fmcomms2-3.zip>`_    |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| KCU105       | ADRV9371X  | `2021_r1_kcu105_adrv9371x.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/kcu105_adrv9371x.zip>`_    |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCDAQ2    | `2021_r1_kcu105_fmcdaq2.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/kcu105_fmcdaq2.zip>`_        |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCOMMS2-3 | `2021_r1_kcu105_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/kcu105_fmcomms2-3.zip>`_  |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| VC707        | AD6676EVB  | `2021_r1_vc707_ad6676evb.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/vc707_ad6676evb.zip>`_      |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| VC707        | FMCADC5    | `2021_r1_vc707_fmcadc5.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/vc707_fmcadc5.zip>`_          |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| VC707        | FMCOMMS2-3 | `2021_r1_vc707_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/vc707_fmcomms2-3.zip>`_    |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+
| VC707        | FMCOMMS4   | `2021_r1_vc707_fmcomms4.zip <https://swdownloads.analog.com/cse/microblaze/2021_r1/vc707_fmcomms4.zip>`_        |
+--------------+------------+-----------------------------------------------------------------------------------------------------------------+

.. note::

   **Latest Build: 2021_07_27 - 2019_R2**

   
   | Linux branch: 2019_R2
   | Linux repository: :git-linux:`linux`
   | HDL branch: hdl_2019_r2
   | HDL repository: :git-hdl:`hdl`



+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| FPGA Carrier | FMC Card     | Download                                                                                                                        |
+==============+==============+=================================================================================================================================+
| KC705        | AD9467_FMC   | `2019_r2_kc705_ad9467_fmc.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kc705_ad9467_fmc.zip>`_        |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCDAQ2      | `2019_r2_kc705_fmcdaq2.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kc705_fmcdaq2.zip>`_              |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCJESDADC1  | `2019_r2_kc705_fmcjesdadc1.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kc705_fmcjesdadc1.zip>`_      |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCOMMS2-3   | `2019_r2_kc705_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kc705_fmcomms2-3.zip>`_        |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCOMMS4     | `2019_r2_kc705_fmcomms4.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kc705_fmcomms4.zip>`_            |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | ADRV9371X    | `2019_r2_kcu105_adr9371x.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kcu105_adrv9371x.zip>`_         |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCDAQ2      | `2019_r2_kcu105_fmcdaq2.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kcu105_fmcdaq2.zip>`_            |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCOMMS2-3   | `2019_r2_kcu105_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kcu105_fmcomms2-3.zip>`_      |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCOMMS4     | `2019_r2_kcu105_fmcomms4.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.kcu105_fmcomms4.zip>`_          |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VC707        | AD6676EVB    | `2019_r2_vc707_ad6676evb.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vc707_ad6676evb.zip>`_          |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCADC2      | `2019_r2_vc707_fmcadc2.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vc707_fmcadc2.zip>`_              |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCADC5      | `2019_r2_vc707_fmcadc5.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vc707_fmcadc5.zip>`_              |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCJESDADC1  | `2019_r2_vc707_fmcjesdadc1.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vc707_fmcjesdadc1.zip>`_      |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCOMMS2-3   | `2019_r2_vc707_fmcomms2-3.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vc707_fmcomms2-3.zip>`_        |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | AD9081       | `2019_r2_vcu118_ad9081.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vcu118_ad9081.zip>`_              |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | AD9081 M8 L4 | `2019_r2_vcu118_ad9081_m8_l4.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vcu118_ad9081_m8_l4.zip>`_  |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | AD9208 Dual  | `2019_r2_vcu118_dual_ad9208.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vcu118_dual_ad9208.zip>`_    |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+
| VCU118       | FMCDAQ3      | `2019_r2_vcu118_fmcdaq3.zip <https://swdownloads.analog.com/cse/microblaze/2019_r2/simpleImage.vcu118_fmcdaq3.zip>`_            |
+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------+

.. note::

   **Latest Build: 2018_05_08 - 2018_R1**

   
   | Linux branch:2018_R1
   | Linux repository::git-linux:`linux`
   | Vivado branch:hdl_2018_r1
   | Vivado repository::git-hdl:`hdl`



+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| FPGA Carrier | FMC Card    | Download                                                                                                               |
+==============+=============+========================================================================================================================+
| KC705        | AD9467_FMC  | `2018_r1_kc705_ad9467_fmc.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kc705_ad9467_fmc.zip>`_    |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCDAQ2     | `2018_r1_kc705_fmcdaq2.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kc705_fmcdaq2.zip>`_          |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCJESDADC1 | `2018_r1_kc705_fmcjesdadc1.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kc705_fmcjesdadc1.zip>`_  |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCOMMS2-3  | `2018_r1_kc705_fmcomms2-3.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kc705_fmcomms2-3.zip>`_    |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KC705        | FMCOMMS4    | `2018_r1_kc705_fmcomms4.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kc705_fmcomms4.zip>`_        |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KCU105       | ADRV9371X   | `2018_r1_kcu105_adr9371x.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kcu105_adr9371x.zip>`_      |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCDAQ2     | `2018_r1_kcu105_fmcdaq2.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kcu105_fmcdaq2.zip>`_        |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCDAQ3     | `2018_r1_kcu105_fmcdaq3.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kcu105_fmcdaq3.zip>`_        |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCOMMS2-3  | `2018_r1_kcu105_fmcomms2-3.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kcu105_fmcomms2-3.zip>`_  |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| KCU105       | FMCOMMS4    | `2018_r1_kcu105_fmcomms4.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_kcu105_fmcomms4.zip>`_      |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | AD6676EVB   | `2018_r1_vc707_ad6676evb.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_ad6676evb.zip>`_      |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCADC2     | `2018_r1_vc707_fmcadc2.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_fmcadc2.zip>`_          |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCADC5     | `2018_r1_vc707_fmcadc5.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_fmcadc5.zip>`_          |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCDAQ2     | `2018_r1_vc707_fmcdaq2.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_fmcdaq2.zip>`_          |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCJESDADC1 | `2018_r1_vc707_fmcjesdadc1.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_fmcjesdadc1.zip>`_  |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCOMMS2-3  | `2018_r1_vc707_fmcomms2-3.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_fmcomms2-3.zip>`_    |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+
| VC707        | FMCOMMS4    | `2018_r1_vc707_fmcomms4.zip <http://swdownloads.analog.com/cse/microblaze/2018_r1/2018_r1_vc707_fmcomms4.zip>`_        |
+--------------+-------------+------------------------------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/section>/resources/tools-software/linux-software/adi-kuiper_images/master#master_microblaze_images&
   :alt: master#master_microblaze_images&

There are two ways of loading the design. One is using the XMD command line. Open a xmd command window/shell and enter the commands manually.

Below is just a example and the file-names may vary.

.. container:: box bgblue

   
   .. warning::

      Xilinx XMD command console

   
   

.. raw:: html

   <details><summary>Click to expand

::
   
      Dave@HAL9000:~$ xmd
                                                                                                                                                                                                                   
      **** Xilinx Microprocessor Debugger (XMD) Engine
      **** XMD v2014.2 (64-bit)
        ** SW Build 932637 on Wed Jun 11 13:12:06 MDT 2014
          ** Copyright 1986-2014 Xilinx, Inc. All Rights Reserved.
   
   
      XMD% fpga -f download.bit                                                                                                                                                                                    
      Configuring Device 1 (xcku040) with Bitstream -- download.bit
      ....10....20....30....40....50....60.....70....80....90....Done
      Successfully downloaded bit file.
   
      JTAG chain configuration
      Device   ID Code        IR Length    Part Name
       1       03822093           6        xcku040
   
      0
      XMD% connect mb mdm                                                                                                                                                                                          
                                                                                                                                                                                                                   
      JTAG chain configuration
      Device   ID Code        IR Length    Part Name
       1       03822093           6        xcku040
   
      MicroBlaze Processor Configuration :
      Version............................9.3
      Optimization.......................Performance
      Interconnect.......................AXI-LE
      MMU Type...........................Full_MMU
      No of PC Breakpoints...............1
      No of Read Addr/Data Watchpoints...0
      No of Write Addr/Data Watchpoints..0
      Instruction Cache Support..........on
      Instruction Cache Base Address.....0x80000000
      Instruction Cache High Address.....0xbfffffff
      Data Cache Support.................on
      Data Cache Base Address............0x80000000
      Data Cache High Address............0xbfffffff
      Exceptions  Support................on
      FPU  Support.......................off
      Hard Divider Support...............on
      Hard Multiplier Support............on - (Mul64)
      Barrel Shifter Support.............on
      MSR clr/set Instruction Support....on
      Compare Instruction Support........on
      PVR Supported......................on
      PVR Configuration Type.............Full
      Data Cache Write-back Support......off
      Fault Tolerance Support............off
      Stack Protection Support...........off
   
      Connected to "mb" target. id = 0
      Starting GDB server for "mb" target (id = 0) at TCP port no 1234
   
      XMD% dow /home/dace/linux/arch/microblaze/boot/simpleImage.kcu105_ad_fmcdaq2_ebz                                                                                                   
      System Reset .... DONE
      Downloading Program -- /home/michael/linux/arch/microblaze/boot/simpleImage.kcu105_ad_fmcdaq2_ebz                                                                                     
          section, .text: 0x80000000-0x8031cda7
          section, .init.text: 0x803fc000-0x804185eb
          section, .init.ivt: 0x8041afac-0x8041afd3
          section, __fdt_blob: 0x8031cda8-0x80324da7
          section, .rodata: 0x80325000-0x803b950f
          section, __ksymtab: 0x803b9510-0x803be90f
          section, __ksymtab_gpl: 0x803be910-0x803c1e27
          section, __ksymtab_strings: 0x803c1e28-0x803d4dd7
          section, __param: 0x803d4dd8-0x803d5147
          section, __modver: 0x803d5148-0x803d5fff
          section, __ex_table: 0x803d6000-0x803d75df
          section, .notes: 0x803d75e0-0x803d7603
          section, .sdata2: 0x803d7604-0x803d7fff
          section, .data: 0x803d8000-0x803fbc5f
          section, .init.data: 0x804185ec-0x8041afab
          section, .init.setup: 0x8041afd4-0x8041b327
          section, .initcall.init: 0x8041b328-0x8041b683
          section, .con_initcall.init: 0x8041b684-0x8041b68b
          section, .init.ramfs: 0x8041b68c-0x806f97b3
          section, .bss: 0x806fa000-0x8070f8db
      Download Progress........10.......20.......30.......40.......50........60.......70.......80.......90........Done                                                                                             
      Setting PC with Program Start Address 0x80000000
      XMD% con                                                                                                                                                                                                     
      Processor started. Type "stop" to stop processor
   
      RUNNING> XMD%

.. raw:: html

   </details>


XMD has been replaced with XSCT/XSDB in newer releases of VIVADO. In windows, you can run the XSCT terminal from start menu -> Xilinx Design Tools -> Xilinx Software Command Line Tool...

.. container:: box bgblue

   
   .. warning::

      Xilinx XSCT command console

   
   ::
   
      **** Xilinx System Debugger (XSDB) v2021.1
        ** Build date : Jun 10 2021-20:11:58
          ** Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
   
   
      xsdb% connect
      attempting to launch hw_server
   
      **** Xilinx hw_server v2021.1
        ** Build date : Jun 10 2021 at 20:11:57
          ** Copyright 1986-2021 Xilinx, Inc. All Rights Reserved.
   
      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application
   
      INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121
   
      tcfchan#0
      xsdb% fpga -f system_top.bit
      100%    4MB   1.7MB/s  00:02
      xsdb% targets
        1  xc7k325t
           2  MicroBlaze Debug Module at USER2
              3  MicroBlaze #0 (Running)
      xsdb% target 3
      xsdb% dow simpleImage.kc705_fmcomms2-3.strip
      Downloading Program -- /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
              section, .text: 0x80000000 - 0x804763ab
              section, __fdt_blob: 0x804763ac - 0x804863ab
              section, .rodata: 0x80487000 - 0x808b110f
              section, .builtin_fw: 0x808b1110 - 0x808b1133
              section, __ksymtab: 0x808b1134 - 0x808b746b
              section, __ksymtab_gpl: 0x808b746c - 0x808bc483
              section, __ksymtab_strings: 0x808bc484 - 0x808d6973
              section, __param: 0x808d6974 - 0x808d6e5f
              section, __modver: 0x808d6e60 - 0x808d6fff
              section, __ex_table: 0x808d7000 - 0x808d844f
              section, .notes: 0x808d8450 - 0x808d848b
              section, .sdata2: 0x808d848c - 0x808d8fff
              section, .data: 0x808d9000 - 0x8095893f
              section, .init.text: 0x80959000 - 0x8097a75b
              section, .init.data: 0x8097a75c - 0x8097c053
              section, .init.ivt: 0x8097c054 - 0x8097c07b
              section, .init.setup: 0x8097c07c - 0x8097c3f3
              section, .initcall.init: 0x8097c3f4 - 0x8097c80f
              section, .con_initcall.init: 0x8097c810 - 0x8097c813
              section, .init.ramfs: 0x8097c814 - 0x80c2a9fb
              section, .bss: 0x80c2b000 - 0x80c4225b
      100%   12MB   0.2MB/s  00:56
      Setting PC to Program Start Address 0x80000000
      Successfully downloaded /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
      xsdb% Info: MicroBlaze #0 (target 3) Stopped at 0x0 (Stop)
      xsdb% con
      Info: MicroBlaze #0 (target 3) Running
      xsdb%
   


The second method is to run the tcl script which takes care of loading the bit file and the linux image. Run Vivado TCL Shell from Windows start menu -> Xilinx Design Suite -> Vivado -> Vivado TCL Shell. (In Linux, source the settings.sh file first)

Then run the tcl script:

.. container:: box bgblue

   
   .. warning::

      Vivado TCL shell or Linux console

   
   ::
   
   
      **** Xilinx System Debugger (XSDB) v2021.1
        ** Build date : Jun 10 2021-20:11:58
          ** Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
   
   
      xsdb% source run.tcl
      attempting to launch hw_server
   
      **** Xilinx hw_server v2021.1
        ** Build date : Jun 10 2021 at 20:11:57
          ** Copyright 1986-2021 Xilinx, Inc. All Rights Reserved.
   
      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application
   
      INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121
   
      100%    4MB   1.7MB/s  00:02
      Downloading Program -- /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
              section, .text: 0x80000000 - 0x804763ab
              section, __fdt_blob: 0x804763ac - 0x804863ab
              section, .rodata: 0x80487000 - 0x808b110f
              section, .builtin_fw: 0x808b1110 - 0x808b1133
              section, __ksymtab: 0x808b1134 - 0x808b746b
              section, __ksymtab_gpl: 0x808b746c - 0x808bc483
              section, __ksymtab_strings: 0x808bc484 - 0x808d6973
              section, __param: 0x808d6974 - 0x808d6e5f
              section, __modver: 0x808d6e60 - 0x808d6fff
              section, __ex_table: 0x808d7000 - 0x808d844f
              section, .notes: 0x808d8450 - 0x808d848b
              section, .sdata2: 0x808d848c - 0x808d8fff
              section, .data: 0x808d9000 - 0x8095893f
              section, .init.text: 0x80959000 - 0x8097a75b
              section, .init.data: 0x8097a75c - 0x8097c053
              section, .init.ivt: 0x8097c054 - 0x8097c07b
              section, .init.setup: 0x8097c07c - 0x8097c3f3
              section, .initcall.init: 0x8097c3f4 - 0x8097c80f
              section, .con_initcall.init: 0x8097c810 - 0x8097c813
              section, .init.ramfs: 0x8097c814 - 0x80c2a9fb
              section, .bss: 0x80c2b000 - 0x80c4225b
      100%   12MB   0.2MB/s  00:56
      Setting PC to Program Start Address 0x80000000
      Successfully downloaded /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
      Info: MicroBlaze #0 (target 3) Running
      xsdb% Info: tcfchan#0 closed
      xsdb%
   



Messages
--------

If you are interested in the Linux console messages and command line interface, connect a USB cable to the USB UART port. Terminal settings are 115200,8N1.

There are two users:

====== ========
user   password
====== ========
root   analog
analog analog
====== ========

If you FPGA carrier board (`KC705 <https://www.xilinx.com/KC705>`_, `vc707 <https://www.xilinx.com/vc707>`_, `ml605 <https://www.xilinx.com/ml605>`_) features a LCD display and the board is connected to a DHCP enabled network. You should also see it's IP address printed on the display. This allows you to connect remote to the board as well. (ssh, libiio remote)

Unlike shown in the picture below you won't see the second line. In case the IP address is 192.168.2.2, this indicates that DHCP failed and it's now using it's default address. This address may not be within your subnet, and things therefore may fail.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/ml605-lcd.png
   :alt: LCD image
   :width: 200px

You should see the kernel start-up messages as follows:


.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      # Early console on uartlite at 0x40600000
      bootconsole [earlyser0] enabled
      Ramdisk addr 0x00000000,
      Compiled-in FDT at 8031cda8
      Linux version 3.17.0-126658-g6807aea (michael@mhenneri-D04) (gcc version 4.8.3 20140131 (prerelease) (crosstool-NG 1.18.0) ) #1647 Fri Nov 21 10:33:05 CET 2014
      setup_cpuinfo: initialising
      setup_cpuinfo: Using full CPU PVR support
      wt_msr_noirq
      setup_memory: max_mapnr: 0x30000
      setup_memory: min_low_pfn: 0x80000
      setup_memory: max_low_pfn: 0xb0000
      setup_memory: max_pfn: 0xb0000
      Zone ranges:
        DMA      [mem 0x80000000-0xafffffff]
        Normal   empty
      Movable zone start for each node
      Early memory node ranges
        node   0: [mem 0x80000000-0xbfffffff]
      On node 0 totalpages: 196608
      free_area_init_node: node 0, pgdat 803fb104, node_mem_map 80800000
        DMA zone: 1536 pages used for memmap
        DMA zone: 0 pages reserved
        DMA zone: 196608 pages, LIFO batch:31
      early_printk_console remapping from 0x40600000 to 0xffffd000
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
      pcpu-alloc: [0] 0
      Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 195072
      Kernel command line: console=ttyUL0,115200
      PID hash table entries: 4096 (order: 2, 16384 bytes)
      Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
      Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
      Memory: 771408K/786432K available (3187K kernel code, 143K rwdata, 708K rodata, 3061K init, 86K bss, 15024K reserved)
      Kernel virtual memory layout:
        * 0xffffe000..0xfffff000  : fixmap
        * 0xffffd000..0xffffe000  : early ioremap
        * 0xb0000000..0xffffd000  : vmalloc & ioremap
      NR_IRQS:128
      /axi@0/axi-intc@41200000: num_irq=15, edge=0x3810
      /axi@0/axi-timer@41c00000: irq=1
      xilinx_timer_set_mode: shutdown
      xilinx_timer_set_mode: periodic
      sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 42949672950ns
      Calibrating delay loop... 48.51 BogoMIPS (lpj=97024)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
      Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
      devtmpfs: initialized
      NET: Registered protocol family 16
      Switched to clocksource xilinx_clocksource
      xilinx_timer_set_mode: oneshot
      NET: Registered protocol family 2
      TCP established hash table entries: 8192 (order: 3, 32768 bytes)
      TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
      TCP: Hash tables configured (established 8192 bind 8192)
      TCP: reno registered
      UDP hash table entries: 512 (order: 1, 8192 bytes)
      UDP-Lite hash table entries: 512 (order: 1, 8192 bytes)
      NET: Registered protocol family 1
      RPC: Registered named UNIX socket transport module.
      RPC: Registered udp transport module.
      RPC: Registered tcp transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      XGpio: /axi@0/gpio@40000000: registered, base is 251
      XGpio: /axi@0/gpio@40000000: dual channel registered, base is 245
      XGpio: /axi@0/gpio@40020000: registered, base is 232
      XGpio: /axi@0/gpio@40020000: dual channel registered, base is 224
      Skipping unavailable RESET gpio -2 (reset)
      futex hash table entries: 256 (order: -1, 3072 bytes)
      jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      msgmni has been set to 1506
      Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
      io scheduler noop registered
      io scheduler deadline registered
      io scheduler cfq registered (default)
      Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 46, base_baud = 0) is a uartlite
      console [ttyUL0] enabled
      console [ttyUL0] enabled
      bootconsole [earlyser0] disabled
      bootconsole [earlyser0] disabled
      of_serial 41400000.serial: Unknown serial port found, ignored
      brd: module loaded
      Xilinx SystemACE device driver, major=254
      xilinx_lcd 40010000.gpio_lcd: Device Tree Probing 'gpio_lcd'
      xilinx_lcd 40010000.gpio_lcd: LCD 0x40010000 mapped to 0xb01a0000
      xilinx_spi 44a70000.axi-quad-spi: property name 'xlnx,num-ss-bits' is deprecated.
      xilinx_spi 44a70000.axi-quad-spi: at 0x44A70000 mapped to 0xb01c0000, irq=10
      libphy: Fixed MDIO Bus: probed
      xilinx_axienet 40e00000.network: TX_CSUM 0
      xilinx_axienet 40e00000.network: RX_CSUM 0
      libphy: Xilinx Axi Ethernet MDIO: probed
      i2c /dev entries driver
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.2: Driver ad9467 requests probe deferral
      platform 44a90000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      platform 44a91000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      platform 44a60000.axi-jesd-gt: Driver cf_axi_jesd204b_gt requests probe deferral
      ad9523 spi32766.0: probed ad9523-1
      platform 44a04000.axi-ad9144-hpc: Driver cf_axi_dds requests probe deferral
      ad9144 spi32766.1: Failed to get clocks
      spi spi32766.1: Driver ad9144 requests probe deferral
      TCP: cubic registered
      NET: Registered protocol family 17
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.2: Driver ad9467 requests probe deferral
      platform 44a90000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      platform 44a91000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      cf_axi_jesd204b_gt 44a60000.axi-jesd-gt: AXI-JESD204B (5.00.b) at 0x44A60000 mapped to 0xb0280000,
      platform 44a04000.axi-ad9144-hpc: Driver cf_axi_dds requests probe deferral
      ad9144 spi32766.1: Failed to get clocks
      spi spi32766.1: Driver ad9144 requests probe deferral
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.2: Driver ad9467 requests probe deferral
      cf_axi_jesd204b_v51 44a90000.jesd204: AXI-JESD204B 5.2 Rev 1, at 0x44A90000 mapped to 0xb0032000,
      cf_axi_jesd204b_v51 44a91000.jesd204: AXI-JESD204B 5.2 Rev 1, at 0x44A91000 mapped to 0xb0034000,
      platform 44a04000.axi-ad9144-hpc: Driver cf_axi_dds requests probe deferral
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      ad9467 spi32766.2: AD9680 PLL LOCKED
      cf_axi_dds 44a04000.axi-ad9144-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (8.00.b) at 0x44A04000 mapped to 0xb0098000, probed DDS AD9144
      cf_axi_adc 44a10000.axi-ad9680-hpc: ADI AIM (8.00.b) at 0x44A10000 mapped to 0xb02c0000, probed ADC AD9680 as MASTER
      Freeing unused kernel memory: 3060K (803fc000 - 806f9000)
      Starting logging: OK
      Starting network...
      Starting network...
      udhcpc (v1.22.1) started
      net eth0: Promiscuous mode disabled.
      net eth0: Promiscuous mode disabled.
      Sending discover...
      xilinx_axienet 40e00000.network eth0: Link is Down
      xilinx_axienet 40e00000.network eth0: Link is Up - 100Mbps/Full - flow control off
      Sending discover...
      Sending select for 10.44.2.94...
      Lease of 10.44.2.94 obtained, lease time 86400
      deleting routers
      adding dns 10.32.51.110
      adding dns 10.64.53.110
      Starting dropbear sshd: OK
      random: dropbear urandom read with 86 bits of entropy available
      Starting IIO Server Daemon
   
      Welcome to Buildroot
      buildroot login: root
      #
   


IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/connect.png
   :alt: Connect Window
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/plot_window.png
   :alt: Plot
   :align: center
   :width: 800px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/daq2_plugin.png
   :alt: DAQ2 plugin
   :align: center
   :width: 800px


