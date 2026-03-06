ADXL362 - No-OS Driver for Microchip Microcontroller Platforms
==============================================================

.. include:: ../adxl362.rst

**HW Platform(s):**

-  `Digilent Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`__
-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`__

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL362 DSPIC33 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxl362_dspic33.zip>`__
   -  `ADXL362 chipKIT Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/adxl362_arduino.zip>`__
   -  **ADXL362 Driver:** :git-no-OS:`drivers/accel/adxl362`
   -  **PmodACL2 Demo for PIC32MX320F128H:** :git-no-OS:`Microchip/PIC32MX320F128H/PmodACL2`
   -  **PIC32MX320F128H Common Drivers:** :git-no-OS:`Microchip/PIC32MX320F128H/Common`
   


Digilent Cerebot MX3cK Quick Start Guide
========================================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Digilent Cerebot MX3cK platform.

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`__
-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`__

Required Software
~~~~~~~~~~~~~~~~~

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`__
-  `MPLAB XC32 compiler <http://www.microchip.com/mplabxc>`__
-  The ADXL362 demonstration project for PIC32MX320F128H.

.. note::

   The ADXL362 demonstration project for PIC32MX320F128H consists of three parts: the **ADXL362 Driver**, the **PmodACL2 Demo for PIC32MX320F128H** and the **PIC32MX320F128H Common Drivers**.

   
   All three parts have to be downloaded.


Hardware Setup
~~~~~~~~~~~~~~

A PmodACL2 has to be connected to the JE connector of Cerebot MX3cK development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl2_pic32.jpg
   :align: center

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following commands were implemented in this version of ADXL362 reference project for Cerebot MX3cK board.

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

This section contains a description of the steps required to run the ADXL362 demonstration project on a Digilent Cerebot MC7 platform.

.. _required-hardware-1:

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Cerebot MC7 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MC7>`__
-  PmodACL2

.. _required-software-1:

Required Software
~~~~~~~~~~~~~~~~~

-  `MPLAB X Integrated Development Environment <http://www.microchip.com/mplabx>`__
-  `MPLAB XC16 compiler <http://www.microchip.com/mplabxc>`__

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

A PmodACL2 can be connected to the JB connector of Cerebot MC7 development board for SPI operation,

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl2_dspic33.jpg
   :align: center

.. _reference-project-overview-1:

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

Following commands were implemented in this version of ADXL362 reference project for Cerebot MC7 board.

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

Commands can be executed using a serial terminal connected to the UART1 peripheral of dsPIC33FJ128MC706A.

The following image shows a list of commands in a serial terminal connected to processor’s UART peripheral.


|image2|

.. _software-project-setup-1:

Software Project Setup
~~~~~~~~~~~~~~~~~~~~~~

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

This section contains a description of the steps required to run the ADXL362 chipKIT demonstration project on a Digilent Cerebot MX3cK platform.

.. _required-hardware-2:

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Cerebot MX3cK (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=CEREBOT-MX3CK>`__
-  PmodACL2

.. _required-software-2:

Required Software
~~~~~~~~~~~~~~~~~

-  `MPIDE <https://github.com/chipKIT32/chipKIT32-MAX/downloads>`__

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

A PmodACL2 has to be connected to the JE connector of Cerebot MX3cK development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/pmod_acl2_pic32_arduino.jpg
   :align: center

.. _reference-project-overview-2:

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

Following commands were implemented in this version of ADXL362 chipKIT reference project for Cerebot MX3cK board.

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

.. _software-project-setup-2:

Software Project Setup
~~~~~~~~~~~~~~~~~~~~~~

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
