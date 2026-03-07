Loading file from USB storage in u-boot
=======================================

Overview
--------

This document talks about how we can load files on USB memory stick, into system RAM from u-boot. Here we take ADSP-SC573 board as example.

Hardware Setup
--------------

-  An ADSP-SC5xx EZ-Board:

   -  ADSP-SC589 Ezkit v1.1 and above, or,

      -  ADSP-SC584 Ezkit v1.0 and above, or,

         -  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

-  A USB memory stick
-  A USB adapter cable (provided in the ezkit box)

Connect USB stick to the USB OTG port, via the USB adapter cable, as following, and reset the board 

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/das-u-boot/dasu-loading_file-hw_setup.jpg
   :width: 600px

Test method
-----------

Formatting the USB stick
~~~~~~~~~~~~~~~~~~~~~~~~

Insert the USB memory stick into a Linux PC, you will see new items show up in /dev/sd\*, as following:

::

   $ ls /dev/sd*
   /dev/sda  /dev/sda1  /dev/sda2  /dev/sda5  /dev/sdb  /dev/sdb1

In this case the /dev/sdb is for the USB stick we just plugged in.

.. important::

   **Caution** : Please double check the device node newly created for your memory stick, otherwise serious damage like system permanent crash down happens!


The format a vfat partiton on it:

::

   $ sudo mkfs.vfat /dev/sdb1
   [sudo] password for ...
   mkfs.vfat 3.0.12 (29 Oct 2011)

Copy files in it
~~~~~~~~~~~~~~~~

::

   $ sudo mount /dev/sdb1 /mnt
   $ sudo cp build/tmp/deploy/images/<MACHINE>/<RAMDISK_FILE> /mnt/boot/ramdisk.cpio.xz.u-boot
   $ sudo cp build/tmp/deploy/images/<MACHINE>/<DTB_FILE> /mnt/boot/
   $ sudo cp build/tmp/deploy/images/<MACHINE>/zImage /mnt/boot/
   $ sudo umount /mnt

Then plug the USB stick to the USB OTG port in board, via the USB adapter cable, and reset the board 

Start the USB
~~~~~~~~~~~~~

Run "start usb" In the u-boot console:

::

   sc # usb start
   (Re)start USB...
   USB0:   scanning bus 0 for devices... 1 USB Device(s) found
          scanning usb for storage devices... 1 Storage Device(s) found

 

Run "fatls usb 0:1" In the u-boot console:

::

   sc # fatls usb 0:1
     4231792   zImage
       21512   sc589-ezkit.dtb
    12225998   ramdisk.cpio.xz.u-boot
   3 file(s), 0 dir(s)

This shows the FAT files information in USB device 0 partition 1, with files we copied.

Load file into RAM
~~~~~~~~~~~~~~~~~~

 As example we load both the dtb, zImage and the ramdisk file into proper location.

.. important::

   Don't forget to change the file/dtb name and load address according to your board type (i.e. SC589-ezkit or SC584-ezkit or SC573-ezkit), otherwise it may not boot properly.


::

   sc # fatload usb 0:1 ${dtbaddr} ${dtbfile}
   reading sc589-ezkit.dtb
   19120 bytes read in 30 ms (335 KiB/s)
   sc # fatload usb 0:1 ${loadaddr} ${ramfile}
   reading zImage
   4106096 bytes read in 2610 ms (1.5 MiB/s)
   sc # fatload usb 0:1 ${initramaddr} ${initramfile}
   reading ramdisk.cpio.xz.u-boot
   12225833 bytes read in 7772 ms (1.5 MiB/s)

 Verify the read operation:

