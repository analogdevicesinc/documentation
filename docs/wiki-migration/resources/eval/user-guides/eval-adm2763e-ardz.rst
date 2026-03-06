EVAL-ADM2763E-ARDZ ARDUINO SHIELD
=================================

| Use the <fc #ff0000>\ **EVAL-ADM2763E-ARDZ**\ </fc> Arduino Shield with the widely available Arduino UNO and other Arduino compatible devices to easily evaluate the :adi:`ADM2763E <en/products/adm2763e.html>` <del>\ *5 kV rms* </del> \*\* 5.7 kV rms*\* signal isolated RS-485 transceiver with ESD protection on the RS-485 A, B, Y, and Z bus pins:

-  // ≥ ±12 kV IEC 61000-4-2 contact discharge//
-  // ≥ ±15 kV IEC 61000-4-2 air discharge//

|

| :adi:`ADM2763E <en/products/adm2763e.html>` also has a high common-mode transient immunity (greater than 250 kV/μs) with a **short-circuit**, **open-circuit**, and **floating** input receiver fail-safe. This transceiver is designed for low speed 500 kbps data rate for EMI control. It has flexible power supply inputs, i.e.

-  // Primary VDD1 supply of 1.7 V to 5.5 V//
   \* // Isolated VDD2 supply of 3.0 V to 5.5 V//

<fc #ff0000>\ **EVAL-ADM2763E-ARDZ**\ </fc> also features the :adi:`ADP7104 <en/products/adp7104.html>`. The :adi:`ADP7104 <en/products/adp7104.html>` is a CMOS, low dropout linear regulator that operates from 3.3 V to 20 V and provides up to 500 mA of output current. However, this can be replaced with :adi:`ADP7102 <en/products/adp7102.html>` which is also a CMOS low noise LDO that provides up to a maximum of 300 mA output current).

This board can be powered up from external 5V supply, USB or even from the Arduino and allows for either 5V or 3.3V logic. It also has a switchable Full/Half duplex capability (configured using a jumper).

--------------

EVAL-ADM2763E-ARDZ FEATURES
===========================

-  *Full <fc #6495ed>Data</fc> Isolation*
-  *Arduino style header for easy evaluation*
-  *Terminal blocks for easy wire connections*
-  *Test points and jumpers for easy config and monitoring of signals*

--------------

KEY FEATURES
============

ROBUST LOW POWER DIGITAL ISOLATOR
---------------------------------

The :adi:`ADM2763E <en/products/adm2763e.html>` features a low power, digital isolator block to galvanically isolate the primary and secondary sides of the device. The use of coplanar transformer coils with an on or off keying modulation scheme allows a high data throughput across the isolation barrier while minimizing radiation emissions. This architecture provides a robust digital isolator with immunity to common-mode transients >250 kV/µs across the full temperature and supply range of the devices. The digital isolator circuitry features a flexible VDD1 power supply with an input voltage range of 1.7 V to 5.5 V.

HIGH DRIVER DIFFERENTIAL OUTPUT VOLTAGE
---------------------------------------

The :adi:`ADM2763E <en/products/adm2763e.html>` features a proprietary transmitter architecture with a low driver output impedance that results in an increased differential output voltage. This architecture is useful when operating the devices at lower data rates over long cable runs where the dc resistance of the transmission line dominates signal attenuation. In these applications, the increased differential voltage extends the reach of the devices to longer cable lengths. When operated as a 5 V transceiver (VDD2 > 4.5 V), this transceiver meet or exceed the PROFIBUS requirement of a minimum 2.1 V differential output voltage.

RECEIVER FAIL-SAFE
------------------

The :adi:`ADM2763E <en/products/adm2763e.html>` guarantees a logic high receiver output when the receiver inputs are shorted, open, or connected to a terminated transmission line with all drivers disabled. To achieve a fail-safe logic high output, set the receiver input threshold between −30 mV and −200 mV. If (A − B) ≥ −30 mV, the RxD output is logic high. If (A − B) ≤ −200 mV, the RxD output is logic low. To preserve the fail-safe feature when the receiver inversion feature is enabled (INVR = VDD1), the inverted receiver input threshold is set between 30 mV and 200 mV. In the case of a terminated bus with all transmitters disabled, the termination resistor pulls the receiver differential input voltage to 0 V, which results in a logic high RxD output with a 30 mV minimum noise margin. This feature eliminates the need for the external biasing components usually required to implement fail-safe.

