AD-FMCDAQ2-EBZ Arria 10 GX Quick Start Guide
============================================

|

.. warning::

   \ **NOTE:**

   | Support for the A10GX carrier is discontinued and will not be supported in future releases. Last pre-build images can be found at :doc:`Nios2 Linux on the Altera FPGA Development Boards </wiki-migration/resources/tools-software/linux-drivers/platforms/nios2>` page.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/arria10-fpga_daq2.jpg
   :alt: arria10-fpga_daq2.jpg
   :align: center
   :width: 330px

This guide provides some quick instructions on how to setup the AD-FMCDAQ2-EBZ on `A10GX <https://www.intel.com/en:products:details:fpga:development-kits:arria:10-gx>`_

Prerequisites
-------------

Required Hardware
~~~~~~~~~~~~~~~~~

-  `A10GX <https://www.intel.com/en:products:details:fpga:development-kits:arria:10-gx>`_ board
-  :adi:`AD-FMCDAQ2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcdaq2-ebz.html>` FMC board
-  Ethernet cable
-  Micro-USB cable

Required Software
~~~~~~~~~~~~~~~~~

-  You need a Host PC (Windows)
-  Intel Quartus 21.2
-  Bitfile and Linux ELF image
-  IIO Scope `Download <https://wiki.analog.com/https/github.com/analogdevicesinc/iio-oscilloscope/releases>`_

.. tip::

   \ :doc:`Pre-build Images for Intel Arria 10 GX. </wiki-migration/resources/tools-software/linux-drivers/platforms/nios2>`\


Setting up the hardware (A10GX)
-------------------------------

You will need to:


|arria10-fpga-kit.jpg|

