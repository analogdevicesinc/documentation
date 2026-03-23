ADAQ8092 ZedBoard User Guide
================================

.. note::
   **UNDER CONSTRUCTION**

.. figure:: ../images/adaq8092.png
   :width: 300px
   :align: center

Introduction
--------------

The :adi:`ADAQ8092` is a 14-bit, 105 MSPS, high-speed dual-channel data acquisition
(DAQ) μModule® solution. It incorporates signal conditioning, ADC driver, and ADC
in a single package via system-in-package (SiP) technology.

This μModule® solution simplifies the development of a high-speed data acquisition
system by transferring the design burden of component selection, optimization, and
layout from the designer to the device. It enables a 6× footprint reduction.

Quick Start (Linux on ZedBoard)
---------------------------------

Prerequisites
~~~~~~~~~~~~~~~~

Required Hardware
^^^^^^^^^^^^^^^^^^^^^^

* :url:`ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>` Rev D or later
* ADAQ8092 FMC board
* :url:`FMC extender board <https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-fmc-ext-g-3074457345635221630/>`
* 8 GB SD card
* Ethernet cable
* Micro-USB cable

Required Software
^^^^^^^^^^^^^^^^^^^^^^

* Host PC (Windows or Linux)
* UART terminal (PuTTY, Tera Term, Minicom, etc.)
  Baud rate: **115200 (8N1)**
* IIO Oscilloscope:
  :url:`https://github.com/analogdevicesinc/iio-oscilloscope/releases`

Creating / Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::
   Use Kuiper Linux to create the SD image for Zynq boards (single image for all boards):
   :adi:`Kuiper Linux <resources:tools-software:linux-software:kuiper-linux>`

In this case the root of 'BOOT' should contain:

* Linux image for Zynq
* ``BOOT.BIN`` specific to **ADAQ8092 + ZedBoard**
* ``system.dtb`` specific to **ADAQ8092 + ZedBoard**

Setting Up the Hardware (ZedBoard)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to:

* Get the <ZedBoard>

  .. figure:: ../images/zedboard.png
     :width: 600px

* Insert the SD-CARD into the SD Card Interface Connector (J12).
* Connect the ADAQ8092 FMC board to the FMC extender board.
* Connect the ADAQ8092 FMC with the extender board to the FPGA carrier FMC-LPC socket.
* Connect USB UART J14 (Micro USB) to your host PC.
* Plug your ethernet cable into the RJ45 ethernet connector(J11).
* Plug the Power Supply into 12V Power input connector (J20) (DO NOT turn the device on).
* Set the jumpers as seen in the below picture:

  .. figure:: ../images/zed_jumpers.jpg
     :width: 400px

.. tip::
   Ensure **VADJ is set to 2.5 V** before powering on the board.

* Power on the board
* Wait ~30 seconds for the **DONE** LED (near DISP1) to turn blue

.. esd-warning::

Booting the SD Card
~~~~~~~~~~~~~~~~~~~~~~

Remote IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Observe kernel and serial console messages on your UART terminal (use the first ttyUSB or COM port resisted):

.. collapsible:: Complete boot log

   ::

      Booting Linux on physical CPU 0x0
      Linux version 5.10.0-98063-gfe3c980b3ef1-dirty (amiclaus@amiclaus-VirtualBox) (a                                                                                                                                                             rm-linux-gnueabihf-gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, GNU ld (GNU Binutil                                                                                                                                                             s for Ubuntu) 2.34) #51 SMP PREEMPT Thu Mar 3 16:24:26 EET 2022
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
      percpu: Embedded 15 pages/cpu s29900 r8192 d23348 u61440
      Built 1 zonelists, mobility grouping on.  Total pages: 130048
      Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootf                                                                                                                                                             stype=ext4 rootwait clk_ignore_unused cpuidle.off=1
      Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
      mem auto-init: stack:off, heap alloc:off, heap free:off
      Memory: 367344K/524288K available (10240K kernel code, 774K rwdata, 7352K rodata                                                                                                                                                             , 1024K init, 170K bss, 25872K reserved, 131072K cma-reserved, 0K highmem)
      rcu: Preemptible hierarchical RCU implementation.
      rcu:    RCU event tracing is enabled.
      rcu:    RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
              Trampoline variant of Tasks RCU enabled.
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
      random: get_random_bytes called from start_kernel+0x33c/0x4dc with crng_init=0
      zynq_clock_init: clkc starts at (ptrval)
      Zynq clock init
      sched_clock: 64 bits at 333MHz, resolution 3ns, wraps every 4398046511103ns
      clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x4ce07af025                                                                                                                                                             , max_idle_ns: 440795209040 ns
      Switching to timer-based delay loop, resolution 3ns
      clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 5375                                                                                                                                                             38477 ns
      timer #0 at (ptrval), irq=25
      Console: colour dummy device 80x30
      Calibrating delay loop (skipped), value calculated using timer frequency.. 666.6                                                                                                                                                             6 BogoMIPS (lpj=3333333)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      CPU: Testing write buffer coherency: ok
      CPU0: Spectre v2: using BPIALL workaround
      CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      Setting up static identity map for 0x100000 - 0x100060
      rcu: Hierarchical SRCU implementation.
      smp: Bringing up secondary CPUs ...
      CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      CPU1: Spectre v2: using BPIALL workaround
      smp: Brought up 1 node, 2 CPUs
      SMP: Total of 2 processors activated (1333.33 BogoMIPS).
      CPU: All CPU(s) started in SVC mode.
      devtmpfs: initialized
      VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 1911                                                                                                                                                             2604462750000 ns
      futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      pinctrl core: initialized pinctrl subsystem
      NET: Registered protocol family 16
      DMA: preallocated 256 KiB pool for atomic coherent allocations
      thermal_sys: Registered thermal governor 'step_wise'
      hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      hw-breakpoint: maximum watchpoint size is 4 bytes.
      zynq-ocm f800c000.ocmc: ZYNQ OCM pool: 256 KiB @ 0x(ptrval)
      e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 33, base_baud = 3125000) is a                                                                                                                                                              xuartps
      printk: console [ttyPS0] enabled
      SCSI subsystem initialized
      usbcore: registered new interface driver usbfs
      usbcore: registered new interface driver hub
      usbcore: registered new device driver usb
      mc: Linux media interface: v0.10
      videodev: Linux video capture interface: v2.00
      jesd204: found 0 devices and 0 topologies
      FPGA manager framework
      Advanced Linux Sound Architecture Driver Initialized.
      clocksource: Switched to clocksource arm_global_timer
      NET: Registered protocol family 2
      tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
      TCP established hash table entries: 4096 (order: 2, 16384 bytes, linear)
      TCP bind hash table entries: 4096 (order: 3, 32768 bytes, linear)
      TCP: Hash tables configured (established 4096 bind 4096)
      UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
      UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
      NET: Registered protocol family 1
      hw perfevents: no interrupt-affinity property for /pmu@f8891000, guessing.
      hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
      workingset: timestamp_bits=30 max_order=17 bucket_order=0
      io scheduler mq-deadline registered
      io scheduler kyber registered
      zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
      dma-pl330 f8003000.dmac: Loaded driver for PL330 DMAC-241330
      dma-pl330 f8003000.dmac:        DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Even                                                                                                                                                             ts-16
      brd: module loaded
      loop: module loaded
      Registered mathworks_ip class
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
      libphy: Fixed MDIO Bus: probed
      tun: Universal TUN/TAP device driver, 1.6
      libphy: MACB_mii_bus: probed
      macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 36 (aa                                                                                                                                                             :bb:cc:dd:ee:ff)
      usbcore: registered new interface driver asix
      usbcore: registered new interface driver ax88179_178a
      usbcore: registered new interface driver cdc_ether
      usbcore: registered new interface driver net1080
      usbcore: registered new interface driver cdc_subset
      usbcore: registered new interface driver zaurus
      usbcore: registered new interface driver cdc_ncm
      ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
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
      usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
      usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      usb usb1: Product: EHCI Host Controller
      usb usb1: Manufacturer: Linux 5.10.0-98063-gfe3c980b3ef1-dirty ehci_hcd
      usb usb1: SerialNumber: ci_hdrc.0
      hub 1-0:1.0: USB hub found
      hub 1-0:1.0: 1 port detected
      i2c /dev entries driver
      adv7511 0-0039: supply avdd not found, using dummy regulator
      adv7511 0-0039: supply dvdd not found, using dummy regulator
      adv7511 0-0039: supply pvdd not found, using dummy regulator
      adv7511 0-0039: supply bgvdd not found, using dummy regulator
      adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
      at24 1-0050: supply vcc not found, using dummy regulator
      at24 1-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      usbcore: registered new interface driver uvcvideo
      USB Video Class driver (1.1.1)
      gspca_main: v2.14.0 registered
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
      mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
      mmc0: new high speed SDHC card at address aaaa
      mmcblk0: mmc0:aaaa SC32G 29.7 GiB
       mmcblk0: p1 p2 p3
      cf_axi_adc 44a00000.cf_axi_adc: ADI AIM (10.01.b) at 0x44A00000 mapped to 0x(ptr                                                                                                                                                             val), probed ADC adaq8092_axi_adc as MASTER
      axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      axi_sysid 45000000.axi-sysid-0: [adaq8092_fmc] on [zed] git branch <stage1_adaq8                                                                                                                                                             092_ddr_lvds> git <23ffcde9632eab2ff9d7df0edb590b73079a3310> clean [2022-03-03 1                                                                                                                                                             2:33:32] UTC
      fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
      usbcore: registered new interface driver snd-usb-audio
      axi-i2s 77600000.axi-i2s: probed, capture enabled, playback enabled
      NET: Registered protocol family 10
      Segment Routing with IPv6
      sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      NET: Registered protocol family 17
      NET: Registered protocol family 36
      Registering SWP/SWPB emulation handler
      [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for 70e00000.axi_hdmi on minor 0
      axi-hdmi 70e00000.axi_hdmi: [drm] Cannot find any crtc or sizes
      clk: Not disabling unused clocks
      ALSA device list:
        #0: HDMI monitor
        #1: ZED ADAU1761
      EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      VFS: Mounted root (ext4 filesystem) on device 179:2.
      devtmpfs: mounted
      Freeing unused kernel memory: 1024K
      Run /sbin/init as init process
      random: fast init done
      systemd[1]: System time before build time, advancing clock.
      systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPA                                                                                                                                                             RMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOM                                                                                                                                                             P +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
      systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 10 (buster)!

      systemd[1]: Set hostname to <analog>.
      systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an I                                                                                                                                                             P firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup                                                                                                                                                              based firewalling.
      systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only show                                                                                                                                                             n for the first loaded unit using IP firewalling.)
      systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of sect                                                                                                                                                             ion. Ignoring.
      systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of sect                                                                                                                                                             ion. Ignoring.
      random: systemd: uninitialized urandom read (16 bytes read)
      random: systemd: uninitialized urandom read (16 bytes read)
      systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R&uests to Wall Directory Watch.
      random: systemd: uninitialized urandom read (16 bytes read)
      systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [  OK  ] Listening on Journal Socket.
               Mounting Kernel Debug File System...
      [  OK  ] Created slice system-serial\x2dgetty.slice.
               Starting Set the console keyboard layout...
      [  OK  ] Listening on udev Control Socket.
               Starting udev Coldplug all Devices...
               Starting Load Kernel Modules...
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [  OK  ] Created slice User and Session Slice.
      [  OK  ] Reached target Slices.
               Mounting RPC Pipe File System...
      [  OK  ] Listening on Journal Socket (/dev/log).
               Starting Restore / save the current clock...
      [  OK  ] Reached target Swap.
               Starting Journal Service...
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-getty.slice.
      [  OK  ] Mounted Kernel Debug File System.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [FAILED] Failed to mount RPC Pipe File System.
      See 'systemctl status run-rpc_pipefs.mount' for details.
      [DEPEND] Dependency failed for RPC &ice for NFS client and server.
      [DEPEND] Dependency failed for RPC &curity service for NFS server.
      [  OK  ] Started Journal Service.
      [  OK  ] Started Set the console keyboard layout.
      [  OK  ] Started Restore / save the current clock.
      [  OK  ] Started udev Coldplug all Devices.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Remount Root and Kernel File Systems...
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
               Starting Apply Kernel Variables...
               Mounting Kernel Configuration File System...
      [  OK  ] Started Helper to synchronize boot up for ifupdown.
      [  OK  ] Started Apply Kernel Variables.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Started Remount Root and Kernel File Systems.
               Starting Create System Users...
               Starting Load/Save Random Seed...
               Starting Flush Journal to Persistent Storage...
      [  OK  ] Started Create System Users.
      [  OK  ] Started Load/Save Random Seed.
               Starting Create Static Device Nodes in /dev...
      [  OK  ] Started Flush Journal to Persistent Storage.
      [  OK  ] Started Create Static Device Nodes in /dev.
      [  OK  ] Reached target Local File Systems (Pre).
               Starting udev Kernel Device Manager...
      [  OK  ] Started udev Kernel Device Manager.
               Starting Show Plymouth Boot Screen...
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Started Forward Password R&s to Plymouth Directory Watch.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Found device /dev/ttyPS0.
      [  OK  ] Found device /dev/disk/by-partuuid/004ba301-01.
               Starting Load Kernel Modules...
               Starting File System Check&isk/by-partuuid/004ba301-01...
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Started File System Check Daemon to report status.
      [  OK  ] Started File System Check &/disk/by-partuuid/004ba301-01.
               Mounting /boot...
      [  OK  ] Mounted /boot.
      [  OK  ] Reached target Local File Systems.
               Starting Set console font and keymap...
               Starting Preprocess NFS configuration...
               Starting Create Volatile Files and Directories...
               Starting Tell Plymouth To Write Out Runtime Data...
               Starting Raise network interfaces...
      [  OK  ] Started Set console font and keymap.
      [  OK  ] Started Preprocess NFS configuration.
      [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Started Create Volatile Files and Directories.
               Starting Network Time Synchronization...
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Started Update UTMP about System Boot/Shutdown.
      [  OK  ] Started Network Time Synchronization.
      [  OK  ] Reached target System Time Synchronized.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Started CUPS Scheduler.
      [  OK  ] Reached target Paths.
      [  OK  ] Listening on GPS (Global P&ioning System) Daemon Sockets.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Started Daily man-db regeneration.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Listening on CUPS Scheduler.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Reached target Sockets.
      [  OK  ] Reached target Basic System.
      [  OK  ] Started D-Bus System Message Bus.
      [  OK  ] Started Manage Sound Card State (restore and store).
      [  OK  ] Started CUPS Scheduler.
               Starting LSB: Switch to on&nless shift key is pressed)...
      [  OK  ] Started Regular background program processing daemon.
      [  OK  ] Started tof-server.service.
               Starting System Logging Service...
               Starting Modem Manager...
               Starting Check for Raspberry Pi EEPROM updates...
               Starting Disk Manager...
               Starting Avahi mDNS/DNS-SD Stack...
               Starting Save/Restore Sound Card State...
               Starting dphys-swapfile - &unt, and delete a swap file...
               Starting Login Service...
      [  OK  ] Started Daily apt download activities.
               Starting rng-tools.service...
      [  OK  ] Started Daily rotation of log files.
               Starting triggerhappy global hotkey daemon...
               Starting dhcpcd on all interfaces...
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Reached target Timers.
               Starting WPA supplicant...
      [  OK  ] Started System Logging Service.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started Check for Raspberry Pi EEPROM updates.
      [FAILED] Failed to start rng-tools.service.
      See 'systemctl status rng-tools.service' for details.
      [  OK  ] Started Save/Restore Sound Card State.
      [  OK  ] Reached target Sound Card.
      [  OK  ] Started Login Service.
      [  OK  ] Started Raise network interfaces.
      [  OK  ] Started LSB: Switch to ond&(unless shift key is pressed).
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Started dhcpcd on all interfaces.
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started dphys-swapfile - s&mount, and delete a swap file.
      [  OK  ] Reached target Network.
               Starting Permit User Sessions...
      [  OK  ] Reached target Network is Online.
               Starting Internet superserver...
      [  OK  ] Started IIO Daemon.
               Starting /etc/rc.local Compatibility...
               Starting OpenBSD Secure Shell server...
               Starting HTTP based time synchronization tool...
      [  OK  ] Started Internet superserver.
      [  OK  ] Started Permit User Sessions.
      [  OK  ] Started /etc/rc.local Compatibility.
               Starting Authorization Manager...
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started OpenBSD Secure Shell server.
      [  OK  ] Started Authorization Manager.

      Raspbian GNU/Linux 10 analog ttyPS0

      analog login: root (automatic login)

      Last login: Thu Mar  3 15:00:15 GMT 2022 on ttyPS0
      Linux analog 5.10.0-98063-gfe3c980b3ef1-dirty #51 SMP PREEMPT Thu Mar 3 16:24:26                                                                                                                                                              EET 2022 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      root@analog:~# 

      Login credentials:

      +----------+----------+
      | **User** | **Pass** |
      +----------+----------+
      | root     | analog   |
      +----------+----------+

