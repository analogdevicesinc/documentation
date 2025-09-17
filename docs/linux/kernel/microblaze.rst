.. _linux-kernel microblaze:

Build MicroBlaze Linux kernel
=============================

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
As the compiler, the Microblaze GNU Tools are included on both
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

The Microblaze GNU Toolchain included in AMD Vivado/Xilinx is the recommended
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
   xsdb> dow simpleImage.kcu105_fmcdaq2.strip
   xsdb> con
   xsdb> disconnect

To automate, the same commands can be added to a *.tcl* script and run with ``xsdb run.tcl``.

With ``xmd``:

::

   xmd> fpga -f system_top.bit
   xmd> connect mb mdm
   xmd> dow simpleImage.vc707_fmcomms2-3.strip
   xmd> run
