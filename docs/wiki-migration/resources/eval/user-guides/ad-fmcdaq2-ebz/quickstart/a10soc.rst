AD-FMCDAQ2-EBZ Arria10 SoC Development Kit Quick Start Guide
============================================================

Requirements
------------

-  :adi:`AD-FMCDAQ2-EBZ`

   -  2x SMA cable for analog signal loopback (optional, but recommended)

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__ (Rev. C or later)

   -  Power-supply
   -  USB mini cable for serial console (optional, but recommended)
   -  Ethernet cable for network connectivity (optional, but recommended)

-  SD card with latest ADI Linux image

Creating / Configuring the SD Card
----------------------------------

:doc:`Create SD Image. (it is a single image for all boards) </wiki-migration/resources/tools-software/linux-software/zynq_images>`

Hardware Setup
--------------

FMC Pin Connection Configuration Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   To be compatible with the AD-FMCDAQ2-EBZ the Arria10 SoC Development Kit requires a minor rework.


In the default configuration of the Arria10 SoC Development Kit some of the FMC header pins are connected to a dedicated clock chip. To be compatible with the AD-FMCDAQ2-EBZ these pins need to be connected directly to the FPGA.

The connection of those pins can be changed by moving the position of four zero Ohm resistors:

-  R612 to R610
-  R613 to R611
-  R621 to R620
-  R633 to R632

These resistors can be found on the backside of the Arria10 SoC Development Kit underneath the FMC A connector (J29). The following picture shows the required configuration to be compatible with the AD-FMCDAQ2-EBZ.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/a10soc_fmc_rework.jpg
   :align: center

Connections
-----------

-  Insert the AD-FMCDA2-EBZ board into the FMC A (J29) header of the Arria10 SoC Development Kit
-  Both the HPS (J26) and FPGA (J27) memory module must be installed on the Arria10 SoC Development Kit.
-  For network connectivity connect a Ethernet cable to the right most Ethernet port (J5).
-  For the serial console connect a USB cable to UART1 (J10).
-  Insert the microSD card into the microSD card slot.

All jumpers and switches on the Arria10 SoC Development Kit should be in the `default position <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/ug/ug-a10-soc-devkit.pdf#page=15>`__ configuring the board for SD card boot.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/a10soc_daq2.jpg
   :align: center

Booting the System
------------------

After turning on the power switch the following messages should appear on the serial console.

::

   <nowiki>
   U-Boot 2014.10 (Aug 23 2017 - 05:49:00)

   CPU   : Altera SOCFPGA Arria 10 Platform
   BOARD : Altera SOCFPGA Arria 10 Dev Kit
   I2C:   ready
   DRAM:  WARNING: Caches not enabled
   SOCFPGA DWMMC: 0
   FPGA: writing socfpga.rbf ...
   </nowiki>

Configuring the FPGA will take a few seconds. Once the FPGA has been configured the green D18 LED will turn on and the boot process will continue.

::

   <nowiki>
   Full Configuration Succeeded.
   DDRCAL: Success
   INFO  : Skip relocation as SDRAM is non secure memory
   Reserving 2048 Bytes for IRQ stack at: ffe386e8
   DRAM  : 1 GiB
   WARNING: Caches not enabled
   MMC:   In:    serial
   Out:   serial
   Err:   serial
   Model: SOCFPGA Arria10 Dev Kit
   Net:   dwmac.ff800000
   Hit any key to stop autoboot:  0
   FPGA must be in Early Release mode to program core.
   fpga - loadable FPGA image support

   ** Unable to read file u-boot.scr **
   4845256 bytes read in 230 ms (20.1 MiB/s)
   36860 bytes read in 9 ms (3.9 MiB/s)
   FPGA BRIDGES: enable
   Kernel image @ 0x080000 [ 0x000000 - 0x49eec8 ]
   ## Flattened Device Tree blob at 00000100
      Booting using the fdt blob at 0x000100
      Loading Device Tree to 01ff4000, end 01fffffb ... OK

   Starting kernel ...

   Uncompressing Linux... done, booting the kernel.
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 4.6.0-09244-g5f1195d00092-dirty (lars@lars-laptop) (gcc version 4.9.2 (Sourcery CodeBench Lite 2015.05-17) ) #12563 SMP Fri Aug 25 14:00:36 CEST 2017
   [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] Machine model: Altera SOCFPGA Arria 10
   ...
   </nowiki>



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

