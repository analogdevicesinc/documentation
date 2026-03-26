.. _fmcomms2 quickstart microblaze:

Microblaze Quickstart (Obsolete)
===============================================================================

This guide provides quick instructions on how to setup the
 :adi:`EVAL-AD-FMCOMMS2` on:

- :xilinx:`KC705` on LPC FMC
- :xilinx:`VC707` on FMC1 HPC

Using Linux as software
-------------------------------------------------------------------------------

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Bitfile and Linux ELF image
- Xilinx XSCT/XSDB console (or legacy XMD) for programming
- A UART terminal (Tera Term/Putty/Minicom), baud rate 115200 (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :xilinx:`KC705` or :xilinx:`VC707` FPGA board
- AD-FMCOMMS2-EBZ or AD-FMCOMMS3-EBZ FMC board
- Micro / Mini-USB cable

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. esd-warning::

#. Connect the AD-FMCOMMS2-EBZ FMC board to the FPGA carrier
   (KC705: LPC FMC, VC707: FMC1 HPC connector)
#. Connect USB JTAG (Micro USB) to your host PC
#. Turn on the power switch on the FPGA board
#. Open XMD/XSCT/XSDB console to configure the FPGA and download
   the ELF image

Loading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are several ways to load the design onto the FPGA.

**Method 1: Using XMD command line (legacy)**

.. collapsible:: XMD example (click to expand)

   ::

      Dave@HAL9000:~$ xmd

      * Xilinx Microprocessor Debugger (XMD) Engine
      * XMD v2014.2 (64-bit)
        *** SW Build 932637 on Wed Jun 11 13:12:06 MDT 2014
          ** Copyright 1986-2014 Xilinx, Inc. All Rights Reserved.

      XMD% fpga -f download.bit
      Configuring Device 1 (xcku040) with Bitstream -- download.bit
      ....10....20....30....40....50....60.....70....80....90....Done
      Successfully downloaded bit file.

      JTAG chain configuration
      Device   ID Code        IR Length    Part Name
       1       03822093           6        xcku040

      0
      XMD% connect mb mdm

      JTAG chain configuration
      Device   ID Code        IR Length    Part Name
       1       03822093           6        xcku040

      MicroBlaze Processor Configuration :
      Version............................9.3
      Optimization.......................Performance
      Interconnect.......................AXI-LE
      MMU Type...........................Full_MMU
      No of PC Breakpoints...............1
      No of Read Addr/Data Watchpoints...0
      No of Write Addr/Data Watchpoints..0
      Instruction Cache Support..........on
      Instruction Cache Base Address.....0x80000000
      Instruction Cache High Address.....0xbfffffff
      Data Cache Support.................on
      Data Cache Base Address............0x80000000
      Data Cache High Address............0xbfffffff
      Exceptions  Support................on
      FPU  Support.......................off
      Hard Divider Support...............on
      Hard Multiplier Support............on - (Mul64)
      Barrel Shifter Support.............on
      MSR clr/set Instruction Support....on
      Compare Instruction Support........on
      PVR Supported......................on
      PVR Configuration Type.............Full
      Data Cache Write-back Support......off
      Fault Tolerance Support............off
      Stack Protection Support...........off

      Connected to "mb" target. id = 0
      Starting GDB server for "mb" target (id = 0) at TCP port no 1234

      XMD% dow /home/dace/linux/arch/microblaze/boot/simpleImage.kcu105_ad_fmcdaq2_ebz
      System Reset .... DONE
      Downloading Program -- /home/michael/linux/arch/microblaze/boot/simpleImage.kcu105_ad_fmcdaq2_ebz
          section, .text: 0x80000000-0x8031cda7
          section, .init.text: 0x803fc000-0x804185eb
          section, .init.ivt: 0x8041afac-0x8041afd3
          section, __fdt_blob: 0x8031cda8-0x80324da7
          section, .rodata: 0x80325000-0x803b950f
          section, __ksymtab: 0x803b9510-0x803be90f
          section, __ksymtab_gpl: 0x803be910-0x803c1e27
          section, __ksymtab_strings: 0x803c1e28-0x803d4dd7
          section, __param: 0x803d4dd8-0x803d5147
          section, __modver: 0x803d5148-0x803d5fff
          section, __ex_table: 0x803d6000-0x803d75df
          section, .notes: 0x803d75e0-0x803d7603
          section, .sdata2: 0x803d7604-0x803d7fff
          section, .data: 0x803d8000-0x803fbc5f
          section, .init.data: 0x804185ec-0x8041afab
          section, .init.setup: 0x8041afd4-0x8041b327
          section, .initcall.init: 0x8041b328-0x8041b683
          section, .con_initcall.init: 0x8041b684-0x8041b68b
          section, .init.ramfs: 0x8041b68c-0x806f97b3
          section, .bss: 0x806fa000-0x8070f8db
      Download Progress........10.......20.......30.......40.......50........60.......70.......80.......90........Done
      Setting PC with Program Start Address 0x80000000
      XMD% con
      Processor started. Type "stop" to stop processor

      RUNNING> XMD%

**Method 2: Using XSCT/XSDB command line**

XMD has been replaced with XSCT/XSDB in newer releases of Vivado.
In Windows, you can run the XSCT terminal from Start menu -> Xilinx
Design Tools -> Xilinx Software Command Line Tool.

.. collapsible:: XSCT example (click to expand)

   ::

      * Xilinx System Debugger (XSDB) v2021.1
        *** Build date : Jun 10 2021-20:11:58
          ** Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.


      xsdb% connect
      attempting to launch hw_server

      * Xilinx hw_server v2021.1
        *** Build date : Jun 10 2021 at 20:11:57
          ** Copyright 1986-2021 Xilinx, Inc. All Rights Reserved.

      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application

      INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121

      tcfchan#0
      xsdb% fpga -f system_top.bit
      100%    4MB   1.7MB/s  00:02
      xsdb% targets
        1  xc7k325t
           2  MicroBlaze Debug Module at USER2
              3  MicroBlaze #0 (Running)
      xsdb% target 3
      xsdb% dow simpleImage.kc705_fmcomms2-3.strip
      Downloading Program -- /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
              section, .text: 0x80000000 - 0x804763ab
              section, __fdt_blob: 0x804763ac - 0x804863ab
              section, .rodata: 0x80487000 - 0x808b110f
              section, .builtin_fw: 0x808b1110 - 0x808b1133
              section, __ksymtab: 0x808b1134 - 0x808b746b
              section, __ksymtab_gpl: 0x808b746c - 0x808bc483
              section, __ksymtab_strings: 0x808bc484 - 0x808d6973
              section, __param: 0x808d6974 - 0x808d6e5f
              section, __modver: 0x808d6e60 - 0x808d6fff
              section, __ex_table: 0x808d7000 - 0x808d844f
              section, .notes: 0x808d8450 - 0x808d848b
              section, .sdata2: 0x808d848c - 0x808d8fff
              section, .data: 0x808d9000 - 0x8095893f
              section, .init.text: 0x80959000 - 0x8097a75b
              section, .init.data: 0x8097a75c - 0x8097c053
              section, .init.ivt: 0x8097c054 - 0x8097c07b
              section, .init.setup: 0x8097c07c - 0x8097c3f3
              section, .initcall.init: 0x8097c3f4 - 0x8097c80f
              section, .con_initcall.init: 0x8097c810 - 0x8097c813
              section, .init.ramfs: 0x8097c814 - 0x80c2a9fb
              section, .bss: 0x80c2b000 - 0x80c4225b
      100%   12MB   0.2MB/s  00:56
      Setting PC to Program Start Address 0x80000000
      Successfully downloaded /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
      xsdb% Info: MicroBlaze #0 (target 3) Stopped at 0x0 (Stop)
      xsdb% con
      Info: MicroBlaze #0 (target 3) Running
      xsdb%

**Method 3: Using TCL script**

Run Vivado TCL Shell from Windows Start menu -> Xilinx Design Suite
-> Vivado -> Vivado TCL Shell. In Linux, source the ``settings.sh``
file first, then run the TCL script:

.. collapsible:: TCL script example (click to expand)

   ::

      * Xilinx System Debugger (XSDB) v2021.1
        *** Build date : Jun 10 2021-20:11:58
          ** Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.


      xsdb% source run.tcl
      attempting to launch hw_server

      * Xilinx hw_server v2021.1
        *** Build date : Jun 10 2021 at 20:11:57
          ** Copyright 1986-2021 Xilinx, Inc. All Rights Reserved.

      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application

      INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121

      100%    4MB   1.7MB/s  00:02
      Downloading Program -- /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
              section, .text: 0x80000000 - 0x804763ab
              section, __fdt_blob: 0x804763ac - 0x804863ab
              section, .rodata: 0x80487000 - 0x808b110f
              section, .builtin_fw: 0x808b1110 - 0x808b1133
              section, __ksymtab: 0x808b1134 - 0x808b746b
              section, __ksymtab_gpl: 0x808b746c - 0x808bc483
              section, __ksymtab_strings: 0x808bc484 - 0x808d6973
              section, __param: 0x808d6974 - 0x808d6e5f
              section, __modver: 0x808d6e60 - 0x808d6fff
              section, __ex_table: 0x808d7000 - 0x808d844f
              section, .notes: 0x808d8450 - 0x808d848b
              section, .sdata2: 0x808d848c - 0x808d8fff
              section, .data: 0x808d9000 - 0x8095893f
              section, .init.text: 0x80959000 - 0x8097a75b
              section, .init.data: 0x8097a75c - 0x8097c053
              section, .init.ivt: 0x8097c054 - 0x8097c07b
              section, .init.setup: 0x8097c07c - 0x8097c3f3
              section, .initcall.init: 0x8097c3f4 - 0x8097c80f
              section, .con_initcall.init: 0x8097c810 - 0x8097c813
              section, .init.ramfs: 0x8097c814 - 0x80c2a9fb
              section, .bss: 0x80c2b000 - 0x80c4225b
      100%   12MB   0.2MB/s  00:56
      Setting PC to Program Start Address 0x80000000
      Successfully downloaded /home/liacob/microblaze/simpleImage.kc705_fmcomms2-3/simpleImage.kc705_fmcomms2-3.strip
      Info: MicroBlaze #0 (target 3) Running
      xsdb% Info: tcfchan#0 closed
      xsdb%

Boot messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are interested in the Linux console messages and command line
interface, connect a USB cable to the USB UART port. Terminal
settings are 115200, 8N1.

There are two users:

====== ========
user   password
====== ========
root   analog
analog analog
====== ========

If your FPGA carrier board (:xilinx:`KC705`, :xilinx:`VC707`)
features a LCD display and the board is connected to a DHCP enabled
network, you should also see its IP address printed on the display.
This allows you to connect remotely to the board as well (SSH,
libiio remote).

.. image:: ../images/ml605-lcd.png
   :alt: LCD image
   :width: 200

.. collapsible:: Complete boot log (click to expand)

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
