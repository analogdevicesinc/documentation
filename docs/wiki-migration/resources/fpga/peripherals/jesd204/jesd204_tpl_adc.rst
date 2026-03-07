ADC JESD204B/C Transport Peripheral
===================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/ad_ip_jesd204_tpl_adc/index.html\


The ADC JESD204B/C Transport Peripheral implements the transport level handling of a JESD204B/C transmitter device. It is compatible with a `wide range of Analog Devices high-speed analog-to-digital converters <https://wiki.analog.com/>`_.

The core handles the JESD204B/C de-framing of the payload data.

The peripheral can be configured at runtime through a AXI4-Lite memory mapped register map.

Features
--------

-  ADI high-speed ADC compatible JESD204B/C data de-framing
-  Test-pattern checker
-  Per-channel data formatting (sign-extension, two's complement to offset binary)
-  Runtime re-configurability through memory-mapped register interface (AXI4-Lite)

Files
-----

`ad_ip_jesd204_tpl_adc.v <https://github.com/hdl?/master/library/jesd204/ad_ip_jesd204_tpl_adc/ad_ip_jesd204_tpl_adc.v>`_

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/ad_ip_jesd204_transport_adc.png
   :alt: AD-IP-JESD204-TRANSPORT-ADC block diagram
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
| ``TWOS_COMPLEMENT``      | PRBS data format.                                 | 1       |
+--------------------------+---------------------------------------------------+---------+
| ``PN7_ENABLE``           | Enable PN7 check.                                 | 1       |
+--------------------------+---------------------------------------------------+---------+
| ``PN15_ENABLE``          | Enable PN15 check.                                | 1       |
+--------------------------+---------------------------------------------------+---------+
| ``PN31_ENABLE``          | Enable PN31 check.                                | 1       |
+--------------------------+---------------------------------------------------+---------+

Signal and Interface Pins
-------------------------

+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                        | Type                           | Description                                                                                                                                                                                                                          |
+=============================+================================+======================================================================================================================================================================================================================================+
| ``s_axi_aclk``              | Clock                          | All ``S_AXI`` signals are synchronous to this clock.                                                                                                                                                                                 |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``s_axi_aresetn``           | Synchronous active low reset   | Resets the internal state of the peripheral.                                                                                                                                                                                         |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``S_AXI``                   | AXI4-Lite bus slave            | Memory mapped AXI-lite bus that provides access to modules register map.                                                                                                                                                             |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link layer interface        |                                |                                                                                                                                                                                                                                      |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``link_clk``                | Clock                          | :doc:`Device clock </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_glossary>` for the JESD204B interface. Must be line clock / 40 for correct 204B operation. Must be line clock / 66 for correct 64b66b 204C operation. |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``LINK_DATA``               | AXI4-Streaming interface slave | JESD204 link data interface.                                                                                                                                                                                                         |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Application layer interface |                                |                                                                                                                                                                                                                                      |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``enable``                  | Output                         | Channel enable indicator.                                                                                                                                                                                                            |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``adc_valid``               | Output                         | Qualifier signal for each channel. Always '1'.                                                                                                                                                                                       |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``adc_data``                | Output                         | Raw application layer data, every channel concatenated.                                                                                                                                                                              |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``adc_dovf``                | Input                          | Application layer overflow.                                                                                                                                                                                                          |
+-----------------------------+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The S_AXI interface is synchronous to the s_axi_aclk clock. All other signals and interfaces are synchronous to the device_clk clock.

Register Map
------------

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

Theory of Operation
-------------------

Interfaces and Signals
~~~~~~~~~~~~~~~~~~~~~~

Configuration Interface
^^^^^^^^^^^^^^^^^^^^^^^

The peripheral features a register map configuration interface that can be accessed through the AXI4-Lite ``S_AXI`` port. The register map can be used to configure the peripherals operational parameters, query the current status of the device and query the features supported by the device.

Link layer interface
^^^^^^^^^^^^^^^^^^^^

The link layer interface description can be found in the :doc:`User Data Interface </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>` section of the :doc:`JESD204B/C Link Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>` IP.

Application layer interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The application layer is connected to the deframer block output. The deframer module creates sample data from the lane mapped and formatted JESD204 link data based on the specified deframer configuration.

| The data in the application layer interface ``adc_data`` has the following layout:
| MSB LSB

::

     [ MmSn, ..., MmS1, MnS0, ..., M1Sn, ... M1S1, M1S0, M0Sn, ... M0S1, M0S0 ] 

Where MjSi refers to the i-th sample of the j-th converter. With m being the number of converters and n the number of samples per converter per beat.

The core asserts the ``enable`` signal for each channel that is enabled by the software.

Clock Monitor
^^^^^^^^^^^^^

The ``REG_STATUS`` (``0x054``) register ``CLK_FREQ`` field allows to determine the clock rate of the device clock (``link_clk``) relative to the AXI interface clock (``s_axi_aclk``). This can be used to verify that the device clock is running at the expected rate.

The number is represented as unsigned 16.16 format. Assuming a 100MHz processor clock this corresponds to a resolution of 1.523kHz per LSB. A raw value of 0 indicates that the link clock is currently not active.

Data Formatter
^^^^^^^^^^^^^^

The component is configured by the ``REG_CHAN_CNTRL`` register ``FORMAT_SIGNEXT,FORMAT_TYPE,FORMAT_ENABLE`` fields. The block introduces one clock cycle latency.

PRBS Check
^^^^^^^^^^

The block can monitor and compare the incoming deframed raw data against PN9,PN23 and PN7, PN15, PN31 (if enabled) patterns selected by the ``ADC_PN_SEL`` field of ``REG_CHAN_CNTRL_3`` register.

========== ==== ===========
ADC_PN_SEL PN   ENABLE
========== ==== ===========
0          PN9  1
1          PN23 1
4          PN7  PN7_ENABLE
5          PN15 PN15_ENABLE
7          PN31 PN31_ENABLE
========== ==== ===========

Before performing these tests you need to make sure that the ADC OUTPUT FORMAT is set according to the ``TWOS_COMPLEMENT`` synthesis parameter.

For each channel mismatches are reported in ``PN_ERR`` and ``PN_OOS`` fields of the ``REG_CHAN_STATUS`` register.

External synchronization
^^^^^^^^^^^^^^^^^^^^^^^^

An external synchronization signal ``adc_sync_in`` can be used to trigger data movement from the link layer to user application layer.

The external synchronization signal should be synchronous with the adc clock. Synchronization will be done on the rising edge of the signal.

The self clearing ``SYNC`` control bit from the ``REG_CNTRL (0x44)`` register will arm the trigger logic to wait for the external sync signal. The ``ADC_SYNC`` status bit from ``REG_SYNC_STATUS (0x68)`` register will show that the synchronization is armed but the synchronization signal has not yet been received.

Once the sync signal is received the data will start to flow and the ``ADC_SYNC`` status bit will reflect that with a deassertion.

While the synchronization mechanism is armed, the ``adc_rst`` output signal is set so downstream logic can be cleared in order to have a fresh start once the trigger is received.

Software Support
----------------

.. important::

   To ensure correct operation it is highly recommended to use the Analog Devices provided JESD204B/C software packages for interfacing the peripheral. Analog Devices is not able to provide support in case issues arise from using custom low-level software for interfacing the peripheral.


Restrictions
------------

| Reduced number of octets-per-frame (``F``) settings. The following values are supported by the peripheral: 1, 2, 4

-  Starting from :git-hdl:`this <commit/454b900f90081fb95be857114e768f662178c8bd>` commit this restriction no longer applies

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
