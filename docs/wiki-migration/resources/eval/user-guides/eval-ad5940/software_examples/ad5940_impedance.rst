AD5940_Impedance
================

This example will use **EVAL-ADICUP3029** and **EVAL_AD5940ELCZ** to carry out a 2-wire Impedance measurement.

Overview
--------

A standard 2-wire impedance measurement implements a ratio metric measurement. A signal is applied across the known resistor, (RCAL), and the response current is measured. The same signal is then applied across the unknown impedance and response current is measured. A DFT is performed on the response currents to determine the magnitude and phase values of each. The unknown impedance can then be calculated using the following equation:


|image1|

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

   -  AD5940_Amperometric Example Project (Git Lab)
   -  Serial Terminal Program, Such as Putty or RealTerm
   -  IDE such as IAR or Keil

Setting up the Hardware
-----------------------

-  Set switch S2 to USB Arduino function in order to view data over UART. The UART baud rate is **230400**
-  Set S5 to Wall/USB to power the board from the USB cable\

|image2|

-  Place the **EVAL-AD5940ELCZ** on top of the **EVAL-ADICUP3029**.
-  Ensure jumper on JP10 and JP11 is on PIN2 and PIN4 (to use the USB connected probe with EVAL-AD5940ELCZ, JP9,JP10 and JP11 should be configured to position C - pins 5 and 6)
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

   
   `AD5940 Source Code <https://github.com/analogdevicesinc/ad5940-examples>`_
   


Configuring the Software
------------------------

To compile and run the example open the project in either Keil or IAR. The AD5940ImpedanceStructInit() function is used to configure application parameters. These include setting the value of the RCAL, setting sine wave frequency, configuring the switch matrix and more.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/keil_impedance.png
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


|image3|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/impedance_equation.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/img_20170612_144023_hdr.jpg
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/realterm_impedance.png
   :width: 600px
