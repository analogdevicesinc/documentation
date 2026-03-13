.. _ad_fmcdaq2_ebz quickstart microblaze:

MICROBLAZE Quickstart
=====================

This guide provides some quick instructions on how to setup the
:adi:`AD-FMCDAQ2-EBZ` on:

- :xilinx:`KCU105` on FMC HPC

.. image:: ./../images/kcu105.png
   :width: 900

.. esd-warning::

Using Linux as software
-----------------------

Necessary files
~~~~~~~~~~~~~~~

The following files are needed for the system to boot:

- HDL boot image: ``system_top.bit``
- Linux simple image: ``simpleImage.kcu105_fmcdaq2.strip``

Instructions on how to manually build the boot files from source can be found here:

- :ref:`linux-kernel microblaze`
- :external+hdl:ref:`daq2` build documentation.

More HDL build details at :external+hdl:ref:`build_hdl`.

.. shell::
   :show-user:

   $git clone https://github.com/analogdevicesinc/hdl.git
   $cd projects/daq2/kcu105
   $make
     Building daq2/kcu105
     [/home/microblaze/hdl/projects/daq2/kcu105/daq2_kcu105_vivado.log] ... OK

Required Software
~~~~~~~~~~~~~~~~~

- AMD Xilinx Vivado and Vitis (downloading Vitis from `here <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_ will include Vivado as well)
- A UART terminal (Putty/Tera Term/Minicom, etc.) with baud rate 115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~

- AMD Xilinx :xilinx:`KCU105` FPGA board and its power supply
- :adi:`AD-FMCDAQ2-EBZ` evaluation board
- 2x Micro-USB cable (UART and JTAG)
- LAN cable (Ethernet)
- (Optional) 2x SMA cable for analog signal loopback

Testing
~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^

.. image:: ./../images/ad-fmcdaq2-ebz_kcu105_setup.jpg
   :width: 900

.. caution::

    This project was tested with **VADJ = 1.8 V**

In the following example, we will make a physical loopback between the ADC and
the DAC channels on the evaluation board, using SMA cables.

#. Connect the AD-FMCDAQ2-EBZ FMC board to the FPGA carrier, on the HPC FMC
   connector.
#. Connect USB UART J4 (Micro-USB) to your host PC
#. Connect USB JTAG J87 (Micro-USB) to your host PC
#. (Optional) Connect SMA cable for analog signal loopback
#. Turn on the power switch on the FPGA board.
#. Program the FPGA using the steps shown
   :ref:`here <linux-kernel microblaze boot>`.
#. Open xsct/xsdb and run the run.tcl script.
#. Observe console output messages on your terminal (use the first ttyUSB or
   COM port registered)

We need to prepare a working directory where we will gather all the required
binary files.

From the HDL build directory locate the system_top.bit and copy it to the
working directory.

From the Linux build directory locate the simpleImage and copy it to the working
directory.

.. shell::

   $mkdir working_dir
   $cp <hdl_repo_dir>/projects/daq2/kcu105/daq2_kcu105.runs/impl_1/system_top.bit working_dir
   $cp <linux_repo_dir>/arch/microblaze/boot/simpleImage.kcu105_fmcdaq2.strip working_dir

Next step is to program the board with xsct or similar tool

.. shell::

   $xsct
   $xsct% connect
   $xsct% fpga -f system_top.bit
   $xsct% after 1000
   $xsct% target 3
   $xsct% dow simpleImage.kcu105_fmcdaq2.strip
   $xsct% after 1000
   $xsct% con
   $xsct% disconnect

Alternatively, you can run the TCL script directly:

.. code-block:: tcl

   connect
   fpga -f system_top.bit
   after 1000
   target 3
   dow simpleImage.kcu105_fmcdaq2.strip
   after 1000
   con
   disconnect

.. note::

   Login Information

   - Welcome to Buildroot
   - buildroot login: **root**, password: **analog**
   - buildroot login: **analog**, password: **analog**

.. note::

   For other obsolete carrier:
   If your FPGA carrier board (:xilinx:`KC705`, :xilinx:`VC707`,
   :xilinx:`ML605`) features a LCD display and the board is connected to a DHCP
   enabled network. You should also see its IP address printed on the display.
   This allows you to connect remote to the board as well. (ssh, libiio remote)

   Unlike shown in the picture below you won't see the second line. In case the IP
   address is 192.168.2.2, this indicates that DHCP failed and it is now using its
   default address. This address may not be within your subnet, and things
   therefore may fail.

Boot messages
^^^^^^^^^^^^^

.. collapsible:: Complete boot log

    ::

       Ramdisk addr 0x00000000,
       Compiled-in FDT at 0x8077ab50
       earlycon: uartlite_a0 at MMIO 0x40600000 (options '115200n8')
       printk: bootconsole [uartlite_a0] enabled
       cma: Reserved 512 MiB at 0x8fc00000
       Linux version 6.1.70-35308-ge2e62cc28c80 (jenkins@romlxbuild1) (microblazeel-xilinx-linux-gcc.real (GCC) 12.2.0, GNU ld (GNU Binutils) 2.39.0.20220819) #1706 Tue Sep 16 08:02:59 EEST 2025
       setup_memory: max_mapnr: 0x7ffff
       setup_memory: min_low_pfn: 0x80000
       setup_memory: max_low_pfn: 0xb0000
       setup_memory: max_pfn: 0xfffff
       Zone ranges:
       DMA      [mem 0x0000000080000000-0x00000000afffffff]
       Normal   empty
       HighMem  [mem 0x00000000b0000000-0x00000000ffffefff]
       Movable zone start for each node
       Early memory node ranges
       node   0: [mem 0x0000000080000000-0x00000000ffffefff]
       Initmem setup node 0 [mem 0x0000000080000000-0x00000000ffffefff]
       setup_cpuinfo: initialising cpu 0
       setup_cpuinfo: Using full CPU PVR support
       wt_msr_noirq
       pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
       pcpu-alloc: [0] 0
       Built 1 zonelists, mobility grouping on.  Total pages: 522751
       Kernel command line: earlycon
       Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
       Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
       mem auto-init: stack:all(zero), heap alloc:off, heap free:off
       Memory: 1535084K/2097148K available (7658K kernel code, 598K rwdata, 6064K rodata, 210K init, 166K bss, 37776K reserved, 524288K cma-reserved, 1310716K highmem)
       NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
       irq-xilinx: mismatch in kind-of-intr param
       irq-xilinx: /amba_pl/interrupt-controller@41200000: num_irq=16, sw_irq=0, edge=0xffff05f0
       xilinx_timer_init: Timer base: 0xb0002000, Clocksource base: 0xb0002010
       clocksource: xilinx_clocksource: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
       sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
       /amba_pl/timer@41c00000: irq=1, cpu_id 0
       xilinx_timer_shutdown
       xilinx_timer_set_periodic
       Calibrating delay loop... 49.35 BogoMIPS (lpj=246784)
       pid_max: default: 4096 minimum: 301
       Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
       Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
       devtmpfs: initialized
       clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
       futex hash table entries: 16 (order: -4, 448 bytes, linear)
       NET: Registered PF_NETLINK/PF_ROUTE protocol family
       DMA: preallocated 256 KiB GFP_KERNEL pool for atomic allocations
       DMA: preallocated 256 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
       gpio gpiochip0: (40000000.gpio): not an immutable chip, please consider fixing it!
       pps_core: LinuxPPS API ver. 1 registered
       pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
       PTP clock support registered
       jesd204: created con: id=0, topo=1, link=0, /amba_pl/axi-ad9144-adxcvr@44a60000 <-> /amba_pl/axi-jesd204-tx@44a90000
       jesd204: created con: id=1, topo=0, link=0, /amba_pl/axi-ad9680-adxcvr@44a50000 <-> /amba_pl/axi-jesd204-rx@44aa0000
       jesd204: created con: id=2, topo=1, link=0, /amba_pl/axi-jesd204-tx@44a90000 <-> /amba_pl/axi-ad9144-hpc@44a04000
       jesd204: created con: id=3, topo=0, link=0, /amba_pl/axi-jesd204-rx@44aa0000 <-> /amba_pl/axi-ad9680-hpc@44a10000
       jesd204: created con: id=4, topo=0, link=0, /amba_pl/axi-ad9680-hpc@44a10000 <-> /amba_pl/spi@44a70000/ad9680@2
       jesd204: created con: id=5, topo=1, link=0, /amba_pl/axi-ad9144-hpc@44a04000 <-> /amba_pl/spi@44a70000/ad9144@1
       jesd204: /amba_pl/spi@44a70000/ad9680@2: JESD204[0:0] transition uninitialized -> initialized
       jesd204: /amba_pl/spi@44a70000/ad9144@1: JESD204[1:0] transition uninitialized -> initialized
       jesd204: found 8 devices and 2 topologies
       vgaarb: loaded
       clocksource: Switched to clocksource xilinx_clocksource
       NET: Registered PF_INET protocol family
       IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
       tcp_listen_portaddr_hash hash table entries: 512 (order: 1, 10240 bytes, linear)
       Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
       TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
       TCP bind hash table entries: 8192 (order: 6, 327680 bytes, linear)
       TCP: Hash tables configured (established 8192 bind 8192)
       UDP hash table entries: 512 (order: 2, 24576 bytes, linear)
       UDP-Lite hash table entries: 512 (order: 2, 24576 bytes, linear)
       NET: Registered PF_UNIX/PF_LOCAL protocol family
       RPC: Registered named UNIX socket transport module.
       RPC: Registered udp transport module.
       RPC: Registered tcp transport module.
       RPC: Registered tcp NFSv4.1 backchannel transport module.
       PCI: CLS 0 bytes, default 32
       workingset: timestamp_bits=30 max_order=19 bucket_order=0
       Key type cifs.idmap registered
       jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
       romfs: ROMFS MTD (C) 2007 Red Hat, Inc.
       bounce: pool size: 64 pages
       io scheduler mq-deadline registered
       io scheduler kyber registered
       Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
       40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 4, base_baud = 0) is a uartlite
       printk: console [ttyUL0] enabled
       printk: bootconsole [uartlite_a0] disabled
       uartlite 41400000.serial: error -EINVAL: could not read current-speed
       uartlite: probe of 41400000.serial failed with error -22
       brd: module loaded
       SPI driver spidev has no spi_device_id for adi,swspi
       xilinx_axienet 40e00000.ethernet: TX_CSUM 2
       xilinx_axienet 40e00000.ethernet: RX_CSUM 2
       i2c_dev: i2c /dev entries driver
       i2c i2c-0: Added multiplexed i2c bus 1
       at24 2-0050: supply vcc not found, using dummy regulator
       at24 2-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
       i2c i2c-0: Added multiplexed i2c bus 2
       i2c i2c-0: Added multiplexed i2c bus 3
       i2c i2c-0: Added multiplexed i2c bus 4
       pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
       ad9523 spi0.0: supply vcc not found, using dummy regulator
       axi_adxcvr_drv 44a50000.axi-ad9680-adxcvr: AXI-ADXCVR-RX (17.05.a) using CPLL on GTH3 at 0x44A50000. Number of lanes: 4.
       axi_adxcvr_drv 44a60000.axi-ad9144-adxcvr: AXI-ADXCVR-TX (17.05.a) using QPLL on GTH3 at 0x44A60000. Number of lanes: 4.
       axi-jesd204-rx 44aa0000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x44AA0000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
       axi-jesd204-tx 44a90000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0x44A90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
       axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
       axi_sysid 45000000.axi-sysid-0: [daq2] [RX:M=2 L=4 S=1 TX:M=2 L=4 S=1 ADC_OFFLOAD:TYPE=0 SIZE=524288 DAC_OFFLOAD:TYPE=0 SIZE=1048576] on [kcu105] git branch <main> git <5da8736cb717e92a827934dd1c272b5c07c8e871> clean [2026-02-24 21:17:14] UTC
       Initializing XFRM netlink socket
       NET: Registered PF_INET6 protocol family
       Segment Routing with IPv6
       In-situ OAM (IOAM) with IPv6
       sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
       NET: Registered PF_PACKET protocol family
       NET: Registered PF_KEY protocol family
       Key type dns_resolver registered
       Key type encrypted registered
       ad9208 spi0.2: ad9680 PLL LOCKED
       ad9208 spi0.2: ad9680 Rev. 3 Grade 10 (API 1.0.1) probed
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition initialized -> probed
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition probed -> initialized
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition initialized -> probed
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition probed -> idle
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition idle -> device_init
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition device_init -> link_init
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition link_init -> link_supported
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition link_supported -> link_pre_setup
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition link_pre_setup -> clk_sync_stage1
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition clk_sync_stage1 -> clk_sync_stage2
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition clk_sync_stage2 -> clk_sync_stage3
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition clk_sync_stage3 -> link_setup
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition link_setup -> opt_setup_stage1
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition opt_setup_stage1 -> opt_setup_stage2
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition opt_setup_stage2 -> opt_setup_stage3
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition opt_setup_stage3 -> opt_setup_stage4
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition opt_setup_stage4 -> opt_setup_stage5
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition opt_setup_stage5 -> clocks_enable
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition clocks_enable -> link_enable
       ad9144 spi0.1: Link0 code grp sync: f
       ad9144 spi0.1: Link0 frame sync stat: f
       ad9144 spi0.1: Link0 good checksum stat: f
       ad9144 spi0.1: Link0 init lane_sync stat: f
       ad9144 spi0.1: Link0 4 lanes @ 10000000 kBps
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition link_enable -> link_running
       jesd204: /amba_pl/spi@44a70000/ad9144@1,jesd204:0,parent=spi0.1: JESD204[1:0] transition link_running -> opt_post_running_stage
       cf_axi_dds 44a04000.axi-ad9144-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.02.b) at 0x44A04000 mapped to 0x(ptrval), probed DDS (null)
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition initialized -> probed
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition probed -> initialized
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition initialized -> probed
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition probed -> idle
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition idle -> device_init
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition device_init -> link_init
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition link_init -> link_supported
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition link_supported -> link_pre_setup
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition clk_sync_stage3 -> link_setup
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition link_setup -> opt_setup_stage1
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_stage2
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage3
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage4
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage5
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition clocks_enable -> link_enable
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition link_enable -> link_running
       jesd204: /amba_pl/spi@44a70000/ad9680@2,jesd204:1,parent=spi0.2: JESD204[0:0] transition link_running -> opt_post_running_stage
       cf_axi_adc 44a10000.axi-ad9680-hpc: ADI AIM (10.03.) at 0x44A10000 mapped to 0x(ptrval) probed ADC AD9680 as MASTER
       Freeing unused kernel image (initmem) memory: 208K
       This architecture does not have kernel memory protection.
       Run /init as init process
         with arguments:
           /init
         with environment:
           HOME=/
           TERM=linux
       Starting syslogd: OK
       Starting klogd: OK
       Running sysctl: OK
       Saving 256 bits of non-creditable seed for next boot
       Starting network: udhcpc: started, v1.36.1
       xilinx_axienet 40e00000.ethernet eth0: PHY [axienet-40e00000:07] driver [Marvell 88E1111] (irq=POLL)
       xilinx_axienet 40e00000.ethernet eth0: configuring for phy/sgmii link mode
       random: crng init done
       udhcpc: broadcasting discover
       xilinx_axienet 40e00000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
       IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
       udhcpc: broadcasting discover
       udhcpc: broadcasting discover
       udhcpc: broadcasting select for 10.48.65.202, server 10.48.65.20
       udhcpc: lease of 10.48.65.202 obtained from 10.48.65.20, lease time 21600
       deleting routers
       adding dns 10.32.51.110
       adding dns 10.64.53.110
       Starting dropbear sshd: OK
       Starting IIO Server Daemon

Using no-OS as software
-----------------------

Necessary files
~~~~~~~~~~~~~~~

The following files are needed for the system to boot:

- HDL boot file: ``system_top.xsa``
- no-OS project: :git-no-os:`projects/fmcdaq2`
- rootfs.cpio.gz

Instructions on how to build the boot files from source can be found here:

- More no-OS build details at :external+no-OS:doc:`build_guide`.
- :external+hdl:ref:`daq2`. More HDL build details at
  :external+hdl:ref:`build_hdl`.

Required Software
~~~~~~~~~~~~~~~~~

- AMD Xilinx Vivado and Vitis (downloading Vitis from `here <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_ will include Vivado as well)
- A UART terminal (Putty/Tera Term/Minicom, etc.) with baud rate 115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~

