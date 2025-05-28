.. _linux-kernel:

Kernel and devicetrees
""""""""""""""""""""""

.. toctree::
   :hidden:

   petalinux

This section provides a concise guide on building the Linux kernel and
devicetrees for different platforms on different hosts.

Jump to your platform and preferred method:

.. contents::
   :depth: 2
   :local:

.. _kernel-zynq:

Building the Zynq Linux kernel and devicetrees from source
==========================================================

Using a script
--------------

We provide
:git-wiki-scripts:`a script <raw+linux/build_zynq_kernel_image.sh>`
that does automates the build for Zynq using the Linaro toolchain.

The script takes up to 3 parameters, but if left blank, it uses defaults:

#. **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this,
   if you want to use an already cloned kernel repo
#. **<devicetree_file>** - which device tree should be exported/copied from the
   build. Default is ``zynq-zc702-adv7511-ad9361-fmcomms2-3.dtb`` for Zynq
#. **<path_to_other_toolchain>** - in case you have your own preferred toolchain
   (other than Linaro's or Xilinx's) you can use override it with this 3rd param

The script will:

* Clone the ADI kernel tree
* Download the Linaro GCC toolchain (if no other is specified)
* Build the ADI kernel tree
* Export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line, with defaults:

.. shell::

   $wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynq_kernel_image.sh && \
   $chmod +x build_zynq_kernel_image.sh && \
   $./build_zynq_kernel_image.sh

Building with Petalinux
-----------------------

Please see here: :ref:`linux-kernel petalinux`.

On the development host
-----------------------

Make sure you have ``u-boot-tools`` installed, to have the ``mkimage`` utility
available. You can install it via your distro's package manager.

Then

.. shell::

   $git clone https://github.com/analogdevicesinc/linux.git \
   $            --no-single-branch --depth=10 \
   $            -- linux

or do a git pull in a existing cloned repository.

The ``depth`` and ``no-single-branch`` options are included to speed up the
cloning by fetching only near the head of each branch/release, you may remove
them to fetch all history, but bear in mind it will go from around 800MB to
around 3.4GB and growing.

Checkout the Release branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Use the latest release, if not required otherwise!

The release branches have the format ``<Year>_R[1|2]``, starting from ``2014_R2``.

.. shell::

   $git checkout origin/2021_R1 -b 2021_R1
    Branch 2021_R1 set up to track remote branch 2021_R1 from origin.
    Switched to a new branch '2021_R1'

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few toolchains that can be used. The AMD Xilinx toolchain is
recommended, but the Linaro toolchain can also be used.

Other toolchains/compilers for ARM may work as well, but the ones described here
have been tested and found to work.

Using the AMD Xilinx toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   - - Release names and Branches
     - Required Vivado/Vitis versions
   - - 2014_R2
     - Vivado 2014.2
   - - 2015_R2
     - Vivado 2015.2
   - - 2016_R1
     - Vivado 2015.4.2
   - - 2016_R2
     - Vivado 2016.2
   - - 2017_R1
     - Vivado 2016.4
   - - 2018_R1
     - Vivado 2017.4
   - - 2018_R2
     - Vivado 2018.2
   - - 2019_R1
     - Vivado 2018.3
   - - 2019_R2
     - Vivado 2019.1
   - - 2021_R1
     - Vivado 2021.1

.. shell::

   $source $PATH_TO_XILINX/Vitis/$VITIS_VERSION/settings64.sh
   $which which arm-linux-gnueabihf-gcc
    $PATH_TO_XILINX/Vitis/$VITIS_VERSION/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin/arm-linux-gnueabihf-gcc

.. important::

   Find the path to the Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.

.. shell::

   $export ARCH=arm
   $export CROSS_COMPILE="arm-linux-gnueabihf-"

Using the Linaro toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Linaro toolchain/compiler can be used to compile to kernel.
Linaro compilers (that work with Zynq) can be downloaded from
`here <https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabi>`__.
Always use the latest release just in case.

.. shell::

   $wget https://releases.linaro.org/components/toolchain/binaries/latest-7/arm-linux-gnueabi/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi.tar.xz
   $tar -xvf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi.tar.xz

.. shell::

   $export ARCH=arm
   $export CROSS_COMPILE=$(pwd)/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabi/bin/arm-linux-gnueabi-

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the
kernel tree.
The command shown below is generic and is not project specific.
As long as the board is a ZYNQ FPGA, use the configuration below.

.. shell::

   $make zynq_xcomm_adv7511_defconfig
    #
    # configuration written to .config
    #

Build the kernel
~~~~~~~~~~~~~~~~

Build the kernel via 'make'. This is the same for all AMD Xilinx ZYNQ FPGAs.

.. shell::

   $make -j5 UIMAGE_LOADADDR=0x8000 uImage
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

Build the devicetree FCMOMMS2/3/4/5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card

.. list-table::
   :header-rows: 1

   - - device tree
     - board
     - chip
   - - zynq-adrv9361-z7035-bob
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-bob-cmos
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-packrf
     - :adi:`ADRV-PACKRF`
     - | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-fmc
     - :adi:`ADRV1CRR-FMC`
     - | :adi:`ADV7511` (on-board) and the
       | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-fmc-rfcard-tdd
     - :adi:`ADRV1CRR-FMC`
     - | :adi:`ADV7511` (on-board), the
       | :adi:`ADRV9361` and the
       | :adi:`AD-PZSDR2400TDD-EB`
   - - zynq-adrv9364-z7020-bob
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9364`
   - - zynq-adrv9364-z7020-bob-cmos
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9364`
   - - zynq-adrv9364-z7020-packrf
     - :adi:`ADRV-PACKRF`
     - | :adi:`ADRV9364`
   - - zynq-coraz7s
     - `Cora Z7`_
     - |
   - - zynq-mini-itx-adv7511
     - `Mini-ITX`_
     - | :adi:`ADV7511` (on-board)
   - - zynq-mini-itx-adv7511-ad9361-fmcomms2-3
     - `Mini-ITX`_
     - | :adi:`ADV7511` (on-board)
       | :dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>`
       | :dokuwiki:`AD-FMCOMMS3-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>`
   - - zynq-mini-itx-adv7511-ad9364-fmcomms4
     - `Mini-ITX`_
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>` board
   - - zynq-zc702-adv7511
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board)
   - - zynq-zc702-adv7511-ad9361-fmcomms2-3
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>` or
       | :dokuwiki:`AD-FMCOMMS3-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>` board
   - - zynq-zc702-adv7511-ad9361-fmcomms5
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS5-EBZ <resources/eval/user-guides/ad-fmcomms5-ebz>`
   - - zynq-zc702-adv7511-ad9364-fmcomms4
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>` board
   - - zynq-zc706-adv7511
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board)
   - - zynq-zc706-adv7511-ad6676-fmc
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD6676-FMC-EBZ <resources/eval/ad6676-wideband_rx_subsystem_ad6676ebz>` board
   - - zynq-zc706-adv7511-ad9265-fmc-125ebz
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD9265-FMC-125EBZ <resources/fpga/xilinx/fmc/ad9265>` board
   - - zynq-zc706-adv7511-ad9361-fmcomms2-3
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>` or
       | :dokuwiki:`AD-FMCOMMS3-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>` board
   - - zynq-zc706-adv7511-ad9361-fmcomms5
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS5-EBZ <resources/eval/user-guides/ad-fmcomms5-ebz>` board
   - - zynq-zc706-adv7511-ad9361-fmcomms5-ext-lo-adf5355
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS5-EBZ <resources/eval/user-guides/ad-fmcomms5-ebz>` board
   - - zynq-zc706-adv7511-ad9364-fmcomms4
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>` board
   - - zynq-zc706-adv7511-ad9434-fmc-500ebz
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD9434-FMC-500EBZ <resources/fpga/xilinx/fmc/ad9434>` board
   - - zynq-zc706-adv7511-ad9625-fmcadc2
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCADC2-EBZ <resources/eval/user-guides/ad-fmcdaq2-ebz>` board
   - - zynq-zc706-adv7511-ad9739a-fmc
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :adi:`EVAL-AD9739A`
   - - zynq-zc706-adv7511-adrv9371
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`ADRV9371 <resources/eval/user-guides/mykonos>` board
   - - zynq-zc706-adv7511-adrv9375
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`ADRV9375 <resources/eval/user-guides/mykonos>` board
   - - zynq-zc706-adv7511-fmcadc4
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCADC4-EBZ <resources/eval/user-guides/ad-fmcadc4-ebz>` board
   - - zynq-zc706-adv7511-fmcdaq2
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCDAQ2-EBZ <resources/eval/user-guides/ad-fmcdaq2-ebz>` board
   - - zynq-zc706-adv7511-fmcdaq3
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCDAQ3-EBZ <resources/eval/user-guides/ad-fmcdaq3-ebz>` board
   - - zynq-zc706-adv7511-fmcjesdadc1
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCJESDADC1-EBZ <resources/eval/user-guides/ad-fmcjesdadc1-ebz>` board
   - - zynq-zc706-imageon
     - :xilinx:`ZC706`
     - | FMC-IMAGEON
   - - zynq-zed-adv7511
     - `Zed Board <http://zedboard.org/product/zedboard>`__
     - :adi:`ADV7511` (on-board)
   - - zynq-zed-adv7511-ad9361-fmcomms2-3
     - `Zed Board <http://zedboard.org/product/zedboard>`__
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>` or
       | :dokuwiki:`AD-FMCOMMS3-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>` board
   - - zynq-zed-adv7511-ad9364-fmcomms4
     - `ZedBoard`_
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>` board
   - - zynq-zed-adv7511-ad9467-fmc-250ebz
     - `ZedBoard`_
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`AD9467-FMC-250EBZ <resources/eval/ad9467-fmc-250ebz>` board
   - - zynq-zed-adv7511-cn0363
     - `ZedBoard`_
     - | :adi:`ADV7511` (on-board) and the
       | :dokuwiki:`EVAL-CN0363-PMDZ <resources/eval/user-guides/eval-cn0363-pmdz>` board
   - - zynq-zed-imageon
     - `ZedBoard`_
     - | FMC-IMAGEON

.. _ZedBoard: https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard
.. _Mini-ITX: https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/mini-itx
.. _Cora Z7: https://digilent.com/reference/programmable-logic/cora-z7/start

Building the device tree uses 'make' by turning the .dts file to a .dtb. The
command is simply 'make' plus the device tree name with a .dtb file extension.

.. shell::

   $make zynq-zc702-adv7511-ad9361.dtb
    DTC     arch/arm/boot/dts/zynq-zc702-adv7511-ad9361.dtb

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **uImage** and
**<device_tree_name>.dtb**. Refer to the code below to find their respective
output directories. Take note that the device tree file needs to be renamed to
**devicetree.dtb**.
See :ref:`kuiper sdcard` for more information in configuring the SD card.

.. shell::

   $cp arch/arm/boot/uImage /media/BOOT/uImage
   $cp arch/arm/boot/dts/zynq-zc702-adv7511-ad9361.dtb  /media/BOOT/devicetree.dtb

On the target platform (devicetrees)
------------------------------------

To modify devicetrees on the target platform:

#. Make sure the boot partition is mounted. On new images, this can be done by
   right-clicking the boot icon on the desktop and selecting the "Mount Volume"
   option. The partition will then be mounted at */media/analog/boot*.

#. Convert the compiled devicetree related to the target back into an editable
   format.

   .. shell::

      $cd /media/analog/boot/zynq-zc702-adv7511
      $dtc -I dtb -O dts -o devicetree.dts devicetree.dtb


#. Modify the devicetree.dts file as required.

#. Recompile the devicetree file. Note that this will overwrite the original dtb
   file, copy or rename the original file if you want to keep it before running
   this step.

   .. shell::

      $cd /media/analog/boot/zynq-zc702-adv7511
      $dtc -I dts -O dtb -o devicetree.dtb devicetree.dts

.. _kernel-zynqmp:

Building the ZynqMP / MPSoC Linux kernel and devicetrees from source
====================================================================

Using a script
--------------

We provide
:git-wiki-scripts:`a script <raw+linux/build_zynqmp_kernel_image.sh>`
that does automates the build for Zynq using the Linaro toolchain.

.. attention::

   This script differs from the one for Zynq.

The script takes up to 3 parameters, but if left blank, it uses defaults:

#. **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this,
   if you want to use an already cloned kernel repo
#. **<devicetree_file>** - which device tree should be exported/copied from the
   build. Default is ``xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb`` for
   ZynqMP
#. **<path_to_other_toolchain>** - in case you have your own preferred toolchain
   (other than Linaro's or AMD Xilinx's) you can use override it with this 3rd paramameter

The script will:

* Clone the ADI kernel tree
* Download the Linaro GCC toolchain (if no other is specified)
* Build the ADI kernel tree
* Export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line, with defaults:

.. shell::

   $wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynqmp_kernel_image.sh && \
   $       chmod +x build_zynqmp_kernel_image.sh && \
   $       ./build_zynqmp_kernel_image.sh


Building with Petalinux
-----------------------

Please see here: :ref:`linux-kernel petalinux`.

On the development host
-----------------------

Make sure you have ``u-boot-tools`` installed, to have the ``mkimage`` utility
available. You can install it via your distro's package manager.

Then

.. shell::

   $git clone https://github.com/analogdevicesinc/linux.git \
   $            --no-single-branch --depth=10 \
   $            -- linux

or do a git pull in a existing cloned repository.

The ``depth`` and ``no-single-branch`` options are included to speed up the
cloning by fetching only near the head of each branch/release, you may remove
them to fetch all history, but bear in mind it will go from around 800MB to
around 3.4GB and growing.

Checkout the Release branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Use the latest release, if not required otherwise!

The release branches have the format ``<Year>_R[1|2]``, starting from ``2014_R2``.

.. shell::

   $git checkout origin/2021_R1 -b 2021_R1
    Branch 2021_R1 set up to track remote branch 2021_R1 from origin.
    Switched to a new branch '2021_R1'

Add aarch64-linux-gnu-gcc to PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the Xilinx toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   $source $PATH_TO_XILINX/Vitis/$VITIS_VERSION/settings64.sh
   $which aarch64-linux-gnu-gcc
    $PATH_TO_XILINX/Vitis/$VITIS_VERSION/gnu/aarch64/lin/aarch64-linux/bin/aarch64-linux-gnu-gcc

.. important::

   Find the path to the Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.

.. shell::

   $export ARCH=arm64
   $export CROSS_COMPILE="aarch64-linux-gnu-"

Using the Linaro toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Linaro toolchain/compiler can be used to compile to kernel.
Linaro compilers (that work with ZYNQMP) can be downloaded from
`here <https://releases.linaro.org/components/toolchain/binaries/latest-7/aarch64-linux-gnu>`__.
Always use the latest release just in case.

.. shell::

   $wget https://releases.linaro.org/components/toolchain/binaries/latest-7/aarch64-linux-gnu/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz
   $tar -xvf gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz

.. shell::

   $export ARCH=arm64
   $export CROSS_COMPILE=$(pwd)/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the
kernel tree.

.. shell::

   $make adi_zynqmp_defconfig
    #
    # configuration written to .config
    #

Build the kernel via 'make'. This is the same for all Xlinx ZYNQMP MPSoC FPGAs.

.. shell::

   $make -j5 Image UIMAGE_LOADADDR=0x8000
      CHK     include/config/kernel.release
      CHK     include/generated/uapi/linux/version.h
      HOSTCC  scripts/basic/fixdep
      HOSTCC  scripts/basic/bin2c

    [ -- snip --]

      CC      init/version.o
      LD      init/built-in.o
      KSYM    .tmp_kallsyms1.o
      KSYM    .tmp_kallsyms2.o
      LD      vmlinux
      SORTEX  vmlinux
      SYSMAP  System.map
      OBJCOPY arch/arm64/boot/Image

Build the devicetree FCMOMMS2/3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card

.. list-table::
   :header-rows: 1

   - - device tree
     - board
     - chip
   - - zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dts
     - :xilinx:`ZCU102` **Rev. 1.0**
     - | :dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>` or
       | :dokuwiki:`AD-FMCOMMS3-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>` board
   - - zynqmp-zcu102-rev10-ad9364-fmcomms4.dts
     - :xilinx:`ZCU102` **Rev. 1.0**
     - | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>` or
       | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>` board
   - - zynqmp-zcu102-revB-ad9361-fmcomms2-3.dts
     - :xilinx:`ZCU102` Rev.B
     - | :dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>` or
       | :dokuwiki:`AD-FMCOMMS3-EBZ <resources/eval/user-guides/ad-fmcomms3-ebz>` board
   - - zynqmp-zcu102-revB-ad9364-fmcomms4.dts
     - :xilinx:`ZCU102` Rev.B
     - | :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>` board

The device tree **zynqmp-zcu102-revA.dts** can also be used for any ZCU102 FPGA
that uses an SD card for boot up. Building the device tree uses 'make' by
turning the .dts file to a .dtb. The command is simply 'make' plus the device
tree name with a .dtb file extension.

.. shell::

   $make xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb
    DTC     arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **uImage** and
**<device_tree_name>.dtb**. Refer to the code below to find their respective
output directories. Take note that the device tree file needs to be renamed to
**devicetree.dtb**.
See :ref:`kuiper sdcard` for more information in configuring the SD card.

.. shell::

   $cp arch/arm64/boot/Image /media/michael/BOOT/
   $cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-revB-ad9361-fmcomms2-3.dtb /media/michael/BOOT/system.dtb

Common Issues
-------------

This sections goes through common issues related to the Linux Kernel on the
ZynqMP.

DisplayPort - no picture?
~~~~~~~~~~~~~~~~~~~~~~~~~

The default configuration for most of the projects is to use the HDMI output,
and that is what the configuration is set up for.

For DisplayPort projects, you may need to add a custom ``xorg.conf`` file.

.. code:: bash

   printf 'Section "Device"
     Identifier "myfb"
     Driver "fbdev"
     Option "fbdev" "/dev/fb0"
   EndSection' > /etc/X11/xorg.conf

After following that, the board should be rebooted.

You can find a list with tested monitors
:xilinx:`here <support/answers/68671.html>`.
Resolution or image problems may appear if there is used a monitor that was not
tested.

.. _kernel-microblaze:

Building the MicroBlaze Linux kernel and devicetrees from source
================================================================

On the development host
-----------------------

This guide provides some step-by-step instructions on how to build a Microblaze
Linux Kernel image for the FMC board connected to a:

* :xilinx:`KC705`
* :xilinx:`KCU105`
* :xilinx:`VC707`
* :xilinx:`VCU118`
* :xilinx:`VCU128`

The :git-linux:`/` contains the Linux Kernel flavor from Analog Devices Inc.
:download:`rootfs.cpio.gz <https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz>`
contains the files system to be used.
As the compiler, the Microblaze GNU Tools are bumbled on both
:xilinx:`AMD Vivado <en/products/software/adaptive-socs-and-fpgas/vivado.html>` and
:xilinx:`AMD Vivis <en/products/software/adaptive-socs-and-fpgas/vivado.html>`, as well
as the ``xsdb`` tool for booting.

After ensuring all tools are installed, clone the :git-linux:`/`

.. shell::

   $git clone https://github.com/analogdevicesinc/linux.git \
   $            --no-single-branch --depth=10 \
   $            -- linux

The ``depth`` and ``no-single-branch`` options are included to speed up the
cloning by fetching only near the head of each branch/release, you may remove
them to fetch all history, but bear in mind it will go from around 800 MB to
around 3.4GB and growing.

Checkout the Release branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Use the latest release, if not required otherwise!

The release branches have the format ``<Year>_R[1|2]``, starting from ``2014_R2``.

.. shell::

   $git checkout origin/2021_R1 -b 2021_R1
    Branch 2021_R1 set up to track remote branch 2021_R1 from origin.
    Switched to a new branch '2021_R1'

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Microblaze GNU Toolchain bumbled in AMD Vivado/Xilinx is the recommended
compiler.

/data/opt/Xilinx/Vitis/$XVERSION/gnu/microblaze/linux_toolchain/lin64_le/bin/

.. shell::

   $XVERSION=2024.2
   $GCC_MICROBLAZE=$PATH_TO_XILINX/Vits/$VITIS_VERSION/gnu/microblaze/linux_toolchain/lin64_le/bin/
   $export ARCH=microblaze
   $export CROSS_COMPILE="$GCC_MICROBLAZE/microblazeel-xilinx-linux-gnu-"

.. important::

   Find the path to the Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.
   Alternatively, you can replace Vitis with Vivado.

Compile the kernel
~~~~~~~~~~~~~~~~~~

Prepare the configuration:

.. shell::

   ~/linux
   $make adi_mb_defconfig
    #
    # configuration written to .config
    #

Download the rootfs:

.. shell::

   ~/linux
   $wget https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
     Saving to: ‘rootfs.cpio.gz’
     rootfs.cpio.gz    100%[======================>]   4.74M  6.39MB/s    in 0.7s
     2025-05-28 11:00:09 (6.39 MB/s) - ‘rootfs.cpio.gz’ saved [4970267/4970267]


The result of building the kernel is an elf file in *arch/microblaze/boot* named
`simpleImage.<dts-file>` based on the dts specified.

The build process for the kernel searches in the *arch/microblaze/boot/dts*
directory for a specified device tree file and then builds the device tree into
the kernel image.

The following command shows the general format for the build target name. Note
that the *<dts-file>* does not include the file extension *.dts*.

.. shell::

   ~/linux
   $make simpleImage.<dts-file>

To see what device-trees for the different FPGA carrier and FMC module combination exist type:

.. shell::

   ~/linux
   $ls -l arch/microblaze/boot/dts

So, for example, for *vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.dts*:

.. shell::

   ~/linux
   $make simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
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

The STRIP image (*.strip*) found under *arch/microblaze/boot* is the ELF image
to load via the debugger.

Boot on FPGA MicroBlaze
~~~~~~~~~~~~~~~~~~~~~~~

One method to load the kernel onto the already built and running FPGA which has
the MicroBlaze processor is to use ``xsdb``/``xsct`` or ``xmd`` from the AMD
Xilinx Vivado/Vitis toolset to download the build *.strip* file.

Go to the folder containing the *.strip* and *system_top.bit* file, to flash the
bitstream and download the Image.

.. note::

   The **system_top.bit** is obtained from the HDL project.
   Learn how to :external+hdl:ref:`build_hdl`, but instead of using the generated
   **\*.sdk/system_top.xsa**, use the **\*.runs/impl_1/system_top.bit**.

With ``xsdb``/``xsct``:

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
   xsdb> disconnect

To automate, the same commands can be added to a *.tcl* script and run with ``xsdb run.tcl``.

With ``xmd``:

::

   xmd> fpga -f system_top.bit
   xmd> connect mb mdm
   xmd> dow simpleImage.vc707_fmcomms2-3
   xmd> run

