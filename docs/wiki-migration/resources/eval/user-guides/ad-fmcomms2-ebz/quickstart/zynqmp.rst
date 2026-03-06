AD-FMCOMMS2-EBZ Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide
===============================================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS2-EBZ on:

-  `ZCU102 <https://www.xilinx.com/ZCU102>`__

Instructions on how to build the ZynqMP / MPSoC Linux kernel and devicetrees from source can be found here:

-  :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`
-  :doc:`How to build the ZynqMP boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`

Required Software
-----------------

-  SD Card 16GB or more, image with the latest image available, using the instructions here: :doc:`Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Setup
~~~~~

-  Copy the following files into the BOOT partition of the SD Card (Replace files if they already exist).
-  **Image** file from **zynqmp-common**.
-  **BOOT.BIN** from **zynqmp-zcu102-rev10-ad936x-fmcomms2-3-4**.
-  **system.dtb** from **zynqmp-zcu102-rev10-ad9361-fmcomms2-3**.
-  Safely eject the SD Card

Required Hardware
-----------------

-  Xilinx `ZCU102 <https://www.xilinx.com/ZCU102>`__ Board
-  AD-FMCOMMS2-EBZ or AD-FMCOMMS3-EBZ FMC Board.
-  Micro-USB Cable

Testing
=======

-  Connect the AD-FMCOMMS2-EBZ FMC board to the FPGA carrier **HPC0** FMC socket.
-  Connect USB UART J83 (Micro USB) to your host PC.
-  Insert SD card into socket.
-  Configure ZCU102 for SD BOOT.
-  Turn on the power switch on the FPGA board.
-  Observe kernel and serial console messages on your terminal.

