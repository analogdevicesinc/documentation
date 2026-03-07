AD9081 Arria10 SoC Development Kit Quick Start Guide
====================================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/eval-ad9081/quickstart/a10soc.html\


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081/quickstart/a10soc_adrv9081.jpg
   :align: center
   :width: 600px

Requirements
------------

-  :adi:`EVAL-AD9081`

   -  2x SMA cable for analog signal loopback (optional, but recommended)

-  `Arria10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_ (Rev. C or later)

   -  Power-supply
   -  USB mini cable for serial console (optional, but recommended)
   -  Ethernet cable for network connectivity (optional, but recommended)

-  SD card with latest ADI Linux image


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


Creating / Configuring the SD Card
----------------------------------

:doc:`Create SD Image. (it is a single image for all boards) </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

-   Copy next boot files from <fc #ff0000>\ ``socfpga_arria10_socdk_ad9081``\ </fc> directory directly on SD Card ``BOOT`` partition :

   -  ``fit_spl_fpga.itb``
   -  ``socfpga_arria10_socdk_sdmmc.dtb``
   -  ``u-boot.img``
   -  ``zImage`` (from ``socfpga_arria10-common`` folder)
   -  ``extlinux.conf`` in the extlinux folder from SD Card

-  Write u-boot-splx4.sfp from <fc #ff0000>\ ``socfpga_arria10_socdk_ad9081``\ </fc> folder on third SD Card partition:

::

       root@raspberrypi:~# lsblk
       NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
       sda           8:0    1 14.9G  0 disk 
       ├─sda1        8:1    1    1G  0 part /media/pi/BOOT
       ├─sda2        8:2    1  7.6G  0 part /media/pi/rootfs
       └─sda3        8:3    1    4M  0 part 
       root@raspberrypi:~# dd if="./u-boot-splx4.sfp" of="/dev/sda3" bs=512
       2048+0 records in
       2048+0 records out
       1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.25035 s, 4.2 MB/s

Hardware Setup
--------------

AD9081-FMCA-EBZ / AD9082-FMCA-EBZ (Single MxFE) HDL Reference Design
====================================================================

.. important::

   We are in the process of migrating our documentation to GitHub IO. Please check the following link for updated information regarding the **HDL project**: https://analogdevicesinc.github.io/hdl/projects/ad9081_fmca_ebz/index.html.


Functional Overview
-------------------

The AD9081-FMCA-EBZ / AD9082-FMCA-EBZ reference design is a processor based (e.g. Microblaze) embedded system. The design consists from a receive and a transmit chain.

The receive chain transports the captured samples from ADC to the system memory (DDR). Before transferring the data to DDR the samples are stored in a buffer implemented on block rams from the FPGA fabric (util_adc_fifo). The space allocated in the buffer for each channel depends on the number of currently active channels. It goes up to M x 64k samples if a single channel is selected or 64k samples per channel if all channels are selected.

The transmit chain transports samples from the system memory to the DAC devices. Before streaming out the data to the DAC through the JESD link the samples first are loaded into a buffer (util_dac_fifo) which will cyclically stream the samples at the tx_device_clk data rate. The space allocated in the transmit buffer for each channel depends on the number of currently active channels. It goes up to M x 64k samples if a single channel is selected or 64k samples per channel if all channels are selected.

All cores from the receive and transmit chains are programmable through an AXI-Lite interface.

The transmit and receive chains can operate at different data rates having separate rx_device_clk/tx_device_clk and corresponding lane rates but must share the same reference clock.

Board setup
-----------

.. important::

   **The following rework is required:**

   
   -  In order to avoid using an external clock source and fully rely on the HMC7044 clock chip,*\* rotate the C6D/C4D caps in C5D/C3D position*\* (**Please note:** In the latest version of the board, this is now the default configuration, so this configuration step **might not be needed anymore**)
   -  If LEDS V1P0_LED and VINT_LED are not on please \*\* depopulate R22M and populate R2M*\*
   


HDL source code
---------------

.. admonition:: Download
   :class: download

   **Reference design location:**

   
   -  :git-hdl:`projects/ad9081_fmca_ebz`
   


Supported Carriers
~~~~~~~~~~~~~~~~~~

-  `ZCU102 <https://www.xilinx.com/ZCU102>`_ FMC HPC0 Slot
-  `ZC706 <https://www.xilinx.com/ZC706>`_ FMC HPC Slot
-  `VCU118 <https://www.xilinx.com/VCU118>`_ FMC+ Slot

Useful links
------------

-  :doc:`AD9081 Quick Start Guides </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`
-  :doc:`Building HDL </wiki-migration/resources/fpga/docs/build>`
-  :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

Block design
------------

The block design supports parameters and scales based on it as shown on the below two examples.

The parameters for Rx or Tx links can be changed from the system_project.tcl :

.. code:: tcl

   # Parameter description:
   #    JESD_MODE : used link layer encoder mode 
   #      64B66B - 64b66b link layer defined in JESD 204C
   #      8B10B  - 8b10b link layer defined in JESD 204B
   #    
   #    RX_RATE :  line rate of the Rx link ( MxFE to FPGA ) 
   #    TX_RATE :  line rate of the Tx link ( FPGA to MxFE )
   #    [RX/TX]_JESD_M : number of converters per link
   #    [RX/TX]_JESD_L : number of lanes per link
   #    [RX/TX]_JESD_NP : number of bits per sample, only 16 is supported
   #    [RX/TX]_NUM_LINKS : number of links, 1 - single link; 2 - dual link. 

   adi_project mxfe_zcu102 0 [list \
       JESD_MODE 8B10B \   
       RX_JESD_M 8 \
       RX_JESD_L 4 \
       RX_JESD_S 1 \
       RX_JESD_NP 16 \
       RX_NUM_LINKS 1 \
       TX_JESD_M 8 \
       TX_JESD_L 4 \
       TX_JESD_S 1 \
       TX_JESD_NP 16 \
       TX_NUM_LINKS 1 \
   ]

For the parameter selection the following restrictions apply:

-  NP = 8, 12, 16
-  F = 1, 2, 3, 4, 6, 8
-  :doc:`/wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx`
-  :doc:`/wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx`

IP list
~~~~~~~

| Following IPs are used in the block design:
| ^IP name^Wiki page^

