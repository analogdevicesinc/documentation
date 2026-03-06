Hardware Guide
==============

Device Description
------------------

The :adi:`AD4113 <en/products/ad4111.html>` is a highly accurate, high resolution, multiplexed, Σ-Δ ADC with eight single-ended or four differential voltage inputs. The maximum channel to channel scan rate is 6.21 kSPS (161 µs) for fully settled data. The output data rates range from 1.25 SPS to 31.25 kSPS. The device includes integrated analog reference buffers, an integrated precision 2.5 V reference, and an integrated oscillator. See the AD4113 data sheet for complete specifications. Full details on the EVAL-AD4113ARDZ are available on the product page on the Analog Devices website.

Set-up Procedures
-----------------

After following the instructions in the Software Installation Procedures section, set up the evaluation board and the SDP-K1 board as detailed in this section.

.. important::

   The ACE software and drivers must be installed before connecting the EVAL-AD4113ARDZ and the EVAL-SDP-CK1Z board to the USB port of the PC to ensure that the PC correctly recognizes the evaluation system


| **Configuring the Evaluation and SDP Boards**
| Use the following procedure to configure the boards

-  Connect the SDP-K1 to the Arduino headers of the evaluation board.
-  If using the SDP-K1 board the Arduino headers can also be used to connect to the board
-  Ensure that LK10 is in Position A (USB)
-  Connect the SDP board to the PC using the USB cable.

Evaluation Board
----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/board_photo.png
   :align: center
   :width: 600px

Hardware Link Options
---------------------

+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Number  | Default Position | Description                                                                                                                                                                                                 |
+==============+==================+=============================================================================================================================================================================================================+
| LK1          | B                | Selects which inverter to use. **Position A**: LTC1983 is used as inverter. **Position B**: ADP5075 is used as inverter.                                                                                    |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK2          | B                | Enables the :adi:`LTC1983 <en/products/ltc1983.html>` (U7) LDO for split. Vout of U7 is Vin for ADP7182. **Position A**: U7 Vout = -3.3 V. **Position B**: LTC1983 is in shutdown mode.                     |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK3          | B                | Selects between LTC1983 or ADP5075 output. **Position A**: Use LTC1983_VOUT. **Position B**: Use ADP5075_VOUT.                                                                                              |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK4          | B                | Used for bypassing LDO (U8). **Position A**: -2.5 V Output, set to bypass LDO (U8) only. **Position B**: -3 V Output.                                                                                       |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK5          | A                | Used for bypassing LDO (U8). **Position A**: Connects to LDO. **Position B**: Bypass LDO. **NOTE: Do not bypass LDO (U8) when using LTC1983 for split supply configuration**                                |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK6          | B                | Enables the :adi:`ADP7182 <en/products/adp7182.html>` LDO (U8) for split supply configuration. **Position A**: ADP7182 Vout= -2.5 V. **Position B**: ADP7182 is in shutdown mode                            |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK7          | Inserted         | Disconnect to bypass LDO (U8).                                                                                                                                                                              |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK8          | B                | Enables the :adi:`ADP150 <en/products/adp150.html>` (U3) LDO for split supply configuration. **Position A**: ADP150 Vout = 2.5 V. **Position B:** ADP150 is in shutdown mode                                |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK9          | A                | Enable options for 5 V and 3.3 V supply for AVDD. **Position A**: AVDD = 5 V. **Position B**: AVDD = 3.3 V                                                                                                  |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK10         | A                | Selects the power supply voltage. **Position A**: board is powered from USB through the Arduino Connector. **Position B**: board is powered from external dc power supply connector                         |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK11         | B                | Selects which external reference to use. **Position A**: LTC6655 will be used sa reference. **Position B**: ADR4525 will be used as reference.                                                              |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK12         | Inserted         | Connects the on-board external reference :adi:`ADR4525 <en/products/adr4525.html>` for 2.5 V voltage reference of the ADC core. Remove LK12 if using a different external reference                         |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK13         | B                | **Position A**: LTC6655 output is used as reference. **Position B**: ADR4525 output is used as reference.                                                                                                   |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK14 to LK16 | STD              | Selects which Arduino SPI Lines to connect. **STD**: Standard Arduino Headers. **ALT**: Alternate IFCSP Header.                                                                                             |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK17         | A                | **Position A:** Selects CS_ARD_1. **Position B:** Selects CS_ARD_2. **Position C:** Selects CS_ARD_3. **Position D:** Selects CS_ARD_4.                                                                     |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK18         | Inserted         | Connects VINCOM to GND_ISO. This configuration is typical for single-ended measurement.                                                                                                                     |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK19         | Inserted         | Shorts VIN0 and VIN1 for noise test configuration                                                                                                                                                           |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK20, LK22   | Removed          | Connects VIN0 and VIN1 to the Zener diode, D7 and D8 respectively to evaluate the voltage inputs of the AD4111 directly by removing external components.                                                    |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK21, LK23   | Inserted         | Bypasses R27 and R28 on VIN0 and VIN1 respectively. By inserting this link, the resistor is removed from the input path and AD4111 can be evaluated directly.                                               |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK24         | A                | Selects the IOVDD supply. **Position A**: Connects IOVDD to SWD_AVDD for 5V or 3.3V Single Supply. **Position B**: Connects IOVDD to 2.5V. Used for Split Supply                                            |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK25         | A                | Used to shutdown ADUM6421 for isolation purpose only. **Position A**: Turns the ADUM6421 in OFF or SHUTDOWN MODE **Position B**: ADUM6421 is ON                                                             |
+--------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Follow each Link setting for different configurations.

.. container:: center

   
   ===================================================== ========
   **Single supply**: AVDD = 5 V, AVSS = 0V, IOVDD = 5 V 
   ===================================================== ========
   Link Number                                           Position
   LK1                                                   B
   LK2                                                   B
   LK3                                                   B
   LK4                                                   B
   LK5                                                   A
   LK6                                                   B
   LK7                                                   Removed
   LK8                                                   B
   LK9                                                   A
   LK10                                                  A
   LK11                                                  B
   LK12                                                  Inserted
   LK13                                                  B
   LK14                                                  A
   LK15                                                  A
   LK16                                                  A
   LK17                                                  A
   LK18                                                  Inserted
   LK19                                                  Inserted
   LK20                                                  Removed
   LK21                                                  Inserted
   LK22                                                  Removed
   LK23                                                  Inserted
   LK24                                                  A
   LK25                                                  B
   ===================================================== ========
   
   +---------------------------------------------------------+----------------------------------------------------------+
   | **Single supply**: AVDD = 5 V, AVSS = 0V, IOVDD = 3.3 V |                                                          |
   +=========================================================+==========================================================+
   | Link Number                                             | Position                                                 |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK1                                                     | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK2                                                     | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK3                                                     | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK4                                                     | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK5                                                     | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK6                                                     | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK7                                                     | Removed                                                  |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK8                                                     | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK9                                                     | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK10                                                    | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK11                                                    | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK12                                                    | Inserted                                                 |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK13                                                    | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK14                                                    | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK15                                                    | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK16                                                    | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK17                                                    | A                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK18                                                    | Inserted                                                 |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK19                                                    | Inserted                                                 |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK20                                                    | Removed                                                  |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK21                                                    | Inserted                                                 |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK22                                                    | Removed                                                  |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK23                                                    | Inserted                                                 |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK24                                                    | Removed. \*Connect IOVDD to external 3.3V supply via Pin |
   +---------------------------------------------------------+----------------------------------------------------------+
   | LK25                                                    | B                                                        |
   +---------------------------------------------------------+----------------------------------------------------------+
   
   On Board Connections
   ~~~~~~~~~~~~~~~~~~~~
   
   +-----------+------------------------------------+-------------------------------------------------------+
   | Connector | Function                           | Connector Type                                        |
   +===========+====================================+=======================================================+
   | P1        | Connects to GPIO’s of AD4113       | 2-pin header, 2.54mm pitch                            |
   +-----------+------------------------------------+-------------------------------------------------------+
   | P2, P3    | Voltage inputs to AD4113           | Connector, header, 90°, 5 position, 2.54 mm           |
   +-----------+------------------------------------+-------------------------------------------------------+
   | P4        | PMOD form factor                   | 12-pin header, 2.54mm pitch                           |
   +-----------+------------------------------------+-------------------------------------------------------+
   | J6        | External supply voltage (optional) | Connector, header, 90°, 3 position, 3.81 mm pitch     |
   +-----------+------------------------------------+-------------------------------------------------------+
   | J7        | Arduino Headers (Power)            | 8 Position Receptacle Connector, 2.54mm pitch         |
   +-----------+------------------------------------+-------------------------------------------------------+
   | J8        | Arduino Header (Analog)            | 6 Position Receptacle Connector, 2.54mm pitch         |
   +-----------+------------------------------------+-------------------------------------------------------+
   | J9        | Arduino Header (Digital 1          | 10 Position Receptacle Connector, 2.54mm pitch        |
   +-----------+------------------------------------+-------------------------------------------------------+
   | J10       | Arduino Header (Digital 0)         | 8 Position Receptacle Connector, 2.54mm pitch         |
   +-----------+------------------------------------+-------------------------------------------------------+
   | J11       | Arduino Header (IFCSP)             | 6 Position, 2 row, Receptable Connector, 2.54mm pitch |
   +-----------+------------------------------------+-------------------------------------------------------+
   


Power Supplies
==============

By default, the board is powered from the USB. The board can be also powered from the J6 connector by setting LK17 to Position B or from Arduino standard headers. The :adi:`ADuM6421A <en/products/adum6421a.html>` isoPower® digital isolator is used to isolate power and data lines up to

Serial Interface
================

The evaluation board connects via the serial peripheral interface (SPI) to the STM32F469NIH6 on the SDP-K1 board. There are four primary signals: CS, SCLK, DIN, and DOUT/RDY (all are inputs, except for DOUT/RDY, which is an output). The EVAL-AD4113ARDZ evaluation board connects to any microcontroller board that uses the Arduino standard headers. This can be developed user code in for a variety of platforms.

To operate the evaluation board in standalone mode, disconnect any board connected, J9 can be used to access all SPI signals and set the input/output voltage levels.

For an introduction to the Serial Peripheral Interface (SPI), click :adi:`here <en/analog-dialogue/articles/introduction-to-spi-interface.html>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4116asdz/spi_int_for_wikipage.png
   :align: center

Analog Inputs
=============

There are two types of analog inputs: voltage and current. Eight voltage inputs are available on P2 and P3. Four current inputs are available on P8. If a different common voltage must be set for single-ended measurement, remove LK10 and connect the desired voltage to VCOM on P2.

Reference Options
=================

The EVAL-AD4113ARDZ includes an external 2.5 V reference, the ADR4525 and LTC6655. By default, LK12 is inserted, connecting the external reference to the REF+ pin of the AD4113. Remove LK12 if using a different single-ended external reference.

Schematic, PCB Layout, Bill of Materials
========================================

.. admonition:: Download
   :class: download

   EVAL-AD4113ARDZ Rev B Design and Integration Files

   
   -  `schematic.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/schematic.pdf>`__
   
   -  `layout.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/layout.pdf>`__
   
   -  `bom.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4116asdz/bom.xlsx>`__
   


| :doc:`Continue to Software Guide </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`
| :doc:`Return to Homepage </wiki-migration/resources/eval/user-guides/eval-ad4116asdz>`
