AD-FMCOMMS1-EBZ ML605 Quick Start Guide
=======================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


.. important::

   Building Linux on ML605 Virtex6 board remains on this website only for legacy purposes. The Linux support for this carrier has been discontinued.


This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS1-EBZ on either:

-  `ML605 <https://www.xilinx.com/ML605>`_

Required Software
-----------------

-  ml605_restoring_CF_flash_contents_AD-FMCOMMS1-EBZ.zip (CF Card filesystem contents)
-  mkdosfs – utility used to format the CF Card with an appropriate FAT16 filesystem.

Downloads
---------

-  `ml605_restoring_cf_flash_contents_ad-fmcomms1-ebz.zip OUTDATED <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/quickstart/ml605_restoring_cf_flash_contents_ad-fmcomms1-ebz.zip>`_
-  `mkdosfs (Linux mkdosfs for Windows NT/2K/XP) <http://www1.mager.org/mkdosfs/>`_
-  `ad-fmcomms1-ebz_ml605.zip MARCH 5th 2014 <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/ad-fmcomms1-ebz_ml605_05052014.zip>`_

Required Hardware
-----------------

-  Xilinx ML605
-  1GB or 2GB CompactFlash card (Sandisk Ulra II or similar)
-  AD-FMCOMMS1-EBZ FMC Board.

Software Installs
-----------------

-  Format and populate CF Card

   -  In order to use a CF card with the Xilinx SystemACE it must be formatted with a FAT12 or FAT16 filesystem. You cannot format the Card using Windows XP or later. Please use the mkdosfs utlity.
   -  Format instructions:

      -  Put your empty CF card into a CF reader.
      -  You will need to BACKUP ALL YOUR DATA ON THE CF CARD
      -  Click Start -> Run
      -  Enter cmd and click Run
      -  cd to the directory where you extracted mkdosfs.exe
      -  **MAKE SURE YOU HAVE SAVED ANY DATA FROM THE CF CARD!**
      -  You will need to know the drive letter of your CF reader
      -  Type mkdosfs –s 64 –F 16 –R 1 f:
      -  Notice that f: should be replaced by the drive letter of your CF reader followed by a colon.

   -  Now unzip ml605_restoring_CF_flash_contents_AD-FMCOMMS1-EBZ.zip onto your freshly formatted CF Card.

Hardware Setup
~~~~~~~~~~~~~~

-  Connect the ML605 power and Ethernet cables.
-  Set SACE MODE switches (S1) (18c) to

   -  SYSACE MODE: ON
   -  CFGAddr2: OFF
   -  CFGAddr1: ON
   -  CFGAddr0: OFF

Testing
=======

Testing the AD-FMComms1-EBZ board uses the ML605 board from Xilinx. You should be familiar with a few of the connectors as switches on the board:


|ML605 Diagram|

-  Connect the AD-FMCOMMS1-EBZ FMC board to the ML605, on the LPC FMC connector (20).
-  Turn on the power switch on the ML605 board (18A)

   -  Wait ~11 seconds. The DS1 System ACE Status LED should be blinking. This indicates that the ACE file in the CF card is being loaded.

      -  Wait ~10 seconds more. The blue light on the AD-FMComms1-EBZ should start blinking, indicating that the card is being initialized.
      -  Wait ~10 seconds more. The LCD should display the IP number of the board, and the line "XCOMM LPC", this indicates that the Linux kernel booted on the Microblaze is properly configured, and found all the devices on the card.
      -  In total, this step should take ~30 seconds.

-  Observe LCD Display (17f).


|LCD image|

   -  Line 1: Target IP Address
   -  Line2: XCOMM LPC if device is present

-  Open up your favourite Web Browser and enter the XCOMM target IP address into the URL/Address bar.\ |image1|\


|image2|

