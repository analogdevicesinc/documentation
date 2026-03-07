ADALM1000 DC Voltmeter:
=======================

Objective:
----------

This document serves as a User's Guide for the DC Voltmeter software interface written for use with the ADALM1000 active learning kit hardware.

Background:
-----------

The ALM1000 contains two 16 bit 100KSPS analog to digital converters. These voltage inputs are often used to measure time varying waveforms as in the :doc:`ALICE oscilloscope interface </wiki-migration/university/tools/m1k/alice/users-guide>`. However, there are often times when simple, accurate, DC measurements are all that is required. The following Python interface is provided for that purpose. It provides the means to more accurately calibrate the measurements than provided by the factory calibration contained on the ALM1000 board itself.

Required files:
---------------

The Voltmeter Tool program is written in Python and requires that version 2.7.8 or higher of Python and libsmu version 0.89 be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run the Voltmeter:

All OS:
~~~~~~~

volt-meter-tool-1.1.pyw Run from source with libsum 0.89 only installed

Windows:
~~~~~~~~

Run from Windows executable included in ALICE desktop 1.1

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>` ( especially useful )

| First a few notes on nomenclature used in this document:
| CA-V refers to the Channel A voltage signal
| CB-V refers to the Channel B voltage signal

Screen Setup:
-------------

Once the program is running the main screen, as shown in figure 1, should appear. Be sure that the ALM1000 is plugged into the USB port before starting the program.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-1.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 1 Voltmeter screen


At the top of the screen the measured DC voltages for channel A and channel B are displayed. Below the channel B display the difference (CA-CB) between the two voltages is calculated and displayed. Below that are two buttons to run and stop ( pause ) the program looping and taking measurements continuously. At the bottom there are entry slots for gain and offset calibration factors for both channels.

Calibrating the Voltmeter
-------------------------

The program starts with the gain calibration factors set to 1.0 and the offset calibration factors set to 0.0. The first step in the calibration procedure is to connect both input channels to ground. Press the Run button. The screen should look something like figure 2 with some small (of the order of 1mV) non-zero values for CA Volts and CB Volts. You can pause (stop button) the program after a few seconds and it looks like you are getting a steady reading.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-2.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 2 Cal step 1, Both inputs connected to ground


The second calibration step is to enter the CA Volts reading into the CA offset entry window ( should have 0.0 in it ) and enter the CB Volts reading into the CB offset entry window. Press the Run button. The screen should look something like figure 3 with some small nearly zero values for CA Volts and CB Volts. You can pause (stop button) the program after a few seconds and it looks like you are getting a steady reading.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-3.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 3 Cal step 2, Offset values entered


The third calibration step is to measure a known voltage. The AD584 voltage reference from the ADALP2000 Analog Parts Kit is a good choice. Plug it into your solderless breadboard and connect as shown in figure 4. The AD584 is configured as a 2.5V reference by connecting pins 1 and 3 together. Connect both voltmeter input channels to the 2.5V output of the AD584. Note: the internal 2.5V and 5V sources of the ALM1000 are not accurate enough for this step ( unless you can accurately measure them with a good bench DMM ).

.. image:: https://wiki.analog.com/_media/university/tools/volt-meter-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 AD584 2.5 V reference connections


After double checking your connections press the Run button. The screen should look something like figure 5 with values for CA Volts and CB Volts close to 2.5 Volts.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-4.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 5, Cal step 3, Both inputs connected to AD584 output


We want to calculate values for the channel A and B gain such that the measurements displayed are equal to the actual 2.500 volts of the reference. The Gain correction factor is simply 2.500 V divided by the unadjusted measured value. In the case for channel A in figure 5 we get 2.500/2.4383 or 1.0253; typical Gain correction factors are a few percent. We do that for both channels and enter the results in the gain entry windows as shown in figure 6. Press the Run button. The screen should look something like figure 6 with values for CA Volts and CB Volts almost exactly equal to 2.5 Volts. If not try making small adjustments to the gain factors.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-5.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 6, Cal step 4, Gain values adjusted


To save these calibration values to a file for future use, press the Save button. To reload the saved calibration factors press the Load button. The values are saved to a file with a unique name for this particular ALM1000 board based on the last 14 characters of the board device ID serial number. For example something like: 23230313430333_V.cal.

Your ALM1000 is now ready to make accurate 0 to 5 V DC measurements.

After calibration the accuracy should be better than 1 mV. This gives 5000 count resolution from 0 to 5 Volts. If you have access to a bench DMM with 4 and 1/2 or 5 and 1/2 digits you can further check the calibration accuracy by measuring the actual AD584 output voltage.

Customizing the program
-----------------------

There may be times when the user wishes to customize the program to add additional functions such as controlling the digital I/O pins on the ALM1000. This should be relatively easy to do in the Python program file. There are a number of :doc:`Python tutorial examples here </wiki-migration/university/tools/python-tutorial/table-of-contents>`.

Use Example:
------------

To demonstrate how to use the Voltmeter Tool consider the resistor network, shown in figure E1, as a voltage divider and we wish to measure the voltages at the 4 nodes and the voltages across the 6 resistors. In the figure the nodes are numbered from N0 to N4 with N0 being the ground or common node that all the voltage measurements will be made with respect to. With the Voltmeter Tool we can measure two node voltages at a time and the voltage difference between those two nodes.

.. image:: https://wiki.analog.com/_media/university/tools/volt-meter-fige1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E1, Test resistor network, measuring nodes N1 and N2


We start with the network powered from the fixed +5 volt power supply at node N1 and the channel A input also connected to N1. The channel B input is connected to node N2. Figure E2 shows the results.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-e2.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure E2, Measuring nodes N1 and N2


We can now proceed around the network measuring pairs of nodes until we can fill out the table below. Figure E3 shows the voltmeter inputs connected to nodes N3 and N4. Any combination of two nodes can be measured and the voltage difference between the two nodes will be displayed.

.. image:: https://wiki.analog.com/_media/university/tools/volt-meter-fige3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E3, Test resistor network, measuring nodes N3 and N4


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/volt-meter-screen-e4.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure E4, Measuring nodes N3 and N4


==== =======
Node Voltage
==== =======
N0   0.00
N1   4.975
N2   4.143
N3   1.852
N4   0.819
==== =======

Table 1 Node voltages

From the measured node voltages ( and the difference voltages ) we can get the voltages across the 6 resistors.

======== ==============
Resistor Voltage
======== ==============
R1       N1 - N2 =0.832
R2       N2 - N0 =4.143
R3       N2 - N3 =2.291
R4       N3 - N4 =0.991
R5       N4 - N0 =1.033
R6       N2 - N4 =3.324
======== ==============

Table 2 Resistor voltages

From these voltages and the values of the resistors the currents through the resistors can be calculated.

**For Further Reading:**

**Return to** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
