:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/supportedplatforms>`

USBi 2.0 (EVAL-A2B-USBi)
========================

The USBi 2.0 (EVAL-A2B-USBi) device is a Analog Devices USB adapter board that aids in communication data from the PC host to the serial input pins of a target platform over SPI, I2C or GPIO. This device is the successor to the original USBi board :adi:`EVAL-ADUSB2EBZ`.

Overview
========

| The USBi 2.0 device supports transmission of SPI or I2C packets from the PC host to the target platfrom connected on the other end of the device. It also enables GPIO write, read and probing interrupts from the target board. The device is supported in :adi:`SigmaStudio+ (SS+) <sigmastudio-plus>` tool from SS+ 2.3.0 version onwards. The SS+ USBi 2.0 plugin programs the device to transmit SS+ application packets over the protocol of choice. The plugin can be used to program DSP or A2B transceiver registers, apply network configurations and download and tune audio schematics.
| The device does not require any external power supply to operate as it is powered over the USB-C cable. The on-board regulators enable both 1.8V and 3.3V IOVDD operation, allowing for increased compatibility with target devices. This can be configured using the switch S2 on the board - Position 1-2 for 1.8V and 2-3 for 3.3V. The device can be used to send data over SPI (to a maximum of three SPI responders), I2C, and GPIO (to control a maximum of four GPIO lines). These functionalities are enabled through two USBi 2.0 Mode configurations, Mode 0 and Mode 1. This mode of operation can be controlled on the board using the switch S1 - Position 1-2 for Mode 0 and 2-3 for Mode 1. More about this is explained in detail using the SigmaStudio+ configuration in the later sections of the page. The device provides a 16-pin connector which exposes all the pins required for different operations. A 16-to-10 pin SigmaStudio adapter can be requested through the ADI field representative to use the device for legacy USBi operations.
| |image1| |image2| |image3|
| |image4|
| ======USBi 2.0 Configuration using SigmaStudio+====== The USBi 2.0 device is supported in :adi:`SigmaStudio+ (SS+) <sigmastudio-plus>` tool from SS+ 2.3.0 version onwards. Users can drag and drop the USBi 2.0 shape from the toolbox under Communication Adapters into the System canvas, visually representing the USBi 2.0 device connected from the PC host to the target platform of choice. The USBi 2.0 plugin can be used to program DSP or A2B transceiver registers, apply network configurations and download and tune audio schematics.
| |usbi2plugin.png|
| =====Introduction===== Each USBi 2.0 device is encoded with a unique part number in its OTP. When the device is connected to the host, SigmaStudio+ recognises the device uniquely through its part number and lists as a separate devices in the combo box of the USBi shape in the canvas. Hence multiple USBi 2.0 devices can be connected to the PC and used in SS+ environment to communicate with various chains of target platforms. When a project with the selected USBi device is opened in SS+, the USB icon on the shape glows blue when the respective device is connected to the PC. When the respective device is disconnected from the PC, the icon on the USBi 2.0 shape ceases to glow blue - this behavior is similar to the existing USBi shape.
|

.. tip::

   \ **USBi 2.0 Drivers** - The USBi device inherently packages an FTDI FT4222H part inside the custom board. Most Windows systems support the FTDI driver by default. But if the user's system does not recognize the part during connection, then please install the drivers from the `FTDI Website <https://ftdichip.com/drivers/d2xx-drivers/>`__.


Context Menu
------------

Apart from general options on the shape, the right-click context menu on the USBi 2.0 shape provides few USBi specific functional options as shown below. These are -

-  **Check Connection** - Checks the connection status of the USBi device. If connected, the USB icon glows blue, else, the icon is dim
-  **Identify Device** - Identifies the connected USBi device with the serial number displayed on the shape by glowing the LED on the board with the color Cyan. This becomes useful to identify multiple USBi boards connected to the PC. Refer the LED section of the USBi 2.0 settings page below for more details.
-  **Reset Device** - Resets the USBi 2.0 hardware device to rediscover its state