Messages
--------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   

   .. raw:: html

      <details><summary>Boot log (click to expand)</summary>

   ::
   
      Xilinx Zynq MP First Stage Boot Loader
      Release 2021.1   Aug  3 2022  -  10:34:27
      NOTICE:  BL31: v2.4(release):xilinx-v2020.2-2024-g0a69763
      NOTICE:  BL31: Built : 07:48:38, Sep 23 2021
      PMUFW:  v1.1
   
   
      U-Boot 2018.01-21439-gd244ce5 (Jul 29 2021 - 16:37:20 +0100) Xilinx ZynqMP ZCU102 revA, Build: jenkins-development-build_uboot-1
   
      I2C:   ready
      DRAM:  4 GiB
      EL Level:       EL2
      Chip ID:        zu9eg
      MMC:   sdhci@ff170000: 0 (SD)
      *** Warning - bad CRC, using default environment
   
      In:    serial@ff000000
      Out:   serial@ff000000
      Err:   serial@ff000000
      Bootmode: LVL_SHFT_SD_MODE1
      Net:   ZYNQ GEM: ff0e0000, phyaddr 15, interface rgmii-id
   
      Warning: ethernet@ff0e0000 using MAC address from ROM
      eth0: ethernet@ff0e0000
      Hit any key to stop autoboot:  0
      switch to partitions #0, OK
      mmc0 is current device
      Device: sdhci@ff170000
      Manufacturer ID: 89
      OEM: 303
      Name: NCard
      Tran Speed: 50000000
      Rd Block Len: 512
      SD version 3.0
      High Capacity: Yes
      Capacity: 14.6 GiB
      Bus Width: 4-bit
      Erase Group Size: 512 Bytes
      reading uEnv.txt
      407 bytes read in 21 ms (18.6 KiB/s)
      Loaded environment from uEnv.txt
      Importing environment from SD ...
      Running uenvcmd ...
      Copying Linux from SD to RAM...
      ** No boot file defined **
      reading system.dtb
      57875 bytes read in 30 ms (1.8 MiB/s)
      reading Image
      32514560 bytes read in 2188 ms (14.2 MiB/s)
      ## Flattened Device Tree blob at 04000000
         Booting using the fdt blob at 0x4000000
         Loading Device Tree to 000000000ffee000, end 000000000ffff212 ... OK
   
      Starting kernel ...
   
      [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
      [    0.000000] Linux version 5.10.0-98248-g1bbe32fa5182 (jenkins@romlxbuild1.adlk.analog.com) (aarch64-xilinx-linux-gcc.real (GCC) 10.2.0, GNU ld (GNU Binutils) 2.35.0.20200730) #1143 SMP Wed Aug 3 18:38:55 IST 2022
      [    0.000000] Machine model: ZynqMP ZCU102 Rev1.0
      [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff000000 (options '115200n8')
      [    0.000000] printk: bootconsole [cdns0] enabled
      [    0.000000] efi: UEFI not found.
      [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
      [    0.000000] Zone ranges:
      [    0.000000]   DMA      [mem 0x0000000000000000-0x000000003fffffff]
      [    0.000000]   DMA32    [mem 0x0000000040000000-0x00000000ffffffff]
      [    0.000000]   Normal   [mem 0x0000000100000000-0x000000087fffffff]
      [    0.000000] Movable zone start for each node
      [    0.000000] Early memory node ranges
      [    0.000000]   node   0: [mem 0x0000000000000000-0x000000007fffffff]
      [    0.000000]   node   0: [mem 0x0000000800000000-0x000000087fffffff]
      [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000087fffffff]
      [    0.000000] psci: probing for conduit method from DT.
      [    0.000000] psci: PSCIv1.1 detected in firmware.
      [    0.000000] psci: Using standard PSCI v0.2 function IDs
      [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
      [    0.000000] psci: SMC Calling Convention v1.2
      [    0.000000] percpu: Embedded 22 pages/cpu s49496 r8192 d32424 u90112
      [    0.000000] Detected VIPT I-cache on CPU0
      [    0.000000] CPU features: detected: ARM erratum 845719
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
      [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1 root=/dev/mmcblk0p2 rw rootwait
      [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] software IO TLB: mapped [mem 0x000000003bfff000-0x000000003ffff000] (64MB)
      [    0.000000] Memory: 3761568K/4194304K available (15488K kernel code, 1672K rwdata, 11952K rodata, 2496K init, 507K bss, 170592K reserved, 262144K cma-reserved)
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
      [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
      [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
      [    0.000000] GIC: Using split EOI/Deactivate mode
      [    0.000000] random: get_random_bytes called from start_kernel+0x31c/0x550 with crng_init=0
      [    0.000000] arch_timer: cp15 timer(s) running at 100.00MHz (phys).
      [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x171024e7e0, max_idle_ns: 440795205315 ns
      [    0.000003] sched_clock: 56 bits at 100MHz, resolution 10ns, wraps every 4398046511100ns
      [    0.008485] Console: colour dummy device 80x25
      [    0.012484] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
      [    0.022841] pid_max: default: 32768 minimum: 301
      [    0.027558] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.034789] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.043434] rcu: Hierarchical SRCU implementation.
      [    0.047568] EFI services will not be available.
      [    0.051941] smp: Bringing up secondary CPUs ...
      [    0.056663] Detected VIPT I-cache on CPU1
      [    0.056702] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [    0.057074] Detected VIPT I-cache on CPU2
      [    0.057098] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [    0.057438] Detected VIPT I-cache on CPU3
      [    0.057461] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [    0.057508] smp: Brought up 1 node, 4 CPUs
      [    0.091780] SMP: Total of 4 processors activated.
      [    0.096452] CPU features: detected: 32-bit EL0 Support
      [    0.101555] CPU features: detected: CRC32 instructions
      [    0.106694] CPU: All CPU(s) started at EL2
      [    0.110736] alternatives: patching kernel code
      [    0.116198] devtmpfs: initialized
      [    0.124524] Registered cp15_barrier emulation handler
      [    0.124575] Registered setend emulation handler
      [    0.128552] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      [    0.138133] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
      [    0.151555] pinctrl core: initialized pinctrl subsystem
      [    0.152221] NET: Registered protocol family 16
      [    0.156648] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
      [    0.162630] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
      [    0.170358] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
      [    0.178166] audit: initializing netlink subsys (disabled)
      [    0.183626] audit: type=2000 audit(0.116:1): state=initialized audit_enabled=0 res=1
      [    0.183979] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
      [    0.197991] ASID allocator initialised with 65536 entries
      [    0.223864] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
      [    0.224919] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
      [    0.231589] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
      [    0.238259] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
      [    1.303615] DRBG: Continuing without Jitter RNG
      [    1.381660] raid6: neonx8   gen()  2149 MB/s
      [    1.449715] raid6: neonx8   xor()  1599 MB/s
      [    1.517778] raid6: neonx4   gen()  2189 MB/s
      [    1.585824] raid6: neonx4   xor()  1567 MB/s
      [    1.653890] raid6: neonx2   gen()  2072 MB/s
      [    1.721945] raid6: neonx2   xor()  1437 MB/s
      [    1.790018] raid6: neonx1   gen()  1775 MB/s
      [    1.858055] raid6: neonx1   xor()  1220 MB/s
      [    1.926112] raid6: int64x8  gen()  1438 MB/s
      [    1.994171] raid6: int64x8  xor()   771 MB/s
      [    2.062250] raid6: int64x4  gen()  1599 MB/s
      [    2.130301] raid6: int64x4  xor()   820 MB/s
      [    2.198373] raid6: int64x2  gen()  1399 MB/s
      [    2.266418] raid6: int64x2  xor()   749 MB/s
      [    2.334489] raid6: int64x1  gen()  1031 MB/s
      [    2.402538] raid6: int64x1  xor()   517 MB/s
      [    2.402576] raid6: using algorithm neonx4 gen() 2189 MB/s
      [    2.406525] raid6: .... xor() 1567 MB/s, rmw enabled
      [    2.411459] raid6: using neon recovery algorithm
      [    2.416472] iommu: Default domain type: Translated
      [    2.421095] SCSI subsystem initialized
      [    2.424756] usbcore: registered new interface driver usbfs
      [    2.430082] usbcore: registered new interface driver hub
      [    2.435360] usbcore: registered new device driver usb
      [    2.440484] mc: Linux media interface: v0.10
      [    2.444611] videodev: Linux video capture interface: v2.00
      [    2.450102] EDAC MC: Ver: 3.0.0
      [    2.453528] zynqmp-ipi-mbox mailbox@ff990400: Registered ZynqMP IPI mbox with TX/RX channels.
      [    2.462023] jesd204: found 0 devices and 0 topologies
      [    2.466674] FPGA manager framework
      [    2.470150] Advanced Linux Sound Architecture Driver Initialized.
      [    2.476459] Bluetooth: Core ver 2.22
      [    2.479633] NET: Registered protocol family 31
      [    2.484033] Bluetooth: HCI device and connection manager initialized
      [    2.490350] Bluetooth: HCI socket layer initialized
      [    2.495192] Bluetooth: L2CAP socket layer initialized
      [    2.500216] Bluetooth: SCO socket layer initialized
      [    2.505419] clocksource: Switched to clocksource arch_sys_counter
      [    2.511214] VFS: Disk quotas dquot_6.6.0
      [    2.515052] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
      [    2.525762] NET: Registered protocol family 2
      [    2.526501] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
      [    2.534679] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
      [    2.542709] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
      [    2.550170] TCP: Hash tables configured (established 32768 bind 32768)
      [    2.556330] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
      [    2.562993] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
      [    2.570161] NET: Registered protocol family 1
      [    2.574635] RPC: Registered named UNIX socket transport module.
      [    2.580231] RPC: Registered udp transport module.
      [    2.584895] RPC: Registered tcp transport module.
      [    2.589564] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    2.596554] PCI: CLS 0 bytes, default 64
      [    2.600273] hw perfevents: no interrupt-affinity property for /pmu, guessing.
      [    2.607124] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
      [    2.615493] Initialise system trusted keyrings
      [    2.619163] workingset: timestamp_bits=62 max_order=20 bucket_order=0
      [    2.626064] NFS: Registering the id_resolver key type
      [    2.630493] Key type id_resolver registered
      [    2.634630] Key type id_legacy registered
      [    2.638627] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    2.645289] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      [    2.652460] fuse: init (API version 7.32)
      [    2.692910] NET: Registered protocol family 38
      [    2.692953] xor: measuring software checksum speed
      [    2.700640]    8regs           :  2363 MB/sec
      [    2.704306]    32regs          :  2799 MB/sec
      [    2.709249]    arm64_neon      :  2380 MB/sec
      [    2.709442] xor: using function: 32regs (2799 MB/sec)
      [    2.714464] Key type asymmetric registered
      [    2.718526] Asymmetric key parser 'x509' registered
      [    2.723387] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
      [    2.730724] io scheduler mq-deadline registered
      [    2.735220] io scheduler kyber registered
      [    2.764706] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      [    2.769571] cacheinfo: Unable to detect cache hierarchy for CPU 0
      [    2.775675] brd: module loaded
      [    2.779959] loop: module loaded
      [    2.780252] Registered mathworks_ip class
      [    2.783724] libphy: Fixed MDIO Bus: probed
      [    2.786672] tun: Universal TUN/TAP device driver, 1.6
      [    2.790765] CAN device driver interface
      [    2.795331] usbcore: registered new interface driver asix
      [    2.799893] usbcore: registered new interface driver ax88179_178a
      [    2.805922] usbcore: registered new interface driver cdc_ether
      [    2.811716] usbcore: registered new interface driver net1080
      [    2.817337] usbcore: registered new interface driver cdc_subset
      [    2.823218] usbcore: registered new interface driver zaurus
      [    2.828771] usbcore: registered new interface driver cdc_ncm
      [    2.835212] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    2.840850] ehci-pci: EHCI PCI platform driver
      [    2.845685] usbcore: registered new interface driver uas
      [    2.850564] usbcore: registered new interface driver usb-storage
      [    2.856553] usbcore: registered new interface driver usbserial_generic
      [    2.863005] usbserial: USB Serial support registered for generic
      [    2.868976] usbcore: registered new interface driver ftdi_sio
      [    2.874680] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    2.881952] usbcore: registered new interface driver upd78f0730
      [    2.887832] usbserial: USB Serial support registered for upd78f0730
      [    2.895526] rtc_zynqmp ffa60000.rtc: registered as rtc0
      [    2.899252] rtc_zynqmp ffa60000.rtc: setting system clock to 2022-09-06T11:23:39 UTC (1662463419)
      [    2.908113] i2c /dev entries driver
      [    2.913394] usbcore: registered new interface driver uvcvideo
      [    2.917227] USB Video Class driver (1.1.1)
      [    2.922790] Bluetooth: HCI UART driver ver 2.3
      [    2.925710] Bluetooth: HCI UART protocol H4 registered
      [    2.930808] Bluetooth: HCI UART protocol BCSP registered
      [    2.936096] Bluetooth: HCI UART protocol LL registered
      [    2.941187] Bluetooth: HCI UART protocol ATH3K registered
      [    2.946563] Bluetooth: HCI UART protocol Three-wire (H5) registered
      [    2.952812] Bluetooth: HCI UART protocol Intel registered
      [    2.958151] Bluetooth: HCI UART protocol QCA registered
      [    2.963354] usbcore: registered new interface driver bcm203x
      [    2.968973] usbcore: registered new interface driver bpa10x
      [    2.974512] usbcore: registered new interface driver bfusb
      [    2.979961] usbcore: registered new interface driver btusb
      [    2.985427] usbcore: registered new interface driver ath3k
      [    2.990910] EDAC MC: ECC not enabled
      [    2.994535] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
      [    3.006844] sdhci: Secure Digital Host Controller Interface driver
      [    3.012641] sdhci: Copyright(c) Pierre Ossman
      [    3.016959] sdhci-pltfm: SDHCI platform and OF driver helper
      [    3.023026] ledtrig-cpu: registered to indicate activity on CPUs
      [    3.028565] SMCCC: SOC_ID: ARCH_SOC_ID not implemented, skipping ....
      [    3.034994] zynqmp_firmware_probe Platform Management API v1.1
      [    3.040751] zynqmp_firmware_probe Trustzone version v1.0
      [    3.078127] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
      [    3.124554] zynqmp-aes firmware:zynqmp-firmware:zynqmp-aes: will run requests pump with realtime priority
      [    3.140222] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
      [    3.140932] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
      [    3.146446] usbcore: registered new interface driver usbhid
      [    3.151833] usbhid: USB HID core driver
      [    3.162357] axi_sysid 85000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    3.164705] axi_sysid 85000000.axi-sysid-0: [fmcomms2] on [zcu102] git branch <hdl_2021_r1> git <6a6c5acc8ec422c068c7787cdeb5b0ee4ae1aa51> clean [2022-05-20 17:39:13] UTC
      [    3.180217] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
      [    3.186586] usbcore: registered new interface driver snd-usb-audio
      [    3.194020] pktgen: Packet Generator for packet performance testing. Version: 2.75
      [    3.200241] Initializing XFRM netlink socket
      [    3.204059] NET: Registered protocol family 10
      [    3.208793] Segment Routing with IPv6
      [    3.212168] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    3.218242] NET: Registered protocol family 17
      [    3.222335] NET: Registered protocol family 15
      [    3.226824] can: controller area network core
      [    3.231087] NET: Registered protocol family 29
      [    3.235474] can: raw protocol
      [    3.238410] can: broadcast manager protocol
      [    3.242565] can: netlink gateway - max_hops=1
      [    3.246958] Bluetooth: RFCOMM TTY layer initialized
      [    3.251738] Bluetooth: RFCOMM socket layer initialized
      [    3.256847] Bluetooth: RFCOMM ver 1.11
      [    3.260557] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
      [    3.265828] Bluetooth: BNEP filters: protocol multicast
      [    3.271022] Bluetooth: BNEP socket layer initialized
      [    3.275949] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
      [    3.281833] Bluetooth: HIDP socket layer initialized
      [    3.286900] 9pnet: Installing 9P2000 support
      [    3.291011] NET: Registered protocol family 36
      [    3.295427] Key type dns_resolver registered
      [    3.299869] registered taskstats version 1
      [    3.303725] Loading compiled-in X.509 certificates
      [    3.308834] Btrfs loaded, crc32c=crc32c-generic
      [    3.321662] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 48, base_baud = 6249999) is a xuartps
      [    3.330682] printk: console [ttyPS0] enabled
      [    3.330682] printk: console [ttyPS0] enabled
      [    3.334977] printk: bootconsole [cdns0] disabled
      [    3.334977] printk: bootconsole [cdns0] disabled
      [    3.344620] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 49, base_baud = 6249999) is a xuartps
      [    3.357820] of-fpga-region fpga-full: FPGA Region probed
      [    3.364788] nwl-pcie fd0e0000.pcie: host bridge /axi/pcie@fd0e0000 ranges:
      [    3.371686] nwl-pcie fd0e0000.pcie:      MEM 0x00e0000000..0x00efffffff -> 0x00e0000000
      [    3.379693] nwl-pcie fd0e0000.pcie:      MEM 0x0600000000..0x07ffffffff -> 0x0600000000
      [    3.387762] nwl-pcie fd0e0000.pcie: Link is DOWN
      [    3.392522] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
      [    3.398706] pci_bus 0000:00: root bus resource [bus 00-ff]
      [    3.404187] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
      [    3.411056] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
      [    3.418560] pci 0000:00:00.0: [10ee:d021] type 01 class 0x060400
      [    3.424617] pci 0000:00:00.0: PME# supported from D0 D1 D2 D3hot
      [    3.435384] pci 0000:00:00.0: PCI bridge to [bus 01-0c]
      [    3.441391] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
      [    3.448578] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
      [    3.455747] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
      [    3.462922] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
      [    3.470090] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
      [    3.477263] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
      [    3.484430] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
      [    3.491596] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
      [    3.498992] xilinx-zynqmp-dpdma fd4c0000.dma-controller: Xilinx DPDMA engine is probed
      [    3.507572] ahci-ceva fd0c0000.ahci: supply ahci not found, using dummy regulator
      [    3.515112] ahci-ceva fd0c0000.ahci: supply phy not found, using dummy regulator
      [    3.523616] ad9361 spi1.0: ad9361_probe : enter (ad9361)
      [    3.529870] ad9361 spi1.0: No GPIOs defined for ext band ctrl
      [    3.545027] random: fast init done
      [    3.760865] ad9361 spi1.0: ad9361_probe : AD936x Rev 0 successfully initialized
      [    3.768944] spi-nor spi0.0: SPI-NOR-UniqueID 2eae9700180c001300980596158d
      [    3.775732] spi-nor spi0.0: found mt25qu512a, expected m25p80
      [    3.782144] spi-nor spi0.0: trying to lock already unlocked area
      [    3.788148] spi-nor spi0.0: mt25qu512a (131072 Kbytes)
      [    3.793311] 4 fixed-partitions partitions found on MTD device spi0.0
      [    3.799654] Creating 4 MTD partitions on "spi0.0":
      [    3.804438] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
      [    3.810953] 0x000000100000-0x000000600000 : "qspi-linux"
      [    3.816918] 0x000000600000-0x000000620000 : "qspi-device-tree"
      [    3.823419] 0x000000620000-0x000000c00000 : "qspi-rootfs"
      [    3.832024] macb ff0e0000.ethernet: Not enabling partial store and forward
      [    3.839556] libphy: MACB_mii_bus: probed
      [    3.844359] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 30 (00:0a:35:05:60:78)
      [    3.854582] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
      [    3.861146] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
      [    3.867675] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
      [    3.874214] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
      [    3.884317] pca953x 0-0020: supply vcc not found, using dummy regulator
      [    3.891010] pca953x 0-0020: using no AI
      [    3.895486] gpio-496 (sel0): hogged as output/low
      [    3.900390] gpio-497 (sel1): hogged as output/high
      [    3.905378] gpio-498 (sel2): hogged as output/high
      [    3.910360] gpio-499 (sel3): hogged as output/high
      [    3.915564] pca953x 0-0021: supply vcc not found, using dummy regulator
      [    3.922232] pca953x 0-0021: using no AI
      [    3.928031] ina2xx 2-0040: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.935065] ina2xx 2-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.942101] ina2xx 2-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.949132] ina2xx 2-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.956161] ina2xx 2-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.963199] ina2xx 2-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.970228] ina2xx 2-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.977262] ina2xx 2-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.984347] ina2xx 2-004a: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.991379] ina2xx 2-004b: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.997782] i2c i2c-0: Added multiplexed i2c bus 2
      [    4.003375] ina2xx 3-0040: power monitor ina226 (Rshunt = 2000 uOhm)
      [    4.010409] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.017451] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.024482] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.031519] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.038557] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.045584] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.052613] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.059015] i2c i2c-0: Added multiplexed i2c bus 3
      [    4.114980] i2c i2c-0: Added multiplexed i2c bus 4
      [    4.119924] i2c i2c-0: Added multiplexed i2c bus 5
      [    4.124719] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
      [    4.132067] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 32
      [    4.139870] at24 6-0054: supply vcc not found, using dummy regulator
      [    4.146758] at24 6-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
      [    4.153506] i2c i2c-1: Added multiplexed i2c bus 6
      [    4.159790] si5341 7-0036: Chip: 5341 Grade: 1 Rev: 1
      [    4.197775] i2c i2c-1: Added multiplexed i2c bus 7
      [    4.205453] si570 8-005d: registered, current frequency 300000000 Hz
      [    4.211852] i2c i2c-1: Added multiplexed i2c bus 8
      [    4.231656] si570 9-005d: registered, current frequency 148500000 Hz
      [    4.238059] i2c i2c-1: Added multiplexed i2c bus 9
      [    4.243109] si5324 10-0069: si5328 probed
      [    4.309842] si5324 10-0069: si5328 probe successful
      [    4.314774] i2c i2c-1: Added multiplexed i2c bus 10
      [    4.319807] i2c i2c-1: Added multiplexed i2c bus 11
      [    4.324836] i2c i2c-1: Added multiplexed i2c bus 12
      [    4.329872] i2c i2c-1: Added multiplexed i2c bus 13
      [    4.334748] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
      [    4.343941] at24 14-0050: supply vcc not found, using dummy regulator
      [    4.350728] at24 14-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      [    4.357475] i2c i2c-1: Added multiplexed i2c bus 14
      [    4.362511] i2c i2c-1: Added multiplexed i2c bus 15
      [    4.367546] i2c i2c-1: Added multiplexed i2c bus 16
      [    4.372580] i2c i2c-1: Added multiplexed i2c bus 17
      [    4.377614] i2c i2c-1: Added multiplexed i2c bus 18
      [    4.382653] i2c i2c-1: Added multiplexed i2c bus 19
      [    4.387696] i2c i2c-1: Added multiplexed i2c bus 20
      [    4.392735] i2c i2c-1: Added multiplexed i2c bus 21
      [    4.397610] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
      [    4.405217] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 33
      [    4.415375] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
      [    4.459408] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
      [    4.502741] mmc0: new high speed SDHC card at address b368
      [    4.508564] mmcblk0: mmc0:b368 NCard 14.6 GiB
      [    4.514406]  mmcblk0: p1 p2 p3
      [    5.255248] cf_axi_adc 99020000.cf-ad9361-lpc: ADI AIM (10.01.b) at 0x99020000 mapped to 0x(____ptrval____), probed ADC AD9361 as MASTER
      [    5.285857] cf_axi_dds 99024000.cf-ad9361-dds-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x99024000 mapped to 0x(____ptrval____), probed DDS AD9361
      [    5.301580] zynqmp-display fd4a0000.display: vtc bridge property not present
      [    5.309785] zynqmp_clk_divider_set_rate() set divider failed for spi1_ref_div1, ret = -13
      [    5.319469] xilinx-dp-snd-codec fd4a0000.display:zynqmp_dp_snd_codec0: Failed to get required clock freq
      [    5.328966] xilinx-dp-snd-codec: probe of fd4a0000.display:zynqmp_dp_snd_codec0 failed with error -22
      [    5.338532] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
      [    5.346700] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
      [    5.354967] OF: graph: no port node found in /axi/display@fd4a0000
      [    5.361363] xlnx-drm xlnx-drm.0: bound fd4a0000.display (ops 0xffffffc010ffd810)
      [    6.445437] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
      [    6.453085] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.display on minor 0
      [    6.460577] zynqmp-display fd4a0000.display: ZynqMP DisplayPort Subsystem driver probed
      [    6.468896] ahci-ceva fd0c0000.ahci: supply ahci not found, using dummy regulator
      [    6.476444] ahci-ceva fd0c0000.ahci: supply phy not found, using dummy regulator
      [    6.483895] ahci-ceva fd0c0000.ahci: supply target not found, using dummy regulator
      [    6.501782] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
      [    6.510739] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst
      [    6.521288] scsi host0: ahci-ceva
      [    6.524875] scsi host1: ahci-ceva
      [    6.528305] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 45
      [    6.536221] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 45
      [    6.544870] OF: graph: no port node found in /axi/phy@fd400000
      [    6.561006] input: gpio-keys as /devices/platform/gpio-keys/input/input0
      [    6.568247] of_cfs_init
      [    6.570705] of_cfs_init: OK
      [    6.573691] cfg80211: Loading compiled-in X.509 certificates for regulatory database
      [    6.712063] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
      [    6.718590] clk: Not disabling unused clocks
      [    6.723122] ALSA device list:
      [    6.726081]   No soundcards found.
      [    6.729763] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
      [    6.738370] cfg80211: failed to load regulatory.db
      [    6.855627] ata2: SATA link down (SStatus 0 SControl 330)
      [    6.861043] ata1: SATA link down (SStatus 0 SControl 330)
      [    7.529447] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
      [   14.380304] EXT4-fs (mmcblk0p2): warning: mounting fs with errors, running e2fsck is recommended
      [   14.492024] EXT4-fs (mmcblk0p2): recovery complete
      [   14.578133] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [   14.586257] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [   14.599775] devtmpfs: mounted
      [   14.603610] Freeing unused kernel memory: 2496K
      [   14.608263] Run /sbin/init as init process
      [   15.227496] systemd[1]: systemd 247.3-7+rpi1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [   15.250752] systemd[1]: Detected architecture arm64.
   
      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!
   
      [   15.282449] systemd[1]: Set hostname to <analog>.
      [   16.855957] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [   17.084624] systemd[1]: Queued start job for default target Graphical Interface.
      [   17.093226] random: systemd: uninitialized urandom read (16 bytes read)
      [   17.100036] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [   17.112382] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [   17.121424] systemd[1]: Created slice system-getty.slice.
      [  OK  ] Created slice system-getty.slice.
      [   17.141524] random: systemd: uninitialized urandom read (16 bytes read)
      [   17.148512] systemd[1]: Created slice system-modprobe.slice.
      [  OK  ] Created slice system-modprobe.slice.
      [   17.169507] random: systemd: uninitialized urandom read (16 bytes read)
      [   17.176464] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [   17.197816] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [   17.221734] systemd[1]: Created slice User and Session Slice.
      [  OK  ] Created slice User and Session Slice.
      [   17.241765] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [   17.265740] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [   17.278165] systemd[1]: Reached target Slices.
      [  OK  ] Reached target Slices.
      [   17.293632] systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      [   17.310254] systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [   17.325846] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [   17.349668] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [   17.376773] systemd[1]: Listening on Journal Audit Socket.
      [  OK  ] Listening on Journal Audit Socket.
      [   17.397860] systemd[1]: Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket (/dev/log).
      [   17.421888] systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      [   17.445475] systemd[1]: Listening on udev Control Socket.
      [  OK  ] Listening on udev Control Socket.
      [   17.465827] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [   17.487436] systemd[1]: Mounting Huge Pages File System...
               Mounting Huge Pages File System...
      [   17.503356] systemd[1]: Mounting POSIX Message Queue File System...
               Mounting POSIX Message Queue File System...
      [   17.527103] systemd[1]: Mounting RPC Pipe File System...
               Mounting RPC Pipe File System...
      [   17.543385] systemd[1]: Mounting Kernel Debug File System...
               Mounting Kernel Debug File System...
      [   17.561978] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
      [   17.570631] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [   17.583314] systemd[1]: Starting Restore / save the current clock...
               Starting Restore / save the current clock...
      [   17.609712] systemd[1]: Starting Set the console keyboard layout...
               Starting Set the console keyboard layout...
      [   17.636616] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [   17.650210] systemd[1]: Starting Load Kernel Module configfs...
               Starting Load Kernel Module configfs...
      [   17.667701] systemd[1]: Starting Load Kernel Module drm...
               Starting Load Kernel Module drm...
      [   17.687697] systemd[1]: Starting Load Kernel Module fuse...
               Starting Load Kernel Module fuse...
      [   17.708717] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [   17.717983] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [   17.729053] systemd[1]: Starting Journal Service...
               Starting Journal Service...
      [   17.750063] systemd[1]: Starting Load Kernel Modules...
               Starting Load Kernel Modules...
      [   17.767598] systemd[1]: Starting Remount Root and Kernel File Systems...
               Starting Remount Root and Kernel File Systems...
      [   17.791561] systemd[1]: Starting Coldplug All udev Devices...
               Starting Coldplug All udev Devices...
      [   17.814846] systemd[1]: Mounted Huge Pages File System.
      [  OK  ] Mounted Huge Pages File System.
      [   17.843501] systemd[1]: Mounted POSIX Message Queue File System.
      [  OK  ] Mounted POSIX Message Queue File System.
      [   17.866054] systemd[1]: Mounted RPC Pipe File System.
      [  OK  ] Mounted RPC Pipe File System.
      [   17.882062] systemd[1]: Mounted Kernel Debug File System.
      [  OK  ] Mounted Kernel Debug File System.
      [   17.906458] systemd[1]: Finished Restore / save the current clock.
      [  OK  ] Finished Restore / save the current clock.
      [   17.930679] systemd[1]: Finished Set the console keyboard layout.
      [  OK  ] Finished Set the console keyboard layout.
      [   17.953966] systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
      [  OK  ] Finished Load Kernel Module configfs.
      [  OK  ] Finished Load Kernel Module drm.
      [   17.997740] random: crng init done
      [   18.001139] random: 7 urandom warning(s) missed due to ratelimiting
      [  OK  ] Finished Load Kernel Module fuse.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
               Mounting FUSE Control File System...
               Mounting Kernel Configuration File System...
               Starting Apply Kernel Variables...
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Finished Apply Kernel Variables.
      [  OK  ] Finished Remount Root and Kernel File Systems.
               Starting Flush Journal to Persistent Storage...
               Starting Load/Save Random Seed...
               Starting Create System Users...
      [  OK  ] Finished Coldplug All udev Devices.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Wait for udev To …plete Device Initialization...
      [*     ] (1 of 10) A start job is running fo…d/Save Random Seed (3s / 10min 1s)
      [   20.713866] EXT4-fs error (device mmcblk0p2): ext4_mb_generate_buddy:802: group 32, block bitmap and bg descriptor inconsistent: 8461 vs 10906 free clusters
      [   20.731848] EXT4-fs error (device mmcblk0p2): ext4_mb_generate_buddy:802: group 64, block bitmap and bg descriptor inconsistent: 23266 vs 23260 free clusters
      [   20.779729] EXT4-fs error (device mmcblk0p2): ext4_mb_generate_buddy:802: group 0, block bitmap and bg descriptor inconsistent: 18343 vs 18331 free clusters
      [   20.793915] EXT4-fs error (device mmcblk0p2): ext4_mb_generate_buddy:802: group 25, block [  OK  ] Finished Helper to synchronize boot up for ifupdown.
      [  OK  ] Finished Create System Users.
               Starting Create Static Device Nodes in /dev...
      [   20.874353] EXT4-fs error (device mmcblk0p2): ext4_mb_generate_buddy:802: group 59, block bitmap and bg descriptor inconsistent: 2718 vs 2714 free clusters
      [   20.910902] EXT4-fs error (device mmcblk0p2): ext4_lookup:1708: inode #16388: comm systemd-journal: deleted inode referenced: 11882
      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Finished Create Static Device Nodes in /dev.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting Rule-based Manage…for Device Events and Files...
      [     *] (3 of 8) A start job is running for…rtuuid/f7eeebee-01 (9s / 1min 30s)
      [   27.126343] EXT4-fs error (device mmcblk0p2): ext4_lookup:1708: inode #16388: comm systemd[    **] (3 of 8) A start job is running for…tuuid/f7eeebee-01 (10s / 1min 30s)
      [   27.448819] EXT4-fs error (device mmcblk0p2): ext4_lookup:1708: inode #16388: comm systemd[  OK  ] Finished Flush Journal to Persistent Storage.
      [  OK  ] Started Rule-based Manager for Device Events and Files.
               Starting Show Plymouth Boot Screen...
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Found device /dev/ttyPS0.
      [  OK  ] Reached target Hardware activated USB gadget.
               Starting Load Kernel Modules...
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Found device /dev/ttyS0.
      [  OK  ] Found device /dev/disk/by-partuuid/f7eeebee-01.
      [  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
               Starting File System Check…isk/by-partuuid/f7eeebee-01...
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
      [  OK  ] Finished File System Check…/disk/by-partuuid/f7eeebee-01.
               Mounting /boot...
      [  OK  ] Started File System Check Daemon to report status.
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
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Finished Update UTMP about System Boot/Shutdown.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Started Daily apt download activities.
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
      [  OK  ] Started Discard unused blocks once a week.
      [  OK  ] Started Daily rotation of log files.
      [  OK  ] Started Daily man-db regeneration.
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Reached target Paths.
      [  OK  ] Reached target Timers.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on CUPS Scheduler.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Listening on Erlang Port Mapper Daemon Activation Socket.
      [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Reached target Sockets.
      [  OK  ] Reached target Basic System.
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
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started DHCP Client Daemon.
      [  OK  ] Finished Raise network interfaces.
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Started System Logging Service.
      [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
      [   32.756194] EXT4-fs error (device mmcblk0p2): ext4_mb_generate_buddy:802: group 75, block bitmap and bg descriptor inconsistent: 32730 vs 32733 free clusters
      [FAILED] Failed to start Rotate log files.
      See 'systemctl status logrotate.service' for details.
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
               Starting Online ext4 Metad…a Check for All Filesystems...
      [  OK  ] Finished Online ext4 Metadata Check for All Filesystems.
      [  OK  ] Finished Creating IIOD Context Attributes....
      [  OK  ] Started User Login Management.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Reached target Network.
      [  OK  ] Reached target Network is Online.
               Starting CUPS Scheduler...
      [  OK  ] Started Erlang Port Mapper Daemon.
               Starting Load USB gadget scheme...
               Starting HTTP based time synchronization tool...
      [  OK  ] Started IIO Daemon.
               Starting Internet superserver...
               Starting /etc/rc.local Compatibility...
               Starting OpenBSD Secure Shell server...
               Starting Permit User Sessions...
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Finished Permit User Sessions.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started Authorization Manager.
               Starting Modem Manager...
      [  OK  ] Started Internet superserver.
      [  OK  ] Finished Load USB gadget scheme.
               Mounting Mount FunctionFS instance...
      [  OK  ] Found device /dev/ttyGS0.
      [  OK  ] Mounted Mount FunctionFS instance.
               Starting IIO Daemon with USB FFS support...
               Stopping IIO Daemon...
      [  OK  ] Stopped IIO Daemon.
      [  OK  ] Started IIO Daemon with USB FFS support.
               Starting Start USB gadget scheme...
      [  OK  ] Started OpenBSD Secure Shell server.
   
      Raspbian GNU/Linux 11 analog ttyPS0
   
      analog login: root (automatic login)
   

   .. raw:: html

      </details>



.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# iio_info | grep iio:device
              iio:device0: ams
              iio:device1: ad9361-phy
              iio:device2: ad7291
              iio:device3: cf-ad9361-lpc (buffer capable)
              iio:device4: cf-ad9361-dds-core-lpc (buffer capable)
   


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# fru-dump -b /sys/bus/i2c/devices/14-0050/eeprom
      read 256 bytes from /sys/bus/i2c/devices/14-0050/eeprom
      Date of Man     : Wed Jun 18 12:51:00 2014
      Manufacturer    : Analog Devices
      Product Name    : AD9361 RF Hardware Development Kit
      Serial Number   : 00051
      Part Number     : AD-FMCOMMS2-EBZ
      FRU File ID     : Empty Field
      PCB Rev         : C
      PCB ID          : 9361FMC01A
      BOM Rev         : 1
      Uses LVDS       : Y
   


IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.
