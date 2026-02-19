.. _ad-jupiter-ebz quickstart:

Jupiter SDR Quick Start Guide
=============================

.. figure:: jupitersdr_front_explained.png
   :align: center

This guide provides some quick instructions on how to setup Jupiter SDR.

Required Software
-----------------

- SD Card 16GB image using the instructions here: :external+adi-kuiper-gen:doc:`Kuiper Linux image <index>`
- Instructions on how to build the ZynqMP / MPSoC Linux kernel and 
  devicetrees from source can be found here:

    - :ref:`linux-kernel zynqmp`
    - :external+hdl:ref:`build_boot_bin`
    
- When streaming data over USB3 interface is desired 
  :git-plutosdr-m2k-drivers-win:`USB driver <releases+>` need to be 
  installed on the host computer
- UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).
- :ref:`iio-oscilloscope`

Please use the :external+adi-kuiper-gen:doc:`release Image 2021_R2 or later <index>`

Hardware Setup
--------------

What's in the box
~~~~~~~~~~~~~~~~~

- Jupiter SDR
- 2 x USB Type-C cables
- 150mm RF loopback cable
- micro SD Card with pre-programmed image
- USB Type-C power supply (one USB Type-C cable is used to 
  supply the board)

Use case 1 - data streaming to a host computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Jupiter SDR
- Micro-USB cable
- USB Type-C cable (or Ethernet cable)
- USB Type-C Power Supply

Use case 2 - stand alone use
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Jupiter SDR
- Display Port compatible Monitor
- USB Type-C multiport hub, mouse and keyboard
- USB Type-C Power Supply

Testing
-------


- Insert SD card into the socket.
- Connect USB UART (Micro USB) to your host PC and connect your 
  terminal application to the corresponding port.
- Connect the Power Supply to USB Type-C power only connector - 
  after this the Status LED turns on red.
- Press Power Button to boot up - short time after button press 
  Status LED becomes purple (both red and blue LEDs are on)
- Observe kernel and serial console messages on your terminal.
- Optionally connect test and measurement equipment to SMA ports 
  or just connect the loopback cable included and use 
  IIO Osciloscope to control the :adi:`ADRV9002` settings.

.. note::
    
    This specifies any shell prompt running on the target

