USB Interfaces
==============

| 
| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| SigmaStudio can communicate with hardware in real over a USB connection. DSP Program Data, Register Settings, and Parameter control data is sent to a USB device, converted to either SPI (serial peripheral interface) data or I²C data, and sent to the SigmaDSP hardware. It is also possible to read hardware register values via USB.
| When using an evaluation board with integrated USB connectors, locate the Communication Channel block with the corresponding SigmaDSP part number. For example, EvalBoard170x should be used with the EVAL-ADAU1701EB and EVAL-ADAU1702EB platforms. Connect a USB cable directly to the evaluation hardware and to the PC.
| There are also two generic communication channels available:

-  :doc:`USB Serial Converter (EVAL-ADUSB1) </wiki-migration/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/usbserialconverter>`
-  :doc:`USBi (EVAL-ADUSB2) </wiki-migration/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/usbi>`
-  :doc:`AARDVARK </wiki-migration/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/aardvark>`

See your evaluation hardware's data sheet for more information, www.analog.com/sigmadsp.

--------------

USB Driver Installation:
------------------------

The proper USB drivers must be installed to communicate with SigmaStudio. To setup the USB hardware:

-  Connect the USB cable to your evaluation hardware and to a spare USB port on your PC.
-  The Windows "Found New Hardware Wizard" will launch.
-  Choose “Install from a list or a specific location” and click "Next".
-  Select “Search for the best driver in these locations” and Check the box for “Include this location in the search.”
-  Press the "Browse" button and locate the appropriate driver file in the SigmaStudio application folder (default folder is C:\\Program Files\\Analog Devices Inc\\Sigma Studio\\USB drivers):

   -  For USB serial converter and Eval-Boards (FDTIxx.inf) select ftd2xx.inf file.
   -  For USBi interface select the CyUSB.inf file.

-  Click "Continue Anyway" if you're prompted with "This software has not passed Windows Logo testing."

--------------

To enable USB communication in SigmaStudio:
-------------------------------------------

-  Select the Hardware Configuration Tab.
-  Click the Communication Channels category (at the bottom of the ToolBox window).
-  Select your evaluation board, USBSerialConv or USBi and drag and drop it into the Configuration window.
-  Connect the Communication Channel to the DSP IC processor block(s).

| 
| |usbint1.png|
| The color of the USB label on the communication block indicates if a USB connection has been established. If the USB hardware is properly configured, the background color will be light orange or white. If the communication is not properly initialized the background will be red. Note that this only indicates that a USB connection is active, it does not guarantee communication with the SigmaDSP IC or that the SigmaDSP hardware is properly configured.

| 
| |usbint2.png|

The "Connected" background color is white when all board ICs are connected, and orange when only some ICs are connected, but not all. For example the ADAU1701 evaluation board includes both an ADAU1701 IC and an E2Prom IC. When connecting only the ADAU1701 the background will be light orange, but it will be white when connecting both an ADAU1701 and an E2Prom IC.

.. |usbint1.png| image:: https://wiki.analog.com/_media/../gettingstarted/usbint1.png
.. |usbint2.png| image:: https://wiki.analog.com/_media/../gettingstarted/usbint2.png
