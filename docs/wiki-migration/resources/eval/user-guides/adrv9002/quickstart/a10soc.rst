ADRV9002 Arria10 SoC Quick Start Guide
======================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/quickstart/adrv9002_a10soc_quickstart.png
   :align: center
   :width: 600px

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` on:

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_ Rev. C or later

Instructions on how to build the Zynq Linux kernel and devicetrees from source can be found here:

-  :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  :doc:`Altera SOC - Build Preloader and Bootloader Image </wiki-migration/resources/tools-software/linux-software/altera_soc_images>`

Required Software
-----------------

-  SD Card 16GB image using the instructions here: :doc:`SDCARD for Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`. Use 2020_r1 or later release. (Pre-released files, built using Vivado 2020.1 can be downloaded from `here <https://wiki.analog.com/https/swdownloads.analog.com/cse/prebuilt/socfpga_arria10_socdk_adrv9002_rx2tx2.zip>`_)
-   Copy next boot files from <fc #ff0000>\ ``socfpga_arria10_socdk_adrv9002``\ </fc> directory directly on SD Card ``BOOT`` partition :

   -  ``socfpga_arria10_socdk.rbf``
   -  ``socfpga_arria10_socdk_sdmmc.dtb``
   -  ``zImage`` (from ``socfpga_arria10-common`` folder)

-  Write preloader_bootloader.bin from <fc #ff0000>\ ``socfpga_arria10_socdk_adrv9002``\ </fc> folder on third SD Card partition:

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

