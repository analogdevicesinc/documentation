User Guide for AD74115H Software
================================

Copyright, Disclaimer Statements

Copyright Information
---------------------

Copyright (c) 2022 Analog Devices, Inc. All Rights Reserved. This software is proprietary and confidential to Analog Devices, Inc. and its licensors. This document may not be reproduced in any form without prior, express written consent from Analog Devices, Inc.

Disclaimer
----------

Analog Devices, Inc. reserves the right to change this product without prior notice. Information furnished by Analog Devices is believed to be accurate and reliable. However, no responsibility is assumed by Analog Devices for its use; nor for any infringement of patents or other rights of third parties which may result from its use. No license is granted by implication or otherwise under the patent rights of Analog Devices, Inc.

Description
~~~~~~~~~~~

This document explains how to use standalone software drivers to evaluate AD74115H hardware on top of Raspberry pi 4. It is possible to port this driver to any other platform, this is done by implementing the HAL API to the new hardware platform. As all hardware accesses are done through the HAL and the HAL definition supports all the hardware features required by the driver, the HAL is the only component that changes between platforms.

Hardware Setup
~~~~~~~~~~~~~~

Raspberrypi4 and Arduino Shield can be used to test hart modem drivers with the help of HART stack (master/slave).

-  Raspberry pi 4 is used to run the HART stack (master/slave).
-  Arduino shield is used as a bridge between raspberry pi board and AD74115H HART modem.
-  AD74115H HART modem (DUT).
-  Another HART modem (DUT) to for HART network where one device can send requests and other device can respond.

Figure 1 below shows what hardware is used to set up HART modem.

.. image:: https://wiki.analog.com/_media/hart_1.png
   :alt: hart_1.png

// Figure 1: Hardware Required to Set Up HART Modem //

As demonstrated in figure 2 below, connect HART modem to Raspberry pi board with the help of Arduino Shield. Establish all required connections to Raspberry pi such as display, power, ethernet to PC, mouse, keyboard, etc...

Connect loop power to HART modem power terminal plug and HART slave/master to I/O EXTx terminal plug. Make sure terminal polarities are not miss matched.

.. image:: https://wiki.analog.com/_media/hart_2.png
   :alt: hart_2.png

// Figure 2: All the Hardware Connected //

Driver Architecture
~~~~~~~~~~~~~~~~~~~

Figure 3 below shows different levels of HART architecture.

.. image:: https://wiki.analog.com/_media/driver_architecture.png
   :alt: driver_architecture.png

// Figure 3: HART Driver Architecture //

\* Low level drivers.

-   Drivers for the peripherals used (SPI, GPIO, LED, etc).

-   Typically provided by the software support package of the host processor Ex: bcm2835 Library.

-   Users need to download from web.

\* HAL.

-   Abstraction of the low drivers API to a generic

API for the common tasks required from the hardware peripherals.

-   Read/write HART frames over SPI interface.

\* High level driver.

-   Exposes a platform-agnostic API to the user.

-   Uses the HAL API exclusively to access the hardware.

Configuration of AD74115H in RPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Device Reset: Toggle the RESETb pin for a second at the start-up

2. Clear the ALERT_STATUS register. Write 0x7FFF to the ALERT_STATUS register.

3. Blink the LED for 1s Toggle GPIOA so that the green LED on the evaluation board blinks. This is done as a diagnostic step to ensure that the GPIO peripherals and SPI is correctly configured and working.

4. Configuration for HART: Configure the HART peripheral to make the ALERTb pin go low when one character byte is received in the Rx FIFO.

|hart_table.png| // Table 1 //

5. Read any junk data that is left in the RX FIFO. After the configuring the HART in the previous step, the ALERTb pin goes low. There is some junk data on the Rx FIFO, which will be read. Once there is no data in the Rx FIFO the ALERTb pin goes high. Now, the configuration is complete.

Set up for Receiving the Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There may be multiple threads that are running in the program such as Transmit thread, receive thread etc. The Receive thread, continuously monitor the status of the ALERTb pin. The ALERTb pin is configured to only go low when more than one byte of data is received. When the ALERTb pin goes low, the data byte is read. Then send the data to the above layer for further processing. The ALERTb pin goes HIGH once the data is cleared from the Rx FIFO.

Example Code
~~~~~~~~~~~~

Install BCM2835 package on redberry-pi4, it is one time set-up:

1. Install Raspi-config: http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/

2. Open terminal, sudo raspi-config->interfacting option->enable spi

3. Install BCM2835 package.

a. Go to http://www.airspayce.com/mikem/bcm2835/index.html

b. Download and install the package.

4. Download VS code, install C++ Microsoft extension from market place. The ‘AD74115H_main.c’ file implies how to use the driver with an example. It performs below steps.

• Initializes resbery-pi4 board and initialize GPIOs

• Configures AD74115H modem by following the steps mentioned in section 4.

• Initiates HART command 1 and read response message

• Then continuously read if there is any RX data in HART network for every 1000us

.. |hart_table.png| image:: https://wiki.analog.com/_media/hart_table.png
