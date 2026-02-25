.. _adalm-buck-ardz:

ADALM-BUCK-ARDZ
================

Buck Converter Active Learning Module.

Overview
--------

The ADALM-BUCK-ARDZ is a companion module designed for the Buck Basics lab
exercise, eliminating breadboard assembly time while preserving experimental
measurements and hands-on learning. The board functions as a pre-assembled buck
converter circuit module that pairs with the :adi:`ADALM2000` active learning
module and Arduino UNO platform, enabling students to conduct converter
characterization experiments without manual circuit construction.

Required Equipment
------------------

- ADALM-BUCK-ARDZ evaluation board
- :adi:`ADALM2000` active learning module
- Arduino UNO (or compatible clone)
- USB cables

Hardware Setup
--------------

**Jumper Settings (Default Configuration):**

- **P1** -- Power supply selection (5 V from Arduino).
- **P2** -- Inductor tap configuration (6 taps / maximum inductance).
- **P3, P6, P18** -- Open connections (ADALM2000 measurement points).
- **P5** -- DC coupling enabled.
- **P13** -- Arduino PWM source selected.
- **P19--P20** -- Output capacitors (10 uF and 47 uF) enabled.
- **P24** -- Arduino PWM output 3 connection.

**ADALM2000 Measurement Connections:**

- **Channel 1** -- Switch node voltage measurement.
- **Channel 2** -- Ripple current measurement.

Software Setup
--------------

Upload the ``LT1054_voltage_mode_buck_DC_ctrl.ino`` sketch to the Arduino UNO.
Details are provided in the Buck Basics lab exercise documentation.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `ADALM-BUCK-ARDZ Design & Integration Files
   <https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/adalm-buck-ardz-designsupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADALM2000 Product Page <ADALM2000>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
