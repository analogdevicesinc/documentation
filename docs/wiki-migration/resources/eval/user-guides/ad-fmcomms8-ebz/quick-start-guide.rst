FMCOMMS8 Quick Start Guide
==========================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the FMCOMMS8 on ADRV9009-ZU11EG and ZCU102.

Instructions on how to build the ZynqMP / MPSoC Linux kernel and devicetrees from source can be found here:

-  :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`
-  :doc:`How to build the ZynqMP boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`

Required Software
-----------------

-  SD Card 16GB imaged using the instructions here: :doc:`Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

FMCOMMS8 Specific Boot Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After writing the image, on the boot partition FMCOMMS8 specific files can be added from:

-  `FMCOMMS8 with ADRV9009-ZU11EG HW Rev.B boot files (2019_R2 Relase) <https://swdownloads.analog.com/cse/boot_partition_files/2019_R2/latest_boot_partition.tar.xz>`_ - from folder zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-sync-fmcomms8

   -  `ADRV9009-ZU11EG HDL Project source files <https://wiki.analog.com/https/github.com/analogdevicesinc/hdl/tree/master/projects/adrv9009zu11eg/adrv2crr_fmcomms8>`_.
   -  `Linux source files <https://wiki.analog.com/https/github.com/analogdevicesinc/linux/tree/master>`_

-  `FMCOMMS8 with ZCU102 boot files (2019_R2 Relase) <https://swdownloads.analog.com/cse/boot_partition_files/2019_R2/latest_boot_partition.tar.xz>`_ - from folder zynqmp-zcu102-rev10-adrv9009-fmcomms8

   -  `ZCU102 HDL Project source files <https://wiki.analog.com/https/github.com/analogdevicesinc/hdl/tree/master/projects/fmcomms8/zcu102>`_
   -  `Linux source files <https://wiki.analog.com/https/github.com/analogdevicesinc/linux/tree/master>`_

Copy:

-  BOOT.BIN
-  Image (from folder zynqmp-common)
-  system.dtb

-> To the root directory of the SD-Card FAT32 BOOT partition.

Required Hardware
-----------------

-  ADRV9009-ZU11EG SoM board
-  ADRV2CRR-FMC carrier board
-  FMCOMMS8 evaluation board
-  Micro-USB cable
-  Ethernet cable
-  Power Supply

OR

-  ZCU102
-  FMCOMMS8 evaluation board
-  Micro-USB cable
-  Ethernet cable
-  Power Supply

Optional Hardware
-----------------

-  Reference clock source
-  USB Type-C multiport HUB
-  USB keyboard and mouse
-  DisplayPort compatible monitor

Testing
=======


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


Hardware Setup
--------------

ADRV9009-ZU11EG
~~~~~~~~~~~~~~~

-  Connect the ``ADRV9009-ZU11EG`` System on Module to the ``ADRV2CRR-FMC`` carrier board.
-  Connect the ``FMCOMMS8`` to the ``ADRV2CRR-FMC`` carrier board using the FMC HPC connector.
-  Connect the 12V Power Supply to ``P11``
-  Connect USB UART ``P8`` (Micro USB) to your host PC.
-  Connect fan to ``P9``
-  Insert SD card into socket ``P15``.
-  Configure ADRV2CRR-FMC for SD BOOT using ``S13``, ``S14``, ``S15``, ``S16``. See picture below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/ADRV2CRR Rev A and B Sw_Jmp settings.JPG
   :align: center
   :width: 800px

-  Configure ``ADRV2CRR-FMC`` for SD BOOT from carrier using ``S9``. See picture below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/adrv9009-zu11g-sd-card-select.png
   :align: center
   :width: 400px

