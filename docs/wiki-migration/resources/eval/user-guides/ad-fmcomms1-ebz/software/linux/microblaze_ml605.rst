Linux on the Xilinx ML605 Virtex6 FPGA development Board
========================================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



This guide provides some step-by-step instructions on how to build a Microblaze Linux Kernel image for the AD-FMCOMMS1 FMC board connected to an `ML605 <https://www.xilinx.com/ML605>`__.

.. important::

   Building Linux on ML605 Virtex6 board remains on this website only for legacy purposes. The Linux support for this carrier has been discontinued.


Required Software
-----------------

-  Microblaze GNU Tools
-  :git-linux:`Linux Kernel Source <tree/master>`
-

|Root File-system (initramfs)|

-  `Xilinx ISE Design Suite <https://www.xilinx.com/ISE>`__

Build Linux - Step by Step instructions
---------------------------------------

Get Microblaze Little Endian Toolchain from Xilinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1$ git clone git://git.xilinx.com/xldk/microblaze_v1.0_le.git
      Cloning into 'microblaze_v1.0_le'...
      remote: Counting objects: 4, done.
      remote: Compressing objects: 100% (4/4), done.
      Receiving objects:  75% (3/4), 12.65 MiB | 5 KiB/s
      [--snip--]
   


Untar Toolchain
~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1$ cd microblaze_v1.0_le/
      Dave@HAL9000:~/fmcomms1/microblaze_v1.0_le$ tar xzf microblazeel-unknown-linux-gnu.tar.gz
   


Get Linux kernel source
~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1$ git clone https://github.com/analogdevicesinc/linux.git
      Cloning into 'linux'...
      remote: Counting objects: 2757163, done.
      remote: Compressing objects: 100% (495484/495484), done.
      remote: Total 2757163 (delta 2296596), reused 2687337 (delta 2234506)
      Receiving objects: 100% (2757163/2757163), 782.04 MiB | 1.39 MiB/s, done.
      Resolving deltas: 100% (2296596/2296596), done.
      Dave@HAL9000:~/fmcomms1$
   


Checkout master branch
~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1$ cd linux/
      Dave@HAL9000:~/fmcomms1/linux$ git checkout origin/master
      Checking out files: 100% (16412/16412), done.
      Dave@HAL9000:~/fmcomms1/linux$
   


Set Environmental Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ export PATH=~/fmcomms1/microblaze_v1.0_le/microblazeel-unknown-linux-gnu/bin/:$PATH
      Dave@HAL9000:~/fmcomms1/linux$ export ARCH=microblaze
      Dave@HAL9000:~/fmcomms1/linux$ export CROSS_COMPILE=microblazeel-unknown-linux-gnu-
   


