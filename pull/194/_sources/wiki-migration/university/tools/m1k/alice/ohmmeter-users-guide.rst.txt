ADALM1000 DC Ohmmeter:
======================

.. important::

   The first sections of this document are now obsolete and are supersede by the main ALICE desktop User's Guide. Skip ahead to the Alternate Method Section of this document for relevant information.


Objective:
----------

This document serves as a User's Guide for the DC Ohmmeter software interface written for use with the ADALM1000 active learning kit hardware.

Background:
-----------

The ALM1000 contains two 16 bit 100KSPS analog to digital converters and two 16 bit digital to analog converters. Along with a means to source a voltage with the DACs the system can simultaneously measure the current. These inputs and outputs are often used to measure time varying waveforms as in the :doc:`ALICE oscilloscope interface </wiki-migration/university/tools/m1k/alice/users-guide>`. However, there are often times when simple, accurate, DC measurements such as resistance are required. The following Python interface is provided for that purpose. It provides the means to more accurately calibrate the measurements than provided by the factory calibration contained on the ALM1000 board itself.

Required files:
---------------

The Ohmmeter Tool program is written in Python and requires that version 2.7.8 or higher of Python be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run the Ohmmeter Tool:

All OS:
~~~~~~~

`ohm-meter-tool.py(w) <https://wiki.analog.com/_media/university/tools/ohm-meter-tool.zip>`_

Windows:
~~~~~~~~

`libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`_ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`_ (needs to be in Python27\\DLLs directory))

Linux:
~~~~~~

`libpysmu.so <https://github.com/analogdevicesinc/libsmu>`_

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Voltmeter User's Guide </wiki-migration/university/tools/m1k/alice/voltmeter-users-guide>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>` ( especially useful )
| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`

| First a few notes on nomenclature used in this document:
| CA-V refers to the Channel A voltage signal
| CB-V refers to the Channel B voltage signal

Screen Setup:
~~~~~~~~~~~~~

Once the program is running the main screen, as shown in figure 1, should appear. Be sure that the ALM1000 is plugged into the USB port before starting the program.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-0.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Ohmmeter screen (measuring a 1.82K and 100 Ohm resistor)


At the top of the screen are two buttons to run and stop ( pause ) the program looping and taking measurements continuously. There are also buttons to save and load the calibration factors. The two frames below that display the measured resistance in KiloOhms for channel A and channel B. Below the resistance display the current flowing in the test resistance is displayed. Next there is a place to enter the desired test voltage that is applied across the test resistance. More on that later. Below that at the bottom there are entry slots for both voltage and current, gain and offset calibration factors for each channel. Using the Voltmeter tool is the best way to get the voltage calibration factors. Refer to the Voltmeter User's Guide for that procedure. Once you have the gain and offset numbers they can be entered here. Getting the current gain and offset factors is explained in the next section.

Calibrating the Ohmmeter
~~~~~~~~~~~~~~~~~~~~~~~~

The program starts with all the gain calibration factors set to 1.0 and all the offset calibration factors set to 0.0. The first step in the calibration procedure is to set the desired test voltage for each channel. For resistances larger than 100 Ohms setting the test voltage to its maximum of 5.0 Volts gives the best results. For resistances less than 100 Ohms a lower test voltage is needed to keep the current supplied to the resistor under test to less than 100 mA.

With the CA and CB pins open circuit ( i.e. the resistance is infinity ) press the Run button. The screen should look something like figure 2 with some small non-zero values for CA current and CB current. Note that the voltage calibration factors (VA, VB) have already been filled in from using the Voltmeter Tool. You can pause (stop button) the program after a few seconds and it looks like you are getting a steady reading.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Cal step 1, Both inputs open circuit


The second calibration step is to enter the CA current reading into the CA current offset entry window ( IA should have had 0.0 in it ) and enter the CB current reading into the CB current offset entry window. Press the Run button. The screen should look something like figure 3 with some small nearly zero values for CA current and CB current. The CA and CB resistance should be some large value in the 100's KOhms range ( might even be a large negative value ). You can pause (stop button) the program after a few seconds and it looks like you are getting a steady current reading.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Cal step 2, Current Offset values entered, inputs open circuit


The third calibration step is to measure a known resistance. The resistors provided in the ADALP2000 Analog Parts Kit are only good to probably 5%. The value of these will not be accurate enough unless you can accurately measure them with a good bench DMM. For demonstration purposes here a 0.005% 2 KOhm resistor and a 0.1% ( or better ) 1 KOhm test resistor are used.

Connect the test resistors between ground and the Channel A input ( 2K ) and ground and the Channel B input ( 1K ). Plugging the resistors into your solderless breadboard and connecting to the ALM1000 connector with jumper wires is a good way to do this. After double checking your connections press the Run button. The screen should look something like figure 4 with values for CA KOhms and CB KOhms close to your test resistor values ( 2K and 1K in this example ).

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Cal step 3, Both inputs connected to test resistors


We want to calculate values for the channel A and B current gain such that the measurements displayed are equal to the actual test resistor values. The Gain correction factor is simply the un adjusted measured value divided by the actual resistor value (measured resistance from the DMM if you don't have precession resistors to use). In the case for channel A in figure 4 we get 2.038/2.000 or 1.019. We do that for both channels and enter the results in the gain entry windows as shown in figure 5. Press the Run button. The screen should look something like figure 5 with values for CA KOhms and CB KOhms almost exactly equal to 2K and 1K. To get the best results you need to wait for the ALM1000 to warm up for some time and small adjustments to the gain and offset factors may be required. Also the offset current will change based on the test voltage so readjusting the current offset factors will be needed as the test voltage is changed.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Cal step 4, Gain values adjusted


To save these calibration values to a file for future use, press the Save button. To reload the saved calibration factors press the Load button. The values are saved to a file with a unique name for this particular ALM1000 board based on the last 14 characters of the board device ID serial number. For example something like: 23230313430333_O.cal.

Your ALM1000 is now ready to make accurate resistance measurements in the range from 10 Ohms to 50 KOhms.

After calibration the accuracy should be better than a few ohms for resistors larger than 1K and around 1 Ohm for resistors less than 1K. If you have access to a bench DMM with 4 and 1/2 or 5 and 1/2 digits you can further check the calibration accuracy by measuring the actual values of the resistors used for calibration.

Alternate Method:
-----------------

The above approach is based on Ohm's Law where both the voltage across and the current through the test resistance is known or measured. The accuracy of the measured resistance is based on the measurement accuracy of the voltage and current and both must be calibrated. This second method is based on the voltage divider configuration shown in figure 6.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-fig6.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 6, Voltage Divider Method


If we assume that voltage source V\ :sub:`S` is known, resistance of R\ :sub:`1` is known and we can measure voltage V\ :sub:`2`, the voltage across R\ :sub:`2`, we can use the voltage divider formula to calculate the resistance of R\ :sub:`2`.

:math:`V_2 = V_S \times (R_2/( R_1 + R_2 ))`

Which can be rearranged to:

:math:`R_2 = R_1 \times (V_2 / (V_S - V_2))`

There is a certain advantage to using this voltage divider method over the Ohm's Law method in that a much wider range of resistances can be measured. The Ohm's Law method is limited in one extreme by the maximum current that the ALM1000 can safely source ( about 100 mA or 10 Ohms ) and in the other by the minimum current that the ALM1000 can accurately measure ( about 200 uA or 25 KOhms). Using the voltage divider method, because we can choose a range of R\ :sub:`1` values, we are only limited by the voltage measurement resolution of the ALM1000 ( about 100 uV ). R\ :sub:`1` can range from as low as 10 Ohms to as high as 10 KOhms in practice which extends the range from 1 Ohm or less to nearly a MOhm.

For the highest values of R\ :sub:`2` the internal 1 MOhm resistance of Channel B comes into effect and the software removes this parallel resistance when calculating the value for R\ :sub:`2`.

Slight Variation:
~~~~~~~~~~~~~~~~~

Built into the ALM1000 is a switch that can connect an on-board 50 Ohm resistor from the channel B input / output pin to ground. We can use this "known" resistor as R\ :sub:`2` in figure 6 and calculate for R\ :sub:`1` instead.

:math:`\displaystyle R_1 = R_2 \times (\frac{V_S - V_2}{V_2})`

The series resistance of the switch, which is approximately 1 Ohm, must be included in the value of R\ :sub:`2`. The actual value for R\ :sub:`2` is more like 51 Ohms. Of course the true value for R\ :sub:`2` can be found by calibrating its value based on measuring a known precision resistor standard.

Both ways can be used in this version of the Ohm meter tool:

`ohm-meter-vdiv.py(w) <https://wiki.analog.com/_media/university/tools/ohm-meter-tool.zip>`_

