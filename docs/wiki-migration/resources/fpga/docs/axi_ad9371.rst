AXI_AD9371 (Obsolete)
=====================

.. important::

   This page is kept for historical reasons. The same functionalities are implemented using the :doc:`generic JESD204 TPL IPs </wiki-migration/resources/fpga/peripherals/jesd204>`


| The :git-hdl:`library/axi_ad9371` IP core interfaces to the :adi:`AD9371` device. This documentation only covers the IP core and requires that one must be familiar with the device for a complete and better understanding.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`, and for DACs: :doc:`axi_dac_ip </wiki-migration/resources/fpga/docs/axi_dac_ip>`.

Features
--------

-  AXI Lite control/status interface
-  Hardware and software DC filtering
-  IQ correction
-  Internal DDS
-  Receive and transmit loopback
-  Supports both Altera and Xilinx devices

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad9371_2.svg
   :alt: AXI_AD9371 Block diagram
   :align: center

Functional Description
----------------------

| The axi_ad9371 cores architecture contains:
| \* :git-hdl:`Interface <library/axi_ad9371/axi_ad9371_if.v>` module, which implements the application layer of the JESD20B interface. This interface is connected to the JESD204B IP core.

-  :git-hdl:`Receive <library/axi_ad9371/axi_ad9371_rx.v>` module, which contains:

   -  :git-hdl:`ADC channel processing <library/axi_ad9371/axi_ad9371_rx_channel.v>` modules, one for each channel (receive path supports 4 channels)
      \* data processing modules (:git-hdl:`DC filter <library/xilinx/common/ad_dcfilter.v>`, :git-hdl:`IQ Correction <library/common/ad_iqcor.v>` and :git-hdl:`Data format control <library/common/ad_datafmt.v>`)

::

         * [[:git-hdl:`library/common/up_adc_channel`.v| ADC Channel register map]]
       * [[:git-hdl:`library/common/up_adc_common`.v| ADC Common register map]]
   * [[:git-hdl:`library/axi_ad9371/axi_ad9371_rx_os`.v| Observation]] module, which has the same architecture as the **Receive module**, but supports just 2 channels
   * [[:git-hdl:`library/axi_ad9371/axi_ad9371_tx`.v| Transmit]] module, which contains:
     * [[:git-hdl:`library/axi_ad9371/axi_ad9371_tx_channel`.v| DAC channel processing]] modules, one for each channel \\
       * Different data generators ([[:git-hdl:`library/common/ad_dds`.v| DDS]], pattern)
       * [[:git-hdl:`library/common/ad_iqcor`.v| IQ Correction]] 
       * [[:git-hdl:`library/common/up_dac_channel`.v| DAC Channel register map]]
     * [[:git-hdl:`library/common/up_delay_cntrl`.v| Delay Control]] and [[:git-hdl:`library/common/up_dac_common`.v| DAC Common register map]]
   * [[:git-hdl:`library/common/up_axi`.v| AXI to uP interface wrapper]] modules. You can find information about the uP interface [[/resources/fpga/docs/up_if|here]].\\

Interface Description
---------------------

The interface module of the core is connected to the JESD204B IP core and does a simple realignment of the data stream.

Parameters
----------

+--------------------------+----------------------------------------------------------------------------------------+---------------+
| Name                     | Description                                                                            | Default Value |
+==========================+========================================================================================+===============+
| ``ID``                   | Core ID should be unique for each ad9371 IP in the system                              | 0             |
+--------------------------+----------------------------------------------------------------------------------------+---------------+
| ``DEVICE_TYPE``          | Used to select between 7 Series (0), Virtex 6 (1) or Ultrascale (2) for Xilinx devices | 0             |
+--------------------------+----------------------------------------------------------------------------------------+---------------+
| ``ADC_DATAPATH_DISABLE`` | Disable the receive data path modules.                                                 | 0             |
+--------------------------+----------------------------------------------------------------------------------------+---------------+
| ``DAC_DATAPATH_DISABLE`` | Disable the transmit data path modules.                                                | 0             |
+--------------------------+----------------------------------------------------------------------------------------+---------------+

I/O interface and signals
-------------------------

+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| Interface                                          | Pin                 | Type             | Description                                                                                 |
+====================================================+=====================+==================+=============================================================================================+
| **Receive interface from JESD204B IP**             |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_clk``         | ``input``        | Rx core clock from the GTs, in general clock rate is (Lane Rate)/40.                        |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_valid``    | ``input``        | This signal is unused; is defined just to make tools happy.                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_sof``      | ``input[3:0]``   | Frame boundary indication signals. Indicate the byte position of the first byte of a frame. |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_data``     | ``input[63:0]``  | Received data stream from the JESD204B IP.                                                  |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_ready``    | ``output``       | This signal is tied to one; is defined just to make tools happy.                            |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **Observation receive interface from JESD204B IP** |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_os_clk``      | ``input``        | Rx core clock from the GTs, in general clock rate is (Lane Rate)/40.                        |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_os_valid`` | ``input``        | This signal is unused; is defined just to make tools happy.                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_os_sof``   | ``input[3:0]``   | Frame boundary indication signals. Indicate the byte position of the first byte of a frame. |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_os_data``  | ``input[63:0]``  | Received data stream from the JESD204B IP.                                                  |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_rx_os_ready`` | ``output``       | This signal is tied to one; is defined just to make tools happy.                            |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **Transmit interface to JESD204B IP**              |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_clk``         | ``input``        | Tx core clock from the GTs, in general clock rate is (Lane Rate)/40.                        |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_tx_valid``    | ``output``       | This signal is tied to one; is defined just to make tools happy.                            |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_tx_data``     | ``output[63:0]`` | Transmitted data stream to the JESD204B IP.                                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_tx_ready``    | ``input``        | This signal is not used; is defined just to make tools happy.                               |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **Transmit master/slave**                          |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_sync_in``     | ``input``        | Synchronization signal of the transmit path for slave devices (ID>0)                        |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_sync_out``    | ``output``       | Synchronization signal of the transmit path for master device (ID==0)                       |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **Receive FIFO interface (for DMA)**               |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_enable_*``    | ``output``       | If set, the channel is enabled (one for each channel)                                       |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_valid_*``     | ``output``       | Indicates valid data at the current channel (one for each channel)                          |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_data_*``      | ``output[15:0]`` | Received data output (one for each channel)                                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_dovf``        | ``input``        | Data overflow, must be connected to the DMA                                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_dunf``        | ``input``        | Data underflow, must be connected to the DMA                                                |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **Observation FIFO interface (for DMA)**           |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_os_enable_*`` | ``output``       | If set, the channel is enabled (one for each channel)                                       |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_os_valid_*``  | ``output``       | Indicates valid data at the current channel (one for each channel)                          |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_os_data_*``   | ``output[31:0]`` | Received data output (one for each channel)                                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_os_dovf``     | ``input``        | Data overflow, must be connected to the DMA                                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``adc_os_dunf``     | ``input``        | Data underflow, must be connected to the DMA                                                |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **Transmit FIFO interface (for DMA)**              |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_enable_*``    | ``output``       | If set, the channel is enabled (one for each channel)                                       |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_valid_*``     | ``output``       | Indicates valid data request at the current channel (one for each channel)                  |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_data_*``      | ``input[31:0]``  | Transmitted data output (one for each channel)                                              |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_dovf``        | ``input``        | Data overflow, must be connected to the DMA                                                 |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``dac_dunf``        | ``input``        | Data underflow, must be connected to the DMA                                                |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
| **AXI Slave Memory Mapped interface**              |                     |                  |                                                                                             |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+
|                                                    | ``s_axi_*``         |                  | Standard AXI Slave Memory Map interface                                                     |
+----------------------------------------------------+---------------------+------------------+---------------------------------------------------------------------------------------------+

Register Map
------------

The register map of the core contains instances of several generic register maps like ADC common, ADC channel, DAC common, DAC channel etc. The following table presents the base addresses of each instance, after that can be found the detailed description of each generic register map. The absolute address of a register should be calculated by adding the instance base address to the registers relative address.

Register Map base addresses for axi_ad9371
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| Address |        | Name           |     |     | Description                                                                                   |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |                |     |     |                                                                                               |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | BASE           |     |     | See the `Base (common to all cores) <https://wiki.analog.com/>`_ table for more detail        |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | RX COMMON      |     |     | See the `ADC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | ADC TPL        |     |     | See the `JESD TPL <https://wiki.analog.com/>`_ table for more detail                          |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | RX CHANNELS    |     |     | See the `ADC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | TX COMMON      |     |     | See the `DAC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | DAC TPL        |     |     | See the `JESD TPL <https://wiki.analog.com/>`_ table for more detail                          |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x1000  | 0x4000 | TX CHANNELS    |     |     | See the `DAC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x2000  | 0x8000 | RX OS COMMON   |     |     | See the `ADC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x2000  | 0x8000 | RX OS CHANNELS |     |     | See the `ADC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+----------------+-----+-----+-----------------------------------------------------------------------------------------------+

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

.. include:: hdl/regmap.rst

Software Guidelines
-------------------

| The software for this IP can be found as part of the FMCOMMS2/3/4/5 Reference Design at :git-no-OS:`No-Os Software <projects/ad9371>`.
| Linux is supported also using :git-linux>`__

References
----------

-  `ad9371 IP source code <https::`ADI Linux repository </github.com/analogdevicesinc/hdl/tree/hdl_2019_r2/library/axi_ad9371>`
   \* :adi:`ad9371 chip information <ad9371>`
   \* :doc:`AD9371 & AD9375 Prototyping Platform User Guide </wiki-migration/resources/eval/user-guides/mykonos>`
   \* :doc:`ADI Reference designs architecture </wiki-migration/resources/fpga/docs/arch>`
   \* :git-no-OS:`No-Os Software <projects/ad9371>`
-  :git-linux>`__
-  `7 Series IO <https::`ADI Linux repository </www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`
   \* `7 Series Clocking <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
   \* `7 Series libraries <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2015_2/ug953-vivado-7series-libraries.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
