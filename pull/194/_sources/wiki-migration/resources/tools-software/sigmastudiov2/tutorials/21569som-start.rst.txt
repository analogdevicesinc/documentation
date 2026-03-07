:doc:`Return to previous page </wiki-migration/resources/tools-software/sigmastudiov2/tutorials>`

Getting Started with the ADSP-21569-SOM
=======================================

Overview
--------

There are several options for developing SigmaStudio+ projects with the ADSP21569 This example will use the ADSP-21569 SOM processor board and the EV-SOMCRR-EZKit carrier board

Outline of Steps for Getting Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(see also installation documentation on previous pages)

-  Install SigmaStudio+ (the audio system graphical development environment)
-  Install CrossCore Embedded Studio (CCES) tools

   -  CCES is used for compiling and linking SHARC code
   -  CCES tools will be invoked (behind the scenes) by SigmaStudio+ to build the SHARC code

-  Obtain and set up the hardware to use for your system

   -  for example: Processor System On Module (SOM) plus a base board to plug the SOM onto (carrier board). The carrier board (like the EV-SOMCRR-EZKIT) - this pair of boards is shown below
   -  the EVAL-ADUSB2EBZ USB-to-I2C/SPI commincations adapter (also referred to as the USBi) - SPI communications is used for the SigmaStudio+ to SHARC programming and tuning

::

         {{:resources:tools-software:sigmastudiov2:tutorials:usbi.jpg?600|}}

Hardware for this Example
~~~~~~~~~~~~~~~~~~~~~~~~~

-  the SOM module used here is a Rev E with Rev 0.2 ADSP-21569 silicon (also tested with Rev B SOM and 0.0 silicon)
-  the EV-SOMCRR-EZKit carrier board is a Rev D (the version shown in the previous setup pages is a Rev A)

   -  (the version shown in the previous setup pages is a Rev A)
   -  Note: the USBi header is flipped 180 degrees from the Rev A to the Rev D board (Rev A also uses an unshrouded header for the USBi connection at P3)

