ADXL345 - No-OS Driver for Renesas Microcontroller Platforms
============================================================

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

Several special sensing functions are provided. Activity and inactivity sensing
detect the presence or lack of motion and if the acceleration on any axis
exceeds a user-set level. Tap sensing detects single and double taps. Free-fall
sensing detects if the device is falling. These functions can be mapped to one
of two interrupt output pins. An integrated, patent pending 32-level first in,
first out (FIFO) buffer can be used to store data to minimize host processor
intervention.

Low power modes enable intelligent motion-based power management with threshold
sensing and active acceleration measurement at extremely low power dissipation.

The :adi:`ADXL345` is supplied in a small, thin, 3 mm × 5 mm × 1 mm, 14-lead, plastic package.

Applications
============

-  ADXL345-EP Supports defense and aerospace applications (AQEC)

.. image:: https://wiki.analog.com/_media/resources/pmods/adxl345_pmod_acl.jpg
   :align: center

The goal of this project (Microcontroller No-OS) is to be able to provide
reference projects for lower end processors, which can't run Linux, or aren't
running a specific operating system, to help those customers using
microcontrollers with ADI parts. Here you can find a generic driver which can be
used as a base for any microcontroller platform and also specific drivers for
different microcontroller platforms.

Driver Description
------------------

The driver contains two parts:

-  The driver for the ADXL345 part, which may be used, without modifications, with any microcontroller.
-  The Communication Driver, where the specific communication functions for the
   desired type of processor and communication protocol have to be implemented.
   This driver implements the communication with the device and hides the actual
   details of the communication protocol to the ADI driver.

The Communication Driver has a standard interface, so the ADXL345 driver can be
used exactly as it is provided.

If the SPI communication is chosen, there are three functions which are called
by the ADXL345 driver:

-  SPI_Init() – initializes the communication peripheral.
-  SPI_Write() – writes data to the device.
-  SPI_Read() – reads data from the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_architecture.png
   :align: center

.. container:: centeralign

   SPI driver architecture

If the I2C communication is chosen, there are three functions which are called
by the ADXL345 driver:

-  I2C_Init() – initializes the communication peripheral.
-  I2C_Write() – writes data to the device.
-  I2C_Read() – reads data from the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/i2c_architecture.png
   :align: center

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

**HW Platform(s):**

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `Renesas Demo Kit for RX62N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL345 RL78G13 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g13.zip>`_
   -  `ADXL345 RX62N Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rx62n.zip>`_
   -  **ADXL345 Driver:** :git-no-OS:`drivers/accel/adxl345`
   -  **PmodACL Demo for RL78G14:** :git-no-OS:`Renesas/RL78G14/PmodACL`
   -  **RL78G14 Common Drivers:** :git-no-OS:`Renesas/RL78G14/Common`
   

Renesas RL78G13 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL345
demonstration project on a Renesas RL78G13 platform.

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_ (optional, because an ADXL345 part is installed on Renesas Demonstration Kit (RDK) for RL78G13)

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_

Hardware Setup
--------------

There are two options:

-  The ADXL345 part installed on the Renesas Demonstration Kit (RDK) for RL78G13
   can be used. In this case, the I2C protocol has to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g13.jpg
   :align: center

-  A PmodACL can be connected to the PMOD1 connector. In this case, the SPI
   protocol has to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl_rl78g13.jpg
   :align: center

Reference Project Overview
--------------------------

In this example, the output data of each axis is read and displayed on the
Renesas Demonstration Kit for RL78G13 board’s LCD. Were also activated “Single
Tap”, “Double Tap” and “Free-Fall” interrupts. When one of them occurs, on the
LCD screen appears a corresponding message.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g13_screen.jpg
   :align: center

Software Project Setup
----------------------

.. note::

   See `rl78g13_software_tutorial_without_applilet3 <https://wiki.analog.com/rl78g13_software_tutorial_without_applilet3>`_

