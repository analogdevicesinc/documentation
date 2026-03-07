Building the ZynqMP / MPSoC Linux kernel and devicetrees from source
====================================================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/linux/kernel/zynqmp.html


The script method
-----------------

We provide `a script that does automates <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynqmp_kernel_image.sh>`_ the build for ZynqMP using the Linaro toolchain.

<fc #ff0000>\ **Note**\ </fc> that this script differs from the one for Zynq.

The script takes up to 3 parameters, but if left blank, it uses defaults:

-  **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this, if you want to use an already cloned kernel repo
-  **<devicetree_file>** - which device tree should be exported/copied from the build ; default is ``zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb`` for Zynq
-  **<path_to_other_toolchain>** - in case you have your own preferred ARM64 toolchain [other than Linaro's or Xilinx's] you can use override it with this 3rd param

The script will:

-  clone the ADI kernel tree
-  download the Linaro GCC toolchain [if no other is specified]
-  build the ADI kernel tree
-  export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line [with defaults]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynqmp_kernel_image.sh && chmod +x build_zynqmp_kernel_image.sh && ./build_zynqmp_kernel_image.sh zynqmp

Building using Petalinux
------------------------

Please see here: :doc:`Building with Petalinux </wiki-migration/resources/tools-software/linux-build/generic/petalinux>`

On the development host
-----------------------

Create a local copy of ADI's kernel tree. From now on, we will be working in this "linux" folder, the :git-linux>`__.

::

   user@analog:~$ git clone https::`ADI Linux repository </github.com/analogdevicesinc/linux.git
   user@analog:~$ cd linux/

or do a git pull in an existing repository.

Checkout the main development/main branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   linux$ git checkout main
   Already on 'main'
   Your branch is up-to-date with 'origin/main'.

Add aarch64-linux-gnu-gcc to PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AMD Xilinx Vivado & Vitis 2023.2 may be installed into a different directory.

::

   linux$ export PATH=$PATH:/opt/Xilinx/Vitis/2023.2/gnu/aarch64/lin/aarch64-linux/bin

Other toolchains/compilers for ARM may work as well, but the ones described here have been tested and found to work.

Using the Linaro toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Linaro toolchain/compiler can be used to compile to kernel. Linaro compilers (that work with ZYNQMP) can be downloaded from: https://releases.linaro.org/components/toolchain/binaries/latest-7/aarch64-linux-gnu/ . Always use the latest release just in case.

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   linux$ export ARCH=arm64
   linux$ export CROSS_COMPILE="/opt/Xilinx/Vitis/2023.2/gnu/aarch64/lin/aarch64-linux/bin/aarch64-linux-gnu-"

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the kernel tree.

::

   linux$ make adi_zynqmp_defconfig 
   #
   # configuration written to .config
   #
   linux$

Build the kernel
~~~~~~~~~~~~~~~~

Build the kernel via 'make'. This is the same for all AMD Xilinx ZynqMP UltraScale+ FPGAs. The "-j4" represents the number of threads on which this process should run. This build takes about 10-15 minutes, depending on the capabilities of your PC.

::

   linux$ make -j4 Image UIMAGE_LOADADDR=0x8000
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
   linux$

Build the devicetree FCMOMMS2/3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| device tree                               | board                                                                                                                                                                                                                                           |
+===========================================+=================================================================================================================================================================================================================================================+
| zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dts | `ZCU102 <https://www.xilinx.com/ZCU102>` **Rev. 1.0** and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board  |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-rev10-ad9364-fmcomms4.dts   | `ZCU102 <https://www.xilinx.com/ZCU102>`_ **Rev. 1.0** and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` or :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-revB-ad9361-fmcomms2-3.dts  | `ZCU102 <https://www.xilinx.com/ZCU102>`_ Rev.B and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board        |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-revB-ad9364-fmcomms4.dts    | `ZCU102 <https://www.xilinx.com/ZCU102>`_ Rev.B and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                               |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The device tree **zynqmp-zcu102-revA.dts** can also be used for any ZCU102 FPGA that uses an SD card for boot up. Building the device tree uses 'make' by turning the .dts file to a .dtb. The command is simply 'make' plus the device tree name with a .dtb file extension.

::

   linux$  make xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb
     DTC     arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **Image** and **<device_tree_name>.dtb**. Refer to the code below to find their respective output directories. The device tree file needs to be renamed to **system.dtb**. See :doc:`kuiper-linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` for more information in configuring the SD card.

::

   linux$ cp arch/arm64/boot/Image /media/michael/BOOT/
   linux$ cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-revB-ad9361-fmcomms2-3.dtb /media/michael/BOOT/system.dtb

Building the ZynqMP boot image
------------------------------

.. include:: ../../linux-software/build-the-zynqmp-boot-image.rst

DisplayPort - no picture?
-------------------------

The default configuration for most of the projects is to use the HDMI output, and that is what the configuration is set up for.

For DisplayPort projects, you may need to add a custom ``xorg.conf`` file.

::

   root@analog:~# printf "Section \"Device\"\n  Identifier \"myfb\"\n  Driver \"fbdev\"\n  Option \"fbdev\" \"/dev/fb0\"\nEndSection\n" > /etc/X11/xorg.conf
   root@analog:~# cat /etc/X11/xorg.conf 
   Section "Device"
     Identifier "myfb"
     Driver "fbdev"
     Option "fbdev" "/dev/fb0"
   EndSection

After following that, the board should be rebooted.

You can find a list with tested monitors `here <https://www.xilinx.com/support/answers/68671.html>`_. Resolution or image problems may appear if there is used a monitor that was not tested.
