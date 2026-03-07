AD9695 FMC Card Reference Design
================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/ad9695_fmc/index.html\


Overview
--------

The AD9695 is a dual 14-bit, 1300/625MSPS analog-to-digital converter (ADC) featuring an on-chip buffer and a sample-and-hold circuit designed for low power, small size, and ease of use. The dual ADC cores feature a multistage, differential pipelined architecture with integrated output error correction logic. Each ADC features wide bandwidth inputs supporting a variety of user-selectable input ranges.

The AD9695-FMC reference design is a processor based (e.g. Microblaze) embedded system. The design consists of a receive chain that transports the captured samples from the ADC to the system memory (DDR).

All cores from the receive chain are programmable through an AXI-Lite interface.

Supported Devices
-----------------

-  :adi:`AD9695-1300EBZ <AD9695>`

Supported Carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`_ - HPC1 Slot

Required Hardware
-----------------

-  :adi:`AD9695-1300EBZ <AD9695>`
-  `ZCU102 <https://www.xilinx.com/ZCU102>`_
-  :doc:`AD-SYNCHRONA14-EBZ </wiki-migration/resources/eval/user-guides/ad-synchrona14-ebz>`
-  5 \* SMA to SMA cable
-  3 \* 50 Ohm DC to 12Ghz SMA Termination

Clock Selection
~~~~~~~~~~~~~~~

-  External clock source :doc:`AD-SYNCHRONA14-EBZ </wiki-migration/resources/eval/user-guides/ad-synchrona14-ebz>`
-  SYSREF clocks are LVDS
-  ADCCLK and REFCLK are LVPECL

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/timing_ad9695_1.png
   :alt: timing_ad9695_1.png

Synchrona Output Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only the channels presented in the clocking selection are relevant. For the rest, you can either disable them or just put a divided frequency of the source clock.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/synchronasettings1.png
   :alt: synchronasettings1.png

Block Diagram
~~~~~~~~~~~~~

The data path and clock domains are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9695_fmc_02.svg
   :alt: ad9695_fmc_02.svg

The design has one JESD receive chain with 4 lanes at rate of 13Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module and transport layer represented by a RX JESD TPL module. The link operates in Subclass 1.

The link is set for full bandwidth mode and operate with the following parameters:

Deframer paramaters: L=4, M=2, F=1, S=1, N’=16

| SYSREF - 5.078125 MHZ
| REFCLK – 325MHz (Lane Rate/40)
| DEVICECLK -325 MHz
| ADCCLK – 1300MHz
| JESD204B Lane Rate – 13Gbps

The transport layer component presents on its output 128 bits at once on every clock cycle, representing 4 samples per converter. The two receive chains are merged together and transferred to the DDR with a single DMA.

Building the HDL project
~~~~~~~~~~~~~~~~~~~~~~~~

ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository. Then go to the /projects/ad9695_fmc/zcu102 location and run the make command by typing in your command prompt:

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad9695_fmc/zcu102
   user@analog:~/hdl/projects/ad9695_fmc/zcu102$ make

A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

System setup
~~~~~~~~~~~~

Connections
^^^^^^^^^^^

AD9695 connected to ZCU102 on FMC HPC1

====== ========
ZCU102 SYNCRONA
====== ========
J79    CH2_P
J80    CH2_N
====== ========

============ ========
ADC9695 EVAL SYNCRONA
============ ========
J202         CH10_P
J200         CH1_P
P202         CH9_P
============ ========

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/setup_ad9695_zcu102_1.jpg
   :alt: setup_ad9695_zcu102_1.jpg

