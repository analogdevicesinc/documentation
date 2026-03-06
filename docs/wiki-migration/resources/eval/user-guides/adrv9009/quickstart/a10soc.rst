EVAL-ADRV9009 Arria10 SoC Development Kit Quick Start Guide
===========================================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/quickstart/fmcomms8_a10soc.jpeg
   :align: center
   :width: 600px

Requirements
------------

-  :adi:`EVAL-ADRV9008-9009`

   -  2x SMA cable for analog signal loopback (optional, but recommended)

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__ (Rev. C or later)

   -  Power-supply
   -  USB mini cable for serial console (optional, but recommended)
   -  Ethernet cable for network connectivity (optional, but recommended)

-  SD card with latest ADI Linux image

.. esd-warning::


Creating / Configuring the SD Card
----------------------------------

:doc:`Create SD Image. (it is a single image for all boards) </wiki-migration/resources/tools-software/linux-software/zynq_images>`

Hardware Setup
--------------

FMC Pin Connection Configuration Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   To be compatible with the EVAL-ADRV9008-9009 the Arria10 SoC Development Kit requires a minor rework.


In the default configuration of the Arria10 SoC Development Kit some of the FMC header pins are connected to a dedicated clock chip. To be compatible with the EVAL-ADRV9008-9009 these pins need to be connected directly to the FPGA.

The connection of those pins can be changed by moving the position of four zero Ohm resistors:

-  R612 to R610
-  R613 to R611
-  R621 to R620
-  R633 to R632

These resistors can be found on the backside of the Arria10 SoC Development Kit underneath the FMC A connector (J29). The following picture shows the required configuration to be compatible with the EVAL-ADRV9008-9009.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/a10soc_fmc_rework.jpg
   :align: center

Connections
-----------

-  Insert the EVAL-ADRV9008-9009 board into the FMC A (J29) header of the Arria10 SoC Development Kit
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
   U-Boot SPL 2021.07-16360-gee63370553-dirty (Jan 14 2022 - 20:13:46 +0200)

   U-Boot SPL 2021.07-16360-gee63370553-dirty (Jan 14 2022 - 20:13:46 +0200)
   DDRCAL: Success
   WDT:   Started with servicing (10s timeout)
   Trying to boot from MMC1
   </nowiki>

Configuring the FPGA will take a few seconds. Once the FPGA has been configured the green D18 LED will turn on and the boot process will continue.

::

   <nowiki>
   U-Boot 2021.07-16360-gee63370553-dirty (Jan 14 2022 - 20:13:46 +0200)socfpga_arria10, Build: jenkins-master-quartus_boot_on_ubuntu_master-32

   CPU:   Altera SoCFPGA Arria 10
   BOOT:  SD/MMC External Transceiver (1.8V)
   Model: Altera SOCFPGA Arria 10
   DRAM:  1 GiB
   WDT:   Started with servicing (10s timeout)
   MMC:   dwmmc0@ff808000: 0
   Loading Environment from MMC... OK
   In:    serial
   Out:   serial
   Err:   serial
   Model: Altera SOCFPGA Arria 10
   Net:
   Warning: ethernet@ff800000 (eth0) using random MAC address - e6:20:e5:4d:c6:2c
   eth0: ethernet@ff800000
   Hit any key to stop autoboot:  0
   Failed to load 'u-boot.scr'
   switch to partitions #0, OK
   mmc0 is current device
   Scanning mmc 0:1...
   Found /extlinux/extlinux.conf
   Retrieving file: /extlinux/extlinux.conf
   162 bytes read in 6 ms (26.4 KiB/s)
   1:      Linux Default
   Retrieving file: /extlinux/../zImage
   8121200 bytes read in 396 ms (19.6 MiB/s)
   append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
   Retrieving file: /extlinux/../socfpga_arria10_socdk_sdmmc.dtb
   49926 bytes read in 9 ms (5.3 MiB/s)
   Kernel image @ 0x1000000 [ 0x000000 - 0x7beb70 ]
   ## Flattened Device Tree blob at 02000000
      Booting using the fdt blob at 0x2000000
      Loading Device Tree to 09ff0000, end 09fff305 ... OK

   Starting kernel ...

   Deasserting all peripheral resets
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.10.0-97952-ga2a6fc514c77 (jenkins@romlxbuild1.adlk.analog.com) (arm-xilinx-linux-gnueabi-gcc.real (GCC) 10.2.0, GNU ld (GNU Binutils) 2.35.0.20200730) #4513 SMP Sat Jan 15 09:16:57 GMT 2022
   [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] OF: fdt: Machine model: Altera SOCFPGA Arria 10
   ...
   </nowiki>



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

