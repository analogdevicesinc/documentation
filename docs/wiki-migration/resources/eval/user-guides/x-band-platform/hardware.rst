X-Band Platform Hardware
========================

The following "shopping list" details what is provided when purchasing the hardware herein and what a user needs to procure separately.

Required Equipment
------------------

Equipment Included with Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADAR1000EVAL1Z
^^^^^^^^^^^^^^

-  1x :doc:`ADAR1000EVAL1Z (Stingray) </wiki-migration/resources/eval/user-guides/stingray>`

   -  Heatsink and H-Frame Mechanical Hardware `Assembly Instructions <https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/stingray_assembly_v2.pdf>`__

-  2x ADAR1000EVAL1Z-ANT 10 GHz Lattice Spacing Antenna Tiles

   -  `32x SMPM Bullets for Antenna Connection <https://www.digikey.com/125-0901-811>`__

-  `2x 12-Pin PMOD 8 Inch Cables <https://www.mouser.com/IDSD-06-D-08.00-T>`__
-  `4x 12-Pin 0.100" Male-Male Header <https://www.digikey.com/TSW-106-22-T-D>`__
-  `2x SMPM-SMA 12 Inch Cable <https://www.centricrf.com/cable-assemblies/sma-cable-assemblies/27-ghz-047-mini-smp-to-sma/c575-047-12-cable-mini-smp-f-to-sma-m-047-flexible-27ghz-vswr-1-35-12/>`__
-  `1x 12V, Wall Supply <https://www.digikey.com/TE240A1251F01>`__

ADXUD1AEBZ
^^^^^^^^^^

-  :doc:`Interposer Board (connect FPGA control lines to XUD1A) </wiki-migration/resources/eval/user-guides/xud1a/user-guide>`
-  `1x SMPM-SMA 12 Inch Cable <https://www.centricrf.com/cable-assemblies/sma-cable-assemblies/27-ghz-047-mini-smp-to-sma/c575-047-12-cable-mini-smp-f-to-sma-m-047-flexible-27ghz-vswr-1-35-12/>`__
-  `RF Shields <https://www.digikey.com/BMI-S-202-C>`__
-  `1x 12V, Wall Supply <https://www.digikey.com/ME30A1203F01>`__

AD9081-FMCA-EBZ
^^^^^^^^^^^^^^^

-  1x 16GB SD Card

ZCU102 FPGA
^^^^^^^^^^^

-  1x Ethernet Cable
-  1x USB to Ethernet Dongle
-  2x USB Micro Cables
-  `1x 12V, Wall Supply <https://www.digikey.com/TE150A1251F01>`__

Additional Required Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _adar1000eval1z-1:

ADAR1000EVAL1Z
^^^^^^^^^^^^^^

-  `2x 12-Pin PMOD 16 Inch Cable <https://www.mouser.com/IDSD-06-D-1600-R>`__

.. note::

   Note that the Stingray board includes 2x cables already (`IDSD-06-D-08.00-T <https://www.mouser.com/IDSD-06-D-08.00-T>`__). One example part number for the second set of cables: `IDSD-06-D-1600 <https://www.mouser.com/IDSD-06-D-1600>`__. (16" long, using these 2 cables together creates a 24" cable).


-  `6x SMPM-SMA 12 Inch Cables <https://www.centricrf.com/cable-assemblies/sma-cable-assemblies/27-ghz-047-mini-smp-to-sma/c575-047-12-cable-mini-smp-f-to-sma-m-047-flexible-27ghz-vswr-1-35-12/>`__

.. _adxud1aebz-1:

ADXUD1AEBZ
^^^^^^^^^^

-  `FMC extension <https://www.digikey.com/HDR-169468-01>`__
-  `14-Pin PMOD 6 Inch Cable (optional) <https://www.digikey.com/H3AKH-1406G>`__

