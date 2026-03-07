SPI Engine Interconnect FPGA Peripheral
=======================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/spi_engine/spi_engine_interconnect.html\


.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/spi_engine/spi_engine_interconnect.png
   :align: right

The SPI Engine Interconnect module allows connecting multiple `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ masters to a single `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ slave. This enables multiple command stream generators to connect to a single `SPI Engine Execution module <https://wiki.analog.com/engine>`_ and consequential give them access to the same SPI bus. The interconnect modules take care of properly arbitrating between the different command streams.

Combining multiple command stream generators in a design and connecting them to a single execution module allows for the creation of flexible and efficient designs using standard components.

Files
-----

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Name                                                                                                                                         | Description                                                                 |
+==============================================================================================================================================+=============================================================================+
| `spi_engine_interconnect.v <https://github.com/hdl?master/library/spi_engine/spi_engine_interconnect/spi_engine_interconnect.v>`_            | Verilog source for the peripheral.                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `spi_engine_interconnect_ip.tcl <https://github.com/hdl?master/library/spi_engine/spi_engine_interconnect/spi_engine_interconnect_ip.tcl>`_  | TCL script to generate the Vivado IP-integrator project for the peripheral. |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Configuration Parameters
------------------------

+----------------+-----------------------------------------------------+---------+
| Name           | Description                                         | Default |
+================+=====================================================+=========+
| ``DATA_WIDTH`` | Data width of the parallel SDI/SDO data interfaces. | 8       |
+----------------+-----------------------------------------------------+---------+
| ``NUM_OF_SDI`` | Number of SDI lines on the physical SPI interface.  | 1       |
+----------------+-----------------------------------------------------+---------+

Signal and Interface Pins
-------------------------

+---------+-----------------------------------------------------------------------------------------------+--------------------------------------------------------+
| Name    | Type                                                                                          | Description                                            |
+=========+===============================================================================================+========================================================+
| clk     | Clock                                                                                         | A signals of the module are synchronous to this clock. |
+---------+-----------------------------------------------------------------------------------------------+--------------------------------------------------------+
| resetn  | Synchronous active-low reset                                                                  | Resets the internal state of the module.               |
+---------+-----------------------------------------------------------------------------------------------+--------------------------------------------------------+
| s0_ctrl | `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ slave  | Connects to the first control interface master         |
+---------+-----------------------------------------------------------------------------------------------+--------------------------------------------------------+
| s1_ctrl | `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ slave  | Connects to the second control interface master        |
+---------+-----------------------------------------------------------------------------------------------+--------------------------------------------------------+
| m_ctrl  | `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ master | Connects to the control interface slave                |
+---------+-----------------------------------------------------------------------------------------------+--------------------------------------------------------+

Theory of Operation
-------------------

The SPI Engine Interconnect module has multiple `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ slave ports and a single `spi_engine_control_interface <https://wiki.analog.com/spi_engine_control_interface>`_ master port. It can be used to connect multiple command stream generators to a single command execution engine. Arbitration between the streams is done on a priority basis, streams with a lower index have higher priority. This means if commands are present on two streams arbitration will be granted to the one with the lower index. Once arbitration has been granted the port it was granted to stays in control until it sends a SYNC command. When the interconnect module sees a SYNC command arbitration will be re-evaluated after the SYNC command has been completed. This makes sure that once a SPI transaction consisting of multiple commands has been started it is able to complete without being interrupted by a higher priority stream.

More Information
----------------

-  `SPI Engine Framework <https://wiki.analog.com/.>`_
