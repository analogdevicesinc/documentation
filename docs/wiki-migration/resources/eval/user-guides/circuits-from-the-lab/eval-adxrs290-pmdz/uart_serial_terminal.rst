Outputting Data
===============

A serial terminal is an application that runs on a PC or laptop that is used to display data and interact with a connected device (including many of the Circuits from the Lab reference designs). The device's UART peripheral is most often connected to a UART to USB interface IC, which appears as a traditional COM port on the host PC/ laptop. (Traditionally, the device's UART port would have been connected to an RS-232 line driver / receiver and connected to the PC via a 9-pin or 25-pin serial port.) There are many open-source applications, and while there are many choices, typically we use one of the following:

-  `Tera Term <https://ttssh2.osdn.jp/index.html.en>`__
-  `Putty <https://www.putty.org/>`__
-  `Real Term <https://realterm.sourceforge.io/>`__

Before continuing, please make sure you download and install one of the above programs.

There are several parameters on all serial terminal programs that must be setup properly in order for the PC and the connected device to communicate. Below are the common settings that must match on both the PC side and the connected UART device.

#. **COM Port** - This is the physical connection made to your PC or Laptop, typically made through a USB cable but can be any serial communications cable. You can determine the COM port assigned to your device by visiting the device manager on your computer. Another method for identifying which COM port is associated with a USB-based device is to look at which COM ports are present before plugging in your device, then plug in your device, and look for a new COM port.
#. **Baud Rate** - This is the speed at which data is being transferred from the connected device to your PC. These parameters must be the same on both devices or data will be corrupted. The default setting for most of the reference designs in 115200.
#. **Data Bits** - The number of data bits per transfer. Typically UART transmits ASCII codes back to the serial port so by default this is almost always set to 8-Bits.
#. **Stop Bits** - The number of "stop" conditions per transmission. This usually set to 1, but can be set to 2 for redundancy.
#. **Parity** - Is a way to check for errors during the UART transmission. Unless otherwise specified, set parity to "none".
#. **Flow Control** - Is a way to ensure that data lose between fast and slow devices on the same UART bus are not lost during transmission. This is typically not implemented in a simple system, and unless otherwise specified, set to "none".

In many instances there are other options that each of the different serial terminal applications provide, such as **local line echo** or **local line editing**, and features like this can be turned on or off depending on your preferences. This setup guide will not go over all the options of each tool, but just the minor features that will make it easier to read back data from the connected devices.

**Example setup using Putty**

#. Plug in your connected device using a USB cable or other serial cable.
#. Wait for the device driver of the connected device to install on your PC or Laptop.
#. Open your device manager, and find out which COM port was assigned to your device.\

|image1|

#. Open up your serial terminal program (Putty for this example)
#. Click on the serial configuration tab or window, and input the settings to match the requirements of your connected device. The default baud rate for most of the reference designs is 115200. Make sure that you use the correct baud rate for your application.\

|image2|

#. Ensure you click on the checkboxes for **Implicit CR in every LF** and **Implicit LF in every CF**.
#. Ensure that local echo and line editing are enabled, so that you can see what you type and are able to correct mistakes. (Some devices may echo typed characters - if so, you will see each typed character twice. If this happens, turn off local echo.)\

|image3|

#. Click on the open button, and as long as your connected device and serial terminal program are setup the same, than you should see data displaying.

.. tip::

   Hint: If you see nothing in the serial terminal, try hitting the reset button on the embedded development board.


.. |image1| image:: https://wiki.analog.com/_media/wiki/device_manager.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/wiki/putty_serial_config.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/wiki/putty_terminal_options.png
   :width: 400px

   |image1|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/example_serial_output.png
   :width: 600px
