AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ Microblaze Quick Start Guide
==========================================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ on:

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `VC707 <https://www.xilinx.com/VC707>`_

Required Software
-----------------

-  Bitfile and Linux ELF image.
-  Xilinx ISE Microprocessor Debugger (XMD) is sufficient for the demo.
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  Xilinx KC705 or KCU105 or VC707
-  AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ FMC Board.
-  Micro / Mini-USB Cable

Testing
=======

-  Connect the AD-FMCDAQ2-EBZ/AD-FMCDAQ3-EBZ FMC board to the FPGA carrier, on the HPC FMC connector.
-  Connect USB JTAG (Micro USB) to your host PC.
-  Turn on the power switch on the FPGA board.
-  Open XMD console to configure the FPGA and download the elf image.

Loading
-------

.. include:: ../../../../tools-software/linux-drivers/platforms/microblaze_loading.rst

Messages
--------

.. include:: ../../../../tools-software/linux-drivers/platforms/microblaze_loading.rst

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # Early console on uartlite at 0x40600000
      bootconsole [earlyser0] enabled
      Ramdisk addr 0x00000000, 
      Compiled-in FDT at 8031cda8
      Linux version 3.17.0-126658-g6807aea (michael@mhenneri-D04) (gcc version 4.8.3 20140131 (prerelease) (crosstool-NG 1.18.0) ) #1647 Fri Nov 21 10:33:05 CET 2014
      setup_cpuinfo: initialising
      setup_cpuinfo: Using full CPU PVR support
      wt_msr_noirq
      setup_memory: max_mapnr: 0x30000
      setup_memory: min_low_pfn: 0x80000
      setup_memory: max_low_pfn: 0xb0000
      setup_memory: max_pfn: 0xb0000
      Zone ranges:
        DMA      [mem 0x80000000-0xafffffff]
        Normal   empty
      Movable zone start for each node
      Early memory node ranges
        node   0: [mem 0x80000000-0xbfffffff]
      On node 0 totalpages: 196608
      free_area_init_node: node 0, pgdat 803fb104, node_mem_map 80800000
        DMA zone: 1536 pages used for memmap
        DMA zone: 0 pages reserved
        DMA zone: 196608 pages, LIFO batch:31
      early_printk_console remapping from 0x40600000 to 0xffffd000
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
      pcpu-alloc: [0] 0 
      Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 195072
      Kernel command line: console=ttyUL0,115200
      PID hash table entries: 4096 (order: 2, 16384 bytes)
      Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
      Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
      Memory: 771408K/786432K available (3187K kernel code, 143K rwdata, 708K rodata, 3061K init, 86K bss, 15024K reserved)
      Kernel virtual memory layout:
        * 0xffffe000..0xfffff000  : fixmap
        * 0xffffd000..0xffffe000  : early ioremap
        * 0xb0000000..0xffffd000  : vmalloc & ioremap
      NR_IRQS:128
      /axi@0/axi-intc@41200000: num_irq=15, edge=0x3810
      /axi@0/axi-timer@41c00000: irq=1
      xilinx_timer_set_mode: shutdown
      xilinx_timer_set_mode: periodic
      sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 42949672950ns
      Calibrating delay loop... 48.51 BogoMIPS (lpj=97024)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
      Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
      devtmpfs: initialized
      NET: Registered protocol family 16
      Switched to clocksource xilinx_clocksource
      xilinx_timer_set_mode: oneshot
      NET: Registered protocol family 2
      TCP established hash table entries: 8192 (order: 3, 32768 bytes)
      TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
      TCP: Hash tables configured (established 8192 bind 8192)
      TCP: reno registered
      UDP hash table entries: 512 (order: 1, 8192 bytes)
      UDP-Lite hash table entries: 512 (order: 1, 8192 bytes)
      NET: Registered protocol family 1
      RPC: Registered named UNIX socket transport module.
      RPC: Registered udp transport module.
      RPC: Registered tcp transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      XGpio: /axi@0/gpio@40000000: registered, base is 251
      XGpio: /axi@0/gpio@40000000: dual channel registered, base is 245
      XGpio: /axi@0/gpio@40020000: registered, base is 232
      XGpio: /axi@0/gpio@40020000: dual channel registered, base is 224
      Skipping unavailable RESET gpio -2 (reset)
      futex hash table entries: 256 (order: -1, 3072 bytes)
      jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      msgmni has been set to 1506
      Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
      io scheduler noop registered
      io scheduler deadline registered
      io scheduler cfq registered (default)
      Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 46, base_baud = 0) is a uartlite
      console [ttyUL0] enabled
      console [ttyUL0] enabled
      bootconsole [earlyser0] disabled
      bootconsole [earlyser0] disabled
      of_serial 41400000.serial: Unknown serial port found, ignored
      brd: module loaded
      Xilinx SystemACE device driver, major=254
      xilinx_lcd 40010000.gpio_lcd: Device Tree Probing 'gpio_lcd'
      xilinx_lcd 40010000.gpio_lcd: LCD 0x40010000 mapped to 0xb01a0000
      xilinx_spi 44a70000.axi-quad-spi: property name 'xlnx,num-ss-bits' is deprecated.
      xilinx_spi 44a70000.axi-quad-spi: at 0x44A70000 mapped to 0xb01c0000, irq=10
      libphy: Fixed MDIO Bus: probed
      xilinx_axienet 40e00000.network: TX_CSUM 0
      xilinx_axienet 40e00000.network: RX_CSUM 0
      libphy: Xilinx Axi Ethernet MDIO: probed
      i2c /dev entries driver
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.2: Driver ad9467 requests probe deferral
      platform 44a90000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      platform 44a91000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      platform 44a60000.axi-jesd-gt: Driver cf_axi_jesd204b_gt requests probe deferral
      ad9523 spi32766.0: probed ad9523-1
      platform 44a04000.axi-ad9144-hpc: Driver cf_axi_dds requests probe deferral
      ad9144 spi32766.1: Failed to get clocks
      spi spi32766.1: Driver ad9144 requests probe deferral
      TCP: cubic registered
      NET: Registered protocol family 17
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.2: Driver ad9467 requests probe deferral
      platform 44a90000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      platform 44a91000.jesd204: Driver cf_axi_jesd204b_v51 requests probe deferral
      cf_axi_jesd204b_gt 44a60000.axi-jesd-gt: AXI-JESD204B (5.00.b) at 0x44A60000 mapped to 0xb0280000,
      platform 44a04000.axi-ad9144-hpc: Driver cf_axi_dds requests probe deferral
      ad9144 spi32766.1: Failed to get clocks
      spi spi32766.1: Driver ad9144 requests probe deferral
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.2: Driver ad9467 requests probe deferral
      cf_axi_jesd204b_v51 44a90000.jesd204: AXI-JESD204B 5.2 Rev 1, at 0x44A90000 mapped to 0xb0032000,
      cf_axi_jesd204b_v51 44a91000.jesd204: AXI-JESD204B 5.2 Rev 1, at 0x44A91000 mapped to 0xb0034000,
      platform 44a04000.axi-ad9144-hpc: Driver cf_axi_dds requests probe deferral
      platform 44a10000.axi-ad9680-hpc: Driver cf_axi_adc requests probe deferral
      ad9467 spi32766.2: AD9680 PLL LOCKED
      cf_axi_dds 44a04000.axi-ad9144-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (8.00.b) at 0x44A04000 mapped to 0xb0098000, probed DDS AD9144
      cf_axi_adc 44a10000.axi-ad9680-hpc: ADI AIM (8.00.b) at 0x44A10000 mapped to 0xb02c0000, probed ADC AD9680 as MASTER
      Freeing unused kernel memory: 3060K (803fc000 - 806f9000)
      Starting logging: OK
      Starting network...
      Starting network...
      udhcpc (v1.22.1) started
      net eth0: Promiscuous mode disabled.
      net eth0: Promiscuous mode disabled.
      Sending discover...
      xilinx_axienet 40e00000.network eth0: Link is Down
      xilinx_axienet 40e00000.network eth0: Link is Up - 100Mbps/Full - flow control off
      Sending discover...
      Sending select for 10.44.2.94...
      Lease of 10.44.2.94 obtained, lease time 86400
      deleting routers
      adding dns 10.32.51.110
      adding dns 10.64.53.110
      Starting dropbear sshd: OK
      random: dropbear urandom read with 86 bits of entropy available
      Starting IIO Server Daemon
   
      Welcome to Buildroot
      buildroot login: root
      #
   


IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/connect.png
   :alt: Connect Window
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/plot_window.png
   :alt: Plot
   :align: center
   :width: 800px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/daq2_plugin.png
   :alt: DAQ2 plugin
   :align: center
   :width: 800px
