ADXRS453 - No-OS Driver for Microchip Microcontroller Platforms
===============================================================

Supported Devices
-----------------

-  :adi:`ADXRS453`

Evaluation Boards
-----------------

-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`_

Overview
--------

The :adi:`ADXRS453` is an angular rate sensor (gyroscope) intended for industrial, instrumentation, and stabilization applications in high vibration environments. An advanced, differential, quad sensor design rejects the influence of linear acceleration, enabling the :adi:`ADXRS453` to offer high accuracy rate sensing in harsh environments where shock and vibration are present.

The :adi:`ADXRS453` uses an internal, continuous self-test architecture. The integrity of the electromechanical system is checked by applying a high frequency electrostatic force to the sense structure to generate a rate signal that can be differentiated from the base-band rate data and internally analyzed.

The :adi:`ADXRS453` is capable of sensing an angular rate of up to ±300°/sec. Angular rate data is presented as a 16-bit word that is part of a 32-bit SPI message.

The :adi:`ADXRS453` is available in a 16-lead plastic cavity SOIC (SOIC_CAV) and an SMT-compatible vertical mount package (LCC_V), and is capable of operating across a wide voltage range (3.3 V to 5 V).

Applications
~~~~~~~~~~~~

-  Rotation sensing in high vibration environments
-  Rotation sensing for industrial and instrumentation applications
-  High performance platform stabilization

.. image:: https://wiki.analog.com/_media/resources/pmods/adxrs453_pmod_gyro2.jpg
   :align: center


The goal of this project (Microcontroller No-OS) is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. Here you can find a generic driver which can be used as a base for any microcontroller platform and also specific drivers for different microcontroller platforms.

Driver Description
------------------

The driver contains two parts:

-  The driver for the ADXRS453 part, which may be used, without modifications, with any microcontroller.
-  The Communication Driver, where the specific communication functions for the desired type of processor and communication protocol have to be implemented. This driver implements the communication with the device and hides the actual details of the communication protocol to the ADI driver.

The Communication Driver has a standard interface, so the ADXRS453 driver can be used exactly as it is provided.

There are three functions which are called by the ADXRS453 driver:

-  SPI_Init() – initializes the communication peripheral.
-  SPI_Write() – writes data to the device.
-  SPI_Read() – reads data from the device.

|image1|

.. container:: centeralign

   SPI driver architecture


The following functions are implemented in this version of ADXRS453 driver:

+----------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Function                                                                         | Description                                                         |
+==================================================================================+=====================================================================+
| char ADXRS453_Init(void)                                                         | Initializes the ADXRS453 and checks if the device is present.       |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------+
| unsigned short ADXRS453_GetRegisterValue(unsigned char regAddress)               | Reads the value of a register.                                      |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------+
| void ADXRS453_SetRegisterValue(unsigned char regAddress, unsigned short regData) | Writes data into a register.                                        |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------+
| unsigned long ADXRS453_GetSensorData(void)                                       | Reads the sensor data.                                              |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------+
| float ADXRS453_GetRate(void)                                                     | Reads the rate data and converts it to degrees/second.              |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------+
| float ADXRS453_GetTemperature(void)                                              | Reads temperature from ADXRS453 and converts it to degrees Celsius. |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_architecture.png


**HW Platform(s):**

-  `Digilent Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXRS453 DSPIC33 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxrs453_dspic33.zip>`_
   -  `ADXRS453 chipKIT Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxrs453_arduino.zip>`_
   -  **ADXRS453 Driver:** :git-no-OS:`drivers/gyro/adxrs453`
   -  **PmodGYRO2 Demo for PIC32MX320F128H:** :git-no-OS:`Microchip/PIC32MX320F128H/PmodGYRO2`
   -  **PIC32MX320F128H Common Drivers:** :git-no-OS:`Microchip/PIC32MX320F128H/Common`
   


Digilent Cerebot MX3cK Quick Start Guide
========================================

This section contains a description of the steps required to run the ADXRS453 demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`_

Required Software
-----------------

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`_
-  `MPLAB XC32 compiler <http://www.microchip.com/mplabxc>`_
-  The ADXRS453 demonstration project for PIC32MX320F128H.

.. note::

   The ADXRS453 demonstration project for PIC32MX320F128H consists of three parts: the ADXRS453 Driver, the PmodGYRO2 Demo for PIC32MX320F128H and the PIC32MX320F128H Common Drivers.

   
   All three parts have to be downloaded.


Hardware Setup
--------------

A PmodGYRO2 has to be connected to the JE connector of Cerebot MX3cK development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_gyro2_pic32.jpg
   :align: center

Reference Project Overview
--------------------------

The following commands were implemented in this version of ADXRS453 reference project for Cerebot MX3cK board.

============ ==================================
Command      Description
============ ==================================
help?        Displays all available commands.
temperature? Displays the ambient temperature.
measure!     Starts measurement for 30 samples.
============ ==================================

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

This section contains a description of the steps required to run the ADXRS453 demonstration project on a Digilent Cerebot MC7 platform.

Required Hardware
-----------------

-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`_
-  PmodGYRO2

Required Software
-----------------

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`_
-  `MPLAB XC16 compiler <http://www.microchip.com/mplabxc>`_

Hardware Setup
--------------

A PmodGYRO2 has to be connected to the JB connector of Cerebot MC7 development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_gyro2_dspic33.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXRS453 reference project for Cerebot MC7 board.

============ ======================================
Command      Description
============ ======================================
help?        Displays all available commands.
temperature? Displays the temperature.
start=       Starts measurement. Accepted value: 1.
============ ======================================

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

This section contains a description of the steps required to run the ADXRS453 chipKIT demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
-----------------

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`_
-  PmodGYRO2

Required Software
-----------------

-  `MPIDE <https://github.com/chipKIT32/chipKIT32-MAX/downloads>`_

Hardware Setup
--------------

A PmodGYRO2 has to be connected to the JE connector of Cerebot MX3cK development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_gyro2_pic32_arduino.jpg
   :align: center

Reference Project Overview
--------------------------

Following commands were implemented in this version of ADXRS453 chipKIT reference project for Cerebot MX3cK board.

============ ========================================
Command      Description
============ ========================================
help?        Displays all available commands.
temperature? Displays the ambient device temperature.
start=       Starts measurement. Accepted value: 1.
============ ========================================

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
