.. _kuiper:

Kuiper Linux
============

Analog Devices Kuiper Linux is a distribution based on Raspberry Pi OS for the
Raspberry Pi. It incorporates thousands of Linux device drivers for ADI
products, and is created with ease of use in mind. The reasoning for creating
this distribution is to minimize the barriers to integrating ADI hardware
devices into an embedded Linux system. ADI Kuiper Linux also includes a host of
additional applications, software libraries, and utilities including for rapid
prototyping and development

-  IIO Oscilloscope (basic GUI for debugging IIO devices)
-  IIOD (exposes IIO devices over a network connection to a remote host)
-  libiio (library for applications running locally)
-  pyadi-iio (Python abstraction layer for iio devices)
-  libm2k (software API for the ADALM2000 multifunction USB instrument)
-  GNURadio (including GR-IIO blocks, ADALM2000, ADALM-Pluto blocks)

ADI Kuiper Linux supports many platforms and development kits containing
AMD(Xilinx) and Intel(Altera) FPGAs, as well as Raspberry Pi systems.
Please see :ref `kuiper project-list`
for a complete list of supported development kits and hardware projects.

Requirements
------------

- You need a Host PC (Windows or Linux).
- You need a SD card writer connected to above PC (Supported USB SD
  readers/writers are OK).
- 16 GB SD Card
- Imager Application (Etcher, Raspberry Pi Imager, WinDisk32)

Release Notes
-------------

.. toctree::
   :hidden:

   release-notes

See :ref:`kuiper release-notes`.

.. admonition:: SD Card Write Issues
   :class: warning

   If your computer has security restrictions imposed by your company's IT
   department, which prevent you from writing data to SD-cards (or the data is
   encrypted when written on the SD-card), then consider using a computer that
   doesn't have such restrictions, or communicating with your IT department to
   find a solution.

.. _kuiper imaging sdcard:

Imaging your SD Card
--------------------

If you are planning on imaging your own SD card, depending if you are using
Linux or Windows, follow these instructions to write the image file to your SD
card.

.. toctree::
   :hidden:

   sdcard/index

* :ref:`kuiper sdcard linux`
* :ref:`kuiper sdcard windows`


Supported Projects
------------------

.. toctree::
   :hidden:

   project-list

See :ref:`Complete Project List <kuiper project-list>`.

Users and Passwords
-------------------

The default user is the "analog" user, the password for this user is "analog".
The password for the "root" account is "analog" as well.

.. list-table::
   :header-rows: 1

   * - User
     - Password
   * - root
     - analog
   * - analog
     - analog

Configuring the SD Card for FPGA Projects
-----------------------------------------

The SD card includes several folders in the root directory of the ``BOOT``
partition. In order to configure the SD card to work with a specific FPGA board
and ADI hardware, several files must be copied onto the root directory. Using
the host PC, drag and drop the required files onto the ``BOOT`` partition, and
use the **EJECT** function when removing the SD card from the reader.

AMD/Xilinx
~~~~~~~~~~

For the **zynq projects** copy these files to the root of the BOOT FAT32
partition:

#. target/BOOT.BIN
#. target/<specific_folder>/devicetree.dtb
#. zynq-common/uImage

For the **zynqmp projects** copy these files to the root of the BOOT FAT32
partition:

#. target/BOOT.BIN
#. target/<specific_folder>/system.dtb
#. zynqmp-common/Image

For the **versal projects** copy these files to the root of the BOOT FAT32
partition:

#. target/BOOT.BIN
#. target/<specific_folder>/system.dtb
#. target/boot.scr
#. versal-common/Image

Intel/Altera
~~~~~~~~~~~~

For **Arria10 SOC projects** copy these files to the root of the BOOT FAT32
partition:

#. target/fit_spl_fpga.itb
#. target/socfpga_arria10_socdk_sdmmc.dtb
#. target/u-boot.img
#. socfpga_arria10_common/zImage
#. socfpga_arria10_common/extlinux.conf, inside a folder named 'extlinux'.
   Create the folder if it does not exist;
#. write preloader file (fit_spl_fpga.itb) to the corresponding SD card
   partition (third partition - 4MB in size).

(e.g. :code:`dd if=u-boot-splx4.sfp of=/dev/mmcblk0p3`).

For **Cyclone5 projects** copy these files to the root of the BOOT FAT32
partition:

#. target/soc_system.rbf
#. target/socfpga.dtb
#. target/u-boot.scr
#. target/u-boot-with-spl.sfp
#. socfpga_cyclone5_common/zImage
#. socfpga_cyclone5_common/extlinux.conf , in a folder called 'extlinux'. Create
   the folder if it does not exist;
#. write preloader file (u-boot-with-spl.sfp) to the corresponding SD card
   partition (third partition - 4MB in size)

(e.g. :code:`dd if=u-boot-with-spl.bin of=/dev/mmcblk0p3`).

Configuring the SD Card for Raspberry Pi Projects
-------------------------------------------------

The system will need to be configured according to what devices are connected to
the Raspberry Pi. The most straightforward way to do this for Raspberry Pi is to
edit the config.txt file, which is located in the boot partition. Any text
editor can be used, including the Mousepad editor that is included with Kuiper
Linux. Using the Raspberry Pi itself also avoids problems with USB encryption,
often present on company computers.

Connect a keyboard, mouse, and monitor to the Raspberry Pi and connect power.
The ADI Kuiper Linux desktop should appear. Before editing, it is a good idea to
make a backup of the original file, just in case something goes wrong (which it
won't, but still...) Open a terminal and enter the following command (noting
that "analog@analog:~ $" is the prompt, and does not need to be typed):

.. code-block::

   analog@analog:~ $ sudo cp /boot/config.txt /boot/config.backup
   analog@analog:~ $ sudo mousepad /boot/config.txt

This will bring up the text editor. At this point, the appropriate device tree
overlays can be included, for example, add the following line to enable the
ADXL345 3-axis SPI accelerometer, noting that the lirc-rpi lines are shown for
reference, and any line beginning with "#" is ignored:

.. code-block::

   # Uncomment this to enable the lirc-rpi module
   #dtoverlay=lirc-rpi
   dtoverlay=rpi-adxl345

Many ADI hardware overlays are included with Kuiper Linux, for evaluation boards
and reference designs. For a complete list of overlays for available hardware,
please visit the :ref:`project list <kuiper project-list>`.

After editing config.txt, **reboot** for changes to take effect.

.. code-block::

   analog@analog:~ $ reboot

System Verification
-------------------

There are two things to check when making sure your system is setup properly.

#. The platform is booting to Kuiper Linux
#. The hardware configuration files are correct

Physical System Setup
~~~~~~~~~~~~~~~~~~~~~

#. On the platform board

   #. Insert the SD card
   #. Plug in the monitor (HDMI or display port)
   #. Connect the USB keyboard/mouse
   #. Plug in the console UART cable

#. Ensure all the hardware jumpers and switches are set properly for the
   platform board to boot from SD card
#. Plug the ADI hardware into the correct connector according to the user guide
   of the board
#. Connect the console UART cable to the PC
#. Power on the setup

Successful Boot Message
~~~~~~~~~~~~~~~~~~~~~~~

The example boot messages may change based on your specific platform, but when
connected to UART via a serial terminal session from your host PC, your terminal
should read similar to the the log provided below. Make sure when creating a
serial connection, you are using the baud rate of 115200 and you are connected
**BEFORE** you power up your platform.

