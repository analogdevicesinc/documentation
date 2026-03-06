nanoDAC+ Console Application
============================

Introduction
------------

Analog Devices :adi:`nanoDAC+® <en/products/landing-pages/001/cu_over_analog_devices_introduces_nanodac_family.html>` products are low power, single-channel, 16-/14-/12-bit buffered voltage output DACs. This page gives an overview of using the nanodac+® firmware example with :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` EVAL board, interfacing with various EVAL boards supporting nanodac+ family devices. The firmware example comprises 3 layers of software (from top to bottom): Console Application Layer, Device No-OS Layer and Platform Drivers (Mbed-OS) layer.


|image1|

The application layer uses the ADI Console Libraries to create console based User Interactive (UI). The middle layer of No-OS device library have device specific APIs to interface with nanodac+ device. These APIs allows direct access to device register map in order to read/write device registers. The bottom layer of Platform Drivers is responsible for Low Level Interface. The platform drivers uses mbed-os libraries to access low level peripheral (like GPIOs, SPI, I2C, etc). The devices from nanodac+ family uses either SPI or I2C communication interface.

The nanoDac+ Mbed firmware example can be used as a starting point for developing your own code for Analog Devices nanoDAC+ products in your own environment utilizing the benefits of the Mbed platform. The Mbed Platform simplifies the overall software development process by providing the low level driver support. This reduces the hardware dependency as any Mbed enabled board can be used with same firmware with little modifications (precisely changing a pin mapping).

Interface Diagram
-----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_interface_diagram.jpg
   :align: center
   :width: 600px

The :adi:`AD568xRSDZ(nanodac+)-EVAL <media/en/technical-documentation/user-guides/EVAL-AD5686RSDZ_UG-725.pdf>` board is connected to SDP-K1 through on-board default 120-pin SDP Connector. The nanodac+ EVAL board can be powered-up through a SDP-K1 USB supply or from external DC supply, depending on the power supply jumper settings. The settings can vary board to board and user must refer user manual of respective EVAL board for ensuring the proper connections. Apart from power supply selection option, the EVAL board does provide an options to select Vref level, Gain level, I2C slave address bits-2:1 (A0,A1 pins) and other options based on the EVAL board hardware configurations. The SDP-K1 is connected to PC through an USB cable. The firmware (binary executable) can be loaded into SDP-K1 board through this USB interface from the PC. The SDP-K1 acts as a Serial Device (UART) and firmware loaded into it interacts with any serial terminal (like Teraterm, Putty, Coolterm, etc) by configuring terminal for proper serial settings (COM Port, Baud Rate, data bits, etc).

*\*Note:The firmware provides a basic user-interface for interacting with the evaluation-board. All the main functionality of the nanoDAC+ is provided in the application-code in abstracted form and the user is free to customize the software to suit their own needs for working with the nanoDAC+ This firmware can support the following members of the nanoDAC+ family:*

:adi:`AD5671R <en/products/ad5671r.html>` :adi:`AD5672R <en/products/ad5672r.html>` AD5673R :adi:`AD5674 <en/products/ad5674.html>` :adi:`AD5674R <en/products/ad5674r.html>` :adi:`AD5675R <en/products/ad5675r.html>` :adi:`AD5676 <en/products/ad5676.html>` :adi:`AD5676R <en/products/ad5676r.html>` AD5677R :adi:`AD5679 <en/products/ad5679.html>` :adi:`AD5679R <en/products/ad5679r.html>` :adi:`AD5686 <en/products/ad5686.html>` :adi:`AD5684R <en/products/ad5684r.html>` :adi:`AD5685R <en/products/ad5685r.html>` :adi:`AD5686R <en/products/ad5686r.html>` :adi:`AD5687 <en/products/ad5687.html>` :adi:`AD5687R <en/products/ad5687r.html>` :adi:`AD5689 <en/products/ad5689.html>` :adi:`AD5689R <en/products/ad5689r.html>` :adi:`AD5697R <en/products/ad5697r.html>` :adi:`AD5694 <en/products/ad5694.html>` :adi:`AD5694R <en/products/ad5694r.html>` :adi:`AD5695R <en/products/ad5695r.html>` :adi:`AD5696 <en/products/ad5696.html>` :adi:`AD5696R <en/products/ad5696r.html>` :adi:`AD5681R <en/products/ad5681r.html>` :adi:`AD5682R <en/products/ad5682r.html>` :adi:`AD5683R <en/products/ad5683r.html>` :adi:`AD5683 <en/products/ad5683.html>` :adi:`AD5691R <en/products/ad5691r.html>` :adi:`AD5692R <en/products/ad5692r.html>` :adi:`AD5693R <en/products/ad5693r.html>` :adi:`AD5693 <en/products/ad5693.html>`

Useful links
============

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :doc:`nanoDAC+ No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/ad5676>`
-  :doc:`nanoDAC+ IIO DAC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`

Hardware Connections
--------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_hardware_connection.jpg
   :align: center
   :width: 400px

SDP-K1-
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

EVAL-AD56x86RSDZ Board (AD5696R chip)-
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect REF connector to 2.5V position for Vref=2.5V.
-  Connect PWRSEL connector to USB_SUPP position to power-up device from the SDP-K1 USB.
-  Disconnect/Open the P1 jumper to open the connection of VDD and VLOGIC. Use this option when using the SDP board.

*<fc #cd5c5c>*Note: The settings can vary board to board and user must refer user manual of respective EVAL board for ensuring the proper connections.</fc>*

SDP-K1 is powered through USB connection from the PC. SDP-K1 acts as a Serial device when connected to PC, which creates a COM Port to connect to Serial Terminals like Teraterm, Putty, etc. The COM port assigned to a device can be seen through the device manager for windows based OS.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/com_port_sdp-k1.jpg
   :align: center
   :width: 300px

nanoDAC+ Mbed Firmware
----------------------

This section briefs on the usage of MBED firmware. This also explains the steps to compile and build the application using mbed and *make* based build.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`__
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   


