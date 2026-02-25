.. _eval-ltpa-comprb:

EVAL-LTPA-COMPRB
=================

LTpowerAnalyzer Compensation Probe.

.. figure:: eval-ltpa-comprb-top.png
   :align: center

   EVAL-LTPA-COMPRB Board Photo

Overview
--------

The EVAL-LTPA-COMPRB is an optional companion board to the
:ref:`EVAL-LTPA-KIT <eval-ltpa-kit>`, and is designed to support the
optimization of loop compensation in power supply designs. The board functions
as a programmable substitute for the series R-C network in a Type 2
compensator, and allows users to easily evaluate Bode plots and transient
responses with different combinations of resistances and capacitances without
soldering components directly to test circuits.

Features
--------

- 500 Ohm to 100 kOhm programmable resistance range
- 10 pF to 39 nF programmable capacitance range
- USB-C interface for data and power
- Small form-factor (2.82" x 1.25") enables portable applications

Hardware Interface
------------------

The compensation terminals on the EVAL-LTPA-COMPRB are described in the table
below.

.. figure:: eval-ltpa-comprb-hardware-interface.png
   :align: center

   EVAL-LTPA-COMPRB Hardware Interface

.. list-table::
   :header-rows: 1

   * - Terminal
     - Function
   * - R
     - Resistor Terminal. Connected to one end of the programmable resistor
       array.
   * - COM
     - Common Terminal. Connected to the junction between the resistor and the
       capacitor arrays.
   * - C
     - Capacitor Terminal. Connected to one end of the programmable capacitor
       array and its parasitic series resistance.

The equivalent circuit of the compensation probe is shown below.

.. figure:: eval-ltpa-comprb-equivalent-circuit.png
   :align: center

   EVAL-LTPA-COMPRB Equivalent Circuit

Basic Operation
---------------

Required Equipment
~~~~~~~~~~~~~~~~~~

- EVAL-LTPA-COMPRB (LTpowerAnalyzer Compensation Probe)
- :ref:`EVAL-LTPA-KIT <eval-ltpa-kit>` (LTpowerAnalyzer Kit)
- :adi:`ADALM2000` Advanced Active Learning Module
- Device Under Test (e.g., LT8642S demo board)
- DC Power Supply
- USB-C cable
- Host PC with LTpowerAnalyzer software

Step-by-Step Procedure
~~~~~~~~~~~~~~~~~~~~~~

**Step 1:** The EVAL-LTPA-COMPRB can function as either a programmable resistor
(R and COM terminals), capacitor (C and COM terminals), or series
resistor-capacitor network (R and C terminals), depending on how it is
connected to your DUT.

.. note::

   The compensation probe has a PCB capacitance of approximately 8 pF, which
   appears connected in parallel with the DUT.

**Step 2:** Identify where the compensation resistor and/or capacitor (whichever
is being tuned using the probe) are on your DUT, and verify that the
component(s) are not populated. Solder wires across the component locations.

.. important::

   The compensation probe should be placed as close as possible to the DUT, and
   any wires used must be kept short to minimize parasitic inductance and
   capacitance.

.. figure:: eval-ltpa-comprb-location-example.png
   :align: center

   Example Compensation Component Location on DUT

**Step 3:** Setup the LTpowerAnalyzer hardware, ADALM2000, and the DUT for Bode
Plot measurement per the :ref:`EVAL-LTPA-KIT <eval-ltpa-kit>` User Guide.
Connect a DC power supply to the DUT input.

**Step 4:** Connect a USB cable from the host PC to the USB-C port on the
EVAL-LTPA-COMPRB.

**Step 5:** Launch the LTpowerAnalyzer software. Upon launching, it will
automatically check for any compensation probes that are connected to the host
PC. If a probe is detected, a separate compensation probe control interface
window will be opened automatically.

**Step 6:** Click on the drop-down menus for Resistance and Capacitance and
select your desired setting for each. Upon selection, the probe's embedded
algorithm will automatically calculate and implement the best
resistor/capacitor combination that will result in the closest value to your
chosen setting.

.. figure:: eval-ltpa-comprb-control-panel.png
   :align: center

   LTpowerAnalyzer Compensation Probe Control Panel

**Step 7:** In the main LTpowerAnalyzer control interface, make a Bode Plot
measurement and observe the loop gain with the programmed compensation values.
Adjust the resistance and capacitance settings as needed to achieve the desired
stability requirements.

.. figure:: eval-ltpa-comprb-bode-plot-example.png
   :align: center

   Example Bode Plot Measurement with Compensation Probe

Example Setup
~~~~~~~~~~~~~

A hardware setup of the compensation probe is shown below for reference. This
example uses the LT8642S demo board included with the
:ref:`EVAL-LTPA-KIT <eval-ltpa-kit>` as the device under test.

.. note::

   These photos were taken using an older version of the EVAL-LTPA-COMPRB with
   a green solder mask.

.. figure:: eval-ltpa-comprb-example-application.png
   :align: center

   Example Application Setup

.. figure:: eval-ltpa-comprb-example-iso.png
   :align: center

   Example Setup - Isometric View

.. figure:: eval-ltpa-comprb-example-top.png
   :align: center

   Example Setup - Top View

Accuracy and Limitations
------------------------

If the Compensation Probe is connected properly, the resulting Bode plots
should be very similar to what would be captured had the compensation resistor
and capacitor been soldered directly to the DUT. The following Bode plot
comparisons demonstrate this at various resistance settings.

.. figure:: eval-ltpa-comprb-bode-plot-comparison-13k.png
   :align: center

   Bode Plot Comparison at 13 kOhm

.. figure:: eval-ltpa-comprb-bode-plot-comparison-26k.png
   :align: center

   Bode Plot Comparison at 26 kOhm

.. figure:: eval-ltpa-comprb-bode-plot-comparison-52k.png
   :align: center

   Bode Plot Comparison at 52 kOhm

.. figure:: eval-ltpa-comprb-bode-plot-comparison-100k.png
   :align: center

   Bode Plot Comparison at 100 kOhm

The hardware architecture of the Compensation Probe uses digitally-controlled
switches to implement a parallel combination of resistors (or capacitors), with
the total effective value used to emulate a standard E96 resistor (or E24
capacitor). A limitation of this architecture is that the compensation
resistance and capacitance becomes less accurate at higher and lower settings
respectively. This is inherent to how parallel connections work, as there are
simply fewer available resistors (or capacitors) that can be combined to produce
a valid result at those settings.

.. figure:: eval-ltpa-comprb-resistance-error.png
   :align: center

   Resistance Error Across Operating Range

.. figure:: eval-ltpa-comprb-capacitance-error.png
   :align: center

   Capacitance Error Across Operating Range

Additional Information
----------------------

- :adi:`EVAL-LTPA-COMPRB Product Page <EVAL-LTPA-COMPRB>`
- :adi:`EVAL-LTPA-KIT Product Page <EVAL-LTPA-KIT>`
- :ref:`EVAL-LTPA-KIT User Guide <eval-ltpa-kit>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
