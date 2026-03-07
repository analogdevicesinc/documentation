AD9081/AD9082 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide
=============================================================

|image1| This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the :adi:`AD9081-FMCA-EBZ`/:adi:`AD9082-FMCA-EBZ` on ZCU102

Instructions on how to build the ZynqMP / MPSoC Linux kernel and devicetrees from source can be found here:

-  :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`
-  :doc:`How to build the ZynqMP boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`

Required Software
-----------------

-  SD Card 16GB imaged using the instructions here: :doc:`Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/zynq_images>`. <fc #ff0000>Use the 2019_R2 or later.</fc>
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

-  Xilinx `ZCU102 <https://www.xilinx.com/ZCU102>`_ Rev 1.0 or later board
-  AD9081-FMCA-EBZ/AD9082-FMCA-EBZ FMC board.
-  Micro-USB cable
-  Ethernet cable
-  Optionally USB keyboard mouse and a Display Port compatible monitor

.. include:: ../ad9081_fmca_ebz_hdl.rst

Example Device Trees
--------------------

AD9081-FMCA-EBZ / AD9082-FMCA-EBZ / AD9988-FMCB-EBZ on ZCU102 (Zynq UltraScale+ MPSoC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                              |
+==========+===================================================================================================================================================================================================+
| dtsi     | :git-linux:`arch/arm64/boot/dts/xilinx/adi-ad9081-fmc-ebz.dtsi`                                                                                                                                   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4-qpllrx.dts`                                                                                                               |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4-vcxo122p88.dts`                                                                                                           |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4.dts`                                                                                                                      |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081.dts`                                                                                                                            |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9082-m4-l8.dts`                                                                                                                      |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-204b-txmode9-rxmode4.dts`                                                                                                       |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-204c-txmode0-rxmode1.dts`                                                                                                       |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`ynqmp-zcu102-rev10-ad9082-204c-txmode22-rxmode23.dts <arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9082-204c-txmode22-rxmode23.dts>`                                              |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9988-fmcb-m8-l4.dts`                                                                                                                 |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Testing
=======

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/zcu102.jpg
   :align: center
   :width: 900px

-  Connect the :adi:`AD9082-FMCA-EBZ` FMC board to the FPGA carrier **HPC0** FMC0 socket.
-  Connect USB UART J83 (Micro USB) to your host PC.
-  Insert SD card into socket.
-  Configure ZCU102 for SD BOOT (mode SW6[4:1] switch in the position **OFF,OFF,OFF,ON** as seen in the below picture).
-  Turn on the power switch on the FPGA board.
-  Observe kernel and serial console messages on your terminal. (use the first ttyUSB or COM port registered)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/zcu102_1p0_bootmode.jpg
   :align: center
   :width: 400px


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


SDcard boot files
-----------------

The files that need to be present on the sdcard ``BOOT`` partition are:

-  ``BOOT.BIN``
-  ``Image``
-  ``system.dtb``

| Copy the ``BOOT.BIN`` and ``system.dtb`` from the ``zynqmp-zcu102-rev10-ad9081-m8-l4`` directory.
| For evaluation boards populated with VXCO 100 MHz copy the device tree from ``vcxo100`` folder.
| For evaluation boards populated with VXCO 122.88 MHz copy the device tree from ``vcxo122p88`` folder.
| Copy the ``Image`` from the ``zynqmp-common`` directory.
|

.. important::

   On windows machines make sure the copy process did not encrypted the files.


Setting up UART
---------------

When setting up the UART make sure you connect to the Interface 0

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zcu102_uart.png
   :align: center
   :width: 600px

Boot messages
-------------

The **2019_R2** Image based boot messages looks like the followings :



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   

   .. raw:: html

      <details><summary>Boot log (click to expand)</summary>

   ::
   
   
      Xilinx Zynq MP First Stage Boot Loader 
      Release 2019.1   Feb 19 2021  -  15:58:23
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
      Name: SC32G 
      Tran Speed: 50000000
      Rd Block Len: 512
      SD version 3.0
      High Capacity: Yes
      Capacity: 29.7 GiB
      Bus Width: 4-bit
      Erase Group Size: 512 Bytes
      reading uEnv.txt
      407 bytes read in 16 ms (24.4 KiB/s)
      Loaded environment from uEnv.txt
      Importing environment from SD ...
      Running uenvcmd ...
      Copying Linux from SD to RAM...
      ** No boot file defined **
      reading system.dtb
      44731 bytes read in 24 ms (1.8 MiB/s)
      reading Image
      29737472 bytes read in 2000 ms (14.2 MiB/s)
      ## Flattened Device Tree blob at 04000000
         Booting using the fdt blob at 0x4000000
         Loading Device Tree to 000000000fff2000, end 000000000ffffeba ... OK
   
      Starting kernel ...
   
      [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
      [    0.000000] Linux version 4.19.0-ga6ef26d (jenkins@romlxbuild1.adlk.analog.com) (gcc version 8.2.0 (GCC)) #1105 SMP Fri Feb 19 16:51:27 GMT 2021
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
      [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1 root=/dev/mmcblk0p2 rw 
      rootwait
      [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
      [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
      [    0.000000] software IO TLB: mapped [mem 0x6bfff000-0x6ffff000] (64MB)
      [    0.000000] Memory: 3772348K/4194304K available (12796K kernel code, 1520K rwdata, 13828K rodata, 832K init, 326K bss, 159812K reserved, 262144K cma-reserved)
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
      [    0.008255] Console: colour dummy device 80x25
      [    0.012391] Calibrating delay loop (skipped), value calculated using timer frequency.. 199.98 BogoMIPS (lpj=399960)
      [    0.022756] pid_max: default: 32768 minimum: 301
      [    0.027449] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.034012] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.041794] ASID allocator initialised with 32768 entries
      [    0.046508] rcu: Hierarchical SRCU implementation.
      [    0.051548] EFI services will not be available.
      [    0.055828] smp: Bringing up secondary CPUs ...
      [    0.060485] Detected VIPT I-cache on CPU1
      [    0.060515] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [    0.060814] Detected VIPT I-cache on CPU2
      [    0.060834] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [    0.061114] Detected VIPT I-cache on CPU3
      [    0.061133] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [    0.061176] smp: Brought up 1 node, 4 CPUs
      [    0.095681] SMP: Total of 4 processors activated.
      [    0.100354] CPU features: detected: 32-bit EL0 Support
      [    0.106862] CPU: All CPU(s) started at EL2
      [    0.109534] alternatives: patching kernel code
      [    0.114847] devtmpfs: initialized
      [    0.122736] Registered cp15_barrier emulation handler
      [    0.122785] Registered setend emulation handler
      [    0.126847] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      [    0.136437] futex hash table entries: 1024 (order: 4, 65536 bytes)
      [    0.148125] xor: measuring software checksum speed
      [    0.186641]    8regs     :  2375.000 MB/sec
      [    0.226666]    8regs_prefetch:  2051.000 MB/sec
      [    0.266697]    32regs    :  2724.000 MB/sec
      [    0.306725]    32regs_prefetch:  2308.000 MB/sec
      [    0.306766] xor: using function: 32regs (2724.000 MB/sec)
      [    0.311069] pinctrl core: initialized pinctrl subsystem
      [    0.316855] NET: Registered protocol family 16
      [    0.321065] audit: initializing netlink subsys (disabled)
      [    0.326090] audit: type=2000 audit(0.272:1): state=initialized audit_enabled=0 res=1
      [    0.333728] vdso: 2 pages (1 code @ (____ptrval____), 1 data @ (____ptrval____))
      [    0.333733] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
      [    0.348492] DMA: preallocated 256 KiB pool for atomic allocations
      [    0.367721] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
      [    0.436460] raid6: int64x1  gen()   445 MB/s
      [    0.504424] raid6: int64x1  xor()   451 MB/s
      [    0.572515] raid6: int64x2  gen()   679 MB/s
      [    0.640548] raid6: int64x2  xor()   600 MB/s
      [    0.708557] raid6: int64x4  gen()   980 MB/s
      [    0.776599] raid6: int64x4  xor()   737 MB/s
      [    0.844679] raid6: int64x8  gen()  1162 MB/s
      [    0.912701] raid6: int64x8  xor()   759 MB/s
      [    0.980756] raid6: neonx1   gen()   736 MB/s
      [    1.048776] raid6: neonx1   xor()   880 MB/s
      [    1.116859] raid6: neonx2   gen()  1129 MB/s
      [    1.184865] raid6: neonx2   xor()  1173 MB/s
      [    1.252949] raid6: neonx4   gen()  1480 MB/s
      [    1.320970] raid6: neonx4   xor()  1418 MB/s
      [    1.389006] raid6: neonx8   gen()  1550 MB/s
      [    1.457058] raid6: neonx8   xor()  1459 MB/s
      [    1.457096] raid6: using algorithm neonx8 gen() 1550 MB/s
      [    1.461056] raid6: .... xor() 1459 MB/s, rmw enabled
      [    1.465986] raid6: using neon recovery algorithm
      [    1.471291] SCSI subsystem initialized
      [    1.474463] usbcore: registered new interface driver usbfs
      [    1.479776] usbcore: registered new interface driver hub
      [    1.485050] usbcore: registered new device driver usb
      [    1.490203] media: Linux media interface: v0.10
      [    1.494556] videodev: Linux video capture interface: v2.00
      [    1.500037] pps_core: LinuxPPS API ver. 1 registered
      [    1.504917] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    1.514010] PTP clock support registered
      [    1.517908] EDAC MC: Ver: 3.0.0
      [    1.521385] zynqmp-ipi-mbox mailbox@ff990400: Probed ZynqMP IPI Mailbox driver.
      [    1.528760] jesd204: created con: id=0, topo=0, link=0, /amba/spi@ff050000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-tx@84b60000
      [    1.539355] jesd204: created con: id=1, topo=0, link=2, /amba/spi@ff050000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-rx@84a60000
      [    1.550427] jesd204: created con: id=2, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@84b60000 <-> /fpga-axi@0/axi-jesd204-tx@84b90000
      [    1.562104] jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx@84a60000 <-> /fpga-axi@0/axi-jesd204-rx@84a90000
      [    1.573782] jesd204: created con: id=4, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@84b90000 <-> /fpga-axi@0/axi-ad9081-tx-hpc@84b10000
      [    1.585807] jesd204: created con: id=5, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@84a90000 <-> /fpga-axi@0/axi-ad9081-rx-hpc@84a10000
      [    1.597833] jesd204: created con: id=6, topo=0, link=2, /fpga-axi@0/axi-ad9081-rx-hpc@84a10000 <-> /amba/spi@ff040000/ad9081@0
      [    1.609167] jesd204: created con: id=7, topo=0, link=0, /fpga-axi@0/axi-ad9081-tx-hpc@84b10000 <-> /amba/spi@ff040000/ad9081@0
      [    1.620504] jesd204: /amba/spi@ff040000/ad9081@0: JESD204[2] transition uninitialized -> initialized
      [    1.629577] jesd204: /amba/spi@ff040000/ad9081@0: JESD204[0] transition uninitialized -> initialized
      [    1.638658] jesd204: found 8 devices and 1 topologies
      [    1.643706] FPGA manager framework
      [    1.647220] Advanced Linux Sound Architecture Driver Initialized.
      [    1.653380] Bluetooth: Core ver 2.22
      [    1.656666] NET: Registered protocol family 31
      [    1.661065] Bluetooth: HCI device and connection manager initialized
      [    1.667382] Bluetooth: HCI socket layer initialized
      [    1.672225] Bluetooth: L2CAP socket layer initialized
      [    1.677258] Bluetooth: SCO socket layer initialized
      [    1.682620] clocksource: Switched to clocksource arch_sys_counter
      [    1.688238] VFS: Disk quotas dquot_6.6.0
      [    1.692077] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
      [    1.703496] NET: Registered protocol family 2
      [    1.703884] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes)
      [    1.711025] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
      [    1.718360] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
      [    1.725133] TCP: Hash tables configured (established 32768 bind 32768)
      [    1.731285] UDP hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.737263] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.743750] NET: Registered protocol family 1
      [    1.748136] RPC: Registered named UNIX socket transport module.
      [    1.753814] RPC: Registered udp transport module.
      [    1.758473] RPC: Registered tcp transport module.
      [    1.763146] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    1.770312] hw perfevents: no interrupt-affinity property for /pmu, guessing.
      [    1.776794] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
      [    1.785179] Initialise system trusted keyrings
      [    1.788825] workingset: timestamp_bits=62 max_order=20 bucket_order=0
      [    1.795858] NFS: Registering the id_resolver key type
      [    1.800184] Key type id_resolver registered
      [    1.804323] Key type id_legacy registered
      [    1.808307] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    1.814975] jffs2: version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.
      [    2.903619] NET: Registered protocol family 38
      [    2.964582] Key type asymmetric registered
      [    2.964620] Asymmetric key parser 'x509' registered
      [    2.967916] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
      [    2.975239] io scheduler noop registered
      [    2.979129] io scheduler deadline registered
      [    2.983387] io scheduler cfq registered (default)
      [    2.988040] io scheduler mq-deadline registered
      [    2.992537] io scheduler kyber registered
      [    3.024197] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      [    3.028267] cacheinfo: Unable to detect cache hierarchy for CPU 0
      [    3.035571] brd: module loaded
      [    3.039411] loop: module loaded
      [    3.039622] Registered mathworks_ip class
      [    3.041890] mtdoops: mtd device (mtddev=name/number) must be supplied
      [    3.048941] libphy: Fixed MDIO Bus: probed
      [    3.052744] tun: Universal TUN/TAP device driver, 1.6
      [    3.056689] CAN device driver interface
      [    3.061300] usbcore: registered new interface driver asix
      [    3.065785] usbcore: registered new interface driver ax88179_178a
      [    3.071820] usbcore: registered new interface driver cdc_ether
      [    3.077615] usbcore: registered new interface driver net1080
      [    3.083240] usbcore: registered new interface driver cdc_subset
      [    3.089120] usbcore: registered new interface driver zaurus
      [    3.094666] usbcore: registered new interface driver cdc_ncm
      [    3.100944] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    3.106748] ehci-pci: EHCI PCI platform driver
      [    3.111413] usbcore: registered new interface driver uas
      [    3.116466] usbcore: registered new interface driver usb-storage
      [    3.122459] usbcore: registered new interface driver usbserial_generic
      [    3.128910] usbserial: USB Serial support registered for generic
      [    3.134882] usbcore: registered new interface driver ftdi_sio
      [    3.140589] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    3.147857] usbcore: registered new interface driver upd78f0730
      [    3.153736] usbserial: USB Serial support registered for upd78f0730
      [    3.161301] rtc_zynqmp ffa60000.rtc: rtc core: registered ffa60000.rtc as rtc0
      [    3.167191] i2c /dev entries driver
      [    3.172562] usbcore: registered new interface driver uvcvideo
      [    3.176302] USB Video Class driver (1.1.1)
      [    3.181738] Bluetooth: HCI UART driver ver 2.3
      [    3.184784] Bluetooth: HCI UART protocol H4 registered
      [    3.189881] Bluetooth: HCI UART protocol BCSP registered
      [    3.195179] Bluetooth: HCI UART protocol LL registered
      [    3.200262] Bluetooth: HCI UART protocol ATH3K registered
      [    3.205642] Bluetooth: HCI UART protocol Three-wire (H5) registered
      [    3.211894] Bluetooth: HCI UART protocol Intel registered
      [    3.217236] Bluetooth: HCI UART protocol QCA registered
      [    3.222446] usbcore: registered new interface driver bcm203x
      [    3.228057] usbcore: registered new interface driver bpa10x
      [    3.233593] usbcore: registered new interface driver bfusb
      [    3.239046] usbcore: registered new interface driver btusb
      [    3.244468] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
      [    3.250134] usbcore: registered new interface driver ath3k
      [    3.255665] EDAC MC: ECC not enabled
      [    3.259365] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
      [    3.271530] CPUidle arm: Failed to register cpuidle driver
      [    3.276816] sdhci: Secure Digital Host Controller Interface driver
      [    3.282791] sdhci: Copyright(c) Pierre Ossman
      [    3.287115] sdhci-pltfm: SDHCI platform and OF driver helper
      [    3.293118] ledtrig-cpu: registered to indicate activity on CPUs
      [    3.298752] zynqmp_firmware_probe Platform Management API v1.1
      [    3.304507] zynqmp_firmware_probe Trustzone version v1.0
      [    3.312598] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
      [    3.339995] zynqmp_clk_mux_get_parent() getparent failed for clock: lpd_wdt, ret = -22
      [    3.342694] alg: No test for xilinx-zynqmp-aes (zynqmp-aes)
      [    3.347809] zynqmp_aes zynqmp_aes: AES Successfully Registered
      [    3.347809] 
      [    3.355326] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
      [    3.361554] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
      [    3.367047] usbcore: registered new interface driver usbhid
      [    3.372366] usbhid: USB HID core driver
      [    3.383901] axi_sysid 85000000.axi-sysid-0: [ad9081_fmca_ebz] on [zcu102] git <7c86b9f84f75d6eaad0ef29a31e74b6f6f37c447> clean [2021-02-15 23:49:25] UTC
      [    3.392227] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
      [    3.398822] usbcore: registered new interface driver snd-usb-audio
      [    3.406188] pktgen: Packet Generator for packet performance testing. Version: 2.75
      [    3.412338] Initializing XFRM netlink socket
      [    3.416261] NET: Registered protocol family 10
      [    3.420966] Segment Routing with IPv6
      [    3.424320] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    3.430457] NET: Registered protocol family 17
      [    3.434536] NET: Registered protocol family 15
      [    3.438952] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
      [    3.452044] can: controller area network core (rev 20170425 abi 9)
      [    3.457998] NET: Registered protocol family 29
      [    3.462384] can: raw protocol (rev 20170425)
      [    3.466621] can: broadcast manager protocol (rev 20170425 t)
      [    3.472247] can: netlink gateway (rev 20170425) max_hops=1
      [    3.477965] Bluetooth: RFCOMM TTY layer initialized
      [    3.482546] Bluetooth: RFCOMM socket layer initialized
      [    3.487654] Bluetooth: RFCOMM ver 1.11
      [    3.491367] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
      [    3.496639] Bluetooth: BNEP filters: protocol multicast
      [    3.501831] Bluetooth: BNEP socket layer initialized
      [    3.506761] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
      [    3.512645] Bluetooth: HIDP socket layer initialized
      [    3.517685] 9pnet: Installing 9P2000 support
      [    3.521822] NET: Registered protocol family 36
      [    3.526238] Key type dns_resolver registered
      [    3.530999] registered taskstats version 1
      [    3.534525] Loading compiled-in X.509 certificates
      [    3.539629] Btrfs loaded, crc32c=crc32c-generic
      [    3.550250] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 41, base_baud = 6249999) is a xuartps
      [    3.559638] console [ttyPS0] enabled
      [    3.559638] console [ttyPS0] enabled
      [    3.563238] bootconsole [cdns0] disabled
      [    3.563238] bootconsole [cdns0] disabled
      [    3.571303] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 42, base_baud = 6249999) is a xuartps
      [    3.584662] of-fpga-region fpga-full: FPGA Region probed
      [    3.590786] nwl-pcie fd0e0000.pcie: Link is DOWN
      [    3.595430] nwl-pcie fd0e0000.pcie: host bridge /amba/pcie@fd0e0000 ranges:
      [    3.602400] nwl-pcie fd0e0000.pcie:   MEM 0xe0000000..0xefffffff -> 0xe0000000
      [    3.609622] nwl-pcie fd0e0000.pcie:   MEM 0x600000000..0x7ffffffff -> 0x600000000
      [    3.617203] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
      [    3.623380] pci_bus 0000:00: root bus resource [bus 00-ff]
      [    3.628863] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
      [    3.635732] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
      [    3.647664] pci 0000:00:00.0: PCI bridge to [bus 01-0c]
      [    3.653802] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
      [    3.660381] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
      [    3.667483] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
      [    3.674585] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
      [    3.681683] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
      [    3.688789] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
      [    3.695893] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
      [    3.702994] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
      [    3.710096] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
      [    3.717341] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:8 protocol:4 pll_locked:yes
      [    3.728810] zynqmp_clk_divider_set_rate() set divider failed for spi1_ref_div1, ret = -13
      [    3.737497] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
      [    3.748264] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
      [    3.756343] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
      [    3.764844] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
      [    3.777288] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
      [    3.789963] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
      [    3.800141] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
      [    3.807107] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
      [    3.813716] [drm] No driver support for vblank timestamp query.
      [    3.819699] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffff8008dc2e70)
      [    4.906629] [drm] Cannot find any crtc or sizes
      [    4.911375] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
      [    4.919475] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
      [    4.928469] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:3 protocol:2 pll_locked:yes
      [    4.946413] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
      [    4.955374] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst 
      [    4.965786] scsi host0: ahci-ceva
      [    4.969342] scsi host1: ahci-ceva
      [    4.972799] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 37
      [    4.980710] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 37
      [    5.039829] jesd204: /amba/spi@ff050000/hmc7044@0,jesd204:1,parent=spi2.0: Using as SYSREF provider
      [    5.049613] m25p80 spi0.0: SPI-NOR-UniqueID 1044000ad9040001f6ff0f009e90a67dfd
      [    5.056835] m25p80 spi0.0: found n25q512a, expected m25p80
      [    5.062534] m25p80 spi0.0: n25q512a (131072 Kbytes)
      [    5.067427] 4 fixed-partitions partitions found on MTD device spi0.0
      [    5.073774] Creating 4 MTD partitions on "spi0.0":
      [    5.078559] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
      [    5.084753] 0x000000100000-0x000000600000 : "qspi-linux"
      [    5.090451] 0x000000600000-0x000000620000 : "qspi-device-tree"
      [    5.096678] 0x000000620000-0x000000c00000 : "qspi-rootfs"
      [    5.104544] macb ff0e0000.ethernet: Not enabling partial store and forward
      [    5.111908] libphy: MACB_mii_bus: probed
      [    5.115903] mdio_bus ff0e0000.ethernet-ffffffff: MDIO device at address 21 is missing.
      [    5.126076] TI DP83867 ff0e0000.ethernet-ffffffff:0c: attached PHY driver [TI DP83867] (mii_bus:phy_addr=ff0e0000.ethernet-ffffffff:0c, irq=POLL)
      [    5.139117] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 22 (00:0a:35:07:26:39)
      [    5.149227] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
      [    5.155754] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
      [    5.162237] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
      [    5.168720] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
      [    5.176674] dwc3 fe200000.dwc3: Failed to get clk 'ref': -2
      [    5.182527] xilinx-psgtr fd400000.zynqmp_phy: Lane:2 type:0 protocol:3 pll_locked:yes
      [    5.190909] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
      [    5.196407] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
      [    5.204406] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000202010810
      [    5.213817] xhci-hcd xhci-hcd.0.auto: irq 51, io mem 0xfe200000
      [    5.219940] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
      [    5.228203] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    5.235422] usb usb1: Product: xHCI Host Controller
      [    5.240290] usb usb1: Manufacturer: Linux 4.19.0-ga6ef26d xhci-hcd
      [    5.246462] usb usb1: SerialNumber: xhci-hcd.0.auto
      [    5.251612] hub 1-0:1.0: USB hub found
      [    5.255375] hub 1-0:1.0: 1 port detected
      [    5.259480] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
      [    5.264973] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
      [    5.272626] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0  SuperSpeed
      [    5.279352] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 4.19
      [    5.287614] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    5.294833] usb usb2: Product: xHCI Host Controller
      [    5.299702] usb usb2: Manufacturer: Linux 4.19.0-ga6ef26d xhci-hcd
      [    5.300811] ata1: SATA link down (SStatus 0 SControl 330)
      [    5.305874] usb usb2: SerialNumber: xhci-hcd.0.auto
      [    5.306113] hub 2-0:1.0: USB hub found
      [    5.311293] ata2: SATA link down (SStatus 0 SControl 330)
      [    5.316171] hub 2-0:1.0: 1 port detected
      [    5.330409] pca953x 0-0020: 0-0020 supply vcc not found, using dummy regulator
      [    5.337665] pca953x 0-0020: Linked as a consumer to regulator.0
      [    5.344455] GPIO line 496 (sel0) hogged as output/low
      [    5.349834] GPIO line 497 (sel1) hogged as output/high
      [    5.355300] GPIO line 498 (sel2) hogged as output/high
      [    5.360765] GPIO line 499 (sel3) hogged as output/high
      [    5.366112] pca953x 0-0021: 0-0021 supply vcc not found, using dummy regulator
      [    5.373354] pca953x 0-0021: Linked as a consumer to regulator.0
      [    5.380763] ina2xx 3-0040: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.387580] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.394384] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.401192] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.408001] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.414808] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.421623] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.428431] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.435240] ina2xx 3-004a: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.442056] ina2xx 3-004b: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.448469] i2c i2c-0: Added multiplexed i2c bus 3
      [    5.453935] ina2xx 4-0040: power monitor ina226 (Rshunt = 2000 uOhm)
      [    5.460744] ina2xx 4-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.467547] ina2xx 4-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.474367] ina2xx 4-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.481181] ina2xx 4-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.487994] ina2xx 4-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.494816] ina2xx 4-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.501622] ina2xx 4-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.508017] i2c i2c-0: Added multiplexed i2c bus 4
      [    5.516615] random: fast init done
      [    5.550092] i2c i2c-0: Added multiplexed i2c bus 5
      [    5.555052] i2c i2c-0: Added multiplexed i2c bus 6
      [    5.559839] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
      [    5.567190] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 24
      [    5.574995] at24 7-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
      [    5.581742] i2c i2c-1: Added multiplexed i2c bus 7
      [    5.586868] i2c i2c-1: Added multiplexed i2c bus 8
      [    5.593772] si570 9-005d: registered, current frequency 300000000 Hz
      [    5.600174] i2c i2c-1: Added multiplexed i2c bus 9
      [    5.619008] si570 10-005d: registered, current frequency 148500000 Hz
      [    5.625495] i2c i2c-1: Added multiplexed i2c bus 10
      [    5.630593] si5324 11-0069: si5328 probed
      [    5.694709] si5324 11-0069: si5328 probe successful
      [    5.699631] i2c i2c-1: Added multiplexed i2c bus 11
      [    5.704679] i2c i2c-1: Added multiplexed i2c bus 12
      [    5.709716] i2c i2c-1: Added multiplexed i2c bus 13
      [    5.714769] i2c i2c-1: Added multiplexed i2c bus 14
      [    5.719646] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
      [    5.727932] at24 15-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      [    5.734677] i2c i2c-1: Added multiplexed i2c bus 15
      [    5.739725] i2c i2c-1: Added multiplexed i2c bus 16
      [    5.744770] i2c i2c-1: Added multiplexed i2c bus 17
      [    5.749819] i2c i2c-1: Added multiplexed i2c bus 18
      [    5.754868] i2c i2c-1: Added multiplexed i2c bus 19
      [    5.759911] i2c i2c-1: Added multiplexed i2c bus 20
      [    5.764953] i2c i2c-1: Added multiplexed i2c bus 21
      [    5.770001] i2c i2c-1: Added multiplexed i2c bus 22
      [    5.774882] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
      [    5.782491] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 25
      [    5.788864] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
      [    5.828893] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
      [    5.845173] axi_adxcvr 84a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.01.a) using CPLL on GTH4 at 0x84A60000. Number of lanes: 4.
      [    5.857108] axi_adxcvr 84b60000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.01.a) using QPLL on GTH4 at 0x84B60000. Number of lanes: 4.
      [    5.951002] mmc0: new ultra high speed SDR104 SDHC card at address aaaa
      [    5.958116] mmcblk0: mmc0:aaaa SC32G 29.7 GiB 
      [    5.966523]  mmcblk0: p1 p2 p3
      [    6.038634] [drm] Cannot find any crtc or sizes
      [    6.682135] ad9081 spi1.0: AD9081 Rev. 3 Grade 10 (API 1.0.6) probed
      [    6.710789] cf_axi_adc 84a10000.axi-ad9081-rx-hpc: ADI AIM (10.01.b) at 0x84A10000 mapped to 0x(____ptrval____), probed ADC AD9081 as MASTER
      [    6.743436] cf_axi_dds 84b10000.axi-ad9081-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84B10000 mapped to 0x(____ptrval____), probed DDS AD9081
      [    6.757628] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition initialized -> probed
      [    6.768231] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition initialized -> probed
      [    6.778837] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition probed -> idle
      [    6.788830] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition probed -> idle
      [    6.798825] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition idle -> device_init
      [    6.809255] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition idle -> device_init
      [    6.819686] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition device_init -> link_init
      [    6.830549] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition device_init -> link_init
      [    6.841421] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_init -> link_supported
      [    6.852547] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_init -> link_supported
      [    6.863766] hmc7044 spi2.0: hmc7044_jesd204_link_pre_setup: Link2 forcing continuous SYSREF mode
      [    6.872686] hmc7044 spi2.0: hmc7044_jesd204_link_pre_setup: Link0 forcing continuous SYSREF mode
      [    6.881514] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_supported -> link_pre_setup
      [    6.893071] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_supported -> link_pre_setup
      [    6.904644] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_pre_setup -> clk_sync_stage1
      [    6.916290] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_pre_setup -> clk_sync_stage1
      [    6.927935] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.939669] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.951401] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.963132] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.975886] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition clk_sync_stage3 -> link_setup
      [    6.987180] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition clk_sync_stage3 -> link_setup
      [    7.003833] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_setup -> opt_setup_stage1
      [    7.015222] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_setup -> opt_setup_stage1
      [    7.031631] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage1 -> opt_setup_stage2
      [    7.043540] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage1 -> opt_setup_stage2
      [    7.055540] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage2 -> opt_setup_stage3
      [    7.067445] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage2 -> opt_setup_stage3
      [    7.079358] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage3 -> opt_setup_stage4
      [    7.091263] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage3 -> opt_setup_stage4
      [    7.103170] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage4 -> opt_setup_stage5
      [    7.115075] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage4 -> opt_setup_stage5
      [    7.128071] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage5 -> clocks_enable
      [    7.139722] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage5 -> clocks_enable
      [    7.151421] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition clocks_enable -> link_enable
      [    7.162632] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition clocks_enable -> link_enable
      [    7.174069] ad9081 spi1.0: JESD RX (JTX) Link2 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
      [    7.184652] ad9081 spi1.0: JESD TX (JRX) Link0 0xF lanes in DATA
      [    7.190662] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_enable -> link_running
      [    7.201788] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_enable -> link_running
      [    7.212914] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_running -> opt_post_running_stage
      [    7.224992] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_running -> opt_post_running_stage
      [    7.239566] input: gpio-keys as /devices/platform/gpio-keys/input/input0
      [    7.246550] rtc_zynqmp ffa60000.rtc: setting system clock to 2018-11-14 18:30:57 UTC (1542220257)
      [    7.255424] of_cfs_init
      [    7.257871] of_cfs_init: OK
      [    7.260796] cfg80211: Loading compiled-in X.509 certificates for regulatory database
      [    7.399733] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
      [    7.406260] clk: Not disabling unused clocks
      [    7.410526] ALSA device list:
      [    7.413484]   #0: DisplayPort monitor
      [    7.417510] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
      [    7.426120] cfg80211: failed to load regulatory.db
      [    7.440104] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [    7.448203] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    7.459066] devtmpfs: mounted
      [    7.462199] Freeing unused kernel memory: 832K
      [    7.482646] Run /sbin/init as init process
      [    7.712777] systemd[1]: System time before build time, advancing clock.
      [    7.734730] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +S
      ECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
      [    7.756467] systemd[1]: Detected architecture arm64.
   
      Welcome to Kuiper GNU/Linux 10 (buster)!
   
      [    7.781175] systemd[1]: Set hostname to <analog>.
      [    7.925008] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/c
      group based firewalling.
      [    7.942166] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
      [    8.063665] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
      [    8.073365] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
      [    8.225124] random: systemd: uninitialized urandom read (16 bytes read)
      [    8.237991] random: systemd: uninitialized urandom read (16 bytes read)
      [    8.245182] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [    8.266718] random: systemd: uninitialized urandom read (16 bytes read)
      [    8.273358] systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      [    8.286958] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Control Socket.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [  OK  ] Started Forward Password R�…uests to Wall Directory Watch.
      [  OK  ] Created slice system-getty.slice.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on Syslog Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on Journal Audit Socket.
      [  OK  ] Created slice User and Session Slice.
      [  OK  ] Reached target Slices.
      [  OK  ] Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket.
               Mounting Kernel Debug File System...
               Starting udev Coldplug all Devices...
               Starting Restore / save the current clock...
               Mounting POSIX Message Queue File System...
               Mounting RPC Pipe File System...
               Mounting Huge Pages File System...
               Starting Set the console keyboard layout...
               Starting Journal Service...
               Starting Load Kernel Modules...
      [  OK  ] Mounted Kernel Debug File System.
      [  OK  ] Started Restore / save the current clock.
      [  OK  ] Mounted POSIX Message Queue File System.
      [  OK  ] Mounted RPC Pipe File System.
      [  OK  ] Mounted Huge Pages File System.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
               Starting Apply Kernel Variables...
               Mounting Kernel Configuration File System...
               Starting Remount Root and Kernel File Systems...
      [  OK  ] Started Journal Service.
      [  OK  ] Started Apply Kernel Variables.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Started Set the console keyboard layout.
      [  OK  ] Started Remount Root and Kernel File Systems.
               Starting Flush Journal to Persistent Storage...
               Starting Create System Users...
               Starting Load/Save Random Seed...
      [  OK  ] Started Create System Users.
      [  OK  ] Started Flush Journal to Persistent Storage.
      [  OK  ] Started udev Coldplug all Devices.
      [  OK  ] Started Load/Save Random Seed.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Create Static Device Nodes in /dev...
      [  OK  ] Started Helper to synchronize boot up for ifupdown.
      [  OK  ] Started Create Static Device Nodes in /dev.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting udev Kernel Device Manager...
      [  OK  ] Started udev Kernel Device Manager.
               Starting Show Plymouth Boot Screen...
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Started Forward Password R�…s to Plymouth Directory Watch.
      [  OK  ] Found device /dev/ttyPS0.
               Starting Load Kernel Modules...
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Found device /dev/disk/by-partuuid/18f1f9d5-01.
               Starting File System Check�…isk/by-partuuid/18f1f9d5-01...
      [  OK  ] Started File System Check Daemon to report status.
      [  OK  ] Found device /dev/ttyS0.
      [  OK  ] Listening on Load/Save RF �…itch Status /dev/rfkill Watch.
      [  OK  ] Started File System Check �…/disk/by-partuuid/18f1f9d5-01.
               Mounting /boot...
      [  OK  ] Mounted /boot.
      [  OK  ] Reached target Local File Systems.
               Starting Set console font and keymap...
               Starting Tell Plymouth To Write Out Runtime Data...
               Starting Preprocess NFS configuration...
               Starting Raise network interfaces...
               Starting Create Volatile Files and Directories...
      [  OK  ] Started Set console font and keymap.
      [  OK  ] Started Preprocess NFS configuration.
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
      [  OK  ] Started Create Volatile Files and Directories.
               Starting Update UTMP about System Boot/Shutdown...
               Starting Network Time Synchronization...
      [  OK  ] Started Update UTMP about System Boot/Shutdown.
               Starting Load Kernel Modules...
               Starting Tell Plymouth To Write Out Runtime Data...
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Started Raise network interfaces.
      [  OK  ] Started Network Time Synchronization.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on GPS (Global P�…ioning System) Daemon Sockets.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Reached target Paths.
      [  OK  ] Listening on CUPS Scheduler.
      [  OK  ] Reached target Sockets.
      [  OK  ] Reached target Basic System.
      [  OK  ] Started D-Bus System Message Bus.
               Starting triggerhappy global hotkey daemon...
      [  OK  ] Started Manage Sound Card State (restore and store).
               Starting rng-tools.service...
               Starting WPA supplicant...
               Starting Modem Manager...
      [  OK  ] Started CUPS Scheduler.
               Starting Save/Restore Sound Card State...
               Starting Avahi mDNS/DNS-SD Stack...
      [  OK  ] Started Regular background program processing daemon.
               Starting dhcpcd on all interfaces...
               Starting dphys-swapfile - �…unt, and delete a swap file...
               Starting LSB: Switch to on�…nless shift key is pressed)...
               Starting System Logging Service...
               Starting Login Service...
               Starting Disk Manager...
      [  OK  ] Started tof-server.service.
               Starting Check for Raspberry Pi EEPROM updates...
      [  OK  ] Reached target System Time Synchronized.
      [  OK  ] Started Daily apt download activities.
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Started Daily rotation of log files.
      [  OK  ] Started Daily man-db regeneration.
      [  OK  ] Reached target Timers.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [FAILED] Failed to start rng-tools.service.
      See 'systemctl status rng-tools.service' for details.
      [  OK  ] Started Save/Restore Sound Card State.
      [  OK  ] Reached target Sound Card.
      [  OK  ] Started Login Service.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started dhcpcd on all interfaces.
      [FAILED] Failed to start Check for Raspberry Pi EEPROM updates.
      See 'systemctl status rpi-eeprom-update.service' for details.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started dphys-swapfile - s�…mount, and delete a swap file.
               Starting Authorization Manager...
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Reached target Network.
               Starting OpenBSD Secure Shell server...
      [  OK  ] Started IIO Daemon.
               Starting /etc/rc.local Compatibility...
               Starting Permit User Sessions...
               Starting HTTP based time synchronization tool...
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started Permit User Sessions.
               Starting Hold until boot process finishes up...
               Starting Light Display Manager...
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started OpenBSD Secure Shell server.
      [  OK  ] Started Authorization Manager.
   
      Raspbian GNU/Linux 10 analog ttyPS0
   
      analog login: root (automatic login)
   
      Last login: Wed Feb 24 01:09:27 GMT 2021 on ttyPS0
      Linux analog 4.19.0-ga6ef26d #1105 SMP Fri Feb 19 16:51:27 GMT 2021 aarch64
   
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


