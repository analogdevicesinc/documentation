.. _eval-ad353xr quickstart coraz7s:

CoraZ7s Quick start
===============================================================================

.. figure:: ../images/cora_board.jpeg
   :alt: CoraZ7s board with labeled port locations
   :width: 800

   CoraZ7s port locations


.. esd-warning::

This guide provides step-by-step instructions to set up the
:adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` on:

- `CoraZ7-07s <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development/>`_

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
   The files must be built manually using the links above. Official release
   artifacts will be provided here once available.

   The HDL source is available at :git-hdl:`/projects/ad353xr/coraz7s`.
   The Linux driver is at
   :git-linux:`drivers/iio/dac/ad3530r.c <64ec98ac2413d592e484d4cb206fbca93c419693:drivers/iio/dac/ad3530r.c>`.
   The device tree source for this reference design is not yet upstream.

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- A UART terminal (e.g. PuTTY, Tera Term, Minicom) at 115200 baud (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :digikey:`CoraZ7-07S <DIGILENT-410-346>` FPGA board and its power supply
- :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` evaluation board
- Jumper wires for SPI and GPIO connections
- Micro-USB to USB Type-A cable (UART connection to the CoraZ7s)
- Ethernet cable (for IIO Oscilloscope)
- microSD card (at least 16 GB)
- 5 V power supply for the AD3530R (USB-C connector or any available VCC/GND pin)
- 3.3 V supply for the IOREF pin of the EVAL board

More details can be found at :ref:`eval-ad353xr prerequisites`.

.. _eval-ad353xr quickstart coraz7s hw-setup:

Hardware setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The photo below shows the complete setup with both the CoraZ7s and the
EVAL-AD3530R connected:

.. figure:: ../images/full_set_up_cora.jpeg
   :width: 600
   :alt: Full setup with CoraZ7s and EVAL-AD3530R connected

   Full setup - CoraZ7s with EVAL-AD3530R

CoraZ7s alone:

.. figure:: ../images/cora_setup.jpeg
   :width: 600
   :alt: CoraZ7s board setup

   CoraZ7s board

EVAL-AD3530R alone:

.. figure:: ../images/eval-ad353XR_setup.jpeg
   :width: 600
   :alt: EVAL-AD3530R evaluation board setup

   EVAL-AD3530R evaluation board

Setting the boot jumpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the CoraZ7s, place a jumper on **JP2**, shorting both pins together.
Select **JP3** based on your power supply source (USB or external supply).

Wiring the eval board to the CoraZ7s
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the EVAL-AD3530R to the CoraZ7s using jumper wires according to the
table below.

.. list-table:: Hardware connections - CoraZ7s <-> EVAL-AD3530R
   :header-rows: 1
   :widths: 20 40 40

   * - Signal
     - CoraZ7s
     - EVAL-AD3530R
   * - SPI CLK
     - 2×3 ICSP Header Pin 3
     - DIG-IO Pin 13
   * - SPI MISO
     - 2×3 ICSP Header Pin 1
     - DIG-IO Pin 11 (SDI)
   * - SPI MOSI
     - 2×3 ICSP Header Pin 4
     - DIG-IO Pin 12 (SDO)
   * - SPI CSB/SS
     - 2×3 ICSP Header Pin 5
     - DIG-IO Pin 10
   * - RESET
     - Analog Header A1
     - DIG-IO Pin 8
   * - LDAC
     - Analog Header A2
     - DIG-IO Pin 6

Power the EVAL-AD3530R by connecting a **5 V** supply to either the USB-C
connector or any available VCC/GND pin on the board. Connect **3.3 V** to the
IOREF pin.

Inserting the SD card and connecting cables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Insert the prepared microSD card into the CoraZ7s SD card slot.
#. Connect the Micro-USB cable to the UART port on the CoraZ7s.
#. Connect the Ethernet cable to the Ethernet port.
#. Power on the board.
#. Observe serial console output in your terminal at 115200 baud.

Booting up the FPGA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy ``BOOT.BIN``, ``devicetree.dtb``, and ``uImage`` to the ``BOOT``
partition of the SD card. Insert the SD card into the CoraZ7s and power on.
The boot log should appear in your terminal.

A successful boot:

