LTC268X Console Application
===========================

Introduction
------------

The LTC2686/8 are 8/16-channel, 16-bit, ±15 V digital-to-analog converters (DAC) with an integrated precision reference. The LTC268X Mbed example software can be used as a starting point for developing your own code for Analog Devices DC2873A-B or DC2904A board in your own environment utilizing the benefits of the Mbed platform. This guide will focus interfacing the :adi:`DC2873A-B <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/DC2873A.html>` or :adi:`DC2904A-B <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/DC2904A.html>` evaluation board with Analog Devices :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` controller board or any an MBED-Enabled board.

The firmware example comprises 3 layers of software (from top to bottom): Console Application Layer, Device No-OS Layer and Platform Drivers (Mbed-OS) layer.


|image1|

The application layer uses the ADI Console Libraries to create console-based User Interactive (UI). The middle layer of No-OS device library has device specific APIs to interface with LTC2686/8 devices. These APIs allows direct access to device register map in order to read/write device registers. The bottom layer of Platform Drivers is responsible for Low Level Interface. The platform drivers use mbed-os libraries to access low level peripheral (like GPIOs, SPI, I2C, etc). The devices from LTC2686/8 family use SPI communication interfaces respectively.

At this time Analog Devices supports Mbed code development only on the `Keil Studio Cloud <https://www.keil.arm.com/mbed/>`_. See `here <https://developer.arm.com/documentation/102497/1-5/Prerequisites/Access-Keil-Studio>`_ for instructions on setting up an account and using the Keil Studio. This guide focuses on the SDP-K1, connected to the DC2873A-B or DC2904A-B board, but it should be general enough to cover any compatible controller board (the controller board should be Mbed-enabled, and expose at least SPI or I2C and some GPIO's). The Mbed Platform simplifies the overall software development process by providing the low-level driver support. This reduces the hardware dependency as any Mbed enabled board can be used with same firmware with little modifications (changing a pin mapping).

The software described below allows for an Mbed enabled controller board to be connected with an Analog Devices evaluation board. Unmodified, the code will communicate over any serial terminal emulator (CoolTerm, putty, etc) using the UART provided by the controller board over USB.

Useful Links
============

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :adi:`LTC2686 <en/products/ltc2686.html>`
-  :adi:`LTC2688 <en/products/ltc2688.html>`

Hardware Connection
-------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ltc2688_jumper_connection.jpg
   :alt: ltc2688_jumper_connection.jpg
   :align: right
   :width: 600px

The DC2873A-B/DC2904A-B evaluation board can be connected to the SDP-K1 using jumper wires from the Arduino header to the signal pins available via through-hole headers right beside the J1 connector. Either you can solder header pins on the through-hole mounting area or directly connect wires to them.

The power to the evaluation board should be supplied through the on-board turret connections within the following supply range:

===== ====== ==============
Pin   Turret Voltage Supply
===== ====== ==============
VCC   E31    5V
IOVCC E10    3.3V
V1+   E1     5V - 21V
V2+   E14    5V - 21V
V-    E3     -21V - 0
GND   E2     GND
===== ====== ==============

.. important::

   V2+ must be less than or equal to V1+. The VIO_ADJUST jumper on the SDP-K1 board should be on 3.3V position. Remove the jumpers from JP1, JP2, JP3, JP4 for using the board with VIO = 3.3V


The connections to be made between the SDP-K1 and the DC2873A-B/DC2904A-B are as follows:

===================== ================================
SDP-K1 Arduino Header DC2873A-B/DC2904A-B Through-Hole
===================== ================================
SCLK/D13              SCK
MISO/D12              SDO
MOSI/D11              SDI
CS/D10                CS
GND                   GND
===================== ================================

Interface Diagram
-----------------

|image2| The DC2873A-B/DC2904A-B evaluation board is connected to SDP-K1 using the Arduino Headers and jumper wires. The DC2873A-B/DC2904A-B evaluation board VCC and IOVCC can be powered-up through a SDP-K1 USB supply or from external DC supply using the turrets connection. The SDP-K1 is connected to PC through an USB cable. The firmware (binary executable) can be loaded into SDP-K1 board through this USB interface from the PC. The SDP-K1 acts as a Serial Device (UART) and firmware loaded into it interacts with any serial terminal (like Teraterm, Putty, Coolterm, etc) by configuring terminal for proper serial settings (COM Port, Baud Rate, data bits, etc).

LTC268X Mbed Firmware
---------------------

For developing firmware code for controller boards on the Mbed platform visit the link below.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   


Quick Start
===========

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail.

-  Connect the evaluation-board to the Mbed-enabled controller board using the Arduino connector and jumper wires.
-  Connect all the power supplies to the evaluation board as instructed in the hardware connection section.
-  Connect the controller board to your computer over USB. (Make sure that the VIO_ADJUST is set to 3.3 volts)
-  Go to the :doc:`link </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>` provided above in the 'Build Guide' section to import and build firmware in Keil Studio. For more details visit this `page <https://developer.arm.com/documentation/102497/1-5/Create-or-import-a-project/Import-an-Mbed-project-from-a-URL>`_
-  Ensure your controller board is selected (top right of online-compiler page)
-  Compile the code.
-  After a successful compile a binary will be downloaded to your computer - store this somewhere.
-  Drag and drop this binary to the USB drive hosted by your controller board.
-  Start up a terminal emulator,

   -  Find the com-port your controller board is connected on and select it.
   -  Set the baud-rate for 230400 - other defaults should be fine.
   -  Reset the controller board and connect.

-  Use the menu provided over the terminal window to access the evaluation board.

Using the Software
------------------

The firmware is delivered as a basic, text-based user-interface that operates through a UART on the controller board using the same USB cable that is used to flash the firmware to the boards. Any terminal-emulator should work, but it is not possible for Analog Devices to test everyone. It is necessary to connect a serial terminal-emulator to interact with the running firmware.

Here `TeraTerm <https://osdn.net/projects/ttssh2/wiki/TeraTerm>`_ is used as an example, Analog Devices does not endorse any particular program for this, but TeraTerm works well and is made freely available, other terminals such as CoolTerm, or PuTTY will work.


|image3|

Set the baud-rate for 230400, configure the console terminal settings as shown in the picture above and select the connected controller board’s COM port. If using TeraTerm, you should be able to keep the defaults, however adjustments may need to be made to how carriage return (CR) is handled in order for everything to display correctly.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ltc2688_main_menu.jpg
   :align: center
   :width: 600px

The software is designed to be straight forward to use and requires little explanation. The main menu provides two options:

-  DAC Configuration: This option lets to configure various DAC parameters such as active channel, span and toggle/dither selection.
-  DAC Data Operation: This option lets you set the output voltage for DAC channels.

It is hoped that the most features of the LTC2686/8 are coded, but it's likely that some special functionality is not implemented.

.. tip::

   Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc. My test.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ltc2688_software_layers.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ltc2688_interface_diagram.jpg
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ltc2688_terminal_size.jpg
   :width: 600px
