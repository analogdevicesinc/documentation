.. _eval-ad353xr quickstart zed:

ZedBoard Quick start
===============================================================================

.. figure:: ../images/zed_board_setup.jpeg
   :alt: ZedBoard with EVAL-AD3530R connected via FMC LPC connector
   :width: 800

   ZedBoard with EVAL-AD3530R hardware setup

.. figure:: ../images/ad353xr_setup.jpeg
   :alt: EVAL-AD3530R evaluation board setup on ZedBoard
   :width: 800

   EVAL-AD3530R evaluation board

.. esd-warning::

This guide provides step-by-step instructions to set up the
:adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` on:

- `ZedBoard
  <https://digilent.com/reference/programmable-logic/zedboard/start>`_

.. warning::

   The ZedBoard FMC connector is **low pin count**. Ensure VADJ is set to
   **2.5 V** before powering on. Incorrect VADJ may damage the evaluation
   board.

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``BOOT.BIN``, built from the HDL project;
  follow :external+hdl:ref:`Build an HDL project <build_hdl>`
- ``devicetree.dtb``, compiled from the device tree source
- ``uImage``, the Linux kernel image;
  follow :ref:`linux-kernel zynq`

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

- `ZedBoard
  <https://digilent.com/reference/programmable-logic/zedboard/start>`_
  and its power supply
