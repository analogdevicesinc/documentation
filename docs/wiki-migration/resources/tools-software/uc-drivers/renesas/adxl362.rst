ADXL362 - No-OS Driver for Renesas Microcontroller Platforms
============================================================

Supported Devices
-----------------

-  :adi:`ADXL362`

Evaluation Boards
-----------------

-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

Overview
--------

The :adi:`ADXL362` is an ultralow power, 3-axis MEMS accelerometer that consumes less than 2 μA at a 100 Hz output data rate and 270 nA when in motion triggered wake-up mode. Unlike accelerometers that use power duty cycling to achieve low power consumption, the :adi:`ADXL362` does not alias input signals by undersampling; it samples the full bandwidth of the sensor at all data rates.

The :adi:`ADXL362` always provides 12-bit output resolution; 8-bit formatted data is also provided for more efficient single-byte transfers when a lower resolution is sufficient. Measurement ranges of ±2 g, ±4 g, and ±8 g are available, with a resolution of 1 mg/LSB on the ±2 g range. For applications where a noise level lower than the normal 550 μg/√Hz of the :adi:`ADXL362` is desired, either of two lower noise modes (down to 175 μg/√Hz typical) can be selected at minimal increase in supply current.

In addition to its ultralow power consumption, the :adi:`ADXL362` has many features to enable true system level power reduction. It includes a deep multimode output FIFO, a built-in micropower temperature sensor, and several activity detection modes including adjustable threshold sleep and wake-up operation that can run as low as 270 nA at a 6 Hz (approximate) measurement rate. A pin output is provided to directly control an external switch when activity is detected, if desired. In addition, the :adi:`ADXL362` has provisions for external control of sampling time and/or an external clock.

The :adi:`ADXL362` operates on a wide 1.6 V to 3.5 V supply range, and can interface, if necessary, to a host operating on a separate, lower supply voltage. :adi:`ADXL362` is available in a 3 mm × 3.25 mm × 1.06 mm package.

Applications
~~~~~~~~~~~~

-  Hearing aids
-  Home healthcare devices
-  Motion enabled power save switches
-  Wireless sensors
-  Motion enabled metering devices

.. image:: https://wiki.analog.com/_media/resources/pmods/adxl362_pmod_acl2.jpg
   :align: center


The goal of this project (Microcontroller No-OS) is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. Here you can find a generic driver which can be used as a base for any microcontroller platform and also specific drivers for different microcontroller platforms.

Driver Description
------------------

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


**HW Platform(s):**

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `Renesas Demo Kit for RX63N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx63n-yrdkrx63n-demonstration-kit-rx63n>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL362 Generic Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adxl362_generic.zip>`_
   -  `ADXL362 RL78G13 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl362_rl78g13.zip>`_
   -  `ADXL362 RX63N Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl362_rx63n.zip>`_
   -  **ADXL362 Driver:** :git-no-OS:`drivers/accel/adxl362`
   -  **PmodACL2 Demo for RL78G14:** :git-no-OS:`Renesas/RL78G14/PmodACL2`
   -  **RL78G14 Common Drivers:** :git-no-OS:`Renesas/RL78G14/Common`
   


Renesas RL78G13 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Renesas RL78G13 platform using the PmodACL2.

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_

Hardware Setup
--------------

A PmodACL2 has to be connected to the PMOD1 connector.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g13.jpg
   :align: center

Reference Project Overview
--------------------------

The reference project continuously displays on the LCD the accelerations on x-axis, y-axis and x-axis and simultaneously detects any activity or inactivity detected by the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g13_screen.jpg
   :align: center

Software Project Tutorial
-------------------------


.. note::

   See `rl78g13_software_tutorial_without_applilet3 <https://wiki.analog.com/rl78g13_software_tutorial_without_applilet3>`_


Renesas RL78G14 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Renesas RL78G14 platform using the PmodACL2.

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G14 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g14-yrdkrl78g14-demonstration-kit-rl78g14>`_
-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_
-  The ADXL362 demonstration project for the Renesas RL78G14 platform.

.. note::

   The ADXL362 demonstration project for the Renesas RL78G14 platform consists of three parts: the ADXL362 Driver, the PmodACL2 Demo for RL78G14 and the RL78G14 Common Drivers.

   
   All three parts have to be downloaded.


Hardware Setup
--------------

A PmodACL2 has to be connected to the PMOD1 connector (see image below).

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g14.jpg
   :align: center

Reference Project Overview
--------------------------

The reference project:

-  displays the acceleration values on x, y and z axis;
-  displays temperature;
-  detects any activity or inactivity supported by the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g14_screen.jpg
   :align: center

Software Project Tutorial
-------------------------


.. note::

   See `rl78g14_software_tutorial <https://wiki.analog.com/rl78g14_software_tutorial>`_


Renesas RX63N Quick Start Guide
===============================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Renesas RX63N platform.

Required Hardware
-----------------

-  `Renesas Demo Kit for RX63N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx63n-yrdkrx63n-demonstration-kit-rx63n>`_
-  PmodACL2

Required Software
-----------------

-  `High-performance Embedded Workshop for RX63N family <https://www.renesas.com/us/en/software-tool/high-performance-embedded-workshop>`_
-  `Renesas Peripheral Driver Library for RX63N family <https://www.renesas.com/us/en/software-tool/renesas-peripheral-driver-library>`_

Hardware Setup
--------------

A PmodACL2 has to be connected to the PMOD1 connector.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rx63n.jpg
   :align: center

Reference Project Overview
--------------------------

The reference project continuously displays on the LCD the accelerations on x-axis, y-axis and x-axis and simultaneously detects any activity or inactivity detected by the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rx63n_screen.jpg
   :align: center

Software Project Setup
----------------------


.. note::

   See `rx63n_software_design <https://wiki.analog.com/rx63n_software_design>`_


More information
================

-  :ez:`ask questions about the Microcontroller no-OS Drivers <community/linux-device-drivers/microcontroller-no-os-drivers>`
-  Example questions:

|//ez.analog.com/community/feeds/allcontent/atom|

.. |//ez.analog.com/community/feeds/allcontent/atom| image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom

