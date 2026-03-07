AXI_AD9783
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9783/index.html\


| The :git-hdl:`library/axi_ad9783` IP core interfaces to the :adi:`AD9783 <en/products/ad9783.html>` device. It is a dual DAC with 16 bits resolution, interfaced through LVDS, and with sample rates up to 500 MSPS. This documentation only covers the IP core and requires that one must be familiar with the device for a complete and better understanding.
| More about the generic framework interfacing DACs can be read here: :doc:`axi_dac_ip </wiki-migration/resources/fpga/docs/axi_dac_ip>`.

Features
--------

-  AXI Memory-Mapped to Streaming control/status interface
-  PRBS monitoring
-  Internal DDS
-  BIST testing
-  Supports only Xilinx devices

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9783.jpg
   :align: center
   :width: 600px

Functional Description
----------------------

| The axi_ad9783 cores architecture contains:
| \* :git-hdl:`Interface <library/axi_ad9783/axi_ad9783.v#L135>` module in LVDS mode for Xilinx devices
| \* :git-hdl:`Transmit <library/axi_ad9783/axi_ad9783_core.v>` module, which contains:

::

     * [[:git-hdl:`library/axi_ad9783/axi_ad9783_channel`.v| DAC channel processing]] modules, one for each channel \\
       * Different data generators ([[:git-hdl:`library/common/ad_dds`.v| DDS]], pattern, PRBS)
       * [[:git-hdl:`library/common/up_dac_channel`.v| DAC Channel register map]]
     * [[:git-hdl:`library/common/up_dac_common`.v| DAC Common register map]]
   * [[:git-hdl:`library/common/up_axi`.v| AXI control and status]] modules. \\

Parameters
----------

+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| Name                        | Description                                                                                                              | Default Value |
+=============================+==========================================================================================================================+===============+
| ``ID``                      | Instance identification number, if more than one AD9783 instance is used                                                 | 0             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_TECHNOLOGY``         | Encoded value describing the technology/generation of the FPGA device (1 - 7series, 2 - UltraScale, 3 - UltraScale Plus) | 0             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ''FPGA_FAMILY ''            | Encoded value describing the family variant of the FPGA device(e.g., SX, GX, GT)                                         | 0             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ''SPEED_GRADE ''            | Encoded value describing the FPGA's speed-grade                                                                          | 0             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ''DEV_PACKAGE ''            | Encoded value describing the device package. The package might affect high-speed interfaces                              | 0             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ``DAC_DDS_TYPE``            | 1 for CORDIC or 2 for Polynomial                                                                                         | 1             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ``DAC_DDS_CORDIC_DW``       | CORDIC DDS data width                                                                                                    | 16            |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ``DAC_DDS_CORDIC_PHASE_DW`` | CORDIC DDS phase width                                                                                                   | 16            |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+
| ``DAC_DATAPATH_DISABLE``    | Disable DAC processing blocks. Disables DDS                                                                              | 0             |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------+---------------+

.. note::

   Make sure these parameters have the appropriate values set.


I/O Interface
-------------

+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
| Interface                     | Pin                    | Type             | Description                                                                                                      |
+===============================+========================+==================+==================================================================================================================+
| **LVDS TX interface signals** |                        |                  |                                                                                                                  |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_clk_in_p & n``   | ``input``        | LVDS input clock; comes from DCOP/N of the AD9783 chip                                                           |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_clk_out_p & n``  | ``output``       | LVDS output clock; goes to DCIP/N of the AD9783 chip                                                             |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_data_out_p & n`` | ``output[15:0]`` | LVDS output data lines                                                                                           |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
| **Clock and reset**           |                        |                  |                                                                                                                  |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_div_clk``        | ``output``       | Frequency divided clock used for clocking the DMA and the UPACK; it is 1/4 compared to the reference input clock |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_rst``            | ``output``       | Core reset signal                                                                                                |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
| **DMA_TX interface**          |                        |                  |                                                                                                                  |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_enable_*``       | ``output``       | If set, the channel is enabled (one for each channel)                                                            |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_valid``          | ``output``       | Indicates valid data request for all channels                                                                    |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_ddata_*``        | ``input[64:0]``  | Transmitted data output (one for each channel)                                                                   |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``dac_dunf``           | ``input``        | Data underflow, must be connected to the DMA                                                                     |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
| **AXI_S_MM interface**        |                        |                  |                                                                                                                  |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+
|                               | ``s_axi_*``            |                  | Standard AXI Slave Memory Map interface                                                                          |
+-------------------------------+------------------------+------------------+------------------------------------------------------------------------------------------------------------------+

Device Interface Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interface also provides a single clock tree for the entire core. This clock uses a global buffer that has the minimum skew all across the die. On Xilinx devices, this is done via the IBUFGDS, BUFGCE_DIV and BUFG primitives. The clock ``dac_clk_in_p`` is passed through these primitives in order to obtain the divided clock: through IBUFGDS, then BUFGCE_DIV to BUFG. The core and the interface run at the same clock frequency.

Internal Interface Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main purpose of all (including this) ADI IP cores is to provide a common, well-defined internal interface within the FPGA. This interface consists of the following signals per channel, except for VALID which is common to all channels.

VALID
^^^^^

It is always set to logic 1 and indicates a valid sample on each DATA port. Because it is in the transmit (DAC) direction, this indicates the current sample is being read by the core.

ENABLE
^^^^^^

The enable signal is only for software use and it is controlled by the corresponding register bit. The core simply reflects the programmed bit as an output port. In ADI reference projects, this bit is used to activate the channel that one is interested in. It is then used by the UPACK core to route the data based on total number of channels and the selected number of channels. As an example, AXI_AD9783 supports a total of 2 channels, 64 bits each. Because the SERDES factor was chosen to be 8, we have 4 samples of 16 bits each, on I channel and Q channel also, resulting in DMA with 128 bits as data width.

