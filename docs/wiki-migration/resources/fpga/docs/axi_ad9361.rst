AXI_AD9361
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad9361/index.html


| The :git-hdl:`library/axi_ad9361` IP core interfaces to the :adi:`AD9361` device. This documentation only covers the IP core and requires that one must be familiar with the device for a complete and better understanding.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`, and for DACs: :doc:`axi_dac_ip </wiki-migration/resources/fpga/docs/axi_dac_ip>`.

Features
--------

-  AXI Lite control/status interface
-  PRBS monitoring
-  Hardware and software DC filtering
-  IQ correction
-  Internal DDS
-  Programmable line delays
-  Receive and transmit loop back
-  Supports both Altera and Xilinx devices

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9361_3.svg
   :alt: AXI_AD9361 Block diagram
   :align: center

Functional Description
----------------------

| The axi_ad9361 cores architecture contains:
| \* :git-hdl:`Interface <library/axi_ad9361/axi_ad9361.v#L302>` module in either CMOS Dual Port Full Duplex or LVDS mode for :git-hdl:`Intel <library/axi_ad9361/intel>` or :git-hdl:`Xilinx <library/axi_ad9361/xilinx>` devices.
| \* :git-hdl:`Receive <library/axi_ad9361/axi_ad9361_rx.v>` module, which contains:

::

     * [[:git-hdl:`library/axi_ad9361/axi_ad9361_rx_channel`.v|ADC channel processing]] modules, one for each channel \\
       * data processing modules ([[:git-hdl:`library/xilinx/common/ad_dcfilter`.v|DC filter]], [[:git-hdl:`library/common/ad_iqcor`.v|IQ Correction]] and [[:git-hdl:`library/common/ad_datafmt`.v|Data format control]])
       * [[:git-hdl:`library/axi_ad9361/axi_ad9361_rx_pnmon`.v|ADC PN Monitor]]  for interface validation \\
       * [[:git-hdl:`library/common/up_adc_channel`.v|ADC Channel register map]]
     * [[:git-hdl:`library/common/up_delay_cntrl`.v|Delay Control]] and [[:git-hdl:`library/common/up_adc_common`.v|ADC Common register map]]
   * [[:git-hdl:`library/axi_ad9361/axi_ad9361_tx`.v|Transmit]] module, which contains:
     * [[:git-hdl:`library/axi_ad9361/axi_ad9361_tx_channel`.v|DAC channel processing]] modules, one for each channel \\
       * Different data generators ([[:git-hdl:`library/common/ad_dds`.v|DDS]], pattern, PRBS)
       * [[:git-hdl:`library/common/ad_iqcor`.v|IQ Correction]] 
       * [[:git-hdl:`library/common/up_dac_channel`.v|DAC Channel register map]]
     * [[:git-hdl:`library/common/up_delay_cntrl`.v|Delay Control]] and [[:git-hdl:`library/common/up_dac_common`.v|DAC Common register map]]
   * [[:git-hdl:`library/axi_ad9361/axi_ad9361_tdd`.v|TDD control module]] for TDD mode, see more information on the [[/resources/eval/user-guides/ad-pzsdr2400tdd-eb/reference_hdl|HDL support for AD9361 TDD mode]] wiki page.
   * [[:git-hdl:`library/common/up_axi`.v|AXI control and status]] modules. \\

Device (AD9361) Interface Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IP supports both LVDS and CMOS Dual Port Full Duplex interfaces (configurable, see parameters section). It avoids all the programmable flavors of the device interface mess. The interface is in fact quite simple, in LVDS mode samples require two active clock edges and in CMOS mode a single edge. The samples are then delineated in-order using the FRAME signal. This is applicable to both DDR and SDR modes. There is a limitation though, the IP core does NOT support swapping of the data ports in CMOS mode. This option is left as a constraint. As an example the PZSDR projects uses SWAP on some boards based on the board layout.

Let's consider the 2R2T configuration, each frame consists of 4 samples in each direction. In LVDS-DDR mode that is 8 clock edges (4 full clock cycles) identified by a frame pattern of 8'b11110000. The IP interface logic simply collects data on consecutive 8 edges and deframes using the FRAME signal and outputs the samples. The device does the same in the transmit direction. In CMOS mode, the same is done over 4 clock edges.

