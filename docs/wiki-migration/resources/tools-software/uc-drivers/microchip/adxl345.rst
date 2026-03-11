ADXL345 - No-OS Driver for Microchip Microcontroller Platforms
==============================================================


ADXL345 No-OS Driver
====================

Supported Devices
-----------------

-  :adi:`ADXL345`

Evaluation Boards
-----------------

-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_
-  :adi:`EVAL-ADXL313-Z-M`
-  :adi:`EVAL-ADXL345Z`
-  :adi:`EVAL-ADXL345Z-DB`

Reference Circuits
------------------

-  :adi:`CN0133`

Overview
--------


The :adi:`ADXL345` is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g. Digital output data is formatted as 16-bit twos complement and is accessible through either a SPI (3- or 4-wire) or I2C digital interface.

The :adi:`ADXL345` is well suited for mobile device applications. It measures the static acceleration of gravity in tilt-sensing applications, as well as dynamic acceleration resulting from motion or shock. Its high resolution (4 mg/LSB) enables measurement of inclination changes less than 1.0°.

Several special sensing functions are provided. Activity and inactivity sensing detect the presence or lack of motion and if the acceleration on any axis exceeds a user-set level. Tap sensing detects single and double taps. Free-fall sensing detects if the device is falling. These functions can be mapped to one of two interrupt output pins. An integrated, patent pending 32-level first in, first out (FIFO) buffer can be used to store data to minimize host processor intervention.

Low power modes enable intelligent motion-based power management with threshold sensing and active acceleration measurement at extremely low power dissipation.

The :adi:`ADXL345` is supplied in a small, thin, 3 mm × 5 mm × 1 mm, 14-lead, plastic package.

Applications
============

-  ADXL345-EP Supports defense and aerospace applications (AQEC)

.. image:: https://wiki.analog.com/_media/resources/pmods/adxl345_pmod_acl.jpg
   :align: center



The goal of this project (Microcontroller No-OS) is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. Here you can find a generic driver which can be used as a base for any microcontroller platform and also specific drivers for different microcontroller platforms.

Driver Description
------------------

The driver contains two parts:

-  The driver for the ADXL345 part, which may be used, without modifications, with any microcontroller.
-  The Communication Driver, where the specific communication functions for the desired type of processor and communication protocol have to be implemented. This driver implements the communication with the device and hides the actual details of the communication protocol to the ADI driver.

The Communication Driver has a standard interface, so the ADXL345 driver can be used exactly as it is provided.

If the SPI communication is chosen, there are three functions which are called by the ADXL345 driver:

-  SPI_Init() – initializes the communication peripheral.
-  SPI_Write() – writes data to the device.
-  SPI_Read() – reads data from the device.

|image1|

.. container:: centeralign

   SPI driver architecture


If the I2C communication is chosen, there are three functions which are called by the ADXL345 driver:

-  I2C_Init() – initializes the communication peripheral.
-  I2C_Write() – writes data to the device.
-  I2C_Read() – reads data from the device.

|image2|

.. container:: centeralign

   I2C driver architecture


The implementation of these three functions depends on the used microcontroller.

The following functions are implemented in this version of ADXL345 driver:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Function                                                                                                                                                                                          | Description                                                                         |
+===================================================================================================================================================================================================+=====================================================================================+
| char ADXL345_Init(char commProtocol)                                                                                                                                                              | Initializes the communication peripheral and checks if the ADXL345 part is present. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetRegisterValue(unsigned char registerAddress, unsigned char registerValue)                                                                                                         | Writes data into a register.                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| unsigned char ADXL345_GetRegisterValue(unsigned char registerAddress)                                                                                                                             | Reads the value of a register.                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetPowerMode(unsigned char pwrMode)                                                                                                                                                  | Places the device into standby/measure mode.                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_GetXyz(short\* x, short\* y, short\* z)                                                                                                                                              | Reads the raw output data of each axis.                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_GetGxyz(float\* x, float\* y, float\* z)                                                                                                                                             | Reads the raw output data of each axis and converts it to g.                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetTapDetection(unsigned char tapType, unsigned char tapAxes, unsigned char tapDur, unsigned char tapLatent, unsigned char tapWindow, unsigned char tapThresh, unsigned char tapInt) | Enables/disables the tap detection.                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetActivityDetection(unsigned char actOnOff, unsigned char actAxes, unsigned char actAcDc, unsigned char actThresh, unsigned char actInt)                                            | Enables/disables the activity detection.                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetInactivityDetection(unsigned char inactOnOff, unsigned char inactAxes, unsigned char inactAcDc, unsigned char inactThresh, unsigned char inactTime, unsigned char inactInt)       | Enables/disables the inactivity detection.                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetFreeFallDetection(unsigned char ffOnOff, unsigned char ffThresh, unsigned char ffTime, unsigned char ffInt)                                                                       | Enables/disables the free-fall detection.                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetOffset(unsigned char xOffset, unsigned char yOffset, unsigned char zOffset)                                                                                                       | Calibrates the accelerometer.                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| void ADXL345_SetRangeResolution(unsigned char gRange, unsigned char fullRes)                                                                                                                      | Selects the measurement range.                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_architecture.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/i2c_architecture.png



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

