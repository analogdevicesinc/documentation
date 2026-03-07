Supported Devices
=================

-  :adi:`ADXRS453`

Evaluation Boards
=================

-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`_

Overview
========

.. include:: ../../pmods/adxrs453.rst

The goal of this project (Microcontroller No-OS) is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. Here you can find a generic driver which can be used as a base for any microcontroller platform and also specific drivers for different microcontroller platforms.

Driver Description
==================

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