* Run the ifconfig command on your UART terminal and get your board IP.

.. code-block:: console

   root@analog:~# ifconfig
   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>
         inet <board_ip> netmask 255.255.255.0

* Open IIO Scope application and type ip:board_ip in the URI tab.

.. figure:: ../images/iioosc_remote_adaq8092_zed_login.png
   :width: 700px

You should see two screens:

.. figure:: ../images/iioosc_remote_adaq8092_zed.png
   :width: 1000px

.. important::
    Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with sudo shutdown -h now

Hardware
----------

.. note::
   Hardware details will be added later.

Reference HDL Design
----------------------

Functional Overview
~~~~~~~~~~~~~~~~~~~~~~~

The reference design is a processor-based (ARM) embedded system.
A functional block diagram of the system is given below.
The device interface is a self-contained peripheral similar to other such pcores in the system. The core is programmable through an AXI-lite interface.

.. figure:: ../images/adaq8092_xilinx_v4.png
   :width: 800px

Reference Design Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Project:
  :url:`https://github.com/analogdevicesinc/hdl/tree/master/projects/adaq8092_fmc`

* Carrier (ZedBoard):
  :url:`https://github.com/analogdevicesinc/hdl/tree/master/projects/adaq8092_fmc/zed`

* Library Cores:
   - :url:`axi_adaq8092 <https://github.com/analogdevicesinc/hdl/tree/master/library/axiadaq8092>`
   - :url:`axi_dmac <https://github.com/analogdevicesinc/hdl/tree/master/library/axi_dmac>`
   - :url:`axi_hdmi_tx <https://github.com/analogdevicesinc/hdl/tree/master/library/axi_hdmi_tx>`
   - :url:`util_cpack2 <https://github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/util_pack/util_cpack2>`

No‑OS Drivers
---------------

.. note::
   No‑OS driver documentation will be added here.

More Information
------------------

* :adi:`ADAQ8092 Datasheet`
* :adi:`AXI‑ADAQ8092 <resources:fpga:docs:adaq8092>`

.. ../common/support.rst
