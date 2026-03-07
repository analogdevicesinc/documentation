DAC JESD204B/C Transport Peripheral
===================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/ad_ip_jesd204_tpl_dac/index.html\


The DAC JESD204B/C Transport Peripheral (AD-IP-JESD204-TRANSPORT-DAC) implements the transport level handling of a JESD204B/C transmitter device. It is compatible with a `wide range of Analog Devices high-speed digital-to-analog converters <https://wiki.analog.com/>`_.

The core handles the JESD204B/C framing of the user-provided payload data. In addition it is capable of generating standard and user-defined test-pattern data for interface verification. It also features a per-channel dual-tone DDS that can be used to dynamically generate test-tones.

The peripheral can be configured at runtime through a AXI4-Lite memory mapped register map.

Features
--------

-  ADI high-speed DAC compatible JESD204B/C data framing
-  Test-pattern generator for interface verification
-  Per-channel dual-tone DDS (optional)
-  Runtime re-configurability through memory-mapped register interface (AXI4-Lite)

Files
-----

`ad_ip_jesd204_tpl_dac.v <https://github.com/hdl?master/library/jesd204/ad_ip_jesd204_tpl_dac/ad_ip_jesd204_tpl_dac.v>`_

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/ad_ip_jesd204_transport_dac.png
   :align: center

Synthesis Configuration Parameters
----------------------------------

+--------------------------+---------------------------------------------------+---------+
| Name                     | Description                                       | Default |
+==========================+===================================================+=========+
| ``ID``                   | Instance identification number.                   | 0       |
+--------------------------+---------------------------------------------------+---------+
| ``NUM_LANES``            | Number of lanes supported by the peripheral.      | 4       |
|                          | Equivalent to JESD204 ``L`` parameter.            |         |
+--------------------------+---------------------------------------------------+---------+
| ``NUM_CHANNELS``         | Number of converters supported by the peripheral. | 2       |
|                          | Equivalent to JESD204 ``M`` parameter.            |         |
+--------------------------+---------------------------------------------------+---------+
| ``SAMPLES_PER_FRAME``    | Number of samples per frame.                      | 1       |
|                          | Equivalent to JESD204 ``S`` parameter.            |         |
+--------------------------+---------------------------------------------------+---------+
| ``CONVERTER_RESOLUTION`` | Resolution of the converter.                      | 16      |
|                          | Equivalent to JESD204 ``N`` parameter.            |         |
+--------------------------+---------------------------------------------------+---------+
| ``BITS_PER_SAMPLE``      | Number of bits per sample.                        | 16      |
|                          | Equivalent to JESD204 ``NP`` parameter.           |         |
+--------------------------+---------------------------------------------------+---------+
| ``OCTETS_PER_BEAT``      | Number of bytes per beat for each link.           | 4       |
+--------------------------+---------------------------------------------------+---------+
| ``DDS_TYPE``             | DDS Type. Set 1 for CORDIC or 2 for Polynomial    | 1       |
+--------------------------+---------------------------------------------------+---------+
| ``DDS_CORDIC_DW``        | CORDIC DDS Data Width                             | 16      |
+--------------------------+---------------------------------------------------+---------+
| ``DDS_CORDIC_PHASE_DW``  | CORDIC DDS Phase Width                            | 16      |
+--------------------------+---------------------------------------------------+---------+
| ``DATAPATH_DISABLE``     | Disable instantiation of DDS core.                | 0       |
+--------------------------+---------------------------------------------------+---------+

Signal and Interface Pins
-------------------------

+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                        | Type                         | Description                                                                                                                                                                                                                     |
+=============================+==============================+=================================================================================================================================================================================================================================+
| Configuration interface     |                              |                                                                                                                                                                                                                                 |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``s_axi_aclk``              | Clock                        | All ``S_AXI`` signals and ``irq`` are synchronous to this clock.                                                                                                                                                                |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``s_axi_aresetn``           | Synchronous active low reset | Resets the internal state of the peripheral.                                                                                                                                                                                    |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``S_AXI``                   | AXI4-Lite bus slave          | Memory mapped AXI-lite bus that provides access to modules register map.                                                                                                                                                        |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link layer interface        |                              |                                                                                                                                                                                                                                 |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``link_clk``                | Clock                        | :doc:`Device clock </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_glossary>` for the JESD204B/C interface. Must be line clock / 40 for 204B correct operation. Must be line clock / 66 for correct 204C operation. |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``LINK_DATA``               | AXI4-Streaming interface     | Framed transmit data towards link layer.                                                                                                                                                                                        |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Application layer interface |                              |                                                                                                                                                                                                                                 |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``enable``                  | Output                       | Request signal for each channel.                                                                                                                                                                                                |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``dac_valid``               | Output                       | Qualifier signal for each channel. Always '1'.                                                                                                                                                                                  |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``dac_ddata``               | Input                        | Raw application layer data, every channel concatenated.                                                                                                                                                                         |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``dac_dunf``                | Input                        | Application layer underflow.                                                                                                                                                                                                    |
+-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Register Map
------------

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

