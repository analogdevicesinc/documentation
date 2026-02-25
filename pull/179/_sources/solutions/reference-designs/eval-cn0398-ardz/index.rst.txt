.. _eval-cn0398-ardz:

EVAL-CN0398-ARDZ
================

Soil Moisture, pH, and Temperature Measurement System.

The :adi:`EVAL-CN0398-ARDZ <CN0398>` is a single supply, low power, high
precision complete solution for soil moisture and pH measurements, including
temperature compensation. The circuit is optimized for use with capacitive soil
moisture sensors that are insensitive to water salinity and do not corrode over
time. The circuit also measures soil pH and is suitable for a variety of
applications.

.. figure:: cn0398_board.png
   :align: center
   :width: 500

   EVAL-CN0398-ARDZ evaluation board

.. toctree::
   :hidden:

   hardware
   software

Table of Contents
-----------------

#. :doc:`Hardware Guide <hardware>`
#. :doc:`Software Demos <software>`

Overview
--------

The system is divided into three independent measurement front ends: pH, soil
moisture, and temperature. After signal conditioning, the three channels share
an :adi:`AD7124-8`, 24-bit sigma-delta ADC. The :adi:`AD7124-8` is a low power,
low noise, completely integrated analog front end for high precision measurement
applications. The device contains a low noise 24-bit analog-to-digital
converter and can be configured to have 8 differential inputs or 15
single-ended or pseudo-differential inputs. The on-chip gain stage ensures that
signals of small amplitude can be interfaced directly to the ADC.

The :adi:`AD7124-8` uses the :adi:`ADR3433`, a low cost, low power, high
precision CMOS voltage reference featuring +/-0.1% initial accuracy, low
operating current, and low output noise. The :adi:`ADR3433` provides both the
3.3 V reference and the AVDD supply to the :adi:`AD7124-8`.

The :adi:`ADP7118`-2.5 is a CMOS, low dropout (LDO) linear regulator which
provides the power supply for the moisture sensor. The input to the
:adi:`ADP7118`-2.5 is selectable via jumper P10 as either 5 V or 7 V to 12 V
from the Arduino-compatible platform board. The output of the :adi:`ADP7118`-2.5
is also selectable as 3.3 V or 5 V using the jumper on P8.

The circuit uses the :adi:`ADA4661-2`, a precision op amp, to buffer the high
impedance pH probe output and to drive the ADC. The :adi:`ADA4661-2` is a dual,
precision, rail-to-rail input/output amplifier optimized for low power, high
bandwidth, and wide operating supply voltage range.

Supported Devices
-----------------

- :adi:`AD7124-8` -- 24-bit Sigma-Delta ADC
- :adi:`ADR3433` -- High Precision CMOS Voltage Reference
- :adi:`ADP7118` -- CMOS Low Dropout Linear Regulator
- :adi:`ADA4661-2` -- Dual Precision Rail-to-Rail Op Amp

Documents
---------

- :adi:`CN0398 Circuit Note <CN0398>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0398-ARDZ Design & Integration Files
   <https://www.analog.com/cn0398-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
