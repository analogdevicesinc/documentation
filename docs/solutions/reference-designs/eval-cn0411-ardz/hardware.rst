.. _eval-cn0411-ardz-hardware:

Hardware Guide
==============

The EVAL-CN0411-ARDZ shield connects to the :adi:`EVAL-ADICUP360 <ADICUP360>`
base board using the Arduino mating headers.

.. figure:: cn0411_shunt_headers.jpg
   :align: center
   :width: 500

   EVAL-CN0411-ARDZ with labeled hardware connections and jumper headers

Total Dissolved Solids Measurement
----------------------------------

The measurement of total dissolved solids in a solution relies primarily on the
conductivity and temperature of the solution. The TDS factor, used to compute
TDS from the temperature-compensated conductivity value, varies at a defined
range for different types of solutions based on the type of dissolved solids.
The temperature coefficient used for compensation also depends on the type of
dissolved solid. Thus, total dissolved solids remains a general measure for
water quality and cannot distinguish between the constituents of the dissolved
solids in the solution.

Sensor Connections
~~~~~~~~~~~~~~~~~~

The EVAL-CN0411-ARDZ has three hardware connectors which have no polarity and
can connect directly to the sensors.

**J1** -- BNC connector for 2-wire conductivity probes. This is compatible with
common commercial probes. Below are recommended probes of different cell
constants:

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Cell Constant
     - Description
     - Conductivity Range
   * - 0.1
     - CS SK21T 2-Electrode Glass Cell
     - 0.1 uS/cm to 100 uS/cm
   * - 1
     - CS SK20T 2-Electrode Glass Cell
     - 100 uS/cm to 10 mS/cm
   * - 10
     - CS SK23T 2-Electrode Glass Cell
     - 10 mS/cm to 1 S/cm

**P2** -- Terminal block connector for conductivity probes without a BNC plug.

.. figure:: cn0411_probe_connection.png
   :align: center
   :width: 500

   P2 probe connection diagram

**P3** -- Terminal block connector for a 2-wire RTD. The software is compatible
with Pt100 and Pt1000 RTDs.

.. figure:: cn0411_rtd_connection.png
   :align: center
   :width: 500

   P3 RTD connection diagram

Jumper Configurations
~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0411-ARDZ has four jumper headers which configure different settings.
The default shunt positions are highlighted below.

.. figure:: cn0411_board_silkscreen.png
   :align: center
   :width: 500

   Board silkscreen with jumper positions

**PRB_SEL** -- Selects the connection to the conductivity sensor. By default,
the shunt is placed connecting pin 1 and 2 to measure the conductivity of the
solution.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - PRB_SEL Shunt Position
     - Conductivity Sensor Connection
   * - 1 and 2
     - Conductivity Probe
   * - 3 and 4
     - 200 ohm Precision Resistor (calibration in 0.01 S range)
   * - 5 and 6
     - 20 ohm Precision Resistor (calibration in 0.1 S range)

**P6** -- Selects the input to the :adi:`AD8220` instrumentation amplifier. By
default, the shunt position connects pins 1 and 2 to sample the conductivity
sensor.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - P6 Shunt Position
     - AD8220 Input
   * - 1 and 2
     - Conductivity Sensor
   * - 2 and 3
     - 0V (for zero-scale calibration)

**CS_ADC** -- Selects the chip select GPIO pin for the :adi:`AD7124-8`. Allows
multiple board stack-up. Default connects pins 1 and 2 to GPIO28.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - CS_ADC Shunt Position
     - AD7124-8 Chip Select
   * - 1 and 2
     - DIGI1 Pin 1 or GPIO28
   * - 3 and 4
     - DIGI1 Pin 2 or GPIO30

**CS_DAC** -- Selects the chip select GPIO pin for the :adi:`AD5683R`. Default
connects pins 1 and 2 to GPIO26.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - CS_DAC Shunt Position
     - AD5683R Chip Select
   * - 1 and 2
     - DIGI1 Pin 3 or GPIO26
   * - 3 and 4
     - DIGI0 Pin 3 or GPIO15

Conductivity Measurement
------------------------

The system measures conductivity using a 2-wire conductivity probe immersed in
the solution.

.. figure:: cn0411_probe_immersion.png
   :align: center
   :width: 200

   Conductivity probe immersion

It is preferable that the conductivity probe be positioned at the center of the
container to maximize measurement accuracy. The cell constant of a 2-wire
conductivity probe is the distance between its two cells or electrodes divided
by their inner surface area.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Cell Constant
     - Range of Measured Conductivity
   * - 0.01
     - < 0.1 uS/cm
   * - 0.1
     - 0.1 uS/cm to 100 uS/cm
   * - 1
     - 100 uS/cm to 10 mS/cm
   * - 10
     - 10 mS/cm to 1 S/cm

Conductivity probes have different rated voltages. Before connecting the probe
to the CN0411, check the excitation voltage setting in the software and
configure it to within the specified rating.

The frequency of the excitation signal across the conductivity cells depends on
the range of conductivity measurement. The system can switch between 94 Hz
(suitable for measurements in the uS range) and 2.4 kHz (suitable for
measurements in the mS range and above).

Temperature Measurement
-----------------------

The system can use either Pt100 or Pt1000 RTD sensors, configurable through the
software. Most commercial probes have these RTDs built in to the conductivity
probe.

The temperature coefficient depends on the type of solution and can be
configured in the software. The system has built-in stored values:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Salt Solution
     - Temperature Coefficient (alpha)
   * - Potassium Chloride (KCl)
     - 1.88
   * - Sodium Chloride (NaCl)
     - 2.14

TDS Computation
---------------

The total dissolved solids in the solution is computed from the
temperature-compensated conductivity measurement by the TDS factor, which varies
per type of dissolved solid. The system has built-in stored values:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Salt Solution
     - Range of TDS Factor (ke)
   * - Potassium Chloride (KCl)
     - 0.50 to 0.57
   * - Sodium Chloride (NaCl)
     - 0.47 to 0.50

Calibration and Auto-ranging
-----------------------------

The system can automatically select the proper gain resistance from the
user-defined excitation voltage when commanding the system to measure TDS.

.. figure:: cn0411_autorange_flowchart.png
   :align: center
   :width: 500

   Auto-range gain resistance selection procedure

Zero-Scale Calibration
~~~~~~~~~~~~~~~~~~~~~~~

To decrease the effect of system noise on the measurement, zero-scale
calibration should be performed once per board:

#. Place the shunt position of jumper header **P6** to connect pins 2 and 3.
#. Command the software to perform zero-scale calibration (``syscal`` command).
#. Wait for the command to finish.
#. Place the shunt position of jumper header **P6** back to pins 1 and 2.

Reference-Resistor Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To increase accuracy in the 0.01 S or 0.1 S range, reference-resistor
calibration should be performed once per board:

#. Place the shunt position of **PRB_SEL** to connect pins 3 and 4 (for 0.01 S
   range) or pins 5 and 6 (for 0.1 S range).
#. Command the software to perform reference resistor calibration (``refres``
   command).
#. Wait for the command to finish.
#. Place the shunt position of **PRB_SEL** back to pins 1 and 2.