-  Turn on the power switch on the carrier board using ``S12``.
-  Optionally connect test and measurement equipment to U.FL RF ports.
-  Observe kernel and serial console messages on your terminal. (use the first ttyUSB or COM port registered, Baud rate 115200 (8N1))

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
   
      Starting kernel ...
   
      [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
      [    0.000000] Linux version 4.19.0-14271-g4f88022 (michael@mhenneri-D06) (gcc version 8.2.0 (GCC)) #3201 SMP Fri Aug 28 12:05:21 CEST 2020
      [    0.000000] Machine model: Analog Devices ADRV9009-ZU11EG Rev.B
      [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff010000 (options '115200n8')
      [    0.000000] bootconsole [cdns0] enabled
      [    0.000000] efi: Getting EFI parameters from FDT:
      [    0.000000] efi: UEFI not found.
      [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
      [    0.000000] psci: probing for conduit method from DT.
      [    0.000000] psci: PSCIv1.1 detected in firmware.
      [    0.000000] psci: Using standard PSCI v0.2 function IDs
      [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
      [    0.000000] psci: SMC Calling Convention v1.1
      [    0.000000] random: get_random_bytes called from start_kernel+0x94/0x3f8 with crng_init=0
      [    0.000000] percpu: Embedded 22 pages/cpu @(____ptrval____) s52504 r8192 d29416 u90112
      [    0.000000] Detected VIPT I-cache on CPU0
      [    0.000000] CPU features: enabling workaround for ARM erratum 845719
      [    0.000000] Speculative Store Bypass Disable mitigation not required
      [    0.000000] CPU features: detected: Kernel page table isolation (KPTI)
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
      [    0.000000] Kernel command line: earlycon console=ttyPS0,115200 root=/dev/mmcblk0p2 rw rootfstype=ext4 rootwait
      [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
      [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
      [    0.000000] software IO TLB: mapped [mem 0x6bfff000-0x6ffff000] (64MB)
      [    0.000000] Memory: 3773200K/4194304K available (12540K kernel code, 1552K rwdata, 12976K rodata, 832K init, 326K bss, 158960K reserved, 262144K cma-reserved)
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
      [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
      [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
      [    0.000000] GIC: Using split EOI/Deactivate mode
      [    0.000000] arch_timer: cp15 timer(s) running at 33.33MHz (phys).
      [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x7b0074340, max_idle_ns: 440795202884 ns
      [    0.000003] sched_clock: 56 bits at 33MHz, resolution 30ns, wraps every 2199023255543ns
      [    0.008228] Console: colour dummy device 80x25
      [    0.012388] Calibrating delay loop (skipped), value calculated using timer frequency.. 66.66 BogoMIPS (lpj=133332)
      [    0.022667] pid_max: default: 32768 minimum: 301
      [    0.027349] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.033921] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.041634] ASID allocator initialised with 32768 entries
      [    0.046414] rcu: Hierarchical SRCU implementation.
      [    0.051414] EFI services will not be available.
      [    0.055724] smp: Bringing up secondary CPUs ...
      [    0.060372] Detected VIPT I-cache on CPU1
      [    0.060399] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [    0.060679] Detected VIPT I-cache on CPU2
      [    0.060696] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [    0.060959] Detected VIPT I-cache on CPU3
      [    0.060975] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [    0.061015] smp: Brought up 1 node, 4 CPUs
      [    0.095586] SMP: Total of 4 processors activated.
      [    0.100259] CPU features: detected: 32-bit EL0 Support
      [    0.106673] CPU: All CPU(s) started at EL2
      [    0.109437] alternatives: patching kernel code
      [    0.114672] devtmpfs: initialized
      [    0.125242] Registered cp15_barrier emulation handler
      [    0.125291] Registered setend emulation handler
      [    0.129257] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      [    0.138845] futex hash table entries: 1024 (order: 4, 65536 bytes)
      [    0.149972] xor: measuring software checksum speed
      [    0.189042]    8regs     :  2639.000 MB/sec
      [    0.229068]    8regs_prefetch:  2280.000 MB/sec
      [    0.269095]    32regs    :  3027.000 MB/sec
      [    0.309122]    32regs_prefetch:  2565.000 MB/sec
      [    0.309162] xor: using function: 32regs (3027.000 MB/sec)
      [    0.313470] pinctrl core: initialized pinctrl subsystem
      [    0.319202] NET: Registered protocol family 16
      [    0.323342] audit: initializing netlink subsys (disabled)
      [    0.328485] audit: type=2000 audit(0.272:1): state=initialized audit_enabled=0 res=1
      [    0.336148] cpuidle: using governor menu
      [    0.340159] vdso: 2 pages (1 code @ (____ptrval____), 1 data @ (____ptrval____))
      [    0.347376] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
      [    0.354735] DMA: preallocated 256 KiB pool for atomic allocations
      [    0.371607] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
      [    0.438777] raid6: int64x1  gen()   493 MB/s
      [    0.506819] raid6: int64x1  xor()   502 MB/s
      [    0.574924] raid6: int64x2  gen()   754 MB/s
      [    0.642903] raid6: int64x2  xor()   666 MB/s
      [    0.710946] raid6: int64x4  gen()  1089 MB/s
      [    0.778967] raid6: int64x4  xor()   819 MB/s
      [    0.847015] raid6: int64x8  gen()  1291 MB/s
      [    0.915059] raid6: int64x8  xor()   844 MB/s
      [    0.983151] raid6: neonx1   gen()   818 MB/s
      [    1.051148] raid6: neonx1   xor()   979 MB/s
      [    1.119206] raid6: neonx2   gen()  1255 MB/s
      [    1.187206] raid6: neonx2   xor()  1304 MB/s
      [    1.255263] raid6: neonx4   gen()  1643 MB/s
      [    1.323287] raid6: neonx4   xor()  1576 MB/s
      [    1.391347] raid6: neonx8   gen()  1725 MB/s
      [    1.459371] raid6: neonx8   xor()  1621 MB/s
      [    1.459409] raid6: using algorithm neonx8 gen() 1725 MB/s
      [    1.463364] raid6: .... xor() 1621 MB/s, rmw enabled
      [    1.468295] raid6: using neon recovery algorithm
      [    1.473740] SCSI subsystem initialized
      [    1.476751] usbcore: registered new interface driver usbfs
      [    1.482111] usbcore: registered new interface driver hub
      [    1.487364] usbcore: registered new device driver usb
      [    1.492396] media: Linux media interface: v0.10
      [    1.496858] videodev: Linux video capture interface: v2.00
      [    1.502335] pps_core: LinuxPPS API ver. 1 registered
      [    1.507221] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    1.516312] PTP clock support registered
      [    1.520209] EDAC MC: Ver: 3.0.0
      [    1.523650] zynqmp-ipi-mbox mailbox@ff990400: Probed ZynqMP IPI Mailbox driver.
      [    1.531079] jesd204: created con: id=0, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@84a30000 <-> /fpga-axi@0/axi-adrv9009-tx-hpc@84a04000
      [    1.542780] jesd204: created con: id=1, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@84a20000 <-> /fpga-axi@0/axi-jesd204-tx@84a30000
      [    1.554457] jesd204: created con: id=2, topo=0, link=0, /amba/spi@ff040000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-tx@84a20000
      [    1.565527] jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx-os@84a60000 <-> /fpga-axi@0/axi-jesd204-rx@84a70000
      [    1.577465] jesd204: created con: id=4, topo=0, link=2, /amba/spi@ff040000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-rx-os@84a60000
      [    1.588796] jesd204: created con: id=5, topo=0, link=1, /fpga-axi@0/axi-adxcvr-rx@84a40000 <-> /fpga-axi@0/axi-jesd204-rx@84a50000
      [    1.600474] jesd204: created con: id=6, topo=0, link=1, /amba/spi@ff040000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-rx@84a40000
      [    1.611550] jesd204: created con: id=7, topo=0, link=1, /amba/spi@ff040000/hmc7044-car@3 <-> /amba/spi@ff050000/hmc7044-fmc@2
      [    1.622790] jesd204: created con: id=8, topo=0, link=2, /amba/spi@ff040000/hmc7044-car@3 <-> /amba/spi@ff050000/hmc7044-fmc@2
      [    1.634037] jesd204: created con: id=9, topo=0, link=0, /amba/spi@ff040000/hmc7044-car@3 <-> /amba/spi@ff050000/hmc7044-fmc@2
      [    1.645296] jesd204: created con: id=10, topo=0, link=1, /fpga-axi@0/axi-jesd204-rx@84a50000 <-> /amba/spi@ff050000/adrv9009-phy-d@1
      [    1.657139] jesd204: created con: id=11, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@84a70000 <-> /amba/spi@ff050000/adrv9009-phy-d@1
      [    1.668989] jesd204: created con: id=12, topo=0, link=0, /fpga-axi@0/axi-adrv9009-tx-hpc@84a04000 <-> /amba/spi@ff050000/adrv9009-phy-d@1
      [    1.681309] jesd204: created con: id=13, topo=0, link=1, /amba/spi@ff050000/adrv9009-phy-d@1 <-> /amba/spi@ff050000/adrv9009-phy-c@0
      [    1.693136] jesd204: created con: id=14, topo=0, link=2, /amba/spi@ff050000/adrv9009-phy-d@1 <-> /amba/spi@ff050000/adrv9009-phy-c@0
      [    1.704994] jesd204: created con: id=15, topo=0, link=0, /amba/spi@ff050000/adrv9009-phy-d@1 <-> /amba/spi@ff050000/adrv9009-phy-c@0
      [    1.716824] jesd204: created con: id=16, topo=0, link=1, /amba/spi@ff050000/hmc7044-fmc@2 <-> /amba/spi@ff040000/hmc7044@0
      [    1.727803] jesd204: created con: id=17, topo=0, link=2, /amba/spi@ff050000/hmc7044-fmc@2 <-> /amba/spi@ff040000/hmc7044@0
      [    1.738789] jesd204: created con: id=18, topo=0, link=0, /amba/spi@ff050000/hmc7044-fmc@2 <-> /amba/spi@ff040000/hmc7044@0
      [    1.749820] jesd204: created con: id=19, topo=0, link=1, /amba/spi@ff050000/adrv9009-phy-c@0 <-> /amba/spi@ff040000/adrv9009-phy-b@0
      [    1.761645] jesd204: created con: id=20, topo=0, link=2, /amba/spi@ff050000/adrv9009-phy-c@0 <-> /amba/spi@ff040000/adrv9009-phy-b@0
      [    1.773502] jesd204: created con: id=21, topo=0, link=0, /amba/spi@ff050000/adrv9009-phy-c@0 <-> /amba/spi@ff040000/adrv9009-phy-b@0
      [    1.785369] jesd204: created con: id=22, topo=0, link=1, /amba/spi@ff040000/adrv9009-phy-b@0 <-> /amba/spi@ff040000/adrv9009-phy@0
      [    1.797024] jesd204: created con: id=23, topo=0, link=2, /amba/spi@ff040000/adrv9009-phy-b@0 <-> /amba/spi@ff040000/adrv9009-phy@0
      [    1.808709] jesd204: created con: id=24, topo=0, link=0, /amba/spi@ff040000/adrv9009-phy-b@0 <-> /amba/spi@ff040000/adrv9009-phy@0
      [    1.820416] jesd204: /amba/spi@ff040000/adrv9009-phy@0: JESD204 link[0] transition uninitialized -> initialized
      [    1.830389] jesd204: /amba/spi@ff040000/adrv9009-phy@0: JESD204 link[1] transition uninitialized -> initialized
      [    1.840422] jesd204: /amba/spi@ff040000/adrv9009-phy@0: JESD204 link[2] transition uninitialized -> initialized
      [    1.850455] jesd204: found 14 devices and 1 topologies
      [    1.855593] FPGA manager framework
      [    1.859099] Advanced Linux Sound Architecture Driver Initialized.
      [    1.865236] Bluetooth: Core ver 2.22
      [    1.868546] NET: Registered protocol family 31
      [    1.872947] Bluetooth: HCI device and connection manager initialized
      [    1.879262] Bluetooth: HCI socket layer initialized
      [    1.884105] Bluetooth: L2CAP socket layer initialized
      [    1.889132] Bluetooth: SCO socket layer initialized
      [    1.894331] clocksource: Switched to clocksource arch_sys_counter
      [    1.900094] VFS: Disk quotas dquot_6.6.0
      [    1.903948] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
      [    1.914855] NET: Registered protocol family 2
      [    1.915379] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes)
      [    1.922897] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
      [    1.930217] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
      [    1.936973] TCP: Hash tables configured (established 32768 bind 32768)
      [    1.943155] UDP hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.949130] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.955605] NET: Registered protocol family 1
      [    1.959994] RPC: Registered named UNIX socket transport module.
      [    1.965680] RPC: Registered udp transport module.
      [    1.970348] RPC: Registered tcp transport module.
      [    1.975016] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    1.982025] hw perfevents: no interrupt-affinity property for /pmu, guessing.
      [    1.988643] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
      [    1.996956] Initialise system trusted keyrings
      [    2.000675] workingset: timestamp_bits=62 max_order=20 bucket_order=0
      [    2.007639] NFS: Registering the id_resolver key type
      [    2.012050] Key type id_resolver registered
      [    2.016193] Key type id_legacy registered
      [    2.020175] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    2.026841] jffs2: version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.
      [    3.007338] NET: Registered protocol family 38
      [    3.061147] Key type asymmetric registered
      [    3.061184] Asymmetric key parser 'x509' registered
      [    3.064486] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
      [    3.071807] io scheduler noop registered
      [    3.075697] io scheduler deadline registered
      [    3.079954] io scheduler cfq registered (default)
      [    3.084608] io scheduler mq-deadline registered
      [    3.089105] io scheduler kyber registered
      [    3.118365] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      [    3.121939] cacheinfo: Unable to detect cache hierarchy for CPU 0
      [    3.129156] brd: module loaded
      [    3.132690] loop: module loaded
      [    3.132884] Registered mathworks_ip class
      [    3.135914] mtdoops: mtd device (mtddev=name/number) must be supplied
      [    3.142928] libphy: Fixed MDIO Bus: probed
      [    3.146824] tun: Universal TUN/TAP device driver, 1.6
      [    3.150842] CAN device driver interface
      [    3.155345] usbcore: registered new interface driver asix
      [    3.159945] usbcore: registered new interface driver ax88179_178a
      [    3.165983] usbcore: registered new interface driver cdc_ether
      [    3.171779] usbcore: registered new interface driver net1080
      [    3.177400] usbcore: registered new interface driver cdc_subset
      [    3.183282] usbcore: registered new interface driver zaurus
      [    3.188825] usbcore: registered new interface driver cdc_ncm
      [    3.195029] usbcore: registered new interface driver uas
      [    3.199728] usbcore: registered new interface driver usb-storage
      [    3.205717] usbcore: registered new interface driver upd78f0730
      [    3.211564] usbserial: USB Serial support registered for upd78f0730
      [    3.218209] i2c /dev entries driver
      [    3.222896] usbcore: registered new interface driver uvcvideo
      [    3.226945] USB Video Class driver (1.1.1)
      [    3.231465] axi_fan_control_driver 80000000.axi-fan-control: clk_get failed with -517
      [    3.239471] Bluetooth: HCI UART driver ver 2.3
      [    3.243215] Bluetooth: HCI UART protocol H4 registered
      [    3.248310] Bluetooth: HCI UART protocol BCSP registered
      [    3.253604] Bluetooth: HCI UART protocol LL registered
      [    3.258690] Bluetooth: HCI UART protocol ATH3K registered
      [    3.264068] Bluetooth: HCI UART protocol Three-wire (H5) registered
      [    3.270314] Bluetooth: HCI UART protocol Intel registered
      [    3.275670] Bluetooth: HCI UART protocol QCA registered
      [    3.280865] usbcore: registered new interface driver bcm203x
      [    3.286481] usbcore: registered new interface driver bpa10x
      [    3.292017] usbcore: registered new interface driver bfusb
      [    3.297468] usbcore: registered new interface driver btusb
      [    3.302892] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
      [    3.308553] usbcore: registered new interface driver ath3k
      [    3.314375] EDAC MC0: Giving out device to module 1 controller synps_ddr_controller: DEV synps_edac (INTERRUPT)
      [    3.324152] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
      [    3.336714] sdhci: Secure Digital Host Controller Interface driver
      [    3.342251] sdhci: Copyright(c) Pierre Ossman
      [    3.346574] sdhci-pltfm: SDHCI platform and OF driver helper
      [    3.352526] ledtrig-cpu: registered to indicate activity on CPUs
      [    3.358205] zynqmp_firmware_probe Platform Management API v1.1
      [    3.363967] zynqmp_firmware_probe Trustzone version v1.0
      [    3.371775] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
      [    3.398037] zynqmp_clk_mux_get_parent() getparent failed for clock: lpd_wdt, ret = -22
      [    3.400712] alg: No test for xilinx-zynqmp-aes (zynqmp-aes)
      [    3.405938] zynqmp_aes zynqmp_aes: AES Successfully Registered
      [    3.405938] 
      [    3.413356] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
      [    3.419561] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
      [    3.425099] usbcore: registered new interface driver usbhid
      [    3.430407] usbhid: USB HID core driver
      [    3.441340] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
      [    3.442604] usbcore: registered new interface driver snd-usb-audio
      [    3.449997] pktgen: Packet Generator for packet performance testing. Version: 2.75
      [    3.456160] Initializing XFRM netlink socket
      [    3.460112] NET: Registered protocol family 10
      [    3.464817] Segment Routing with IPv6
      [    3.468175] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    3.474282] NET: Registered protocol family 17
      [    3.478395] NET: Registered protocol family 15
      [    3.482808] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
      [    3.495881] can: controller area network core (rev 20170425 abi 9)
      [    3.501879] NET: Registered protocol family 29
      [    3.506241] can: raw protocol (rev 20170425)
      [    3.510478] can: broadcast manager protocol (rev 20170425 t)
      [    3.516102] can: netlink gateway (rev 20170425) max_hops=1
      [    3.521746] Bluetooth: RFCOMM TTY layer initialized
      [    3.526401] Bluetooth: RFCOMM socket layer initialized
      [    3.531511] Bluetooth: RFCOMM ver 1.11
      [    3.535220] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
      [    3.540493] Bluetooth: BNEP filters: protocol multicast
      [    3.545685] Bluetooth: BNEP socket layer initialized
      [    3.550615] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
      [    3.556497] Bluetooth: HIDP socket layer initialized
      [    3.561529] 9pnet: Installing 9P2000 support
      [    3.565673] NET: Registered protocol family 36
      [    3.570090] Key type dns_resolver registered
      [    3.574725] registered taskstats version 1
      [    3.578386] Loading compiled-in X.509 certificates
      [    3.583434] Btrfs loaded, crc32c=crc32c-generic
      [    3.593532] ff010000.serial: ttyPS0 at MMIO 0xff010000 (irq = 23, base_baud = 6249999) is a xuartps
      [    3.603348] console [ttyPS0] enabled
      [    3.603348] console [ttyPS0] enabled
      [    3.606948] bootconsole [cdns0] disabled
      [    3.606948] bootconsole [cdns0] disabled
      [    3.615272] GPIO line 13 (ulpi-phy-reset) hogged as output/high
      [    3.624522] of-fpga-region fpga-full: FPGA Region probed
      [    3.631312] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
      [    3.637998] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:8 protocol:4 pll_locked:yes
      [    3.647368] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Failed to get required clock freq
      [    3.657475] xilinx-dp-snd-codec: probe of fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0 failed with error -22
      [    3.667543] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
      [    3.675585] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
      [    3.683630] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: ASoC: CPU DAI (null) not registered
      [    3.693702] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
      [    3.700724] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
      [    3.707333] [drm] No driver support for vblank timestamp query.
      [    3.713300] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffff8008d82d70)
      [    4.798343] [drm] Cannot find any crtc or sizes
      [    4.803127] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
      [    4.811231] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
      [    4.821270] adrv9009 spi1.0: adrv9009_probe : enter
      [    4.826981] adrv9009 spi1.1: adrv9009_probe : enter
      [    4.879268] jesd204: /amba/spi@ff040000/hmc7044-car@3,jesd204:3,parent=spi1.3: Using as SYSREF provider
      [    4.938744] adrv9009 spi2.0: adrv9009_probe : enter
      [    4.944145] adrv9009 spi2.1: adrv9009_probe : enter
      [    4.970864] random: fast init done
      [    5.000762] macb ff0b0000.ethernet: Not enabling partial store and forward
      [    5.008133] libphy: MACB_mii_bus: probed
      [    5.044177] macb ff0e0000.ethernet: Not enabling partial store and forward
      [    5.051528] libphy: MACB_mii_bus: probed
      [    5.126778] Marvell 88E1510 ff0e0000.ethernet-ffffffff:00: attached PHY driver [Marvell 88E1510] (mii_bus:phy_addr=ff0e0000.ethernet-ffffffff:00, irq=POLL)
      [    5.140679] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 13 (da:d3:5c:02:19:ba)
      [    5.150861] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
      [    5.157362] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
      [    5.163832] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
      [    5.170291] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
      [    5.178175] dwc3 fe200000.dwc3: Failed to get clk 'ref': -2
      [    5.184036] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:0 protocol:3 pll_locked:yes
      [    5.194103] OF: graph: no port node found in /amba/zynqmp_phy@fd400000/lane1
      [    5.297423] at24 0-002c: 2048 byte 24c16 EEPROM, writable, 1 bytes/write
      [    5.304172] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 15
      [    5.311457] i2c i2c-1: Added multiplexed i2c bus 3
      [    5.316395] i2c i2c-1: Added multiplexed i2c bus 4
      [    5.321332] i2c i2c-1: Added multiplexed i2c bus 5
      [    5.355094] i2c i2c-1: Added multiplexed i2c bus 6
      [    5.387727] i2c i2c-1: Added multiplexed i2c bus 7
      [    5.418429] i2c i2c-1: Added multiplexed i2c bus 8
      [    5.423364] i2c i2c-1: Added multiplexed i2c bus 9
      [    5.428299] i2c i2c-1: Added multiplexed i2c bus 10
      [    5.433169] pca954x 1-0070: registered 8 multiplexed busses for I2C switch pca9548
      [    5.440766] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 16
      [    5.446987] axi_fan_control_driver 80000000.axi-fan-control: Failed to initialize device
      [    5.455109] axi_fan_control_driver: probe of 80000000.axi-fan-control failed with error -22
      [    5.463963] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
      [    5.471442] cpufreq: cpufreq_online: CPU0: Running at unlisted freq: 1333333 KHz
      [    5.478843] cpu cpu0: dev_pm_opp_set_rate: failed to find current OPP for freq 1333333320 (-34)
      [    5.487574] cpufreq: cpufreq_online: CPU0: Unlisted initial frequency changed to: 1199999 KHz
      [    5.496102] cpu cpu0: dev_pm_opp_set_rate: failed to find current OPP for freq 1333333320 (-34)
      [    5.534338] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
      [    5.551258] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: ASoC: CPU DAI (null) not registered
      [    5.561417] adrv9009 spi1.0: adrv9009_probe : enter
      [    5.566943] adrv9009 spi1.1: adrv9009_probe : enter
      [    5.619517] adrv9009 spi2.0: adrv9009_probe : enter
      [    5.629010] adrv9009 spi2.1: adrv9009_probe : enter
      [    5.638728] macb ff0b0000.ethernet: Not enabling partial store and forward
      [    5.646107] libphy: MACB_mii_bus: probed
      [    5.692486] mmc0: new high speed SDHC card at address e624
      [    5.698455] mmcblk0: mmc0:e624 SU08G 7.40 GiB 
      [    5.704132]  mmcblk0: p1 p2 p3
      [    5.726748] Marvell 88E1510 ff0e0000.ethernet-ffffffff:01: attached PHY driver [Marvell 88E1510] (mii_bus:phy_addr=ff0e0000.ethernet-ffffffff:01, irq=POLL)
      [    5.740657] macb ff0b0000.ethernet eth1: Cadence GEM rev 0x50070106 at 0xff0b0000 irq 12 (ba:3f:2a:7d:83:a3)
      [    5.753209] axi_adxcvr 84a40000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.01.a) using GTH4 at 0x84A40000 mapped to 0x(____ptrval____). Number of lanes: 8.
      [    5.768283] axi_adxcvr 84a60000.axi-adxcvr-rx-os: AXI-ADXCVR-RX (17.01.a) using GTH4 at 0x84A60000 mapped to 0x(____ptrval____). Number of lanes: 8.
      [    5.782481] axi_adxcvr 84a20000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.01.a) using GTH4 at 0x84A20000 mapped to 0x(____ptrval____). Number of lanes: 16.
      [    5.797972] asoc-simple-card talise_sound: adau-hifi <-> 82000000.axi-i2s-adi mapping ok
      [    5.809396] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: ASoC: CPU DAI (null) not registered
      [    5.819567] adrv9009 spi1.0: adrv9009_probe : enter
      [    5.829322] adrv9009 spi1.1: adrv9009_probe : enter
      [    5.859999] cf_axi_adc 84a00000.axi-adrv9009-rx-hpc: ADI AIM (10.01.b) at 0x84A00000 mapped to 0x(____ptrval____), probed ADC ADRV9009-X4 as MASTER
      [    5.891851] cf_axi_dds 84a04000.axi-adrv9009-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84A04000 mapped to 0x(____ptrval____), probed DDS ADRV9009-X4
      [    5.906703] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition initialized -> probed
      [    5.918264] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition initialized -> probed
      [    5.929815] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition initialized -> probed
      [    5.941422] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition probed -> idle
      [    5.952366] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition probed -> idle
      [    5.963311] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition probed -> idle
      [    5.974306] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition idle -> device_init
      [    5.985689] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition idle -> device_init
      [    5.997068] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition idle -> device_init
      [    6.008502] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition device_init -> link_init
      [    6.020313] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition device_init -> link_init
      [    6.032127] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition device_init -> link_init
      [    6.043997] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition link_init -> link_supported
      [    6.056076] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition link_init -> link_supported
      [    6.068149] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition link_init -> link_supported
      [    6.080261] [drm] Cannot find any crtc or sizes
      [    6.085431] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition link_supported -> link_pre_setup
      [    6.097944] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition link_supported -> link_pre_setup
      [    6.110458] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition link_supported -> link_pre_setup
      [    6.158383] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition link_pre_setup -> clk_sync_stage1
      [    6.170985] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition link_pre_setup -> clk_sync_stage1
      [    6.183578] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition link_pre_setup -> clk_sync_stage1
      [    6.206385] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.219073] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.231753] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.244613] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.257301] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.269988] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.282676] jesd204: /fpga-axi@0/axi-jesd204-rx@84a50000,jesd204:8,parent=84a50000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 8, Link[1] lanes 2
      [    6.297883] jesd204: /fpga-axi@0/axi-jesd204-rx@84a70000,jesd204:10,parent=84a70000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 8, Link[2] lanes 2
      [    6.313290] jesd204: /fpga-axi@0/axi-jesd204-tx@84a30000,jesd204:12,parent=84a30000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 16, Link[0] lanes 4
      [    6.329815] adrv9009 spi2.1: ADIHAL_resetHw
      [    6.662995] adrv9009 spi2.0: ADIHAL_resetHw
      [    6.995331] adrv9009 spi1.1: ADIHAL_resetHw
      [    7.321870] adrv9009 spi1.0: ADIHAL_resetHw
      [    7.648158] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition clk_sync_stage3 -> link_setup
      [    7.660409] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition clk_sync_stage3 -> link_setup
      [    7.672656] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition clk_sync_stage3 -> link_setup
      [    7.685193] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition link_setup -> opt_setup_stage1
      [    7.697537] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition link_setup -> opt_setup_stage1
      [    7.709877] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition link_setup -> opt_setup_stage1
      [    7.784925] random: crng init done
      [   15.571761] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition opt_setup_stage1 -> opt_setup_stage2
      [   15.584618] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition opt_setup_stage1 -> opt_setup_stage2
      [   15.597481] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition opt_setup_stage1 -> opt_setup_stage2
      [   15.610685] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition opt_setup_stage2 -> opt_setup_stage3
      [   15.623550] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition opt_setup_stage2 -> opt_setup_stage3
      [   15.636411] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition opt_setup_stage2 -> opt_setup_stage3
      [   15.649719] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition opt_setup_stage3 -> opt_setup_stage4
      [   15.662583] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition opt_setup_stage3 -> opt_setup_stage4
      [   15.675445] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition opt_setup_stage3 -> opt_setup_stage4
      [   20.790497] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition opt_setup_stage4 -> opt_setup_stage5
      [   20.803356] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition opt_setup_stage4 -> opt_setup_stage5
      [   20.816219] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition opt_setup_stage4 -> opt_setup_stage5
      [   20.833059] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition opt_setup_stage5 -> clocks_enable
      [   20.845663] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition opt_setup_stage5 -> clocks_enable
      [   20.858267] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition opt_setup_stage5 -> clocks_enable
      [   20.871707] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition clocks_enable -> link_enable
      [   20.883873] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition clocks_enable -> link_enable
      [   20.896042] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition clocks_enable -> link_enable
      [   20.909201] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition link_enable -> link_running
      [   20.921284] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition link_enable -> link_running
      [   20.933363] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition link_enable -> link_running
      [   21.047396] adrv9009 spi2.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   21.161751] adrv9009 spi2.0: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   21.275707] adrv9009 spi1.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   21.389673] adrv9009 spi1.0: adrv9009_info: adrv9009-x4 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   21.402363] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[0] transition link_running -> opt_post_running_stage
      [   21.415398] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[1] transition link_running -> opt_post_running_stage
      [   21.428433] jesd204: /amba/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204 link[2] transition link_running -> opt_post_running_stage
      [   21.441824] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: ASoC: CPU DAI (null) not registered
      [   21.452041] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: ASoC: CPU DAI (null) not registered
      [   21.464598] input: gpio_keys as /devices/platform/gpio_keys/input/input0
      [   21.471544] hctosys: unable to open rtc device (rtc0)
      [   21.476592] of_cfs_init
      [   21.479053] of_cfs_init: OK
      [   21.482031] cfg80211: Loading compiled-in X.509 certificates for regulatory database
      [   21.490084] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: ASoC: CPU DAI (null) not registered
      [   21.618026] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
      [   21.625298] ALSA device list:
      [   21.628254]   #0: ADRV9009 ZU11EG ADAU1761
      [   21.632672] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
      [   21.641280] cfg80211: failed to load regulatory.db
      [   22.395615] EXT4-fs (mmcblk0p2): recovery complete
      [   22.773788] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [   22.781899] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [   22.793532] devtmpfs: mounted
      [   22.796661] Freeing unused kernel memory: 832K
      [   22.801145] Run /sbin/init as init process
      Mount failed for selinuxfs on /sys/fs/selinux:  No such file or directory
      [   23.101760] init: hwclock main process (2333) terminated with status 1
      [   24.291153] systemd-udevd[3420]: could not open moddep file '/lib/modules/4.19.0-14271-g4f88022/modules.dep.bin'
      [ OK ]ting up X socket directories...        
        * STARTDISTCC is set to false in /etc/default/distcc
        * /usr/bin/distccd not starting
      [ OK ]rting IIO Daemon iiod        
   
      Last login: Thu Jan  1 00:00:26 UTC 1970 on ttyPS0
      Welcome to Linaro 14.04 (GNU/Linux 4.19.0-14271-g4f88022 aarch64)
   
        * Documentation:  https://wiki.analog.com/ https://ez.analog.com/
   
      New release '16.04.6 LTS' available.
      Run 'do-release-upgrade' to upgrade to it.
   
      root@analog:~#


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
   
      root@analog:~# **iio_info | grep iio:device**
              iio:device0: ams
              iio:device1: hmc7044-car
              iio:device10: axi-adrv9009-rx-obs-hpc (buffer capable)
              iio:device11: axi-adrv9009-tx-hpc (buffer capable)
              iio:device2: hmc7044-ext
              iio:device3: hmc7044-fmc
              iio:device4: hmc7044
              iio:device5: adrv9009-phy-c
              iio:device6: adrv9009-phy-d
              iio:device7: adrv9009-phy
              iio:device8: adrv9009-phy-b
              iio:device9: axi-adrv9009-rx-hpc (buffer capable)
   


