.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`
| ====== ezLINX Sample PC Application Software User Guide ====== :doc:`ezLINX Sample PC Application Installation Guide </wiki-migration/resources/eval/ezlinx/pcapp-installation-guide>`

:doc:`Isolated USB ethernet gadget network adapter configuration </wiki-migration/resources/eval/ezlinx/usb-ip-config>`

Introduction
============

The *ez*\ LINX *i*\ Coupler Isolated Interface Development Environment provides users with a convenient, cost-effective method of evaluating various isolated communication standards. This significantly reduces design and evaluation time for designers who are using Analog Devices isolated transceivers in their design. The *ez*\ LINX hardware platform contains an Analog Devices ADSP-BF548 processor which runs the open source uCLinux kernel and *ez*\ LINX embedded sample application. A Sample PC Application is also provided, which integrates with the *ez*\ LINX hardware platform via isolated USB, allowing for a complete plug and play evaluation and development experience with 8 isolated communication interfaces:

-  Isolated USB
-  Isolated CAN
-  Isolated RS-485/RS-422
-  Isolated RS-232
-  Isolated I2C
-  Isolated SPI
-  Isolated LVDS

The embedded software application is written in C and the Sample PC Application is written in Microsoft Visual C# and uses version 4 of the Microsoft .NET Framework. The Sample PC Application and embedded software have many features when used together, including the following:

-  Simultaneous data transmission/reception on multiple isolated interfaces
-  User friendly software which can instantly switch between running interfaces
-  View data traffic during current session
-  Interfaces are readily customizable to suit your application
-  Embedded firmware is easily updated through isolated USB
-  Quickly save and load your entire configuration for all communication standards
-  Supports hardware routing of signals between interfaces

The open source nature of both the PC Application and the embedded software allow the user to view and edit the source code of the application to obtain the best use of the ezLINX hardware system for their application. The source code and Sample PC Application can be downloaded :doc:`here </wiki-migration/resources/eval/ezlinx>`.

Main Window
===========

Upon starting the ezLINX Sample PC Application the Main System window is displayed:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig1MainWindow.jpg
   :align: center
   :width: 850px

.. container:: centeralign

   \ *Figure1: Main Window*\


From this window we see a complete overview of the ezLINX hardware system and how it integrates with the ADSP-BF548 processor. The Sample PC Application is designed to easily allow for the simultaneous use and evaluation of multiple communication standards. The application has two sidebars at the left and the right of the main window with seven active buttons allowing access to the different transceiver interfaces. These interfaces can be accessed from any window in the application. The color of these buttons indicates the status of the transceiver, so:

- The **Light Gray** color: the transceiver is deactivated and disconnected.

- The **Steel Blue** color: the transceiver is activated and disconnected.

- The **Royal Blue** color: the transceiver is activated and connected.

The STATUS bar along the bottom of the window shows whether the application is connected to an ezLINX hardware platform, the IP address of that hardware platform, and the transceivers on the hardware which are currently enabled. Clicking on the word STATUS opens the Transceiver Status Window, where you can view the amount of data sent and received by each interface in the current session. The Main Window of the application also has 3 buttons located under the system block diagram:

**- Connect**

The Connect button in the main window serves to establish a connection with the ezLINX hardware board using the current IP address configuration.

\*\*- View Configuration \*\*

The View Configuration button opens the Configuration Window, which displays the complete system configuration of all transceivers on the ezLINX hardware board.

\*\*- Configure \*\*

The Configure button opens the Board Configuration Window to configure the IP address to connect to, change the IP configuration of the connected ezLINX hardware, or apply updates to the embedded software of the ezLINX hardware. The Board Configuration Window can also be accessed at any time by clicking on the image of the ezLINX hardware at the bottom left of the application.

Board Configuration Window
==========================

There are two possibilities to open the Board Configuration Window:

1. By pressing the Configure button, the below window appears:


|image1|

.. container:: centeralign

   \ *Figure 2: Configuration window from Configure button*\


2. By clicking on the image of the ezLINX hardware platform on the bottom left of the application, the below window appears:



|image2|

.. container:: centeralign

   \ *Figure 3: Configuration Window from the ezLINX image*\


The Configuration Window is divided into three boxes:

-

.. container:: em

   Network Features Box


: Modify the network features of the ezLINX hardware platform.



|image3|

.. container:: centeralign

   \ *Figure 4: Network features box*\


\**Connect to IP Address: \*\*

The IP address of the ezLINX hardware platform which the PC Application will connect to when the **Connect** button is pressed.

The default address is 192.168.3.21.

\**Set New Address To: \*\*

Modify the IP address of the connected ezLINX hardware platform. You must check the **Set New Address** To box and connect to a hardware platform to use this and the two functions below.

**New Subnet Mask:**

Specify a new Subnet Mask for the connected ezLINX hardware platform.

**New IP Gateway:**

Specify a new IP Gateway for the connected ezLINX hardware platform.

-

.. container:: em

   Firmware Upgrade Box


: In order to facilitate the update of the embedded software flashed on the ezLINX hardware platform, the application gives this function to easily load newer firmware versions, by using the **Send** button to select the new embedded software version to be loaded to the ezLINX hardware platform.For information on how to perform a firmware update refer to the section on Updating Embedded Firmware later in this guide. The Firmware Upgrade Box also provides the functionality to check the current PC Application software and the embedded firmware versions on the ezLINX hardware platform.



|image4|

.. container:: centeralign

   \ *Figure 5: Firmware Upgrade box*\


\**PC Version: \*\*

The current PC Software Application version.

\**Embedded Version: \*\*

The embedded software version on the ezLINX hardware platform. Click the \*Check\* button to request which version is currently on the hardware platform.

\**DLL Version: \*\*

The current DLL version.

-

.. container:: em

   Enable/Disable Box


:this box can be used to switch any of the transceivers on the ezLINX hardware platform on or off. To enable or disable an interface check the box next to the interface name.



|image5|

.. container:: centeralign

   \ *Figure 6: Enable/Disable box*\


A notification message will be displayed above the checked transceiver indicating that the transceiver is currently enabled. See the following figure:



|image6|

.. container:: centeralign

   \ *Figure 7: Notification message for enabled transceivers*\


Isolated RS-232
===============

The isolated RS-232 interface on the ezLINX development platform is implemented using Analog Devices :adi:`adm3252e` driver/receiver. For more information on the hardware implementation of the RS-232 interface click :doc:`here </wiki-migration/resources/eval/ezlinx/isolated-rs232>`.

RS-232 Configuration Window
---------------------------

To open the RS-232 configuration menu select it from the button on the top right of the Application. This opens the RS-232 Configuration Window:


|image7|

.. container:: centeralign

   \ *Figure 8: RS232 Configuration Window*\


To configure the RS-232 for use, check the **Transceiver Enable** box (seen above). The Transceiver Enable box is present on all the configuration windows, and is used to enable or disable the transceivers on the ezLINX hardware.

The RS-232 Configuration Window is divided into three boxes:

-

.. container:: em

   Interface Settings Box


: To select the appropriate communication interface for RS-232 transceiver.



|image8|

.. container:: centeralign

   \ *Figure 9: Interface settings box*\


Select UART3 from the drop-down interface menu.

-

.. container:: em

   RS-232 Settings Box


: To communicate with ezLINX hardware board through the RS-232 port, you need to configure the device using the following features:



|image9|

.. container:: centeralign

   \ *Figure 10: RS-232 settings box*\


**Baud Rate:**

Select the symbol rate for the RS-232 device. Note that the ADM3251E RS-232 transceiver’s performance is not specified above 460800 Baud.

From the **Baud Rate** drop-down menu, you can select different transmission rate values from: 110 bits/s to 1000000 bits/s

**Parity:**

Select whether to append an even, odd or no parity bit to the end of each word transmitted.

**Stop Bits:**

Select between using one or two stop bits.

**Word Size:**

Select whether the application sends 7 bit words or 8 bit words.

**Flow Control:**

Select whether or not to use flow control. When connected to the ezLINX hardware platform no flow control should be selected.

-

.. container:: em

   RS-232 Routing Box


: The RS-232 interface supports hardware routing to the outputs of other interfaces. To enable hardware routing check the Enable Routing box and select the interface to route to from the drop down menu. To route to RS-485 select UART2 from the drop down menu.



|image10|

.. container:: centeralign

   \ *Figure 11: RS-232 Routing box*\


RS-232 Send/Receive Window
--------------------------

Shown below is the send/receive window for the RS-232 protocol. The window consists of two main sections; a send window on the left and a receive window on the right. To send data from the RS-232 port, type the data to be sent into the left hand text box. Click **Send Data** button to transmit the contents of the text box. Data sent to the RS-232 port will automatically appear in the right hand receive window in real time.


|image11|

.. container:: centeralign

   \ *Figure 12: RS-232 Send/Receive Window*\


There are also a variety of other functions which can be used from this window.

**On/Off buttons:**

Turns the transceiver on or off. When off the RS-232 transceiver is disconnected.

**Send Data:**

Transmit the text contained in the Send box.

**Auto:**

Toggles the Auto setting, which transmits data automatically as you type it in the Send box.

**Load File:**

Opens a load file menu to select a .txt file to send. The contents of the file are automatically sent through the RS – 232 port once loaded.

**Clear:**

Clears the text box.

**Send Data Format:**

Choose whether to send the characters in the text box as HEX or ASCII data.

**Receive Data Format:**

Choose whether to display the received data on the screen as HEX or ACSII characters.

**Save To File:**

Opens a create .txt file window. Once created all received data will be saved to this file.

Click again to toggle the Save To File function.

\**Log To File: \*\*

Opens a create .txt file window. Once created all received data will be logged to this file with a timestamp. Click again to toggle the Log to File function.

To close the Send /Receive Window simply turn the transceiver off and click on a different interface button, or deselect the RS-232 interface button from the sidebar to return to the RS-232 Configuration Window.

Isolated RS – 485 / RS – 422
============================

Both the isolated RS-485 and isolated RS-422 interfaces on the ezLINX development platform were implemented using Analog Devices :adi:`adm2587e` transceiver. For more information on the hardware implementation of the RS-485 / RS-422 interfaces click :doc:`here </wiki-migration/resources/eval/ezlinx/isolated-rs485-rs422>`.

RS-485/ RS-422 Configuration Window
-----------------------------------

In the ezLINX Sample PC Application both the RS-485 and the RS-422 protocols are implemented in the same section. To open this interface menu select it using the button on the top left of the Application. This opens the RS-485 / RS-422 configuration window:


|image12|

.. container:: centeralign

   \ *Figure 13: RS-485 Configuration Window*\


To configure the RS-485/RS-422 for use, check the **Transceiver Enable** box (seen above). The Transceiver Enable box is present on all the configuration windows, and is used to enable or disable the transceivers on the ezLINX hardware.

The RS-485/RS-422 Configuration Window is divided into three boxes:

-

.. container:: em

   Interface Settings Box


: To select the appropriate interface for RS-485 transceiver.



|image13|

.. container:: centeralign

   \ *Figure 14: Interface Settings Box*\


Select UART2 from the drop-down interface menu.

-

.. container:: em

   RS-485 Settings Box


: to communicate with ezLINX hardware board through RS-485 port, you need to configure the device using the following features:



|image14|

.. container:: centeralign

   \ *Figure 15: RS-485 Settings Box*\


**Baud Rate:**

Select the symbol rate for the RS-485 / RS-422 device. Note that the ADM2587E transceiver’s performance is not specified above 500 kBaud. From the “Baud Rate” drop-down menu, you can select different transmission rate values from: 110 bits/s to 1000000 bits/s

**Parity:**

Select whether to append an even, odd or no parity bit to the end of each word transmitted.

**Stop Bits:**

Select between using one or two stop bits.

**Word Size:**

Select whether the application sends 7 bit words or 8 bit words.

**Flow Control:**

Select whether or not to use flow control. When connected to the ezLINX hardware platform no flow control should be selected.

**Duplex:**

Choose between half and full duplex operation. If using half duplex operation jumpers JP3, JP4 and JP40 should be connected on the ezLINX hardware

-

.. container:: em

   RS-485 / RS-422 Routing Box


: The RS-485 / RS-422 interface supports hardware routing to the outputs of other interfaces. To enable hardware routing check the **Enable Routing** box and select the interface to route to from the drop down menu. To route to RS-232 select UART3 from the drop down menu.



|image15|

.. container:: centeralign

   \ *Figure 16: Routing box*\


RS-485 / RS-422 Send/Receive Window
-----------------------------------

Shown below is the transmit/receive window for the RS-485/RS-422 protocol. The window is identical to the RS-232 send/receive window. The left hand text box is used to transmit data via the Send Data button, and the right hand text box is used to receive real time data.


|image16|

.. container:: centeralign

   \ *Figure 17: RS-485/RS-422 Send/Receive Window*\


The following functions are also available:

**On/Off buttons:**

Turns the transceiver on or off. When off the RS-485 / RS -422 transceiver is disconnected.

**Send Data:**

Transmit the text contained in the Send box.

**Auto:**

Toggles the Auto setting, which transmits data automatically as you type it in the Send box.

**Load File:**

Opens a load file menu to select a .txt file to send. The contents of the file are automatically sent through the RS-485 / RS-422 port once loaded.

**Clear:**

Clears the text box.

**Send Data Format:**

Choose whether to send the characters in the text box as HEX or ASCII data.

**Receive Data Format:**

Choose whether to display the received data on the screen as HEX or ACSII characters.

**Save To File:**

Opens a create .txt file window. Once created all received data will be saved to this file.

Click again to toggle the Save To File function.

\**Log To File: \*\*

Opens a create .txt file window. Once created all received data will be logged to this file with a timestamp. Click again to toggle the Log to File function.

To close the Send/Receive window simply turn the transceiver off and click on a different interface button, or deselect the RS-485/RS-422 interface button from the sidebar to return to the RS—485/RS-422 Configuration Window.

Isolated I2C
============

The isolated Inter-Integrated Circuit (I2C) interface on the ezLINX development platform is implemented using Analog Devices :adi:`adum1250` and :adi:`adum5000`. For more information on the I2C hardware implementation click :doc:`here </wiki-migration/resources/eval/ezlinx/isolated-i2c>`.

I2C Configuration Window
------------------------

To open the I2C interface select it from the left hand sidebar. This will open the I2C configuration window:


|image17|

.. container:: centeralign

   \ *Figure 18: I2C Configuration Window*\


To configure the I2C for use, check the **Transceiver Enable** box (seen above). The Transceiver Enable box is present on all the configuration windows, and is used to enable or disable the transceivers on the ezLINX hardware.

The I2C Configuration Window is divided into two boxes:

-

.. container:: em

   Interface Settings Box


: to select the appropriate interface for I2C transceiver.



|image18|

.. container:: centeralign

   \ *Figure 19: Interface Settings Box*\


Select TWI1 from the drop-down interface menu.

-

.. container:: em

   I2C Settings Box


: to communicate with ezLINX hardware board through I2C protocol, you need to configure the device using the following features:



|image19|

.. container:: centeralign

   \ *Figure 20: I2C settings box*\


**Client:**

If you are using the ADUM1250 as a master device, this specifies which client to connect to. If you are using the ADUM1250 as a slave device, this specifies the client address of the transceiver.

**Baud Rate:**

Select either 100 Baud or 400 Baud as the symbol rate.

**Mode:**

Select whether to configure the connected device as a master or a slave.

**Write Read Flag:**

Select whether the device is performing a read or write operation.

To confirm your selection click the **Use Changes** button. If you are connected to an ezLINX hardware platform and the **Enable Transceiver** box is checked, this will open the I2C Transmit/Receive window.

I2C Send/Receive Window
-----------------------

Shown below is the transmit/receive window for the I2C protocol. The left hand text box is used to transmit data via the **Send Data** button, and the right hand text box is used to receive real time data.


|image20|

.. container:: centeralign

   \ *Figure 21: I2C Send/Receive Window*\


The I2C module can only send Hexadecimal data. When using the ezLINX I2C transceiver to write to a slave device, data must be sent in multiples of 2 bytes (4 HEX digits) for correct operation. The first byte represents the memory address to write to, while the second byte contains the value to be written to that address. When using the I2C transceiver to read from a slave device, the data must be sent as one or more whole bytes (multiples of 2 HEX digits). Each byte specifies a memory address to read from. When sent the value of that register will be received by the master from the slave and displayed in the Receive window.

The following functions are also available:

**On/Off buttons:**

Turns the transceiver on or off. When off the I2C transceiver is disconnected.

\**Send Data: \*\*

Transmit the text written in the Send box.

**Auto:**

Toggles the Auto setting, which transmits data automatically as you type it in the Send box.

**Load File:**

Opens a load file menu to select a .txt file to send. The contents of the file are automatically sent through the I2C port once loaded. Files must contain hexadecimal characters only.

**Clear:**

Clears the text box.

**Save To File:**

Opens a create .txt file window. Once created all received data will be saved to this file.

Click again to toggle the Save To File function.

\**Log To File: \*\*

Opens a create .txt file window. Once created all received data will be logged to this file with a timestamp. Click again to toggle the Log to File function.

To close the Send/Receive window simply turn the transceiver off and click on a different interface button, or deselect the I2C interface button from the sidebar to return to the I2C Configuration Window.

Isolated SPI
============

The two isolated Serial Peripheral Interface (SPI) ports on the ezLINX development platform are implemented using Analog Devices :adi:`adum3401`, :adi:`adum3402` and :adi:`adum5000` signal and power isolators. For more information on the SPI hardware implementation click :doc:`here </wiki-migration/resources/eval/ezlinx/isolated-spi>`.

.

SPI Configuration Window
------------------------

To open the SPI menu select it using the button on the right hand sidebar of the Application. This opens the SPI configuration window:


|image21|

.. container:: centeralign

   \ *Figure 22: SPI Configuration Window.*\


To configure the SPI for use, check the **Transceiver Enable** box (seen above). The Transceiver Enable box is present on all the configuration windows, and is used to enable or disable the transceivers on the ezLINX hardware.

The SPI Configuration interface is divided into three boxes:

-

.. container:: em

   Interface Settings Box


: To select the appropriate interface for SPI transceiver.



|image22|

.. container:: centeralign

   \ *Figure 23: Interface Settings Box.*\


Select SPI0, SPI1 or SPI2 from the drop-down interface menu.

-

.. container:: em

   SPI Settings Box


: to communicate with ezLINX hardware board through SPI protocol, you need to choose the following parameters:



|image23|

.. container:: centeralign

   \ *Figure 24: SPI Settings Box.*\


**Max Speed:**

Specifies the max speed (in bps) that the SPI interface will operate at. The maximum baud rate that can be used it 32.81 MHz.

\**LSB First: \*\*

Activate the LSB (Least Significant Byte) First mode.

On power up, MSB-first mode is the default. This can be changed by programming the configuration register. In LSB-first mode, the serial exchange starts with the lowest-order bit and ends with the MSB (Most Significant Byte).

The instruction is 16 bits long, consisting of 2 bytes. From the SPI configuration window, you can choose the number of bits to be reversed.

**Word Size:**

Select whether to send data as 1, 2 or 4 byte words.

**Operation Mode:**

Select whether the device is operating as a master as a slave.

**Channel:**

This is only available when the Operation Mode selected is Master. This selects which slave device to connect to, via the slave select lines. The ezLINX hardware platform has 3 slave select lines and a master can thus be connected to up to 3 slave devices. To confirm your selection click the Use Changes button. If you are connected to an ezLINX hardware platform and the Enable Transceiver box is checked, this will open the SPI Send/Receive window

-

.. container:: em

   SPI Routing Box


: The SPI interfaces support hardware routing to the outputs of other interfaces. To enable hardware routing check the **Enable Routing** box and select the interface to route to from the drop down menu. To route to RS-232 select UART3 from the drop down menu.



|image24|

.. container:: centeralign

   \ *Figure 25: Routing box.*\


To confirm your selection click the Use Changes button. If you are connected to an ezLINX hardware platform and the Enable Transceiver box is checked, this will open the SPI Send/Receive window.

SPI Send/Receive Window
-----------------------

Shown below is the transmit/receive window for the SPI protocol. The left hand text box is used to transmit data via the Send Data button, and the right hand text box is used to receive real time data.


|image25|

.. container:: centeralign

   \ *Figure 26: SPI Send/Receive Window.*\


The following functions are also available:

**On/Off buttons:**

Turns the transceiver on or off. When off the SPI transceiver is disconnected.

**Auto:**

Toggles the Auto setting, which transmits data automatically as you type it in the Send box.

**Load File:**

Opens a load file menu to select a .txt file to send. The contents of the file are automatically sent through the SPI port once loaded.

**Clear:**

Clears the text box.

**Send Data Format:**

Choose whether to send the characters in the text box as HEX or ASCII data.

**Receive Data Format:**

Choose whether to display the received data on the screen as HEX or ACSII characters.

**Save To File:**

Opens a create .txt file window. Once created all received data will be saved to this file. Click again to toggle the Save To File function.

**Log To File:**

Opens a create .txt file window. Once created all received data will be logged to this file with a timestamp. Click again to toggle the Log to File function.

To close the Send /Receive window simply turn the transceiver off and click on a different interface button, or deselect the SPI interface button from the sidebar to return to the SPI Configuration Window.

Isolated CAN
============

The isolated Controller Area Network (CAN) interface on the ezLINX development platform is implemented using Analog Devices :adi:`adm3053` transceiver. For more information on the CAN hardware implementation click :doc:`here </wiki-migration/resources/eval/ezlinx/isolated-can>`.

CAN Configuration Window
------------------------

To open the CAN menu select it from the sidebar on the left hand side of the Application. The CAN button on the right hand side of the application is unimplemented and can’t be selected. Selecting CAN from the left hand sidebar opens the CAN configuration window shown below:


|image26|

.. container:: centeralign

   \ *Figure 27: CAN Configuration window.*\


To configure the CAN for use, check the “Transceiver Enable” box (seen above). The Transceiver Enable box is present on all the configuration windows, and is used to enable or disable the transceivers on the ezLINX hardware. The CAN Configuration interface is divided into three boxes:

-

.. container:: em

   Interface Settings Box


: to select the appropriate interface for CAN transceiver.



|image27|

.. container:: centeralign

   \ *Figure 28: Interface settings box.*\


Select CAN0 from the drop-down interface menu.

-

.. container:: em

   CAN Settings Box


:to communicate with ezLINX hardware board through CAN protocol, you need to specify the following data:



|image28|

.. container:: centeralign

   \ *Figure 29: CAN Settings Box.*\


**Bit Rate:**

Select the bit rate that the ADM3053 will operate at. Note that the ADM3053 is not specified at data rates above 1Mbps.

**Error Filter:**

Error filter allows detection of hardware issues on the physical transceiver layer as well as arbitration problems and error frames. The reception of error frames is disabled by default. To enable it, check the “Error Filter” box. You can then select your desired error filter from the below list by checking the relevant box:

CAN_ERR_TX_TIMEOUT : TX timeout (netdevice driver).

CAN_ERR_LOSTARB : Lost arbitration.

CAN_ERR_CRTL : Controller problems.

CAN_ERR_PROT : Protocol violations.

CAN_ERR_TRX : Transceiver status.

CAN_ERR_ACK : Received no ACK on transmission.

CAN_ERR_BUSOFF : Bus off.

CAN_ERR_BUSERROR : Bus error.

CAN_ERR_RESTARTED : Controller restarted.

CAN_ERR_MASK : Omit EFF, RTR, ERR flags.

**CAN Filter/Mask:**

The reception of CAN frames can be controlled by three filters/masks. Each filter/mask can be used for messages with either standard or extended identifiers. Note that you must check the box next to the appropriate name of the filter/mask to enter your selected value.

**Normal Filter 1 – 3:**

Filter for standard frame (11 bit identifier).

**Extended Filter 1 – 3:**

Filter for extended frame (29 bit identifier).

**Normal Mask 1 – 3:**

Mask for standard frame (11 bit identifier).

**Extended Filter 1 - 3:**

Mask for extended frame (29 bit identifier).

-

.. container:: em

   CAN Routing Box


: The CAN interface supports hardware routing to the outputs of other interfaces. To enable hardware routing check the Enable Routing box and select the interface to route to from the drop down menu. To route to RS-485 select UART2 from the drop down menu.



|image29|

.. container:: centeralign

   \ *Figure 30: Routing box.*\


To confirm your selection click the Use Changes button. If you are connected to an ezLINX hardware platform and the Enable Transceiver box is checked, this will open the CAN Send/Receive window.

CAN Send/Receive Window
-----------------------

Shown below is the transmit/receive window for the CAN protocol. The left hand text box is used to transmit data via the Send Data button, and the right hand text box is used to receive real time data.


|image30|

.. container:: centeralign

   \ *Figure 31: CAN Send/Receive window.*\


The CAN module can only send Hexadecimal data. The colon is used to separate the two parts of each CAN message. Each CAN message have both an identifier and the data. The identifier can be either a standard identifier (SID), ranging from 000h – 7FFh, or an extended ID (EXID), from 8000 0000h – FFFF FFFFh. The data section of each CAN message must be sent as whole bytes (multiples of two HEX digits). Some examples of CAN messages are shown below:



|image31|

.. container:: centeralign

   \ *Figure 32: Examples of CAN messages.*\


The following functions are also available:

**On/Off buttons:**

Turns the transceiver on or off. When off the CAN transceiver can not transmit or receive data.

**Auto:**

Toggles the Auto setting, which transmits data automatically as you type it in the Send box.

**Load File:**

Before using this function you must check the File box. Opens a load file menu to select a .txt file to send. Your choice must be a correctly formatted file containing only hexadecimal values, with the identifier and data sections of each CAN message separated by a colon (no spaces). The contents of the file are automatically sent through the CAN port once loaded.

**Clear:**

Clears the text box.

**Save To File:**

Opens a create .txt file window. Once created all received data will be saved to this file.

Click again to toggle the Save To File function.

\**Log To File: \*\*

Opens a create .txt file window. Once created all received data will be logged to this file with a timestamp. Click again to toggle the Log to File function.

To close the Send/Receive window simply turn the transceiver off and click on a different interface button, or deselect the CAN interface button from the sidebar to return to the CAN Configuration Window.

Isolated LVDS
=============

The isolated LVDS interface on the ezLINX hardware platform is implemented using the :adi:`adum3442` and :adi:`adum5000` signal and power isolators, and the :adi:`adn4663` and :adi:`adn4664` LVDS receivers and drivers. For more information on the LVDS implementation click :doc:`here </wiki-migration/resources/eval/ezlinx/isolated-lvds>`.

LVDS Configuration Window
-------------------------

To open the Low Voltage Differential Signalling (LVDS) menu select it from the sidebar on the right hand side of the Application. This opens the LVDS configuration window shown below:


|image32|

.. container:: centeralign

   \ *Figure 33: LVDS Configuration Window.*\


To configure the LVDS interface for use, check the **Transceiver Enable** box (seen above). The Transceiver Enable box is present on all the configuration windows, and is used to enable or disable the transceivers on the ezLINX hardware.

The LVDS Configuration interface is divided into two boxes:

-

.. container:: em

   Interface Settings Box


: To select the appropriate interface for LVDS transceiver.



|image33|

.. container:: centeralign

   \ *Figure 34: Interface settings box.*\


Select SPORT2 from the drop-down interface menu.

-

.. container:: em

   LVDS Settings Box


: to configure the LVDS interface:



|image34|

.. container:: centeralign

   \ *Figure 35: LVDS settings box.*\


**Baud Rate Tx:**

Specifies the baud rate that the LVDS interface will transmit data at.

**Baud Rate Rx:**

Specifies the baud rate that the LVDS interface will read received data at.

**Word Size:**

Select whether to send data in 1 or 2 byte words.

**Frame Delay:**

Transfer delay.

**Active Low:**

Active Low Enable and Power-Down Input with Pull-Down (3 V TTL/CMOS). If EN is held high, EN enables the drivers when low or open circuit and disables the drivers and powers down the device when high.

**Internal Clock Tx:**

Select whether to use the internal clock to driver the LVDS transmitter, or to trigger on an external clock. Select 1 for an internal clock or 0 for an external clock. For best results for board to board communication one device should use an internal clock and the other device trigger on this clock.

**Internal Clock Rx:**

Select whether to use the internal clock to drive the LVDS receiver, or to trigger on an external clock. Select 1 for an internal clock or 0 for an external clock. For best results for board to board communication one device should use an internal clock and the other device trigger on this clock. Secondary Channel Enable:

Select whether to enable the second LVDS channel (Pins 17 – 32). Select 1 to enable this channel or 0 to disable it.

-

.. container:: em

   LVDS Routing Box


: The LVDS interface supports hardware routing to the outputs of other interfaces. To enable hardware routing check the Enable Routing box and select the interface to route to from the drop down menu. To route to RS-485 select UART2 from the drop down menu.



|image35|

.. container:: centeralign

   \ *Figure 36: LVDS Routing Box.*\


To confirm your selection click the **Use Changes** button. If you are connected to an ezLINX hardware platform and the **Enable Transceiver** box is checked, this will open the LVDS Send/Receive window.

LVDS Send/Receive Window
------------------------

Shown below is the transmit/receive window for the LVDS protocol. The window is identical to the RS -232 send/receive window. The left hand text box is used to transmit data via the **Send Data** button, and the right hand text box is used to receive real time data.


|image36|

.. container:: centeralign

   \ *Figure 37: LVDS Send/Receive window.*\


The following functions are also available:

**On/Off buttons:**

Turns the transceiver on or off. When off the LVDS transceiver can not transmit or receive data.

**Auto:**

Toggles the Auto setting, which transmits data automatically as you type it in the Send box.

**Load File:**

Opens a load file menu to select a .txt file to send. The contents of the file are automatically sent through the LVDS port once loaded.

**Clear:**

Clears the text box.

**Send Data Format:**

Choose whether to send the characters in the text box as HEX or ASCII data.

**Receive Data Format:**

Choose whether to display the received data on the screen as HEX or ACSII characters.

**Save To File:**

Opens a create .txt file window. Once created all received data will be saved to this file. Click again to toggle the Save To File function.

**Log To File:**

Opens a create .txt file window. Once created all received data will be logged to this file with a timestamp. Click again to toggle the Log to File function.

To close the Send /Receive window simply turn the transceiver off and click on a different interface button, or deselect the LVDS interface button from the sidebar to return to the LVDS Configuration Window.

GPIO (LEDs)
===========

The Sample PC Application also has GPIO functionality, through which you can control 6 LED’s on the ezLINX hardware platform. To access the GPIO interface, select the GPIO button from the left hand sidebar of the application. This opens the GPIO Interface Settings window.


|image37|

.. container:: centeralign

   \ *Figure 38: GPIO Configuration Window.*\


To enable a GPIO pin, check the GPIO box on the left hand side of the screen.

The GPIO Configuration Window is divided into two boxes:

-

.. container:: em

   Interface Settings Box


: to select the appropriate interface for GPIO transceiver.



|image38|

.. container:: centeralign

   \ *Figure 39: Interface settings box.*\


Select GPIO from the drop-down interface menu.

-

.. container:: em

   GPIO Settings Box


: to configure GPIO pins:



|image39|

.. container:: centeralign

   \ *Figure 40: GPIO Settings Box.*\


**Direction:**

Select whether you wish to configure the GPIO pin as an input or an output. Select 0 for Input and 1 for output.

**GPIO Pin:**

Select which GPIO pin to use.

**Value:**

Select the binary value for the GPIO pin.

By checking multiple GPIO enable boxes, you can use multiple GPIO pins together. To confirm your settings click the Use Changes box at the bottom of the screen.

Firmware Update
===============

To update the embedded software version on the evaluation board, there are a number of steps you must follow. First the application FTPServer.exe must be allowed through Windows Firewall. To do this, go to:

**Windows XP / Vista:** Start → Control Panel → Windows Firewall → Exceptions → Add Program

**Windows 7:** Start → Control Panel (All items view) → Windows Firewall → Allow a program through Windows Firewall → Change settings → Allow another program And select FTPServer.exe from the distributed package.


|image40|

.. container:: centeralign

   \ *Figure 41: Allow FTPServer through Windows Firewall.*\


To use FTPServer.exe, you must configure the application to connect to the correct IP address. In Configure Settings, under PASV Settings, you must select the IP address of the adapter used to connect the board to the PC from the drop down menu, as shown below:



|image41|

.. container:: centeralign

   \ *Figure 42: Update Firmware.*\


In User Accounts, you must then change the path to the directory containing the uImage file to be downloaded to the ezLINX hardware platform. Click Start at the top left of the application to begin running the FTP service.

From the PC software enter the IP Address of the server that contains the needed uImage than press Send button.

The software application prompts you to restart the application.


|image42|

.. container:: centeralign

   \ *Figure 43: Restart Application to update the embedded software version.*\


Close the application and wait approximately 2 – 3 minutes for the the application to erase the hardware platform and download and extract the new firmware version. **WARNING: Do not reset the ezLINX hardware during the update.** You will know the transfer is complete when the data sent counter at the bottom right of the Quick ‘n Easy FTP Server application is equal to the size of the update file. The board must then be reset and the PC application started. To confirm that the firmware update was downloaded correctly, go to the board configuration window and click the Check button next to the Embedded Version box. This should display the new version.

Transceiver Status Window
=========================

The Transceivers Status window (shown below) allows the user to monitor the status of each interface as it transmits data. To access the Transceivers Status window click on the word STATUS on the bottom left hand side of the application. The enabled transceivers will show up with a checked box, and the amount of data sent and received through each interface during the current session is shown in the boxes in kilobytes. The Tx box displays the amount of kilobytes of data that has been sent through that transceiver, and the Rx box displays the amount of kilobytes of data has been received. To refresh the figures you must close and reopen the Transceivers Status window as the figures do not update in real-time.


|image43|

.. container:: centeralign

   \ *Figure 44: Transceiver Status window.*\


Transceivers Configuration Window
=================================

To access the Transceiver Configuration window (shown below) select the View Configuration button at the bottom of the application. The Transceivers Configuration window allows the user to view the global configuration of all transceivers and GPIO on the ezLINX hardware platform. From here you can see which transceivers are enabled, what hardware routing is active and the settings of each individual interface. The configuration can not be modified from this window, however the application supports loading and saving configurations as an XML file. To save your current configuration simply click the Save button and choose a name. To load a previously saved configuration press Load and select the desired XML config file.


|image44|

.. container:: centeralign

   \ *Figure 45: Configuration window*\


The configuration window has three buttons at the left bottom enabling the following functionalities:

1. Load an existing configuration from an XML file through the “Load” button. The Load Interface will appear:


|image45|

.. container:: centeralign

   \ *Figure 46: Loading an existing configuration to the board.*\


- Clicking on “OK” button means that you enable the load of this configuration.

- Clicking on “Cancel” button, the load will be canceled and this window will be closed.

2. Save the current configuration to a new XML file when clicking on the Save button.

3. Close the configuration window using the Close button. A confirmation message will appear asking if the configuration changes should be kept or not.


|image46|

.. container:: centeralign

   \ *Figure 47: Ask for keeping the loaded configuration before closing the configuration window.*\


**Note:** When a configuration is loaded you must exit the Transceivers Configuration window via the Close button. Exiting the window via the X will not load the configuration.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig2ConfigurationwindowfromConfigurebutton.jpg
   :width: 850px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig3ConfigurationWindowfromtheezLINXimage.jpg
   :width: 850px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig4Networkfeaturesbox.jpg
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/update_firmware.jpg
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig6EnableDisablebox.jpg
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig7Notificationmessageforenabledtransceivers.jpg
   :width: 850px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig8RS232ConfigurationWindow.jpg
   :width: 850px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig9Interfacesettingsbox.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig10RS-232settingsbox.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig11RS-232Routingbox.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig12RS-232Send-ReceiveWindow.jpg
   :width: 850px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig13RS-485ConfigurationWindow.jpg
   :width: 850px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig14InterfaceSettingsBox.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig15RS-485SettingsBox.jpg
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig16Routingbox.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig17RS-485-RS-422Send-ReceiveWindow.jpg
   :width: 850px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig18I2CConfigurationWindow.jpg
   :width: 850px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig19InterfaceSettingsBox.jpg
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig20I2Csettingsbox.jpg
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig21-I2CSend-ReceiveWindow.jpg
   :width: 850px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig22-SPIConfigurationWindow.jpg
   :width: 850px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig23-InterfaceSettingsBox.jpg
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig24-SPISettingsBox.jpg
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig25-Routingbox.jpg
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig26-SPISend-ReceiveWindow.jpg
   :width: 850px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig27-CANConfigurationWindow.jpg
   :width: 850px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig28-InterfaceSettingsBox.jpg
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig29-CANSettingsBox.jpg
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig30-RoutingBox.jpg
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig31-CANSendReceiveWindow.jpg
   :width: 850px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig32-ExamplesofCANMessages.jpg
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig33-LVDSConfigurationWindow.jpg
   :width: 850px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig34-InterfaceSettingsBox.jpg
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig35-LVDSSettingsBox.jpg
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig36-LVDSRoutingBox.jpg
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig37-LVDSSend-ReceiveWindow.jpg
   :width: 850px
.. |image37| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig38-GPIOConfigurationWindow.jpg
   :width: 850px
.. |image38| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig39-InterfaceSettingsBox.jpg
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig40-GPIOSettingsBox.jpg
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig41_WindowsFirewall.jpg
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig42_FTPServerWindow.jpg
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Fig43_RestartApplicationWindow.jpg
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/TRANSCEIVERSTATUS.jpg
   :width: 500px
.. |image44| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/ConfigurationWindow.jpg
   :width: 800px
.. |image45| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/LoadInterface.jpg
   :width: 300px
.. |image46| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/ug/Askforkeepingtheloadedconfiguration.jpg
   :width: 300px
