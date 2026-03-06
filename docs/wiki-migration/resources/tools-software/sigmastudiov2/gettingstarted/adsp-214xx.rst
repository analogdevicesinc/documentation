:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/hwsetup>`

ADSP-214xx Hardware Setup
=========================

Requirements
------------

The following are the list of hardware components required for setting up the demo application.

-  ADSP-21489 EZ-KIT Lite.
-  PC/Laptop with a stereo audio out and USB port.
-  ADZS-ICE-2000/ICE-1000 emulator for downloading/debugging/flashing the framework to the Target.
-  EVAL-ADUSB2EBZ USB to SPI converter.
-  ADZS-USBI2EZB is an adapter board used to connect EVAL-ADUSB2EBZ socket to the EZ-KIT Lite.
-  Aardvark I2C/SPI Host Adapter
-  Audio cables and USB cables.

| 
| =====Setup===== The SigmaStudio+ demonstration setup for ADSP-214xx includes a Host PC running SigmaStudio+ which is connected to the ADSP-21489 EZ-KIT Lite. The connection is achieved using a USB-to-SPI converter. The EVAL-ADUSB2EBZ or Aardvark I2C/SPI acts as the USB-to-SPI converter, which is connected to the PC through a USB port and to the Target EZ-KIT Lite through SPI lines using ADZS-USBI2EZB. The basic steps to set up the Target for SigmaStudio+ demonstration are given below.
| =====Connections=====

-  `adsp-21489_ez-kit <https://wiki.analog.com/adsp-21489_ez-kit>`__

| 
| ===Connect EZ-BOARD to PC using USBi=== The EVAL-ADUSB2EBZ (hereafter referred to as the ‘USBi’) has a 10 pin socket and each EZ-KIT has a different header to which the SPI lines connect. Hence an adapter board ADZS-USBI2EZB (hereafter referred to as the ‘adapter board’) is used to connect the USBi socket to the EZ-KIT. The adapter board connects to the primary SPI of the respective EZ-KIT. The USBi should be connected to P1 of the adapter board. When connected, Pin 1 of the USBi socket should match pin 1 of header P1 on the adapter board. LED1 on the adapter board is ON only if the connection is correct.
| === Connect EZ-Board to PC using Aardvark I2C/SPI Host Adapter === Connect Aardvark I2C/SPI Host Adapter to the PC running SigmaStudio using a USB cable. Aardvark I2C/SPI Host Adapter has a 10 pin socket and each EZ-KIT has a different header to which the SPI lines connect. Hence an adapter board ADZS-USBI2EZB (hereafter referred to as the ‘adapter board’) is used to connect the Aardvark socket to the EZ-KIT. The adapter board connects to the primary SPI of the respective EZ-KIT. The Aardvark should be connected to P1 of the adapter board. When connected, Pin 1 of the Aardvark socket should match pin 1 of header P1 on the adapter board. LED1 on the adapter board is ON only if the connection is correct.
| === Connect Audio Input and Output === Connect an analog audio source and headphones/speakers to the audio ports on the EZ-KIT.
| === Connect Power to the EZ-KIT === Connect the power and reset the board by pressing the ‘RESET’ button on the EZ-BOARD.
| =====Switch/Jumper/Port Settings=====

-  `adsp-21489_ez-kit <https://wiki.analog.com/adsp-21489_ez-kit>`__