Check clock chip lock status on SoM, FMCOMMS8 and Carrier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>`
-  :doc:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **iio_attr -q -D hmc7044 status**
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN1 @ 30720000 Hz
      PFD:    30720 kHz
      --- PLL2 ---
      Status: Locked (Synchronized)
      Frequency:      2949120000 Hz (Autocal cap bank value: 13)
      SYSREF Status:  Valid & Locked
      SYNC Status:    Synchronized
      Lock Status:    PLL1 & PLL2 Locked
   
      root@analog:~# **iio_attr -q -D hmc7044-fmc status**
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN1 @ 30720000 Hz
      PFD:    30720 kHz
      --- PLL2 ---
      Status: Locked (Synchronized)
      Frequency:      2949120000 Hz (Autocal cap bank value: 14)
      SYSREF Status:  Valid & Locked
      SYNC Status:    Synchronized
      Lock Status:    PLL1 & PLL2 Locked
   
      root@analog:~# **iio_attr -q -D hmc7044-car status**
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN3 @ 38400000 Hz
      PFD:    7680 kHz
      --- PLL2 ---
      Status: Locked (Unsynchronized)
      Frequency:      2949120000 Hz (Autocal cap bank value: 14)
      SYSREF Status:  Valid & Locked
      SYNC Status:    Unsynchronized
      Lock Status:    PLL1 & PLL2 Locked
   


Synchronizing the ADRV9009s
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>` the tranceivers should always be in a synchronized state.

