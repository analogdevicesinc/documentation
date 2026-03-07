Building the Zynq Linux kernel and devicetrees from source
==========================================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/linux/kernel/zynq.html


The script method
-----------------

We provide `a script that does automates <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynq_kernel_image.sh>`_ the build for Zynq using the Linaro toolchain.

The script takes up to 3 parameters, but if left blank, it uses defaults:

-  **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this, if you want to use an already cloned kernel repo
-  **<devicetree_file>** - which device tree should be exported/copied from the build ; default is ``zynq-zc702-adv7511-ad9361-fmcomms2-3.dtb`` for Zynq
-  **<path_to_other_toolchain>** - in case you have your own preferred toolchain [other than Linaro's or Xilinx's] you can use override it with this 3rd param

The script will:

-  clone the ADI kernel tree
-  download the Linaro GCC toolchain [if no other is specified]
-  build the ADI kernel tree
-  export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line [with defaults]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynq_kernel_image.sh && chmod +x build_zynq_kernel_image.sh && ./build_zynq_kernel_image.sh 

Building using Petalinux
------------------------

Please see here: :doc:`Building with Petalinux </wiki-migration/resources/tools-software/linux-build/generic/petalinux>`

On the development host
-----------------------

Make sure you have ``u-boot-tools`` installed, to have the ``mkimage`` utility available. You can install it via your distro's package manager.

Then

::

   git clone https://github.com/analogdevicesinc/linux.git

or do a git pull in the existing repository.

Checkout the Release branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Use the latest release, if not required otherwise!


+----------------------------+



| Release names and Branches |

+============================+

| 2014_R2                    |

+----------------------------+

| 2015_R2                    |

+----------------------------+

| 2016_R1                    |

+----------------------------+

| 2016_R2                    |

+----------------------------+

| 2017_R1                    |

+----------------------------+

| 2018_R1                    |

+----------------------------+

| 2018_R2                    |

+----------------------------+

| 2019_R1                    |

+----------------------------+

| 2019_R2                    |

+----------------------------+

| 2021_R1                    |

+----------------------------+

::

   dave@hal9000:~/github-linux-build/linux$ git checkout origin/2021_R1 -b 2021_R1
   Branch 2021_R1 set up to track remote branch 2021_R1from origin.
   Switched to a new branch '2021_R1'

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few toolchains that can be used. The Xilinx toolchain is recommended, but the Linaro toolchain can also be used.

Other toolchains/compilers for ARM may work as well, but the ones described here have been tested and found to work.

Using the Xilinx toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

========================== ==============================
Release names and Branches Required Vivado/Vitis versions
========================== ==============================
2014_R2                    Vivado 2014.2
2015_R2                    Vivado 2015.2
2016_R1                    Vivado 2015.4.2
2016_R2                    Vivado 2016.2
2017_R1                    Vivado 2016.4
2018_R1                    Vivado 2017.4
2018_R2                    Vivado 2018.2
2019_R1                    Vivado 2018.3
2019_R2                    Vivado 2019.1
2021_R1                    Vivado 2021.1
========================== ==============================

::

   dave@hal9000:~/github-linux-build/linux$ source $PATH_to_Xilinx/Xilinx/Vitis/$Vitis_version/settings64.sh

::

   dave@hal9000:~/github-linux-build/linux$ export ARCH=arm
   dave@hal9000:~/github-linux-build/linux$ export CROSS_COMPILE="arm-linux-gnueabihf-"

.. important::

   Find the path to the Xilinx installation folder, and then use it to replace this string: **:math:`PATH_to_Xilinx** that is written above. Same goes for the **`\ Vitis_version**, where you choose the Vitis version.


Using the Linaro toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Linaro toolchain/compiler can be used to compile to kernel. Linaro compilers (that work with Zynq) can be downloaded from: https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabi/ . Always use the latest release just in case.

Example:

