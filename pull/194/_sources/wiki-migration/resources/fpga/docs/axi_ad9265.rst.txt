AXI_AD9265
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9265/index.html\


| The :git-hdl:`library/axi_ad9265` IP core can be used to interface the :adi:`AD9265` ADC, in LVDS mode.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`.

Features
--------

-  AXI based configuration
   \* PRBS monitoring (PN9 and PN23)
   \* DC filtering
   \* Configurable line delays
   \* Vivado compatible

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_lvds_1.svg
   :alt: AXI_AD9265 Block diagram
   :align: center

Configuration Parameters
------------------------

+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| Name                     | Description                                                                                        | Default Value        |
+==========================+====================================================================================================+======================+
| ``ID``                   | Core ID should be unique for each AD9265 IP in the system                                          | 0                    |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| ``DEVICE_TYPE``          | Used to select between 7 Series (1), Ultrascale (2) or Ultrascale+ (3) devices                     | 0                    |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DATAPATH_DISABLE`` | If set, the datapath processing is not generated and output data is taken directly from the AD9265 | 0                    |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| ``IO_DELAY_GROUP``       | The delay group name which is set for the delay controller                                         | "adc_if_delay_group" |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+

Interface
---------

+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface           | Pin                                           | Type             | Description                                                                                                                                                |
+=====================+===============================================+==================+============================================================================================================================================================+
| ``adc interface``   | **ADC interface signals**                     |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_clk_in_*``                              | ``input``        | LVDS input clock                                                                                                                                           |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_data_in_*``                             | ``input[7:0]``   | LVDS input data                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_or_in_*``                               | ``input``        | LVDS input over range                                                                                                                                      |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``delay interface`` | **Interface used to control the delay lines** |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``delay_clock``                               | ``input``        | Clock used by the IDELAYCTRL. Connect to 200MHz                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ''s axi ''          | **AXI Slave Memory Map interface**            |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``adc fifo``        | **FIFO interface for connecting to the DMA**  |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ''adc_clk ''                                  | ``output``       | The input clock is passed through an IBUFGDS and a BUFG primitive and adc_clk reults. This is the clock domain that most of the modules of the core run on |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_rst``                                   | ``output``       | Output reset, on the adc_clk domain                                                                                                                        |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_enable``                                | ``output``       | Set when the channel is enabled, activated by software                                                                                                     |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_valid``                                 | ``output``       | Set when valid data is available on the bus                                                                                                                |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_data``                                  | ``output[15:0]`` | Data bus                                                                                                                                                   |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_dovf``                                  | ``input``        | Data overflow input, from the DMA                                                                                                                          |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_dunf``                                  | ``input``        | Data underflow input. Not used                                                                                                                             |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Detailed Architecture
---------------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9265_4.svg
   :alt: AXI_AD9265 IP architecture?800x600
   :align: center

Detailed Description
--------------------

| The top module, axi_ad9265, instantiates:
| \* the lvds interface module
| \* the channel processing module
| \* the ADC common register map
| \* the AXI handling interface
| \* delay control module
| The LVDS interface module, axi_ad9265_if, has as input the lvds signals for clock, data[7:0] and over range. It uses IO block primitives inside of IP to handle the input signals. The input clock is routed to a clock distribution primitive from which it drives all the ADC related processing circuitry. The data signals are passed through an IDELAYE2 so that each line can be delayed independently through the delay controller register map. The IP outputs a data value on every clock cycle, along with the over range signal. The latency between input and output of the interface module is 3 clock cycles.
| The data from the interface module is processed by the adc channel module.
| The channel module implements:
| \* a PRBS monitor
| \* data format conversion
| \* DC filter
| \* the ADC CHANNEL register map
| The data analyzed by the PRBS monitor is raw data received from the interface, before being processed in any way. Selection between PN9 and PN23 sequences can be done by programming the REG_CHAN_CNTRL_3 register.

Up_adc_common module implements the ADC COMMON register map, allowing for basic monitoring and control of the ADC.

| The delay controller module, up_delay_cntrl, allows the dynamic reconfiguration of the IDELAYE2 blocks. Changing the delay on each individual line helps compensate trace differences between the data lines on the PCB. A calibration procedure can be run on software by changing the delays and monitoring the PRBS sequence.

Register Map
------------

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Design Guidelines
-----------------

The IP was developed part of the :doc:`AD9265 Native FMC Card Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad9265>`.

The control of the AD9265 chip is done through a SPI interface, which is needed at system level.

The *ADC interface signals* must be connected directly to the top file of the design, as IO primitives are part of the IP.

The example design uses a DMA to move the data from the output of the IP to memory.

If the data needs to be processed in HDL before moved to the memory, it can be done at the output of the IP (at system level) or inside of the adc channel module (at IP level).

The example design uses a processor to program all the registers. If no processor is available in your system, you can create your own IP starting from the interface module.

Software Guidelines
-------------------

| The software for this IP can be found as part of the AD9265 Native FMC Card Reference Design at: :git-no-OS:`No-OS Software <projects/ad9265-fmc-125ebz>`
| Linux is supported also using :git-linux>`__

References
----------

-  `AD9265 IP source code <https::`ADI Linux repository </github.com/analogdevicesinc/hdl/tree/master/library/axi_ad9265>`
   \* :adi:`AD9265 chip information <AD9265>`
   \* :doc:`AD9265 Native FMC Card Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad9265>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-no-OS:`No-Os Software <projects/ad9265-fmc-125ebz>`
-  :git-linux>`__
-  `7 Series IO <https::`ADI Linux repository </www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`
   \* `7 Series Clocking <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
   \* `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2015_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