Login Information

-  user: analog
-  password: analog

The following devices should be present:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# iio_info | grep iio:device
              iio:device0: ams
              iio:device1: hmc7044
              iio:device2: axi-ad9081-rx-hpc (buffer capable)
              iio:device3: axi-ad9081-tx-hpc (buffer capable)
   


AD9988-FMCB-EBZ Testing
-----------------------

Checking clocking and lock status

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **iio_attr -D hmc7044 status**
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN0 @ 122880000 Hz
      PFD:    7680 kHz
      --- PLL2 ---
      Status: Locked (Synchronized)
      Frequency:      2949120000 Hz (Autocal cap bank value: 14)
      SYSREF Status:  Valid & Locked
      SYNC Status:    Synchronized
      Lock Status:    PLL1 & PLL2 Locked
      root@analog:~# 
   


Using the :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>` make sure all links are in DATA without SYSREF allignment errors.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
        (DEVICES) Found 2 JESD204 Link Layer peripherals
   
        (0): axi-jesd204-rx/84a90000.axi-jesd204-rx  [*]
        (1): axi-jesd204-tx/84b90000.axi-jesd204-tx
   
        (STATUS)
        Link is                      enabled
        Link Status                  DATA
        Measured Link Clock (MHz)    245.779
        Reported Link Clock (MHz)    245.760
        Measured Device Clock (MHz)  245.779
        Reported Device Clock (MHz)  245.760
        Desired Device Clock (MHz)   245.760
        Lane rate (MHz)              9830.400
        Lane rate / 40 (MHz)         245.760
        LMFC rate (MHz)              7.680
        SYSREF captured              Yes
        SYSREF alignment error       No
        SYNC~
   
   
        (LANE STATUS)
        Lane#                             0      1      2      3
        Errors                            0      0      0      0
        Latency (Multiframes/Octets)      1/19   1/19   1/18   1/19
        CGS State                         DATA   DATA   DATA   DATA
        Initial Frame Sync                Yes    Yes    Yes    Yes
        Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes
   


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
        (DEVICES) Found 2 JESD204 Link Layer peripherals
   
        (0): axi-jesd204-rx/84a90000.axi-jesd204-rx
        (1): axi-jesd204-tx/84b90000.axi-jesd204-tx  [*]
   
        (STATUS)
        Link is                      enabled
        Link Status                  DATA
        Measured Link Clock (MHz)    245.779
        Reported Link Clock (MHz)    245.760
        Measured Device Clock (MHz)  245.779
        Reported Device Clock (MHz)  245.760
        Desired Device Clock (MHz)   245.760
        Lane rate (MHz)              9830.400
        Lane rate / 40 (MHz)         245.760
        LMFC rate (MHz)              7.680
        SYSREF captured              Yes
        SYSREF alignment error       No
        SYNC~                        deasserted
   


Read status information from the MxFE

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **iio_attr -D axi-ad9081-rx-hpc status**
      JESD TX (JRX) Link1 0xF lanes in DATA
      JESD TX (JRX) Link1 TPL Phase Difference Read 1, Set 3
      JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
      root@analog:~# 
   


These are the relevant kernel messages which should be present

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   

   .. raw:: html

      <details><summary>Boot log (click to expand)</summary>

   ::
   
      [    2.467939] jesd204: created con: id=0, topo=0, link=0, /axi/spi@ff050000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-tx@84b60000
      [    2.478527] jesd204: created con: id=1, topo=0, link=2, /axi/spi@ff050000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-rx@84a60000
      [    2.489512] jesd204: created con: id=2, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@84b60000 <-> /fpga-axi@0/axi-jesd204-tx@84b90000
      [    2.501187] jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx@84a60000 <-> /fpga-axi@0/axi-jesd204-rx@84a90000
      [    2.512886] jesd204: created con: id=4, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@84b90000 <-> /fpga-axi@0/axi-ad9081-tx-hpc@84b10000
      [    2.524893] jesd204: created con: id=5, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@84a90000 <-> /fpga-axi@0/axi-ad9081-rx-hpc@84a10000
      [    2.536934] jesd204: created con: id=6, topo=0, link=2, /fpga-axi@0/axi-ad9081-rx-hpc@84a10000 <-> /axi/spi@ff040000/ad9988@0
      [    2.548157] jesd204: created con: id=7, topo=0, link=0, /fpga-axi@0/axi-ad9081-tx-hpc@84b10000 <-> /axi/spi@ff040000/ad9988@0
      [    2.559407] jesd204: /axi/spi@ff040000/ad9988@0: JESD204[2] transition uninitialized -> initialized
      [    2.568392] jesd204: /axi/spi@ff040000/ad9988@0: JESD204[0] transition uninitialized -> initialized
      [    2.577384] jesd204: found 8 devices and 1 topologies
   
      [    3.697779] hmc7044 spi2.0: PLL1: Locked, CLKIN0 @ 122880000 Hz, PFD: 7680 kHz - PLL2: Locked @ 2949.120000 MHz
      [    3.708225] jesd204: /axi/spi@ff050000/hmc7044@0,jesd204:1,parent=spi2.0: Using as SYSREF provider
   
      [    4.336180] axi_adxcvr 84a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.05.a) using CPLL on GTH4 at 0x84A60000. Number of lanes: 4.
      [    4.348316] axi_adxcvr 84b60000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.05.a) using QPLL on GTH4 at 0x84B60000. Number of lanes: 4.
      [    4.359953] axi-jesd204-rx 84a90000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x84A90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
      [    4.372796] axi-jesd204-tx 84b90000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0x84B90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
   
      [    6.274158] ad9081 spi1.0: AD9988 Rev. 3 Grade 10 (API 1.2.0) probed
      [    6.306717] cf_axi_adc 84a10000.axi-ad9081-rx-hpc: ADI AIM (10.01.b) at 0x84A10000 mapped to 0x(____ptrval____), probed ADC AD9081 as MASTER
      [    6.337977] cf_axi_dds 84b10000.axi-ad9081-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84B10000 mapped to 0x(____ptrval____), probed DDS AD9081
      [    6.352184] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition initialized -> probed
      [    6.362702] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition initialized -> probed
      [    6.373230] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition probed -> idle
      [    6.383143] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition probed -> idle
      [    6.393059] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition idle -> device_init
      [    6.403401] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition idle -> device_init
      [    6.413753] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition device_init -> link_init
      [    6.424528] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition device_init -> link_init
      [    6.435319] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_init -> link_supported
      [    6.446357] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_init -> link_supported
      [    6.457508] hmc7044 spi2.0: hmc7044_jesd204_link_pre_setup: Link2 forcing continuous SYSREF mode
      [    6.466488] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_supported -> link_pre_setup
      [    6.477965] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_supported -> link_pre_setup
      [    6.501763] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_pre_setup -> clk_sync_stage1
      [    6.513326] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_pre_setup -> clk_sync_stage1
      [    6.524891] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.536535] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition clk_sync_stage1 -> clk_sync_stage2
      [    6.548187] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.559831] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition clk_sync_stage2 -> clk_sync_stage3
      [    6.572498] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition clk_sync_stage3 -> link_setup
      [    6.583715] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition clk_sync_stage3 -> link_setup
      [    6.599838] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_setup -> opt_setup_stage1
      [    6.611142] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_setup -> opt_setup_stage1
      [    6.627592] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage1 -> opt_setup_stage2
      [    6.639412] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage1 -> opt_setup_stage2
      [    6.651481] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage2 -> opt_setup_stage3
      [    6.663300] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage2 -> opt_setup_stage3
      [    6.675123] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage3 -> opt_setup_stage4
      [    6.686942] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage3 -> opt_setup_stage4
      [    6.698770] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage4 -> opt_setup_stage5
      [    6.710591] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage4 -> opt_setup_stage5
      [    6.727601] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition opt_setup_stage5 -> clocks_enable
      [    6.739162] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition opt_setup_stage5 -> clocks_enable
      [    6.750782] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition clocks_enable -> link_enable
      [    6.761913] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition clocks_enable -> link_enable
      [    6.797400] ad9081 spi1.0: JESD RX (JTX) Link2 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
      [    6.808002] ad9081 spi1.0: JESD TX (JRX) Link0 0xF lanes in DATA
      [    6.814012] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_enable -> link_running
      [    6.825053] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_enable -> link_running
      [    6.836097] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[2] transition link_running -> opt_post_running_stage
      [    6.848096] jesd204: /axi/spi@ff040000/ad9988@0,jesd204:0,parent=spi1.0: JESD204[0] transition link_running -> opt_post_running_stage
   

   .. raw:: html

      </details>



IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used locally on FPGA platforms featuring a graphical desktop environment such as ZCU102 or ZC706 or remote using a network connection.

When using the remote option, once you logged in to the Linux terminal you need to check the IP address of the using the ifconfig command to see if there was any address assigned by a DHCP server. If not, you need to manually set an address with ifconfig in the same address space your PC is using.

Once the IIO Osc application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.


|image2|

.. include:: ../ad9081_iio_osc.rst AD9081 Plugin Description
------------------------------------------------------------

The AD9081 plugin works with the :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the AD9081 settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the AD9081 or the FPGA fabric) does not support that mode/precision.

If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the devices behind the back of the GUI, it's still possible to see the settings by clicking the ``Reload Settings`` button at the bottom of the GUI.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin.png
   :align: right
   :width: 400px

The AD9081 view is divided in three sections:

-  **Receive Chain**
-  **Transmit Chain**
-  **FPGA Settings**

--------------

Receive Chain
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin_rx.png
   :align: right
   :width: 300px

-  **ADC Rate(MHz):** Displays the ADC Sample Rate. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **ADC Nyquist Zone Control:** Selects the Nyquist Zone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Main NCO Frequency Control:** Controls the Main NCO. Frequency :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Main NCO Phase Control:** Controls the Main NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Channel NCO Frequency Control:** Controls the Channel NCO Frequency. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **RX Channel NCO Phase Control:** Controls the Channel NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

--------------

Transmit Chain
~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin_tx.png
   :align: right
   :width: 300px

-  **DAC Rate(MHz):** Displays the DAC Sample Rate. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Main NCO Frequency Control:** Controls the Main NCO Frequency.\ :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Main NCO Phase Control:** Controls the Main NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Channel NCO Frequency Control:** Controls the Channel. NCO Frequency :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX Channel NCO Phase Control:** Controls the Channel NCO Phase. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX NCO Channel Digital Gain:** Controls the Channel NCO digital gain. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  **TX NCO Test Tone Modes:** Controls the Test Tone generation. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

--------------

FPGA Settings
~~~~~~~~~~~~~

Transmit/DDS
^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ad9081_osc_plugin_fpga.png
   :align: center
   :width: 600px

The plugin provides several options on how the transmitted data is generated.

It is possible to either use the built-in two tone **Direct Digital Synthesizer (DDS)** to transmit a bi-tonal signal on channels I and Q of the DAC. Or it is possible to use the **Direct Memory Access (DMA) facility** to transmit custom data that you have stored in a file.

This can be achieved by selecting one of the following options listed by the **DDS Mode**:

One CW Tone
^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/one_cw_tone.png
   :align: right

In **One CW Tone** mode one continuous wave (CW) tone will be outputted. The plugin displays the controls to set the Frequency, Amplitude and Phase for just one tone and makes sure that the amplitude of the other tone is set to 0. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Two CW Tone
^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/two_cw_tones.png
   :align: right

In **Two CW Tone** mode two continuous wave (CW) tones will be outputted. The plugin displays the controls to set the frequencies F1 and F2, amplitudes A1 and A2, phases P1 and P2 for the two tones. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Independent I/Q Control
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iq_independent.png
   :align: right

In **Independent I/Q Control** the plugin displays the controls to set the frequencies, amplitudes and phases for the two tones that will be outputted on channel I and additionally it allows for the two tones that will be outputted on channel Q of the DAC to be configured independently.

|

.. note::

   Note: The bi-tonal signal (T) is defined as the sum of two tones:

   | T(t) = A1 \* sin(2 \* p \* F1 \* t + P1) + A2 \* sin(2 \* p \* F2 \* t + P2),
   | where A-amplitude, F-frequency, P-phase of a tone.



DAC Buffer Output
^^^^^^^^^^^^^^^^^

|image1| The file selector under the **File Selection** section is used to locate and choose the desired data file. Under the **DAC Channels** section the enabled channels will be used to transmit the data stored in the file. To finalize the process, a click on the **Load** button is required.

| **Restrictions:**
| \* There are two types of files than can be loaded: **.txt** or **.mat**. The IIO-Oscilloscope comes with several :git-iio-oscilloscope:`data files <waveforms>` that can be used. If you want to create your own data files please take a look at the :doc:`Basic IQ Data Files </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>` documentation first.
| \* Due to hardware limitation only specific combinations of enabled channels are possible. You can enable a total of 1, 2, 4, etc. channels. If 1 channel is enabled then it can be any of them. If two channels are enabled then channels 0, 1 or channels 2, 3 can be enabled and so on.


Disable
^^^^^^^

| In this mode both DDS and DMA are disabled causing the DAC channels to stop transmitting any data.
|

.. note::

   Upon pressing **Reload Settings** button the values will be reloaded with the corresponding driver values. Useful in scenarios where the diver values get changed outside this plugin and a refresh on plugin's values is needed.


.. hint::

   Some plugin values will be rounded to the nearest value supported by the hardware.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/dac_output_buffer_panel.png


Shut down
---------

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image3|

.. include:: ../common.rst .. include:: ../common.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/hwsetup_zcu102_ad9081.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/osc.png
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
