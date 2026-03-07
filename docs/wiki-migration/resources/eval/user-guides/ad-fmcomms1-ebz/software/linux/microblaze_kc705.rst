Linux on the Xilinx KC705 Kintex™-7 FPGA development Board
==========================================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


This guide provides some step-by-step instructions on how to build a Microblaze Linux Kernel image for the AD-FMCOMMS1 FMC board connected to an `KC705 <https://www.xilinx.com/KC705>`_.

Required Software
-----------------

-  Microblaze GNU Tools included as part of the `Vivado/Vitis <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_ you will have the cross compiler tools for Microblaze under: <Vivado/vitis_install_dir>/Vitis/<version>/gnu/microblaze/linux_toolchain/lin64_le/bin/microblazeel-xilinx-linux-gnu-gcc.
-  :git-linux:`Linux Kernel Source <tree/main>`
-

|Root File-system (initramfs)|

-  `Xilinx ISE Design Suite <https://www.xilinx.com/ISE>`_

.. tip::

   Latest released files can be downloaded from :doc:`here </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>`


Build Linux - Step by Step instructions
---------------------------------------

Get Microblaze Little Endian Toolchain from Xilinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The Microblaze Little Endian Toolchain can be found in the Xilinx Vitis install folder:
| For 64-bit hosts use:
| /opt/Xilinx/Vitis/2021.2/gnu/microblaze/linux_toolchain/lin64_le/bin

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
   


Checkout main branch
~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1$ cd linux/
      Dave@HAL9000:~/fmcomms1/linux$ git checkout main
      Checking out files: 100% (16412/16412), done.
      Branch main set up to track remote branch main from origin.
      Switched to a new branch 'main'
      Dave@HAL9000:~/fmcomms1/linux$
   


Set Environmental Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ export PATH=/opt/Xilinx/Vitis/2021.2/gnu/microblaze/linux_toolchain/lin64_le/bin:$PATH
      Dave@HAL9000:~/fmcomms1/linux$ export ARCH=microblaze
      Dave@HAL9000:~/fmcomms1/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-
   


Configure Kernel for KC705 XCOMM platform (aka FMCOMMS1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ make adi_mb_defconfig
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

|image1|

.. tip::

   rootfs.cpio.gz must be placed in the root of your kernel tree.


.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/linux$ wget https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
      --2014-11-21 14:27:54--  http://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/rootfs.cpio.gz
      Resolving wiki.analog.com (wiki.analog.com)... 195.170.124.184
      Connecting to wiki.analog.com (wiki.analog.com)|195.170.124.184|:80... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 3006465 (2.9M) [application/octet-stream]
      Saving to: `rootfs.cpio.gz'
   
      100%[===================================================================================================================================================================>] 3,006,465   75.1K/s   in 37s     
   
      2014-11-21 14:28:32 (79.2 KB/s) - `rootfs.cpio.gz' saved [3006465/3006465]
   
      Dave@HAL9000:~/linux$
   


Build kernel
~~~~~~~~~~~~

The result of building the kernel is an elf file in arch/microblaze/boot named simpleImage.<dts file name> based on the dts specified.

The build process for the kernel searches in the arch/microblaze/boot/dts directory for a specified device tree file and then builds the device tree into the kernel image.

The following command shows the general format for the build target name. Note that the <dts file name> does not include the file extension ".dts".

::

   Dave@HAL9000:~/linux$ make simpleImage.<dts file name>

To see what device-trees for the different FPGA carrier and FMC module combination exist type:

::

   Dave@HAL9000:~/linux$ ls -l arch/microblaze/boot/dts

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   
      Dave@HAL9000:~/fmcomms1/linux$ make -j5 simpleImage.kc705_fmcomms1
        CHK     include/linux/version.h
        UPD     include/linux/version.h
        HOSTCC  scripts/kallsyms
        HOSTCC  scripts/bin2c
        HOSTCC  scripts/dtc/checks.o
        CC      scripts/mod/empty.o
      [--snip--]
        CP      vmlinux arch/microblaze/boot/simpleImage.kc705_fmcomms1.unstrip
        OBJCOPY arch/microblaze/boot/simpleImage.kc705_fmcomms1
        UIMAGE  arch/microblaze/boot/simpleImage.kc705_fmcomms1.ub
      Image Name:   Linux-3.5.0-rc4-00817-gbf1afb2
      Created:      Tue Dec 18 16:50:37 2012
      Image Type:   MicroBlaze Linux Kernel Image (uncompressed)
      Data Size:    6178556 Bytes = 6033.75 kB = 5.89 MB
      Load Address: c0000000
      Entry Point:  c0000000
        STRIP   arch/microblaze/boot/simpleImage.kc705_fmcomms1
      Kernel: arch/microblaze/boot/simpleImage.kc705_fmcomms1is ready  (#1)
      Dave@HAL9000:~/devel/git/staging_3$
   


The newly created Linux ELF file can now be loaded using the Xilinx ISE Microprocessor Debugger (XMD). Further instructions can be found here:

:doc:`AD-FMCOMMS1-EBZ KC705 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/microblaze_kc705>`

More information
----------------

-  :doc:`AD-FMCOMMS1-EBZ Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz>`
-  :doc:`ADI IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9523>`
-  :doc:`ADF4351: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
-  :doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  `Xilinx Open Source Wiki site <http://wiki.xilinx.com>`_

*Need Help?*

-  :ez:`Analog Devices Linux Device Drivers Help Forum <linux-software-drivers>`
-  `Ask a Question <https://ez.analog.com/>`_


.. |Root File-system (initramfs)| image:: https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
.. |image1| image:: https://swdownloads.analog.com/cse/microblaze/rootfs/latest_microblaze_rootfs.cpio.gz