The interface also provides a single clock tree for the entire core. This clock uses a global buffer that has the minimum skew all across the die. On Altera devices, this is done via the PLL and because the LVDS cores do NOT support a serialization factor of 2, runs at half the interface clock frequency. On Xilinx devices, this is done via the BUFG and the core and interface runs at the same clock frequency.

Altera
^^^^^^

The core is tested to work only on Cyclone V Arrow SOC Kit. Since Altera does half-thought board designs that do not favor FMC bank allocations, we are incapable of validating the core on other devices.

Xilinx
^^^^^^

Alternative Clocking Methods
""""""""""""""""""""""""""""

1. Using MMCM 2. Using BUFIO/BUFR

Alternative Use Models
""""""""""""""""""""""

1. Interface Logic Only 2. Disable DSP Functions 3. Removing AXI interface and Processor Control

Internal Interface Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main purpose of all (including this) ADI IP cores is to provide a common, well-defined internal interface within the FPGA. This interface consists of the following signals per channel.

ENABLE
^^^^^^

The enable signal is strictly for software use and is controlled by the corresponding register bit. The core simply reflects the programmed bit as an output port. In ADI reference projects, this bit is used to activate the channel of interest. It is then used by the PACK/UNPACK cores to route the data based on total number of channels and the selected number of channels. As an example, AXI_AD9361 supports a total of 4 channels 16bits each. This corresponds to a packed channel data width of 64bits. If software enables only two channels the packed 64bits of data is exclusively shared by the enabled 2 channels (each channel gets 32 bits of data).

VALID
^^^^^

The valid signal is sourced by the core to indicate a valid sample on the DATA port. In the receive (ADC) direction this indicates a valid sample and in the transmit (DAC) direction this indicates the current sample is being read by the core. The valid is simply a 'reflective' of the 'sampling rate'. Note that he cores always run at the interface clock. This is to avoid any customized clock handling or transfer within this core. However in many cases interface clock may not be the sampling clock. As an example for AD9361 the interface clock is 244Mhz for a sampling clock of 61MHz. That is each channel's sampling rate is 61MHz. This translates into the VALID signal being asserted once every 4 clocks. In cores where sampling rate is same as the interface clock, VALID is always asserted and may be safely ignored.

A common interpretation of this is that all channels has the same VALID behavior. This is NOT necessarily true. A majority of use cases may have this as a result of data path equivalency. However, if software decides to enable/disable functions differently among channels, the VALID signals of those channels will NOT be the same.

DATA
^^^^

The DATA is the raw Analog samples. It follows two simple rules.

-  The samples are always 16bits, regardless of the ADC/DAC data width. That is the source or destination is intended to handle samples as 16bits. In the transmit direction, if the DAC data width is less than 16bits, the most significant bits are used. In the receive direction, if the ADC data width is less than 16bits, the most significant bits are sign extended. This allows the same source or destination portable across different ADC/DAC data widths. In other words, if the source is generating a 16bits tone the signal appears the same across a 12bit, 14bit or 16bit DAC with only the corresponding amplitude change. The source can thus be independent of the number of bits supported by DAC. In the receive direction, the samples are sign extended. Thus the destination always receives a 16bit sample with different amplitude levels corresponding to the number of bits supported by the ADC. This may seem to break the symmetry rule, but in most DSP functions the samples are rounded up towards the MSB as only precision is allowed to lost or gained at the expense of the LSB bits. The MSB bits retains all the physical nature of the signal.
-  The DATA is received and transmitted with most significant sample "newest" regardless of the channel width. In other words the most significant sample is the "newest" sample. If the total channel width is 64bits, it carries 4 samples (16bits) per clock. If we were to name these samples as S3 (bits 63 down to 48), S2 (bits 47 down to 32), S1 (bits 31 down to 16) and S0 (bits 15 down to 0), the following is true. In the transmit direction, S0 is sent first and S3 is sent last to the DAC. The analog samples are S0, S1, S2 and S3 across time with S0 being the oldest and S3 being the newest sample. In the receive direction, S0 carries the oldest sample received and S3 carries the newest sample from the ADC.

Parameters
----------

