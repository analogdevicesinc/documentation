.. imported from: https://wiki.analog.com/resources/eval/user-guides/arduino-uno/reference_designs/demo_cn0410

.. _eval-cn0410-ardz:

EVAL-CN0410-ARDZ
=================

3-Channel LED Current Source Driver for Smart Agriculture.

Overview
--------

:adi:`CN0410` is an Arduino-compatible shield optimized for smart agriculture
applications, providing precise current control for up to three independent LED
channels. The :adi:`EVAL-CN0410-ARDZ <CN0410>` is used together with the
CFTL-LED-BAR, which contains LEDs with specific wavelengths that plants utilize
for photosynthesis.

The circuit is a complete 3-channel, single-supply, 16-bit unbuffered voltage
output DAC system that maintains +/-2 LSB integral and differential nonlinearity
by utilizing a CMOS DAC. The voltage-to-current conversion stage controls the
amount of current passing through each LED using a MOSFET in its configuration.
The circuit also includes an isoSPI repeater that allows multiple boards to be
controlled with a single master over distances up to 100 meters.

.. figure:: images/cn0410_board.jpg
   :align: center
   :width: 500

   EVAL-CN0410-ARDZ Evaluation Board

Key Components
~~~~~~~~~~~~~~

- :adi:`AD5686` -- 16-bit, quad-channel voltage output DAC
- :adi:`LT6820` -- isoSPI repeater for long-distance multi-drop communication

.. toctree::

   hardware
   software

Documents
---------

- :adi:`CN0410 Circuit Note <CN0410>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0410-ARDZ Design & Integration Files
   <https://www.analog.com/cn0410-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`AD5686 Product Page <AD5686>`
- :adi:`LT6820 Product Page <LT6820>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
