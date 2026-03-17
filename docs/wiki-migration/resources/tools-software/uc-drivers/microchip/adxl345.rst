ADXL345 - No-OS Driver for Microchip Microcontroller Platforms
==============================================================

.. include:: ../adxl345.rst

**HW Platform(s):**

-  `Digilent Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL345 DSPIC33 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxl345_dspic33.zip>`_
   -  `ADXL345 chipKIT Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxl345_arduino.zip>`_
   -  **ADXL345 Driver:** :git-no-OS:`drivers/accel/adxl345`
   -  **PmodACL Demo for PIC32MX320F128H:** :git-no-OS:`Microchip/PIC32MX320F128H/PmodACL`
   -  **PIC32MX320F128H Common Drivers:** :git-no-OS:`Microchip/PIC32MX320F128H/Common`
   

Digilent Cerebot MX3cK Quick Start Guide
========================================

This section contains a description of the steps required to run the ADXL345
demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_

Required Software
-----------------

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`_
-  `MPLAB XC32 compiler <http://www.microchip.com/mplabxc>`_
-  The ADXL345 demonstration project for PIC32MX320F128H.

.. note::

   The ADXL345 demonstration project for PIC32MX320F128H consists of three
   parts: the ADXL345 Driver, the PmodACL Demo for PIC32MX320F128H and the
   PIC32MX320F128H Common Drivers.

   
   All three parts have to be downloaded.

Hardware Setup
--------------

A PmodACL can be connected to the J2 connector of Cerebot MX3cK development
board for I2C operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_i2c_pic32.jpg
   :align: center

or to the JE connector of Cerebot MX3cK development board for SPI operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_spi_pic32.jpg
   :align: center

Reference Project Overview
--------------------------

The following commands were implemented in this version of ADXL345 reference
project for Cerebot MX3cK board.

============== =====================================================
Command        Description
============== =====================================================
help?          Displays all available commands.
communication= Selects the communication interface. Accepted values:
               0 - SPI.
               1 - I2C.
communication? Displays the selected communication interface.
acceleration?  Displays the accelerations on XYZ axes.
accelerationX? Displays the acceleration on X axis.
accelerationY? Displays the acceleration on Y axis.
accelerationZ? Displays the acceleration on Z axis.
interrupts?    Displays the state of the interrupts.
============== =====================================================

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

This section contains a description of the steps required to run the ADXL345
demonstration project on a Digilent Cerebot MC7 platform.

Required Hardware
-----------------

-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`_
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_

Required Software
-----------------

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`_
-  `MPLAB XC16 compiler <http://www.microchip.com/mplabxc>`_

Hardware Setup
--------------

A PmodACL can be connected to the J6 connector of Cerebot MC7 development board
for I2C operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_i2c_dspic33.jpg
   :align: center

or to the JB connector of Cerebot MC7 development board for SPI operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_spi_dspic33.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXL345 reference project
for Cerebot MC7 board.

+----------------+----------------------------------------------------------------------+
| Command        | Description                                                          |
+================+======================================================================+
| help?          | Displays all available commands.                                     |
+----------------+----------------------------------------------------------------------+
| communication= | Selects the communication interface. Accepted values: 0(I2C),1(SPI). |
+----------------+----------------------------------------------------------------------+
| communication? | Displays the selected communication interface.                       |
+----------------+----------------------------------------------------------------------+
| acceleration?  | Displays the acceleration on XYZ axis.                               |
+----------------+----------------------------------------------------------------------+
| interrupts?    | Displays the state of the interrupts.                                |
+----------------+----------------------------------------------------------------------+

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

This section contains a description of the steps required to run the ADXL345
chipKIT demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  PmodACL

Required Software
-----------------

-  `MPIDE <https://github.com/chipKIT32/chipKIT32-MAX/downloads>`_

Hardware Setup
--------------

A PmodACL can be connected to the J2 connector of Cerebot MX3cK development
board for I2C operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_i2c_pic32_arduino.jpg
   :align: center

or to the JE connector of Cerebot MX3cK development board for SPI operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_spi_pic32_arduino.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXL345 reference project
for Cerebot MX3cK board.

+----------------+----------------------------------------------------------------------+
| Command        | Description                                                          |
+================+======================================================================+
| help?          | Displays all available commands.                                     |
+----------------+----------------------------------------------------------------------+
| communication= | Selects the communication interface. Accepted values: 0(I2C),1(SPI). |
+----------------+----------------------------------------------------------------------+
| communication? | Displays the selected communication interface.                       |
+----------------+----------------------------------------------------------------------+
| acceleration?  | Displays the acceleration on XYZ axis.                               |
+----------------+----------------------------------------------------------------------+
| interrupts?    | Displays the state of the interrupts.                                |
+----------------+----------------------------------------------------------------------+

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