.. collapsible:: Complete boot log

   .. code-block::

      rgetz@brain:~/newest$ kermit -l /dev/ttyACM0 -b 115200  -c
      Connecting to /dev/ttyACM0, speed 115200
       Escape character: Ctrl-\ (ASCII 28, FS): enabled
      Type the escape character followed by C to get back,
      or followed by ? to see other options.
      ----------------------------------------------------

      U-Boot SPL 2021.07-16360-gee63370553-dirty (Jun 09 2022 - 23:13:35 +0300)
      FPGA: Checking FPGA configuration setting ...
      FPGA: Start to program peripheral/full bitstream ...
      FPGA: Early Release Succeeded.
      FPGA: Checking FPGA configuration setting ...
      FPGA: Start to program peripheral/full bitstream ...
      FPGA: Early Release Succeeded.

      U-Boot SPL 2021.07-16360-gee63370553-dirty (Jun 09 2022 - 23:13:35 +0300)
      DDRCAL: Success
      FPGA: Checking FPGA configuration setting ...
      FPGA: Start to program core bitstream ...
      Full Configuration Succeeded.
      FPGA: Enter user mode.
      WDT:   Started with servicing (10s timeout)
      Trying to boot from MMC1

      U-Boot 2021.07-16360-gee63370553-dirty (Jun 09 2022 - 23:13:35 +0300)socfpga_arria10, Build: jenkins-master-quartus_boot_on_ubuntu_master-97

      CPU:   Altera SoCFPGA Arria 10
      BOOT:  SD/MMC External Transceiver (1.8V)
      Model: Altera SOCFPGA Arria 10
      DRAM:  1 GiB
      WDT:   Started with servicing (10s timeout)
      MMC:   dwmmc0@ff808000: 0
      Loading Environment from MMC... OK
      In:    serial
      Out:   serial
      Err:   serial
      Model: Altera SOCFPGA Arria 10
      Net:   eth0: ethernet@ff800000
      Hit any key to stop autoboot:  0
      150 bytes read in 4 ms (36.1 KiB/s)
      ## Executing script at 02100000
      Failed to load 'soc_system.rbf'
      Full Configuration Succeeded.
      FPGA: Enter user mode.
      15038392 bytes read in 730 ms (19.6 MiB/s)
      fpga - loadable FPGA image support

      Usage:
      fpga [operation type] [device number] [image address] [image size]
      fpga operations:
        dump  [dev] [address] [size]  Load device to memory buffer
        info  [dev]                   list known device information
        load  [dev] [address] [size]  Load device from memory buffer
        loadb [dev] [address] [size]  Load device from bitstream buffer (Xilinx only)
        loadmk [dev] [address]        Load device generated with mkimage
              For loadmk operating on FIT format uImage address must include
              subimage unit name in the form of addr:<subimg_uname>
      switch to partitions #0, OK
      mmc0 is current device
      Scanning mmc 0:1...
      Found /extlinux/extlinux.conf
      Retrieving file: /extlinux/extlinux.conf
      162 bytes read in 5 ms (31.3 KiB/s)
      1:      Linux Default
      Retrieving file: /extlinux/../zImage
      8289256 bytes read in 408 ms (19.4 MiB/s)
      append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      Retrieving file: /extlinux/../socfpga_arria10_socdk_sdmmc.dtb
      30586 bytes read in 9 ms (3.2 MiB/s)
      Kernel image @ 0x1000000 [ 0x000000 - 0x7e7be8 ]
      ## Flattened Device Tree blob at 02000000
         Booting using the fdt blob at 0x2000000
         Loading Device Tree to 09ff5000, end 09fff779 ... OK
      Starting kernel ...

      Deasserting all peripheral resets
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 5.10.0-98183-gf814ae972859-dirty (liviu@LADACE-Debian) (arm-none-linux-gnueabihf-gcc (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 10.2.1 20201103, GNU ld (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16)) 2.35.1.20201028) #27 SMP Wed May 25 16:01:50 EEST 2022
      [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Altera SOCFPGA Arria 10
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
      [    0.000000] percpu: Embedded 19 pages/cpu s45324 r8192 d24308 u77824
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
      [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] Memory: 884076K/1048576K available (13312K kernel code, 1284K rwdata, 7440K rodata, 1024K init, 348K bss, 33428K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 42085 entries in 83 pages
      [    0.000000] ftrace: allocated 83 pages with 4 groups
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000]  Rude variant of Tasks RCU enabled.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      [    0.000000] L2C-310 erratum 769419 enabled
      [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
      [    0.000000] L2C-310: enabling full line of zeros but not enabled in Cortex-A9
      [    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
      [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
      [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
      [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76560001
      [    0.000000] random: get_random_bytes called from start_kernel+0x39c/0x558 with crng_init=0
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000005] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.007886] Switching to timer-based delay loop, resolution 10ns
      [    0.014168] Console: colour dummy device 80x30
      [    0.018614] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.029098] pid_max: default: 32768 minimum: 301
      [    0.033798] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.041076] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.049358] CPU: Testing write buffer coherency: ok
      [    0.054259] CPU0: Spectre v2: using BPIALL workaround
      [    0.059451] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.065541] Setting up static identity map for 0x100000 - 0x100060
      [    0.071799] rcu: Hierarchical SRCU implementation.
      [    0.076836] smp: Bringing up secondary CPUs ...
      [    0.081933] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.081940] CPU1: Spectre v2: using BPIALL workaround
      [    0.092713] smp: Brought up 1 node, 2 CPUs
      [    0.096792] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.103043] CPU: All CPU(s) started in SVC mode.
      [    0.108126] devtmpfs: initialized
      [    0.115824] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.123762] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.133573] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.144486] NET: Registered protocol family 16
      [    0.150612] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.158377] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.166360] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.178562] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
      [    0.191504] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
      [    0.212418] vgaarb: loaded
      [    0.215392] SCSI subsystem initialized
      [    0.219290] usbcore: registered new interface driver usbfs
      [    0.224797] usbcore: registered new interface driver hub
      [    0.230122] usbcore: registered new device driver usb
      [    0.235284] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
      [    0.245476] mc: Linux media interface: v0.10
      [    0.249753] videodev: Linux video capture interface: v2.00
      [    0.255312] pps_core: LinuxPPS API ver. 1 registered
      [    0.260254] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.269376] PTP clock support registered
      [    0.273547] jesd204: found 0 devices and 0 topologies
      [    0.278599] FPGA manager framework
      [    0.282059] Advanced Linux Sound Architecture Driver Initialized.
      [    0.289059] clocksource: Switched to clocksource timer1
      [    0.814051] NET: Registered protocol family 2
      [    0.818906] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
      [    0.827312] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.835085] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.842298] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.848723] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.855377] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.862577] NET: Registered protocol family 1
      [    0.867321] RPC: Registered named UNIX socket transport module.
      [    0.873246] RPC: Registered udp transport module.
      [    0.877928] RPC: Registered tcp transport module.
      [    0.882620] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.889045] PCI: CLS 0 bytes, default 64
      [    0.894135] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.905441] NFS: Registering the id_resolver key type
      [    0.910533] Key type id_resolver registered
      [    0.914697] Key type id_legacy registered
      [    0.918694] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
      [    0.925534] ntfs: driver 2.1.32 [Flags: R/W].
      [    0.930026] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.936524] fuse: init (API version 7.32)
      [    0.940868] bounce: pool size: 64 pages
      [    0.944693] io scheduler mq-deadline registered
      [    0.949230] io scheduler kyber registered
      [    0.957511] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
      [    0.964223] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    0.974943] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.982120] printk: console [ttyS0] disabled
      [    0.986427] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 45, base_baud = 6250000) is a 16550A
      [    0.995416] printk: console [ttyS0] enabled
      [    0.995416] printk: console [ttyS0] enabled
      [    1.003753] printk: bootconsole [earlycon0] disabled
      [    1.003753] printk: bootconsole [earlycon0] disabled
      [    1.015314] brd: module loaded
      [    1.018644] at24 0-0051: supply vcc not found, using dummy regulator
      [    1.026304] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
      [    1.034084] spi_altera ff200040.spi: regoff 0, irq 48
      [    1.040511] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
      [    1.047986] libphy: Fixed MDIO Bus: probed
      [    1.052567] CAN device driver interface
      [    1.056629] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.063246] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
      [    1.069526] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
      [    1.076198] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
      [    1.082581] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
      [    1.089769] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
      [    1.096011] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
      [    1.102086] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    1.108850] stmmaceth ff800000.ethernet:     DWMAC1000
      [    1.113722] stmmaceth ff800000.ethernet: DMA HW capability register supported
      [    1.120841] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
      [    1.127943] stmmaceth ff800000.ethernet: COE Type 2
      [    1.132807] stmmaceth ff800000.ethernet: TX Checksum insertion supported
      [    1.139484] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
      [    1.146068] stmmaceth ff800000.ethernet: Enabled extended descriptors
      [    1.152490] stmmaceth ff800000.ethernet: Ring mode enabled
      [    1.157950] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    1.173670] libphy: stmmac: probed
      [    1.177073] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
      [    1.190760] usbcore: registered new interface driver asix
      [    1.196178] usbcore: registered new interface driver ax88179_178a
      [    1.202304] usbcore: registered new interface driver cdc_ether
      [    1.208130] usbcore: registered new interface driver net1080
      [    1.213804] usbcore: registered new interface driver cdc_subset
      [    1.219725] usbcore: registered new interface driver zaurus
      [    1.225310] usbcore: registered new interface driver cdc_ncm
      [    1.231429] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
      [    1.238653] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
      [    1.246013] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    1.253648] dwc2 ffb00000.usb: DWC OTG Controller
      [    1.258354] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
      [    1.265430] dwc2 ffb00000.usb: irq 46, io mem 0xffb00000
      [    1.270874] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
      [    1.279113] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.286304] usb usb1: Product: DWC OTG Controller
      [    1.290994] usb usb1: Manufacturer: Linux 5.10.0-98183-gf814ae972859-dirty dwc2_hsotg
      [    1.298787] usb usb1: SerialNumber: ffb00000.usb
      [    1.303852] hub 1-0:1.0: USB hub found
      [    1.307616] hub 1-0:1.0: 1 port detected
      [    1.312338] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
      [    1.318839] ehci-pci: EHCI PCI platform driver
      [    1.323776] usbcore: registered new interface driver uas
      [    1.329160] usbcore: registered new interface driver usb-storage
      [    1.335214] usbcore: registered new interface driver usbserial_generic
      [    1.341746] usbserial: USB Serial support registered for generic
      [    1.347745] usbcore: registered new interface driver ftdi_sio
      [    1.353494] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.360844] usbcore: registered new interface driver upd78f0730
      [    1.366749] usbserial: USB Serial support registered for upd78f0730
      [    1.376546] rtc-ds1307 0-0068: SET TIME!
      [    1.384754] rtc-ds1307 0-0068: registered as rtc0
      [    1.389543] i2c /dev entries driver
      [    1.393645] usbcore: registered new interface driver uvcvideo
      [    1.399381] USB Video Class driver (1.1.1)
      [    1.407645] ltc2978: probe of 0-005c failed with error -121
      [    1.413942] Synopsys Designware Multimedia Card Interface Driver
      [    1.420180] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
      [    1.426844] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
      [    1.433036] dw_mmc ff808000.dwmmc0: Version ID is 270a
      [    1.438197] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 41,32 bit host data width,1024 deep fifo
      [    1.447540] mmc_host mmc0: card is polling.
      [    1.453462] ledtrig-cpu: registered to indicate activity on CPUs
      [    1.459576] usbcore: registered new interface driver usbhid
      [    1.464345] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.465125] usbhid: USB HID core driver
      [    1.490963] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
      [    1.498177] usbcore: registered new interface driver snd-usb-audio
      [    1.506251] NET: Registered protocol family 10
      [    1.511420] Segment Routing with IPv6
      [    1.515131] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.521517] NET: Registered protocol family 17
      [    1.525961] NET: Registered protocol family 15
      [    1.530557] can: controller area network core
      [    1.534941] NET: Registered protocol family 29
      [    1.539395] can: raw protocol
      [    1.542352] can: broadcast manager protocol
      [    1.546521] can: netlink gateway - max_hops=1
      [    1.551013] 8021q: 802.1Q VLAN Support v1.8
      [    1.552310] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.555215] NET: Registered protocol family 36
      [    1.564943] mmc0: new high speed SDHC card at address aaaa
      [    1.569338] Key type dns_resolver registered
      [    1.575303] mmcblk0: mmc0:aaaa SC32G 29.7 GiB
      [    1.579361] oprofile: no performance counters
      [    1.587935] oprofile: using timer interrupt.
      [    1.592299] ThumbEE CPU extension supported.
      [    1.592852]  mmcblk0: p1 p2 p3
      [    1.596566] Registering SWP/SWPB emulation handler
      [    1.628855] adrv9002 spi0.0: adrv9002_setup, 2804: failed with "Failed to reset device and set SPI Config" (3)
      [    1.639954] adrv9002 spi0.0: adrv9002_setup, 2804: failed with "Failed to reset device and set SPI Config" (3)
      [    1.651046] adrv9002 spi0.0: adrv9002_init, 4197: failed with "Failed to reset device and set SPI Config" (3)
      [    1.660988] cf_axi_adc: probe of ff220000.axi-adrv9002-rx1-lpc failed with error -14
      [    1.671202] of_cfs_init
      [    1.673672] of_cfs_init: OK
      [    1.676654] ALSA device list:
      [    1.679631]   No soundcards found.
      [    1.683233] dw-apb-uart ffc02100.serial1: forbid DMA for kernel console
      [    1.707544] random: fast init done
      [    1.942481] EXT4-fs (mmcblk0p2): recovery complete
      [    1.948189] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [    1.956309] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    1.965770] devtmpfs: mounted
      [    1.971587] Freeing unused kernel memory: 1024K
      [    1.976516] Run /sbin/init as init process
      [    2.495793] systemd[1]: System time before build time, advancing clock.
      [    2.546077] systemd[1]: systemd 247.3-7+rpi1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [    2.569272] systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

      [    2.622132] systemd[1]: Set hostname to <analog>.
      [    4.137436] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [    4.378487] systemd[1]: Queued start job for default target Graphical Interface.
      [    4.387531] random: systemd: uninitialized urandom read (16 bytes read)
      [    4.394498] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    4.406868] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [    4.416537] systemd[1]: Created slice system-getty.slice.
      [  OK  ] Created slice system-getty.slice.
      [    4.449268] random: systemd: uninitialized urandom read (16 bytes read)
      [    4.456609] systemd[1]: Created slice system-modprobe.slice.
      [  OK  ] Created slice system-modprobe.slice.
      [    4.489256] random: systemd: uninitialized urandom read (16 bytes read)
      [    4.496572] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [    4.529917] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [    4.559661] systemd[1]: Created slice User and Session Slice.
      [  OK  ] Created slice User and Session Slice.
      [    4.589562] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [    4.619502] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [    4.631946] systemd[1]: Reached target Slices.
      [  OK  ] Reached target Slices.
      [    4.659334] systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      [    4.690278] systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [    4.719816] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [    4.749507] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [    4.802106] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
      [    4.810944] systemd[1]: Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket (/dev/log).
      [    4.839975] systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      [    4.879147] systemd[1]: Listening on udev Control Socket.
      [  OK  ] Listening on udev Control Socket.
      [    4.909763] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [    4.939873] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
      [    4.948438] systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
      [    4.960413] systemd[1]: Mounting RPC Pipe File System...
               Mounting RPC Pipe File System...
      [    4.992209] systemd[1]: Mounting Kernel Debug File System...
               Mounting Kernel Debug File System...
      [    5.022090] systemd[1]: Mounting Kernel Trace File System...
               Mounting Kernel Trace File System...
      [    5.049485] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [    5.065551] systemd[1]: Starting Restore / save the current clock...
               Starting Restore / save the current clock...
      [    5.102840] systemd[1]: Starting Set the console keyboard layout...
               Starting Set the console keyboard layout...
      [    5.140096] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [    5.155786] systemd[1]: Starting Load Kernel Module configfs...
               Starting Load Kernel Module configfs...
      [    5.192594] systemd[1]: Starting Load Kernel Module drm...
               Starting Load Kernel Module drm...
      [    5.212630] systemd[1]: Starting Load Kernel Module fuse...
               Starting Load Kernel Module fuse...
      [    5.254201] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [    5.263665] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [    5.276012] systemd[1]: Starting Journal Service...
               Starting Journal Service...
      [    5.296804] systemd[1]: Starting Load Kernel Modules...
               Starting Load Kernel Modules...
      [    5.342287] systemd[1]: Starting Remount Root and Kernel File Systems...
               Starting Remount Root and Kernel File Systems...
      [    5.382711] systemd[1]: Starting Coldplug All udev Devices...
               Starting Coldplug All udev Devices...
      [    5.426047] systemd[1]: Mounted RPC Pipe File System.
      [  OK  ] Mounted RPC Pipe File System.
      [    5.472608] systemd[1]: Mounted Kernel Debug File System.
      [  OK  ] Mounted Kernel Debug File System.
      [    5.488602] systemd[1]: Mounted Kernel Trace File System.
      [  OK  ] Mounted Kernel Trace File System.
      [    5.520488] systemd[1]: Finished Restore / save the current clock.
      [  OK  ] Finished Restore / save the current clock.
      [    5.596975] systemd[1]: modprobe@configfs.service: Succeeded.
      [    5.611072] systemd[1]: Finished Load Kernel Module configfs.
      [  OK  ] Finished Load Kernel Module configfs.
      [    5.629523] systemd[1]: Started Journal Service.
      [    5.645346] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
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
               Starting Apply Kernel Variables...
      [    6.015539] systemd-journald[98]: Received client request to flush runtime journal.
               Starting Create System Users...
      [    6.056206] systemd-journald[98]: File /var/log/journal/1064eace00dd4e3daeb15d4eed400196/system.journal corrupted or uncleanly shut down, renaming and replacing.
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Finished Coldplug All udev Devices.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Finished Apply Kernel Variables.
      [  OK  ] Finished Create System Users.
               Starting Helper to synchronize boot up for ifupdown...
               Starting Create Static Device Nodes in /dev...
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
      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Reached target Hardware activated USB gadget.
               Starting Load Kernel Modules...
      [  OK  ] Found device /dev/ttyS0.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Found device /dev/disk/by-partuuid/0b25bea5-01.
               Starting File System Check…isk/by-partuuid/0b25bea5-01...
      [  OK  ] Started File System Check Daemon to report status.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
      [  OK  ] Finished File System Check…/disk/by-partuuid/0b25bea5-01.
               Mounting /boot...
      [  OK  ] Mounted /boot.
      [  OK  ] Reached target Local File Systems.
               Starting Set console font and keymap...
               Starting Raise network interfaces...
               Starting Preprocess NFS configuration...
               Starting Tell Plymouth To Write Out Runtime Data...
               Starting Create Volatile Files and Directories...
      [  OK  ] Finished Set console font and keymap.
      [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Finished Preprocess NFS configuration.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
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
               Starting Check for Raspberry Pi EEPROM updates...
               Starting System Logging Service...
               Starting User Login Management...
               Starting triggerhappy global hotkey daemon...
               Starting Disk Manager...
               Starting WPA supplicant...
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
      [  OK  ] Finished Check for Raspberry Pi EEPROM updates.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started Authorization Manager.
      [  OK  ] Started DHCP Client Daemon.
               Starting Modem Manager...
      [  OK  ] Started WPA supplicant.
      [FAILED] Failed to start dphys-swap…mount, and delete a swap file.
      See 'systemctl status dphys-swapfile.service' for details.
      [  OK  ] Finished Raise network interfaces.
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
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started LSB: rng-tools (Debian variant).
      [  OK  ] Found device /dev/ttyGS0.
      [  OK  ] Finished Load USB gadget scheme.
      [  OK  ] Started /etc/rc.local Compatibility.
               Mounting Mount FunctionFS instance...
      [  OK  ] Started Internet superserver.
      [  OK  ] Mounted Mount FunctionFS instance.
      [  OK  ] Finished Permit User Sessions.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started User Login Management.
      [  OK  ] Started Unattended Upgrades Shutdown.
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyS0

      analog login: root (automatic login)

      Password:
      Linux analog 5.10.0-98183-gf814ae972859-dirty #27 SMP Wed May 25 16:01:50 EEST 2022 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Fri Jun 17 14:45:22 BST 2022 on ttyS0
      root@analog:~#


Hardware & Driver Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the platform running Kuiper Linux is powered up, any IIO devices present
and enabled in the configuration file, will be displayed in the terminal window
by running the **iio_info** command, this is a good way to verify that the
hardware and device drivers loaded properly.

Here's an example output:

.. code-block:: bash

   analog@analog:~ $ iio_info
   Library version: 0.21 (git tag: 1c0781b)
   Compiled with backends: local xml ip
   IIO context created with local backend.
   Backend version: 0.21 (git tag: 1c0781b)
   Backend description string: Linux analog 4.19.86-v7l+ #3 SMP Tue Sep 1 19:43:06 UTC 2020 armv7l
   IIO context has 2 attributes:
       local,kernel: 4.19.86-v7l+
       uri: local:
   IIO context has 5 devices:
       iio:device0: ad7127-8 (buffer capable)
           8 channels found:
               voltage0-voltage1:  (input, index: 0, format: be:u24/32>>0)
               6 channel-specific attributes found:
                   attr  0: filter_low_pass_3db_frequency value: 3
                   attr  1: offset value: 0
   ...
   ...

So if your setup is running Kuiper Linux and you can see the device drivers from
your hardware, then you are all set and ready to use the setup!!

Powering Down
-------------

.. important::

   Even thought this is Linux, this is a persistent file
   systems. You have to take care not to corrupt the file system -- please shut
   down things, don't just turn off the power switch. Using the desktop shutdown
   feature is the easiest way, but depending on your monitor, the standard power
   off button could be hiding. You can also do this from the terminal window as
   well with:
   ``sudo shutdown -h now`` or ``sudo poweroff``.

Updating
--------

.. toctree::
   :hidden:

   update

See :ref:`kuiper update`.

Advanced Information For Power Users
------------------------------------

:ref:`linux-kernel`

:ref-hdl:`build_hdl`

:ref-hdl:`build_boot_bin`
