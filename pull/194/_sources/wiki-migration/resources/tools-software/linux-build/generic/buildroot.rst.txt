Building with buildroot
=======================

Aside from building the Linux kernel manually, there is also the possibility of building the ADI Linux kernel with :git-buildroot>`__.

Ideally, you should already be familiar with `buildroot <https::`the ADI buildroot repository </www.buildroot.org>`, but even if not, the steps in this guide should be pretty straight forward.

The starting point is to clone the ADI buildroot repository

::

   git clone https://github.com/analogdevicesinc/buildroot

Building for Microblaze
-----------------------

First make sure that the GNU toolchain for Microblaze is in the shell path.

Example:

::

   export PATH="/opt/Xilinx/Vitis/2021.2/gnu/microblaze/linux_toolchain/lin64_le/bin:$PATH"

.. important::

   \ **<fc #ff0000>Note:</fc>** There are 2 toolchains for GCC. The recommended ones, should be under **/opt/Xilinx/Vitis/2021.2/gnu/microblaze/linux_toolchain/**.

   
   And also make sure that the the directory to the Vivado Vitis is correct. The current example assumes that it is Vivado 2021.2 and it's installed in **/opt/Xilinx/**


Building for Microblaze - rootfs only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
   :alt: Root File-system

If building just the rootfs, go into the cloned buildroot directory

::

   cd <buildroot>
   make microblaze_adi_rootfs_defconfig
   make

Building for Microblaze - simpleImage.<board>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If building an entire simpleImage that can be ran on a board:

::

   cd <buildroot>
   make microblaze_adi_defconfig
   make BR2_LINUX_KERNEL_INTREE_DTS_NAME=kcu105_fmcdaq2

.. tip::

   \ **kcu105_fmcdaq2** is an example. Valid device-tree names can be found in :git-linux:`arch/microblaze/boot/dts` or in the list below


A list of supported images for Microblaze:

-  kc705
-  kc705_fmcdaq2
-  kc705_fmcjesdadc1
-  kc705_fmcomms1
-  kc705_fmcomms2-3
-  kc705_fmcomms4
-  kcu105_adrv9371x
-  kcu105
-  kcu105_fmcdaq2
-  kcu105_fmcdaq3
-  kcu105_fmcomms2-3
-  kcu105_fmcomms4
-  vc707_ad6676evb
-  vc707
-  vc707_fmcadc2
-  vc707_fmcadc5
-  vc707_fmcdaq2
-  vc707_fmcjesdadc1
-  vc707_fmcomms1
-  vc707_fmcomms2-3
-  vc707_fmcomms4

Building for Nios2
------------------

First make sure that the GNU toolchain for Nios2 is in the shell path.

Example:

::

   export PATH=/<your path>/CodeSourcery/Sourcery_CodeBench_Lite_for_Nios_II_GNU_Linux/bin/:$PATH

Building for Nios2 - rootfs only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://swdownloads.analog.com/cse/nios2/rootfs/rootfs.cpio.gz
   :alt: Root File-system

If building just the rootfs, go into the cloned buildroot directory

::

   cd <buildroot>
   make nios2_adi_rootfs_defconfig
   make

Building for Nios2 - zImage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If building an entire zImage that can be ran on a board:

::

   cd <buildroot>
   cp <rootfs-path> arch/nios2/boot/rootfs.cpio.gz
   make adi_nios2_defconfig
   make clean
   cp arch/nios2/boot/dts/a10gx_daq2.dts arch/nios2/boot/devicetree.dts
   make zImage

.. tip::

   \ **a10gx_daq2** is an example. Valid device-tree names can be found in :git-linux:`arch/nios2/boot/dts`\


Build output & device images
----------------------------

They are always present under:

::

   <path-to-buildroot>/output/images

For Microblaze it's **simpleImage.<board-name>** (example: **simpleImage.kcu105_fmcdaq2**)

For Nios2 it's zImage
