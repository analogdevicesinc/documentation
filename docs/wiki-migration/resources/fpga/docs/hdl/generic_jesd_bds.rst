Generic JESD204B block designs
==============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/generic_jesd_bds/index.html\


Using the generic building blocks from the ADI IP library together with the JESD framework, parametrizable block designs can be built to interface ADI DACs and ADCs in various JESD modes.

Changing the Link parameters
----------------------------

Typically projects are built and configured to exercise the DAC/ADC devices maximum capability using all available lanes, this corresponds to a single JESD operation mode. In order to switch to other modes, the generic block designs can be reconfigured by changing its parameters. These parameters map to the JESD link parameters. See the example below taken from :git-hdl:`this block design <projects/adrv9009/common/adrv9009_bd.tcl>`:

.. container:: prewrap 500px

   
   .. code:: tcl
   
      # TX parameters
      set TX_NUM_OF_LANES 4      ; # L
      set TX_NUM_OF_CONVERTERS 4 ; # M
      set TX_SAMPLES_PER_FRAME 1 ; # S
      set TX_SAMPLE_WIDTH 16     ; # N/NP
   
      set TX_SAMPLES_PER_CHANNEL 2 ; # L * 32 / (M * N)
   


.. important::

   Changing the number of lanes parameter will affect the top level file, as the constraints file. If the number of lanes is reduced both files must be updated to remove references to the unused lanes.


JESD204B Glossary
=================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/index.html\


Control characters
------------------