-  If you are interested in the Linux console messages and command line interface, connect a USB cable to the ML605 port USB UART (12). Terminal settings are 57600,8N1. You should see the kernel startup messages as follows. (password is **root**)

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      Ramdisk addr 0x00000000, 
      Compiled-in FDT at c029f4d8
      Linux version 3.13.0-68971-g879e3f3 (michael@mhenneri-D04) (gcc version 4.6.4 20120924 (prerelease) (crosstool-NG 1.15.3) ) #1210 Wed Mar 54
      setup_cpuinfo: initialising
      setup_cpuinfo: Using full CPU PVR support
      wt_msr_noirq
      setup_memory: max_mapnr: 0x20000
      setup_memory: min_low_pfn: 0xc0000
      setup_memory: max_low_pfn: 0xe0000
      setup_memory: max_pfn: 0xe0000
      Zone ranges:
        DMA      [mem 0xc0000000-0xdfffffff]
        Normal   empty
      Movable zone start for each node
      Early memory node ranges
        node   0: [mem 0xc0000000-0xdfffffff]
      On node 0 totalpages: 131072
      free_area_init_node: node 0, pgdat c035d0b0, node_mem_map c0800000
        DMA zone: 1024 pages used for memmap
        DMA zone: 0 pages reserved
        DMA zone: 131072 pages, LIFO batch:31
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
      pcpu-alloc: [0] 0 
      Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 130048
      Kernel command line: console=ttyUL0,57600 root=/dev/ram
      PID hash table entries: 2048 (order: 1, 8192 bytes)
      Dentry cache hash table entries: 65536 (order: 6, 262144 bytes)
      Inode-cache hash table entries: 32768 (order: 5, 131072 bytes)
      Memory: 512700K/524288K available (2685K kernel code, 118K rwdata, 600K rodata, 2968K init, 84K bss, 11588K reserved)
      Kernel virtual memory layout:
        * 0xffffe000..0xfffff000  : fixmap
        * 0xffffe000..0xffffe000  : early ioremap
        * 0xf0000000..0xffffe000  : vmalloc & ioremap
      NR_IRQS:33
      /axi@0/interrupt-controller@41200000: num_irq=12, edge=0xc00
      ERROR: CPU CCF input clock not found
      /axi@0/timer@41c00000: irq=9
      ERROR: timer CCF input clock not found
      xilinx_timer_set_mode: shutdown
      xilinx_timer_set_mode: periodic
      sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 42949672950ns
      Calibrating delay loop... 49.08 BogoMIPS (lpj=98176)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 512
      NET: Registered protocol family 16
      Switched to clocksource xilinx_clocksource
      xilinx_timer_set_mode: oneshot
      NET: Registered protocol family 2
      TCP established hash table entries: 4096 (order: 2, 16384 bytes)
      TCP bind hash table entries: 4096 (order: 2, 16384 bytes)
      TCP: Hash tables configured (established 4096 bind 4096)
      TCP: reno registered
      UDP hash table entries: 256 (order: 0, 4096 bytes)
      UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
      NET: Registered protocol family 1
      RPC: Registered named UNIX socket transport module.
      RPC: Registered udp transport module.
      RPC: Registered tcp transport module.
      RPC: Registered tcp NFSv4.1 backchannel transport module.
      GPIO IRQ not connected
      XGpio: /axi@0/gpio@40040000: registered, base is 243
      GPIO IRQ not connected
      XGpio: /axi@0/gpio@40040000: dual channel registered, base is 230
      Skipping unavailable RESET gpio -2 (reset)
      jffs2: version 2.2. (NAND) (SUMMARY)  ?© 2001-2006 Red Hat, Inc.
      msgmni has been set to 1001
      Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 11, base_baud = 0) is a uartlite
      console [ttyUL0] enabled
      xilinx_lcd 40000000.gpio: Device Tree Probing 'gpio'
      xilinx_lcd 40000000.gpio: LCD 0x40000000 mapped to 0xf0160000
      xilinx_emaclite 40e00000.ethernet: Device Tree Probing
      libphy: Xilinx Emaclite MDIO: probed
      xilinx_emaclite 40e00000.ethernet: MAC address is now 00:0a:35:ac:a4:00
      xilinx_emaclite 40e00000.ethernet: Xilinx EmacLite at 0x40E00000 mapped to 0xF0180000, irq=10
      i2c /dev entries driver
      at24 0-0051: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      at24 0-0055: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      at24 1-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      at24 1-0054: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      platform 7c820000.cf-ad9643-core-lpc: Driver cf_axi_adc requests probe deferral
      platform 7c800000.cf-ad9643-core-hpc: Driver cf_axi_adc requests probe deferral
      spi spi32766.1: Driver ad9467 requests probe deferral
      spi spi32765.1: Driver ad9467 requests probe deferral
      cf_axi_fft_core 7ee00000.axi-fft: Device Tree Probing 'axi-fft'
      cf_axi_fft_core 7ee00000.axi-fft: ADI-FFT (0x40062) at 0x7EE00000 mapped to 0xf01e0000, DMA-0, DMA-1 probed
      ad9523 spi32766.3: probed ad9523-lpc
      ad9523 spi32765.3: probed ad9523-hpc
      ad9548 spi32766.2: Rev. 0xC6 probed
      ad9548 spi32765.2: Rev. 0xC6 probed
      platform 7a024000.cf-ad9122-core-lpc: Driver cf_axi_dds requests probe deferral
      platform 7a004000.cf-ad9122-core-hpc: Driver cf_axi_dds requests probe deferral
      TCP: cubic registered
      NET: Registered protocol family 17
      platform 7c820000.cf-ad9643-core-lpc: Driver cf_axi_adc requests probe deferral
      platform 7c800000.cf-ad9643-core-hpc: Driver cf_axi_adc requests probe deferral
      o|oo DCI 1
      cf_axi_dds 7a024000.cf-ad9122-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (0x60061) at 0x7A024000 mapped to 0xf0200000, probed DDS AD9122
      o|oo DCI 1
      cf_axi_dds 7a004000.cf-ad9122-core-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (0x60061) at 0x7A004000 mapped to 0xf0620000, probed DDS AD9122
      -------------oooooooooooo|oooooooooooo----------------------------  DCO 0x98 CLK 245760000 Hz
      cf_axi_adc 7c820000.cf-ad9643-core-lpc: ADI AIM (0x60061) at 0x7C820000 mapped to 0xf0a40000, DMA-0 probed ADC AD9643 as MASTER
      ------ooooooooooo|oooooooooo-----  DCO 0x90 CLK 245760000 Hz
      cf_axi_adc 7c800000.cf-ad9643-core-hpc: ADI AIM (0x60061) at 0x7C800000 mapped to 0xf0a60000, DMA-0 probed ADC AD9643 as SLAVE
      Freeing unused kernel memory: 2968K (c035e000 - c0644000)
      Starting logging: OK
      Initializing random number generator... random: dd urandom read with 65 bits of entropy available
      done.
      Starting network...
      Starting network...
      udhcpc (v1.21.1) started
      grep: /etc/resolv.conf: No such file or directory
      Sending discover...
      libphy: 40e00000:07 - Link is Up - 100/Full
      Sending discover...
      Sending select for 10.44.2.111...
      Lease of 10.44.2.111 obtained, lease time 86400
      deleting routers
      route: SIOCDELRT: No such process
      adding dns 10.32.51.110
       thttpd
      Welcome to ADI Microblaze Buildroot
      buildroot login: root
      #
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCOMMS1-EBZ#none#./
   :alt: Quick Start Guides#zynq|Linux on ZC702, ZC706, ZED

.. |ML605 Diagram| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/ml605.png
   :width: 500px
.. |LCD image| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/ml605-lcd.png
   :width: 200px
.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/quickstart/fmcomms1_netscope_td.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/quickstart/fmcomms1_netscope_fd.png
   :width: 600px
