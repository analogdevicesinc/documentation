AD-FMCOMMS1-EBZ KC705/VC707 Quick Start Guide
=============================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS1-EBZ on:

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `VC707 <https://www.xilinx.com/VC707>`_

Required Software
-----------------

-  Bitfile and Linux ELF image.
-  Xilinx ISE Microprocessor Debugger (XMD) is sufficient for the demo.
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  Xilinx KC705 or VC707
-  AD-FMCOMMS1-EBZ FMC Board.
-  Micro / Mini-USB Cable

Testing
=======

-  Connect the AD-FMCOMMS1-EBZ FMC board to the FPGA carrier, on the KC705: FMC LPC or VC707: FMC2 connector.
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
   
      Early console on uartlite at 0x40600000
      bootconsole [earlyser0] enabled
      Ramdisk addr 0x00000000, 
      Compiled-in FDT at 80323fe8
      Linux version 3.17.0-126736-gdf1ca8f-dirty (michael@mhenneri-D04) (gcc version 4.8.3 20140131 (prerelease) (crosstool-NG 1.18.0) ) #1944 Wed Dec 17 11:03:31 CET 2014
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
      free_area_init_node: node 0, pgdat 8040751c, node_mem_map 81000000
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
      Memory: 768432K/786432K available (3215K kernel code, 148K rwdata, 724K rodata, 5988K init, 86K bss, 18000K reserved)
      Kernel virtual memory layout:
        * 0xffffe000..0xfffff000  : fixmap
        * 0xffffd000..0xffffe000  : early ioremap
        * 0xb0000000..0xffffd000  : vmalloc & ioremap
      NR_IRQS:128
      /axi@0/axi-intc@41200000: num_irq=32, edge=0xffff001e
      /axi@0/axi-timer@41c00000: irq=1
      xilinx_timer_set_mode: shutdown
      xilinx_timer_set_mode: periodic
      sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 42949672950ns
      Calibrating delay loop... 49.56 BogoMIPS (lpj=247808)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
      Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
      devtmpfs: initialized
      regulator-dummy: no parameters
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
      XGpio: /axi@0/gpio@40020000: registered, base is 247
      XGpio: /axi@0/gpio@40020000: dual channel registered, base is 239
      Skipping unavailable RESET gpio -2 (reset)
      futex hash table entries: 256 (order: -1, 3072 bytes)
      jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      msgmni has been set to 1500
      Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
      io scheduler noop registered
      io scheduler deadline registered
      io scheduler cfq registered (default)
      Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 4, base_baud = 0) is a uartlite
      console [ttyUL0] enabled
      console [ttyUL0] enabled
      bootconsole [earlyser0] disabled
      bootconsole [earlyser0] disabled
      of_serial 41400000.serial: FAILED to find out alias id
      of_serial 41400000.serial: Unknown serial port found, ignored
      brd: module loaded
      Xilinx SystemACE device driver, major=254
      xilinx_lcd 40010000.gpio_lcd: Device Tree Probing 'gpio_lcd'
      xilinx_lcd 40010000.gpio_lcd: LCD 0x40010000 mapped to 0xb0140000
      libphy: Fixed MDIO Bus: probed
      xilinx_emaclite 40e00000.network: Device Tree Probing
      libphy: Xilinx Emaclite MDIO: probed
      xilinx_emaclite 40e00000.network: MAC address is now 00:0a:35:00:00:07
      xilinx_emaclite 40e00000.network: Xilinx EmacLite at 0x40E00000 mapped to 0xB0034000, irq=2
      i2c /dev entries driver
      i2c i2c-0: Added multiplexed i2c bus 1
      i2c i2c-0: Added multiplexed i2c bus 2
      at24 3-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      at24 3-0054: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      i2c i2c-0: Added multiplexed i2c bus 3
      i2c i2c-0: Added multiplexed i2c bus 4
      i2c i2c-0: Added multiplexed i2c bus 5
      i2c i2c-0: Added multiplexed i2c bus 6
      i2c i2c-0: Added multiplexed i2c bus 7
      i2c i2c-0: Added multiplexed i2c bus 8
      pca954x 0-0074: registered 8 multiplexed busses for I2C switch pca9548
      platform 79020000.cf-ad9643-core-lpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.1: Driver ad9467 requests probe deferral
      spi32766.6 supply vcc not found, using dummy regulator
      spi32766.3 supply vcc not found, using dummy regulator
      ad9523 spi32766.3: probed ad9523-lpc
      ad9548 spi32766.2: Rev. 0xC6 probed
      spi32766.4 supply vcc not found, using dummy regulator
      spi32766.5 supply vcc not found, using dummy regulator
      platform 74204000.cf-ad9122-core-lpc: Driver cf_axi_dds requests probe deferral
      TCP: cubic registered
      NET: Registered protocol family 17
      platform 79020000.cf-ad9643-core-lpc: Driver cf_axi_adc requests probe deferral
      o|oo DCI 1
      cf_axi_dds 74204000.cf-ad9122-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (8.00.b) at 0x74204000 mapped to 0xb01a0000, probed DDS AD9122
      o--------------------------------
      -----ooooooooooo|oooooooooo------ INVERT DCO 0x8F CLK 245760000 Hz
      cf_axi_adc 79020000.cf-ad9643-core-lpc: ADI AIM (8.00.b) at 0x79020000 mapped to 0xb01c0000, probed ADC AD9643 as MASTER
      Freeing unused kernel memory: 5988K (80409000 - 809e2000)
      Starting logging: OK
      Starting network...
      Starting network...
      udhcpc (v1.22.1) started
      Sending discover...
      xilinx_emaclite 40e00000.network eth0: Link is Down
      Sending discover...
      xilinx_emaclite 40e00000.network eth0: Link is Up - 100Mbps/Full - flow control off
      Sending discover...
      Sending select for 10.44.2.146...
      Lease of 10.44.2.146 obtained, lease time 86400
      deleting routers
      adding dns 10.32.51.110
      adding dns 10.64.53.110
      random: ssh-keygen urandom read with 75 bits of entropy available
      Starting sshd: OK
      Starting IIO Server Daemon: OK
   
   
      Welcome to Buildroot
   
      buildroot login: random: nonblocking pool is initialized
   


IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.