DATA
^^^^

The DATA is the raw analog samples, and 4096 samples generated by PRBS are sent. It follows two simple rules.

-  The samples are always 16 bits. In the transmit direction, if the DAC data width is less than 16 bits, the most significant bits are used. This allows the same destination portable across different DAC data widths. In other words, if the source is generating a 16 bits tone, the signal appears the same across a 12 bit, 14 bit or 16 bit DAC with only the corresponding amplitude change. The source can thus be independent of the number of bits supported by DAC.
-  The DATA is received and transmitted with most significant sample "newest" regardless of the channel width. In other words, the most significant sample is the "newest" sample. If the total channel width is 64 bits, it carries 4 samples (16 bits) per clock. If we were to name these samples as S3 (bits 63 down to 48), S2 (bits 47 down to 32), S1 (bits 31 down to 16) and S0 (bits 15 down to 0), the following is true. In the transmit direction, S0 is sent first and S3 is sent last to the DAC. The analog samples are S0, S1, S2 and S3 across time with S0 being the oldest and S3 being the newest sample.

Parallel data port interface
----------------------------

| The parallel port data interface consists of up to 18 differential signals, ``dac_clk_out_*``, ``dac_clk_in_*``, and up to 16 data lines (``dac_data_out_*``\ [15:0]).
| DCO is the output clock generated by the AD9783 that is used to clock out the data from the digital data engine.
| The data lines transmit the multiplexed I and Q data words for the I and Q DACs, respectively.
| DCI provides timing information about the parallel data and signals the I/Q status of the data.
| The incoming LVDS data is latched by an internally generated clock referred to as the data sampling signal (DSS). DSS is a delayed version of the main DAC clock signal.
| The clock input signal provides timing information about the parallel data, as well as indicating the destination (that is, I DAC or Q DAC) of the data. The data that is processed on rising edge will be outputted on the I DAC, and the data that is on falling edge will be outputted on Q DAC (see figure below).

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9783_parallel_interface.jpg
   :align: center
   :width: 800px

Calibration of the device
-------------------------

| Calibrating the device means finding the proper value for the SMP_DLY register (see datasheet) in order for the PRBS function (PN23 in this case) to work properly when generating the 4096 samples of data.
| The BIST feature in the AD9783 is a simple type adder and is a user synchronizable BIST feature. When a reading is performed, it adds up all the data that was generated on the rising edges of the ``dac_div_clk`` and it writes it in the registers accessible by the user: the low part of the result is written in register 0x1B, and the high part in 0x1C. For the sum of data from falling edges, read 0x1D and 0x1E respectively.

::

   register 0x1A <- 0x20
   register 0x1A <- 0x00 # to clear the BIST registers 
   register 0x1A <- 0x80 # enable BIST
   # 4096 samples generated by PN23 are sent 
   # send zeroes
   register 0x1A <- 0xC0 # perform BIST read
   # read registers 0x1B, 0x1C for the sum of data from rising edges
   # read registers 0x1D, 0x1E for the sum of data from falling edges

| In register 0x1A, write 0x20 then 0x00 to clear the BIST registers while the IP is writing zeros to the data bits. To enable BIST, write 0x80 to register 0x1A. Afterwards, 4096 samples of data are generated by PN23 PRBS and are sent to the data inputs.
| When all samples are sent, the IP is continuously sending zeros after the samples, while the BIST read is being performed. Sending zeroes after the samples is required in order to maintain the sums unchanged in the registers.
| Perform a BIST read by writing 0xC0 to register 0x1A to receive the unique sum of rising edge data in register 0x1B and register 0x1C and a unique sum of falling edge data in register 0x1D and register 0x1E. These register contents must always give the same values for the same samples each time they are sent.
| In order to change what data is sent, the DAC_DDS_SEL register value should be changed. To send PN23, 0x9 should be written in the register. The address for the DAC_DDS_SEL register is calculated by adding 0x418 (for the first channel) to the offset found in the devicetree, for the device.

Register map
------------


.. note::

   See `resources/fpga/docs/reg_map_description <https://wiki.analog.com/resources/fpga/docs/reg_map_description>`_


Register map - Base addresses for axi_ad9783
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| Address |        | Name        |     |     | Description                                                                                   |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |             |     |     |                                                                                               |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | BASE        |     |     | See the `Base (common to all cores) <https://wiki.analog.com/>`_ table for more detail        |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | TX COMMON   |     |     | See the `DAC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | TX CHANNELS |     |     | See the `DAC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Software Guidelines
-------------------

| The software for this IP can be found as part of the ZCU102 Reference Design at: `ADI Linux repository <https://github.com/analogdevicesinc/linux>`_.
| The IP expects the software run a calibration at least once. It has to find out what value for the SMP_DLY (see in datasheet) is good for the PRBS to work.

References
----------

-  :adi:`AD9783 DAC information <AD9783>`
   \* :adi:`EVAL-AD9783 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9783.html>`
-  :doc:`EVAL-AD9783 with ZCU102 reference design description </wiki-migration/resources/fpga/xilinx/interposer/ad9783>`
-  :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-hdl:`AD9783 IP source code <library/axi_ad9783>`
   \* :git-linux>`__
-  `Ultrascale SelectIO <https::`ADI Linux repository </www.xilinx.com/support/documentation/user_guides/ug571-ultrascale-selectio.pdf>`
   \* `UltraScale Architecture Clocking Resources User Guide <https://www.xilinx.com/support/documentation/user_guides/ug572-ultrascale-clocking.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
