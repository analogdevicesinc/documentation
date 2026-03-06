USB Serial Converter (EVAL-ADUSB1)
==================================

| `Click here to return to the USB Interfaces page <https://wiki.analog.com/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces>`__
|

.. important::

   This article refers to an outdated piece of hardware that is no longer available from Analog Devices. This information is included as a reference for users with pre-2007 evaluation boards.


.. warning::

   The AD1953 is not recommended for new designs. Information related to the AD1953 is included here for reference only.


| The Analog Devices USB Serial Converter (EVAL-ADUSB1) board is the interface between your PC's USB port and the evaluation board control-port connections. In the case of the AD1953, -1954, -1940, and -1941 boards, the USB serial converter connects directly to the DB25 connector on the board.
| The USB adapter is typically powered from the computer's USB port. To use the adapter in standalone mode, power it by connecting +5Vdc and ground to test points TP1 and TP2.

--------------

To Install the USB Serial Converter:
------------------------------------

-  Plug the adapter into the evaluation board's control port (DB25 connector).
-  Connect the USB cable to your PC and to the USB adapter.
-  When prompted for drivers:

   -  **Windows 2000** - Choose “Search for a suitable driver” and click next.
   -  Check “Specify a location” and uncheck the other options. Click Next.

-  **Windows XP** - Choose “Install from a list or a specific location.”

   -  Choose “Search for the best driver in these locations.”

      -  Check the box for “Include this location in the search.”

-  Click Browse and find the ftd2xx.inf file in the USB driver folder in the SigmaStudio installation directory. The default location is C:\\Program Files\\Analog Devices Inc\\SigmaStudio\\USB drivers .
-  In Windows XP, click Continue Anyway if you're presented with a dialog regarding the software not passing Windows Logo testing.

--------------

Using the USB Serial Converter:
-------------------------------

| To communication between SigmaStudio and the USB Serial Converter board, a communication channel block must be added to the Schematic design. To locate these blocks, select the Hardware Configuration Tab and in the ToolBox or Tree ToolBox window choose the "Communication Channels" category.
| |usbpic1.png|
| There are 2 communication channel blocks that can be used with the USB Serial Converter board: USBSerialConv and USBSerialConvAddress. Both blocks offer connections for multiple processors, allowing you to use multiple processors in a single design.

.. tip::

   Note: Only one of the USBSerialConv/USBSerialConvAddress block output pins must be connected. It is not necessary to connect or terminate all of the output pins. Also, you connect the processor to any of the pins, there is no specific requirement for order of pin connection.


USBSerialConv
~~~~~~~~~~~~~

| Allows connection of multiple DSP processors blocks and the E2Prom block. Addresses are assigned sequentially from top to bottom (e.g. SPI communication The pins are associated with clatch0 - 4 from top to bottom).
| |usbpic2.png|
| ===USBSerialConvAddress=== This block allows you to explicitly specify the part addresses, I²C address or SPI clatch line (see below). Note that the DSP hardware's address must match the block's selected address for communication to function. See the parts data sheet for more information about addressing (e.g. ADR_SEL, ADDR0, or ADDR1 pins).
| |usbpic3.png|
| Depending on the SigmaDSP part, connections made to this block will be for either SPI (serial peripheral interface) data or I²C data. For SPI, this channel lets you connect multiple boards at once, with the option of connecting a particular board to any clatch line. (The only exception is clatch1, which is reserved for the converter EPROM, represented on the USBSerialConv block by a grayed pin.) The pins are clatch0 - 4 from top to bottom. The diagram below shows one possible configuration of connecting boards to pins.
| |usbpic4.png|
| --------------------------------------------------------------------------------

EVAL-ADUSB1 board switches and jumpers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  S1 - Load a program saved in flash to the SigmaDSP.
-  S2 - Select which of eight SigmaDSP programs will be loaded when S1 is pressed.
-  S3 - Reset the USB adapter board.
-  TP1 - +5Vdc connection for cases where the adapter isn't powered through the PC's USB port.
-  TP2 - Ground connection for cases where the adapter isn't powered through the PC's USB port.
-  J3 - When a jumper is present on this header, writing is enabled to the flash memory (for storing SigmaDSP programs).
-  D4 - This LED indicates the USB board is powered.

| 
| The SigmaDSP program and parameter files can be saved to flash memory on the USB board using the Flash Downloader tool in SigmaStudio. Each program can be loaded to the SigmaDSP by setting S2 to the appropriate setting and then pressing the program load button, S1. Refer to the Flash Downloader page.
| See the EVAL-ADUSB1 data sheet for more information, analog.com/sigmadsp.

.. |usbpic1.png| image:: https://wiki.analog.com/_media/usbpic1.png
.. |usbpic2.png| image:: https://wiki.analog.com/_media/usbpic2.png
.. |usbpic3.png| image:: https://wiki.analog.com/_media/usbpic3.png
.. |usbpic4.png| image:: https://wiki.analog.com/_media/usbpic4.png