-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_ Rev. C or later
-  :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` daughterboard
-  Reference clock source
-  Mini-USB cable
-  Ethernet cable
-  Optionally USB keyboard, mouse and a Display Port compatible monitor


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


FMC Pin Connection Configuration Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   To be compatible with the :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` the Arria10 SoC Development Kit requires a minor rework.

   
   In the default configuration of the Arria10 SoC Development Kit some of the FMC header pins are connected to a dedicated clock chip. To be compatible with the :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` these pins need to be connected directly to the FPGA.


The connection of those pins can be changed by moving the position of four zero Ohm resistors:

-  R612 to R610
-  R613 to R611
-  R621 to R620
-  R633 to R632

These resistors can be found on the backside of the Arria10 SoC Development Kit underneath the FMC A connector (J29). The following picture shows the required configuration to be compatible with the AD-FMCDAQ2-EBZ.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/a10soc_fmc_rework.jpg
   :align: center
   :width: 400px

Testing
=======

.. warning::

   **<fc #ff0000>Before executing below steps, VADJ for FMCA must be set to 1.8V.</fc>**

   
   This can be done by changing VADJ FMCA Voltage using J42 (see below picture).
   
   On an ADRV9002 Card, there is a red LED close to the FMC connector. The role of this LED is to indicate if VADJ voltage exceeded 2.0V level. If that was the case this LED will be ON. If this LED does not turn off after few seconds after boot, then there is an issue and while the board might still operate this is exceeding the recommended level for VADJ, decreasing board lifetime and can lead to permanent damage of the IC in the worst case.

   
   |image1|

-  Connect the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` or :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` FMC board to the FMCA carrier socket -.
-  On the FMC card set switch to select clock source between:

|image2|

   -  an on-board 38.4MHz VCTCXO (default)
   -  external (thru J501) 10MHz to 1000MHz / +13dBm

-  Connect USB UART (Mini USB) to your host PC.
-  Insert SD card into socket.
-  Configure\ `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_ for SD Card booting (Set the Jumpers and Switches accordingly).
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
   
      U-Boot 2014.10-00334-gf7a7e26-dirty (Jun 30 2021 - 18:30:00), Build: jenkins-master-hdl_jobs_for_linux-projects-adrv9001.a10soc-14
   
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
      7699728 bytes read in 353 ms (20.8 MiB/s)
      22104 bytes read in 4 ms (5.3 MiB/s)
      FPGA BRIDGES: enable
      Kernel image @ 0x010000 [ 0x000000 - 0x757d10 ]
      ## Flattened Device Tree blob at 00000100
         Booting using the fdt blob at 0x000100
         Loading Device Tree to 01ff7000, end 01fff657 ... OK
   
      Starting kernel ...
   
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 5.4.0-00475-gc588ee4bed9a (dragos@debian) (gcc version 10.2.1 20201103 (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16))) #12 SMP Fri Jul 2 19:31:54 EEST 2021
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
      [    0.000000] Memory: 885444K/1048576K available (12288K kernel code, 1132K rwdata, 7180K rodata, 1024K init, 173K bss, 32060K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 38575 entries in 76 pages
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
      [    0.000000] random: get_random_bytes called from start_kernel+0x32c/0x4e4 with crng_init=0
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000005] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.000013] Switching to timer-based delay loop, resolution 10ns
      [    0.000181] Console: colour dummy device 80x30
      [    0.000210] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.000221] pid_max: default: 32768 minimum: 301
      [    0.000328] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000341] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000882] CPU: Testing write buffer coherency: ok
      [    0.000909] CPU0: Spectre v2: using BPIALL workaround
      [    0.001127] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.001626] Setting up static identity map for 0x100000 - 0x100060
      [    0.001744] rcu: Hierarchical SRCU implementation.
      [    0.001996] smp: Bringing up secondary CPUs ...
      [    0.002591] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.002597] CPU1: Spectre v2: using BPIALL workaround
      [    0.002702] smp: Brought up 1 node, 2 CPUs
      [    0.002711] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.002716] CPU: All CPU(s) started in SVC mode.
      [    0.003186] devtmpfs: initialized
      [    0.006718] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.006897] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.006913] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.010752] NET: Registered protocol family 16
      [    0.012595] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.013335] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.013343] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.027402] vgaarb: loaded
      [    0.027688] SCSI subsystem initialized
      [    0.027859] usbcore: registered new interface driver usbfs
      [    0.027894] usbcore: registered new interface driver hub
      [    0.027939] usbcore: registered new device driver usb
      [    0.028065] usb_phy_generic soc:usbphy: soc:usbphy supply vcc not found, using dummy regulator
      [    0.028903] mc: Linux media interface: v0.10
      [    0.028938] videodev: Linux video capture interface: v2.00
      [    0.028995] pps_core: LinuxPPS API ver. 1 registered
      [    0.029000] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.029017] PTP clock support registered
      [    0.029225] jesd204: found 0 devices and 0 topologies
      [    0.029263] FPGA manager framework
      [    0.029332] Advanced Linux Sound Architecture Driver Initialized.
      [    0.030073] clocksource: Switched to clocksource timer1
      [    0.427376] NET: Registered protocol family 2
      [    0.427876] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
      [    0.427900] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.427960] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.428057] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.428159] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.428205] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.428370] NET: Registered protocol family 1
      [    0.428781] RPC: Registered named UNIX socket transport module.
      [    0.428789] RPC: Registered udp transport module.
      [    0.428793] RPC: Registered tcp transport module.
      [    0.428798] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.428809] PCI: CLS 0 bytes, default 64
      [    0.430041] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.435557] NFS: Registering the id_resolver key type
      [    0.435581] Key type id_resolver registered
      [    0.435587] Key type id_legacy registered
      [    0.435598] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
      [    0.436174] ntfs: driver 2.1.32 [Flags: R/W].
      [    0.436410] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.463586] bounce: pool size: 64 pages
      [    0.463602] io scheduler mq-deadline registered
      [    0.463608] io scheduler kyber registered
      [    0.467968] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
      [    0.467982] dma-pl330 ffda1000.pdma:     DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    0.470420] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.471244] printk: console [ttyS0] disabled
      [    0.471289] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 37, base_baud = 6250000) is a 16550A
      [    1.067467] printk: console [ttyS0] enabled
      [    1.073097] brd: module loaded
      [    1.102849] spi_altera ff200040.spi: base (ptrval), irq 40
      [    1.109054] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
      [    1.116166] libphy: Fixed MDIO Bus: probed
      [    1.120690] CAN device driver interface
      [    1.124727] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.131331] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
      [    1.137572] socfpga-dwmac ff800000.ethernet: PTP uses main clock
      [    1.143578] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
      [    1.150254] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
      [    1.156600] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
      [    1.163769] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.170009] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
      [    1.175893] stmmaceth ff800000.ethernet: PTP uses main clock
      [    1.181680] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    1.188442] stmmaceth ff800000.ethernet:     DWMAC1000
      [    1.193311] stmmaceth ff800000.ethernet: DMA HW capability register supported
      [    1.200424] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
      [    1.207526] stmmaceth ff800000.ethernet: COE Type 2
      [    1.212387] stmmaceth ff800000.ethernet: TX Checksum insertion supported
      [    1.219056] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
      [    1.225643] stmmaceth ff800000.ethernet: Enabled extended descriptors
      [    1.232058] stmmaceth ff800000.ethernet: Ring mode enabled
      [    1.237518] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    1.252854] libphy: stmmac: probed
      [    1.256250] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
      [    1.269549] usbcore: registered new interface driver asix
      [    1.274986] usbcore: registered new interface driver ax88179_178a
      [    1.281080] usbcore: registered new interface driver cdc_ether
      [    1.286904] usbcore: registered new interface driver net1080
      [    1.292565] usbcore: registered new interface driver cdc_subset
      [    1.298473] usbcore: registered new interface driver zaurus
      [    1.304075] usbcore: registered new interface driver cdc_ncm
      [    1.310173] dwc2 ffb00000.usb: ffb00000.usb supply vusb_d not found, using dummy regulator
      [    1.318465] dwc2 ffb00000.usb: ffb00000.usb supply vusb_a not found, using dummy regulator
      [    1.326911] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    1.334682] dwc2 ffb00000.usb: DWC OTG Controller
      [    1.339385] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
      [    1.346455] dwc2 ffb00000.usb: irq 38, io mem 0xffb00000
      [    1.351892] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
      [    1.360135] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.367325] usb usb1: Product: DWC OTG Controller
      [    1.372017] usb usb1: Manufacturer: Linux 5.4.0-00475-gc588ee4bed9a dwc2_hsotg
      [    1.379205] usb usb1: SerialNumber: ffb00000.usb
      [    1.384214] hub 1-0:1.0: USB hub found
      [    1.387973] hub 1-0:1.0: 1 port detected
      [    1.392470] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    1.398968] ehci-pci: EHCI PCI platform driver
      [    1.403713] usbcore: registered new interface driver uas
      [    1.409051] usbcore: registered new interface driver usb-storage
      [    1.415122] usbcore: registered new interface driver usbserial_generic
      [    1.421653] usbserial: USB Serial support registered for generic
      [    1.427654] usbcore: registered new interface driver ftdi_sio
      [    1.433400] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.440742] usbcore: registered new interface driver upd78f0730
      [    1.446650] usbserial: USB Serial support registered for upd78f0730
      [    1.454450] rtc-ds1307: probe of 0-0068 failed with error -121
      [    1.460330] i2c /dev entries driver
      [    1.464473] usbcore: registered new interface driver uvcvideo
      [    1.470219] USB Video Class driver (1.1.1)
      [    1.476836] ltc2978: probe of 0-005c failed with error -121
      [    1.482999] Synopsys Designware Multimedia Card Interface Driver
      [    1.489172] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
      [    1.495848] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
      [    1.502034] dw_mmc ff808000.dwmmc0: Version ID is 270a
      [    1.507188] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 31,32 bit host data width,1024 deep fifo
      [    1.516467] mmc_host mmc0: card is polling.
      [    1.533255] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.622641] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.632388] mmc0: new high speed SDHC card at address aaaa
      [    1.638528] mmcblk0: mmc0:aaaa SB16G 14.8 GiB 
      [    1.649483]  mmcblk0: p1 p2 p3
      [    2.431855] ledtrig-cpu: registered to indicate activity on CPUs
      [    2.437975] usbcore: registered new interface driver usbhid
      [    2.443541] usbhid: USB HID core driver
      [    2.468407] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
      [    2.475657] usbcore: registered new interface driver snd-usb-audio
      [    2.483273] oprofile: no performance counters
      [    2.487701] oprofile: using timer interrupt.
      [    2.492051] drop_monitor: Initializing network drop monitor service
      [    2.498933] NET: Registered protocol family 10
      [    2.504117] Segment Routing with IPv6
      [    2.507817] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    2.514189] NET: Registered protocol family 17
      [    2.518630] NET: Registered protocol family 15
      [    2.523205] can: controller area network core (rev 20170425 abi 9)
      [    2.529410] NET: Registered protocol family 29
      [    2.533860] can: raw protocol (rev 20170425)
      [    2.538111] can: broadcast manager protocol (rev 20170425 t)
      [    2.543760] can: netlink gateway (rev 20190810) max_hops=1
      [    2.549372] 8021q: 802.1Q VLAN Support v1.8
      [    2.553586] NET: Registered protocol family 36
      [    2.558031] Key type dns_resolver registered
      [    2.562347] ThumbEE CPU extension supported.
      [    2.566603] Registering SWP/SWPB emulation handler
      [    2.595815] random: fast init done
      [    2.634372] random: crng init done
      [   11.982155] adrv9002 spi0.0: adrv9002-phy Rev 12.0, Firmware 0.16.3.8,  Stream 0.7.3.0,  API version: 48.8.7 successfully initialized
      [   11.995290] cf_axi_adc ff220000.axi-adrv9002-rx-lpc: ADI AIM (10.01.b) at 0xFF220000 mapped to 0x6a138419, probed ADC ADRV9002 as MASTER
      [   12.030682] cf_axi_dds ff22a000.axi-adrv9002-tx-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0xFF22A000 mapped to 0x913a51ba, probed DDS ADRV9002
      [   12.044681] of_cfs_init
      [   12.047142] of_cfs_init: OK
      [   12.050103] ALSA device list:
      [   12.053059]   No soundcards found.
      [   12.056640] ttyS0 - failed to request DMA
      [   12.276053] EXT4-fs (mmcblk0p2): recovery complete
      [   12.284520] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [   12.292644] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [   12.302364] devtmpfs: mounted
      [   12.309448] Freeing unused kernel memory: 1024K
      [   12.314357] Run /sbin/init as init process
      [   12.897820] systemd[1]: System time before build time, advancing clock.
      [   12.965398] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
      [   12.987283] systemd[1]: Detected architecture arm.
   
      Welcome to Kuiper GNU/Linux 10 (buster)!
   
      [   13.074023] systemd[1]: Set hostname to <analog>.
      [   13.442796] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
      [   13.459883] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
      [   13.642873] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
      [   13.652554] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
      [   13.883412] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [   13.920646] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [   13.950781] systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
               Starting Load Kernel Modules...
      [  OK  ] Listening on initctl Compatibility Named Pipe.
               Starting Set the console keyboard layout...
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [  OK  ] Listening on Journal Socket (/dev/log).
      [  OK  ] Created slice system-serial\x2dgetty.slice.
               Mounting Kernel Debug File System...
      [  OK  ] Listening on udev Control Socket.
      [  OK  ] Listening on Syslog Socket.
               Starting Restore / save the current clock...
               Starting Journal Service...
      [  OK  ] Created slice User and Session Slice.
      [  OK  ] Reached target Slices.
      [  OK  ] Reached target Swap.
               Mounting RPC Pipe File System...
               Starting udev Coldplug all Devices...
      [  OK  ] Created slice system-getty.slice.
      [  OK  ] Started Journal Service.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Started Set the console keyboard layout.
      [  OK  ] Mounted Kernel Debug File System.
      [  OK  ] Started Restore / save the current clock.
      [  OK  ] Mounted RPC Pipe File System.
               Starting Remount Root and Kernel File Systems...
               Starting Apply Kernel Variables...
               Mounting Kernel Configuration File System...
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
               Starting Create Static Device Nodes in /dev...
      [  OK  ] Started Flush Journal to Persistent Storage.
      [  OK  ] Started Create Static Device Nodes in /dev.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting udev Kernel Device Manager...
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
               Starting Create Volatile Files and Directories...
               Starting Tell Plymouth To Write Out Runtime Data...
               Starting Preprocess NFS configuration...
               Starting Set console font and keymap...
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Started Preprocess NFS configuration.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
      [  OK  ] Started Set console font and keymap.
      [  OK  ] Started Create Volatile Files and Directories.
               Starting Update UTMP about System Boot/Shutdown...
               Starting Network Time Synchronization...
      [  OK  ] Started Update UTMP about System Boot/Shutdown.
      [  OK  ] Started Network Time Synchronization.
      [  OK  ] Reached target System Time Synchronized.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on CUPS Scheduler.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Reached target Paths.
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Started Daily apt download activities.
      [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Reached target Sockets.
      [  OK  ] Reached target Basic System.
               Starting Check for Raspberry Pi EEPROM updates...
      [  OK  ] Started Regular background program processing daemon.
               Starting Disk Manager...
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Started tof-server.service.
               Starting System Logging Service...
               Starting Avahi mDNS/DNS-SD Stack...
               Starting dhcpcd on all interfaces...
               Starting rng-tools.service...
               Starting Login Service...
      [  OK  ] Started D-Bus System Message Bus.
               Starting WPA supplicant...
               Starting LSB: Switch to on…nless shift key is pressed)...
      [  OK  ] Started Daily man-db regeneration.
               Starting dphys-swapfile - …unt, and delete a swap file...
               Starting Modem Manager...
               Starting triggerhappy global hotkey daemon...
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Started Daily rotation of log files.
      [  OK  ] Reached target Timers.
      [  OK  ] Started Check for Raspberry Pi EEPROM updates.
      [FAILED] Failed to start rng-tools.service.
      See 'systemctl status rng-tools.service' for details.
      [  OK  ] Started Login Service.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started dhcpcd on all interfaces.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started Raise network interfaces.
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
               Starting Authorization Manager...
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Reached target Network.
               Starting /etc/rc.local Compatibility...
               Starting OpenBSD Secure Shell server...
               Starting Permit User Sessions...
               Starting HTTP based time synchronization tool...
      [  OK  ] Started IIO Daemon.
      [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started Permit User Sessions.
      [  OK  ] Started HTTP based time synchronization tool.
               Starting Light Display Manager...
               Starting Manage, Install and Generate Color Profiles...
               Starting Hold until boot process finishes up...
      [  OK  ] Started OpenBSD Secure Shell server.
      [  OK  ] Started Authorization Manager.
      [  OK  ] Started Manage, Install and Generate Color Profiles.
   
      Raspbian GNU/Linux 10 analog ttyS0
   
      analog login: root (automatic login)
   
      Last login: Wed Jun 30 17:58:11 BST 2021 on ttyS0
      Linux analog 5.4.0-00475-gc588ee4bed9a #12 SMP Fri Jul 2 19:31:54 EEST 2021 armv7l
   
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
   
      root@analog:~#  iio_info | grep ':device'
          iio:device0: adrv9002-phy
          iio:device1: axi-adrv9002-rx-lpc (buffer capable)
          iio:device2: axi-adrv9002-tx-lpc (buffer capable)
   


For more on device modes, check :doc:`device modes. </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`

Pyadi-iio Example
-----------------

Pyadi-iio is a python abstraction module for ADI hardware with IIO drivers to make them easier to use. For more check :git-pyadi-iio>`__. An example of using adrv9002 can be checked `here <https::`Pyadi-iio </github.com/analogdevicesinc/pyadi-iio/blob/master/examples/adrv9002_example.py>`

IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image3|

.. include:: ../common.rst .. include:: ../common.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/quickstart/adrv9002_a10soc_vadj_jumper.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/quickstart/adrv9002_vadj_led.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
