AD5940_Amperometric
===================

This example will use **EVAL-ADICUP3029** and **EVAL_AD5940ELCZ** to carry put Amperometric measurements.

Overview
--------

This example project is designed to carry out amperometric measurements. Amperometric measurement is a basic electrochemical measurement where a bias voltage is applied to a sensor and the response current is monitored. Some sensors require no bias and are referred to zero bias sensors. The AD5940 uses its low power DAC, potentiostat amplifier, and low power TIA (LPTIA) to set a voltage on the sensor and measure the current. The low power DAC is a dual output DAC with a 12-bit option and a 6-bit option. The 12-bit output, known as VBIAS, sets the voltage on the counter and reference electrode. The 6-bit output, known as VZERO, sets the voltage on the working electrode, also known as the sense electrode (SE0). For zero bias sensors, the VBIAS and VZERO¬ outputs are set to the same value, which is optimally 1.1 V for the AD5940. For a nonzero bias sensor, the bias across the sensor is set by adjusting VBIAS and VZERO. In general the current measured on the sense electrode (SE0) is directly proportional to what is being measured.

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
-  Place jumper in position B on JP6 to connect 1k||3k between RE0 and SE0
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

To compile and run the example open the project in either Keil or IAR. The AD5940AMPStructInit() function is used to configure application parameters including, SensorBias and RtiaValue.

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

Gas Sensor
----------

The EVAL-AD5940ELCZ contains a footprint to connect an electrochemical gas sensor. To carry out amperometric measurements on a gas sensor connect the gas sensor to M1 as shown in image below. Move the jumpers on JP10 and JP11 to PIN1 and PIN2. Note the specified bias voltage for the sensor in the sensor datasheet. Modify the SensorBias variable in the AD5940_Amperometric firmware to correspond.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/img_20170612_144023_hdr.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/realterm_amperometric.png
   :width: 600px
