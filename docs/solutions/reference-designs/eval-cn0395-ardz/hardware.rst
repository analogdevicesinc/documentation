.. _eval-cn0395-ardz hardware:

Hardware
========

This page describes the hardware setup and connector configuration for the
:ref:`eval-cn0395-ardz` shield board used with the EVAL-ADICUP360 development
platform.

The EVAL-CN0395-ARDZ shield is designed to be compatible with the Arduino R3
shield form factor and is compatible with either 5 V or 3.3 V processor boards.

Connectors and Jumper Configurations
-------------------------------------

.. figure:: jumper_config.jpg
   :align: center
   :width: 600

   EVAL-CN0395-ARDZ jumper and connector configuration

Headers
~~~~~~~

**P1 -- ENCOMP Pin**

The current output DAC, :adi:`ADN8810 <ADN8810>`, has an output voltage
compliance that needs to be met to maintain a linear current output. This can
be configured using the P1 jumper:

- **Position 2-3**: Attaches the ENCOMP pin to ground for output voltages up
  to 2 V.
- **Tie to +5 V**: For higher output voltages above 2 V, tie the ENCOMP pin to
  +5 V to maintain output stability.

**P2 -- Current Path Selection**

P2 header selects the current path from the ADN8810. It is populated across
RH+ by default.

.. list-table:: P2 Current Path Selection
   :header-rows: 1

   * - Silkscreen
     - Current Path
     - Pins
   * - RCAL1
     - 71.5 Ohm
     - 1 & 2
   * - RCAL1
     - 10.0 Ohm
     - 3 & 4
   * - RH+
     - Heating Resistor
     - 5 & 6

Sensor
~~~~~~

The CN0395 has the `Figaro TGS8100
<http://www.figarosensor.com/products/entry/tgs8100.html>`__ on board as the
default sensor. Using a different sensor requires recalculation and replacement
of the sense resistors that set the full-scale current for the device.

Provision for Alphasense sensors (or sensors with similar footprint) is
available, and a screw terminal is in place for any other types of sensors.

.. warning::

   The calculation for the sense resistor and placement of the correct sense
   resistors are crucial to proper operation of the board. Incorrect values may
   violate absolute maximum ratings of the sensors.

**Recommended Sensors:**

- `Figaro TGS8100
  <http://www.figarosensor.com/products/entry/tgs8100.html>`__
- `Alphasense VOC-MF1
  <http://www.alphasense.com/index.php/products/metal-oxide-sensors-2/>`__

If you are using a different sensor, you will need to wire in the appropriate
signals into the board via the screw terminal (P8). This also means that you
will have to remove the TGS8100 sensor that comes on the board by default.

**P8 -- External Sensor Screw Terminal**

.. list-table:: P8 Screw Terminal Connections
   :header-rows: 1

   * - Silkscreen Name
     - Pin Number
     - Description
   * - RH+
     - Pin 1
     - Positive pin of heating resistor
   * - AGND
     - Pin 2
     - Negative pin of heating resistor
   * - RS+
     - Pin 3
     - Positive pin of sensing resistor
   * - AGND
     - Pin 4
     - Negative pin of sensing resistor

Spacers
~~~~~~~

Spacers that accommodate various surface mount and through-hole packages are
available on the board for easy modifications.

Resistor spacers **R17_SPACER** and **R19_SPACER** hold the sense resistors
that select the maximum output current of the ADN8810. Changing the maximum
output current allows the board to support multiple types of sensors that use
up to 300 mA of current for measurements.

Sense resistors (RSN) can be calculated using:

.. code-block:: none

   RSN = 4.096 / (10 * Full Scale Current)

Button
~~~~~~

Pressing push button **S2** allows the user to perform a hard reset of the
temperature and humidity sensor (Sensirion SHT-30).

Setting Up the Hardware
-----------------------

1. To program the base board, set the jumpers/switches as shown in the figure
   below. The important jumpers/switches are highlighted in red.

   .. figure:: cn0216_hw_config.png
      :align: center
      :width: 600

      EVAL-ADICUP360 jumper and switch configuration for programming

2. Connect the **EVAL-CN0395-ARDZ** to the Arduino connectors **P2, P5, P6,
   P7, P8** of the **EVAL-ADICUP360** board.
3. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).
