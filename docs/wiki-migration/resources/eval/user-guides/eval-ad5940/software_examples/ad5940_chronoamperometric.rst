AD5940_ChronoAmperometric
=========================

This example will use **EVAL-ADICUP3029** and **EVAL_AD5940ELCZ** to carry put Chrono-amperometric measurements.

Overview
--------

Chrono-amperometric, or pulse test, is a test in which the voltage across the counter electrode and sense electrode is pulsed, disturbing the normal bias for the electrochemical cell. The current response is measured on the sense electrode through the LPTIA. The measurement technique can have a number of applications. In the case of an electrochemical gas sensor this test checks that the passage of charge between electrodes through the internal electrolyte during oxidation and reduction is operating properly In normal operation, the AD5940 sets the voltage on the counter electrode via VBIAS and the voltage on the sense electrode is set via VZERO. These are typically set to 1.1 V for a zero bias sensor. Then a pulse is applied on VBIAS for a defined duration. The response current is measured using the low power TIA or the high speed TIA, depending on the speed of the response required. In this application the LPTIA is used.

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

   -  AD5940_Amperometric Example Project (Git Lab)
   -  Serial Terminal Program, Such as Putty or RealTerm
   -  IDE such as IAR or Keil

Setting up the Hardware
-----------------------

-  Set switch S2 to USB Arduino function in order to view data over UART. The UART baud rate is **230400**
-  Set S5 to Wall/USB to power the board from the USB cable\

|image1|

-  Place the **EVAL-AD5940ELCZ** on top of the **EVAL-ADICUP3029**.
-  Ensure jumper on JP10 and JP11 is on PIN2 and PIN4
-  Place jumper in position A on JP6 to connect 6.8K resistor in series with a 10uF capacitor between RE0 and SE0
-  Plug in the micro USB cable into the (P10) USB port on the EVAL-ADICUP3029, and the other end into the PC or laptop.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/ad5940elcz.jpg
   :align: center
   :width: 600px

Obtaining the Source Code
-------------------------

The source code and include files for the project can be found on Git

.. admonition:: Download
   :class: download

   
   `AD5940 Source Code <https://github.com/analogdevicesinc/ad5940-examples>`__
   


Configuring the Software
------------------------

To compile and run the example open the project in either Keil or IAR. The AD5940AMPStructInit() function is used to configure application parameters including, pulseAmplitude and pulseLength.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/keil_amperometric.png
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

The data on the terminal consists of the Frequency of the excitation signal, the magnitude of the impedance and the phase of the impedance in degrees as in below screenshot.


|image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/img_20170612_144023_hdr.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/realterm_amperometric.png
   :width: 600px
