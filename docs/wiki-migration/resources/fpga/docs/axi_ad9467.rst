AXI_AD9467
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9467/index.html\


Overview
--------

| The :git-hdl:`library/axi_ad9467` IP core can be used to interface the :adi:`AD9467` ADC. An AXI Memory Map interface is used for configuration. The data is output using a FIFO interface.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`.

Features
--------

-  AXI based configuration
-  PRBS monitoring (PN9 and PN23)
-  DC filtering
-  Configurable line delays
-  Vivado compatible

Block diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_lvds_1.svg
   :alt: AXI_AD9467 Block diagram
   :align: center

Configuration parameters
------------------------

+--------------------+-------------------------------------------------------------+----------------------+
| Name               | Description                                                 | Default Value        |
+====================+=============================================================+======================+
| ``ID``             | Core ID should be unique for each AD9467 IP in the system   | 0                    |
+--------------------+-------------------------------------------------------------+----------------------+
| ``DEVICE_TYPE``    | Used to select between Virtex 6 (1) or 7 Series (0) devices | 0                    |
+--------------------+-------------------------------------------------------------+----------------------+
| ``IO_DELAY_GROUP`` | The delay group name which is set for the delay controller  | "adc_if_delay_group" |
+--------------------+-------------------------------------------------------------+----------------------+

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
|                     | ``adc_valid``                                 | ``output``       | Set when valid data is available on the bus                                                                                                                |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_enable``                                | ``output``       | Set when the channel is enabled, activated by software                                                                                                     |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_data``                                  | ``output[15:0]`` | Data bus                                                                                                                                                   |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_dovf``                                  | ``input``        | Data overflow input, from the DMA                                                                                                                          |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_dunf``                                  | ``input``        | Data underflow input.                                                                                                                                      |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 

Detailed Architecture
---------------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9467_1.svg
   :alt: AXI_AD9467 IP architecture?800x600
   :align: center

Detailed description
--------------------

The top module, axi_ad9467, instantiates:

-  the LVDS interface module
-  two channel processing module
-  the ADC common register map
-  the AXI handling interface
-  delay control module

| The LVDS interface module (axi_ad9467_if.v) takes at the input the lvds signals for clock, data[7:0] and over range and outputs single ended signals. The data signals are passed through an IDELAYE2 so that each line can be delayed independently through the delay controller register map.
| The latency between input and output of the interface module is 3 clock cycles.
| For more information regarding the 7 Series primitives you can take a look at UG472, UG471 and UG953.

The channel module implements:

-  a PRBS monitor
-  data format conversion
-  DC filter
-  the ADC CHANNEL register map

The data analyzed by the PRBS monitor is raw data received from the interface. You can select between PN9 and PN23 sequences.

The delay controller module (up_delay_cntrl) allows the dynamic reconfiguration of the IDELAYE2 block, which allows for a calibration procedure to be run by software.

up_adc_common implements the ADC COMMON register map, allowing for basic monitoring and control of the ADC.

Design guidelines
-----------------

The IP was developed part of the :doc:`AD9467-FMC-EBZ Reference Design </wiki-migration/resources/eval/ad9467-fmc-250ebz>`.

The control of the AD9467 chip is done through a SPI interface, which is needed at system level.

The *ADC interface signals* must be connected directly to the top file of the design, as IO primitives are part of the IP.

The example design uses a DMA to move the data from the output of the IP to memory.

If the data needs to be processed in HDL before moved to the memory, it can be done at the output of the IP (at system level) or inside of the ADC channel module (at IP level).

The example design uses a processor to program all the registers. If no processor is available in your system, you can create your own IP starting from the interface module.

Register map
------------

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

References
----------

-  :git-hdl:`AD9467 IP source code <library/axi_ad9467>`
   \* :adi:`AD9467 chip information <AD9467>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-no-OS:`AD9467-FMC-EBZ No-OS software <projects/ad9467>`
-  :git-linux>`__
-  `7 Series IO <https::`ADI Linux repository </www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`
   \* `7 Series Clocking <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
   \* `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2016_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide #ip_cores
   :alt: IP cores #hdl|Main page #tips|Using and modifying the HDL design
