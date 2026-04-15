.. _eval-ad777x quickstart zed:

ZedBoard Quick start
===============================================================================

.. figure:: ../images/zed_board.jpeg
   :alt: ZedBoard

   ZedBoard

.. esd-warning::

This guide provides step-by-step instructions on how to set up the
:adi:`EVAL-AD7770-AD7779` on:

- `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
  on the FMC LPC connector

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``BOOT.BIN`` - pre-built boot binary for the EVAL-AD777x on ZedBoard
- ``uImage`` - Linux kernel image
- ``devicetree.dtb`` - device tree blob for the ZedBoard + EVAL-AD777x

These files are available as part of the ADI Kuiper Linux image.
They replace the corresponding files on the FAT boot partition of
a Kuiper Linux SD card. See :ref:`eval-ad777x prerequisites` for
details.

.. note::

   To build these files from source instead of using the pre-built
   downloads, build the HDL project with:

   .. shell::

      $cd hdl/projects/ad777x_fmcz/zed
      $make

   Full build instructions are at
   :external+hdl:ref:`Build an HDL project <build_hdl>`.

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- A UART terminal (e.g. PuTTY, Tera Term, Minicom) at 115200 baud
  (8N1)
- :external+kuiper:ref:`use-kuiper-image` - for flashing the root
  filesystem to the SD card

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
  FPGA board and its power supply
- :adi:`EVAL-AD7770-AD7779` evaluation board
- Micro-SD card (16 GB or larger)
- Micro-USB cable (for UART)
- Ethernet cable connected to a router or switch

Testing
-------------------------------------------------------------------------------

Creating the setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/zed_setup.jpeg
   :alt: ZedBoard with EVAL-AD7770-AD7779 mounted on the FMC LPC
         connector, showing UART and Ethernet connections
   :width: 800

   ZedBoard with EVAL-AD7770-AD7779 hardware setup

Follow the steps below in order to avoid damaging the components:

#. Prepare the SD card:

   a. Flash the Kuiper Linux image to the SD card. See
      :external+kuiper:ref:`use-kuiper-image` for instructions.
   b. After flashing, mount the FAT boot partition and replace the
      ``BOOT.BIN``, ``uImage``, and ``devicetree.dtb``.
   c. Safely unmount and eject the SD card.

#. Configure the ZedBoard for SD card boot mode and set the VADJ
   voltage as shown in the figure below:

   .. figure:: ../images/zed_vadj_sd_boot.jpeg
      :alt: ZedBoard jumper settings for VADJ voltage and SD card boot
            mode selection
      :width: 600

      ZedBoard VADJ and SD boot mode jumper configuration

#. Insert the :adi:`EVAL-AD7770-AD7779` evaluation board into the FMC
   LPC connector on the ZedBoard.
#. Insert the prepared SD card into the ZedBoard SD slot.
#. Connect the Micro-USB cable to the UART port on the ZedBoard and
   open a terminal at 115200 baud, 8N1.
#. Connect an Ethernet cable from your router or switch to the
   ZedBoard Ethernet port.
#. Power on the ZedBoard.
#. Observe boot messages on the serial terminal.

Boot messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once powered on, U-Boot loads the kernel image and device tree from
the SD card, then boots into Kuiper Linux. The complete boot sequence
is shown below.

.. collapsible:: Complete boot log

   ::

      U-Boot 2018.01-21442-gf06dec3cab (Mar 12 2025 - 16:44:08 +0200), Build: jenkins-development-build_uboot-63

      Model: Zynq Zed Development Board
      Board: Xilinx Zynq
      Silicon: v3.1
      DRAM:  ECC disabled 512 MiB
      MMC:   sdhci@e0100000: 0 (SD)
      SF: Detected s25fl256s_64k with page size 256 Bytes, erase size 64 KiB, total 32 MiB
      In:    serial@e0001000
      Out:   serial@e0001000
      Err:   serial@e0001000
      Net:   ZYNQ GEM: e000b000, phyaddr 0, interface rgmii-id
      eth0: ethernet@e000b000
      reading uEnv.txt
      407 bytes read in 22 ms (17.6 KiB/s)
      Importing environment from SD ...
      Hit any key to stop autoboot:  0
      Device: sdhci@e0100000
      Manufacturer ID: 9f
      OEM: 5449
      Name: SD64G
      Tran Speed: 50000000
      Rd Block Len: 512
      SD version 3.0
      High Capacity: Yes
      Capacity: 58 GiB
      Bus Width: 4-bit
      Erase Group Size: 512 Bytes
      reading uEnv.txt
      407 bytes read in 23 ms (16.6 KiB/s)
      Loaded environment from uEnv.txt
      Importing environment from SD ...
      Running uenvcmd ...
      Copying Linux from SD to RAM...
      reading uImage
      8264504 bytes read in 477 ms (16.5 MiB/s)
      reading devicetree.dtb
      16471 bytes read in 28 ms (574.2 KiB/s)
      ** Unable to read file uramdisk.image.gz **
      ## Booting kernel from Legacy Image at 03000000 ...
         Image Name:   Linux-6.1.0-22858-gb5010ed573e9-
         Image Type:   ARM Linux Kernel Image (uncompressed)
         Data Size:    8264440 Bytes = 7.9 MiB
         Load Address: 00008000
         Entry Point:  00008000
         Verifying Checksum ... OK
      ## Flattened Device Tree blob at 02a00000
         Booting using the fdt blob at 0x2a00000
         Loading Kernel Image ... OK
         Loading Device Tree to 1eb13000, end 1eb1a056 ... OK

      Starting kernel ...

      Booting Linux on physical CPU 0x0
      Linux version 6.1.0-22858-gb5010ed573e9-dirty (bcapota@romlx5) (arm-linux-gnueabi-gcc (Linaro GCC 7.5-2019.12) 7.5.0, GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706) #5 SMP PREEMPT Tue Jun  3 11:05:39 EEST 2025
      CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
      CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      OF: fdt: Machine model: Xilinx Zynq ZED
      OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
      Memory policy: Data cache writealloc
      cma: Reserved 128 MiB at 0x16800000
      Zone ranges:
      Normal   [mem 0x0000000000000000-0x000000001fffffff]
      HighMem  empty
      Movable zone start for each node
      Early memory node ranges
      node   0: [mem 0x0000000000000000-0x000000001fffffff]
      Initmem setup node 0 [mem 0x0000000000000000-0x000000001fffffff]
      percpu: Embedded 11 pages/cpu s14420 r8192 d22444 u45056
      Built 1 zonelists, mobility grouping on.  Total pages: 130048
      Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1
      Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
      mem auto-init: stack:off, heap alloc:off, heap free:off
      Memory: 361904K/524288K available (12288K kernel code, 816K rwdata, 10256K rodata, 1024K init, 475K bss, 31312K reserved, 131072K cma-reserved, 0K highmem)
      rcu: Preemptible hierarchical RCU implementation.
      rcu:    RCU event tracing is enabled.
      rcu:    RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
      rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
      NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      efuse mapped to (ptrval)
      slcr mapped to (ptrval)
      L2C: platform modifies aux control register: 0x72360000 -> 0x72760000
      L2C: DT/platform modifies aux control register: 0x72360000 -> 0x72760000
      L2C-310 erratum 769419 enabled
      L2C-310 enabling early BRESP for Cortex-A9
      L2C-310 full line of zeros enabled for Cortex-A9
      L2C-310 ID prefetch enabled, offset 1 lines
      L2C-310 dynamic clock gating enabled, standby mode enabled
      L2C-310 cache controller enabled, 8 ways, 512 kB
      L2C-310: CACHE_ID 0x410000c8, AUX_CTRL 0x76760001
      rcu: srcu_init: Setting srcu_struct sizes based on contention.
      zynq_clock_init: clkc starts at (ptrval)
      Zynq clock init
      sched_clock: 64 bits at 167MHz, resolution 6ns, wraps every 4398046511103ns
      clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x26703d7dd8, max_idle_ns: 440795208065 ns
      Switching to timer-based delay loop, resolution 6ns
      clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
      timer #0 at (ptrval), irq=25
      Console: colour dummy device 80x30
      Calibrating delay loop (skipped), value calculated using timer frequency.. 333.33 BogoMIPS (lpj=1666666)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      CPU: Testing write buffer coherency: ok
      CPU0: Spectre v2: using BPIALL workaround
      CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      Setting up static identity map for 0x100000 - 0x100060
      rcu: Hierarchical SRCU implementation.
      rcu:    Max phase no-delay instances is 1000.
      smp: Bringing up secondary CPUs ...
      CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      CPU1: Spectre v2: using BPIALL workaround
      smp: Brought up 1 node, 2 CPUs
      SMP: Total of 2 processors activated (666.66 BogoMIPS).
      CPU: All CPU(s) started in SVC mode.
      devtmpfs: initialized
      VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      pinctrl core: initialized pinctrl subsystem
      NET: Registered PF_NETLINK/PF_ROUTE protocol family
      DMA: preallocated 256 KiB pool for atomic coherent allocations
      thermal_sys: Registered thermal governor 'step_wise'
      amba f8801000.etb: Fixing up cyclic dependency with replicator
      amba f8803000.tpiu: Fixing up cyclic dependency with replicator
      amba f8804000.funnel: Fixing up cyclic dependency with replicator
      amba f889c000.ptm: Fixing up cyclic dependency with f8804000.funnel
      amba f889d000.ptm: Fixing up cyclic dependency with f8804000.funnel
      hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      hw-breakpoint: maximum watchpoint size is 4 bytes.
      e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 27, base_baud = 3125000) is a xuartps
      printk: console [ttyPS0] enabled
      SCSI subsystem initialized
      usbcore: registered new interface driver usbfs
      usbcore: registered new interface driver hub
      usbcore: registered new device driver usb
      mc: Linux media interface: v0.10
      videodev: Linux video capture interface: v2.00
      pps_core: LinuxPPS API ver. 1 registered
      pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      PTP clock support registered
      jesd204: found 0 devices and 0 topologies
      FPGA manager framework
      Advanced Linux Sound Architecture Driver Initialized.
      clocksource: Switched to clocksource arm_global_timer
      NET: Registered PF_INET protocol family
      IP idents hash table entries: 8192 (order: 4, 65536 bytes, linear)
      tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes, linear)
      Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
      TCP established hash table entries: 4096 (order: 2, 16384 bytes, linear)
      TCP bind hash table entries: 4096 (order: 4, 65536 bytes, linear)
      TCP: Hash tables configured (established 4096 bind 4096)
      UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
      UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
      NET: Registered PF_UNIX/PF_LOCAL protocol family
      RPC: Registered named UNIX socket transport module.
      RPC: Registered udp transport module.
      RPC: Registered tcp transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      armv7-pmu f8891000.pmu: hw perfevents: no interrupt-affinity property, guessing.
      hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
      workingset: timestamp_bits=30 max_order=17 bucket_order=0
      NFS: Registering the id_resolver key type
      Key type id_resolver registered
      Key type id_legacy registered
      nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
      fuse: init (API version 7.37)
      io scheduler mq-deadline registered
      io scheduler kyber registered
      zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
      dma-pl330 f8003000.dma-controller: Loaded driver for PL330 DMAC-241330
      dma-pl330 f8003000.dma-controller:      DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
      brd: module loaded
      loop: module loaded
      Registered mathworks_ip class
      SPI driver spidev has no spi_device_id for adi,swspi
      spi-nor spi1.0: found s25fl256s1, expected n25q128a11
      spi-nor spi1.0: s25fl256s1 (32768 Kbytes)
      5 fixed-partitions partitions found on MTD device spi1.0
      Creating 5 MTD partitions on "spi1.0":
      0x000000000000-0x000000500000 : "boot"
      0x000000500000-0x000000520000 : "bootenv"
      0x000000520000-0x000000540000 : "config"
      0x000000540000-0x000000fc0000 : "image"
      0x000000fc0000-0x000002000000 : "spare"
      MACsec IEEE 802.1AE
      tun: Universal TUN/TAP device driver, 1.6
      hwmon hwmon0: temp1_input not attached to any thermal zone
      macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 44 (c2:a0:b0:a0:00:00)
      usbcore: registered new interface driver asix
      usbcore: registered new interface driver ax88179_178a
      usbcore: registered new interface driver cdc_ether
      usbcore: registered new interface driver net1080
      usbcore: registered new interface driver cdc_subset
      usbcore: registered new interface driver zaurus
      usbcore: registered new interface driver cdc_ncm
      usbcore: registered new interface driver r8153_ecm
      usbcore: registered new interface driver uas
      usbcore: registered new interface driver usb-storage
      usbcore: registered new interface driver usbserial_generic
      usbserial: USB Serial support registered for generic
      usbcore: registered new interface driver ftdi_sio
      usbserial: USB Serial support registered for FTDI USB Serial Device
      usbcore: registered new interface driver upd78f0730
      usbserial: USB Serial support registered for upd78f0730
      ULPI transceiver vendor/product ID 0x0451/0x1507
      Found TI TUSB1210 ULPI transceiver.
      ULPI integrity check: passed.
      ci_hdrc ci_hdrc.0: EHCI Host Controller
      ci_hdrc ci_hdrc.0: new USB bus registered, assigned bus number 1
      ci_hdrc ci_hdrc.0: USB 2.0 started, EHCI 1.00
      usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
      usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      usb usb1: Product: EHCI Host Controller
      usb usb1: Manufacturer: Linux 6.1.0-22858-gb5010ed573e9-dirty ehci_hcd
      usb usb1: SerialNumber: ci_hdrc.0
      hub 1-0:1.0: USB hub found
      hub 1-0:1.0: 1 port detected
      SPI driver ads7846 has no spi_device_id for ti,tsc2046
      SPI driver ads7846 has no spi_device_id for ti,ads7843
      SPI driver ads7846 has no spi_device_id for ti,ads7845
      SPI driver ads7846 has no spi_device_id for ti,ads7873
      i2c_dev: i2c /dev entries driver
      i2c 0-0039: Fixing up cyclic dependency with 70e00000.axi_hdmi
      adv7511 0-0039: supply avdd not found, using dummy regulator
      adv7511 0-0039: supply dvdd not found, using dummy regulator
      adv7511 0-0039: supply pvdd not found, using dummy regulator
      adv7511 0-0039: supply bgvdd not found, using dummy regulator
      adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
      at24 1-0050: supply vcc not found, using dummy regulator
      at24 1-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      gspca_main: v2.14.0 registered
      usbcore: registered new interface driver uvcvideo
      cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer with timeout 10s
      Xilinx Zynq CpuIdle Driver started
      failed to register cpuidle driver
      sdhci: Secure Digital Host Controller Interface driver
      sdhci: Copyright(c) Pierre Ossman
      sdhci-pltfm: SDHCI platform and OF driver helper
      ledtrig-cpu: registered to indicate activity on CPUs
      hid: raw HID events driver (C) Jiri Kosina
      usbcore: registered new interface driver usbhid
      usbhid: USB HID core driver
      SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7988-5
      mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7988-1
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7984
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7983
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7982
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7980
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7949
      mmc0: new high speed SDXC card at address 5048
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7946
      mmcblk0: mmc0:5048 SD64G 58.0 GiB
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7942
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7699
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7693
      mmcblk0: p1 p2 p3
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7691
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7690
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7689
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7688
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7687
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7686
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7685
      SPI driver pulsar_adc has no spi_device_id for adi,pulsar,ad7682
      SPI driver ad7124 has no spi_device_id for adi,ad7124-4
      SPI driver ad7124 has no spi_device_id for adi,ad7124-8
      SPI driver ad7192 has no spi_device_id for adi,ad7190
      SPI driver ad7192 has no spi_device_id for adi,ad7193
      SPI driver ad7192 has no spi_device_id for adi,ad7195
      cf_axi_adc 43c00000.cf_axi_AD777X: ADI AIM (10.03.) at 0x43C00000 mapped to 0x(ptrval) probed ADC AD777X_axi_adc as MASTER
      SPI driver ad9467 has no spi_device_id for adi,ad9643
      SPI driver ad9467 has no spi_device_id for adi,ad9250
      SPI driver ad9467 has no spi_device_id for adi,ad9250_2
      SPI driver ad9467 has no spi_device_id for adi,ad9265
      SPI driver ad9467 has no spi_device_id for adi,ad9683
      SPI driver ad9467 has no spi_device_id for adi,ad9434
      SPI driver ad9467 has no spi_device_id for adi,ad9625
      SPI driver ad9467 has no spi_device_id for adi,ad9652
      SPI driver ad9467 has no spi_device_id for adi,ad9649
      SPI driver adar3000 has no spi_device_id for adi,adar3001
      SPI driver adar3000 has no spi_device_id for adi,adar3002
      SPI driver ad9783 has no spi_device_id for adi,ad9780
      SPI driver ad9783 has no spi_device_id for adi,ad9781
      SPI driver adis16475 has no spi_device_id for adi,adis16470
      SPI driver adis16475 has no spi_device_id for adi,adis16475-1
      SPI driver adis16475 has no spi_device_id for adi,adis16475-2
      SPI driver adis16475 has no spi_device_id for adi,adis16475-3
      SPI driver adis16475 has no spi_device_id for adi,adis16477-1
      SPI driver adis16475 has no spi_device_id for adi,adis16477-2
      SPI driver adis16475 has no spi_device_id for adi,adis16477-3
      SPI driver adis16475 has no spi_device_id for adi,adis16465-1
      SPI driver adis16475 has no spi_device_id for adi,adis16465-2
      SPI driver adis16475 has no spi_device_id for adi,adis16465-3
      SPI driver adis16475 has no spi_device_id for adi,adis16467-1
      SPI driver adis16475 has no spi_device_id for adi,adis16467-2
      SPI driver adis16475 has no spi_device_id for adi,adis16467-3
      SPI driver adis16475 has no spi_device_id for adi,adis16500
      SPI driver adis16475 has no spi_device_id for adi,adis16505-1
      SPI driver adis16475 has no spi_device_id for adi,adis16505-2
      SPI driver adis16475 has no spi_device_id for adi,adis16505-3
      SPI driver adis16475 has no spi_device_id for adi,adis16507-1
      SPI driver adis16475 has no spi_device_id for adi,adis16507-2
      SPI driver adis16475 has no spi_device_id for adi,adis16507-3
      axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      axi_sysid 45000000.axi-sysid-0: [AD777X_ardz] on [zed] git branch <AD777X_fmc> git <a941a1c7ee2e70ea01e87a0b80218a9bfc442eb0> dirty [2025-06-05 11:22:12] UTC
      fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
      usbcore: registered new interface driver snd-usb-audio
      axi-i2s 77600000.axi-i2s: probed, capture enabled, playback enabled
      NET: Registered PF_INET6 protocol family
      Segment Routing with IPv6
      In-situ OAM (IOAM) with IPv6
      sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      NET: Registered PF_PACKET protocol family
      NET: Registered PF_IEEE802154 protocol family
      Key type dns_resolver registered
      zynq_pm_remap_ocm: OCM pool is not available
      zynq_pm_suspend_init: Unable to map OCM.
      Registering SWP/SWPB emulation handler
      of-fpga-region fpga-full: FPGA Region probed
      [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for 70e00000.axi_hdmi on minor 0
      axi-hdmi 70e00000.axi_hdmi: [drm] Cannot find any crtc or sizes
      debugfs: File 'Capture' in directory 'dapm' already present!
      of_cfs_init
      of_cfs_init: OK
      clk: Not disabling unused clocks
      ALSA device list:
      #0: HDMI monitor
      #1: ZED ADAU1761
      EXT4-fs (mmcblk0p2): recovery complete
      EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Quota mode: disabled.
      VFS: Mounted root (ext4 filesystem) on device 179:2.
      devtmpfs: mounted
      Freeing unused kernel image (initmem) memory: 1024K
      Run /sbin/init as init process
      systemd[1]: System time before build time, advancing clock.
      systemd[1]: systemd 247.3-7+rpi1+deb11u6 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

      systemd[1]: Set hostname to <analog>.
      systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      systemd[1]: /lib/systemd/system/iiod.service:14: Invalid environment assignment, ignoring: $IIOD_EXTRA_OPTS=
      systemd[1]: Queued start job for default target Graphical Interface.
      random: crng init done
      systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      systemd[1]: Created slice system-getty.slice.
      [  OK  ] Created slice system-getty.slice.
      systemd[1]: Created slice system-modprobe.slice.
      [  OK  ] Created slice system-modprobe.slice.
      systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      systemd[1]: Created slice User and Session Slice.
      [  OK  ] Created slice User and Session Slice.
      systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      systemd[1]: Reached target Slices.
      [  OK  ] Reached target Slices.
      systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
      systemd[1]: Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket (/dev/log).
      systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      systemd[1]: Listening on udev Control Socket.
      [  OK  ] Listening on udev Control Socket.
      systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      systemd[1]: Condition check resulted in Huge Pages File System being skipped.
      systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
      systemd[1]: Mounting RPC Pipe File System...
               Mounting RPC Pipe File System...
      systemd[1]: Mounting Kernel Debug File System...
               Mounting Kernel Debug File System...
      systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
      systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      systemd[1]: Starting Restore / save the current clock...
               Starting Restore / save the current clock...
      systemd[1]: Starting Set the console keyboard layout...
               Starting Set the console keyboard layout...
      systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      systemd[1]: Starting Load Kernel Module configfs...
               Starting Load Kernel Module configfs...
      systemd[1]: Starting Load Kernel Module drm...
               Starting Load Kernel Module drm...
      systemd[1]: Starting Load Kernel Module fuse...
               Starting Load Kernel Module fuse...
      systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      systemd[1]: Starting Journal Service...
               Starting Journal Service...
      systemd[1]: Starting Load Kernel Modules...
               Starting Load Kernel Modules...
      systemd[1]: Starting Remount Root and Kernel File Systems...
               Starting Remount Root and Kernel File Systems...
      systemd[1]: Starting Coldplug All udev Devices...
               Starting Coldplug All udev Devices...
      systemd[1]: Mounted RPC Pipe File System.
      [  OK  ] Mounted RPC Pipe File System.
      systemd[1]: Mounted Kernel Debug File System.
      [  OK  ] Mounted Kernel Debug File System.
      systemd[1]: Finished Restore / save the current clock.
      [  OK  ] Finished Restore / save the current clock.
      systemd[1]: modprobe@configfs.service: Succeeded.
      systemd[1]: Finished Load Kernel Module configfs.
      [  OK  ] Finished Load Kernel Module configfs.
      systemd[1]: modprobe@drm.service: Succeeded.
      systemd[1]: Finished Load Kernel Module drm.
      [  OK  ] Finished Load Kernel Module drm.
      systemd[1]: modprobe@fuse.service: Succeeded.
      systemd[1]: Finished Load Kernel Module fuse.
      [  OK  ] Finished Load Kernel Module fuse.
      systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
               Mounting FUSE Control File System...
               Mounting Kernel Configuration File System...
               Starting Apply Kernel Variables...
      [  OK  ] Finished Set the console keyboard layout.
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Finished Remount Root and Kernel File Systems.
      [  OK  ] Finished Apply Kernel Variables.
               Starting Flush Journal to Persistent Storage...
               Starting Load/Save Random Seed...
               Starting Create System Users...
      [  OK  ] Finished Load/Save Random Seed.
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
      [  OK  ] Found device /dev/ttyPS0.
      [  OK  ] Found device /dev/disk/by-partuuid/5c29002e-01.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
               Starting File System Check…isk/by-partuuid/5c29002e-01...
               Starting Load Kernel Modules...
      [  OK  ] Started File System Check Daemon to report status.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Finished File System Check…/disk/by-partuuid/5c29002e-01.
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
      [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
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
               Starting Save/Restore Sound Card State...
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
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Finished Save/Restore Sound Card State.
      [  OK  ] Finished Fix DP audio and X11 for Jupiter.
      [  OK  ] Started DHCP Client Daemon.
      [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Started Authorization Manager.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Reached target Network.
      [  OK  ] Reached target Network is Online.
      [  OK  ] Reached target Sound Card.
               Starting Modem Manager...
               Starting CUPS Scheduler...
      [  OK  ] Started Erlang Port Mapper Daemon.
               Starting HTTP based time synchronization tool...
               Starting Internet superserver...
               Starting /etc/rc.local Compatibility...
               Starting OpenBSD Secure Shell server...
               Starting Permit User Sessions...
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started Internet superserver.
      [  OK  ] Started User Login Management.
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Finished Analog Devices power up/down sequence.
      [  OK  ] Finished Permit User Sessions.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [  OK  ] Started Modem Manager.
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyPS0

      analog login: root (automatic login)

      Linux analog 6.1.0-22858-gb5010ed573e9-dirty #5 SMP PREEMPT Tue Jun  3 11:05:39 EEST 2025 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Fri Nov  8 15:17:16 GMT 2024 on ttyPS0
      root@analog:~#


Useful commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The below commands are to be run in the serial terminal connected to the
ZedBoard.

To find out the IP address of the board, run:

.. shell::

   $ifconfig

Take the IP address shown for ``eth0 inet``.

To find the IIO devices detected, run:

.. shell::

   $iio_info | grep iio:device

To power off the system cleanly, run the following command and wait for
the final message before switching off the board:

.. shell::

   $poweroff

.. important::

   The Kuiper Linux root filesystem is mounted from the ext4 partition
   of the SD card. Changes made at runtime are persistent across reboots.
   To restart the system, power cycle the ZedBoard.

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`iio-oscilloscope` is a cross-platform GUI application that can
connect to the board remotely over the network and capture data from IIO
devices.

.. note::

   Connect an analog signal to the evaluation board's input channels
   before capturing data. The captures below used a DC reference signal
   applied to one channel to verify baseline operation.

To connect, open IIO Oscilloscope on the host PC, go to Settings,
Connect, check the Manual option, and enter the URI using the board
IP address obtained from ``ifconfig``:

.. code-block:: none

   ip:<board-ip>

Press Refresh to list the available IIO devices, then press Connect.

.. figure:: ../images/iio_connect.jpeg
   :alt: IIO Oscilloscope connect dialog
   :width: 600

   IIO Oscilloscope connect dialog

Once connected, select the AD777X device and use the Capture window to
acquire and display ADC samples.

.. figure:: ../images/iio_capture_t.jpeg
   :alt: IIO Oscilloscope showing AD777X time domain waveform
   :width: 800

   AD777X time domain capture in IIO Oscilloscope