Messages
^^^^^^^^



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   

   .. raw:: html

      <details><summary>Boot log (click to expand)</summary>

   ::
   
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
      [    0.000000] On node 0 totalpages: 1048576
      [    0.000000]   DMA zone: 3584 pages used for memmap
      [    0.000000]   DMA zone: 0 pages reserved
      [    0.000000]   DMA zone: 262144 pages, LIFO batch:63
      [    0.000000]   DMA32 zone: 3584 pages used for memmap
      [    0.000000]   DMA32 zone: 262144 pages, LIFO batch:63
      [    0.000000]   Normal zone: 7168 pages used for memmap
      [    0.000000]   Normal zone: 524288 pages, LIFO batch:63
      [    0.000000] psci: probing for conduit method from DT.
      [    0.000000] psci: PSCIv1.1 detected in firmware.
      [    0.000000] psci: Using standard PSCI v0.2 function IDs
      [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
      [    0.000000] psci: SMC Calling Convention v1.2
      [    0.000000] percpu: Embedded 22 pages/cpu s49496 r8192 d32424 u90112
      [    0.000000] pcpu-alloc: s49496 r8192 d32424 u90112 alloc=22\*4096
      [    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
      [    0.000000] Detected VIPT I-cache on CPU0
      [    0.000000] CPU features: detected: ARM erratum 845719
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
      [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1 root=/dev/mmcblk0p2 rw rootwait
      [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] software IO TLB: mapped [mem 0x000000003bfff000-0x000000003ffff000] (64MB)
      [    0.000000] Memory: 3761576K/4194304K available (15488K kernel code, 1672K rwdata, 11952K rodata, 2496K init, 507K bss, 170584K reserved, 262144K cma-reserved)
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
      [    0.008460] Console: colour dummy device 80x25
      [    0.012482] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
      [    0.022841] pid_max: default: 32768 minimum: 301
      [    0.027560] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.034788] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.043409] rcu: Hierarchical SRCU implementation.
      [    0.047553] EFI services will not be available.
      [    0.051939] smp: Bringing up secondary CPUs ...
      [    0.056659] Detected VIPT I-cache on CPU1
      [    0.056698] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [    0.057065] Detected VIPT I-cache on CPU2
      [    0.057089] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [    0.057427] Detected VIPT I-cache on CPU3
      [    0.057450] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [    0.057496] smp: Brought up 1 node, 4 CPUs
      [    0.091780] SMP: Total of 4 processors activated.
      [    0.096452] CPU features: detected: 32-bit EL0 Support
      [    0.101555] CPU features: detected: CRC32 instructions
      [    0.106694] CPU: All CPU(s) started at EL2
      [    0.110736] alternatives: patching kernel code
      [    0.116173] devtmpfs: initialized
      [    0.124277] Registered cp15_barrier emulation handler
      [    0.124327] Registered setend emulation handler
      [    0.128308] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      [    0.137890] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
      [    0.151251] pinctrl core: initialized pinctrl subsystem
      [    0.151892] NET: Registered protocol family 16
      [    0.156335] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
      [    0.162327] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
      [    0.170055] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
      [    0.177862] audit: initializing netlink subsys (disabled)
      [    0.183314] audit: type=2000 audit(0.116:1): state=initialized audit_enabled=0 res=1
      [    0.183661] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
      [    0.197688] ASID allocator initialised with 65536 entries
      [    0.223211] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
      [    0.224270] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
      [    0.230941] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
      [    0.237606] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
      [    1.302908] DRBG: Continuing without Jitter RNG
      [    1.381012] raid6: neonx8   gen()  2149 MB/s
      [    1.449068] raid6: neonx8   xor()  1597 MB/s
      [    1.517125] raid6: neonx4   gen()  2193 MB/s
      [    1.585177] raid6: neonx4   xor()  1561 MB/s
      [    1.653252] raid6: neonx2   gen()  2074 MB/s
      [    1.721299] raid6: neonx2   xor()  1434 MB/s
      [    1.789367] raid6: neonx1   gen()  1776 MB/s
      [    1.857412] raid6: neonx1   xor()  1220 MB/s
      [    1.925471] raid6: int64x8  gen()  1438 MB/s
      [    1.993531] raid6: int64x8  xor()   771 MB/s
      [    2.061597] raid6: int64x4  gen()  1599 MB/s
      [    2.129650] raid6: int64x4  xor()   815 MB/s
      [    2.197722] raid6: int64x2  gen()  1399 MB/s
      [    2.265775] raid6: int64x2  xor()   747 MB/s
      [    2.333852] raid6: int64x1  gen()  1034 MB/s
      [    2.401898] raid6: int64x1  xor()   517 MB/s
      [    2.401936] raid6: using algorithm neonx4 gen() 2193 MB/s
      [    2.405884] raid6: .... xor() 1561 MB/s, rmw enabled
      [    2.410819] raid6: using neon recovery algorithm
      [    2.415807] iommu: Default domain type: Translated 
      [    2.420451] SCSI subsystem initialized
      [    2.423986] libata version 3.00 loaded.
      [    2.424114] usbcore: registered new interface driver usbfs
      [    2.429443] usbcore: registered new interface driver hub
      [    2.434718] usbcore: registered new device driver usb
      [    2.439846] mc: Linux media interface: v0.10
      [    2.443966] videodev: Linux video capture interface: v2.00
      [    2.449459] EDAC MC: Ver: 3.0.0
      [    2.452879] zynqmp-ipi-mbox mailbox@ff990400: Registered ZynqMP IPI mbox with TX/RX channels.
      [    2.461324] jesd204: found 0 devices and 0 topologies
      [    2.466034] FPGA manager framework
      [    2.469505] Advanced Linux Sound Architecture Driver Initialized.
      [    2.475811] Bluetooth: Core ver 2.22
      [    2.478992] NET: Registered protocol family 31
      [    2.483393] Bluetooth: HCI device and connection manager initialized
      [    2.489710] Bluetooth: HCI socket layer initialized
      [    2.494552] Bluetooth: L2CAP socket layer initialized
      [    2.499576] Bluetooth: SCO socket layer initialized
      [    2.504776] clocksource: Switched to clocksource arch_sys_counter
      [    2.510570] VFS: Disk quotas dquot_6.6.0
      [    2.514414] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
      [    2.525104] NET: Registered protocol family 2
      [    2.525850] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
      [    2.534039] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
      [    2.542068] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
      [    2.549514] TCP: Hash tables configured (established 32768 bind 32768)
      [    2.555688] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
      [    2.562353] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
      [    2.569518] NET: Registered protocol family 1
      [    2.573984] RPC: Registered named UNIX socket transport module.
      [    2.579589] RPC: Registered udp transport module.
      [    2.584256] RPC: Registered tcp transport module.
      [    2.588925] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    2.595917] PCI: CLS 0 bytes, default 64
      [    2.599621] hw perfevents: no interrupt-affinity property for /pmu, guessing.
      [    2.606481] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
      [    2.614806] Initialise system trusted keyrings
      [    2.618524] workingset: timestamp_bits=62 max_order=20 bucket_order=0
      [    2.625408] NFS: Registering the id_resolver key type
      [    2.629854] Key type id_resolver registered
      [    2.633994] Key type id_legacy registered
      [    2.637983] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    2.644648] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      [    2.651817] fuse: init (API version 7.32)
      [    2.690955] NET: Registered protocol family 38
      [    2.690998] xor: measuring software checksum speed
      [    2.698686]    8regs           :  2363 MB/sec
      [    2.702351]    32regs          :  2799 MB/sec
      [    2.707293]    arm64_neon      :  2380 MB/sec
      [    2.707484] xor: using function: 32regs (2799 MB/sec)
      [    2.712510] Key type asymmetric registered
      [    2.716571] Asymmetric key parser 'x509' registered
      [    2.721434] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
      [    2.728769] io scheduler mq-deadline registered
      [    2.733265] io scheduler kyber registered
      [    2.762472] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      [    2.766891] cacheinfo: Unable to detect cache hierarchy for CPU 0
      [    2.773435] brd: module loaded
      [    2.777653] loop: module loaded
      [    2.777938] Registered mathworks_ip class
      [    2.781417] libphy: Fixed MDIO Bus: probed
      [    2.784422] tun: Universal TUN/TAP device driver, 1.6
      [    2.788532] CAN device driver interface
      [    2.793020] usbcore: registered new interface driver asix
      [    2.797656] usbcore: registered new interface driver ax88179_178a
      [    2.803687] usbcore: registered new interface driver cdc_ether
      [    2.809483] usbcore: registered new interface driver net1080
      [    2.815108] usbcore: registered new interface driver cdc_subset
      [    2.820988] usbcore: registered new interface driver zaurus
      [    2.826537] usbcore: registered new interface driver cdc_ncm
      [    2.832918] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    2.838619] ehci-pci: EHCI PCI platform driver
      [    2.843395] usbcore: registered new interface driver uas
      [    2.848335] usbcore: registered new interface driver usb-storage
      [    2.854325] usbcore: registered new interface driver usbserial_generic
      [    2.860778] usbserial: USB Serial support registered for generic
      [    2.866747] usbcore: registered new interface driver ftdi_sio
      [    2.872448] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    2.879721] usbcore: registered new interface driver upd78f0730
      [    2.885595] usbserial: USB Serial support registered for upd78f0730
      [    2.893221] rtc_zynqmp ffa60000.rtc: registered as rtc0
      [    2.897019] rtc_zynqmp ffa60000.rtc: setting system clock to 2022-12-21T08:48:43 UTC (1671612523)
      [    2.905879] i2c /dev entries driver
      [    2.911091] usbcore: registered new interface driver uvcvideo
      [    2.914995] USB Video Class driver (1.1.1)
      [    2.920523] Bluetooth: HCI UART driver ver 2.3
      [    2.923474] Bluetooth: HCI UART protocol H4 registered
      [    2.928574] Bluetooth: HCI UART protocol BCSP registered
      [    2.933866] Bluetooth: HCI UART protocol LL registered
      [    2.938955] Bluetooth: HCI UART protocol ATH3K registered
      [    2.944331] Bluetooth: HCI UART protocol Three-wire (H5) registered
      [    2.950582] Bluetooth: HCI UART protocol Intel registered
      [    2.955921] Bluetooth: HCI UART protocol QCA registered
      [    2.961122] usbcore: registered new interface driver bcm203x
      [    2.966743] usbcore: registered new interface driver bpa10x
      [    2.972283] usbcore: registered new interface driver bfusb
      [    2.977729] usbcore: registered new interface driver btusb
      [    2.983190] usbcore: registered new interface driver ath3k
      [    2.988677] EDAC MC: ECC not enabled
      [    2.992297] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
      [    3.004608] sdhci: Secure Digital Host Controller Interface driver
      [    3.010409] sdhci: Copyright(c) Pierre Ossman
      [    3.014729] sdhci-pltfm: SDHCI platform and OF driver helper
      [    3.020759] ledtrig-cpu: registered to indicate activity on CPUs
      [    3.026331] SMCCC: SOC_ID: ARCH_SOC_ID not implemented, skipping ....
      [    3.032758] zynqmp_firmware_probe Platform Management API v1.1
      [    3.038519] zynqmp_firmware_probe Trustzone version v1.0
      [    3.073689] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
      [    3.118900] zynqmp-aes firmware:zynqmp-firmware:zynqmp-aes: will run requests pump with realtime priority
      [    3.134934] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
      [    3.135643] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
      [    3.141159] usbcore: registered new interface driver usbhid
      [    3.146548] usbhid: USB HID core driver
      [    3.157479] axi_adxcvr 84a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.05.a) using QPLL on GTH4 at 0x84A60000. Number of lanes: 4.
      [    3.163612] axi-jesd204-rx 84aa0000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x84AA0000. Encoder 8b10b, width 4/4, lanes 4.
      [    3.175182] axi_sysid 85000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    3.182241] axi_sysid 85000000.axi-sysid-0: [ad9695_fmc] [sys rom custom string placeholder] on [zcu102] git branch <hdl_2021_r1> git <6a6c5acc8ec422c068c7787cdeb5b0ee4ae1aa51> clean [2022-05-20 22:58:48] UTC
      [    3.201038] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
      [    3.207377] usbcore: registered new interface driver snd-usb-audio
      [    3.214767] pktgen: Packet Generator for packet performance testing. Version: 2.75
      [    3.221046] Initializing XFRM netlink socket
      [    3.224874] NET: Registered protocol family 10
      [    3.229592] Segment Routing with IPv6
      [    3.232981] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    3.239043] NET: Registered protocol family 17
      [    3.243143] NET: Registered protocol family 15
      [    3.247639] can: controller area network core
      [    3.251897] NET: Registered protocol family 29
      [    3.256286] can: raw protocol
      [    3.259222] can: broadcast manager protocol
      [    3.263377] can: netlink gateway - max_hops=1
      [    3.267777] Bluetooth: RFCOMM TTY layer initialized
      [    3.272551] Bluetooth: RFCOMM socket layer initialized
      [    3.277662] Bluetooth: RFCOMM ver 1.11
      [    3.281369] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
      [    3.286641] Bluetooth: BNEP filters: protocol multicast
      [    3.291834] Bluetooth: BNEP socket layer initialized
      [    3.296765] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
      [    3.302646] Bluetooth: HIDP socket layer initialized
      [    3.307698] 9pnet: Installing 9P2000 support
      [    3.311824] NET: Registered protocol family 36
      [    3.316239] Key type dns_resolver registered
      [    3.320670] registered taskstats version 1
      [    3.324536] Loading compiled-in X.509 certificates
      [    3.329655] Btrfs loaded, crc32c=crc32c-generic
      [    3.342459] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 48, base_baud = 6249999) is a xuartps
      [    3.351484] printk: console [ttyPS0] enabled
      [    3.355781] printk: bootconsole [cdns0] disabled
      [    3.365408] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 49, base_baud = 6249999) is a xuartps
      [    3.378627] of-fpga-region fpga-full: FPGA Region probed
      [    3.385578] nwl-pcie fd0e0000.pcie: host bridge /axi/pcie@fd0e0000 ranges:
      [    3.392472] nwl-pcie fd0e0000.pcie:      MEM 0x00e0000000..0x00efffffff -> 0x00e0000000
      [    3.400480] nwl-pcie fd0e0000.pcie:      MEM 0x0600000000..0x07ffffffff -> 0x0600000000
      [    3.408547] nwl-pcie fd0e0000.pcie: Link is DOWN
      [    3.413305] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
      [    3.419482] pci_bus 0000:00: root bus resource [bus 00-ff]
      [    3.424962] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
      [    3.431828] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
      [    3.439332] pci 0000:00:00.0: [10ee:d021] type 01 class 0x060400
      [    3.445393] pci 0000:00:00.0: PME# supported from D0 D1 D2 D3hot
      [    3.455674] pci 0000:00:00.0: PCI bridge to [bus 01-0c]
      [    3.461466] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
      [    3.468640] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
      [    3.475807] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
      [    3.482979] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
      [    3.490143] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
      [    3.497314] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
      [    3.504497] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
      [    3.511659] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
      [    3.519039] xilinx-zynqmp-dpdma fd4c0000.dma-controller: Xilinx DPDMA engine is probed
      [    3.527580] ahci-ceva fd0c0000.ahci: supply ahci not found, using dummy regulator
      [    3.535128] ahci-ceva fd0c0000.ahci: supply phy not found, using dummy regulator
      [    3.560096] ad9208 spi1.0: ad9695 PLL LOCKED
      [    3.572922] ad9208 spi1.0: ad9695 Rev. 2 Grade 0 (API 1.0.1) probed
      [    3.579859] spi-nor spi0.0: SPI-NOR-UniqueID 2ab990001501002a00e62e735a86
      [    3.586644] spi-nor spi0.0: found mt25qu512a, expected m25p80
      [    3.593032] spi-nor spi0.0: trying to lock already unlocked area
      [    3.599037] spi-nor spi0.0: mt25qu512a (131072 Kbytes)
      [    3.604194] 4 fixed-partitions partitions found on MTD device spi0.0
      [    3.610541] Creating 4 MTD partitions on "spi0.0":
      [    3.615325] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
      [    3.621855] 0x000000100000-0x000000600000 : "qspi-linux"
      [    3.627826] 0x000000600000-0x000000620000 : "qspi-device-tree"
      [    3.634381] 0x000000620000-0x000000c00000 : "qspi-rootfs"
      [    3.642891] macb ff0e0000.ethernet: Not enabling partial store and forward
      [    3.650402] libphy: MACB_mii_bus: probed
      [    3.655048] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 30 (00:0a:35:04:c2:ab)
      [    3.665264] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
      [    3.671830] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
      [    3.678350] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
      [    3.684886] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
      [    3.694907] pca953x 0-0020: supply vcc not found, using dummy regulator
      [    3.701587] pca953x 0-0020: using no AI
      [    3.706072] gpio-496 (sel0): hogged as output/low
      [    3.710970] gpio-497 (sel1): hogged as output/high
      [    3.715956] gpio-498 (sel2): hogged as output/high
      [    3.720946] gpio-499 (sel3): hogged as output/high
      [    3.726128] pca953x 0-0021: supply vcc not found, using dummy regulator
      [    3.732806] pca953x 0-0021: using no AI
      [    3.738591] ina2xx 2-0040: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.745618] ina2xx 2-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.752640] ina2xx 2-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.759666] ina2xx 2-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.766694] ina2xx 2-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.773712] ina2xx 2-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.780746] ina2xx 2-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.787772] ina2xx 2-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.794848] ina2xx 2-004a: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.801880] ina2xx 2-004b: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.808283] i2c i2c-0: Added multiplexed i2c bus 2
      [    3.813870] ina2xx 3-0040: power monitor ina226 (Rshunt = 2000 uOhm)
      [    3.820899] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.827919] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.834951] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.841981] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.849006] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.856034] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.863062] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    3.869466] i2c i2c-0: Added multiplexed i2c bus 3
      [    3.877760] random: fast init done
      [    3.928546] i2c i2c-0: Added multiplexed i2c bus 4
      [    3.933563] i2c i2c-0: Added multiplexed i2c bus 5
      [    3.938356] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
      [    3.945707] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 32
      [    3.953499] at24 6-0054: supply vcc not found, using dummy regulator
      [    3.960389] at24 6-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
      [    3.967136] i2c i2c-1: Added multiplexed i2c bus 6
      [    3.973584] si5341 7-0036: Chip: 5341 Grade: 1 Rev: 1
      [    4.011343] i2c i2c-1: Added multiplexed i2c bus 7
      [    4.019000] si570 8-005d: registered, current frequency 300000000 Hz
      [    4.025403] i2c i2c-1: Added multiplexed i2c bus 8
      [    4.045178] si570 9-005d: registered, current frequency 148500000 Hz
      [    4.051581] i2c i2c-1: Added multiplexed i2c bus 9
      [    4.056626] si5324 10-0069: si5328 probed
      [    4.125126] si5324 10-0069: si5328 probe successful
      [    4.130051] i2c i2c-1: Added multiplexed i2c bus 10
      [    4.135082] i2c i2c-1: Added multiplexed i2c bus 11
      [    4.140105] i2c i2c-1: Added multiplexed i2c bus 12
      [    4.145131] i2c i2c-1: Added multiplexed i2c bus 13
      [    4.150008] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
      [    4.158120] at24 14-0050: supply vcc not found, using dummy regulator
      [    4.190934] i2c i2c-1: Added multiplexed i2c bus 14
      [    4.195973] i2c i2c-1: Added multiplexed i2c bus 15
      [    4.201015] i2c i2c-1: Added multiplexed i2c bus 16
      [    4.206049] i2c i2c-1: Added multiplexed i2c bus 17
      [    4.211100] i2c i2c-1: Added multiplexed i2c bus 18
      [    4.216132] i2c i2c-1: Added multiplexed i2c bus 19
      [    4.221169] i2c i2c-1: Added multiplexed i2c bus 20
      [    4.226203] i2c i2c-1: Added multiplexed i2c bus 21
      [    4.231079] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
      [    4.238688] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 33
      [    4.248434] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
      [    4.277237] cf_axi_adc 84a00000.axi-ad9695-hpc: ADI AIM (10.01.b) at 0x84A00000 mapped to 0x(____ptrval____), probed ADC AD9208 as MASTER
      [    4.289647] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
      [    4.297714] zynqmp-display fd4a0000.display: vtc bridge property not present
      [    4.305878] zynqmp_clk_divider_set_rate() set divider failed for spi1_ref_div1, ret = -13
      [    4.315717] xilinx-dp-snd-codec fd4a0000.display:zynqmp_dp_snd_codec0: Failed to get required clock freq
      [    4.325215] xilinx-dp-snd-codec: probe of fd4a0000.display:zynqmp_dp_snd_codec0 failed with error -22
      [    4.334767] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
      [    4.341090] mmc0: new high speed SDHC card at address aaaa
      [    4.342930] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
      [    4.348426] mmcblk0: mmc0:aaaa SC32G 29.7 GiB 
      [    4.356263] OF: graph: no port node found in /axi/display@fd4a0000
      [    4.364327]  mmcblk0: p1 p2 p3
      [    4.366714] xlnx-drm xlnx-drm.0: bound fd4a0000.display (ops 0xffffffc010ffd810)
      [    5.456792] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
      [    5.464416] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.display on minor 0
      [    5.471906] zynqmp-display fd4a0000.display: ZynqMP DisplayPort Subsystem driver probed
      [    5.480258] ahci-ceva fd0c0000.ahci: supply ahci not found, using dummy regulator
      [    5.487794] ahci-ceva fd0c0000.ahci: supply phy not found, using dummy regulator
      [    5.495253] ahci-ceva fd0c0000.ahci: supply target not found, using dummy regulator
      [    5.503090] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
      [    5.512046] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst 
      [    5.522740] scsi host0: ahci-ceva
      [    5.526342] scsi host1: ahci-ceva
      [    5.529770] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 45
      [    5.537685] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 45
      [    5.546510] xhci-hcd xhci-hcd.1.auto: xHCI Host Controller
      [    5.552005] xhci-hcd xhci-hcd.1.auto: new USB bus registered, assigned bus number 1
      [    5.559754] xhci-hcd xhci-hcd.1.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000002010810
      [    5.569179] xhci-hcd xhci-hcd.1.auto: irq 58, io mem 0xfe200000
      [    5.575321] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
      [    5.583586] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    5.590807] usb usb1: Product: xHCI Host Controller
      [    5.595675] usb usb1: Manufacturer: Linux 5.10.0-98248-g1bbe32fa5182 xhci-hcd
      [    5.602800] usb usb1: SerialNumber: xhci-hcd.1.auto
      [    5.607963] hub 1-0:1.0: USB hub found
      [    5.611733] hub 1-0:1.0: 1 port detected
      [    5.615834] xhci-hcd xhci-hcd.1.auto: xHCI Host Controller
      [    5.621325] xhci-hcd xhci-hcd.1.auto: new USB bus registered, assigned bus number 2
      [    5.628980] xhci-hcd xhci-hcd.1.auto: Host supports USB 3.0 SuperSpeed
      [    5.635601] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.10
      [    5.643860] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    5.651080] usb usb2: Product: xHCI Host Controller
      [    5.655948] usb usb2: Manufacturer: Linux 5.10.0-98248-g1bbe32fa5182 xhci-hcd
      [    5.663074] usb usb2: SerialNumber: xhci-hcd.1.auto
      [    5.668187] hub 2-0:1.0: USB hub found
      [    5.671945] hub 2-0:1.0: 1 port detected
      [    5.685598] input: gpio-keys as /devices/platform/gpio-keys/input/input0
      [    5.692599] of_cfs_init
      [    5.695065] of_cfs_init: OK
      [    5.698028] cfg80211: Loading compiled-in X.509 certificates for regulatory database
      [    5.835909] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
      [    5.842443] clk: Not disabling unused clocks
      [    5.846980] ALSA device list:
      [    5.849937]   No soundcards found.
      [    5.853607] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
      [    5.862217] cfg80211: failed to load regulatory.db
      [    5.862241] ata1: SATA link down (SStatus 0 SControl 330)
      [    5.872413] ata2: SATA link down (SStatus 0 SControl 330)
      [    5.880417] EXT4-fs (mmcblk0p2): Unrecognized mount option "\xfeǉ\xdc/\x8cG<\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff" or missing value
      [    5.893194] EXT4-fs (mmcblk0p2): failed to parse options in superblock: \xfeǉ\xdc/\x8cG<\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff
      [    5.915034] EXT4-fs (mmcblk0p2): warning: mounting fs with errors, running e2fsck is recommended
      [    5.927801] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: \xfeǉ\xdc/\x8cG<\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff; (null)
      [    5.941651] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    5.957234] devtmpfs: mounted
      [    5.961035] Freeing unused kernel memory: 2496K
      [    5.965646] Run /sbin/init as init process
      [    5.969737]   with arguments:
      [    5.969739]     /sbin/init
      [    5.969741]   with environment:
      [    5.969744]     HOME=/
      [    5.969746]     TERM=linux
      [    6.495814] systemd[1]: systemd 247.3-7+rpi1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [    6.519063] systemd[1]: Detected architecture arm64.
      [    6.544806] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
      [    6.563449] systemd[1]: Set hostname to <analog>.
      [    7.808367] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [    8.015724] systemd[1]: Queued start job for default target Graphical Interface.
      [    8.024310] random: systemd: uninitialized urandom read (16 bytes read)
      [    8.031110] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    8.043463] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [    8.052488] systemd[1]: Created slice system-getty.slice.
      [    8.072897] random: systemd: uninitialized urandom read (16 bytes read)
      [    8.079885] systemd[1]: Created slice system-modprobe.slice.
      [    8.100884] random: systemd: uninitialized urandom read (16 bytes read)
      [    8.107824] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [    8.129185] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [    8.153077] systemd[1]: Created slice User and Session Slice.
      [    8.173117] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [    8.197113] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [    8.209568] systemd[1]: Reached target Slices.
      [    8.224963] systemd[1]: Reached target Swap.
      [    8.241662] systemd[1]: Listening on Syslog Socket.
      [    8.257180] systemd[1]: Listening on fsck to fsckd communication Socket.
      [    8.281033] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [    8.305514] systemd[1]: Listening on Journal Audit Socket.
      [    8.325187] systemd[1]: Listening on Journal Socket (/dev/log).
      [    8.349233] systemd[1]: Listening on Journal Socket.
      [    8.373927] systemd[1]: Listening on udev Control Socket.
      [    8.397183] systemd[1]: Listening on udev Kernel Socket.
      [    8.418774] systemd[1]: Mounting Huge Pages File System...
      [    8.434551] systemd[1]: Mounting POSIX Message Queue File System...
      [    8.458420] systemd[1]: Mounting RPC Pipe File System...
      [    8.474687] systemd[1]: Mounting Kernel Debug File System...
      [    8.489300] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
      [    8.497955] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [    8.512195] systemd[1]: Starting Restore / save the current clock...
      [    8.535658] systemd[1]: Starting Set the console keyboard layout...
      [    8.557628] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [    8.571135] systemd[1]: Starting Load Kernel Module configfs...
      [    8.591025] systemd[1]: Starting Load Kernel Module drm...
      [    8.610961] systemd[1]: Starting Load Kernel Module fuse...
      [    8.633243] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [    8.642540] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [    8.653528] systemd[1]: Starting Journal Service...
      [    8.674465] systemd[1]: Starting Load Kernel Modules...
      [    8.690880] systemd[1]: Starting Remount Root and Kernel File Systems...
      [    8.714824] systemd[1]: Starting Coldplug All udev Devices...
      [    8.739921] systemd[1]: Mounted Huge Pages File System.
      [    8.761402] systemd[1]: Mounted POSIX Message Queue File System.
      [    8.793352] systemd[1]: Mounted RPC Pipe File System.
      [    8.809340] systemd[1]: Mounted Kernel Debug File System.
      [    8.829841] systemd[1]: Finished Restore / save the current clock.
      [    8.853906] systemd[1]: Finished Set the console keyboard layout.
      [    8.881979] systemd[1]: modprobe@configfs.service: Succeeded.
      [    8.888226] systemd[1]: Finished Load Kernel Module configfs.
      [    8.910015] systemd[1]: modprobe@drm.service: Succeeded.
      [    8.915881] systemd[1]: Finished Load Kernel Module drm.
      [    8.937650] systemd[1]: Started Journal Service.
      [    9.021839] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
      [    9.165974] systemd-journald[174]: Received client request to flush runtime journal.
      [   10.668817] random: crng init done


   .. raw:: html

      </details>

.. raw:: html

   </details>


Make sure all devices are present
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# iio_info | grep iio:device
          iio:device0: ams
          iio:device1: axi-ad9695-hpc (buffer capable)
      root@analog:~# iio_info | grep hwmon
          hwmon0: ina226
          hwmon1: ina226
          hwmon10: ina226
          hwmon11: ina226
          hwmon12: ina226
          hwmon13: ina226
          hwmon14: ina226
          hwmon15: ina226
          hwmon16: ina226
          hwmon17: ina226
          hwmon18: max20751
          hwmon19: max20751
          hwmon2: ina226
          hwmon3: ina226
          hwmon4: ina226
          hwmon5: ina226
          hwmon6: ina226
          hwmon7: ina226
          hwmon8: ina226
          hwmon9: ina226
   


More Information
~~~~~~~~~~~~~~~~

-  :doc:`EVALUATING THE AD9695/AD9697 ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/eval/ad9695-1300ebz>`
-  :doc:`AD-SYNCHRONA14-EBZ </wiki-migration/resources/eval/user-guides/ad-synchrona14-ebz>`
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.
