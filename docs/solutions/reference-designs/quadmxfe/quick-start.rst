Quad-MxFE Software Quick Start Guide
====================================

This Quad-MxFE Software Quick Start Guide should be used in conjunction with the :doc:`Quad-MxFE Quick Start Guide </solutions/reference-designs/quadmxfe/quickbringup>` to begin using the system.

.. image:: images/quad_mxfe.png
   :align: center
   :width: 600

Hardware
--------

-  :doc:`Equipment Needed </solutions/reference-designs/quadmxfe/quickbringup>`

Software
--------

-  :doc:`Xilinx Vivado Design Suite </solutions/reference-designs/quadmxfe/quickbringup>`
-  :doc:`Terminal program for serial and ssh connection (PuTTY) </solutions/reference-designs/quadmxfe/quickbringup>`
-  `IIO Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

   -  `adi-osc-setup.exe (Latest build) <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`_

-  :doc:`Required System Boot Files </solutions/reference-designs/quadmxfe/quick-start>`

Required System Boot Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

Testcase DAC M8,L4 ADC M8,L4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  TX: JESD204B, Subclass 1, Mode 9 - M8, L4, 12GHz 6x8 (250MSPS)
-  RX: JESD204B, Subclass 1, Mode 10 - M8, L4, 4GHz 4x4 (250MSPS)

-  use: run.vcu118_quad_ad9081_204b_txmode_9_rxmode_10.tcl

Testcase DAC M16,L4 ADC M8,L2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  TX: JESD204C, Subclass 1, Mode 11 - M16, L4, 12GHz 6x8 (250MSPS)
-  RX: JESD204C, Subclass 1, Mode 4 - M8, L2, 4GHz 4x4 (250MSPS)

-  use: run.vcu118_quad_ad9081_204c_txmode_11_rxmode_4.tcl

Testcase DAC M4,L4 ADC M4,L4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  TX: JESD204C, Subclass 1, Mode 10 - M4, L4, 12GHz 12x1 (1000MSPS)
-  RX: JESD204C, Subclass 1, Mode 11 - M4, L4, 4GHz 4x1 (1000MSPS)

Testcase DAC M4,L4,N=N'=12 ADC M4,L4,N=N'=12 (vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  2Txs / 2Rxs per MxFE
-  DAC_CLK = 12GSPS
-  ADC_CLK = 4GSPS
-  Tx I/Q Rate: 2 GSPS (Interpolation of 6x1)
-  Rx I/Q Rate: 2 GSPS (Decimation of 2x1)
-  DAC JESD204C: Mode 23, L=4, M=4, N=N'=12
-  ADC JESD204C: Mode 25, L=4, M=4, N=N'=12
-  DAC-Side JESD204C Lane Rate: 24.75Gbps
-  ADC-Side JESD204C Lane Rate: 24.75Gbps

Testcase DAC M8,L4,N=N'=12 ADC M8,L4,N=N'=12 (vcu118_quad_ad9081_204c_txmode_29_rxmode_24_revc)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  4Txs / 4Rxs per MxFE
-  DAC_CLK = 12GSPS
-  ADC_CLK = 4GSPS
-  Tx I/Q Rate: 1 GSPS (Interpolation of 12x1)
-  Rx I/Q Rate: 1 GSPS (Decimation of 4x1)
-  DAC JESD204C: Mode 24, L=4, M=8, N=N'=12
-  ADC JESD204C: Mode 29, L=4, M=8, N=N'=12
-  DAC-Side JESD204C Lane Rate: 24.75Gbps
-  ADC-Side JESD204C Lane Rate: 24.75Gbps

Downloads
^^^^^^^^^

-   `Quad_MxFE_for_VCU118_2022-06-27.zip <http://swdownloads.analog.com/cse/mxfe/Quad_MxFE_for_VCU118_2022-06-27.zip>`_

.. collapsible:: Older releases (Click to expand)

   -   `Quad_MxFE_for_VCU118_2021-08-10.zip <http://swdownloads.analog.com/cse/mxfe/Quad_MxFE_for_VCU118_2021-08-10.zip>`_
   -   `Quad_MxFE_for_VCU118_2021-04-28.zip <http://swdownloads.analog.com/cse/mxfe/Quad_MxFE_for_VCU118_2021-04-28.zip>`_
   -   `Quad_MxFE_for_VCU118_2021-03-05.zip <http://swdownloads.analog.com/cse/mxfe/Quad_MxFE_for_VCU118_2021-03-05.zip>`_
   -   `Quad MxFE for VCU118 2020-12-22.zip <http://swdownloads.analog.com/cse/mxfe/Quad MxFE for VCU118 2020-12-22.zip>`_

-  use: run.vcu118_quad_ad9081_204c_txmode_29_rxmode_24.tcl

-  **system_top\_[MODE][HW_REV].bit** (FPGA bitstream)
-  **simpleImage.vcu118_quad_ad9081\_[MODE][HW_REV].strip** (Single blob: Linux kernel + devicetree + userspace filesystem)
-  **run.vcu118_quad_ad9081\_[MODE][HW_REV].tcl** (helper script to load and start the above)
-  For Rev.A/B use the files without suffix. For Rev.C use files suffixed with ``_revc``

Example Device Trees
~~~~~~~~~~~~~~~~~~~~