.. collapsible:: Complete boot log

   ::

      # Booting Linux on physical CPU 0x0
      Linux version 6.12.0-27098-g298669e57d37 (atorreno@ATORRENO-L02) (arm-none-linux-gnueabihf-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #380 SMP PREEMPT Mon Mar 23 12:08:09 CST 2026
      CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
      CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      OF: fdt: Machine model: Zynq Cora Z7 Development Board
      earlycon: cdns0 at MMIO 0xe0000000 (options '115200n8')
      printk: legacy bootconsole [cdns0] enabled
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
      sched_clock: 64 bits at 163MHz, resolution 6ns, wraps every 4398046511101ns
      clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x257a3bfb55, max_idle_ns: 440795207830 ns
      Switching to timer-based delay loop, resolution 6ns
      Console: colour dummy device 80x30
      Calibrating delay loop (skipped), value calculated using timer frequency.. 325.00 BogoMIPS (lpj=1625000)
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
      CPU1: failed to boot: -1
      smp: Brought up 1 node, 1 CPU
      SMP: Total of 1 processors activated (325.00 BogoMIPS).
      CPU: All CPU(s) started in SVC mode.
      Memory: 359512K/524288K available (13312K kernel code, 907K rwdata, 10968K rodata, 1024K init, 497K bss, 32440K reserved, 131072K cma-reserved, 0K highmem)
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
      hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      hw-breakpoint: maximum watchpoint size is 4 bytes.
      e0000000.serial: ttyPS0 at MMIO 0xe0000000 (irq = 26, base_baud = 6250000) is a xuartps
      printk: legacy console [ttyPS0] enabled
      printk: legacy console [ttyPS0] enabled
      printk: legacy bootconsole [cdns0] disabled
      printk: legacy bootconsole [cdns0] disabled
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
      MACsec IEEE 802.1AE
      tun: Universal TUN/TAP device driver, 1.6
      macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 38 (00:0a:35:00:01:22)
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
      ULPI transceiver vendor/product ID 0x0424/0x0007
      Found SMSC USB3320 ULPI transceiver.
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
      gspca_main: v2.14.0 registered
      usbcore: registered new interface driver uvcvideo
      cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer with timeout 10s
      Xilinx Zynq CpuIdle Driver started
      failed to register cpuidle driver
      sdhci: Secure Digital Host Controller Interface driver
      sdhci: Copyright(c) Pierre Ossman
      sdhci-pltfm: SDHCI platform and OF driver helper
      clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 551318127 ns
      timer #0 at (ptrval), irq=42
      hid: raw HID events driver (C) Jiri Kosina
      usbcore: registered new interface driver usbhid
      usbhid: USB HID core driver
      SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
      armv7-pmu f8891000.pmu: hw perfevents: no interrupt-affinity property, guessing.
      hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 (8000003f) counters available
      fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
      usbcore: registered new interface driver snd-usb-audio
      NET: Registered PF_INET6 protocol family
      Segment Routing with IPv6
      In-situ OAM (IOAM) with IPv6
      mmc0: new high speed SDHC card at address 5048
      mmcblk0: mmc0:5048 SD32G 29.7 GiB
      sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      NET: Registered PF_PACKET protocol family
       mmcblk0: p1 p2 p3
      NET: Registered PF_IEEE802154 protocol family
      Key type dns_resolver registered
      Registering SWP/SWPB emulation handler
      of-fpga-region fpga-region: FPGA Region probed
      of_cfs_init
      of_cfs_init: OK
      clk: Not disabling unused clocks
      ALSA device list:
        No soundcards found.
      EXT4-fs (mmcblk0p2): recovery complete
      EXT4-fs (mmcblk0p2): mounted filesystem 61c00ade-b582-4574-a434-d56f9cb59143 r/w with ordered data mode. Quota mode: disabled.
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
      systemd[1]: systemd-modules-load.service: Main process exited, code=exited, status=1/FAILURE
      systemd[1]: systemd-modules-load.service: Failed with result 'exit-code'.
      systemd[1]: Failed to start Load Kernel Modules.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
               Mounting FUSE Control File System...
      EXT4-fs (mmcblk0p2): re-mounted 61c00ade-b582-4574-a434-d56f9cb59143 r/w. Quota mode: disabled.
               Mounting Kernel Configuration File System...
               Starting Apply Kernel Variables...
      [  OK  ] Finished Remount Root and Kernel File Systems.
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.
               Starting Flush Journal to Persistent Storage...
               Starting Load/Save Random Seed...
               Starting Create System Users...
      [  OK  ] Finished Apply Kernel Variables.
      [  OK  ] Finished Set the console keyboard layout.
      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Finished Create System Users.
               Starting Create Static Device Nodes in /dev...
      [  OK  ] Finished Coldplug All udev Devices.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Wait for udev To …plete Device Initialization...
      [  OK  ] Finished Create Static Device Nodes in /dev.
      [  OK  ] Finished Helper to synchronize boot up for ifupdown.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting Rule-based Manage…for Device Events and Files...
      [  OK  ] Finished Flush Journal to Persistent Storage.
      [  OK  ] Started Rule-based Manager for Device Events and Files.
               Starting Show Plymouth Boot Screen...
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Found device /dev/ttyPS0.
      [  OK  ] Found device /dev/disk/by-partuuid/5c29002e-01.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
               Starting File System Check…isk/by-partuuid/5c29002e-01...
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
      [  OK  ] Finished Raise network interfaces.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
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
      [  OK  ] Finished Fix DP audio and X11 for Jupiter.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started Authorization Manager.
      [  OK  ] Reached target Network.
               Starting Modem Manager...
               Starting CUPS Scheduler...
      [  OK  ] Started Erlang Port Mapper Daemon.
               Starting HTTP based time synchronization tool...
               Starting OpenBSD Secure Shell server...
               Starting Permit User Sessions...
      [  OK  ] Finished Permit User Sessions.
               Starting Light Display Manager...
      [  OK  ] Started HTTP based time synchronization tool.
               Starting Load Kernel Module drm...
      [  OK  ] Finished Load Kernel Module drm.
      [  OK  ] Finished Creating IIOD Context Attributes....
      [  OK  ] Started IIO Daemon.
      [  OK  ] Finished Analog Devices power up/down sequence.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Started User Login Management.
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Started DHCP Client Daemon.
      [  OK  ] Reached target Network is Online.
               Starting Internet superserver...
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyPS0

      analog login: root (automatic login)

      Linux analog 6.12.0-27098-g298669e57d37 #380 SMP PREEMPT Mon Mar 23 12:08:09 CST 2026 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Wed Jan  7 09:17:25 PST 2026 on ttyPS0
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

Open IIO Oscilloscope on the host PC, go to **Settings → Connect**,
select the **Manual** option and enter the URI using the board IP:

.. code-block:: none

   ip:<board-ip>

Press **Refresh** to enumerate the IIO context, then press **Connect**.

.. figure:: ../images/ad353XR_iio_connect.jpeg
   :alt: IIO Oscilloscope connect dialog showing AD3530R detected
   :width: 700

   IIO Oscilloscope - connect dialog with AD3530R detected

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

      root@analog:/sys/kernel/debug/iio/iio:device1# iio_info
      iio_info version: 0.26 (git tag:bdd5c000)
      Libiio version: 0.26 (git tag: bdd5c00) backends: local xml ip usb serial
      IIO context created with local backend.
      Backend version: 0.26 (git tag: bdd5c00)
      Backend description string: Linux analog 6.12.0-27098-g298669e57d37 #380 SMP PREEMPT Mon Mar 23 12:08:09 CST 2026 armv7l
      IIO context has 3 attributes:
            hw_carrier: Zynq Cora Z7 Development Board
            local,kernel: 6.12.0-27098-g298669e57d37
            uri: local:
      IIO context has 3 devices:
            iio:device0: xadc
                     9 channels found:
                              voltage5: vccoddr (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccoddr
                                    attr  1: raw value: 1843
                                    attr  2: scale value: 0.732421875
                              voltage0: vccint (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccint
                                    attr  1: raw value: 1365
                                    attr  2: scale value: 0.732421875
                              voltage4: vccpaux (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccpaux
                                    attr  1: raw value: 2457
                                    attr  2: scale value: 0.732421875
                              temp0:  (input)
                              3 channel-specific attributes found:
                                    attr  0: offset value: -2219
                                    attr  1: raw value: 2606
                                    attr  2: scale value: 123.040771484
                              voltage7: vrefn (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vrefn
                                    attr  1: raw value: 5
                                    attr  2: scale value: 0.732421875
                              voltage1: vccaux (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccaux
                                    attr  1: raw value: 2457
                                    attr  2: scale value: 0.732421875
                              voltage2: vccbram (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccbram
                                    attr  1: raw value: 1366
                                    attr  2: scale value: 0.732421875
                              voltage3: vccpint (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vccpint
                                    attr  1: raw value: 1365
                                    attr  2: scale value: 0.732421875
                              voltage6: vrefp (input)
                              3 channel-specific attributes found:
                                    attr  0: label value: vrefp
                                    attr  1: raw value: 1711
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
