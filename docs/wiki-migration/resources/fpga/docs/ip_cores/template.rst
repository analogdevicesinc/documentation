IP NAME
=======

Features
--------

-  AXI-based configuration
   \* Vivado and Quartus compatible

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/ad777x_diagrams/block_diagram_ad777x.svg
   :alt: AXI_AD777x Block diagram
   :align: center

Configuration Parameters
------------------------

====== ================================================== =============
Name   Description                                        Default Value
====== ================================================== =============
``ID`` Core ID should be unique for each IP in the system 0
====== ================================================== =============

Interface
---------

+--------------------------+--------------------------------------------------+------------+-----------------------------------------------------------------------+
| Interface                | Pin                                              | Type       | Description                                                           |
+==========================+==================================================+============+=======================================================================+
| ``Input data interface`` | **ADC data interface signals**                   |            |                                                                       |
+--------------------------+--------------------------------------------------+------------+-----------------------------------------------------------------------+
|                          | ``clk_in``                                       | ``input``  | input clock                                                           |
+--------------------------+--------------------------------------------------+------------+-----------------------------------------------------------------------+
| ''s axis ''              | **AXI Slave Memory Map interface**               |            |                                                                       |
+--------------------------+--------------------------------------------------+------------+-----------------------------------------------------------------------+
| ''adc fifo ''            | \*\* FIFO interface for connecting to the DMA*\* |            |                                                                       |
+--------------------------+--------------------------------------------------+------------+-----------------------------------------------------------------------+
|                          | ''adc_clk ''                                     | ``output`` | This is the clock domain that most of the modules of the core run on. |
+--------------------------+--------------------------------------------------+------------+-----------------------------------------------------------------------+

Detailed Architecture
---------------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/ad777x_diagrams/arhitecture_ad777x.svg
   :alt: AXI_AD777x IP architecture
   :align: center

Detailed Description
--------------------

| The top module instantiates
| \* The ADC channel register map
| \* The ADC common register map
| \* The AXI handling interface

| The data from the interface module is processed by the ADC channel module.
| The Up_adc_common module implements the ADC COMMON register map, allowing for basic monitoring and control of the ADC.
| The Up_adc_channel module implements the ADC CHANNEL register map, allowing for basic monitoring and control of the ADC's channel.

Register Map
------------

.. include:: ../hdl/regmap.rst

.. include:: ../hdl/regmap.rst

.. include:: ../hdl/regmap.rst

Design Guidelines
-----------------

The control of the chip is done through an SPI interface, which is needed at the system level.

The *ADC interface signals* must be connected directly to the top file of the design, as IO primitives are part of the IP.

The example design uses a DMA to move the data from the output of the IP to memory.

If the data needs to be processed in HDL before moving to the memory, it can be done at the output of the IP (at the system level) or inside the ADC interface module (at the IP level).

The example design uses a processor to program all the registers. If no processor is available in your system, you can create your IP starting from the interface module.

Software Guidelines
-------------------

Linux is supported also using :git-linux>`__

References
----------

-  `ADI HDL repository <https::`ADI Linux repository </github.com/analogdevicesinc/hdl/tree/master/library/axi_ad777x>`
   \* :git-linux>`__
-  `Zynq-7000 SoC Overview <https::`ADI Linux repository </www.xilinx.com/support/documentation/data_sheets/ds190-Zynq-7000-Overview.pdf>`
   \* `Zynq-7000 SoC Packaging and Pinout <https://www.xilinx.com/support/documentation/user_guides/ug865-Zynq-7000-Pkg-Pinout.pdf>`__

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#resources/fpga/docs/ip_cores
   :alt: IP cores#resources/fpga/docs/hdl|Main page#resources/fpga/docs/tips|Using and modifying the HDL design