ADQUADMXFE1EBZ Rev.A/Rev.B on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                                   |
+==========+========================================================================================================================================================================================================+
| dtsi     | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081.dtsi`                                                                                                                                          |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204b_txmode_9_rxmode_10.dts`                                                                                                                   |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_10_rxmode_11.dts`                                                                                                                  |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4.dts`                                                                                                                   |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_direct_6g.dts`                                                                                                         |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADQUADMXFE1EBZ Rev.C on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                           |
+==========+================================================================================================================================================================================================+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204b_txmode_9_rxmode_10_revc.dts`                                                                                                      |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_10_rxmode_11_revc.dts`                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.dts`                                                                                                      |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc.dts`                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_29_rxmode_24_revc.dts`                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADQUADMXFE1EBZ Rev.C using onchip-PLL on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                                                 |
+==========+======================================================================================================================================================================================================================+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204b_txmode_9_rxmode_10_onchip_pll_revc.dts`                                                                                                                 |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_10_rxmode_11_onchip_pll_revc.dts`                                                                                                                |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_onchip_pll_revc.dts`                                                                                                                 |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc.dts`                                                                                                                |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_29_rxmode_24_onchip_pll_revc.dts`                                                                                                                |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADUQADMXFE2EBZ Rev.C on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                                   |
+==========+========================================================================================================================================================================================================+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204b_txmode_9_rxmode_10_revc_nz1.dts`                                                                                                          |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_10_rxmode_11_revc_nz1.dts`                                                                                                         |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc_nz1.dts`                                                                                                          |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc_nz1.dts`                                                                                                         |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_29_rxmode_24_revc_nz1.dts`                                                                                                         |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADUQADMXFE2EBZ Rev.C using onchip-PLL on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                                                         |
+==========+==============================================================================================================================================================================================================================+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204b_txmode_9_rxmode_10_onchip_pll_revc_nz1.dts`                                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_10_rxmode_11_onchip_pll_revc_nz1.dts`                                                                                                                    |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_onchip_pll_revc_nz1.dts`                                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.dts`                                                                                                                    |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_29_rxmode_24_onchip_pll_revc_nz1.dts`                                                                                                                    |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADQUADMXFE3EBZ Rev.C on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                 |
+==========+======================================================================================================================================================================================+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_12_rxmode_13.dts`                                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_23_rxmode_25.dts`                                                                                                |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_3_rxmode_2.dts`                                                                                                  |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADQUADMXFE3EBZ Rev.C using onchip-PLL on VCU118 (Xilinx Virtex UltraScale+)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                                                                       |
+==========+============================================================================================================================================================================================================+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_12_rxmode_13_onchip_pll.dts`                                                                                                           |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_23_rxmode_25_onchip_pll.dts`                                                                                                           |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dts      | :git-linux:`arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_3_rxmode_2_onchip_pll.dts`                                                                                                             |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

HDL Reference Design And Instructions To Build HDL Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `ADQUADMXFE1EBZ HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad_quadmxfe1_ebz/ad_quadmxfe1_ebz_hdl>`_

--------------

Booting Pre-Build Binary Images
-------------------------------

Loading
~~~~~~~

In windows, you can run the ``XSCT`` or ``XSDB`` terminal from start menu → Xilinx Design Tools → Xilinx Software Command Line Tool… On Linux open command terminal and execute following commands:

.. container:: box bggreen

   This specifies a system console

   
   ::
   

   
      xsct% source run.vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.tcl
      attempting to launch hw_server
   
       * Xilinx hw_server v2018.2
        *** Build date : Jun 14 2018-20:42:52
          ** Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
   
      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application
   
      * Xilinx hw_server v2018.2
        *** Build date : Jun 14 2018-20:42:52
          ** Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
   
      INFO: hw_server application started
      INFO: Use Ctrl-C to exit hw_server application
   
      INFO: To connect to this hw_server instance use url: TCP:127.0.0.1:3121
   
      100%   42MB   1.7MB/s  00:25
      Downloading Program -- C:/Users/cfrick/Desktop/quadmxfe_matlab_code/FPGA_image/Quad_MxFE_for_VCU118_2021-04-28/simpleImage.vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.strip
              section, .text: 0x80000000 - 0x805229df
              section, __fdt_blob: 0x805229e0 - 0x805329df
              section, .rodata: 0x80533000 - 0x80a0d73f
              section, .pci_fixup: 0x80a0d740 - 0x80a0f3ff
              section, .builtin_fw: 0x80a0f400 - 0x80a0f423
              section, __ksymtab: 0x80a0f424 - 0x80a194af
              section, __ksymtab_gpl: 0x80a194b0 - 0x80a21c3f
              section, __ksymtab_strings: 0x80a21c40 - 0x80a3f0e4
              section, __param: 0x80a3f0e8 - 0x80a3f6c3
              section, __modver: 0x80a3f6c4 - 0x80a3ffff
              section, __ex_table: 0x80a40000 - 0x80a414ef
              section, .notes: 0x80a414f0 - 0x80a4152b
              section, .sdata2: 0x80a4152c - 0x80a41fff
              section, .data: 0x80a42000 - 0x80ace93f
              section, .data..percpu: 0x80acf000 - 0x80acefff
              section, .init.text: 0x80acf000 - 0x80af55ab
              section, .init.data: 0x80af55ac - 0x80af8253
              section, .init.ivt: 0x80af8254 - 0x80af827b
              section, .init.setup: 0x80af827c - 0x80af865f
              section, .initcall.init: 0x80af8660 - 0x80af8aff
              section, .con_initcall.init: 0x80af8b00 - 0x80af8b03
              section, .bss: 0x80af9000 - 0x80b1f3b3
              section, .init.ramfs: 0x81000000 - 0x814bd68b
      100%   15MB   0.2MB/s  01:20
      Setting PC to Program Start Address 0x80000000
      Successfully downloaded C:/Users/cfrick/Desktop/quadmxfe_matlab_code/FPGA_image/Quad_MxFE_for_VCU118_2021-04-28/simpleImage.vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.strip
      Info: MicroBlaze #0 (target 3) Running
      xsct% Info: tcfchan#1 closed
      xsct%

Kernel startup
~~~~~~~~~~~~~~

-  Open terminal (Putty, etc.)
-  Configure your serial terminal for 115200-8N1

When connecting the VCU118 USB UART to PC, it typically registers two USB
COMx/ttyUSBx ports. The first one is the connected to the system controller,
while the second one is connected to the FPGA and features the serial terminal.

**Observe following startup messages:**