.. code-block::

    Xilinx Zynq MP First Stage Boot Loader
    Release 2022.2   Jun 27 2023  -  07:04:57
    NOTICE:  BL31: Non secure code at 0x8000000
    NOTICE:  BL31: v2.8(release):4683880e5
    NOTICE:  BL31: Built : 06:39:41, Jun 27 2023


    U-Boot 2022.01-40843-ga16a6a9cb3 (Jun 26 2023 - 15:37:16 +0300)

    CPU:   ZynqMP
    Silicon: v3
    Model: Analog Devices, Inc. Jupiter SDR
    Board: Xilinx ZynqMP
    DRAM:  2 GiB
    PMUFW:  v1.1
    PMUFW:  No permission to change config object
    EL Level:       EL2
    Chip ID:        zu3eg
    NAND:  0 MiB
    MMC:   mmc@ff170000: 0
    Loading Environment from FAT... *** Error - No Valid Environment Area found
    *** Warning - bad env area, using default environment

    In:    serial
    Out:   serial
    Err:   serial
    Bootmode: LVL_SHFT_SD_MODE1
    Reset reason:   EXTERNAL
    Net:   FEC: can't find phy-handle

    ZYNQ GEM: ff0e0000, mdio bus ff0e0000, phyaddr 15, interface rgmii-id

    Error: ethernet@ff0e0000 address not set.
    No ethernet found.

    scanning bus for devices...
    SATA link 0 timeout.
    SATA link 1 timeout.
    AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl SATA mode
    flags: 64bit ncq pm clo only pmp fbss pio slum part ccc apst
    starting USB...
    No working controllers found
    Hit any key to stop autoboot:  0
    switch to partitions #0, OK
    mmc0 is current device
    Scanning mmc 0:1...
    Found U-Boot script /boot.scr
    242 bytes read in 20 ms (11.7 KiB/s)
    ## Executing script at 20000000
    33378 bytes read in 29 ms (1.1 MiB/s)
    33384960 bytes read in 2251 ms (14.1 MiB/s)
    ## Flattened Device Tree blob at 00100000
         Booting using the fdt blob at 0x100000
    FEC: can't find phy-handle

    ZYNQ GEM: ff0e0000, mdio bus ff0e0000, phyaddr 15, interface rgmii-id

    Error: ethernet@ff0e0000 address not set.
    FEC: can't find phy-handle

    ZYNQ GEM: ff0e0000, mdio bus ff0e0000, phyaddr 15, interface rgmii-id

    Error: ethernet@ff0e0000 address not set.
         Loading Device Tree to 000000007bdf8000, end 000000007be03261 ... OK

    Starting kernel ...

    [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
    [    0.000000] Linux version 5.15.0-175797-g9379dba5c06d (dragos@debian) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #6 SMP Fri Jun 23 12:59:00 EEST 2023
    [    0.000000] Machine model: Analog Devices, Inc. Jupiter SDR
    [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff010000 (options '115200n8')
    [    0.000000] printk: bootconsole [cdns0] enabled
    [    0.000000] efi: UEFI not found.
    [    0.000000] Zone ranges:
    [    0.000000]   DMA      [mem 0x0000000000000000-0x000000007fffffff]
    [    0.000000]   DMA32    empty
    [    0.000000]   Normal   empty
    [    0.000000] Movable zone start for each node
    [    0.000000] Early memory node ranges
    [    0.000000]   node   0: [mem 0x0000000000000000-0x000000007fffffff]
    [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000007fffffff]
    [    0.000000] cma: Reserved 256 MiB at 0x000000006bc00000
    [    0.000000] psci: probing for conduit method from DT.
    [    0.000000] psci: PSCIv1.1 detected in firmware.
    [    0.000000] psci: Using standard PSCI v0.2 function IDs
    [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
    [    0.000000] psci: SMC Calling Convention v1.2
    [    0.000000] percpu: Embedded 18 pages/cpu s34008 r8192 d31528 u73728
    [    0.000000] Detected VIPT I-cache on CPU0
    [    0.000000] CPU features: detected: ARM erratum 845719
    [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 517120
    [    0.000000] Kernel command line: earlycon clk_ignore_unused root=/dev/mmcblk0p2 rw rootwait
    [    0.000000] Dentry cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
    [    0.000000] Inode-cache hash table entries: 131072 (order: 8, 1048576 bytes, linear)
    [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
    [    0.000000] Memory: 1765380K/2097152K available (16000K kernel code, 1690K rwdata, 12252K rodata, 2560K init, 615K bss, 69628K reserved, 262144K cma-reserved)
    [    0.000000] rcu: Hierarchical RCU implementation.
    [    0.000000] rcu:     RCU event tracing is enabled.
    [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
    [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
    [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
    [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
    [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
    [    0.000000] Root IRQ handler: gic_handle_irq
    [    0.000000] GIC: Using split EOI/Deactivate mode
    [    0.000000] random: get_random_bytes called from start_kernel+0x470/0x6fc with crng_init=0
    [    0.000000] arch_timer: cp15 timer(s) running at 33.33MHz (phys).
    [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x7b0074340, max_idle_ns: 440795202884 ns
    [    0.000000] sched_clock: 56 bits at 33MHz, resolution 30ns, wraps every 2199023255543ns
    [    0.008302] Console: colour dummy device 80x25
    [    0.012374] printk: console [tty0] enabled
    [    0.016436] printk: bootconsole [cdns0] disabled
    [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
    [    0.000000] Linux version 5.15.0-175797-g9379dba5c06d (dragos@debian) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #6 SMP Fri Jun 23 12:59:00 EEST 2023
    [    0.000000] Machine model: Analog Devices, Inc. Jupiter SDR
    [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff010000 (options '115200n8')
    [    0.000000] printk: bootconsole [cdns0] enabled
    [    0.000000] efi: UEFI not found.
    [    0.000000] Zone ranges:
    [    0.000000]   DMA      [mem 0x0000000000000000-0x000000007fffffff]
    [    0.000000]   DMA32    empty
    [    0.000000]   Normal   empty
    [    0.000000] Movable zone start for each node
    [    0.000000] Early memory node ranges
    [    0.000000]   node   0: [mem 0x0000000000000000-0x000000007fffffff]
    [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000007fffffff]
    [    0.000000] cma: Reserved 256 MiB at 0x000000006bc00000
    [    0.000000] psci: probing for conduit method from DT.
    [    0.000000] psci: PSCIv1.1 detected in firmware.
    [    0.000000] psci: Using standard PSCI v0.2 function IDs
    [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
    [    0.000000] psci: SMC Calling Convention v1.2
    [    0.000000] percpu: Embedded 18 pages/cpu s34008 r8192 d31528 u73728
    [    0.000000] Detected VIPT I-cache on CPU0
    [    0.000000] CPU features: detected: ARM erratum 845719
    [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 517120
    [    0.000000] Kernel command line: earlycon clk_ignore_unused root=/dev/mmcblk0p2 rw rootwait
    [    0.000000] Dentry cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
    [    0.000000] Inode-cache hash table entries: 131072 (order: 8, 1048576 bytes, linear)
    [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
    [    0.000000] Memory: 1765380K/2097152K available (16000K kernel code, 1690K rwdata, 12252K rodata, 2560K init, 615K bss, 69628K reserved, 262144K cma-reserved)
    [    0.000000] rcu: Hierarchical RCU implementation.
    [    0.000000] rcu:     RCU event tracing is enabled.
    [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
    [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
    [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
    [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
    [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
    [    0.000000] Root IRQ handler: gic_handle_irq
    [    0.000000] GIC: Using split EOI/Deactivate mode
    [    0.000000] random: get_random_bytes called from start_kernel+0x470/0x6fc with crng_init=0
    [    0.000000] arch_timer: cp15 timer(s) running at 33.33MHz (phys).
    [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x7b0074340, max_idle_ns: 440795202884 ns
    [    0.000000] sched_clock: 56 bits at 33MHz, resolution 30ns, wraps every 2199023255543ns
    [    0.008302] Console: colour dummy device 80x25
    [    0.012374] printk: console [tty0] enabled
    [    0.016436] printk: bootconsole [cdns0] disabled
    [    0.021040] Calibrating delay loop (skipped), value calculated using timer frequency.. 66.66 BogoMIPS (lpj=133332)
    [    0.021057] pid_max: default: 32768 minimum: 301
    [    0.021183] Mount-cache hash table entries: 4096 (order: 3, 32768 bytes, linear)
    [    0.021203] Mountpoint-cache hash table entries: 4096 (order: 3, 32768 bytes, linear)
    [    0.022116] rcu: Hierarchical SRCU implementation.
    [    0.022306] EFI services will not be available.
    [    0.022442] smp: Bringing up secondary CPUs ...
    [    0.022805] Detected VIPT I-cache on CPU1
    [    0.022842] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
    [    0.023222] Detected VIPT I-cache on CPU2
    [    0.023246] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
    [    0.023598] Detected VIPT I-cache on CPU3
    [    0.023621] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
    [    0.023663] smp: Brought up 1 node, 4 CPUs
    [    0.023699] SMP: Total of 4 processors activated.
    [    0.023708] CPU features: detected: 32-bit EL0 Support
    [    0.023716] CPU features: detected: CRC32 instructions
    [    0.023757] CPU: All CPU(s) started at EL2
    [    0.023776] alternatives: patching kernel code
    [    0.024818] devtmpfs: initialized
    [    0.028759] Registered cp15_barrier emulation handler
    [    0.028776] Registered setend emulation handler
    [    0.028888] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
    [    0.028911] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
    [    0.037569] pinctrl core: initialized pinctrl subsystem
    [    0.038315] NET: Registered PF_NETLINK/PF_ROUTE protocol family
    [    0.039513] DMA: preallocated 256 KiB GFP_KERNEL pool for atomic allocations
    [    0.039662] DMA: preallocated 256 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
    [    0.039792] DMA: preallocated 256 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
    [    0.039846] audit: initializing netlink subsys (disabled)
    [    0.039937] audit: type=2000 audit(0.032:1): state=initialized audit_enabled=0 res=1
    [    0.040223] cpuidle: using governor menu
    [    0.040299] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
    [    0.040362] ASID allocator initialised with 65536 entries
    [    0.054625] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
    [    0.054646] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
    [    0.054657] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
    [    0.054668] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
    [    1.114544] DRBG: Continuing without Jitter RNG
    [    1.217848] raid6: neonx8   gen()  2133 MB/s
    [    1.285908] raid6: neonx8   xor()  1582 MB/s
    [    1.353965] raid6: neonx4   gen()  2184 MB/s
    [    1.422013] raid6: neonx4   xor()  1556 MB/s
    [    1.490086] raid6: neonx2   gen()  2071 MB/s
    [    1.558128] raid6: neonx2   xor()  1429 MB/s
    [    1.626187] raid6: neonx1   gen()  1769 MB/s
    [    1.694248] raid6: neonx1   xor()  1212 MB/s
    [    1.762293] raid6: int64x8  gen()  1437 MB/s
    [    1.830358] raid6: int64x8  xor()   771 MB/s
    [    1.898414] raid6: int64x4  gen()  1602 MB/s
    [    1.966471] raid6: int64x4  xor()   818 MB/s
    [    2.034540] raid6: int64x2  gen()  1398 MB/s
    [    2.102591] raid6: int64x2  xor()   749 MB/s
    [    2.170653] raid6: int64x1  gen()  1033 MB/s
    [    2.238705] raid6: int64x1  xor()   517 MB/s
    [    2.238715] raid6: using algorithm neonx4 gen() 2184 MB/s
    [    2.238724] raid6: .... xor() 1556 MB/s, rmw enabled
    [    2.238733] raid6: using neon recovery algorithm
    [    2.239067] iommu: Default domain type: Translated
    [    2.239078] iommu: DMA domain TLB invalidation policy: strict mode
    [    2.239294] SCSI subsystem initialized
    [    2.239462] usbcore: registered new interface driver usbfs
    [    2.239498] usbcore: registered new interface driver hub
    [    2.239527] usbcore: registered new device driver usb
    [    2.239654] mc: Linux media interface: v0.10
    [    2.239678] videodev: Linux video capture interface: v2.00
    [    2.239742] pps_core: LinuxPPS API ver. 1 registered
    [    2.239752] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
    [    2.239772] PTP clock support registered
    [    2.239805] EDAC MC: Ver: 3.0.0
    [    2.240099] zynqmp-ipi-mbox mailbox@ff990400: Registered ZynqMP IPI mbox with TX/RX channels.
    [    2.240421] jesd204: found 0 devices and 0 topologies
    [    2.240461] FPGA manager framework
    [    2.240589] Advanced Linux Sound Architecture Driver Initialized.
    [    2.241014] Bluetooth: Core ver 2.22
    [    2.241041] NET: Registered PF_BLUETOOTH protocol family
    [    2.241050] Bluetooth: HCI device and connection manager initialized
    [    2.241064] Bluetooth: HCI socket layer initialized
    [    2.241075] Bluetooth: L2CAP socket layer initialized
    [    2.241091] Bluetooth: SCO socket layer initialized
    [    2.241506] clocksource: Switched to clocksource arch_sys_counter
    [    2.241624] VFS: Disk quotas dquot_6.6.0
    [    2.241669] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
    [    2.245768] NET: Registered PF_INET protocol family
    [    2.245886] IP idents hash table entries: 32768 (order: 6, 262144 bytes, linear)
    [    2.246780] tcp_listen_portaddr_hash hash table entries: 1024 (order: 2, 16384 bytes, linear)
    [    2.246818] TCP established hash table entries: 16384 (order: 5, 131072 bytes, linear)
    [    2.246933] TCP bind hash table entries: 16384 (order: 6, 262144 bytes, linear)
    [    2.247145] TCP: Hash tables configured (established 16384 bind 16384)
    [    2.247225] UDP hash table entries: 1024 (order: 3, 32768 bytes, linear)
    [    2.247275] UDP-Lite hash table entries: 1024 (order: 3, 32768 bytes, linear)
    [    2.247406] NET: Registered PF_UNIX/PF_LOCAL protocol family
    [    2.247787] RPC: Registered named UNIX socket transport module.
    [    2.247799] RPC: Registered udp transport module.
    [    2.247808] RPC: Registered tcp transport module.
    [    2.247816] RPC: Registered tcp NFSv4.1 backchannel transport module.
    [    2.248419] PCI: CLS 0 bytes, default 64
    [    2.248814] armv8-pmu pmu: hw perfevents: no interrupt-affinity property, guessing.
    [    2.248987] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
    [    2.249729] Initialise system trusted keyrings
    [    2.249810] workingset: timestamp_bits=62 max_order=19 bucket_order=0
    [    2.250372] NFS: Registering the id_resolver key type
    [    2.250391] Key type id_resolver registered
    [    2.250401] Key type id_legacy registered
    [    2.250421] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
    [    2.250432] nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
    [    2.250458] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
    [    2.250637] fuse: init (API version 7.34)
    [    2.286700] NET: Registered PF_ALG protocol family
    [    2.286714] xor: measuring software checksum speed
    [    2.290896]    8regs           :  2363 MB/sec
    [    2.294427]    32regs          :  2799 MB/sec
    [    2.298740]    arm64_neon      :  2287 MB/sec
    [    2.298749] xor: using function: 32regs (2799 MB/sec)
    [    2.298762] Key type asymmetric registered
    [    2.298770] Asymmetric key parser 'x509' registered
    [    2.298812] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
    [    2.298826] io scheduler mq-deadline registered
    [    2.298835] io scheduler kyber registered
    [    2.324628] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
    [    2.326446] cacheinfo: Unable to detect cache hierarchy for CPU 0
    [    2.330645] brd: module loaded
    [    2.334122] loop: module loaded
    [    2.334341] Registered mathworks_ip class
    [    2.336103] libphy: Fixed MDIO Bus: probed
    [    2.337258] tun: Universal TUN/TAP device driver, 1.6
    [    2.337350] CAN device driver interface
    [    2.337928] usbcore: registered new interface driver asix
    [    2.337974] usbcore: registered new interface driver ax88179_178a
    [    2.338005] usbcore: registered new interface driver cdc_ether
    [    2.338033] usbcore: registered new interface driver net1080
    [    2.338061] usbcore: registered new interface driver cdc_subset
    [    2.338088] usbcore: registered new interface driver zaurus
    [    2.338125] usbcore: registered new interface driver cdc_ncm
    [    2.338566] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    [    2.338577] ehci-pci: EHCI PCI platform driver
    [    2.338893] usbcore: registered new interface driver uas
    [    2.338930] usbcore: registered new interface driver usb-storage
    [    2.338998] usbcore: registered new interface driver usbserial_generic
    [    2.339021] usbserial: USB Serial support registered for generic
    [    2.339047] usbcore: registered new interface driver ftdi_sio
    [    2.339068] usbserial: USB Serial support registered for FTDI USB Serial Device
    [    2.339095] usbcore: registered new interface driver upd78f0730
    [    2.339115] usbserial: USB Serial support registered for upd78f0730
    [    2.339928] i2c_dev: i2c /dev entries driver
    [    2.341249] usbcore: registered new interface driver uvcvideo
    [    2.342168] Bluetooth: HCI UART driver ver 2.3
    [    2.342180] Bluetooth: HCI UART protocol H4 registered
    [    2.342190] Bluetooth: HCI UART protocol BCSP registered
    [    2.342213] Bluetooth: HCI UART protocol LL registered
    [    2.342223] Bluetooth: HCI UART protocol ATH3K registered
    [    2.342244] Bluetooth: HCI UART protocol Three-wire (H5) registered
    [    2.342285] Bluetooth: HCI UART protocol Intel registered
    [    2.342307] Bluetooth: HCI UART protocol QCA registered
    [    2.342341] usbcore: registered new interface driver bcm203x
    [    2.342374] usbcore: registered new interface driver bpa10x
    [    2.342405] usbcore: registered new interface driver bfusb
    [    2.342436] usbcore: registered new interface driver btusb
    [    2.342480] usbcore: registered new interface driver ath3k
    [    2.342569] EDAC MC: ECC not enabled
    [    2.342710] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
    [    2.343077] sdhci: Secure Digital Host Controller Interface driver
    [    2.343088] sdhci: Copyright(c) Pierre Ossman
    [    2.343096] sdhci-pltfm: SDHCI platform and OF driver helper
    [    2.343390] ledtrig-cpu: registered to indicate activity on CPUs
    [    2.343546] SMCCC: SOC_ID: ID = jep106:0049:0000 Revision = 0x14710093
    [    2.343622] zynqmp_firmware_probe Platform Management API v1.1
    [    2.343636] zynqmp_firmware_probe Trustzone version v1.0
    [    2.373414] zynqmp-aes firmware:zynqmp-firmware:zynqmp-aes: will run requests pump with realtime priority
    [    2.385413] zynqmp-keccak-384 firmware:zynqmp-firmware:sha384: The zynqmp-sha-deprecated driver shall be deprecated in 2022.2 and removed in 2023.1 release
    [    2.385509] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
    [    2.385689] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
    [    2.385844] usbcore: registered new interface driver usbhid
    [    2.385856] usbhid: USB HID core driver
    [    2.391942] axi_sysid 85000000.axi-sysid-0: AXI System ID core version (1.01.a) found
    [    2.392138] axi_sysid 85000000.axi-sysid-0:     [jupiter] on     [sdr] git branch <dev_pluto_ng_revb> git <38d58dc604ac06fe2912b1420a2963b46dd28984> dirty     [2023-06-26 13:37:34] UTC
    [    2.392686] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
    [    2.393093] usbcore: registered new interface driver snd-usb-audio
    [    2.394630] pktgen: Packet Generator for packet performance testing. Version: 2.75
    [    2.395046] Initializing XFRM netlink socket
    [    2.395132] NET: Registered PF_INET6 protocol family
    [    2.395583] Segment Routing with IPv6
    [    2.395607] In-situ OAM (IOAM) with IPv6
    [    2.395662] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
    [    2.396003] NET: Registered PF_PACKET protocol family
    [    2.396023] NET: Registered PF_KEY protocol family
    [    2.396112] can: controller area network core
    [    2.396146] NET: Registered PF_CAN protocol family
    [    2.396156] can: raw protocol
    [    2.396166] can: broadcast manager protocol
    [    2.396177] can: netlink gateway - max_hops=1
    [    2.396251] Bluetooth: RFCOMM TTY layer initialized
    [    2.396266] Bluetooth: RFCOMM socket layer initialized
    [    2.396286] Bluetooth: RFCOMM ver 1.11
    [    2.396299] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
    [    2.396308] Bluetooth: BNEP filters: protocol multicast
    [    2.396319] Bluetooth: BNEP socket layer initialized
    [    2.396327] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
    [    2.396339] Bluetooth: HIDP socket layer initialized
    [    2.396454] 9pnet: Installing 9P2000 support
    [    2.396474] NET: Registered PF_IEEE802154 protocol family
    [    2.396498] Key type dns_resolver registered
    [    2.396686] registered taskstats version 1
    [    2.396697] Loading compiled-in X.509 certificates
    [    2.397183] Btrfs loaded, crc32c=crc32c-generic, zoned=no, fsverity=no
    [    2.405842]  domain0: domain0 request failed for node 33: -13
    [    2.405882] xuartps ff000000.serial: failed to add to PM domain domain0: -13
    [    2.405896] xuartps: probe of ff000000.serial failed with error -13
    [    2.406984] ff010000.serial: ttyPS0 at MMIO 0xff010000 (irq = 30, base_baud = 6249999) is a xuartps
    [    3.845140] printk: console     [ttyPS0] enabled
    [    3.849794] of-fpga-region fpga-full: FPGA Region probed
    [    3.855292] gpio-347 (usb-reset): hogged as output/high
    [    3.860522] gpio-413 (adrv9002-clksrc): hogged as output/high
    [    3.866275] gpio-478 (fan-en): hogged as output/high
    [    3.871246] gpio-479 (fan-ctl): hogged as output/low
    [    3.877645] xilinx-zynqmp-dpdma fd4c0000.dma-controller: Xilinx DPDMA engine is probed
    [    3.886533] zynqmp-display fd4a0000.display: vtc bridge property not present
    [    3.900973] zynqmp_clk_divider_set_rate() set divider failed for adma_ref_div1, ret = -13
    [    3.911337] xilinx-dp-snd-codec fd4a0000.display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
    [    3.921442] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
    [    3.929531] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
    [    3.938458] xilinx-dp-snd-card fd4a0000.display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
    [    3.948039] OF: graph: no port node found in /axi/display@fd4a0000
    [    3.954570] xlnx-drm xlnx-drm.0: bound fd4a0000.display (ops 0xffffffc0110729d0)
    [    5.041526] zynqmp-display fd4a0000.display:     [drm] Cannot find any crtc or sizes
    [    5.049170]     [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.display on minor 0
    [    5.056685] zynqmp-display fd4a0000.display: ZynqMP DisplayPort Subsystem driver probed
    [    5.064899] ahci-ceva fd0c0000.ahci: supply ahci not found, using dummy regulator
    [    5.072458] ahci-ceva fd0c0000.ahci: supply phy not found, using dummy regulator
    [    5.079928] ahci-ceva fd0c0000.ahci: supply target not found, using dummy regulator
    [    5.087778] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
    [    5.096744] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst
    [    5.107274] scsi host0: ahci-ceva
    [    5.110866] scsi host1: ahci-ceva
    [    5.114287] ata1: SATA max UDMA/133 mmio     [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 26
    [    5.122215] ata2: SATA max UDMA/133 mmio     [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 26
    [    5.131641] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
    [    5.138184] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
    [    5.144669] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
    [    5.151160] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
    [    5.181487] at24 0-0050: supply vcc not found, using dummy regulator
    [    5.185596] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
    [    5.193350] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
    [    5.201022] at24 0-0050: 2048 byte 24c16 EEPROM, writable, 16 bytes/write
    [    5.201116] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000002010090
    [    5.217223] xhci-hcd xhci-hcd.0.auto: irq 40, io mem 0xfe200000
    [    5.223251] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
    [    5.228754] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
    [    5.236436] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0 SuperSpeed
    [    5.243101] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
    [    5.251393] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    5.258635] usb usb1: Product: xHCI Host Controller
    [    5.263521] usb usb1: Manufacturer: Linux 5.15.0-175797-g9379dba5c06d xhci-hcd
    [    5.270753] usb usb1: SerialNumber: xhci-hcd.0.auto
    [    5.275960] hub 1-0:1.0: USB hub found
    [    5.279749] hub 1-0:1.0: 1 port detected
    [    5.283904] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
    [    5.292074] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
    [    5.300357] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    5.307594] usb usb2: Product: xHCI Host Controller
    [    5.312494] usb usb2: Manufacturer: Linux 5.15.0-175797-g9379dba5c06d xhci-hcd
    [    5.319721] usb usb2: SerialNumber: xhci-hcd.0.auto
    [    5.324875] hub 2-0:1.0: USB hub found
    [    5.328646] hub 2-0:1.0: 1 port detected
    [    5.396777] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 22
    [    5.403171] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
    [    5.440693] random: fast init done
    [    5.445064] ata1: SATA link down (SStatus 0 SControl 330)
    [    5.449552] mmc0: SDHCI controller on ff170000.mmc     [ff170000.mmc] using ADMA 64-bit
    [    5.450501] ata2: SATA link down (SStatus 0 SControl 330)
    [    5.550685] mmc0: new ultra high speed SDR104 SDHC card at address 5048
    [    5.557732] mmcblk0: mmc0:5048 SD32G 28.8 GiB
    [    5.564178]  mmcblk0: p1 p2 p3
    [    6.125532] zynqmp-display fd4a0000.display:     [drm] Cannot find any crtc or sizes
    [    6.477135] random: crng init done
    [   13.058846] adrv9002 spi0.0: adrv9002-phy Rev 12.0, Firmware 0.22.0.0,  Stream 0.7.9.0,  API version: 68.5.0 successfully initialized
    [   13.072050] cf_axi_adc 84a00000.axi-adrv9002-rx-lpc: ADI AIM (10.02.b) at 0x84A00000 mapped to 0x000000008edaa943 probed ADC ADRV9002 as MASTER
    [   13.105827] cf_axi_dds 84a0a000.axi-adrv9002-tx-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84A0A000 mapped to 0x00000000fbe94996, probed DDS ADRV9002
    [   13.137822] cf_axi_dds 84a0c000.axi-adrv9002-tx2-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84A0C000 mapped to 0x000000002101aee5, probed DDS ADRV9002
    [   13.153803] macb ff0e0000.ethernet: Not enabling partial store and forward
    [   13.161811] libphy: MACB_mii_bus: probed
    [   13.166237] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 20 (00:05:f7:80:74:3e)
    [   13.178792] input: gpio-keys-power as /devices/platform/gpio-keys-power/input/input0
    [   13.186908] of_cfs_init
    [   13.189367] of_cfs_init: OK
    [   13.192291] cfg80211: Loading compiled-in X.509 certificates for regulatory database
    [   13.326959] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
    [   13.333490] clk: Not disabling unused clocks
    [   13.338021] ALSA device list:
    [   13.340984]   #0: DisplayPort monitor
    [   13.344946] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
    [   13.353572] cfg80211: failed to load regulatory.db
    [   13.364112] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
    [   13.373893] VFS: Mounted root (ext4 filesystem) on device 179:2.
    [   13.383115] devtmpfs: mounted
    [   13.387102] Freeing unused kernel memory: 2560K
    [   13.405563] Run /sbin/init as init process
    [   13.617964] systemd[1]: System time before build time, advancing clock.
    [   13.637584] systemd[1]: systemd 247.3-7+rpi1+deb11u1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
    [   13.661587] systemd[1]: Detected architecture arm64.

    Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

    [   13.682526] systemd[1]: Set hostname to <analog>.
    [   14.436264] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
    [   14.636253] systemd[1]: Queued start job for default target Graphical Interface.
    [   14.645081] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
    [   14.657451] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
    [   14.666547] systemd[1]: Created slice system-getty.slice.
    [  OK  ] Created slice system-getty.slice.
    [   14.690008] systemd[1]: Created slice system-modprobe.slice.
    [  OK  ] Created slice system-modprobe.slice.
    [   14.709928] systemd[1]: Created slice system-serial\x2dgetty.slice.
    [  OK  ] Created slice system-serial\x2dgetty.slice.
    [   14.733910] systemd[1]: Created slice system-systemd\x2dfsck.slice.
    [  OK  ] Created slice system-systemd\x2dfsck.slice.
    [   14.757807] systemd[1]: Created slice User and Session Slice.
    [  OK  ] Created slice User and Session Slice.
    [   14.777865] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
    [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
    [   14.801843] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
    [   14.814148] systemd[1]: Reached target Slices.
    [  OK  ] Reached target Slices.
    [   14.829696] systemd[1]: Reached target Swap.
    [  OK  ] Reached target Swap.
    [   14.846351] systemd[1]: Listening on Syslog Socket.
    [  OK  ] Listening on Syslog Socket.
    [   14.861920] systemd[1]: Listening on fsck to fsckd communication Socket.
    [  OK  ] Listening on fsck to fsckd communication Socket.
    [   14.885747] systemd[1]: Listening on initctl Compatibility Named Pipe.
    [  OK  ] Listening on initctl Compatibility Named Pipe.
    [   14.910252] systemd[1]: Listening on Journal Audit Socket.
    [  OK  ] Listening on Journal Audit Socket.
    [   14.929933] systemd[1]: Listening on Journal Socket (/dev/log).
    [  OK  ] Listening on Journal Socket (/dev/log).
    [   14.953990] systemd[1]: Listening on Journal Socket.
    [  OK  ] Listening on Journal Socket.
    [   14.970994] systemd[1]: Listening on udev Control Socket.
    [  OK  ] Listening on udev Control Socket.
    [   14.993934] systemd[1]: Listening on udev Kernel Socket.
    [  OK  ] Listening on udev Kernel Socket.
    [   15.015596] systemd[1]: Mounting Huge Pages File System...
         Mounting Huge Pages File System...
    [   15.035385] systemd[1]: Mounting POSIX Message Queue File System...
         Mounting POSIX Message Queue File System...
    [   15.059209] systemd[1]: Mounting RPC Pipe File System...
         Mounting RPC Pipe File System...
    [   15.075541] systemd[1]: Mounting Kernel Debug File System...
         Mounting Kernel Debug File System...
    [   15.094063] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
    [   15.102800] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
    [   15.115549] systemd[1]: Starting Restore / save the current clock...
         Starting Restore / save the current clock...
    [   15.142746] systemd[1]: Starting Set the console keyboard layout...
         Starting Set the console keyboard layout...
    [   15.170869] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
    [   15.184556] systemd[1]: Starting Load Kernel Module configfs...
         Starting Load Kernel Module configfs...
    [   15.203983] systemd[1]: Starting Load Kernel Module drm...
         Starting Load Kernel Module drm...
    [   15.223826] systemd[1]: Starting Load Kernel Module fuse...
         Starting Load Kernel Module fuse...
    [   15.244489] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
    [   15.253802] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
    [   15.264835] systemd[1]: Starting Journal Service...
         Starting Journal Service...
    [   15.285903] systemd[1]: Starting Load Kernel Modules...
         Starting Load Kernel Modules...
    [   15.303738] systemd[1]: Starting Remount Root and Kernel File Systems...
         Starting Remount Root and Kernel File Systems...
    [   15.327623] systemd[1]: Starting Coldplug All udev Devices...
         Starting Coldplug All udev Devices...
    [   15.352792] systemd[1]: Mounted Huge Pages File System.
    [  OK  ] Mounted Huge Pages File System.
    [   15.386242] systemd[1]: Mounted POSIX Message Queue File System.
    [  OK  ] Mounted POSIX Message Queue File System.
    [   15.410207] systemd[1]: Started Journal Service.
    [  OK  ] Started Journal Service.
    [  OK  ] Mounted RPC Pipe File System.
    [  OK  ] Mounted Kernel Debug File System.
    [  OK  ] Finished Restore / save the current clock.
    [  OK  ] Finished Set the console keyboard layout.
    [  OK  ] Finished Load Kernel Module configfs[   15.493163] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null). Quota mode: none.
    .
    [  OK  ] Finished Load Kernel Module drm.
    [  OK  ] Finished Load Kernel Module fuse.
    [FAILED] Failed to start Load Kernel Modules.
    See 'systemctl status systemd-modules-load.service' for details.
    [  OK  ] Finished Remount Root and Kernel File Systems.
         Mounting FUSE Control File System...
         Mounting Kernel Configuration File System...
         Starting Flush Journal to Persistent Storage...
    [   15.660144] systemd-journald[184]: Received client request to flush runtime journal.
         Starting Load/Save Random Seed...
         Starting Apply Kernel Variables...
    [   15.686650] systemd-journald[184]: File /var/log/journal/ada1ca10884b40d5a842c3234f7b495f/system.journal corrupted or uncleanly shut down, renaming and replacing.
         Starting Create System Users...
    [  OK  ] Mounted FUSE Control File System.
    [  OK  ] Mounted Kernel Configuration File System.
    [  OK  ] Finished Load/Save Random Seed.
    [  OK  ] Finished Apply Kernel Variables.
    [  OK  ] Finished Create System Users.
         Starting Create Static Device Nodes in /dev...
    [  OK  ] Finished Coldplug All udev Devices.
         Starting Helper to synchronize boot up for ifupdown...
         Starting Wait for udev To …plete Device Initialization...
    [  OK  ] Finished Helper to synchronize boot up for ifupdown.
    [  OK  ] Finished Create Static Device Nodes in /dev.
    [  OK  ] Reached target Local File Systems (Pre).
         Starting Rule-based Manage…for Device Events and Files...
    [  OK  ] Finished Flush Journal to Persistent Storage.
    [  OK  ] Started Rule-based Manager for Device Events and Files.
         Starting Show Plymouth Boot Screen...
    [  OK  ] Started Show Plymouth Boot Screen.
    [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
    [  OK  ] Reached target Local Encrypted Volumes.
    [  OK  ] Found device /dev/ttyPS0.
    [  OK  ] Found device /dev/disk/by-partuuid/9785213e-01.
    [  OK  ] Found device /dev/ttyS0.
    [  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting File System Check…isk/by-partuuid/9785213e-01...
         Starting Load Kernel Modules...
    [FAILED] Failed to start Load Kernel Modules.
    See 'systemctl status systemd-modules-load.service' for details.
    [  OK  ] Finished Wait for udev To Complete Device Initialization.
    [  OK  ] Finished File System Check…/disk/by-partuuid/9785213e-01.
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
         Starting Analog Devices power up/down sequence...
         Starting Save/Restore Sound Card State...
         Starting Avahi mDNS/DNS-SD Stack...
    [  OK  ] Started Regular background program processing daemon.
    [  OK  ] Started D-Bus System Message Bus.
         Starting dphys-swapfile - …unt, and delete a swap file...
         Starting Remove Stale Onli…t4 Metadata Check Snapshots...
         Starting Creating IIOD Context Attributes......
         Starting Analog Devices Jupiter User LED...
         Starting Initialize hardware monitoring sensors...
         Starting Authorization Manager...
         Starting DHCP Client Daemon...
         Starting LSB: Switch to on…nless shift key is pressed)...
         Starting LSB: rng-tools (Debian variant)...
         Starting System Logging Service...
         Starting User Login Management...
         Starting triggerhappy global hotkey daemon...
         Starting Disk Manager...
         Starting WPA supplicant...
    [  OK  ] Finished Save/Restore Sound Card State.
    [  OK  ] Reached target Sound Card.
    [  OK  ] Started triggerhappy global hotkey daemon.
    [  OK  ] Finished Raise network interfaces.
    [  OK  ] Finished Initialize hardware monitoring sensors.
    [  OK  ] Started System Logging Service.
    [  OK  ] Started DHCP Client Daemon.
    [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
    [  OK  ] Started LSB: rng-tools (Debian variant).
    [  OK  ] Started Avahi mDNS/DNS-SD Stack.
    [  OK  ] Started User Login Management.
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
    [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
    [  OK  ] Started Internet superserver.
    [  OK  ] Started /etc/rc.local Compatibility.
    [  OK  ] Started Authorization Manager.
         Starting Modem Manager...
    [  OK  ] Finished Permit User Sessions.
         Starting Light Display Manager...
         Starting Hold until boot process finishes up...
    [  OK  ] Started HTTP based time synchronization tool.
    [  OK  ] Started OpenBSD Secure Shell server.
         Starting Manage, Install and Generate Color Profiles...
    [  OK  ] Finished Analog Devices power up/down sequence.
    [FAILED] Failed to start VNC Server for X11.

    Raspbian GNU/Linux 11 analog ttyPS0

    analog login: root (automatic login)

    Linux analog 5.15.0-175797-g9379dba5c06d #6 SMP Fri Jun 23 12:59:00 EEST 2023 aarch64

    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Thu Jun 29 14:36:16 BST 2023 on ttyPS0
    root@analog:~#

Make sure all devices are present
---------------------------------

.. note::
    
    This specifies any shell prompt running on the target

.. code-block::

 root@analog:~# iio_info | grep iio:device
         iio:device0: ams
         iio:device1: adrv9002-phy
         iio:device2: axi-adrv9002-rx-lpc (buffer capable)
         iio:device3: axi-adrv9002-rx2-lpc (buffer capable)
         iio:device4: axi-adrv9002-tx-lpc (buffer capable)
         iio:device5: axi-adrv9002-tx2-lpc (buffer capable)

RX gain control
---------------

The following commands enable the LNA on RX1A channel.

.. note::
    
    This specifies any shell prompt running on the target

.. code-block::

    root@analog:~# cd /sys/kernel/debug/iio/iio:device1
    root@analog:/sys/kernel/debug/iio/iio:device1# echo 1 > agpio4_direction
    root@analog:/sys/kernel/debug/iio/iio:device1# echo 1 > agpio4_value

RF Add-on power enable
----------------------

When RXB or TXB channels need to be used the RF Add-on board could be 
powered on with the following commands. Once the RF Add-on is powered 
up the TX amplifieres will be turned on.

.. note::
    
    This specifies any shell prompt running on the target

.. code-block::

    root@analog:/# cd /sys/class/gpio
    root@analog:/sys/class/gpio# echo 475 > export
    root@analog:/sys/class/gpio# cd gpio475
    root@analog:/sys/class/gpio/gpio475# echo out > direction
    root@analog:/sys/class/gpio/gpio475# echo 1 > value

TX channel selection
--------------------

The transceiver TX could be routed to the main board output 
connector (TXA) or to the RF Add-on board (TXB). The 
out_voltage0_port_select and out_voltage1_port_select 
attributes allows us to select the desired TX1 respective TX2 
outputs. Below is a command example showing how to configure 
TX1 channel to TX1B (RF Add-on output).

.. note::
    
    This specifies any shell prompt running on the target

.. code-block::

    root@analog:/# cd /sys/bus/iio/devices/iio:device1
    root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_port_select_available
    tx_a tx_b
    root@analog:/sys/bus/iio/devices/iio:device1# echo tx_b > out_voltage0_port_select

Video Configuration
-------------------

The default configuration for most of the projects is to use the HDMI 
output, but for this project the DisplayPort is used. In order for it
to work, you should follow the steps described here: 
:dokuwiki:`DisplayPort No Picture <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp#displayport_-_no_picture>`

After following the steps, the board should be rebooted.

Setup Networking
----------------

Follow :dokuwiki:`this article for further network config <resources/tools-software/linux-software/network-config>`