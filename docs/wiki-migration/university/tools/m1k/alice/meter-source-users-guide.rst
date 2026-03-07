ADALM1000 DC Meter-Source User's Guide:
=======================================

Objective:
----------

This document serves as a User's Guide for the DC Meter ( V and I ) / Source ( V and I ) software interface written for use with the ADALM1000 active learning kit hardware.

Background:
-----------

The ALM1000 contains two 16 bit 100KSPS analog to digital converters and two 16 bit digital to analog converters. Along with a means to source both voltage and current with the DACs the system can simultaneously measure the current or voltage. These inputs and outputs are often used to measure time varying waveforms as in the :doc:`ALICE oscilloscope interface </wiki-migration/university/tools/m1k/alice/users-guide>`. However, there are often times when simple, accurate, DC measurements are required such as in a resistor network. The following Python interface is provided for that purpose. It provides the means to more accurately calibrate the measurements than provided by the factory calibration contained on the ALM1000 board itself.

Required files:
---------------

The DC Meter-Source Tool program is written in Python and requires that version 2.7.8 or higher of Python be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run the DC Meter-Source Tool:

All OS:
~~~~~~~

`dc-meter-source-tool.py(w) <https://wiki.analog.com/_media/university/tools/dc-meter-source-tool.zip>`_

Windows:
~~~~~~~~

`libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`_ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`_ (needs to be in Python27\\DLLs directory)

Linux:
~~~~~~

`libpysmu.so <https://github.com/analogdevicesinc/libsmu>`_

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Voltmeter User's Guide </wiki-migration/university/tools/m1k/alice/voltmeter-users-guide>`
| :doc:`ADALM1000 Ohmmeter User's Guide </wiki-migration/university/tools/m1k/alice/ohmmeter-users-guide>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>` ( especially useful )
| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`

First a few notes on nomenclature used in this document:

| CA-V refers to the Channel A voltage measurement
| CB-V refers to the Channel B voltage measurement
| CA-I refers to the Channel A current measurement
| CB-I refers to the Channel B current measurement

Screen Setup:
-------------

Once the program is running the main screen, as shown in figure 1, should appear. Be sure that the ALM1000 is plugged into the USB port before starting the program.

.. image:: https://wiki.analog.com/_media/university/tools/meter-source-screen-0.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 DC Meter-Source screen


At the top of the screen are two buttons to run and stop ( pause ) the program looping and taking measurements continuously. There are also buttons to save and load the calibration factors. There are four frames below that. The two on the left display the measured voltage and current for channel A and channel B. Below the voltage display the current flowing in that channel's source output is displayed if the source is turned on. When a channel's source is off ( channel is in Hi-Z mode measuring voltage only) the current display is blanked out with dashes.

Below the voltage and current displays at the bottom are entry slots for both voltage and current, gain and offset calibration factors for each channel. Using the calibration procedure from the Voltmeter tool is the best way to get the voltage calibration factors. Refer to the Voltmeter User's Guide for that procedure. Once you have the gain and offset numbers they can be entered here. Getting the current gain and offset factors requires a known resistance and is explained in the Ohmmeter User's Guide. To save these calibration values to a file for future use, press the Save button. To reload the saved calibration factors press the Load button. The values are saved to a file with a unique name for this particular ALM1000 board based on the last 14 characters of the board device ID serial number. This program uses the same naming scheme as the Ohmmeter Tool, for example something like: 203131543_O.cal.

The other two frames, on the right, are for controlling the DC voltage/current sources for each channel A and B. The CHA off and CHA on selector turns on the channel as a source ( same for CHB ). The CHA V and CHA I selector set the source mode to either source voltage or source current ( same for CHB ). The CA-V and CA-I entry slots are used to set the voltage and current source values ( same for CHB ). The channels can source voltage from 0 to 5V, entry is in volts. The channels can source ( positive number ) or sink ( negative number ) from -200 mA to 200 mA, entry is in milliamps.

Customizing the program
-----------------------

There may be times when the user wishes to customize the program to add additional functions such as controlling the digital I/O pins on the ALM1000 or combining the Voltmeter tool with the Ohmmeter tool. This should be relatively easy to do in the Python program file. There are a number of Python tutorial examples here.

Use Examples:
-------------

To demonstrate using the ALM1000 to measure current while sourcing voltage consider the resistor current divider circuit shown in figure E1. We would like to measure the currents flowing in resistors R\ :sub:`S` and R\ :sub:`2` while supplying 5V to R\ :sub:`S`. We will be using R\ :sub:`S` = R\ :sub:`1` = R\ :sub:`2` = 100Ω for this example.

.. image:: https://wiki.analog.com/_media/university/tools/meter-source-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E1, Using CHB as an ammeter


With CA source turned on set to source 5.0V and CB source turned on set to source 0.0V ( same as if R\ :sub:`2` were connected to GND ) we measure the currents in CA and CB as shown in figure E2. CA current is positive because it is sourcing current and CB is negative because it is sinking current.

.. image:: https://wiki.analog.com/_media/university/tools/meter-source-screen-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E2, Measuring Currents


**For Further Reading:**

**Return to** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