::

   Ramdisk addr 0x00000000,
   Compiled-in FDT at 0x8046b89c
   Linux version 4.19.0-76252-ga6650ce-dirty (michael@mhenneri-D06) (gcc version 7.3.1 20180425 (crosstool-NG 1.20.0)) #1268 Wed Sep 2 14:54:16 CEST 2020
   setup_memory: max_mapnr: 0x30000
   setup_memory: min_low_pfn: 0x80000
   setup_memory: max_low_pfn: 0xb0000
   setup_memory: max_pfn: 0xb0000
   Zone ranges:
     DMA      [mem 0x0000000080000000-0x00000000afffffff]
     Normal   empty
   Movable zone start for each node
   Early memory node ranges
     node   0: [mem 0x0000000080000000-0x00000000ffffefff]
   Initmem setup node 0 [mem 0x0000000080000000-0x00000000ffffefff]
   On node 0 totalpages: 196608
     DMA zone: 1536 pages used for memmap
     DMA zone: 0 pages reserved
     DMA zone: 196608 pages, LIFO batch:63
   setup_cpuinfo: initialising
   setup_cpuinfo: Using full CPU PVR support
   ERROR: Microblaze HW_MUL-different for PVR and DTS
   wt_msr_noirq
   pcpu-alloc: s0 r0 d32768 u32768 alloc=1\*32768
   pcpu-alloc: [0] 0
   Built 1 zonelists, mobility grouping on.  Total pages: 195072
   Kernel command line: console=ttyUL0,115200
   Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
   Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
   Memory: 764272K/786432K available (4526K kernel code, 489K rwdata, 4264K rodata, 4906K init, 93K bss, 22160K reserved, 0K cma-reserved)
   Kernel virtual memory layout:
     * 0xffffe000..0xfffff000  : fixmap
     * 0xffffe000..0xffffe000  : early ioremap
     * 0xb0000000..0xffffe000  : vmalloc & ioremap
   NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
   irq-xilinx: /amba_pl/interrupt-controller@41200000: num_irq=16, edge=0x4f0
   /amba_pl/timer@41c00000: irq=1
   clocksource: xilinx_clocksource: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
   xilinx_timer_shutdown
   xilinx_timer_set_periodic
   sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
   Calibrating delay loop... 49.35 BogoMIPS (lpj=246784)
   pid_max: default: 32768 minimum: 301
   Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
   Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
   devtmpfs: initialized
   random: get_random_u32 called from bucket_table_alloc.isra.7+0x1e8/0x218 with crng_init=0
   clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   futex hash table entries: 256 (order: -1, 3072 bytes)
   NET: Registered protocol family 16
   GPIO line 482 (ADRF5020_CTRL) hogged as output/high
   GPIO line 428 (GPIO_0 HDL mux mode) hogged as output/high
   jesd204: created con: id=0, topo=0, link=0, /amba_pl/axi_quad_spi@44a80000/hmc7043@4 <-> /amba_pl/axi-adxcvr-tx@44b60000
   jesd204: created con: id=1, topo=0, link=2, /amba_pl/axi_quad_spi@44a80000/hmc7043@4 <-> /amba_pl/axi-adxcvr-rx@44a60000
   jesd204: created con: id=2, topo=0, link=0, /amba_pl/axi-adxcvr-tx@44b60000 <-> /amba_pl/axi-jesd204-tx@44b90000
   jesd204: created con: id=3, topo=0, link=2, /amba_pl/axi-adxcvr-rx@44a60000 <-> /amba_pl/axi-jesd204-rx@44a90000
   jesd204: created con: id=4, topo=0, link=0, /amba_pl/axi-jesd204-tx@44b90000 <-> /amba_pl/axi-ad9081-tx-3@44b10000
   jesd204: created con: id=5, topo=0, link=2, /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-2@2 <-> /amba_pl/axi_quad_spi@44a70000/ad9081@3
   jesd204: created con: id=6, topo=0, link=0, /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-2@2 <-> /amba_pl/axi_quad_spi@44a70000/ad9081@3
   jesd204: created con: id=7, topo=0, link=2, /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-1@1 <-> /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-2@2
   jesd204: created con: id=8, topo=0, link=0, /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-1@1 <-> /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-2@2
   jesd204: created con: id=9, topo=0, link=2, /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-0@0 <-> /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-1@1
   jesd204: created con: id=10, topo=0, link=0, /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-0@0 <-> /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-1@1
   jesd204: created con: id=11, topo=0, link=2, /amba_pl/axi-jesd204-rx@44a90000 <-> /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-0@0
   jesd204: created con: id=12, topo=0, link=0, /amba_pl/axi-ad9081-tx-3@44b10000 <-> /amba_pl/axi_quad_spi@44a70000/axi-ad9081-rx-0@0
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3: JESD204 link[2] transition uninitialized -> initialized
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3: JESD204 link[0] transition uninitialized -> initialized
   jesd204: found 10 devices and 1 topologies
   clocksource: Switched to clocksource xilinx_clocksource
   NET: Registered protocol family 2
   tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes)
   TCP established hash table entries: 8192 (order: 3, 32768 bytes)
   TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
   TCP: Hash tables configured (established 8192 bind 8192)
   UDP hash table entries: 512 (order: 1, 8192 bytes)
   UDP-Lite hash table entries: 512 (order: 1, 8192 bytes)
   NET: Registered protocol family 1
   RPC: Registered named UNIX socket transport module.
   RPC: Registered udp transport module.
   RPC: Registered tcp transport module.
   RPC: Registered tcp NFSv4.1 backchannel transport module.
   random: fast init done
   Skipping unavailable RESET gpio -2 (reset)
   workingset: timestamp_bits=30 max_order=18 bucket_order=0
   jffs2: version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.
   Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
   io scheduler noop registered
   io scheduler deadline registered
   io scheduler cfq registered (default)
   io scheduler mq-deadline registered
   io scheduler kyber registered
   Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
   40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 5, base_baud = 0) is a uartlite
   console [ttyUL0] enabled
   brd: module loaded
   Xilinx SystemACE device driver, major=254
   xilinx_spi 44a70000.axi_quad_spi: no CS gpios available
   xilinx_spi 44a80000.axi_quad_spi: no CS gpios available
   xilinx_spi 44b80000.axi_quad_spi: no CS gpios available
   libphy: Fixed MDIO Bus: probed
   xilinx_axienet 40c00000.ethernet: TX_CSUM 2
   xilinx_axienet 40c00000.ethernet: RX_CSUM 2
   xilinx_axienet 40c00000.ethernet: missing/invalid xlnx,addrwidth property, using default
   libphy: Xilinx Axi Ethernet MDIO: probed
   i2c /dev entries driver
   i2c i2c-0: Added multiplexed i2c bus 1
   at24 2-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
   i2c i2c-0: Added multiplexed i2c bus 2
   i2c i2c-0: Added multiplexed i2c bus 3
   i2c i2c-0: Added multiplexed i2c bus 4
   i2c i2c-0: Added multiplexed i2c bus 5
   i2c i2c-0: Added multiplexed i2c bus 6
   i2c i2c-0: Added multiplexed i2c bus 7
   i2c i2c-0: Added multiplexed i2c bus 8
   pca954x 0-0075: registered 8 multiplexed busses for I2C switch pca9548
   hmc425a amba_pl:hmc425a: amba_pl:hmc425a supply vcc-supply not found, using dummy regulator
   hmc425a amba_pl:hmc425a: Linked as a consumer to regulator.0
   ad5592r spi2.0: Linked as a consumer to regulator.1
   jesd204: /amba_pl/axi_quad_spi@44a80000/hmc7043@4,jesd204:4,parent=spi1.4: Using as SYSREF provider
   axi_adxcvr 44a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.01.a) using GTY4 at 0x44A60000 mapped to 0x(ptrval). Number of lanes: 16.
   axi_adxcvr 44b60000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.01.a) using GTY4 at 0x44B60000 mapped to 0x(ptrval). Number of lanes: 16.
   axi_sysid 45000000.axi-sysid-0: [ad] on [quadmxfe1] git <77ed1ee52339171167922d2a3f64372ce9eed601> clean [2020-07-30 15:54:12] UTC
   NET: Registered protocol family 17
   ad9081 spi0.0: AD9081 Rev. 3 Grade 10 (API 1.0.5) probed
   ad9081 spi0.1: AD9081 Rev. 3 Grade 10 (API 1.0.5) probed
   ad9081 spi0.2: AD9081 Rev. 3 Grade 10 (API 1.0.5) probed
   ad9081 spi0.3: AD9081 Rev. 3 Grade 10 (API 1.0.5) probed
   iio_dmaengine_buffer_alloc:227 width 0 (DMA width >= 256-bits ?)
   cf_axi_dds 44b10000.axi-ad9081-tx-3: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x44B10000 mapped to 0x(ptrval), probed DDS AD9081
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition initialized -> probed
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition initialized -> probed
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition probed -> idle
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition probed -> idle
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition idle -> device_init
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition idle -> device_init
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition device_init -> link_init
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition device_init -> link_init
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition link_init -> link_supported
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition link_init -> link_supported
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition link_supported -> link_pre_setup
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition link_supported -> link_pre_setup
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition link_pre_setup -> clk_sync_stage1
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition link_pre_setup -> clk_sync_stage1
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition clk_sync_stage1 -> clk_sync_stage2
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition clk_sync_stage1 -> clk_sync_stage2
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition clk_sync_stage2 -> clk_sync_stage3
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition clk_sync_stage2 -> clk_sync_stage3
   jesd204: /amba_pl/axi-jesd204-rx@44a90000,jesd204:6,parent=44a90000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 16, Link[2] lanes 4
   jesd204: /amba_pl/axi-jesd204-tx@44b90000,jesd204:7,parent=44b90000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 16, Link[0] lanes 4
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition clk_sync_stage3 -> link_setup
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition clk_sync_stage3 -> link_setup
   random: crng init done
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition link_setup -> opt_setup_stage1
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition link_setup -> opt_setup_stage1
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition opt_setup_stage1 -> opt_setup_stage2
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition opt_setup_stage1 -> opt_setup_stage2
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition opt_setup_stage2 -> opt_setup_stage3
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition opt_setup_stage2 -> opt_setup_stage3
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition opt_setup_stage3 -> opt_setup_stage4
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition opt_setup_stage3 -> opt_setup_stage4
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition opt_setup_stage4 -> opt_setup_stage5
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition opt_setup_stage4 -> opt_setup_stage5
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition opt_setup_stage5 -> clocks_enable
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition opt_setup_stage5 -> clocks_enable
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition clocks_enable -> link_enable
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition clocks_enable -> link_enable
   ad9081 spi0.0: JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.0: JESD TX (JRX) Link1 0xF lanes in DATA
   ad9081 spi0.1: JESD RX (JTX) Link1 in DATA, SYNC asserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.1: JESD TX (JRX) Link1 0xF lanes in DATA
   ad9081 spi0.2: JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.2: JESD TX (JRX) Link1 0xF lanes in DATA
   ad9081 spi0.3: JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.3: JESD TX (JRX) Link1 0xF lanes in DATA
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition link_enable -> link_running
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition link_enable -> link_running
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[2] transition link_running -> opt_post_running_stage
   jesd204: /amba_pl/axi_quad_spi@44a70000/ad9081@3,jesd204:3,parent=spi0.3: JESD204 link[0] transition link_running -> opt_post_running_stage
   iio_dmaengine_buffer_alloc:227 width 0 (DMA width >= 256-bits ?)
   cf_axi_adc 44a10000.axi-ad9081-rx-3: ADI AIM (10.01.b) at 0x44A10000 mapped to 0x80242c2b, probed ADC AD9081 as MASTER
   Freeing unused kernel memory: 4904K
   This architecture does not have kernel memory protection.
   Run /init as init process
   Starting syslogd: OK
   Starting klogd: OK
   Initializing random number generator... done.
   Starting network: udhcpc: started, v1.29.3
   net eth0: Promiscuous mode disabled.
   net eth0: Promiscuous mode disabled.
   udhcpc: sending discover
   xilinx_axienet 40c00000.ethernet eth0: Link is Down
   xilinx_axienet 40c00000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
   udhcpc: sending discover
   udhcpc: sending discover
   udhcpc: sending select for 10.44.3.52
   udhcpc: lease of 10.44.3.52 obtained, lease time 43200
   deleting routers
   adding dns 10.32.51.110
   adding dns 10.64.53.110
   Starting dropbear sshd: OK
   Starting IIO Server Daemon

   Welcome to Buildroot
   buildroot login:

Login
~~~~~

========= ==========
Login:    **root**
Password: **analog**
========= ==========

Get IP Address
~~~~~~~~~~~~~~

When the system starts it tries to acquire an IP using the DHCP protocol. In case it fails DHCP it will configure a static IP address of ``192.168.2.1``

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   

   
      # ifconfig
      eth0      Link encap:Ethernet  HWaddr 00:0A:35:00:00:00
                inet addr:10.44.3.93  Bcast:10.44.3.255  Mask:255.255.255.0
                UP BROADCAST RUNNING  MTU:1500  Metric:1
                RX packets:418 errors:0 dropped:32 overruns:0 frame:0
                TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:31911 (31.1 KiB)  TX bytes:684 (684.0 B)
   
      #

Check JESD204 Link Status
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/image2019-12-4_10-32-57.png
   :align: center
   :width: 800

.. important::

   Both Links must be in ``DATA``

The link status can be checked either from the

Serial terminal
^^^^^^^^^^^^^^^

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   

   
      #resize
      #jesd_status -s

SSH Terminal
^^^^^^^^^^^^

.. container:: box bggreen

   This specifies any shell prompt running on a remote PC

   
   ::
   

   
      dave@hal9000:~$ slogin root@10.44.3.93
      The authenticity of host '10.44.3.93 (10.44.3.93)' can't be established.
      ECDSA key fingerprint is SHA256:0AcYkl+45GBw+Fg5/oxbrh5No1UYXgkpNoLSYlrEjqs.
      Are you sure you want to continue connecting (yes/no)? yes
      Warning: Permanently added '10.44.3.93' (ECDSA) to the list of known hosts.
      root@10.44.3.93's password:
      #
      #resize
      #jesd_status

