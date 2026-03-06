ADRV9001/ADRV9002 HDL Reference Design
======================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/adrv9001/index.html\


This design allows controlling, receiving and transmitting sample stream from/to an ADRV9001/ADRV9002 device through two independent source synchronous interface. Supports both CMOS and LVDS interface, but not in the same time. The selection of the I/O standard must be done with a parameter during build.

The design supports SDR or DDR modes in CMOS mode with one of four lanes, as in LVDS mode one or two lane mode. This is runtime selectable. The complete list of supported modes can be consulted in the :doc:`AXI_ADRV9001/AXI_ADRV9002 Interface Core </wiki-migration/resources/eval/user-guides/adrv9002/axi_adrv9002>` documentation.

Source code
-----------

.. admonition:: Download
   :class: download

   The source files can be accessed at:

   
   -  :git-hdl:`projects/adrv9001`
   


.. important::

   **Build instructions:**

   
   For an LVDS interface the project must be built with the following parameters:
   
   ::
   
      make CMOS_LVDS_N=0
   
   For a CMOS interface the project must be built with the following parameters:
   
   ::
   
      make CMOS_LVDS_N=1
   


Block design
------------

The design has two receive paths and two transmit paths. One of the receive paths (Rx12) has four channels and the other (Rx2) two channels. These can work independently having each two active channels, or just the Rx12 path having four active channels, while Rx2 is disabled. The same applies to the transmit path but in the other direction.

When only the Rx12 path is active with four channels mode the core will take ownership of both source synchronous interfaces. The requirement in this case is that both interfaces run at the same rate.


|image1|

FMC locations
-------------

-  ZCU102 - FMC0

DAC Interface
-------------

-  Has DDS
-  **Has PRBS** generation

ADC Interface
-------------

-  Has PN checking
-  Has data formater
-  Has programmable input delay

SW programming
--------------

Register map
~~~~~~~~~~~~

+------------+----------------------------------------------------------------------------------------+
| Address    | IP                                                                                     |
+------------+----------------------------------------------------------------------------------------+
| 0x44A00000 | :doc:`axi_adrv9001 </wiki-migration/resources/eval/user-guides/adrv9002/axi_adrv9002>` |
+------------+----------------------------------------------------------------------------------------+
| 0x44A30000 | :doc:`axi_adrv9001_rx1_dma </wiki-migration/resources/fpga/docs/axi_dmac>`             |
+------------+----------------------------------------------------------------------------------------+
| 0x44A40000 | :doc:`axi_adrv9001_rx2_dma </wiki-migration/resources/fpga/docs/axi_dmac>`             |
+------------+----------------------------------------------------------------------------------------+
| 0x44A50000 | :doc:`axi_adrv9001_tx1_dma </wiki-migration/resources/fpga/docs/axi_dmac>`             |
+------------+----------------------------------------------------------------------------------------+
| 0x44A60000 | :doc:`axi_adrv9001_tx2_dma </wiki-migration/resources/fpga/docs/axi_dmac>`             |
+------------+----------------------------------------------------------------------------------------+

.. container:: hide

   
   ZC706 VADJ protection
   ^^^^^^^^^^^^^^^^^^^^^
   
   For ZC706 after bitfile loading all outputs of FPGA are high Z .
   
   -  SW should wait until the VADJ is set to 1.8V
   -  Set **GPIO[52]** to enable the output lines.
   -  Pull out of reset the RX and TX channels (ADC/DAC common REG_RSTN reg RSTN bit)
   


.. include:: common.rst .. include:: common.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/9002_blockdiagram.png
