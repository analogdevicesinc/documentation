SPI Engine Offload FPGA Peripheral
==================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/spi_engine/spi_engine_offload.html\


.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/spi_engine/spi_engine_offload.png
   :align: right

The SPI Engine Offload peripheral allows to store a SPI Engine command and SDO data stream in a RAM or ROM module. The command stream is executed when the ``trigger`` signal is asserted. This allows the execution of SPI transactions with a very short delay in reaction to a event.

Files
-----

+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Name                                                                                                                          | Description                                                                 |
+===============================================================================================================================+=============================================================================+
| `spi_engine_offload.v <https://github.com/hdl?master/library/spi_engine/spi_engine_offload/spi_engine_offload.v>`_            | Verilog source for the peripheral.                                          |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `spi_engine_offload_ip.tcl <https://github.com/hdl?master/library/spi_engine/spi_engine_offload/spi_engine_offload_ip.tcl>`_  | TCL script to generate the Vivado IP-integrator project for the peripheral. |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Configuration Parameters
------------------------

+------------------------+----------------------------------------------------------------------------------------------------+---------+
| Name                   | Description                                                                                        | Default |
+========================+====================================================================================================+=========+
| ``SPI_CLK_ASYNC``      | If set to 1 the ``ctrl_clk`` and ``spi_clk`` are assumed to be asynchronous                        | 0       |
+------------------------+----------------------------------------------------------------------------------------------------+---------+
| ``CMD_MEM_ADDR_WIDTH`` | Configures the size of the command stream storage. The size is ``2**CMD_MEM_ADDR_WIDTH`` entries.  | 4       |
+------------------------+----------------------------------------------------------------------------------------------------+---------+
| ``SDO_MEM_ADDR_WIDTH`` | Configures the size of the SDO data stream storage. The size is ``2**SDO_MEM_ADDR_WIDTH`` entries. | 4       |
+------------------------+----------------------------------------------------------------------------------------------------+---------+

Signal and Interface Pins
-------------------------

+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Name                        | Type                                                                                                         | Description                                                                                         |
+=============================+==============================================================================================================+=====================================================================================================+
| ``ctrl_clk``                | Clock                                                                                                        | The ``spi_engine_offload_ctrl`` signals are synchronous to this clock.                              |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``spi_clk``                 | Clock                                                                                                        | The ``spi_engine_ctrl`` signals, ``offload_sdi`` signals and trigger are synchronous to this clock. |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``spi_resetn``              | Synchronous active low reset                                                                                 | Resets the internal state machine of the core.                                                      |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``trigger``                 | Input                                                                                                        | When asserted the stored command and data stream is send out on the ``spi_engine_ctrl`` interface.  |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``spi_engine_offload_ctrl`` | `spi_engine_offload_control_interface <https://wiki.analog.com/spi_engine_offload_control_interface>`_ slave | Control interface which allows to re-program the stored command and SDO data stream.                |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``spi_engine_ctrl``         | `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ master                | SPI Engine Control stream that contains commands and data.                                          |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``offload_sdi``             | Streaming AXI master                                                                                         | Output stream of the received SPI data                                                              |
+-----------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

Theory of Operation
-------------------

More Information
----------------

-  `SPI Engine Framework <https://wiki.analog.com/.>`_
