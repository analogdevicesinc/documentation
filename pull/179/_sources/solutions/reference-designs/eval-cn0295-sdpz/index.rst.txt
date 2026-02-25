.. _eval-cn0295-sdpz:

EVAL-CN0295-SDPZ
=================

Flexible 4--20 mA Pressure Sensor Transmitter with Voltage or Current Drive.

Overview
--------

:adi:`CN0295` is a flexible current transmitter that converts the differential
voltage output from a pressure sensor to a 4 mA to 20 mA current output. The
circuit is optimized for a wide variety of bridge-based voltage or current
driven pressure sensors, utilizes only five active devices, and has a total
unadjusted error of less than 1%. The power supply voltage can range from 7 V
to 36 V depending on the component and sensor driver configuration. The input
of the circuit is protected for ESD and voltages beyond the supply rail, making
it ideal for industrial applications.

.. figure:: cn0295-hw-1024.jpg
   :width: 300px
   :align: center

   EVAL-CN0295-EB1Z evaluation board

.. figure:: cn0295_system_diagram.png
   :align: center

   CN0295 system diagram

Required Equipment
------------------

- :adi:`EVAL-CN0295-EB1Z` circuit evaluation board
- +7 V to +24 V power supply or equivalent
- Precision power supply
- Agilent 3458A or equivalent current meter
- Differential pressure sensor or equivalent dual-channel DC signal source

Hardware Setup
--------------

Power Supply
~~~~~~~~~~~~

Connect a +7 V to +24 V supply to **J2** for proper operation of the
evaluation board.

.. important::

   In order for the circuit to operate properly, the supply voltage must be
   greater than 7 V to provide sufficient headroom.

Input Signal
~~~~~~~~~~~~

Using an Actual Sensor
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0295_sensor_interface.png
   :width: 500px
   :align: center

   CN0295 sensor interface connections

.. figure:: cn0295_sensor_interface_table.png
   :width: 300px
   :align: center

   Sensor interface pin assignments

#. A differential output bridge-type sensor should be attached to the
   4-channel screw terminal block (**J3**) labeled SUPPLYSNS on the PCB.
#. A differential sensor gauge such as an NXP pressure sensor can be used for
   evaluation.

.. note::

   - **Vsense** is where the analog voltage output of the sensor is taken for
     measurement. Pin polarity should be taken into account.
   - **V/Iforce** is the sensor excitation, supplied either from a current or
     voltage source.

.. important::

   Pin polarity for Vsense and V/Iforce should be taken into consideration.

Using a Simulated Input Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following configuration can be used to simulate the sensor characteristic
for evaluation purposes.

.. figure:: cn0295_functional_block_diagram.png
   :width: 500px
   :align: center

   Functional block diagram for simulated sensor test setup

#. A dual power supply can be used to power the board from Vout1 and to
   generate a common-mode voltage of 2.5 V from Vout2 as shown in the block
   diagram.
#. A precision voltage source generates the 0 to 100 mV differential input
   voltage at the instrumentation amplifier input, simulating the sensor
   output.
#. A 3 kOhm resistor at R_bridge simulates the bridge-type sensor impedance.

.. figure:: cn0295_r6.png
   :width: 100px
   :align: right

   Resistor R6 location on the PCB

.. note::

   For bridge resistances lower than 5 kOhm, the drive voltage can be
   decreased to 5 V using a buffer configuration by removing resistor **R6**.

Sensor Drive
~~~~~~~~~~~~

The circuit can be switched between current and voltage drive configurations
by moving **S1** to the position labeled on the PCB.

.. figure:: cn0295_switch.png
   :width: 300px
   :align: center

   S1 switch for voltage/current drive selection

Voltage Drive Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In voltage drive mode with VDRIVE = 10 V, the supply voltage VLOOP (or system
supply) must be greater than 10.2 V.

Current Drive Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In current drive mode, the supply voltage VLOOP (or system supply) must be
greater than 11.2 V to maintain sufficient headroom.

.. note::

   Current drive configuration can be used for four-wire ohm circuit
   configurations. The main advantage of this configuration is that the
   voltage is measured directly across the load cell, neglecting the load
   effect of the lead wires for long-distance measurements.

.. important::

   For both voltage and current drive modes, the minimum loop supply voltage
   is dependent on the configuration of the drive circuit for the bridge.

Output Measurements
~~~~~~~~~~~~~~~~~~~

The output of the system can be measured in two ways: direct output current
measurement or voltage output through the series resistor.

.. figure:: cn0295_measurements.png
   :width: 500px
   :align: center

   CN0295 output measurement connections

Voltage Measurement
^^^^^^^^^^^^^^^^^^^

Voltage output measurement is done across a series 250 Ohm resistor through
the screw-type terminal block (**P1**).

.. important::

   The 2-pin male header (**J1**) must be populated before doing a voltage
   measurement across the terminal block (**P1**).

.. figure:: cn0295_r14.png
   :width: 100px
   :align: right

   R14, J1, and P1 locations on the PCB

Current Measurement
^^^^^^^^^^^^^^^^^^^

Current output measurement is done by connecting the positive terminal of the
current meter to one pin of the male header shunt terminal (**J1**) and the
negative terminal of the meter to the other pin of the same male header shunt
terminal.

.. note::

   The system has an onboard resistor load (**R14**) of 500 Ohm that can be
   desoldered and replaced with a desired resistor load value.

Documents
---------

- :adi:`CN0295 Circuit Note <CN0295>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0295-EB1Z Design & Integration Files
   <https://www.analog.com/cn0295-designsupport>`__

   - Schematics
   - Bill of Materials
   - Layout Gerbers
   - Assembly Drawing

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
