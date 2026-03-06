EVAL-LTC2854/59-ARDZ Arduino Shield
===================================

Use the <fc #ff0000>\ **EVAL-LTC2854/59-ARDZ**\ </fc> Arduino Shield with the widely available Arduino UNO and other Arduino compatible devices to easily evaluate: // *\** **<fc #ff0000>\ **\ *\ *\ :adi:`LTC2854 <en/products/ltc2854.html>`\ *\ *\ **\ </fc>** *(*\ 3.3V, 20Mbps, Half duplex RS485/RS422 Transceiver with Integrated Switchable Termination\ *)* **<fc #6495ed>and</fc>**\ *\* <fc #ff0000>\ *\ :adi:`LTC2859 <en/products/ltc2859.html>`\ *\ </fc> (*\ 5V, 20Mbps, Half duplex, RS485 Transceivers with Integrated Switchable Termination//) This board also includes:

-  **<fc #ff0000>\ **\ :adi:`ADUM6020 <en/products/adum6020.html>`\ **\ </fc>**, a Low Emission, 5 kV Isolated DC-to-DC Converter that provides regulated, isolated power that is below CISPR22 Class B limits.
-  **<fc #ff0000>\ **\ :adi:`ADuM261N <en/products/adum261n.html>`\ **\ </fc>**, a 5.0 kV RMS, 6-Channel Digital Isolators based on Analog Devices, Inc., iCoupler® technology for the full isolation of the data channels.
-  Onboard pullup/down resistors for the A and B channel of the featured transceivers.

-  A Zener diode between VCC and GND pins of the <fc #ff0000>\ :adi:`LTC2854 <en/products/ltc2854.html>`\ </fc> for protection against the short circuit currents.

-  Test points (for tracking and monitoring all input/output signals on the board).

The <fc #ff0000>\ **EVAL-LTC2854/59-ARDZ**\ </fc> board can be powered up from an external 5V supply or from an Arduino. It allows for a logic supply ranging from 1.8V and 5V.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/47444_evalltc2859ardzangleweb_sourcecopy_4.gif
   :align: center
   :width: 600px

--------------

EVAL-LTC2854/59-ARDZ features
=============================

-  *Full <fc #6495ed>Data</fc> + <fc #ffa500>Power</fc> Isolation*
-  *Arduino style header for easy evaluation*
-  *Terminal blocks for easy wire connections*
-  *Test points and jumpers for easy configuration and monitoring of signals*

Key Features
============

Switchable termination
----------------------

| One key feature of the :adi:`LTC2854 <en/products/ltc2854.html>`/:adi:`LTC2859 <en/products/ltc2859.html>` featured on this Evaluation board is the switchable termination.
| Proper cable termination is very important for good signal fidelity. If the cable is not terminated with its characteristic impedance, reflections will result in distorted waveforms.
| The :adi:`LTC2854 <en/products/ltc2854.html>`/:adi:`LTC2859 <en/products/ltc2859.html>` are the first RS485 transceivers to offer integrated switchable termination resistors on the receiver input pins. This provides the tremendous advantage of being able to easily change, through logic control, the proper line termination for optimal performance when configuring transceiver networks. When the TE pin is high, the termination resistor is enabled and the differential resistance from A to B is 120Ω. The resistance is maintained over the entire RS485 common mode range of –7V to +12V.
| The integrated termination resistor has a high frequency response which does not limit performance at the maximum specified data rate. However, the termination resistor cannot be enabled by TE if the device is unpowered or in thermal shutdown mode.

Supply Current
--------------

The unloaded static supply currents in the :adi:`LTC2854 <en/products/ltc2854.html>` are very low -typically under 500µA for all modes of operation. In the case of :adi:`LTC2859 <en/products/ltc2859.html>`, they are typically under 700µA for all modes of operation without the internal terminator enabled.

Driver Overvoltage and Overcurrent Protection
---------------------------------------------

The driver outputs are protected from short-circuits to any voltage within the Absolute Maximum range of (VCC –15V)to +15V. The typical peak current in this condition does not exceed 180mA for :adi:`LTC2854 <en/products/ltc2854.html>`. The maximum current in this condition is 250mA for :adi:`LTC2859 <en/products/ltc2859.html>`.

Receiver and Failsafe
---------------------

With the receiver enabled, when the absolute value of the differential voltage between the A and B pins is greater than 200mV, the state of RO will reflect the polarity of (A-B).The :adi:`LTC2854 <en/products/ltc2854.html>`/:adi:`LTC2859 <en/products/ltc2859.html>` have a failsafe feature that guarantees the receiver output to be in a logic-high state when the inputs are either shorted, left open, or terminated(externally or internally), but not driven. This failsafe feature is guaranteed to work for inputs spanning the entire common mode range of –7V to +12V.