.. note::

   The `FMC extension <https://www.digikey.com/HDR-169468-01>`__ is used both to move the interposer board and XUD1A away from the MxFE evaluation board as well as to allow access to the HPC1 connector which is otherwise blocked by the MxFE evaluation board.


.. _ad9081-fmca-ebz-1:

AD9081-FMCA-EBZ
^^^^^^^^^^^^^^^

-  `7x SMA-SMPM 6 Inch Cables <https://www.centricrf.com/cable-assemblies/sma-cable-assemblies/27-ghz-047-mini-smp-to-sma/c575-047-06-cable-mini-smp-f-to-sma-m-047-flexible-27ghz-vswr-1-35-6/>`__
-  `4x SMA LPF (ADC - Optional) <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-8400%2B>`__
-  `4x SMA LPF (DAC - Optional) <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-5500%2B>`__
-  `1x FMC riser <https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-fmc-ext-g-3074457345635221630/>`__

.. note::

   If the suggested vendor for the FMC Riser has no stock available, then a FMC Riser can be procured from Samtec. Create a "My Samtec" account and request a quote for Part Number: REF-228680-01, directly from Samtec.


Other
^^^^^

-  `4x 2:1 Power Splitter/Combiner <https://www.minicircuits.com/WebStore/dashboard.html?model=ZX10-2-183-S%2B>`__
-  `4x SMA-M to SMA-M RF Cables <https://www.centricrf.com/cable-assemblies/sma-cable-assemblies/27-ghz-047-flexible-sma-sma/c589-047-03-sma-27ghz-flexible-cable-047-vswr-1-3-s-steel-sma-3/>`__ OR `4x SMA-M to SMA-M Adapters <https://www.digikey.com/2993-6001>`__
-  `3x Fan <https://www.acinfinity.com/component-cooling/axial-ac-fan-kits/axial-1238-muffin-120v-ac-cooling-fan-120mm-x-120mm-x-38mm/>`__
-  50Ω SMA Cables - As Needed
-  2x RF Signal Generator up to 20 GHz (optional)
-  1x RF Spectrum up to 20 GHz (optional)
-  1x 100 MHz Reference Oscillator or Waveform Generator (optional)
-  1x 12 GHz Waveform Generator (optional)

--------------

Hardware Connections
====================

|image1|

.. container:: centeralign

   \ **Figure 1: High Level Block Diagram**\


   |image2|

.. container:: centeralign

   \ **Figure 2: Detailed Block Diagram**\


--------------

Required Peripherals
--------------------

Digital
~~~~~~~

-  4x PMOD ribbon cables, length depends on desired setup, but the total length of each combined PMOD cable will need to be at least 20" (50cm). You need 2x cables for *each* Stingray PMOD connection as the ZCU102's PMOD pinout orientation doesn't directly match that of the Stingray board. You can use any 12-pin cable compatible with PMOD headers.
-  12-pin male-male adapters to connect PMOD cables to each other and to the ZCU102/Stingray. Quantity depends on the gender of the cables used. Both Stingray connectors are female, while on the ZCU102, one PMOD connector is male and the other female.
   One example part number: `TSW-106-08-G-D <https://www.mouser.com/TSW-106-08-G-D>`__.
-  `FMC riser <https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-fmc-ext-g-3074457345635221630/>`__ to raise the MxFE board and allow access to the HPC1 connector for XUD1A control.
-  `FMC extension <https://www.digikey.com/HDR-169468-01>`__ used to extend access to the HPC1 connector for XUD1A control.

| 

RF Connectors
~~~~~~~~~~~~~

-  The Stingray board uses SMPM connectors on both sides of the board, so depending on how the board is used, adapters to mate with test equipment cabling may be required. Note that the Stingray board includes 2x 12" SMPM-SMA cable.
   One example adapter cable: `SMPM to SMA Adapter Cable <https://www.centricrf.com/cable-assemblies/mini-smp-cable-assemblies/27-ghz-047-mini-smp-to-sma>`__