Useful IIO commands
~~~~~~~~~~~~~~~~~~~

.. image:: images/image2019-12-4_12-23-20.png
   :align: center
   :width: 400

.. note::

   See `Cmd Line <https://wiki.analog.com/resources/tools-software/linux-software/libiio/cmd_line>`_.

.. important::

   All of these commands can be used local or remote

When using remote backend please install libiio for your platform.

-  https://github.com/analogdevicesinc/libiio/releases

Windows Example
^^^^^^^^^^^^^^^

-  Download and install: https://github.com/analogdevicesinc/libiio/releases/download/v0.18/libiio-0.18.g4e22517-Windows-setup.exe
-  Open windows command prompt: cmd

.. tip::

   unlike ``iio_info`` and ``iio_attr``, ``iio_reg`` requires an environmental variable ``IIOD_REMOTE`` to be set with the target IP address.

The names of the iio devices can be obtained using ``iio_attr`` command.

.. image:: images/image2019-12-4_10-58-4.png
   :align: center
   :width: 600

**Example**: Change main NCO frequency

.. container:: box bggreen

   This specifies a system console

   
   ::
   

   
      C:\Users\dave>iio_attr -u ip:10.44.3.56 -i -c axi-ad9081-rx-3 voltage0_i main_nco_frequency 1200000000
   
      dev 'axi-ad9081-rx-3', channel 'voltage0_i' (input), attr 'main_nco_frequency', value '1000000000'
   
      wrote 11 bytes to main_nco_frequency
   
      dev 'axi-ad9081-rx-3', channel 'voltage0_i' (input), attr 'main_nco_frequency', value '1200000000'
   
      C:\Users\dave>

Further information
^^^^^^^^^^^^^^^^^^^

Further information about libiio and it's usage can be found here: **Weblinks**:

-  About IIO: `iio <https://wiki.analog.com/software/linux/docs/iio/iio>`_
-  API Documentation: http://analogdevicesinc.github.io/libiio/
-  Libiio : `libiio <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_
-  Libiio internals : `libiio_internals <https://wiki.analog.com/resources/tools-software/linux-software/libiio_internals>`_
-  `pyadi-iio <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_

Software architecture overview
------------------------------

.. image:: images/quad_sw_bd.png
   :align: center
   :width: 800

.. tip::

   All programmable devices on the Quad MxFE platform are abstracted by IIO
   devices.

+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| IIO Device   | Device Name     | Driver Documentation                                                                                                                           |
+==============+=================+================================================================================================================================================+
| iio:device0  | hmc425a         | `HMC425A Digital Step Attenuator Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-amplifiers/hmc425a>`_        |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device1  | adf4371-0       | `ADF4371 IIO Wideband Synthesizer Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/adf4371>`_              |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device2  | adf4371-1       | `ADF4371 IIO Wideband Synthesizer Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/adf4371>`_              |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device3  | adf4371-2       | `ADF4371 IIO Wideband Synthesizer Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/adf4371>`_              |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device4  | adf4371-3       | `ADF4371 IIO Wideband Synthesizer Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/adf4371>`_              |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device5  | hmc7043         | `HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/hmc7044>`_ |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device6  | axi-ad9081-rx-0 | `AD9081 MxFE Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_                                   |
|              |                 | `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_                               |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device7  | axi-ad9081-rx-1 | `AD9081 MxFE Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_                                   |
|              |                 | `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_                               |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device8  | axi-ad9081-rx-2 | `AD9081 MxFE Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_                                   |
|              |                 | `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_                               |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device9  | axi-ad9081-tx-3 | `AXI DAC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`_                           |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| iio:device10 | axi-ad9081-rx-3 | `AD9081 MxFE Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_                                   |
|              |                 | `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_                               |
+--------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+

All these drivers feature a runtime API which can be controlled using `IIO Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_, `libiio <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_, etc. However some configuration is static and done inside the device tree. For Microblaze projects (`VCU118 <https://www.xilinx.com/VCU118>`_) the device tree is build into the kernel image. Please see instructions on Building custom kernel and devicetree images here:

-  `Linux on the Xilinx FPGA development Board <https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/microblaze>`_

IIO device ``axi-ad9081-rx-3`` is special compared to the ``axi-ad9081-rx-[0..2]``, since it controls the transport layer and therefore features the IIO buffer. So all 16R data captures are controlled via this device, while the other similar devices are there, to control the device instance specific controls.

Also ``axi-ad9081-rx-3`` aka. ``spi0.3`` instantiates last, it therefore brings up the JESD204 multi-link.

::

   ad9081 spi0.0: JESD RX (JTX) Link1 in DATA, SYNC asserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.0: JESD TX (JRX) Link1 0x0 lanes in DATA
   ad9081 spi0.0: AD9081 Rev. 1 Grade 10 (API 0.7.4) probed
   ad9081 spi0.1: JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.1: JESD TX (JRX) Link1 0x0 lanes in DATA
   ad9081 spi0.1: AD9081 Rev. 1 Grade 10 (API 0.7.4) probed
   ad9081 spi0.2: JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.2: JESD TX (JRX) Link1 0x0 lanes in DATA
   ad9081 spi0.2: AD9081 Rev. 1 Grade 10 (API 0.7.4) probed
   ad9081 spi0.3: JESD RX (JTX) Link1 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.3: JESD TX (JRX) Link1 0xF lanes in DATA
   ad9081 spi0.3: AD9081 Rev. 1 Grade 10 (API 0.7.4) probed

It's expected that JRX, JTX status information may contain error status until the last device probes and the Link is finally enabled. Device ``axi-ad9081-tx-3`` purely controls the TX transport layer, it therefore doesn't have any MxFE controls. Please use the `iio_info <https://wiki.analog.com/resources/tools-software/linux-software/libiio/iio_info>`_ command to get an overview on what controls and capabilities exists.

IIO Oscilloscope
----------------

The ADI IIO Oscilloscope is a cross platform GUI application, which demonstrates
how to interface different evaluation boards from within a Linux system. The
application supports plotting of the captured data in four different modes (time
domain, frequency domain, constellation and cross-correlation). The application
also allows to view and modify several settings of the development platform's
devices.

Documentation can be found here:

-  `IIO Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

The MxFE AD9081 plugin is included in the official OSC release, which can be
downloaded from here:

-  `adi-osc-setup.exe <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`_

Instructions and Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Ordered List ItemStart OSC from your application launcher or type ``OSC``.
-  Enter the target IP address under ``Remote Devices`` and press the ``Refresh`` followed by the ``Ok`` button.

.. image:: images/microsoftteams-image_3_.png
   :align: center
   :width: 450

-  The main capture window will appear

.. image:: images/image2019-12-4_13-1-15.png
   :align: center
   :width: 600

-  Use the scroll bar in the Plot Channel box to select the channels to display.
   The first eight channels correspond to the first device, second eight to the
   second device, etc.

**Device To Channel Mapping (Rev. B/C Platforms):**

::

   axi-ad9081-rx-0: spi.0.0 - MxFE U48
   voltage0_i: (input, index: 0, format: le:S16/16>>0)
   voltage0_q: (input, index: 1, format: le:S16/16>>0)
   voltage1_i: (input, index: 2, format: le:S16/16>>0)
   voltage1_q: (input, index: 3, format: le:S16/16>>0)
   voltage2_i: (input, index: 4, format: le:S16/16>>0)
   voltage2_q: (input, index: 5, format: le:S16/16>>0)
   voltage3_i: (input, index: 6, format: le:S16/16>>0)
   voltage3_q: (input, index: 7, format: le:S16/16>>0)

   axi-ad9081-rx-1: spi.0.1 - MxFE U49
   voltage4_i: (input, index: 8, format: le:S16/16>>0)
   voltage4_q: (input, index: 9, format: le:S16/16>>0)
   voltage5_i: (input, index: 10, format: le:S16/16>>0)
   voltage5_q: (input, index: 11, format: le:S16/16>>0)
   voltage6_i: (input, index: 12, format: le:S16/16>>0)
   voltage6_q: (input, index: 13, format: le:S16/16>>0)
   voltage7_i: (input, index: 14, format: le:S16/16>>0)
   voltage7_q: (input, index: 15, format: le:S16/16>>0)

   axi-ad9081-rx-2: spi.0.2 - MxFE U61
   voltage8_i: (input, index: 16, format: le:S16/16>>0)
   voltage8_q: (input, index: 17, format: le:S16/16>>0)
   voltage9_i: (input, index: 18, format: le:S16/16>>0)
   voltage9_q: (input, index: 19, format: le:S16/16>>0)
   voltage10_i: (input, index: 20, format: le:S16/16>>0)
   voltage10_q: (input, index: 21, format: le:S16/16>>0)
   voltage11_i: (input, index: 22, format: le:S16/16>>0)
   voltage11_q: (input, index: 23, format: le:S16/16>>0)

   axi-ad9081-rx-3: spi.0.3 - MxFE U76
   voltage12_i: (input, index: 24, format: le:S16/16>>0)
   voltage12_q: (input, index: 25, format: le:S16/16>>0)
   voltage13_i: (input, index: 26, format: le:S16/16>>0)
   voltage13_q: (input, index: 27, format: le:S16/16>>0)
   voltage14_i: (input, index: 28, format: le:S16/16>>0)
   voltage14_q: (input, index: 29, format: le:S16/16>>0)
   voltage15_i: (input, index: 30, format: le:S16/16>>0)
   voltage15_q: (input, index: 31, format: le:S16/16>>0)
   voltage15_q: (input, index: 31, format: le:S16/16>>0)

.. important::

   Note: In Frequency Domain view channels can be only enabled pairwise (I+Q).

   
   And not more that 2 frequency plots can be enabled in the same window.
   
   However multiple (independent) plot windows can be opened.

The plugin window
^^^^^^^^^^^^^^^^^

.. image:: images/image2019-12-4_13-14-41.png
   :align: center
   :width: 600

OSC will instantiate multiple notebook plugin tabs on the main window. One for each device ``AD9081-X`` with an additional Debug plugin.

``AD9081-3`` again is special since it also has the controls for the TX transport layer core (``axi-ad9081-tx-3``), and the ``HMC425`` Digital Step Attenuator.

|image1|

Loading custom waveform
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: images/image2019-12-4_13-24-46.png
   :align: center
   :width: 600

Set DDS mode to ``DAC Buffer Output``, select a file hit ``Load`` button.

Optionally set a scale, and select the channels.

.. tip::

   Please be aware that due to DDR3 memory bandwidth limitations only 2 or 4 can
   be enabled simultaneously.

The Debug Plugin
^^^^^^^^^^^^^^^^

.. image:: images/image2019-12-4_13-29-56.png
   :align: center
   :width: 600

Under ``Device Selection``, select the IIO device which should be debugged/controlled.

In the ``IIO Device Attribute`` section, all device and channel attributes can be read or written,

including all attributes which are not handled by the ``AD9081-X`` device plugin itself.

In the ``Register`` section select source ``SPI``, check ``Detailed Register Map`` and ``AutoRead``, this will enable a complete AD9081 register view with description bitfields and dropdown options if available.

IIO devices ``axi-ad9081-tx-3`` and ``axi-ad9081-rx-3`` are again special, since beside the SPI option they also can access the AXI_CORE register space of the transport layer core.

MATLAB Support
--------------

MATLAB support is provided through the `High Speed Converter Toolbox <https://wiki.analog.com/resources/tools-software/hsx-toolbox>`_, with unique classes for transmit and receive functionality. Currently you must grab a development build but installers are provided for convenience.