| |usbi2contextmenu.png|

Settings Page
-------------

Users can access the USBi settings page by double clicking the shape. The settings page is user friendly with options to easily navigate and search a specific configuration based on users needs. The USBi 2.0 settings are organized into five categories -

-  **General** - Outlines the general USBi device settings.
-  **SPI** - Provides configurations specific to SPI transmissions.
-  **I2C** - Provides configurations specific to I2C transmissions.
-  **GPIO** - Details the GPIO settings and operations.
-  **LEDs** - Provides information and configurations for the USBi 2.0 device LEDs.

| |usbi2settingspage.png|

General
~~~~~~~

The General settings lists configurations that govern the behaviour of the overall device. These include -

-  **EVAL-A2B-USBi Device** - This is an advanced field - it is enabled for the USBi 2.0 devices.
-  **Mode of Operation** - The USBi 2.0 device supports two modes of operation controlled by switch S1 on the board, Mode 0 and Mode 1. In Mode 0, the device allows transmission of data over the SPI protocol to one SPI respnder on the first chip select SPI0, or, over the I2C bus connected to the I2C lines of the connector. The device can transmit the data over one of these protocols at a time. In Mode 1, the device allows data transmission over the SPI protocol to a maximum of three responders, and transmission over the I2C protocol is not supported. Users can write or read (or poll interrupts for) GPIO data over the last two GPIO lines (GPIO 3 and GPIO 4). GPIO 0 and 1 lines are multiplexed with other functionality (refer the pin out diagram) and therefore disabled.
-  **Identify USBi Device** - Triggers identification of the connected USBi device with the serial number displayed on the shape by glowing the LED on the board with the color Cyan. This becomes useful to identify multiple USBi boards connected to the PC. Refer the LED section of the USBi 2.0 settings page below for more details.
-  **Reset USBi Device** - Hardware resets the USBi device
-  **Reset Target Board** - Resets the target platform connected the USBi device on the other end of the 16-pin connector. This is enabled when the GPIO2 line is enabled in the GPIO section of the settings page. The value written on the GPIO line is also determined by the value configured in the GPIO settings - High or Low. To use this feature, the jumper JP3 should be connected on the USBi device. Refer to the device schematic for the same.

| |usbi2settingspagegeneral.png|
| SigmaStudio+ Mode Settings for USBi 2.0 device
| |usbi2mode0.png|
| |usbi2mode1.png|

SPI
~~~

The USBI 2.0 SPI configurations are captured under the SPI section of the settings page. These settings are applicable to the data transmitted to all the SPI responders from the USBi. The settings are categorized as General settings - for general behaviour of the SPI module, and Clock settings - to configure the SPI clock. Currently, a few configurations are masked from user's control and will be made available in the future releases. Users will be able to set the drive strength of the SPI signals, tune the SPI clock based on the system clock and the clock divider, and set the phase and polarity of the clock based on the SPI responder in the target board.

| |usbi2settingspagespi.png|

I2C
~~~

The USBI 2.0 I2C configurations are captured under the I2C section of the settings page. Users can modify the I2C configurations in Mode 0 of operation. In Mode 1, the I2C lines, SCL and SDA are multiplexed with the chip selects of SPI 1 and SPI 2 lines (refer to the 16-pin out diagram) and therefore the I2C is diabled in Mode 1. The settings are categorized as General settings - for general behaviour of the I2C device, and Clock settings - to set the various I2C clock configurations. Currently, a few configurations are masked from user's control and will be made available in the future releases. Users can currently set the I2C clock rate upto 3.4MHz as per the support for I2C responder.

| |image5|

GPIO
~~~~

The USBi 2.0 plugin allows users to write, read or probe four GPIO lines. GPIO 0 and 1 are disabled as the GPIO lines conflict with the I2C lines (refer to the 16-pin out diagram). Each GPIO module can be used to -