::


   sc # bootz ${loadaddr} ${initramaddr} ${dtbaddr}
   Kernel image @ 0xc2000000 [ 0x000000 - 0x3ea770 ]
   ## Loading init Ramdisk from Legacy Image at c5000000 ...
      Image Name:   Analog Devices Ram Disk Image
      Image Type:   ARM Linux RAMDisk Image (gzip compressed)
      Data Size:    12225769 Bytes = 11.7 MiB
      Load Address: 00000000
      Entry Point:  00000000
      Verifying Checksum ... OK
   ## Flattened Device Tree blob at c4000000
      Booting using the fdt blob at 0xc4000000
      Loading Ramdisk to cf2b7000, end cfe5fce9 ... OK
      Loading Device Tree to cf2af000, end cf2b6aaf ... OK

   Starting kernel ...

   Uncompressing Linux... done, booting the kernel.
   Booting Linux on physical CPU 0x0
   Linux version 4.19.0-yocto-standard (oe-user@oe-host) (gcc version 8.2.0 (GCC)) #1 Fri Jul 31 10:34:04 UTC 2020
   CPU: ARMv7 Processor [410fc051] revision 1 (ARMv7), cr=10c53c7d
   CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   OF: fdt: Machine model: ADI sc589-mini
   bootconsole [earlycon0] enabled
   Memory policy: Data cache writeback
   Hit pending asynchronous external abort (FSR=0x00001c06) during first unmask, this is most likely caused by a firmware/bootloader bug.
   CPU: All CPU(s) started in SVC mode.
   dump init clock rate
   CGU0_PLL 450 MHz
   CGU0_SYSCLK 225 MHz
   CGU0_CCLK 450 MHz
   CGU0_SYS0 112 MHz
   CGU0_DCLK 450 MHz
   CGU0_OCLK 150 MHz
   CGU0_SYS0 112 MHz
   random: get_random_bytes called from start_kernel+0x98/0x3dc with crng_init=0
   Built 1 zonelists, mobility grouping on.  Total pages: 56896
   Kernel command line: root=/dev/mtdblock2 rw rootfstype=jffs2 clkin_hz=(25000000) earlyprintk=serial,uart0,57600 console=ttySC0,57600 mem=224M ip=10.99.24.96:10.99.24.65:10.99.24.1:255.255.255.0:sc58x:ethf
   Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
   Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
   Memory: 205764K/229376K available (6144K kernel code, 200K rwdata, 1512K rodata, 1024K init, 112K bss, 23612K reserved, 0K cma-reserved)
   Virtual kernel memory layout:
       vector  : 0xffff0000 - 0xffff1000   (   4 kB)
       fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
       vmalloc : 0xce800000 - 0xff800000   ( 784 MB)
       lowmem  : 0xc0000000 - 0xce000000   ( 224 MB)
       modules : 0xbf000000 - 0xc0000000   (  16 MB)
         .text : 0x(ptrval) - 0x(ptrval)   (7136 kB)
         .init : 0x(ptrval) - 0x(ptrval)   (1024 kB)
         .data : 0x(ptrval) - 0x(ptrval)   ( 201 kB)
          .bss : 0x(ptrval) - 0x(ptrval)   ( 113 kB)
   NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
   clocksource: cs_gptimer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 16988981748 ns
   sched_clock: 32 bits at 112MHz, resolution 8ns, wraps every 19088743419ns
   Console: colour dummy device 80x30
   Calibrating delay loop... 297.98 BogoMIPS (lpj=595968)
   pid_max: default: 32768 minimum: 301
   Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
   Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
   CPU: Testing write buffer coherency: ok
   Setting up static identity map for 0xc2100000 - 0xc210003c
   devtmpfs: initialized
   VFP support v0.3: implementor 41 architecture 2 part 30 variant 5 rev 1
   clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
   futex hash table entries: 256 (order: -1, 3072 bytes)
   pinctrl core: initialized pinctrl subsystem
   NET: Registered protocol family 16
   DMA: preallocated 256 KiB pool for atomic coherent allocations
   L2C: device tree omits to specify unified cache
   L2C-310 dynamic clock gating enabled, standby mode enabled
   L2C-310 cache controller enabled, 8 ways, 256 kB
   L2C-310: CACHE_ID 0x410000c9, AUX_CTRL 0x06040000
   sc58x_init: registering device resources
   sec init...
   enabled
   hw-breakpoint: Failed to enable monitor mode on CPU 0.
   ADI DMA2 Controller
   SCSI subsystem initialized
   usbcore: registered new interface driver usbfs
   usbcore: registered new interface driver hub
   usbcore: registered new device driver usb
   i2c-adi-twi 31001400.twi: ADI on-chip I2C TWI Controller, regs_base@(ptrval)
   i2c-adi-twi 31001500.twi: ADI on-chip I2C TWI Controller, regs_base@(ptrval)
   i2c-adi-twi 31001600.twi: ADI on-chip I2C TWI Controller, regs_base@(ptrval)
   pps_core: LinuxPPS API ver. 1 registered
   pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
   PTP clock support registered
   Advanced Linux Sound Architecture Driver Initialized.
   clocksource: Switched to clocksource cs_gptimer
   NET: Registered protocol family 2
   tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes)
   TCP established hash table entries: 2048 (order: 1, 8192 bytes)
   TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
   TCP: Hash tables configured (established 2048 bind 2048)
   UDP hash table entries: 256 (order: 0, 4096 bytes)
   UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
   NET: Registered protocol family 1
   RPC: Registered named UNIX socket transport module.
   RPC: Registered udp transport module.
   RPC: Registered tcp transport module.
   RPC: Registered tcp NFSv4.1 backchannel transport module.
   Unpacking initramfs...
   random: fast init done
   Freeing initrd memory: 11940K
   hw perfevents: enabled with armv7_cortex_a5 PMU driver, 3 counters available
   Initialise system trusted keyrings
   workingset: timestamp_bits=30 max_order=16 bucket_order=0
   NFS: Registering the id_resolver key type
   Key type id_resolver registered
   Key type id_legacy registered
   nfs4filelayout_init: NFSv4 File Layout Driver Registering...
   jffs2: version 2.2. (NAND) �© 2001-2006 Red Hat, Inc.
   Key type asymmetric registered
   Asymmetric key parser 'x509' registered
   io scheduler noop registered (default)
   io scheduler mq-deadline registered
   io scheduler kyber registered
   ADI serial driver
   adi-uart4.0: ttySC0 at MMIO 0x31003000 (irq = 20, base_baud = 7031250) is a ADI-UART4
   console [ttySC0] enabled
   console [ttySC0] enabled
   bootconsole [earlycon0] disabled
   bootconsole [earlycon0] disabled
   loop: module loaded
   adi-spi3 31042000.spi: registered ADI SPI controller spi0
   m25p80 spi2.38: unrecognized JEDEC id bytes: 9d, 60, 1a
   m25p80: probe of spi2.38 failed with error -2
   adi-spi3 31044000.spi: registered ADI SPI controller spi2
   libphy: Fixed MDIO Bus: probed
   adi-dwmac 3100c000.ethernet: PTP uses main clock
   adi-dwmac 3100c000.ethernet: no reset control found
   adi-dwmac 3100c000.ethernet: User ID: 0x10, Synopsys ID: 0x37
   adi-dwmac 3100c000.ethernet:    DWMAC1000
   adi-dwmac 3100c000.ethernet: DMA HW capability register supported
   adi-dwmac 3100c000.ethernet: RX Checksum Offload Engine supported
   adi-dwmac 3100c000.ethernet: COE Type 2
   adi-dwmac 3100c000.ethernet: TX Checksum insertion supported
   adi-dwmac 3100c000.ethernet: Wake-Up On Lan supported
   adi-dwmac 3100c000.ethernet: Enhanced/Alternate descriptors
   adi-dwmac 3100c000.ethernet: Enabled extended descriptors
   adi-dwmac 3100c000.ethernet: Ring mode enabled
   adi-dwmac 3100c000.ethernet: Enable RX Mitigation via HW Watchdog Timer
   libphy: stmmac: probed
   usbcore: registered new interface driver usb-storage
   musb-hdrc musb-hdrc.1.auto: MUSB HDRC host driver
   musb-hdrc musb-hdrc.1.auto: new USB bus registered, assigned bus number 1
   hub 1-0:1.0: USB hub found
   hub 1-0:1.0: 1 port detected
   musb-hdrc musb-hdrc.3.auto: MUSB HDRC host driver
   musb-hdrc musb-hdrc.3.auto: new USB bus registered, assigned bus number 2
   hub 2-0:1.0: USB hub found
   hub 2-0:1.0: 1 port detected
   i2c /dev entries driver
   adi_wdt: initialized: timeout=20 sec (nowayout=0)
   Synopsys Designware Multimedia Card Interface Driver
   dwmmc_adi 31010000.mmc: IDMAC supports 32-bit address mode.
   dwmmc_adi 31010000.mmc: Using internal DMA controller.
   dwmmc_adi 31010000.mmc: Version ID is 270a
   dwmmc_adi 31010000.mmc: DW MMC controller at irq 38,32 bit host data width,1024 deep fifo
   mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
   ADI hardware CRC crypto driver
   adi-hmac-crc 31001200.crc: initialized
   adi-hmac-crc 31001300.crc: initialized
   usbcore: registered new interface driver usbhid
   usbhid: USB HID core driver
   adau1761 0-0038: Direct firmware load for adau1761.bin failed with error -2
   adau1761 0-0038: Could not find firmware file: -2
   sc5xx-i2s-dai 31002000.i2s: SPORT create success
   snd-sc5xx scb:sound: adau-hifi <-> 31002000.i2s mapping ok
   NET: Registered protocol family 10
   Segment Routing with IPv6
   sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   NET: Registered protocol family 17
   Key type dns_resolver registered
   ThumbEE CPU extension supported.
   Loading compiled-in X.509 certificates
   console [netcon0] enabled
   netconsole: network logging started
   TI DP83867 stmmac-0:00: attached PHY driver [TI DP83867] (mii_bus:phy_addr=stmmac-0:00, irq=POLL)
   adi-dwmac 3100c000.ethernet eth0: No Safety Features support found
   adi-dwmac 3100c000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
   adi-dwmac 3100c000.ethernet eth0: registered PTP clock
   IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
   adi-dwmac 3100c000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
   IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
   IP-Config: Complete:
        device=eth0, hwaddr=02:80:ad:20:31:e2, ipaddr=10.99.24.96, mask=255.255.255.0, gw=10.99.24.1
        host=sc58x, domain=, nis-domain=(none)
        bootserver=10.99.24.65, rootserver=10.99.24.65, rootpath=
   cfg80211: Loading compiled-in X.509 certificates for regulatory database
   cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
   ALSA device list:
     #0: sc5xx-asoc-card
   platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
   cfg80211: failed to load regulatory.db
   Freeing unused kernel memory: 1024K
   Run /init as init process
   init started: BusyBox v1.29.3 (2020-08-07 10:16:01 UTC)
   starting pid 665, tty '': '/bin/mount -t proc proc /proc'
   starting pid 666, tty '': '/bin/mount -t sysfs sysfs /sys'
   starting pid 667, tty '': '/bin/mount -t devtmpfs devtmpfs /dev'
   starting pid 668, tty '': '/bin/mount -o remount,rw /'
   starting pid 669, tty '': '/bin/mkdir -p /dev/pts'
   starting pid 670, tty '': '/bin/mount -t devpts devpts /dev/pts'
   starting pid 671, tty '': '/bin/mount -a'
   mount: mounting /dev/root on / failed: No such file or directory
   starting pid 675, tty '': '/usr/bin/fastboot-listener'
   Failed to open SHARC notify device: No such file or directory
   starting pid 678, tty '/dev/ttySC0': '/bin/sh'

