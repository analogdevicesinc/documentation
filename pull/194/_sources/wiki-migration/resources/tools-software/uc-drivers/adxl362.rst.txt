Supported Devices
=================

-  :adi:`ADXL362`

Evaluation Boards
=================

-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

Overview
========

.. include:: ../../pmods/adxl362.rst

The goal of this project (Microcontroller No-OS) is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. Here you can find a generic driver which can be used as a base for any microcontroller platform and also specific drivers for different microcontroller platforms.

Driver Description
==================

The driver contains two parts:

-  The driver for the ADXL362 part, which may be used, without modifications, with any microcontroller.
-  The Communication Driver, where the specific communication functions for the desired type of processor and communication protocol have to be implemented. This driver implements the communication with the device and hides the actual details of the communication protocol to the ADI driver.

The Communication Driver has a standard interface, so the ADXL362 driver can be used exactly as it is provided.

There are three functions which are called by the ADXL362 driver:

-  SPI_Init() – initializes the communication peripheral.
-  SPI_Write() – writes data to the device.
-  SPI_Read() – reads data from the device.

|image1|

.. container:: centeralign

   SPI driver architecture


The following functions are implemented in this version of ADXL362 driver:

+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Function                                                                                                              | Description                                                            |
+=======================================================================================================================+========================================================================+
| char ADXL362_Init(void)                                                                                               | Initializes the device.                                                |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SetRegisterValue(unsigned short registerValue, unsigned char registerAddress, unsigned char bytesNumber) | Writes data into a register.                                           |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_GetRegisterValue(unsigned char \*pReadData, unsigned char registerAddress, unsigned char bytesNumber)    | Performs a burst read of a specified number of registers.              |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_GetFifoValue(unsigned char \*pBuffer, unsigned short bytesNumber)                                        | Reads multiple bytes from the device's FIFO buffer.                    |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SoftwareReset(void)                                                                                      | Resets the device via SPI communication bus.                           |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SetPowerMode(unsigned char pwrMode)                                                                      | Places the device into standby/measure mode.                           |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SetRange(unsigned char gRange)                                                                           | Selects the measurement range.                                         |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SetOutputRate(unsigned char outRate)                                                                     | Selects the Output Data Rate of the device.                            |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_GetXyz(short \*x, short \*y, short \*z)                                                                  | Reads the 3-axis raw data from the accelerometer.                      |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_GetGxyz(float\* x, float\* y, float\* z)                                                                 | Reads the 3-axis raw data from the accelerometer and converts it to g. |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| float ADXL362_ReadTemperature(void)                                                                                   | Reads the temperature of the device.                                   |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_FifoSetup(unsigned char mode, unsigned short waterMarkLvl, unsigned char enTempRead)                     | Configures the FIFO feature.                                           |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SetupActivityDetection(unsigned char refOrAbs, unsigned short threshold, unsigned char time)             | Configures activity detection.                                         |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| void ADXL362_SetupInactivityDetection(unsigned char refOrAbs, unsigned short threshold, unsigned short time)          | Configures inactivity detection.                                       |
+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_architecture.png