DRIVER AND RECEIVER CABLE INVERSION
-----------------------------------

The :adi:`ADM2763E <en/products/adm2763e.html>` features receiver cable inversion functionality to correct for errors during installation. This adjustment can be implemented in the software on the controller driving the RS-485 transceiver to avoid additional installation costs to fix wiring errors. It features a receiver cable invert pin, INVR, that can correct receiver functionality in cases where connections to the A and B pins are made incorrectly. When the receiver is inverted, the device maintains a Logic 1 receiver output with a 30 mV noise margin when inputs are shorted together or open circuit.

OTHER FEATURES
--------------

-  Hot Swap Inputs
   \* 192 Transceivers supported on the bus
   \* Driver Output Protection
   \* IEC 61000-4-2 ESD PROTECTION

CONNECTORS
==========

+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Port Name**   | Type                                                                                         | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+=================+==============================================================================================+=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **P1,P3,P6,P7** | Samtec, SSQ PCB Socket, Through Hole                                                         | Arduino headers for connection to the Arduino/SDP-K1/Arduino Compatible Device. P6.1 (Pin 1 of the P6 Arduino header) is connected to the RX_RS485 pin of the :adi:`ADM2763E <en/products/adm2763e.html>` transceiver, P6.2 to the TX_RS485 pin ,P6.3 to the DE (Driver-Enable) and P6.4 to the RE (Receiver-Enable) pins of the :adi:`ADM2763E <en/products/adm2763e.html>` transceiver. P3.5 (Pin 5 of the P3) should be connected to the 5V rail of the Arduino (if used). P3.8 should be connected to the VIN supply rail of the Arduino (if used). P3.4 should be connected to the 3.3V rail of the Arduino (if used).                                         |
+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **P10**         | Power Barrel Connector Jack 2.10mm ID (0.083"), 5.50mm OD (0.217") Through Hole, Right Angle | Provides 7.5V to the VIN of :adi:`ADP7104 <en/products/adp7104.html>` (Regulator's Input Supply).The output of the :adi:`ADP7104 <en/products/adp7104.html>` regulator (VOUT) powers the VDD2 side of the board.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **P2**          | 4-pin Wire-To-Board Terminal Block, 5 mm, 4 Ways, 2.5 mm², Screw                             | Provides connection for the Receiver inputs and Driver outputs of the :adi:`ADM2763E <en/products/adm2763e.html>` transceiver(A, B, Y and Z.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **J1**          | Straight Edge Mount SMA Connector                                                            | Provides external connection for the transmitter, TX_RS485 of the :adi:`ADM2763E <en/products/adm2763e.html>` transceiver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------

Jumper Configuration
====================

+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Jumper-** | -Config--    | Comment                                                                                                                                                                                                                                  |
+=============+==============+==========================================================================================================================================================================================================================================+
| **P5**      | Inserted     | Connects the termination resistor, R6 between pins Y and Z of the :adi:`ADM2763E <en/products/adm2763e.html>`                                                                                                                            |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Not Inserted | Disconnects the termination resistor, R6 between pins Y and Z of the :adi:`ADM2763E <en/products/adm2763e.html>` .                                                                                                                       |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **P9**      | Inserted     | Connects the termination resistor, R5 between pins A and B of the :adi:`ADM2763E <en/products/adm2763e.html>`.                                                                                                                           |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Not inserted | Disconnects the termination resistor, R5 between pins A and B of the :adi:`ADM2763E <en/products/adm2763e.html>` .                                                                                                                       |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **JP1**     | Position A   | Connects the DE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to Pin 3 of the Arduino header, P6 and to the DE terminal(pin 3) of the P8 terminal block.<fc #ff00ff>(corrected)</fc>                                            |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position B   | Connects the DE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to VDD1 of the :adi:`ADM2763E <en/products/adm2763e.html>` . This enables the RS-485 driver outputs.                                                              |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position C   | Connects the DE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to GND1 of the :adi:`ADM2763E <en/products/adm2763e.html>` . This disables the RS-485 driver outputs.                                                             |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **JP2**     | Position A   | Connects the RE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to Pin 4 of the Arduino header (P6) and to the RE terminal(pin 2) of the P8 terminal block<fc #ff00ff>(corrected)</fc>.                                           |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position B   | Connects the RE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to VDD1 of the :adi:`ADM2763E <en/products/adm2763e.html>` . This disables the RS-485 receiver output. (Active low)                                               |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position C   | Connects the RE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to the DE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` . RE is controlled by position of JP1.                                                           |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position D   | Connects the RE pin of the :adi:`ADM2763E <en/products/adm2763e.html>` to GND1 of the :adi:`ADM2763E <en/products/adm2763e.html>` . This enables the RS-485 receiver output. (Active low)                                                |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **JP3**     | Position A   | Power the VDD1 supply of the :adi:`ADM2763E <en/products/adm2763e.html>` from the 3.3V rail of the Arduino.                                                                                                                              |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position B   | Powers the VDD1 supply of the :adi:`ADM2763E <en/products/adm2763e.html>` from the 5V rail of the Arduino.                                                                                                                               |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position C   | Powers the VDD1 supply of the :adi:`ADM2763E <en/products/adm2763e.html>` from the VIN rail (7-12V) of the Arduino.<fc #ff00ff>(Absolute max rating of VDD1 is +7V. There is no LDO on this side of the board!)</fc>                     |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **JP4**     | Not Inserted | Power the VDD2 supply from the VDD2 terminal on the P4 terminal block.                                                                                                                                                                   |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position A   | Powers the VDD2 supply with regulated 5V supply. (Power the P10 barrel connector with at least 5.2V)                                                                                                                                     |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position B   | Powers the VDD2 supply with a regulated 3.3V supply. (Power the P10 barrel connector with at least 3.5V)                                                                                                                                 |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             | Position C   | Powers the VDD2 supply directly from the barrel connector P10 and screw terminal block P4.                                                                                                                                               |
+-------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------

TestPoints
==========

===================== ====== =======================
\**TestPoint \*\*     Colour Signal
===================== ====== =======================
**TP1**               Yellow TX_RS485
**TP2**               Yellow RX_RS485
**TP3**               Yellow DE
**TP4**               Yellow RE_N
**TP7**               Yellow A_RS485
**TP8**               Yellow B_RS485
**TP18**              Yellow Y_RS485
**TP19**              Yellow Z_RS485
**TP12**              Yellow INVR
**TP13**              RED    VDD1
**TP5**               RED    VDD2
**TP14-17**           BLACK  AGND1
**TP6,TP9,TP10,TP11** BLACK  Isolated Ground (AGND2)
===================== ====== =======================

--------------

Schematic, Bill of Materials and Layout Files
=============================================

.. admonition:: Download
   :class: download

   
   -  `Layout <https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/adm2763e_layout.pdf>`__
   -  `BOM <https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/ADM2763E_bom.xlsx>`__
   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/adm2763e_schematic.pdf>`__
   


--------------

Change Log
==========

::

     *Initial Revision 

--------------

Resources and Helpful Documentation
===================================

-  ADM2763E Data Sheet: :adi:`media/en/technical-documentation/data-sheets/adm2761e_adm2763e`.pdf
-  ADP7104 Data Sheet: :adi:`media/en/technical-documentation/data-sheets/ADP7104`.pdf
-  SDP-K1: :adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1`.html
-  RS-485/RS-422 implementation guide AN-960: :adi:`media/en/technical-documentation/application-notes/AN-960`.pdf
-  Enhanced RS-485 Performance: Receiver Fail-Safe, Hysteresis, Common-Mode Range and Gain Bandwidth Optimized for Long Fieldbus Cables AN-1399: :adi:`media/en/technical-documentation/application-notes/an-1399`.pdf

--------------

Software
========

-  `Tera Term <https://ttssh2.osdn.jp/index.html.en>`__
-  `Mbed Studio for SDP-K1 <https://os.mbed.com/studio/>`__
-  `Mbed online Compiler <https://ide.mbed.com/compiler/>`__
-  `SDP-K1 programming / set up guide <https://os.mbed.com/platforms/SDP_K1/>`__
-  `Arduino IDE <https://www.arduino.cc/en/software>`__
-  `Arduino Code <https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/arduino code.zip>`__
-  `SDP-K1 C++ code for evaluating the EVAL-ADM2763E-ARDZ, use Mbed Studio or online compiler, see above for SDP-K1 programming guide <https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/sdp-k1.zip>`__

--------------

Procedure for Evaluating the board with the SDP-K1 and an Arduino
=================================================================

| The SDP-K1 can be powered using the USB VBUS supply. This PC supplied 5 V (±10%) supply can provide up to 500 mA maximum (in certain instances, the amount of available current can be reduced). The SDP-K1 consumes up to 300 mA, so if no other power source is available, the amount of current available on the output power pins of the Arduino headers is reduced below the limits stated in the Arduino Headers section in the SDP-K1 User Guide.
| **Make sure the SDP-K1 VIO_ADJUST is set at 3.3V**. This header is used to set the input/output voltage of the board to either 1.8 V or 3.3 V. Ensure that the VIO_ADJUST header is configured properly before power is applied to the system, otherwise, damage can be caused to the SDP-K1 and the daughter board. The input/output voltage defaults to 1.8 V when the jumper is not in place. This voltage applies to all input/output pins on the Arduino header on the SDP boards. The VIH min levels for digital logic inputs (DE, RE, TXD and INVR) is determined by the VDD1 supply of the transceiver. To ensure we get the min VIH level, we set the VIO_ADJUST to 3.3V (to get a good margin between a high and a low signal).
| The code files given and rest of the steps listed need two **<fc #ff0000>EVAL-ADM2763E-ARDZ</fc>** boards, one SDP-K1 and lastly, an Arduino or another SDP-K1/Arduino compatible device.
| |image1| Photo of board with correct Jumper Configuration for SDP-K1.
| |image2| Photo of board with correct Jumper Configuration for Arduino.

**For both boards**

-  Power and Program the SDP-K1 and or Arduino with the code files provided using the mbed IDE (link in the resources).
-  Unpower the SDP-K1 or Arduino
-  Place **JP1** in position A (DE of the transceiver is connected to Pin 3 of the Arduino header, P6).
-  Place **JP2** in position A (RE of the transceiver is connected to Pin 4 of the Arduino header, P6).
-  Place **JP3** in position C (this supplies the VDD1 side of the board from the 3.3V rail of the Arduino header. P3.4 on the SDP-K1 board supplies 3.3V).
-  If powering the secondary side through a Barrel Jack, set **JP4** to position B or C as required.
-  If powering the secondary side through the screw terminal P4, **do not insert the JP4 jumper**.
-  Insert the jumper on P5 (Termination resistor connection)
-  Insert the jumper on P9 (Termination resistor connection)
-  Connect up driver outputs and receiver inputs from P2 of the board to P2 of the second **<fc #ff0000>EVAL-ADM2763E-ARDZ</fc>** board. Connect A, B, Y, Z of the first board to Y, Z, A, B of the second **<fc #ff0000>EVAL-ADM2763E-ARDZ</fc>** board. (i.e. A of board 1->Y of board 2, B of board 1->Z of board 2, Y of board 1->A board 2, Z of board 1->B board 2)
-  Connect P6.1 (RX_RS485) to D0 of the SDP-K1, P6.2 (TX_RS485) to the D1 of the SDP_K1, P6.3 (DE) to the D2 of the SDP-k1, P6.4 (RE) to the D3 of the SDP-K1 & P6.6 (INVR) on the P6 Arduino header of the **<fc #ff0000>EVAL-ADM2763E-ARDZ</fc>** boards to any pin on SDP-K1 (D4-D7).
-  Power up the SDP-K1 board.
-  Power up the secondary side of the **<fc #ff0000>EVAL-ADM2763E-ARDZ</fc>** board (using a barrel jack or the terminal).
-  Open an instance of Tera Term and connect to the COM port of the SDP-K1 (this typically shows up as COMX USB Serial Device)
-  Type in a character, the character will be transmitted over UART from PC to the SDP-K1, then from the SDP-K1 to the :adi:`ADM2763E <en/products/adm2763e.html>`, then through RS-485 on the transmitting differential pair (Z,Y -> B,A). The Arduino will then echo the character back over the other differential pair to the first board displaying the character on terminal window. The included code will send one character at a time over the full duplex connection.

| |image3|
| The photo above shows characters being received back in Tera Term, i.e. Characters are sent back if they are sent one at a time and will appear on the terminal.

--------------

// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/img_20201204_140346.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/img_20201204_140327.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_adm2763e_ardz/teraterm4.png
   :width: 400px
