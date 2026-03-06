.. _eval-cn0216-ardz-hardware:

Hardware
========

EVAL-CN0216-ARDZ Shield
-----------------------

:adi:`CN0216 <CN0216>` is a precision weigh scale signal conditioning system.
It uses the :adi:`AD7791`, a low power buffered 24-bit sigma-delta ADC along
with dual external :adi:`ADA4528-2` zero-drift amplifiers. This solution allows
for high dc gain with a single supply.

Ultralow noise, low offset voltage, and low drift amplifiers are used at the
front end for amplification of the low-level signal from the load cell. The
circuit yields 15.3 bit noise-free code resolution for a load cell with a
full-scale output of 10 mV.

.. figure:: cn0216revc_-_1.png
   :align: center
   :width: 500

   EVAL-CN0216-ARDZ Rev C Board

The :adi:`AD7791` maintains good performance over the complete output data
range, from 9.5 Hz to 120 Hz, which allows it to be used in weigh scale
applications that operate at various low speeds.

.. important::

   The EVAL-CN0216-ARDZ is powered from the **VIN** connector on the Arduino
   Uno header. The bridge drive voltage requires more than 5 V to power the
   bridge. Therefore it is required to supply power from the baseboard through
   the DC power connector for proper functionality. The board will not work
   properly if you try only to power it from USB.

Connectors and Jumper Configurations
-------------------------------------

Sensor Connector
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Pin Number
     - Pin Function
   * - Pin 1
     - Not Used
   * - Pin 2
     - - Excitation
   * - Pin 3
     - + Signal
   * - Pin 4
     - - Sense
   * - Pin 5
     - + Sense
   * - Pin 6
     - - Signal
   * - Pin 7
     - + Excitation
   * - Pin 8
     - Not Used

.. figure:: cn0216-wiring_schematic.png
   :align: center
   :width: 400

   Load Cell Wiring Schematic

REF SEL / Bridge Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These jumpers allow the circuit to be configured for use with 4-wire or 6-wire
load cells.

.. note::

   Any 4- or 6-wire load cells can be used with the EVAL-CN0216-ARDZ. The
   Tedea-Huntleigh Model 1042 load cell was used during testing.

**6-Wire Resistive Bridge Configuration:**

.. figure:: cn0216_ref_sel_-_2.png
   :align: center
   :width: 100

   6-wire bridge jumper positions

Place jumpers/shunts as shown above for 6-wire configuration:

- **P1** -- Connects ADC REFIN+ to Sensor +Sense pin
- **P2** -- Connects ADC REFIN- to Sensor -Sense pin

**4-Wire Resistive Bridge Configuration:**

.. figure:: cn0216_ref_sel_-_1.png
   :align: center
   :width: 100

   4-wire bridge jumper positions

Place jumpers/shunts as shown above for 4-wire configuration:

- **P1** -- Connects ADC REFIN+ to 5 V supply
- **P2** -- Connects ADC REFIN- to GND

Chip Select
~~~~~~~~~~~

This set of jumpers allows changing the pin mapping of the AD7791 chip select
line to different Arduino digital pins. Place jumper/shunt as shown to connect
to the corresponding Digital IO pin:

.. figure:: cn0216_cs_sel_-_1.png
   :align: center
   :width: 100

   CS -- Arduino Digital Pin 10

.. figure:: cn0216_cs_sel_-_2.png
   :align: center
   :width: 100

   CS -- Arduino Digital Pin 9

.. figure:: cn0216_cs_sel_-_3.png
   :align: center
   :width: 100

   CS -- Arduino Digital Pin 8

.. note::

   If using an EVAL-CN0216-ARDZ board prior to Rev C, install a 0-ohm resistor
   to resistor pads R7, R8, or R9 to change the CS pin:

   - **R7** -- Arduino Digital Pin 8
   - **R8** -- Arduino Digital Pin 9
   - **R9** -- Arduino Digital Pin 10

Change Log
----------

Rev B to Rev C:

- U3 changed from ADG3304BRUZ to NLSX4402FMUTCG
- U4 added (NLSX4402FMUTCG)
- C19 and C20 added (0.1 uF)
- R7, R8, R9 added to short MOSI, MISO, SCLK lines between ICSP and Arduino
  D11, D12, D13
- AD7791_CS header added
