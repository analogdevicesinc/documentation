EV-DNG-RFMOD-9001Z User Guide
=============================

Introduction
------------

EV-DNG-RFMOD-9001Z provides an easy interface between the RF module (Lexiwave module which contains ADuCM3029 and ADF7023) and the PC, enabling the user to readily access all the peripherals and GPIOs on the RF module. The RF module can either be soldered down to the EV-DNG-RFMOD-9001Z USB Dongle through the castellations or it can be connected through hirose connector. A variety of modules like Lexiwave, Tessera, SG6T and Smartmesh modules can be connected through hirose as the standard pin layout is maintained for all the RF modules in COG ecosystem. The rapid 6LoWPAN module (Lexiwave module) is currently soldered down to the Dongle.

Hardware
--------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dongle_1.png
   :width: 600px

High level block diagram
------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/block_diagram_2.png
   :width: 600px

Features
--------

-  Lexiwave module is soldered down to the dongle by default
-  There is also a provision to assemble hirose and use a different module like SG6T, Smartmesh module
-  There is also an option to program and debug the module using TAG Connect
-  One of the channels of FTDI chip can be used as both I2C and UART1 as per the requirements with very minimal jumper changes

Interfaces
----------

On EV-DNG-RFMOD-9001Z, FTDI chip, FT4232H is present. It provides four channels to interface with PC. Multi Protocol Synchronous Serial Engine (MPSSE) is present in channel A and channel B of FT4232H through which any serial communication interface can be emulated. The channel details are as given below:

-  SPI lines are connected to channel A. There is a criss-cross provision provided between MOSI and MISO of SPI0 for future use.
-  Channel B is used to interface with I2C. I2C lines are pulled up by default. There is also a provision to connect UART1 lines to channel B in case we need this option in the future. (Remove R25, R27 and populate R26, R28)
-  Channel C is used to interface GPIOs and RESET, BOOT pins.

   -  CDBUS2 – RESET_N
   -  CDBUS3 – BOOT0
   -  CDBUS4 – SYS_WAKE3/TMR2_OUT/GPIO33
   -  CDBUS5 – GP0
   -  CDBUS6 – GP1

-  Channel D is interfaced with UART0 of the module

Test points
-----------

For quick debugging purpose when hirose connector option is being used, following test points are provided,

-  TP1 : Pin 17
-  TP2 : Pin 25
-  TP3 : Pin 15
-  TP4 : Pin 18
-  TP5 : Pin 20

EV-DNG-RFMOD-9001Z Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. admonition:: Download
   :class: download

   `EV-DNG-RFMOD-9001Z Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ev-dng-rfmod-9001z.pdf>`_

   | `EV-DNG-RFMOD-9001Z Layout and BOM <https://wiki.analog.com/_media/resources/eval/user-guides/ev-dng-rfmod-9001z_-_fab.zip>`_
   | `EV-DNG-RFMOD-9001Z assembly <https://wiki.analog.com/_media/resources/eval/user-guides/ev-dng-rfmod-9001z_-_assembly.zip>`_


:doc:`Back </wiki-migration/resources/eval/user-guides/rapidnet-ip>`
