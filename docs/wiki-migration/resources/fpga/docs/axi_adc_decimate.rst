AXI_ADC_DECIMATE
================

| The AXI_ADC_DECIMATE IP allows decimating of the input data by 10/100/1000/10000/100000, with filtering and arbitrary decimation by dropping samples.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`.

.. important::

   The axi_adc_decimate was design to interface with 12 bit converters, even though the input data bus width is 16, it will not work with anything higher then 12 bit sign extended(to 16bit) data.


Features
--------

-  AXI Lite control/status interface
-  Allows decimation by 10/100/1000/10000/100000 with filtering
-  Allows arbitrary decimation by dropping samples
-  Filtering is implemented by a 6 sections CIC programmable rate filter and a compensation FIR filter.

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_adc_decimate.svg
   :alt: AXI_ADC_DECIMATE Block diagram
   :align: center

Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------------------------+---------------+
| Name                   | Description                                | Default Value |
+========================+============================================+===============+
| ``CORRECTION_DISABLE`` | Disable scale correction of the CIC output | 1             |
+------------------------+--------------------------------------------+---------------+

Interface
---------

+------------------------+-------------------------+------------------+------------------------------------------------+
| Interface              | Pin                     | Type             | Description                                    |
+========================+=========================+==================+================================================+
| **Clock**              |                         |                  |                                                |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_clk``             | ``input``        | Clock input                                    |
+------------------------+-------------------------+------------------+------------------------------------------------+
| **Reset**              |                         |                  |                                                |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_rst``             | ``input``        | Reset, synchronous on the adc_clk clock domain |
+------------------------+-------------------------+------------------+------------------------------------------------+
| **Data Inputs**        |                         |                  |                                                |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_data_a``          | ``input[15:0]``  | Analog data for channel A                      |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_data_b``          | ``input[15:0]``  | Analog data for channel B                      |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_data_valid_a``    | ``input``        | Data valid signal for channel A                |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_data_valid_b``    | ``input``        | Data valid signal for channel B                |
+------------------------+-------------------------+------------------+------------------------------------------------+
| **Decimated Outputs**  |                         |                  |                                                |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_dec_data_a``      | ``output[15:0]`` | Decimated data for channel A                   |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_dec_data_b``      | ``output[15:0]`` | Decimated data for channel B                   |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_dec_valid_a``     | ``output``       | Data valid for channel A                       |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_dec_valid_b``     | ``output``       | Data valid for channel B                       |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_data_rate``       | ``output[2:0]``  | Data rate (decimation ratio)                   |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``adc_oversampling_en`` | ``output``       | Data oversampling enabled                      |
+------------------------+-------------------------+------------------+------------------------------------------------+
| **AXI_S_MM interface** |                         |                  |                                                |
+------------------------+-------------------------+------------------+------------------------------------------------+
|                        | ``s_axi_*``             |                  | Standard AXI Slave Memory Map interface        |
+------------------------+-------------------------+------------------+------------------------------------------------+

Detailed Description
--------------------

For some applications, the maximum sampling rate is not required and leads to lots of samples transferred to memory. In order to avoid that, the decimation IP is used.

The decimation block allows decimating the input data so that the sampling frequency to be reduced by 10, 100, 1000, 10000, 100000, with filtering.

The filtering is implemented by a 6 sections CIC programmable rate filter which allows decimation by 5/50/500/5000/50000 and a compensation FIR filter (decimation by 2).

At the end of the filter chain, there is an arbitrary decimation block. The arbitrary decimation can be activated independently and it does not implement any type of filtering.

Register Map
------------

+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Address |        | Bits                         | Name                      | Type | Description                                                                                                                                                                |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |                              |                           |      |                                                                                                                                                                            |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | REG_VERSION                  |                           |      | Version Register                                                                                                                                                           |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:0]                       | VERSION                   | RO   | Version number                                                                                                                                                             |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0001  | 0x0004 | REG_SCRATCH                  |                           |      | Scratch Register                                                                                                                                                           |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:0]                       | SCRATCH                   | RW   | Scratch register                                                                                                                                                           |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0010  | 0x0040 | REG_DECIMATION_RATIO         |                           |      | Control Arbitrary Decimation Ratio                                                                                                                                         |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:0]                       | DECIMATION_RATIO          | RW   | Set the arbitrary decimation ratio at the end of the decimation chain. Simply drop samples                                                                                 |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0011  | 0x0044 | REG_DECIMATION_STAGE_ENABLE  |                           |      | Control Filtered Decimation                                                                                                                                                |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [2:0]                        | FILTERED_DECIMATION_RATIO | RW   | Enables the filtered decimation:                                                                                                                                           |
|         |        |                              |                           |      | 0: No filtered decimation                                                                                                                                                  |
|         |        |                              |                           |      | 1: Decimation by 10. Result should be corrected by a 1.05 factor                                                                                                           |
|         |        |                              |                           |      | 2: Decimation by 100. Result should be corrected by a 1.1 factor                                                                                                           |
|         |        |                              |                           |      | 3: Decimation by 1000. Result should be corrected by a 1.15 factor                                                                                                         |
|         |        |                              |                           |      | 6: Decimation by 10000. Result should be corrected by a 1.2 factor                                                                                                         |
|         |        |                              |                           |      | 7: Decimation by 100000. Result should be corrected by a 1.26 factor                                                                                                       |
|         |        |                              |                           |      | default: No filtered decimation                                                                                                                                            |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0012  | 0x0048 | REG_CONFIG                   |                           |      | Configuration Register                                                                                                                                                     |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [1]                          | CORRECTION_ENABLE_B       | RW   | If set to 1, correction is enabled on channel B. The decimated data will be multiplied with the value from the CORRECTION_COEFFICIENT_B register.                          |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [0]                          | CORRECTION_ENABLE_A       | RW   | If set to 1, correction is enabled on channel A. The decimated data will be multiplied with the value from the CORRECTION_COEFFICIENT_A register.                          |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0013  | 0x004c | REG_CORRECTION_COEFFICIENT_A |                           |      | Correction Coefficient A                                                                                                                                                   |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [15:0]                       | CORRECTION_COEFFICIENT    | RW   | Scale correction (if equipped) coefficient for channel A. The format is 1.1.14 (sign, integer and fractional bits). Allows for correction of the CIC filter amplification. |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0014  | 0x0050 | REG_CORRECTION_COEFFICIENT_B |                           |      | Correction Coefficient B                                                                                                                                                   |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [15:0]                       | CORRECTION_COEFFICIENT    | RW   | Scale correction (if equipped) coefficient for channel B. The format is 1.1.14 (sign, integer and fractional bits). Allows for correction of the CIC filter amplification. |
+---------+--------+------------------------------+---------------------------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

References
----------

-  :git-hdl:`AXI_ADC_DECIMATE IP source code <library/axi_adc_decimate>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* `ADI Linux repository <https://github.com/analogdevicesinc/linux/>`_
-  `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2016_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
