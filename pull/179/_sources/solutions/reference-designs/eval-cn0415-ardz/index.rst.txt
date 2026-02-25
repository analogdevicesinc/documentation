.. _eval-cn0415-ardz:

EVAL-CN0415-ARDZ
=================

Robust PWM Solenoid Driver with Closed-Loop Current Control.

Overview
--------

:adi:`CN0415` is a robust pulse-width modulation (PWM) solenoid driver circuit
in an Arduino shield form factor. Target applications include motion control,
latches, clamps, brakes, clutches, proportional gas valves, proportional liquid
valves, and other industrial applications. The circuit provides accurate,
closed-loop current control in 2-state solenoid applications, allowing
low-voltage solenoids to be used over a wide range of supply voltages,
tolerating overvoltage and undervoltage transient conditions caused by
cold-cranking and load-dump conditions.

Initial pull-in current, pull-in time delay, and hold current are independently
adjustable in software, greatly reducing power consumption in applications
where the solenoid is continuously energized. In proportional valve
applications, PWM duty cycle and frequency can be directly controlled by an
external PID controller, and a dither current with programmable frequency and
amplitude can be enabled to reduce mechanical stiction.

.. figure:: images/cn0415_board.png
   :align: center
   :width: 500

   EVAL-CN0415-ARDZ Evaluation Board

Simplified Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cn0415_block_diagram.png
   :align: center
   :width: 600

   CN0415 Simplified Functional Block Diagram

.. toctree::

   hardware
   software

Documents
---------

- :adi:`CN0415 Circuit Note <CN0415>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0415-ARDZ Design & Integration Files
   <https://www.analog.com/cn0415-designsupport>`__

   - Schematics
   - Bill of Materials
   - Gerber Files
   - Assembly Files

Additional Information
----------------------

- :adi:`AD8210 Product Page <AD8210>`
- :adi:`LTC4367 Product Page <LTC4367>`
- :adi:`LTC4441 Product Page <LTC4441>`
- :adi:`LTC2312-14 Product Page <LTC2312-14>`
- :adi:`LT1671 Product Page <LT1671>`
- :adi:`LT3433 Product Page <LT3433>`
- :adi:`ADG3304 Product Page <ADG3304>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