The software execution sequence for the nanodac+ Firmware Example is shown below. This is a blocking application as it waits for user input over serial interface (UART). The input is scanned and processed through 'adi console libraries'. The menu functionality is executed from nanodac_conole_app.c file. The application layer talks with No-OS layer for device registers and data access. The No-OS layer interfaces with Platform Drivers layer for accessing low level peripherals. As name suggests, this layer is platform dependent. nanodac+ firmware uses Mbed libraries within Platform Drivers layer.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_software_sequence.jpg
   :align: center
   :width: 800px

Quick Start
===========

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail:

-  Connect the nanodac+ EVAL-board to the SDP-K1 controller board.
-  Connect the SDP-K1 controller board to your computer over USB.
-  Go to the link of the code provided above in the 'Downloads' section and import code into Mbed online compiler (Edit app_config.h file (defaults to SDP connector and AD5686R device) if evaluating any other device).
-  Ensure SDP-K1 controller board is selected (top right of online-compiler page).
-  Compile the code.
-  After a successful compile a binary will be downloaded to your computer - store this on your drive.
-  Drag and drop this binary to the USB drive hosted by your controller board.
-  Start up a serial terminal emulator (e.g. Tera Term)

   -  Find the com-port your controller board is connected on and select it.
   -  Set the baud-rate for 230400
   -  Reset the controller board and connect.

-  Use the menu provided over the terminal window to access the evaluation board.

Using the Firmware
------------------

The nanodac+ firmware example is configured to have following serial settings:

-  Baud rate: 230400
-  Data bits: 8-bits
-  Parity: None
-  Stop bits: 1

Configure your serial terminal (`Tera Term <https://osdn.net/projects/ttssh2/releases/>`__) for below settings:

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/baud_rate_update.png
   :align: center
   :width: 700px

The nanodac+ console main menu looks like below (with Tera Term):


|image2|

The firmware is designed to be intuitive to use, and requires little explanation, simply enter a number corresponding to the required command and follow the on-screen prompts.

.. tip::

   It is hoped that the most common functions of the nanoDAC+ family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.


The firmware comes with an app_config.h file which (at the moment) serves two purposes.

-  Select the active device to test.
-  Configure the pins you want to use to connect the controller board to the evaluation board.

The firmware supports most products in nanoDAC+ family, change the #define DEV_ADxxxxx found in app_config.h to suit your selected device. The products supported are enumerated in the ad5686_type, which is an enum found in AD5686.h, the firmware defaults to the AD5686R device.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_software_layers.jpg
   :width: 250px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_console_menu.jpg
   :width: 600px
