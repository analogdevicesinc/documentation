.. _eval-ad353xr quickstart de10nano:

DE10-Nano Quick start
===============================================================================

.. figure:: ../images/de10_nano_setup.jpeg
   :alt: DE10-Nano with connections
   :width: 800

   DE10-Nano with connections

.. esd-warning::

This guide provides step-by-step instructions to set up the
:adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` on:

- `DE10-Nano FPGA Board
  <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``system_top.rbf``, HDL bitstream built from
  :external+hdl:ref:`Build an HDL project <build_hdl>`
- ``u-boot-with-spl.sfp``, SPL and U-Boot bootloader
- ``socfpga.dtb``, compiled device tree blob
- ``zImage``, the Linux kernel image

.. note::

   Pre-built files for this reference design are not yet available.
   The bitstream must be built manually. Official release artifacts will
   be provided here once available.

   HDL source: :git-hdl:`/`

   Linux driver:
   :git-linux:`drivers/iio/dac/ad3530r.c <64ec98ac2413d592e484d4cb206fbca93c419693:drivers/iio/dac/ad3530r.c>`
   in :git-linux:`/`.

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- A UART terminal (e.g. PuTTY, Tera Term, Minicom) at 115200 baud (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `DE10-Nano FPGA Board
  <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_
  and its power supply
- :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` evaluation board
- Jumper wires for SPI and GPIO connections via the GPIO_1 (JP7) header
- Mini-USB to USB Type-A cable (UART)
- Ethernet cable
- microSD card (at least 16 GB)
- 5 V power supply for the AD3530R (USB-C connector or any VCC/GND pin)
- 3.3 V supply for the IOREF pin of the EVAL board

.. _eval-ad353xr quickstart de10nano hw-setup:

Hardware setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting the FPGA configuration switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adjust the FPGA configuration mode switch (SW10) to the SD card boot
position on the DE10-Nano.

Wiring the eval board to the DE10-Nano
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the EVAL-AD3530R to the DE10-Nano GPIO_1 header (JP7) using
jumper wires according to the table below. Physical pin numbers on JP7
are listed in the last column.

.. list-table:: Hardware connections - DE10-Nano - EVAL-AD3530R
   :header-rows: 1
   :widths: 15 50 35

   * - Signal
     - DE10-Nano GPIO_1 (FPGA pin - JP7 pin)
     - EVAL-AD3530R
   * - SPI CLK
     - PIN_AG18 (pin 33)
     - DIG-IO Pin 13
   * - SPI MISO
     - PIN_AF18 (pin 35)
     - DIG-IO Pin 11 (SDI)
   * - SPI MOSI
     - PIN_AG15 (pin 37)
     - DIG-IO Pin 12 (SDO)
   * - SPI CSB/SS
     - PIN_AE19 (pin 39)
     - DIG-IO Pin 10
   * - RESET
     - PIN_AE20 (pin 38)
     - DIG-IO Pin 8
   * - LDAC
     - PIN_AE17 (pin 40)
     - DIG-IO Pin 6

Power the EVAL-AD3530R by connecting a **5 V** supply to either the
USB-C connector or any available VCC/GND pin. Connect **3.3 V** to the
IOREF pin.

Inserting the SD card and connecting cables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Insert the prepared microSD card into the DE10-Nano SD card slot.
#. Connect the Mini-USB cable to the UART port on the DE10-Nano.
#. Connect the Ethernet cable to the Ethernet port.
#. Power on the board.
#. Observe serial console output in your terminal at 115200 baud.

Programming the bitstream
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy the built ``system_top.rbf`` bitstream to the ``BOOT`` partition of
the SD card before inserting it. The Kuiper boot flow loads the bitstream
automatically via the extlinux boot sequence.

Login information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The system logs in automatically as ``root``. If prompted:

- User: ``root``
- Password: ``analog``

.. collapsible:: Complete boot log

   ::

      ​U-Boot SPL 2021.10-17979-ge7beb4cb47-dirty (Nov 01 2023 - 22:08:40 +0200)
      Trying to boot from MMC1


      U-Boot 2021.10-17979-ge7beb4cb47-dirty (Nov 01 2023 - 22:08:40 +0200), Build: jenkins-2022_r2-hdl_jobs-projects-cn0540.de10nano-2

      CPU:   Altera SoCFPGA Platform
      FPGA:  Altera Cyclone V, SE/A6 or SX/C6 or ST/D6, version 0x0
      BOOT:  SD/MMC Internal Transceiver (3.0V)
            Watchdog enabled
      DRAM:  1 GiB
      MMC:   dwmmc0@ff704000: 0
      Loading Environment from MMC... *** Warning - bad CRC, using default environment

      In:    serial
      Out:   serial
      Err:   serial
      Model: Altera SOCFPGA Cyclone V SoC Development Kit
      Net:
      Warning: ethernet@ff702000 (eth0) using random MAC address - da:90:6c:a2:ed:1d
      eth0: ethernet@ff702000
      Hit any key to stop autoboot:  0
      150 bytes read in 4 ms (36.1 KiB/s)
      ## Executing script at 02100000
      2498608 bytes read in 129 ms (18.5 MiB/s)
      switch to partitions #0, OK
      mmc0 is current device
      Scanning mmc 0:1...
      Found /extlinux/extlinux.conf
      Retrieving file: /extlinux/extlinux.conf
      142 bytes read in 6 ms (22.5 KiB/s)
      1:      Linux Default
      Retrieving file: /extlinux/../zImage
      8844248 bytes read in 445 ms (19 MiB/s)
      append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      Retrieving file: /extlinux/../socfpga.dtb
      32354 bytes read in 9 ms (3.4 MiB/s)
      Kernel image @ 0x1000000 [ 0x000000 - 0x86f3d8 ]
      ## Flattened Device Tree blob at 02000000
         Booting using the fdt blob at 0x2000000
         Loading Device Tree to 09ff5000, end 09fffe61 ... OK

      Starting kernel ...

      Deasserting all peripheral resets
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 5.15.0-175919-g427c94e8faa5 (jenkins@romlxbuild1) (arm-linux-gnueabi-gcc (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #827 SMP Tue Dec 12 11:02:03 EET 2023
      [    0.000000] CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=10c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Terasic DE10-Nano
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
      [    0.000000] percpu: Embedded 15 pages/cpu s29452 r8192 d23796 u61440
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
      [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] Memory: 882928K/1048576K available (14336K kernel code, 1301K rwdata, 8000K rodata, 1024K init, 470K bss, 34576K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 44879 entries in 132 pages
      [    0.000000] ftrace: allocated 132 pages with 2 groups
      [    0.000000] trace event string verifier disabled
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000]  Rude variant of Tasks RCU enabled.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      [    0.000000] L2C-310 erratum 769419 enabled
      [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
      [    0.000000] L2C-310 full line of zeros enabled for Cortex-A9
      [    0.000000] L2C-310 ID prefetch enabled, offset 8 lines
      [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
      [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
      [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76460001
      [    0.000000] random: get_random_bytes called from start_kernel+0x520/0x6e0 with crng_init=0
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000001] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.007892] Switching to timer-based delay loop, resolution 10ns
      [    0.014283] Console: colour dummy device 80x30
      [    0.018751] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.029244] pid_max: default: 32768 minimum: 301
      [    0.033968] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.041255] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.049675] CPU: Testing write buffer coherency: ok
      [    0.054602] CPU0: Spectre v2: using BPIALL workaround
      [    0.059816] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.066170] Setting up static identity map for 0x100000 - 0x100060
      [    0.072485] rcu: Hierarchical SRCU implementation.
      [    0.077586] smp: Bringing up secondary CPUs ...
      [    0.082774] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.082790] CPU1: Spectre v2: using BPIALL workaround
      [    0.093578] smp: Brought up 1 node, 2 CPUs
      [    0.097665] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.103928] CPU: All CPU(s) started in SVC mode.
      [    0.109102] devtmpfs: initialized
      [    0.118310] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.126179] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.136007] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.149246] NET: Registered PF_NETLINK/PF_ROUTE protocol family
      [    0.157274] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.165254] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.173249] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.205844] debugfs: Directory 'fixed-supply' with parent 'regulator' already present!
      [    0.214021] vgaarb: loaded
      [    0.217024] SCSI subsystem initialized
      [    0.220967] usbcore: registered new interface driver usbfs
      [    0.226517] usbcore: registered new interface driver hub
      [    0.231851] usbcore: registered new device driver usb
      [    0.237109] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
      [    0.245284] mc: Linux media interface: v0.10
      [    0.249575] videodev: Linux video capture interface: v2.00
      [    0.255167] pps_core: LinuxPPS API ver. 1 registered
      [    0.260113] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.269232] PTP clock support registered
      [    0.273441] jesd204: found 0 devices and 0 topologies
      [    0.278520] FPGA manager framework
      [    0.281986] Advanced Linux Sound Architecture Driver Initialized.
      [    0.289218] clocksource: Switched to clocksource timer1
      [    0.340320] NET: Registered PF_INET protocol family
      [    0.345367] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
      [    0.353817] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
      [    0.362178] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.369975] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.377199] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.383647] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.390290] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.397502] NET: Registered PF_UNIX/PF_LOCAL protocol family
      [    0.419556] RPC: Registered named UNIX socket transport module.
      [    0.425459] RPC: Registered udp transport module.
      [    0.430174] RPC: Registered tcp transport module.
      [    0.434859] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.441288] PCI: CLS 0 bytes, default 64
      [    0.941478] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
      [    0.950957] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.963379] NFS: Registering the id_resolver key type
      [    0.968439] Key type id_resolver registered
      [    0.972642] Key type id_legacy registered
      [    0.976648] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
      [    0.983802] ntfs: driver 2.1.32 [Flags: R/W].
      [    0.988327] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.994924] fuse: init (API version 7.34)
      [    0.999377] bounce: pool size: 64 pages
      [    1.003222] io scheduler mq-deadline registered
      [    1.007736] io scheduler kyber registered
      [    1.049832] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    1.057249] printk: console [ttyS0] disabled
      [    1.061608] ffc02000.serial0: ttyS0 at MMIO 0xffc02000 (irq = 46, base_baud = 6250000) is a 16550A
      [    1.070593] printk: console [ttyS0] enabled
      [    1.070593] printk: console [ttyS0] enabled
      [    1.078923] printk: bootconsole [earlycon0] disabled
      [    1.078923] printk: bootconsole [earlycon0] disabled
      [    1.089547] ffc03000.serial1: ttyS1 at MMIO 0xffc03000 (irq = 47, base_baud = 6250000) is a 16550A
      [    1.100414] brd: module loaded
      [    1.105017] spi_altera ff30a000.spi: regoff 0, irq 50
      [    1.112593] libphy: Fixed MDIO Bus: probed
      [    1.117385] CAN device driver interface
      [    1.121596] socfpga-dwmac ff702000.ethernet: IRQ eth_wake_irq not found
      [    1.128196] socfpga-dwmac ff702000.ethernet: IRQ eth_lpi not found
      [    1.134498] socfpga-dwmac ff702000.ethernet: PTP uses main clock
      [    1.140539] socfpga-dwmac ff702000.ethernet: No sysmgr-syscon node found
      [    1.147228] socfpga-dwmac ff702000.ethernet: Unable to parse OF data
      [    1.153575] socfpga-dwmac: probe of ff702000.ethernet failed with error -524
      [    1.161000] stmmaceth ff702000.ethernet: IRQ eth_wake_irq not found
      [    1.167258] stmmaceth ff702000.ethernet: IRQ eth_lpi not found
      [    1.173208] stmmaceth ff702000.ethernet: PTP uses main clock
      [    1.179008] stmmaceth ff702000.ethernet: Version ID not available
      [    1.185110] stmmaceth ff702000.ethernet:     DWMAC1000
      [    1.189994] stmmaceth ff702000.ethernet: DMA HW capability register supported
      [    1.197104] stmmaceth ff702000.ethernet: RX Checksum Offload Engine supported
      [    1.204224] stmmaceth ff702000.ethernet: COE Type 2
      [    1.209086] stmmaceth ff702000.ethernet: TX Checksum insertion supported
      [    1.215771] stmmaceth ff702000.ethernet: Enhanced/Alternate descriptors
      [    1.222372] stmmaceth ff702000.ethernet: Extended descriptors not supported
      [    1.229317] stmmaceth ff702000.ethernet: Ring mode enabled
      [    1.234789] stmmaceth ff702000.ethernet: device MAC address e2:8c:41:ca:df:45
      [    1.250477] libphy: stmmac: probed
      [    1.253886] Micrel KSZ9031 Gigabit PHY stmmac-0:01: attached PHY driver (mii_bus:phy_addr=stmmac-0:01, irq=POLL)
      [    1.265388] usbcore: registered new interface driver asix
      [    1.270860] usbcore: registered new interface driver ax88179_178a
      [    1.276963] usbcore: registered new interface driver cdc_ether
      [    1.282843] usbcore: registered new interface driver net1080
      [    1.288520] usbcore: registered new interface driver cdc_subset
      [    1.294465] usbcore: registered new interface driver zaurus
      [    1.300080] usbcore: registered new interface driver cdc_ncm
      [    1.306373] dwc2 ffb40000.usb: supply vusb_d not found, using dummy regulator
      [    1.313662] dwc2 ffb40000.usb: supply vusb_a not found, using dummy regulator
      [    1.321050] dwc2 ffb40000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    1.328862] dwc2 ffb40000.usb: DWC OTG Controller
      [    1.333611] dwc2 ffb40000.usb: new USB bus registered, assigned bus number 1
      [    1.340679] dwc2 ffb40000.usb: irq 48, io mem 0xffb40000
      [    1.346172] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
      [    1.354430] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.361640] usb usb1: Product: DWC OTG Controller
      [    1.366329] usb usb1: Manufacturer: Linux 5.15.0-175919-g427c94e8faa5 dwc2_hsotg
      [    1.373716] usb usb1: SerialNumber: ffb40000.usb
      [    1.378863] hub 1-0:1.0: USB hub found
      [    1.382672] hub 1-0:1.0: 1 port detected
      [    1.387478] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    1.394012] ehci-pci: EHCI PCI platform driver
      [    1.399043] usbcore: registered new interface driver uas
      [    1.404464] usbcore: registered new interface driver usb-storage
      [    1.410566] usbcore: registered new interface driver usbserial_generic
      [    1.417091] usbserial: USB Serial support registered for generic
      [    1.423135] usbcore: registered new interface driver ftdi_sio
      [    1.428881] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.436270] usbcore: registered new interface driver upd78f0730
      [    1.442206] usbserial: USB Serial support registered for upd78f0730
      [    1.449938] i2c_dev: i2c /dev entries driver
      [    1.454712] usbcore: registered new interface driver uvcvideo
      [    1.462577] Synopsys Designware Multimedia Card Interface Driver
      [    1.469092] dw_mmc ff704000.dwmmc0: IDMAC supports 32-bit address mode.
      [    1.475803] ledtrig-cpu: registered to indicate activity on CPUs
      [    1.475846] dw_mmc ff704000.dwmmc0: Using internal DMA controller.
      [    1.481965] usbcore: registered new interface driver usbhid
      [    1.487966] dw_mmc ff704000.dwmmc0: Version ID is 240a
      [    1.493530] usbhid: USB HID core driver
      [    1.502572] dw_mmc ff704000.dwmmc0: DW MMC controller at irq 43,32 bit host data width,1024 deep fifo
      [    1.512013] mmc_host mmc0: card is polling.
      [    1.520951] axi_sysid ff218000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    1.528899] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.529063] axi_sysid ff218000.axi-sysid-0: [cn0540] on [de10nano] git branch <hdl_2022_r2> git <b31d4fbba87a96f329f858da3118771503c7c6b4> clean [2023-11-01 19:32:12] UTC
      [    1.554127] fpga_manager fpga0: Altera SOCFPGA FPGA Manager registered
      [    1.561561] usbcore: registered new interface driver snd-usb-audio
      [    1.570180] NET: Registered PF_INET6 protocol family
      [    1.576153] Segment Routing with IPv6
      [    1.579868] In-situ OAM (IOAM) with IPv6
      [    1.583863] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.585167] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.590359] NET: Registered PF_PACKET protocol family
      [    1.600242] mmc0: new high speed SDXC card at address 5048
      [    1.604563] NET: Registered PF_KEY protocol family
      [    1.615267] mmcblk0: mmc0:5048 SD64G 58.0 GiB
      [    1.619343] can: controller area network core
      [    1.624148] NET: Registered PF_CAN protocol family
      [    1.628934] can: raw protocol
      [    1.631951] can: broadcast manager protocol
      [    1.636135] can: netlink gateway - max_hops=1
      [    1.640273]  mmcblk0: p1 p2 p3
      [    1.640699] 8021q: 802.1Q VLAN Support v1.8
      [    1.647743] NET: Registered PF_IEEE802154 protocol family
      [    1.653165] Key type dns_resolver registered
      [    1.657505] ThumbEE CPU extension supported.
      [    1.661781] Registering SWP/SWPB emulation handler
      [    1.671958] i2c 0-0039: Fixing up cyclic dependency with ff290000.axi_hdmi
      [    1.678976] adv7511 0-0039: supply avdd not found, using dummy regulator
      [    1.685843] adv7511 0-0039: supply dvdd not found, using dummy regulator
      [    1.692610] adv7511 0-0039: supply pvdd not found, using dummy regulator
      [    1.699356] adv7511 0-0039: supply bgvdd not found, using dummy regulator
      [    1.706166] adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
      [    1.726266] dma-pl330 ffe01000.pdma: Loaded driver for PL330 DMAC-341330
      [    1.732985] dma-pl330 ffe01000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    1.742203] [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for ff290000.axi_hdmi on minor 0
      [    1.751336] axi-hdmi ff290000.axi_hdmi: [drm] Cannot find any crtc or sizes
      [    1.758725] of_cfs_init
      [    1.761221] of_cfs_init: OK
      [    1.764273] ALSA device list:
      [    1.767250]   No soundcards found.
      [    1.770915] dw-apb-uart ffc02000.serial0: forbid DMA for kernel console
      [    1.907874] random: fast init done
      [    2.019148] EXT4-fs (mmcblk0p2): recovery complete
      [    2.024743] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null). Quota mode: disabled.
      [    2.034878] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    2.048560] devtmpfs: mounted
      [    2.055823] Freeing unused kernel image (initmem) memory: 1024K
      [    2.062322] Run /sbin/init as init process
      [    2.648285] systemd[1]: System time before build time, advancing clock.
      [    2.716327] systemd[1]: systemd 247.3-7+rpi1+deb11u2 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [    2.740323] systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

      [    2.780438] systemd[1]: Set hostname to <analog>.
      [    4.464790] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [    4.754691] systemd[1]: Queued start job for default target Graphical Interface.
      [    4.764214] random: systemd: uninitialized urandom read (16 bytes read)
      [    4.771197] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    4.783565] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [    4.793537] systemd[1]: Created slice system-getty.slice.
      [  OK  ] Created slice system-getty.slice.
      [    4.829489] random: systemd: uninitialized urandom read (16 bytes read)
      [    4.837031] systemd[1]: Created slice system-modprobe.slice.
      [  OK  ] Created slice system-modprobe.slice.
      [    4.869452] random: systemd: uninitialized urandom read (16 bytes read)
      [    4.876983] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [    4.920357] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [    4.960067] systemd[1]: Created slice User and Session Slice.
      [  OK  ] Created slice User and Session Slice.
      [    4.999864] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [    5.039797] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [    5.052656] systemd[1]: Reached target Slices.
      [  OK  ] Reached target Slices.
      [    5.089639] systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      [    5.120872] systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [    5.162627] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [    5.199835] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [    5.258340] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
      [    5.267318] systemd[1]: Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket (/dev/log).
      [    5.310385] systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      [    5.348050] systemd[1]: Listening on udev Control Socket.
      [  OK  ] Listening on udev Control Socket.
      [    5.390118] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [    5.430288] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
      [    5.438990] systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
      [    5.451690] systemd[1]: Mounting RPC Pipe File System...
               Mounting RPC Pipe File System...
      [    5.492917] systemd[1]: Mounting Kernel Debug File System...
               Mounting Kernel Debug File System...
      [    5.522842] systemd[1]: Mounting Kernel Trace File System...
               Mounting Kernel Trace File System...
      [    5.559815] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [    5.574680] systemd[1]: Starting Restore / save the current clock...
               Starting Restore / save the current clock...
      [    5.631022] systemd[1]: Starting Set the console keyboard layout...
               Starting Set the console keyboard layout...
      [    5.659687] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [    5.675666] systemd[1]: Starting Load Kernel Module configfs...
               Starting Load Kernel Module configfs...
      [    5.713847] systemd[1]: Starting Load Kernel Module drm...
               Starting Load Kernel Module drm...
      [    5.763442] systemd[1]: Starting Load Kernel Module fuse...
               Starting Load Kernel Module fuse...
      [    5.812805] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [    5.822328] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [    5.835304] systemd[1]: Starting Journal Service...
               Starting Journal Service...
      [    5.885732] systemd[1]: Starting Load Kernel Modules...
               Starting Load Kernel Modules...
      [    5.905557] systemd[1]: Starting Remount Root and Kernel File Systems...
               Starting Remount Root and Kernel File Systems...
      [    5.973623] systemd[1]: Starting Coldplug All udev Devices...
               Starting Coldplug All udev Devices...
      [    6.050397] systemd[1]: Mounted RPC Pipe File System.
      [  OK  ] Mounted RPC Pipe File System.
      [    6.080191] systemd[1]: Mounted Kernel Debug File System.
      [  OK  ] Mounted Kernel Debug File System.
      [    6.110268] systemd[1]: Mounted Kernel Trace File System.
      [  OK  ] Mounted Kernel Trace File System.
      [    6.141451] systemd[1]: Finished Restore / save the current clock.
      [  OK  ] Finished Restore / save the current clock.
      [    6.223409] systemd[1]: modprobe@configfs.service: Succeeded.
      [    6.250277] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null). Quota mode: disabled.
      [    6.269805] systemd[1]: Finished Load Kernel Module configfs.
      [  OK  ] Finished Load Kernel Module configfs.
      [    6.314220] systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
      [  OK  ] Finished Set the console keyboard layout.
      [  OK  ] Finished Load Kernel Module drm.
      [  OK  ] Finished Load Kernel Module fuse.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Finished Remount Root and Kernel File Systems.
               Mounting FUSE Control File System...
               Mounting Kernel Configuration File System...
               Starting Flush Journal to Persistent Storage...
               Starting Load/Save Random Seed...
      [    6.652513] systemd-journald[106]: Received client request to flush runtime journal.
               Starting Apply Kernel Variables...
      [    6.698685] systemd-journald[106]: File /var/log/journal/6955d35f266143efae0a878017449443/system.journal corrupted or uncleanly shut down, renaming and replacing.
               Starting Create System Users...
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Finished Apply Kernel Variables.
      [  OK  ] Finished Create System Users.
               Starting Create Static Device Nodes in /dev...
      [  OK  ] Finished Coldplug All udev Devices.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Wait for udev To …plete Device Initialization...
      [  OK  ] Finished Create Static Device Nodes in /dev.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting Rule-based Manage…for Device Events and Files...
      [  OK  ] Finished Flush Journal to Persistent Storage.
      [  OK  ] Started Rule-based Manager for Device Events and Files.
               Starting Show Plymouth Boot Screen...
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Found device /dev/disk/by-partuuid/3c47d971-01.
      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Found device /dev/ttyS0.
      [  OK  ] Reached target Hardware activated USB gadget.
               Starting File System Check…isk/by-partuuid/3c47d971-01...
               Starting Load Kernel Modules...
      [  OK  ] Started File System Check Daemon to report status.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Finished Helper to synchronize boot up for ifupdown.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
      [  OK  ] Finished File System Check…/disk/by-partuuid/3c47d971-01.
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
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started DHCP Client Daemon.
      [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
      [FAILED] Failed to start Raise network interfaces.
      See 'systemctl status networking.service' for details.
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Started Authorization Manager.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
               Starting Modem Manager...
      [  OK  ] Reached target Network.
      [  OK  ] Reached target Network is Online.
               Starting CUPS Scheduler...
      [  OK  ] Started Erlang Port Mapper Daemon.
               Starting Load USB gadget scheme...
               Starting HTTP based time synchronization tool...
               Starting Internet superserver...
               Starting /etc/rc.local Compatibility...
               Starting OpenBSD Secure Shell server...
               Starting Permit User Sessions...
      [  OK  ] Finished Load USB gadget scheme.
      [  OK  ] Started Internet superserver.
      My IP address is 192.168.3.2
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Found device /dev/ttyGS0.
      [  OK  ] Started User Login Management.
               Mounting Mount FunctionFS instance...
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Finished Permit User Sessions.
      [  OK  ] Mounted Mount FunctionFS instance.
      [  OK  ] Started Disk Manager.
      [  OK  ] Started HTTP based time synchronization tool.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Finished Analog Devices power up/down sequence.
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Started Modem Manager.
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyS0

      analog login: root (automatic login)

      Linux analog 5.15.0-175919-g427c94e8faa5 #827 SMP Tue Dec 12 11:02:03 EET 2023 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Sun Dec 17 18:17:15 GMT 2023 on ttyS0
      root@analog:~#

Useful commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To find the IP address of the board:

.. shell::

   $ifconfig

To list detected IIO devices:

.. shell::

   $iio_info | grep iio:device

To power off the system cleanly:

.. shell::

   $poweroff

IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`iio-oscilloscope` is a cross-platform GUI application that connects
to the board over the network and allows reading and writing IIO device
attributes.

Open IIO Oscilloscope on the host PC, go to **Settings -> Connect**,
select the **Manual** option and enter the URI using the board IP:

.. code-block:: none

   ip:<board-ip>

Press **Refresh** to enumerate the IIO context, then press **Connect**.

.. figure:: ../images/iio_connect.jpeg
   :alt: IIO Oscilloscope connect dialog
   :width: 700

   IIO Oscilloscope - connect dialog

Testing the DAC output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AD3530R is an 8-channel 16-bit voltage output DAC. Since there is no
waveform to capture, use the **Debug** panel in IIO Oscilloscope to browse
and write IIO attributes directly to set the analog output voltage.

.. figure:: ../images/ad353xr_iio_debug.jpeg
   :alt: IIO Oscilloscope debug panel showing AD3530R channel attributes
   :width: 700

   IIO Oscilloscope - Debug panel for the AD3530R

.. collapsible:: Complete iio_info output

   ::

      root@analog:~# iio_info
      iio_info version: 0.25 (git tag:8fb78e06)
      Libiio version: 0.25 (git tag: 8fb78e0) backends: local xml ip usb serial
      IIO context created with local backend.
      Backend version: 0.25 (git tag: 8fb78e0)
      Backend description string: Linux analog 5.15.0-175919-g427c94e8faa5 #827 SMP Tue Dec 12 11:02:03 EET 2023 armv7l
      IIO context has 5 attributes:
            hdl_system_id: [cn0540] on [de10nano] git branch [hdl_2022_r2] git [b31d4fbba87a96f329f858da3118771503c7c6b4] clean [2023-11-01 19:32:12] UTC
            hw_carrier: Terasic DE10-Nano
            hw_model: EV-ADAQ7769-1FMC1Z on Xilinx Zynq ZED
            local,kernel: 5.15.0-175919-g427c94e8faa5
            uri: local:
      IIO context has 2 devices:
            iio:device0: ad3530r
                     8 channels found:
                              voltage1:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage7:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage5:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage6:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage2:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage0:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage3:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                              voltage4:  (output)
                              5 channel-specific attributes found:
                                    attr  0: powerdown value: 0
                                    attr  1: powerdown_mode value: 32kohm_to_gnd
                                    attr  2: powerdown_mode_available value: 1kohm_to_gnd 7.7kohm_to_gnd 32kohm_to_gnd
                                    attr  3: raw value: 65535
                                    attr  4: scale value: 0.038146972
                     1 device-specific attributes found:
                                    attr  0: waiting_for_supplier value: 0
                     1 debug attributes found:
                                    debug attr  0: direct_reg_access value: 0xFF
                     No trigger on this device
            iio_sysfs_trigger:
                     0 channels found:
                     2 device-specific attributes found:
                                    attr  0: add_trigger ERROR: Permission denied (13)
                                    attr  1: remove_trigger ERROR: Permission denied (13)
                     No trigger on this device