::

   wget https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabi/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi.tar.xz
   tar -xvf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi.tar.xz

::

   export ARCH=arm
   export CROSS_COMPILE=$(pwd)/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi/bin/arm-linux-gnueabi-

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the kernel tree. The command shown below is generic and is not project specific. As long as the board is a ZYNQ FPGA, use the configuration below.

::

   dave@hal9000:~/github-linux-build/linux$ make zynq_xcomm_adv7511_defconfig
   #
   # configuration written to .config
   #
   dave@hal9000:~/github-linux-build/linux$

Build the kernel
~~~~~~~~~~~~~~~~

Build the kernel via 'make'. This is the same for all Xilinx ZYNQ FPGAs.

::

   dave@hal9000:~/github-linux-build/linux$ make -j5 UIMAGE_LOADADDR=0x8000 uImage
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

Build the devicetree FCMOMMS2/3/4/5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| device tree                                       | board                                                                         | chip                                                                                                                                                                                                                 |
+===================================================+===============================================================================+======================================================================================================================================================================================================================+
| zynq-adrv9361-z7035-bob                           | :adi:`ADRV1CRR-BOB`                                                           | :adi:`ADRV9361`                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9361-z7035-bob-cmos                      | :adi:`ADRV1CRR-BOB`                                                           | :adi:`ADRV9361`                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9361-z7035-packrf                        | :adi:`ADRV-PACKRF`                                                            | :adi:`ADRV9361`                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9361-z7035-fmc                           | :adi:`ADRV1CRR-FMC`                                                           | the on-board :adi:`ADV7511` and the :adi:`ADRV9361`                                                                                                                                                                  |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9361-z7035-fmc-rfcard-tdd                | :adi:`ADRV1CRR-FMC`                                                           | the on-board :adi:`ADV7511`, :adi:`ADRV9361` and the :adi:`AD-PZSDR2400TDD-EB`                                                                                                                                       |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9364-z7020-bob                           | :adi:`ADRV1CRR-BOB`                                                           | :adi:`ADRV9364`                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9364-z7020-bob-cmos                      | :adi:`ADRV1CRR-BOB`                                                           | :adi:`ADRV9364`                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-adrv9364-z7020-packrf                        | :adi:`ADRV-PACKRF`                                                            | :adi:`ADRV9364`                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-coraz7s                                      | `cora-z7 <https://digilent.com/reference/programmable-logic/cora-z7/start>`_  |                                                                                                                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511                             | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`_                      | the on-board :adi:`ADV7511`                                                                                                                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511-ad9361-fmcomms2-3           | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`_                      | on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board     |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511-ad9364-fmcomms4             | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`_                      | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                        |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511                                | `ZC702 <https://www.xilinx.com/ZC702>`_                                       | the on-board :adi:`ADV7511`                                                                                                                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-ad9361-fmcomms2-3              | `ZC702 <https://www.xilinx.com/ZC702>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-ad9361-fmcomms5                | `ZC702 <https://www.xilinx.com/ZC702>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS5-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz>`                                                                                              |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-ad9364-fmcomms4                | `ZC702 <https://www.xilinx.com/ZC702>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                        |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511                                | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511`                                                                                                                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad6676-fmc                     | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD6676-FMC-EBZ </wiki-migration/resources/eval/ad6676-wideband_rx_subsystem_ad6676ebz>` board                                                                              |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9265-fmc-125ebz              | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD9265-FMC-125EBZ </wiki-migration/resources/fpga/xilinx/fmc/ad9265>` board                                                                                                |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9361-fmcomms2-3              | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9361-fmcomms5                | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS5-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz>` board                                                                                        |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9361-fmcomms5-ext-lo-adf5355 | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS5-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz>` board                                                                                        |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9364-fmcomms4                | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                        |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9434-fmc-500ebz              | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD9434-FMC-500EBZ </wiki-migration/resources/fpga/xilinx/fmc/ad9434>` board                                                                                                |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9625-fmcadc2                 | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCADC2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>` board                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9739a-fmc                    | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :adi:`EVAL-AD9739A`                                                                                                                                                              |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-adrv9371                       | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`ADRV9371 </wiki-migration/resources/eval/user-guides/mykonos>` board                                                                                                       |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-adrv9375                       | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`ADRV9375 </wiki-migration/resources/eval/user-guides/mykonos>` board                                                                                                       |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcadc4                        | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCADC4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcadc4-ebz>` board                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcdaq2                        | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCDAQ2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>` board                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcdaq3                        | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCDAQ3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz>` board                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcjesdadc1                    | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | the on-board :adi:`ADV7511` and the :doc:`AD-FMCJESDADC1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcjesdadc1-ebz>` board                                                                                  |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-imageon                                | `ZC706 <https://www.xilinx.com/ZC706>`_                                       | FMC-IMAGEON                                                                                                                                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511                                  | `Zed Board <http://zedboard.org/product/zedboard>`_                           | the on-board :adi:`ADV7511`                                                                                                                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-ad9361-fmcomms2-3                | `Zed Board <http://zedboard.org/product/zedboard>`_                           | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-ad9364-fmcomms4                  | `Zed Board <http://zedboard.org/product/zedboard>`_                           | the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                        |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-ad9467-fmc-250ebz                | `Zed Board <http://zedboard.org/product/zedboard>`_                           | the on-board :adi:`ADV7511` and the :doc:`AD9467-FMC-250EBZ </wiki-migration/resources/eval/ad9467-fmc-250ebz>` board                                                                                                |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-cn0363                           | `Zed Board <http://zedboard.org/product/zedboard>`_                           | the on-board :adi:`ADV7511` and the :doc:`EVAL-CN0363-PMDZ </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz>` board                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-imageon                                  | `Zed Board <http://zedboard.org/product/zedboard>`_                           | FMC-IMAGEON                                                                                                                                                                                                          |
+---------------------------------------------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Building the device tree uses 'make' by turning the .dts file to a .dtb. The command is simply 'make' plus the device tree name with a .dtb file extension.

