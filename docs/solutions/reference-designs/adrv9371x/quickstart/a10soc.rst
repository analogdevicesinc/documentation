EVAL-ADRV9371 Arria10 SoC Development Kit Quick Start Guide
===========================================================

.. image:: ../images/a10soc_adrv9371.jpg
   :align: center
   :width: 600

Requirements
------------

-  :adi:`EVAL-ADRV9371`

   -  2x SMA cable for analog signal loopback (optional, but recommended)

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_ (Rev. C or later)

   -  Power-supply
   -  USB mini cable for serial console (optional, but recommended)
   -  Ethernet cable for network connectivity (optional, but recommended)

-  SD card with latest ADI Linux image

.. esd-warning::

Creating / Configuring the SD Card
----------------------------------

:doc:`Create SD Image. (it is a single image for all boards) </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

-   Copy next boot files from ``socfpga_arria10_socdk_adrv9371`` directory directly on SD Card ``BOOT`` partition :

   -  ``fit_spl_fpga.itb``
   -  ``socfpga_arria10_socdk_sdmmc.dtb``
   -  ``u-boot.img``
   -  ``zImage`` (from ``socfpga_arria10-common`` folder)
   -  ``extlinux.conf`` in the extlinux folder from SD Card

-  Write u-boot-splx4.sfp from ``socfpga_arria10_socdk_adrv9371`` folder on third SD Card partition:

::

       root@raspberrypi:~# lsblk
       NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
       sda           8:0    1 14.9G  0 disk
       ├─sda1        8:1    1    1G  0 part /media/pi/BOOT
       ├─sda2        8:2    1  7.6G  0 part /media/pi/rootfs
       └─sda3        8:3    1    4M  0 part
       root@raspberrypi:~# dd if="./u-boot-splx4.sfp" of="/dev/sda3" bs=512
       2048+0 records in
       2048+0 records out
       1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.25035 s, 4.2 MB/s

Hardware Setup
--------------

FMC Pin Connection Configuration Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   To be compatible with the EVAL-ADRV9371 the Arria10 SoC Development Kit
   requires a minor rework.

In the default configuration of the Arria10 SoC Development Kit some of the FMC
header pins are connected to a dedicated clock chip. To be compatible with the
EVAL-ADRV9371 these pins need to be connected directly to the FPGA.

The connection of those pins can be changed by moving the position of four zero
Ohm resistors:

-  R612 to R610
-  R613 to R611
-  R621 to R620
-  R633 to R632

These resistors can be found on the backside of the Arria10 SoC Development Kit
underneath the FMC A connector (J29). The following picture shows the required
configuration to be compatible with the EVAL-ADRV9371.

.. image:: ../images/a10soc_fmc_rework.jpg
   :align: center

Connections
-----------

-  Insert the EVAL-ADRV9008-9009 board into the FMC A (J29) header of the Arria10 SoC Development Kit
-  Both the HPS (J26) and FPGA (J27) memory module must be installed on the Arria10 SoC Development Kit.
-  For network connectivity connect a Ethernet cable to the right most Ethernet port (J5).
-  For the serial console connect a USB cable to UART1 (J10).
-  Insert the microSD card into the microSD card slot.

All jumpers and switches on the Arria10 SoC Development Kit should be in the `default position <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/ug/ug-a10-soc-devkit.pdf#page=15>`_ configuring the board for SD card boot.

Booting the System
------------------

After turning on the power switch the following messages should appear on the
serial console.

::

   <nowiki>
   U-Boot SPL 2021.07-16360-gee63370553-dirty (Jan 26 2022 - 11:11:00 +0200)
   FPGA: Checking FPGA configuration setting ...
   FPGA: Start to program peripheral/full bitstream ...
   FPGA: Early Release Succeeded.
   FPGA: Checking FPGA configuration setting ...
   FPGA: Start to program peripheral/full bitstream ...
   FPGA: Early Release Succeeded.

   U-Boot SPL 2021.07-16360-gee63370553-dirty (Jan 26 2022 - 11:11:00 +0200)
   DDRCAL: Success
   FPGA: Checking FPGA configuration setting ...
   FPGA: Start to program core bitstream ...
   Full Configuration Succeeded.
   FPGA: Enter user mode.
   WDT:   Started with servicing (10s timeout)
   Trying to boot from MMC1
   </nowiki>

Configuring the FPGA will take a few seconds. Once the FPGA has been configured
the green D18 LED will turn on and the boot process will continue.

