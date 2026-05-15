.. _eval-cn0511-rpiz:

EVAL-CN0511-RPIZ
================

DC to 5.5 GHz Signal Generator with +/-0.5 dB Calibrated Output Power

.. image:: images/cn0511_angle_view.png
   :align: center
   :width: 400

Overview
--------

Instruments that operate at RF range with features like low distortion, ultra
low phase noise, and portable signal generator are difficult to provide at
reasonable cost.

The system shown is an entirely self-contained DC to 5.5 GHz
signal generator. It only requires the Raspberry Pi (RPi) to operate. The RF
digital-to-analog converter (DAC), controlled using a 100 MHz Serial Peripheral
Interface (SPI) from the RPi, allows for single tone, phase coherent, and fast
frequency hopping across the spectrum. All the clocking requirements are
generated using an on-board crystal, so no external clock source is needed. All
the necessary power rails are also converted from the RPi into various supply
voltage requirements of the RF signal generator.

The system is designed to simplify the input requirements, optimize signal
paths, and reduce external cables and components. This circuit can act as a
standalone laboratory equipment or can be incorporated as a module into
automatic test equipment. Its small size makes it particularly attractive when
multiple channels are required. This Raspberry Pi compatible solution makes 
high speed signal generation more accessible and economical.

Features
--------

- DC to 5.5 GHz Single Tone Generator
- +/- 0.5 dB Wideband Amplitude Calibration from 0 dBm to -40 dBm
- 48-Bit Frequency Tuning Resolution (~43 µHz)
- Onboard VCXO for Quick Bring Up
- Compatible with Raspberry Pi 3B+, 4, Zero W, Zero 2W

Applications
------------

- Signal generator applications

.. admonition:: Getting Started

   The :adi:`CN0511` can be used for a wide range of applications, 
   and the following demos are meant to show examples of the flexibility of the board. 
   To get started with setup, configuration, and example use cases, 
   please proceed to the Quick Start Guide and follow the provided demo pages.

   - :doc:`Quick Start Guide <cn0511>`
   - :ref:`Software Requirements <cn0511-software-req>`

Recommendations
---------------
   
People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ez:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------

.. esd-warning::

Help and Support
----------------

Please go to :ez:`Help and Support <help-and-support>` page.

.. toctree::
   :hidden:

   cn0511
   software_update
