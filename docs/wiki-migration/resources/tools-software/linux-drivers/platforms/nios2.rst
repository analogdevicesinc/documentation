Nios2 Linux on the Altera FPGA Development Boards
=================================================

|

.. warning::

   \ **NOTE:**

   | Support for the A10GX carrier is discontinued and will not be supported in future releases. Last pre-build images can be found here.


Loading Pre-built Images
------------------------

Download the pre-built image for you setup:

+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| FPGA Carrier               | FMC Card    | Download                                                                                                                                              |
+============================+=============+=======================================================================================================================================================+
| A10GX (10AX115S2F45I1SG)   | ADRV9009    | |adrv9009_a10gx_2019_r2.zip|                                                                                                                          |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S2F45I1SG)   | ADRV9371x   | |adrv9371x_a10gx_2019_r2.zip|                                                                                                                         |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S2F45I1SG)   | FMCDAQ2     | |daq2_a10gx_2019_r2.zip|                                                                                                                              |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S2F45I1SG)   | FMCDAQ2     | `daq2_a10gx_2018_r1.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/daq2_a10gx_2018_r1.zip>`_              |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S3F45E2SGE3) | FMCDAQ2     | `a10gx_daq2_2016_r1.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a10gx_daq2_2016_r1.zip>`_              |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S3F45E2SGE3) | FMCDAQ3     | `a10gx_daq3_2016_r1.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a10gx_daq3_2016_r1.zip>`_              |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A5GT                       | FMCJESDADC1 | `a5gt_fmcjesdadc1_2015_r2.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a5gt_fmcjesdadc1_2015_r2.zip>`_  |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S2F45I2SG)   | FMCDAQ2     | `a10gx_daq2_2015_r2.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a10gx_daq2_2015_r2.zip>`_              |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A5GT                       | FMCJESDADC1 | `a5gt_fmcjesdadc1_2015_r1.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a5gt_fmcjesdadc1_2015_r1.zip>`_  |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| A10GX (10AX115S2F45I2SG)   | FMCDAQ2     | `a10gx_daq2_2015_r1.zip <https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/a10gx_daq2_2015_r1.zip>`_                    |
+----------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/section>/resources/tools-software/linux-software/adi-kuiper_images/master#master_nios2_images&
   :alt: master#master_nios2_images&

If you are using a Windows machine and Quartus II is installed, the easiest way of loading the design is to directly run program.bat script (make sure that the Quartus II path specified in the script match the one from your machine). It will program the board and will launch a nios2-terminal where the Linux console messages will be printed.

An example of Linux console messages that are printed by the target: 

.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   ::
   
      Linux version 4.4.0-08393-g0e78611 (dragos@dragos-debian) (gcc version 5.3.0 (So
      urcery CodeBench Lite 2016.05-10) ) #149 Mon Jun 6 18:30:22 EEST 2016
      bootconsole [early0] enabled
      early_console initialized at 0xf01814f0
      On node 0 totalpages: 65536
      free_area_init_node: node 0, pgdat c0695f8c, node_mem_map c06b98c0
        Normal zone: 512 pages used for memmap
        Normal zone: 0 pages reserved
        Normal zone: 65536 pages, LIFO batch:15
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
      pcpu-alloc: [0] 0
      Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 65024
      Kernel command line: debug console=ttyJ0,115200
      PID hash table entries: 1024 (order: 0, 4096 bytes)
      Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
      Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
      Sorting __ex_table...
      Memory: 252976K/262144K available (2957K kernel code, 93K rwdata, 672K rodata, 3
      016K init, 99K bss, 9168K reserved, 0K cma-reserved)
      NR_IRQS:64 nr_irqs:64 0
      clocksource: nios2-clksrc: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns:
       19112604467 ns
      Calibrating delay loop (skipped), value calculated using timer frequency.. 200.0
      0 BogoMIPS (lpj=400000)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
      Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
      devtmpfs: initialized
      cpu cpu0: Error -2 creating of_node link
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645
      041785100000 ns
      NET: Registered protocol family 16
      clocksource: Switched to clocksource nios2-clksrc
      NET: Registered protocol family 2
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
      futex hash table entries: 256 (order: -1, 3072 bytes)
      jffs2: version 2.2. (NAND) ┬⌐ 2001-2006 Red Hat, Inc.
      Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
      io scheduler noop registered
      io scheduler deadline registered
      io scheduler cfq registered (default)
      101814f0.serial: ttyJ0 at MMIO 0x101814f0 (irq = 2, base_baud = 0) is a Altera J
      TAG UART
      console [ttyJ0] enabled
      console [ttyJ0] enabled
      bootconsole [early0] disabled
      bootconsole [early0] disabled
      loop: module loaded
      spi_altera 10181400.spi: base f0181400, irq 74
      libphy: altera_tse: probed
      altera_tse 10181000.ethernet (unnamed net_device) (uninitialized): MDIO bus alte
      ra_tse-0: created
      altera_tse 10181000.ethernet: Altera TSE MAC version 15.1 at 0x10181000 irq 3/4
      mousedev: PS/2 mouse device common for all mice
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Altera XCVR probed
      iio iio:device0: ad9528 setup
      ad9528 spi32766.0: probed ad9528-1
      ad9144 spi32766.1: Probed.
      NET: Registered protocol family 17
      ad9467 spi32766.2: AD9680 PLL LOCKED
      cf_axi_dds 10024000.axi-ad9152-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (8.00.b
      ) at 0x10024000 mapped to 0xf0024000, probed DDS AD9152
      cf_axi_adc 10010000.axi-ad9680-hpc: ADI AIM (9.00.b) at 0x10010000 mapped to 0xf
      0010000, probed ADC AD9680 as MASTER
      Freeing unused kernel memory: 3016K (c02e5000 - c05d7000)
      Starting logging: OK
      Initializing random number generator... random: dd urandom read with 35 bits of
      entropy available
      done.
      Starting network...
      altera_tse 10181000.ethernet eth0: device MAC address b2:94:3d:6e:11:8f
      altera_tse 10181000.ethernet eth0: TSE revision f01
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 1 ch 0 CDR/CMU PLL & RX offset cal
      ib OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 1 ch 1 CDR/CMU PLL & RX offset cal
      ib OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 1 ch 2 CDR/CMU PLL & RX offset cal
      ib OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 1 ch 3 CDR/CMU PLL & RX offset cal
      ib OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: RX transceiver ready
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 0 ATX PLL calibration OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 0 ch 0 TX termination and VOD cali
      b OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 0 ch 1 TX termination and VOD cali
      b OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 0 ch 2 TX termination and VOD cali
      b OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: Link 0 ch 3 TX termination and VOD cali
      b OK
      altera_xcvr 10000000.daq3_axi_jesd_xcvr: TX transceiver ready
      altera_tse 10181000.ethernet eth0: Link is Up - 1Gbps/Full - flow control off
      Network cable is plugged
      udhcpc (v1.24.2) started
      Sending discover...
      Sending select for 10.50.1.132...
      Lease of 10.50.1.132 obtained, lease time 28800
      deleting routers
      adding dns 10.32.51.110
      adding dns 10.64.53.110
                inet addr:10.50.1.132  Bcast:10.50.1.255  Mask:255.255.255.0
      Starting dropbear sshd: OK
      Starting IIO Server Daemon
   
      Welcome to Buildroot
      buildroot login:

