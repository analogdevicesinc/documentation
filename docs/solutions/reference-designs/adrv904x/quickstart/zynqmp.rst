ADRV904x-HB/PCBZ Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide
================================================================

.. image:: ../images/adrv904x-zcu102-quickstart.jpeg
   :width: 600

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the :adi:`ADRV904x-HB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>` on:

-  `ZCU102 <https://www.xilinx.com/ZCU102>`_

Instructions on how to build the ZynqMP / MPSoC Linux kernel and devicetrees
from source can be found here:

-  `Building the ZynqMP / MPSoC Linux kernel and devicetrees from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`_
-  `How to build the ZynqMP boot image BOOT.BIN <https://wiki.analog.com/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`_

.. tip::

   NOTE: Three jumpers must be mounted on the board on the following headers
   with the following settings:

   
   -  P209 - GPIO4_FMC
   -  P216 - GPIO11_FMC
   -  P2021 - TEST connected to GND
   

Required Software
-----------------

-  SD Card 8GB imaged using the instructions here: `Zynq & Altera SoC Quick Start Guide <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  Xilinx `ZCU102 <https://www.xilinx.com/ZCU102>`_ Rev 1.0 board
-  ADRV904x-HB/PCBZ board

   -  powered using the 12V / 3A power supply

      -  no external reference required

-  Micro-USB cable
-  Ethernet cable
-  Optionally USB keyboard mouse and a Display Port compatible monitor

Testing
=======

.. image:: ../images/zcu102.jpg
   :align: center
   :width: 900

-  Connect the ADRV904x-HB/PCBZ board to the FPGA carrier **HPC2** FMC1 socket.
-  Connect USB UART J83 (Micro USB) to your host PC.
-  Insert SD card into socket.
-  Configure ZCU102 for SD BOOT (mode SW6[4:1] switch in the position **OFF,OFF,OFF,ON** as seen in the below picture).
-  Turn on the power switch on the FPGA board.
-  Observe kernel and serial console messages on your terminal. (use the first
   ttyUSB or COM port registed)

.. image:: ../images/zcu102_1p0_bootmode.jpg
   :align: center
   :width: 400

.. esd-warning::

Messages
--------

