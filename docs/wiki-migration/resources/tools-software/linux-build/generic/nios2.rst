Build Linux - Script method
===========================

We provide `a script that does automates <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_nios2_kernel_image.sh>`_ the build for Nios 2.

The script takes 4 parameters:

-  **<path_to_nios2_toolchain>** - this is mandatory, since already built Nios 2 toolchains are not very common ; point this to the **nios2eds** directory [e.g. **/home/<user>/intelFPGA/<version>/nios2eds/bin/gnu/H-x86_64-pc-linux-gnu/bin/nios2-elf-** ]
-  **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this, if you want to use an already cloned kernel repo
-  **<altera_branch>** - default is **master** if left blank
-  **<devicetree_file>** - which device tree should be used for build; default is ``a10gx_adrv9371.dts``

The script will:

-  clone the ADI kernel tree
-  download the Linaro GCC toolchain [if no other is specified]
-  build the ADI kernel tree
-  export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line
------------------------------

::

   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_nios2_kernel_image.sh && chmod +x build_nios2_kernel_image.sh && ./build_nios2_kernel_image.sh /home/<user>/intelFPGA/<version>/nios2eds/bin/gnu/H-x86_64-pc-linux-gnu/bin/nios2-elf-

Build Linux - Step by Step Instructions
=======================================

Get Linux Kernel Source
-----------------------

.. container:: box bgblue

   
   ::
   
      user@pc:~/nios2$ git clone https://github.com/analogdevicesinc/linux.git
      Cloning into 'linux'...
      remote: Counting objects: 4331580, done.
      remote: Compressing objects: 100% (23/23), done.
      remote: Total 4331580 (delta 10), reused 5 (delta 5), pack-reused 4331552
      Receiving objects: 100% (4331580/4331580), 1.27 GiB | 1.88 MiB/s, done.
      Resolving deltas: 100% (3598928/3598928), done.
      Checking connectivity... done.
      Checking out files: 100% (49759/49759), done.
      user@pc:~/nios2$ 
   


Get Root Filesystem
-------------------

.. container:: box bgblue

   
   ::
   
      user@pc:~/nios2/linux$ wget https://swdownloads.analog.com/cse/nios2/rootfs/rootfs.cpio.gz -P arch/nios2/boot/rootfs.cpio.gz
      Resolving wiki.analog.com (wiki.analog.com)... 195.170.124.184
      Connecting to wiki.analog.com (wiki.analog.com)|195.170.124.184|:80... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 2786418 (2.7M) [application/octet-stream]
      Saving to: ‘arch/nios2/boot/rootfs.cpio.gz’
   
      arch/nios2/boot/rootfs.cpi 100%[=========================================>]   2.66M   111KB/s   in 20s
   
      2015-07-21 09:30:40 (134 KB/s) - ‘arch/nios2/boot/rootfs.cpio.gz’ saved [2786418/2786418]
   
      user@pc:~/nios2/linux$
   


Set Environmental Variables
---------------------------

.. container:: box bgblue

   
   ::
   
      user@pc:~/nios2/linux$ export ARCH=nios2
      user@pc:~/nios2/linux$ export CROSS_COMPILE=~/nios2/tools/bin/nios2-linux-gnu-
      user@pc:~/nios2/linux$
   


Configure Kernel for Nios2 Platforms
------------------------------------

.. container:: box bgblue

   
   ::
   
      user@pc:~/nios2/linux$ make adi_nios2_defconfig
      #
      # configuration written to .config
      #
      user@pc:~/nios2/linux$
   


Copy Corresponding Devicetree
-----------------------------

**your_setup.dts** is a generic file name - it should be replaced by the desired devicetree file name.

Valid options: **a5gt_fmcjesdadc1.dts** , **a10gx_daq2.dts** , **a10gx_daq3.dts**

.. container:: box bgblue

   
   ::
   
      user@pc:~/nios2/linux$ cp arch/nios2/boot/dts/your_setup.dts arch/nios2/boot/dts/devicetree.dts
      user@pc:~/nios2/linux$
   


Build Kernel
------------

.. container:: box bgblue

   
   ::
   
      user@pc:~/nios2/linux$ make zImage
      scripts/kconfig/conf --silentoldconfig Kconfig
        CHK     include/config/kernel.release
        WRAP    arch/nios2/include/generated/asm/atomic.h
      .......
        LD      arch/nios2/boot/compressed/vmlinux
        OBJCOPY arch/nios2/boot/zImage
      Kernel: arch/nios2/boot/zImage is ready
      user@pc:~/nios2/linux$ 
   

