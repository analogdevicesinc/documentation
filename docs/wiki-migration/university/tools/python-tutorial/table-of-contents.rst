ADALM1000 Python tutorial materials
===================================

Objective:
----------

This tutorial will introduce you to the libpysmu Python interface software layer to control the ADALM1000 active learning hardware module. Python is a general-purpose, object-oriented interpreted language you can use along with the ALM1000 hardware for countless standalone projects.

Required files:
---------------

These tutorial example programs are written in Python and requires that version 2.7.8 of Python be installed on the user's computer. The programs only import modules generally included with standard Python installation packages. The following files are required do these tutorials:

All OS:
~~~~~~~

:git-libsmu:`Libsmu with Python bindings. <releases/latest>`

Common Notes:
-------------

As in all the ALM activities we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 – PIO 3 on the ALM1000 board silkscreen.

Table of Contents:
------------------

-  :doc:`Controlling multiple LEDs </wiki-migration/university/tools/python-tutorial/tutorial1-toggle-led>`
-  :doc:`Reading push button switches </wiki-migration/university/tools/python-tutorial/tutorial2-read-buttons>`
-  :doc:`Using shift registers for more digital inputs/outputs </wiki-migration/university/tools/python-tutorial/tutorial-digital-shift-register>`
-  Using the CD4052 dual 4:1 analog Mux for more analog inputs
-  :doc:`Reading an analog voltage from a potentiometer </wiki-migration/university/tools/python-tutorial/tutorial3-potentiometer>`
-  :doc:`Program the AD8402 dual digital potentiometer </wiki-migration/university/tools/python-tutorial/tutorial-digital-potentiometer>`
-  :doc:`Use photocell to measure ambient light </wiki-migration/university/tools/python-tutorial/tutorial4-photocell>`
-  Read temperature values from an AD22100 sensor
-  Control a DC motor
-  :doc:`Control a Stepper Motor </wiki-migration/university/tools/python-tutorial/tutorial7-stepper-motors>`
-  Control a Servo Motor
-  Drive a piezoelectric transducer and use as a vibration sensor
-  Use an electret microphone as a sound detector
-  How to read acceleration data from the ADXL327

Materials:
~~~~~~~~~~

ADALM1000 hardware module

High Level Functions in libpysmu:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is are a few pre-defined python functions that interface to the C++ libsmu library. Contained in the pysmu.py file they provide the high level access functions to configure and control the ALM1000 hardware. The pysmu.py file must be imported or cut and pasted into your python program. The following lists the functions currently implemented:

| Smu()
| Must be run first
| Returns a list of the devices currently plugged into the computer
| Example:
| devx = Smu()

| devx.devices[int]
| takes a integer for the device, 0 for first device in list, 1 for second etc.
| returns index to that device

| Example:
| Both = devx.devices[0]

| devx.channels[string]
| takes one of the following strings as input 'A' , 'B' for first device, 'C' , 'D' for second device etc.
| returns index to that channel

| Examples:
| CHA = devx.channels['A']
| CHB = devx.channels['B']

| AllChan = Both.get_samples(n_samples):
| query device for a list of samples from all channels
| n_samples parameter is number of samples
| n_samples is of type int
| returns list of n samples from all the device's channels

AnalogInA = CHA.get_samples(20) get 20 readings and return them to list variable AnalogInA

| CHA.set_mode(mode) or CHB.set_mode(mode):
| mode can be one of the following strings:
| 'V' or 'v' sets channel to source voltage measure current ( SVMI )
| 'I' or 'I' sets channel to source current measure voltage ( SIMV )
| 'D' or 'd' set channel to high impedance mode, measure voltage

The following functions control the waveform of the analog output channels (could be CHA or CHB).

| CHA.constant(value)
| value is a floating point number from 0 to 5 representing the DC output voltage for that channel
| or value is a floating point number from -0.200 to + 0.200 representing the DC output current for that channel

CHA.sine(value1, value2, periodvalue, delayvalue)

CHA.triangle(value1, value2, periodvalue, delayvalue)

CHA.sawtooth(value1, value2, periodvalue, delayvalue)

CHA.square(value1, value2, periodvalue, delayvalue, dutycyclevalue)

CHA.stairstep(value1, value2, periodvalue, delayvalue)

| To better visualize how to specify a waveform look at figure 1 where:
| value1 is the first peak value of the waveform, could be the minimum or the maximum peak.
| value2 is the second peak value of the waveform, could be the minimum or the maximum peak.
| If for example value1 is less than value 2 the apparent phase of the wave is 180 degrees from a wave where value1 is greater than value2.
| dutycyclevalue is a fractional number from 0 to 1. dutycyclevalue only applies to the square waveform.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial0_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 How to build a waveform.


