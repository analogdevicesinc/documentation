.. _adrv9002-a10soc:

A10SoC Quick start
===============================================================================

.. image:: ../../images/a10soc_marked.png
   :width: 800

This guide provides quick instructions on how to setup the
:adi:`EVAL-ADRV9002` on:

- :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
  (Rev. C or later) on FMCA

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note::

   For Intel SoC-FPGA boards, one boot file must be written to the third SD
   card partition, which is not accessible from Windows. You will need either
   a native Linux system or WSL to properly configure the SD card. For detailed
   file placement instructions, refer to
   :external+hdl:ref:`Using Kuiper Linux pre-built images <build_intel_boot_image>`.

   On the Kuiper image, the ``zImage file`` and the ``extlinux.conf`` file can be found
   in the carrier-specific folder, which is common to all projects that use this
   carrier. All remaining boot files are located in the project-specific folder.
   The extlinux directory is not provided and must be created by the user.

The following files are needed for the system to boot:

- HDL boot image: ``fit_spl_fpga.itb``
- Linux Kernel image: ``zImage``
- Linux device tree: ``socfpga_arria10_socdk_sdmmc.dtb``
- U-Boot image: ``u-boot.img``
- ``extlinux.conf`` in the **extlinux** folder from SD Card
- Write ``u-boot-splx4.sfp`` on **third** SD Card partition:

Instructions on how to manually build the boot files from source can be found
here:

- :external+hdl:ref:`Building the Intel SoC-FPGA kernel and devicetrees from source <build_intel_boot_image>`
- :external+hdl:ref:`adrv9001` build documentation.
  More HDL build details at :external+hdl:ref:`build_hdl`.

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- SD Card 16GB imaged with :external+kuiper:doc:`Kuiper <index>`
- A UART terminal (Putty/Tera Term/Minicom, etc.) with baud rate 115200 (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
  (Rev. C or later) FPGA board and its power supply
- :adi:`EVAL-ADRV9002` FMC evaluation board
- MicroSD card with at least 16GB of memory
- Mini-USB cable (UART)
- LAN cable (Ethernet)
- Signal generator
- Signal analyzer
- Signal synthesizer (required only if using external clock source)
- 1x SMA cable for signal generator
- 1x SMA cable for signal analyzer
- 1x SMA cable for signal synthesizer (if using external clock)
- (Optional) USB keyboard & mouse and a HDMI compatible monitor

More details as to why you need these, can be found at
:ref:`adrv9002 prerequisites`.

.. _adrv9002-a10soc-changes:

A10SoC required hardware changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

   The following rework is required on the A10SoC FPGA:

   To avoid using an external clock source and fully rely on the
   :adi:`HMC7044` clock chip, rotate the C6D/C4D caps in C5D/C3D position.
   (Please note: In the latest version of the board, this is now the default
   configuration, so this configuration step might not be needed anymore).

   If LEDS V1P0_LED and VINT_LED are not on please depopulate R22M and
   populate R2M.

In the default configuration of the
:intel:`Arria10 SoC Development Kit <content/www/us/en/products/details/fpga/arria/10.html>`,
some of the FMC header pins are connected to a dedicated clock chip.
To be compatible with the :adi:`EVAL-ADRV9002`, these pins need to be connected
directly to the FPGA.

The connection of those pins can be changed by moving the position of
four zero Ohm resistors:

- R612 to R610
- R613 to R611
- R621 to R620
- R633 to R632

These resistors can be found on the backside of the A10SoC, underneath the
FMCA connector (J29). The following picture shows the required configuration
to be compatible with the :adi:`EVAL-ADRV9002`.

.. image:: ../images/a10soc_fmc_rework.jpg
   :width: 900

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../images/adrv9002_a10soc_quickstart.png
   :width: 900

.. esd-warning::

.. warning::

   Before executing the steps below, **VADJ for FMCA must be set to 1.8V**.
   Short pins 9 and 10 on J32 (default position).

On the ADRV9002 card, there is a red LED close to the FMC connector. This LED
indicates if VADJ voltage exceeded 2.0V. If the LED does not turn off after a
few seconds after boot, VADJ is exceeding the recommended level, decreasing
board lifetime and potentially causing permanent damage to the IC.

.. image:: ../images/adrv9002_vadj_led.png
   :width: 900

Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`EVAL-ADRV9002` FMC board to the FMCA carrier socket (G14).
#. On the FMC card, set the switch to select clock source between:

    #. an on-board 38.4 MHz VCTCXO (default)
    #. external (via J501) 10 MHz to 1000 MHz / +13 dBm

#. Connect USB UART (Mini-USB) to your host PC (J10).
#. Insert MicroSD card into socket.
#. Configure the Arria 10 SoC Development Kit for SD card booting (set the
   jumpers and switches accordingly).
