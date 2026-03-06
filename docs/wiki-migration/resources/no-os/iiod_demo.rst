IIOD demo
=========

IIOD demo is a standard example, provided in most no-OS projects, that launches a IIOD server on the board so that the user may connect to it via an IIO client. Using **iio-oscilloscope**, the user can configure the DAC and view the ADC data on a plot.

To build the IIOD demo, add the following flag when invoking make which will build the IIOD server and the IIO section of the driver.

::

   make IIOD=y

To run the IIOD demo, first connect to the board via UART to see the runtime output messages with the following settings:

::

   Baud Rate: 115200bps
   Data: 8 bit
   Parity: None
   Stop bits: 1 bit
   Flow Control: none

Please note that for proper message display, you may need to convert all LF characters to CRLF, if your serial terminal supports it.

With a serial terminal correctly configured and listening to incoming messages, launch the application (``make run`` or click the debug button in your SDK). Runtime messages specific to the application will apear on your serial terminal screen, and eventually the following message is printed:

::

   Running IIOD server...
   If successful, you may connect an IIO client application by:
   1. Disconnecting the serial terminal you use to view this message.
   2. Connecting the IIO client application using the serial backend configured as shown:
       Baudrate: 921600
       Data size: 8 bits
       Parity: none
       Stop bits: 1
       Flow control: none

This message implies a IIOD server is being run and you may connect to it using a serial-backend enabled `iio-oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope>`__ and with the settings indicated at the serial terminal.
