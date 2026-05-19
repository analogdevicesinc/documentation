.. _eval-cn0579-ardz quickstart de10-nano:

DE10-Nano
===============================================================================

Hardware Setup
-------------------------------------------------------------------------------

.. figure:: ../images/de10_nano_setup_top.jpeg
   :alt: DE10-Nano with EVAL-CN0579-ARDZ mounted (top view)
   :width: 800

   DE10-Nano with EVAL-CN0579-ARDZ mounted (top view).

.. figure:: ../images/de10_nano_setup_side.jpeg
   :alt: DE10-Nano with EVAL-CN0579-ARDZ mounted (side view)
   :width: 800

   DE10-Nano with EVAL-CN0579-ARDZ mounted (side view).

#. Mount the :adi:`EVAL-CN0579-ARDZ` onto the DE10-Nano via the Arduino
   headers.
#. Connect a Mini-USB cable from the DE10-Nano's UART port to the host PC.
#. Connect an Ethernet cable from the DE10-Nano to the host PC or network switch.
#. Connect a signal generator to the :adi:`EVAL-CN0579-ARDZ` analog
   inputs using SMA cables.
#. Insert the microSD card with the ADI Kuiper Linux image into the microSD
   card slot on the DE10-Nano.
#. Open a serial terminal of your choice (e.g. PuTTY, Tera Term) on the host PC
   configured to 115200 baud, 8N1.
#. Plug in the DE10-Nano power supply.
#. Wait for the system to boot. Boot messages will appear in the serial
   terminal.

Software Setup
-------------------------------------------------------------------------------

Preparing the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download and flash the :external+kuiper:doc:`ADI Kuiper Linux <index>` image
   to a 16 GB (or larger) microSD card. Follow the
   :external+kuiper:doc:`Use Kuiper Image <use-kuiper-image>` guide for
   instructions.
#. Mount the FAT32 BOOT partition of the SD card and copy the following files
   to its root:

   - ``socfpga_cyclone5_common/zImage``
   - ``<target_project>/u-boot.scr``
   - ``<target_project>/socfpga.dtb``
   - ``<target_project>/soc_system.rbf``

#. Create the ``extlinux`` folder at the root of the BOOT partition and place
   the ``extlinux.conf`` file inside it:

   .. code-block:: bash

      mkdir -p /media/$USER/BOOT/extlinux
      cp socfpga_cyclone5_common/extlinux.conf /media/$USER/BOOT/extlinux/extlinux.conf

#. Write the U-Boot SPL image to the third SD card partition (raw, not a
   filesystem):

   .. code-block:: bash

      dd if=<target_project>/u-boot-with-spl.sfp of=/dev/sdX3 bs=64k && sync

   Replace ``/dev/sdX3`` with the correct device node for your SD card
   (e.g. ``/dev/sdd3``). Use ``lsblk`` to identify it.

#. Safely unmount the SD card and insert it into the microSD card slot on the
   DE10-Nano.

Boot Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After powering the board, the following boot sequence is expected:

.. collapsible:: DE10-Nano boot log

   ::

      U-Boot SPL 2021.10-17979-ge7beb4cb47f-dirty (May 12 2026 - 16:53:52 +0100)
      Trying to boot from MMC1

      U-Boot 2021.10-17979-ge7beb4cb47f-dirty (May 12 2026 - 16:53:52 +0100), Build: jenkins-hdl_2026_r1-builds-hdl_2026_r1_latest_commit-projects-cn0579.de10nano-19

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
      Warning: ethernet@ff702000 (eth0) using random MAC address - 66:bd:44:e1:f5:d0
      eth0: ethernet@ff702000
      Hit any key to stop autoboot:  0
      150 bytes read in 7 ms (20.5 KiB/s)
      ## Executing script at 02100000
      2513308 bytes read in 131 ms (18.3 MiB/s)
      switch to partitions #0, OK
      mmc0 is current device
      Scanning mmc 0:1...
      Found /extlinux/extlinux.conf
      Retrieving file: /extlinux/extlinux.conf
      142 bytes read in 8 ms (16.6 KiB/s)
      1:      Linux Default
      Retrieving file: /extlinux/../zImage
      10229904 bytes read in 513 ms (19 MiB/s)
      append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      Retrieving file: /extlinux/../socfpga.dtb
      31663 bytes read in 11 ms (2.7 MiB/s)
      Kernel image @ 0x1000000 [ 0x000000 - 0x9c1890 ]
      ## Flattened Device Tree blob at 02000000
         Booting using the fdt blob at 0x2000000
         Loading Device Tree to 09ff5000, end 09fffbae ... OK

      Starting kernel ...

      Deasserting all peripheral resets
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 6.12.77-g0d285126d15a (root@1e165a90fec8) (arm-linux-gnueabi-gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #1 SMP Fri May  8 12:42:12 UTC 2026
      [    0.000000] CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=10c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Terasic DE10-Nano
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
      [    0.000000] percpu: Embedded 16 pages/cpu s33804 r8192 d23540 u65536
      [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      [    0.000000] Unknown kernel command line parameters "earlyprintk", will be passed to user space.
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 262144
      [    0.000000] mem auto-init: stack:all(zero), heap alloc:off, heap free:off
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000]  Tracing variant of Tasks RCU enabled.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] RCU Tasks Trace: Setting shift to 1 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=2.
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
      [    0.000015] Switching to timer-based delay loop, resolution 10ns
      [    0.000481] Console: colour dummy device 80x30
      [    0.000530] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.000544] CPU: Testing write buffer coherency: ok
      [    0.000586] CPU0: Spectre v2: using BPIALL workaround
      [    0.000594] pid_max: default: 32768 minimum: 301
      [    0.000738] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000754] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.001576] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.003143] Setting up static identity map for 0x100000 - 0x100060
      [    0.003376] rcu: Hierarchical SRCU implementation.
      [    0.003383] rcu:     Max phase no-delay instances is 1000.
      [    0.004112] smp: Bringing up secondary CPUs ...
      [    0.005068] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.005089] CPU1: Spectre v2: using BPIALL workaround
      [    0.005264] smp: Brought up 1 node, 2 CPUs
      [    0.005277] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.005286] CPU: All CPU(s) started in SVC mode.
      [    0.005802] Memory: 874668K/1048576K available (15360K kernel code, 1570K rwdata, 11676K rodata, 1024K init, 505K bss, 40004K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.006368] devtmpfs: initialized
      [    0.012059] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.012287] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.012309] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.018538] NET: Registered PF_NETLINK/PF_ROUTE protocol family
      [    0.020460] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.021608] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.021622] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.029008] /soc/i2c@ffc04000/adv7513@39: Fixed dependency cycle(s) with /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000
      [    0.029231] /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000: Fixed dependency cycle(s) with /soc/i2c@ffc04000/adv7513@39
      [    0.031332] /soc/i2c@ffc04000/adv7513@39: Fixed dependency cycle(s) with /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000
      [    0.035556] /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000: Fixed dependency cycle(s) with /soc/i2c@ffc04000/adv7513@39
      [    0.036354] /soc/i2c@ffc04000/adv7513@39: Fixed dependency cycle(s) with /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000
      [    0.036441] /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000: Fixed dependency cycle(s) with /soc/i2c@ffc04000/adv7513@39
      [    0.047906] SCSI subsystem initialized
      [    0.048134] usbcore: registered new interface driver usbfs
      [    0.048175] usbcore: registered new interface driver hub
      [    0.048215] usbcore: registered new device driver usb
      [    0.048378] usb_phy_generic soc:usbphy: dummy supplies not allowed for exclusive requests (id=vbus)
      [    0.048841] mc: Linux media interface: v0.10
      [    0.048893] videodev: Linux video capture interface: v2.00
      [    0.048971] pps_core: LinuxPPS API ver. 1 registered
      [    0.048977] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.048995] PTP clock support registered
      [    0.049288] jesd204: found 0 devices and 0 topologies
      [    0.049354] FPGA manager framework
      [    0.049444] Advanced Linux Sound Architecture Driver Initialized.
      [    0.051160] debugfs: Directory 'fixed-supply' with parent 'regulator' already present!
      [    0.051344] vgaarb: loaded
      [    0.052222] clocksource: Switched to clocksource timer1
      [    0.062450] NET: Registered PF_INET protocol family
      [    0.062683] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
      [    0.064502] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes, linear)
      [    0.064531] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.064548] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.064625] TCP bind hash table entries: 8192 (order: 5, 131072 bytes, linear)
      [    0.064855] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.064966] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.065011] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.065192] NET: Registered PF_UNIX/PF_LOCAL protocol family
      [    0.066494] RPC: Registered named UNIX socket transport module.
      [    0.066505] RPC: Registered udp transport module.
      [    0.066509] RPC: Registered tcp transport module.
      [    0.066513] RPC: Registered tcp-with-tls transport module.
      [    0.066517] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.066534] PCI: CLS 0 bytes, default 64
      [    0.068076] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.068799] NFS: Registering the id_resolver key type
      [    0.068875] Key type id_resolver registered
      [    0.068881] Key type id_legacy registered
      [    0.069169] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.069259] fuse: init (API version 7.41)
      [    0.069664] bounce: pool size: 64 pages
      [    0.069693] io scheduler mq-deadline registered
      [    0.069701] io scheduler kyber registered
      [    0.069725] io scheduler bfq registered
      [    0.071531] ledtrig-cpu: registered to indicate activity on CPUs
      [    0.079960] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.081440] printk: legacy console [ttyS0] disabled
      [    0.081877] ffc02000.serial: ttyS0 at MMIO 0xffc02000 (irq = 30, base_baud = 6250000) is a 16550A
      [    0.081927] printk: legacy console [ttyS0] enabled
      [    0.835046] ffc03000.serial: ttyS1 at MMIO 0xffc03000 (irq = 31, base_baud = 6250000) is a 16550A
      [    0.847790] brd: module loaded
      [    0.853515] spi_altera ff30a000.spi: regoff 0, irq 32
      [    0.859871] spi_altera ff308000.spi: regoff 0, irq 33
      [    0.867444] CAN device driver interface
      [    0.871654] socfpga-dwmac ff702000.ethernet: IRQ eth_wake_irq not found
      [    0.878282] socfpga-dwmac ff702000.ethernet: IRQ eth_lpi not found
      [    0.884473] socfpga-dwmac ff702000.ethernet: IRQ sfty not found
      [    0.890440] socfpga-dwmac ff702000.ethernet: Deprecated MDIO bus assumption used
      [    0.897902] socfpga-dwmac ff702000.ethernet: PTP uses main clock
      [    0.903918] socfpga-dwmac ff702000.ethernet: No sysmgr-syscon node found
      [    0.910598] socfpga-dwmac ff702000.ethernet: Unable to parse OF data
      [    0.916955] socfpga-dwmac ff702000.ethernet: probe with driver socfpga-dwmac failed with error -524
      [    0.926631] stmmaceth ff702000.ethernet: IRQ eth_wake_irq not found
      [    0.932949] stmmaceth ff702000.ethernet: IRQ eth_lpi not found
      [    0.938769] stmmaceth ff702000.ethernet: IRQ sfty not found
      [    0.944408] stmmaceth ff702000.ethernet: Deprecated MDIO bus assumption used
      [    0.951503] stmmaceth ff702000.ethernet: PTP uses main clock
      [    0.960932] stmmaceth ff702000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    0.967763] stmmaceth ff702000.ethernet:     DWMAC1000
      [    0.972652] stmmaceth ff702000.ethernet: DMA HW capability register supported
      [    0.979764] stmmaceth ff702000.ethernet: RX Checksum Offload Engine supported
      [    0.986888] stmmaceth ff702000.ethernet: COE Type 2
      [    0.991753] stmmaceth ff702000.ethernet: TX Checksum insertion supported
      [    0.998441] stmmaceth ff702000.ethernet: Enhanced/Alternate descriptors
      [    1.005042] stmmaceth ff702000.ethernet: Enabled extended descriptors
      [    1.011460] stmmaceth ff702000.ethernet: Ring mode enabled
      [    1.016936] stmmaceth ff702000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    1.024604] stmmaceth ff702000.ethernet: device MAC address 6e:96:d2:a2:49:b2
      [    1.042882] Micrel KSZ9031 Gigabit PHY stmmac-1:01: attached PHY driver (mii_bus:phy_addr=stmmac-1:01, irq=POLL)
      [    1.054429] usbcore: registered new interface driver asix
      [    1.059862] usbcore: registered new interface driver ax88179_178a
      [    1.066015] usbcore: registered new interface driver cdc_ether
      [    1.071871] usbcore: registered new interface driver net1080
      [    1.077578] usbcore: registered new interface driver cdc_subset
      [    1.083557] usbcore: registered new interface driver zaurus
      [    1.089156] usbcore: registered new interface driver cdc_ncm
      [    1.094862] usbcore: registered new interface driver r8153_ecm
      [    1.101519] dwc2 ffb40000.usb: supply vusb_d not found, using dummy regulator
      [    1.108810] dwc2 ffb40000.usb: supply vusb_a not found, using dummy regulator
      [    1.116289] dwc2 ffb40000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    1.124269] dwc2 ffb40000.usb: DWC OTG Controller
      [    1.128992] dwc2 ffb40000.usb: new USB bus registered, assigned bus number 1
      [    1.136067] dwc2 ffb40000.usb: irq 35, io mem 0xffb40000
      [    1.141597] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.12
      [    1.149863] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.157084] usb usb1: Product: DWC OTG Controller
      [    1.161776] usb usb1: Manufacturer: Linux 6.12.77-g0d285126d15a dwc2_hsotg
      [    1.168647] usb usb1: SerialNumber: ffb40000.usb
      [    1.173901] hub 1-0:1.0: USB hub found
      [    1.177691] hub 1-0:1.0: 1 port detected
      [    1.183252] usbcore: registered new interface driver uas
      [    1.188625] usbcore: registered new interface driver usb-storage
      [    1.194746] usbcore: registered new interface driver usbserial_generic
      [    1.201285] usbserial: USB Serial support registered for generic
      [    1.207332] usbcore: registered new interface driver ftdi_sio
      [    1.213096] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.220463] usbcore: registered new interface driver upd78f0730
      [    1.226411] usbserial: USB Serial support registered for upd78f0730
      [    1.234307] i2c_dev: i2c /dev entries driver
      [    1.239164] usbcore: registered new interface driver uvcvideo
      [    1.247416] Synopsys Designware Multimedia Card Interface Driver
      [    1.253760] usbcore: registered new interface driver usbhid
      [    1.259318] usbhid: USB HID core driver
      [    1.262438] dw_mmc ff704000.mmc: clk-phase-sd-hs was specified, but failed to find altr,sys-mgr regmap!
      [    1.263424] SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      [    1.272536] dw_mmc ff704000.mmc: IDMAC supports 32-bit address mode.
      [    1.285965] dw_mmc ff704000.mmc: Using internal DMA controller.
      [    1.291891] dw_mmc ff704000.mmc: Version ID is 240a
      [    1.296873] dw_mmc ff704000.mmc: DW MMC controller at irq 37,32 bit host data width,1024 deep fifo
      [    1.306122] mmc_host mmc0: card is polling.
      [    1.322243] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.327902] cf_axi_adc ff230000.cf_axi_adc: ADI AIM (10.03.) probed ADC ad7768_4_axi_adc as MASTER
      [    1.349899] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 (8000003f) counters available
      [    1.359379] axi_sysid ff218000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    1.367513] axi_sysid ff218000.axi-sysid-0: [cn0579] on [de10nano] git branch <hdl_2026_r1> git <35b7afa0dd458ea7d268622d35a97fd992ad144d> clean [2026-05-12 15:19:09] UTC
      [    1.380890] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.383404] fpga_manager fpga0: Altera SOCFPGA FPGA Manager registered
      [    1.392532] mmc0: new high speed SDHC card at address 0001
      [    1.399899] usbcore: registered new interface driver snd-usb-audio
      [    1.412817] mmcblk0: mmc0:0001 USD 29.1 GiB
      [    1.412934] NET: Registered PF_INET6 protocol family
      [    1.424227] Segment Routing with IPv6
      [    1.427957] In-situ OAM (IOAM) with IPv6
      [    1.431948] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.432604]  mmcblk0: p1 p2 p3
      [    1.438533] NET: Registered PF_PACKET protocol family
      [    1.445982] NET: Registered PF_KEY protocol family
      [    1.450993] can: controller area network core
      [    1.455417] NET: Registered PF_CAN protocol family
      [    1.460200] can: raw protocol
      [    1.463186] can: broadcast manager protocol
      [    1.467365] can: netlink gateway - max_hops=1
      [    1.471768] 8021q: 802.1Q VLAN Support v1.8
      [    1.475989] NET: Registered PF_IEEE802154 protocol family
      [    1.481402] Key type dns_resolver registered
      [    1.485842] ThumbEE CPU extension supported.
      [    1.490111] Registering SWP/SWPB emulation handler
      [    1.514387] /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000: Fixed dependency cycle(s) with /soc/i2c@ffc04000/adv7513@39
      [    1.525276] /soc/i2c@ffc04000/adv7513@39: Fixed dependency cycle(s) with /soc/axi_h2f_lw_bridge@ff200000/axi_hdmi@90000
      [    1.536313] adv7511 0-0039: supply avdd not found, using dummy regulator
      [    1.543162] adv7511 0-0039: supply dvdd not found, using dummy regulator
      [    1.549889] adv7511 0-0039: supply pvdd not found, using dummy regulator
      [    1.556660] adv7511 0-0039: supply bgvdd not found, using dummy regulator
      [    1.563495] adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
      [    1.585287] dma-pl330 ffe01000.pdma: Loaded driver for PL330 DMAC-341330
      [    1.591985] dma-pl330 ffe01000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    1.601330] [drm] Initialized axi_hdmi_drm 1.0.0 for ff290000.axi_hdmi on minor 0
      [    1.609712] axi-hdmi ff290000.axi_hdmi: [drm] Cannot find any crtc or sizes
      [    1.617277] of_cfs_init
      [    1.618562] axi-hdmi ff290000.axi_hdmi: [drm] Cannot find any crtc or sizes
      [    1.619758] of_cfs_init: OK
      [    1.629823] clk: Disabling unused clocks
      [    1.633810] ALSA device list:
      [    1.636773]   No soundcards found.
      [    1.640410] dw-apb-uart ffc02000.serial: forbid DMA for kernel console
      [    1.662985] EXT4-fs (mmcblk0p2): mounted filesystem 61c00ade-b582-4574-a434-d56f9cb59143 r/w with ordered data mode. Quota mode: disabled.
      [    1.675482] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    1.689689] devtmpfs: mounted
      [    1.694051] Freeing unused kernel image (initmem) memory: 1024K
      [    1.700658] Run /sbin/init as init process
      [    2.259814] systemd[1]: System time before build time, advancing clock.
      [    2.294493] systemd[1]: Failed to look up module alias 'autofs4': Function not implemented
      [    2.333313] systemd[1]: systemd 247.3-7+rpi1+deb11u6 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [    2.357231] systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

      [    2.403847] systemd[1]: Set hostname to <analog>.
      [    4.251050] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [    4.449793] systemd[1]: /lib/systemd/system/iiod.service:14: Invalid environment assignment, ignoring: $IIOD_EXTRA_OPTS=
      [    4.574954] systemd[1]: Queued start job for default target Graphical Interface.
      [    6.762226] random: crng init done
      [    6.766062] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    6.778408] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [    6.788372] systemd[1]: Created slice system-getty.slice.
      [  OK  ] Created slice system-getty.slice.
      [    6.823370] systemd[1]: Created slice system-modprobe.slice.
      [  OK  ] Created slice system-modprobe.slice.
      [    6.843320] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [    6.873358] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [    6.893030] systemd[1]: Created slice User and Session Slice.
      [  OK  ] Created slice User and Session Slice.
      [    6.922849] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [    6.952695] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [    6.965457] systemd[1]: Reached target Slices.
      [  OK  ] Reached target Slices.
      [    7.002582] systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      [    7.030695] systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [    7.053045] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [    7.082756] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [    7.142409] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
      [    7.151277] systemd[1]: Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket (/dev/log).
      [    7.183267] systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      [    7.241908] systemd[1]: Listening on udev Control Socket.
      [  OK  ] Listening on udev Control Socket.
      [    7.263060] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [    7.283112] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
      [    7.291809] systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
      [    7.342763] systemd[1]: Mounting RPC Pipe File System...
               Mounting RPC Pipe File System...
      [    7.375888] systemd[1]: Mounting Kernel Debug File System...
               Mounting Kernel Debug File System...
      [    7.395930] systemd[1]: Mounting Kernel Trace File System...
               Mounting Kernel Trace File System...
      [    7.412837] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [    7.428133] systemd[1]: Starting Restore / save the current clock...
               Starting Restore / save the current clock...
      [    7.463428] systemd[1]: Starting Set the console keyboard layout...
               Starting Set the console keyboard layout...
      [    7.485188] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [    7.503223] systemd[1]: Starting Load Kernel Module configfs...
               Starting Load Kernel Module configfs...
      [    7.531766] systemd[1]: Starting Load Kernel Module drm...
               Starting Load Kernel Module drm...
      [    7.558914] systemd[1]: Starting Load Kernel Module fuse...
               Starting Load Kernel Module fuse...
      [    7.586432] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [    7.596085] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [    7.653186] systemd[1]: Starting Journal Service...
               Starting Journal Service...
      [    7.687821] systemd[1]: Starting Load Kernel Modules...
               Starting Load Kernel Modules...
      [    7.733111] systemd[1]: Starting Remount Root and Kernel File Systems...
               Starting Remount Root and Kernel File Systems...
      [    7.766559] systemd[1]: Starting Coldplug All udev Devices...
               Starting Coldplug All udev Devices...
      [    7.831577] systemd[1]: Mounted RPC Pipe File System.
      [  OK  ] Mounted RPC Pipe File System.
      [    7.883276] systemd[1]: Mounted Kernel Debug File System.
      [  OK  ] Mounted Kernel Debug File System.
      [    7.915130] systemd[1]: Mounted Kernel Trace File System.
      [  OK  ] Mounted Kernel Trace File System.
      [    7.954132] systemd[1]: Finished Restore / save the current clock.
      [  OK  ] Finished Restore / save the current clock.
      [    8.033108] systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
      [  OK  ] Finished Load Kernel Module configfs.
      [  OK  ] Finished Load Kernel Module drm.
      [  OK  ] Finished Load Kernel Module fuse.
      [    8.133304] EXT4-fs (mmcblk0p2): re-mounted 61c00ade-b582-4574-a434-d56f9cb59143.
      [  OK  ] Finished Set the console keyboard layout.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Finished Remount Root and Kernel File Systems.
               Mounting FUSE Control File System...
               Mounting Kernel Configuration File System...
               Starting Flush Journal to Persistent Storage...
               Starting Load/Save Random Seed...
               Starting Apply Kernel Variables...
               Starting Create System Users...
      [    8.434437] systemd-journald[102]: Received client request to flush runtime journal.
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.[    8.502371] systemd-journald[102]: File /var/log/journal/d1c174cf922348be8fb806d50779aab2/system.journal corrupted or uncleanly shut down, renaming and replacing.

      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Finished Apply Kernel Variables.
      [  OK  ] Finished Coldplug All udev Devices.
      [  OK  ] Finished Create System Users.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Create Static Device Nodes in /dev...
               Starting Wait for udev To …plete Device Initialization...
      [  OK  ] Finished Flush Journal to Persistent Storage.
      [  OK  ] Finished Helper to synchronize boot up for ifupdown.
      [  OK  ] Finished Create Static Device Nodes in /dev.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting Rule-based Manage…for Device Events and Files...
      [  OK  ] Started Rule-based Manager for Device Events and Files.
               Starting Show Plymouth Boot Screen...
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Found device /dev/disk/by-partuuid/5c29002e-01.
      [  OK  ] Found device /dev/ttyS0.
      [  OK  ] Reached target Hardware activated USB gadget.
               Starting File System Check…isk/by-partuuid/5c29002e-01...
               Starting Load Kernel Modules...
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
      [  OK  ] Started File System Check Daemon to report status.
      [  OK  ] Finished File System Check…/disk/by-partuuid/5c29002e-01.
               Mounting /boot...
      [  OK  ] Mounted /boot.
      [  OK  ] Reached target Local File Systems.
               Starting Set console font and keymap...
               Starting Raise network interfaces...
               Starting Preprocess NFS configuration...
               Starting Tell Plymouth To Write Out Runtime Data...
               Starting Create Volatile Files and Directories...
      [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Finished Set console font and keymap.
      [  OK  ] Finished Preprocess NFS configuration.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
      [  OK  ] Finished Create Volatile Files and Directories.
               Starting Network Time Synchronization...
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Finished Update UTMP about System Boot/Shutdown.
               Starting Load Kernel Modules...
      [  OK  ] Started Network Time Synchronization.
      [  OK  ] Finished Raise network interfaces.
      [  OK  ] Reached target System Time Set.
      [  OK  ] Reached target System Time Synchronized.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
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
               Starting Avahi mDNS/DNS-SD Stack...
      [  OK  ] Started Regular background program processing daemon.
      [  OK  ] Started D-Bus System Message Bus.
               Starting dphys-swapfile - …unt, and delete a swap file...
               Starting Remove Stale Onli…t4 Metadata Check Snapshots...
      [  OK  ] Started fan-control.
               Starting Fix DP audio and X11 for Jupiter...
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
      [  OK  ] Finished Fix DP audio and X11 for Jupiter.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started DHCP Client Daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
      [  OK  ] Started User Login Management.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started WPA supplicant.
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
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Finished Load USB gadget scheme.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started Authorization Manager.
      [  OK  ] Found device /dev/ttyGS0.
               Mounting Mount FunctionFS instance...
               Starting Modem Manager...
      [  OK  ] Started Internet superserver.
      [  OK  ] Finished Permit User Sessions.
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Mounted Mount FunctionFS instance.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [  OK  ] Started Disk Manager.
      [  OK  ] Finished Creating IIOD Context Attributes....
      [  OK  ] Started IIO Daemon.
               Starting IIO Daemon with USB FFS support...
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Finished Analog Devices power up/down sequence.
      [  OK  ] Finished Hold until boot process finishes up.
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyS0

      analog login: root (automatic login)

      Linux analog 6.12.77-g0d285126d15a #1 SMP Fri May  8 12:42:12 UTC 2026 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Fri Nov  8 15:12:39 GMT 2024 on ttyS0
      root@analog:~#

Install IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install one of the following tools on your PC:

- :ref:`iio-oscilloscope` - the classic IIO-based waveform viewer
- :external+scopy:doc:`Scopy <index>` - a more modern alternative with a
  built-in IIO plugin that can connect to the board over the network

Connecting to the Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open IIO Oscilloscope and connect to the board using its IP address over the
network. Use the ``ifconfig`` command on the serial terminal to find the
board's IP address.

.. figure:: ../images/cn0579_iio_connect_de10.jpeg
   :alt: IIO Oscilloscope connection dialog
   :width: 800

   IIO Oscilloscope - connecting to the board via IP address.

Configure the device settings as needed from the configuration panel.

.. figure:: ../images/cn0579_iio_conf_de10.jpeg
   :alt: IIO Oscilloscope configuration panel
   :width: 800

   IIO Oscilloscope - device configuration panel.

Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the DMM panel to read instantaneous ADC channel values.

.. figure:: ../images/cn0579_iio_dmm_de10.jpeg
   :alt: IIO Oscilloscope DMM panel
   :width: 800

   IIO Oscilloscope - DMM panel showing ADC channel readings.

Switch to the oscilloscope view to capture waveforms in the time domain.

.. figure:: ../images/cn0579_iio_capture_de10.jpeg
   :alt: IIO Oscilloscope time-domain capture
   :width: 800

   IIO Oscilloscope - time-domain waveform capture.

For frequency-domain analysis, switch to the FFT view.

.. figure:: ../images/cn0579_iio_capture_freq_de10.jpeg
   :alt: IIO Oscilloscope frequency-domain capture
   :width: 800

   IIO Oscilloscope - frequency-domain (FFT) capture.

Useful Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the network interface and assigned IP address:

.. shell::

   $ifconfig

List all IIO devices detected by the kernel:

.. shell::

   $iio_info -s

Power off the board safely:

.. shell::

   $poweroff

PyADI-IIO
-------------------------------------------------------------------------------

:ref:`pyadi-iio` is a Python abstraction layer for ADI hardware with IIO
drivers. It provides a device-specific API for the CN0579 that makes it easy
to stream data directly into Python without dealing with the low-level IIO
interface.

Follow the :ref:`pyadi-iio` page for installation instructions, then run the
CN0579 example script connecting to the board's IP address.

Capturing a single channel:

.. figure:: ../images/cn0579_py_1_channel_de10.jpeg
   :alt: PyADI-IIO single channel capture
   :width: 800

   PyADI-IIO - single channel data capture.

Capturing two channels simultaneously:

.. figure:: ../images/cn0579_py_2_channels_de10.jpeg
   :alt: PyADI-IIO two channel capture
   :width: 800

   PyADI-IIO - two channel data capture.
