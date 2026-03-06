AD9081/AD9082 Quick Start Guides
================================

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the :adi:`AD9081-FMCA-EBZ` and :adi:`AD9082-FMCA-EBZ` boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
------------------

The :adi:`AD9081-FMCA-EBZ` and :adi:`AD9082-FMCA-EBZ` is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

+--------------------------------------------+-----------------+-----------------+
| Board                                      | AD9081-FMCA-EBZ | AD9082-FMCA-EBZ |
+============================================+=================+=================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`__ | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`__   | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `VCU118 <https://www.xilinx.com/VCU118>`__ | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `VCU128 <https://www.xilinx.com/VCU128>`__ | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `VCK190 <https://www.xilinx.com/VCK190>`__ | √               | √               |
+--------------------------------------------+-----------------+-----------------+
| `A10Soc <https://www.intel.com/A10Soc>`__  | √               | √               |
+--------------------------------------------+-----------------+-----------------+

Supported Environments
----------------------

The supported OS are:

+--------------------------------------------+-----+----------------+----------------+
| Board                                      | HDL | Linux Software | No-OS Software |
+============================================+=====+================+================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`__ | √   | √              | √              |
+--------------------------------------------+-----+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`__   | √   | √              | √              |
+--------------------------------------------+-----+----------------+----------------+
| `VCU118 <https://www.xilinx.com/VCU118>`__ | √   | √              | √              |
+--------------------------------------------+-----+----------------+----------------+

Quick Start Guides
------------------

ZC706 + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Zynq-7000 SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`

ZCU102 + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD9081 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`

VCU118 + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`

VCK190 + AD9081-FMCA-EBZ/AD9082-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Versal ACAP VCK190 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal>`

A10SoC + AD9081-FMCA-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Arria10 SoC Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081/quickstart/a10soc>`

Hardware Setup
--------------

In most carriers, the :adi:`AD9081-FMCA-EBZ` board connects to the HPC0 connector (unless otherwise noted). The carrier setup requires power, UART (115200), ethernet (Linux), DisplayPort or HDMI (if available) and/or JTAG (no-OS) connections. A few typical setups are shown below.

AD9081-FMCA-EBZ / AD9082-FMCA-EBZ (Single MxFE) HDL Reference Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   We are in the process of migrating our documentation to GitHub IO. Please check the following link for updated information regarding the **HDL project**: https://analogdevicesinc.github.io/hdl/projects/ad9081_fmca_ebz/index.html.


Functional Overview
===================

The AD9081-FMCA-EBZ / AD9082-FMCA-EBZ reference design is a processor based (e.g. Microblaze) embedded system. The design consists from a receive and a transmit chain.

The receive chain transports the captured samples from ADC to the system memory (DDR). Before transferring the data to DDR the samples are stored in a buffer implemented on block rams from the FPGA fabric (util_adc_fifo). The space allocated in the buffer for each channel depends on the number of currently active channels. It goes up to M x 64k samples if a single channel is selected or 64k samples per channel if all channels are selected.

The transmit chain transports samples from the system memory to the DAC devices. Before streaming out the data to the DAC through the JESD link the samples first are loaded into a buffer (util_dac_fifo) which will cyclically stream the samples at the tx_device_clk data rate. The space allocated in the transmit buffer for each channel depends on the number of currently active channels. It goes up to M x 64k samples if a single channel is selected or 64k samples per channel if all channels are selected.

All cores from the receive and transmit chains are programmable through an AXI-Lite interface.

The transmit and receive chains can operate at different data rates having separate rx_device_clk/tx_device_clk and corresponding lane rates but must share the same reference clock.

Board setup
===========

.. important::

   **The following rework is required:**

   
   -  In order to avoid using an external clock source and fully rely on the HMC7044 clock chip,*\* rotate the C6D/C4D caps in C5D/C3D position*\* (**Please note:** In the latest version of the board, this is now the default configuration, so this configuration step **might not be needed anymore**)
   -  If LEDS V1P0_LED and VINT_LED are not on please \*\* depopulate R22M and populate R2M*\*
   


HDL source code
===============

.. admonition:: Download
   :class: download

   **Reference design location:**

   
   -  :git-hdl:`projects/ad9081_fmca_ebz`
   


Supported Carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`__ FMC HPC0 Slot
-  `ZC706 <https://www.xilinx.com/ZC706>`__ FMC HPC Slot
-  `VCU118 <https://www.xilinx.com/VCU118>`__ FMC+ Slot

Useful links
============

-  :doc:`AD9081 Quick Start Guides </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`
-  :doc:`Building HDL </wiki-migration/resources/fpga/docs/build>`
-  :doc:`AD-FMC-SDCARD for Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

Block design
============

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
-------

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
-----------------------------------------------

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
-----------------------------------------------

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
--------------------------------------------------------

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
=============

The clock sources depend on the in use carrier and are depicted on the below diagrams:

ZCU102
------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_clocking_zcu102.png
   :align: center

VC118
-----

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_clocking_vcu118.png
   :align: center

Software considerations
=======================

ADC - crossbar config
---------------------

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
---------------------

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


HDL Reference Design
--------------------

-  :doc:`AD9081-FMCA-EBZ (Single MxFE) HDL Reference Design </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`

Software support
----------------

-  :doc:`AD9081 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

.. include:: common.rst .. include:: common.rst
