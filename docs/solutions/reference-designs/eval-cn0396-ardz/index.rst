.. imported from: https://wiki.analog.com/resources/eval/user-guides/arduino-uno/reference_designs/demo_cn0396

.. _eval-cn0396-ardz:

EVAL-CN0396-ARDZ
=================

Portable Electrochemical Dual Toxic Gas Detector.

.. toctree::
   :hidden:

   hardware
   software

Overview
--------

:adi:`CN0396` is a single-supply, low-noise portable gas detector using a
4-electrode electrochemical sensor for simultaneous detection of two distinct
gases. The Alphasense COH-A2 sensor, which detects carbon monoxide (CO) and
hydrogen sulfide (H2S), is used in this example. Electrochemical sensors offer
several advantages for instruments that detect or measure the concentration of
many toxic gases. Most sensors are gas-specific and have usable resolutions
under one part per million (ppm) of gas concentration.

.. figure:: cn0396_board_wiki.png
   :align: center
   :width: 600px

   EVAL-CN0396-ARDZ evaluation board.

The circuit uses the :adi:`ADA4528-2` dual auto-zero amplifier, which has a
maximum offset voltage of 2.5 uV at room temperature and an industry-leading
5.6 uV/sqrt(Hz) of voltage noise density. The :adi:`AD5270` programmable
rheostat is used rather than a fixed transimpedance resistor, allowing for
rapid prototyping of different gas sensor systems without changing the bill of
materials.

The :adi:`ADR3412` precision, low-noise, micropower reference establishes the
1.2 V common-mode pseudo ground reference voltage with 0.1% accuracy and
8 ppm/degrees C drift. For applications where measuring fractions of ppm gas
concentration is important, using the ADA4528-2 and the ADR3412 makes the
circuit performance suitable for interfacing with a 16-bit ADC, such as the
:adi:`AD7790`.

An :adi:`ADT7310` 16-bit digital SPI temperature sensor is also included to
monitor environmental temperature, allowing for correction of temperature
effects on the sensor.

The EVAL-CN0396-ARDZ shield is designed to be compatible with the Arduino R3
shield form factor and is compatible with either 5 V or 3.3 V processor
boards.

.. figure:: cn0396_demo_1.png
   :align: center
   :width: 650px

   EVAL-CN0396-ARDZ connected to EVAL-ADICUP360.

Required Equipment
------------------

**Hardware:**

- EVAL-CN0396-ARDZ evaluation board
- :adi:`EVAL-ADICUP360` development board or Arduino R3 compatible processor
- 4-electrode electrochemical gas sensor (CO-H2S sensor included)
- Power supply: 6 V or 6 V wall wart (not needed if plugged into PC via USB)
- Environmental chamber and calibration gases (for calibration)
- Precision current sources (alternative to actual sensor and gases)

**Software:**

- PC with a USB port and Windows 7 (32-bit) or higher
- ADICUP360 Eclipse IDE
- CN0396 demo software
- Serial terminal software (PuTTY, Tera Term, or similar)

For detailed hardware setup and connector configuration, see :doc:`hardware`.
For software demo and configuration, see :doc:`software`.

Documents
---------

- :adi:`CN0396 Circuit Note <CN0396>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0396-ARDZ Design & Integration Files
   <https://www.analog.com/cn0396-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`ADA4528-2 Product Page <ADA4528-2>`
- :adi:`AD5270 Product Page <AD5270>`
- :adi:`AD7790 Product Page <AD7790>`
- :adi:`ADT7310 Product Page <ADT7310>`
- :adi:`ADR3412 Product Page <ADR3412>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
