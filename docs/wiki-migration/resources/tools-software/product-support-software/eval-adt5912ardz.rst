EVAL-AD590-ARDZ Mbed Example
============================

The EVAL-AD590-ARDZ Mbed example software can be used as a starting point for developing your own code for Analog Devices EVAL-AD590-ARDZ board in your own environment utilizing the benefits of the Mbed platform. Analog Devices is an MBED Partner and develops code on the platform for multiple products. The Analog Devices Mbed code-repo can be found in the links below.

This guide will focus on the Analog Devices :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` controller board, as it is directly compatible with the EVAL-AD590-ARDZ evaluation board and is an MBED-Enabled device. Customers are of course, not limited to using the SDP-K1 board for code development, given that any ARM-based, MBED-enabled board that satisfies a small set of requirements can use the provided code and it will work with only minor changes to the source (see below).

It is further assumed that SDP-K1 board will be connected to the appropriate AD590 eval-board such as the :adi:`EV-TempSense-ARDZ Evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EV-TempSense-ARDZ.html#eb-overview>` which has the LTC2488 (SPI) built in with the ability to connect external sensor via headers on the board.

Useful Links
============

`Online Compiler Mbed <https://ide.mbed.com/compiler>`__

`SDP-K1 on Mbed <https://os.mbed.com/platforms/SDP_K1/>`__

`ADI's code on Mbed <https://os.mbed.com/teams/AnalogDevices/code/>`__

EVAL-AD590-ARDZ Mbed Software
=============================

For developing firmware code for controller boards on the Mbed platform visit the link below.

`EV-TempSense-ARDZ code on Mbed <https://os.mbed.com/teams/AnalogDevices/code/EVAL-TempSense-ARDZ/>`__

Introduction
============

At this time Analog Devices supports Mbed code development only on the Mbed online-compiler. See here for instructions on setting up an account and using the compiler. Analog Devices may, at a later date support other offline-IDE's. This guide focuses on the SDP-K1, connected to the EVAL-ADT5912-ARDZ board, but it should be general enough to cover any compatible controller board (the controller board should be Mbed-enabled, and expose at least SPI or I2C and some GPIO's).

The software described below allows for an Mbed enabled controller board to be connected with an Analog Devices evaluation board. Unmodified, the code will communicate over any serial terminal emulator (CoolTerm, putty, etc) using the UART provided by the controller board over USB.

The software provides a basic user-interface for interacting with temperature sensors on the evaluation-board. All the main functionality of the ADT5912 and AD590 is provided in the application-code in abstracted form and the user is free to customize the software to suit their own needs for working with the sensors

Quick Start
===========

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail.

-  Connect the evaluation-board to the Mbed-enabled controller board using the SDP-120 or Arduino connector. ( Switch the P8 Jumper accordingly).
-  Connect the controller board to your computer over USB. ( Make sure that the VIO_ADJUST is set to 3.3 volts)
-  Go to the code for this product in the Mbed compiler.
-  Ensure your controller board is selected (top right of online-compiler page)
-  Edit LTC288_user_config.h to (defaults to SDP connector)
-  Enable the SDP-120 Header if you are not using the Arduino connector. Do this by uncommenting #define SDP-120 in LTC288_user_config.
-  Compile the code.
-  After a successful compile a binary will be downloaded to your computer - store this somewhere.
-  Drag and drop this binary to the USB drive hosted by your controller board.
-  Start up a terminal emulator,

   -  Find the com-port your controller board is connected on and select it.
   -  Set the baud-rate for 115200 - other defaults should be fine.
   -  Reset the controller board and connect.

-  Use the menu provided over the terminal window to access the evaluation board.

User Guide
==========

Getting Started
---------------

The SDP-K1 board has two ways to connect to the EVAL-ADT5912-ARDZ board, it can use the 120-pin SDP connector on the underside of the board, or the Arduino connector can be used.

The Getting Started with `Mbed page <https://os.mbed.com/platforms/SDP_K1/#getting-started-with-mbed>`__ describes the Arduino Uno Header, the SDP connector, pin-outs and other information related to understanding the SDP-K1 controller board.

Hardware Setup
--------------

Connecting the EVAL-ADT5912-ARDZ evaluation board using the SDP connector on the K1 is the simplest and most convenient way to get up and running quickly, simply mate the two boards to together.

.. important::

   If using the Arduino header pins, compile the software only after uncommenting the #define SDP-120 in ltc2488_user_config.h


.. important::

   The P8 Jumper position can be switched between ARD_5V and SDP_5V according to the connector in use


|image1| |image2|

Connecting Remote Sensors
~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-ADT5912-ARDZ board supports remote AD590 and ADT5912 through the P6 and P7 3-position wire to Board terminal block located at the top of the eval board. Incase of ADT5912 remote sensor, the middle pin should be left floating, while connecting to the other pins, as shown in the image below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/remote_sensor_connection.jpg
   :align: center
   :width: 600px

There is no need to adjust the source code to start using the remote sensors. Selecting these devices can be done within the provided application which is described below.

Compiling and flashing firmware
-------------------------------

ARM provide a guide to setting-up and using their online-compiler `here <https://os.mbed.com/docs/mbed-os/v5.12/quick-start/online-with-the-online-compiler.html>`__. For the SDP-K1 the following `guide <https://os.mbed.com/platforms/SDP_K1/>`__ can also be used to help understand the process. Specifically for the EVAL-ADT5912-ARDZ evaluation board and the SDP-K1, the following steps can be used.

Go here to find the EV-TempSense-ARDZ firmware example.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`EV-TempSense-ARDZ <https://os.mbed.com/teams/AnalogDevices/code/EVAL-TempSense-ARDZ/>`__

-  Connect your controller board to your computer - your mbed-enabled board will show as a USB drive.
-  Import into your online compiler workspace by clicking the Import into Compiler button.
-  Select the newly imported program, and select your controller board (e.g. SDP-K1) - see the links above if this process is new to you.
-  Click the compile button
-  When compile is completed a .bin file will be downloaded to your system.
-  Drag and drop the binary file to your USB drive, this will flash the binary to your board.

Using the Software
------------------

The firmware is delivered as a basic, text-based user-interface that operates through a UART on the controller board using the same USB cable that is used to flash the firmware to the boards. Any terminal-emulator should work, but it is not possible for Analog Devices to test every one. It is necessary to connect a serial terminal-emulator to interact with the running firmware.

Here `TeraTerm <https://osdn.net/projects/ttssh2/wiki/TeraTerm>`__ is used as an example, Analog Devices does not endorse any particular program for this, but TeraTerm works well and is made freely available, other terminals such as CoolTerm, or PuTTY will work.


|image3|

Set the baud-rate for 115200, configure the console terminal settings as shown in the picture above and select the connected controller board’s COM port. If using TeraTerm, you should be able to keep the defaults, however adjustments may need to be made to how carriage return (CR) is handled in order for everything to display correctly.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/teraterm_console_menu.jpg
   :align: center
   :width: 600px

The software is designed to be straight forward to use, and requires little explanation. Simply select which sensor you would like to use, whether you want to use the internal sensor or a remote one and then simply enter a number corresponding to the required command and follow the on-screen prompts. The code is also written with a view to keeping things simple, you do not have to be a coding-ninja to understand and expand upon the delivered functions.

It is hoped that the most features of the AD5912 and ADAD590 are coded, but it's likely that some special functionality is not implemented.

.. tip::

   Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc. My test.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/arduino_connection.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/sdp_120_connection.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/teraterm_configuration.jpg
   :width: 600px
