.. imported from: https://wiki.analog.com/university/tools/m2k/accessories/power

.. _ad-m2kpwr-ebz:

AD-M2KPWR-EBZ
==============

ADALM2000 Power Booster Board.

The :adi:`AD-M2KPWR-EBZ` is an :adi:`ADALM2000` add-on board which increases
the output current capability up to 700 mA. This board can also be used as a
standalone benchtop power supply with positive and negative outputs.

.. grid::
   :widths: 50% 50%

   .. figure:: ad-m2kpwr-ebz-top-web.png
      :width: 400px

      AD-M2KPWR-EBZ top view

   .. figure:: ad-m2kpwr-ebz-bottom-web.png
      :width: 400px

      AD-M2KPWR-EBZ bottom view

Features
--------

- :adi:`ADALM2000` compatible
- USB Type-C powered (no Power Delivery included)
- Provides two outputs with increased current sourcing capabilities

Description
-----------

The AD-M2KPWR-EBZ is a USB Type-C powered board capable of increasing the
output current of the ADALM2000 power supplies.

**Inputs:**

.. list-table::
   :header-rows: 1

   * - Input
     - Voltage Range
     - Max Power
   * - USB Type-C
     - 4--18 V
     - 15 W
   * - External screw terminal
     - 4--18 V
     - 20 W

**Outputs** (two control modes):

.. list-table::
   :header-rows: 1

   * - Mode
     - Positive Output
     - Negative Output
   * - M2K (tracks ADALM2000 supplies)
     - 0 V to 5 V, 400 mA (USB powered)
     - -5 V to 0 V, 400 mA (USB powered)
   * - POT (potentiometer-adjusted)
     - 1.5 V to 15 V, up to 700 mA at 18 V input
     - -15 V to -1.5 V, up to 700 mA at 18 V input

Applications
~~~~~~~~~~~~

- General-purpose electronic systems
- Educational applications
- Automated test equipment

Package Contents
----------------

- AD-M2KPWR-EBZ board
- Standoffs and mounting screws

.. figure:: ad-m2kpwr-ebz-angle-web.png
   :align: center
   :width: 400

   AD-M2KPWR-EBZ package contents

Getting Started
---------------

The AD-M2KPWR-EBZ must be supplied either from a 5.1 V / 3 A USB Type-C power
adapter or from a lab supply using the screw terminal connector. Use the jumper
on the P2 connector to select the power source:

.. figure:: m2kpwr_supply_jumper.png
   :align: center
   :width: 400

   AD-M2KPWR-EBZ supply select jumper

.. list-table::
   :header-rows: 1

   * - P2 Position
     - Selected Supply
   * - Jumper 1-2 shorted
     - Vext -- external lab supply
   * - Jumper 2-3 shorted
     - Vusb -- USB Type-C power adapter

M2K and POT Modes
~~~~~~~~~~~~~~~~~~

In **M2K mode**, the board is plugged into the ADALM2000. The programmable user
supplies of the ADALM2000 can be used as usual, but with increased current
sourcing. Set the jumpers on P6 and P7 to the M2K positions.

In **POT mode**, the board operates as a standalone benchtop power supply. The
output voltage is adjusted with potentiometers R19 (negative) and R20
(positive). The output voltage is available at the V+ and V- pins.

.. figure:: m2kpwr_pot_control.png
   :align: center
   :width: 500

   AD-M2KPWR-EBZ POT/M2K mode setup jumpers

.. list-table::
   :header-rows: 1

   * - P6 Position
     - Positive Output Voltage
   * - Jumper 1-2 shorted
     - Potentiometer-adjusted (1.5 V to 15 V)
   * - Jumper 2-3 shorted
     - M2K positive supply (0 V to 5 V)

.. list-table::
   :header-rows: 1

   * - P7 Position
     - Negative Output Voltage
   * - Jumper 1-2 shorted
     - Potentiometer-adjusted (-15 V to -1.5 V)
   * - Jumper 2-3 shorted
     - M2K negative supply (-5 V to 0 V)

Gain Configuration
~~~~~~~~~~~~~~~~~~

The board can be configured so that the output voltage is double or triple the
value set from the ADALM2000. This feature is only available in M2K mode and
is activated by soldering or desoldering the solder jumpers on the bottom of
the board. Refer to the table printed on the bottom of the board for soldering
instructions.

Schematics and CAD Files
-------------------------

.. admonition:: Download

   - :download:`Rev B Schematics <02-065173-01-b.pdf>`
   - :download:`Rev B Gerbers <09-065173-01b.zip>`
   - :download:`Rev B Cadence Project <20-065173-01b.zip>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the :ez:`/`.