::

   -Get the [[https://www.intel.com/en:products:details:fpga:development-kits:arria:10-gx|A10GX]] board.
   -Connect the AD-FMCDAQ2-EBZ FMC board to the FPGA carrier **FMC1** socket(J1).
   -Connect the USB JTAG J3 (Micro USB) to your Host PC.
   -Connect the Ethernet cable.
   -Plug the Power Supply into 12V Power input connector (DC Input).
   -Turn it on.


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


Programming the FPGA
--------------------

Nios II Command Shell is used to program the FPGA. To run Nios II Command Shell navigate to C:\\intelFPGA_pro\\21.2\\nios2eds and start Nios II Command Shell.bat. Windows Subsystem for Linux (WSL) needs to be installed in order to run Nios II Command Shell.

After starting the Command Shell, navigate to the path where the pre-build images are saved. For example:

::

   ceshu@LADACE-L02:/mnt/c/intelFPGA_pro/21.2/nios2eds$ cd /mnt/c/Users/ladace/Downloads/a10gx_daq2_2019_r2/

Programming FPGA bitfiled image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To flash the bitfield pre-build image, **nios2-configure-sof** command is used. For example:

::

   ceshu@LADACE-L02:/mnt/c/Users/ladace/Downloads/a10gx_daq2_2019_r2$ nios2-configure-sof daq2_a10gx.sof
   Searching for SOF file:
   in .
     daq2_a10gx.sof

   Info: *******************************************************************
   Info: Running Quartus Prime Programmer
   Info: Command: quartus_pgm --no_banner --mode=jtag -o p;./daq2_a10gx.sof
   Info (213045): Using programming cable "USB-BlasterII [USB-1]"
   Info (213011): Using programming file ./daq2_a10gx.sof with checksum 0x312984DD for device 10AX115S2F45@1
   Info (209060): Started Programmer operation at Thu Dec  9 15:10:50 2021
   Info (209016): Configuring device index 1
   Info (209017): Device 1 contains JTAG ID code 0x02E060DD
   Info (209007): Configuration succeeded -- 1 device(s) configured
   Info (209011): Successfully performed operation(s)
   Info (209061): Ended Programmer operation at Thu Dec  9 15:11:05 2021
   Info: Quartus Prime Programmer was successful. 0 errors, 0 warnings
       Info: Peak virtual memory: 1829 megabytes
       Info: Processing ended: Thu Dec  9 15:11:05 2021
       Info: Elapsed time: 00:00:22
       Info: System process ID: 20500

Programming Linux image
~~~~~~~~~~~~~~~~~~~~~~~

To flash the Linux pre-build image, **nios2-download** command is used. For example:

::

   ceshu@LADACE-L02:/mnt/c/Users/ladace/Downloads/a10gx_daq2_2019_r2$ nios2-download -g zImage
   Using cable "USB-BlasterII [USB-1]", device 1, instance 0x00
   Pausing target processor: OK
   Initializing CPU cache (if present)
   OK
   Downloaded 5468KB in 6.1s (896.3KB/s)
   Verified OK
   Starting processor at address 0xC4000000

Nios II Terminal
~~~~~~~~~~~~~~~~

To start the Nios II Terminal use the following **nios2-terminal.exe** command. Example of console: 

.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   ::
   
      ceshu@LADACE-L02:/mnt/c/Users/ladace/Downloads/a10gx_daq2_2019_r2$ nios2-terminal.exe
      nios2-terminal: connected to hardware target using JTAG UART on cable
      nios2-terminal: "USB-BlasterII [USB-1]", device 1, instance 0
      nios2-terminal: (Use the IDE stop button or Ctrl-C to terminate)
   
      Linux version 4.19.0-g17f4223 (jenkins@romlxbuild1.adlk.analog.com) (gcc version 8.3.1 20190416 (Altera 19.3 Build 222))
       #1874 Tue Jul 27 14:44:52 IST 2021
      On node 0 totalpages: 65536
        Normal zone: 512 pages used for memmap
        Normal zone: 0 pages reserved
        Normal zone: 65536 pages, LIFO batch:15
      pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
      pcpu-alloc: [0] 0
      Built 1 zonelists, mobility grouping on.  Total pages: 65024
      Kernel command line: debug console=ttyJ0,115200
      Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
      Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
      Sorting __ex_table...
      Memory: 247936K/262144K available (3795K kernel code, 465K rwdata, 4372K rodata, 3156K init, 106K bss, 14208K reserved,
      0K cma-reserved)
      NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      clocksource: nios2-clksrc: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
      pid_max: default: 32768 minimum: 301
      Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
      Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
      devtmpfs: initialized
      random: get_random_u32 called from bucket_table_alloc.isra.6+0x98/0x1e8 with crng_init=0
      clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      futex hash table entries: 256 (order: -1, 3072 bytes)
      NET: Registered protocol family 16
      jesd204: found 0 devices and 0 topologies
      clocksource: Switched to clocksource nios2-clksrc
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
      random: fast init done
      workingset: timestamp_bits=30 max_order=16 bucket_order=0
      jffs2: version 2.2. (NAND) ┬⌐ 2001-2006 Red Hat, Inc.
      Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
      io scheduler noop registered
      io scheduler deadline registered
      io scheduler cfq registered (default)
      io scheduler mq-deadline registered
      io scheduler kyber registered
      101814f0.serial: ttyJ0 at MMIO 0x101814f0 (irq = 2, base_baud = 0) is a Altera JTAG UART
      console [ttyJ0] enabled
      loop: module loaded
      spi_altera 10181400.spi: base (ptrval), irq 8
      libphy: Fixed MDIO Bus: probed
      libphy: altera_tse: probed
      altera_tse 10181000.ethernet (unnamed net_device) (uninitialized): MDIO bus altera_tse-0: created
      altera_tse 10181000.ethernet: Altera TSE MAC version 19.3 at 0x10181000 irq 1/3
      ad9680 spi0.2: Unrecognized CHIP_ID 0x0
      iio iio:device0: SPI Read Verify failed (0x0)
      ad9523: probe of spi0.0 failed with error -5
      ad9144 spi0.1: Unrecognized CHIP_ID 0xFF00 and CHIP_GRADE 0x0
      NET: Registered protocol family 17
      Freeing unused kernel memory: 3156K
      This architecture does not have kernel memory protection.
      Run /init as init process
      Starting logging: OK
      Initializing random number generator... random: dd: uninitialized urandom read (512 bytes read)
      done.
      Starting network: OK
      altera_tse 10181000.ethernet eth0: device MAC address b2:94:3d:6e:11:8f
      altera_tse 10181000.ethernet eth0: TSE revision 1303
      altera_tse 10181000.ethernet eth0: PCS PHY ID: 0x00000000
      altera_tse 10181000.ethernet eth0: SGMII PCS block initialised OK
      altera_tse 10181000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
      Network cable is plugged
      udhcpc: started, v1.25.0
      udhcpc: sending discover
      udhcpc: sending select for 10.48.65.150
      udhcpc: lease of 10.48.65.150 obtained, lease time 21600
      deleting routers
      adding dns 10.32.51.110
      adding dns 10.64.53.110
                inet addr:10.48.65.150  Bcast:10.48.65.255  Mask:255.255.255.0
      Starting dropbear sshd: random: dropbear: uninitialized urandom read (32 bytes read)
      OK
      Starting IIO Server Daemon
   
      Welcome to Buildroot
      buildroot login:

.. raw:: html

   </details>


IIO Oscilloscope
----------------

To connect the board to IIO Scope start the IIO Oscilloscope application and go to **Settings** menu and then press **Connect**. From **Select or Discover libIIO Context** select **Manual** and enter the URI in the following format **ip:<your_board_ip>** Press the **Refresh** button and then **Connect**.

To determine the IP of the board, in Nios II Command Shell login using **root** and password **analog**. Then run the **ifconfig** command. For example:

::

   ifconfig
   eth0      Link encap:Ethernet  HWaddr B2:94:3D:6E:11:8F
             inet addr:10.48.65.132  Bcast:10.48.65.255  Mask:255.255.255.0
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:96785 errors:0 dropped:13841 overruns:0 frame:0
             TX packets:13511 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:17852315 (17.0 MiB)  TX bytes:8770953 (8.3 MiB)
             Memory:10181000-101813ff

   lo        Link encap:Local Loopback
             inet addr:127.0.0.1  Mask:255.0.0.0
             UP LOOPBACK RUNNING  MTU:65536  Metric:1
             RX packets:0 errors:0 dropped:0 overruns:0 frame:0
             TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/iioscope_connect.jpg
   :alt: iioscope_connect.jpg
   :align: center

To plot the captured waveforms go to **File** menu then click **New Plot**. Select the channels to plot and then click **Capture / Stop** button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/iioscope_newplot.png
   :alt: iioscope_newplot.png
   :align: center

More Information
----------------

-  :doc:`AD-FMCDAQ2-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>`
-  :doc:`AD-FMCDAQ2-EBZ HDL Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/reference_hdl>`

Useful links
------------

-  :doc:`AD9081/AD9082/AD9988/AD9986 Quick Start Guides </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`

   -  :doc:`Zynq-7000 SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`
   -  :doc:`Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`
   -  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`
   -  :doc:`Versal ACAP VCK190 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal>`
   -  `Arria10 SoC Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081/quickstart/a10soc]>`_

-  :doc:`AD9081-FMCA-EBZ (Single MxFE) HDL Reference Design </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`

   -  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
   -  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
   -  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

-  :doc:`AD9081/AD9082/AD9988/AD9986 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

::

         - [[resources:tools-software:linux-drivers:jesd204:jesd204-fsm-framework|JESD204 (FSM) Interface Linux Kernel Framework]]
         - [[resources:tools-software:linux-drivers:iio-pll:hmc7044|HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver]]
         - [[resources:tools-software:linux-drivers:axi-dmac| AXI-DMAC DMA Controller Linux Driver]]
         - [[resources:tools-software:linux-drivers:jesd204:axi_jesd204_tx|JESD204B Transmit Linux Driver]]
           - [[resources:tools-software:linux-software:jesd_status|JESD204B Status Utility]] 
         - [[resources:tools-software:linux-drivers:jesd204:axi_jesd204_rx|JESD204B Receive Linux Driver]]
           - [[resources:tools-software:linux-software:jesd_status|JESD204B Status Utility]] 
         - [[resources:tools-software:linux-drivers:jesd204:axi_adxcvr|JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver]]
           - [[resources:tools-software:linux-software:jesd_eye_scan|JESD204 Eye Scan]]
         - [[resources:tools-software:linux-drivers:iio-adc:axi-adc-hdl|AXI ADC HDL Linux Driver]]
         - [[resources:tools-software:linux-drivers:iio-dds:axi-dac-dds-hdl|AXI DAC HDL Linux Driver]]
   * [[:resources:tools-software:hsx-toolbox|MATLAB Support]]
        * MATLAB support is provided through the [[:resources:tools-software:hsx-toolbox|High Speed Converter Toolbox]]
   * [[resources:tools-software:linux-software:pyadi-iio| Python Support]]
        * PYTHON support is provided through the [[resources:tools-software:linux-software:pyadi-iio|Device Specific Python Interfaces For IIO Drivers]] 
        * [[https://analogdevicesinc.github.io/pyadi-iio/|PyADI-IIO Documentation]]
        * [[https://analogdevicesinc.github.io/pyadi-iio/devices/adi.ad9081.html|AD9081 class documentation]]
   * Product Datasheet
       * [[:adi:`media/en/technical-documentation/data-sheets/AD9081`.pdf|AD9081]]
       * [[:adi:`media/en/technical-documentation/data-sheets/AD9082`.pdf|AD9082]]
       * [[:adi:`media/en/technical-documentation/data-sheets/AD9988`.pdf|AD9988]]
       * [[:adi:`media/en/technical-documentation/data-sheets/AD9986`.pdf|AD9986]]
   * [[:adi:`media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578`.pdf|UG-1578, Device User Guide]]
   * [[:adi:`media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829`.pdf|UG-1829, Evaluation Board User Guide]]

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

Software support
----------------

-  :doc:`AD9081/AD9082/AD9988/AD9986 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`


.. |arria10-fpga-kit.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/arria10-fpga-kit.jpg
   :width: 330px