+--------------+-----------------------------------------------------------------------------------------------------------------+
| XCVR         | :doc:`UTIL_ADXCVR core for Xilinx devices </wiki-migration/resources/fpga/docs/util_xcvr>`                      |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| XCVR         | :doc:`AXI_ADXCVR </wiki-migration/resources/fpga/docs/axi_adxcvr>`                                              |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| RX JESD LINK | :doc:`JESD204B/C Link Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>`   |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| TX JESD LINK | :doc:`JESD204B/C Link Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>`  |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| RX JESD TPL  | :doc:`ADC JESD204B/C Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_adc>` |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| TX JESD TPL  | :doc:`DAC JESD204B/C Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| UTIL CPACK   | :doc:`Channel CPACK Utility Core (util_cpack) </wiki-migration/resources/fpga/docs/util_cpack>`                 |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| UTIL UPACK   | :doc:`Channel UNPACK Utility Core (util_upack) </wiki-migration/resources/fpga/docs/util_upack>`                |
+--------------+-----------------------------------------------------------------------------------------------------------------+
| AXI DMAC     | :doc:`High-Speed DMA Controller Peripheral </wiki-migration/resources/fpga/docs/axi_dmac>`                      |
+--------------+-----------------------------------------------------------------------------------------------------------------+

Example block design for Single Link; M=8; L=4;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_204b_m8l4.svg
   :align: center

The Rx links (ADC Path) operate with the following parameters:

-  Rx Deframer parameters: L=4, M=8, F=4, S=1, N’=16, N = 16 (Quick Config 0x0A)
-  Sample Rate : 250 MSPS
-  Dual link : No
-  RX_DEVICE_CLK – 250 MHz (Lane Rate/40)
-  REF_CLK – 500MHz (Lane Rate/20)
-  JESD204B Lane Rate – 10Gbps
-  QPLL0 or CPLL

The Tx links (DAC Path) operate with the following parameters:

-  Tx Framer parameters: L=4, M=8, F=4, S=1, N’=16, N = 16 (Quick Config 0x09)
-  Sample Rate : 250 MSPS
-  Dual link : No
-  TX_DEVICE_CLK – 250 MHz (Lane Rate/40)
-  REF_CLK – 500MHz (Lane Rate/20)
-  JESD204B Lane Rate – 10Gbps
-  QPLL0 or CPLL

Example block design for Single Link; M=4; L=8;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_204b_m4l8.svg
   :align: center

The Rx links are set for full bandwidth mode and operate with the following parameters:

-  Rx Deframer parameters: L=8, M=4, F=1, S=1, N’=16, N = 16 (Quick Config 0x12)
-  Sample Rate : 1550 MSPS
-  Dual link : No
-  RX_DEVICE_CLK – 387.5 MHz (Lane Rate/40)
-  REF_CLK – 775MHz (Lane Rate/20)
-  JESD204B Lane Rate – 15.5Gbps
-  QPLL0

The Tx links are set for full bandwidth mode and operate with the following parameters:

-  Tx Framer parameters: L=8, M=4, F=1, S=1, N’=16, N = 16 (Quick Config 0x11)
-  Sample Rate : 1550 MSPS
-  Dual link : No
-  TX_DEVICE_CLK – 387.5 MHz (Lane Rate/40)
-  REF_CLK – 775MHz (Lane Rate/20)
-  JESD204B Lane Rate – 15.5Gbps
-  QPLL0

Example block design for Single Link; M=2; L=8; JESD204C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Observation: In 2019_R2 release the Xilinx JESD Physical layer IP Core is used, however in newer versions it is replaced with ADI's util_adxcvr IP core.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_204c_m2l8.svg
   :align: center

.. important::

   **Build instructions:**

   
   The project must be built with the following parameters:
   
   ::
   
      make JESD_MODE=64B66B \
           RX_RATE=16.5 \
           TX_RATE=16.5 \
           RX_JESD_M=2 \
           RX_JESD_L=8 \
           RX_JESD_S=2 \
           RX_JESD_NP=16 \
           TX_JESD_M=2 \
           TX_JESD_L=8 \
           TX_JESD_S=4 \
           TX_JESD_NP=8
   


The Rx link is operating with the following parameters:

-  Rx Deframer parameters: L=8, M=2, F=1, S=2, N’=16, N=16 (Quick Config 0x13)
-  Sample Rate : 4000 MSPS
-  Dual link : No
-  RX_DEVICE_CLK – 250 MHz (Lane Rate/66)
-  REF_CLK – 500 MHz (Lane Rate/33)
-  JESD204C Lane Rate – 16.5Gbps
-  QPLL1

The Tx link is operating with the following parameters:

-  Tx Framer parameters: L=8, M=2, F=1, S=4, N’=8, N=8 (Quick Config 0x13)
-  Sample Rate : 8000 MSPS
-  Dual link : No
-  TX_DEVICE_CLK – 250 MHz (Lane Rate/66)
-  REF_CLK – 500 MHz (Lane Rate/33)
-  JESD204C Lane Rate – 16.5Gbps
-  QPLL1

Clock sources
-------------

The clock sources depend on the in use carrier and are depicted on the below diagrams:

ZCU102
~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_clocking_zcu102.png
   :align: center

VC118
~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_clocking_vcu118.png
   :align: center

Software considerations
-----------------------

ADC - crossbar config
~~~~~~~~~~~~~~~~~~~~~

Due physical constraints Rx lanes are reordered as described in the following table. e.g physical lane 2 from ADC connects to logical lane 7 from the FPGA. Therefore the crossbar from the device must be set accordingly.

============ ===========================
ADC phy Lane FPGA Rx lane / Logical Lane
============ ===========================
0            2
1            0
2            7
3            6
4            5
5            4
6            3
7            1
============ ===========================

DAC - crossbar config
~~~~~~~~~~~~~~~~~~~~~

Due physical constraints Tx lanes are reordered as described in the following table: e.g physical lane 2 from DAC connects to logical lane 7 from the FPGA. Therefore the crossbar from the device must be set accordingly.

============ ===========================
DAC phy Lane FPGA Tx lane / Logical Lane
============ ===========================
0            0
1            2
2            7
3            6
4            1
5            5
6            4
7            3
============ ===========================

|common##Useful links&nofooter&noeditbtn| |common##Support&nofooter&noeditbtn|

.. |common##Useful links&nofooter&noeditbtn| image:: https://wiki.analog.com/_media/page>/resources/eval/user-guides/ad9081_fmca_ebz/common##Useful links&nofooter&noeditbtn
.. |common##Support&nofooter&noeditbtn| image:: https://wiki.analog.com/_media/page>/resources/eval/user-guides/ad9081_fmca_ebz/common##Support&nofooter&noeditbtn


FMC Pin Connection Configuration Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   To be compatible with the EVAL-AD9081-9082 the Arria10 SoC Development Kit requires a minor rework.


In the default configuration of the Arria10 SoC Development Kit some of the FMC header pins are connected to a dedicated clock chip. To be compatible with the EVAL-AD9081-9082 these pins need to be connected directly to the FPGA.

The connection of those pins can be changed by moving the position of four zero Ohm resistors:

-  R612 to R610
-  R613 to R611
-  R621 to R620
-  R633 to R632

These resistors can be found on the backside of the Arria10 SoC Development Kit underneath the FMC A connector (J29). The following picture shows the required configuration to be compatible with the EVAL-AD9081-9082.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/a10soc_fmc_rework.jpg
   :align: center

Connections
-----------

-  Insert the EVAL-AD9081 board into the FMC A (J29) header of the Arria10 SoC Development Kit
-  Both the HPS (J26) and FPGA (J27) memory module must be installed on the Arria10 SoC Development Kit.
-  For network connectivity connect a Ethernet cable to the right most Ethernet port (J5).
-  For the serial console connect a USB cable to UART1 (J10).
-  Insert the microSD card into the microSD card slot.

All jumpers and switches on the Arria10 SoC Development Kit should be in the `default position <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/ug/ug-a10-soc-devkit.pdf#page=15>`_ configuring the board for SD card boot.

