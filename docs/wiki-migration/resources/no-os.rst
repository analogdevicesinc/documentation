no-OS overview
==============

no-OS is a software framework by Analog Devices Inc for systems without OS, otherwise known as baremetal. This framework defines a common interface (API) for accessing typical baremetal peripherals such as GPIO, SPI, I2C, RTC, Timer, Interrupt Controller. This common API may be then used to initialize and control these peripherals in a common way across multiple microcontroller platforms. Currently supported platforms are Intel and Xilinx microprocessors and SoC's as well as Analog Devices' own precision microcontrollers, several Maxim Integrated MAX32xxx microcontrollers, STMicroelectronics' STM32, Raspberry Pi's Pico, and mbedOS supported devices.

By using this common driver API, the no-OS is able to provide reference projects for Analog Devices Inc evaluation boards running on various underlying hardware.

Thanks to the no-OS build system, no-OS users may generate standalone reference projects and use them as starting point for their own development.

no-OS is an open-source software, and its official repository is :git-no-OS>`__. You are free to use and distribute no-OS, provided that you comply with the `license <https::`no-OS Github Repository </github.com/analogdevicesinc/no-OS/blob/master/LICENSE>`.

Drivers and Projects
--------------------

-  :doc:`no-OS drivers </wiki-migration/resources/no-os/drivers>`
-  :doc:`no-OS projects </wiki-migration/resources/no-os/projects>`

Documentation
-------------

-  :doc:`no-OS build guide </wiki-migration/resources/no-os/build>`
-  :doc:`no-OS build system </wiki-migration/resources/no-os/make>`
-  :doc:`no-OS API </wiki-migration/resources/no-os/api>`
-  :doc:`no-OS drivers guide </wiki-migration/resources/no-os/drivers-guide>`
-  `no-OS Doxygen <http://analogdevicesinc.github.io/no-OS/>`_
-  :adi:`Understanding and Using the No-OS and Platform Drivers <en/analog-dialogue/articles/understanding-and-using-the-no-os-and-platform-drivers.html>`
