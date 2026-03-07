AXI_AD9144 (Obsolete)
=====================

.. important::

   This page is kept for historical reasons. The same functionalities are implemented using the :doc:`generic JESD204 TPL IPs </wiki-migration/resources/fpga/peripherals/jesd204>`


.. important::

   We are in the process of migrating our documentation to GitHubIO. Although obsolete, for legacy purposes, this page can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9144/index.html\


| The :git-hdl:`library/axi_ad9144` IP core can be used to interface the :adi:`AD9144` DAC. An AXI Memory Map interface is used for configuration. Data is sent in a format that can be transmitted by Xilinx's JESD IP.
| More about the generic framework interfacing DACs can be read here: :doc:`axi_dac_ip </wiki-migration/resources/fpga/docs/axi_dac_ip>`.

Features
--------

-  AXI based configuration
   \* Hardware PRBS generation
   \* Hardware DDS generation
   \* Xilinx Vivado compatible
   \* Altera Quartus compatible

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/dac_jesd.svg
   :alt: AXI_AD9144 Block diagram
   :align: center

Configuration Parameters
------------------------

+--------------------------+-----------------------------------------------------------+---------------+
| Name                     | Description                                               | Default Value |
+==========================+===========================================================+===============+
| ``ID``                   | Core ID should be unique for each AD9144 IP in the system | 0             |
+--------------------------+-----------------------------------------------------------+---------------+
| ``QUAD_OR_DUAL_N``       | Selects if 4 lanes (1) or 2 lanes (0) are connected       | 1             |
+--------------------------+-----------------------------------------------------------+---------------+
| ``DAC_DATAPATH_DISABLE`` | If set, the DDS modules are not implemented               | 0             |
+--------------------------+-----------------------------------------------------------+---------------+

Interface
---------

+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
| Interface          | Pin                                          | Type                  | Description                                                                                       |
+====================+==============================================+=======================+===================================================================================================+
| ``jesd interface`` | **Data to be connected to the JESD core**    |                       |                                                                                                   |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``tx_clk*``                                  | ``input``             | Line rate / 40                                                                                    |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``tx_ready*``                                | ``input``             | Not used in the IP, just for interface compatibility reasons                                      |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``tx_data``                                  | ``output[255/127:0]`` | Data to be sent to the JESD core. 256 bit wide for QUAD operation, and 128 bit for DUAL operation |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``tx_valid*``                                | ``output``            | Always set to 1, for interface compatibility reasons                                              |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
| ''s axi ''         | **AXI Slave Memory Map interface**           |                       |                                                                                                   |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
| ``dma interface``  | **FIFO interface for connecting to the DMA** |                       |                                                                                                   |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ''dac_clk ''                                 | ``output``            | Loopback of the tx_clk. Most of the modules of the core run on this clock                         |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_valid_0``                              | ``output``            | DAC valid, used to read new data from the DMA                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_enable_0``                             | ``output``            | Set when the channel is enabled, activated by software                                            |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_ddata_0``                              | ``input[63:0]``       | Data for channel 0, 4 samples                                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_valid_1``                              | ``output``            | DAC valid, used to read new data from the DMA                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_enable_1``                             | ``output``            | Set when the channel is enabled, activated by software                                            |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_ddata_1``                              | ``input[63:0]``       | Data for channel 1, 4 samples                                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_valid_2``                              | ``output``            | DAC valid, used to read new data from the DMA                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_enable_2``                             | ``output``            | Set when the channel is enabled, activated by software                                            |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_ddata_2``                              | ``input[63:0]``       | Data for channel 2, 4 samples                                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_valid_3``                              | ``output``            | DAC valid, used to read new data from the DMA                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_enable_3``                             | ``output``            | Set when the channel is enabled, activated by software                                            |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_ddata_3``                              | ``input[63:0]``       | Data for channel 3, 4 samples                                                                     |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_dovf``                                 | ``input``             | Data overflow input                                                                               |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+
|                    | ``dac_dunf``                                 | ``input``             | Data underflow input                                                                              |
+--------------------+----------------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------+

Detailed Architecture
---------------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9144.svg
   :alt: AXI_AD9144 IP architecture?800x600
   :align: center

Detailed Description
--------------------

| The top module, axi_ad9144, instantiates:
| \* the JESD interface module
| \* the core module
| \* the AXI handling interface
| The interface module, axi_ad9144_if, has at the input four samples for each of the four channels and arranges them in a format which is compatible with the Xilinx's JESD core.

The axi_ad9144_core module implements the channels modules and the DAC COMMON register map module. Each channel has it's own module, implementing PN7/PN15 data generation, inverse PN7/PN15, DDS data and fixed pattern generators. The module is configured through the DAC CHANNEL register map.

The up_axi module implements the AXI bus interface.

Register Map
~~~~~~~~~~~~

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Software Guidelines
-------------------

| The software for this IP can be found as part of the DAQ2 Reference Design at: :git-no-OS:`No-OS Software <projects/fmcdaq2>`
| Linux is supported also using :git-linux>`__

References
----------

-  `AD9144 IP source code <https::`ADI Linux repository </github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/axi_ad9144>`
   \* :adi:`AD9144 chip information <AD9144>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-no-OS:`No-Os Software <projects/fmcdaq2>`.
   \* `ADI Linux repository <https://github.com/analogdevicesinc/linux>`_
-  :adi:`Analog Device's JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
   \* `Altera Quartus JESD IP documentation <https://www.altera.com/en_US/pdfs/literature/ug/ug_jesd204b.pdf>`_
   \* `Xilinx Vivado JESD IP documentation <https://www.xilinx.com/support/documentation/ip_documentation/jesd204/v6_0/pg066-jesd204.pdf>`_
   \* `Arria 10 Transceivers <https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/hb/arria-10/ug_arria10_xcvr_phy.pdf>`_
   \* `7 Series transceivers <https://www.xilinx.com/support/documentation/user_guides/ug476_7Series_Transceivers.pdf>`_
   \* `Ultrascale GTY transceivers <https://www.xilinx.com/support/documentation/user_guides/ug578-ultrascale-gty-transceivers.pdf>`_
   \* `Ultrascale GTH transceivers <https://www.xilinx.com/support/documentation/user_guides/ug576-ultrascale-gth-transceivers.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