Configure Kernel for ML605 XCOMM platform (aka FMCOMMS1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ make ml605_xcomm_defconfig
        HOSTCC  scripts/basic/fixdep
        HOSTCC  scripts/kconfig/conf.o
        SHIPPED scripts/kconfig/zconf.tab.c
        SHIPPED scripts/kconfig/zconf.lex.c
        SHIPPED scripts/kconfig/zconf.hash.c
        HOSTCC  scripts/kconfig/zconf.tab.o
        HOSTLD  scripts/kconfig/conf
      #
      # configuration written to .config
      #
      Dave@HAL9000:~/fmcomms1/linux$
   


Get Root File-System
~~~~~~~~~~~~~~~~~~~~

.. image:: https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
   :alt: Root File-system (initramfs)

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ wget http://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/rootfs.cpio.gz
      --2012-12-19 09:25:28--  http://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/rootfs.cpio.gz
      Resolving wiki.analog.com (wiki.analog.com)... 195.170.124.184
      Connecting to wiki.analog.com (wiki.analog.com)|195.170.124.184|:80... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 2958801 (2.8M) [application/octet-stream]
      Saving to: `rootfs.cpio.gz'
   
      100%[=====================================================================================================
      =====================================================================>] 2,958,801   1.42M/s   in 2.0s    
   
      2012-12-19 09:25:30 (1.42 MB/s) - `rootfs.cpio.gz' saved [2958801/2958801]
      Dave@HAL9000:~/fmcomms1/linux$
   


Build kernel
~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ make -j5 simpleImage.cf_xcomm_ml605
        CHK     include/linux/version.h
        UPD     include/linux/version.h
        HOSTCC  scripts/kallsyms
        HOSTCC  scripts/bin2c
        HOSTCC  scripts/dtc/checks.o
        CC      scripts/mod/empty.o
      [--snip--]
        CP      vmlinux arch/microblaze/boot/simpleImage.cf_xcomm_ml605.unstrip
        OBJCOPY arch/microblaze/boot/simpleImage.cf_xcomm_ml605
        UIMAGE  arch/microblaze/boot/simpleImage.cf_xcomm_ml605.ub
      Image Name:   Linux-3.5.0-rc4-00817-gbf1afb2
      Created:      Tue Dec 18 16:50:37 2012
      Image Type:   MicroBlaze Linux Kernel Image (uncompressed)
      Data Size:    6178556 Bytes = 6033.75 kB = 5.89 MB
      Load Address: c0000000
      Entry Point:  c0000000
        STRIP   arch/microblaze/boot/simpleImage.cf_xcomm_ml605
      Kernel: arch/microblaze/boot/simpleImage.cf_xcomm_ml605 is ready  (#1)
      Dave@HAL9000:~/devel/git/staging_3$
   


Generate ML605 SysACE Compact Flash File
----------------------------------------

.. tip::

   Following example shows building the System ACE file on a Linux host. Same steps can alternatively performed on a **Windows ISE** installation.


Create a directory and gather required files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1$ mkdir build
      Dave@HAL9000:~/fmcomms1$ cd build/
      Dave@HAL9000:~/fmcomms1/build$ cp ~/fpgahdl_xilinx/cf_xcomm/implementation/system.bit .
      Dave@HAL9000:~/fmcomms1/build$ cp ../linux/arch/microblaze/boot/simpleImage.cf_xcomm_ml605 .
   


Source Xilinx ISE settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

On Windows open a ISE Design Suite Command Prompt.

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/build$ source /opt/Xilinx/14.1/ISE_DS/settings64.sh
      . /opt/Xilinx/14.1/ISE_DS/common/.settings64.sh /opt/Xilinx/14.1/ISE_DS/common
      . /opt/Xilinx/14.1/ISE_DS/EDK/.settings64.sh /opt/Xilinx/14.1/ISE_DS/EDK
      . /opt/Xilinx/14.1/ISE_DS/common/CodeSourcery/.settings64.sh /opt/Xilinx/14.1/ISE_DS/common/CodeSourcery
      . /opt/Xilinx/14.1/ISE_DS/PlanAhead/.settings64.sh /opt/Xilinx/14.1/ISE_DS/PlanAhead
      . /opt/Xilinx/14.1/ISE_DS/../../Vivado/2012.1/.settings64.sh /opt/Xilinx/14.1/ISE_DS/../../Vivado/2012.1
      . /opt/Xilinx/14.1/ISE_DS/ISE/.settings64.sh /opt/Xilinx/14.1/ISE_DS/ISE
      . /opt/Xilinx/14.1/ISE_DS/SysGen/.settings64.sh /opt/Xilinx/14.1/ISE_DS/SysGen
   


Run XMD genace tcl script
~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/build$ xmd -tcl genace.tcl -hw system.bit -elf simpleImage.cf_xcomm_ml605 -ace linux.ace -board ml605 -target mdm
      Xilinx Microprocessor Debugger (XMD) Engine
      Xilinx EDK 14.1 Build EDK_P.15xf
      Copyright (c) 1995-2009 Xilinx, Inc.  All rights reserved.
      Executing xmd script : /opt/Xilinx/14.1/ISE_DS/EDK/data/xmd/genace.tcl
   
      #######################################################################
      XMD GenACE utility. Generate SystemACE File from bit/elf/data Files
      #######################################################################
      Parsing genace option: -hw system.bit -elf simpleImage.cf_xcomm_ml605 -ace linux.ace -board ml605 -target mdm
      GenACE Options:
          Board      : ml605
          Jtag Devs  : xc6vlx240t
          FPGA pos   : 1
          JPROG      : false
          HW File    : system.bit
          ACE File   : linux.ace
          nCPUs      : 1
   
          Processor mdm_1 Information
              Debug opt : -debugdevice devicenr 1 cpunr 1
              ELF files : simpleImage.cf_xcomm_ml605
              Start PC Address : 0xc0000000
      Open SVF file
   
      ############################################################
      Converting Bitstream 'system.bit' to SVF file 'system.svf'
   
      [--snip--]
   
      RUNNING>
      ############################################################
      Converting SVF file 'linux.svf' to SystemACE file 'linux.ace'
      Executing 'impact -batch svf2ace.scr'
   
      SystemACE file 'linux.ace' created
   


The newly created System ACE file can now be transferred to an Compact Flash card. Instructions on how to format and setup the CF Card and configure the ML605 for SysACE boot can be found here:

:doc:`AD-FMCOMMS1-EBZ ML605 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/microblaze_ml605>`

More information
----------------

-  :doc:`AD-FMCOMMS1-EBZ Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz>`
-  :doc:`ADI IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9523>`
-  :doc:`ADF4351: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
-  :doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  `Xilinx Open Source Wiki site <http://wiki.xilinx.com>`__

*Need Help?*

-  :ez:`Analog Devices Linux Device Drivers Help Forum <linux-software-drivers>`
-  `Ask a Question <https://ez.analog.com/>`__


.. |Root File-system (initramfs)| image:: https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
