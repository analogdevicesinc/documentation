.. _arduino_uno eval:

ARDUINO UNO
===================================================================

.. image:: images/arduino2.png
   :align: center
   :width: 500

Overview
-------------------------------------------------------------------------------

The `Arduino Uno <https://www.arduino.cc/>`__ is an open-source microcontroller
board based on the ATmega328P. It exposes a standardized set of digital and
analog I/O headers that accept stackable expansion boards ("shields"), making it
a convenient, low-cost prototyping platform.

Analog Devices offers a broad range of Arduino-compatible shields (``ARDZ``
evaluation boards) that stack directly onto the Arduino Uno to evaluate
precision sensors and complete signal-chain solutions. The demos collected on
this page pair those shields with ready-to-run Arduino sketches, so you can
acquire real measurements with minimal setup.

Features:

- ATmega328P microcontroller running at 16 MHz
- 14 digital I/O pins (6 with PWM output) and 6 analog inputs
- SPI, I2C and UART peripherals exposed on the standard Arduino headers
- USB interface for programming and serial communication
- Programmable with the free, cross-platform Arduino IDE

Applications:

- Rapid prototyping and evaluation of ADI precision signal chains
- Sensor measurement and data acquisition
- Educational and hobbyist electronics projects

The following demos are available for the Arduino Uno:

.. toctree::
   :maxdepth: 1

   reference_designs/demo_adxl362
   reference_designs/demo_adxl372
   reference_designs/demo_cn0216
   reference_designs/demo_cn0357
   reference_designs/demo_cn0391
   reference_designs/demo_cn0395
   reference_designs/demo_cn0396
   reference_designs/demo_cn0397
   reference_designs/demo_cn0410
   reference_designs/demo_cn0411
   reference_designs/demo_cn0428
   reference_designs/demo_cn0429

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
