ADXL362 - No-OS Driver for Microchip Microcontroller Platforms
==============================================================

.. include:: ../adxl362.rst

**HW Platform(s):**

-  `Digilent Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL362 DSPIC33 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxl362_dspic33.zip>`_
   -  `ADXL362 chipKIT Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxl362_arduino.zip>`_
   -  **ADXL362 Driver:** :git-no-OS:`drivers/accel/adxl362`
   -  **PmodACL2 Demo for PIC32MX320F128H:** :git-no-OS:`Microchip/PIC32MX320F128H/PmodACL2`
   -  **PIC32MX320F128H Common Drivers:** :git-no-OS:`Microchip/PIC32MX320F128H/Common`
   

Digilent Cerebot MX3cK Quick Start Guide
========================================

This section contains a description of the steps required to run the ADXL362
demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

Required Software
-----------------

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`_
-  `MPLAB XC32 compiler <http://www.microchip.com/mplabxc>`_
-  The ADXL362 demonstration project for PIC32MX320F128H.

.. note::

   The ADXL362 demonstration project for PIC32MX320F128H consists of three
   parts: the ADXL362 Driver, the PmodACL2 Demo for PIC32MX320F128H and the
   PIC32MX320F128H Common Drivers.

   
   All three parts have to be downloaded.

Hardware Setup
--------------

A PmodACL2 has to be connected to the JE connector of Cerebot MX3cK development
board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl2_pic32.jpg
   :align: center

Reference Project Overview
--------------------------

The following commands were implemented in this version of ADXL362 reference
project for Cerebot MX3cK board.

+----------------+------------------------------------------------------------------------------+
| Command        | Description                                                                  |
+================+==============================================================================+
| help?          | Displays all available commands.                                             |
+----------------+------------------------------------------------------------------------------+
| id?            | Displays device details.                                                     |
+----------------+------------------------------------------------------------------------------+
| measure=       | Start/stop the measurement process of the device. Accepted values:           |
|                | 0 - Stop measurement.                                                        |
|                | 1 - Start measurement.                                                       |
+----------------+------------------------------------------------------------------------------+
| temperature?   | Displays the temperature.                                                    |
+----------------+------------------------------------------------------------------------------+
| reset!         | Resets the device.                                                           |
+----------------+------------------------------------------------------------------------------+
| acceleration?  | Displays the accelerations on XYZ axes.                                      |
+----------------+------------------------------------------------------------------------------+
| accelerationX? | Displays the acceleration on X axis.                                         |
+----------------+------------------------------------------------------------------------------+
| accelerationY? | Displays the acceleration on Y axis.                                         |
+----------------+------------------------------------------------------------------------------+
| accelerationZ? | Displays the acceleration on Z axis.                                         |
+----------------+------------------------------------------------------------------------------+
| activity?      | Displays the activity status of the device. It runs for 5 motion detections. |
+----------------+------------------------------------------------------------------------------+

Commands can be executed using a serial terminal connected to the UART1
peripheral of PIC32MX320F128H.

The following image shows a generic list of commands in a serial terminal
connected to processor’s UART peripheral.

|image1|

Software Project Setup
----------------------

.. include:: pic32_software_design.rst

Digilent Cerebot MC7 Quick Start Guide
======================================

This section contains a description of the steps required to run the ADXL362
demonstration project on a Digilent Cerebot MC7 platform.

Required Hardware
-----------------

-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`_
-  PmodACL2

Required Software
-----------------

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`_
-  `MPLAB XC16 compiler <http://www.microchip.com/mplabxc>`_

Hardware Setup
--------------

A PmodACL2 can be connected to the JB connector of Cerebot MC7 development board
for SPI operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl2_dspic33.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXL362 reference project
for Cerebot MC7 board.

+---------------+------------------------------------------------------------------------------+
| Command       | Description                                                                  |
+===============+==============================================================================+
| help?         | Displays all available commands.                                             |
+---------------+------------------------------------------------------------------------------+
| id?           | Device details.                                                              |
+---------------+------------------------------------------------------------------------------+
| measure=      | Start/stop the measure process of the device. Accepted values: 0 - 1.        |
+---------------+------------------------------------------------------------------------------+
| temp?         | Read the temperature.                                                        |
+---------------+------------------------------------------------------------------------------+
| reset=        | Reset the device.                                                            |
+---------------+------------------------------------------------------------------------------+
| acceleration? | Displays the accelerations on XYZ axis.                                      |
+---------------+------------------------------------------------------------------------------+
| activity?     | Displays the activity status of the device. It runs for 5 motion detections. |
+---------------+------------------------------------------------------------------------------+

Commands can be executed using a serial terminal connected to the UART1
peripheral of dsPIC33FJ128MC706A.

The following image shows a list of commands in a serial terminal connected to
processor’s UART peripheral.

|image2|

Software Project Setup
----------------------

.. include:: dspic33_software_design.rst

Digilent Cerebot MX3cK Quick Start Guide - chipKIT Project
==========================================================

This section contains a description of the steps required to run the ADXL362
chipKIT demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  PmodACL2

Required Software
-----------------

-  `MPIDE <https://github.com/chipKIT32/chipKIT32-MAX/downloads>`_

Hardware Setup
--------------

A PmodACL2 has to be connected to the JE connector of Cerebot MX3cK development
board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl2_pic32_arduino.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXL362 chipKIT reference
project for Cerebot MX3cK board.

+---------------+------------------------------------------------------------------------------+
| Command       | Description                                                                  |
+===============+==============================================================================+
| help?         | Displays all available commands.                                             |
+---------------+------------------------------------------------------------------------------+
| id?           | Device details.                                                              |
+---------------+------------------------------------------------------------------------------+
| measure=      | Start/stop the measure process of the device. Accepted values: 0 - 1.        |
+---------------+------------------------------------------------------------------------------+
| temp?         | Read the temperature.                                                        |
+---------------+------------------------------------------------------------------------------+
| reset=        | Reset the device.                                                            |
+---------------+------------------------------------------------------------------------------+
| acceleration? | Displays the accelerations on XYZ axis.                                      |
+---------------+------------------------------------------------------------------------------+
| activity?     | Displays the activity status of the device. It runs for 5 motion detections. |
+---------------+------------------------------------------------------------------------------+

Commands can be executed using the serial monitor.

**Carriage return** has to be selected as a line ending character. The required baud rate is **9600 baud**.

The following image shows a list of commands in the serial monitor.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_arduino.png
   :align: center

Software Project Setup
----------------------

.. include:: arduino_software_design.rst

More information
================

.. include:: ../more-information.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_pic32.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_dspic33.png
