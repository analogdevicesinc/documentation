External LED Array Driver
=========================

:doc:`Click here to return to the Licensed Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/licensedalgorithms>`

.. important::

   This block is not included in the SigmaStudio installation. Please contact Analog Devices for evaluation and licensing information.


.. warning::

   This algorithm is not currently being distributed.


.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/licensedalgorithms/adi_led_driver_018.jpg
   :align: right

The ADAU1701 block drives an external LED level meter using three of its multipurpose pins. The external circuit requires only an LED driver IC and the proper number of LEDs for the level meter.

ADI's A6276EA serial-input LED driver can drive two 8-LED meters. The driver IC requires three control signals (clock, latch, data) to drive the LED meters.

These three signals are obtained from the External LED Array Driver block, which takes the stereo signal as input and outputs the clock, latch, and data signals in its first, second, and third blue output pins. Clicking Table brings up the LEDTable window (right), where the linear values that turn on each LED can be set. (To the right of these linear values are their decibel equivalents.)

For more details, see the Example.

Note: ADI’s LED driver add-on board can be easily connected to the breadboard section of the ADAU1701 GPIO interface board; click here for details.
