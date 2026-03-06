ADXRS453 - No-OS Driver for Microchip Microcontroller Platforms
===============================================================

.. include:: ../adxrs453.rst

**HW Platform(s):**

-  `Digilent Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`__
-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`__

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXRS453 DSPIC33 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxrs453_dspic33.zip>`__
   -  `ADXRS453 chipKIT Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxrs453_arduino.zip>`__
   -  **ADXRS453 Driver:** :git-no-OS:`drivers/gyro/adxrs453`
   -  **PmodGYRO2 Demo for PIC32MX320F128H:** :git-no-OS:`Microchip/PIC32MX320F128H/PmodGYRO2`
   -  **PIC32MX320F128H Common Drivers:** :git-no-OS:`Microchip/PIC32MX320F128H/Common`
   


Digilent Cerebot MX3cK Quick Start Guide
========================================

This section contains a description of the steps required to run the ADXRS453 demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`__
-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`__

Required Software
~~~~~~~~~~~~~~~~~

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`__
-  `MPLAB XC32 compiler <http://www.microchip.com/mplabxc>`__
-  The ADXRS453 demonstration project for PIC32MX320F128H.

.. note::

   The ADXRS453 demonstration project for PIC32MX320F128H consists of three parts: the **ADXRS453 Driver**, the **PmodGYRO2 Demo for PIC32MX320F128H** and the **PIC32MX320F128H Common Drivers**.

   
   All three parts have to be downloaded.


Hardware Setup
~~~~~~~~~~~~~~

A PmodGYRO2 has to be connected to the JE connector of Cerebot MX3cK development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_gyro2_pic32.jpg
   :align: center

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~

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

.. _required-hardware-1:

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`__
-  PmodGYRO2

.. _required-software-1:

Required Software
~~~~~~~~~~~~~~~~~

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`__
-  `MPLAB XC16 compiler <http://www.microchip.com/mplabxc>`__

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

A PmodGYRO2 has to be connected to the JB connector of Cerebot MC7 development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_gyro2_dspic33.jpg
   :align: center

.. _reference-project-overview-1:

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. _software-project-setup-1:

Software Project Setup
~~~~~~~~~~~~~~~~~~~~~~

.. include:: dspic33_software_design.rst

Digilent Cerebot MX3cK Quick Start Guide - chipKIT Project
==========================================================

This section contains a description of the steps required to run the ADXRS453 chipKIT demonstration project on a Digilent Cerebot MX3cK platform.

.. _required-hardware-2:

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`__
-  PmodGYRO2

.. _required-software-2:

Required Software
~~~~~~~~~~~~~~~~~

-  `MPIDE <https://github.com/chipKIT32/chipKIT32-MAX/downloads>`__

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

A PmodGYRO2 has to be connected to the JE connector of Cerebot MX3cK development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_gyro2_pic32_arduino.jpg
   :align: center

.. _reference-project-overview-2:

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. _software-project-setup-2:

Software Project Setup
~~~~~~~~~~~~~~~~~~~~~~

.. include:: arduino_software_design.rst

More information
================

.. include:: ../more-information.rst

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_pic32.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/terminal_dspic33.png
