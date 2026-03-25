.. _arradio quick-start:

ARRADIO Terasic C5 SoCkit Quick Start Guide
===========================================

.. image:: ../images/terasic_c5_sockit_arradio.jpg
   :align: left
   :width: 500

This guide provides some quick instructions (still takes awhile to
download, and set things up) on how to setup the ARRADIO board on `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_

.. _arradio carriers:

Supported carriers
-------------------------------------------------------------------------------

The `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`_
board is an HSMC (High Speed Mezzanine Card) board; that means it needs a
carrier to plug into.

The ARRADIO board is designed specifically for the
`Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_
carrier, which features an Intel Cyclone V SoC FPGA.

Supported Environments
-------------------------------------------------------------------------------

The supported OS and software environments are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
   - - `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_
     - :git-hdl:`Yes <projects/arradio>`
     - :git-linux:`Yes <arch/arm/boot/dts/intel/socfpga/socfpga_cyclone5_sockit_arradio.dts>`

.. note::

   The ARRADIO board does not have No-OS software support. All software
   development and evaluation is done through Linux.

Creating the Micro-SD Card
--------------------------

.. tip::

   :doc:`Create SD Image for Terasic C5 SoCkit board(it is a single image for all boards). </linux/kuiper/index>`

Required files
~~~~~~~~~~~~~~

The root of 'BOOT' should contain the following files:

-  ``socfpga.dtb``
-  ``zImage``
-  ``u-boot.scr``
-  ``soc_system.rbf``

The root of preloader partition should contain the following file:

-  ``preloader_bootloader.img``

.. note::

   More information regarding the build process of the HDL boot image can be
   found here: :external+hdl:ref:`build_intel_boot_image`

Configuring the Micro-SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   analog@analog:~ $ lsblk

   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part /media/analog/BOOT
   ├─sdb2        8:18   1  9.8G  0 part /media/analog/rootfs
   └─sdb3        8:19   1    4M  0 part

   analog@analog:~ $ cd /media/analog/BOOT/socfpga_cyclone5_sockit_arradio
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ ls -l

   total 10248
   -rwxr-xr-x 1 root root  500432 Jul 27 15:06 preloader_bootloader.img
   -rwxr-xr-x 1 root root   25291 Jul 27 15:06 socfpga.dtb
   -rwxr-xr-x 1 root root 2685848 Jul 27 15:06 soc_system.rbf
   -rwxr-xr-x 1 root root     200 Jul 27 15:06 u-boot.scr
   -rwxr-xr-x 1 root root 7269944 Jul 27 15:06 zImage

   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp socfpga.dtb /media/analog/BOOT/socfpga.dtb
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp zImage /media/analog/BOOT/zImage
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp u-boot.scr /media/analog/BOOT/u-boot.scr
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp soc_system.rbf /media/analog/BOOT/soc_system.rbf
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo dd if=preloader_bootloader.img of=/dev/sdb3

   977+1 records in
   977+1 records out
   500432 bytes (500 kB, 489 KiB) copied, 0.138791 s, 3.6 MB/s

   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sync
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ cd ../../
   analog@analog:/media/analog $ sudo umount /dev/sdb1
   analog@analog:/media/analog $ sudo umount /dev/sdb2
   analog@analog:/media/analog $ lsblk

   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part
   ├─sdb2        8:18   1  9.8G  0 part
   └─sdb3        8:19   1    4M  0 part

Setting up the hardware (Terasic C5 SoCkit)
-------------------------------------------

You will need to:

- Get the `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_

.. image:: ../images/terasic_c5_sockit.jpg
   :align: center
   :width: 500

#. Insert the Micro-SD Card into the Micro-SD Card  Connector
#. Connect the ARRADIO board to the FPGA carrier HSMC connector
#. Plug your monitor device into the VGA Video Connector
#. Plug your USB mouse/keyboard into the USB 2.0 OTG Port
#. Plug the Power Supply into 12V Power Supply connector (DO NOT turn the device
   on)
#. Set the jumpers according to the following table:

======= ========= ========= ======== ======== ========
\       CLOCKSEL0 CLOCKSEL1 BOOTSEL0 BOOTSEL1 BOOTSEL2
======= ========= ========= ======== ======== ========
**POS** 2-3       2-3       2-3      2-3      1-2
======= ========= ========= ======== ======== ========

.. image:: ../images/sockit_clksel_bootsel.jpg
   :align: center
   :width: 400

+--------------+
| JP2          |
+==============+
| 2.5V or 1.8V |
+--------------+

.. image:: ../images/sockit_jp2.jpg
   :align: center
   :width: 300

======= ===== ===== ===== ===== ===== =========
SW6     MSEL0 MSEL1 MSEL2 MSEL3 MSEL4 CODEC_SEL
======= ===== ===== ===== ===== ===== =========
**POS** 0     1     0     1     0     0
======= ===== ===== ===== ===== ===== =========

.. image:: ../images/sockit_sw6.jpg
   :align: center
   :width: 300

.. esd-warning::

Booting the Micro-SD Card
-------------------------

.. note::

   There're two options to connect to the IIO-OScilloscope & Scopy, directly on
   the target or remotely from a PC via ethernet. Below examples showcase the
   remote connection method.

UART setup
~~~~~~~~~~

A UART terminal (serial console) can be used to capture the output of the
example application. The number of used UART port depends on the computer's
configuration. The following settings must be used in the UART terminal:

- **Baud Rate**: 115200bps
- **Data**: 8 bit
- **Parity**: None
- **Stop bits**: 1 bit
- **Flow Control**: none

**On Windows**:

Exampele of terminal emulators on Windows:

- `TeraTerm <https://teratermproject.github.io/index-en.html>`__

   - Setting up Tera Term:

      - Open Tera Term
      - Select Serial and your Port: (COMx)
      - Setup → Serial port…

- `PuTTy <https://putty.org/index.html>`__

**On Linux**:

- `GTKterm <https://elinux.org/Communicate_with_hardware_using_USB_cable_for_Ubuntu>`__
- `Minicom <https://help.ubuntu.com/community/Minicom>`__

**See Also:**

- `Setup a Serial Console - Xilinx <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18842446/Setup+a+Serial+Console>`__

.. collapsible:: Complete boot log

   ::

      U-Boot SPL 2021.10-17979-ge7beb4cb47f-dirty (Mar 20 2026 - 22:33:05 +0200)
      Trying to boot from MMC1

      U-Boot 2021.10-17979-ge7beb4cb47f-dirty (Mar 20 2026 - 22:33:05 +0200), Build: jenkins-hdl_2026_r1-builds-hdl_2026_r1_latest_commit-projects-arradio.c5soc-10

      CPU:   Altera SoCFPGA Platform
      FPGA:  Altera Cyclone V, SE/A6 or SX/C6 or ST/D6, version 0x0
      BOOT:  SD/MMC External Transceiver (1.8V)
            Watchdog enabled
      DRAM:  1 GiB
      MMC:   dwmmc0@ff704000: 0
      Loading Environment from MMC... *** Warning - bad CRC, using default environment

      In:    serial
      Out:   serial
      Err:   serial
      Model: Altera SOCFPGA Cyclone V SoC Development Kit
      Net:
      Warning: ethernet@ff702000 (eth0) using random MAC address - ae:f9:22:64:95:f1
      eth0: ethernet@ff702000
      Hit any key to stop autoboot:  0
      150 bytes read in 6 ms (24.4 KiB/s)
      ## Executing script at 02100000
      2728692 bytes read in 141 ms (18.5 MiB/s)
      switch to partitions #0, OK
      mmc0 is current device
      Scanning mmc 0:1...
      Found /extlinux/extlinux.conf
      Retrieving file: /extlinux/extlinux.conf
      142 bytes read in 7 ms (19.5 KiB/s)
      1:      Linux Default
      Retrieving file: /extlinux/../zImage
      9510496 bytes read in 477 ms (19 MiB/s)
      append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      Retrieving file: /extlinux/../socfpga.dtb
      33327 bytes read in 10 ms (3.2 MiB/s)
      Kernel image @ 0x1000000 [ 0x000000 - 0x911e60 ]
      ## Flattened Device Tree blob at 02000000
         Booting using the fdt blob at 0x2000000
         Loading Device Tree to 09ff4000, end 09fff22e ... OK

      Starting kernel ...

      Deasserting all peripheral resets
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 6.12.77-ge2f9fe8e3654 (root@0388ddad3d8b) (arm-linux-gnueabi-gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #1 SMP Thu Mar 26 11:56:56 UTC 2026
      [    0.000000] CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=10c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Terasic SoCkit
      [    0.000000] Memory policy: Data cache writealloc
      [    0.000000] cma: Reserved 128 MiB at 0x38000000 on node -1
      [    0.000000] Zone ranges:
      [    0.000000]   Normal   [mem 0x0000000000000000-0x000000002fffffff]
      [    0.000000]   HighMem  [mem 0x0000000030000000-0x000000003fffffff]
      [    0.000000] Movable zone start for each node
      [    0.000000] Early memory node ranges
      [    0.000000]   node   0: [mem 0x0000000000000000-0x000000003fffffff]
      [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000003fffffff]
      [    0.000000] OF: reserved mem: Reserved memory: No reserved-memory node in the DT
      [    0.000000] percpu: Embedded 12 pages/cpu s16716 r8192 d24244 u49152
      [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      [    0.000000] Unknown kernel command line parameters "earlyprintk", will be passed to user space.
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 262144
      [    0.000000] mem auto-init: stack:all(zero), heap alloc:off, heap free:off
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      [    0.000000] L2C-310 erratum 769419 enabled
      [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
      [    0.000000] L2C-310 full line of zeros enabled for Cortex-A9
      [    0.000000] L2C-310 ID prefetch enabled, offset 8 lines
      [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
      [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
      [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76460001
      [    0.000000] rcu: srcu_init: Setting srcu_struct sizes based on contention.
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000001] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.000014] Switching to timer-based delay loop, resolution 10ns
      [    0.000415] Console: colour dummy device 80x30
      [    0.000464] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.000477] CPU: Testing write buffer coherency: ok
      [    0.000518] CPU0: Spectre v2: using BPIALL workaround
      [    0.000525] pid_max: default: 32768 minimum: 301
      [    0.000689] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000706] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.001533] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.003038] Setting up static identity map for 0x100000 - 0x100060
      [    0.003264] rcu: Hierarchical SRCU implementation.
      [    0.003271] rcu:     Max phase no-delay instances is 1000.
      [    0.003964] smp: Bringing up secondary CPUs ...
      [    0.004882] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.004902] CPU1: Spectre v2: using BPIALL workaround
      [    0.005061] smp: Brought up 1 node, 2 CPUs
      [    0.005073] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.005083] CPU: All CPU(s) started in SVC mode.
      [    0.005558] Memory: 876948K/1048576K available (14336K kernel code, 874K rwdata, 11312K rodata, 1024K init, 485K bss, 38236K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.006175] devtmpfs: initialized
      [    0.011749] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.011978] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.011999] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.018279] NET: Registered PF_NETLINK/PF_ROUTE protocol family
      [    0.020220] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.021366] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.021379] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.037577] SCSI subsystem initialized
      [    0.037817] usbcore: registered new interface driver usbfs
      [    0.037859] usbcore: registered new interface driver hub
      [    0.037906] usbcore: registered new device driver usb
      [    0.038067] usb_phy_generic soc:usbphy: dummy supplies not allowed for exclusive requests (id=vbus)
      [    0.038478] mc: Linux media interface: v0.10
      [    0.038539] videodev: Linux video capture interface: v2.00
      [    0.038604] pps_core: LinuxPPS API ver. 1 registered
      [    0.038610] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.038628] PTP clock support registered
      [    0.038908] jesd204: found 0 devices and 0 topologies
      [    0.038986] FPGA manager framework
      [    0.039072] Advanced Linux Sound Architecture Driver Initialized.
      [    0.040410] vgaarb: loaded
      [    0.040815] clocksource: Switched to clocksource timer1
      [    0.050776] NET: Registered PF_INET protocol family
      [    0.051047] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
      [    0.052845] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes, linear)
      [    0.052875] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.052888] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.052965] TCP bind hash table entries: 8192 (order: 5, 131072 bytes, linear)
      [    0.053196] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.053312] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.053361] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.053561] NET: Registered PF_UNIX/PF_LOCAL protocol family
      [    0.054396] RPC: Registered named UNIX socket transport module.
      [    0.054409] RPC: Registered udp transport module.
      [    0.054413] RPC: Registered tcp transport module.
      [    0.054417] RPC: Registered tcp-with-tls transport module.
      [    0.054422] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.054438] PCI: CLS 0 bytes, default 64
      [    0.055595] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.056455] NFS: Registering the id_resolver key type
      [    0.056495] Key type id_resolver registered
      [    0.056501] Key type id_legacy registered
      [    0.056800] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.056875] fuse: init (API version 7.41)
      [    0.057297] bounce: pool size: 64 pages
      [    0.057330] io scheduler mq-deadline registered
      [    0.057338] io scheduler kyber registered
      [    0.057356] io scheduler bfq registered
      [    0.058549] ledtrig-cpu: registered to indicate activity on CPUs
      [    0.064589] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.066022] printk: legacy console [ttyS0] disabled
      [    0.066455] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 30, base_baud = 6250000) is a 16550A
      [    0.066498] printk: legacy console [ttyS0] enabled
      [    0.728471] ffc03000.serial: ttyS1 at MMIO 0xffc03000 (irq = 31, base_baud = 6250000) is a 16550A
      [    0.739552] brd: module loaded
      [    0.744471] spi_altera ff308000.spi: regoff 0, irq 32
      [    0.751923] CAN device driver interface
      [    0.756104] socfpga-dwmac ff702000.ethernet: IRQ eth_wake_irq not found
      [    0.762761] socfpga-dwmac ff702000.ethernet: IRQ eth_lpi not found
      [    0.768925] socfpga-dwmac ff702000.ethernet: IRQ sfty not found
      [    0.774907] socfpga-dwmac ff702000.ethernet: Deprecated MDIO bus assumption used
      [    0.782381] socfpga-dwmac ff702000.ethernet: PTP uses main clock
      [    0.788384] socfpga-dwmac ff702000.ethernet: No sysmgr-syscon node found
      [    0.795086] socfpga-dwmac ff702000.ethernet: Unable to parse OF data
      [    0.801446] socfpga-dwmac ff702000.ethernet: probe with driver socfpga-dwmac failed with error -524
      [    0.810981] stmmaceth ff702000.ethernet: IRQ eth_wake_irq not found
      [    0.817239] stmmaceth ff702000.ethernet: IRQ eth_lpi not found
      [    0.823087] stmmaceth ff702000.ethernet: IRQ sfty not found
      [    0.828692] stmmaceth ff702000.ethernet: Deprecated MDIO bus assumption used
      [    0.835811] stmmaceth ff702000.ethernet: PTP uses main clock
      [    0.841821] stmmaceth ff702000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    0.848601] stmmaceth ff702000.ethernet:     DWMAC1000
      [    0.853492] stmmaceth ff702000.ethernet: DMA HW capability register supported
      [    0.860605] stmmaceth ff702000.ethernet: RX Checksum Offload Engine supported
      [    0.867739] stmmaceth ff702000.ethernet: COE Type 2
      [    0.872617] stmmaceth ff702000.ethernet: TX Checksum insertion supported
      [    0.879296] stmmaceth ff702000.ethernet: Enhanced/Alternate descriptors
      [    0.885900] stmmaceth ff702000.ethernet: Enabled extended descriptors
      [    0.892329] stmmaceth ff702000.ethernet: Ring mode enabled
      [    0.897796] stmmaceth ff702000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    0.905454] stmmaceth ff702000.ethernet: device MAC address 3a:0e:7e:2f:97:9a
      [    0.921530] Micrel KSZ9021 Gigabit PHY stmmac-0:01: attached PHY driver (mii_bus:phy_addr=stmmac-0:01, irq=POLL)
      [    0.933030] usbcore: registered new interface driver asix
      [    0.938466] usbcore: registered new interface driver ax88179_178a
      [    0.944620] usbcore: registered new interface driver cdc_ether
      [    0.950479] usbcore: registered new interface driver net1080
      [    0.956192] usbcore: registered new interface driver cdc_subset
      [    0.962161] usbcore: registered new interface driver zaurus
      [    0.967759] usbcore: registered new interface driver cdc_ncm
      [    0.973460] usbcore: registered new interface driver r8153_ecm
      [    0.980005] dwc2 ffb40000.usb: supply vusb_d not found, using dummy regulator
      [    0.987287] dwc2 ffb40000.usb: supply vusb_a not found, using dummy regulator
      [    0.994970] dwc2 ffb40000.usb: DWC OTG Controller
      [    0.999700] dwc2 ffb40000.usb: new USB bus registered, assigned bus number 1
      [    1.006790] dwc2 ffb40000.usb: irq 34, io mem 0xffb40000
      [    1.012341] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.12
      [    1.020584] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.027805] usb usb1: Product: DWC OTG Controller
      [    1.032518] usb usb1: Manufacturer: Linux 6.12.77-ge2f9fe8e3654 dwc2_hsotg
      [    1.039369] usb usb1: SerialNumber: ffb40000.usb
      [    1.044628] hub 1-0:1.0: USB hub found
      [    1.048419] hub 1-0:1.0: 1 port detected
      [    1.053567] usbcore: registered new interface driver uas
      [    1.058942] usbcore: registered new interface driver usb-storage
      [    1.065067] usbcore: registered new interface driver usbserial_generic
      [    1.071633] usbserial: USB Serial support registered for generic
      [    1.077659] usbcore: registered new interface driver ftdi_sio
      [    1.083426] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.090812] usbcore: registered new interface driver upd78f0730
      [    1.096738] usbserial: USB Serial support registered for upd78f0730
      [    1.104472] i2c_dev: i2c /dev entries driver
      [    1.109316] usbcore: registered new interface driver uvcvideo
      [    1.117562] Synopsys Designware Multimedia Card Interface Driver
      [    1.124509] usbcore: registered new interface driver usbhid
      [    1.130069] usbhid: USB HID core driver
      [    1.131217] dw_mmc ff704000.mmc: clk-phase-sd-hs was specified, but failed to find altr,sys-mgr regmap!
      [    1.134190] SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      [    1.143286] dw_mmc ff704000.mmc: IDMAC supports 32-bit address mode.
      [    1.152569] ad9361 spi0.0: ad9361_probe : enter (ad9361)
      [    1.162793] ad9361 spi0.0: No GPIOs defined for ext band ctrl
      [    1.170717] dw_mmc ff704000.mmc: Using internal DMA controller.
      [    1.176673] dw_mmc ff704000.mmc: Version ID is 240a
      [    1.181640] dw_mmc ff704000.mmc: DW MMC controller at irq 36,32 bit host data width,1024 deep fifo
      [    1.190932] mmc_host mmc0: card is polling.
      [    1.207843] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.269479] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.279291] mmc0: new high speed SDHC card at address 0001
      [    1.285494] mmcblk0: mmc0:0001 00000 29.1 GiB
      [    1.292299]  mmcblk0: p1 p2 p3
      [    1.435784] ad9361 spi0.0: ad9361_probe : AD936x Rev 0 successfully initialized
      [    1.471853] cf_axi_dds ff324000.cf-ad9361-dds-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.02.b) at 0xFF324000 mapped to 0x(ptrval), probed DDS AD9361
      [    1.488328] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 (8000003f) counters available
      [    1.498175] fpga_manager fpga0: Altera SOCFPGA FPGA Manager registered
      [    1.505600] usbcore: registered new interface driver snd-usb-audio
      [    1.513871] NET: Registered PF_INET6 protocol family
      [    1.520167] Segment Routing with IPv6
      [    1.523935] In-situ OAM (IOAM) with IPv6
      [    1.527941] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.534498] NET: Registered PF_PACKET protocol family
      [    1.539550] NET: Registered PF_KEY protocol family
      [    1.544570] can: controller area network core
      [    1.548961] NET: Registered PF_CAN protocol family
      [    1.553777] can: raw protocol
      [    1.556746] can: broadcast manager protocol
      [    1.560936] can: netlink gateway - max_hops=1
      [    1.565340] 8021q: 802.1Q VLAN Support v1.8
      [    1.569539] NET: Registered PF_IEEE802154 protocol family
      [    1.574967] Key type dns_resolver registered
      [    1.579393] ThumbEE CPU extension supported.
      [    1.583678] Registering SWP/SWPB emulation handler
      [    1.609736] at24 0-0050: supply vcc not found, using dummy regulator
      [    1.645731] dma-pl330 ffe01000.pdma: Loaded driver for PL330 DMAC-341330
      [    1.652481] dma-pl330 ffe01000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    2.862557] cf_axi_adc ff320000.cf-ad9361-lpc: ADI AIM (10.03.) probed ADC AD9361 as MASTER
      [    2.871301] of_cfs_init
      [    2.873775] of_cfs_init: OK
      [    2.876877] clk: Disabling unused clocks
      [    2.880900] ALSA device list:
      [    2.883866]   No soundcards found.
      [    2.887454] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
      [    3.042466] EXT4-fs (mmcblk0p2): mounted filesystem 66300ab8-01bc-428e-8e3c-2d9b293210b5 r/w with ordered data mode. Quota mode: disabled.
      [    3.054950] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    3.061689] devtmpfs: mounted
      [    3.066001] Freeing unused kernel image (initmem) memory: 1024K
      [    3.072597] Run /sbin/init as init process
      [    3.662590] systemd[1]: System time advanced to built-in epoch: Wed 2025-09-03 14:38:20 EDT
      [    3.694669] systemd[1]: Failed to find module 'autofs4'
      [    3.770960] systemd[1]: systemd 257.9-1~deb13u1 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +IPE +SMACK +SECCOMP +GCRYPT -GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBCRYPTSETUP_PLUGINS +LIBFDISK +PCRE2 +PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -BPF_FRAMEWORK -BTF -XKBCOMMON -UTMP +SYSVINIT +LIBARCHIVE)
      [    3.805113] systemd[1]: Detected architecture arm.

      Welcome to Debian GNU/Linux 13 (trixie)!

      [    3.852076] systemd[1]: Hostname set to <analog>.
      [    5.812368] systemd[1]: /usr/lib/systemd/system/iiod.service:16: Invalid environment assignment, ignoring: $IIOD_EXTRA_OPTS=
      [    6.373375] systemd[1]: Queued start job for default target graphical.target.
      [    6.413865] systemd[1]: Created slice system-getty.slice - Slice /system/getty.
      [  OK  ] Created slice system-getty.slice - Slice /system/getty.
      [    6.443654] systemd[1]: Created slice system-modprobe.slice - Slice /system/modprobe.
      [  OK  ] Created slice system-modprobe.slice - Slice /system/modprobe.
      [    6.473650] systemd[1]: Created slice system-serial\x2dgetty.slice - Slice /system/serial-getty.
      [  OK  ] Created slice system-serial\x2dget…slice - Slice /system/serial-getty.
      [    6.513509] systemd[1]: Created slice system-systemd\x2dfsck.slice - Slice /system/systemd-fsck.
      [  OK  ] Created slice system-systemd\x2dfs…slice - Slice /system/systemd-fsck.
      [    6.552086] systemd[1]: Created slice user.slice - User and Session Slice.
      [  OK  ] Created slice user.slice - User and Session Slice.
      [    6.581495] systemd[1]: Started systemd-ask-password-wall.path - Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started systemd-ask-password-wall.…d Requests to Wall Directory Watch.
      [    6.621434] systemd[1]: proc-sys-fs-binfmt_misc.automount - Arbitrary Executable File Formats File System Automount Point was skipped because of an unmet condition check (ConditionPathExists=/proc/sys/fs/binfmt_misc).
      [    6.640976] systemd[1]: Expecting device dev-disk-by\x2dpartuuid-d29065e8\x2d01.device - /dev/disk/by-partuuid/d29065e8-01...
               Expecting device dev-disk-by\x2dpa…dev/disk/by-partuuid/d29065e8-01...
      [    6.681067] systemd[1]: Expecting device dev-ttyGS0.device - /dev/ttyGS0...
               Expecting device dev-ttyGS0.device - /dev/ttyGS0...
      [    6.711032] systemd[1]: Expecting device dev-ttyGS1.device - /dev/ttyGS1...
               Expecting device dev-ttyGS1.device - /dev/ttyGS1...
      [    6.741003] systemd[1]: Expecting device dev-ttyPS0.device - /dev/ttyPS0...
               Expecting device dev-ttyPS0.device - /dev/ttyPS0...
      [    6.770997] systemd[1]: Expecting device dev-ttyS0.device - /dev/ttyS0...
               Expecting device dev-ttyS0.device - /dev/ttyS0...
      [    6.801302] systemd[1]: Reached target nss-user-lookup.target - User and Group Name Lookups.
      [  OK  ] Reached target nss-user-lookup.target - User and Group Name Lookups.
      [    6.831135] systemd[1]: Reached target remote-fs.target - Remote File Systems.
      [  OK  ] Reached target remote-fs.target - Remote File Systems.
      [    6.861124] systemd[1]: Reached target slices.target - Slice Units.
      [  OK  ] Reached target slices.target - Slice Units.
      [    6.891210] systemd[1]: Reached target swap.target - Swaps.
      [  OK  ] Reached target swap.target - Swaps.
      [    6.931773] systemd[1]: Listening on systemd-creds.socket - Credential Encryption/Decryption.
      [  OK  ] Listening on systemd-creds.socket - Credential Encryption/Decryption.
      [    6.951759] systemd[1]: Listening on systemd-initctl.socket - initctl Compatibility Named Pipe.
      [  OK  ] Listening on systemd-initctl.socke…- initctl Compatibility Named Pipe.
      [    6.982244] systemd[1]: Listening on systemd-journald-dev-log.socket - Journal Socket (/dev/log).
      [  OK  ] Listening on systemd-journald-dev-…socket - Journal Socket (/dev/log).
      [    7.012135] systemd[1]: Listening on systemd-journald.socket - Journal Sockets.
      [  OK  ] Listening on systemd-journald.socket - Journal Sockets.
      [    7.041313] systemd[1]: systemd-pcrextend.socket - TPM PCR Measurements was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
      [    7.055276] systemd[1]: systemd-pcrlock.socket - Make TPM PCR Policy was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
      [    7.069532] systemd[1]: Listening on systemd-udevd-control.socket - udev Control Socket.
      [  OK  ] Listening on systemd-udevd-control.socket - udev Control Socket.
      [    7.101550] systemd[1]: Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
      [  OK  ] Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
      [    7.131797] systemd[1]: dev-hugepages.mount - Huge Pages File System was skipped because of an unmet condition check (ConditionPathExists=/sys/kernel/mm/hugepages).
      [    7.147189] systemd[1]: dev-mqueue.mount - POSIX Message Queue File System was skipped because of an unmet condition check (ConditionPathExists=/proc/sys/fs/mqueue).
      [    7.168036] systemd[1]: Mounting run-lock.mount - Legacy Locks Directory /run/lock...
               Mounting run-lock.mount - Legacy Locks Directory /run/lock...
      [    7.218693] systemd[1]: Mounting sys-kernel-debug.mount - Kernel Debug File System...
               Mounting sys-kernel-debug.mount - Kernel Debug File System...
      [    7.251722] systemd[1]: sys-kernel-tracing.mount - Kernel Trace File System was skipped because of an unmet condition check (ConditionPathExists=/sys/kernel/tracing).
      [    7.313916] systemd[1]: Mounting tmp.mount - Temporary Directory /tmp...
               Mounting tmp.mount - Temporary Directory /tmp...
      [    7.361791] systemd[1]: Starting fake-hwclock-load.service - Restore the current clock...
               Starting fake-hwclock-load.service - Restore the current clock...
      [    7.402619] systemd[1]: kmod-static-nodes.service - Create List of Static Device Nodes was skipped because of an unmet condition check (ConditionFileNotEmpty=/lib/modules/6.12.77-ge2f9fe8e3654/modules.devname).
      [    7.458653] systemd[1]: Starting modprobe@configfs.service - Load Kernel Module configfs...
               Starting modprobe@configfs.service - Load Kernel Module configfs...
      [    7.504103] systemd[1]: Starting modprobe@drm.service - Load Kernel Module drm...
               Starting modprobe@drm.service - Load Kernel Module drm...
      [    7.543911] systemd[1]: Starting modprobe@efi_pstore.service - Load Kernel Module efi_pstore...
               Starting modprobe@efi_pstore.servi… - Load Kernel Module efi_pstore...
      [    7.591737] systemd[1]: Starting modprobe@fuse.service - Load Kernel Module fuse...
               Starting modprobe@fuse.service - Load Kernel Module fuse...
      [    7.622434] systemd[1]: systemd-hibernate-clear.service - Clear Stale Hibernate Storage Info was skipped because of an unmet condition check (ConditionPathExists=/sys/firmware/efi/efivars/HibernateLocation-8cf2644b-4b0b-428f-9387-6d876050dc67).
      [    7.646981] systemd[1]: systemd-journald.service: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    7.659933] systemd[1]: systemd-journald.service: (This warning is only shown for the first unit using IP firewalling.)
      [    7.701807] systemd[1]: Starting systemd-journald.service - Journal Service...
               Starting systemd-journald.service - Journal Service...
      [    7.741871] systemd[1]: Starting systemd-modules-load.service - Load Kernel Modules...
      [    7.750314] systemd[1]: systemd-pcrmachine.service - TPM PCR Machine ID Measurement was skipped because of an unmet condition check (ConditionSecurity=measured-uki).

      [    7.781741] systemd[1]: Starting systemd-tmpfiles-setup-dev-early.service - Create Static Device Nodes in /dev gracefully...
               Starting systemd-tmpfiles-setup-de… Device Nodes in /dev gracefully...
      [    7.831379] systemd[1]: systemd-tpm2-setup-early.service - Early TPM SRK Setup was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
      [    7.865978] systemd[1]: Starting systemd-udev-load-credentials.service - Load udev Rules from Credentials...
               Starting systemd-udev-load-credent…Load udev Rules from Credentials...
      [    7.931704] systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
               Starting systemd-udev-trigger.service - Coldplug All udev Devices...
      [    8.006309] systemd[1]: Mounted run-lock.mount - Legacy Locks Directory /run/lock.
      [  OK  ] Mounted run-lock.mount - Legacy Locks Directory /run/lock.
      [    8.052225] systemd[1]: Mounted sys-kernel-debug.mount - Kernel Debug File System.
      [  OK  ] Mounted sys-kernel-debug.mount - Kernel Debug File System.
      [    8.072327] systemd[1]: Mounted tmp.mount - Temporary Directory /tmp.
      [  OK  ] Mounted tmp.mount - Temporary Directory /tmp.
      [    8.107837] systemd-journald[87]: Collecting audit messages is disabled.
      [    8.115571] systemd[1]: fake-hwclock-load.service: Deactivated successfully.
      [    8.131936] systemd[1]: Finished fake-hwclock-load.service - Restore the current clock.
      [  OK  ] Finished fake-hwclock-load.service - Restore the current clock.
      [    8.186073] systemd[1]: modprobe@configfs.service: Deactivated successfully.
      [    8.201937] systemd[1]: Finished modprobe@configfs.service - Load Kernel Module configfs.
      [  OK  ] Finished modprobe@configfs.service - Load Kernel Module configfs.
      [    8.222911] systemd[1]: modprobe@drm.service: Deactivated successfully.
      [    8.241361] systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
      [  OK  ] Finished modprobe@drm.service - Load Kernel Module drm.
      [    8.262976] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
      [    8.281377] systemd[1]: Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
      [  OK  ] Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
      [    8.302854] systemd[1]: modprobe@fuse.service: Deactivated successfully.
      [    8.331108] systemd[1]: Finished modprobe@fuse.service - Load Kernel Module fuse.
      [  OK  ] Finished modprobe@fuse.service - Load Kernel Module fuse.
      [    8.362118] systemd[1]: Started systemd-journald.service - Journal Service.
      [  OK  ] Started systemd-journald.service - Journal Service.
      [  OK  ] Finished systemd-modules-load.service - Load Kernel Modules.
      [  OK  ] Finished systemd-tmpfiles-setup-de…ic Device Nodes in /dev gracefully.
      [  OK  ] Finished systemd-udev-load-credent…- Load udev Rules from Credentials.
               Mounting sys-fs-fuse-connections.mount - FUSE Control File System...
               Mounting sys-kernel-config.mount - Kernel Configuration File System...
               Starting systemd-remount-fs.servic…unt Root and Kernel File Systems...
               Starting systemd-sysctl.service - Apply Kernel Variables...
      [  OK  ] Mounted sys-fs-fuse-connections.mount - FUSE Control File System.
      [  OK  ] Mounted sys-kernel-config.mount - Kernel Configuration File System.
      [  OK  ] Finished systemd-sysctl.service - Apply Kernel Variables.
      [  OK  ] Finished systemd-udev-trigger.service - Coldplug All udev Devices.
               Starting ifupdown-pre.service - He…synchronize boot up for ifupdown...
               Starting systemd-udev-settle.servi…o Complete Device Initialization...
      [  OK  ] Finished systemd-remount-fs.servic…mount Root and Kernel File Systems.
      [  OK  ] Finished ifupdown-pre.service - He…o synchronize boot up for ifupdown.
               Starting systemd-journal-flush.ser…sh Journal to Persistent Storage...
               Starting systemd-random-seed.service - Load/Save OS Random Seed...
               Starting systemd-tmpfiles-setup-de…eate Static Device Nodes in /dev...
      [  OK  ] Finished systemd-tmpfiles-setup-de…Create Static Device Nodes in /dev.
      [  OK  ] Reached target local-fs-pre.target…Preparation for Local File Systems.
               Starting systemd-udevd.service - R…ager for Device Events and Files...
      [  OK  ] Finished systemd-journal-flush.ser…lush Journal to Persistent Storage.
      [  OK  ] Finished systemd-random-seed.service - Load/Save OS Random Seed.
      [  OK  ] Started systemd-udevd.service - Ru…anager for Device Events and Files.
               Starting plymouth-start.service - Show Plymouth Boot Screen...
      [  OK  ] Found device dev-ttyS0.device - /dev/ttyS0.
      socfpga-dwmac ff702000.ethernet: Unable to parse OF data
      socfpga-dwmac ff702000.ethernet: probe with driver socfpga-dwmac failed with error -524
      systemd[1]: Failed to find module 'autofs4'
      [  OK  ] Started plymouth-start.service - Show Plymouth Boot Screen.
      [  OK  ] Found device dev-disk-by\x2dpartuu… /dev/disk/by-partuuid/d29065e8-01.
      [  OK  ] Started systemd-ask-password-plymo…quests to Plymouth Directory Watch.
      [  OK  ] Reached target paths.target - Path Units.
               Starting systemd-fsck@dev-disk-by\…dev/disk/by-partuuid/d29065e8-01...
      [  OK  ] Finished systemd-udev-settle.servi… To Complete Device Initialization.
      [  OK  ] Finished systemd-fsck@dev-disk-by\… /dev/disk/by-partuuid/d29065e8-01.
               Mounting boot.mount - /boot...
      [  OK  ] Mounted boot.mount - /boot.
      [  OK  ] Reached target local-fs.target - Local File Systems.
      [  OK  ] Listening on systemd-sysext.socket… System Extension Image Management.
               Starting networking.service - Raise network interfaces...
               Starting plymouth-read-write.servi…ymouth To Write Out Runtime Data...
               Starting systemd-tmpfiles-setup.se…ate System Files and Directories...
      [  OK  ] Finished plymouth-read-write.servi…Plymouth To Write Out Runtime Data.
      [  OK  ] Finished systemd-tmpfiles-setup.se…reate System Files and Directories.
      [  OK  ] Reached target sysinit.target - System Initialization.
      [  OK  ] Started apt-daily.timer - Daily apt download activities.
      [  OK  ] Started apt-daily-upgrade.timer - …y apt upgrade and clean activities.
      [  OK  ] Started dpkg-db-backup.timer - Daily dpkg database backup timer.
      [  OK  ] Started e2scrub_all.timer - Period…Metadata Check for All Filesystems.
      [  OK  ] Started fake-hwclock-save.timer - Periodically save current clock.
      [  OK  ] Started fstrim.timer - Discard unused filesystem blocks once a week.
      [  OK  ] Started logrotate.timer - Daily rotation of log files.
      [  OK  ] Started man-db.timer - Daily man-db regeneration.
      [  OK  ] Started ntpsec-rotate-stats.timer - Rotate ntpd stats daily.
      [  OK  ] Started systemd-tmpfiles-clean.tim…y Cleanup of Temporary Directories.
      [  OK  ] Reached target timers.target - Timer Units.
      [  OK  ] Listening on avahi-daemon.socket -…DNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on dbus.socket - D-Bus System Message Bus Socket.
      [  OK  ] Listening on sshd-unix-local.socke…temd-ssh-generator, AF_UNIX Local).
      [  OK  ] Listening on systemd-hostnamed.socket - Hostname Service Socket.
      [  OK  ] Reached target sockets.target - Socket Units.
      [  OK  ] Reached target basic.target - Basic System.
               Starting accounts-daemon.service - Accounts Service...
               Starting adi-power.service - Analog Devices power up/down sequence...
               Starting avahi-daemon.service - Avahi mDNS/DNS-SD Stack...
               Starting blueman-mechanism.service - Bluetooth management mechanism...
      [  OK  ] Started cron.service - Regular background program processing daemon.
               Starting dbus.service - D-Bus System Message Bus...
               Starting e2scrub_reap.service - Re…ne ext4 Metadata Check Snapshots...
      [  OK  ] Started fan-control.service - fan-control.
               Starting fix-display-port.service - Fix DP audio and X11...
               Starting iiod_context_attr.service…ating IIOD Context Attributes......
               Starting systemd-logind.service - User Login Management...
               Starting udisks2.service - Disk Manager...
               Starting xserver.service - ADI X Server...
      [  OK  ] Finished fix-display-port.service - Fix DP audio and X11.
      [  OK  ] Started dbus.service - D-Bus System Message Bus.
               Starting NetworkManager.service - Network Manager...
               Starting wpa_supplicant.service - WPA supplicant...
      [  OK  ] Started avahi-daemon.service - Avahi mDNS/DNS-SD Stack.
      [  OK  ] Finished networking.service - Raise network interfaces.
               Starting polkit.service - Authorization Manager...
      [  OK  ] Started systemd-logind.service - User Login Management.
      [  OK  ] Finished adi-power.service - Analog Devices power up/down sequence.
      [  OK  ] Started wpa_supplicant.service - WPA supplicant.
      [  OK  ] Finished iiod_context_attr.service…reating IIOD Context Attributes....
      [  OK  ] Created slice user-1000.slice - User Slice of UID 1000.
               Starting user-runtime-dir@1000.ser…Runtime Directory /run/user/1000...
               Starting systemd-hostnamed.service - Hostname Service...
      [  OK  ] Finished e2scrub_reap.service - Re…line ext4 Metadata Check Snapshots.
      [  OK  ] Started polkit.service - Authorization Manager.
      [  OK  ] Finished user-runtime-dir@1000.ser…r Runtime Directory /run/user/1000.
      [  OK  ] Started accounts-daemon.service - Accounts Service.
      [  OK  ] Started udisks2.service - Disk Manager.
      [  OK  ] Started systemd-hostnamed.service - Hostname Service.
               Starting NetworkManager-dispatcher…anager Script Dispatcher Service...
      [  OK  ] Started NetworkManager.service - Network Manager.
      [  OK  ] Reached target network.target - Network.
               Starting htpdate.service - HTTP based time synchronization tool...
      [  OK  ] Started iiod.service - IIO Daemon.
               Starting ntpsec.service - Network Time Service...
               Starting ssh.service - OpenBSD Secure Shell server...
               Starting systemd-user-sessions.service - Permit User Sessions...
      [  OK  ] Started udiskie.service - Udiskie …rvice for managing removable media.
      [  OK  ] Started NetworkManager-dispatcher.… Manager Script Dispatcher Service.
      [  OK  ] Started ntpsec.service - Network Time Service.
      [  OK  ] Started htpdate.service - HTTP based time synchronization tool.
      [  OK  ] Finished systemd-user-sessions.service - Permit User Sessions.
               Starting plymouth-quit-wait.servic…d until boot process finishes up...
               Starting user@1000.service - User Manager for UID 1000...
      [  OK  ] Started ssh.service - OpenBSD Secure Shell server.
      [  OK  ] Started blueman-mechanism.service - Bluetooth management mechanism.
      [  OK  ] Started user@1000.service - User Manager for UID 1000.
      [  OK  ] Started session-c1.scope - Session c1 of User analog.
               Starting rtkit-daemon.service - Re…imeKit Scheduling Policy Service...
      [  OK  ] Finished xserver.service - ADI X Server.
               Starting lightdm.service - Light Display Manager...
               Starting x11vnc.service - VNC Server for X11...
      [  OK  ] Started rtkit-daemon.service - RealtimeKit Scheduling Policy Service.

      Debian GNU/Linux 13 analog ttyS0

      analog login: root (automatic login)

      Linux analog 6.12.77-ge2f9fe8e3654 #1 SMP Thu Mar 26 11:56:56 UTC 2026 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      root@analog:~#