#. Connect the power supply for the FPGA.   
#. Turn on the power switch on the FPGA board.
#. Observe kernel and serial console messages on your terminal.

.. seealso::
    For more detailed information on a10soc jumper configuration, check the
    *A10SoC Hardware User Guide* (chapter "Default Switch and Jumper Settings")
    `here <https://www.intel.com/content/www/us/en/content-details/641216/arria-10-soc-development-kit-user-guide.html>`__.

Boot messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is what is printed in the serial console, after you have
connected to the proper ttyUSB or COM port.

Configuring the FPGA will take a few seconds. Once the FPGA has been configured
the green D18 LED will turn on and the boot process will continue.

.. collapsible:: Complete boot log

   .. code-block:: text

      U-Boot SPL 2021.07-16360-gee63370553-dirty (Nov 01 2024 - 18:51:45 +0000)
      FPGA: Checking FPGA configuration setting ...
      FPGA: Start to program peripheral/full bitstream ...
      FPGA: Early Release Succeeded.
      FPGA: Checking FPGA configuration setting ...
      FPGA: Start to program peripheral/full bitstream ...
      FPGA: Early Release Succeeded.

      U-Boot SPL 2021.07-16360-gee63370553-dirty (Nov 01 2024 - 18:51:45 +0000)
      DDRCAL: Success
      FPGA: Checking FPGA configuration setting ...
      FPGA: Start to program core bitstream ...
      Full Configuration Succeeded.
      FPGA: Enter user mode.
      WDT:   Started with servicing (10s timeout)
      Trying to boot from MMC1


      U-Boot 2021.07-16360-gee63370553-dirty (Nov 01 2024 - 18:51:45 +0000)socfpga_arria10, Build: jenkins-hdl_2023_r2-builds-hdl_2023_r2_latest_commit-projects-adrv9001.a10soc-4

      CPU:   Altera SoCFPGA Arria 10
      BOOT:  SD/MMC External Transceiver (1.8V)
      Model: Altera SOCFPGA Arria 10
      DRAM:  1 GiB
      WDT:   Started with servicing (10s timeout)
      MMC:   dwmmc0@ff808000: 0
      Loading Environment from MMC... *** Warning - bad CRC, using default environment

      In:    serial
      Out:   serial
      Err:   serial
      Model: Altera SOCFPGA Arria 10
      Net:
      Warning: ethernet@ff800000 (eth0) using random MAC address - e2:7e:71:eb:7b:d2
      eth0: ethernet@ff800000
      Hit any key to stop autoboot:  0
      Failed to load 'u-boot.scr'
      15042032 bytes read in 853 ms (16.8 MiB/s)
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
      162 bytes read in 8 ms (19.5 KiB/s)
      1:      Linux Default
      Retrieving file: /extlinux/../zImage
      9543072 bytes read in 519 ms (17.5 MiB/s)
      append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      Retrieving file: /extlinux/../socfpga_arria10_socdk_sdmmc.dtb
      31255 bytes read in 11 ms (2.7 MiB/s)
      Kernel image @ 0x1000000 [ 0x000000 - 0x919da0 ]
      ## Flattened Device Tree blob at 02000000
         Booting using the fdt blob at 0x2000000
         Loading Device Tree to 09ff5000, end 09fffa16 ... OK

      Starting kernel ...

      Deasserting all peripheral resets
      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 6.1.70-284114-g2e8908932dfd (jenkins@romlxbuild1) (arm-linux-gnueabi-gcc (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #1063 SMP Tue Mar 18 17:12:50 EET 2025
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
      [    0.000000] percpu: Embedded 15 pages/cpu s30036 r8192 d23212 u61440
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
      [    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] Memory: 879768K/1048576K available (14336K kernel code, 1367K rwdata, 10896K rodata, 1024K init, 498K bss, 37736K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 46749 entries in 138 pages
      [    0.000000] ftrace: allocated 137 pages with 3 groups
      [    0.000000] trace event string verifier disabled
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
      [    0.000000] rcu: srcu_init: Setting srcu_struct sizes based on contention.
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000000] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.007886] Switching to timer-based delay loop, resolution 10ns
      [    0.014228] Console: colour dummy device 80x30
      [    0.018681] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.029167] CPU: Testing write buffer coherency: ok
      [    0.034056] CPU0: Spectre v2: using BPIALL workaround
      [    0.039085] pid_max: default: 32768 minimum: 301
      [    0.043819] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.051107] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.059558] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.065904] cblist_init_generic: Setting adjustable number of callback queues.
      [    0.073120] cblist_init_generic: Setting shift to 1 and lim to 1.
      [    0.079295] Setting up static identity map for 0x100000 - 0x100060
      [    0.085604] rcu: Hierarchical SRCU implementation.
      [    0.090376] rcu:     Max phase no-delay instances is 1000.
      [    0.095928] smp: Bringing up secondary CPUs ...
      [    0.101092] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.101109] CPU1: Spectre v2: using BPIALL workaround
      [    0.111874] smp: Brought up 1 node, 2 CPUs
      [    0.115958] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.122215] CPU: All CPU(s) started in SVC mode.
      [    0.127410] devtmpfs: initialized
      [    0.134938] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.142770] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.152586] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.165000] NET: Registered PF_NETLINK/PF_ROUTE protocol family
      [    0.172692] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.180403] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.188396] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.221613] gpio gpiochip0: (/soc/bridge@ff200000/gpio@60000): not an immutable chip, please consider fixing it!
      [    0.232859] SCSI subsystem initialized
      [    0.236751] usbcore: registered new interface driver usbfs
      [    0.242333] usbcore: registered new interface driver hub
      [    0.247650] usbcore: registered new device driver usb
      [    0.252833] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
      [    0.260568] usb_phy_generic soc:usbphy: dummy supplies not allowed for exclusive requests
      [    0.269050] mc: Linux media interface: v0.10
      [    0.273368] videodev: Linux video capture interface: v2.00
      [    0.278880] pps_core: LinuxPPS API ver. 1 registered
      [    0.283832] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.292935] PTP clock support registered
      [    0.297128] jesd204: found 0 devices and 0 topologies
      [    0.302218] FPGA manager framework
      [    0.305668] Advanced Linux Sound Architecture Driver Initialized.
      [    0.312510] vgaarb: loaded
      [    0.322791] clocksource: Switched to clocksource timer1
      [    0.334098] NET: Registered PF_INET protocol family
      [    0.339162] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
      [    0.348008] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes, linear)
      [    0.356361] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.364089] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.371852] TCP bind hash table entries: 8192 (order: 5, 131072 bytes, linear)
      [    0.379238] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.385688] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.392330] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.399555] NET: Registered PF_UNIX/PF_LOCAL protocol family
      [    0.405786] RPC: Registered named UNIX socket transport module.
      [    0.411687] RPC: Registered udp transport module.
      [    0.416393] RPC: Registered tcp transport module.
      [    0.421074] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.427499] PCI: CLS 0 bytes, default 64
      [    0.432725] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
      [    0.441854] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.452819] NFS: Registering the id_resolver key type
      [    0.457895] Key type id_resolver registered
      [    0.462060] Key type id_legacy registered
      [    0.466724] ntfs: driver 2.1.32 [Flags: R/W].
      [    0.471199] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
      [    0.477655] fuse: init (API version 7.37)
      [    0.482099] bounce: pool size: 64 pages
      [    0.486023] io scheduler mq-deadline registered
      [    0.490535] io scheduler kyber registered
      [    0.501539] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.508854] printk: console [ttyS0] disabled
      [    0.513198] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 35, base_baud = 6250000) is a 16550A
      [    0.522163] printk: console [ttyS0] enabled
      [    0.522163] printk: console [ttyS0] enabled
      [    0.530507] printk: bootconsole [earlycon0] disabled
      [    0.530507] printk: bootconsole [earlycon0] disabled
      [    0.541970] brd: module loaded
      [    0.545516] SPI driver spidev has no spi_device_id for adi,swspi
      [    0.552546] spi_altera ff200040.spi: regoff 0, irq 36
      [    0.560014] CAN device driver interface
      [    0.564188] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
      [    0.570781] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
      [    0.577076] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
      [    0.583764] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
      [    0.590093] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
      [    0.597330] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
      [    0.603590] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
      [    0.609683] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
      [    0.616475] stmmaceth ff800000.ethernet:     DWMAC1000
      [    0.621334] stmmaceth ff800000.ethernet: DMA HW capability register supported
      [    0.628447] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
      [    0.635557] stmmaceth ff800000.ethernet: COE Type 2
      [    0.640414] stmmaceth ff800000.ethernet: TX Checksum insertion supported
      [    0.647090] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
      [    0.653681] stmmaceth ff800000.ethernet: Enabled extended descriptors
      [    0.660093] stmmaceth ff800000.ethernet: Ring mode enabled
      [    0.665559] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
      [    0.673217] stmmaceth ff800000.ethernet: device MAC address 6a:20:54:8c:58:3f
      [    0.689065] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
      [    0.700263] usbcore: registered new interface driver asix
      [    0.705713] usbcore: registered new interface driver ax88179_178a
      [    0.711803] usbcore: registered new interface driver cdc_ether
      [    0.717655] usbcore: registered new interface driver net1080
      [    0.723319] usbcore: registered new interface driver cdc_subset
      [    0.729231] usbcore: registered new interface driver zaurus
      [    0.734842] usbcore: registered new interface driver cdc_ncm
      [    0.740498] usbcore: registered new interface driver r8153_ecm
      [    0.746874] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
      [    0.754122] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
      [    0.761526] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
      [    0.772746] dwc2 ffb00000.usb: DWC OTG Controller
      [    0.777493] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
      [    0.784556] dwc2 ffb00000.usb: irq 39, io mem 0xffb00000
      [    0.789994] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
      [    0.798273] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    0.805538] usb usb1: Product: DWC OTG Controller
      [    0.810238] usb usb1: Manufacturer: Linux 6.1.70-284114-g2e8908932dfd dwc2_hsotg
      [    0.817656] usb usb1: SerialNumber: ffb00000.usb
      [    0.823071] hub 1-0:1.0: USB hub found
      [    0.826917] hub 1-0:1.0: 1 port detected
      [    0.832277] usbcore: registered new interface driver uas
      [    0.837707] usbcore: registered new interface driver usb-storage
      [    0.843789] usbcore: registered new interface driver usbserial_generic
      [    0.850302] usbserial: USB Serial support registered for generic
      [    0.856324] usbcore: registered new interface driver ftdi_sio
      [    0.862056] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    0.869411] usbcore: registered new interface driver upd78f0730
      [    0.875329] usbserial: USB Serial support registered for upd78f0730
      [    0.882560] SPI driver ads7846 has no spi_device_id for ti,tsc2046
      [    0.888734] SPI driver ads7846 has no spi_device_id for ti,ads7843
      [    0.894908] SPI driver ads7846 has no spi_device_id for ti,ads7845
      [    0.901062] SPI driver ads7846 has no spi_device_id for ti,ads7873
      [    0.907350] i2c_dev: i2c /dev entries driver
      [    0.911973] usbcore: registered new interface driver uvcvideo
      [    0.919422] Synopsys Designware Multimedia Card Interface Driver
      [    0.925683] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
      [    0.932347] ledtrig-cpu: registered to indicate activity on CPUs
      [    0.938502] usbcore: registered new interface driver usbhid
      [    0.944068] usbhid: USB HID core driver
      [    0.948082] SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      [    0.959737] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
      [    0.960158] SPI driver adis16475 has no spi_device_id for adi,adis16470
      [    0.965949] dw_mmc ff808000.dwmmc0: Version ID is 270a
      [    0.972521] SPI driver adis16475 has no spi_device_id for adi,adis16475-1
      [    0.977689] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 41,32 bit host data width,1024 deep fifo
      [    0.984400] SPI driver adis16475 has no spi_device_id for adi,adis16475-2
      [    0.993734] mmc_host mmc0: card is polling.
      [    1.000330] SPI driver adis16475 has no spi_device_id for adi,adis16475-3
      [    1.011261] SPI driver adis16475 has no spi_device_id for adi,adis16477-1
      [    1.017164] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
      [    1.018033] SPI driver adis16475 has no spi_device_id for adi,adis16477-2
      [    1.034217] SPI driver adis16475 has no spi_device_id for adi,adis16477-3
      [    1.040974] SPI driver adis16475 has no spi_device_id for adi,adis16465-1
      [    1.047753] SPI driver adis16475 has no spi_device_id for adi,adis16465-2
      [    1.054524] SPI driver adis16475 has no spi_device_id for adi,adis16465-3
      [    1.061285] SPI driver adis16475 has no spi_device_id for adi,adis16467-1
      [    1.068053] SPI driver adis16475 has no spi_device_id for adi,adis16467-2
      [    1.074825] SPI driver adis16475 has no spi_device_id for adi,adis16467-3
      [    1.081587] SPI driver adis16475 has no spi_device_id for adi,adis16500
      [    1.088182] SPI driver adis16475 has no spi_device_id for adi,adis16501
      [    1.094776] SPI driver adis16475 has no spi_device_id for adi,adis16505-1
      [    1.101538] SPI driver adis16475 has no spi_device_id for adi,adis16505-2
      [    1.108306] SPI driver adis16475 has no spi_device_id for adi,adis16505-3
      [    1.115075] SPI driver adis16475 has no spi_device_id for adi,adis16507-1
      [    1.121837] SPI driver adis16475 has no spi_device_id for adi,adis16507-2
      [    1.128613] SPI driver adis16475 has no spi_device_id for adi,adis16507-3
      [    1.135387] SPI driver adis16475 has no spi_device_id for adi,adis16575-2
      [    1.142144] SPI driver adis16475 has no spi_device_id for adi,adis16575-3
      [    1.148912] SPI driver adis16475 has no spi_device_id for adi,adis16576-2
      [    1.155680] SPI driver adis16475 has no spi_device_id for adi,adis16576-3
      [    1.162436] SPI driver adis16475 has no spi_device_id for adi,adis16577-2
      [    1.169203] SPI driver adis16475 has no spi_device_id for adi,adis16577-3
      [    1.177185] axi_sysid ff218000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    1.185201] axi_sysid ff218000.axi-sysid-0: [adrv9001] on [a10soc] git branch <hdl_2023_r2> git <2156ac7e874a1dc321d9f64a325009fafe563419> clean [2024-11-01 18:27:53] UTC
      [    1.201043] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
      [    1.208348] usbcore: registered new interface driver snd-usb-audio
      [    1.216485] NET: Registered PF_INET6 protocol family
      [    1.222438] Segment Routing with IPv6
      [    1.226197] In-situ OAM (IOAM) with IPv6
      [    1.230127] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
      [    1.230186] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.246196] mmc0: new high speed SDHC card at address aaaa
      [    1.246347] NET: Registered PF_PACKET protocol family
      [    1.252265] mmcblk0: mmc0:aaaa SK32G 29.7 GiB
      [    1.256789] NET: Registered PF_KEY protocol family
      [    1.266341] can: controller area network core
      [    1.270809] NET: Registered PF_CAN protocol family
      [    1.275623] can: raw protocol
      [    1.278588] can: broadcast manager protocol
      [    1.282760] can: netlink gateway - max_hops=1
      [    1.287173] 8021q: 802.1Q VLAN Support v1.8
      [    1.291372] NET: Registered PF_IEEE802154 protocol family
      [    1.296811] Key type dns_resolver registered
      [    1.301150] ThumbEE CPU extension supported.
      [    1.305422] Registering SWP/SWPB emulation handler
      [    1.310566]  mmcblk0: p1 p2 p3
      [    1.320512] at24 0-0051: supply vcc not found, using dummy regulator
      [    1.328134] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
      [    1.337441] rtc-ds1307 0-0068: SET TIME!
      [    1.345652] rtc-ds1307 0-0068: registered as rtc0
      [    1.352167] ltc2978: probe of 0-005c failed with error -121
      [    1.362213] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
      [    1.368932] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
      [    1.377658] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
      [    1.462850] random: crng init done
      [    6.692294] adrv9002 spi0.0: Interface tuning failed: -5
      [    6.698863] cf_axi_adc: probe of ff220000.axi-adrv9002-rx-lpc failed with error -5
      [    6.709102] of_cfs_init
      [    6.711579] of_cfs_init: OK
      [    6.714627] ALSA device list:
      [    6.717587]   No soundcards found.
      [    6.721182] dw-apb-uart ffc02100.serial1: forbid DMA for kernel console
      [    7.015809] EXT4-fs (mmcblk0p2): recovery complete
      [    7.022330] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Quota mode: disabled.
      [    7.031238] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    7.044847] devtmpfs: mounted
      [    7.051811] Freeing unused kernel image (initmem) memory: 1024K
      [    7.058257] Run /sbin/init as init process
      [    7.608351] systemd[1]: System time before build time, advancing clock.
      [    7.676486] systemd[1]: systemd 247.3-7+rpi1+deb11u6 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [    7.700362] systemd[1]: Detected architecture arm.

      Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

      [    7.743752] systemd[1]: Set hostname to <analog>.
      [    9.366669] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [    9.602242] systemd[1]: Queued start job for default target Graphical Interface.
      [    9.611550] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    9.623985] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [    9.633679] systemd[1]: Created slice system-getty.slice.
      [  OK  ] Created slice system-getty.slice.
      [    9.673733] systemd[1]: Created slice system-modprobe.slice.
      [  OK  ] Created slice system-modprobe.slice.
      [    9.713666] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [  OK  ] Created slice system-serial\x2dgetty.slice.
      [    9.753634] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [  OK  ] Created slice system-systemd\x2dfsck.slice.
      [    9.793415] systemd[1]: Created slice User and Session Slice.
      [  OK  ] Created slice User and Session Slice.
      [    9.833325] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
      [    9.873226] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [    9.885623] systemd[1]: Reached target Slices.
      [  OK  ] Reached target Slices.
      [    9.923064] systemd[1]: Reached target Swap.
      [  OK  ] Reached target Swap.
      [    9.962594] systemd[1]: Listening on Syslog Socket.
      [  OK  ] Listening on Syslog Socket.
      [   10.003472] systemd[1]: Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [   10.043210] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [   10.105286] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
      [   10.114133] systemd[1]: Listening on Journal Socket (/dev/log).
      [  OK  ] Listening on Journal Socket (/dev/log).
      [   10.143640] systemd[1]: Listening on Journal Socket.
      [  OK  ] Listening on Journal Socket.
      [   10.180698] systemd[1]: Listening on udev Control Socket.
      [  OK  ] Listening on udev Control Socket.
      [   10.213479] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [   10.243588] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
      [   10.252141] systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
      [   10.313346] systemd[1]: Mounting RPC Pipe File System...
               Mounting RPC Pipe File System...
      [   10.356097] systemd[1]: Mounting Kernel Debug File System...
               Mounting Kernel Debug File System...
      [   10.396010] systemd[1]: Mounting Kernel Trace File System...
               Mounting Kernel Trace File System...
      [   10.423259] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [   10.437686] systemd[1]: Starting Restore / save the current clock...
               Starting Restore / save the current clock...
      [   10.476881] systemd[1]: Starting Set the console keyboard layout...
               Starting Set the console keyboard layout...
      [   10.513242] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [   10.583617] systemd[1]: Starting Load Kernel Module configfs...
               Starting Load Kernel Module configfs...
      [   10.617036] systemd[1]: Starting Load Kernel Module drm...
               Starting Load Kernel Module drm...
      [   10.676309] systemd[1]: Starting Load Kernel Module fuse...
               Starting Load Kernel Module fuse...
      [   10.706087] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [   10.715497] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [   10.728048] systemd[1]: Starting Journal Service...
               Starting Journal Service...
      [   10.768696] systemd[1]: Starting Load Kernel Modules...
               Starting Load Kernel Modules...
      [   10.806203] systemd[1]: Starting Remount Root and Kernel File Systems...
               Starting Remount Root and Kernel File Systems...
      [   10.876917] systemd[1]: Starting Coldplug All udev Devices...
               Starting Coldplug All udev Devices...
      [   10.929851] systemd[1]: Mounted RPC Pipe File System.
      [  OK  ] Mounted RPC Pipe File System.
      [   10.973629] systemd[1]: Started Journal Service.
      [  OK  ] Started Journal Service.
      [  OK  ] Mounted Kernel Debug File System.
      [  OK  ] Mounted Kernel Trace File System.
      [  OK  ] Finished Restore / save the current clock.
      [  OK  ] Finished Set the console keyboard layout.
      [   11.079190] EXT4-fs (mmcblk0p2): re-mounted. Quota mode: disabled.
      [  OK  ] Finished Load Kernel Module configfs.
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
      [   11.490834] systemd-journald[103]: Received client request to flush runtime journal.
               Starting Create System Users...
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Configuration File System.
      [  OK  ] Finished Coldplug All udev Devices.
      [  OK  ] Finished Load/Save Random Seed.
      [  OK  ] Finished Apply Kernel Variables.
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
      [  OK  ] Found device /dev/ttyS0.
      [  OK  ] Found device /dev/disk/by-partuuid/a22286d2-01.
      [  OK  ] Reached target Hardware activated USB gadget.
               Starting File System Check…isk/by-partuuid/a22286d2-01...
               Starting Load Kernel Modules...
      [  OK  ] Started File System Check Daemon to report status.
      [FAILED] Failed to start Load Kernel Modules.
      See 'systemctl status systemd-modules-load.service' for details.
      [  OK  ] Finished Wait for udev To Complete Device Initialization.
      [  OK  ] Finished File System Check…/disk/by-partuuid/a22286d2-01.
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
               Starting Network Time Synchronization...
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Finished Update UTMP about System Boot/Shutdown.
               Starting Load Kernel Modules...
      [  OK  ] Finished Raise network interfaces.
      [  OK  ] Started Network Time Synchronization.
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
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started LSB: rng-tools (Debian variant).
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
      [  OK  ] Started Internet superserver.
      [  OK  ] Finished Load USB gadget scheme.
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Found device /dev/ttyGS0.
      [  OK  ] Started Authorization Manager.
               Mounting Mount FunctionFS instance...
               Starting Modem Manager...
      [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
      [  OK  ] Finished Permit User Sessions.
      [  OK  ] Mounted Mount FunctionFS instance.
               Starting Light Display Manager...
               Starting Hold until boot process finishes up...
      [  OK  ] Finished Analog Devices power up/down sequence.
      [  OK  ] Started Disk Manager.
               Starting Manage, Install and Generate Color Profiles...
      [FAILED] Failed to start VNC Server for X11.

      Raspbian GNU/Linux 11 analog ttyS0

      analog login: root (automatic login)

      Linux analog 6.1.70-284114-g2e8908932dfd #1063 SMP Tue Mar 18 17:12:50 EET 2025 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Tue Mar 18 19:11:15 GMT 2025 on ttyS0

Useful commands for the serial terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below commands are to be run in the serial terminal connected to the FPGA.

To find out the IP of the FPGA board, run the following command and take the
IP specified at "eth0 inet":

.. shell::

   $ifconfig

If the A10Soc is connected to a network with a DHCP server, the IP address
assigned to the board appears on the LCD.
To manually assign an IP address, run `ifconfig eth0 IP_ADDR`.

To see the IIO devices detected, run:

.. shell::

   $iio_info | grep iio:device

To power off the system, run the following command, and wait for the final
message to be printed, then power off the FPGA board from the switch as well.

.. shell::

   $poweroff

To reboot the system, run:

.. shell::

   $reboot

.. important::

   Even though this is Linux, this is a persistent file system. Care should
   be taken not to corrupt the file system -- please shut down properly, don't
   just turn off the power switch. Depending on your monitor, the standard
   power off could be hiding. You can do this from the terminal as well with
   :code:`sudo shutdown -h now` or the above-mentioned command for powering off.
