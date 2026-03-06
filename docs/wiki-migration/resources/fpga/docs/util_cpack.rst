Channel CPACK Utility Core
==========================

The channel CPACK utility core (util_cpack) is meant to allow one or more channels to be enabled by software without any padding. This allows full usage of the DMA bandwidth without any overhead. This core is normally works with an ADC and DMA modules. The ADC interface is channel based (one interface per each ADC channel) and consists of enable, valid and data signals. The DMA interface is a single FIFO interface consisting of valid and data signals. The enable signals are usually controlled by software. The core simply packs the ADC data of the individual channels into a single data bus, as defined by the ADC enables.

Features
--------

-  Supports Intel/Altera and Xilinx devices
-  Supports up to 8 channels
-  Supports configurable channel data width

Functional Description
----------------------

The core 'collects' samples from the ADC interface and passes it to the DMA (or any other sink module), the data flow is controlled by the ADC. This is best explained through some examples. Let's consider a 4 channel ADC with a channel data width of 32 bits. The ADC core provides two 16-bit samples on its output for all channels when the valid is asserted. The DMA interface, in this case, is an interleaved 8 samples (128 bits) stream. This is because irrespective of the ADC channel data width, the software always sees data as 'samples interleaved'. The same data set may received by the DMA core with a channel width of 128 bits or 16 bits.

a. Four channels enabled (4'b1111)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/4channel_cpack_1.svg
   :alt: Cpack data flow, when 4 channel is enabled

b. Three channels enabled (4'b1110)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/3channel_cpack_1.svg
   :alt: Cpack data flow, when 4 channel is enabled

c. Two channels enabled (4'b1100)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/2channel_cpack_1.svg
   :alt: Cpack data flow, when 4 channel is enabled

Parameters
----------

====================== ================================== =============
Name                   Description                        Default Value
====================== ================================== =============
``CHANNEL_DATA_WIDTH`` Data width of a channel            32
``NUM_OF_CHANNELS``    Number of channels, max value is 8 8
====================== ================================== =============

Interface
---------

+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface/Pin                               | Type                             | Description                                                                                                                                                                                                      |
+=============================================+==================================+==================================================================================================================================================================================================================+
| '' adc_clk ''                               | input                            | ADC interface clock (core clock). The module runs on this clock.                                                                                                                                                 |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_rst ''                               | input                            | Reset signal from the ADC core.                                                                                                                                                                                  |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*\* FIFO interfaces from the ADC core \*\* |                                  |                                                                                                                                                                                                                  |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_enable\_\* ''                        | input                            | Indicates the status of the channel, if asserted the channel is active                                                                                                                                           |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_valid\_\* ''                         | input                            | Indicates a valid data on the adc_data\_\* bus                                                                                                                                                                   |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_data\_\* ''                          | input[(CHANNEL_DATA_WIDTH-1):0]  | ADC data bus from the ADC core                                                                                                                                                                                   |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*\* FIFO interface to the DMA (sink) \*\*  |                                  |                                                                                                                                                                                                                  |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_valid ''                             | output                           | Indicates data on the adc_data bus                                                                                                                                                                               |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_sync ''                              | output                           | Control the correct alignment, when the source and sink interface data width is different. When this bit is asserted, the first sample on the DMA interface (16 bit LBS), must be a sample of the first channel. |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| '' adc_data ''                              | output[(CHANNEL_DATA_WIDTH-1):0] | DAC data bus to the DAC core (sink)                                                                                                                                                                              |
+---------------------------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Register Map
------------

This core does not have a register map.

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
