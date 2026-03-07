AXI_LTC235x IP core
===================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ltc235x/index.html\


The axi_ltc235x IP core can be used to interface the :adi:`LTC2358-18`, :adi:`LTC2358-16`, and similar devices using an FPGA. The core has a AXI Memory Map interface for configuration, supports the CMOS and LVDS interfaces of the device, and has a simple FIFO interface for the DMAC. This documentation only covers the IP core and requires that one must be familiar with the devices for a complete and better understanding.

More about the generic framework interfacing ADCs, that contains the up_adc_channel and up_adc_common modules, can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`.

Features
--------

-  AXI based configuration
-  Quartus Prime compatible
-  :adi:`LTC2358-18`. No support yet for :adi:`LTC2358-16`, :adi:`LTC2357-18`, :adi:`LTC2357-16`, :adi:`LTC2353-18`, :adi:`LTC2353-16`
-  CMOS and LVDS Mode
-  SoftSpan configuration

Block Diagram
-------------

| 
| |AXI_LTC235x CMOS Block diagram|
| |AXI_LTC235x LVDS Block diagram|
| ===== Configuration Parameters =====

+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| Name               | Description                                                                                                      | Default Value |
+====================+==================================================================================================================+===============+
| ``ID``             | Core ID should be unique for each IP in the system. Core ID should be unique for each ltc235x IP in the system.  | 0             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``XILINX_INTEL_N`` | IP Core compatibility, set 0 for Intel and 1 for Xilinx.                                                         | 0             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LVDS_CMOS_N``    | Defines the physical interface type, set 0 for CMOS and set 1 for LVDS.                                          | 0             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LTC235X_FAMILY`` | Set 0 for 2358-18. Set 1 for 2358-16. Set 2 for 2357-18. Set 3 for 2357-16. Set 4 for 2353-18. Set 5 for 2353-16 | 0             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_0_ENABLE``  | Enable option for LANE 0.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_1_ENABLE``  | Enable option for LANE 1.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_2_ENABLE``  | Enable option for LANE 2.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_3_ENABLE``  | Enable option for LANE 3.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_4_ENABLE``  | Enable option for LANE 4.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_5_ENABLE``  | Enable option for LANE 5.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_6_ENABLE``  | Enable option for LANE 6.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_7_ENABLE``  | Enable option for LANE 7.                                                                                        | 1             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``NUM_CHANNELS``   | Select number of ADC channels.                                                                                   | 8             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``DATA_WIDTH``     | Select width of data in bits.                                                                                    | 18            |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+
| ``EXTERNAL_CLK``   | Defines the external clock option for the ADC clock: 0 - No, 1 - Yes                                             | 0             |
+--------------------+------------------------------------------------------------------------------------------------------------------+---------------+

Interface
---------

+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface                | Pin                                              | Type              | Description                                                                                                                                                  |
+==========================+==================================================+===================+==============================================================================================================================================================+
| ``Input data interface`` | **ADC data interface signals**                   |                   |                                                                                                                                                              |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``busy``                                         | ``input``         | Indicates that a conversion is in progress. This pin transitions lowto-high at the start of each conversion and stays high until the conversion is complete. |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``lvds_cmos_n``                                  | ``output``        | I/O mode select                                                                                                                                              |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``external_clk``                                 | ``input``         | external clock                                                                                                                                               |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | **CMOS signals**                                 |                   |                                                                                                                                                              |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``scki``                                         | ``output``        | serial clock input of device                                                                                                                                 |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``scko``                                         | ``input``         | serial clock output of device                                                                                                                                |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``sdi``                                          | ``output``        | serial data input of device                                                                                                                                  |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``sdo``                                          | ``input [7:0]``   | serial data output of device                                                                                                                                 |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | **LVDS signals**                                 |                   |                                                                                                                                                              |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``scki_p``                                       | ``output``        | positive serial clock input of device                                                                                                                        |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``scki_n``                                       | ``output``        | negative serial clock input of device                                                                                                                        |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``scko_p``                                       | ``input``         | positive serial clock output of device                                                                                                                       |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``scko_n``                                       | ``input``         | negative serial clock output of device                                                                                                                       |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``sdi_p``                                        | ``output``        | positive serial data input of device                                                                                                                         |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``sdi_n``                                        | ``output``        | negative serial data input of device                                                                                                                         |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``sdo_p``                                        | ``input``         | positive serial data output of device                                                                                                                        |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``sdo_n``                                        | ``input``         | negative serial data output of device                                                                                                                        |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``s axi_*``              | **AXI Slave Memory Map interface**               |                   |                                                                                                                                                              |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ''adc fifo ''            | \*\* FIFO interface for connecting to the DMA*\* |                   |                                                                                                                                                              |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``adc_dovf``                                     | ``input``         | Data overflow, must be connected to the DMA.                                                                                                                 |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``adc_enable_*``                                 | ``output``        | If set, the channel is enabled (one for each channel).                                                                                                       |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``adc_valid_*``                                  | ``output``        | Indicates valid data at the current channel (one for each channel).                                                                                          |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | ``adc_data_*``                                   | ``output [31:0]`` | Received data output (one for each channel).                                                                                                                 |
+--------------------------+--------------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Detailed Architecture
---------------------

| 
| |AXI_LTC235x IP architecture|

Detailed Description
--------------------

The top module, axi_ltc235x, instantiates:

-  the ltc235x cmos interface module
-  the channel processing module
-  the ADC common register map
-  the AXI handling interface

The interface module, axi_ltc235x_cmos, consists of the physical interface connected to the device. The signals used are the serial clock input and output, serial data input and outputs, and the busy signal that are also found with the device.

The data from the interface module is processed by the adc channel module. This includes the channel ID and the SoftSpan ID.

Up_adc_common module implements the ADC COMMON register map, allowing for basic monitoring and control of the ADC.

Up_adc_channel module implements the ADC CHANNEL register map, allowing for basic monitoring and control of the ADC's channel. The SoftSpan ID per channel are also implemented here.

The up_axi module implements the AXI bus interface.

Register Map
------------

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Design Guidelines
-----------------

The control of the LTC235x chip is done through the CMOS/LVDS interface at system level. The SoftSpan ID register per channel in up_adc_channel can be configured. The SoftSpan ID of all the channels are sent to the ADC through the interface module on every conversion.

The *ADC interface signals* must be connected directly to the top file of the design, as IO primitives are part of the IP.

The example design uses a DMA to move the data from the output of the IP to memory.

If the data needs to be processed in HDL before moving to the memory, it can be done at the output of the IP (at the system level) or inside the ADC interface module (at the IP level).

The example design uses a processor to program all the registers. If no processor is available in your system, you can create your IP starting from the interface module.

Software Guidelines
-------------------

Linux is supported also using `ADI Linux repository <https://github.com/analogdevicesinc/linux>`_

References
----------

-  LTC235x IP Source Code
-  :doc:`DC2677A Reference Design </wiki-migration/resources/eval/user-guides/dc2677a>`
-  ADC Parts: :adi:`LTC2358-18`, :adi:`LTC2358-16`, :adi:`LTC2357-18`, :adi:`LTC2357-16`, :adi:`LTC2353-18`, :adi:`LTC2353-16`
-  ADC Eval Board: :adi:`DC2677A`
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic AXI ADC IP core </wiki-migration/resources/fpga/docs/axi_adc_ip>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#resources/fpga/docs/ip_cores
   :alt: IP cores#resources/fpga/docs/hdl|Main page#resources/fpga/docs/tips|Using and modifying the HDL design

.. |AXI_LTC235x CMOS Block diagram| image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ltc235x_cmos.svg
.. |AXI_LTC235x LVDS Block diagram| image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ltc235x_lvds.svg
.. |AXI_LTC235x IP architecture| image:: https://wiki.analog.com/_media/resources/fpga/docs/arhi_axi_ltc235x.svg
