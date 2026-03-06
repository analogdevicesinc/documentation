.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/hardware/cn0338

.. _eval-cn0338-ardz:

EVAL-CN0338-ARDZ
=================

NDIR Thermopile-Based CO2 Gas Sensor.

.. toctree::
   :hidden:

   hardware
   software

Overview
--------

:adi:`CN0338` is a complete thermopile-based gas sensor using the nondispersive
infrared (NDIR) principle, optimized for CO2 sensing. The system can measure
the concentration of various gases by using thermopiles with different optical
filters. No chemical reaction occurs, producing no toxic byproducts.

.. figure:: cn0338_angle.jpg
   :width: 500px

   EVAL-CN0338-ARDZ shield board.

The circuit uses the :adi:`ADuCM360` precision analog microcontroller with dual
24-bit sigma-delta ADCs and ARM Cortex-M3 processor. The CN0338 circuit uses
the 24-bit sigma-delta ADCs of the ADuCM360 for simultaneous sampling of a
dual element thermopile at programmable rates of 3.5 Hz to 3.906 kHz.

The :adi:`AD8629` zero-drift precision op-amp (22 nV/sqrt(Hz) noise) amplifies
the thermopile outputs, the :adi:`ADA4528-1` zero-drift precision op-amp
provides additional signal conditioning, and the :adi:`ADP7105` LDO regulator
provides stable power supply.

The EVAL-CN0338-ARDZ uses the NDIR physical sensing technique and does not
chemically react with the target gas or give off any toxic byproducts when
measuring gas concentration. The system is stable after long periods of storage.
With two calibration methods (standard Beer-Lambert and modified Beer-Lambert
calibration), the measurement range extends from 0% to 100% CO2 concentration.
A temperature compensation algorithm in the firmware eliminates temperature
drift from the ideal gas law.

Required Equipment
------------------

- EVAL-CN0338-ARDZ evaluation board (Arduino shield)
- :adi:`EVAL-ADICUP360` development board
- 7 V to 12 V DC power supply (for lamp)
- Micro USB to USB cable
- PC or laptop with a USB port

For detailed hardware setup, see :doc:`hardware`.
For software demo and calibration procedures, see :doc:`software`.

Documents
---------

- :adi:`CN0338 Circuit Note <CN0338>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0338-ARDZ Design & Integration Files
   <https://www.analog.com/cn0338-designsupport>`__

   - Schematics
   - Layout Files
   - Gerber Files
   - Assembly Drawing

Additional Information
----------------------

- :adi:`ADuCM360 Product Page <ADUCM360>`
- :adi:`AD8629 Product Page <AD8629>`
- :adi:`ADA4528-1 Product Page <ADA4528-1>`
- :adi:`ADP7105 Product Page <ADP7105>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
