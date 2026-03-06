:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/hwsetup>`

ADSP-215xx/ADSP-SC5xx Hardware Setup
====================================

Requirements
------------

The following are the list of hardware components required for setting up the demo application.

-  ADSP-21569/ADSP-SC573/ADSP-SC584/ADSP-SC589 EZ-Board, EV-21568/EV-21569/21593/SC594/SC598 SOM Boards with carrier board and ADSP-SC589 MINI BOARD. ADSP-21573/ADSP-21584 processor mounted on ADSP-SC573/ADSP-SC584 EZ-BOARD.
-  PC/Laptop with a stereo audio out and USB port.
-  ADZS-ICE-2000/ICE-1000 emulator for downloading/debugging/flashing the framework to the Target.
-  EVAL-ADUSB2EBZ USB to SPI converter.
-  Aardvark I2C/SPI Host Adapter
-  Audio cables and USB cables.

| 
| =====Setup===== The SigmaStudio+ demonstration setup for ADSP-SC5xx/ADSP-215xx includes a Host PC running SigmaStudio+ which is connected to the ADSP-SC573/ADSP-SC584/ADSP-SC589/ADSP-21584/ADSP-21573/ADSP-21569 EZ-Board or ADSP-21568/ADSP-21569/ADSP-21593/ADSP-SC594/ADSP-SC598 EV-SOM with carrier board. The connection is achieved using a USB-to-SPI converter. The EVAL-ADUSB2EBZ or Aardvark I2C/SPI acts as the USB-to-SPI converter, which is connected to the PC through a USB port and to the Target EZ-Board through SPI lines. The basic steps to set up the Target for SigmaStudio+ demonstration is given below. The setup required to run the demo application is illustrated in below figure.
| |image1|
| =====Connections=====

-  `adsp-sc584_ez-board <https://wiki.analog.com/adsp-sc584_ez-board>`__
-  `adsp-sc589_ez-board <https://wiki.analog.com/adsp-sc589_ez-board>`__
-  `adsp-sc573_ez-board <https://wiki.analog.com/adsp-sc573_ez-board>`__
-  `adsp-21569_ez-board <https://wiki.analog.com/adsp-21569_ez-board>`__
-  `adsp-sc589_mini_board <https://wiki.analog.com/adsp-sc589_mini_board>`__
-  `ev-21568-som <https://wiki.analog.com/ev-21568-som>`__
-  `ev-21569-som <https://wiki.analog.com/ev-21569-som>`__
-  `ev-21593-som <https://wiki.analog.com/ev-21593-som>`__
-  `ev-sc594-som <https://wiki.analog.com/ev-sc594-som>`__
-  `ev-sc598-som <https://wiki.analog.com/ev-sc598-som>`__

| 
| ===Connect EZ-BOARD to PC using USBi=== Connect EVAL-ADUSB2EBZ to the PC running SigmaStudio+ using a USB cable. The EVAL-ADUSB2EBZ (hereafter referred to as the ‘USBi’) has a 10-pin socket. This socket should be connected to the header P2 (marked SIGMASTUDIO) on EZ-BOARD and P3 on EV-SOM carrier board. When connected, Pin 1 of the USBi socket should match pin 1 of header P2 on the EZ-BOARD or Pin 1 of the USBi socket match pin 1 of header P3 on the EV-SOM carrier board (The first letter S in "SIGMA STUDIO" port name points to pin 1). This connection is used to download SigmaStudio+ packets from host PC to the EZ-BOARD.
| The USBi to EZ-board connection (direction) is different across different EZ-Boards for example ADSP-SC589 EZ-KIT. Please refer to figures in above links on how to connect to the specific EZ-Board.
| === Connect EZ-Board to PC using Aardvark I2C/SPI Host Adapter === Connect Aardvark I2C/SPI Host Adapter to the PC running SigmaStudio+ using a USB cable. Aardvark I2C/SPI Host Adapter has a 10-pin socket. This socket should be connected to the header P2 (marked SIGMASTUDIO) on EZ-BOARD. When connected, Pin 1 of the USBi socket should match pin 1 of header P2 on the EZ-BOARD. For EV-SOM Pin 1 of the USBi socket match pin 1 of header P3 on the EV-SOM carrier board (The first letter S in "SIGMA STUDIO" port name points to pin 1). This connection is used to download SigmaStudio packets from host PC to the EZ-BOARD.
| The Aardvark to EZ-board connection (direction) is different across different EZ-Boards for example ADSP-SC589 EZ-KIT. Please refer to figures in above links on how to connect to the specific EZ-Board
| === Connect to PC using ICE-2000/ICE-1000 === Connect ADZS-ICE-2000/ICE-1000 to the PC running SigmaStudio using a USB cable. In case of ADZS-ICE-2000, the ribbon cable of ICE-2000 should be connected to header P1 (marked DEBUG) on EZ-BOARD. In case of ICE-1000, connect header J2 of ICE-1000 directly to header P1 (marked DEBUG) on EZ-BOARD. For ADSP-215xx/ADSP-SC59x EV-SOM board, the ADZS-ICE-2000 or ADZS-ICE-1000 can be connected using the ribbon cable, should be connected to header P1. For ADSP-SC598 EV-SOM board, the ADZS-ICE-2000 or ADZS-ICE-1000 can be connected using the ribbon cable, should be connected to header P6. For ADSP-21568 EV-SOM-CRR EZ-Lite, the ADZS-ICE-2000 or ADZS-ICE-1000 can be connected using the ribbon cable, should be connected to header P2. This connection is used to download/debug/flash the framework to the target.
| === Connect Audio Input and Output === Connect an analog audio source and headphones/speakers to the audio ports on the EZ-BOARD.
| === Connect Power to the EZ-BOARD === Connect the power and reset the board by pressing the ‘RESET’ button on the EZ-BOARD.
| =====Switch/Jumper/Port Settings=====

-  `adsp-sc584_ez-board <https://wiki.analog.com/adsp-sc584_ez-board>`__
-  `adsp-sc589_ez-board <https://wiki.analog.com/adsp-sc589_ez-board>`__
-  `adsp-sc573_ez-board <https://wiki.analog.com/adsp-sc573_ez-board>`__
-  `adsp-21569_ez-board <https://wiki.analog.com/adsp-21569_ez-board>`__
-  `adsp-sc589_mini_board <https://wiki.analog.com/adsp-sc589_mini_board>`__
-  `ev-21568-som <https://wiki.analog.com/ev-21568-som>`__
-  `ev-21569-som <https://wiki.analog.com/ev-21569-som>`__
-  `ev-21593-som <https://wiki.analog.com/ev-21593-som>`__
-  `ev-sc594-som <https://wiki.analog.com/ev-sc594-som>`__
-  `ev-sc598-som <https://wiki.analog.com/ev-sc598-som>`__

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/gettingstarted/hardwaresetup.jpg
   :width: 600px
