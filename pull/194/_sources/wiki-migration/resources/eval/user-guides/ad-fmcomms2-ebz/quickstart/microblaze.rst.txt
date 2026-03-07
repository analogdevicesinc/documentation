AD-FMCOMMS2-EBZ Microblaze Quick Start Guide
============================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS2-EBZ on:

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
-  AD-FMCOMMS2-EBZ or AD-FMCOMMS3-EBZ FMC Board.
-  Micro / Mini-USB Cable

Testing
=======

-  Connect the AD-FMCOMMS2-EBZ FMC board to the FPGA carrier, on the KC705:LPC FMC or VC707: FMC1 HPC connector.
-  Connect USB JTAG (Micro USB) to your host PC.
-  Turn on the power switch on the FPGA board.
-  Open XMD/XSCT/XSDB console to configure the FPGA and download the elf image.

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
   
      Ramdisk addr 0x00000000,
      Compiled-in FDT at 0x804763ac
      Linux version 4.19.0-g17f4223 (jenkins@romlxbuild1.adlk.analog.com) (gcc version 8.2.0 (crosstool-NG 1.20.0)) #1853 Tue Jul 27 13:32:24 IST 2021
      setup_memory: max_mapnr: 0x30000
      setup_memory: min_low_pfn: 0x80000
      setup_memory: max_low_pfn: 0xb0000
      setup_memory: max_pfn: 0xb0000
      Zone ranges:
        DMA      [mem 0x0000000080000000-0x00000000afffffff]
        Normal   empty
      Movable zone start for each node
      Early memory node ranges
        node   0: [mem 0x0000000080000000-0x00000000bfffffff]
      Initmem setup node 0 [mem 0x0000000080000000-0x00000000bfffffff]
      On node 0 totalpages: 196608
        DMA zone: 1536 pages used for memmap
        DMA zone: 0 pages reserved
        DMA zone: 196608 pages, LIFO batch:63
      setup_cpuinfo: initialising
      setup_cpuinfo: Using full CPU PVR support
      ERROR: Microblaze HW_MUL-different for PVR and DTS
      wt_msr_noirq
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
      pcpu-alloc: [0] 0
      Built 1 zonelists, mobility grouping on.  Total pages: 195072
      Kernel command line: console=ttyUL0,115200
      Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
      Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
      Memory: 766124K/786432K available (4568K kernel code, 510K rwdata, 4416K rodata, 2886K init, 92K bss, 20308K reserved, 0K cma-reserved)
      Kernel virtual memory layout:
        * 0xffffe000..0xfffff000  : fixmap
        * 0xffffe000..0xffffe000  : early ioremap
        * 0xb0000000..0xffffe000  : vmalloc & ioremap
      NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      irq-xilinx: mismatch in kind-of-intr param
      irq-xilinx: /amba_pl/interrupt-controller@41200000: num_irq=16, edge=0xffffc5de
      /amba_pl/timer@41c00000: irq=1
      clocksource: xilinx_clocksource: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      xilinx_timer_shutdown
      xilinx_timer_set_periodic
      sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      Calibrating delay loop... 49.35 BogoMIPS (lpj=246784)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
      Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
      devtmpfs: initialized
      random: get_random_u32 called from bucket_table_alloc.isra.6+0x1e8/0x218 with crng_init=0
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      futex hash table entries: 256 (order: -1, 3072 bytes)
      NET: Registered protocol family 16
      jesd204: found 0 devices and 0 topologies
      clocksource: Switched to clocksource xilinx_clocksource
      NET: Registered protocol family 2
      tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes)
      TCP established hash table entries: 8192 (order: 3, 32768 bytes)
      TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
      TCP: Hash tables configured (established 8192 bind 8192)
      UDP hash table entries: 512 (order: 1, 8192 bytes)
      UDP-Lite hash table entries: 512 (order: 1, 8192 bytes)
      NET: Registered protocol family 1
      RPC: Registered named UNIX socket transport module.
      RPC: Registered udp transport module.
      RPC: Registered tcp transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      random: fast init done
      Skipping unavailable RESET gpio -2 (reset)
      workingset: timestamp_bits=30 max_order=18 bucket_order=0
      jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
      io scheduler noop registered
      io scheduler deadline registered
      io scheduler cfq registered (default)
      io scheduler mq-deadline registered
      io scheduler kyber registered
      Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 4, base_baud = 0) is a uartlite
      console [ttyUL0] enabled
      brd: module loaded
      Xilinx SystemACE device driver, major=254
      60000000.flash: Found 1 x16 devices at 0x0 in 16-bit bank. Manufacturer ID 0x000089 Chip ID 0x008962
      NOR chip too large to fit in mapping. Attempting to cope...
      Intel/Sharp Extended Query Table at 0x010A
      Intel/Sharp Extended Query Table at 0x010A
      Intel/Sharp Extended Query Table at 0x010A
      Intel/Sharp Extended Query Table at 0x010A
      Intel/Sharp Extended Query Table at 0x010A
      Using buffer write method
      Using auto-unlock on power-up/resume
      cfi_cmdset_0001: Erase suspend on write enabled
      erase region 0: offset=0x0,size=0x20000,blocks=1023
      erase region 1: offset=0x7fe0000,size=0x8000,blocks=4
      Reducing visibility of 131072KiB chip to 32768KiB
      4 fixed-partitions partitions found on MTD device 60000000.flash
      Creating 4 MTD partitions on "60000000.flash":
      0x000000000000-0x000001380000 : "fpga"
      0x000001380000-0x000001400000 : "boot"
      0x000001400000-0x000001440000 : "bootenv"
      0x000001440000-0x000002000000 : "image"
      xilinx_spi 44a70000.axi_quad_spi: no CS gpios available
      libphy: Fixed MDIO Bus: probed
      xilinx_emaclite 40e00000.ethernet: Device Tree Probing
      libphy: Xilinx Emaclite MDIO: probed
      xilinx_emaclite 40e00000.ethernet: MAC address is now 00:0a:35:00:00:02
      xilinx_emaclite 40e00000.ethernet: Xilinx EmacLite at 0x40E00000 mapped to 0xB007A000, irq=2
      i2c /dev entries driver
      i2c i2c-0: Added multiplexed i2c bus 1
      i2c i2c-0: Added multiplexed i2c bus 2
      at24 3-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      i2c i2c-0: Added multiplexed i2c bus 3
      i2c i2c-0: Added multiplexed i2c bus 4
      i2c i2c-0: Added multiplexed i2c bus 5
      i2c i2c-0: Added multiplexed i2c bus 6
      i2c i2c-0: Added multiplexed i2c bus 7
      i2c i2c-0: Added multiplexed i2c bus 8
      pca954x 0-0074: registered 8 multiplexed busses for I2C switch pca9548
      ad9361 spi0.0: ad9361_probe : enter (ad9361)
      ad9361 spi0.0: ad9361_probe : AD936x Rev 2 successfully initialized
      cf_axi_dds 79024000.cf-ad9361-dds-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x79024000 mapped to 0x(ptrval), probed DDS AD9361
      axi_sysid 45000000.axi-sysid-0: [fmcomms2] on [kc705] git <43c6ae1ca9faf268f30c7ef489f1428fc30a8b23> clean [2021-06-09 21:38:35] UTC
      NET: Registered protocol family 17
      cf_axi_adc 79020000.cf-ad9361-lpc: ADI AIM (10.01.b) at 0x79020000 mapped to 0x(ptrval), probed ADC AD9361 as MASTER
      Freeing unused kernel memory: 2884K
      This architecture does not have kernel memory protection.
      Run /init as init process
      Starting logging: OK
      Initializing random number generator... random: dd: uninitialized urandom read (512 bytes read)
      done.
      Starting network: udhcpc: started, v1.27.2
      udhcpc: sending discover
      xilinx_emaclite 40e00000.ethernet eth0: Link is Down
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: no lease, failing
      Starting dropbear sshd: random: dropbear: uninitialized urandom read (32 bytes read)
      OK
      Starting IIO Server Daemon
   
      Welcome to Buildroot
      buildroot login: root
      Password:
      #
   


IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.