Getting remote information
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect USB UART (Micro USB) to your host PC.
- Plug your ethernet cable into the RJ45 ethernet connector
- Run the ifconfig command on your UART terminal and get your board IP

::

   root@analog:~# ifconfig

   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet your_board_ip  netmask 255.255.255.0  broadcast
           inet6 fe80::e6e7:b2c:f962:dc57  prefixlen 64  scopeid 0x20<link>
           ether 1c:76:ca:01:23:45  txqueuelen 1000  (Ethernet)
           RX packets 25208  bytes 4726181 (4.5 MiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 5987  bytes 2260634 (2.1 MiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
           device interrupt 29  base 0x2000

Remote IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~

- Open IIO Scope application and type ip:board_ip in the URI tab.

.. image:: ../images/iio_remote_c5soc_arradio.png
   :alt: iio_remote_c5soc_arradio.png
   :align: center
   :width: 600

- Below it's an example on how to configure the setup to 2.3 GHz and visualise
  the frequency domain (loopback between TX1A and RX2A).

.. image:: ../images/iio_remote_c5soc_arradio_2.png
   :align: center
   :width: 600

.. image:: ../images/iio_remote_c5soc_arradio_3.png
   :align: center
   :width: 600

Remote Scopy
~~~~~~~~~~~~

- Open Scopy application, click on the "+" and type ip:board_ip in the URI tab.
- Connect to the device

.. image:: ../images/scopy_remote_c5soc_arradio_1.png
   :align: center
   :width: 600

- Below it's an example on how to configure the setup and visualise the
  frequency domain (loopback between TX1A and RX2A).

.. image:: ../images/scopy_remote_c5soc_arradio_2.png
   :align: center
   :width: 600

.. image:: ../images/scopy_remote_c5soc_arradio_3.png
   :align: center
   :width: 600

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be
   taken not to corrupt the file system -- please shut down things, don't just
   turn off the power switch. Depending on your monitor, the standard power off
   could be hiding. You can do this from the terminal as well with ``sudo
   shutdown -h now``

   .. image:: ../images/shutdown.png
      :width: 300

More Information
----------------

- :doc:`ARRADIO User Guide </solutions/reference-designs/arradio/index>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.