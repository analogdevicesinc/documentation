.. _eval-cn0411-ardz:

EVAL-CN0411-ARDZ
================

Total Dissolved Solids (TDS) Measurement System.

The :adi:`EVAL-CN0411-ARDZ <CN0411>` is a total dissolved solids measurement
system using direct measurement of conductivity of the solution. The system can
measure low to high conductivity levels ranging from 1 uS to 0.1 S and can
accommodate 2-wire conductivity probes of different cell constants from 0.01
to 10. Temperature compensation is performed using either a 100 ohm or
1000 ohm 2-wire RTD.

.. figure:: cn0411_board.jpg
   :align: center
   :width: 500

   EVAL-CN0411-ARDZ evaluation board

.. toctree::
   :hidden:

   hardware
   software

Table of Contents
-----------------

#. :doc:`Hardware Guide <hardware>`
#. :doc:`Software Demo <software>`

Overview
--------

:adi:`CN0411` generates a bipolar square wave excitation across the conductivity
probe using the :adi:`AD5683R`, a 16-bit SPI voltage DAC, and the
:adi:`ADG884`, an ultra-low on-resistance CMOS Dual 2:1 SPDT switch. The
frequency of the excitation is controlled by a PWM signal from the
microcontroller which can be set to either 2.4 kHz or 94 Hz via the system
software.

The range of conductivity measurement can be adjusted using gain resistors
switched using the :adi:`ADG1608`, a 16:1 multiplexer. The conductivity cell
signal is measured by the :adi:`AD8220`, a low-input current JFET
instrumentation amplifier. A track-and-hold amplifier implemented using
:adi:`AD8628`, a zero-drift rail-to-rail single supply op amp, samples the
signal for the :adi:`AD7124-8`, a low noise low power 24-bit Sigma-Delta ADC.

With software calibration, the calibrated system accuracy is less than 2% for
all conductivity ranges from 1 uS to 0.01 S and less than 7% for conductivity
ranges greater than 0.01 S. This makes the system reliable for conductivity
measurement used to compute TDS.

This design uses a combination of components that allow for single supply
operation which minimize circuit complexity, making it suitable for low-power
and portable instrument applications. Applications include chemical water
analysis for field research, and monitoring water systems and natural bodies
of water.

Supported Devices
-----------------

- :adi:`AD7124-8` -- 24-bit Sigma-Delta ADC
- :adi:`AD5683R` -- 16-bit SPI Voltage DAC
- :adi:`AD8220` -- JFET Instrumentation Amplifier
- :adi:`AD8628` -- Zero-Drift Rail-to-Rail Op Amp
- :adi:`ADG884` -- CMOS Dual 2:1 SPDT Switch
- :adi:`ADG1608` -- 16:1 Multiplexer

Documents
---------

- :adi:`CN0411 Circuit Note <CN0411>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0411-ARDZ Design & Integration Files
   <https://www.analog.com/cn0411-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
