AD717x/AD411x Console Application
=================================

Introduction
------------

The :adi:`AD717x <en/products/landing-pages/001/ad717x-family.html>`/:adi:`AD411x <en/products/ad4111.html>` family offer a complete integrated Sigma-Delta ADC solution which can be used in high precision, low noise single channel applications (Life Science measurements) or higher speed multiplexed applications (Factory Automation PLC Input modules). This page gives an overview of using the AD717x/AD411x firmware example with :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` EVAL board, interfacing with various EVAL boards supporting AD711x/AD411x family devices. The firmware example comprises 3 layers of software (from top to bottom): Console Application Layer, Device No-OS Layer and Platform Drivers (Mbed-OS) layer.


|image1|

The application layer uses the ADI Console Libraries to create console based User Interactive (UI). The middle layer of No-OS device library have device specific APIs to interface with AD717x/AD411x device. These APIs allows direct access to device register map in order to read/write device registers. The bottom layer of Platform Drivers is responsible for Low Level Interface. The platform drivers uses mbed-os libraries to access low level peripheral (like GPIOs, SPI, I2C, etc). The devices from AD711x/AD411x family uses SPI communication interface.

The Mbed Platform simplifies the overall software development process by providing the low level driver support. This reduces the hardware dependency as any Mbed enabled board can be used with same firmware with little modifications (precisely changing a pin mapping).

Interface Diagram
-----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_interface_diagram.jpg
   :align: center
   :width: 600px

The :adi:`EVAL-AD411x <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4111.html>`/:adi:`EVAL-AD717x <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7177-2.html>` board is connected to SDP-K1 through on-board default 120-pin SDP Connector. The AD717x/AD411x EVAL boards can be powered-up through a SDP-K1 USB supply or from external DC supply, depending on the power supply jumper settings. The settings can vary board to board and user must refer user manual of respective EVAL board for ensuring the proper connections. The SDP-K1 is connected to PC through an USB cable. The firmware (binary executable) can be loaded into SDP-K1 board through this USB interface from the PC. The SDP-K1 acts as a Serial Device (UART) and firmware loaded into it interacts with any serial terminal (like Teraterm, Putty, Coolterm, etc) by configuring terminal for proper serial settings (COM Port, Baud Rate, data bits, etc).

*\*Note:The firmware provides a basic user-interface for interacting with the evaluation-board. All the main functionality of the AD411x/AD711x is provided in the application-code in abstracted form and the user is free to customize the software to suit their own needs for working with the AD711x/AD411x.*

Useful links
============

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :doc:`AD717x No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/ad717x>`
-  :adi:`AD4111 <en/products/ad4111.html>`
-  :adi:`AD4112 <en/products/ad4112.html>`
-  :adi:`AD4114 <en/products/ad4114.html>`
-  :adi:`AD4115 <en/products/ad4115.html>`
-  :adi:`AD4116 <en/products/ad4116.html>`
-  :adi:`AD7175-2 <en/products/ad7172-2.html>`
-  :adi:`AD7175-8 <en/products/ad7175-8.html>`
-  :adi:`AD7176-2 <en/products/ad7176-2.html>`
-  :adi:`AD7177-2 <en/products/ad7177-2.html>`
-  :adi:`AD7172-2 <en/products/ad7172-2.html>`
-  :adi:`AD7172-4 <en/products/ad7172-4.html>`
-  :adi:`AD7173-8 <en/products/ad7173-8.html>`

Hardware Connections
--------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_hw_connection.jpg
   :align: center
   :width: 500px

SDP-K1-
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

EVAL-AD4111SDZ Board (AD4111/AD4112 chip)-
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect PWR (LK3) connector to USB_SUPP (B) position to power-up device from the SDP-K1 USB.

*<fc #cd5c5c>*Note: The settings can vary board to board and user must refer user manual of respective EVAL board for ensuring the proper connections.</fc>*

SDP-K1 is powered through USB connection from the PC. SDP-K1 acts as a Serial device when connected to PC, which creates a COM Port to connect to Serial Terminals like Teraterm, Putty, etc. The COM port assigned to a device can be seen through the device manager for windows based OS.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/com_port_sdp-k1.jpg
   :align: center
   :width: 300px

AD717x Mbed Firmware
--------------------

This section briefs on the usage of MBED firmware. This also explains the steps to compile and build the application using mbed and *make* based build.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   


The software execution sequence for the AD717x/AD411x Firmware Example is shown below. This is a blocking application as it waits for user input over serial interface (UART). The input is scanned and processed through 'adi console libraries'. The menu functionality is executed from ad717x_conole_app.c file. The application layer talks with No-OS layer for device registers and data access. The No-OS layer interfaces with Platform Drivers layer for accessing low level peripherals. As name suggests, this layer is platform dependent. AD717x/AD411x firmware uses Mbed libraries within Platform Drivers layer.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/sequence_diagram_ad717x.jpg
   :align: center
   :width: 650px

Quick Start
===========

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail:

-  Connect the AD717x/AD411x EVAL-board to the SDP-K1 controller board.
-  Connect the SDP-K1 controller board to your computer over USB.
-  Go to the link of the code provided above in the 'Downloads' section and import code into Mbed online compiler (Edit app_config.h file (defaults to SDP connector and AD4111 device) if evaluating any other device).
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

The AD711x/AD411x firmware example is configured to have following serial settings:

-  Baud rate: 230400
-  Data bits: 8-bits
-  Parity: None
-  Stop bits: 1

Configure your serial terminal (`Tera Term <https://osdn.net/projects/ttssh2/releases/>`_) for below settings:

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/baud_rate_update.png
   :align: center
   :width: 600px

The AD717x/AD411x console main menu looks like below (with Tera Term):


|image2|

The firmware is designed to be intuitive to use, and requires little explanation, simply enter a number corresponding to the required command and follow the on-screen prompts.

.. tip::

   It is hoped that the most common functions of the AD711x/AD411x family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.


The firmware comes with an app_config.h file which (at the moment) serves two purposes.

-  Select the active device to test.
-  Configure the pins you want to use to connect the controller board to the evaluation board.

The firmware supports most products in AD717x/AD411x family, change the #define DEV_ADxxxx found in app_config.h to suit your selected device. e.g. #define DEV_AD7111_2 executes the AD7112-2 device functionality.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_architecture.jpg
   :width: 250px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4111_console_menu.png
   :width: 400px
