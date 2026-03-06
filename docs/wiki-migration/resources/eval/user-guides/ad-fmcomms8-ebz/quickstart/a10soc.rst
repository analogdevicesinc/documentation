AD-FMCOMMS8-EBZ Arria10 SoC Quick Start Guide
=============================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/quickstart/fmcomms8_a10soc.jpeg
   :align: center
   :width: 600px

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the :adi:`AD-FMCOMMS8-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcomms8-ebz.html>` on:

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__ Rev. C or later

Instructions on how to build the Zynq Linux kernel and devicetrees from source can be found here:

-  :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  :doc:`Altera SOC - Build Preloader and Bootloader Image </wiki-migration/resources/tools-software/linux-software/altera_soc_images>`

Required Software
-----------------

-  SD Card 16GB image using the instructions here: :doc:`SDCARD for Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.
-   Copy next boot files from <fc #ff0000>\ ``socfpga_arria10_socdk_fmcomms8``\ </fc> directory directly on SD Card ``BOOT`` partition :

   -  ``socfpga_arria10_socdk.rbf``
   -  ``socfpga_arria10_socdk_sdmmc.dtb``
   -  ``zImage`` (from ``socfpga_arria10-common`` folder)

-  Write preloader_bootloader.bin from <fc #ff0000>\ ``socfpga_arria10_socdk_fmcomms8``\ </fc> folder on third SD Card partition:

::

       root@raspberrypi:~# lsblk
       NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
       sda           8:0    1 14.9G  0 disk 
       ├─sda1        8:1    1    1G  0 part /media/pi/BOOT
       ├─sda2        8:2    1  7.6G  0 part /media/pi/rootfs
       └─sda3        8:3    1    4M  0 part 
       root@raspberrypi:~# dd if="./preloader_bootloader.bin" of="/dev/sda3" bs=512
       2048+0 records in
       2048+0 records out
       1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.25035 s, 4.2 MB/s

-  UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__ Rev. C or later
-  :doc:`AD-FMCOMMS8-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz>` daughterboard
-  Mini-USB cable
-  Ethernet cable
-  Optionally USB keyboard, mouse and a Display Port compatible monitor

.. esd-warning::


FMC Pin Connection Configuration Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   To be compatible with the AD-FMCOMMS8-EBZ daughterboard the Arria10 SoC Development Kit requires a minor rework.

   
   In the default configuration of the Arria10 SoC Development Kit some of the FMC header pins are connected to a dedicated clock chip. To be compatible with the AD-FMCOMMS8-EBZ daughterboard, these pins need to be connected directly to the FPGA.


The connection of those pins can be changed by moving the position of six zero Ohm resistors:

-  R575 to R574
-  R576 to R577
-  R612 to R610
-  R613 to R611
-  R621 to R620
-  R633 to R632

These resistors can be found on the backside of the Arria10 SoC Development Kit underneath the FMC A connector (J29). The following picture shows the required configuration to be compatible with the AD-FMCOMMS8-EBZ.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/quickstart/a10soc_fmc_rework_6r.jpg
   :align: center
   :width: 400px

Testing
=======

-  Connect the :adi:`AD-FMCOMMS8-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcomms8-ebz.html>` board to the FMCA carrier socket.
-  Connect USB UART (Mini USB) to your host PC.
-  Insert SD card into socket.
-  Configure\ `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__ for SD Card booting (Set the Jumpers and Switches accordingly).
-  Turn on the power switch on the FPGA board.
-  Observe kernel and serial console messages on your terminal.

