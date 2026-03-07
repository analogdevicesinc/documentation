AXI_AD9963
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9963/index.html


| The :git-hdl:`library/axi_ad9963` IP is implementing the interfacing with the :adi:`AD9963` chip. It features a dual 12 bit ADC working up to 100MSPS and a dual 12 bit DAC with up to 170MSPS. It also features a DLL which can provide clock for both the ADC and the DAC path.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`, and for DACs: :doc:`axi_dac_ip </wiki-migration/resources/fpga/docs/axi_dac_ip>`.

Features
--------

-  AXI Lite control/status interface
-  PRBS monitoring
-  Hardware DC filtering
-  IQ/Scale correction
-  Internal DDS
-  Programmable line delays
-  Supports Xilinx devices

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9963.svg
   :alt: AXI_AD9963 Block diagram
   :align: center

Configuration Parameters
------------------------

+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| Name                         | Description                                                                                         | Default Value        |
+==============================+=====================================================================================================+======================+
| ``ID``                       | Core ID should be unique for each AD9963 IP in the system                                           | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``DEVICE_TYPE``              | Used to select between Virtex 6 (1) or 7 Series (0) devices                                         | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_IODELAY_ENABLE``       | Enable IODELAY for tuning the TRX interface                                                         | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``IO_DELAY_GROUP``           | The delay group name which is set for the delay controller                                          | "adc_if_delay_group" |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``DAC_DATAPATH_DISABLE``     | Disable DAC processing blocks. Disables DDS                                                         | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_USERPORTS_DISABLE``    | Disable ADC userports                                                                               | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DATAFORMAT_DISABLE``   | Disable ADC data format processing block                                                            | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DCFILTER_DISABLE``     | Disable ADC dc filtering processing block                                                           | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_IQCORRECTION_DISABLE`` | Disable ADC IQ corection processing block                                                           | 0                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_SCALECORRECTION_ONLY`` | If IQ correction block is enabled and only the scale needs to be corrected, this should be set to 1 | 1                    |
+------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+

Interface
---------

+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface                     | Pin              | Type             | Description                                                                                                                                    |
+===============================+==================+==================+================================================================================================================================================+
| **CMOS RX interface signals** |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``trx_clk``      | ``input``        | CMOS input clock                                                                                                                               |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``trx_iq``       | ``input``        | CMOS input channel selection                                                                                                                   |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``trx_data``     | ``input[11:0]``  | CMOS input data                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **CMOS TX interface signals** |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``tx_clk``       | ``input``        | CMOS input clock                                                                                                                               |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``tx_iq``        | ``output``       | CMOS output channel selection                                                                                                                  |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``tx_data``      | ``output[11:0]`` | CMOS output data                                                                                                                               |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **Transmit master/slave**     |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_sync_in``  | ``input``        | DAC synchronization signal. It is generated by the master core and used by all the cores in the system. Only one of the IPs should be master   |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_sync_out`` | ``output``       | DAC synchronization signal. It is generated by the master core and used by all the cores in the system. Only one of the cores should be master |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **Delay Clock**               |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``delay_clock``  | ``input``        | Clock used by the IDELAYCTRL. Connect to 200MHz                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **DMA_RX interface**          |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ''adc_clk ''     | ``output``       | Clock derived from the TRX clock. It is the clock on which all ADC related logic runs.                                                         |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_rst``      | ``output``       | Output reset, on the adc_clk domain                                                                                                            |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_enable_i`` | ``output``       | Set when the channel I is enabled, activated by software                                                                                       |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_valid_i``  | ``output``       | Set when valid data is available on the channel I                                                                                              |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_data_i``   | ``output[15:0]`` | Channel I data bus                                                                                                                             |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_enable_q`` | ``output``       | Set when the channel Q is enabled, activated by software                                                                                       |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_valid_q``  | ``output``       | Set when valid data is available on the channel Q                                                                                              |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_data_q``   | ``output[15:0]`` | Channel Q data bus                                                                                                                             |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``adc_dovf``     | ``input``        | Data overflow input, from the DMA                                                                                                              |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **DMA_TX interface**          |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ''dac_clk ''     | ``output``       | Clock derived from the TX clock. It is the clock on which all DAC related logic runs.                                                          |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_rst``      | ``output``       | Output reset, on the dac_clk domain                                                                                                            |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_enable_i`` | ``output``       | Set when the channel I is enabled, activated by software                                                                                       |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_valid_i``  | ``output``       | Set when valid data is available on the channel I                                                                                              |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_data_i``   | ``input[15:0]``  | Channel I data bus                                                                                                                             |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_enable_q`` | ``output``       | Set when the channel Q is enabled, activated by software                                                                                       |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_valid_q``  | ``output``       | Set when valid data is available on the channel Q                                                                                              |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_data_q``   | ``input[15:0]``  | Channel Q data bus                                                                                                                             |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_dunf``     | ``input``        | Data underflow input from the DMA                                                                                                              |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **AXI_S_MM interface**        |                  |                  |                                                                                                                                                |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | ``s_axi_*``      |                  | Standard AXI Slave Memory Map interface                                                                                                        |
+-------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

Detailed Description
--------------------

The TRX (ADC) interface is set at 100 MSPS, full duplex mode, double data rate (DDR), two channels. The clock comes from the AD9963 chip.

The TX (DAC) interface works at 75MSPS data rate with interpolation by 2 on the AD9963 chip. The DAC path inside AD9963 chip works at 150MHz, pushing part of the spurs outside the 100MHz bandwidth. The design assumes that the 75MHz clock is not available in the FPGA. In order to reduce the number of PLL used in the FPGA, we are using AD9963 and a BUFR (divide by 2) to generate this clock. When the clock is generated by AD9963, DDR transfer is not available. The TX interface works at 150 MHz, SDR.

Register Map
------------


.. note::

   See `resources/fpga/docs/reg_map_description <https://wiki.analog.com/resources/fpga/docs/reg_map_description>`_