-  If using the 10 GHz lattice spacing antenna tiles, `SMPM Bullets <https://www.digikey.com/125-0901-811>`__, are recommended to directly connect the antenna tiles to the Stingray board. Users can cable out to a custom antenna with different lattice spacings, if desired.
-  The XUD1A board uses SMA connectors on the RF side of the board and SMPM connectors on the IF side of the board. Note that the XUD1A board includes 1x 12" SMPM-SMA cable.
-  The MxFE board uses SMA connectors for both the ADCs and DACs.

--------------

Board Connections to the ZCU102
-------------------------------

ADAR1000EVAL1Z: Stingray
~~~~~~~~~~~~~~~~~~~~~~~~

Connect the Stingray board to the PMOD connectors on the ZCU102 as described below:

-  J55 from the ZCU102 should connect to P3 on the Stingray board using a ribbon cable and any required adapters. Note that pin 1 should connect to pin 1. This will require two PMOD cables to vertically flip the pinout from the ZCU102 to match that of the Stingray board.
-  J87 from the ZCU102 should connect to P4 on the Stingray board using a ribbon cable and any required adapters. Note that pin 1 should connect to pin 1. This will require two PMOD cables to vertically flip the pinout from the ZCU102 to match that of the Stingray board.

|image3|

.. container:: centeralign

   \ **Figure 3: ZCU102-Stingray Digital Connections**\


| 
| ==== ADXUD1AEBZ:XUD1A ==== Connect the XUD1A evaluation board to the ZCU102's HPC1 port. The `FMC extension <https://www.digikey.com/HDR-169468-01>`__ is used both to move the interposer board and XUD1A away from the MxFE evaluation board as well as to allow access to the HPC1 connector which is otherwise blocked by the MxFE evaluation board.

.. note::

   The Interposer board PMOD is pin-compatible with the XUD1A PMOD enabling a direct connect. The `14-Pin PMOD 6 Inch Cable <https://www.digikey.com/H3AKH-1406G>`__ is optional, but recommended as it allows XUD1A to move away from the interposer board for easier RF cabling connections.


   |image4|

.. container:: centeralign

   \ **Figure 4: ZCU102-XUD1A Digital Connections**\


| 
| ==== AD9081-FMCA-EBZ: MxFE ==== Connect the MxFE evaluation board to the ZCU102's HPC0 port as shown below.

.. note::

   Don't forget to use the use the `FMC riser <https://www.avnet.com/shop/us/products/avnet-engineering-services/aes-fmc-ext-g-3074457345635221630/>`__ to raise the AD9081 up!


   |MxFE Connection|

.. container:: centeralign

   \ **Figure 5: ZCU102-AD9081 Attachment**\


--------------

Inter-Board Connections
-----------------------

The platform is divided into four 8:1 subarrays as detailed in the below figure. Two ADAR1000s are connected via RF Splitter/Combiner to a single up/down converter channel on the ADXUD1AEBZ. The IF portion of an individual up/down converter channel is split to a TX IF and RX IF input/out. Each IF output is directly connected to its respective ADC and DAC.

For more details, review the ADAR1000EVAL1Z `Primary Side <https://wiki.analog.com/resources/eval/user-guides/stingray/adar1000eval1z_top-web.gif>`__ and `Secondary Side <https://wiki.analog.com/resources/eval/user-guides/stingray/adar1000eval1z_bottom-web.gif>`__ board images, the `ADXUD1AEBZ Primary Side <https://wiki.analog.com/resources/eval/user-guides/xud1a/eval-adxud1aebz_top-web.gif>`__ board image, and the :adi:`AD9081-EVAL <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9081.html#eb-overview>` images.


|image5|

.. container:: centeralign

   \ **Figure 6: Inter-Board Connections Diagram**\


MxFE to XUD1A
~~~~~~~~~~~~~

Connect the MxFE and XUD1A together using SMA-SMPM cables as indicated below:

+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| Connection # | MxFE Connector | RF Filter                                                                              | XUD1A Connector |
+==============+================+========================================================================================+=================+
| 1            | ADC3 (SMA)     | `VLF-8400+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-8400%2B>`__ | J10 (SMPM)      |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 2            | ADC1 (SMA)     | `VLF-8400+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-8400%2B>`__ | J8 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 3            | DAC3 (SMA)     | `VLF-5500+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-5500%2B>`__ | J9 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 4            | DAC2 (SMA)     | `VLF-5500+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-5500%2B>`__ | J7 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 5            | DAC1 (SMA)     | `VLF-5500+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-5500%2B>`__ | J5 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 6            | DAC0 (SMA)     | `VLF-5500+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-5500%2B>`__ | J1 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 7            | ADC0 (SMA)     | `VLF-8400+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-8400%2B>`__ | J6 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+
| 8            | ADC2 (SMA)     | `VLF-8400+ <https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-8400%2B>`__ | J2 (SMPM)       |
+--------------+----------------+----------------------------------------------------------------------------------------+-----------------+

.. note::

   The ADXUD1AEBZ contains IF bandpass filters per channel (FL3, FL6, FL7, FL8). The rejection for these filters is not sufficient for optimized system performance and additional rejection is required to suppress mixing products, LO feedthrough, DAC image, etc.


   |image6|

.. container:: centeralign

   \ **Figure 7: AD9081 - XUD1A Connections**\


| 
| ==== XUD1A to Stingray ==== The XUD1A has 4 RFIO ports whereas the Stingray board has 8 RFIO ports. For this system, the Stingray's 8 channels will be paired using external splitter/combiners (`Recommended Splitter/Combiner <https://www.minicircuits.com/WebStore/dashboard.html?model=ZX10-2-183-S%2B>`__) to create 4 digital channels which can interface with the XUD1A and MxFE thus created four subarrays where each subarray consists of eight analog channels each. The below tables show how these connections are to be made.

============ =================== ======================
Connection # Stingray Connectors Splitter # (Ports 1/2)
============ =================== ======================
1            J1, J3 (SMPM)       1 (SMA)
2            J2, J4 (SMPM)       2 (SMA)
3            J6, J8 (SMPM)       3 (SMA)
4            J5, J7 (SMPM)       4 (SMA)
============ =================== ======================

============ =============== =====================
Connection # XUD1A Connector Splitter # (Sum Port)
============ =============== =====================
1            J1D (SMA)       1 (SMA)
2            J1C (SMA)       2 (SMA)
3            J1B (SMA)       3 (SMA)
4            J1A (SMA)       4 (SMA)
============ =============== =====================

--------------

Clocking Architecture
=====================

Default MxFE Clocking Scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default clocking scheme used for the :adi:`AD9081-FMCA-EBZ <eval-ad9081>` uses the on-chip PLL. The :adi:`hmc7044` provides the reference into the chip derived from the on-board VCXO crystal oscillator. An external reference signal can be applied to the HMC7044 if the reference signal requires phase lock to other test equipment used in evaluation. The AD9081 firmware contains a HMC7044 reference clock priority table. No firmware changes are required if the reference clock is supplied via EXT_HMCREF SMP-F connection.


|image7|

.. container:: centeralign

   \ **Figure 8: AD9081 Clocking Block Diagram**\


.. note::

   The firmware build HMC7044 reference clock priority is: [CLKIN1 -> CLKIN0 -> CLKIN2 -> CLKIN3]. An external reference clock can be applied to the EXT_HMCREF SMP-F input without any changes to the firmware or hardware.


--------------

Direct MxFE Clocking
~~~~~~~~~~~~~~~~~~~~

The MxFE Evaluation Platform has provisions for directly driving the sampling clock of the MxFE data converter. An SMP-F plug is available for this purpose, which connects to an AC-coupling capacitor that is not populated by default. Reference the schematic for more information. The table below lists the modifications required for direct clocking.


