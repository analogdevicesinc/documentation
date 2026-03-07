AXI_AD9671 (Obsolete)
=====================

.. important::

   The support for AXI_AD9671 IP has been discontinued. This wiki page is left only for legacy purposes.


.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9671/index.html\


Overview
--------

| The :git-hdl:`library/axi_ad9671` IP core can be used to interface the :adi:`AD9671` Octal Ultrasound AFE with digital demodulator. An AXI Memory Map interface is used for configuration. Data is received from Xilinx JESD IP.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`.

Features
--------

-  AXI based configuration
   \* PRBS monitoring (PN9 and PN23)
   \* Altera Quartus compatible
   \* Xilinx Vivado compatible

Block diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_jesd.svg
   :alt: AXI_AD9671 Block diagram
   :align: center

Configuration parameters
------------------------

+--------------------+---------------------------------------------------------------------------+---------------+
| Name               | Description                                                               | Default Value |
+====================+===========================================================================+===============+
| ``ID``             | Core ID should be unique for each AD9671 IP in the system. ID 0 is master | 0             |
+--------------------+---------------------------------------------------------------------------+---------------+
| ``DEVICE_TYPE``    | Selection between Xilinx(0) and Altera(1) devices                         | 0             |
+--------------------+---------------------------------------------------------------------------+---------------+
| ``QUAD_OR_DUAL_N`` | Selects if 4 lanes (1) or 2 lanes (0) are connected                       | 1             |
+--------------------+---------------------------------------------------------------------------+---------------+

Interface
---------

+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
| Interface          | Pin                                          | Type                | Description                                                                                    |
+====================+==============================================+=====================+================================================================================================+
| ``jesd interface`` | **Data to be connected to the JESD core**    |                     |                                                                                                |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``rx_clk*``                                  | ``input``           | JESD clock rate / 40                                                                           |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``rx_data``                                  | ``input[127/63:0]`` | RX data from the JESD core. 128 bit wide for QUAD operation, and 64 bit for DUAL operation     |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``rx_sof*``                                  | ``input[3:0]``      |                                                                                                |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``rx_valid``                                 | ``input``           | Placeholder for interfaces. Assume data is always valid                                        |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``rx_ready``                                 | ``output``          | Always ready                                                                                   |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``rx_sof*``                                  | ``input[3:0]``      |                                                                                                |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
| ''s axi ''         | **AXI Slave Memory Map interface**           |                     |                                                                                                |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
| ``dma interface``  | **FIFO interface for connecting to the DMA** |                     |                                                                                                |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ''adc_clk ''                                 | ``output``          | Loopback of the tx_clk. most of the modules of the core run on this clock                      |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_valid``                                | ``output[7:0]``     | ADC valid, used to read new data from the DMA. Each bit applies to one channel                 |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_enable``                               | ``output[7:0]``     | Set when the channel is enabled, activated by software. Each bit applies to one channel        |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_data``                                 | ``input[127:0]``    | Data for all channels                                                                          |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_dovf``                                 | ``input``           | Data overflow input                                                                            |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_dunf``                                 | ``input``           | Data underflow input.                                                                          |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
| ``sync interface`` | **Synchronization between multiples cores**  |                     |                                                                                                |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_sync_in``                              | ``input``           | Starts the synchronization procedure. Comes from the master IP                                 |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_sync_out``                             | ``output``          | Starts the synchronization procedure. Sent to the slave IPs                                    |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_raddr_in``                             | ``input[3:0]``      | Read address. All IPs are sending data from the same memory location. Comes from the master IP |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+
|                    | ``adc_raddr_out``                            | ``output[3:0]``     | Read address. All IPs are sending data from the same memory location. Sent to the slave IPs    |
+--------------------+----------------------------------------------+---------------------+------------------------------------------------------------------------------------------------+

Architecture
------------

| |AXI_AD9671 IP architecture?800x600|

Description
-----------

| The top module, axi_ad9671, instantiates:
| \* the interface module
| \* the channel processing module
| \* the ADC common register map
| \* the AXI handling interface
| The interface module, axi_ad9671_if, takes the data from the Xilinx JESD IP and splits it into channels. In order to synchronize several AD9671 chips, a FIFO is used and a comparison mechanism with a start code.

| The data from the interface module is processed by the adc channel module.
| The channel module implements:
| \* a PRBS monitor
| \* data format conversion
| \* the ADC CHANNEL register map

Design Guidelines
-----------------

The control of the AD9671 chip is done through a SPI interface, which is needed at system level.

The design should use a DMA to move the data from the output of the IP to memory.

If the data needs to be processed in HDL before moved to the memory, it can be done at the output of the IP (at system level) or inside of the adc channel module (at IP level).

Register map
------------

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

References
----------

-  :git-hdl:`AD9671 IP source code <library/axi_ad9671>`
   \* :adi:`AD9671 chip information <AD9671>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* `ADI Linux repository <https://github.com/analogdevicesinc/linux>`_
-  :adi:`Analog Device's JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
   \* `Altera Quartus JESD IP documentation <https://www.altera.com/en_US/pdfs/literature/ug/ug_jesd204b.pdf>`_
   \* `Xilinx Vivado JESD IP documentation <https://www.xilinx.com/support/documentation/ip_documentation/jesd204/v6_0/pg066-jesd204.pdf>`_
   \* `Arria 5 Transceivers <https://www.altera.com/en_US/pdfs/literature/ug/xcvr_user_guide.pdf>`_
   \* `7 Series transceivers <https://www.xilinx.com/support/documentation/user_guides/ug476_7Series_Transceivers.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design

.. |AXI_AD9671 IP architecture?800x600| image:: https://wiki.analog.com/_media/resources/fpga/docs/ad9671.svg
