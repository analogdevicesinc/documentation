AD5770R Console Application
===========================

Supported Device
----------------

-  :adi:`AD5770R`

Introduction
------------

The :adi:`AD5770R` is a 6-channel, 14-bit resolution, low noise, programmable current output digital-to-analog converter (DAC) for photonics control applications. This chip incorporates a 1.25 V on-chip voltage reference, a 2.5 kΩ precision resistor for reference current generation, die temperature, output monitoring functions, fault alarm, and reset functions.

The :adi:`AD5770R` contains five 14-bit resolution current sourcing DAC channels and one 14-bit resolution current sourcing/ sinking DAC channel.

Channel 0 can be configured to sink up to 60 mA and source up to 300 mA. Channel 1 to Channel 5 have multiple, programmable output current sourcing ranges, set by register access. Each DAC can operate with a wide power supply rail from 0.8 V to AVDD − 0.4 V for optimizing power efficiency and thermal power dissipation.

This page describes the AD5770R firmware example running on the :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` controller board, interfacing with the AD5770R evaluation board. The firmware example comprises 3 layers of software, built on top of the Mbed OS.

-  Console Application - uses the ADI console libraries to provide a basic terminal UI
-  AD5770R No-OS Driver - AD5770R device C API
-  Mbed Platform Drivers - Hardware Abstraction Layer (SPI, GPIO, ...) to adapt No-OS driver to Mbed OS

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r/software_layers.jpg
   :align: center
   :width: 400px

The AD5770R Mbed firmware example can be used as a starting point for developing your own code in your own environment utilizing the benefits of the Mbed platform. The Mbed Platform simplifies the overall software development process by providing a common low level driver abstraction. This reduces the hardware dependency as any Mbed enabled board can be used with same firmware with little to no modifications, usually just changing the pin mapping.

Useful links
============

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :doc:`AD5770R No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/ad5770r>`
-  :doc:`AD5770R IIO DAC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5770r>`
-  :adi:`AD5770R Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5770R.html>`

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r/hardware_setup.jpg
   :align: center
   :width: 400px

The :adi:`AD5770R Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5770R.html>` is connected to SDP-K1 using the 120-pin SDP Connector. The evaluation board must be powered externally, typically using an external 3.3V DC supply connected to the AVDD input supply terminal, if using the default power supply jumper settings.

The SDP-K1 is connected to a PC through a USB cable. The firmware image, a .BIN file created using the online mbed compiler, can be loaded into SDP-K1 board by copying the .BIN file to the drive representing the SDP-K1. The SDP-K1 provides a USB to Serial link (UART) and any serial terminal (such as Teraterm, Putty, Coolterm, etc) can be used to connect to by configuring terminal with the necessary settings (serial port, baud rate, data bits, etc).

.. important::

   Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V


The default jumper configuration of the evaluation board selects a diode dummy load on all of the output channels. Refer to the evaluation board user guide for the jumper configuration necessary to route the output current to the screw terminal.

AD5770R Mbed Firmware
---------------------

This section briefs on the usage of MBED firmware. This also explains the steps to compile and build the application using mbed and *make* based build.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`__
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   


Quick Start
===========

If you are familiar with the Mbed platform, the following is a basic list of steps required to start running the code:

-  Connect the evaluation board to the SDP-K1 controller board, and power it appropriately, usually 3.3V to AVDD.
-  Connect the SDP-K1 controller board to your computer over USB.
-  Go to the link of the code provided above in the 'Source Code' section and import the code into the Mbed online compiler
-  Ensure the SDP-K1 controller board is selected as the target

   -  *If a different controller board is being used, then it should be selected, and the pin out in app_config.h may also need to be updated.*

-  In the Mbed Online IDE compile the code.
-  After a successful compile a binary file (.BIN) will be downloaded to your computer.
-  Drag and drop this binary to the USB drive corresponding to the SDP-K1 controller board.
-  Start up a serial terminal emulator (e.g. Tera Term)

   -  Find the com-port your controller board is connected on and select it.
   -  Set the baud-rate for 230400 baud, 8 data, no parity, 1 stop bit.
   -  Reset the controller board and connect.

-  The terminal windows should display the console menu providing access to the AD5770R functionality.

Firmware in Detail
------------------

The example source code is made available from Mbed, and can be imported into the online Mbed compiler and compiled there, entirely in a web browser. The example is menu driven, providing keyboard shortcuts to access/execute the menus items, and prompting for further inputs where necessary. When the example runs, it attempts to connect and initialize the AD5770R. The configuration used is defined in the ad5770r_user_config.h file, which can be modified as needs be to suit specific applications.

*Note: While much of the functionality of the AD5770R No-OS driver is made available through the console UI, not all function are available. The additional AD5770R functionality can only be configured the ad5770r_user_config.c file.*

Main Menu
~~~~~~~~~

The AD5770R Console App main menu provides basic initialization/reset type functions, and access to several sub-menus that provide more detailed configuration and control settings. Like most menus in the firmware, the menu options are framed by a header and footer that display status information related to the functions on the menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r/main_menu.jpg
   :align: center
   :width: 400px

The value of the scratchpad register is displayed in both the header and the footer. After reading the scratchpad value for the header, the value is incremented and written back to the device, such that the scratchpad footer value should always be equal to the header value + 1. This can be useful a debug aid to confirm communications.

DAC Operations
~~~~~~~~~~~~~~

This menu provides the ability to set the Input and DAC register values, and control the update of the DAC using both the hardware and software LDAC functions. The ordering of menu items is intended to follow the order in which actions are typically performed by the user.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r/dac_operations.jpg
   :align: center
   :width: 400px

There are three ways in which the DAC output may be controlled using this menu.

-  Write to Input Channel(s), set software LDAC shadow value, then write software LDAC to update DAC output
-  Write to Input Channel(s), toggle hardware LDAC
-  Write to DAC Channel to directly update DAC output

Toggling a channel in the software LDAC shadow sets a bit corresponding to that channel in a mask. This SW LDAC Channel shadow value can then be written in a single transaction, transferring the input to the DAC value for all of the channels which are set in the shadow mask.

The channels affected by the hardware LDAC pin toggling are set in the ad5770r_user_config.h file at compile time.

.. note::

   The toggling of the hardware LDAC is outside of the AD5770R No-OS driver, and as such the DAC values are not updated by this action.


.. tip::

   For support on this firmware example and No-OS drivers please go to :adi:`Engineer-Zone <engineerzone>`.

