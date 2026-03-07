Channel UNPACK Utility Core
===========================

The channel UNPACK utility core (util_upack) is meant to allow one or more channels to be enabled by software without any padding. This allows full usage of the DMA bandwidth without any overhead. This core is normally works with the DAC and DMA modules. The DAC interface is channel based (one interface per each DAC channel) and consists of enable, valid and data signals. The DMA interface is a single FIFO interface consisting of valid and data signals. The enable signals are usually controlled by software. The core simply unpacks the DMA data into the individual channels as defined by the enables.

Features
--------

-  Supports Intel/Altera and Xilinx devices
-  Supports up to 8 channels
-  Supports configurable channel data width

Functional Description
----------------------

The core 'collects' samples from the DMA interface (or any other source) and passes it to the DAC on every valid request from the DAC. This is best explained through some examples. Let's consider a 4 channel DAC with a channel data width of 32 bits. That is, the DAC requires two 16-bit samples be present at its input for all channels when the valid is asserted. The DMA interface in this case is an interleaved 8 samples (128 bits) stream. This is because irrespective of the DAC channel data width, the software always sees data as 'samples interleaved'. The same data set may drive a DAC core with a channel width of 128 bits or 16 bits.

a. Four channels enabled (4'b1111)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/4channel_upack_4.svg
   :alt: Upack data flow, when 4 channel is enabled

b. Three channels enabled (4'b1110)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/3channel_upack_4.svg
   :alt: Upack data flow, when 4 channel is enabled

c. Two channels enabled (4'b1100)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/2channel_upack_4.svg
   :alt: Upack data flow, when 4 channel is enabled

This data unpacking now needs to factor in the valid and the number of samples that are to be read from the DMA. It is quite simple a valid at the DAC interface translates into a data required count based on the number of enables. So if three channels are enabled the requirement is 6 samples, so the core initiates a read from the DMA three out of four clock cycles.

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

+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Interface/Pin                          | Type                                               | Description                                                                                                     |
+========================================+====================================================+=================================================================================================================+
| '' dac_clk ''                          | input                                              | DAC interface clock (core clock). The module runs on this clock.                                                |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| \*\* FIFO interface to the source \*\* |                                                    |                                                                                                                 |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_valid ''                        | output                                             | DAC valid, request the next valid data from the source                                                          |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_data ''                         | input[((NUM_OF_CHANNELS\*CHANNEL_DATA_WIDTH)-1):0] | DAC data bus from the source                                                                                    |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_sync ''                         | output                                             | DAC sync signal to the DMA (optional)                                                                           |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| \*\* FIFO interface to the DAC \*\*    |                                                    |                                                                                                                 |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_enable\_\* ''                   | input                                              | Indicates the status of the channel, if asserted the channel is active                                          |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_valid\_\* ''                    | input                                              | Validates the data on the dac_data\_\* bus                                                                      |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_data\_\* ''                     | output[(CHANNEL_DATA_WIDTH-1):0]                   | DAC data bus to the DAC core (sink)                                                                             |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' upack_valid\_\* ''                  | output                                             | Delayed valid signal, using this control signal, the initial transient state of the module will be filtered out |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| \*\* Control signals \*\*              |                                                    |                                                                                                                 |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dma_xfer_in ''                      | input                                              | XFER_REQ from DMA, indicates an active DMA transfer                                                             |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| '' dac_xfer_out ''                     | output                                             | XFER_REQ to DAC, forwarded xfer request                                                                         |
+----------------------------------------+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

Register Map
------------

This core does not have a register map.

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
