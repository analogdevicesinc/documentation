SPI Engine Execution FPGA Peripheral
====================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/spi_engine/spi_engine_execution.html\


.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/spi_engine/spi_engine_execution.png
   :align: right

The SPI Engine Execution peripheral forms the heart of the SPI Engine framework. It is responsible for handling a SPI Engine control stream and translates it into low-level SPI bus transactions.

Files
-----

+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Name                                                                                                                                | Description                                                                 |
+=====================================================================================================================================+=============================================================================+
| `spi_engine_execution.v <https://github.com/hdl?master/library/spi_engine/spi_engine_execution/spi_engine_execution.v>`__           | Verilog source for the peripheral.                                          |
+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `spi_engine_execution_ip.tcl <https://github.com/hdl?master/library/spi_engine/spi_engine_execution/spi_engine_execution_ip.tcl>`__ | TCL script to generate the Vivado IP-integrator project for the peripheral. |
+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Configuration Parameters
------------------------

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| Name                | Description                                                                                                                                                         | Default |
+=====================+=====================================================================================================================================================================+=========+
| ``NUM_CS``          | Number of chip-select signals for the SPI bus (min: 1, max: 8)                                                                                                      | 1       |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| ``DEFAULT_SPI_CFG`` | Reset configuration value for the :doc:`SPI configuration register </wiki-migration/resources/fpga/peripherals/spi_engine/instruction_format>`                      | 0       |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| ``DEFAULT_CLK_DIV`` | Reset configuration value for the :doc:`prescaler clock divider register </wiki-migration/resources/fpga/peripherals/spi_engine/instruction_format>`                | 0       |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| ``DATA_WIDTH``      | Data width of the parallel data stream. Will define the transaction's granularity. Supported values: 8/16/24/32                                                     | 8       |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| ``NUM_OF_SDI``      | Number of multiple SDI lines, (min: 1, max: 8)                                                                                                                      | 1       |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+

Signal and Interface Pins
-------------------------

+------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Name       | Type                                                                                          | Description                                                                         |
+============+===============================================================================================+=====================================================================================+
| ``clk``    | Clock                                                                                         | All other signals are synchronous to this clock.                                    |
+------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| ``resetn`` | Synchronous active-low reset                                                                  | Resets the internal state machine of the core.                                      |
+------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| ``active`` | Output                                                                                        | Indicates whether the peripheral is currently active and processing commands.       |
+------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| ``ctrl``   | `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`__ slave | SPI Engine Control stream that contains commands and data for the execution module. |
+------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| ``spi``    | `spi_bus_interface <https://wiki.analog.com/spi_bus_interface>`__ master                      | Low-level SPI bus interface that is controlled by peripheral.                       |
+------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

Theory of Operation
-------------------

The SPI Engine Execution module implements the physical access to the SPI bus. It implements a small but powerful programmable state machine that translates a SPI Engine command stream into low-level SPI bus access.

Communication with a command stream generator happens via the ``ctrl`` interface and the low-level SPI access is handled on the ``spi`` interface. The ``active`` signal is asserted as long as the peripheral is busy executing incoming commands.

Internally the SPI Engine execution module consists of an instruction encoder that translates the incoming commands into an internal control signal, a multi-function counter and compares unit that is responsible for handling the timing and a shift register which holds the received and transmitted SPI data.

The module has an optional programmable pre-scaler register that can be used to divide the external clock to the counter and compare unit.

.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/spi_engine/spi_engine.svg

More Information
----------------

-  `SPI Engine Framework <https://wiki.analog.com/.>`__