|image8|

.. container:: centeralign

   \ **Figure 9: AD9081 Direct Clocking Implementation**\


============================= ====================================
Direct Clocking Modifications 
============================= ====================================
SMP-F Ref Des                 Modifications
EXT_CLK                       Depopulate C3D/C5D, Populate C4D/C6D
============================= ====================================

--------------

Default XUD1A LO Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default LO configuration for the XUD1A is for an external LO via SMA-F connector. The LO is common across all 4 up/down converter channels via splitter network. Refer to the :doc:`XUD1A Block Diagram </wiki-migration/resources/eval/user-guides/xud1a/user-guide>` for more details.


|image9|

.. container:: centeralign

   \ **Figure 10: XUD1A LO Block Diagram**\


--------------

On-Board XUD1A LO Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The on-board :adi:`adf4371` PLL can be used in lieu of an external LO signal. The default ADF4371 reference clock is an on-board 100 MHz VCXO crystal oscillator, but provisions are available to provide an external reference via a SMP-F connector.


|image10|

.. container:: centeralign

   \ **Figure 11: XUD1A On-Board PLL Implementation**\


The table below lists the modifications required for the on-board LO.

=============================== =====================================
XUD1A On-Board LO Modifications 
=============================== =====================================
Implementation                  Modifications
ADF4371 Output                  Depopulate C165, Populate C61
ADF4371 External Reference      Depopulate C372, Populate C373
ADF4371 +5V Enable              Populate R20 with 0 Ohm 0402 Resistor
=============================== =====================================

--------------

ZCU102 Configuration
====================

Boot from SD Card
~~~~~~~~~~~~~~~~~

To configure the ZCU102 to boot from the SD card, set SW6 as shown below. SW6 is halfway between the SD card input and the vertical SMA connectors on the ZCU102.


|SW6 Configuration for SD Card Boot|

| 
| ==== USB Host Mode ==== Setting up the ZCU102 in USB Host Mode allows the use of USB peripherals such as a keyboard and mouse. This can be useful for operating the board directly rather than having to use the UART connection or some other form of indirect control. Configure the jumpers as indicated below:

-  Shunt J7
-  J109 -> Shunt pins 2-3
-  J110 -> Shunt pins 2-3
-  J112 -> Shunt pins 1-2
-  J113 -> Shunt pins 1-2

|Jumper Configuration for USB Host Mode|

| 
| ==== DisplayPort Not Working ==== Once you have the board up and running (and control using the UART connection through PuTTy), :doc:`try this procedure at the bottom of the page </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`.

| 
| ==== USB to UART Bridge ==== The ZCU102 uses a mini-B USB cable to connect the USB UART port on the board to a host PC. If the USB to UART bridge is not installed or automatically recognized, then a drive must be installed. This will allow control using the UART connection through PuTTy or other SSH/Telnet Client, `select Downloads tab for Driver download <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>`__.

| 
| ==== Network Configuration ==== The ZCU102 uses a RJ45 ethernet cable to connect the ethernet port on the board a host PC or network port to enable network access. Modifications to the network settings can be made following the guidance detailed on the :doc:`Network Configuration </wiki-migration/resources/tools-software/linux-software/network-config>` wiki.

Time Division Duplexing
=======================

The system platform is capable of Time Division Duplexing (TDD) is controlled using a TDD Engine implemented in firmware. The TDD engine controls the MxFE TX and RX data enable paths, the ADXUD1AEBZ up/down converter circuitry and ADAR1000EVAL1Z RF circuitry. See the Matlab Control Overview section for user-level control.

TDD Nets
~~~~~~~~

Replicated IO for the TDD controller is created in hardware all tied to a common software control. The replicas of the MxFE datapath enable pins are routed to signal nets on the ADXUD1AEBZ Interposer board.