::

   <nowiki>
   U-Boot 2021.07-16360-gee63370553-dirty (Jan 26 2022 - 11:11:00 +0200)socfpga_arria10, Build: jenkins-master-quartus_boot_on_ubuntu_master-40

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
   Warning: ethernet@ff800000 (eth0) using random MAC address - f6:25:8a:7b:fc:03
   eth0: ethernet@ff800000
   Hit any key to stop autoboot:  0
   Failed to load 'u-boot.scr'
   14981396 bytes read in 728 ms (19.6 MiB/s)
   fpga - loadable FPGA image support

   Usage:
   fpga [operation type] [device number] [image address] [image size]
   fpga operations:
     dump  [dev] [address] [size]  Load device to memory buffer
     info  [dev]                   list known device information
     load  [dev] [address] [size]  Load device from memory buffer
     loadb [dev] [address] [size]  Load device from bitstream buffer (Xilinx only)
     loadmk [dev] [address]        Load device generated with mkimage
           For loadmk operating on FIT format uImage address must include
           subimage unit name in the form of addr:<subimg_uname>
   switch to partitions #0, OK
   mmc0 is current device
   Scanning mmc 0:1...
   Found /extlinux/extlinux.conf
   Retrieving file: /extlinux/extlinux.conf
   162 bytes read in 6 ms (26.4 KiB/s)
   1:      Linux Default
   Retrieving file: /extlinux/../zImage
   8124456 bytes read in 399 ms (19.4 MiB/s)
   append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
   Retrieving file: /extlinux/../socfpga_arria10_socdk_sdmmc.dtb
   36828 bytes read in 9 ms (3.9 MiB/s)
   Kernel image @ 0x1000000 [ 0x000000 - 0x7bf828 ]
   ## Flattened Device Tree blob at 02000000
      Booting using the fdt blob at 0x2000000
      Loading Device Tree to 09ff4000, end 09ffffdb ... OK

   Starting kernel ...

   Deasserting all peripheral resets
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.10.0-97993-ga7064610e8f3 (jenkins@romlxbuild1.adlk.analog.com) (arm-xilinx-linux-gnueabi-gcc.real (GCC) 10.2.0, GNU ld (GNU Binutils) 2.35.0.20200730) #4699 SMP Sat Jan 29 09:17:25 GMT 2022
   [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] OF: fdt: Machine model: Altera SOCFPGA Arria 10
   ...
   </nowiki>

