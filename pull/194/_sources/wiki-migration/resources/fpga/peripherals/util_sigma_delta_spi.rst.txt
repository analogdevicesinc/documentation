Sigma-Delta SPI Util FPGA Peripheral
====================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/util_sigma_delta_spi/index.html\


.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/util_sigma_delta_spi.png
   :align: right

ADCs from the Analog Devices Sigma-Delta converter family use a low-level communication protocol that multiplexes the SPI bus MISO signal and the data ready interrupt signal over the same physical wire (DOUT/RDY). The Sigma-Delta SPI Util peripheral can be used to de-multiplex these signals inside a FPGA.


Files
-----

+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| File                                                                                                                     | Description                                                                |
+==========================================================================================================================+============================================================================+
| `util_sigma_delta_spi.v <https://github.com/hdl?master/library/util_sigma_delta_spi/util_sigma_delta_spi.v>`_            | Verilog source for the peripheral                                          |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| `util_sigma_delta_spi_ip.tcl <https://github.com/hdl?master/library/util_sigma_delta_spi/util_sigma_delta_spi_ip.tcl>`_  | TCL script to generate the Vivado IP-integrator project for the peripheral |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

Configuration Parameters
------------------------

+------------------+------------------------------------------------------------------------------+---------+
| Name             | Description                                                                  | Default |
+==================+==============================================================================+=========+
| ``IDLE_TIMEOUT`` | Number of clock cycles after SPI bus activity before data ready is detected. | 63      |
+------------------+------------------------------------------------------------------------------+---------+
| ``CS_PIN``       | Chip-select pin used for the Sigma-Delta converter.                          | 0       |
+------------------+------------------------------------------------------------------------------+---------+
| ``NUM_CS``       | Number of total chip-select pins on the SPI bus.                             | 2       |
+------------------+------------------------------------------------------------------------------+---------+

Signal and Interface Pins
-------------------------

+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Signal         | Type                                                                                                      | Description                                                                  |
+================+===========================================================================================================+==============================================================================+
| ``clk``        | Clock                                                                                                     | All other signals are synchronous to this clock.                             |
+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ``resetn``     | Synchronous active low reset                                                                              | Resets the internal state machine of the core.                               |
+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ``spi_active`` | Input                                                                                                     | Indicates whether a SPI transaction is active on the SPI bus. (Active high). |
+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ``data_ready`` | Output                                                                                                    | Indicates when a data ready condition is detected. (Active high).            |
+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ``s_spi``      | :doc:`SPI bus interface </wiki-migration/resources/fpga/peripherals/spi_engine/spi_bus_interface>` slave  | SPI bus interface connected to the upstream SPI controller.                  |
+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| ``m_spi``      | :doc:`SPI bus interface </wiki-migration/resources/fpga/peripherals/spi_engine/spi_bus_interface>` master | SPI bus interface connected to the downstream SPI bus.                       |
+----------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

Theory of Operation
-------------------

The Sigma-Delta Util Peripheral monitors the SPI bus that is connected to the ``s_spi`` interface for the converters data ready condition. The ``m_spi`` interface is directly connected to the ``s_spi`` interface. In a typical configuration the ``s_spi`` interface is connected to a SPI controller and the ``m_spi`` interface is connected to external SPI bus pins.

The ``data_ready`` signal is level active high and will be asserted as long as the data ready condition is detected. It can for example be connected to a interrupt controller to start a interrupt service routine that will read the converted data sample from the ADC or it can be connected to a HDL block like the :doc:`SPI Engine Offload </wiki-migration/resources/fpga/peripherals/spi_engine/offload>` block that will generate a SPI transaction to read the converted signal.

The data ready condition is only detected if the chip-select signal which is connected to the converter is asserted and the ``spi_active`` signal is de-asserted and both signals have been in that state for at least ``IDLE_TIMEOUT`` clock cycles. The timeout is used to avoid spurious signal detection and the ``IDLE_TIMEOUT`` parameter should be configured so that the period it takes to complete ``IDLE_TIMEOUT`` clock cycles with the ``clk`` clock is larger than the "CS falling edge to DOUT/RDY active time" and "SCLK inactive edge to DOUT/RDY high/low" as specified in the datasheet for the converter.

Supported Devices
-----------------

-  :adi:`AD7172-2`
-  :adi:`AD7173-8`
-  :adi:`AD7175-2`
-  :adi:`AD7176-2`
-  :adi:`AD7190`
-  :adi:`AD7192`
-  :adi:`AD7195`
-  :adi:`AD7780`
-  :adi:`AD7785`
-  :adi:`AD7787`
-  :adi:`AD7788`
-  :adi:`AD7789`
-  :adi:`AD7790`
-  :adi:`AD7791`
-  :adi:`AD7792`
-  :adi:`AD7793`
-  :adi:`AD7794`
-  :adi:`AD7795`
-  :adi:`AD7796`
-  :adi:`AD7797`
-  :adi:`AD7798`
-  :adi:`AD7799`