To install the toolbox perform the follow:

-  Download and install the `Zynq SDR support package <https://mathworks.com/hardware-support/zynq-sdr.html>`_
-  Download the `master build artifact <https://gitlab.com/tfcollins/HighSpeedConverterToolbox/-/jobs/artifacts/master/download?job=deploy>`_ containing the installer for the High Speed Converter Toolbox. Once downloaded inside the zip will be the mltbx installer which will install the toolbox.

More information on controlling the Quad-MxFE Platform with MATLAB can be found
at:

-  :doc:`Quad-MxFE MATLAB Control Overview </solutions/reference-designs/quadmxfe/quickbringup>`

Linux Image build instructions
==============================

A more comprehensive guide can be found here: `Linux on the Xilinx FPGA development Board <https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/microblaze>`_

Linux on the Xilinx FPGA development Board
==========================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/linux/kernel/microblaze.html

.. note::

   This content is purely informational, and the best place for questions about this content is normally `Xilinx <https://forums.xilinx.com/t5/Embedded-Linux/bd-p/ELINUX>`_, or a friendly consultant (who you will pay), or `trainer <https://training.linuxfoundation.org/training/embedded-linux-development/>`_. These instructions work for us. That does not mean they are complete, accurate, or supported.

20

This guide provides some step-by-step instructions on how to build a Microblaze
Linux Kernel image for the FMC board connected to an

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `VC707 <https://www.xilinx.com/VC707>`_
-  `VCU118 <https://www.xilinx.com/VCU118>`_
-  `VCU128 <https://www.xilinx.com/VCU128>`_

Required Software
-----------------

-  `Linux Kernel Source <http://github.com/analogdevicesinc/linux>`_
-  `rootfs.cpio.gz <https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz>`_
-  `Xilinx Vivado Design Suite (Microblaze GNU Tools) <https://www.xilinx.com/products/design-tools/vivado.html>`_
-  `Microblaze GNU Toolchain <http://xilinx.wikidot.com/mb-gnu-tools>`_ (See note below)

Microblaze gnu toolchain from Xilinx is no longer available on git. Please use
gnu tools from Vitis installation as below:

| ~/linux$ export PATH=/opt/Xilinx/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin/::math:`PATH\\ ~/linux` export ARCH=microblaze
| ~/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-

.. tip::

   Latest released files can be downloaded from `here <https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/microblaze_loading>`_

Build Linux - Step by Step instructions
---------------------------------------

Get Microblaze Little Endian Toolchain from Xilinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the Vivado Vitis from here `Download <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_ And make sure you followed the instructions for `Microblaze GNU Toolchain <http://xilinx.wikidot.com/mb-gnu-tools>`_

Get Linux kernel source
~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   

   
      $ git clone `linux <https://github.com/analogdevicesinc/linux>`_
      Cloning into 'linux'...
      remote: Counting objects: 2757163, done.
      remote: Compressing objects: 100% (495484/495484), done.
      remote: Total 2757163 (delta 2296596), reused 2687337 (delta 2234506)
      Receiving objects: 100% (2757163/2757163), 782.04 MiB

      | 1.39 MiB/s, done.
      Resolving deltas: 100% (2296596/2296596), done.

Checkout main branch
~~~~~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   

   
      $ cd linux/
      ~/linux$ git checkout main
      Checking out files: 100% (16412/16412), done.
      Branch main set up to track remote branch main from origin.
      Switched to a new branch 'main'

Set Environmental Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   

   
      ~/linux$ source /opt/Xilinx/Vivado/2023.2/settings64.sh
      ~/linux$ export ARCH=microblaze
      ~/linux$ export CROSS_COMPILE=microblazeel-xilinx-linux-gnu-