This section contains a description of the steps required to run the ADXL345 demonstration project on a Digilent Cerebot MX3cK platform.

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

   The ADXL345 demonstration project for PIC32MX320F128H consists of three parts: the **ADXL345 Driver**, the **PmodACL Demo for PIC32MX320F128H** and the **PIC32MX320F128H Common Drivers**.

   
   All three parts have to be downloaded.


Hardware Setup
--------------

A PmodACL can be connected to the J2 connector of Cerebot MX3cK development board for I2C operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_i2c_pic32.jpg
   :align: center

or to the JE connector of Cerebot MX3cK development board for SPI operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_spi_pic32.jpg
   :align: center

Reference Project Overview
--------------------------

The following commands were implemented in this version of ADXL345 reference project for Cerebot MX3cK board.

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

Commands can be executed using a serial terminal connected to the UART1 peripheral of PIC32MX320F128H.

The following image shows a generic list of commands in a serial terminal connected to processor’s UART peripheral.


|image1|

Software Project Setup
----------------------


This section presents the steps for developing a software application that will run on the **Digilent Cerebot MX3cK** development board for controlling and monitoring the operation of the **ADI** part.

-  Run the **MPLAB X** integrated development environment.
-  Choose to create a new project.
-  In the **Choose Project** window select **Microchip Embedded** category, **Standalone Project** and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_0.png
   :align: center

-  In the **Select Device** window choose **PIC32MX320F128H** device and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_1.png
   :align: center

-  In the **Select Tool** window select the desired hardware tool and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_2.png
   :align: center

-  In the **Select Compiler** window chose the **XC32** compiler and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_3.png
   :align: center

-  In the **Select Project Name and Folder** window choose a name and a location for the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_4.png
   :align: center

-  After the project is created, all the downloaded source files have to be copied in the project folder and included in the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_5.png
   :align: center

-  The project is ready to be built and downloaded on the development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pic32_software_design_6.png
   :align: center



Digilent Cerebot MC7 Quick Start Guide
======================================

This section contains a description of the steps required to run the ADXL345 demonstration project on a Digilent Cerebot MC7 platform.

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

A PmodACL can be connected to the J6 connector of Cerebot MC7 development board for I2C operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_i2c_dspic33.jpg
   :align: center

or to the JB connector of Cerebot MC7 development board for SPI operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_spi_dspic33.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXL345 reference project for Cerebot MC7 board.

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

Commands can be executed using a serial terminal connected to the UART1 peripheral of dsPIC33FJ128MC706A.

The following image shows a list of commands in a serial terminal connected to processor’s UART peripheral.


|image2|

Software Project Setup
----------------------


This section presents the steps for developing a software application that will run on the **Digilent Cerebot MC7** development board for controlling and monitoring the operation of the **ADI** part.

-  Run the **MPLAB X** integrated development environment.
-  Choose to create a new project.
-  In the **Choose Project** window select **Microchip Embedded** category, **Standalone Project** and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_0.png
   :align: center

-  In the **Select Device** window choose **dsPIC33FJ128MC706A** device and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_1.png
   :align: center

-  In the **Select Tool** window select the desired hardware tool and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_2.png
   :align: center

-  In the **Select Compiler** window chose the **XC16** compiler and press **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_3.png
   :align: center

-  In the **Select Project Name and Folder** window choose a name and a location for the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_4.png
   :align: center

-  After the project is created, the source files have to be copied in the project folder and included in the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_5.png
   :align: center

-  The project is ready to be built and downloaded on the development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/dspic33_software_design_6.png
   :align: center



Digilent Cerebot MX3cK Quick Start Guide - chipKIT Project
==========================================================

This section contains a description of the steps required to run the ADXL345 chipKIT demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  PmodACL

Required Software
-----------------

-  `MPIDE <https://github.com/chipKIT32/chipKIT32-MAX/downloads>`_

Hardware Setup
--------------

A PmodACL can be connected to the J2 connector of Cerebot MX3cK development board for I2C operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_i2c_pic32_arduino.jpg
   :align: center

or to the JE connector of Cerebot MX3cK development board for SPI operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl_spi_pic32_arduino.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXL345 reference project for Cerebot MX3cK board.

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


This section presents the steps for developing a chipKIT application that will run on the **Digilent Cerebot MX3cK** development board for controlling and monitoring the operation of the **ADI** part.

-  Under your **Sketchbook** directory create a folder called "Libraries"; this folder may already exist.
-  Unzip the downloaded file in the libraries folder.
-  Run the **MPIDE** environment.
-  You should see the new library under **Sketch->Import Library**, under **Contributed**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/arduino_software_design_1.png
   :align: center

-  Also you should see under **File->Examples** the demo project for the ADI library.
-  Select the ADIDriver example.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/arduino_software_design_2.png
   :align: center

-  Select the **Cerebot MX3cK** board from **Tools->Board**.
-  Select the corresponding Serial Communication Port from **Tools->Serial Port**
-  The project is ready to be uploaded on the development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/arduino_software_design_3.png
   :align: center



More information
================


-  :ez:`ask questions about the Microcontroller no-OS Drivers <community/linux-device-drivers/microcontroller-no-os-drivers>`
-  Example questions:

|//ez.analog.com/community/feeds/allcontent/atom|

.. |//ez.analog.com/community/feeds/allcontent/atom| image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom



.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_pic32.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_dspic33.png
