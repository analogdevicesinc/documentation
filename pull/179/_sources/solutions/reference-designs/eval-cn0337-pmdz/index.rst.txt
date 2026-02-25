.. _eval-cn0337-pmdz:

EVAL-CN0337-PMDZ
=================

Isolated RTD Temperature Measurement System (PMOD Interface).

The :adi:`EVAL-CN0337-PMDZ <CN0337>` is a completely isolated 12-bit, 300 kSPS
RTD temperature measurement system using only three active devices. It processes
the output of a Pt100 RTD and includes an innovative circuit for lead-wire
compensation using a standard 3-wire connection.

.. figure:: cn0337-hw-1024.jpg
   :align: center
   :width: 500

   EVAL-CN0337-PMDZ evaluation board

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

:adi:`CN0337` is a 12-bit, 300 kSPS, single-supply, fully isolated RTD
temperature measurement system with 3-wire compensation. The input stage is an
RTD signal conditioning circuit using a compensated 3-wire connection to the
RTD. The circuit translates the RTD input resistance range (100 ohm to
212.05 ohm for a 0 C to 300 C temperature range) into voltage levels compatible
with the input range of the ADC (0 V to 2.5 V).

The circuit incorporates the :adi:`AD8608` op amp, the :adi:`AD7091R` 12-bit
successive approximation (SAR) ADC, and the :adi:`ADuM5401` isolator to create
a standard temperature measurement system.

The design solution is optimized for high precision and low-cost measurement,
with a total unadjusted temperature error of less than 0.039% FSR/C. The total
error after room temperature calibration is less than +/-0.024% FSR/C, making
it ideal for a wide variety of industrial temperature measurements.

The circuit has a 12-pin PMOD connector on board, which can be used for
connection to a customer microprocessor or FPGA.

Supported Devices
-----------------

- :adi:`AD7091R` -- 12-bit SAR ADC
- :adi:`AD8608` -- Precision CMOS Op Amp
- :adi:`ADuM5401` -- Quad-Channel Digital Isolator

Documents
---------

- :adi:`CN0337 Circuit Note <CN0337>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0337-PMDZ Design & Integration Files
   <https://www.analog.com/cn0337-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