.. tip::

   Instead of sourcing the Vivado settings64.sh script you can alternatively add
   your microblaze gcc toolchain directly to your PATH variable:

   | ``~/linux$ export PATH=/opt/Xilinx/Vitis/2023.2/gnu/microblaze/linux_toolchain/lin64_le/bin/:$PATH``

Configure Kernel
~~~~~~~~~~~~~~~~

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the development host

   
   ::
   

   
      ~/linux$ make adi_mb_defconfig
      #
      # configuration written to .config
      #

Get Root File-System
~~~~~~~~~~~~~~~~~~~~

The root file system or rootfs contains everything (besides the Linux kernel itself) needed to support a full Linux system. It contains all the (user) applications, configurations, services, data, etc. Without the rootfs your Linux system cannot run. You can either just download the pre-build image or build it yourself. Instructions can be found here: `Building with buildroot <https://wiki.analog.com/resources/tools-software/linux-build/generic/buildroot>`_

`rootfs.cpio.gz <https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz>`_

.. tip::

   rootfs.cpio.gz must be placed in the root of your kernel tree.
   (~/linux/rootfs.cpio.gz)

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   

   
      ~/linux$ wget https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
      --2022-01-18 09:52:08--  https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz
      Resolving swdownloads.analog.com (swdownloads.analog.com)... 23.63.205.142
      Connecting to swdownloads.analog.com (swdownloads.analog.com)|23.63.205.142|:443... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 6772207 (6,5M) [application/x-gzip]
      Saving to: ‘rootfs.cpio.gz’
   
      rootfs.cpio.gz                                     100%[===============================================================================================================>]   6,46M  3,32MB/s    in 1,9s    
   
      2022-01-18 09:52:12 (3,32 MB/s) - ‘rootfs.cpio.gz’ saved [6772207/6772207]

Build kernel
~~~~~~~~~~~~

The result of building the kernel is an elf file in arch/microblaze/boot named
simpleImage.<dts file name> based on the dts specified.

The build process for the kernel searches in the arch/microblaze/boot/dts
directory for a specified device tree file and then builds the device tree into
the kernel image.

The following command shows the general format for the build target name. Note
that the <dts file name> does not include the file extension ".dts".

::

   ~/linux$ make simpleImage.<dts file name>

To see what device-trees for the different FPGA carrier and FMC module
combination exist type:

::

   ~/linux$ ls -l arch/microblaze/boot/dts

.. container:: box bgblue

   
   .. note::

      This specifies any shell prompt running on the target or development host

   
   ::
   

   
      ~/linux$ make -j4 simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
        SYNC    include/config/auto.conf.cmd
        CC      scripts/mod/empty.o
        CC      scripts/mod/devicetable-offsets.s
        MKELF   scripts/mod/elfconfig.h
        HOSTCC  scripts/mod/modpost.o
        HOSTCC  scripts/mod/sumversion.o
        HOSTCC  scripts/mod/file2alias.o
   
      [ --snip-- ]
   
        AR      init/built-in.a
        LD      vmlinux.o
        MODPOST vmlinux.symvers
        MODINFO modules.builtin.modinfo
        GEN     modules.builtin
        LD      .tmp_vmlinux.kallsyms1
        KSYMS   .tmp_vmlinux.kallsyms1.S
        AS      .tmp_vmlinux.kallsyms1.S
        LD      .tmp_vmlinux.kallsyms2
        KSYMS   .tmp_vmlinux.kallsyms2.S
        AS      .tmp_vmlinux.kallsyms2.S
        LD      vmlinux
        SORTTAB vmlinux
        SYSMAP  System.map
        OBJCOPY arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
        SHIPPED arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.unstrip
        STRIP   vmlinux arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.strip
        UIMAGE  arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.ub
      Image Name:   Linux-5.10.0-97916-g513446e488c3
      Created:      Tue Jan 18 12:07:35 2022
      Image Type:   MicroBlaze Linux Kernel Image (uncompressed)
      Data Size:    18398124 Bytes = 17966.92 KiB = 17.55 MiB
      Load Address: 80000000
      Entry Point:  80000000
      Kernel: arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1 is ready  (#3678)

.. tip::

   The STRIP image found under arch/microblaze/boot/ is the ELF image which can
   be loaded via the debugger

Boot Kernel on FPGA Microblaze
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then one method to load the kernel onto the already built and running FPGA which
has the Microblaze processor is to launch XMD or XSDB from the Xilinx Vivado
toolset from within .../linux/arch/microblaze/boot and run from the XMD or XSDB
shell:

.. important::

   XMD has been deprecated and will be removed in the future. XSDB/XSCT replaces XMD and provides additional functionality. Xilinx recommends you switch to XSDB for command line debugging. You can find more information about these tools in the `Embedded System Tools Reference Manual <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2017_4/ug1043-embedded-system-tools.pdf>`_ (UG1043)

For XMD:

::

   xmd> fpga -f system_top.bit
   xmd> connect mb mdm
   xmd> dow simpleImage.vc707_fmcomms2-3
   xmd> run

For XSDB or XSCT:

::

   xsdb> connect
   xsdb> fpga -f system_top.bit
   xsdb> targets
     1  xcku040
        2  MicroBlaze Debug Module at USER2
           3  MicroBlaze #0 (Running)
   xsdb> targets 3
   xsdb> dow simpleImage.kcu105_fmcdaq2
   xsdb> con

Configure and loading using a TCL script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example TCL script:

.. code:: c

   run.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.tcl
   connect
   fpga -f system_top.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc.bit
   after 1000
   target 3
   dow simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.strip
   after 1000
   con
   disconnect

From XSDB or XSCT:

::

   xsdb> source run.tcl

(more details, methods of how to get bit file and kernel on flash and/or boot
off SD Card is appreciated)

--------------

:doc:`Back To Quad-MxFE Main Page </solutions/reference-designs/quadmxfe/quick-start>`

.. |image1| image:: images/image2019-12-4_13-20-29.png
   :width: 600
