AD9081/AD9082 Virtex UltraScale+ VCU118 Quick Start Guide
=========================================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the :adi:`AD9081-FMCA-EBZ` or :adi:`AD9082-FMCA-EBZ` on the `VCU118 <https://www.xilinx.com/VCU118>`__ platform.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/hwsetup_vcu118_ad9081.jpg
   :align: center
   :width: 600px

Prerequisites
-------------

Required Hardware
~~~~~~~~~~~~~~~~~

-  Xilinx `VCU118 <https://www.xilinx.com/VCU118>`__ Rev 1.0 or later board
-  :adi:`AD9081-FMCA-EBZ` or :adi:`AD9082-FMCA-EBZ` board.
-  2 x Micro-USB cable
-  Ethernet cable
-  Signal generator
-  4 way splitter (optional)

Required Software
~~~~~~~~~~~~~~~~~

-  A Linux OS on a PC
-  Xilinx Vivado 2019.1 or later
-  UART terminal (e.g TeraTerm)
-  IIO-Oscilloscope :git-iio-oscilloscope:`Download <releases/latest>`

Downloads (Pre-build Images for VCU118)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   :doc:`microblaze_loading </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>`

Example Device Trees
~~~~~~~~~~~~~~~~~~~~

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                                 |
+==========+======================================================================================================================================================================================================+
| dtsi     | :git-linux:`arch/microblaze/boot/dts/adi-ad9081-fmc-ebz.dtsi`                                                                                                                                        |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081.dts`                                                                                                                                              |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_204c_txmode_10_rxmode_11.dts`                                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps.dts`                                                                                                        |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_204c_txmode_23_rxmode_25.dts`                                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps.dts`                                                                                                        |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_204c_txmode_23_rxmode_25_vcxo100.dts`                                                                                                             |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps.dts`                                                                                                        |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9081_m8_l4.dts`                                                                                                                                        |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_ad9082_204c_txmode_18_rxmode_19_lr_24_75Gbps.dts`                                                                                                        |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Board setup
~~~~~~~~~~~

.. include:: ../ad9081_fmca_ebz_hdl.rst

Steps
-----

1. Build the HDL project
~~~~~~~~~~~~~~~~~~~~~~~~

Before building the hdl project setup your computer based on the following guide: :doc:`Building HDL projects </wiki-migration/resources/fpga/docs/build>`

::

   git clone https://github.com/analogdevicesinc/hdl.git
   git checkout hdl_2019_r2;  // or latest release
   cd hdl/projects/ad9081_fmca_ebz/vcu118
   make

2. Build the Linux files
~~~~~~~~~~~~~~~~~~~~~~~~

Instructions on how to build the MicroBlaze Linux kernel and devicetrees from source can be found here:

-  :doc:`Linux on the MicroBlaze based Xilinx FPGA development Board </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze>`

::

   make simpleImage.vcu118_ad9081_m8_l4

.. tip::

   Latest released files can be downloaded from :doc:`here </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>`


3. Program the board
~~~~~~~~~~~~~~~~~~~~

| First we need to prepare a working directory where we will gather all the required binary files.
| From the HDL build directory locate the system_top.bit and copy it to the working directory. From the Linux build directory locate the simpleImage and copy it to the working directory.

::

   mkdir <working_dir>
   cp <hdl_repo_dir>/projects/ad9081_fmca_ebz_vcu118.runs/impl_1/system_top.bit  <working_dir>
   cp <linux_repo_dir>/arch/microblaze/boot/simpleImage.vcu118_ad9081_m8_l4.strip  <working_dir>

Next step is to program the board with xsct or similar tool. See generic instructions for programming the MicroBlaze bases systems here :doc:`Boot Kernel on FPGA Microblaze </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze>`

::

   xsct% connect
   xsct% fpga -f system_top.bit
   xsct% after 1000
   xsct% target 3
   xsct% dow simpleImage.vcu118_ad9081_m8_l4.strip
   xsct% after 1000
   xsct% con
   xsct% disconnect

.. tip::

   When using the downloaded archives, simply open xsdb and source ``run.tcl``\




.. raw:: html

   <details><summary>Complete Xilinx xsdb command log (Click to expand)</summary>

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      michael@mhenneri-D06:~/vcu118_ad9081_m8_l4$ xsdb
                                                                                                                                                                                                                 
      ****** Xilinx System Debugger (XSDB) v2019.1
        **** Build date : May 24 2019-15:06:52
          ** Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
   
      xsdb% source run.tcl                                                                                                                                                                                       
      attempting to launch hw_server                                                                                                                                                                             
                                                                                                                                                                                                                 
      ****** Xilinx hw_server v2019.1
        **** Build date : May 24 2019 at 15:06:40
          ** Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
   
      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application
   
      INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121
   
      100%   30MB   1.7MB/s  00:17                                                                                                                                                                               
      Downloading Program -- /home/michael/devel/pshare/AD9081/AD9081_FMCA_EBZ/vcu118_ad9081_m8_l4/simpleImage.vcu118_ad9081_m8_l4.strip                                                                         
          section, .text: 0x80000000 - 0x80510477
          section, __fdt_blob: 0x80510478 - 0x80520477
          section, .rodata: 0x80521000 - 0x809f63a7
          section, .pci_fixup: 0x809f63a8 - 0x809f8067
          section, .builtin_fw: 0x809f8068 - 0x809f808b
          section, __ksymtab: 0x809f808c - 0x80a02117
          section, __ksymtab_gpl: 0x80a02118 - 0x80a0a88f
          section, __ksymtab_strings: 0x80a0a890 - 0x80a27cfc
          section, __param: 0x80a27d00 - 0x80a282db
          section, __modver: 0x80a282dc - 0x80a28fff
          section, __ex_table: 0x80a29000 - 0x80a2a4ef
          section, .notes: 0x80a2a4f0 - 0x80a2a52b
          section, .sdata2: 0x80a2a52c - 0x80a2afff
          section, .data: 0x80a2b000 - 0x80ab879f
          section, .data..percpu: 0x80ab9000 - 0x80ab8fff
          section, .init.text: 0x80ab9000 - 0x80adf0f3
          section, .init.data: 0x80adf0f4 - 0x80ae1d93
          section, .init.ivt: 0x80ae1d94 - 0x80ae1dbb
          section, .init.setup: 0x80ae1dbc - 0x80ae219f
          section, .initcall.init: 0x80ae21a0 - 0x80ae263b
          section, .con_initcall.init: 0x80ae263c - 0x80ae263f
          section, .bss: 0x80ae3000 - 0x80b0992f
          section, .init.ramfs: 0x81000000 - 0x814bd74b
      100%   15MB   0.2MB/s  01:22                                                                                                                                                                               
      Setting PC to Program Start Address 0x80000000
      Successfully downloaded /home/michael/devel/pshare/AD9081/AD9081_FMCA_EBZ/vcu118_ad9081_m8_l4/simpleImage.vcu118_ad9081_m8_l4.strip
      Info: MicroBlaze #0 (target 3) Running                                                                                                                                                                     
      xsdb% Info: tcfchan#0 closed
      xsdb%

.. raw:: html

   </details>


Linux BOOT messages
^^^^^^^^^^^^^^^^^^^



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      Ramdisk addr 0x00000000, 
      Compiled-in FDT at 0x80510478
      earlycon: uartlite_a0 at MMIO 0x40600000 (options '115200n8')
      printk: bootconsole [uartlite_a0] enabled
      cma: Reserved 512 MiB at 0x8e000000
      Linux version 5.4.0-168125-g1d1209cdb0ce (michael@mhenneri-D06) (gcc version 7.3.1 20180425 (crosstool-NG 1.20.0)) #2837 Fri Mar 12 17:41:16 CET 2021
      setup_memory: max_mapnr: 0x7ffff
      setup_memory: min_low_pfn: 0x80000
      setup_memory: max_low_pfn: 0xb0000
      setup_memory: max_pfn: 0xfffff
      Zone ranges:
        DMA      [mem 0x0000000080000000-0x00000000afffffff]
        Normal   empty
        HighMem  [mem 0x00000000b0000000-0x00000000ffffefff]
      Movable zone start for each node
      Early memory node ranges
        node   0: [mem 0x0000000080000000-0x00000000ffffefff]
      Initmem setup node 0 [mem 0x0000000080000000-0x00000000ffffefff]
      setup_cpuinfo: initialising cpu 0
      setup_cpuinfo: Using full CPU PVR support
      wt_msr_noirq
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
      pcpu-alloc: [0] 0 
      Built 1 zonelists, mobility grouping on.  Total pages: 522751
      Kernel command line: earlycon
      Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      mem auto-init: stack:off, heap alloc:off, heap free:off
      Memory: 1538692K/2097148K available (5185K kernel code, 565K rwdata, 5152K rodata, 165K init, 154K bss, 34168K reserved, 524288K cma-reserved, 1310716K highmem)
      Kernel virtual memory layout:
        * 0xfffea000..0xfffff000  : fixmap
        * 0xff800000..0xffc00000  : highmem PTEs
        * 0xff7ff000..0xff800000  : early ioremap
        * 0xb0000000..0xff7ff000  : vmalloc & ioremap
      NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      irq-xilinx: mismatch in kind-of-intr param
      irq-xilinx: /amba_pl/interrupt-controller@41200000: num_irq=16, sw_irq=0, edge=0xffff05f0
      xilinx_timer_init: Timer base: 0xb0002000, Clocksource base: 0xb0002010
      clocksource: xilinx_clocksource: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      /amba_pl/timer@41c00000: irq=1, cpu_id 0
      xilinx_timer_shutdown
      xilinx_timer_set_periodic
      Calibrating delay loop... 49.35 BogoMIPS (lpj=246784)
      pid_max: default: 4096 minimum: 301
      Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      devtmpfs: initialized
      random: get_random_u32 called from bucket_table_alloc.isra.24+0x13c/0x170 with crng_init=0
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      futex hash table entries: 16 (order: -4, 448 bytes, linear)
      NET: Registered protocol family 16
      DMA: preallocated 256 KiB pool for atomic allocations
      PCI: Probing PCI hardware
      vgaarb: loaded
      jesd204: created con: id=0, topo=0, link=0, /amba_pl/axi_quad_spi@44a70000/hmc7044@1 <-> /amba_pl/axi-adxcvr-tx@44b60000
      jesd204: created con: id=1, topo=0, link=2, /amba_pl/axi_quad_spi@44a70000/hmc7044@1 <-> /amba_pl/axi-adxcvr-rx@44a60000
      jesd204: created con: id=2, topo=0, link=0, /amba_pl/axi-adxcvr-tx@44b60000 <-> /amba_pl/axi-jesd204-tx@44b90000
      jesd204: created con: id=3, topo=0, link=2, /amba_pl/axi-adxcvr-rx@44a60000 <-> /amba_pl/axi-jesd204-rx@44a90000
      jesd204: created con: id=4, topo=0, link=0, /amba_pl/axi-jesd204-tx@44b90000 <-> /amba_pl/axi-ad9081-tx-hpc@44b10000
      jesd204: created con: id=5, topo=0, link=2, /amba_pl/axi-jesd204-rx@44a90000 <-> /amba_pl/axi-ad9081-rx-hpc@44a10000
      jesd204: created con: id=6, topo=0, link=2, /amba_pl/axi-ad9081-rx-hpc@44a10000 <-> /amba_pl/axi_quad_spi@44a70000/ad9081@0
      jesd204: created con: id=7, topo=0, link=0, /amba_pl/axi-ad9081-tx-hpc@44b10000 <-> /amba_pl/axi_quad_spi@44a70000/ad9081@0
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0: JESD204[2] transition uninitialized -> initialized
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0: JESD204[0] transition uninitialized -> initialized
      jesd204: found 8 devices and 1 topologies
      clocksource: Switched to clocksource xilinx_clocksource
      NET: Registered protocol family 2
      tcp_listen_portaddr_hash hash table entries: 512 (order: 1, 12288 bytes, linear)
      TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      TCP bind hash table entries: 8192 (order: 5, 163840 bytes, linear)
      TCP: Hash tables configured (established 8192 bind 8192)
      UDP hash table entries: 512 (order: 2, 24576 bytes, linear)
      UDP-Lite hash table entries: 512 (order: 2, 24576 bytes, linear)
      NET: Registered protocol family 1
      RPC: Registered named UNIX socket transport module.
      RPC: Registered udp transport module.
      RPC: Registered tcp transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      PCI: CLS 0 bytes, default 32
      random: fast init done
      workingset: timestamp_bits=30 max_order=19 bucket_order=0
      Key type cifs.idmap registered
      jffs2: version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.
      romfs: ROMFS MTD (C) 2007 Red Hat, Inc.
      bounce: pool size: 64 pages
      io scheduler mq-deadline registered
      io scheduler kyber registered
      Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 5, base_baud = 0) is a uartlite
      printk: console [ttyUL0] enabled
      printk: console [ttyUL0] enabled
      printk: bootconsole [uartlite_a0] disabled
      printk: bootconsole [uartlite_a0] disabled
      uartlite 41400000.serial: IRQ index 0 not found
      brd: module loaded
      Xilinx SystemACE device driver, major=254
      libphy: Fixed MDIO Bus: probed
      xilinx_axienet 40c00000.ethernet: TX_CSUM 2
      xilinx_axienet 40c00000.ethernet: RX_CSUM 2
      xilinx_axienet 40c00000.ethernet: Failed to get clock: -2
      xilinx_axienet 40c00000.ethernet (unnamed net_device) (uninitialized): Setting assumed host clock to 100000000
      libphy: Xilinx Axi Ethernet MDIO: probed
      i2c /dev entries driver
      i2c i2c-0: Added multiplexed i2c bus 1
      i2c i2c-0: Added multiplexed i2c bus 2
      i2c i2c-0: Added multiplexed i2c bus 3
      at24 4-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
      i2c i2c-0: Added multiplexed i2c bus 4
      i2c i2c-0: Added multiplexed i2c bus 5
      i2c i2c-0: Added multiplexed i2c bus 6
      i2c i2c-0: Added multiplexed i2c bus 7
      i2c i2c-0: Added multiplexed i2c bus 8
      pca954x 0-0075: registered 8 multiplexed busses for I2C switch pca9548
      i2c i2c-0: Added multiplexed i2c bus 9
      i2c i2c-0: Added multiplexed i2c bus 10
      i2c i2c-0: Added multiplexed i2c bus 11
      i2c i2c-0: Added multiplexed i2c bus 12
      i2c i2c-0: Added multiplexed i2c bus 13
      i2c i2c-0: Added multiplexed i2c bus 14
      i2c i2c-0: Added multiplexed i2c bus 15
      i2c i2c-0: Added multiplexed i2c bus 16
      pca954x 0-0074: registered 8 multiplexed busses for I2C switch pca9548
      jesd204: /amba_pl/axi_quad_spi@44a70000/hmc7044@1,jesd204:0,parent=spi0.1: Using as SYSREF provider
      axi_adxcvr 44a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.01.a) using CPLL on GTY4 at 0x44A60000. Number of lanes: 4.
      axi_adxcvr 44b60000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.01.a) using QPLL on GTY4 at 0x44B60000. Number of lanes: 4.
      axi-jesd204-rx 44a90000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x44A90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
      axi-jesd204-tx 44b90000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0x44B90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
      axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      axi_sysid 45000000.axi-sysid-0: [ad9081_fmca_ebz] on [vcu118] git branch <(HEAD> git <e2a111d74bdcc055cc78409074346977a0f8452b> clean [2021-03-08 11:47:34] UTC
      NET: Registered protocol family 17
      Key type encrypted registered
      ad9081 spi0.0: AD9081 Rev. 3 Grade 10 (API 1.1.0) probed
      cf_axi_dds 44b10000.axi-ad9081-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x44B10000 mapped to 0x(ptrval), probed DDS AD9081
      cf_axi_adc 44a10000.axi-ad9081-rx-hpc: ADI AIM (10.01.b) at 0x44A10000 mapped to 0x(ptrval), probed ADC AD9081 as MASTER
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition initialized -> probed
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition initialized -> probed
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition probed -> idle
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition probed -> idle
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition idle -> device_init
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition idle -> device_init
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition device_init -> link_init
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition device_init -> link_init
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition link_init -> link_supported
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition link_init -> link_supported
      hmc7044 spi0.1: hmc7044_jesd204_link_pre_setup: Link2 forcing continuous SYSREF mode
      hmc7044 spi0.1: hmc7044_jesd204_link_pre_setup: Link0 forcing continuous SYSREF mode
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition link_supported -> link_pre_setup
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition link_supported -> link_pre_setup
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition link_pre_setup -> clk_sync_stage1
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition link_pre_setup -> clk_sync_stage1
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition clk_sync_stage1 -> clk_sync_stage2
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition clk_sync_stage1 -> clk_sync_stage2
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition clk_sync_stage2 -> clk_sync_stage3
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition clk_sync_stage2 -> clk_sync_stage3
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition clk_sync_stage3 -> link_setup
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition clk_sync_stage3 -> link_setup
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition link_setup -> opt_setup_stage1
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition link_setup -> opt_setup_stage1
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition opt_setup_stage1 -> opt_setup_stage2
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition opt_setup_stage1 -> opt_setup_stage2
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition opt_setup_stage2 -> opt_setup_stage3
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition opt_setup_stage2 -> opt_setup_stage3
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition opt_setup_stage3 -> opt_setup_stage4
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition opt_setup_stage3 -> opt_setup_stage4
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition opt_setup_stage4 -> opt_setup_stage5
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition opt_setup_stage4 -> opt_setup_stage5
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition opt_setup_stage5 -> clocks_enable
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition opt_setup_stage5 -> clocks_enable
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition clocks_enable -> link_enable
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition clocks_enable -> link_enable
      ad9081 spi0.0: JESD RX (JTX) Link2 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
      ad9081 spi0.0: JESD TX (JRX) Link0 0xF lanes in DATA
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition link_enable -> link_running
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition link_enable -> link_running
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[2] transition link_running -> opt_post_running_stage
      jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@0,jesd204:1,parent=spi0.0: JESD204[0] transition link_running -> opt_post_running_stage
      Freeing unused kernel memory: 164K
      This architecture does not have kernel memory protection.
      Run /init as init process
      Starting syslogd: OK
      Starting klogd: OK
      Running sysctl: OK
      Saving random seed: random: dd: uninitialized urandom read (512 bytes read)
      OK
      Starting network: udhcpc: started, v1.31.1
      net eth0: Promiscuous mode disabled.
      xilinx_axienet 40c00000.ethernet eth0: Setting assumed host clock to 100000000
      net eth0: Promiscuous mode disabled.
      net eth0: Speed other than 10, 100 
      net eth0: or 1Gbps is not supported
      xilinx_axienet 40c00000.ethernet eth0: Link is Down
      udhcpc: sending discover
      xilinx_axienet 40c00000.ethernet eth0: Link is Up - 1Gbps/Full - flow control off
      udhcpc: sending discover
      udhcpc: sending select for 10.44.3.51
      udhcpc: lease of 10.44.3.51 obtained, lease time 43200
      deleting routers
      adding dns 10.32.51.110
      adding dns 10.64.53.110
      Starting dropbear sshd: random: dropbear: uninitialized urandom read (32 bytes read)
      OK
      Starting IIO Server Daemon
   
      Welcome to Buildroot
      buildroot login: root
      Password: 
      #

.. raw:: html

   </details>


| 
| **Login Information**

-  user: root
-  password: analog

The following devices should be present:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **iio_info | grep iio:device**
              iio:device0: hmc7044
              iio:device1: axi-ad9081-tx-hpc (buffer capable)
              iio:device2: axi-ad9081-rx-hpc (buffer capable)
   


All links should be in ``DATA`` without errors:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **jesd_status -s**
        (DEVICES) Found 2 JESD204 Link Layer peripherals
   
        (0): axi-jesd204-rx/44a90000.axi-jesd204-rx  [*]
        (1): axi-jesd204-tx/44b90000.axi-jesd204-tx
   
        (STATUS)
        Link is                      enabled
        Link Status                  DATA
        Measured Link Clock (MHz)    249.998
        Reported Link Clock (MHz)    250.000
        Measured Device Clock (MHz)  250.000
        Reported Device Clock (MHz)  250.000
        Desired Device Clock (MHz)   250.000
        Lane rate (MHz)              10000.000
        Lane rate / 40 (MHz)         250.000
        LMFC rate (MHz)              7.812
        SYSREF captured              Yes
        SYSREF alignment error       No
        SYNC~
   
        (LANE STATUS)
        Lane#                             0      1      2      3
        Errors                            0      0      0      0
        Latency (Multiframes/Octets)      1/22   1/20   1/25   1/21
        CGS State                         DATA   DATA   DATA   DATA        
        Initial Frame Sync                Yes    Yes    Yes    Yes                           
        Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes
   


4. Connect to board with IIO Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the UART console find out the board IP address that was allocated by the DHCP server. If you do not use a DHCP server manually assign an IP to the board Ethernet port.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/iio_connect_noip.png
   :align: center

5. Capture data with IIO Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IIO Oscilloscope Remote
^^^^^^^^^^^^^^^^^^^^^^^

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used locally on FPGA platforms featuring a graphical desktop environment such as ZCU102 or ZC706, however for VCU118 we must use the remote network connection.

When using the remote option, once you logged in to the Linux terminal you need to check the IP address of the using the ifconfig command to see if there was any address assigned by a DHCP server. If not, you need to manually set an address with ifconfig in the same address space your PC is using.

Once the IIO Osc application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.


|image1|

.. include:: ../ad9081_iio_osc.rst AD9081 Plugin Description
------------------------------------------------------------

The AD9081 plugin works with the :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the AD9081 settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the AD9081 or the FPGA fabric) does not support that mode/precision.

If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the devices behind the back of the GUI, it's still possible to see the settings by clicking the ``Reload Settings`` button at the bottom of the GUI.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin.png
   :align: right
   :width: 400px

The AD9081 view is divided in three sections:

-  **Receive Chain**
-  **Transmit Chain**
-  **FPGA Settings**

--------------

Receive Chain
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin_rx.png
   :align: right
   :width: 300px

-  **ADC Rate(MHz):** Displays the ADC Sample Rate. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **ADC Nyquist Zone Control:** Selects the Nyquist Zone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Main NCO Frequency Control:** Controls the Main NCO. Frequency :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Main NCO Phase Control:** Controls the Main NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Channel NCO Frequency Control:** Controls the Channel NCO Frequency. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Channel NCO Phase Control:** Controls the Channel NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

--------------

Transmit Chain
~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin_tx.png
   :align: right
   :width: 300px

-  **DAC Rate(MHz):** Displays the DAC Sample Rate. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Main NCO Frequency Control:** Controls the Main NCO Frequency.\ :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Main NCO Phase Control:** Controls the Main NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Channel NCO Frequency Control:** Controls the Channel. NCO Frequency :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Channel NCO Phase Control:** Controls the Channel NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX NCO Channel Digital Gain:** Controls the Channel NCO digital gain. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX NCO Test Tone Modes:** Controls the Test Tone generation. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

--------------

FPGA Settings
~~~~~~~~~~~~~

Transmit/DDS
^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin_fpga.png
   :align: center
   :width: 600px

The plugin provides several options on how the transmitted data is generated.

It is possible to either use the built-in two tone **Direct Digital Synthesizer (DDS)** to transmit a bi-tonal signal on channels I and Q of the DAC. Or it is possible to use the **Direct Memory Access (DMA) facility** to transmit custom data that you have stored in a file.

This can be achieved by selecting one of the following options listed by the **DDS Mode**:

One CW Tone
^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/one_cw_tone.png
   :align: right

In **One CW Tone** mode one continuous wave (CW) tone will be outputted. The plugin displays the controls to set the Frequency, Amplitude and Phase for just one tone and makes sure that the amplitude of the other tone is set to 0. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Two CW Tone
^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/two_cw_tones.png
   :align: right

In **Two CW Tone** mode two continuous wave (CW) tones will be outputted. The plugin displays the controls to set the frequencies F1 and F2, amplitudes A1 and A2, phases P1 and P2 for the two tones. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Independent I/Q Control
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iq_independent.png
   :align: right

In **Independent I/Q Control** the plugin displays the controls to set the frequencies, amplitudes and phases for the two tones that will be outputted on channel I and additionally it allows for the two tones that will be outputted on channel Q of the DAC to be configured independently.

|

.. note::

   Note: The bi-tonal signal (T) is defined as the sum of two tones:

   | T(t) = A1 \* sin(2 \* p \* F1 \* t + P1) + A2 \* sin(2 \* p \* F2 \* t + P2),
   | where A-amplitude, F-frequency, P-phase of a tone.



DAC Buffer Output
^^^^^^^^^^^^^^^^^

|image1| The file selector under the **File Selection** section is used to locate and choose the desired data file. Under the **DAC Channels** section the enabled channels will be used to transmit the data stored in the file. To finalize the process, a click on the **Load** button is required.

| **Restrictions:**
| \* There are two types of files than can be loaded: **.txt** or **.mat**. The IIO-Oscilloscope comes with several :git-iio-oscilloscope:`data files <waveforms>` that can be used. If you want to create your own data files please take a look at the :doc:`Basic IQ Data Files </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>` documentation first.
| \* Due to hardware limitation only specific combinations of enabled channels are possible. You can enable a total of 1, 2, 4, etc. channels. If 1 channel is enabled then it can be any of them. If two channels are enabled then channels 0, 1 or channels 2, 3 can be enabled and so on.


Disable
^^^^^^^

| In this mode both DDS and DMA are disabled causing the DAC channels to stop transmitting any data.
|

.. note::

   Upon pressing **Reload Settings** button the values will be reloaded with the corresponding driver values. Useful in scenarios where the diver values get changed outside this plugin and a refresh on plugin's values is needed.


.. hint::

   Some plugin values will be rounded to the nearest value supported by the hardware.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/dac_output_buffer_panel.png


.. include:: ../common.rst .. include:: ../common.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/osc.png