+---------------+----------------------+--------------------------------+---------------------------+-----------------+
| Signal        | ZCU102 FPGA Pin (U1) | ZCU102 FMC HPC1 Connector (J4) | Interposer Board Net (P3) | Pin Number (P3) |
+===============+======================+================================+===========================+=================+
| MxFE TX EN    | AG3                  | D11                            | IMU_GPIO0                 | P3-13           |
+---------------+----------------------+--------------------------------+---------------------------+-----------------+
| MxFE RX EN    | AH3                  | D12                            | IMU_GPIO1                 | P3-14           |
+---------------+----------------------+--------------------------------+---------------------------+-----------------+
| External Sync | AE2                  | D14                            | IMU_GPIO2                 | P3-15           |
+---------------+----------------------+--------------------------------+---------------------------+-----------------+
| Ground        |                      |                                | GND                       | P3-7            |
+---------------+----------------------+--------------------------------+---------------------------+-----------------+

The control logic for the RF switching is common between the ADAR1000EVAL1Z and the ADXUD1AEBZ. The TR_EN probe point on the secondary side of the ADAR1000EVAL1Z is recommended to use for connecting a measurement probe.


|image11|

.. container:: centeralign

   \ **Figure 12: ADAR1000EVAL1Z TR Probe**\


Troubleshooting
===============

AD9081 Power On
~~~~~~~~~~~~~~~

ADXUD1AEBZ FMC EEPROM
^^^^^^^^^^^^^^^^^^^^^

There are two potential issues that prevent the 1.8V VADJ from powering on the AD9081-FMCA-EBZ board. Upon boot, the FPGA queries the EEPROM of the different boards attached. If a non-compliant EEPROM is detected, the VADJ stays low during boot thus preventing the AD9081 board from powering on.

Currently, the FMC EEPROM of the interposer board used for the ADXUD1AEBZ is not factory programmed. The user must execute some commands within a UART terminal to program the FMC EEPROM. The command sets to program the FMC EEPROM of the ADXUD1AEBZ interposer board are detailed on the :doc:`software wiki </wiki-migration/resources/eval/user-guides/x-band-platform/software>`. Reboot the FPGA after programming the FMC EEPROM.

AD9081 LTM4616 Enable
^^^^^^^^^^^^^^^^^^^^^

The AD9081 :adi:`ltm4616` power module run control pin voltage threshold is 1.7V. Verify the voltage and resistance of the R1M resistor on the AD9081-FMCA-EBZ exceed the voltage threshold of 1.7V. If not, measure the R1M resistor and verify the resistance value is 2.2 kΩ. The resistor can be replaced with a 0402 220 Ω resistor to meet the voltage threshold requirements of the power module.


|image12|

.. container:: centeralign

   \ **Figure 13: AD9081-FMCA-EBZ R1M Location**\


--------------

Support
=======

For additional questions or support, please visit the Engineering Zone forum at :ez:`ADEF <adef-system-platforms>`.

:doc:`X Band Development Platform Main Page </wiki-migration/resources/eval/user-guides/x-band-platform>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/xbdp-wiki-system-block-diagram.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/platformblockdiagram.jpg
   :width: 1000px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/stingray_zcu102_pmod.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/XUD1A_fmc_v2.png
   :width: 600px
.. |MxFE Connection| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/mxfe_connection.jpg
   :width: 1000px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/xbdp_hardwareconnectiondiagram.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/ad9081-xud1a-connect.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/ad9081_default_clk.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/ad9081_direct_clk.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/XUD1A_lo_pll.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/XUD1A_rework_onboard_pll.png
   :width: 600px
.. |SW6 Configuration for SD Card Boot| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/zcu102_sw6_sdcard.jpg
.. |Jumper Configuration for USB Host Mode| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/zcu102_usb_host_mode.jpg
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/adar1000eval1z_tr_probe.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/x-band-platform/ad9081_ltm4616_en_resistor_r1m.png
   :width: 600px
