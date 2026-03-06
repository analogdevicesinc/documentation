Building the Intel SoC-FPGA kernel and devicetrees from source
==============================================================

The script method
-----------------

We provide `a script that does automates <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_socfpga_kernel_image.sh>`__ the build for SoC-FPGA using the Linaro toolchain.

The script takes up to 3 parameters, but if left blank, it uses defaults:

-  **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this, if you want to use an already cloned kernel repo
-  **<devicetree_file>** - which device tree should be exported/copied from the build [argument is optional]
-  **<path_to_other_toolchain>** - in case you have your own preferred toolchain [other than Linaro's or Intel's] you can use override it with this 3rd param

The script will:

-  clone the ADI kernel tree
-  download the Linaro GCC toolchain [if no other is specified]
-  build the ADI kernel tree
-  export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line [with defaults]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_socfpga_kernel_image.sh && chmod +x build_socfpga_kernel_image.sh && ./build_socfpga_kernel_image.sh 

Checkout the Release branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   If not otherwise required always use the latest release!


+----------------------------+



| Release names and Branches |

+============================+

| altera_4.0                 |

+----------------------------+

| altera_4.4                 |

+----------------------------+

| altera_4.6                 |

+----------------------------+

| altera_4.9                 |

+----------------------------+

| altera_4.14                |

+----------------------------+

::

   dave@hal9000:~/github-linux-build/linux$ git checkout origin/altera_4.14 -b altera_4.14
   Branch altera_4.14 set up to track remote branch altera_4.14 from origin.
   Switched to a new branch '2015_R2'

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few toolchains that can be used.

Other toolchains/compilers for ARM may work as well, but the ones described here have been tested and found to work.

Using the Linaro toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Linaro toolchain/compiler can be used to compile to kernel. Linaro compilers (that work with Intel SoC-FPGA) can be downloaded from: https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabi/ . Always use the latest release just in case.

Example:

::

   wget https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabi/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi.tar.xz
   tar -xvf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi.tar.xz

::

   export ARCH=arm
   export CROSS_COMPILE=$(pwd)/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi/bin/arm-linux-gnueabi-

Clone the ADI kernel tree
~~~~~~~~~~~~~~~~~~~~~~~~~

If you do not yet have a local copy of ADI's kernel tree, you can get it via git from:

::

   git clone https://github.com/analogdevicesinc/linux.git

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the kernel tree.

::

   dave@hal9000:~/github-linux-build/linux$ make socfpga_adi_defconfig
   #
   # configuration written to .config
   #
   dave@hal9000:~/github-linux-build/linux$

Build the kernel
~~~~~~~~~~~~~~~~

Build the kernel via 'make'. This is the same for all Intel SoC FPGAs.

::

   dave@hal9000:~/github-linux-build/linux$ make -j5 zImage
   scripts/kconfig/conf --silentoldconfig Kconfig
     CHK     include/config/kernel.release
     CHK     include/generated/uapi/linux/version.h
     UPD     include/config/kernel.release
     CHK     include/generated/utsrelease.h

   [ -- snip --]

     AS      arch/arm/boot/compressed/bswapsdi2.o
     AS      arch/arm/boot/compressed/piggy.gzip.o
     LD      arch/arm/boot/compressed/vmlinux
     OBJCOPY arch/arm/boot/zImage
     Kernel: arch/arm/boot/zImage is ready
     UIMAGE  arch/arm/boot/uImage
   Image Name:   Linux-3.17.0-126697-g611e217-dir
   Created:      Fri Nov 28 10:20:40 2014
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    3195872 Bytes = 3120.97 kB = 3.05 MB
   Load Address: 00008000
   Entry Point:  00008000
   dave@hal9000:~/github-linux-build/linux$

Build the devicetree
~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| device tree                                   | board                                                                                                                       | chip                                                                                                                                                                                                                                                                      |
+===============================================+=============================================================================================================================+===========================================================================================================================================================================================================================================================================+
| socfpga_arria10_socdk_ad9136_fmc_ebz.dts      | :adi:`eval-ad9135` :adi:`EVAL-AD9136`                                                                                       | :adi:`AD9136`                                                                                                                                                                                                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_ad9172_fmc.dts          | :adi:`eval-ad9135` :adi:`EVAL-AD9136`                                                                                       | :adi:`AD9171`, :adi:`AD9172`, :adi:`AD9173`, :adi:`AD9174`, :adi:`AD9175` and :adi:`AD9176`                                                                                                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_adin1300_dual-mii.dts   | TBA                                                                                                                         | :adi:`ADIN1300`                                                                                                                                                                                                                                                           |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_adin1300_dual-rgmii.dts | TBA                                                                                                                         | :adi:`ADIN1300`                                                                                                                                                                                                                                                           |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_adrv9008-1.dts          | :adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>`                                                                                | :adi:`ADRV9008-1`                                                                                                                                                                                                                                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_adrv9008-2.dts          | :adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>`                                                                                | :adi:`ADRV9008-2`                                                                                                                                                                                                                                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_adrv9009.dts            | :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`                                                                                 | :adi:`ADRV9009`                                                                                                                                                                                                                                                           |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| socfpga_arria10_socdk_adrv9371.dts            | :doc:`ADRV9371 </wiki-migration/resources/eval/user-guides/mykonos>` board                                                  | :adi:`AD9371`                                                                                                                                                                                                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The device tree **socfpga_arria10_socdk_sdmmc.dts** can also be used for any Arria10 FPGA that uses an SD card for boot up. Building the device tree uses 'make' by turning the .dts file to a .dtb. The command is simply 'make' plus the device tree name with a .dtb file extension.

::

   dave@hal9000:~/github-linux-build/linux$ make socfpga_arria10_socdk_adin1300_dual-mii.dtb
     DTC     arch/arm/boot/dts/socfpga_arria10_socdk_adin1300_dual-mii.dtb
   dave@hal9000:~/github-linux-build/linux$

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **zImage** and **<device_tree_name>.dtb**. Refer to the code below to find their respective output directories. See :doc:`kuiper-linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` for more information in configuring the SD card.

::

   dave@hal9000:~/github-linux-build/linux$ cp arch/arm/boot/zImage /media/BOOT/zImage
   dave@hal9000:~/github-linux-build/linux$ cp arch/arm/boot/dts/socfpga_arria10_socdk_adin1300_dual-mii.dtb  /media/BOOT/socfpga_arria10_socdk_sdmmc.dtb
