Hardware Guide
==============

Device Description
------------------

The :adi:`AD4116 <en/products/ad4116.html>` is a highly accurate, high resolution, multiplexed, Σ Δ ADC with eleven single-ended or six differential voltage inputs, a voltage range of ±10 V and additional 2 differential or 4 single-ended/pseudo differential direct ADC inputs provides excellent performance at lower input ranges. The maximum channel-to-channel scan rate is 12.4 kSPS (80 µs) for fully settled data. The output data rates range from 1.25 SPS to 62.5 kSPS. The device includes integrated analog reference buffers, an integrated precision 2.5 V reference, and an integrated oscillator. See the AD4116 datasheet for complete specifications. Consult the datasheet in conjunction with this user guide when using the evaluation board.

Set-up Procedures
-----------------

After following the instructions in the Software Installation Procedures section, set up the evaluation board and SDP board as detailed in the Configuring the Evaluation and SDP Boards section.

.. important::

   The evaluation software and drivers must be installed before connecting the EVAL-AD4116ASDZ evaluation board and EVAL-SDP-CB1Z board to the USB port of the PC to ensure the PC correctly recognizes the evaluation system.


| **Configuring the Evaluation and SDP Boards**
| Use the following procedure to configure the boards

-  Connect the SDP board to Connector A or Connector B on the EVAL-AD4116ASDZ board. Screw the two boards together firmly using the plastic screw and washer set included in the evaluation board kit.
-  If using the SDP-K1 board the Arduino headers can also be used to connect to the board
-  Ensure that LK3 is in Position B (USB).
-  Connect the SDP board to the PC using the USB cable.

Evaluation Board
----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/board_photo.png
   :align: center
   :width: 600px

Hardware Link Options
---------------------

+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Number | Default Position | Description                                                                                                                                                                                             |
+=============+==================+=========================================================================================================================================================================================================+
| LK1         | Inserted         | Connects the on-board external reference :adi:`ADR4525 <en/products/adr4525.html>` (U2) to AD4116(U1). Remove LK1 if using a different single-ended external reference.                                 |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK2         | Inserted         | Connects VINCOM to GND_ISO. This configuration is typical for single-ended measurement. Remove LK2 to set the custom common analog input for single-ended channels. VINCOM is available on Pin 5 of J3. |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK3         | B (USB)          | Selects the power supply voltage. **Position A:** board is powered from the external dc power supply connector, J4. **Position B:** board is powered from USB through the SDP or Arduino connector.     |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK4 to LK6  | STD              | Selects which Arduino SPI Lines to connect. **STD :** Standard Arduino Headers. **ALT :** Alternate IFCSP Header                                                                                        |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK9, LK10   | Inserted         | Connects VIN4 and VIN5 to the Zener diode D16 and D17 respectfully. These can be removed to evaluate the voltage inputs of the AD4116 directly by removing external components.                         |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK11, LK12  | Removed          | Bypasses R10 and R11 on VIN4 and VIN5 respectfully. By inserting this link the resistor is removed from the input path and AD4116 can be evaluated directly.                                            |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK13, LK14  | Inserted         | Connects ADCIN11 and ADCIN12 to the Zener diode D8 and D9 respectfully. These can be removed to evaluate the voltage inputs of the AD4116 directly by removing external components.                     |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK15, LK16  | Removed          | Bypasses R21 and R22 on ADCIN11 and ADCIN12 respectfully. By inserting this link the resistor is removed from the input path and AD4116 can be evaluated directly.                                      |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J14         | CS0              | Selects which GPIO to use on the Arduino header as CS to enable stacking boards.                                                                                                                        |
+-------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

On Board Connections
--------------------

+------------+---------------------------------------------------+-------------------------------------------------------+
| Connector  | Function                                          | Connector Type                                        |
+============+===================================================+=======================================================+
| J1         | Connects to GPIO’s of AD4116                      | 4-pin header, 2.54mm pitch                            |
+------------+---------------------------------------------------+-------------------------------------------------------+
| P1, P2, P3 | Voltage inputs to AD4116                          | Connector, header, 90°, 5 position, 3.81 mm           |
+------------+---------------------------------------------------+-------------------------------------------------------+
| P4         | Low-level inputs to AD4116                        | Connector, header, 90°, 5 position, 3.81 mm           |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J4         | External supply voltage (optional)                | Power socket block, 3-way, 3.81 mm pitch              |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J7         | Arduino Headers (Power)                           | 8 Position Receptacle Connector, 2.54mm pitch         |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J8         | Arduino Header (Analog)                           | 6 Position Receptacle Connector, 2.54mm pitch         |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J9         | Arduino Header (Digital 1                         | 10 Position Receptacle Connector, 2.54mm pitch        |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J10        | Arduino Header (Digital 0)                        | 8 Position Receptacle Connector, 2.54mm pitch         |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J11        | Arduino Header (IFCSP)                            | 6 Position, 2 row, Receptable Connector, 2.54mm pitch |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J12        | SDP Connector                                     | 120-way connector, 0.6 mm pitch                       |
+------------+---------------------------------------------------+-------------------------------------------------------+
| J13        | Earth for electromagnetic discharge (ESD testing) | Not applicable                                        |
+------------+---------------------------------------------------+-------------------------------------------------------+

Power Supplies
==============

By default, the board is powered from the USB. The board can be also powered from the J4 connector by setting LK3 to Position A or from Arduino standard headers The :adi:`ADuM6411 <en/products/Adum6411.html>` isoPower® digital isolator is used to isolate power and data lines up to 2.5 kV rms.

Serial Interface
================

The evaluation board connects via the serial peripheral interface (SPI) to the Blackfin® :adi:`ADSP-BF527 <en/products/adsp-bf527.html>` on the SDP-B board. There are four primary signals: CS, SCLK, DIN, and DOUT/RDY (all are inputs, except for DOUT/RDY, which is an output). The EVAL-AD4116ASDZ evaluation board connects to any microcontroller board that uses the Arduino standard headers. This can be developed user code in for a variety of platforms.

To operate the evaluation board in standalone mode, disconnect any board connected, J9 can be used to access all SPI signals and set the input/output voltage levels.

For an introduction to the Serial Peripheral Interface (SPI), click :adi:`here <en/analog-dialogue/articles/introduction-to-spi-interface.html>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4116asdz/spi_int_for_wikipage.png
   :align: center

Analog Inputs
=============

Eleven voltage inputs are available on P1 to P3. If a different common voltage must be set for single-ended measurement, remove LK2 and connect the desired voltage to VINCOM on P2. Five additional low-level inputs are available on P4. The differential voltage for these inputs is ±VREF only.

Reference Options
=================

The EVAL-AD4116ASDZ includes an external 2.5 V reference, the ADR4525ARZ. By default, LK1 is inserted, connecting the external reference to REF+ of the AD4116. Remove LK1 if using a different single-ended external reference. In the evaluation software, click the blue pop-up button associated with Setup 0 to Setup 7 to select the reference used for conversions by the AD4116. The pop-up button is located below the external reference controls in the block diagram (Label 7 in Figure 16).

Schematic, PCB Layout, Bill of Materials
========================================

.. admonition:: Download
   :class: download

   EVAL-AD4116ASDZ Rev B Design and Integration Files

   
   -  `schematic.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/schematic.pdf>`_
   
   -  `layout.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/layout.pdf>`_
   
   -  `bom.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4116asdz/bom.xlsx>`_
   


| :doc:`Continue to Software Guide </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`
| :doc:`Return to Homepage </wiki-migration/resources/eval/user-guides/eval-ad4116asdz>`