Theory of Operation
-------------------

Data paths
~~~~~~~~~~

The data is intended for the DAC can have multiple sources:

-  **DMA source** Raw data can be accepted from a external block representing the Application layer.
-  **DDS source** For each DAC channel a dual-tone can be generated by a DDS core.
-  **PRBS source** For each DAC channel one of the following PN sequence can be selected: PN7, PN15, inverted PN7, inverted PN15

Interfaces and Signals
~~~~~~~~~~~~~~~~~~~~~~

Application layer interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The application layer connects to the framer block when the DMA source is selected. The framer module takes sample data and maps it onto the format that the JESD204 link expects for the specified framer configuration.

| The data in the application layer interface ``dac_ddata`` is expected to have the following layout:
| MSB LSB

::

     [ MmSn, ..., MmS1, MnS0, ..., M1Sn, ... M1S1, M1S0, M0Sn, ... M0S1, M0S0 ] 

Where MjSi refers to the i-th sample of the j-th converter. With m being the number of converters and n the number of samples per converter per beat.

The core asserts the ``enable`` signal for each channel that is enabled by the software. The ``dac_ddata`` data bus must contain data for each channel regardless if the channels are enabled or not.

Link layer interface
^^^^^^^^^^^^^^^^^^^^

The link layer interface description can be found in the :doc:`User Data Interface </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>` section of the :doc:`JESD204B/C Link Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>` IP.

Clock Monitor
^^^^^^^^^^^^^

The ``REG_STATUS`` (``0x054``) register ``CLK_FREQ`` field allows to determine the clock rate of the device clock (``link_clk``) relative to the AXI interface clock (``s_axi_aclk``). This can be used to verify that the device clock is running at the expected rate.

The number is represented as unsigned 16.16 format. Assuming a 100MHz processor clock this corresponds to a resolution of 1.523kHz per LSB. A raw value of 0 indicates that the link clock is currently not active.

External synchronization
^^^^^^^^^^^^^^^^^^^^^^^^

By setting the ``EXT_SYNC`` parameter of the IP to 1 an external synchronization signal ``dac_sync_in`` can be used to trigger data movement from user application layer to the link layer, reset internal DDS cores or PRBS generators. If the ``EXT_SYNC`` parameter is set to zero the external signal is ignored and only a software controlled reset happens inside the DDS,PRBS logic.

The external synchronization signal should be synchronous with the dac clock. Synchronization will be done on the rising edge of the signal.

The self clearing ``SYNC`` control bit from the ``REG_CNTRL_1`` (``0x44``) register will arm the trigger logic to wait for the external sync signal. The ``DAC_SYNC_STATUS`` status bit from the ``REG_SYNC_STATUS`` (``0x68``) register will show that the synchronization is armed but the synchronization signal has not yet been received.

Once the sync signal is received the data will start to flow and the ``DAC_SYNC_STATUS`` status bit will reflect that with a deassertion.

While the synchronization mechanism is armed the ``dac_valid`` output signal is gated until the trigger signal is received. The gating happens only during this period, meaning that ``dac_valid`` will stay high in all other cases (normal operation).

Restrictions
------------

| Reduced number of octets-per-frame (``F``) settings. The following values are supported by the peripheral: 1, 2, 4

-  Starting from :git-hdl:`this <commit/454b900f90081fb95be857114e768f662178c8bd>` commit this restriction no longer applies

Software Support
----------------

.. important::

   To ensure correct operation it is highly recommended to use the Analog Devices provided JESD204B/C software packages for interfacing the peripheral. Analog Devices is not able to provide support in case issues arise from using custom low-level software for interfacing the peripheral.


Supported Devices
-----------------

.. include:: ../jesd204.rst

.. include:: ../jesd204.rst

.. include:: ../jesd204.rst

More Information
----------------

-  :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>`
-  :doc:`Glossary of terms </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_glossary>`
-  `HDL User Guide <https://wiki.analog.com/../../docs/hdl>`_

Technical Support
-----------------

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Video, Audio, etc) via the :ez:`EngineerZone <community/fpga>`.
