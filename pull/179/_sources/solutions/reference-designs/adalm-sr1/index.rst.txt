.. _adalm-sr1:

ADALM-SR1
=========

Active Learning Module for Switching Regulators.

General Description
-------------------

.. figure:: adalm_sr1_overview.png
   :width: 600 px

   ADALM-SR1 Board Overview

The :adi:`ADALM-SR1` is a "disintegrated" DC-DC switcher designed to help
users understand fundamental switching regulator concepts. Rather than using a
fully integrated controller, the platform allows configuration of individual
building blocks, enabling users to investigate and manipulate signals that are
not easily accessible in integrated designs.

The board supports both buck and boost converter topologies with configurable
inductance, output capacitance, load resistance, and control modes.

Features
~~~~~~~~

- Buck and boost converter topologies
- Peak current mode and duty cycle control
- Open-loop and closed-loop operation
- 6-tap coupled inductor with selectable inductance (7.7 uH to 313.4 uH)
- Configurable output capacitance (4.7 uF to 521.7 uF)
- Selectable load resistors (12.5 ohm to 200 ohm)
- Input overvoltage/undervoltage protection (3 V to 15 V operating range)
- Output overvoltage protection (22 V threshold)
- Overcurrent limiting (2 A maximum)
- Thermal monitoring for inductor and load resistors (60 C threshold)
- Multiple measurement test points and signal injection points
- Designed for use with the :adi:`ADALM2000` measurement platform

Specifications
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Value
   * - Experiment Power Input
     - 3 V to 15 V (variable based on application)
   * - Input Protection Range
     - -40 V to +60 V (circuit protection)
   * - Housekeeping Supply
     - 5 V via micro-USB
   * - Maximum Current
     - 2 A
   * - Output Overvoltage Threshold
     - 22 V
   * - Thermal Protection Threshold
     - 60 C (inductor and load resistors)

.. figure:: adalm_sr1_topology_modes_loads.png
   :width: 600 px

   Topology, Modes, and Load Configuration

Inductance Selection
--------------------

The board uses a Wurth 749196141 6-winding coupled inductor (8.5 uH base,
344 mohm DC resistance per winding). The inductor taps are selected using
jumper **P3**.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Configuration
     - Inductance
   * - External
     - User-supplied
   * - 1 tap
     - 7.7 uH
   * - 2 taps
     - 31.5 uH
   * - 3 taps
     - 72.6 uH
   * - 4 taps
     - 131.5 uH
   * - 5 taps
     - 216.2 uH
   * - 6 taps
     - 313.4 uH

Output Capacitor Selection
--------------------------

The base output capacitance is 4.7 uF (always connected). Additional
capacitance can be added using jumpers:

- **P8** -- adds 47 uF
- **P11** -- adds 470 uF

Load Resistor Configuration
----------------------------

A 0.1 ohm sense resistor enables current measurement. Load resistors are
selected using jumpers:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Jumper
     - Load Resistance
   * - P18
     - 200 ohm
   * - P14
     - 200 ohm
   * - P13
     - 100 ohm
   * - P17
     - 50 ohm
   * - P16
     - 25 ohm
   * - P15
     - 12.5 ohm

.. warning::

   7 V maximum across the 25 ohm and 12.5 ohm resistors. Exceeding this
   threshold will activate the Over Power LED.

Operating Modes
---------------

Mode Selection (P32)
~~~~~~~~~~~~~~~~~~~~

- **Peak Current** -- Fixed-frequency clock starts the current ramp; the
  MOSFET opens when the peak current threshold is reached.
- **Duty Cycle** -- Direct MOSFET duty cycle control.

Topology Configuration
~~~~~~~~~~~~~~~~~~~~~~

The converter topology is configured using jumpers P25, P35, and P37:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Jumper
     - Buck
     - Boost
   * - P25
     - Low-side current sense
     - High-side current sense
   * - P35
     - High-side FET driver
     - Low-side FET driver
   * - P37
     - Bypasses D4
     - Does not bypass D4

Duty Cycle Control (P23)
~~~~~~~~~~~~~~~~~~~~~~~~

- **Closed-loop** -- Error amplifier controls duty cycle.
- **Manual** -- Potentiometer (DUTY CYCLE knob) controls switching.

Current Threshold Control (P22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Manual** -- Potentiometer (CURRENT THRESHOLD knob) sets peak current.
- **Closed-loop** -- Error amplifier controls the threshold.

Feedback Network (P20)
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Selection
     - Application
   * - 5V
     - Buck topology (input > 5 V)
   * - 12V
     - Boost topology (input < 12 V)
   * - ALT
     - User-defined feedback resistors (0603 footprints)

The reference voltage is 1.25 V (LT1970-1.25).

Measurement Test Points
-----------------------

.. figure:: adalm_sr1_aux_measure_inject.png
   :width: 600 px

   Test Points and Signal Injection Points

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Point
     - Function
   * - TP1
     - Overvoltage/overcurrent protected power
   * - P1
     - Switch node (buck)
   * - P4
     - Switch node (boost)
   * - P2
     - Current sense output (boost): 1.429 A/V, 0.1 ohm sense, gain = 7
   * - P12
     - Current sense output (buck): 1.429 A/V, 0.1 ohm sense, gain = 7
   * - P10, P9, TP5, TP7
     - Output voltage
   * - P5
     - Feedback measurement (AC-coupled)
   * - TP25, P39
     - Load current measurement
   * - P33
     - Master clock (3.3 V logic)
   * - P34
     - FET gate control (3.3 V logic)

Signal Injection Points
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Point
     - Function
   * - P28
     - Peak current modulation (1.429 A/V); P29 enables DC coupling
   * - P27
     - Duty cycle modulation (100%/V); P26 enables DC coupling
   * - P7
     - Feedback modulation for loop gain; P6 enables DC coupling

Auxiliary Circuitry
-------------------

.. figure:: adalm_sr1_aux_circuits.png
   :width: 600 px

   Auxiliary Circuits Block Diagram

The board includes the following auxiliary and protection circuitry:

- :adi:`LTC4368` -- Input protection and current limiting (2 A)
- :adi:`LT3472` -- Generates +/-15 V and -2 V from 5 V housekeeping supply
- :adi:`LT1995` -- Current sense amplifiers
- :adi:`LTC2912` -- Output overvoltage/undervoltage supervisor (22 V threshold)
- SMAJ24A -- 24 V TVS diode for output clamping
- Temperature sensors for inductor and load resistor monitoring (60 C threshold)

.. figure:: adalm_sr1_engineer_proofing.png
   :width: 600 px

   Engineer-Proofing Protection Circuitry

Laboratory Exercises
--------------------

The following lab activities are designed for use with the :adi:`ADALM2000`
measurement platform:

#. Boost and Buck converter elements and open-loop operation
#. Buck Converters: closed-loop operation
#. Boost Converters: closed-loop operation

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the :ez:`/`.