-  **Write Data**

   -  Users can write High or Low level to the GPIO line by clicking the **Write** button.
   -  Users can trigger an impulse of High or Low level on the GPIO line through the **Trigger** button. When the Trigger button in the respective GPIO port is pressed, SS+ shall write the value chosen (High/Low) onto the line. When the button is released, the opposite value is written onto the line, thus allowing users to trigger an impulse onto the line.

-  **Read Data/Trigger Interrupts**

   -  Users can read the GPIO line by clicking the **Read** button. The read value will be displayed in the text box next to the read button.
   -  Users can poll the GPIO interrupts for any trigger value - Level high/Low, Rising/Falling edge. Once the trigger type is selected, users can request SS+ to start polling the interrupt by enabling the Read Notification toggle button. Once the interrupt is caught by SS+, the button switches off and the notification bulb next to the read button glows blue.

.. tip::

   The USBi 2.0 plugin provides an option to reset the target platform connected the USBi device. To use this feature, enable the GPIO2 port from the settings page, connect the jumper JP3 on the USBi board (refer to the USBi 2.0 device schematic) and either, write the reset value from the GPIO write section of the GPIO 2 settings, or click the Reset Target Board button from the General settings section of the settings page.


| |usbi2settingspagegpio.png|
| ====LED==== The USBi 2.0 device has an LED embedded inside the platform to notify the on-going USBi operation. The LED transitions from one color to another when the SS+ programs the USBi 2.0 device to perform transactions. Given below are a comprehensive color map and a color transition diagram which explain the LED transitions during different SS+ operations.

-  The LED glows Green when the USBi state is in steady-state or idle or when the device is reset from SS+.
-  When an SPI transaction is processed, the LED glows Blue.
-  When an I2C transaction is processed, the LED glows Cyan.
-  When a GPIO data is writen/read or interrupt polled, the LED glows purple.
-  The LED state does not change unless a transaction of a different protocol is transmitted. For example, if three transactions of SPI, five transactions of I2C and four transactions of SPI are being transmitted from SS+, the LED will toggle from what state it is in, to blue and remain blue for the three transactions of SPI. Then it changes to cyan when the protocol shifts to I2C and remains cyan for all five transactions of I2C, and then turns blue for the last four transactions of SPI. Thus in between these 12 transactions, the LED will only switch at best twice.
-  When the user tries to identify the USBi 2.0 device (either from the context menu or the general settings), the USBi LED glows with an RGB cycle for a brief moment to indicate the USBi chosen.

.. tip::

   The LED functionality of the USBi 2.0 plugin is active only during the Mode 0 operation. This is because SS+ programs the LED module on the USBi device through I2C. Therefore, the LED functionality becomes inactive during Mode 1 of operation.


|

.. tip::

   As mentioned above, in Mode 0 of operation, SS+ programs the LED module over I2C. Thus, this can slightly impact the bandwidth of the transaction stream. If users want to disable the LED functionality in Mode 0, they can disable the LED enable button on the right side of the LED settings page as shown below.


| |usbi2settingspageled.png|
| ====LED Color Transition Diagram==== |ledcolortransitiondiagram.png|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/EVAL-A2B-USBITOP.jpg
   :width: 150px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/EVAL-A2B-USBIANGLE.jpg
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/EVAL-A2B-USBIBOTTOM.jpg
   :width: 150px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/USBi16-PinConnector.png
   :width: 500px
.. |usbi2plugin.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2plugin.png
.. |usbi2contextmenu.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2contextmenu.png
.. |usbi2settingspage.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2settingspage.png
.. |usbi2settingspagegeneral.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2settingspagegeneral.png
.. |usbi2mode0.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2mode0.png
.. |usbi2mode1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2mode1.png
.. |usbi2settingspagespi.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2settingspagespi.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2settingspagei2c.png
   :width: 800px
.. |usbi2settingspagegpio.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2settingspagegpio.png
.. |usbi2settingspageled.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/usbi2settingspageled.png
.. |ledcolortransitiondiagram.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/supportedplatforms/ledcolortransitiondiagram.png