-  the SOM module plugs onto the carrier board

   -  the SOM module is powered from the carrier board - Install a jumper on pins 2-3 of JP1 of the SOM module (towards the "POWER" label, this will select power from the carrier base board

-  assorted cables and power supply for the processor/carrier board

   -  3.5mm stereo audio cables for connecting the the EZKIT carrier board
   -  a mini USB cable for connecting the USBi to the PC
   -  a micro USB cable to connect to the SOM (only used for initial loader file flashing). note the usb connector on the processor SOM may be different for other SOM boards

.. important::

   Before the SOM/carrier can be used with SigmaStudio+, the SOM's flash memory must be programmed (see steps below)


Setup the SOM and EzKit Carrier
-------------------------------

Here is a picture of the 21569 SOM installed on the EV-SOMCRR-EZKIT carrier board


|image1|

.. note::

   Don't worry about the state of the LEDs at this point if you have not already programmed the loader (.ldr) file. Instructions for programming the loader file follow this section


-  JP1 power to SOM should be on pins 2-3 (toward the POWER label)
-  Boot Select switch should be on position 1 (SPI2 master boot) – this is after you have programmed the flash with the loader (.ldr file)

   -  it is recommended to program the flash with the CrossCore serial flash programmer as I think it is much easier

-  Power with 12V wall wart or 12V supply (supplied adapter is 1.6A)
-  USBi dongle (for connection to the PC) for SigmaStudio+ programming and tuning

   -  tested with USBi version 1.3, 1.4, and 1.5

-  Connect and audio source to ADC 1-2
-  Connect a powered speaker (or headphones) (can also use the headphones jack)
-  LEDs 4 and 6 should light (with the modified ldr file), they will be off with the original ldr file supplied with the default installation of SigmaStudio+ for Sharc release 2.4.0
-  LED 8 and 9 will come on at startup/powerup and then LED 10 will light with a successful compile and download from SigmaStudio+

.. note::

   SW1 dip switches originally are all ON (default with a new board) – this selects the on-board debugger. If using an ICE-1000 or ICE-2000, they all should be turned OFF (direction shown by arrow)


Programming the Loader File
---------------------------

At this point we are assuming that the hardware is set up and ready to program the loader file.

.. note::

   A modified loader file is provided here that can be used in place of the default loader if desired


This is the modified loader file: `ss_app_21569_leds <https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/ss_app_21569_leds_.zip>`_

-  The modified loader file lights LEDs 4 and 6 on the SOM to show that the processor has booted and is running the loader file from flash
-  Download and extract the .ldr file if desired.

Steps to Program the Loader File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Download and Install the CrossCore Serial Flash Programmer utility

   -  this is part of the CrssCore Utilites software package
   -  :adi:`Serial Flash Programming Utility <en/resources/evaluation-hardware-and-software/embedded-development-software/crosscore-utilities.html#software-overview>`

-  Run the Serial Flash Programmer from Windows

   -


   |image2|

-  set the SOM boot mode switch to "3" (this puts the processor into UART boot mode), (don't power the carrier board yet)
-  You should see a screen similar to this:

   -


   |image3|

-  power up the EzKit carrier board (with the SOM USB cable NOT connected)
-  reset the board (either SW2 RESET pushbutton on the carrier board or the small SW2 RESET on the SOM)
-  To determine which serial port is used for programming, we start without the USB programming cable attached to the SOM. Note which COMM ports are shown in the Serial Port (B) fields:

   -


   |image4|

-  Plug the USB micro cable into the processor SOM (for the 21569 SOM, this is labeled P2 UART) (Note: other SOMs may have a different USB connector). If the programming port was detected, then it will now be shown in the dropdown list of Serial Ports (B)
-  Select the COMM port that was added when the cable was plugged in
-  Set the "Target" (A) to "ADSP-21569 SOM"
-  Set the "Baudrate" (C) to 115200
-  Set the "Action" (D) to Program
-  Set the "File to download" (E) to the desired .ldr file using the Browse button
-  Press "Start" (F) to program the SPI flash device on the SOM
-  The Status window will show the Download, Erase and Programming cycles and will respond with "Flash Completed"
-  At this point, the programming USB cable can be disconnected from P2
-  Change the Boot Mode rotary selector to "1" (SPI flash boot) and power cycle or reset the board

   -  if using the "modified" loader file, LEDs 4 and 6 will be on and LED 7 will be off
   -  the board is now ready for connection to SigmaStudio+
   -  programming the loader only needs to be done once (unless you want to change the framework/loader file for some reason)

-  connect the USBi USB-to-SPI communications board to P3 (if not already attached). The RED power LED should be on and the YELLOW SPI LED should be on (solid).

Test with SigmaStudio+
----------------------

At this point we are ready to run and audio project from SigmaStudio+

-  launch SigmaStudioPlus (SS+) from windows

   -  you can select preferences like light mode vs dark mode, etc

-  download and unzip an example project (available from: :doc:`Tutorials and Examples </wiki-migration/resources/tools-software/sigmastudiov2/tutorials>`)

   -  for example: `adsp-21569_example.zip <https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/adsp-21569_example.zip>`_

-  open the .ssprj project file from the **File** menu. The example project should open and you should see the audio "schematic" - something like:

   -


   |image5|

-  The USBi Firmware Version **must** be correctly set to match the USBi Revision being used! (from the **System** tab)

   -


   |image6|

-  execute the **Link-Compile-Download** operation (from the **Action** menu, or from the taskbar button)
-  after the schematic compilation and download, you should see the message: "Schematic Downloaded Sucessfully" and then the "**ACTIVE**" status should be set on the right side of the status bar at the bottom of the window
-  in the default example, the current audio project can be **"Tuned"**

   -  set the Gain (dB) of the Sine Tone to -12 (or lower), turn on the Sine Tone with the switch
   -  turn on the (Single Band) level meters located just before the outputs, you should see the signal change with the Sine Tone being turned on and off
   -  likewise you can turn the White Noise source on and off and observe the level change
   -  if speakers are connected, you will hear the audio outputs on DAC outputs 1 and 2 (and also at the headphonse jacks)
   -  once the level meters (or other similar blocks) are enabled, the USBi **SPI LED** will flash rapidly to indicate the SPI transfers between SS+ and the hardware

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/21569som-ezkit.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/cces-serial-programmer.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/serialprog1.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/serialprog3.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/ss_screen1.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/ss_usbi.jpg
   :width: 600px
