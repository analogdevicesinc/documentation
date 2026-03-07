:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/hwsetup>`

ADAU145x / ADAU146x Hardware Setup
==================================

Requirements
------------

The following are the list of hardware components required for setting up the demo application.

-  EVAL-ADAU1452MINIZ / EVAL-ADAU1466Z / EVAL-ADAU1467Z.
-  PC/Laptop with a stereo audio out and USB port.
-  EVAL-ADUSB2EBZ USB to SPI converter.
-  Aardvark I2C/SPI Host Adapter
-  Audio cables and USB cables.

Setup
-----

| The SigmaStudio+ demonstration setup for ADAU145x and ADAU146x includes a Host PC running SigmaStudio+ which is connected to the evaluation board. The connection is achieved using a USB-to-SPI converter. The EVAL-ADUSB2EBZ or Aardvark I2C/SPI acts as the USB-to-SPI converter, which is connected to the PC through a USB port and to the evaluation board through SPI pins.
| =====Connections=====
| ===Connect EVAL board to PC using USBi=== The EVAL-ADUSB2EBZ (hereafter referred to as the ‘USBi’) has a 10 pin socket. This is connected to SPI CONTROL PORT/CONTROL PORT header on the board.
| === Connect EZ-Board to PC using Aardvark I2C/SPI Host Adapter === Connect Aardvark I2C/SPI Host Adapter to the PC running SigmaStudio using a USB cable. Aardvark I2C/SPI Host Adapter has a 10 pin socket. This is connected to SPI CONTROL PORT/CONTROL PORT header on the board.
| === Connect Audio Input and Output === Connect an analog audio source and headphones/speakers to the audio ports on the EVAL board.
| === Connect Power to the EVAL Board === Connect the power and reset the board by pressing the ‘RESET’ button on the EVAL Board.