Register Map base addresses for axi_ad9963
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| Address |        | Name         |     |     | Description                                                                                   |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |              |     |     |                                                                                               |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | BASE         |     |     | See the `Base (common to all cores) <https://wiki.analog.com/>`_ table for more detail        |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | ADC COMMON   |     |     | See the `ADC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | ADC CHANNELS |     |     | See the `ADC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | DAC COMMON   |     |     | See the `DAC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | DAC CHANNELS |     |     | See the `DAC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+--------------+-----+-----+-----------------------------------------------------------------------------------------------+

.. include:: hdl/regmap.rst .. include:: hdl/regmap.rst .. include:: hdl/regmap.rst .. include:: hdl/regmap.rst .. include:: hdl/regmap.rst

Design Guidelines
-----------------

In order to reduce the power and resource utilization, all the unused features should be disabled.

Software Guidelines
-------------------

For RX PRBS data, when 2's complement mode is selected, each new word is the 1 bit shifted version of the previous word. Steps to do in order to test the PRBS on the RX path:

-  1. Write to AD9963 SPI register 0x51 the value 1, which enables the BIST core.
-  2. Write to AD9963 SPI register 0x51 the value 7
-  3. Read register 0x404 from the AD9361 ADC core (should read value 2 or 6)
-  4. Write back to register 0x404 from the AD9361 ADC core the value read above
-  5. Read register 0x404 from the AD9361 ADC core. It should read 0x0 if the RX path is working correctly for channel 1
-  6. Perform steps 3-6 with register 0x444. This will validate the RX path for channel 2

If the TRX path does not work correctly, the output current on the TRX pins can be changed by writing to register 0x63.

The TX interface testing is done by writing 1024 samples of PRBS data and checking the BIST signature values for both the I and the Q side. Interpolation should not be active during the BIST testing.

References
----------

-  :git-hdl:`AD9963 IP source code <library/axi_ad9963>`
   \* :adi:`AD9963 chip information <en/products/rf-microwave/communications-analog-front-ends/mixed-signal-frontends/ad9963.html>`
-  :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* `ADI Linux repository <https://github.com/analogdevicesinc/linux/>`_
-  `7 Series IO <https://www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`_
   \* `7 Series Clocking <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
   \* `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2016_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