.. collapsible:: Complete kernel boot log (Click to expand)

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
      [    0.000000] Memory: 884232K/1048576K available (13312K kernel code, 1261K rwdata, 7360K rodata, 1024K init, 202K bss, 33272K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 40785 entries in 80 pages
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
      [    0.000005] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.007885] Switching to timer-based delay loop, resolution 10ns
      [    0.014178] Console: colour dummy device 80x30
      [    0.018624] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.029109] pid_max: default: 32768 minimum: 301
      [    0.033809] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.041086] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.049369] CPU: Testing write buffer coherency: ok
      [    0.054270] CPU0: Spectre v2: using BPIALL workaround
      [    0.059458] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.065547] Setting up static identity map for 0x100000 - 0x100060
      [    0.071811] rcu: Hierarchical SRCU implementation.
      [    0.076844] smp: Bringing up secondary CPUs ...
      [    0.081947] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.081955] CPU1: Spectre v2: using BPIALL workaround
      [    0.092726] smp: Brought up 1 node, 2 CPUs
      [    0.096807] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.103058] CPU: All CPU(s) started in SVC mode.
      [    0.108137] devtmpfs: initialized
      [    0.116294] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.124229] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.134039] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.144919] NET: Registered protocol family 16
      [    0.151058] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.158753] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.166734] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.179520] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
      [    0.192735] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
      [    0.214690] vgaarb: loaded
      [    0.217618] SCSI subsystem initialized
      [    0.221502] usbcore: registered new interface driver usbfs
      [    0.227025] usbcore: registered new interface driver hub
      [    0.232356] usbcore: registered new device driver usb
      [    0.237538] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
      [    0.247964] mc: Linux media interface: v0.10
      [    0.252241] videodev: Linux video capture interface: v2.00
      [    0.257779] pps_core: LinuxPPS API ver. 1 registered
      [    0.262730] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.271831] PTP clock support registered
      [    0.276006] jesd204: found 0 devices and 0 topologies
      [    0.281059] FPGA manager framework
      [    0.284518] Advanced Linux Sound Architecture Driver Initialized.
      [    0.291511] clocksource: Switched to clocksource timer1
      [    0.839051] NET: Registered protocol family 2
      [    0.843954] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
      [    0.852302] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.860064] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.867265] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.873708] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.880334] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.887548] NET: Registered protocol family 1
      [    0.892306] RPC: Registered named UNIX socket transport module.
      [    0.898200] RPC: Registered udp transport module.
      [    0.902909] RPC: Registered tcp transport module.
      [    0.907591] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.914018] PCI: CLS 0 bytes, default 64
      [    0.919059] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.930375] NFS: Registering the id_resolver key type
      [    0.935467] Key type id_resolver registered
      [    0.939630] Key type id_legacy registered
      [    0.943644] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
      [    0.950467] ntfs: driver 2.1.32 [Flags: R/W].
      [    0.954967] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.961590] bounce: pool size: 64 pages
      [    0.965417] io scheduler mq-deadline registered
      [    0.969925] io scheduler kyber registered
      [    0.978274] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
      [    0.984988] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    0.995679] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    1.002890] printk: console [ttyS0] disabled
      [    1.007196] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 45, base_baud = 6250000) is a 16550A
      [    1.016187] printk: console [ttyS0] enabled
      [    1.016187] printk: console [ttyS0] enabled
      [    1.024523] printk: bootconsole [earlycon0] disabled
      [    1.024523] printk: bootconsole [earlycon0] disabled
      [    1.036006] brd: module loaded
      [    1.039334] at24 0-0051: supply vcc not found, using dummy regulator
      [    1.046955] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
      [    1.054822] spi_altera ff200040.spi: regoff 0, irq 48
      [    1.061311] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
      [    1.068838] libphy: Fixed MDIO Bus: probed
      [    1.073423] CAN device driver interface
      [    1.077462] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.084067] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
      [    1.090346] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
      [    1.097031] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
      [    1.103415] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
      [    1.110596] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.116850] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
      [    1.122942] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    1.129707] stmmaceth ff800000.ethernet:     DWMAC1000
      [    1.134582] stmmaceth ff800000.ethernet: DMA HW capability register supported
      [    1.141693] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
      [    1.148794] stmmaceth ff800000.ethernet: COE Type 2
      [    1.153656] stmmaceth ff800000.ethernet: TX Checksum insertion supported
      [    1.160327] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
      [    1.166916] stmmaceth ff800000.ethernet: Enabled extended descriptors
      [    1.173333] stmmaceth ff800000.ethernet: Ring mode enabled
      [    1.178793] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    1.186433] stmmaceth ff800000.ethernet: device MAC address 36:e8:4c:f3:8d:b4
      [    1.201649] libphy: stmmac: probed
      [    1.205053] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
      [    1.218691] usbcore: registered new interface driver asix
      [    1.224149] usbcore: registered new interface driver ax88179_178a
      [    1.230238] usbcore: registered new interface driver cdc_ether
      [    1.236097] usbcore: registered new interface driver net1080
      [    1.241767] usbcore: registered new interface driver cdc_subset
      [    1.247680] usbcore: registered new interface driver zaurus
      [    1.253280] usbcore: registered new interface driver cdc_ncm
      [    1.259404] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
      [    1.266610] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
      [    1.273934] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    1.281592] dwc2 ffb00000.usb: DWC OTG Controller
      [    1.286297] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
      [    1.293363] dwc2 ffb00000.usb: irq 46, io mem 0xffb00000
      [    1.298803] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
      [    1.307049] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.314246] usb usb1: Product: DWC OTG Controller
      [    1.318930] usb usb1: Manufacturer: Linux 5.10.0-97993-ga7064610e8f3 dwc2_hsotg
      [    1.326211] usb usb1: SerialNumber: ffb00000.usb
      [    1.331273] hub 1-0:1.0: USB hub found
      [    1.335058] hub 1-0:1.0: 1 port detected
      [    1.339586] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    1.346104] ehci-pci: EHCI PCI platform driver
      [    1.351022] usbcore: registered new interface driver uas
      [    1.356404] usbcore: registered new interface driver usb-storage
      [    1.362478] usbcore: registered new interface driver usbserial_generic
      [    1.368991] usbserial: USB Serial support registered for generic
      [    1.375001] usbcore: registered new interface driver ftdi_sio
      [    1.380740] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.388090] usbcore: registered new interface driver upd78f0730
      [    1.394006] usbserial: USB Serial support registered for upd78f0730
      [    1.403860] rtc-ds1307 0-0068: SET TIME!
      [    1.412067] rtc-ds1307 0-0068: registered as rtc0
      [    1.416845] i2c /dev entries driver
      [    1.420936] usbcore: registered new interface driver uvcvideo
      [    1.426684] USB Video Class driver (1.1.1)
      [    1.434980] ltc2978: probe of 0-005c failed with error -121
      [    1.441253] Synopsys Designware Multimedia Card Interface Driver
      [    1.447498] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
      [    1.454179] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
      [    1.460351] dw_mmc ff808000.dwmmc0: Version ID is 270a
      [    1.465535] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 41,32 bit host data width,1024 deep fifo
      [    1.474927] mmc_host mmc0: card is polling.
      [    1.480611] ledtrig-cpu: registered to indicate activity on CPUs
      [    1.486713] usbcore: registered new interface driver usbhid
      [    1.491518] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.492268] usbhid: USB HID core driver
      [    1.507230] ad9371 spi0.1: ad9371_probe : enter
      [    1.516179] ad9528 spi0.0: supply vcc not found, using dummy regulator
      [    1.533566] random: fast init done
      [    1.580804] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.590551] mmc0: new high speed SDHC card at address aaaa
      [    1.596534] mmcblk0: mmc0:aaaa SC32G 29.7 GiB
      [    1.603785] altera-a10-fpll ff245000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
      [    1.605622]  mmcblk0: p1 p2 p3
      [    1.613782] altera-a10-fpll ff235000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
      [    1.624832] altera-a10-fpll ff225000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
      [    1.666076] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: ATX PLL calibration OK (20 ms)
      [    1.686518] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: Lane 0 TX termination and VOD calibration OK (600 us)
      [    1.718221] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: Lane 1 TX termination and VOD calibration OK (600 us)
      [    1.736838] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: Lane 2 TX termination and VOD calibration OK (600 us)
      [    1.762371] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: Lane 3 TX termination and VOD calibration OK (600 us)
      [    1.772193] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: Altera ADXCVR (17.01.a) probed
      [    1.784621] altera_adxcvr ff234000.axi-ad9371-rx-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    1.798010] altera_adxcvr ff234000.axi-ad9371-rx-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    1.807900] altera_adxcvr ff234000.axi-ad9371-rx-xcvr: Altera ADXCVR (17.01.a) probed
      [    1.820257] altera_adxcvr ff244000.axi-ad9371-rx-os-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    1.834212] altera_adxcvr ff244000.axi-ad9371-rx-os-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    1.844367] altera_adxcvr ff244000.axi-ad9371-rx-os-xcvr: Altera ADXCVR (17.01.a) probed
      [    1.853577] altera_adxcvr ff224000.axi-ad9371-tx-xcvr: Setting link rate to 122880000 (lane rate: 4915200)
      [    1.861611] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
      [    1.864263] altera_adxcvr ff234000.axi-ad9371-rx-xcvr: Setting link rate to 122880000 (lane rate: 4915200)
      [    1.870458] usbcore: registered new interface driver snd-usb-audio
      [    1.880426] altera_adxcvr ff244000.axi-ad9371-rx-os-xcvr: Setting link rate to 122880000 (lane rate: 4915200)
      [    1.887451] NET: Registered protocol family 10
      [    1.900660] Segment Routing with IPv6
      [    1.904402] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.910747] NET: Registered protocol family 17
      [    1.915215] NET: Registered protocol family 15
      [    1.919809] can: controller area network core
      [    1.924222] NET: Registered protocol family 29
      [    1.928649] can: raw protocol
      [    1.931615] can: broadcast manager protocol
      [    1.935783] can: netlink gateway - max_hops=1
      [    1.940252] 8021q: 802.1Q VLAN Support v1.8
      [    1.944463] NET: Registered protocol family 36
      [    1.948904] Key type dns_resolver registered
      [    1.953441] oprofile: no performance counters
      [    1.957874] oprofile: using timer interrupt.
      [    1.962223] ThumbEE CPU extension supported.
      [    1.966481] Registering SWP/SWPB emulation handler
      [    1.971825] ad9371 spi0.1: ad9371_probe : enter
      [    1.977547] axi-jesd204-rx ff230000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0xFF230000. Encoder 8b10b, width 4/4, lanes 2.
      [    1.989501] axi-jesd204-rx ff240000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0xFF240000. Encoder 8b10b, width 4/4, lanes 2.
      [    2.001267] axi-jesd204-tx ff220000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0xFF220000. Encoder 8b10b, width 4/4, lanes 4.
      [    2.013073] ad9371 spi0.1: ad9371_probe : enter
      [    2.801402] random: crng init done
      [    8.621922] ad9371 spi0.1: framerStatus (0x20)
      [    8.803108] ad9371 spi0.1: ad9371_probe: failed to register debugfs
      [    8.809757] ad9371 spi0.1: AD9371 Rev 4, Firmware 5.2.2 API version: 1.5.2.3566 successfully initialized
      [    8.842130] cf_axi_dds ff254000.axi-ad9371-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0xFF254000 mapped to 0xa6a60f22, probed DDS AD9371
      [    8.876361] cf_axi_adc ff250000.axi-ad9371-rx-hpc: ADI AIM (10.01.b) at 0xFF250000 mapped to 0x385ee267, probed ADC AD9371 as MASTER
      [    8.888499] of_cfs_init
      [    8.890960] of_cfs_init: OK
      [    8.894010] ALSA device list:
      [    8.896968]   No soundcards found.
      [    8.900580] dw-apb-uart ffc02100.serial1: forbid DMA for kernel console
      [    9.309025] EXT4-fs (mmcblk0p2): recovery complete
      [    9.314777] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [    9.322904] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    9.332238] devtmpfs: mounted
      [    9.339085] Freeing unused kernel memory: 1024K
      [    9.344073] Run /sbin/init as init process
      [    9.931269] systemd[1]: System time before build time, advancing clock.
      [    9.985512] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
      [   10.007376] systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 10 (buster)!

      [   10.104423] systemd[1]: Set hostname to <analog>.
      [   10.462857] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
      [   10.479877] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
      [   10.664321] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
      [   10.674012] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
      [   10.901063] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [   10.913560] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [   10.952108] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [  OK  ] Created slice system-getty.slice.
      [  OK  ] Listening on Syslog Socket.
      [  OK  ] Reached target Swap.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [  OK  ] Listening on Journal Socket.
               Starting Restore / save the current clock...
               Mounting RPC Pipe File System...
               Starting Set the console keyboard layout...
               Starting Load Kernel Modules...
      [  OK  ] Created slice User and Session Slice.
      [  OK  ] Reached target Slices.
      [  OK  ] Listening on Journal Socket (/dev/log).
               Starting Journal Service...
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on udev Control Socket.
               Starting udev Coldplug all Devices...
      [  OK  ] Started Restore / save the current clock.
      [  OK  ] Mounted RPC Pipe File System.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Started Journal Service.
      [  OK  ] Started Set the console keyboard layout.
               Starting Apply Kernel Variables...
               Mounting Kernel Configuration File System...
               Starting Remount Root and Kernel File Systems...
      [  OK  ] Started Apply Kernel Variables.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Started udev Coldplug all Devices.
               Starting Helper to synchronize boot up for ifupdown...
      [  OK  ] Started Helper to synchronize boot up for ifupdown.
      [  OK  ] Started Remount Root and Kernel File Systems.
               Starting Flush Journal to Persistent Storage...
               Starting Create System Users...
               Starting Load/Save Random Seed...
      [  OK  ] Started Load/Save Random Seed.
      [  OK  ] Started Create System Users.
      [  OK  ] Started Flush Journal to Persistent Storage.
               Starting Create Static Device Nodes in /dev...
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
               Starting Create Volatile Files and Directories...
               Starting Raise network interfaces...
               Starting Set console font and keymap...
               Starting Preprocess NFS configuration...
               Starting Tell Plymouth To Write Out Runtime Data...
      [  OK  ] Started Preprocess NFS configuration.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
      [  OK  ] Started Set console font and keymap.
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Started Create Volatile Files and Directories.
               Starting Network Time Synchronization...
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Started Update UTMP about System Boot/Shutdown.
      [  OK  ] Started Network Time Synchronization.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Listening on CUPS Scheduler.
      [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Reached target Sockets.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Reached target Paths.
      [  OK  ] Reached target Basic System.
               Starting LSB: Switch to on…nless shift key is pressed)...
               Starting System Logging Service...
      [  OK  ] Started D-Bus System Message Bus.
               Starting dphys-swapfile - …unt, and delete a swap file...
      [  OK  ] Started tof-server.service.
               Starting Login Service...
      [  OK  ] Started Regular background program processing daemon.
               Starting Check for Raspberry Pi EEPROM updates...
               Starting Modem Manager...
               Starting Avahi mDNS/DNS-SD Stack...
               Starting triggerhappy global hotkey daemon...
               Starting WPA supplicant...
               Starting rng-tools.service...
      [  OK  ] Started CUPS Scheduler.
               Starting dhcpcd on all interfaces...
               Starting Disk Manager...
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Reached target System Time Synchronized.
      [  OK  ] Started Daily man-db regeneration.
      [  OK  ] Started Daily rotation of log files.
      [  OK  ] Started Daily apt download activities.
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Reached target Timers.
      [FAILED] Failed to start rng-tools.service.
      See 'systemctl status rng-tools.service' for details.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started Check for Raspberry Pi EEPROM updates.
      [  OK  ] Started Login Service.
      [  OK  ] Started Raise network interfaces.
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started dhcpcd on all interfaces.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Reached target Network.
      [  OK  ] Started IIO Daemon.
               Starting OpenBSD Secure Shell server...
               Starting Permit User Sessions...
               Starting HTTP based time synchronization tool...
      [  OK  ] Reached target Network is Online.
               Starting Internet superserver...
               Starting /etc/rc.local Compatibility...
      [  OK  ] Started Internet superserver.
      [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started Permit User Sessions.
      [  OK  ] Started /etc/rc.local Compatibility.
               Starting Authorization Manager...
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
               Starting Manage, Install and Generate Color Profiles...
      [  OK  ] Started OpenBSD Secure Shell server.
      [  OK  ] Started Manage, Install and Generate Color Profiles.
      [  OK  ] Started Authorization Manager.

      Raspbian GNU/Linux 10 analog ttyS0

      analog login: root (automatic login)

      Last login: Mon Jan 17 16:17:12 GMT 2022 on ttyS0
      Linux analog 5.10.0-97993-ga7064610e8f3 #4699 SMP Sat Jan 29 09:17:25 GMT 2022 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      root@analog:~#
      </nowiki>

Once the boot process has completed you'll be greeted with command prompt. As a quick check if the EVAL-ADRV9008/9 was correctly recognized run the \`iio_info\` command and filter for the registered devices.

::

   <nowiki>
   Last login: Thu Jan  1 00:00:12 UTC 1970 on tty1
   Welcome to Linaro 14.04 (GNU/Linux 4.6.0-09244-g5f1195d00092-dirty armv7l)

     * Documentation:  https://wiki.analog.com/ https://ez.analog.com/

   root@analog:~# iio_info | grep :device
           iio:device0: 0-0014
           iio:device1: 0-0016
           iio:device2: ad9528-1
           iio:device3: ad9371-phy
           iio:device4: axi-ad9371-rx-obs-hpc (buffer capable)
           iio:device5: axi-ad9371-tx-hpc (buffer capable)
           iio:device6: axi-ad9371-rx-hpc (buffer capable)
   </nowiki>

If the Arria 10 SoC Development Kit is connected to a network with a DHCP server the IP address assigned to the board appears on the LCD. Alternatively you can query the IP address by running \`ifconfig eth0\` on the command line. To manually assign an IP address run \`ifconfig eth0 *IP_ADDR*\ \`.

IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that
has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP
address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``

   .. image:: ../images/shutdown.png
   :width: 300

More information
================

:doc:`ADRV9371 User Guide </wiki-migration/resources/eval/user-guides/mykonos>`

More Information
----------------

-  :doc:`ADRV9001/2 Quick Start Guides </wiki-migration/resources/eval/user-guides/adrv9002/quickstart>`

   -  :doc:`ADRV9002 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zynqmp>`
   -  :doc:`ADRV9002 Zynq SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zynq>`
   -  :doc:`ADRV9002 Zynq Zed Board Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zed>`
   -  :doc:`ADRV9002 Arria10 SoC Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/a10soc>`

-  :doc:`ADRV9001/ADRV9002 HDL Reference Design </wiki-migration/resources/eval/user-guides/adrv9002/reference_hdl>`

   -  :doc:`AXI_ADRV9001/AXI_ADRV9002 Interface Core </wiki-migration/resources/eval/user-guides/adrv9002/axi_adrv9002>`
   -  :doc:`Building HDL how-to, ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`

-  :doc:`ADRV9002 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002-customization>`
-  :doc:`ADRV9002 Integrated Dual RF Transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

Software resources
------------------

-  :doc:`ADRV9002 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002-customization>`
-  :doc:`ADRV9002 Integrated Dual RF Transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`