- AMD Xilinx :xilinx:`KCU105` board
- :adi:`AD-FMCDAQ2-EBZ` evaluation board
- 2x Micro-USB cables, one for UART and one for JTAG
- LAN cable (Ethernet)
- Power supply for the FPGA carrier board
- (Optional) 2x SMA cable for analog signal loopback

Testing
~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^

.. image:: ./../images/ad-fmcdaq2-ebz_kcu105_setup.jpg
   :width: 900

.. caution::

    This project was tested with **VADJ = 1.8 V**

Follow the steps in this order, to avoid damaging the components:

#. Connect the AD-FMCDAQ2-EBZ FMC board to the FPGA carrier, on the HPC FMC
   connector.
#. Connect USB UART J4 (Micro-USB) to your host PC
#. Connect USB JTAG J87 (Micro-USB) to your host PC
#. (Optional) Connect the SMA cable for analog signal loopback
#. Turn on the power switch on the FPGA board.
#. Build and run the project using the steps shown
   :external+no-OS:doc:`here <projects/rf-transceiver/ad9371>`.
#. Open xsct/xsdb and run the run.tcl script.
#. Observe console output messages on your terminal (use the first ttyUSB or
   COM port registered)

Console output
^^^^^^^^^^^^^^

The following is what is printed in the serial console, after you have connected
to the proper ttyUSB or COM port:

.. collapsible:: Complete boot log

   ::

       Available sampling rates:
      	1 - ADC 1000 MSPS; DAC 1000 MSPS
      	2 - ADC  500 MSPS; DAC 1000 MSPS
      	3 - ADC  500 MSPS; DAC  500 MSPS
      	4 - ADC  600 MSPS; DAC  600 MSPS
      	5 - ADC 1000 MSPS; DAC 2000 MSPS (2x interpolation)
      choose an option [default 1]:
      4 - ADC  600 MSPS; DAC  600 MSPS
      ad9144_xcvr: OK (6000000 kHz)
      ad9680_xcvr: OK (6000000 kHz)
      ad9680_adc: Successfully initialized (599981689 Hz)
      ad9144_dac: Successfully initialized (599987792 Hz)
      ad9680_xcvr: OK (6000000 kHz)
      ad9144_xcvr: OK (6000000 kHz)
      Link0 code grp sync: f
      Link0 frame sync stat: f
      Link0 good checksum stat: f
      Link0 init lane_sync stat: f
      Link0 4 lanes @ 6000000 kBps
      ad9680_jesd status:
      	Link is enabled
      	Measured Link Clock: 149.997 MHz
      	Reported Link Clock: 150.000 MHz
      	Lane rate: 6000.000 MHz
      	Lane rate / 40: 150.000 MHz
      	LMFC rate: 18.750 MHz
      	Link status: DATA
      	SYSREF captured: Yes
      	SYSREF alignment error: No
      ad9144_jesd status:
      	Link is enabled
      	Measured Link Clock: 149.997 MHz
      	Reported Link Clock: 150.000 MHz
      	Lane rate: 6000.000 MHz
      	Lane rate / 40: 150.000 MHz
      	LMFC rate: 18.750 MHz
      	SYNC~: deasserted
      	Link status: DATA
      	SYSREF captured: Yes
      	SYSREF alignment error: No
       [ --snip-- ]
       522       |    0x0bb4   |    0x013f    |
        523       |    0x0c19   |    0x029e    |
        524       |    0x0b12   |    0x03fe    |
        525       |    0x08bc   |    0x0553    |
        526       |    0x0558   |    0x0694    |
        527       |    0x0160   |    0x07b9    |
        528       |    0xfd32   |    0x08be    |
        529       |    0xf95d   |    0x09b6    |
        530       |    0xf654   |    0x0a86    |
        531       |    0xf473   |    0x0b2c    |
        532       |    0xf3ec   |    0x0bb5    |
        533       |    0xf4d9   |    0x0c0e    |
        534       |    0xf70a   |    0x0c4d    |
        535       |    0xfa54   |    0x0c57    |
        536       |    0xfe4e   |    0x0c37    |
        537       |    0x0274   |    0x0bee    |
        538       |    0x065d   |    0x0b80    |
        539       |    0x0973   |    0x0ae0    |
        540       |    0x0b7c   |    0x0a2e    |
        541       |    0x0c25   |    0x0951    |
        542       |    0x0b5b   |    0x084c    |
        543       |    0x093f   |    0x0734    |
        544       |    0x0606   |    0x0602    |
        545       |    0x0224   |    0x04b8    |
        546       |    0xfdf2   |    0x0362    |
        547       |    0xfa04   |    0x0201    |
        548       |    0xf6ca   |    0x009e    |
        549       |    0xf4af   |    0xff35    |
        550       |    0xf3e7   |    0xfdca    |
        551       |    0xf48a   |    0xfc66    |
        552       |    0xf689   |    0xfb13    |
        553       |    0xf9ae   |    0xf9cc    |
        554       |    0xfd8b   |    0xf8a1    |
        555       |    0x01be   |    0xf78a    |
        556       |    0x05b3   |    0xf692    |
        557       |    0x08fd   |    0xf5bd    |
        558       |    0x0b37   |    0xf504    |
        559       |    0x0c1e   |    0xf476    |
        560       |    0x0b97   |    0xf40c    |
        561       |    0x09b7   |    0xf3cc    |
        562       |    0x06ac   |    0xf3b0    |
        563       |    0x02d2   |    0xf3c2    |
        564       |    0xfeae   |    0xf3fe    |
        565       |    0xfaac   |    0xf466    |
        566       |    0xf74c   |    0xf4f1    |
        567       |    0xf4f9   |    0xf59d    |
        568       |    0xf3f3   |    0xf67a    |
        569       |    0xf454   |    0xf76c    |
        570       |    0xf619   |    0xf87f    |
        571       |    0xf90a   |    0xf9a4    |
        572       |    0xfcd0   |    0xfae8    |
        573       |    0x0101   |    0xfc3c    |
        574       |    0x0502   |    0xfd9a    |
        575       |    0x0877   |    0xff05    |
        576       |    0x0ae7   |    0x006f    |
        577       |    0x0c11   |    0x01d6    |
        578       |    0x0bce   |    0x0337    |
        579       |    0x0a21   |    0x0496    |
        580       |    0x074a   |    0x05e1    |
        581       |    0x0392   |    0x070f    |
        582       |    0xff6e   |    0x082c    |
        583       |    0xfb60   |    0x092a    |
        584       |    0xf7d4   |    0x0a12    |
        585       |    0xf54f   |    0x0ad2    |
        586       |    0xf405   |    0x0b6d    |
        587       |    0xf42a   |    0x0bdf    |
        588       |    0xf5b5   |    0x0c2c    |
        589       |    0xf873   |    0x0c50    |
        590       |    0xfc20   |    0x0c50    |
        591       |    0x003a   |    0x0c19    |
        592       |    0x0450   |    0x0bbf    |
        593       |    0x07ed   |    0x0b44    |
        594       |    0x0a8a   |    0x0a99    |
        595       |    0x0bf5   |    0x09ce    |
        596       |    0x0bf6   |    0x08df    |
        597       |    0x0a86   |    0x07de    |
        598       |    0x07e2   |    0x06b3    |
        599       |    0x044c   |    0x0578    |
        600       |    0x0030   |    0x042c    |
        601       |    0xfc13   |    0x02cc    |
        602       |    0xf86d   |    0x0162    |
        603       |    0xf5a7   |    0xfffe    |
        604       |    0xf424   |    0xfe96    |
        605       |    0xf406   |    0xfd2f    |
        606       |    0xf556   |    0xfbd2    |
        607       |    0xf7e6   |    0xfa88    |
        608       |    0xfb6b   |    0xf94b    |
        609       |    0xff79   |    0xf828    |
        610       |    0x039b   |    0xf71f    |
        611       |    0x0753   |    0xf637    |
        612       |    0x0a2c   |    0xf568    |
        613       |    0x0bd0   |    0xf4c5    |
        614       |    0x0c0b   |    0xf443    |
        615       |    0x0ae4   |    0xf3e9    |
        616       |    0x086d   |    0xf3ba    |
        617       |    0x04fb   |    0xf3b9    |
        618       |    0x00ec   |    0xf3d8    |
        619       |    0xfcc9   |    0xf429    |
        620       |    0xf900   |    0xf4a1    |
        621       |    0xf615   |    0xf53d    |
        622       |    0xf452   |    0xf5fa    |
        623       |    0xf3f3   |    0xf6e0    |
        624       |    0xf500   |    0xf7dd    |
        625       |    0xf758   |    0xf901    |
        626       |    0xfabc   |    0xfa33    |
        627       |    0xfebd   |    0xfb79    |
        628       |    0x02e5   |    0xfcd6    |
        629       |    0x06b7   |    0xfe3b    |
        630       |    0x09be   |    0xffa2    |
        631       |    0x0b9e   |    0x010a    |
        632       |    0x0c1f   |    0x0273    |
        633       |    0x0b32   |    0x03d3    |
        634       |    0x08f2   |    0x0522    |
        635       |    0x05a4   |    0x0666    |
        636       |    0x01ae   |    0x0790    |
        637       |    0xfd82   |    0x089f    |
        638       |    0xf9a6   |    0x0992    |
        639       |    0xf684   |    0x0a6b    |
        640       |    0xf48b   |    0x0b1d    |
        641       |    0xf3e8   |    0x0ba5    |
        642       |    0xf4b3   |    0x0c0a    |
        643       |    0xf6d5   |    0x0c3e    |
        644       |    0xfa0e   |    0x0c55    |
        645       |    0xfe01   |    0x0c3d    |
        646       |    0x022a   |    0x0bf9    |
        647       |    0x0614   |    0x0b87    |
        648       |    0x0947   |    0x0aff    |
        649       |    0x0b61   |    0x0a40    |
        650       |    0x0c24   |    0x096c    |
        651       |    0x0b72   |    0x0873    |
        652       |    0x0972   |    0x075d    |
        653       |    0x0649   |    0x0632    |
        654       |    0x026f   |    0x04ea    |
        655       |    0xfe42   |    0x0395    |
        656       |    0xfa4b   |    0x0234    |
        657       |    0xf703   |    0x00d0    |
        658       |    0xf4cd   |    0xff62    |
        659       |    0xf3e8   |    0xfdf6    |
        660       |    0xf471   |    0xfc99    |
        661       |    0xf65e   |    0xfb3e    |
        662       |    0xf96b   |    0xf9f9    |
        663       |    0xfd40   |    0xf8c8    |
        664       |    0x016c   |    0xf7b0    |
        665       |    0x056c   |    0xf6b6    |
        666       |    0x08c8   |    0xf5ce    |
        667       |    0x0b16   |    0xf51d    |
        668       |    0x0c1c   |    0xf487    |
        669       |    0x0baf   |    0xf415    |
        670       |    0x09e6   |    0xf3d1    |
        671       |    0x06ef   |    0xf3b5    |
        672       |    0x0324   |    0xf3c1    |
        673       |    0xfefe   |    0xf3f7    |
        674       |    0xfaf8   |    0xf459    |
        675       |    0xf783   |    0xf4de    |
        676       |    0xf51a   |    0xf588    |
        677       |    0xf3f5   |    0xf654    |
        678       |    0xf443   |    0xf74d    |
        679       |    0xf5e8   |    0xf857    |
        680       |    0xf8cf   |    0xf980    |
        681       |    0xfc88   |    0xfab7    |
        682       |    0x00ac   |    0xfc0e    |
        683       |    0x04b8   |    0xfd6e    |
        684       |    0x0842   |    0xfecd    |
        685       |    0x0ac4   |    0x0040    |
        686       |    0x0c08   |    0x01aa    |
        687       |    0x0be0   |    0x030a    |
        688       |    0x0a4c   |    0x046b    |
        689       |    0x0789   |    0x05b0    |
        690       |    0x03da   |    0x06e6    |
        691       |    0xffc0   |    0x0809    |
        692       |    0xfba8   |    0x090f    |
        693       |    0xf814   |    0x09f6    |
        694       |    0xf572   |    0x0ab9    |
        695       |    0xf412   |    0x0b56    |
        696       |    0xf418   |    0x0bd1    |
        697       |    0xf587   |    0x0c2a    |
        698       |    0xf836   |    0x0c50    |
        699       |    0xfbd2   |    0x0c4b    |
        700       |    0xffeb   |    0x0c25    |
        701       |    0x0407   |    0x0bd0    |
        702       |    0x07ab   |    0x0b55    |
        703       |    0x0a66   |    0x0ab4    |
        704       |    0x0be6   |    0x09ed    |
        705       |    0x0c00   |    0x0909    |
        706       |    0x0ab2   |    0x0803    |
        707       |    0x081d   |    0x06e0    |
        708       |    0x048f   |    0x05a5    |
        709       |    0x007f   |    0x045b    |
        710       |    0xfc5b   |    0x02f9    |
        711       |    0xf8aa   |    0x0195    |
        712       |    0xf5d1   |    0x0032    |
        713       |    0xf439   |    0xfec4    |
        714       |    0xf3fc   |    0xfd60    |
        715       |    0xf532   |    0xfc05    |
        716       |    0xf7a6   |    0xfab2    |
        717       |    0xfb1c   |    0xf970    |
        718       |    0xff2c   |    0xf84e    |
        719       |    0x0348   |    0xf740    |
        720       |    0x0716   |    0xf654    |
        721       |    0x0a00   |    0xf581    |
        722       |    0x0bbf   |    0xf4d7    |
        723       |    0x0c1a   |    0xf44e    |
        724       |    0x0b02   |    0xf3f4    |
        725       |    0x08a7   |    0xf3bf    |
        726       |    0x0540   |    0xf3b6    |
        727       |    0x013e   |    0xf3d5    |
        728       |    0xfd14   |    0xf416    |
        729       |    0xf947   |    0xf48a    |
        730       |    0xf646   |    0xf523    |
        731       |    0xf46c   |    0xf5de    |
        732       |    0xf3eb   |    0xf6b9    |
        733       |    0xf4df   |    0xf7b9    |
        734       |    0xf71e   |    0xf8d5    |
        735       |    0xfa6e   |    0xfa09    |
        736       |    0xfe69   |    0xfb52    |
        737       |    0x0296   |    0xfca4    |
        738       |    0x066f   |    0xfe08    |
        739       |    0x098d   |    0xff6a    |
        740       |    0x0b89   |    0x00db    |
        741       |    0x0c25   |    0x0241    |
        742       |    0x0b4d   |    0x039d    |
        743       |    0x092d   |    0x04f8    |
        744       |    0x05e8   |    0x063b    |
        745       |    0x01f9   |    0x0768    |
        746       |    0xfdd3   |    0x087f    |
        747       |    0xf9ea   |    0x0978    |
        748       |    0xf6b7   |    0x0a4d    |
        749       |    0xf4a3   |    0x0b09    |
        750       |    0xf3ea   |    0x0b93    |
        751       |    0xf497   |    0x0c00    |
        752       |    0xf6a9   |    0x0c3d    |
        753       |    0xf9c7   |    0x0c55    |
        754       |    0xfdad   |    0x0c41    |
        755       |    0x01da   |    0x0c07    |
        756       |    0x05cb   |    0x0b9e    |
        757       |    0x090e   |    0x0b14    |
        758       |    0x0b3e   |    0x0a62    |
        759       |    0x0c21   |    0x098a    |
        760       |    0x0b91   |    0x0899    |
        761       |    0x09a2   |    0x0787    |
        762       |    0x0697   |    0x0658    |
        763       |    0x02ba   |    0x0517    |
        764       |    0xfe93   |    0x03c7    |
        765       |    0xfa93   |    0x0268    |
        766       |    0xf737   |    0x00fc    |
        767       |    0xf4f3   |    0xff95    |
        768       |    0xf3f2   |    0xfe29    |
        769       |    0xf45a   |    0xfcc7    |
        770       |    0xf629   |    0xfb71    |
        771       |    0xf928   |    0xfa22    |
        772       |    0xfcef   |    0xf8f1    |
        773       |    0x0117   |    0xf7d1    |
        774       |    0x0520   |    0xf6d7    |
        775       |    0x088b   |    0xf5ee    |
        776       |    0x0af3   |    0xf533    |
        777       |    0x0c13   |    0xf496    |
        778       |    0x0bc5   |    0xf423    |
        779       |    0x0a14   |    0xf3d8    |
        780       |    0x0734   |    0xf3b4    |
        781       |    0x0374   |    0xf3bb    |
        782       |    0xff54   |    0xf3ee    |
        783       |    0xfb42   |    0xf44a    |
        784       |    0xf7c1   |    0xf4cc    |
        785       |    0xf542   |    0xf56d    |
        786       |    0xf402   |    0xf639    |
        787       |    0xf42d   |    0xf72a    |
        788       |    0xf5c4   |    0xf82d    |
        789       |    0xf88f   |    0xf957    |
        790       |    0xfc3c   |    0xfa91    |
        791       |    0x005e   |    0xfbde    |
        792       |    0x046d   |    0xfd3d    |
        793       |    0x0801   |    0xfea2    |
        794       |    0x0a96   |    0x000e    |
        795       |    0x0c00   |    0x0175    |
        796       |    0x0bee   |    0x02da    |
        797       |    0x0a7d   |    0x0437    |
        798       |    0x07cb   |    0x0586    |
        799       |    0x042a   |    0x06c2    |
        800       |    0x0010   |    0x07df    |
        801       |    0xfbf5   |    0x08ea    |
        802       |    0xf853   |    0x09d4    |
        803       |    0xf59e   |    0x0aa5    |
        804       |    0xf41f   |    0x0b4b    |
        805       |    0xf407   |    0x0bc7    |
        806       |    0xf563   |    0x0c1a    |
        807       |    0xf7fa   |    0x0c4b    |
        808       |    0xfb85   |    0x0c51    |
        809       |    0xff9d   |    0x0c2d    |
        810       |    0x03b9   |    0x0bde    |
        811       |    0x076b   |    0x0b6b    |
        812       |    0x0a3d   |    0x0acc    |
        813       |    0x0bd4   |    0x0a09    |
        814       |    0x0c0a   |    0x0927    |
        815       |    0x0ad4   |    0x081e    |
        816       |    0x0859   |    0x0705    |
        817       |    0x04de   |    0x05cf    |
        818       |    0x00cd   |    0x0488    |
        819       |    0xfcad   |    0x032e    |
        820       |    0xf8f0   |    0x01d0    |
        821       |    0xf605   |    0x0063    |
        822       |    0xf447   |    0xfef6    |
        823       |    0xf3f4   |    0xfd8d    |
        824       |    0xf50e   |    0xfc2e    |
        825       |    0xf76d   |    0xfadc    |
        826       |    0xfad3   |    0xf9a3    |
        827       |    0xfed7   |    0xf875    |
        828       |    0x0304   |    0xf765    |
        829       |    0x06d0   |    0xf66d    |
        830       |    0x09d3   |    0xf59a    |
        831       |    0x0ba8   |    0xf4ec    |
        832       |    0x0c1b   |    0xf45e    |
        833       |    0x0b28   |    0xf3fe    |
        834       |    0x08e4   |    0xf3c8    |
        835       |    0x0587   |    0xf3b4    |
        836       |    0x0191   |    0xf3cc    |
        837       |    0xfd62   |    0xf413    |
        838       |    0xf991   |    0xf479    |
        839       |    0xf671   |    0xf510    |
        840       |    0xf480   |    0xf5c0    |
        841       |    0xf3ef   |    0xf69e    |
        842       |    0xf4be   |    0xf794    |
        843       |    0xf6ef   |    0xf8ac    |
        844       |    0xfa24   |    0xf9dc    |
        845       |    0xfe1a   |    0xfb23    |
        846       |    0x0247   |    0xfc71    |
        847       |    0x062f   |    0xfddb    |
        848       |    0x095b   |    0xff3b    |
        849       |    0x0b69   |    0x00aa    |
        850       |    0x0c21   |    0x020e    |
        851       |    0x0b6c   |    0x0376    |
        852       |    0x0960   |    0x04c4    |
        853       |    0x0635   |    0x0611    |
        854       |    0x024d   |    0x0743    |
        855       |    0xfe17   |    0x085a    |
        856       |    0xfa31   |    0x0955    |
        857       |    0xf6ea   |    0x0a32    |
        858       |    0xf4c2   |    0x0aef    |
        859       |    0xf3eb   |    0x0b85    |
        860       |    0xf47f   |    0x0bef    |
        861       |    0xf66f   |    0x0c37    |
        862       |    0xf985   |    0x0c54    |
        863       |    0xfd5d   |    0x0c49    |
        864       |    0x018a   |    0x0c11    |
        865       |    0x0586   |    0x0bb1    |
        866       |    0x08e0   |    0x0b23    |
        867       |    0x0b27   |    0x0a7a    |
        868       |    0x0c23   |    0x09a9    |
        869       |    0x0baa   |    0x08b9    |
        870       |    0x09d5   |    0x07aa    |
        871       |    0x06d7   |    0x0682    |
        872       |    0x030e   |    0x0541    |
        873       |    0xfedf   |    0x03f0    |
        874       |    0xfada   |    0x029a    |
        875       |    0xf772   |    0x012f    |
        876       |    0xf511   |    0xffc6    |
        877       |    0xf3f5   |    0xfe5e    |
        878       |    0xf44c   |    0xfcf4    |
        879       |    0xf5fc   |    0xfb9c    |
        880       |    0xf8e8   |    0xfa55    |
        881       |    0xfca7   |    0xf91d    |
        882       |    0x00cf   |    0xf7f6    |
        883       |    0x04d5   |    0xf6f3    |
        884       |    0x0855   |    0xf607    |
        885       |    0x0ad4   |    0xf54f    |
        886       |    0x0c0f   |    0xf4ac    |
        887       |    0x0bda   |    0xf431    |
        888       |    0x0a3f   |    0xf3da    |
        889       |    0x076e   |    0xf3b4    |
        890       |    0x03c2   |    0xf3b8    |
        891       |    0xff9b   |    0xf3e9    |
        892       |    0xfb8b   |    0xf439    |
        893       |    0xf7f9   |    0xf4b3    |
        894       |    0xf564   |    0xf559    |
        895       |    0xf410   |    0xf61a    |
        896       |    0xf422   |    0xf704    |
        897       |    0xf59a   |    0xf810    |
        898       |    0xf850   |    0xf92e    |
        899       |    0xfbf0   |    0xfa68    |
        900       |    0x0007   |    0xfbae    |
        901       |    0x041f   |    0xfd0d    |
        902       |    0x07c3   |    0xfe73    |
        903       |    0x0a77   |    0xffdc    |
        904       |    0x0bef   |    0x0143    |
        905       |    0x0bf7   |    0x02aa    |
        906       |    0x0aa6   |    0x040e    |
        907       |    0x0804   |    0x0556    |
        908       |    0x0473   |    0x0698    |
        909       |    0x0060   |    0x07be    |
        910       |    0xfc41   |    0x08cb    |
        911       |    0xf88d   |    0x09ba    |
        912       |    0xf5c2   |    0x0a8d    |
        913       |    0xf42e   |    0x0b35    |
        914       |    0xf3fd   |    0x0bbb    |
        915       |    0xf53e   |    0x0c16    |
        916       |    0xf7c6   |    0x0c4e    |
        917       |    0xfb3d   |    0x0c52    |
        918       |    0xff4b   |    0x0c2f    |
        919       |    0x0368   |    0x0be9    |
        920       |    0x0728   |    0x0b7c    |
        921       |    0x0a17   |    0x0ae4    |
        922       |    0x0bc4   |    0x0a27    |
        923       |    0x0c13   |    0x0943    |
        924       |    0x0afa   |    0x084a    |
        925       |    0x0893   |    0x072d    |
        926       |    0x0524   |    0x05fc    |
        927       |    0x0124   |    0x04b2    |
        928       |    0xfcf6   |    0x035e    |
        929       |    0xf931   |    0x01fd    |
        930       |    0xf62e   |    0x0090    |
        931       |    0xf45d   |    0xff2a    |
        932       |    0xf3ee   |    0xfdc0    |
        933       |    0xf4f0   |    0xfc5e    |
        934       |    0xf730   |    0xfb0a    |
        935       |    0xfa8f   |    0xf9c4    |
        936       |    0xfe87   |    0xf896    |
        937       |    0x02b3   |    0xf785    |
        938       |    0x068d   |    0xf68e    |
        939       |    0x099d   |    0xf5b7    |
        940       |    0x0b8f   |    0xf501    |
        941       |    0x0c21   |    0xf46f    |
        942       |    0x0b42   |    0xf406    |
        943       |    0x0915   |    0xf3c7    |
        944       |    0x05d8   |    0xf3ae    |
        945       |    0x01de   |    0xf3ca    |
        946       |    0xfdb4   |    0xf404    |
        947       |    0xf9ce   |    0xf46b    |
        948       |    0xf6a3   |    0xf4f5    |
        949       |    0xf49a   |    0xf5a8    |
        950       |    0xf3e4   |    0xf67f    |
        951       |    0xf49e   |    0xf76f    |
        952       |    0xf6b4   |    0xf886    |
        953       |    0xf9e6   |    0xf9b3    |
        954       |    0xfdc9   |    0xfaf5    |
        955       |    0x01f7   |    0xfc4c    |
        956       |    0x05e9   |    0xfda8    |
        957       |    0x0926   |    0xff11    |
        958       |    0x0b4f   |    0x007a    |
        959       |    0x0c22   |    0x01e2    |
        960       |    0x0b8c   |    0x0347    |
        961       |    0x0990   |    0x049d    |
        962       |    0x0676   |    0x05e9    |
        963       |    0x029d   |    0x0718    |
        964       |    0xfe6c   |    0x0838    |
        965       |    0xfa78   |    0x0937    |
        966       |    0xf71d   |    0x0a17    |
        967       |    0xf4e4   |    0x0ad3    |
        968       |    0xf3eb   |    0x0b6c    |
        969       |    0xf463   |    0x0be7    |
        970       |    0xf63d   |    0x0c2f    |
        971       |    0xf944   |    0x0c50    |
        972       |    0xfd0d   |    0x0c46    |
        973       |    0x0137   |    0x0c1c    |
        974       |    0x0542   |    0x0bbe    |
        975       |    0x08a3   |    0x0b3b    |
        976       |    0x0b01   |    0x0a96    |
        977       |    0x0c14   |    0x09c4    |
        978       |    0x0bbe   |    0x08d7    |
        979       |    0x0a01   |    0x07d2    |
        980       |    0x0719   |    0x06af    |
        981       |    0x0353   |    0x0572    |
        982       |    0xff31   |    0x0420    |
        983       |    0xfb20   |    0x02c8    |
        984       |    0xf7ac   |    0x015f    |
        985       |    0xf533   |    0xfff7    |
        986       |    0xf3fb   |    0xfe87    |
        987       |    0xf431   |    0xfd28    |
        988       |    0xf5d4   |    0xfbcb    |
        989       |    0xf8a5   |    0xfa7e    |
        990       |    0xfc54   |    0xf941    |
        991       |    0x007a   |    0xf81d    |
        992       |    0x048b   |    0xf718    |
        993       |    0x0816   |    0xf62d    |
        994       |    0x0aaa   |    0xf563    |
        995       |    0x0c01   |    0xf4bb    |
        996       |    0x0be8   |    0xf43d    |
        997       |    0x0a6b   |    0xf3eb    |
        998       |    0x07b2   |    0xf3bb    |
        999       |    0x0409   |    0xf3b7    |
       1000       |    0xffee   |    0xf3da    |
       1001       |    0xfbd2   |    0xf42d    |
       1002       |    0xf83a   |    0xf49f    |
       1003       |    0xf586   |    0xf53e    |
       1004       |    0xf418   |    0xf604    |
       1005       |    0xf40b   |    0xf6e4    |
       1006       |    0xf56d   |    0xf7e8    |
       1007       |    0xf813   |    0xf905    |
       1008       |    0xfba4   |    0xfa3e    |
       1009       |    0xffb6   |    0xfb83    |
       1010       |    0x03d6   |    0xfcdb    |
       1011       |    0x0782   |    0xfe40    |
       1012       |    0x0a45   |    0xffaa    |
       1013       |    0x0be2   |    0x0114    |
       1014       |    0x0c0e   |    0x0279    |
       1015       |    0x0ac6   |    0x03db    |
       1016       |    0x0841   |    0x0527    |
       1017       |    0x04bc   |    0x066e    |
       1018       |    0x00b4   |    0x0795    |
       1019       |    0xfc8b   |    0x08a9    |
       1020       |    0xf8ce   |    0x099d    |
       1021       |    0xf5f2   |    0x0a6e    |
       1022       |    0xf443   |    0x0b1d    |
      Running IIOD server...
      If successful, you may connect an IIO client application by:
      1. Disconnecting the serial terminal you use to view this message.
      2. Connecting the IIO client application using the serial backend configured as shown:
      Baudrate: 115200
      Data size: 8 bits
      Parity: none
      Stop bits: 1
      Flow control: none

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~

After booting process is complete, you can open IIO-Oscilloscope. Learn more
about it :ref:`here <iio-oscilloscope>`. You can interact with
the IIO-Osc GUI either directly or over the network.

#. Once the application is launched go to Settings then Connect and enter the IP
   address of the target in the popup window.

   .. image:: ./../images/ad-fmcdaq2-ebz_kcu105_iio_osc.png
        :width: 900

#. Captured Loopback Signal Time Domain

   .. image::  ./../images/ad-fmcdaq2-ebz_kcu105_time_domain.png
        :width: 900

#. Captured Loopback Signal Frequency Domain

   .. image:: ./../images/ad-fmcdaq2-ebz_kcu105_frequency_domain.png
        :width: 900