Messages
--------



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   

   .. raw:: html

      <details><summary>Boot log (click to expand)</summary>

   ::
   
      U-Boot 2014.10-00334-gf7a7e26-dirty (Jun 30 2021 - 18:17:34), Build: jenkins-master-hdl_jobs_for_linux-projects-fmcomms8.a10soc-125
   
      CPU   : Altera SOCFPGA Arria 10 Platform
      BOARD : Altera SOCFPGA Arria 10 Dev Kit
      I2C:   ready
      DRAM:  WARNING: Caches not enabled
      SOCFPGA DWMMC: 0
      FPGA: writing socfpga_arria10_socdk.rbf ...
      Full Configuration Succeeded.
      DDRCAL: Success
      INFO  : Skip relocation as SDRAM is non secure memory
      Reserving 2048 Bytes for IRQ stack at: ffe386e8
      DRAM  : 1 GiB
      WARNING: Caches not enabled
      MMC:   *** Warning - bad CRC, using default environment
   
      In:    serial
      Out:   serial
      Err:   serial
      Model: SOCFPGA Arria10 Dev Kit
      Net:   dwmac.ff800000
      Hit any key to stop autoboot:  0
      FPGA must be in Early Release mode to program core.
      fpga - loadable FPGA image support
   
      ** Unable to read file u-boot.scr **
      7662488 bytes read in 381 ms (19.2 MiB/s)
      47522 bytes read in 17 ms (2.7 MiB/s)
      FPGA BRIDGES: enable
      Kernel image @ 0x010000 [ 0x000000 - 0x74eb98 ]
      ## Flattened Device Tree blob at 00000100
         Booting using the fdt blob at 0x000100
         Loading Device Tree to 01ff1000, end 01fff9a1 ... OK
   
      Starting kernel ...
   
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 5.4.0-00475-gc588ee4 (jenkins@romlxbuild1.adlk.analog.com) (gcc version 9.2.0 (GCC)) #1847 SMP Fri Jul 2 09:07:42 IST 2021
      [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Altera SOCFPGA Arria 10
      [    0.000000] Memory policy: Data cache writealloc
      [    0.000000] cma: Reserved 128 MiB at 0x38000000
      [    0.000000] percpu: Embedded 19 pages/cpu s45196 r8192 d24436 u77824
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
      [    0.000000] Kernel command line: console=ttyS0,115200 root=/dev/mmcblk0p2 rw rootwait
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] Memory: 885384K/1048576K available (12288K kernel code, 1132K rwdata, 7240K rodata, 1024K init, 173K bss, 32120K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 39905 entries in 78 pages
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      [    0.000000] L2C-310 erratum 769419 enabled
      [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
      [    0.000000] L2C-310: enabling full line of zeros but not enabled in Cortex-A9
      [    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
      [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
      [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
      [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76460001
      [    0.000000] random: get_random_bytes called from start_kernel+0x328/0x4dc with crng_init=0
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000005] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.000013] Switching to timer-based delay loop, resolution 10ns
      [    0.000211] Console: colour dummy device 80x30
      [    0.000241] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.000251] pid_max: default: 32768 minimum: 301
      [    0.000367] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000380] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000932] CPU: Testing write buffer coherency: ok
      [    0.000959] CPU0: Spectre v2: using BPIALL workaround
      [    0.001183] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.001694] Setting up static identity map for 0x100000 - 0x100060
      [    0.001810] rcu: Hierarchical SRCU implementation.
      [    0.002065] smp: Bringing up secondary CPUs ...
      [    0.002664] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.002670] CPU1: Spectre v2: using BPIALL workaround
      [    0.002785] smp: Brought up 1 node, 2 CPUs
      [    0.002794] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.002799] CPU: All CPU(s) started in SVC mode.
      [    0.003280] devtmpfs: initialized
      [    0.009355] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.009544] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.009561] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.013437] NET: Registered protocol family 16
      [    0.015305] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.016090] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.016098] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.030610] altera_gpio ff200020.gpio: IRQ index 0 not found
      [    0.031515] vgaarb: loaded
      [    0.031794] SCSI subsystem initialized
      [    0.031963] usbcore: registered new interface driver usbfs
      [    0.031997] usbcore: registered new interface driver hub
      [    0.032041] usbcore: registered new device driver usb
      [    0.032169] usb_phy_generic soc:usbphy: soc:usbphy supply vcc not found, using dummy regulator
      [    0.033176] mc: Linux media interface: v0.10
      [    0.033206] videodev: Linux video capture interface: v2.00
      [    0.033284] pps_core: LinuxPPS API ver. 1 registered
      [    0.033290] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.033303] PTP clock support registered
      [    0.033706] jesd204: created con: id=0, topo=0, link=0, /soc/bridge@ff200000/axi-adrv9009-tx-xcvr@24000 <-> /soc/bridge@ff200000/axi-jesd204-tx@20000
      [    0.033723] jesd204: created con: id=1, topo=0, link=2, /soc/bridge@ff200000/axi-adrv9009-rx-os-xcvr@44000 <-> /soc/bridge@ff200000/axi-jesd204-rx@40000
      [    0.033738] jesd204: created con: id=2, topo=0, link=1, /soc/bridge@ff200000/axi-adrv9009-rx-xcvr@34000 <-> /soc/bridge@ff200000/axi-jesd204-rx@30000
      [    0.033752] jesd204: created con: id=3, topo=0, link=0, /soc/bridge@ff200000/spi@40/hmc7044-fmc@2 <-> /soc/bridge@ff200000/axi-adrv9009-tx-xcvr@24000
      [    0.033765] jesd204: created con: id=4, topo=0, link=2, /soc/bridge@ff200000/spi@40/hmc7044-fmc@2 <-> /soc/bridge@ff200000/axi-adrv9009-rx-os-xcvr@44000
      [    0.033777] jesd204: created con: id=5, topo=0, link=1, /soc/bridge@ff200000/spi@40/hmc7044-fmc@2 <-> /soc/bridge@ff200000/axi-adrv9009-rx-xcvr@34000
      [    0.033815] jesd204: created con: id=6, topo=0, link=1, /soc/bridge@ff200000/axi-jesd204-rx@30000 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy-d@1
      [    0.033835] jesd204: created con: id=7, topo=0, link=2, /soc/bridge@ff200000/axi-jesd204-rx@40000 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy-d@1
      [    0.033855] jesd204: created con: id=8, topo=0, link=0, /soc/bridge@ff200000/axi-jesd204-tx@20000 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy-d@1
      [    0.033920] jesd204: created con: id=9, topo=0, link=1, /soc/bridge@ff200000/spi@40/adrv9009-phy-d@1 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0
      [    0.033958] jesd204: created con: id=10, topo=0, link=2, /soc/bridge@ff200000/spi@40/adrv9009-phy-d@1 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0
      [    0.034003] jesd204: created con: id=11, topo=0, link=0, /soc/bridge@ff200000/spi@40/adrv9009-phy-d@1 <-> /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0
      [    0.034032] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0: JESD204[0] transition uninitialized -> initialized
      [    0.034040] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0: JESD204[1] transition uninitialized -> initialized
      [    0.034047] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0: JESD204[2] transition uninitialized -> initialized
      [    0.034052] jesd204: found 9 devices and 1 topologies
      [    0.034089] FPGA manager framework
      [    0.034165] Advanced Linux Sound Architecture Driver Initialized.
      [    0.034897] clocksource: Switched to clocksource timer1
      [    0.435085] NET: Registered protocol family 2
      [    0.435617] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
      [    0.435642] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.435706] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.435814] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.435952] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.435993] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.436162] NET: Registered protocol family 1
      [    0.436558] RPC: Registered named UNIX socket transport module.
      [    0.436567] RPC: Registered udp transport module.
      [    0.436572] RPC: Registered tcp transport module.
      [    0.436576] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.436587] PCI: CLS 0 bytes, default 64
      [    0.437866] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.443139] NFS: Registering the id_resolver key type
      [    0.443164] Key type id_resolver registered
      [    0.443170] Key type id_legacy registered
      [    0.443181] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
      [    0.443758] ntfs: driver 2.1.32 [Flags: R/W].
      [    0.443978] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.475713] bounce: pool size: 64 pages
      [    0.475728] io scheduler mq-deadline registered
      [    0.475735] io scheduler kyber registered
      [    0.480388] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
      [    0.480402] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    0.482788] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.483620] printk: console [ttyS0] disabled
      [    0.483668] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 37, base_baud = 6250000) is a 16550A
      [    1.272240] printk: console [ttyS0] enabled
      [    1.277949] brd: module loaded
      [    1.282464] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
      [    1.318092] spi_altera ff200040.spi: base (ptrval), irq 40
      [    1.324346] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
      [    1.331474] libphy: Fixed MDIO Bus: probed
      [    1.336004] CAN device driver interface
      [    1.340048] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.346654] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
      [    1.352896] socfpga-dwmac ff800000.ethernet: PTP uses main clock
      [    1.358907] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
      [    1.365588] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
      [    1.371933] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
      [    1.379125] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.385380] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
      [    1.391254] stmmaceth ff800000.ethernet: PTP uses main clock
      [    1.397056] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    1.403819] stmmaceth ff800000.ethernet:     DWMAC1000
      [    1.408700] stmmaceth ff800000.ethernet: DMA HW capability register supported
      [    1.415824] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
      [    1.422927] stmmaceth ff800000.ethernet: COE Type 2
      [    1.427790] stmmaceth ff800000.ethernet: TX Checksum insertion supported
      [    1.434460] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
      [    1.441050] stmmaceth ff800000.ethernet: Enabled extended descriptors
      [    1.447469] stmmaceth ff800000.ethernet: Ring mode enabled
      [    1.452929] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    1.468280] libphy: stmmac: probed
      [    1.471677] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
      [    1.485048] usbcore: registered new interface driver asix
      [    1.490460] usbcore: registered new interface driver ax88179_178a
      [    1.496562] usbcore: registered new interface driver cdc_ether
      [    1.502397] usbcore: registered new interface driver net1080
      [    1.508069] usbcore: registered new interface driver cdc_subset
      [    1.513982] usbcore: registered new interface driver zaurus
      [    1.519572] usbcore: registered new interface driver cdc_ncm
      [    1.525710] dwc2 ffb00000.usb: ffb00000.usb supply vusb_d not found, using dummy regulator
      [    1.533990] dwc2 ffb00000.usb: ffb00000.usb supply vusb_a not found, using dummy regulator
      [    1.542485] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    1.550239] dwc2 ffb00000.usb: DWC OTG Controller
      [    1.554983] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
      [    1.562022] dwc2 ffb00000.usb: irq 38, io mem 0xffb00000
      [    1.567466] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
      [    1.575713] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.582902] usb usb1: Product: DWC OTG Controller
      [    1.587599] usb usb1: Manufacturer: Linux 5.4.0-00475-gc588ee4 dwc2_hsotg
      [    1.594356] usb usb1: SerialNumber: ffb00000.usb
      [    1.599369] hub 1-0:1.0: USB hub found
      [    1.603133] hub 1-0:1.0: 1 port detected
      [    1.607671] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    1.614170] ehci-pci: EHCI PCI platform driver
      [    1.618951] usbcore: registered new interface driver uas
      [    1.624301] usbcore: registered new interface driver usb-storage
      [    1.630365] usbcore: registered new interface driver usbserial_generic
      [    1.636900] usbserial: USB Serial support registered for generic
      [    1.642900] usbcore: registered new interface driver ftdi_sio
      [    1.648645] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.655987] usbcore: registered new interface driver upd78f0730
      [    1.661896] usbserial: USB Serial support registered for upd78f0730
      [    1.675514] rtc-ds1307 0-0068: registered as rtc0
      [    1.680290] i2c /dev entries driver
      [    1.684455] usbcore: registered new interface driver uvcvideo
      [    1.690204] USB Video Class driver (1.1.1)
      [    1.696941] ltc2978: probe of 0-005c failed with error -121
      [    1.703126] Synopsys Designware Multimedia Card Interface Driver
      [    1.709335] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
      [    1.716108] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
      [    1.722266] dw_mmc ff808000.dwmmc0: Version ID is 270a
      [    1.727435] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 31,32 bit host data width,1024 deep fifo
      [    1.736712] mmc_host mmc0: card is polling.
      [    1.753501] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.811082] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.820832] mmc0: new high speed SDHC card at address 0007
      [    1.826995] mmcblk0: mmc0:0007 SD16G 14.4 GiB
      [    1.833923]  mmcblk0: p1 p2 p3
      [    1.984905] altr_a10sr spi1.0: SPI transfer timed out
      [    1.989952] spi_master spi1: failed to transfer one message from queue
      [    2.204896] altr_a10sr spi1.0: SPI transfer timed out
      [    2.209933] spi_master spi1: failed to transfer one message from queue
      [    2.424895] altr_a10sr spi1.0: SPI transfer timed out
      [    2.429929] spi_master spi1: failed to transfer one message from queue
      [    2.644896] altr_a10sr spi1.0: SPI transfer timed out
      [    2.649930] spi_master spi1: failed to transfer one message from queue
      [    2.656677] ledtrig-cpu: registered to indicate activity on CPUs
      [    2.662799] usbcore: registered new interface driver usbhid
      [    2.668366] usbhid: USB HID core driver
      [    2.673347] ad7291: probe of 0-002f failed with error -5
      [    2.679679] adrv9009 spi0.0: adrv9009_probe : enter
      [    2.685424] adrv9009 spi0.1: adrv9009_probe : enter
      [    2.715861] random: fast init done
      [    2.743900] jesd204: /soc/bridge@ff200000/spi@40/hmc7044-fmc@2,jesd204:2,parent=spi0.2: Using as SYSREF provider
      [    2.760781] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    2.773992] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    2.787640] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr: Lane 2 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    2.801156] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr: Lane 3 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    3.812819] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr: Link activation error:
      [    3.820105] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr:     Link PLL not locked
      [    3.827216] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr:     Lane 0 transceiver not ready
      [    3.835105] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr:     Lane 1 transceiver not ready
      [    3.842986] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr:     Lane 2 transceiver not ready
      [    3.850878] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr:     Lane 3 transceiver not ready
      [    3.858796] altera_adxcvr ff234000.axi-adrv9009-rx-xcvr: Altera ADXCVR (17.01.a) probed
      [    3.871277] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    3.884991] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    3.898850] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 2 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    3.912480] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 3 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    4.924406] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Link activation error:
      [    4.931949] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Link PLL not locked
      [    4.939319] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 0 transceiver ready
      [    4.947125] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 1 transceiver ready
      [    4.954927] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 2 transceiver ready
      [    4.962722] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 3 transceiver ready
      [    4.970545] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Altera ADXCVR (17.01.a) probed
      [    5.009595] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: ATX PLL calibration OK (20 ms)
      [    5.027595] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 0 TX termination and VOD calibration OK (600 us)
      [    5.047063] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 1 TX termination and VOD calibration OK (600 us)
      [    5.068254] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 2 TX termination and VOD calibration OK (600 us)
      [    5.093493] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 3 TX termination and VOD calibration OK (600 us)
      [    5.116751] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 4 TX termination and VOD calibration OK (600 us)
      [    5.135770] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 5 TX termination and VOD calibration OK (600 us)
      [    5.158688] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 6 TX termination and VOD calibration OK (600 us)
      [    5.181097] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 7 TX termination and VOD calibration OK (600 us)
      [    6.192671] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Link activation error:
      [    6.199955] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Link PLL not locked
      [    6.207065] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 0 transceiver ready
      [    6.214599] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 1 transceiver ready
      [    6.222140] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 2 transceiver ready
      [    6.229682] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 3 transceiver ready
      [    6.237223] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 4 transceiver ready
      [    6.244757] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 5 transceiver ready
      [    6.252303] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 6 transceiver ready
      [    6.259844] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 7 transceiver ready
      [    6.267408] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Altera ADXCVR (17.01.a) probed
      [    6.276564] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
      [    6.283867] usbcore: registered new interface driver snd-usb-audio
      [    6.291621] oprofile: no performance counters
      [    6.296071] oprofile: using timer interrupt.
      [    6.300390] drop_monitor: Initializing network drop monitor service
      [    6.307286] NET: Registered protocol family 10
      [    6.312417] Segment Routing with IPv6
      [    6.316149] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    6.322481] NET: Registered protocol family 17
      [    6.326943] NET: Registered protocol family 15
      [    6.331516] can: controller area network core (rev 20170425 abi 9)
      [    6.337741] NET: Registered protocol family 29
      [    6.342166] can: raw protocol (rev 20170425)
      [    6.346428] can: broadcast manager protocol (rev 20170425 t)
      [    6.352064] can: netlink gateway (rev 20190810) max_hops=1
      [    6.357688] 8021q: 802.1Q VLAN Support v1.8
      [    6.361888] NET: Registered protocol family 36
      [    6.366341] Key type dns_resolver registered
      [    6.370675] ThumbEE CPU extension supported.
      [    6.374940] Registering SWP/SWPB emulation handler
      [    6.383416] adrv9009 spi0.0: adrv9009_probe : enter
      [    6.394026] adrv9009 spi0.1: adrv9009_probe : enter
      [    6.446153] cf_axi_dds ff254000.axi-adrv9009-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0xFF254000 mapped to 0x(ptrval), probed DDS ADRV9009-X2
      [    6.460933] axi-jesd204-rx ff230000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0xFF230000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
      [    6.473969] axi-jesd204-rx ff240000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0xFF240000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
      [    6.486881] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition initialized -> probed
      [    6.498933] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition initialized -> probed
      [    6.510972] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition initialized -> probed
      [    6.523019] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition probed -> idle
      [    6.534451] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition probed -> idle
      [    6.545890] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition probed -> idle
      [    6.557330] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition idle -> device_init
      [    6.569194] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition idle -> device_init
      [    6.581057] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition idle -> device_init
      [    6.592932] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition device_init -> link_init
      [    6.605228] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition device_init -> link_init
      [    6.617522] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition device_init -> link_init
      [    6.629832] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_init -> link_supported
      [    6.642387] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition link_init -> link_supported
      [    6.654946] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_init -> link_supported
      [    6.667928] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_supported -> link_pre_setup
      [    6.680924] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition link_supported -> link_pre_setup
      [    6.693913] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_supported -> link_pre_setup
      [    6.706908] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_pre_setup -> clk_sync_stage1
      [    6.719981] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition link_pre_setup -> clk_sync_stage1
      [    6.733054] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_pre_setup -> clk_sync_stage1
      [    6.746135] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.759299] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.772460] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.785627] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.798787] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.811946] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.825108] jesd204: /soc/bridge@ff200000/axi-jesd204-rx@30000,jesd204:6,parent=ff230000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 4, Link[1] lanes 2
      [    6.840785] jesd204: /soc/bridge@ff200000/axi-jesd204-rx@40000,jesd204:7,parent=ff240000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 4, Link[2] lanes 2
      [    6.859736] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    6.873476] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    6.887372] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 2 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    6.900868] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Lane 3 CDR/CMU PLL & RX offset calibration OK (600 us)
      [    7.912785] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr: Link activation error:
      [    7.920327] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Link PLL not locked
      [    7.927695] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 0 transceiver not ready
      [    7.935840] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 1 transceiver not ready
      [    7.943980] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 2 transceiver not ready
      [    7.952124] altera_adxcvr ff244000.axi-adrv9009-rx-os-xcvr:  Lane 3 transceiver not ready
      [    7.960284] jesd204: /soc/bridge@ff200000/axi-jesd204-tx@20000,jesd204:8,parent=ff220000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 8, Link[0] lanes 4
      [    8.005980] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: ATX PLL calibration OK (20 ms)
      [    8.024852] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 0 TX termination and VOD calibration OK (600 us)
      [    8.048319] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 1 TX termination and VOD calibration OK (600 us)
      [    8.076093] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 2 TX termination and VOD calibration OK (600 us)
      [    8.110178] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 3 TX termination and VOD calibration OK (600 us)
      [    8.138200] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 4 TX termination and VOD calibration OK (600 us)
      [    8.160214] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 5 TX termination and VOD calibration OK (600 us)
      [    8.192103] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 6 TX termination and VOD calibration OK (600 us)
      [    8.222638] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Lane 7 TX termination and VOD calibration OK (600 us)
      [    9.234207] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr: Link activation error:
      [    9.241488] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Link PLL not locked
      [    9.248596] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 0 transceiver ready
      [    9.256139] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 1 transceiver ready
      [    9.263674] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 2 transceiver ready
      [    9.271213] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 3 transceiver ready
      [    9.278753] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 4 transceiver ready
      [    9.286293] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 5 transceiver ready
      [    9.293826] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 6 transceiver ready
      [    9.301366] altera_adxcvr ff224000.axi-adrv9009-tx-xcvr:     Lane 7 transceiver ready
      [    9.308918] adrv9009 spi0.1: ADIHAL_resetHw
      [    9.654874] adrv9009 spi0.0: ADIHAL_resetHw
      [   10.000779] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition clk_sync_stage3 -> link_setup
      [   10.013514] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition clk_sync_stage3 -> link_setup
      [   10.026243] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition clk_sync_stage3 -> link_setup
      [   10.039217] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_setup -> opt_setup_stage1
      [   10.052037] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition link_setup -> opt_setup_stage1
      [   10.064851] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_setup -> opt_setup_stage1
      [   10.090788] random: crng init done
      [   16.230234] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage1 -> opt_setup_stage2
      [   16.243576] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition opt_setup_stage1 -> opt_setup_stage2
      [   16.256911] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage1 -> opt_setup_stage2
      [   16.270491] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage2 -> opt_setup_stage3
      [   16.283830] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition opt_setup_stage2 -> opt_setup_stage3
      [   16.297164] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage2 -> opt_setup_stage3
      [   16.310874] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage3 -> opt_setup_stage4
      [   16.324211] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition opt_setup_stage3 -> opt_setup_stage4
      [   16.337548] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage3 -> opt_setup_stage4
      [   21.353349] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage4 -> opt_setup_stage5
      [   21.366687] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition opt_setup_stage4 -> opt_setup_stage5
      [   21.380020] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage4 -> opt_setup_stage5
      [   21.393990] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage5 -> clocks_enable
      [   21.407069] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition opt_setup_stage5 -> clocks_enable
      [   21.420143] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage5 -> clocks_enable
      [   21.433844] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition clocks_enable -> link_enable
      [   21.446494] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition clocks_enable -> link_enable
      [   21.459136] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition clocks_enable -> link_enable
      [   21.565472] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_enable -> link_running
      [   21.578032] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition link_enable -> link_running
      [   21.590588] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_enable -> link_running
      [   21.606494] adrv9009 spi0.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   21.622206] adrv9009 spi0.0: adrv9009_info: adrv9009-x2 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   21.634854] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_running -> opt_post_running_stage
      [   21.648361] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[1] transition link_running -> opt_post_running_stage
      [   21.661866] jesd204: /soc/bridge@ff200000/spi@40/adrv9009-phy-c@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_running -> opt_post_running_stage
      [   21.675396] axi-jesd204-tx ff220000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0xFF220000. Encoder 8b10b, width 4/4, lanes 8, jesd204-fsm.
      [   21.708701] cf_axi_adc ff250000.axi-adrv9009-rx-hpc: ADI AIM (10.01.b) at 0xFF250000 mapped to 0x5eb60ce1, probed ADC ADRV9009-X2 as MASTER
      [   21.721402] of_cfs_init
      [   21.723872] of_cfs_init: OK
      [   21.726946] ALSA device list:
      [   21.729901]   No soundcards found.
      [   21.733482] ttyS0 - failed to request DMA
      [   21.767097] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [   21.775233] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [   21.790678] devtmpfs: mounted
      [   21.796445] Freeing unused kernel memory: 1024K
      [   21.801290] Run /sbin/init as init process
      [   22.475184] systemd[1]: System time before build time, advancing clock.
      [   22.546767] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
      [   22.568629] systemd[1]: Detected architecture arm.
   
      Welcome to Kuiper GNU/Linux 10 (buster)!
   
      [   22.645923] systemd[1]: Set hostname to <analog>.
      [   23.028778] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
      [   23.045972] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
      [   23.228395] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
      [   23.238082] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
      [   23.461171] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [   23.495456] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [   23.525477] systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [  OK  ] Created slice User and Session Slice.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on Journal Socket.
               Starting Set the console keyboard layout...
               Mounting Kernel Debug File System...
               Starting Load Kernel Modules...
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Listening on Journal Socket (/dev/log).
      [  OK  ] Reached target Slices.
      [  OK  ] Reached target Swap.
               Mounting RPC Pipe File System...
      [  OK  ] Listening on udev Control Socket.
               Starting Journal Service...
      [  OK  ] Created slice system-serial\x2dgetty.slice.
               Starting Restore / save the current clock...
      [  OK  ] Created slice system-getty.slice.
               Starting udev Coldplug all Devices...
      [  OK  ] Started Journal Service.
      [  OK  ] Started Set the console keyboard layout.
      [  OK  ] Mounted Kernel Debug File System.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Mounted RPC Pipe File System.
      [  OK  ] Started Restore / save the current clock.
               Starting Remount Root and Kernel File Systems...
               Mounting Kernel Configuration File System...
               Starting Apply Kernel Variables...
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Started Apply Kernel Variables.
      [  OK  ] Started udev Coldplug all Devices.
               Starting Helper to synchronize boot up for ifupdown...
      [  OK  ] Started Remount Root and Kernel File Systems.
      [  OK  ] Started Helper to synchronize boot up for ifupdown.
               Starting Flush Journal to Persistent Storage...
               Starting Create System Users...
               Starting Load/Save Random Seed...
      [  OK  ] Started Create System Users.
      [  OK  ] Started Load/Save Random Seed.
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
      [  OK  ] Found device /dev/disk/by-partuuid/9bdcdc9c-01.
               Starting File System Check…isk/by-partuuid/9bdcdc9c-01...
      [  OK  ] Started File System Check Daemon to report status.
      [  OK  ] Started File System Check …/disk/by-partuuid/9bdcdc9c-01.
               Mounting /boot...
      [  OK  ] Mounted /boot.
      [  OK  ] Reached target Local File Systems.
               Starting Raise network interfaces...
               Starting Set console font and keymap...
               Starting Tell Plymouth To Write Out Runtime Data...
               Starting Preprocess NFS configuration...
               Starting Create Volatile Files and Directories...
      [  OK  ] Started Preprocess NFS configuration.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Started Set console font and keymap.
      [  OK  ] Started Create Volatile Files and Directories.
               Starting Network Time Synchronization...
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Started Update UTMP about System Boot/Shutdown.
      [  OK  ] Started Network Time Synchronization.
               Starting Load Kernel Modules...
               Starting Tell Plymouth To Write Out Runtime Data...
      [  OK  ] Reached target System Time Synchronized.
      [  OK  ] Started Raise network interfaces.
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Started Daily man-db regeneration.
      [  OK  ] Started Daily rotation of log files.
      [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Reached target Paths.
      [  OK  ] Started Daily apt download activities.
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Reached target Timers.
      [  OK  ] Listening on CUPS Scheduler.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Reached target Sockets.
      [  OK  ] Reached target Basic System.
               Starting dphys-swapfile - …unt, and delete a swap file...
               Starting dhcpcd on all interfaces...
      [  OK  ] Started tof-server.service.
      [  OK  ] Started CUPS Scheduler.
               Starting System Logging Service...
               Starting Avahi mDNS/DNS-SD Stack...
      [  OK  ] Started Regular background program processing daemon.
               Starting Login Service...
               Starting Disk Manager...
               Starting Check for Raspberry Pi EEPROM updates...
               Starting rng-tools.service...
               Starting LSB: Switch to on…nless shift key is pressed)...
               Starting Modem Manager...
               Starting triggerhappy global hotkey daemon...
      [  OK  ] Started D-Bus System Message Bus.
               Starting WPA supplicant...
      [FAILED] Failed to start rng-tools.service.
      See 'systemctl status rng-tools.service' for details.
      [  OK  ] Started Login Service.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started dhcpcd on all interfaces.
      [  OK  ] Started Check for Raspberry Pi EEPROM updates.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
               Starting Authorization Manager...
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Reached target Network.
               Starting /etc/rc.local Compatibility...
               Starting HTTP based time synchronization tool...
               Starting OpenBSD Secure Shell server...
      [  OK  ] Started IIO Daemon.
               Starting Permit User Sessions...
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started Permit User Sessions.
               Starting Hold until boot process finishes up...
               Starting Light Display Manager...
      [  OK  ] Started Authorization Manager.
      [  OK  ] Started OpenBSD Secure Shell server.
   
      Raspbian GNU/Linux 10 analog ttyS0
   
      analog login: root (automatic login)
   
      Last login: Fri Jul  2 14:47:07 BST 2021 on ttyS0
      Linux analog 5.4.0-00475-gc588ee4 #1847 SMP Fri Jul 2 09:07:42 IST 2021 armv7l
   
      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.
   
      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      root@analog:~#


   .. raw:: html

      </details>

.. raw:: html

   </details>


These devices should be present:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# iio_info | grep :device
              iio:device2: hmc7044-fmc
              iio:device3: adrv9009-phy-c
              iio:device4: adrv9009-phy-d
              iio:device5: axi-adrv9009-rx-obs-hpc (buffer capable)
              iio:device6: axi-adrv9009-tx-hpc (buffer capable)
              iio:device7: axi-adrv9009-rx-hpc (buffer capable)
      root@analog:~#
          
   


For more details, check :doc:`Getting started with ad-fmcomms8-ebz </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz>`

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

:doc:`FMCOMMS8 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide>`

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


.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