Check JESD204B Link Status
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **TERM=vt100 jesd_status -s**
        (DEVICES) Found 3 JESD204 Link Layer peripherals
   
        (0): 84a50000.axi-jesd204-rx  [*]
        (1): 84a30000.axi-jesd204-tx
        (2): 84a70000.axi-jesd204-rx
   
        (STATUS)
        Link is                 enabled
        Link Status             DATA
        Measured Link Clock     245.763
        Reported Link Clock     245.760
        Lane rate               9830.400
        Lane rate / 40          245.760
        LMFC rate               7.680
        SYSREF captured         Yes
        SYSREF alignment error  No
        SYNC~
   
        (LANE STATUS)
        Lane#                             0      1      2      3      4      5      6      7
        Errors                            0      0      0      0      0      0      0      0
        Latency (Multiframes/Octets)      2/38   2/37   2/41   2/39   2/41   2/40   2/39   2/39
        CGS State                         DATA   DATA   DATA   DATA   DATA   DATA   DATA   DATA
        Initial Frame Sync                Yes    Yes    Yes    Yes    Yes    Yes    Yes    Yes
        Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes    Yes    Yes    Yes    Yes
   
        (DEVICES) Found 3 JESD204 Link Layer peripherals
   
        (0): 84a50000.axi-jesd204-rx
        (1): 84a30000.axi-jesd204-tx
        (2): 84a70000.axi-jesd204-rx  [*]
   
        (STATUS)
        Link is                 enabled
        Link Status             DATA
        Measured Link Clock     122.882
        Reported Link Clock     122.880
        Lane rate               4915.200
        Lane rate / 40          122.880
        LMFC rate               3.840
        SYSREF captured         Yes
        SYSREF alignment error  No
        SYNC~
   
        (LANE STATUS)
        Lane#                             0      1      2      3      4      5      6      7
        Errors                            0      0      0      0      0      0      0      0
        Latency (Multiframes/Octets)      2/9    2/11   2/15   2/11   2/13   2/15   2/15   2/15
        CGS State                         DATA   DATA   DATA   DATA   DATA   DATA   DATA   DATA
        Initial Frame Sync                Yes    Yes    Yes    Yes    Yes    Yes    Yes    Yes
        Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes    Yes    Yes    Yes    Yes
   
        (DEVICES) Found 3 JESD204 Link Layer peripherals
   
        (0): 84a50000.axi-jesd204-rx
        (1): 84a30000.axi-jesd204-tx  [*]
        (2): 84a70000.axi-jesd204-rx
   
        (STATUS)
        Link is                 enabled
        Link Status             DATA
        Measured Link Clock     122.882
        Reported Link Clock     122.880
        Lane rate               4915.200
        Lane rate / 40          122.880
        LMFC rate               7.680
        SYSREF captured         Yes
        SYSREF alignment error  No
        SYNC~                   deasserted
   