- :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` evaluation board
- Jumper wires for SPI and GPIO connections via the FMC LPC connector
- Micro-USB to USB Type-A cable (UART)
- Ethernet cable (for IIO Oscilloscope)
- microSD card (at least 16 GB)
- 5 V power supply for the AD3530R (USB-C connector or any VCC/GND pin)
- 3.3 V supply for the IOREF pin of the EVAL board

More details can be found at :ref:`eval-ad353xr prerequisites`.

.. _eval-ad353xr quickstart zed hw-setup:

Hardware setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting VADJ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VADJ must be set to **2.5 V** before powering the board. Refer to the
ZedBoard hardware guide for the VADJ selection jumper location.

Setting the boot jumpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set jumpers **MIO[6:2]** to ``01100`` for SD card boot mode.

Wiring the eval board to the ZedBoard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the EVAL-AD3530R to the ZedBoard FMC LPC connector (J1) using
jumper wires according to the table below. The FMC pin names and
connector positions are listed using the Xilinx FMC105-Debug Card
reference (J1/J9).

.. list-table:: Hardware connections - ZedBoard - EVAL-AD3530R
   :header-rows: 1
   :widths: 15 45 40

   * - Signal
     - ZedBoard (FMC pin - connector)
     - EVAL-AD3530R
   * - SPI CLK
     - FMC-CLK1_P <G2> (J9)
     - DIG-IO Pin 13
   * - SPI MISO
     - FMC-LA01_N <D9> (J1 pin 7)
     - DIG-IO Pin 11 (SDI)
   * - SPI MOSI
     - FMC-LA01_P <D8> (J1 pin 5)
     - DIG-IO Pin 12 (SDO)
   * - SPI CSB/SS
     - FMC-LA00_P <G6> (J1 pin 1)
     - DIG-IO Pin 10
   * - RESET
     - FMC-LA10_N <C15> (J1 pin 4)
     - DIG-IO Pin 8
   * - LDAC
     - FMC-LA05_P <D11> (J1 pin 21)
     - DIG-IO Pin 6

Power the EVAL-AD3530R by connecting a **5 V** supply to either the
USB-C connector or any available VCC/GND pin. Connect **3.3 V** to the
IOREF pin.

Inserting the SD card and connecting cables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Insert the prepared microSD card into the ZedBoard SD card slot.
#. Connect the Micro-USB cable to the UART port on the ZedBoard.
#. Connect the Ethernet cable to the Ethernet port.
#. Power on the board.
#. Observe serial console output in your terminal at 115200 baud.

Booting up the FPGA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy ``BOOT.BIN``, ``devicetree.dtb``, and ``uImage`` to the ``BOOT``
partition of the SD card. Insert the SD card into the ZedBoard and power on.
The boot log should appear in your terminal.

Login information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The system logs in automatically as ``root``. If prompted:

- User: ``root``
- Password: ``analog``

.. collapsible:: Complete boot log

   ::

      ``U-Boot 2018.01-21439-gd244ce5 (Jul 29 2021 - 16:33:01 +0100), Build: jenkins-development-build_uboot-1

      Model: Zynq Zed Development Board
      Board: Xilinx Zynq
      Silicon: v3.1
      DRAM:  ECC disabled 512 MiB
      MMC:   sdhci@e0100000: 0 (SD)
      SF: Detected s25fl256s_64k with page size 256 Bytes, erase size 64 KiB, total 32 MiB
      *** Warning - bad CRC, using default environment

      In:    serial@e0001000
      Out:   serial@e0001000
      Err:   serial@e0001000
      Net:   ZYNQ GEM: e000b000, phyaddr 0, interface rgmii-id
      eth0: ethernet@e000b000
      reading uEnv.txt
      407 bytes read in 18 ms (21.5 KiB/s)
      Importing environment from SD ...
      Hit any key to stop autoboot:  0
      Device: sdhci@e0100000
      Manufacturer ID: 27
      OEM: 5048
      Name: SD64G
      Tran Speed: 50000000
      Rd Block Len: 512
      SD version 3.0
      High Capacity: Yes
      Capacity: 58 GiB
      Bus Width: 4-bit
      Erase Group Size: 512 Bytes
      reading uEnv.txt
      407 bytes read in 18 ms (21.5 KiB/s)
      Loaded environment from uEnv.txt
      Importing environment from SD ...
      Running uenvcmd ...
      Copying Linux from SD to RAM...
      reading uImage
      8926664 bytes read in 516 ms (16.5 MiB/s)
      reading devicetree.dtb
      16790 bytes read in 24 ms (682.6 KiB/s)
      ** Unable to read file uramdisk.image.gz **
      ## Booting kernel from Legacy Image at 03000000 ...
         Image Name:   Linux-6.12.0-27098-g298669e57d37
         Image Type:   ARM Linux Kernel Image (uncompressed)
         Data Size:    8926600 Bytes = 8.5 MiB
         Load Address: 00008000
         Entry Point:  00008000
         Verifying Checksum ... OK
      ## Flattened Device Tree blob at 02a00000
         Booting using the fdt blob at 0x2a00000
         Loading Kernel Image ... OK
         Loading Device Tree to 1eb12000, end 1eb19195 ... OK

      Starting kernel ...

      Booting Linux on physical CPU 0x0
      Linux version 6.12.0-27098-g298669e57d37 (atorreno@ATORRENO-L02) (arm-none-linux-gnueabihf-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #380 SMP PREEMPT Mon Mar 23 12:08:09 CST 2026
      CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
      CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      OF: fdt: Machine model: Xilinx Zynq ZED
      OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
      Memory policy: Data cache writealloc
      cma: Reserved 128 MiB at 0x16800000 on node -1
      Zone ranges:
      Normal   [mem 0x0000000000000000-0x000000001fffffff]
      HighMem  empty
      Movable zone start for each node
      Early memory node ranges
      node   0: [mem 0x0000000000000000-0x000000001fffffff]
      Initmem setup node 0 [mem 0x0000000000000000-0x000000001fffffff]
      percpu: Embedded 12 pages/cpu s17356 r8192 d23604 u49152
      Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1
      Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
      Built 1 zonelists, mobility grouping on.  Total pages: 131072
      mem auto-init: stack:off, heap alloc:off, heap free:off
      SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
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
      Console: colour dummy device 80x30
      Calibrating delay loop (skipped), value calculated using timer frequency.. 333.33 BogoMIPS (lpj=1666666)
      CPU: Testing write buffer coherency: ok
      CPU0: Spectre v2: using BPIALL workaround
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
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
      Memory: 359484K/524288K available (13312K kernel code, 907K rwdata, 10968K rodata, 1024K init, 497K bss, 32468K reserved, 131072K cma-reserved, 0K highmem)
      devtmpfs: initialized
      VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      pinctrl core: initialized pinctrl subsystem
      NET: Registered PF_NETLINK/PF_ROUTE protocol family
      DMA: preallocated 256 KiB pool for atomic coherent allocations
      thermal_sys: Registered thermal governor 'step_wise'
      platform axi: Fixed dependency cycle(s) with /axi/interrupt-controller@f8f01000
      platform replicator: Fixed dependency cycle(s) with /axi/etb@f8801000
      amba f8801000.etb: Fixed dependency cycle(s) with /replicator
      platform replicator: Fixed dependency cycle(s) with /axi/tpiu@f8803000
      amba f8803000.tpiu: Fixed dependency cycle(s) with /replicator
      platform replicator: Fixed dependency cycle(s) with /axi/funnel@f8804000
      amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889d000
      amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889c000
      amba f8804000.funnel: Fixed dependency cycle(s) with /replicator
      amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889c000
      amba f889c000.ptm: Fixed dependency cycle(s) with /axi/funnel@f8804000
      amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889d000
      amba f889d000.ptm: Fixed dependency cycle(s) with /axi/funnel@f8804000
      platform 70e00000.lcd-controller: Fixed dependency cycle(s) with /fpga-axi@0/i2c@41600000/hdmi@39
      hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      hw-breakpoint: maximum watchpoint size is 4 bytes.
      e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 26, base_baud = 3125000) is a xuartps
      printk: legacy console [ttyPS0] enabled
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
      RPC: Registered tcp-with-tls transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      workingset: timestamp_bits=30 max_order=17 bucket_order=0
      NFS: Registering the id_resolver key type
      Key type id_resolver registered
      Key type id_legacy registered
      nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
      fuse: init (API version 7.41)
      io scheduler mq-deadline registered
      io scheduler kyber registered
      zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
      ledtrig-cpu: registered to indicate activity on CPUs
      dma-pl330 f8003000.dma-controller: Loaded driver for PL330 DMAC-241330
      dma-pl330 f8003000.dma-controller:      DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
      brd: module loaded
      loop: module loaded
      Registered mathworks_ip class
      spi-nor spi1.0: found s25fl256s1, expected n25q128a11
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
      macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 40 (00:0a:35:00:01:22)
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
      usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.12
      usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      usb usb1: Product: EHCI Host Controller
      usb usb1: Manufacturer: Linux 6.12.0-27098-g298669e57d37 ehci_hcd
      usb usb1: SerialNumber: ci_hdrc.0
      hub 1-0:1.0: USB hub found
      hub 1-0:1.0: 1 port detected
      i2c_dev: i2c /dev entries driver
      platform 70e00000.lcd-controller: Fixed dependency cycle(s) with /fpga-axi@0/i2c@41600000/hdmi@39
      i2c 0-0039: Fixed dependency cycle(s) with /fpga-axi@0/lcd-controller@70e00000
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
      clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
      timer #0 at (ptrval), irq=46
      hid: raw HID events driver (C) Jiri Kosina
      usbcore: registered new interface driver usbhid
      usbhid: USB HID core driver
      SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
      armv7-pmu f8891000.pmu: hw perfevents: no interrupt-affinity property, guessing.
      hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 (8000003f) counters available
      axi_sysid 45000000.sysid: AXI System ID core version (1.01.a) found
      axi_sysid 45000000.sysid: [ad353xr] on [zed] git branch <dev_ad5706r_spi_engine> git <8a94515f54b321e9e0ff8b90fc6482153de373c2> dirty [2026-03-23 01:49:19] UTC
      mmc0: new high speed SDXC card at address 5048
      fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
      mmcblk0: mmc0:5048 SD64G 58.0 GiB
      usbcore: registered new interface driver snd-usb-audio
      mmcblk0: p1 p2 p3
      axi-i2s 77600000.i2s: probed, capture enabled, playback enabled
      NET: Registered PF_INET6 protocol family
      Segment Routing with IPv6
      In-situ OAM (IOAM) with IPv6
      sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      NET: Registered PF_PACKET protocol family
      NET: Registered PF_IEEE802154 protocol family
      Key type dns_resolver registered
      Registering SWP/SWPB emulation handler
      of-fpga-region fpga-region: FPGA Region probed
      [drm] Initialized axi_hdmi_drm 1.0.0 for 70e00000.lcd-controller on minor 0
      axi-hdmi 70e00000.lcd-controller: [drm] Cannot find any crtc or sizes
      axi-hdmi 70e00000.lcd-controller: [drm] Cannot find any crtc or sizes
      debugfs: File 'Capture' in directory 'dapm' already present!
      input: gpio-keys as /devices/soc0/gpio-keys/input/input0
      of_cfs_init
      of_cfs_init: OK
      clk: Not disabling unused clocks
      ALSA device list:
      #0: HDMI monitor
      #1: ZED ADAU1761
      EXT4-fs (mmcblk0p2): recovery complete
      EXT4-fs (mmcblk0p2): mounted filesystem ec12e3b7-46e4-4c91-b5ba-8110b9ce1e5b r/w with ordered data mode. Quota mode: disabled.
      VFS: Mounted root (ext4 filesystem) on device 179:2.
      devtmpfs: mounted
      Freeing unused kernel image (initmem) memory: 1024K
      Run /sbin/init as init process
      systemd[1]: System time before build time, advancing clock.
      systemd[1]: systemd 247.3-7+rpi1+deb11u2 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

      systemd[1]: Set hostname to <analog>.
      systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
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
      systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
      [  OK  ] Finished Load Kernel Module configfs.
      [  OK  ] Finished Load Kernel Module drm.
      [  OK  ] Finished Load Kernel Module fuse.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
               Mounting FUSE Control File System...
               Mounting Kernel Configuration File System...
               Starting Apply Kernel Variables...
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Finished Set the console keyboard layout.
      [  OK  ] Finished Apply Kernel Variables.
      [  OK  ] Finished Coldplug All udev Devices.
      [  OK  ] Finished Remount Root and Kernel File Systems.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Flush Journal to Persistent Storage...
               Starting Load/Save Random Seed...
               Starting Create System Users...
               Starting Wait for udev To …plete Device Initialization...
      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Finished Create System Users.
               Starting Create Static Device Nodes in /dev...
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
      [  OK  ] Found device /dev/disk/by-partuuid/3c47d971-01.
               Starting File System Check…isk/by-partuuid/3c47d971-01...
      [  OK  ] Finished Helper to synchronize boot up for ifupdown.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
      [  OK  ] Started File System Check Daemon to report status.
               Starting Load Kernel Modules...
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
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
      [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
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
               Starting Save/Restore Sound Card State...
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
      [  OK  ] Finished Save/Restore Sound Card State.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [FAILED] Failed to start Raise network interfaces.
      See 'systemctl status networking.service' for details.
      [  OK  ] Started DHCP Client Daemon.
      [  OK  ] Reached target Sound Card.
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
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
      My IP address is 192.168.3.2
               Starting Permit User Sessions...
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [  OK  ] Started Internet superserver.
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started Authorization Manager.
               Starting Modem Manager...
      [  OK  ] Finished Permit User Sessions.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Finished Creating IIOD Context Attributes....
      [  OK  ] Started IIO Daemon.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Started OpenBSD Secure Shell server.
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyPS0

      analog login: root (automatic login)

      Linux analog 6.12.0-27098-g298669e57d37 #380 SMP PREEMPT Mon Mar 23 12:08:09 CST 2026 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Sun Dec 17 17:17:16 GMT 2023 on ttyPS0
      root@analog:~#``

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
      Backend description string: Linux analog 6.12.0-27098-g298669e57d37 #380 SMP PREEMPT Mon Mar 23 12:08:09 CST 2026 armv7l
      IIO context has 5 attributes:
            hdl_system_id: [ad353xr] on [zed] git branch [dev_ad5706r_spi_engine] git [8a94515f54b321e9e0ff8b90fc6482153de373c2] dirty [2026-03-23 01:49:19] UTC
            hw_carrier: Xilinx Zynq ZED
            hw_model: EV-ADAQ7769-1FMC1Z on Xilinx Zynq ZED
            local,kernel: 6.12.0-27098-g298669e57d37
            uri: local:
      IIO context has 4 devices:
            hwmon0: e000b000ethernetffffffff00
                     1 channels found:
                              temp1:  (input)
                              3 channel-specific attributes found:
                                    attr  0: crit value: 100000
                                    attr  1: input value: 16000
                                    attr  2: max_alarm value: 0
                     No trigger on this device
            iio:device0: xadc
                     9 channels found:
                              voltage5: vccoddr (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccoddr
                                    attr  1: raw value: 2033
                                    attr  2: scale value: 0.732421875
                              voltage0: vccint (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccint
                                    attr  1: raw value: 1372
                                    attr  2: scale value: 0.732421875
                              voltage4: vccpaux (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccpaux
                                    attr  1: raw value: 2438
                                    attr  2: scale value: 0.732421875
                              temp0:  (input)
                              3 channel-specific attributes found:
                                    attr  0: offset value: -2219
                                    attr  1: raw value: 2489
                                    attr  2: scale value: 123.040771484
                              voltage7: vrefn (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vrefn
                                    attr  1: raw value: -8
                                    attr  2: scale value: 0.732421875
                              voltage1: vccaux (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccaux
                                    attr  1: raw value: 2437
                                    attr  2: scale value: 0.732421875
                              voltage2: vccbram (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccbram
                                    attr  1: raw value: 1369
                                    attr  2: scale value: 0.732421875
                              voltage3: vccpint (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccpint
                                    attr  1: raw value: 1373
                                    attr  2: scale value: 0.732421875
                              voltage6: vrefp (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vrefp
                                    attr  1: raw value: 1696
                                    attr  2: scale value: 0.732421875
                     2 device-specific attributes found:
                                    attr  0: sampling_frequency value: 961538
                                    attr  1: waiting_for_supplier value: 0
                     No trigger on this device
            iio:device1: ad3530r
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
      root@analog:~#