Renesas RL78G14 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL345
demonstration project on a Renesas RL78G14 platform using the PmodACL.

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G14 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g14-yrdkrl78g14-demonstration-kit-rl78g14>`_
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_ (optional, because an ADXL345 part is installed on Renesas Demonstration Kit (RDK) for RL78G14)

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_
-  The ADXL345 demonstration project for the Renesas RL78G14 platform.

.. note::

   The ADXL345 demonstration project for the Renesas RL78G14 platform consists
   of three parts: the ADXL345 Driver, the PmodACL Demo for RL78G14 and the
   RL78G14 Common Drivers.

   
   All three parts have to be downloaded.

Hardware Setup
--------------

There are two options:

-  The ADXL345 part installed on the Renesas Demonstration Kit (RDK) for RL78G14
   can be used. In this case, the I2C protocol has to be chosen with
   'ADXL345_Init()' function.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g14.jpg
   :align: center

-  A PmodACL can be connected to the PMOD1 connector. In this case, the SPI
   protocol has to be chosen with 'ADXL345_Init()' function.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl_rl78g14.jpg
   :align: center

Reference Project Overview
--------------------------

The reference project:

-  reads and displays the data for each axis on LCD;
-  it displays also on LCD if the interrupts “Single Tap”, “Double Tap” or
   “Free-Fall” were activated.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g14_screen.jpg
   :align: center

Software Project Tutorial
-------------------------

.. note::

   See `rl78g14_software_tutorial <https://wiki.analog.com/rl78g14_software_tutorial>`_

Renesas RX62N Quick Start Guide
===============================

This section contains a description of the steps required to run the ADXL345
demonstration project on a Renesas RX62N platform.

Required Hardware
-----------------

-  `Renesas Demo Kit for RX62N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`_
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_ (optional, because an ADXL345 part is installed on Renesas Demonstration Kit (RDK) for RX62N)

Required Software
-----------------

-  `High-performance Embedded Workshop for RX62N family <https://www.renesas.com/us/en/software-tool/high-performance-embedded-workshop>`_
-  `Renesas Peripheral Driver Library for RX62N family <https://www.renesas.com/us/en/software-tool/renesas-peripheral-driver-library>`_

Hardware Setup
--------------

There are two options:

-  The ADXL345 part installed on the Renesas Demonstration Kit (RDK) for RX62N
   can be used. In this case, the I2C protocol has to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rx62n.jpg
   :align: center

-  A PmodACL can be connected to the Renesas Demonstration Kit (RDK) for RX62N
   (in this case, the SPI protocol has to be chosen):

::

     PmodACL Pin 1 (CS)   → YRDKRX62N J8 connector Pin 15
     PmodACL Pin 2 (MOSI) → YRDKRX62N J8 connector Pin 19
     PmodACL Pin 3 (MISO) → YRDKRX62N J8 connector Pin 22
     PmodACL Pin 4 (CLK)  → YRDKRX62N J8 connector Pin 20
     PmodACL Pin 5 (GND)  → YRDKRX62N J8 connector Pin 4
     PmodACL Pin 6 (VCC)  → YRDKRX62N J8 connector Pin 3

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl_rx62n.jpg
   :align: center

Reference Project Overview
--------------------------

In this example, the output data of each axis is read and displayed on the
Renesas Demonstration Kit for RX62N board’s LCD. Were also activated “Single
Tap”, “Double Tap” and “Free-Fall” interrupts. When one of them occurs, on the
LCD screen appears a corresponding message.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rx62n_screen.jpg
   :align: center

Software Project Setup
----------------------

.. note::

   See `rx62n_software_design <https://wiki.analog.com/rx62n_software_design>`_

More information
================

-  :ez:`ask questions about the Microcontroller no-OS Drivers <community/linux-device-drivers/microcontroller-no-os-drivers>`
-  Example questions:

.. image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom
   :alt: //ez.analog.com/community/feeds/allcontent/atom