Receiver Input Resistance
-------------------------

The receiver input resistance from A or B to ground is guaranteed to be greater than 96k (C-, I-Grade) when the termination is disabled. This is 8X higher than the requirements for the RS485 standard. This, in turn, means that 8X the standard number of receivers, or 256 total, can be connected to a line without loading it beyond what is called out in the RS485 standard.

--------------

Connectors
==========

+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Port** | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+==========+===========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **P1-5** | P1-5 are Arduino headers on the board for connection to an Arduino or an Arduino Compatible device. DE (Driver-Enable) pin is connected to P5.6 (pin 6 on the P5 header), RE (Receiver-Enable) pin of the transceiver is connected to P5.4, TX_RS485 is connected to P5.2 and RX_RS485 is connected to P5.1. The P2 header provides power from Arduino/SDP-K1 to the board. P2.2 should be connected to the IOREF pin of the Arduino/SDP-K1. P2.3 should be connected to the Reset pin if set on the Arduino. P2.4 should be connected to the 3.3V rail of the Arduino/SDP-k1. P2.5 should be connected to 5V rail of the Arduino. The P4 header provides more GPIO connections (see the schematic for details). P1 is a header for Analog inputs (similar to an Arduino) |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **P6**   | Screw Terminal Block for signals A (P6.2) and B (P6.3) and isolated GND (P6.1 or P6.4).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **P7**   | Screw Terminal Block for inputs/outputs for DI (Driver-Input) (P7.2), RO (Receiver-Output) (P7.1), RE_N/RE (Receiver-Enable) (P7.4) and DE (Driver Enable) (P7.3).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **P8**   | This is the external power Wire-To-Board Terminal Block. 5V must be supplied to pin 2 of the P8 block(P8.2). The IOREF voltage header pin from an Arduino/SDP-K1 should be connected to pin 3 of the P8 terminal block. It should be less than the absolute max ratings of the IO pins it is supplying power to.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------

Jumper Configuration
====================

======================= =============
\**Jumper \*\*          Configuration
======================= =============
\**JMP1_1 / JMP1_2 \*\* 
**JMP4**                
**JMP5**                
**JP7**                 
**JMP8**                Not Inserted
\                       Position ON
\                       Position OFF
**JMP9**                Not Inserted
\                       Position ON
\                       Position OFF
======================= =============

JP7 Configuration
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/jp7config.jpg
   :align: center
   :width: 400px

--------------

Schematic, Bill of Materials and Layout Files
=============================================

.. admonition:: Download
   :class: download

   
   ::
   
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/ltc2859_ardz_bom.xlsx|LTC2859 BOM]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/ltc2854_59_ardz_bom.xlsx|LTC2854 BOM]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/ltc2854_59_ardz_layout.pdf|Layout]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/ltc2854_59_ardz_schematic.pdf|LTC2854 Schematic]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc28654-59-ardz/ltc2859_ardz_schematic.pdf|LTC2859 Schematic]]
   


--------------

Change Log
==========

::

     *Initial Revision 

--------------

Resources and Helpful Documentation
===================================

-  ADuM260N Data Sheet: :adi:`media/en/technical-documentation/data-sheets/ADuM260N-261N-262N-263N`.pdf
-  ADuM6020 Data Sheet: :adi:`media/en/technical-documentation/data-sheets/ADuM6020-6028`.pdf
-  LTC2854/55 Data Sheet: :adi:`media/en/technical-documentation/data-sheets/285455fc`.pdf
-  LTC2859/61 Data Sheet: :adi:`media/en/technical-documentation/data-sheets/285961fc`.pdf
-  SDP-K1: :adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1`.html
-  RS-485/RS-422 implementation guide AN-960: :adi:`media/en/technical-documentation/application-notes/AN-960`.pdf
-  Enhanced RS-485 Performance: Receiver Fail-Safe, Hysteresis, Common-Mode Range and Gain Bandwidth Optimized for Long Fieldbus Cables AN-1399: :adi:`media/en/technical-documentation/application-notes/an-1399`.pdf
-  High Speed Low Power RS485 Transceivers with Integrated Switchable Termination, Technical Article: :adi:`en/technical-articles/high-speed-low-power-rs485-transceivers-with-integrated-switchable-termination`.html
-  Rugged 3.3V RS485/RS422 Transceivers with Integrated Switchable Termination, Technical Article: :adi:`ru/technical-articles/rugged-rs485-rs422-transceivers-with-integrated-switchable-termination`.html

--------------

Software
========

--------------

// End of Document //
