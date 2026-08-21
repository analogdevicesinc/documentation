.. _eval-ad7124-4-8sdz_hardware:

EVAL-AD7124-4SDZ / EVAL-AD7124-8SDZ Hardware Guide
===============================================================================

Set-up Procedures
-------------------------------------------------------------------------------

After reviewing the :ref:`prerequisites <eval-ad7124-x prerequisites>`, set up
the evaluation board as detailed in this section.

Using the SDP-B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the :adi:`SDP-B` to the evaluation board via the
   120-pin SDP connector (J1). The SDP-B can connect to Connector A or
   Connector B on the evaluation board.
#. Screw the two boards together using the plastic screw and washer set.
#. Connect a 7--9 V DC supply to J3 (bench top) or J5 (wall wart/DC plug).
   Select the supply connector using LK2 (Position A for J3, Position B for
   J5).
#. Connect the :adi:`SDP-B` to the PC using a USB cable.

Using the Nucleo-L476RG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the evaluation board to the Nucleo-L476RG via the
  :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`. See the
  :ref:`SPI wiring table <eval-ad7124-x quickstart nucleo>` for pin
  connections.
- Connect a 7--9 V DC power supply to the evaluation board.
- Connect the Nucleo-L476RG to the PC via USB.

Power Supplies
-------------------------------------------------------------------------------

The evaluation board requires an external 7--9 V DC power supply, applied to
either J3 (bench top) or J5 (wall wart/DC plug). Only one supply connector is
used at a time, selected via LK2.

On-board regulators generate all required supply rails:

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Supply
     - Regulator
     - Function
   * - AVDD (3.3 V)
     - ADP1720-3.3 (U7)
     - Supplies AVDD to the AD7124 (default)
   * - AVDD (1.8 V)
     - ADP1720 (U4)
     - Alternative AVDD supply (selected via SL3/SL7)
   * - IOVDD (3.3 V)
     - ADP1720-3.3 (U10)
     - Supplies IOVDD to the AD7124
   * - SDP 5 V
     - ADP7104ARDZ-5.0 (U2)
     - Powers the SDP-B controller board
   * - Reference (2.5 V)
     - ADR4525
     - Precision external reference for the ADC

When a split supply is used, AVSS must be applied externally via connector J9.
AVDD and IOVDD can also be supplied externally via J9, but the 7--9 V supply is
still required to power the on-board ADR4525 reference.

.. list-table:: External Power Supply Options
   :header-rows: 1

   * - Connector
     - Voltage Range
     - Notes
   * - J3
     - 7--9 V
     - Bench top supply. Set LK2 to Position A.
   * - J5
     - 7--9 V
     - Wall wart/DC plug supply (default). Set LK2 to Position B.

Link and Jumper Settings
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 78

   * - Link
     - Default
     - Description
   * - LK1
     - A
     - Connects AVDD to power supply sequencer (ADM1185).
       Pos A: AVDD = 3.3 V; Pos B: AVDD = 1.8 V.
   * - LK2
     - B
     - Selects power supply connector. Pos A: J3 (bench top);
       Pos B: J5 (wall wart/DC plug).
   * - LK3
     - Inserted
     - Connects REFIN(-) to AVSS.
   * - LK4
     - 2.5 V
     - Selects reference source. 2.5 V position: REFIN1(+) to ADR4525;
       INT REF position: REFIN1(+) to REFOUT pin.
   * - LK5
     - Inserted
     - Shorts AIN0 to AIN1 for noise testing. Enable internal bias on
       AIN0 or AIN1 for proper noise test voltage level.
   * - LK6
     - Inserted
     - AIN4/AIN5 connection. Jumpers in place: connects to on-board
       thermistor for cold junction measurement. Remove jumpers to
       connect external components.
   * - SL2
     - A
     - AVDD source. Pos A: from on-board regulator; Pos B: from external
       supply via J9.
   * - SL3, SL7
     - A, A
     - AVDD voltage. Pos A: 3.3 V (U7); Pos B: 1.8 V (U4).
   * - SL5
     - B
     - IOVDD source. Pos A: external via J9; Pos B: on-board 3.3 V (U10).
   * - AVSS/AGND
     - Inserted
     - Ties AVSS to AGND. Remove when using -1.8 V AVSS.

On-Board Connectors
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Connector
     - Function
   * - J1
     - 120-pin SDP connector for :adi:`SDP-B`
   * - J2
     - SMB/SMA footprint for external master clock (not populated)
   * - J3
     - Bench top power supply input (7--9 V)
   * - J5
     - Wall wart/DC plug power supply input (7--9 V, default)
   * - J6
     - Analog input connector: AIN0--AIN5, REFIN1(+/-). For RTD
       connections.
   * - J9
     - External supply connector for AVDD, IOVDD, and AVSS
   * - J11
     - Analog input connector: AIN6--AIN7, REFIN1(+/-), analog power.
       For load cell connections.
   * - J12
     - 6-pin I2C interface for digital temperature sensor (ADT7320-CJC).
       Required for thermocouple cold junction compensation via A2.
   * - J13
     - 7-pin connector for external amplifier on AIN4/AIN5
   * - J14
     - 7-pin connector for direct AIN4/AIN5 access
   * - A0, A1
     - SMB/SMA footprints for AIN4 and AIN5 analog inputs (not populated)
   * - A2
     - Thermocouple connector
   * - A5, A6
     - SMB/SMA footprints for REFIN1(+) and REFIN1(-) (not populated)

Analog Inputs
-------------------------------------------------------------------------------

Analog input voltages can be applied in two ways:

- Using J6 and J11, the green screw terminal connectors
- Using the A0 and A1 SMB/SMA footprints (connecting to AIN4 and AIN5)

The AD7124 Eval+ Software is set up to analyze DC inputs to the ADC.

Serial Interface
-------------------------------------------------------------------------------

The AD7124 communicates via a 4-wire SPI interface: CS, SCLK, DIN, and
DOUT/RDY.

When using the :adi:`SDP-B`, the SPI signals connect via the 120-pin SDP
connector to the Blackfin ADSP-BF527 on the SDP board.

When using the Nucleo-L476RG, SPI connections are made via the
:adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`:

.. list-table:: SPI Wiring (via SDP Breakout Board)
   :header-rows: 1
   :widths: 25 25 30

   * - AD7124 SPI Signal
     - SDP Breakout Board Pin
     - Nucleo-L476RG Pin
   * - GND
     - 81
     - GND on CN5.7
   * - SCLK
     - 82
     - D3 (PB3) on CN9.4
   * - DOUT/RDYB
     - 83
     - D5 (PB4) on CN9.6
   * - DIN
     - 84
     - D4 (PB5) on CN9.5
   * - CSB
     - 85
     - D6 (PB10) on CN9.7

**Standalone mode:** The SPI signals can be disconnected from the 120-pin
header by removing the 0 ohm links R9 through R13. The test points can then be
used to fly-wire the signals to an alternative digital capture setup.

Reference Options
-------------------------------------------------------------------------------

The evaluation board includes an on-board 2.5 V ADR4525 precision voltage
reference and the AD7124's internal 2.5 V reference.

The default configuration uses the external ADR4525 reference (LK4 in 2.5 V
position). To use the internal reference routed externally, set LK4 to the
INT REF position.

The reference source for each conversion is selected through the configuration
registers (Setup 0 to Setup 7) in the evaluation software.

Design and Integration Files
-------------------------------------------------------------------------------

Schematics, layout files, and bill of materials are available on the
:adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` and
:adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` product pages.
