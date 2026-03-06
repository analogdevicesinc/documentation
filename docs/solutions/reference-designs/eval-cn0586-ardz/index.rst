.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0586

.. _eval-cn0586-ardz:

EVAL-CN0586-ARDZ
================

Precision Bipolar High Voltage Output.

Overview
--------

:adi:`CN0586` is a precision bipolar high voltage output drive solution, with
up to 200 V output span and digital interface isolation. The
:adi:`EVAL-CN0586-ARDZ` contains the full signal chain of the CN0586 circuit,
which operates from a +/-15 V external dual supply and integrates low drop-out
regulators, precision references, and high voltage power solutions.

The design is capable of producing up to 200 V span and 20 mA current drive at
the outputs. It features digital interface isolation, temperature or
software-controlled shutdown, and DAC output protection.

.. figure:: cn0586_board.jpg
   :width: 500 px
   :align: center

   EVAL-CN0586-ARDZ Evaluation Board

.. figure:: cn0586_block_diagram.svg
   :align: center

   EVAL-CN0586-ARDZ Simplified Circuit Block Diagram

Features
--------

- Programmable output span up to 200 V
- +/-100 V and +200 V power solution from 15 V input
- On-board precision voltage reference (:adi:`ADR441`)
- Arduino Uno form-factor compatibility
- Open-source firmware example
- Digital isolation and thermal shutdown safety features

Key Components
--------------

- :adi:`AD5754R` -- 4-channel voltage output DAC
- :adi:`ADHV4702-1` -- Low-noise high voltage amplifier (20 mA output current)
- :adi:`LT8365` -- High voltage power supply converter (dual configuration)
- :adi:`ADR441` -- 2.5 V precision voltage reference

Hardware Configuration
----------------------

Connectors
~~~~~~~~~~

+-----+----------+--------------------------------------------------+
| Ref | Connector| Function                                         |
+=====+==========+==================================================+
| A   | P1       | External +/-15 V supply input (100 mA)           |
+-----+----------+--------------------------------------------------+
| B   | P2       | Optional 3.3 V external supply for DAC           |
+-----+----------+--------------------------------------------------+
| C   | J2       | SMA terminal for HV output                       |
+-----+----------+--------------------------------------------------+
| D   | P3, P4   | 4 mm banana connectors for HV output             |
+-----+----------+--------------------------------------------------+
| E   | P6-P8    | 4 mm banana connectors for external HV supplies  |
+-----+----------+--------------------------------------------------+
| F   | P14-P17  | Headers for SDP-K1 Arduino connection            |
+-----+----------+--------------------------------------------------+
| G   | P11      | PMOD-compatible digital control                  |
+-----+----------+--------------------------------------------------+

LED Indicators
~~~~~~~~~~~~~~

+-----+-----------+---------------------------------------------+
| LED | Name      | Function                                    |
+=====+===========+=============================================+
| DS1 | UCON PWR  | SDP-K1 controller is powered                |
+-----+-----------+---------------------------------------------+
| DS2 | DAC PWR   | 15 V AVDD is available                      |
+-----+-----------+---------------------------------------------+
| DS3 | HV PWR    | On-board HV power solution is active        |
+-----+-----------+---------------------------------------------+
| DS4 | HV DRIVER | ADHV4702-1 is powered                       |
+-----+-----------+---------------------------------------------+

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~

- **JP1** -- Reference source (on-board ADR441 vs. external)
- **JP2** -- Digital supply source (3.3 V LDO vs. external)
- **JP3** -- DAC coding scheme (offset binary vs. two's complement)
- **JP4** -- Shutdown control (DAC channel D vs. temperature sensor)
- **JP5-JP6** -- HV supply routing (on-board LT8365 vs. external sources)
- **JP7-JP10** -- DAC channel output routing (HV amplifier vs. evaluation
  provisions)
- **JP11** -- Feedback loop configuration (short for closed-loop default,
  open for remote sensing)
- **JP12** -- External supply connectivity

HV Supply Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

The on-board HV power solution uses dual :adi:`LT8365` circuits configured
via switch S1:

- **Position A** -- +205 V / 0 V (GND)
- **Position B** (default) -- +110 V / -110 V

.. warning::

   Do not adjust jumpers or switches while the board is powered. The board can
   produce voltages up to 200 V+, which are hazardous. Set the HV supply
   configuration before powering the system.

Output Ranges
~~~~~~~~~~~~~

The software-selectable output voltage ranges are:

- 0 to +100 V
- -100 V to +100 V (default)
- -50 V to +50 V
- 0 to +200 V

System Setup
------------

.. figure:: cn0586_hardware_setup.jpg
   :width: 600 px
   :align: center

   EVAL-CN0586-ARDZ Hardware Setup

Equipment Required
~~~~~~~~~~~~~~~~~~

- EVAL-CN0586-ARDZ Circuit Evaluation Board
- :adi:`EVAL-SDP-CK1Z` (SDP-K1) Controller Board
- +/-15 V external dual power supply
- USB Type-C cable
- PC with ACE software installed

Quick Start
~~~~~~~~~~~

#. Set jumpers and switch S1 to default positions.
#. Connect the EVAL-CN0586-ARDZ to the SDP-K1.
#. Apply +/-15 V to P1 (attach the board cover for safety).
#. Connect USB Type-C from SDP-K1 to the PC.
#. Launch the ACE application.
#. Double-click the plugin to open the board view.
#. Select the HV output range, enable the output, and set the voltage value.

Software Setup
--------------

ACE Software
~~~~~~~~~~~~

When paired with the :adi:`EVAL-SDP-CK1Z` (SDP-K1), the ACE
(Analysis, Control, Evaluation) software can communicate with the
EVAL-CN0586-ARDZ over the Linux Industrial Input/Output (IIO) library.

The ACE plugin provides the following attributes:

+--------------+-------------------------------------------------------+
| Attribute    | Function                                              |
+==============+=======================================================+
| hvout_state  | Enable/disable HV driver output (default: disabled)   |
+--------------+-------------------------------------------------------+
| hvout_range  | Pre-defined ranges: 0 to 100 V, -100 to +100 V,       |
|              | -50 to +50 V, 0 to 200 V                              |
+--------------+-------------------------------------------------------+
| hvout_volts  | Set the output voltage value                          |
+--------------+-------------------------------------------------------+

PyADI-IIO
~~~~~~~~~~

:ref:`PyADI-IIO <pyadi-iio>` is a Python abstraction module for ADI hardware
with IIO drivers. Install the required dependencies:

.. code-block:: bash

   pip install -r /path/to/requirements.txt

Manual Firmware Loading
~~~~~~~~~~~~~~~~~~~~~~~

When not using ACE:

#. Connect only the SDP-K1 to the PC via USB.
#. Copy the firmware binary to the SDP-K1 mass storage device.
#. Confirm successful loading: LED1 (DS6) on SDP-K1 blinks red.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0586-ARDZ Design & Integration Files <https://www.analog.com/CN0586-DesignSupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

More Information and Useful Links
---------------------------------

- :adi:`CN0586 Circuit Note Page <CN0586>`
- :adi:`AD5754R Product Page <AD5754R>`
- :adi:`ADHV4702-1 Product Page <ADHV4702-1>`
- :adi:`LT8365 Product Page <LT8365>`
- :adi:`ADR441 Product Page <ADR441>`
- :adi:`ADuM4151 Product Page <ADuM4151>`
- :adi:`EVAL-SDP-CK1Z Product Page <EVAL-SDP-CK1Z>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`ez/reference-designs`.