More information
----------------

There are more command available for USB in u-boot:

::

   sc # usb info
   1: Mass Storage,  USB Revision 2.0
    - Generic  USB Storage 000000009451
    - Class: (from Interface) Mass Storage
    - PacketSize: 64  Configurations: 1
    - Vendor: 0x05e3  Product 0x0723 Version 148.81
      Configuration: 1
      - Interfaces: 1 Bus Powered 500mA
        Interface: 0
        - Alternate Setting 0, Endpoints: 2
        - Class Mass Storage, Transp. SCSI, Bulk only
        - Endpoint 1 In Bulk MaxPacket 512
        - Endpoint 2 Out Bulk MaxPacket 512

::

   sc # usb storage
     Device 0: Vendor: Generic  Rev: 9451 Prod: STORAGE DEVICE
               Type: Removable Hard Disk
               Capacity: 1897.0 MB = 1.8 GB (3885056 x 512)

::

   sc # usb tree
   USB device tree:
     1  Mass Storage (12 Mb/s, 500mA)
        Generic  USB Storage 000000009451

::

   sc # fatinfo usb 0:1
   Interface:  USB
     Device 0: Vendor: Generic  Rev: 9451 Prod: STORAGE DEVICE
               Type: Removable Hard Disk
               Capacity: 1897.0 MB = 1.8 GB (3885056 x 512)
   Filesystem: FAT32 "           "

 