::

   dave@hal9000:~/github-linux-build/linux$ make zynq-zc702-adv7511-ad9361.dtb
     DTC     arch/arm/boot/dts/zynq-zc702-adv7511-ad9361.dtb
   dave@hal9000:~/github-linux-build/linux$

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **uImage** and **<device_tree_name>.dtb**. Refer to the code below to find their respective output directories. Take note that the device tree file needs to be renamed to **devicetree.dtb**. See :doc:`kuiper-linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` for more information in configuring the SD card.

::

   dave@hal9000:~/github-linux-build/linux$ cp arch/arm/boot/uImage /media/BOOT/uImage
   dave@hal9000:~/github-linux-build/linux$ cp arch/arm/boot/dts/zynq-zc702-adv7511-ad9361.dtb  /media/BOOT/devicetree.dtb

On the target platform
----------------------

Modifying devicetrees
~~~~~~~~~~~~~~~~~~~~~

1. Make sure the boot partition is mounted. On new images, this can be done by right-clicking the boot icon on the desktop and selecting the "Mount Volume" option. The partition will then be mounted at /media/analog/boot.

2. Convert the compiled devicetree related to the target back into an editable format.

::

   dave@hal9000:/media/analog/boot/zynq-zc702-adv7511$ dtc -I dtb -O dts -o devicetree.dts devicetree.dtb

3. Modify the devicetree.dts file as required.

4. Recompile the devicetree file. Note that this will overwrite the original dtb file, copy or rename the original file if you want to keep it before running this step.

::

   dave@hal9000:/media/analog/boot/zynq-zc702-adv7511$ dtc -I dts -O dtb -o devicetree.dtb devicetree.dts

Building the Zynq boot image
----------------------------

.. include:: ../../linux-software/build-the-zynq-boot-image.rst