| To calculate the period from frequency ( in Hertz ) use the following formula:
| periodvalue = SAMPLErate/freqvalue where SAMPLErate is generally fixed at 100,000 SPS

| To calculate the delay from the phase ( in degrees ) use the following formula:
| delayvalue = periodvalue \* phasevalue / 360

Direct control over ADALM1000 functionality can be accomplished using the implemented control transfers, a synchronous and slow communication endpoint accessible regardless of the configuration of the device.

Note that the higher level functions libpysmu implements on top of LIBSMU make use of many of the control transfers to configure device state during normal operation. As such, using these low level control transfers while streaming data may not produce the expected results.

| The ALM1000 implements many control transfers, including the following:
| \* 0x17 - read a number of bytes from the ADM1177 hot-swap controller

-  0x50 - Set a GPIO pin low
-  0x51 - Set a GPIO pin high
-  0x91 - Get a GPIO input pin value
-  0x53 - Set device Mode
-  0x59 - Set potentiometer state

M1000 microcontroller pin mappings are described below.

======= ========== =================================== ======
IO Name Net Name   Net Description                     Pin ID
------- --------   ---------------                     ------
PA0     PIO0       user DIO 0-220Ω                     0
PA1     PIO1       user DIO 1-220Ω                     1
PA2     PIO2       user DIO 2-220Ω                     2
PA3     PIO3       user DIO 3-220Ω                     3
PA4     PIO0       user DIO 0-470Ω                     4
PA5     PIO1       user DIO 1-470Ω                     5
PA6     PIO2       user DIO 2-470Ω                     6
PA7     PIO3       user DIO 3-470Ω                     7
PB0     UA11-IN0   50Ω from ChA to 2v5                 32
PB1     UA11-IN1   50Ω from ChA to GND                 33
PB2     UA11-IN2   ChA close voltage sense loop        34
PB3     UA11-IN3   ChA connect output                  35
PB5     UB11-IN0   50Ω from ChB to 2v5                 37
PB6     UB11-IN1   50Ω from ChB to GND                 38
PB7     UB11-IN2   ChB close voltage sense loop        39
PB8     UB11-IN3   ChB connect output                  40
PB17    PWR_ENABLE turn on power for analog components 49
PB19    SWMODE-A   ChA switch SVMI - SIMV              51
PB20    SWMODE-B   ChB switch SVMI - SIMV              52
======= ========== =================================== ======

Examples:
~~~~~~~~~

| #
| import libpysmu
| import pysmu.py

| devx = Smu()
| DevID = devx.serials[0] # device ID for 1\ :sup:`st` M1000 in list

| # set PIO1 high
| devx.ctrl_transfer(DevID, 0x40, 0x51, 1, 0, 0, 0, 100)

| # set PIO1 low
| devx.ctrl_transfer(DevID, 0x40, 0x50, 1, 0, 0, 0, 100)

| # get state of PIO0
| print devx.ctrl_transfer(DevID, 0xc0, 0x91, 0, 0, 0, 1, 100)

| # get state of PIO1
| print devx.ctrl_transfer(DevID, 0xc0, 0x91, 1, 0, 0, 1, 100)

| # set CHA 2.5 V switch to open
| devx.ctrl_transfer(DevID, 0x40, 0x51, 32, 0, 0, 0, 100)

| # set CHA GND switch to open
| devx.ctrl_transfer(DevID, 0x40, 0x51, 33, 0, 0, 0, 100)

| # set CHB 2.5 V switch to open
| devx.ctrl_transfer(DevID, 0x40, 0x51, 37, 0, 0, 0, 100)

| # set CHB GND switch to open
| devx.ctrl_transfer(DevID, 0x40, 0x51, 38, 0, 0, 0, 100)

| # open CHA voltage sense loop
| devx.ctrl_transfer(DevID, 0x40, 0x51, 34, 0, 0, 0, 100)

| # open CHB voltage sense loop
| devx.ctrl_transfer(DevID, 0x40, 0x51, 39, 0, 0, 0, 100)

**For Further Reading:**

| :doc:`Active Learning Interface (for) Circuits (and) Electronics </wiki-migration/university/tools/m1k/alice/users-guide>` (Python program)
| :doc:`ALICE-SA Spectrum Analyzer </wiki-migration/university/tools/m1k/alice/sa-users-guide>` (Python program)
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`ADALM1000 Digital Outputs </wiki-migration/university/tools/m1k/digital-outputs>`

**Return to ALM** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`