+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Name                         | Description                                                                                                                            | Default Value        |
+==============================+========================================================================================================================================+======================+
| ``ID``                       | Core ID should be unique for each AD9361 IP in the system                                                                              | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DEVICE_TYPE``              | Used to select between 7 Series (0), Virtex 6 (1) or Ultrascale (2) for Xilinx devices                                                 | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``MODE_1R1T``                | Used to select between 2RX2TX (0) and 1RX1TX (1) mode.                                                                                 | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``TDD_DISABLE``              | Setting this parameter the TDD control will not be implemented in the core.                                                            | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``CMOS_OR_LVDS_N``           | Defines the physical interface type, set 1 for CMOS and 0 for LVDS                                                                     | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DATAPATH_DISABLE``     | If set, the data path processing logic is not generated in the RX path, and the raw data is pushed directly to the DMA interface.      | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_USERPORTS_DISABLE``    | Disable the User Control ports in receive path.                                                                                        | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DATAFORMAT_DISABLE``   | Disable the Data Format control module.                                                                                                | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_DCFILTER_DISABLE``     | Disable the DC Filter module.                                                                                                          | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_IQCORRECTION_DISABLE`` | Disable the IQ Correction module in receive path.                                                                                      | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DAC_DATAPATH_DISABLE``     | If set, the data path processing logic is not generated in the TX path, and the raw data is pushed directly to the physical interface. | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DAC_IODELAY_ENABLE``       | Set IO_DELAY control in transmit path.                                                                                                 | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DAC_DDS_DISABLE``          | Disable the DDS modules in transmit path.                                                                                              | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DAC_USERPORTS_DISABLE``    | Disable the User Control ports in transmit path.                                                                                       | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DAC_IQCORRECTION_DISABLE`` | Disable the IQ Correction module in transmit path.                                                                                     | 0                    |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``IO_DELAY_GROUP``           | The delay group name which is set for the delay controller                                                                             | "dev_if_delay_group" |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+----------------------+

I/O Interface
-------------

+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| Interface                     | Pin                 | Type             | Description                                                                        |
+===============================+=====================+==================+====================================================================================+
| **LVDS RX interface**         |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rx_clk_in_*``     | ``input``        | LVDS input clock                                                                   |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rx_frame_in_*``   | ``input``        | LVDS input frame signal                                                            |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rx_data_in_*``    | ``input[ 5:0]``  | LVDS input data lines                                                              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **CMOS RX interface**         |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rx_clk_in``       | ``input``        | CMOS input clock                                                                   |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rx_frame_in``     | ``input``        | CMOS input frame signal                                                            |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rx_data_in``      | ``input[11:0]``  | CMOS input data lines                                                              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **LVDS TX interface signals** |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tx_clk_in_*``     | ``output``       | LVDS output clock                                                                  |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tx_frame_in_*``   | ``output``       | LVDS output frame signal                                                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tx_data_in_*``    | ``output[ 5:0]`` | LVDS output data lines                                                             |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **CMOS TX interface signals** |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tx_clk_in``       | ``output``       | CMOS input clock                                                                   |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tx_frame_in``     | ``output``       | CMOS input frame signal                                                            |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tx_data_in``      | ``output[11:0]`` | CMOS input data lines                                                              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **TDD control interface**     |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``enable``          | ``output``       | ENSM control signal, see User Guide for more information                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``txnrx``           | ``output``       | ENSM control signal, see User Guide for more information                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **TDD sync interface**        |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tdd_sync``        | ``input``        | SYNC input for frame synchronization in TDD mode                                   |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``tdd_sync_cntr``   | ``output``       | SYNC output for frame synchronization in TDD mode                                  |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **Delay Clock**               |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``delay_clk``       | ``input``        | Delay clock input for IO_DELAY control, 200 MHz (7 series) or 300 MHz (Ultrascale) |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **Transmit master/slave**     |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_sync_in``     | ``input``        | Synchronization signal of the transmit path for slave devices (ID>0)               |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_sync_out``    | ``output``       | Synchronization signal of the transmit path for master device (ID==0)              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **Core clock and reset**      |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``l_clk``           | ``output``       | This clock should be used for further data processing                              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``clk``             | ``input``        | Must be driven by ``l_clk``                                                        |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``rst``             | ``output``       | Core reset signal                                                                  |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **DMA_RX interface**          |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``adc_enable_*``    | ``output``       | If set, the channel is enabled (one for each channel)                              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``adc_valid_*``     | ``output``       | Indicates valid data at the current channel (one for each channel)                 |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``adc_data_*``      | ``output[15:0]`` | Received data output (one for each channel)                                        |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``adc_dovf``        | ``input``        | Data overflow, must be connected to the DMA                                        |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``adc_dunf``        | ``input``        | Data underflow, must be connected to the DMA                                       |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``adc_r1_mode``     | ``output``       | If set, core is functioning in single channel mode (one I/Q pair)                  |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **DMA_TX interface**          |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_enable_*``    | ``output``       | If set, the channel is enabled (one for each channel)                              |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_valid_*``     | ``output``       | Indicates valid data request at the current channel (one for each channel)         |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_data_*``      | ``input[15:0]``  | Transmitted data output (one for each channel)                                     |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_dovf``        | ``input``        | Data overflow, must be connected to the DMA                                        |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_dunf``        | ``input``        | Data underflow, must be connected to the DMA                                       |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``dac_r1_mode``     | ``output``       | If set, core is functioning in single channel mode (one I/Q pair)                  |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **AXI_S_MM interface**        |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``s_axi_*``         |                  | Standard AXI Slave Memory Map interface                                            |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
| **GPIO interface**            |                     |                  |                                                                                    |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``up_enable``       | ``input``        | GPI control of the ENABLE line in TDD mode, when HDL TDD control is DISABLED       |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``up_txnrx``        | ``input``        | GPI control of the TXNRX line in TDD mode, when HDL TDD control is DISABLED        |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``up_dac_gpio_in``  | ``input[31:0]``  | GPI ports connected to the AXI memory map for custom use                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``up_dac_gpio_out`` | ``output[31:0]`` | GPI ports connected to the AXI memory map for custom use                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``up_adc_gpio_in``  | ``input[31:0]``  | GPI ports connected to the AXI memory map for custom use                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+
|                               | ``up_adc_gpio_out`` | ``output[31:0]`` | GPO ports connected to the AXI memory map for custom use                           |
+-------------------------------+---------------------+------------------+------------------------------------------------------------------------------------+

