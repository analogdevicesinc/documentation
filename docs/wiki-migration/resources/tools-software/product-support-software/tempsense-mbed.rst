EV-TempSense-ARDZ Console Application
=====================================

The EV-Tempsense-ARDZ Mbed support software can be used as a starting point for developing your own code for Analog Devices EV-TempSense-ARDZ board in your own environment utilizing the benefits of the Mbed platform. Analog Devices is an MBED Partner and develops code on the platform for multiple products. The Analog Devices Mbed code-repo can be found in the links below.

This guide will focus on the Analog Devices SDP-K1 controller board, as it is directly compatible with the TempSense evaluation board and is an MBED-Enabled device. Customers are of course, not limited to using the SDP-K1 board for code development, given that any ARM-based, MBED-enabled board that satisfies a small set of requirements can use the provided code and it will work with only minor changes to the source (see below).

It is further assumed that SDP-K1 board will be connected to the appropriate ADT74XX/ADT73XX eval-board such as the :adi:`EV-TempSense-ARDZ Evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EV-TempSense-ARDZ.html#eb-overview>` which has the ADT7320 (SPI) and ADT7420 (I2C) built in with the ability to connect external sensor via headers on the board.

Useful links
============

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :adi:`ADT7420 <en/products/adt7420.html>`
-  :adi:`ADT7320 <en/products/adt7420.html>`

EV-TempSense-ARDZ Mbed Software
===============================

For developing firmware code for controller boards on the Mbed platform go the link below.

`EV-TempSense-ARDZ code on Mbed <https://os.mbed.com/teams/AnalogDevices/code/EVAL-TempSense-ARDZ/>`__

Introduction
============

At this time Analog Devices supports Mbed code development only on the Mbed online-compiler. See here for instructions on setting up an account and using the compiler. Analog Devices may, at a later date support other offline-IDE's. This guide focuses on the SDP-K1, connected to the EV-Tempsense-ARDZ board, but it should be general enough to cover any compatible controller board (the controller board should be Mbed-enabled, and expose at least SPI or I2C and some GPIO's).

The software described below allows for an Mbed enabled controller board to be connected with an Analog Devices evaluation board. Unmodified, the code will communicate over any serial terminal emulator (CoolTerm, putty, etc) using the UART provided by the controller board over USB.

The software provides a basic user-interface for interacting with the evaluation-board. All the main functionality of the ADT73XX (SPI) and ADT74XX (I2C) is provided in the application-code in abstracted form and the user is free to customize the software to suit their own needs for working with the sensors

Quick Start
===========

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail.

-  Connect the evaluation-board to the Mbed-enabled controller board.
-  Connect the controller board to your computer over USB.
-  Go to the code for this product in the Mbed compiler.
-  Ensure your controller board is selected (top right of online-compiler page)
-  Edit app_config.h to (defaults to SDP connector)

   -  Enable the Arduino Header if you are not using the SDP connector. Do this by uncommenting #define ARDUINO in app_config.h

-  Compile the code.
-  After a successful compile a binary will be downloaded to your computer - store this somewhere.
-  Drag and drop this binary to the USB drive hosted by your controller board.
-  Start up a terminal emulator,

   -  Find the com-port your controller board is connected on and select it.
   -  Set the baud-rate for 230400 - other defaults should be fine.
   -  Reset the controller board and connect.

-  Use the menu provided over the terminal window to access the evaluation board.

User Guide
==========

Getting Started
---------------

The SDP-K1 board has two ways to connect to the EVAL-TempSense-ARDZ board, it can use the 120-pin SDP connector on the underside of the board, or the Arduino connector can be used.

The Getting Started with `Mbed page <https://os.mbed.com/platforms/SDP_K1/#getting-started-with-mbed>`__ describes the Arduino Uno Header, the SDP connector, pin-outs and other information related to understanding the SDP-K1 controller board.

Hardware Setup
--------------

Connecting the EV-TempSense evaluation board using the SDP connector on the K1 is the simplest and most convenient way to get up and running quickly, simply mate the two boards to together.

.. important::

   If using the Arduino header pins, compile the software only after uncommenting the #define ARDUINO in app_config.h


Connecting Remote Sensors
~~~~~~~~~~~~~~~~~~~~~~~~~

The EV-TempSense-ARDZ board supports remote ADT74XX and ADT73XX devices. These can be connected to pins at the top of the eval board using ribbon cables or jumper wires, these pins are marked in the image below. SPI devices (EVAL-ADT7320-MBZ) and I2C devices (EV-ADT7420-MBZ) connect to their respective header pins by matching the pins on the board to those labelled on the remote board.

|image1| |image2|

There is no need to adjust the source code to start using the remote sensors. Selecting these devices can be done within the provided application which is described below.

AD717x Mbed Firmware
--------------------

This section briefs on the usage of MBED firmware. This also explains the steps to compile and build the application using mbed and *make* based build.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`__
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   


-  Connect your controller board to your computer - your mbed-enabled board will show as a USB drive.
-  Import into your online compiler workspace by clicking the Import into Compiler button.
-  Select the newly imported program, and select your controller board (e.g. SDP-K1) - see the links above if this process is new to you.
-  Click the compile button
-  When compile is completed a .bin file will be downloaded to your system.
-  Drag and drop the binary file to your USB drive, this will flash the binary to your board.

Using the Software
------------------

The firmware is delivered as a basic, text-based user-interface that operates through a UART on the controller board using the same USB cable that is used to flash the firmware to the boards. Any terminal-emulator should work, but it is not possible for Analog Devices to test every one. It is necessary to connect a serial terminal-emulator to interact with the running firmware.

Here `CoolTerm <https://freeware.the-meiers.org/>`__ is used as an example, Analog Devices does not endorse any particular program for this, but CoolTerm works well and is made freely available, other terminals such as Tera Term, or PuTTY will work.

Set the baud-rate for 115200 and select the connected controller board’s COM port. If using CoolTerm you should be able to keep the defaults, however adjustments may need to be made to how carriage return (CR) is handled in order for everything to display correctly.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/tempsense_cooltermsetup.png
   :align: center
   :width: 400px

The software is designed to be straight forward to use, and requires little explanation. Simply select which interface (SPI/I2C) you would like to use, whether you want to use the internal sensor or a remote one and then simply enter a number corresponding to the required command and follow the on-screen prompts. The code is also written with a view to keeping things simple, you do not have to be a coding-ninja to understand and expand upon the delivered functions.

It is hoped that the most features of the ADT73XX and ADT74XX are coded, but it's likely that some special functionality is not implemented.

.. tip::

   Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc. My test.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/externalpins.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/remotepins.png
   :width: 400px