Booting the System
------------------

After turning on the power switch the following messages should appear on the serial console.

::

   <nowiki>
   U-Boot SPL 2021.07-16360-gee63370553-dirty (Jan 26 2022 - 11:11:00 +0200)
   FPGA: Checking FPGA configuration setting ...
   FPGA: Start to program peripheral/full bitstream ...
   FPGA: Early Release Succeeded.
   FPGA: Checking FPGA configuration setting ...
   FPGA: Start to program peripheral/full bitstream ...
   FPGA: Early Release Succeeded.

   U-Boot SPL 2021.07-16360-gee63370553-dirty (Jan 26 2022 - 11:11:00 +0200)
   DDRCAL: Success
   FPGA: Checking FPGA configuration setting ...
   FPGA: Start to program core bitstream ...
   Full Configuration Succeeded.
   FPGA: Enter user mode.
   WDT:   Started with servicing (10s timeout)
   Trying to boot from MMC1
   </nowiki>

Configuring the FPGA will take a few seconds. Once the FPGA has been configured the green D18 LED will turn on and the boot process will continue.

::

   <nowiki>
   U-Boot 2021.07-16360-gee63370553-dirty (Jan 26 2022 - 11:11:00 +0200)socfpga_arria10, Build: jenkins-master-quartus_boot_on_ubuntu_master-40

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
   Net:
   Warning: ethernet@ff800000 (eth0) using random MAC address - ee:f4:d5:a3:12:2f
   eth0: ethernet@ff800000
   Hit any key to stop autoboot:  0
   Failed to load 'u-boot.scr'
   14981396 bytes read in 721 ms (19.8 MiB/s)
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
   162 bytes read in 6 ms (26.4 KiB/s)
   1:      Linux Default
   Retrieving file: /extlinux/../zImage
   8124456 bytes read in 399 ms (19.4 MiB/s)
   append: root=/dev/mmcblk0p2 rw rootwait earlyprintk console=ttyS0,115200n8
   Retrieving file: /extlinux/../socfpga_arria10_socdk_sdmmc.dtb
   36828 bytes read in 9 ms (3.9 MiB/s)
   Kernel image @ 0x1000000 [ 0x000000 - 0x7bf828 ]
   ## Flattened Device Tree blob at 02000000
      Booting using the fdt blob at 0x2000000
      Loading Device Tree to 09ff4000, end 09ffffdb ... OK

   Starting kernel ...

   Deasserting all peripheral resets
   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.10.0-97993-ga7064610e8f3 (jenkins@romlxbuild1.adlk.analog.com) (arm-xilinx-linux-gnueabi-gcc.real (GCC) 10.2.0, GNU ld (GNU Binutils) 2.35.0.20200730) #4699 SMP Sat Jan 29 09:17:25 GMT 2022
   [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
   [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   [    0.000000] OF: fdt: Machine model: Altera SOCFPGA Arria 10
   ...
   </nowiki>



.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

::

   <nowiki>
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
   [    0.000000] Memory: 884232K/1048576K available (13312K kernel code, 1261K rwdata, 7360K rodata, 1024K init, 202K bss, 33272K reserved, 131072K cma-reserved, 131072K highmem)
   [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
   [    0.000000] ftrace: allocating 40785 entries in 80 pages
   [    0.000000] ftrace: allocated 80 pages with 2 groups
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
   [    0.000000] random: get_random_bytes called from start_kernel+0x3a0/0x558 with crng_init=0
   [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
   [    0.000005] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
   [    0.007885] Switching to timer-based delay loop, resolution 10ns
   [    0.014180] Console: colour dummy device 80x30
   [    0.018626] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
   [    0.029111] pid_max: default: 32768 minimum: 301
   [    0.033810] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   [    0.041088] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   [    0.049361] CPU: Testing write buffer coherency: ok
   [    0.054260] CPU0: Spectre v2: using BPIALL workaround
   [    0.059448] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   [    0.065537] Setting up static identity map for 0x100000 - 0x100060
   [    0.071795] rcu: Hierarchical SRCU implementation.
   [    0.076836] smp: Bringing up secondary CPUs ...
   [    0.081933] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   [    0.081940] CPU1: Spectre v2: using BPIALL workaround
   [    0.092713] smp: Brought up 1 node, 2 CPUs
   [    0.096795] SMP: Total of 2 processors activated (400.00 BogoMIPS).
   [    0.103046] CPU: All CPU(s) started in SVC mode.
   [    0.108124] devtmpfs: initialized
   [    0.116264] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
   [    0.124202] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   [    0.134012] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
   [    0.144869] NET: Registered protocol family 16
   [    0.150976] DMA: preallocated 256 KiB pool for atomic coherent allocations
   [    0.158672] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
   [    0.166655] hw-breakpoint: maximum watchpoint size is 4 bytes.
   [    0.179421] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
   [    0.192639] OF: /soc/gpio@ffc02a00/gpio-controller@0: could not get #gpio-cells for /soc/clkmgr@ffd04000/clocks/l4_sp_clk
   [    0.214584] vgaarb: loaded
   [    0.217513] SCSI subsystem initialized
   [    0.221397] usbcore: registered new interface driver usbfs
   [    0.226919] usbcore: registered new interface driver hub
   [    0.232253] usbcore: registered new device driver usb
   [    0.237437] usb_phy_generic soc:usbphy: supply vcc not found, using dummy regulator
   [    0.247846] mc: Linux media interface: v0.10
   [    0.252125] videodev: Linux video capture interface: v2.00
   [    0.257664] pps_core: LinuxPPS API ver. 1 registered
   [    0.262614] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
   [    0.271714] PTP clock support registered
   [    0.275892] jesd204: found 0 devices and 0 topologies
   [    0.280944] FPGA manager framework
   [    0.284405] Advanced Linux Sound Architecture Driver Initialized.
   [    0.291406] clocksource: Switched to clocksource timer1
   [    0.839355] NET: Registered protocol family 2
   [    0.844253] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
   [    0.852602] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
   [    0.860363] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
   [    0.867569] TCP: Hash tables configured (established 8192 bind 8192)
   [    0.874009] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
   [    0.880635] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
   [    0.887849] NET: Registered protocol family 1
   [    0.892607] RPC: Registered named UNIX socket transport module.
   [    0.898502] RPC: Registered udp transport module.
   [    0.903212] RPC: Registered tcp transport module.
   [    0.907893] RPC: Registered tcp NFSv4.1 backchannel transport module.
   [    0.914320] PCI: CLS 0 bytes, default 64
   [    0.919358] workingset: timestamp_bits=30 max_order=18 bucket_order=0
   [    0.930670] NFS: Registering the id_resolver key type
   [    0.935762] Key type id_resolver registered
   [    0.939925] Key type id_legacy registered
   [    0.943941] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
   [    0.950762] ntfs: driver 2.1.32 [Flags: R/W].
   [    0.955263] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
   [    0.961865] bounce: pool size: 64 pages
   [    0.965693] io scheduler mq-deadline registered
   [    0.970201] io scheduler kyber registered
   [    0.978553] dma-pl330 ffda1000.pdma: Loaded driver for PL330 DMAC-341330
   [    0.985260] dma-pl330 ffda1000.pdma:         DBUFF-512x8bytes Num_Chans-8 Num_Peri-32 Num_Events-8
   [    0.995937] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
   [    1.003152] printk: console [ttyS0] disabled
   [    1.007458] ffc02100.serial1: ttyS0 at MMIO 0xffc02100 (irq = 45, base_baud = 6250000) is a 16550A
   [    1.016446] printk: console [ttyS0] enabled
   [    1.016446] printk: console [ttyS0] enabled
   [    1.024781] printk: bootconsole [earlycon0] disabled
   [    1.024781] printk: bootconsole [earlycon0] disabled
   [    1.036278] brd: module loaded
   [    1.039610] at24 0-0051: supply vcc not found, using dummy regulator
   [    1.047235] at24 0-0051: 4096 byte 24c32 EEPROM, writable, 32 bytes/write
   [    1.055105] spi_altera ff200040.spi: regoff 0, irq 48
   [    1.061652] altr_a10sr_gpio altr_a10sr_gpio.0.auto: DMA mask not set
   [    1.069133] libphy: Fixed MDIO Bus: probed
   [    1.073723] CAN device driver interface
   [    1.077767] socfpga-dwmac ff800000.ethernet: IRQ eth_wake_irq not found
   [    1.084373] socfpga-dwmac ff800000.ethernet: IRQ eth_lpi not found
   [    1.090650] socfpga-dwmac ff800000.ethernet: No sysmgr-syscon node found
   [    1.097336] socfpga-dwmac ff800000.ethernet: Unable to parse OF data
   [    1.103721] socfpga-dwmac: probe of ff800000.ethernet failed with error -524
   [    1.110901] stmmaceth ff800000.ethernet: IRQ eth_wake_irq not found
   [    1.117156] stmmaceth ff800000.ethernet: IRQ eth_lpi not found
   [    1.123251] stmmaceth ff800000.ethernet: User ID: 0x10, Synopsys ID: 0x37
   [    1.130017] stmmaceth ff800000.ethernet:     DWMAC1000
   [    1.134891] stmmaceth ff800000.ethernet: DMA HW capability register supported
   [    1.142003] stmmaceth ff800000.ethernet: RX Checksum Offload Engine supported
   [    1.149105] stmmaceth ff800000.ethernet: COE Type 2
   [    1.153967] stmmaceth ff800000.ethernet: TX Checksum insertion supported
   [    1.160638] stmmaceth ff800000.ethernet: Enhanced/Alternate descriptors
   [    1.167227] stmmaceth ff800000.ethernet: Enabled extended descriptors
   [    1.173643] stmmaceth ff800000.ethernet: Ring mode enabled
   [    1.179104] stmmaceth ff800000.ethernet: Enable RX Mitigation via HW Watchdog Timer
   [    1.186743] stmmaceth ff800000.ethernet: device MAC address fe:10:4c:fb:7b:c0
   [    1.201960] libphy: stmmac: probed
   [    1.205362] Micrel KSZ9031 Gigabit PHY stmmac-0:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=stmmac-0:07, irq=POLL)
   [    1.219006] usbcore: registered new interface driver asix
   [    1.224463] usbcore: registered new interface driver ax88179_178a
   [    1.230552] usbcore: registered new interface driver cdc_ether
   [    1.236409] usbcore: registered new interface driver net1080
   [    1.242076] usbcore: registered new interface driver cdc_subset
   [    1.247989] usbcore: registered new interface driver zaurus
   [    1.253590] usbcore: registered new interface driver cdc_ncm
   [    1.259712] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
   [    1.266917] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
   [    1.274239] dwc2 ffb00000.usb: EPs: 16, dedicated fifos, 8064 entries in SPRAM
   [    1.281884] dwc2 ffb00000.usb: DWC OTG Controller
   [    1.286588] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
   [    1.293664] dwc2 ffb00000.usb: irq 46, io mem 0xffb00000
   [    1.299105] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
   [    1.307344] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    1.314541] usb usb1: Product: DWC OTG Controller
   [    1.319224] usb usb1: Manufacturer: Linux 5.10.0-97993-ga7064610e8f3 dwc2_hsotg
   [    1.326504] usb usb1: SerialNumber: ffb00000.usb
   [    1.331581] hub 1-0:1.0: USB hub found
   [    1.335344] hub 1-0:1.0: 1 port detected
   [    1.339860] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   [    1.346379] ehci-pci: EHCI PCI platform driver
   [    1.351303] usbcore: registered new interface driver uas
   [    1.356690] usbcore: registered new interface driver usb-storage
   [    1.362761] usbcore: registered new interface driver usbserial_generic
   [    1.369274] usbserial: USB Serial support registered for generic
   [    1.375287] usbcore: registered new interface driver ftdi_sio
   [    1.381027] usbserial: USB Serial support registered for FTDI USB Serial Device
   [    1.388376] usbcore: registered new interface driver upd78f0730
   [    1.394296] usbserial: USB Serial support registered for upd78f0730
   [    1.404141] rtc-ds1307 0-0068: SET TIME!
   [    1.412346] rtc-ds1307 0-0068: registered as rtc0
   [    1.417128] i2c /dev entries driver
   [    1.421221] usbcore: registered new interface driver uvcvideo
   [    1.426971] USB Video Class driver (1.1.1)
   [    1.435263] ltc2978: probe of 0-005c failed with error -121
   [    1.441563] Synopsys Designware Multimedia Card Interface Driver
   [    1.447776] dw_mmc ff808000.dwmmc0: IDMAC supports 32-bit address mode.
   [    1.454457] dw_mmc ff808000.dwmmc0: Using internal DMA controller.
   [    1.460628] dw_mmc ff808000.dwmmc0: Version ID is 270a
   [    1.465813] dw_mmc ff808000.dwmmc0: DW MMC controller at irq 41,32 bit host data width,1024 deep fifo
   [    1.475210] mmc_host mmc0: card is polling.
   [    1.480896] ledtrig-cpu: registered to indicate activity on CPUs
   [    1.487000] usbcore: registered new interface driver usbhid
   [    1.491409] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 400000Hz, actual 396825HZ div = 63)
   [    1.492556] usbhid: USB HID core driver
   [    1.507514] ad9371 spi0.1: ad9371_probe : enter
   [    1.516453] ad9528 spi0.0: supply vcc not found, using dummy regulator
   [    1.533318] iio iio:device2: SPI Read Verify failed (0xFFFFFF)
   [    1.539203] ad9528: probe of spi0.0 failed with error -5
   [    1.547352] fpga_manager fpga0: SoCFPGA Arria10 FPGA Manager registered
   [    1.554659] usbcore: registered new interface driver snd-usb-audio
   [    1.562740] NET: Registered protocol family 10
   [    1.567907] Segment Routing with IPv6
   [    1.571661] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   [    1.578038] NET: Registered protocol family 17
   [    1.580807] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
   [    1.582508] NET: Registered protocol family 15
   [    1.592253] mmc0: new high speed SDHC card at address aaaa
   [    1.601456] can: controller area network core
   [    1.606461] NET: Registered protocol family 29
   [    1.610888] can: raw protocol
   [    1.611736] mmcblk0: mmc0:aaaa SC32G 29.7 GiB
   [    1.613896] can: broadcast manager protocol
   [    1.622484] can: netlink gateway - max_hops=1
   [    1.626987] 8021q: 802.1Q VLAN Support v1.8
   [    1.631210] NET: Registered protocol family 36
   [    1.635154]  mmcblk0: p1 p2 p3
   [    1.635676] Key type dns_resolver registered
   [    1.643204] oprofile: no performance counters
   [    1.647639] oprofile: using timer interrupt.
   [    1.651980] ThumbEE CPU extension supported.
   [    1.656240] Registering SWP/SWPB emulation handler
   [    1.661584] ad9371 spi0.1: ad9371_probe : enter
   [    1.668476] ad9371 spi0.1: ad9371_probe : enter
   [    1.675014] of_cfs_init
   [    1.677484] of_cfs_init: OK
   [    1.680501] ALSA device list:
   [    1.683497]   No soundcards found.
   [    1.687104] dw-apb-uart ffc02100.serial1: forbid DMA for kernel console
   [    1.720547] random: fast init done
   [    1.724949] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   [    1.733085] VFS: Mounted root (ext4 filesystem) on device 179:2.
   [    1.749478] devtmpfs: mounted
   [    1.756347] Freeing unused kernel memory: 1024K
   [    1.761310] Run /sbin/init as init process
   [    2.346797] systemd[1]: System time before build time, advancing clock.
   [    2.394194] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
   [    2.416064] systemd[1]: Detected architecture arm.

   Welcome to Kuiper GNU/Linux 10 (buster)!

   [    2.504365] systemd[1]: Set hostname to <analog>.
   [    2.847136] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   [    2.864175] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   [    3.047840] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
   [    3.057524] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
   [    3.272364] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.290704] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
   [    3.302364] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.309824] systemd[1]: Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [    3.341606] random: systemd: uninitialized urandom read (16 bytes read)
   [    3.348834] systemd[1]: Listening on Journal Socket.
   [  OK  ] Listening on Journal Socket.
            Starting Restore / save the current clock...
   [  OK  ] Reached target Swap.
   [  OK  ] Listening on initctl Compatibility Named Pipe.
            Starting Load Kernel Modules...
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
            Mounting RPC Pipe File System...
   [  OK  ] Created slice system-getty.slice.
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Listening on udev Kernel Socket.
   [  OK  ] Listening on Syslog Socket.
   [  OK  ] Reached target Slices.
   [  OK  ] Listening on udev Control Socket.
            Starting udev Coldplug all Devices...
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   [  OK  ] Listening on Journal Socket (/dev/log).
            Starting Journal Service...
            Starting Set the console keyboard layout...
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [  OK  ] Started Restore / save the current clock.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started Journal Service.
   [  OK  ] Mounted RPC Pipe File System.
            Starting Apply Kernel Variables...
            Mounting Kernel Configuration File System...
            Starting Remount Root and Kernel File Systems...
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started Apply Kernel Variables.
   [  OK  ] Started Set the console keyboard layout.
   [  OK  ] Started udev Coldplug all Devices.
            Starting Helper to synchronize boot up for ifupdown...
   [  OK  ] Started Remount Root and Kernel File Systems.
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
            Starting Load/Save Random Seed...
            Starting Flush Journal to Persistent Storage...
            Starting Create System Users...
   [  OK  ] Started Load/Save Random Seed.
   [  OK  ] Started Create System Users.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Started Flush Journal to Persistent Storage.
   [  OK  ] Started Create Static Device Nodes in /dev.
   [  OK  ] Reached target Local File Systems (Pre).
            Starting udev Kernel Device Manager...
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Reached target Local Encrypted Volumes.
   [  OK  ] Found device /dev/ttyS0.
   [  OK  ] Found device /dev/disk/by-partuuid/004ba301-01.
            Starting File System Check…isk/by-partuuid/004ba301-01...
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Started File System Check …/disk/by-partuuid/004ba301-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Create Volatile Files and Directories...
            Starting Preprocess NFS configuration...
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Raise network interfaces...
            Starting Set console font and keymap...
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Create Volatile Files and Directories.
            Starting Network Time Synchronization...
            Starting Update UTMP about System Boot/Shutdown...
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
            Starting Load Kernel Modules...
            Starting Tell Plymouth To Write Out Runtime Data...
   [  OK  ] Started Network Time Synchronization.
   [  OK  ] Started Raise network interfaces.
   [  OK  ] Reached target System Time Synchronized.
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Reached target Sockets.
   [  OK  ] Reached target Basic System.
   [  OK  ] Started tof-server.service.
   [  OK  ] Started Regular background program processing daemon.
   [  OK  ] Started CUPS Scheduler.
            Starting LSB: Switch to on…nless shift key is pressed)...
            Starting Login Service...
            Starting triggerhappy global hotkey daemon...
            Starting rng-tools.service...
   [  OK  ] Started D-Bus System Message Bus.
            Starting System Logging Service...
            Starting dhcpcd on all interfaces...
            Starting Avahi mDNS/DNS-SD Stack...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting dphys-swapfile - …unt, and delete a swap file...
            Starting Modem Manager...
            Starting WPA supplicant...
            Starting Disk Manager...
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Reached target Timers.
   [  OK  ] Started triggerhappy global hotkey daemon.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
   [  OK  ] Started Login Service.
   [  OK  ] Started System Logging Service.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started Check for Raspberry Pi EEPROM updates.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started WPA supplicant.
            Starting Authorization Manager...
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Reached target Network.
   [  OK  ] Started IIO Daemon.
   [  OK  ] Reached target Network is Online.
            Starting Internet superserver...
            Starting /etc/rc.local Compatibility...
            Starting OpenBSD Secure Shell server...
            Starting Permit User Sessions...
            Starting HTTP based time synchronization tool...
   [  OK  ] Started Internet superserver.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
   [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started Permit User Sessions.
   [  OK  ] Started HTTP based time synchronization tool.
            Starting Manage, Install and Generate Color Profiles...
            Starting Light Display Manager...
            Starting Hold until boot process finishes up...
   [  OK  ] Started Authorization Manager.
   [  OK  ] Started Manage, Install and Generate Color Profiles.
   [  OK  ] Started Modem Manager.

   Raspbian GNU/Linux 10 analog ttyS0

   analog login: root (automatic login)

   Last login: Tue Feb  1 11:17:12 GMT 2022 on ttyS0
   Linux analog 5.10.0-97993-ga7064610e8f3 #4699 SMP Sat Jan 29 09:17:25 GMT 2022 armv7l

   The programs included with the Debian GNU/Linux system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
   permitted by applicable law.
   root@analog:~#
   </nowiki>

.. raw:: html

   </details>


Once the boot process has completed you'll be greeted with command prompt. As a quick check if the EVAL-AD9081 was correctly recognized run the \`iio_info\` command and filter for the registered devices.

::

   <nowiki>
   Last login: Thu Jan  1 00:00:12 UTC 1970 on tty1
   Welcome to Linaro 14.04 (GNU/Linux 4.6.0-09244-g5f1195d00092-dirty armv7l)

     * Documentation:  https://wiki.analog.com/ https://ez.analog.com/
   root@analog:~# iio_info | grep :device
           iio:device0: 0-0014
           iio:device1: 0-0016
   </nowiki>

If the Arria 10 SoC Development Kit is connected to a network with a DHCP server the IP address assigned to the board appears on the LCD. Alternatively you can query the IP address by running \`ifconfig eth0\` on the command line. To manually assign an IP address run \`ifconfig eth0 *IP_ADDR*\ \`.

IIO Oscilloscope Remote
-----------------------

Please see also here::doc:`Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The IIO Oscilloscope application can be used to connect to another platform that has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image1|

More information
================

:doc:`AD9081 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`

More Information
----------------

-  :doc:`ADRV9001/2 Quick Start Guides </wiki-migration/resources/eval/user-guides/adrv9002/quickstart>`

   -  :doc:`ADRV9002 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zynqmp>`
   -  :doc:`ADRV9002 Zynq SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zynq>`
   -  :doc:`ADRV9002 Zynq Zed Board Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/zed>`
   -  :doc:`ADRV9002 Arria10 SoC Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9002/quickstart/a10soc>`

-  :doc:`ADRV9001/ADRV9002 HDL Reference Design </wiki-migration/resources/eval/user-guides/adrv9002/reference_hdl>`

   -  :doc:`AXI_ADRV9001/AXI_ADRV9002 Interface Core </wiki-migration/resources/eval/user-guides/adrv9002/axi_adrv9002>`
   -  :doc:`Building HDL how-to, ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`

-  :doc:`ADRV9002 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002-customization>`
-  :doc:`ADRV9002 Integrated Dual RF Transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

Software resources
------------------

-  :doc:`ADRV9002 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002-customization>`
-  :doc:`ADRV9002 Integrated Dual RF Transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`


.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