.. raw:: html

   </details>


IIO Oscilloscope Remote
-----------------------

The IIO Oscilloscope application can be used to remotely connect to another platform that has a connected IIO device in order to configure the device and read data from it.

To install the application, please follow the instructions from here: :doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

Once the application is launched go to Settings -> Connect and enter the IP address of the target in the popup window. Click Refresh and OK.

Note: The IP address of the target can be found by looking to the Linux console messages (*Lease of 10.50.1.114 obtained, lease time 28800*) or using the Linux ifconfig command (log in using user *root* and password *analog*):

::

   Welcome to Buildroot
   buildroot login: root
   Password:
   # ifconfig
   eth0      Link encap:Ethernet  HWaddr B2:94:3D:6E:11:8F
             inet addr:10.50.1.114  Bcast:10.50.1.255  Mask:255.255.255.0
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:47 errors:0 dropped:11 overruns:0 frame:0
             TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:5386 (5.2 KiB)  TX bytes:1026 (1.0 KiB)
             Memory:10181000-101813ff

   lo        Link encap:Local Loopback
             inet addr:127.0.0.1  Mask:255.0.0.0
             UP LOOPBACK RUNNING  MTU:65536  Metric:1
             RX packets:0 errors:0 dropped:0 overruns:0 frame:0
             TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:0
             RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
   #

Some examples of the IIO Oscilloscope running on Windows and connected remotely to a target that runs Linux:

|image1| |image2|

Build Linux
-----------

.. include:: ../../linux-build/generic/nios2.rst

Quickstart Guides
-----------------

-  :doc:`AD-FMCDAQ2-EBZ Arria10GX Quickstart </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/a10gx>`
-  :doc:`AD-FMCDAQ3-EBZ Arria10GX Quickstart </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/a10gx>`
-  :doc:`ADRV9371x Arria10GX Quickstart </wiki-migration/resources/eval/user-guides/adrv9371x/quickstart/a10gx>`
-  :doc:`ADRV9009 Arria10GX Quickstart </wiki-migration/resources/eval/user-guides/adrv9009/quickstart/a10gx>`

.. |adrv9009_a10gx_2019_r2.zip| image:: https://swdownloads.analog.com/cse/nios2/2019_r2/adrv9009_a10gx.zip
.. |adrv9371x_a10gx_2019_r2.zip| image:: https://swdownloads.analog.com/cse/nios2/2019_r2/adrv9371x_a10gx.zip
.. |daq2_a10gx_2019_r2.zip| image:: https://swdownloads.analog.com/cse/nios2/2019_r2/daq2_a10gx.zip
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a10gx_daq2_iio_scope.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/nios2/a5gt_fmcjesdadc1_iio_scope.png
   :width: 500px