.. _calibrating-the-ohmmeter-1:

Calibrating the Ohmmeter
~~~~~~~~~~~~~~~~~~~~~~~~

The program starts with all the gain calibration factors set to 1.0 and all the offset calibration factors set to 0.0. The first step in the calibration procedure is again to set the calibration setting for Channel A and B voltage gain and offset. The program uses the same calibration file naming scheme so the Save and Load buttons are used as in the earlier program. The current measurements are not used in the calculation and the current calibration settings are included for completeness. The CH-A current is displayed for informational purposes only.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-7.png
   :align: center
   :width: 240px

.. container:: centeralign

   Figure 7 Voltage Divider Ohm meter screen.


Figure 7 shows the voltage divider Ohm meter screen with the voltage calibration settings filled in. The Test voltage is set to 5 V and the **external** R\ :sub:`1` value is set to 1000 Ohms. The 2.000 KOhm resistance standard is connected as R\ :sub:`2`. As we see the measured result is spot on. If the actual value of R\ :sub:`1` were not 1000 and the reading does not match the resistance standard's value, a slightly different value for R\ :sub:`1` should be entered until the required measurement value is displayed.

Figure 8 shows the voltage divider Ohm meter screen using the internal "50" Ohm resistor switched in from the I/O pin of CH B and ground. The Test voltage is set to 5 V and the **internal** R\ :sub:`2` value is set to 51.04 Ohms. The 2.000 KOhm resistance standard is connected as R\ :sub:`1`. As we see the measured result is spot on. As indicated the value entered for R\ :sub:`2` is larger than 50 Ohms when the switch resistance is included.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-screen-8.png
   :align: center
   :width: 240px

.. container:: centeralign

   Figure 8, Using the internal 50 Ohm resistor


Customizing the program
-----------------------

There may be times when the user wishes to customize the program to add additional functions such as controlling the digital I/O pins on the ALM1000 or combining the Voltmeter tool with the Ohmmeter tool. This should be relatively easy to do in the Python program file. There are a number of :doc:`Python tutorial examples here </wiki-migration/university/tools/python-tutorial/table-of-contents>`.

**For Further Reading:**

**Return to** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