::

   <nowiki>
   [    0.000000] printk: bootconsole [earlycon0] enabled
   [    0.000000] Memory policy: Data cache writealloc
   [    0.000000] cma: Reserved 128 MiB at 0x38000000
   [    0.000000] Zone ranges:
   [    0.000000]   Normal   [mem 0x0000000000000000-0x000000002fffffff]
   [    0.000000]   HighMem  [mem 0x0000000030000000-0x000000003fffffff]
   [    0.000000] Movable zone start for each node
   [    0.000000] Early memory node ranges
   [    0.000000]   node   0: [mem 0x0000000000000000-0x000000003fffffff]
   [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000003fffffff]
   [    0.000000] percpu: Embedded 19 pages/cpu s45324 r8192 d24308 u77824
   [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
   [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
   [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
   [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
   [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
   [    0.000000] Memory: 884204K/1048576K available (13312K kernel code, 1265K rwdata, 7264K rodata, 1024K init, 202K bss, 33300K reserved, 131072K cma-reserved, 131072K highmem)
   [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
   [    0.000000] ftrace: allocating 40771 entries in 80 pages
   [    0.000000] ftrace: allocated 80 pages with 2 groups
   [    0.000000] rcu: Hierarchical RCU implementation.
   [    0.000000] rcu:     RCU event tracing is enabled.
   [    0.000000]  Rude variant of Tasks RCU enabled.
   [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
   [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
   [    0.000000] L2C-310 erratum 769419 enabled
   [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
   [    0.000000] L2C-310: enabling full line of zeros but not enabled in Cortex-A9
   [    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
   [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
   [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
   [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76560001
   [    0.000000] random: get_random_bytes called from start_kernel+0x3a0/0x558 with crng_init=0
   [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
   [    0.000006] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
   [    0.007886] Switching to timer-based delay loop, resolution 10ns
   [    0.014181] Console: colour dummy device 80x30
   [    0.018626] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
   [    0.029111] pid_max: default: 32768 minimum: 301
   [    0.033811] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   [    0.041089] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   [    0.049368] CPU: Testing write buffer coherency: ok
   [    0.054268] CPU0: Spectre v2: using BPIALL workaround
   [    0.059457] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   [    0.065553] Setting up static identity map for 0x100000 - 0x100060
   [    0.071814] rcu: Hierarchical SRCU implementation.
   [    0.076851] smp: Bringing up secondary CPUs ...
   [    0.081945] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   [    0.081953] CPU1: Spectre v2: using BPIALL workaround
   [    0.092724] smp: Brought up 1 node, 2 CPUs
   [    0.096805] SMP: Total of 2 processors activated (400.00 BogoMIPS).
   [    0.103056] CPU: All CPU(s) started in SVC mode.
   [    0.108130] devtmpfs: initialized
   [    0.117226] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
   [    0.125166] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   [    0.134975] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
   [    0.145811] NET: Registered protocol family 16
   [    0.151938] DMA: preallocated 256 KiB pool for atomic coherent allocations
   [    0.159642] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
   [    0.167623] hw-breakpoint: maximum watchpoint size is 4 bytes.
   [    0.180448] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
   [    0.194282] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
   [    0.217299] vgaarb: loaded
   [    0.220227] SCSI subsystem initialized
   [    0.224137] usbcore: registered new interface driver usbfs
   [    0.229625] usbcore: registered new interface driver hub
   [    0.234972] usbcore: registered new device driver usb
   [    0.240120] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
   [    0.250769] mc: Linux media interface: v0.10
   [    0.255072] videodev: Linux video capture interface: v2.00
   [    0.260580] pps_core: LinuxPPS API ver. 1 registered
   [    0.265531] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
   [    0.274644] PTP clock support registered
   [    0.278941] jesd204: created con: id=0, topo=0, link=0, /soc/bridge@ff200000/axi-jesd204-tx@20000 <-> /soc/bridge@ff200000/axi-adrv9009-tx-hpc@54000
   [    0.292216] jesd204: created con: id=1, topo=0, link=2, /soc/bridge@ff200000/spi@40/ad9528-1@0 <-> /soc/bridge@ff200000/axi-adrv9009-rx-os-xcvr@44000
   [    0.305561] jesd204: created con: id=2, topo=0, link=2, /soc/bridge@ff200000/axi-adrv9009-rx-os-xcvr@44000 <-> /soc/bridge@ff200000/axi-jesd204-rx@40000
   [    0.319166] jesd204: created con: id=3, topo=0, link=1, /soc/bridge@ff200000/spi@40/ad9528-1@0 <-> /soc/bridge@ff200000/axi-adrv9009-rx-xcvr@34000
   [    0.332249] jesd204: created con: id=4, topo=0, link=1, /soc/bridge@ff200000/axi-adrv9009-rx-xcvr@34000 <-> /soc/bridge@ff200000/axi-jesd204-rx@30000
   [    0.345594] jesd204: created con: id=5, topo=0, link=0, /soc/bridge@ff200000/spi@40/ad9528-1@0 <-> /soc/bridge@ff200000/axi-adrv9009-tx-xcvr@24000
   [    0.358677] jesd204: created con: id=6, topo=0, link=0, /soc/bridge@ff200000/axi-adrv9009-tx-xcvr@24000 <-> /soc/bridge@ff200000/axi-jesd204-tx@20000
   [    0.372048] jesd204: created con: id=7, topo=0, link=1, /soc/bridge@ff200000/axi-jesd204-rx@30000 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy@1
   [    0.384972] jesd204: created con: id=8, topo=0, link=2, /soc/bridge@ff200000/axi-jesd204-rx@40000 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy@1
   [    0.397895] jesd204: created con: id=9, topo=0, link=0, /soc/bridge@ff200000/axi-adrv9009-tx-hpc@54000 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy@1
   [    0.411249] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy@1: JESD204[0] transition uninitialized -> initialized
   [    0.421649] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy@1: JESD204[1] transition uninitialized -> initialized
   [    0.432047] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy@1: JESD204[2] transition uninitialized -> initialized
   [    0.442443] jesd204: found 9 devices and 1 topologies
   [    0.447500] FPGA manager framework
   [    0.450944] Advanced Linux Sound Architecture Driver Initialized.
   [    0.457982] clocksource: Switched to clocksource timer1
   [    1.006725] NET: Registered protocol family 2
   [    1.011615] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
   [    1.019963] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
   [    1.027723] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
   [    1.034931] TCP: Hash tables configured (established 8192 bind 8192)
   [    1.041378] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
   [    1.048034] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
   [    1.055216] NET: Registered protocol family 1
   [    1.059983] RPC: Registered named UNIX socket transport module.
   [    1.065879] RPC: Registered udp transport module.
   [    1.070588] RPC: Registered tcp transport module.
   [    1.075269] RPC: Registered tcp NFSv4.1 backchannel transport module.
   [    1.081696] PCI: CLS 0 bytes, default 64
   [    1.086742] workingset: timestamp_bits=30 max_order=18 bucket_order=0
   [    1.098077] NFS: Registering the id_resolver key type
   [    1.103133] Key type id_resolver registered
   [    1.107296] Key type id_legacy registered
   [    1.111315] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
   [    1.118164] ntfs: driver 2.1.32 [Flags: R/W].
   [    1.122643] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
   [    1.129271] bounce: pool size: 64 pages
   [    1.133099] io scheduler mq-deadline registered
   [    1.137607] io scheduler kyber registered
   [    1.145931] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
   [    1.152653] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
   [    1.163347] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
   [    1.170527] printk: console [ttyS0] disabled
   [    1.174832] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 45, base_baud = 6250000) is a 16550A
   [    1.183820] printk: console [ttyS0] enabled
   [    1.183820] printk: console [ttyS0] enabled
   [    1.192157] printk: bootconsole [earlycon0] disabled
   [    1.192157] printk: bootconsole [earlycon0] disabled
   [    1.203639] brd: module loaded
   [    1.206978] at24 0-0051: supply vcc not found, using dummy regulator
   [    1.214597] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
   [    1.222533] spi_altera ff200040.spi: regoff 0, irq 48
   [    1.229124] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
   [    1.236620] libphy: Fixed MDIO Bus: probed
   [    1.241206] CAN device driver interface
   [    1.245245] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
   [    1.251853] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
   [    1.258148] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
   [    1.264819] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
   [    1.271211] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
   [    1.278409] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
   [    1.284652] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
   [    1.290736] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
   [    1.297501] stmmaceth ff800000.ethernet:     DWMAC1000
   [    1.302375] stmmaceth ff800000.ethernet: DMA HW capability register supported
   [    1.309486] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
   [    1.316587] stmmaceth ff800000.ethernet: COE Type 2
   [    1.321449] stmmaceth ff800000.ethernet: TX Checksum insertion supported
   [    1.328125] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
   [    1.334709] stmmaceth ff800000.ethernet: Enabled extended descriptors
   [    1.341125] stmmaceth ff800000.ethernet: Ring mode enabled
   [    1.346586] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
   [    1.354227] stmmaceth ff800000.ethernet: device MAC address f6:ce:13:43:df:3d
   [    1.369445] libphy: stmmac: probed
   [    1.372849] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
   [    1.386484] usbcore: registered new interface driver asix
   [    1.391940] usbcore: registered new interface driver ax88179_178a
   [    1.398052] usbcore: registered new interface driver cdc_ether
   [    1.403877] usbcore: registered new interface driver net1080
   [    1.409542] usbcore: registered new interface driver cdc_subset
   [    1.415453] usbcore: registered new interface driver zaurus
   [    1.421050] usbcore: registered new interface driver cdc_ncm
   [    1.427165] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
   [    1.434378] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
   [    1.441694] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
   [    1.449315] dwc2 ffb00000.usb: DWC OTG Controller
   [    1.454019] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
   [    1.461077] dwc2 ffb00000.usb: irq 46, io mem 0xffb00000
   [    1.466504] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
   [    1.474754] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    1.481958] usb usb1: Product: DWC OTG Controller
   [    1.486640] usb usb1: Manufacturer: Linux 5.10.0-97952-ga2a6fc514c77 dwc2_hsotg
   [    1.493937] usb usb1: SerialNumber: ffb00000.usb
   [    1.498998] hub 1-0:1.0: USB hub found
   [    1.502764] hub 1-0:1.0: 1 port detected
   [    1.507278] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   [    1.513808] ehci-pci: EHCI PCI platform driver
   [    1.518736] usbcore: registered new interface driver uas
   [    1.524081] usbcore: registered new interface driver usb-storage
   [    1.530155] usbcore: registered new interface driver usbserial_generic
   [    1.536669] usbserial: USB Serial support registered for generic
   [    1.542698] usbcore: registered new interface driver ftdi_sio
   [    1.548448] usbserial: USB Serial support registered for FTDI USB Serial Device
   [    1.555788] usbcore: registered new interface driver upd78f0730
   [    1.561707] usbserial: USB Serial support registered for upd78f0730
   [    1.575199] rtc-ds1307 0-0068: registered as rtc0
   [    1.580000] i2c /dev entries driver
   [    1.584084] usbcore: registered new interface driver uvcvideo
   [    1.589825] USB Video Class driver (1.1.1)
   [    1.598096] ltc2978: probe of 0-005c failed with error -121
   [    1.604381] Synopsys Designware Multimedia Card Interface Driver
   [    1.610650] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
   [    1.617292] ledtrig-cpu: registered to indicate activity on CPUs
   [    1.617449] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
   [    1.623412] usbcore: registered new interface driver usbhid
   [    1.629477] dw_mmc ff808000.dwmmc0: Version ID is 270a
   [    1.635010] usbhid: USB HID core driver
   [    1.640172] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 41,32 bit host data width,1024 deep fifo
   [    1.645727] adrv9009 spi0.1: adrv9009_probe : enter
   [    1.653307] mmc_host mmc0: card is polling.
   [    1.664981] ad9528 spi0.0: supply vcc not found, using dummy regulator
   [    1.674754] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
   [    1.681872] iio iio:device2: SPI Read Verify failed (0x0)
   [    1.689749] ad9528: probe of spi0.0 failed with error -5
   [    1.699044] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
   [    1.706275] usbcore: registered new interface driver snd-usb-audio
   [    1.714381] NET: Registered protocol family 10
   [    1.719599] Segment Routing with IPv6
   [    1.723331] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   [    1.729744] NET: Registered protocol family 17
   [    1.734204] NET: Registered protocol family 15
   [    1.738802] can: controller area network core
   [    1.743207] NET: Registered protocol family 29
   [    1.747642] can: raw protocol
   [    1.750625] can: broadcast manager protocol
   [    1.754794] can: netlink gateway - max_hops=1
   [    1.759286] 8021q: 802.1Q VLAN Support v1.8
   [    1.763496] NET: Registered protocol family 36
   [    1.767948] Key type dns_resolver registered
   [    1.772479] oprofile: no performance counters
   [    1.776909] oprofile: using timer interrupt.
   [    1.781264] ThumbEE CPU extension supported.
   [    1.785532] Registering SWP/SWPB emulation handler
   [    1.790929] adrv9009 spi0.1: adrv9009_probe : enter
   [    1.800359] adrv9009 spi0.1: adrv9009_probe : enter
   [    1.809243] of_cfs_init
   [    1.811750] of_cfs_init: OK
   [    1.814822] ALSA device list:
   [    1.817788]   No soundcards found.
   [    1.821381] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
   [    1.831177] dw-apb-uart ffc02100.serial1: forbid DMA for kernel console
   [    1.837880] mmc0: new high speed SDHC card at address aaaa
   [    1.837953] Waiting for root device /dev/mmcblk0p2...
   [    1.843862] mmcblk0: mmc0:aaaa SC32G 29.7 GiB
   [    1.857473]  mmcblk0: p1 p2 p3
   [    1.861719] adrv9009 spi0.1: adrv9009_probe : enter
   [    1.904620] random: fast init done
   [    1.908967] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   [    1.917070] VFS: Mounted root (ext4 filesystem) on device 179:2.
   [    1.933531] devtmpfs: mounted
   [    1.940456] Freeing unused kernel memory: 1024K
   [    1.945416] Run /sbin/init as init process
   [    2.532208] systemd[1]: System time before build time, advancing clock.
   [    2.581732] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
   [    2.603612] systemd[1]: Detected architecture arm.

   Welcome to Kuiper GNU/Linux 10 (buster)!

   [    2.700952] systemd[1]: Set hostname to <analog>.
   [    3.053812] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   [    3.070851] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   [    3.255340] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
   [    3.265035] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
   [    3.481030] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.499528] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
   [    3.511253] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.518686] systemd[1]: Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Journal Socket (/dev/log).
   [    3.548123] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.554770] systemd[1]: Reached target Swap.
   [  OK  ] Reached target Swap.
   [  OK  ] Created slice system-getty.slice.
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
   [  OK  ] Listening on Syslog Socket.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [  OK  ] Listening on udev Control Socket.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Listening on Journal Socket.
            Mounting RPC Pipe File System...
            Starting Restore / save the current clock...
            Starting Set the console keyboard layout...
   [  OK  ] Listening on initctl Compatibility Named Pipe.
   [  OK  ] Listening on udev Kernel Socket.
            Starting udev Coldplug all Devices...
            Starting Journal Service...
            Starting Load Kernel Modules...
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Reached target Slices.
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   [  OK  ] Mounted RPC Pipe File System.
   [  OK  ] Started Restore / save the current clock.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started Journal Service.
   [  OK  ] Started Set the console keyboard layout.
            Mounting Kernel Configuration File System...
            Starting Apply Kernel Variables...
            Starting Remount Root and Kernel File Systems...
   [  OK  ] Started udev Coldplug all Devices.
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started Apply Kernel Variables.
            Starting Helper to synchronize boot up for ifupdown...
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
   [  OK  ] Started Remount Root and Kernel File Systems.
            Starting Flush Journal to Persistent Storage...
            Starting Load/Save Random Seed...
            Starting Create System Users...
   [  OK  ] Started Load/Save Random Seed.
   [  OK  ] Started Create System Users.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Started Flush Journal to Persistent Storage.
   [  OK  ] Started Create Static Device Nodes in /dev.
            Starting udev Kernel Device Manager...
   [  OK  ] Reached target Local File Systems (Pre).
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Reached target Local Encrypted Volumes.
   [  OK  ] Found device /dev/ttyS0.
   [  OK  ] Found device /dev/disk/by-partuuid/004ba301-01.
            Starting File System Check…isk/by-partuuid/004ba301-01...
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Started File System Check …/disk/by-partuuid/004ba301-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Raise network interfaces...
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Create Volatile Files and Directories...
            Starting Preprocess NFS configuration...
            Starting Set console font and keymap...
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Create Volatile Files and Directories.
            Starting Network Time Synchronization...
            Starting Update UTMP about System Boot/Shutdown...
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
   [  OK  ] Started Network Time Synchronization.
   [  OK  ] Reached target System Time Synchronized.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Reached target Sockets.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Reached target Basic System.
   [  OK  ] Started D-Bus System Message Bus.
            Starting rng-tools.service...
            Starting System Logging Service...
            Starting LSB: Switch to on…nless shift key is pressed)...
            Starting Disk Manager...
   [  OK  ] Started tof-server.service.
   [  OK  ] Started Regular background program processing daemon.
            Starting dphys-swapfile - …unt, and delete a swap file...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting Login Service...
            Starting dhcpcd on all interfaces...
            Starting triggerhappy global hotkey daemon...
   [  OK  ] Started CUPS Scheduler.
            Starting Modem Manager...
            Starting WPA supplicant...
            Starting Avahi mDNS/DNS-SD Stack...
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Reached target Timers.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
   [  OK  ] Started triggerhappy global hotkey daemon.
   [  OK  ] Started System Logging Service.
   [  OK  ] Started Raise network interfaces.
   [  OK  ] Started Check for Raspberry Pi EEPROM updates.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started Login Service.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started WPA supplicant.
   [  OK  ] Reached target Network.
            Starting HTTP based time synchronization tool...
   [  OK  ] Reached target Network is Online.
            Starting Internet superserver...
            Starting /etc/rc.local Compatibility...
            Starting Permit User Sessions...
   [  OK  ] Started IIO Daemon.
            Starting OpenBSD Secure Shell server...
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Started Internet superserver.
   [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
   [  OK  ] Started HTTP based time synchronization tool.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started Permit User Sessions.
            Starting Light Display Manager...
            Starting Authorization Manager...
            Starting Hold until boot process finishes up...
   [  OK  ] Started Authorization Manager.

   Raspbian GNU/Linux 10 analog ttyS0

   analog login: root (automatic login)

   Last login: Fri Jan 14 11:18:51 GMT 2022 on ttyS0
   Linux analog 5.10.0-97952-ga2a6fc514c77 #4513 SMP Sat Jan 15 09:16:57 GMT 2022 armv7l

   The programs included with the Debian GNU/Linux system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
   permitted by applicable law.
   root@analog:~#
   </nowiki>

.. raw:: html

   </details>


Once the boot process has completed you'll be greeted with command prompt. As a quick check if the EVAL-ADRV9008/9 was correctly recognized run the \`iio_info\` command and filter for the registered devices.

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

IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image1|

More information
================

:doc:`ADRV9009 User Guide </wiki-migration/resources/eval/user-guides/adrv9009>`

.. include:: ../../adrv9002/common.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