.. container:: box bggreen

   This specifies any shell prompt running on the target

   

   .. collapsible:: Boot log (click to expand)

         ::
   
            Zynq MP First Stage Boot Loader
            Release 2023.1   Apr  4 2024  -  13:24:23
            NOTICE:  BL31: Non secure code at 0x8000000
            NOTICE:  BL31: v2.8(release):xilinx-v2023.2
            NOTICE:  BL31: Built : 13:57:32, Feb 15 2024
            PMUFW:  v1.1
   
   
            U-Boot 2018.01-21442-gf06dec3cab (Feb 15 2024 - 17:04:03 +0200) Xilinx ZynqMP ZCU102 revA, Build: jenkins-development-build_uboot-30
   
            I2C:   ready
            DRAM:  4 GiB
            EL Level:   EL2
            Chip ID:    zu9eg
            MMC:   sdhci@ff170000: 0 (SD)
            reading uboot.env
            In:    serial@ff000000
            Out:   serial@ff000000
            Err:   serial@ff000000
            Net:   ZYNQ GEM: ff0e0000, phyaddr 15, interface rgmii-id
   
            Warning: ethernet@ff0e0000 MAC addresses don't match:
            Address in ROM is          41:4c:2d:41:44:33
            Address in environment is  8a:5f:1c:0d:30:c0
            eth0: ethernet@ff0e0000
            Hit any key to stop autoboot:  0
            switch to partitions #0, OK
            mmc0 is current device
            Device: sdhci@ff170000
            Manufacturer ID: 3
            OEM: 5344
            Name: SB16G
            Tran Speed: 50000000
            Rd Block Len: 512
            SD version 3.0
            High Capacity: Yes
            Capacity: 14.8 GiB
            Bus Width: 4-bit
            Erase Group Size: 512 Bytes
            reading uEnv.txt
            407 bytes read in 20 ms (19.5 KiB/s)
            Loaded environment from uEnv.txt
            Importing environment from SD ...
            Running uenvcmd ...
            Copying Linux from SD to RAM...
             No boot file defined 
            reading system.dtb
            45552 bytes read in 27 ms (1.6 MiB/s)
            reading Image
            40565248 bytes read in 2674 ms (14.5 MiB/s)
            ## Flattened Device Tree blob at 04000000
               Booting using the fdt blob at 0x4000000
               Loading Device Tree to 000000000fff1000, end 000000000ffff1ef ... OK
   
            Starting kernel ...
   
            [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
            [    0.000000] Linux version 6.1.0-271699-g36807a05d5c8 (george@george-precision5560) (aarch64-xilinx-linux-gcc.real (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37.20210721) #388 SMP Thu May  9 22:56:56 EEST 2024
            [    0.000000] Machine model: ZynqMP ZCU102 Rev1.0
            [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff000000 (options '115200n8')
            [    0.000000] printk: bootconsole [cdns0] enabled
            [    0.000000] efi: UEFI not found.
            [    0.000000] Zone ranges:
            [    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
            [    0.000000]   DMA32    empty
            [    0.000000]   Normal   [mem 0x0000000100000000-0x000000087fffffff]
            [    0.000000] Movable zone start for each node
            [    0.000000] Early memory node ranges
            [    0.000000]   node   0: [mem 0x0000000000000000-0x000000007fffffff]
            [    0.000000]   node   0: [mem 0x0000000800000000-0x000000087fffffff]
            [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000087fffffff]
            [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
            [    0.000000] psci: probing for conduit method from DT.
            [    0.000000] psci: PSCIv1.1 detected in firmware.
            [    0.000000] psci: Using standard PSCI v0.2 function IDs
            [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
            [    0.000000] psci: SMC Calling Convention v1.2
            [    0.000000] percpu: Embedded 18 pages/cpu s34536 r8192 d31000 u73728
            [    0.000000] Detected VIPT I-cache on CPU0
            [    0.000000] CPU features: detected: ARM erratum 845719
            [    0.000000] alternatives: applying boot alternatives
            [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
            [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1 root=/dev/mmcblk0p2 rw rootwait
            [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
            [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
            [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
            [    0.000000] software IO TLB: area num 4.
            [    0.000000] software IO TLB: mapped [mem 0x000000006c000000-0x0000000070000000] (64MB)
            [    0.000000] Memory: 3753512K/4194304K available (18176K kernel code, 1726K rwdata, 16816K rodata, 2752K init, 384K bss, 178648K reserved, 262144K cma-reserved)
            [    0.000000] rcu: Hierarchical RCU implementation.
            [    0.000000] rcu:     RCU event tracing is enabled.
            [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
            [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
            [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
            [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
            [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
            [    0.000000] Root IRQ handler: gic_handle_irq
            [    0.000000] GIC: Using split EOI/Deactivate mode
            [    0.000000] rcu: srcu_init: Setting srcu_struct sizes based on contention.
            [    0.000000] arch_timer: cp15 timer(s) running at 100.00MHz (phys).
            [    0.000000] clocksource: arch_sys_counter: mask: 0x1ffffffffffffff max_cycles: 0x171024e7e0, max_idle_ns: 440795205315 ns
            [    0.000000] sched_clock: 57 bits at 100MHz, resolution 10ns, wraps every 4398046511100ns
            [    0.008393] Console: colour dummy device 80x25
            [    0.012483] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
            [    0.022839] pid_max: default: 32768 minimum: 301
            [    0.027564] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
            [    0.034787] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
            [    0.043498] rcu: Hierarchical SRCU implementation.
            [    0.047321] rcu:     Max phase no-delay instances is 1000.
            [    0.052747] EFI services will not be available.
            [    0.057160] smp: Bringing up secondary CPUs ...
            [    0.061899] Detected VIPT I-cache on CPU1
            [    0.061970] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
            [    0.062376] Detected VIPT I-cache on CPU2
            [    0.062432] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
            [    0.062820] Detected VIPT I-cache on CPU3
            [    0.062877] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
            [    0.062923] smp: Brought up 1 node, 4 CPUs
            [    0.096969] SMP: Total of 4 processors activated.
            [    0.101641] CPU features: detected: 32-bit EL0 Support
            [    0.106744] CPU features: detected: CRC32 instructions
            [    0.111901] CPU: All CPU(s) started at EL2
            [    0.115915] alternatives: applying system-wide alternatives
            [    0.122467] devtmpfs: initialized
            [    0.130037] Registered cp15_barrier emulation handler
            [    0.130091] Registered setend emulation handler
            [    0.134355] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
            [    0.143950] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
            [    0.156321] pinctrl core: initialized pinctrl subsystem
            [    0.157193] NET: Registered PF_NETLINK/PF_ROUTE protocol family
            [    0.162662] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
            [    0.168943] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
            [    0.176693] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
            [    0.184459] audit: initializing netlink subsys (disabled)
            [    0.189863] audit: type=2000 audit(0.120:1): state=initialized audit_enabled=0 res=1
            [    0.190224] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
            [    0.204280] ASID allocator initialised with 65536 entries
            [    0.228693] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
            [    0.229847] HugeTLB: 0 KiB vmemmap can be freed for a 1.00 GiB page
            [    0.236071] HugeTLB: registered 32.0 MiB page size, pre-allocated 0 pages
            [    0.242816] HugeTLB: 0 KiB vmemmap can be freed for a 32.0 MiB page
            [    0.249045] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
            [    0.255790] HugeTLB: 0 KiB vmemmap can be freed for a 2.00 MiB page
            [    0.262020] HugeTLB: registered 64.0 KiB page size, pre-allocated 0 pages
            [    0.268765] HugeTLB: 0 KiB vmemmap can be freed for a 64.0 KiB page
            [    0.343058] raid6: neonx8   gen()  2144 MB/s
            [    0.411122] raid6: neonx4   gen()  2189 MB/s
            [    0.479182] raid6: neonx2   gen()  2085 MB/s
            [    0.547241] raid6: neonx1   gen()  1787 MB/s
            [    0.615292] raid6: int64x8  gen()  1366 MB/s
            [    0.683355] raid6: int64x4  gen()  1604 MB/s
            [    0.751420] raid6: int64x2  gen()  1397 MB/s
            [    0.819480] raid6: int64x1  gen()  1034 MB/s
            [    0.819519] raid6: using algorithm neonx4 gen() 2189 MB/s
            [    0.887528] raid6: .... xor() 1558 MB/s, rmw enabled
            [    0.887573] raid6: using neon recovery algorithm
            [    0.891836] iommu: Default domain type: Translated
            [    0.896282] iommu: DMA domain TLB invalidation policy: strict mode
            [    0.902700] SCSI subsystem initialized
            [    0.906377] usbcore: registered new interface driver usbfs
            [    0.911703] usbcore: registered new interface driver hub
            [    0.916975] usbcore: registered new device driver usb
            [    0.922131] mc: Linux media interface: v0.10
            [    0.926234] videodev: Linux video capture interface: v2.00
            [    0.931707] pps_core: LinuxPPS API ver. 1 registered
            [    0.936590] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
            [    0.945687] PTP clock support registered
            [    0.949584] EDAC MC: Ver: 3.0.0
            [    0.952998] zynqmp-ipi-mbox mailbox@ff9905c0: Registered ZynqMP IPI mbox with TX/RX channels.
            [    0.961547] jesd204: created con: id=0, topo=0, link=0, /axi/spi@ff040000/ad9528-1@1 <-> /fpga-axi@0/axi-adxcvr-tx@84a80000
            [    0.972243] jesd204: created con: id=1, topo=0, link=2, /axi/spi@ff040000/ad9528-1@1 <-> /fpga-axi@0/axi-adxcvr-rx@84a60000
            [    0.983304] jesd204: created con: id=2, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@84a80000 <-> /fpga-axi@0/axi-jesd204-tx@84a90000
            [    0.994983] jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx@84a60000 <-> /fpga-axi@0/axi-jesd204-rx@84aa0000
            [    1.006659] jesd204: created con: id=4, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@84a90000 <-> /fpga-axi@0/axi-adrv904x-tx-hpc@84a04000
            [    1.018856] jesd204: created con: id=5, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@84aa0000 <-> /axi/spi@ff040000/adrv904x-phy@0
            [    1.030359] jesd204: created con: id=6, topo=0, link=0, /fpga-axi@0/axi-adrv904x-tx-hpc@84a04000 <-> /axi/spi@ff040000/adrv904x-phy@0
            [    1.042303] jesd204: /axi/spi@ff040000/adrv904x-phy@0: JESD204[0:0] transition uninitialized -> initialized
            [    1.051981] jesd204: /axi/spi@ff040000/adrv904x-phy@0: JESD204[0:2] transition uninitialized -> initialized
            [    1.061669] jesd204: found 7 devices and 1 topologies
            [    1.066712] FPGA manager framework
            [    1.070089] Advanced Linux Sound Architecture Driver Initialized.
            [    1.076536] Bluetooth: Core ver 2.22
            [    1.079671] NET: Registered PF_BLUETOOTH protocol family
            [    1.084939] Bluetooth: HCI device and connection manager initialized
            [    1.091255] Bluetooth: HCI socket layer initialized
            [    1.096098] Bluetooth: L2CAP socket layer initialized
            [    1.101123] Bluetooth: SCO socket layer initialized
            [    1.106459] clocksource: Switched to clocksource arch_sys_counter
            [    1.112158] VFS: Disk quotas dquot_6.6.0
            [    1.115941] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
            [    1.127616] NET: Registered PF_INET protocol family
            [    1.127807] IP idents hash table entries: 65536 (order: 7, 524288 bytes, linear)
            [    1.137656] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
            [    1.143442] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
            [    1.151117] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
            [    1.159186] TCP bind hash table entries: 32768 (order: 8, 1048576 bytes, linear)
            [    1.167110] TCP: Hash tables configured (established 32768 bind 32768)
            [    1.172891] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
            [    1.179555] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
            [    1.186715] NET: Registered PF_UNIX/PF_LOCAL protocol family
            [    1.192476] RPC: Registered named UNIX socket transport module.
            [    1.198085] RPC: Registered udp transport module.
            [    1.202753] RPC: Registered tcp transport module.
            [    1.207422] RPC: Registered tcp NFSv4.1 backchannel transport module.
            [    1.214428] PCI: CLS 0 bytes, default 64
            [    1.218468] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
            [    1.226331] Initialise system trusted keyrings
            [    1.229926] workingset: timestamp_bits=62 max_order=20 bucket_order=0
            [    1.236794] NFS: Registering the id_resolver key type
            [    1.241278] Key type id_resolver registered
            [    1.245396] Key type id_legacy registered
            [    1.249389] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
            [    1.256036] nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
            [    1.263404] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
            [    1.270556] fuse: init (API version 7.37)
            [    1.309412] NET: Registered PF_ALG protocol family
            [    1.309460] xor: measuring software checksum speed
            [    1.317231]    8regs           :  2521 MB/sec
            [    1.321546]    32regs          :  2522 MB/sec
            [    1.326156]    arm64_neon      :  2351 MB/sec
            [    1.326293] xor: using function: 32regs (2522 MB/sec)
            [    1.331318] Key type asymmetric registered
            [    1.335382] Asymmetric key parser 'x509' registered
            [    1.340253] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
            [    1.347583] io scheduler mq-deadline registered
            [    1.352081] io scheduler kyber registered
            [    1.388549] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
            [    1.395931] brd: module loaded
            [    1.399169] loop: module loaded
            [    1.399514] Registered mathworks_ip class
            [    1.401167] mtdoops: mtd device (mtddev=name/number) must be supplied
            [    1.409838] tun: Universal TUN/TAP device driver, 1.6
            [    1.412180] CAN device driver interface
            [    1.416620] SPI driver wl1271_spi has no spi_device_id for ti,wl1271
            [    1.422210] SPI driver wl1271_spi has no spi_device_id for ti,wl1273
            [    1.428517] SPI driver wl1271_spi has no spi_device_id for ti,wl1281
            [    1.434830] SPI driver wl1271_spi has no spi_device_id for ti,wl1283
            [    1.441143] SPI driver wl1271_spi has no spi_device_id for ti,wl1285
            [    1.447458] SPI driver wl1271_spi has no spi_device_id for ti,wl1801
            [    1.453777] SPI driver wl1271_spi has no spi_device_id for ti,wl1805
            [    1.460088] SPI driver wl1271_spi has no spi_device_id for ti,wl1807
            [    1.466401] SPI driver wl1271_spi has no spi_device_id for ti,wl1831
            [    1.472716] SPI driver wl1271_spi has no spi_device_id for ti,wl1835
            [    1.479030] SPI driver wl1271_spi has no spi_device_id for ti,wl1837
            [    1.485449] usbcore: registered new interface driver asix
            [    1.490745] usbcore: registered new interface driver ax88179_178a
            [    1.496786] usbcore: registered new interface driver cdc_ether
            [    1.502581] usbcore: registered new interface driver net1080
            [    1.508202] usbcore: registered new interface driver cdc_subset
            [    1.514083] usbcore: registered new interface driver zaurus
            [    1.519632] usbcore: registered new interface driver cdc_ncm
            [    1.525244] usbcore: registered new interface driver r8153_ecm
            [    1.532187] usbcore: registered new interface driver uas
            [    1.536328] usbcore: registered new interface driver usb-storage
            [    1.542316] usbcore: registered new interface driver usbserial_generic
            [    1.548769] usbserial: USB Serial support registered for generic
            [    1.554741] usbcore: registered new interface driver ftdi_sio
            [    1.560440] usbserial: USB Serial support registered for FTDI USB Serial Device
            [    1.567714] usbcore: registered new interface driver upd78f0730
            [    1.573588] usbserial: USB Serial support registered for upd78f0730
            [    1.580800] SPI driver ads7846 has no spi_device_id for ti,tsc2046
            [    1.585949] SPI driver ads7846 has no spi_device_id for ti,ads7843
            [    1.592088] SPI driver ads7846 has no spi_device_id for ti,ads7845
            [    1.598229] SPI driver ads7846 has no spi_device_id for ti,ads7873
            [    1.604926] rtc_zynqmp ffa60000.rtc: registered as rtc0
            [    1.609574] rtc_zynqmp ffa60000.rtc: setting system clock to 2024-05-13T09:24:13 UTC (1715592253)
            [    1.618447] i2c_dev: i2c /dev entries driver
            [    1.624473] usbcore: registered new interface driver uvcvideo
            [    1.629857] Bluetooth: HCI UART driver ver 2.3
            [    1.632750] Bluetooth: HCI UART protocol H4 registered
            [    1.637847] Bluetooth: HCI UART protocol BCSP registered
            [    1.643137] Bluetooth: HCI UART protocol LL registered
            [    1.648225] Bluetooth: HCI UART protocol ATH3K registered
            [    1.653601] Bluetooth: HCI UART protocol Three-wire (H5) registered
            [    1.659860] Bluetooth: HCI UART protocol Intel registered
            [    1.665192] Bluetooth: HCI UART protocol QCA registered
            [    1.670395] usbcore: registered new interface driver bcm203x
            [    1.676020] usbcore: registered new interface driver bpa10x
            [    1.681550] usbcore: registered new interface driver bfusb
            [    1.687000] usbcore: registered new interface driver btusb
            [    1.692466] usbcore: registered new interface driver ath3k
            [    1.697952] EDAC MC: ECC not enabled
            [    1.701589] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
            [    1.713909] sdhci: Secure Digital Host Controller Interface driver
            [    1.719676] sdhci: Copyright(c) Pierre Ossman
            [    1.724000] sdhci-pltfm: SDHCI platform and OF driver helper
            [    1.730075] ledtrig-cpu: registered to indicate activity on CPUs
            [    1.735649] SMCCC: SOC_ID: ID = jep106:0049:0000 Revision = 0x24738093
            [    1.742148] zynqmp_firmware_probe Platform Management API v1.1
            [    1.747920] zynqmp_firmware_probe Trustzone version v1.0
            [    1.782693] zynqmp-aes zynqmp-aes.0: will run requests pump with realtime priority
            [    1.784902] usbcore: registered new interface driver usbhid
            [    1.790161] usbhid: USB HID core driver
            [    1.794113] SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
            [    1.801532] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7988-5
            [    1.807977] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7988-1
            [    1.815154] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7984
            [    1.822161] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7983
            [    1.829166] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7982
            [    1.836173] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7980
            [    1.843179] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7949
            [    1.850186] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7946
            [    1.857193] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7942
            [    1.864199] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7699
            [    1.871209] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7693
            [    1.878212] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7691
            [    1.885218] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7690
            [    1.892225] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7689
            [    1.899231] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7688
            [    1.906237] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7687
            [    1.913244] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7686
            [    1.920251] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7685
            [    1.927262] SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7682
            [    1.934402] SPI driver ad7124 has no spi_device_id for adi,ad7124-4
            [    1.940494] SPI driver ad7124 has no spi_device_id for adi,ad7124-8
            [    1.946734] SPI driver ad7192 has no spi_device_id for adi,ad7190
            [    1.952776] SPI driver ad7192 has no spi_device_id for adi,ad7193
            [    1.958830] SPI driver ad7192 has no spi_device_id for adi,ad7195
            [    1.965705] SPI driver ad9467 has no spi_device_id for adi,ad9643
            [    1.970942] SPI driver ad9467 has no spi_device_id for adi,ad9250
            [    1.976997] SPI driver ad9467 has no spi_device_id for adi,ad9250_2
            [    1.983223] SPI driver ad9467 has no spi_device_id for adi,ad9265
            [    1.989278] SPI driver ad9467 has no spi_device_id for adi,ad9683
            [    1.995332] SPI driver ad9467 has no spi_device_id for adi,ad9434
            [    2.001388] SPI driver ad9467 has no spi_device_id for adi,ad9625
            [    2.007442] SPI driver ad9467 has no spi_device_id for adi,ad9652
            [    2.013497] SPI driver ad9467 has no spi_device_id for adi,ad9649
            [    2.021998] SPI driver adar3000 has no spi_device_id for adi,adar3001
            [    2.025964] SPI driver adar3000 has no spi_device_id for adi,adar3002
            [    2.033682] SPI driver ad9783 has no spi_device_id for adi,ad9780
            [    2.038413] SPI driver ad9783 has no spi_device_id for adi,ad9781
            [    2.044655] SPI driver adis16475 has no spi_device_id for adi,adis16470
            [    2.051046] SPI driver adis16475 has no spi_device_id for adi,adis16475-1
            [    2.057787] SPI driver adis16475 has no spi_device_id for adi,adis16475-2
            [    2.064533] SPI driver adis16475 has no spi_device_id for adi,adis16475-3
            [    2.071280] SPI driver adis16475 has no spi_device_id for adi,adis16477-1
            [    2.078027] SPI driver adis16475 has no spi_device_id for adi,adis16477-2
            [    2.084777] SPI driver adis16475 has no spi_device_id for adi,adis16477-3
            [    2.091521] SPI driver adis16475 has no spi_device_id for adi,adis16465-1
            [    2.098268] SPI driver adis16475 has no spi_device_id for adi,adis16465-2
            [    2.105015] SPI driver adis16475 has no spi_device_id for adi,adis16465-3
            [    2.111761] SPI driver adis16475 has no spi_device_id for adi,adis16467-1
            [    2.118509] SPI driver adis16475 has no spi_device_id for adi,adis16467-2
            [    2.125256] SPI driver adis16475 has no spi_device_id for adi,adis16467-3
            [    2.132003] SPI driver adis16475 has no spi_device_id for adi,adis16500
            [    2.138577] SPI driver adis16475 has no spi_device_id for adi,adis16505-1
            [    2.145324] SPI driver adis16475 has no spi_device_id for adi,adis16505-2
            [    2.152071] SPI driver adis16475 has no spi_device_id for adi,adis16505-3
            [    2.158818] SPI driver adis16475 has no spi_device_id for adi,adis16507-1
            [    2.165565] SPI driver adis16475 has no spi_device_id for adi,adis16507-2
            [    2.172312] SPI driver adis16475 has no spi_device_id for adi,adis16507-3
            [    2.180143] axi_sysid 85000000.axi-sysid-0: AXI System ID core version (1.01.a) found
            [    2.187027] axi_sysid 85000000.axi-sysid-0: [adrv904x] on [zcu102] git branch <Koror> git <01337fdb128232d3cf520b61e44a11c1c9cb2e1b> dirty [2024-02-28 16:43:31] UTC
            [    2.202114] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
            [    2.208230] usbcore: registered new interface driver snd-usb-audio
            [    2.215830] pktgen: Packet Generator for packet performance testing. Version: 2.75
            [    2.221967] Initializing XFRM netlink socket
            [    2.225836] NET: Registered PF_INET6 protocol family
            [    2.231202] Segment Routing with IPv6
            [    2.234353] In-situ OAM (IOAM) with IPv6
            [    2.238276] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
            [    2.244450] NET: Registered PF_PACKET protocol family
            [    2.249132] NET: Registered PF_KEY protocol family
            [    2.253967] can: controller area network core
            [    2.258230] NET: Registered PF_CAN protocol family
            [    2.262965] can: raw protocol
            [    2.265902] can: broadcast manager protocol
            [    2.270063] can: netlink gateway - max_hops=1
            [    2.274465] Bluetooth: RFCOMM TTY layer initialized
            [    2.279229] Bluetooth: RFCOMM socket layer initialized
            [    2.284337] Bluetooth: RFCOMM ver 1.11
            [    2.288058] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
            [    2.293328] Bluetooth: BNEP filters: protocol multicast
            [    2.298518] Bluetooth: BNEP socket layer initialized
            [    2.303450] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
            [    2.309331] Bluetooth: HIDP socket layer initialized
            [    2.314379] 9pnet: Installing 9P2000 support
            [    2.318507] NET: Registered PF_IEEE802154 protocol family
            [    2.323886] Key type dns_resolver registered
            [    2.328370] registered taskstats version 1
            [    2.332167] Loading compiled-in X.509 certificates
            [    2.337286] Btrfs loaded, crc32c=crc32c-generic, zoned=no, fsverity=no
            [    2.343545] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
            [    2.755916] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 23, base_baud = 6249999) is a xuartps
            [    2.764944] printk: console [ttyPS0] enabled
            [    2.764944] printk: console [ttyPS0] enabled
            [    2.769243] printk: bootconsole [cdns0] disabled
            [    2.769243] printk: bootconsole [cdns0] disabled
            [    2.778888] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 24, base_baud = 6249999) is a xuartps
            [    2.793138] nwl-pcie fd0e0000.pcie: host bridge /axi/pcie@fd0e0000 ranges:
            [    2.800036] nwl-pcie fd0e0000.pcie:      MEM 0x00e0000000..0x00efffffff -> 0x00e0000000
            [    2.808041] nwl-pcie fd0e0000.pcie:      MEM 0x0600000000..0x07ffffffff -> 0x0600000000
            [    2.816149] nwl-pcie fd0e0000.pcie: Link is DOWN
            [    2.820968] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
            [    2.827151] pci_bus 0000:00: root bus resource [bus 00-ff]
            [    2.832633] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
            [    2.839507] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
            [    2.847011] pci 0000:00:00.0: [10ee:d021] type 01 class 0x060400
            [    2.853073] pci 0000:00:00.0: PME# supported from D0 D1 D2 D3hot
            [    2.861046] pci 0000:00:00.0: bridge configuration invalid ([bus 00-00]), reconfiguring
            [    2.869161] pci_bus 0000:01: busn_res: [bus 01-ff] end is updated to 01
            [    2.875789] pci 0000:00:00.0: PCI bridge to [bus 01]
            [    2.883200] xilinx-zynqmp-dpdma fd4c0000.dma-controller: Xilinx DPDMA engine is probed
            [    2.892214] ad9528 spi1.1: supply vcc not found, using dummy regulator
            [    2.920708] jesd204: /axi/spi@ff040000/ad9528-1@1,jesd204:0,parent=spi1.1: Using as SYSREF provider
            [    2.930576] MESSAGE: API_LOG:-> adi_adrv904x_HwOpen()
            [    2.935625] MESSAGE: API_LOG:adi_adrv904x_HwOpen(...)
            [    2.940672] MESSAGE: API_LOG:-> adi_adrv904x_HwReset()
            [    2.996000] MESSAGE: API_LOG:-> adi_adrv904x_SpiCfgSet()
            [    3.001329] MESSAGE: API_LOG:-> adi_adrv904x_GpioDriveStrengthSet()
            [    3.007788] MESSAGE: API_LOG:<- adi_adrv904x_GpioDriveStrengthSet()
            [    3.014045] MESSAGE: API_LOG:-> adi_adrv904x_GpioDriveStrengthSet()
            [    3.020395] MESSAGE: API_LOG:<- adi_adrv904x_GpioDriveStrengthSet()
            [    3.026656] MESSAGE: API_LOG:-> adi_adrv904x_GpioHysteresisSet()
            [    3.032707] MESSAGE: API_LOG:<- adi_adrv904x_GpioHysteresisSet()
            [    3.038704] MESSAGE: API_LOG:<- adi_adrv904x_SpiCfgSet()
            [    3.044007] MESSAGE: API_LOG:<- adi_adrv904x_HwReset()
            [    3.049145] MESSAGE: API_LOG:<- adi_adrv904x_HwOpen()
            [    3.054190] MESSAGE: API_LOG:-> adi_adrv904x_SpiVerify()
            [    3.059646] MESSAGE: API_LOG:<- adi_adrv904x_SpiVerify()
            [    3.064953] MESSAGE: API_LOG:-> adi_adrv904x_ApiVersionGet()
            [    3.070602] MESSAGE: API_LOG:<- adi_adrv904x_ApiVersionGet()
            [    3.076253] adrv9040 spi1.0: adrv9040 Rev 0, API version: 2.10.0.4 found
            [    3.082954] MESSAGE: API_LOG:-> adi_adrv904x_InitDataExtract()
            [    3.088819] MESSAGE: API_LOG:<- adi_adrv904x_InitDataExtract()
            [    3.094646]
            [    3.094646]  Using the Profile Init and PostMcsInit Structures
            [    3.101949] MESSAGE: API_LOG:-> adi_adrv904x_DeviceInfoExtract()
            [    3.107983] MESSAGE: API_LOG:<- adi_adrv904x_DeviceInfoExtract()
            [    3.114180] MESSAGE: API_LOG:adrv904x_TxLinkSamplingRateFind(...)
            [    3.121292] MESSAGE: API_LOG:-> adi_adrv904x_ApiVersionGet()
            [    3.126948] MESSAGE: API_LOG:<- adi_adrv904x_ApiVersionGet()
            [    3.132605] MESSAGE: API_LOG:-> adi_adrv904x_HwClose()
            [    3.137737] MESSAGE: API_LOG:<- adi_adrv904x_HwClose()
            [    3.142864] adrv9040 spi1.0: adrv9040 Rev 0, API version: 2.10.0.4 found
            [    3.150270] spi-nor spi0.0: SPI-NOR-UniqueID 2ab990001501002a00e62e735a86
            [    3.157059] spi-nor spi0.0: found mt25qu512a, expected m25p80
            [    3.163065] spi-nor spi0.0: mt25qu512a (131072 Kbytes)
            [    3.168309] 4 fixed-partitions partitions found on MTD device spi0.0
            [    3.174665] Creating 4 MTD partitions on "spi0.0":
            [    3.179453] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
            [    3.186003] 0x000000100000-0x000000600000 : "qspi-linux"
            [    3.192024] 0x000000600000-0x000000620000 : "qspi-device-tree"
            [    3.198555] 0x000000620000-0x000000c00000 : "qspi-rootfs"
            [    3.207300] macb ff0e0000.ethernet: Not enabling partial store and forward
            [    3.231428] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
            [    3.237968] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
            [    3.244457] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
            [    3.250948] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
            [    3.258191] i2c i2c-0: using pinctrl states for GPIO recovery
            [    3.264115] i2c i2c-0: using generic GPIOs for recovery
            [    3.269714] pca953x 0-0020: supply vcc not found, using dummy regulator
            [    3.276402] pca953x 0-0020: using no AI
            [    3.280958] gpio-318 (sel0): hogged as output/low
            [    3.285862] gpio-319 (sel1): hogged as output/high
            [    3.290852] gpio-320 (sel2): hogged as output/high
            [    3.295846] gpio-321 (sel3): hogged as output/high
            [    3.301009] pca953x 0-0021: supply vcc not found, using dummy regulator
            [    3.307683] pca953x 0-0021: using no AI
            [    3.313237] ina2xx 2-0040: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.320233] ina2xx 2-0041: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.327227] ina2xx 2-0042: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.334214] ina2xx 2-0043: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.341206] ina2xx 2-0044: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.348201] ina2xx 2-0045: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.355206] ina2xx 2-0046: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.362209] ina2xx 2-0047: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.369203] ina2xx 2-004a: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.376194] ina2xx 2-004b: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.382606] i2c i2c-0: Added multiplexed i2c bus 2
            [    3.388163] ina2xx 3-0040: power monitor ina226 (Rshunt = 2000 uOhm)
            [    3.395159] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.402152] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.409141] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.416135] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.423124] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.430122] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.437132] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
            [    3.443536] i2c i2c-0: Added multiplexed i2c bus 3
            [    3.516207] i2c i2c-0: Added multiplexed i2c bus 4
            [    3.521169] i2c i2c-0: Added multiplexed i2c bus 5
            [    3.525962] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
            [    3.533335] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 48
            [    3.540266] i2c i2c-1: using pinctrl states for GPIO recovery
            [    3.546191] i2c i2c-1: using generic GPIOs for recovery
            [    3.552177] at24 6-0054: supply vcc not found, using dummy regulator
            [    3.559055] at24 6-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
            [    3.565819] i2c i2c-1: Added multiplexed i2c bus 6
            [    3.571182] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.578493] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.585801] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.593105] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.600405] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.607705] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.615004] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.622304] si5341 7-0036: no regulator set, defaulting vdd_sel to 2.5V for out
            [    3.630703] si5341 7-0036: Chip: 5341 Grade: 1 Rev: 1
            [    3.668979] i2c i2c-1: Added multiplexed i2c bus 7
            [    3.676627] si570 8-005d: registered, current frequency 300000000 Hz
            [    3.683036] i2c i2c-1: Added multiplexed i2c bus 8
            [    3.702824] si570 9-005d: registered, current frequency 148500000 Hz
            [    3.709232] i2c i2c-1: Added multiplexed i2c bus 9
            [    3.714258] si5324 10-0069: si5328 probed
            [    3.782726] si5324 10-0069: si5328 probe successful
            [    3.787657] i2c i2c-1: Added multiplexed i2c bus 10
            [    3.792701] i2c i2c-1: Added multiplexed i2c bus 11
            [    3.797743] i2c i2c-1: Added multiplexed i2c bus 12
            [    3.802782] i2c i2c-1: Added multiplexed i2c bus 13
            [    3.807663] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
            [    3.815667] i2c i2c-1: Added multiplexed i2c bus 14
            [    3.821013] ad7291: probe of 15-002f failed with error -5
            [    3.826576] at24 15-0050: supply vcc not found, using dummy regulator
            [    3.861010] i2c i2c-1: Added multiplexed i2c bus 15
            [    3.866080] i2c i2c-1: Added multiplexed i2c bus 16
            [    3.871125] i2c i2c-1: Added multiplexed i2c bus 17
            [    3.876175] i2c i2c-1: Added multiplexed i2c bus 18
            [    3.881234] i2c i2c-1: Added multiplexed i2c bus 19
            [    3.886292] i2c i2c-1: Added multiplexed i2c bus 20
            [    3.891351] i2c i2c-1: Added multiplexed i2c bus 21
            [    3.896233] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
            [    3.903856] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 49
            [    3.913238] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
            [    3.941679] iio_dmaengine_buffer_alloc:231 width 0 (DMA width >= 256-bits ?)
            [    3.949547] cf_axi_adc 84a00000.axi-adrv904x-rx-hpc: ADI AIM (10.03.) at 0x84A00000 mapped to 0x(____ptrval____) probed ADC ADRV904X as MASTER
            [    3.954830] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
            [    3.978481] iio_dmaengine_buffer_alloc:231 width 0 (DMA width >= 256-bits ?)
            [    3.987796] cf_axi_dds 84a04000.axi-adrv904x-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.02.b) at 0x84A04000 mapped to 0x(____ptrval____), probed DDS ADRV904X
            [    4.002849] axi_adxcvr 84a60000.axi-adxcvr-rx: adxcvr_enforce_settings: Using QPLL without access, assuming desired Lane rate will be configured by a different instance
            [    4.008562] mmc0: new high speed SDHC card at address aaaa
            [    4.023763] mmcblk0: mmc0:aaaa SB16G 14.8 GiB
            [    4.024310] axi_adxcvr 84a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.05.a) using QPLL on GTH4 at 0x84A60000. Number of lanes: 8.
            [    4.040500] axi_adxcvr 84a80000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.05.a) using QPLL on GTH4 at 0x84A80000. Number of lanes: 8.
            [    4.043663]  mmcblk0: p1 p2 p3
            [    4.052236] axi-jesd204-rx 84aa0000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x84AA0000. Encoder 64b66b, width 8/8, lanes 8, jesd204-fsm.
            [    4.067642] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition initialized -> probed
            [    4.078866] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition initialized -> probed
            [    4.090099] MESSAGE: API_LOG:-> adi_adrv904x_HwOpen()
            [    4.095148] MESSAGE: API_LOG:adi_adrv904x_HwOpen(...)
            [    4.100189] MESSAGE: API_LOG:-> adi_adrv904x_HwReset()
            [    4.155413] MESSAGE: API_LOG:-> adi_adrv904x_SpiCfgSet()
            [    4.160749] MESSAGE: API_LOG:-> adi_adrv904x_GpioDriveStrengthSet()
            [    4.167249] MESSAGE: API_LOG:<- adi_adrv904x_GpioDriveStrengthSet()
            [    4.173513] MESSAGE: API_LOG:-> adi_adrv904x_GpioDriveStrengthSet()
            [    4.179888] MESSAGE: API_LOG:<- adi_adrv904x_GpioDriveStrengthSet()
            [    4.186151] MESSAGE: API_LOG:-> adi_adrv904x_GpioHysteresisSet()
            [    4.192206] MESSAGE: API_LOG:<- adi_adrv904x_GpioHysteresisSet()
            [    4.198206] MESSAGE: API_LOG:<- adi_adrv904x_SpiCfgSet()
            [    4.203508] MESSAGE: API_LOG:<- adi_adrv904x_HwReset()
            [    4.208637] MESSAGE: API_LOG:<- adi_adrv904x_HwOpen()
            [    4.334481] random: crng init done
            [    6.761499] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition probed -> initialized
            [    6.772740] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition probed -> initialized
            [    9.330583] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition initialized -> probed
            [    9.341820] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition initialized -> probed
            [   11.899574] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition probed -> idle
            [   11.910209] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition probed -> idle
            [   14.467209] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition idle -> device_init
            [   14.478271] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition idle -> device_init
            [   14.511049] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition device_init -> link_init
            [   14.522532] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition device_init -> link_init
            [   14.534022] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition link_init -> link_supported
            [   14.545763] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition link_init -> link_supported
            [   14.557775] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition link_supported -> link_pre_setup
            [   14.569957] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition link_supported -> link_pre_setup
            [   14.582370] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
            [   14.594632] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> clk_sync_stage1
            [   14.606899] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
            [   14.619251] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> clk_sync_stage2
            [   14.631603] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
            [   14.643950] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage3
            [   14.660974] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> link_setup
            [   14.672893] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> link_setup
            [   14.685479] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition link_setup -> opt_setup_stage1
            [   14.697483] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition link_setup -> opt_setup_stage1
            [   14.778052] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_stage2
            [   14.790576] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> opt_setup_stage2
            [   14.803293] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage3
            [   14.815818] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage3
            [   14.828344] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage4
            [   14.840865] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage4
            [   14.853384] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage5
            [   14.865906] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage5
            [   14.878433] adrv9040 spi1.0: adrv904x_jesd204_clks_enable:1887 link_num 0 reason initialization
            [   14.887378] adrv9040 spi1.0: adrv904x_jesd204_clks_enable:1887 link_num 2 reason initialization
            [   14.896458] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
            [   14.908718] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> clocks_enable
            [   30.778701] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition clocks_enable -> link_enable
            [   30.790533] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition clocks_enable -> link_enable
            [   30.828730] adrv9040 spi1.0: Link0 deframerStatus lane 0 0xE
            [   30.834390] adrv9040 spi1.0: Link0 deframerStatus lane 1 0xE
            [   30.840042] adrv9040 spi1.0: Link0 deframerStatus lane 2 0xE
            [   30.845699] adrv9040 spi1.0: Link0 deframerStatus lane 3 0xE
            [   30.851350] adrv9040 spi1.0: Link0 deframerStatus lane 4 0xE
            [   30.857000] adrv9040 spi1.0: Link0 deframerStatus lane 5 0xE
            [   30.862651] adrv9040 spi1.0: Link0 deframerStatus lane 6 0xE
            [   30.868301] adrv9040 spi1.0: Link0 deframerStatus lane 7 0xE
            [   30.874637] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition link_enable -> link_running
            [   30.886377] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition link_enable -> link_running
            [   30.905743] adrv9040 spi1.0:
            [   30.905743] adrv9040 Rev 160, API version: 2.10.0.4 successfully initialized via jesd204-fsm
            [   30.917132] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:0] transition link_running -> opt_post_running_stage
            [   30.929825] jesd204: /axi/spi@ff040000/adrv904x-phy@0,jesd204:1,parent=spi1.0: JESD204[0:2] transition link_running -> opt_post_running_stage
            [   30.942529] axi-jesd204-tx 84a90000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0x84A90000. Encoder 64b66b, width 8/8, lanes 8, jesd204-fsm.
            [   30.956373] zynqmp-display fd4a0000.display: vtc bridge property not present
            [   30.966881] xilinx-dp-snd-codec fd4a0000.display:zynqmp-dp-snd-codec0: Failed to get required clock freq
            [   30.976370] xilinx-dp-snd-codec: probe of fd4a0000.display:zynqmp-dp-snd-codec0 failed with error -22
            [   30.985898] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
            [   30.993976] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
            [   31.002138] OF: graph: no port node found in /axi/display@fd4a0000
            [   31.008700] xlnx-drm xlnx-drm.0: bound fd4a0000.display (ops 0xffffffc0092a2e60)
            [   32.094484] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
            [   32.102138] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.display on minor 0
            [   32.109643] zynqmp-display fd4a0000.display: ZynqMP DisplayPort Subsystem driver probed
            [   32.117854] ahci-ceva fd0c0000.ahci: supply ahci not found, using dummy regulator
            [   32.125410] ahci-ceva fd0c0000.ahci: supply phy not found, using dummy regulator
            [   32.132872] ahci-ceva fd0c0000.ahci: supply target not found, using dummy regulator
            [   32.140751] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
            [   32.149707] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst
            [   32.160184] scsi host0: ahci-ceva
            [   32.163785] scsi host1: ahci-ceva
            [   32.167203] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 55
            [   32.175111] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 55
            [   32.184728] macb ff0e0000.ethernet: Not enabling partial store and forward
            [   32.193554] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 45 (8a:5f:1c:0d:30:c0)
            [   32.226425] xhci-hcd xhci-hcd.1.auto: xHCI Host Controller
            [   32.231920] xhci-hcd xhci-hcd.1.auto: new USB bus registered, assigned bus number 1
            [   32.239662] xhci-hcd xhci-hcd.1.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000002010810
            [   32.249072] xhci-hcd xhci-hcd.1.auto: irq 56, io mem 0xfe200000
            [   32.255082] xhci-hcd xhci-hcd.1.auto: xHCI Host Controller
            [   32.260561] xhci-hcd xhci-hcd.1.auto: new USB bus registered, assigned bus number 2
            [   32.268221] xhci-hcd xhci-hcd.1.auto: Host supports USB 3.0 SuperSpeed
            [   32.274852] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
            [   32.283119] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
            [   32.290338] usb usb1: Product: xHCI Host Controller
            [   32.295207] usb usb1: Manufacturer: Linux 6.1.0-271699-g36807a05d5c8 xhci-hcd
            [   32.302332] usb usb1: SerialNumber: xhci-hcd.1.auto
            [   32.307508] hub 1-0:1.0: USB hub found
            [   32.311273] hub 1-0:1.0: 1 port detected
            [   32.315486] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
            [   32.323751] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
            [   32.330975] usb usb2: Product: xHCI Host Controller
            [   32.335848] usb usb2: Manufacturer: Linux 6.1.0-271699-g36807a05d5c8 xhci-hcd
            [   32.342978] usb usb2: SerialNumber: xhci-hcd.1.auto
            [   32.348116] hub 2-0:1.0: USB hub found
            [   32.351878] hub 2-0:1.0: 1 port detected
            [   32.364977] input: gpio-keys as /devices/platform/gpio-keys/input/input0
            [   32.372055] of_cfs_init
            [   32.374526] of_cfs_init: OK
            [   32.377354] cfg80211: Loading compiled-in X.509 certificates for regulatory database
            [   32.424453] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
            [   32.431003] clk: Not disabling unused clocks
            [   32.435550] ALSA device list:
            [   32.438514]   No soundcards found.
            [   32.442168] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
            [   32.450787] cfg80211: failed to load regulatory.db
            [   32.496732] ata1: SATA link down (SStatus 0 SControl 330)
            [   32.502161] ata2: SATA link down (SStatus 0 SControl 330)
            [   32.521415] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Quota mode: none.
            [   32.529969] VFS: Mounted root (ext4 filesystem) on device 179:2.
            [   32.546673] devtmpfs: mounted
            [   32.550398] Freeing unused kernel memory: 2752K
            [   32.555028] Run /sbin/init as init process
            [   33.120468] systemd[1]: systemd 247.3-7+rpi1+deb11u2 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
            [   33.144410] systemd[1]: Detected architecture arm64.
   
            Welcome to Kuiper GNU/Linux 11.2 (bullseye)!
   
            [   33.173417] systemd[1]: Set hostname to <analog>.
            [   33.186492] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
            [   34.540766] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
            [   34.749777] systemd[1]: Queued start job for default target Graphical Interface.
            [   34.758592] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
            [   34.770956] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
            [   34.780034] systemd[1]: Created slice system-getty.slice.
            [  OK  ] Created slice system-getty.slice.
            [   34.802957] systemd[1]: Created slice system-modprobe.slice.
            [  OK  ] Created slice system-modprobe.slice.
            [   34.822886] systemd[1]: Created slice system-serial\x2dgetty.slice.
            [  OK  ] Created slice system-serial\x2dgetty.slice.
            [   34.846876] systemd[1]: Created slice system-systemd\x2dfsck.slice.
            [  OK  ] Created slice system-systemd\x2dfsck.slice.
            [   34.870771] systemd[1]: Created slice User and Session Slice.
            [  OK  ] Created slice User and Session Slice.
            [   34.890773] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
            [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
            [   34.914717] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
            [   34.927124] systemd[1]: Reached target Slices.
            [  OK  ] Reached target Slices.
            [   34.942653] systemd[1]: Reached target Swap.
            [  OK  ] Reached target Swap.
            [   34.969600] systemd[1]: Listening on Syslog Socket.
            [  OK  ] Listening on Syslog Socket.
            [   34.986900] systemd[1]: Listening on fsck to fsckd communication Socket.
            [  OK  ] Listening on fsck to fsckd communication Socket.
            [   35.010710] systemd[1]: Listening on initctl Compatibility Named Pipe.
            [  OK  ] Listening on initctl Compatibility Named Pipe.
            [   35.035181] systemd[1]: Listening on Journal Audit Socket.
            [  OK  ] Listening on Journal Audit Socket.
            [   35.054878] systemd[1]: Listening on Journal Socket (/dev/log).
            [  OK  ] Listening on Journal Socket (/dev/log).
            [   35.078948] systemd[1]: Listening on Journal Socket.
            [  OK  ] Listening on Journal Socket.
            [   35.103892] systemd[1]: Listening on udev Control Socket.
            [  OK  ] Listening on udev Control Socket.
            [   35.126881] systemd[1]: Listening on udev Kernel Socket.
            [  OK  ] Listening on udev Kernel Socket.
            [   35.162634] systemd[1]: Mounting Huge Pages File System...
                     Mounting Huge Pages File System...
            [   35.180413] systemd[1]: Mounting POSIX Message Queue File System...
                     Mounting POSIX Message Queue File System...
            [   35.204288] systemd[1]: Mounting RPC Pipe File System...
                     Mounting RPC Pipe File System...
            [   35.220541] systemd[1]: Mounting Kernel Debug File System...
                     Mounting Kernel Debug File System...
            [   35.239006] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
            [   35.247736] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
            [   35.282850] systemd[1]: Starting Restore / save the current clock...
                     Starting Restore / save the current clock...
            [   35.311156] systemd[1]: Starting Set the console keyboard layout...
                     Starting Set the console keyboard layout...
            [   35.335389] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
            [   35.349021] systemd[1]: Starting Load Kernel Module configfs...
                     Starting Load Kernel Module configfs...
            [   35.368961] systemd[1]: Starting Load Kernel Module drm...
                     Starting Load Kernel Module drm...
            [   35.388883] systemd[1]: Starting Load Kernel Module fuse...
                     Starting Load Kernel Module fuse...
            [   35.411289] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
            [   35.420627] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
            [   35.450854] systemd[1]: Starting Journal Service...
                     Starting Journal Service...
            [   35.472802] systemd[1]: Starting Load Kernel Modules...
                     Starting Load Kernel Modules...
            [   35.492733] systemd[1]: Starting Remount Root and Kernel File Systems...
                     Starting Remount Root and Kernel File Systems...
            [   35.516703] systemd[1]: Starting Coldplug All udev Devices...
                     Starting Coldplug All udev Devices...
            [   35.540004] systemd[1]: Mounted Huge Pages File System.
            [  OK  ] Mounted Huge Pages File System.
            [   35.564361] systemd[1]: Mounted POSIX Message Queue File System.
            [  OK  ] Mounted POSIX Message Queue File System.
            [   35.587059] systemd[1]: Mounted RPC Pipe File System.
            [  OK  ] Mounted RPC Pipe File System.
            [   35.603061] systemd[1]: Mounted Kernel Debug File System.
            [  OK  ] Mounted Kernel Debug File System.
            [   35.623525] systemd[1]: Finished Restore / save the current clock.
            [  OK  ] Finished Restore / save the current clock.
            [   35.647588] systemd[1]: Finished Set the console keyboard layout.
            [  OK  ] Finished Set the console keyboard layout.
            [   35.671560] systemd[1]: modprobe@configfs.service: Succeeded.
            [   35.677866] systemd[1]: Finished Load Kernel Module configfs.
            [  OK  ] Finished Load Kernel Module configfs.
            [   35.699137] systemd[1]: Started Journal Service.
            [  OK  ] Started Journal Service.
            [  OK  ] Finished Load Kernel Module drm.
            [  OK  ] Finished Load Kernel Module fuse.
            [FAILED] Failed to start Load Kernel Modules.
            See 'systemctl status systemd-modules-load.service' for details.
            [   35.796286] EXT4-fs (mmcblk0p2): re-mounted. Quota mode: none.
                     Mounting FUSE Control File System...
                     Mounting Kernel Configuration File System...
                     Starting Apply Kernel Variables...
            [  OK  ] Finished Remount Root and Kernel File Systems.
            [  OK  ] Mounted FUSE Control File System.
            [  OK  ] Mounted Kernel Configuration File System.
            [  OK  ] Finished Apply Kernel Variables.
                     Starting Flush Journal to Persistent Storage...
                     Starting Load/Save Random Seed...
                     Starting Create System Users...
            [  OK  ] Finished Load/Save Random Seed.
            [  OK  ] Finished Create System Users.
                     Starting Create Static Device Nodes in /dev...
            [  OK  ] Finished Coldplug All udev Devices.
                     Starting Helper to synchronize boot up for ifupdown...
                     Starting Wait for udev To …plete Device Initialization...
            [  OK  ] Finished Create Static Device Nodes in /dev.
            [  OK  ] Finished Helper to synchronize boot up for ifupdown.
            [  OK  ] Reached target Local File Systems (Pre).
                     Starting Rule-based Manage…for Device Events and Files...
            [  OK  ] Started Rule-based Manager for Device Events and Files.
                     Starting Show Plymouth Boot Screen...
            [  OK  ] Started Show Plymouth Boot Screen.
            [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
            [  OK  ] Reached target Local Encrypted Volumes.
            [  OK  ] Finished Flush Journal to Persistent Storage.
            [  OK  ] Found device /dev/ttyPS0.
            [  OK  ] Found device /dev/disk/by-partuuid/1bd1871c-01.
            [  OK  ] Found device /dev/ttyS0.
            [  OK  ] Finished Wait for udev To Complete Device Initialization.
            [  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
                     Starting File System Check…isk/by-partuuid/1bd1871c-01...
            [  OK  ] Started File System Check Daemon to report status.
            [  OK  ] Finished File System Check…/disk/by-partuuid/1bd1871c-01.
                     Mounting /boot...
            [  OK  ] Mounted /boot.
            [  OK  ] Reached target Local File Systems.
                     Starting Set console font and keymap...
                     Starting Raise network interfaces...
                     Starting Preprocess NFS configuration...
                     Starting Tell Plymouth To Write Out Runtime Data...
                     Starting Create Volatile Files and Directories...
            [  OK  ] Finished Set console font and keymap.
            [  OK  ] Finished Preprocess NFS configuration.
            [  OK  ] Reached target NFS client services.
            [  OK  ] Reached target Remote File Systems (Pre).
            [  OK  ] Reached target Remote File Systems.
            [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
            [  OK  ] Finished Create Volatile Files and Directories.
                     Starting Network Time Synchronization...
                     Starting Update UTMP about System Boot/Shutdown...
            [  OK  ] Finished Update UTMP about System Boot/Shutdown.
                     Starting Load Kernel Modules...
            [  OK  ] Finished Raise network interfaces.
            [FAILED] Failed to start Load Kernel Modules.
            See 'systemctl status systemd-modules-load.service' for details.
            [  OK  ] Started Network Time Synchronization.
            [  OK  ] Reached target System Initialization.
            [  OK  ] Started CUPS Scheduler.
            [  OK  ] Started Daily Cleanup of Temporary Directories.
            [  OK  ] Reached target Paths.
            [  OK  ] Reached target System Time Set.
            [  OK  ] Reached target System Time Synchronized.
            [  OK  ] Started Daily apt download activities.
            [  OK  ] Started Daily apt upgrade and clean activities.
            [  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
            [  OK  ] Started Discard unused blocks once a week.
            [  OK  ] Started Daily rotation of log files.
            [  OK  ] Started Daily man-db regeneration.
            [  OK  ] Reached target Timers.
            [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
            [  OK  ] Listening on CUPS Scheduler.
            [  OK  ] Listening on D-Bus System Message Bus Socket.
            [  OK  ] Listening on Erlang Port Mapper Daemon Activation Socket.
            [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
            [  OK  ] Listening on triggerhappy.socket.
            [  OK  ] Reached target Sockets.
            [  OK  ] Reached target Basic System.
                     Starting Analog Devices power up/down sequence...
                     Starting Avahi mDNS/DNS-SD Stack...
            [  OK  ] Started Regular background program processing daemon.
            [  OK  ] Started D-Bus System Message Bus.
                     Starting dphys-swapfile - …unt, and delete a swap file...
                     Starting Remove Stale Onli…t4 Metadata Check Snapshots...
                     Starting Creating IIOD Context Attributes......
                     Starting Authorization Manager...
                     Starting DHCP Client Daemon...
                     Starting LSB: Switch to on…nless shift key is pressed)...
                     Starting LSB: rng-tools (Debian variant)...
                     Starting System Logging Service...
                     Starting User Login Management...
                     Starting triggerhappy global hotkey daemon...
                     Starting Disk Manager...
                     Starting WPA supplicant...
                     Starting Rotate log files...
                     Starting Daily man-db regeneration...
            [  OK  ] Started triggerhappy global hotkey daemon.
            [  OK  ] Started DHCP Client Daemon.
            [  OK  ] Started LSB: rng-tools (Debian variant).
            [  OK  ] Started System Logging Service.
            [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
            [  OK  ] Started User Login Management.
            [  OK  ] Started Avahi mDNS/DNS-SD Stack.
            [  OK  ] Started WPA supplicant.
            [  OK  ] Reached target Network.
            [  OK  ] Reached target Network is Online.
                     Starting CUPS Scheduler...
            [  OK  ] Started Erlang Port Mapper Daemon.
                     Starting HTTP based time synchronization tool...
                     Starting Internet superserver...
                     Starting /etc/rc.local Compatibility...
                     Starting OpenBSD Secure Shell server...
                     Starting Permit User Sessions...
            [  OK  ] Started Unattended Upgrades Shutdown.
            [  OK  ] Started Authorization Manager.
            [  OK  ] Started /etc/rc.local Compatibility.
                     Starting Modem Manager...
            [  OK  ] Started HTTP based time synchronization tool.
            [  OK  ] Finished Permit User Sessions.
                     Starting Light Display Manager...
                     Starting Hold until boot process finishes up...
            [  OK  ] Started Internet superserver.
            [  OK  ] Stopped CUPS Scheduler.
            [  OK  ] Stopped CUPS Scheduler.
                     Stopping CUPS Scheduler.
            [  OK  ] Started CUPS Scheduler.
            [  OK  ] Closed CUPS Scheduler.
                     Stopping CUPS Scheduler.
            [  OK  ] Listening on CUPS Scheduler.
                     Starting CUPS Scheduler...
            [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
            [  OK  ] Finished Creating IIOD Context Attributes....
            [  OK  ] Started IIO Daemon.
            [  OK  ] Started OpenBSD Secure Shell server.
            [  OK  ] Finished Analog Devices power up/down sequence.
   
            Raspbian GNU/Linux 11 analog ttyPS0
   
            analog login: root (automatic login)
   
            Linux analog 6.1.0-271699-g36807a05d5c8 #388 SMP Thu May  9 22:56:56 EEST 2024 aarch64
   
            The programs included with the Debian GNU/Linux system are free software;
            the exact distribution terms for each program are described in the
            individual files in /usr/share/doc/*/copyright.
   
            Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
            permitted by applicable law.
            Last login: Thu May  9 20:59:29 BST 2024 on ttyPS0
            root@analog:~#
   

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# iio_info | grep iio:device
          iio:device0: xilinx-ams
          iio:device1: ad9528-1
          iio:device2: adrv904x-phy
          iio:device3: axi-adrv904x-rx-hpc (buffer capable)
          iio:device4: axi-adrv904x-tx-hpc (buffer capable)
   

IIO Oscilloscope Remote
-----------------------

Please see also here:`Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

The IIO Oscilloscope application can be used to connect to another platform that
has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP
address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``

   |image1|

.. |image1| image:: ../images/shutdown.png
   :width: 300
