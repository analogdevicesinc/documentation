ADALM1000 Strip Chart Recorder:
===============================

Objective:
----------

This document serves as a User's Guide for the Strip Chart Recorder software interface written for use with the ADALM1000 active learning kit hardware.

Background:
-----------

The ALM1000 contains two 16 bit 100KSPS analog to digital converters. These voltage inputs are often used to measure fast time varying waveforms as in the :doc:`ALICE oscilloscope interface </wiki-migration/university/tools/m1k/alice/users-guide>`. However, there are often times when accurate measurement of slowly changing signals over time is required. The following Python interface is provided for that purpose. It provides the means to more accurately calibrate the measurements than provided by the factory calibration contained on the ALM1000 board itself.

Required files:
---------------

The Strip Chart Tool program is written in Python and requires that version 2.7.8 or higher of Python be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run the Strip Chart Tool:

All OS:
~~~~~~~

`strip-chart-tool.py(w) <https://wiki.analog.com/_media/university/tools/strip-chart-tool.zip>`_

Windows:
~~~~~~~~

`libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`_ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`_ (needs to be in Python27\\DLLs directory)

Linux:
~~~~~~

`libpysmu.so <https://github.com/analogdevicesinc/libsmu>`_

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>` ( especially useful )
| :doc:`ADALM1000 Voltmeter Tool </wiki-migration/university/tools/m1k/alice/voltmeter-users-guide>` ( for calibration procedure )
| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`

First a few notes on nomenclature used in this document:

| CA-V refers to the Channel A voltage signal
| CB-V refers to the Channel B voltage signal

Screen Setup:
-------------

Once the program is running the main screen, as shown in figure 1, should appear. Be sure that the ALM1000 is plugged into the USB port before starting the program. When first started the chart will be blank. Figure 1 was taken after running the recorder for around 20 seconds measuring the voltage on two different flashing LEDs.

.. image:: https://wiki.analog.com/_media/university/tools/strip-chart-screen-0.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 1 Strip Chart screen


The majority of the window area is taken up by the graph or chart. Below that are various control buttons and entry slots. Starting on the left there are places to enter calibration factors for channel A and channel B gain and offset correction. There are buttons to Save and Load the calibration factors. The Strip Chart Tool uses the same calibration file as the Voltmeter Tool.

The Run button starts the strip recording and the Stop button will pause the recording. The Reset button clears the chart. With the Save Screen button you can save the chart area to an encapsulated postscript file. The average number of samples per second ( Sps ) is displayed.

The on the chart, channel A or B or both can be recorded. They can be drawn on a single grid or on 2 separate grids. There are 9 horizontal equally spaced grid lines drawn on the single grid. The bottom line is 0 V and the top line is +5V and the center blue line is +2.5V. On the dual grids there are 5 equally spaced horizontal lines for each channel again the bottom line is 0 V and the top line is +5V.

Customizing the program:
------------------------

By default 1000 sample points are displayed. The CANVASwidth variable can be used to change this number. The time between samples can be delayed by inserting a time delay in the main loop of the program at the end of the do_start(self): function. There may be times when the user wishes to customize the program to add additional functions such as controlling the digital I/O pins on the ALM1000 etc. This should be relatively easy to do in the Python program file. There are a number of :doc:`Python tutorial examples here </wiki-migration/university/tools/python-tutorial/table-of-contents>`.

Use Example:
------------

To demonstrate how to use the Strip Chart Tool consider the two resistor/capacitor networks shown in figure E1. Resistor R\ :sub:`1` and capacitor C\ :sub:`1` form a low pass RC integrator and capacitor C\ :sub:`2` and resistor R\ :sub:`2` form a high pass RC differentiator. We want to measure the voltages at the RC junctions as shown. The mid rail fixed 2.5 V supply is used as the reference point so the waveforms are centered in the 0 to 5 V range of the inputs. Single pole double throw (SPDT) switch S1 is used to switch the input side of the RC network between +5 V and ground.

.. image:: https://wiki.analog.com/_media/university/tools/strip-chart-fige1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E1, RC time constant test network


The screen shots shown in figures E2 and E3 were obtained by manually switching the SPDT switch S1 back and forth between +5 and ground every few seconds after the signals have more or less settled back to a constant value. Figure E2 was done with both channels recorded on the same grid while E3 was recorded with the channels on 2 separate grids.

.. image:: https://wiki.analog.com/_media/university/tools/strip-chart-screen-1.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure E2, Both signals on same grid


.. image:: https://wiki.analog.com/_media/university/tools/strip-chart-screen-2.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure E3, Each signal on separate grid


Two different resistor values and two different capacitor values are used but the resultant time constant is nearly the same in both cases.

**For Further Reading:**

**Return to** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
