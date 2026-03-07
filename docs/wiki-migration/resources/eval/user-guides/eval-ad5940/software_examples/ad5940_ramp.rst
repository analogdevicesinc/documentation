AD5940_Ramp
===========

This example will use **EVAL-ADICUP3029** and **EVAL_AD5940ELCZ** to carry out a cyclic voltammetry measurement. Note, the corresponding application example in the SDK is the AD5940_Ramp project.

Overview
--------

Cyclic voltammetry is an electrochemical measurement in which the voltage applied to an electrochemical cell is incremented, then decremented, linearly in a triangular shape to a point. The response current on the working electrode is measured. To carry out this measurement on the AD5940, VZERO is set to output a voltage of 1.3 V. VBIAS can sweep from 0.3 V to 2.3 V, giving a ±1 V sweep. The response current is measured using the LPTIA.

For more details refer to the application note, AN-1563.

Measurement Requirements
------------------------

The following is a list of items required to carry out the measurement.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-AD5940ELCZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  Custom Cables (Optional)

-  Software

   -  AD5940_Ramp Example Project (Git Lab)
   -  Serial Terminal Program, Such as Putty or RealTerm
   -  IDE such as IAR or Keil

Setting up the Hardware
-----------------------

-  Set switch S2 to USB Arduino function in order to view data over UART. The UART baud rate is **230400**
-  Set S5 to Wall/USB to power the board from the USB cable\

|image1|

-  Place the **EVAL-AD5940ELCZ** on top of the **EVAL-ADICUP3029**.
-  Ensure jumper on JP10 and JP11 is on PIN2 and PIN4 to connect the dummy sensor to the AD5940 (to use the USB connected probe with EVAL-AD5940ELCZ, JP9,JP10 and JP11 should be configured to position C - pins 5 and 6)
-  Place jumper in position B on JP6 to connect the 10kΩ||10kΩ resistor divider between RE0 and SE0
-  Plug in the micro USB cable into the (P10) USB port on the EVAL-ADICUP3029, and the other end into the PC or laptop.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/ad5940elcz.jpg
   :align: center
   :width: 600px

Obtaining the Source Code
-------------------------

The source code and include files for the project can be found on Git

.. admonition:: Download
   :class: download

   `AD5940 Source Code <https://github.com/analogdevicesinc/ad5940-examples>`_

   


Configuring the Software
------------------------

To compile and run the example open the project in either Keil or IAR. The AD5940RampStructInit() function is used to configure the main application parameters that control the excitation signal and the data acquisition. The parameters and their description are explained in the table below:

+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Variable Name in Firmware | Description                                                                                                                                                                                                    |
+===========================+================================================================================================================================================================================================================+
| RampStartVolt             | This variable sets the voltage at which the excitation signal begins                                                                                                                                           |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RampPeakVolt              | This sets the peak voltage of the signal.                                                                                                                                                                      |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VzeroStart                | This sets the peak voltage of Vzero. Optimully set to 1.3V. The Actual start voltage on the sensor pin is VzeroStart + RampStartVolt                                                                           |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VzeroPeak                 | This sets the start voltage on Vzero. Optimully 1.3V. The Actual peak voltage on the sensor pin is VzeroPeak + RampPeakVolt                                                                                    |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| StepNumber                | This sets the number of steps in the signal. The size of each step is (RampPeakVolt-RampStartVolt)/StepNumber                                                                                                  |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RampDuration              | This variable sets the duration for the total signal. The unit is in milliseconds. The duration of each is the RampDuration/StepNumber                                                                         |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SampleDelay               | This variable sets the duration from when the step is applied to when the ADC measures the response current. Note, the SampleDelay must be shorter than the total step width. There are no checks in firmware. |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/keil_ramp.png
   :align: center
   :width: 600px

Outputting Data
---------------

The measurement results are sent to the PC via UART. To establish connection over UART, connect the Micro-USB cable to the PC and to the EVAL-ADICUP3029 board. A terminal program such as RealTerm or Putty is required to display the results

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 230400
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

The data on the terminal indicates the index number of the data point and the current measured in µA.


|image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/img_20170612_144023_hdr.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/realterm_ramp.png
   :width: 600px