Register Map
------------


.. note::

   See `resources/fpga/docs/reg_map_description <https://wiki.analog.com/resources/fpga/docs/reg_map_description>`_


Register Map base addresses for axi_ad9361
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| Address |        | Name        |     |     | Description                                                                                      |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |             |     |     |                                                                                                  |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | BASE        |     |     | See the `Base (common to all cores) <https://wiki.analog.com/>`_ table for more detail           |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | RX COMMON   |     |     | See the `ADC Common <https://wiki.analog.com/>`_ table for more detail                           |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | RX CHANNELS |     |     | See the `ADC Channel <https://wiki.analog.com/>`_ table for more detail                          |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | TX COMMON   |     |     | See the `DAC Common <https://wiki.analog.com/>`_ table for more detail                           |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | TX CHANNELS |     |     | See the `DAC Channel <https://wiki.analog.com/>`_ table for more detail                          |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+
| 0x2000  | 0x8000 | TDD CONTROL |     |     | See the `Transceiver TDD Control <https://wiki.analog.com/>`_ table for more detail              |
+---------+--------+-------------+-----+-----+--------------------------------------------------------------------------------------------------+

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Software Guidelines
-------------------

| The software for this IP can be found as part of the FMCOMMS2/3/4/5 Reference Design at: :git-no-OS:`No-Os Software <projects/ad9361>`.
| Linux is supported also using :git-linux>`__

References
----------

-  `AD9361 IP source code <https::`ADI Linux repository </github.com/analogdevicesinc/hdl/tree/master/library/axi_ad9361>`
   \* :adi:`AD9361 chip information <AD9361>`
   \* :adi:`AD9361 User Guide <media/en/technical-documentation/user-guides/AD9361_Reference_Manual_UG-570.pdf>`
-  :doc:`FMCOMMS2 Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>`
   \* :doc:`FMCOMMS4 Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-no-OS:`No-Os Software <projects/ad9361>`
-  :git-linux>`__
-  `7 Series IO <https::`ADI Linux repository </www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`
   \* `7 Series Clocking <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
   \* `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2015_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