::

   <nowiki>
   Uncompressing Linux... done, booting the kernel.
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 4.6.0-09244-g5f1195d00092-dirty (lars@lars-laptop) (gcc version 4.9.2 (Sourcery CodeBench Lite 2015.05-17) ) #12563 SMP Fri Aug 25 14:00:36 CEST 2017
   [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] Machine model: Altera SOCFPGA Arria 10
   [    0.000000] Memory policy: Data cache writealloc
   [    0.000000] percpu: Embedded 13 pages/cpu @ef7af000 s24064 r8192 d20992 u53248
   [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 260608
   [    0.000000] Kernel command line: console=ttyS0,115200 root=/dev/mmcblk0p2 rw rootwait
   [    0.000000] PID hash table entries: 4096 (order: 2, 16384 bytes)
   [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
   [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
   [    0.000000] Memory: 1019512K/1048576K available (7682K kernel code, 517K rwdata, 2388K rodata, 1024K init, 7933K bss, 29064K reserved, 0K cma-reserved, 262144K highmem)
   [    0.000000] Virtual kernel memory layout:
   [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
   [    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
   [    0.000000]     vmalloc : 0xf0800000 - 0xff800000   ( 240 MB)
   [    0.000000]     lowmem  : 0xc0000000 - 0xf0000000   ( 768 MB)
   [    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
   [    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
   [    0.000000]       .text : 0xc0008000 - 0xc0ad5ba0   (11063 kB)
   [    0.000000]       .init : 0xc0b00000 - 0xc0c00000   (1024 kB)
   [    0.000000]       .data : 0xc0c00000 - 0xc0c8179c   ( 518 kB)
   [    0.000000]        .bss : 0xc0c8179c - 0xc1440e10   (7934 kB)
   [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
   [    0.000000] Running RCU self tests
   [    0.000000] Hierarchical RCU implementation.
   [    0.000000]  RCU lockdep checking is enabled.
   [    0.000000]  Build-time adjustment of leaf fanout to 32.
   [    0.000000] NR_IRQS:16 nr_irqs:16 16
   [    0.000000] L2C-310 erratum 769419 enabled
   [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
   [    0.000000] L2C-310: enabling full line of zeros but not enabled in Cortex-A9
   [    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
   [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
   [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
   [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76460001
   [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
   [    0.000006] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
   [    0.000018] Switching to timer-based delay loop, resolution 10ns
   [    0.000677] Console: colour dummy device 80x30
   [    0.000722] Lock dependency validator: Copyright (c) 2006 Red Hat, Inc., Ingo Molnar
   [    0.000731] ... MAX_LOCKDEP_SUBCLASSES:  8
   [    0.000738] ... MAX_LOCK_DEPTH:          48
   [    0.000744] ... MAX_LOCKDEP_KEYS:        8191
   [    0.000751] ... CLASSHASH_SIZE:          4096
   [    0.000757] ... MAX_LOCKDEP_ENTRIES:     32768
   [    0.000764] ... MAX_LOCKDEP_CHAINS:      65536
   [    0.000770] ... CHAINHASH_SIZE:          32768
   [    0.000776]  memory used by lock dependency info: 5167 kB
   [    0.000783]  per task-struct memory footprint: 1536 bytes
   [    0.000827] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
   [    0.000842] pid_max: default: 32768 minimum: 301
   [    0.001159] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
   [    0.001173] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
   [    0.003968] CPU: Testing write buffer coherency: ok
   [    0.004046] ftrace: allocating 21813 entries in 64 pages
   [    0.035728] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   [    0.035957] Setting up static identity map for 0x100000 - 0x100058
   [    0.040924] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   [    0.041337] Brought up 2 CPUs
   [    0.041354] SMP: Total of 2 processors activated (400.00 BogoMIPS).
   [    0.041362] CPU: All CPU(s) started in SVC mode.
   [    0.043922] devtmpfs: initialized
   [    0.072857] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
   [    0.073602] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   [    0.078695] NET: Registered protocol family 16
   [    0.079660] DMA: preallocated 256 KiB pool for atomic coherent allocations
   [    0.098683] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
   [    0.098848] hw-breakpoint: maximum watchpoint size is 4 bytes.
   [    0.146547] SCSI subsystem initialized
   [    0.147331] usbcore: registered new interface driver usbfs
   [    0.147493] usbcore: registered new interface driver hub
   [    0.147646] usbcore: registered new device driver usb
   [    0.148074] soc:usbphy@0 supply vcc not found, using dummy regulator
   [    0.209757] lcd-comm 0-0028: LCD driver initialized
   [    0.211367] pps_core: LinuxPPS API ver. 1 registered
   [    0.211529] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
   [    0.211608] PTP clock support registered
   [    0.212198] FPGA manager framework
   [    0.216065] clocksource: Switched to clocksource timer1
   [    0.320289] NET: Registered protocol family 2
   [    0.321909] TCP established hash table entries: 8192 (order: 3, 32768 bytes)
   [    0.322349] TCP bind hash table entries: 8192 (order: 6, 294912 bytes)
   [    0.324356] TCP: Hash tables configured (established 8192 bind 8192)
   [    0.324627] UDP hash table entries: 512 (order: 3, 40960 bytes)
   [    0.324909] UDP-Lite hash table entries: 512 (order: 3, 40960 bytes)
   [    0.325777] NET: Registered protocol family 1
   [    0.327088] RPC: Registered named UNIX socket transport module.
   [    0.327103] RPC: Registered udp transport module.
   [    0.327111] RPC: Registered tcp transport module.
   [    0.327118] RPC: Registered tcp NFSv4.1 backchannel transport module.
   [    0.330733] futex hash table entries: 512 (order: 3, 32768 bytes)
   [    0.333213] workingset: timestamp_bits=28 max_order=18 bucket_order=0
   [    0.367118] NFS: Registering the id_resolver key type
   [    0.367603] Key type id_resolver registered
   [    0.367616] Key type id_legacy registered
   [    0.367799] ntfs: driver 2.1.32 [Flags: R/W].
   [    0.368875] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
   [    0.372866] bounce: pool size: 64 pages
   [    0.372969] io scheduler noop registered (default)
   [    0.385303] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
   [    0.385376] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
   [    0.397079] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
   [    0.405023] console [ttyS0] disabled
   [    0.405342] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 37, base_baud = 6250000) is a 16550A
   [    1.026981] console [ttyS0] enabled
   [    1.036921] brd: module loaded
   [    1.040906] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
   [    1.053902] spi_altera ff200040.spi: base f0916040, irq 40
   [    1.067395] CAN device driver interface
   [    1.072378] stmmac - user ID: 0x10, Synopsys ID: 0x37
   [    1.077448]  Ring mode enabled
   [    1.080491]  DMA HW capability register supported
   [    1.084999]  Enhanced/Alternate descriptors
   [    1.089360]  Enabled extended descriptors
   [    1.093352]  RX Checksum Offload Engine supported (type 2)
   [    1.098823]  TX Checksum insertion supported
   [    1.103072]  Enable RX Mitigation via HW Watchdog Timer
   [    1.114165] libphy: stmmac: probed
   [    1.117604] eth0: PHY ID 00221622 at 7 IRQ POLL (stmmac-0:07) active
   [    1.124905] ffb00000.usb supply vusb_d not found, using dummy regulator
   [    1.131669] ffb00000.usb supply vusb_a not found, using dummy regulator
   [    1.416141] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
   [    1.425087] dwc2 ffb00000.usb: DWC OTG Controller
   [    1.430367] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
   [    1.437550] dwc2 ffb00000.usb: irq 38, io mem 0x00000000
   [    1.443949] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
   [    1.450743] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    1.457953] usb usb1: Product: DWC OTG Controller
   [    1.462639] usb usb1: Manufacturer: Linux 4.6.0-09244-g5f1195d00092-dirty dwc2_hsotg
   [    1.470361] usb usb1: SerialNumber: ffb00000.usb
   [    1.478463] hub 1-0:1.0: USB hub found
   [    1.482367] hub 1-0:1.0: 1 port detected
   [    1.490245] usbcore: registered new interface driver usb-storage
   [    1.498140] mousedev: PS/2 mouse device common for all mice
   [    1.511659] rtc-ds1307 0-0068: rtc core: registered ds1339 as rtc0
   [    1.518021] i2c /dev entries driver
   [    1.527902] watchdog: Invalid min and max timeout values, resetting to 0!
   [    1.537280] Synopsys Designware Multimedia Card Interface Driver
   [    1.543607] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
   [    1.550295] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
   [    1.556477] dw_mmc ff808000.dwmmc0: Version ID is 270a
   [    1.561703] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 33,32 bit host data width,1024 deep fifo
   [    1.606410] dw_mmc ff808000.dwmmc0: 1 slots initialized
   [    1.613878] ledtrig-cpu: registered to indicate activity on CPUs
   [    1.621370] usbcore: registered new interface driver usbhid
   [    1.627094] usbhid: USB HID core driver
   [    1.661259] spi32766.0 supply vcc not found, using dummy regulator
   [    1.798579] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
   [    1.815122] altera-a10-fpll ff245000.altera-a10-fpll: reg write: 0 2 3
   [    1.815152] mmc0: new high speed SDHC card at address aaaa
   [    1.817851] mmcblk0: mmc0:aaaa SL08G 7.40 GiB
   [    1.822016]  mmcblk0: p1 p2 p3
   [    1.971964] ad9523 spi32766.0: probed ad9523-1
   [    2.033178] altera_adxcvr ff224000.axi-ad9144-xcvr: ATX PLL calibration OK (20 ms)
   [    2.057726] altera_adxcvr ff224000.axi-ad9144-xcvr: Lane 0 TX termination and VOD calibration OK (300 us)
   [    2.077646] altera_adxcvr ff224000.axi-ad9144-xcvr: Lane 1 TX termination and VOD calibration OK (500 us)
   [    2.095784] altera_adxcvr ff224000.axi-ad9144-xcvr: Lane 2 TX termination and VOD calibration OK (600 us)
   [    2.119700] altera_adxcvr ff224000.axi-ad9144-xcvr: Lane 3 TX termination and VOD calibration OK (600 us)
   [    2.293664] altera_adxcvr ff224000.axi-ad9144-xcvr: Altera ADXCVR (16.01.a) probed
   [    2.301287] altera_adxcvr ff224000.axi-ad9144-xcvr: Setting link rate to 250000000 (lane rate: 10000000)
   [    2.457609] altera-a10-fpll ff225000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
   [    2.485894] altera_adxcvr ff244000.axi-ad9680-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
   [    2.499655] altera_adxcvr ff244000.axi-ad9680-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
   [    2.512974] altera_adxcvr ff244000.axi-ad9680-xcvr: Lane 2 CDR/CMU PLL & RX offset calibration OK (600 us)
   [    2.526747] altera_adxcvr ff244000.axi-ad9680-xcvr: Lane 3 CDR/CMU PLL & RX offset calibration OK (600 us)
   [    2.679201] altera-a10-fpll ff245000.altera-a10-fpll: FPLL PLL calibration OK (1200 us)
   [    2.700765] altera_adxcvr ff244000.axi-ad9680-xcvr: Altera ADXCVR (16.01.a) probed
   [    2.708381] altera_adxcvr ff244000.axi-ad9680-xcvr: Setting link rate to 250000000 (lane rate: 10000000)
   [    2.887360] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
   [    2.895839] fpga-region soc:base_fpga_region: FPGA Region probed
   [    2.902626] oprofile: no performance counters
   [    2.908092] oprofile: using timer interrupt.
   [    2.915519] NET: Registered protocol family 10
   [    2.922556] sit: IPv6 over IPv4 tunneling driver
   [    2.929337] NET: Registered protocol family 17
   [    2.933837] NET: Registered protocol family 15
   [    2.938607] can: controller area network core (rev 20120528 abi 9)
   [    2.944918] NET: Registered protocol family 29
   [    2.949398] can: raw protocol (rev 20120528)
   [    2.953763] can: broadcast manager protocol (rev 20120528 t)
   [    2.959456] can: netlink gateway (rev 20130117) max_hops=1
   [    2.965776] 8021q: 802.1Q VLAN Support v1.8
   [    2.970272] Key type dns_resolver registered
   [    2.974602] ThumbEE CPU extension supported.
   [    2.978900] Registering SWP/SWPB emulation handler
   [    3.040751] ad9467 spi32766.2: AD9680 PLL LOCKED
   [    3.164173] cf_axi_adc ff250000.axi-ad9680-hpc: ADI AIM (10.00.b) at 0xFF250000 mapped to 0xf09a0000, probed ADC AD9680 as MASTER
   [    3.188173] cf_axi_dds ff234000.axi-ad9144-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.00.b) at 0xFF234000 mapped to 0xf0998000, probed DDS AD9144
   [    3.201528] of_cfs_init
   [    3.205007] of_cfs_init: OK
   [    3.218983] ttyS0 - failed to request DMA
   [    3.224979] EXT4-fs (mmcblk0p2): couldn't mount as ext3 due to feature incompatibilities
   [    3.395796] EXT4-fs (mmcblk0p2): recovery complete
   [    3.402601] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   [    3.410799] VFS: Mounted root (ext4 filesystem) on device 179:2.
   [    3.426777] devtmpfs: mounted
   [    3.431414] Freeing unused kernel memory: 1024K (c0b00000 - c0c00000)
   Mount failed for selinuxfs on /sys/fs/selinux:  No such file or directory
   [    3.750687] random: init urandom read with 49 bits of entropy available
   [    3.903751] init: hwclock main process (734) terminated with status 1
     * Setting up X socket directories...                                    [ OK ]
     * STARTDISTCC is set to false in /etc/default/distcc
     * /usr/bin/distccd not starting
     * Starting IIO Daemon iiod                                              [ OK ]

   Last login: Thu Jan  1 00:00:12 UTC 1970 on tty1
   Welcome to Linaro 14.04 (GNU/Linux 4.6.0-09244-g5f1195d00092-dirty armv7l)

     * Documentation:  https://wiki.analog.com/ https://ez.analog.com/

   root@analog:~# 
   </nowiki>

.. raw:: html

   </details>


Once the boot process has completed you'll be greeted with command prompt. As a quick check if the AD-FMCDAQ2-EBZ was correctly recognized run the \`iio_info\` command and filter for the registered devices.

::

   <nowiki>
   Last login: Thu Jan  1 00:00:12 UTC 1970 on tty1
   Welcome to Linaro 14.04 (GNU/Linux 4.6.0-09244-g5f1195d00092-dirty armv7l)

     * Documentation:  https://wiki.analog.com/ https://ez.analog.com/

   root@analog:~# iio_info | grep iio:device
           iio:device0: ad9523-1
           iio:device1: axi-ad9680-hpc (buffer capable)
           iio:device2: axi-ad9144-hpc (buffer capable)
   </nowiki>

If the Arria 10 SoC Development Kit is connected to a network with a DHCP server the IP address assigned to the board appears on the LCD. Alternatively you can query the IP address by running \`ifconfig eth0\` on the command line. To manually assign an IP address run \`ifconfig eth0 *IP_ADDR*\ \`.