Appendix: Macro Definition
==========================

+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| ``MACHINE``      | ``DTB_FILE``    | ``FULL_FS_IMAGE``                       | ``MINIMAL_FS_IMAGE``                       | '' RAMDISK_FILE''                                  |
+==================+=================+=========================================+============================================+====================================================+
| adsp-sc589-mini  | sc589-mini.dtb  | adsp-sc5xx-full-adsp-sc589-mini.tar.xz  | adsp-sc5xx-minimal-adsp-sc589-mini.tar.xz  | adsp-sc5xx-ramdisk-adsp-sc589-mini.cpio.xz.u-boot  |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| adsp-sc589-ezkit | sc589-ezkit.dtb | adsp-sc5xx-full-adsp-sc589-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc589-ezkit.tar.xz | adsp-sc5xx-ramdisk-adsp-sc589-ezkit.cpio.xz.u-boot |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| adsp-sc584-ezkit | sc584-ezkit.dtb | adsp-sc5xx-full-adsp-sc584-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc584-ezkit.tar.xz | adsp-sc5xx-ramdisk-adsp-sc584-ezkit.cpio.xz.u-boot |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+
| adsp-sc573-ezkit | sc573-ezkit.dtb | adsp-sc5xx-full-adsp-sc573-ezkit.tar.xz | adsp-sc5xx-minimal-adsp-sc573-ezkit.tar.xz | adsp-sc5xx-ramdisk-adsp-sc573-ezkit.cpio.xz.u-boot |
+------------------+-----------------+-----------------------------------------+--------------------------------------------+----------------------------------------------------+

|  
| ----

.. container:: group

   
   .. container:: half column

      \**Pre: :doc:`Ethernet Driver in U-Boot on SC5xx-EZKIT </wiki-migration/resources/tools-software/linuxdsp/docs/das-u-boot/ethernet_driver_in_uboot>`\ **

   
   .. container:: half column

      **\ Next: \*\*\ :doc:`Mobile Storage Interface (MSI) </wiki-migration/resources/tools-software/linuxdsp/docs/das-u-boot/mobile_storage_interface>`

   


 

 
