Software Defined Instrumentation
===============================================================================

.. note::

   This is a work in progress.

Introduction
~~~~~~~~~~~~

Structure
~~~~~~~~~~~~

Theoretical content

- theoretical background for instrumentation devices
- ADALM2000 board overview, features, description
- ADALM2000 connectivity
- Scopy software overview and instruments description

Hands-on activity
~~~~~~~~
- breadboard Low-Pass filter implementation, two stages, 
- with Bode plot visualisation, 
- usage of power supplies and scope inputs
- SPI communication with ADALP2000 AD5626 part, DAC converter, 
- usage of Pattern Generator SPI interface and Scope channels for analog signals

What is Software Defined Instrumentation?​
A single device encapsulating more instruments used for measurements, signal generation, signal acquisition, etc., powered by a PC open-source software that allows the user to customize the measurements, since the software is residing more on the host PC/mobile device instead of on the instrument. ​

Bonus: it has a pocket size!

.. _fig-sdi_1:

.. figure:: sdi_1.png
   :align: center
   
   SDI then vs now
   
ADALM2000

The ADALM2000 (M2K) Advanced Active Learning Module is an affordable USB-powered data acquisition module, that can be used to introduce fundamentals of electrical engineering in a self or instructor lead setting.​

​With 12-bit ADCs and DACs running at 100 MSPS, brings the power of high-performance lab equipment to the palm of your hand, enabling electrical engineering students and hobbyists to explore signals and systems into the tens of MHz without the cost and bulk associated with traditional lab gear. ​

​When coupled with Analog Devices' Scopy™ graphical application software running on a computer, provides the user with high performance instrumentation.​

.. _fig-m2k:

.. figure:: m2k.png
   :align: left
.. _fig-scopy:

.. figure:: scopy.png
   :align: center
   
   M2k and Scopy software

Hands-on activity
~~~~~~~~

By the end of this lab, you will learn:

- How to use a desktop Oscilloscope and Signal generator channels by operating a Network Analyzer, as well as Digital Pattern generator
- How to interface an analog front end simple circuit with M2K channels
- How to generate and display signals with the lab tools Analog Devices provides

Pre-requisites

ADALM2000 drivers installation: <https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win/releases>
Install Scopy software from <https://github.com/analogdevicesinc/scopy/releases/tag/v1.4.1>

Demo 1 - Scope and Signal generator channels – Cascaded LP filters

Materials

- ADALM2000 Active Learning Module
- Solder-less breadboard, and jumper wire kit
- 2 x 1 KΩ resistors
- 2 x 0.1 uF capacitors (marked 104)

Hardware setup


Steps:
1. Open Network Analyzer
2. Set the sweep to logarithmic
3. Set the start frequency to 100Hz and stop to 20kHz
4. Set the magnitude axis between -50dB and 10dB
5. Set the phase axis between -180 and 90 degrees