ZCU102
~~~~~~

For ZCU102, FMCOMMS8 board connects to the HPC0 connector. The carrier setup requires power, UART (115200), ethernet (Linux), DisplayPort and/or JTAG connections.

.. _messages-1:

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
   
      Xilinx Zynq MP First Stage Boot Loader 
      Release 2019.1   Aug 25 2020  -  23:57:00
      NOTICE:  ATF running on XCZU9EG/silicon v4/RTL5.1 at 0xfffea000
      NOTICE:  BL31: Secure code at 0x0
      NOTICE:  BL31: Non secure code at 0x8000000
      NOTICE:  BL31: v2.0(release):xilinx-v2019.2
      NOTICE:  BL31: Built : 10:19:24, Jan 13 2020
      PMUFW:  v1.1
   
   
      U-Boot 2018.01-21436-gbba91bc203 (Jan 13 2020 - 10:50:58 +0200) Xilinx ZynqMP ZCU102 rev1.0, Build: jenkins-development-build_uboot-1
   
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
      Net:   ZYNQ GEM: ff0e0000, phyaddr c, interface rgmii-id
   
      Warning: ethernet@ff0e0000 using MAC address from ROM
      eth0: ethernet@ff0e0000
      Hit any key to stop autoboot:  0 
      switch to partitions #0, OK
      mmc0 is current device
      Device: sdhci@ff170000
      Manufacturer ID: 3
      OEM: 5344
      Name: SU08G 
      Tran Speed: 50000000
      Rd Block Len: 512
      SD version 3.0
      High Capacity: Yes
      Capacity: 7.4 GiB
      Bus Width: 4-bit
      Erase Group Size: 512 Bytes
      reading uEnv.txt
      91 bytes read in 10 ms (8.8 KiB/s)
      Loaded environment from uEnv.txt
      Importing environment from SD ...
      reading system.dtb
      65123 bytes read in 24 ms (2.6 MiB/s)
      reading Image
      28590592 bytes read in 1882 ms (14.5 MiB/s)
      ## Flattened Device Tree blob at 04000000
         Booting using the fdt blob at 0x4000000
         Loading Device Tree to 000000000ffed000, end 000000000ffffe62 ... OK
   
      Starting kernel ...
   
      [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
      [    0.000000] Linux version 4.19.0-14271-g4f88022 (michael@mhenneri-D06) (gcc version 8.2.0 (GCC)) #3201 SMP Fri Aug 28 12:05:21 CEST 2020
      [    0.000000] Machine model: ZynqMP ZCU102 Rev1.0
      [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff000000 (options '115200n8')
      [    0.000000] bootconsole [cdns0] enabled
      [    0.000000] efi: Getting EFI parameters from FDT:
      [    0.000000] efi: UEFI not found.
      [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
      [    0.000000] psci: probing for conduit method from DT.
      [    0.000000] psci: PSCIv1.1 detected in firmware.
      [    0.000000] psci: Using standard PSCI v0.2 function IDs
      [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
      [    0.000000] psci: SMC Calling Convention v1.1
      [    0.000000] random: get_random_bytes called from start_kernel+0x94/0x3f8 with crng_init=0
      [    0.000000] percpu: Embedded 22 pages/cpu @(____ptrval____) s52504 r8192 d29416 u90112
      [    0.000000] Detected VIPT I-cache on CPU0
      [    0.000000] CPU features: enabling workaround for ARM erratum 845719
      [    0.000000] Speculative Store Bypass Disable mitigation not required
      [    0.000000] CPU features: detected: Kernel page table isolation (KPTI)
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
      [    0.000000] Kernel command line: earlycon console=ttyPS0,115200 root=/dev/mmcblk0p2 rw rootfstype=ext4 rootwait root=/dev/mmcblk0p2 rw rootwait
      [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
      [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
      [    0.000000] software IO TLB: mapped [mem 0x6bfff000-0x6ffff000] (64MB)
      [    0.000000] Memory: 3773344K/4194304K available (12540K kernel code, 1552K rwdata, 12976K rodata, 832K init, 326K bss, 158816K reserved, 262144K cma-reserved)
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
      [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
      [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
      [    0.000000] GIC: Using split EOI/Deactivate mode
      [    0.000000] arch_timer: cp15 timer(s) running at 99.99MHz (phys).
      [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x170f8de2d3, max_idle_ns: 440795206112 ns
      [    0.000003] sched_clock: 56 bits at 99MHz, resolution 10ns, wraps every 4398046511101ns
      [    0.008244] Console: colour dummy device 80x25
      [    0.012390] Calibrating delay loop (skipped), value calculated using timer frequency.. 199.98 BogoMIPS (lpj=399960)
      [    0.022756] pid_max: default: 32768 minimum: 301
      [    0.027447] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.034012] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.041766] ASID allocator initialised with 32768 entries
      [    0.046508] rcu: Hierarchical SRCU implementation.
      [    0.051542] EFI services will not be available.
      [    0.055826] smp: Bringing up secondary CPUs ...
      [    0.060486] Detected VIPT I-cache on CPU1
      [    0.060515] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [    0.060820] Detected VIPT I-cache on CPU2
      [    0.060839] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [    0.061124] Detected VIPT I-cache on CPU3
      [    0.061143] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [    0.061187] smp: Brought up 1 node, 4 CPUs
      [    0.095682] SMP: Total of 4 processors activated.
      [    0.100355] CPU features: detected: 32-bit EL0 Support
      [    0.106867] CPU: All CPU(s) started at EL2
      [    0.109534] alternatives: patching kernel code
      [    0.114823] devtmpfs: initialized
      [    0.124311] Registered cp15_barrier emulation handler
      [    0.124360] Registered setend emulation handler
      [    0.128332] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      [    0.137916] futex hash table entries: 1024 (order: 4, 65536 bytes)
      [    0.149501] xor: measuring software checksum speed
      [    0.188118]    8regs     :  2375.000 MB/sec
      [    0.228146]    8regs_prefetch:  2052.000 MB/sec
      [    0.268177]    32regs    :  2724.000 MB/sec
      [    0.308206]    32regs_prefetch:  2308.000 MB/sec
      [    0.308247] xor: using function: 32regs (2724.000 MB/sec)
      [    0.312547] pinctrl core: initialized pinctrl subsystem
      [    0.318316] NET: Registered protocol family 16
      [    0.322493] audit: initializing netlink subsys (disabled)
      [    0.327571] audit: type=2000 audit(0.272:1): state=initialized audit_enabled=0 res=1
      [    0.335228] cpuidle: using governor menu
      [    0.339301] vdso: 2 pages (1 code @ (____ptrval____), 1 data @ (____ptrval____))
      [    0.346462] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
      [    0.353876] DMA: preallocated 256 KiB pool for atomic allocations
      [    0.372834] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
      [    0.441863] raid6: int64x1  gen()   444 MB/s
      [    0.509922] raid6: int64x1  xor()   451 MB/s
      [    0.577973] raid6: int64x2  gen()   678 MB/s
      [    0.646013] raid6: int64x2  xor()   599 MB/s
      [    0.714102] raid6: int64x4  gen()   981 MB/s
      [    0.782113] raid6: int64x4  xor()   737 MB/s
      [    0.850165] raid6: int64x8  gen()  1165 MB/s
      [    0.918212] raid6: int64x8  xor()   759 MB/s
      [    0.986270] raid6: neonx1   gen()   736 MB/s
      [    1.054283] raid6: neonx1   xor()   881 MB/s
      [    1.122342] raid6: neonx2   gen()  1129 MB/s
      [    1.190385] raid6: neonx2   xor()  1174 MB/s
      [    1.258443] raid6: neonx4   gen()  1479 MB/s
      [    1.326454] raid6: neonx4   xor()  1418 MB/s
      [    1.394505] raid6: neonx8   gen()  1553 MB/s
      [    1.462549] raid6: neonx8   xor()  1459 MB/s
      [    1.462587] raid6: using algorithm neonx8 gen() 1553 MB/s
      [    1.466541] raid6: .... xor() 1459 MB/s, rmw enabled
      [    1.471472] raid6: using neon recovery algorithm
      [    1.476770] SCSI subsystem initialized
      [    1.479944] usbcore: registered new interface driver usbfs
      [    1.485257] usbcore: registered new interface driver hub
      [    1.490537] usbcore: registered new device driver usb
      [    1.495580] media: Linux media interface: v0.10
      [    1.500040] videodev: Linux video capture interface: v2.00
      [    1.505518] pps_core: LinuxPPS API ver. 1 registered
      [    1.510402] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    1.519495] PTP clock support registered
      [    1.523392] EDAC MC: Ver: 3.0.0
      [    1.526859] zynqmp-ipi-mbox mailbox@ff990400: Probed ZynqMP IPI Mailbox driver.
      [    1.534269] jesd204: created con: id=0, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@85a20000 <-> /fpga-axi@0/axi-jesd204-tx@85a30000
      [    1.545446] jesd204: created con: id=1, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx-os@85a60000 <-> /fpga-axi@0/axi-jesd204-rx@85a70000
      [    1.557381] jesd204: created con: id=2, topo=0, link=1, /fpga-axi@0/axi-adxcvr-rx@85a40000 <-> /fpga-axi@0/axi-jesd204-rx@85a50000
      [    1.569061] jesd204: created con: id=3, topo=0, link=0, /amba/spi@ff040000/hmc7044-fmc@2 <-> /fpga-axi@0/axi-adxcvr-tx@85a20000
      [    1.580481] jesd204: created con: id=4, topo=0, link=2, /amba/spi@ff040000/hmc7044-fmc@2 <-> /fpga-axi@0/axi-adxcvr-rx-os@85a60000
      [    1.592158] jesd204: created con: id=5, topo=0, link=1, /amba/spi@ff040000/hmc7044-fmc@2 <-> /fpga-axi@0/axi-adxcvr-rx@85a40000
      [    1.603626] jesd204: created con: id=6, topo=0, link=1, /amba/spi@ff040000/adrv9009-phy-c@0 <-> /amba/spi@ff040000/adrv9009-phy-d@1
      [    1.615368] jesd204: created con: id=7, topo=0, link=2, /amba/spi@ff040000/adrv9009-phy-c@0 <-> /amba/spi@ff040000/adrv9009-phy-d@1
      [    1.627139] jesd204: created con: id=8, topo=0, link=0, /amba/spi@ff040000/adrv9009-phy-c@0 <-> /amba/spi@ff040000/adrv9009-phy-d@1
      [    1.638890] jesd204: created con: id=9, topo=0, link=1, /fpga-axi@0/axi-jesd204-rx@85a50000 <-> /amba/spi@ff040000/adrv9009-phy-c@0
      [    1.650645] jesd204: created con: id=10, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@85a70000 <-> /amba/spi@ff040000/adrv9009-phy-c@0
      [    1.662497] jesd204: created con: id=11, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@85a30000 <-> /amba/spi@ff040000/adrv9009-phy-c@0
      [    1.674352] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1: JESD204 link[0] transition uninitialized -> initialized
      [    1.684545] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1: JESD204 link[1] transition uninitialized -> initialized
      [    1.694752] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1: JESD204 link[2] transition uninitialized -> initialized
      [    1.704958] jesd204: found 9 devices and 1 topologies
      [    1.710011] FPGA manager framework
      [    1.713527] Advanced Linux Sound Architecture Driver Initialized.
      [    1.719669] Bluetooth: Core ver 2.22
      [    1.722968] NET: Registered protocol family 31
      [    1.727366] Bluetooth: HCI device and connection manager initialized
      [    1.733683] Bluetooth: HCI socket layer initialized
      [    1.738525] Bluetooth: L2CAP socket layer initialized
      [    1.743555] Bluetooth: SCO socket layer initialized
      [    1.748828] clocksource: Switched to clocksource arch_sys_counter
      [    1.754528] VFS: Disk quotas dquot_6.6.0
      [    1.758374] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
      [    1.769392] NET: Registered protocol family 2
      [    1.769812] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes)
      [    1.777322] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
      [    1.784660] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
      [    1.791409] TCP: Hash tables configured (established 32768 bind 32768)
      [    1.797582] UDP hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.803563] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.810048] NET: Registered protocol family 1
      [    1.814420] RPC: Registered named UNIX socket transport module.
      [    1.820109] RPC: Registered udp transport module.
      [    1.824775] RPC: Registered tcp transport module.
      [    1.829446] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    1.836558] hw perfevents: no interrupt-affinity property for /pmu, guessing.
      [    1.843083] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
      [    1.851462] Initialise system trusted keyrings
      [    1.855113] workingset: timestamp_bits=62 max_order=20 bucket_order=0
      [    1.862113] NFS: Registering the id_resolver key type
      [    1.866484] Key type id_resolver registered
      [    1.870624] Key type id_legacy registered
      [    1.874612] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    1.881276] jffs2: version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.
      [    2.970065] NET: Registered protocol family 38
      [    3.029400] Key type asymmetric registered
      [    3.029438] Asymmetric key parser 'x509' registered
      [    3.032724] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
      [    3.040069] io scheduler noop registered
      [    3.043950] io scheduler deadline registered
      [    3.048206] io scheduler cfq registered (default)
      [    3.052860] io scheduler mq-deadline registered
      [    3.057357] io scheduler kyber registered
      [    3.089187] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      [    3.093325] cacheinfo: Unable to detect cache hierarchy for CPU 0
      [    3.100309] brd: module loaded
      [    3.104136] loop: module loaded
      [    3.104350] Registered mathworks_ip class
      [    3.106909] mtdoops: mtd device (mtddev=name/number) must be supplied
      [    3.113874] libphy: Fixed MDIO Bus: probed
      [    3.117684] tun: Universal TUN/TAP device driver, 1.6
      [    3.121683] CAN device driver interface
      [    3.126306] usbcore: registered new interface driver asix
      [    3.130778] usbcore: registered new interface driver ax88179_178a
      [    3.136814] usbcore: registered new interface driver cdc_ether
      [    3.142611] usbcore: registered new interface driver net1080
      [    3.148234] usbcore: registered new interface driver cdc_subset
      [    3.154114] usbcore: registered new interface driver zaurus
      [    3.159664] usbcore: registered new interface driver cdc_ncm
      [    3.165971] usbcore: registered new interface driver uas
      [    3.170562] usbcore: registered new interface driver usb-storage
      [    3.176555] usbcore: registered new interface driver upd78f0730
      [    3.182399] usbserial: USB Serial support registered for upd78f0730
      [    3.189308] rtc_zynqmp ffa60000.rtc: rtc core: registered ffa60000.rtc as rtc0
      [    3.195851] i2c /dev entries driver
      [    3.201238] usbcore: registered new interface driver uvcvideo
      [    3.204960] USB Video Class driver (1.1.1)
      [    3.210338] Bluetooth: HCI UART driver ver 2.3
      [    3.213447] Bluetooth: HCI UART protocol H4 registered
      [    3.218542] Bluetooth: HCI UART protocol BCSP registered
      [    3.223839] Bluetooth: HCI UART protocol LL registered
      [    3.228922] Bluetooth: HCI UART protocol ATH3K registered
      [    3.234302] Bluetooth: HCI UART protocol Three-wire (H5) registered
      [    3.240557] Bluetooth: HCI UART protocol Intel registered
      [    3.245895] Bluetooth: HCI UART protocol QCA registered
      [    3.251101] usbcore: registered new interface driver bcm203x
      [    3.256717] usbcore: registered new interface driver bpa10x
      [    3.262257] usbcore: registered new interface driver bfusb
      [    3.267706] usbcore: registered new interface driver btusb
      [    3.273129] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
      [    3.278793] usbcore: registered new interface driver ath3k
      [    3.284328] EDAC MC: ECC not enabled
      [    3.287990] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
      [    3.300561] sdhci: Secure Digital Host Controller Interface driver
      [    3.306002] sdhci: Copyright(c) Pierre Ossman
      [    3.310326] sdhci-pltfm: SDHCI platform and OF driver helper
      [    3.316324] ledtrig-cpu: registered to indicate activity on CPUs
      [    3.321964] zynqmp_firmware_probe Platform Management API v1.1
      [    3.327717] zynqmp_firmware_probe Trustzone version v1.0
      [    3.335772] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
      [    3.362949] zynqmp_clk_mux_get_parent() getparent failed for clock: lpd_wdt, ret = -22
      [    3.365642] alg: No test for xilinx-zynqmp-aes (zynqmp-aes)
      [    3.370817] zynqmp_aes zynqmp_aes: AES Successfully Registered
      [    3.370817] 
      [    3.378296] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
      [    3.384425] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
      [    3.389992] usbcore: registered new interface driver usbhid
      [    3.395326] usbhid: USB HID core driver
      [    3.407086] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
      [    3.408381] usbcore: registered new interface driver snd-usb-audio
      [    3.415778] pktgen: Packet Generator for packet performance testing. Version: 2.75
      [    3.421944] Initializing XFRM netlink socket
      [    3.425863] NET: Registered protocol family 10
      [    3.430576] Segment Routing with IPv6
      [    3.433921] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    3.440066] NET: Registered protocol family 17
      [    3.444139] NET: Registered protocol family 15
      [    3.448555] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
      [    3.461661] can: controller area network core (rev 20170425 abi 9)
      [    3.467602] NET: Registered protocol family 29
      [    3.471988] can: raw protocol (rev 20170425)
      [    3.476224] can: broadcast manager protocol (rev 20170425 t)
      [    3.481849] can: netlink gateway (rev 20170425) max_hops=1
      [    3.487545] Bluetooth: RFCOMM TTY layer initialized
      [    3.492149] Bluetooth: RFCOMM socket layer initialized
      [    3.497257] Bluetooth: RFCOMM ver 1.11
      [    3.500970] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
      [    3.506242] Bluetooth: BNEP filters: protocol multicast
      [    3.511435] Bluetooth: BNEP socket layer initialized
      [    3.516364] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
      [    3.522248] Bluetooth: HIDP socket layer initialized
      [    3.527295] 9pnet: Installing 9P2000 support
      [    3.531425] NET: Registered protocol family 36
      [    3.535840] Key type dns_resolver registered
      [    3.540553] registered taskstats version 1
      [    3.544138] Loading compiled-in X.509 certificates
      [    3.549226] Btrfs loaded, crc32c=crc32c-generic
      [    3.559662] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 40, base_baud = 6249999) is a xuartps
      [    3.568843] console [ttyPS0] enabled
      [    3.568843] console [ttyPS0] enabled
      [    3.572435] bootconsole [cdns0] disabled
      [    3.572435] bootconsole [cdns0] disabled
      [    3.580496] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 41, base_baud = 6249999) is a xuartps
      [    3.593879] of-fpga-region fpga-full: FPGA Region probed
      [    3.599730] nwl-pcie fd0e0000.pcie: Link is DOWN
      [    3.604376] nwl-pcie fd0e0000.pcie: host bridge /amba/pcie@fd0e0000 ranges:
      [    3.611346] nwl-pcie fd0e0000.pcie:   MEM 0xe0000000..0xefffffff -> 0xe0000000
      [    3.618567] nwl-pcie fd0e0000.pcie:   MEM 0x600000000..0x7ffffffff -> 0x600000000
      [    3.626147] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
      [    3.632323] pci_bus 0000:00: root bus resource [bus 00-ff]
      [    3.637798] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
      [    3.644668] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
      [    3.656419] pci 0000:00:00.0: PCI bridge to [bus 01-0c]
      [    3.662690] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
      [    3.669266] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
      [    3.676367] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
      [    3.683468] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
      [    3.690568] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
      [    3.697668] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
      [    3.704766] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
      [    3.711874] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
      [    3.718969] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
      [    3.726212] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:8 protocol:4 pll_locked:yes
      [    3.737586] zynqmp_clk_divider_set_rate() set divider failed for spi1_ref_div1, ret = -13
      [    3.746260] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
      [    3.757021] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
      [    3.765094] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
      [    3.773548] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
      [    3.785992] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
      [    3.798654] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
      [    3.808846] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
      [    3.815859] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
      [    3.822469] [drm] No driver support for vblank timestamp query.
      [    3.828449] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffff8008d82d70)
      [    3.979144] random: fast init done
      [    8.165108] [drm] Cannot find any crtc or sizes
      [    8.169885] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
      [    8.177998] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
      [    8.186979] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:3 protocol:2 pll_locked:yes
      [    8.204919] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
      [    8.213885] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst 
      [    8.224308] scsi host0: ahci-ceva
      [    8.227888] scsi host1: ahci-ceva
      [    8.231352] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 37
      [    8.239268] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 37
      [    8.248313] adrv9009 spi1.0: adrv9009_probe : enter
      [    8.253836] adrv9009 spi1.1: adrv9009_probe : enter
      [    8.305718] jesd204: /amba/spi@ff040000/hmc7044-fmc@2,jesd204:2,parent=spi1.2: Using as SYSREF provider
      [    8.315937] m25p80 spi0.0: SPI-NOR-UniqueID 10000023536359160025001817101588af
      [    8.323160] m25p80 spi0.0: found n25q512a, expected m25p80
      [    8.328861] m25p80 spi0.0: n25q512a (131072 Kbytes)
      [    8.333757] 4 fixed-partitions partitions found on MTD device spi0.0
      [    8.340103] Creating 4 MTD partitions on "spi0.0":
      [    8.344889] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
      [    8.351091] 0x000000100000-0x000000600000 : "qspi-linux"
      [    8.356798] 0x000000600000-0x000000620000 : "qspi-device-tree"
      [    8.363022] 0x000000620000-0x000000c00000 : "qspi-rootfs"
      [    8.370887] macb ff0e0000.ethernet: Not enabling partial store and forward
      [    8.378255] libphy: MACB_mii_bus: probed
      [    8.382249] mdio_bus ff0e0000.ethernet-ffffffff: MDIO device at address 21 is missing.
      [    8.392309] TI DP83867 ff0e0000.ethernet-ffffffff:0c: attached PHY driver [TI DP83867] (mii_bus:phy_addr=ff0e0000.ethernet-ffffffff:0c, irq=POLL)
      [    8.405350] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 22 (00:0a:35:03:6f:71)
      [    8.415485] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
      [    8.422041] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
      [    8.428544] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
      [    8.435043] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
      [    8.442856] dwc3 fe200000.dwc3: Failed to get clk 'ref': -2
      [    8.448712] xilinx-psgtr fd400000.zynqmp_phy: Lane:2 type:0 protocol:3 pll_locked:yes
      [    8.456980] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
      [    8.462477] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
      [    8.470468] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000202010810
      [    8.479890] xhci-hcd xhci-hcd.0.auto: irq 52, io mem 0xfe200000
      [    8.486023] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
      [    8.494295] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    8.501516] usb usb1: Product: xHCI Host Controller
      [    8.506385] usb usb1: Manufacturer: Linux 4.19.0-14271-g4f88022 xhci-hcd
      [    8.513077] usb usb1: SerialNumber: xhci-hcd.0.auto
      [    8.518239] hub 1-0:1.0: USB hub found
      [    8.522022] hub 1-0:1.0: 1 port detected
      [    8.526151] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
      [    8.531643] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
      [    8.539301] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0  SuperSpeed
      [    8.546035] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 4.19
      [    8.554305] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    8.561519] usb usb2: Product: xHCI Host Controller
      [    8.563028] ata2: SATA link down (SStatus 0 SControl 330)
      [    8.566388] usb usb2: Manufacturer: Linux 4.19.0-14271-g4f88022 xhci-hcd
      [    8.571798] ata1: SATA link down (SStatus 0 SControl 330)
      [    8.578471] usb usb2: SerialNumber: xhci-hcd.0.auto
      [    8.588988] hub 2-0:1.0: USB hub found
      [    8.592759] hub 2-0:1.0: 1 port detected
      [    8.597942] pca953x 0-0020: 0-0020 supply vcc not found, using dummy regulator
      [    8.605197] pca953x 0-0020: Linked as a consumer to regulator.0
      [    8.612011] GPIO line 496 (sel0) hogged as output/low
      [    8.617412] GPIO line 497 (sel1) hogged as output/high
      [    8.622894] GPIO line 498 (sel2) hogged as output/high
      [    8.628381] GPIO line 499 (sel3) hogged as output/high
      [    8.633743] pca953x 0-0021: 0-0021 supply vcc not found, using dummy regulator
      [    8.640991] pca953x 0-0021: Linked as a consumer to regulator.0
      [    8.648458] ina2xx 3-0040: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.655275] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.662093] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.668912] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.675726] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.682544] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.689360] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.696178] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.702995] ina2xx 3-004a: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.709812] ina2xx 3-004b: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.716231] i2c i2c-0: Added multiplexed i2c bus 3
      [    8.721709] ina2xx 4-0040: power monitor ina226 (Rshunt = 2000 uOhm)
      [    8.728527] ina2xx 4-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.735342] ina2xx 4-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.742156] ina2xx 4-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.748971] ina2xx 4-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.755780] ina2xx 4-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.762603] ina2xx 4-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.769420] ina2xx 4-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    8.775835] i2c i2c-0: Added multiplexed i2c bus 4
      [    8.815441] i2c i2c-0: Added multiplexed i2c bus 5
      [    8.820414] i2c i2c-0: Added multiplexed i2c bus 6
      [    8.825211] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
      [    8.832564] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 24
      [    8.840363] at24 7-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
      [    8.847121] i2c i2c-1: Added multiplexed i2c bus 7
      [    8.852261] i2c i2c-1: Added multiplexed i2c bus 8
      [    8.859199] si570 9-005d: registered, current frequency 300000000 Hz
      [    8.865604] i2c i2c-1: Added multiplexed i2c bus 9
      [    8.882787] si570 10-005d: registered, current frequency 148500000 Hz
      [    8.889281] i2c i2c-1: Added multiplexed i2c bus 10
      [    8.894390] si5324 11-0069: si5328 probed
      [    8.956914] si5324 11-0069: si5328 probe successful
      [    8.961836] i2c i2c-1: Added multiplexed i2c bus 11
      [    8.966886] i2c i2c-1: Added multiplexed i2c bus 12
      [    8.971943] i2c i2c-1: Added multiplexed i2c bus 13
      [    8.977005] i2c i2c-1: Added multiplexed i2c bus 14
      [    8.981891] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
      [    8.991077] at24 15-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      [    8.997830] i2c i2c-1: Added multiplexed i2c bus 15
      [    9.002899] i2c i2c-1: Added multiplexed i2c bus 16
      [    9.007966] i2c i2c-1: Added multiplexed i2c bus 17
      [    9.013028] i2c i2c-1: Added multiplexed i2c bus 18
      [    9.018088] i2c i2c-1: Added multiplexed i2c bus 19
      [    9.023146] i2c i2c-1: Added multiplexed i2c bus 20
      [    9.028210] i2c i2c-1: Added multiplexed i2c bus 21
      [    9.033271] i2c i2c-1: Added multiplexed i2c bus 22
      [    9.038151] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
      [    9.045757] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 25
      [    9.052116] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
      [    9.089308] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
      [    9.105199] axi_adxcvr 85a40000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.01.a) using GTH4 at 0x85A40000 mapped to 0x(____ptrval____). Number of lanes: 4.
      [    9.120382] axi_adxcvr 85a60000.axi-adxcvr-rx-os: AXI-ADXCVR-RX (17.01.a) using GTH4 at 0x85A60000 mapped to 0x(____ptrval____). Number of lanes: 4.
      [    9.134448] axi_adxcvr 85a20000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.01.a) using GTH4 at 0x85A20000 mapped to 0x(____ptrval____). Number of lanes: 8.
      [    9.148874] adrv9009 spi1.0: adrv9009_probe : enter
      [    9.158823] adrv9009 spi1.1: adrv9009_probe : enter
      [    9.168589] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition initialized -> probed
      [    9.180338] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition initialized -> probed
      [    9.192073] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition initialized -> probed
      [    9.203816] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition probed -> idle
      [    9.214937] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition probed -> idle
      [    9.226056] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition probed -> idle
      [    9.237182] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition idle -> device_init
      [    9.248740] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition idle -> device_init
      [    9.260292] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition idle -> device_init
      [    9.271859] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition device_init -> link_init
      [    9.283854] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition device_init -> link_init
      [    9.295842] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition device_init -> link_init
      [    9.307840] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition link_init -> link_supported
      [    9.320088] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition link_init -> link_supported
      [    9.332336] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition link_init -> link_supported
      [    9.344884] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition link_supported -> link_pre_setup
      [    9.357585] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition link_supported -> link_pre_setup
      [    9.370273] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition link_supported -> link_pre_setup
      [    9.382961] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition link_pre_setup -> clk_sync_stage1
      [    9.395735] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition link_pre_setup -> clk_sync_stage1
      [    9.408512] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition link_pre_setup -> clk_sync_stage1
      [    9.421296] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition clk_sync_stage1 -> clk_sync_stage2
      [    9.434154] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition clk_sync_stage1 -> clk_sync_stage2
      [    9.447013] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition clk_sync_stage1 -> clk_sync_stage2
      [    9.459882] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition clk_sync_stage2 -> clk_sync_stage3
      [    9.472742] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition clk_sync_stage2 -> clk_sync_stage3
      [    9.485606] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition clk_sync_stage2 -> clk_sync_stage3
      [    9.498466] jesd204: /fpga-axi@0/axi-jesd204-rx@85a50000,jesd204:6,parent=85a50000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 4, Link[1] lanes 2
      [    9.513677] jesd204: /fpga-axi@0/axi-jesd204-rx@85a70000,jesd204:7,parent=85a70000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 4, Link[2] lanes 2
      [    9.528945] jesd204: /fpga-axi@0/axi-jesd204-tx@85a30000,jesd204:8,parent=85a30000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 8, Link[0] lanes 4
      [    9.545248] adrv9009 spi1.0: ADIHAL_resetHw
      [    9.654212] mmc0: new ultra high speed DDR50 SDHC card at address e624
      [    9.661237] mmcblk0: mmc0:e624 SU08G 7.40 GiB 
      [    9.666861]  mmcblk0: p1 p2 p3
      [    9.870976] adrv9009 spi1.1: ADIHAL_resetHw
      [   10.193595] random: crng init done
      [   10.199953] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition clk_sync_stage3 -> link_setup
      [   10.212385] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition clk_sync_stage3 -> link_setup
      [   10.224809] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition clk_sync_stage3 -> link_setup
      [   10.237392] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition link_setup -> opt_setup_stage1
      [   10.249912] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition link_setup -> opt_setup_stage1
      [   10.262423] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition link_setup -> opt_setup_stage1
      [   13.694125] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition opt_setup_stage1 -> opt_setup_stage2
      [   13.707161] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition opt_setup_stage1 -> opt_setup_stage2
      [   13.720197] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition opt_setup_stage1 -> opt_setup_stage2
      [   13.733389] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition opt_setup_stage2 -> opt_setup_stage3
      [   13.746426] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition opt_setup_stage2 -> opt_setup_stage3
      [   13.759459] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition opt_setup_stage2 -> opt_setup_stage3
      [   13.772703] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition opt_setup_stage3 -> opt_setup_stage4
      [   13.785744] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition opt_setup_stage3 -> opt_setup_stage4
      [   13.798783] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition opt_setup_stage3 -> opt_setup_stage4
      [   16.080839] [drm] Cannot find any crtc or sizes
      [   18.813871] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition opt_setup_stage4 -> opt_setup_stage5
      [   18.826909] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition opt_setup_stage4 -> opt_setup_stage5
      [   18.839948] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition opt_setup_stage4 -> opt_setup_stage5
      [   18.856394] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition opt_setup_stage5 -> clocks_enable
      [   18.869167] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition opt_setup_stage5 -> clocks_enable
      [   18.881942] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition opt_setup_stage5 -> clocks_enable
      [   18.895036] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition clocks_enable -> link_enable
      [   18.907382] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition clocks_enable -> link_enable
      [   18.919721] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition clocks_enable -> link_enable
      [   18.932567] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition link_enable -> link_running
      [   18.944820] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition link_enable -> link_running
      [   18.957076] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition link_enable -> link_running
      [   19.070883] adrv9009 spi1.0: adrv9009_info: adrv9009-x2 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   19.185084] adrv9009 spi1.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [   19.197512] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[0] transition link_running -> opt_post_running_stage
      [   19.210722] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[1] transition link_running -> opt_post_running_stage
      [   19.223934] jesd204: /amba/spi@ff040000/adrv9009-phy-d@1,jesd204:1,parent=spi1.1: JESD204 link[2] transition link_running -> opt_post_running_stage
      [   19.258097] cf_axi_adc 85a00000.axi-adrv9009-rx-hpc: ADI AIM (10.01.b) at 0x85A00000 mapped to 0x000000006fc6d050, probed ADC ADRV9009-X2 as MASTER
      [   19.289610] cf_axi_dds 85a04000.axi-adrv9009-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x85A04000 mapped to 0x00000000088886a9, probed DDS ADRV9009-X2
      [   19.306812] input: gpio-keys as /devices/platform/gpio-keys/input/input0
      [   19.313799] rtc_zynqmp ffa60000.rtc: setting system clock to 2020-08-28 11:01:01 UTC (1598612461)
      [   19.322673] of_cfs_init
      [   19.325130] of_cfs_init: OK
      [   19.328091] cfg80211: Loading compiled-in X.509 certificates for regulatory database
      [   19.466976] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
      [   19.473587] zynqmp_pll_disable() clock disable failed for dpll_int, ret = -13
      [   19.481416] ALSA device list:
      [   19.484367]   #0: DisplayPort monitor
      [   19.488354] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
      [   19.496969] cfg80211: failed to load regulatory.db
      [   20.879217] EXT4-fs (mmcblk0p2): 1 orphan inode deleted
      [   20.884448] EXT4-fs (mmcblk0p2): recovery complete
      [   21.155004] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [   21.163118] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [   21.173357] devtmpfs: mounted
      [   21.176493] Freeing unused kernel memory: 832K
      [   21.180981] Run /sbin/init as init process
      Mount failed for selinuxfs on /sys/fs/selinux:  No such file or directory
      [   22.422854] systemd-udevd[3428]: could not open moddep file '/lib/modules/4.19.0-14271-g4f88022/modules.dep.bin'
      [ OK ]ting up X socket directories...        
        * STARTDISTCC is set to false in /etc/default/distcc
        * /usr/bin/distccd not starting
      [ OK ]rting IIO Daemon iiod        
   
      Last login: Fri Aug 28 10:31:43 UTC 2020 on ttyPS0
      Welcome to Linaro 14.04 (GNU/Linux 4.19.0-14271-g4f88022 aarch64)
   
        * Documentation:  https://wiki.analog.com/ https://ez.analog.com/
   
      root@analog:~#


   .. raw:: html

      </details>

