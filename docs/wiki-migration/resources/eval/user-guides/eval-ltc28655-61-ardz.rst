EVAL-LTC2855/61-ARDZ Arduino Shield
===================================

Use the EVAL-LTC2855/61-ARDZ Arduino Shield with the widely available Arduino UNO and other Arduino compatible devices to easily evaluate:

-  :adi:`LTC2855 <en/products/ltc2855.html>`; 3.3V 20Mbps RS485/RS422 Transceivers with Integrated Switchable Termination
-  :adi:`LTC2861 <en/products/ltc2861.html>`; 5V 20Mbps RS485/RS422 Transceivers with Integrated Switchable Termination
-  :adi:`ADUM6020 <en/products/adum6020.html>`; isoPower®, integrated, isolated dc-to-dc converters based on the Analog Devices, Inc., iCoupler® technology that provides regulated, isolated power that is below CISPR22 Class B limits.
-  :adi:`ADuM261N <en/products/adum261n.html>`; robust 5.0 kVrms Six Channel Digital Isolator w/ Fail-Safe & 1 Reverse Channel

This Evaluation board can be powered from an external block with an additional Logic Supply or from the Arduino. Logic signals can range from 1.8V to 5V. It also features an integrated switchable termination.

| It has onboard pullup/down resistors on A,B,Y and Z (bus pins). In addition, it has a zener diode to protect the 3.3 V RS485 Transceiver, :adi:`LTC2855 <en/products/ltc2855.html>` against short circuit current.
| Labelled test points for signals can be found on the board.

--------------

Eval board features
===================

-  Full Data + Power Isolation
-  Arduino style header for easy evaluation
-  Terminal blocks for easy wire connections
-  Test points and jumpers for easy configuration and monitoring of signals

--------------

Switchable termination
======================

The key feature of the :adi:`LTC2855 <en/products/ltc2855.html>`/:adi:`LTC2861 <en/products/ltc2861.html>` is the switchable termination. Proper cable termination is very important for good signal fidelity. If the cable is not terminated with its characteristic impedance, reflections will result in distorted waveforms. The :adi:`LTC2855 <en/products/ltc2855.html>`/:adi:`LTC2861 <en/products/ltc2861.html>` are the first RS485 transceivers to offer integrated switchable termination resistors on the receiver input pins. This provides the tremendous advantage of being able to easily change, through logic control, the proper line termination for optimal performance when configuring transceiver networks. When the TE pin is high, the termination resistor is enabled and the differential resistance from A to B is 120Ω. The resistance is maintained over the entire RS485 common mode range of –7V to +12V. The integrated termination resistor has a high frequency response which does not limit performance at the maximum specified data rate. The termination resistor cannot be enabled by TE if the device is unpowered or in thermal shutdown mode.

Driver Overvoltage and Overcurrent Protection
=============================================

The driver outputs are protected from short-circuits to any voltage within the Absolute Maximum range of (VCC –15V) to +15V. The typical peak current in this condition does not exceed 180mA in the case of :adi:`LTC2855 <en/products/ltc2855.html>` and 250mA in the case of :adi:`LTC2861 <en/products/ltc2861.html>`.

Receiver and Failsafe
=====================

With the receiver enabled, when the absolute value of the differential voltage between the A and B pins is greater than 200mV, the state of RO will reflect the polarity of (A-B).The :adi:`LTC2855 <en/products/ltc2855.html>`/:adi:`LTC2861 <en/products/ltc2861.html>` have a failsafe feature that guarantees the receiver output to be in a logic-high state when the inputs are either shorted, left open, or terminated, but not driven. This failsafe feature is guaranteed to work for inputs spanning the entire common mode range of –7V to +12V.

SLO Mode: Slew Limiting for EMI Emissions Control
=================================================

The :adi:`LTC2861 <en/products/ltc2861.html>` features a logic-selectable reduced slew mode (SLO mode) that softens the driver output edges to control the high frequency EMI emissions from equipment and data cables.

--------------

Connectors
==========

+----------+----------------------------------------------------------------------------------------------------------------------------------------------+
| **Port** | Function                                                                                                                                     |
+==========+==============================================================================================================================================+
| **P1-5** | Arduino headers                                                                                                                              |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------+
| **P6**   | Screw Terminal for signals A, B, Y and Z.                                                                                                    |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------+
| **P7**   | Terminal block has inputs/outputs for DI, RO, RE_N and DE.                                                                                   |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------+
| **P8**   | This is the external power input block. 5V must be supplied as well as the IO voltage which can be between 1.8 and 5V but must match the IO. |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------+

--------------

Jumper Configuration
====================

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| \**Jumper \*\*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration                                                                         |
+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+=======================================================================================+
| \**JMP1_1 / JMP1_2 **\|Only one of these 0 ohm resistors should be placed to set the output voltage of the ADUM6020. JMP1_1 sets the output to 5V for the** :adi:`LTC2855 <en/products/ltc2855.html>`\ **. JMP1_2 sets the output to 3.3V for the** :adi:`LTC2861 <en/products/ltc2861.html>`\ **.\| \|**\ JMP4\ **\|Selects the IOREF source, either from the Arduino header from an external source.\| \|**\ JMP5\ **\|Selects the 5V source, either from the Arduino header or from the an external source.\| \|**\ JP7\ **\|Allows the user to set the states of DE and RE_N if not connected to Arduino. DE can be connected to ground to disable the driver, or to IOREF to enable it. RE_N can be connected to GND to enable the receiver or to IOREF to disable it. DE and RE_N can also be tied together. Alternatively, both jumpers can be removed and the DE and RE_N signals can be controlled externally. Make sure the jumpers are either removed or DE and RE_N are tied together when using the Arduino header (i.e when using an Arduino to control these signals).\| \|**\ JMP8\ **\|Allows the user to set the state of TE if not connected to Arduino. TE is connected to ground to disable termination, or to IOREF to enable it. Make sure the jumper is removed if the TE signal is controlled using an Arduino via the Arduino headers on the board.\| \|**\ JMP9\ **\|(only applicable for** :adi:`LTC2861 <en/products/ltc2861.html>`\ **) Allows the user to set the state of SLO_N if not connected to Arduino. It is connected to ground to enable slo-mode, or to IOREF to disable it. Make sure jumper is removed if this signal is controlled using an Arduino via the Arduino headers on the board.\| \|**\ LK1 and LK2*\* | These jumpers allow the user to connect A to Y, and B to Z for half duplex operation. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

--------------

Schematic, Bill of Materials and Layout Files
=============================================

.. admonition:: Download
   :class: download

   
   ::
   
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval_ltc2855_61_ardz/ltc2855_ardz_bom.xlsx|LTC2855 BOM]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval_ltc2855_61_ardz/ltc2861_ardz_bom.xlsx|LTC2861 BOM]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval_ltc2855_61_ardz/ltc2855_61_ardz_layout.pdf|Layout]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval_ltc2855_61_ardz/ltc2855_61_ardz_schematic.pdf|LTC2855 Schematic]]
        *[[https://wiki.analog.com/_media/resources/eval/user-guides/eval_ltc2855_61_ardz/ltc2861_ardz_schematic.pdf|LTC2861 Schematic]]
   


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
