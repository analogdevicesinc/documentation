AXI_AD9643 (Obsolete)
=====================

.. important::

   The support for AXI_AD9643 IP has been discontinued, the latest tested release being 2016_r1. This wiki page is left only for legacy purposes.


.. important::

   We are in the process of migrating our documentation to GitHubIO. Although obsolete, for legacy purposes, this page can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9643/index.html\


| The :git-hdl:`library/axi_ad9643` IP core can be used to interface the :adi:`AD9643` dual ADC. An AXI Memory Map interface is used for configuration. The data is output using a FIFO interface.
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
   :alt: AXI_AD9643 Block diagram
   :align: center

Configuration Parameters
------------------------

+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| Name                     | Description                                                                                        | Default Value        |
+==========================+====================================================================================================+======================+
| ``ID``                   | Core ID should be unique for each AD9643 IP in the system                                          | 0                    |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| ``DEVICE_TYPE``          | Used to select between Virtex 6 (1) or 7 Series (0) devices                                        | 0                    |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DATAPATH_DISABLE`` | If set, the datapath processing is not generated and output data is taken directly from the AD9643 | 0                    |
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
|                     | ``adc_data_in_*``                             | ``input[13:0]``  | LVDS input data                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_or_in_*``                               | ``input``        | LVDS input over range                                                                                                                                      |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``delay interface`` | **Interface used to control the delay lines** |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``delay_clock``                               | ``input``        | Clock used by the IDELAYCTRL. Connect to 200MHz                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``s axi``           | **AXI Slave Memory Map interface**            |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``adc fifo``        | **FIFO interface for connecting to the DMA**  |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ''adc_clk ''                                  | ``output``       | The input clock is passed through an IBUFGDS and a BUFG primitive and adc_clk reults. This is the clock domain that most of the modules of the core run on |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_rst``                                   | ``output``       | Output reset, on the adc_clk domain                                                                                                                        |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_enable_0``                              | ``output``       | Set when the channel is enabled, activated by software                                                                                                     |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_valid_0``                               | ``output``       | Set when valid data is available on the bus                                                                                                                |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_data_0``                                | ``output[15:0]`` | Data bus                                                                                                                                                   |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_enable_1``                              | ``output``       | Set when the channel is enabled, activated by software                                                                                                     |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_valid_1``                               | ``output``       | Set when valid data is available on the bus                                                                                                                |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_data_1``                                | ``output[15:0]`` | Data bus                                                                                                                                                   |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_dovf``                                  | ``input``        | Data overflow input, from the DMA                                                                                                                          |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``adc_dunf``                                  | ``input``        | Data underflow input.                                                                                                                                      |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``gpio``            | **Memory mapped controlled GPIO**             |                  |                                                                                                                                                            |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``up_adc_gpio_in``                            | ``input[31:0]``  | GPIO IN                                                                                                                                                    |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | ``up_adc_gpio_out``                           | ``output[31:0]`` | GPIO OUT                                                                                                                                                   |
+---------------------+-----------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 

Detailed Architecture
---------------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9643.svg
   :alt: AXI_AD9643 IP architecture?800x600
   :align: center

Detailed Description
--------------------

| The top module, axi_ad9643, instantiates:
| \* the lvds interface module
| \* two channel processing modules
| \* the ADC common register map
| \* the AXI handling interface
| \* delay control module
| The top module (axi_ad9643.v) instantiates the lvds interface module, the channel processing modules, the ADC common register map, the AXI handling interface and the delay control module

| The LVDS interface module (axi_ad9643_if.v) takes at the input the lvds signals for clock, data[13:0] and over range and outputs single ended signals. The data signals are passed through an IDELAYE2 so that each line can be delayed independently through the delay controller register map.
| For more information regarding the 7 Series primitives you can take a look at UG472, UG471 and UG953.

| The output of the interface module is fed to the channel modules The channel module implements:
| \* a PRBS monitor
| \* data format conversion
| \* DC filter
| \* the ADC CHANNEL register map
| The data analyzed by the PRBS monitor is raw data received from the interface, before being processed in any way. Selection between PN9 and PN23 sequences can be done by programming the REG_CHAN_CNTRL_3 register.

| The delay controller module, up_delay_cntrl, allows the dynamic reconfiguration of the IDELAYE2 blocks. Changing the delay on each individual line helps compensate trace differences between the data lines on the PCB. A calibration procedure can be run on software by changing the delays and monitoring the PRBS sequence.
| Up_adc_common implements the ADC common register map, allowing for basic monitoring and control of the ADC.

Register Map
------------

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Design Guidelines
-----------------

The IP was developed part of the :doc:`FMCOMMS1 Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz>`.

The control of the AD9643 chip is done through a SPI interface, which is needed at system level.

The *ADC interface signals* must be connected directly to the top file of the design, as IO primitives are part of the IP.

The example design uses a DMA to move the data from the output of the IP to memory.

If the data needs to be processed in HDL before moved to the memory, it can be done at the output of the IP (at system level) or inside of the adc channel module (at IP level).

The example design uses a processor to program all the registers. If no processor is available in your system, you can create your own IP starting from the interface module.

Software Guidelines
-------------------

| The software for this IP can be found as part of the FMCOMMS1 Reference Design at: :git-no-OS:`No-Os Software <fmcomms1>`.
| Linux is supported also using :git-linux>`__

References
----------

-  `AD9643 IP source code <https::`ADI Linux repository </github.com/analogdevicesinc/hdl/tree/hdl_2016_r1/library/axi_ad9643>`
   \* :adi:`AD9643 chip information <AD9643>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-no-OS:`No-Os Software <fmcomms1>`.
   \* :git-linux>`__
-  `7 Series IO <https::`ADI Linux repository </www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`
   \* `7 Series Clocking <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
   \* `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2016_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