.. raw:: html

   </details>


.. _make-sure-all-devices-are-present-1:

Make sure all devices are present
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **iio_info | grep iio:device**
              iio:device7: axi-adrv9009-tx-hpc (buffer capable)
              iio:device5: axi-adrv9009-rx-hpc (buffer capable)
              iio:device3: adrv9009-phy-c
              iio:device1: hmc7044-fmc
              iio:device6: axi-adrv9009-rx-obs-hpc (buffer capable)
              iio:device4: adrv9009-phy-d
              iio:device2: ad7291
              iio:device0: ams
   


Check clock chip lock status on FMCOMMS8
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>`
-  :doc:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **iio_attr -q -D hmc7044 status**
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN3 @ 19200000 Hz
      PFD:    3840 kHz
      --- PLL2 ---
      Status: Locked (Unsynchronized)
      Frequency:      2949120000 Hz (Autocal cap bank value: 14)
      SYSREF Status:  Valid & Locked
      SYNC Status:    Unsynchronized
      Lock Status:    PLL1 & PLL2 Locked
   


.. _synchronizing-the-adrv9009s-1:

Synchronizing the ADRV9009s
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>` the tranceivers should always be in a synchronized state.

.. _check-jesd204b-link-status-1:

Check JESD204B Link Status
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **TERM=vt100 jesd_status -s**
        (DEVICES) Found 3 JESD204 Link Layer peripherals
   
        (0): 85a30000.axi-jesd204-tx
        (1): 85a70000.axi-jesd204-rx
        (2): 85a50000.axi-jesd204-rx
   
        (STATUS)               (0)          (1)        (2)
        Link is                 enabled      enabled    enabled
        Link Status             DATA         DATA       DATA
        Measured Link Clock     122.891      122.893    245.782
        Reported Link Clock     122.880      122.880    245.760
        Lane rate               4915.200     4915.200   9830.400
        Lane rate / 40          122.880      122.880    245.760
        LMFC rate               7.680        3.840      7.680
        SYSREF captured         Yes          Yes        Yes
        SYSREF alignment error  No           No         No
        SYNC~                   deasserted
   
        (LANE STATUS)                   (1)                          (2)
        Lane#                             0      1      2      3       0      1      2      3
        Errors                            0      0      0      0       0      0      0      0
        Latency (Multiframes/Octets)      2/54   2/55   2/53   2/53    2/79   2/86   2/77   2/78
        CGS State                         DATA   DATA   DATA   DATA    DATA   DATA   DATA   DATA
        Initial Frame Sync                Yes    Yes    Yes    Yes     Yes    Yes    Yes    Yes
        Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes     Yes    Yes    Yes    Yes
   


Video Configuration
-------------------

| The default configuration for most of the projects is to use the HDMI output, but for this project the DisplayPort is used. In order for it to work, you should follow the steps described here: :doc:`DisplayPort No Picture </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`
| After following the steps, the board should be rebooted.

IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image1|

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
