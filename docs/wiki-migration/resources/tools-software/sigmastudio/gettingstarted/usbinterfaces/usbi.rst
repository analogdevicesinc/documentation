USBi (EVAL-ADUSB2)
==================

| `Click here to return to the USB Interfaces page <https://wiki.analog.com/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces>`_
| The Analog Devices USBi "USB Interface" (EVAL-ADUSB2) board is the interface between your PC's USB port and SigmaDSP hardware's data input pins. This interface can be used with any evaluation board which includes an External SPI/I²C header (Aardvark Header). The EVAL-ADUSB2 board is capable of both SPI and I²C communication (which is user selectable) and can supply IOVDD of either 3.3V or 1.8V.
| The USBi interface is powered from the computer's USB port.

--------------

To Install the USBi Board:
--------------------------

-  Connect the USB cable to the USBi Board a spare USB port on your PC.
-  The Windows "Found New Hardware Wizard" will launch.
-  Choose “Install from a list or a specific location” and click "Next".
-  Select “Search for the best driver in these locations” and Check the box for “Include this location in the search.”
-  Press the "Browse" button and locate the appropriate driver file in the SigmaStudio application folder (default folder is C:\\Program Files\\Analog Devices Inc\\Sigma Studio\\USB drivers): Select the CyUSB.inf file.
-  Click "Continue Anyway" if you're prompted with "This software has not passed Windows Logo testing."

| 
|

.. tip::

   Note: The first time the USBi board drivers are instaledl on a PC, you will be prompted to repeat the above steps a second time, for the "Analog Devices USBi (unloaded)" device. This is normal and occurs because the USBi board's firmware is updated during the first driver installation operation.


--------------

Using USBi in SigmaStudio:
--------------------------

| To communication between SigmaStudio and the USBi board, a communication channel block must be added to the Schematic design. To locate the block, select the Hardware Configuration Tab, int the ToolBox or Tree ToolBox window choose the "Communication Channels" category, and select the USBi block.
| |usbi1.png|
|

.. tip::

   Note: Only one of this block's output pins must be connected. It is not necessary to connect or terminate all of the output pins. Also, you connect a processor to any of the pins, there is no specific requirement for pin connection order.


This block provides connections for multiple processors (ICs / DSPs), allowing you to use multiple processors in a single design. This block allows you to explicitly specify both the communication protocol*\* (SPI or I²C) and the part's address, I²C address or SPI clatch line. The DSP hardware's address must match the block's selected address for communication to function properly. See the parts data sheet for more information about addressing (e.g. ADR_SEL, ADDR0, or ADDR1 pins).

\**The default USBi protocol is I²C, to enable SPI, you must first select an SPI address in the block's drop down menu and then perform three write operations (e.g. press the write button the Register Read/Write Window 3 times). The USBi hardware has LEDs which indicate the current mode, I²C or SPI.

See the EVAL-ADUSB2 data sheet for more information, www.analog.com/sigmadsp.

.. |usbi1.png| image:: https://wiki.analog.com/_media/usbi1.png
