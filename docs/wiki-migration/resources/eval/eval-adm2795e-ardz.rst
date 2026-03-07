====== EVAL-ADM2795EARDZ Arduino Shield======

Use the EVAL-ADM2795EARDZ Arduino Shield with the widely available Arduino UNO to easily evaluate the ADM2795E 5 kV rms signal isolated RS-485 transceiver with Level 4 IEC EMC and 24 V supply fault protection.

The ADM2795E is an RS-485 transceiver that integrates IEC 61000-4-5 Level 4 surge protection, allowing up to ±4 kV protection on the RS-485 bus pins (A and B). The device has IEC 61000-4-4 Level 4 EFT protection up to ±2 kV and IEC 61000-4-2 Level 4 ESD protection on the bus pins, allowing this device to withstand up to ±15 kV on the transceiver interface pins without latching up.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardzangle.jpg
   :align: left
   :width: 400px

This Wiki guide provides hardware references and Arduino software for full integration of the EVAL-ADM2795EARDZ in a demonstration platform.

--------------

Connectors and Jumper Configurations
====================================

The EVAL-ADM2795EARDZ features an RS-485 bus cable connector, an Arduino connector block, and some jumper blocks. The jumper blocks can be used to connect to external devices such as ultrasonic sensors (e.g. Ultrasonic HC-SR04 Distance Measuring Transducer), or joysticks (Arduino Compatible Analogue Joystick Controller). For the demonstration code and setup described in this Wiki guide only the Arduino connector block and RS-485 connector are used. The Joystick and Ultrasonic sensor jumper blocks are not supported with example software in this Wiki guide, however their general function is outlined below.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz board picture_1.jpg
   :align: center
   :width: 600px

Joystick
--------

When the joystick mode is selected and the LED D4 is connected it will be turned off.

+-------------------------------------+------------------------------------------------------------------------------+
| Configuration                       | Function                                                                     |
+=====================================+==============================================================================+
| |eval-adm2795e-ardz joystick 1.png| | This connects 5V to pin 18 (D3) of the Arduino Uno and powers pins D0 to D7. |
+-------------------------------------+------------------------------------------------------------------------------+

+---+---+
| |eval-adm2795e-ardz joystick 2.png| | This connects pins 9 (A0) and 11 (A2) of the Arduino Uno |
+---+---+

+---+---+
| |eval-adm2795e-ardz joystick 3.png| | This connects pin 10 (A1) to GND of the Arduino Uno |
+---+---+

Ultrasound
----------

An Ultrasonic HC-SR04 sensor can be connected to the EVAL-ADM2795EARDZ, and powered from an Arduino UNO.

+---------------------------------------+--------------------------------------------------------------------------------------+
| Configuration                         | Function                                                                             |
+=======================================+======================================================================================+
| |eval-adm2795e-ardz ultrasound 1.png| | This connects 5V to the pin 21 (D6) of the Arduino Uno and powers the D0 to D7 pins. |
+---------------------------------------+--------------------------------------------------------------------------------------+

+---------------------------------------+--------------------------------------------------------------------------------------------------------------+
| |eval-adm2795e-ardz ultrasound 2.png| | This connects pins 19 (D4) and 20 (D5) of the Arduino Uno.                                                   |
|                                       | D4 is a LED that is used to switch between the ultrasonic and joystick functions.                            |
|                                       | If the LED is on then the ultrasonic mode is enabled and if the LED is off then the joystick mode is enabled |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------+

+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| |eval-adm2795e-ardz ultrasound 3.png| | This connects pin 22 (D7) to GND of the Arduino Uno.                                                      |
|                                       | D7 is a button that toggles between turning on and off the LED at D4 that is used to toggle the two modes |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+

Terminal Block
--------------

+---------------+-------------------------------------------------------------------------------------+
| Configuration | Function                                                                            |
+===============+=====================================================================================+
| |image2|      | This connects the ADM2795E RS-485 transceiver to the RS-485 differential bus cable. |
|               | The 3-way terminal block provides A, B, and Ground wire connection points.          |
+---------------+-------------------------------------------------------------------------------------+

| 
| -----

Isolated Motor Control System using Arduino Form Factor Rapid Development Platforms
===================================================================================

| \\\\In this set-up the stimulus from an ultrasonic sensor at one end of the RS-485 bus controls a motor and gearing or fan assembly at the far end of the bus. The EVAL-ADICUP-360 Arduino form factor compatible ARM Cortex-M3 Development Platform accepts inputs from a standard ultrasonic sensor. The EVAL-ADICUP-360 outputs are used to control the EVAL-ADM2795EARDZ logic signals. The first EVAL-ADM2795EARDZ then transmits to a second EVAL-ADM2795EARDZ node over 10 meters of RS-485 Category 5e cable. On the far end of the bus, the second receiving EVAL-ADM2795EARDZ, EVAL-ADICUP-360, and Arduino Motor control shield and provide output to a standard industrial motor. Sample Arduino code for the transmitting and receiving RS-485 nodes is located at the end of this Wiki guide.
| |image3|

.. image:: https://wiki.analog.com/_media/eval-adm2795e-ardz_demo.png
   :width: 800px

--------------

Schematic, Bill of Materials, Gerber Files and Layout Files
===========================================================

.. admonition:: Download
   :class: download

   
   ::
   
      *[[https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz_b_sch.pdf|Schematic]]
      *[[https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz_b.pdf|PCB Layout and Mounting Diagram]]
      *[[https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz_b.xls|Bill of Materials]]
   


--------------

Change Log
==========

::

   *Initial Revision
   *Added an example of how to use the ADM2795E with some code, pictures and a brief explanation

--------------

Resources
=========

\*Standard Evaluation Board User Guide: http://www.analog.com/media/en/technical-documentation/user-guides/EVAL-ADM2795EEBZ-UG-997.pdf

\*Data Sheet: http://www.analog.com/media/en/technical-documentation/data-sheets/ADM2795E.pdf

\*Application Note: http://www.analog.com/media/en/technical-documentation/application-notes/AN-1398.pdf

--------------

Software
========

::

         *Arduino Uno Example Code
           *[[https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz_arduino_code_rev.b.zip|Reciever and Transmitter sample code]]

--------------

.. |eval-adm2795e-ardz joystick 1.png| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz joystick 1.png
   :width: 150px
.. |eval-adm2795e-ardz joystick 2.png| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz joystick 2.png
   :width: 150px
.. |eval-adm2795e-ardz joystick 3.png| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz joystick 3.png
   :width: 150px
.. |eval-adm2795e-ardz ultrasound 1.png| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz ultrasound 1.png
   :width: 150px
.. |eval-adm2795e-ardz ultrasound 2.png| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz ultrasound 2.png
   :width: 150px
.. |eval-adm2795e-ardz ultrasound 3.png| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz ultrasound 3.png
   :width: 150px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz terminal block.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/eval-adm2795e-ardz terminal block.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/eval-adm2795e-ardz_isolation_example.png
   :width: 600px