======= ===== =====================================================
**/R/** K28.0 Initial lane alignment sequence multi-frame start.
**/A/** K28.3 Lane alignment
**/Q/** K28.4 Initial lane alignment sequence configuration marker.
**/K/** K28.5 Code group synchronization.
**/F/** K28.7 Frame synchronization.
======= ===== =====================================================

Abbreviations
-------------

========= =========================================
**CGS**   Code Group Synchronization
**ILAS**  Initial Lane Alignment Sequence
**LMFC**  Local Multi Frame Clock
**LEMC**  Local Extended Multiblock Clock
**MCDA**  Multiple Converter Device Alignment
**NMCDA** No Multiple Converter Device Alignment
**RBD**   RX Buffer Delay
**EMB**   Extended Multiblock
**EoMB**  End-of-multiblock sequence (00001)
**EoEMB** End of extended multiblock identifier bit
========= =========================================

Link parameters
---------------

====== ===============================================
**L**  Lane Count
**M**  Converter Count
**F**  Octets per Frame per Lane
**S**  Samples per Converter per Frame
**NP** Total Number of Bits per Sample
**N**  Converter Resolution
**K**  Frames per Multiframe
**HD** High Density User Data Format
**E**  Number of multiblocks in an extended multiblock
====== ===============================================

Clocks
------

+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **character clock**  | Clock with which 8b10b characters and octets are generated.                                                                                                                                                         |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **conversion clock** | Clock used by a converter device to perform the A2D or D2A conversion.                                                                                                                                              |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **link clock**       | Link parallel clock feeding the link layer, lane rate / 40 or lane rate / 80 for 204B links, lane rate / 66 for 204C 64b66b links                                                                                   |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **device clock**     | Master clock supplied to the JESD204B device from which all other clock signals must be derived. In context of FPGA is an integer multiple of frame clock, used directly in link, transport and application layers. |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **frame clock**      | Clock rate at which samples are generated/processed. Has the same rate as the conversion clock, except for interpolating DACs or decimating DACs, where it is slower by the interpolation/decimation factor.        |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **line clock**       | Clock for the high-speed serial interface.                                                                                                                                                                          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **local clock**      | A clock generated inside a JESD204B device.                                                                                                                                                                         |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **SYSREF clock**     | Slow clock used for cross-device synchronization purposes.                                                                                                                                                          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

All clocks inside a JESD204B system must have a integer relationship.


.. tip::

   In JESD links the following equation must hold:

   
   :math:`M \times S \times NP = L \times F \times 8` or :math:`M/L = (F/S) \times (8/NP)`
   
   Based on this equation a missing parameter can be calculated from the others.


Generic Tx path
---------------

The below diagram presents a generic JESD Tx path from application layer to the FPGA boundary. The application layer is connected to the Tx path through the DAC Transport Layer which for each converter accepts a data beat on every cycle. The width of data beat is defined by the SPC and NP parameter. SPC represents the number of samples per converter per data clock cycle. SPC must be a natural number (greater than one and a whole number).

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/generic_tx_jesd_path.png
   :align: center
   :width: 600px

On each clock cycle the Link Layer accepts 32 bits per every lane as a constraint from the physical layer that is configured to 32bit mode. This means that for each clock cycle the application layer must provide enough samples for each converter so the transport layer can fill 32 bits of data for each lane. Due this constraint the following equation must hold: :math:`L \times 32 = M \times NP \times SPC`

In such design the following constraints apply to the transport layer:

-  F = {1, 2, 4}
-  NP = {8, 16}

More information on the DAC Transport layer can be found in :doc:`DAC JESD204B Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` page.

The Link layer consists from L number of lanes which form the link. More information on the Tx Link layer can be found in :doc:`JESD204B Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>` page.

Example 1 Tx link for L=4; M=1; S=1; F=2; NP=16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| In this mode the Transport Layer will output two frames in every clock cycle. 32 bits / (F\*8) = 2;
| The application layer must provide 8 samples each cycle to be able to fill the 2 frames. SPC = (L\*32) / (M\*NP) = (4\*32) / (1\*16) = 128/16 = 8 |image1|

Example 2 Tx link for L=4; M=4; S=1; F=2; NP=16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| In this mode the Transport Layer will output two frames in every clock cycle. 32 bits / (F\*8) = 2;
| The application layer must provide 8 samples each cycle to be able to fill the 2 frames. SPC = (L\*32) / (M\*NP) = (4\*32) / (4\*16) = 128/64 = 2

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/generig_jesd_tx_samples_ex2.png
   :align: center
   :width: 600px

Generic Rx path
---------------

The below diagram presents a generic JESD Rx path. The application layer is connected to the Rx path through the ADC Transport Layer which for each converter generates a data beat on every cycle. The width of data beat is defined by the SPC and NP parameter. SPC represents the number of samples per converter per data clock cycle. SPC must be a natural number (greater than one and a whole number).

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/generic_rx_jesd_path.png
   :align: center
   :width: 600px

On each clock cycle the Link Layer generates 32 bits per every lane as it is constrained from the physical layer that is configured to 32bit mode. This means that for each clock cycle the application layer must accept enough samples for each converter so the transport layer use 32 bits of data from each lane.

In such design the following constraints apply to the transport layer:

-  F = {1, 2, 4}
-  NP = {8, 16}

More information on the ADC Transport layer can be found in :doc:`ADC JESD204B Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_adc>` page.

The Link layer consists from L number of lanes which form the link. More information on the Rx Link layer can be found in :doc:`JESD204B Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>` page.

Example Rx link for L=4; M=1; S=1; F=2; NP=16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| In this mode the Transport Layer will accept two frames in every clock cycle. 32 bits / (F\*8) = 2;
| The application layer must accept 8 samples each cycle so the transport layer can deframe the 2 frames. SPC = (L\*32) / (M\*NP) = (4\*32) / (1\*16) = 128/16 = 8 |image2|

.. note::

   Such a parametrizable block design was built for the :doc:`ADRV9009 Prototyping Platform </wiki-migration/resources/eval/user-guides/adrv9009>` and can be found `here <https://wiki.analog.com/https/github.com/analogdevicesinc/hdl/blob/master/projects/adrv9009/common/adrv9009_bd.tcl>`_.


JESD modes with F=8
-------------------

In a period of LinkClk the Link layer always handles 32 bits per lane. The transport layer running at a same clock rate can fill the 32 bits with frames of 1,2 or 4 bytes.

However, for a link with L=1, M=4, NP=16 the minimum number of bytes per frame that must be supported is 8 (F=8)

:math:`F= M \times S \times NP / L \times 8 ; F = 8 \times S`

Tx path for F=8
~~~~~~~~~~~~~~~

In order to comply the requirement that in every DataClk period for each converter from the application layer a sample must be accepted (64 bits in this case), DataClk must be run with half the speed of the LinkClk.

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/f8_tx_jesd_path.png
   :align: center
   :width: 600px

The rate adaptation and synchronization is done with a gearbox which receives its clocks from a PLL that ensures its output clocks are in phase.

Rx path for F=8
~~~~~~~~~~~~~~~

The Rx path is similar to the Tx. In order the transport layer to produce a sample per converter in every clock cycle the Data clock must be ran at half of the link clock speed.

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/f8_rx_jesd_path.png
   :align: center
   :width: 600px

.. note::

   Such a parametrizable block design that supports also F=8 was built for the :doc:`ADRV9009 Prototyping Platform </wiki-migration/resources/eval/user-guides/adrv9009>` and can be found `here <https://wiki.analog.com/https/github.com/ronagyl/hdl/blob/dev_adrv9009_less_lanes/projects/adrv9009/common/adrv9009_bd.tcl>`_.


Useful links
------------

-  :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>`: JESD204 Interface Framework
-  :doc:`UTIL_ADXCVR </wiki-migration/resources/fpga/docs/util_xcvr>`: JESD204B Gigabit Transceiver Interface Peripheral for Xilinx FPGAs
-  :doc:`JESD204B Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>`: JESD204B Link Layer Transmit Peripheral
-  :doc:`JESD204B Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>`: JESD204B Link Layer Receive Peripheral
-  :doc:`ADC JESD204B Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_adc>` : JESD204B Transport Layer Receive Peripheral
-  :doc:`DAC JESD204B Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` : JESD204B Transport Layer Transmit Peripheral

Support
-------

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Video, Audio, etc) via the :ez:`EngineerZone <community/fpga>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/sample_tx_jesd_path.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/sample_rx_jesd_path.png
   :width: 600px
