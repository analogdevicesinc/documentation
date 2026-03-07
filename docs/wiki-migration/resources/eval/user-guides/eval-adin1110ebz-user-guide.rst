User Guide for EVAL-ADIN1110EBZ
===============================

.. container:: group

   
   General Description
   -------------------
   
   The EVAL-ADIN1110EBZ is a flexible platform enabling quick evaluation of the ADIN1110, robust, low power 10BASE-T1L MAC-PHY. It provides 10Mbit per second Single Pair Ethernet (SPE) connections with devices across 1.7km of cable.
   
   The evaluation board offers two modes of operation for maximum flexibility. Connected to a PC via USB port, the full set of ADIN1110 register settings and features such as link quality monitoring and diagnostics can be accessed over the USB using serial command interface. The board also provides an Arduino interface.
   
   Alternatively, the board can operate in stand-alone mode where it is configured by setting hardware configuration links and switches. On-board LEDs provide status indication.
   
   The SPI interface provides configuration and data access to the ADIN1110.
   
   A small prototyping area and test points are provided for experimentation with alternative cable connection topologies including isolation transformers and/or power coupling inductors.

   
   |image1|

   .. container:: centeralign

      \ *Figure 1. EVAL-ADIN1110-EBZ – Simplified Block Diagram*\

   
   Features
   ~~~~~~~~
   
   -  User friendly access to all ADIN1110 features
   -  Stand-alone hardware configured operation
   -  Flexible power supplies and prototyping options
   -  On-board ARM Cortex-M4 STM32L4S5QII3P ultra-low-power Microcontroller
   
   Equipment Needed
   ~~~~~~~~~~~~~~~~
   
   -  Link partner with 10BASE-T1L interface
      Recommended to use ADIN1100EBZ Evaluation Board(RJ45 Ethernet interface to use as media converter between 10BASE-T1L and 10BASE-T)
   -  10BASE-T1L compatible Single Pair cable: max. 1.5 mm² / AWG 16 to fit screw terminal connector
   -  Power supply source: 5 to 32 Vdc, 0.6W, or USB as power for the board
   -  Optional: PC running Windows 7 and upwards with USB interface
   -  Optional: ST-LINK programmer
   


Evaluation Kit Contents
-----------------------

-  EVAL-ADIN1110EBZ board
-  2x plug-in screw-terminal connectors for 10BASE-T1L cable and external power supply
-  USB-A to Micro USB-B cable (1 meter)

Software (Optional)
-------------------

-  FTDI USB Virtual Com Port driver (Available from FTDI website)
-  Serial port terminal software (e.g. CompuPhase Termite)

Documentation Needed
--------------------

-  ADIN1110 Datasheet available from the product webpage: :adi:`adin1110.html <en/products/adin1110.html>`
-  EVAL-ADIN1100EBZ User Guide: :doc:`adin1100_userguide </wiki-migration/resources/eval/user-guides/adin1100_userguide>`

--------------

Overview
~~~~~~~~

|image2|

.. container:: centeralign

   \ *Figure 2. EVAL-ADIN1110EBZ Quick Start Info*\


   |image3|

.. container:: centeralign

   //Figure 3. EVAL-ADIN1110EBZ Functional Block Diagram //


Hardware
~~~~~~~~

Power Supplies
--------------

The EVAL-ADIN1110EBZ can be powered from three different sources:

-  5-32V DC external power supply connected to P1 terminal bock or P2 barrel connector
-  USB (5V DC) using the P401 micro-usb connector
-  Arduino connector P403 (Vin pin)

| The power supply source can be configured using the J1 "BOARD PWR SELECTION" link (3-positions: EXT+,USB and ARD).
| Note that the three power supplies can be simultaneously enabled on J1 (3 jumpers inserted) as an internal common cathode diodes circuit selects the highest voltage source.

| The selected input power source is converted by the step-down converter U501 (LT8619) to 3.3V
| The link J2 is used to connect U501 output to the main 3.3V supply rail used on the board
| The green “POWER” LED1 is ON when the 3.3V rail is present.
| The board power consumption depends on the mode of operation, with the maximum of approximately 0.5W.

10BASE-T1L Cable Connection
---------------------------

The 10BASE-T1L cable can be connected via pluggable screw-terminal block to connector P101. If more of the pluggable connectors are needed, for easy connecting / changing cables, additional connectors can be purchased from the vendor or distributors:

-  Manufacturer: Phoenix Contact
-  Manufacturer part number: 1803581
-  Description: “Pluggable Terminal Block, 3.81 mm, 3 Ways, 28AWG to 16AWG, 1.5 mm², Screw”.

Ground Connections
------------------

The demo board has an “Earth node”. We call it “Earth node” here – though this node may or may not be electrically connected to Earth ground. In a real device this node would be typically connected to the device metal housing / chassis. This Earth node can be connected as required in a wider demo system via “Earth” terminal of the power supply connector P1, or via exposed metal plating of 2 mounting holes in the left corners of the board. (The 3rd and 4th holes on the right do not have metal plating, and also no Earth connection.)

The shield of the 10BASE-T1L cable can be disconnected from this Earth node, connected directly, or connected via 4700pF capacitor (C104). The required connection is selected using jumper J101.

The local circuit ground, the external power supply (except the “Earth” terminal P1), and the USB connector are connected to the Earth node via approx. 2000pF capacitance and approx. 4.7MΩ resistance.

**(!) Note: The EVAL-ADIN1110EBZ has been designed only as an Evaluation board. It has NOT been designed, and it has NOT been tested for electrical safety. Any equipment, device, wire, or cable connected to this demo must be already protected and safe to touch without danger of electric shock.**

Hardware Configuration Setup
----------------------------

The EVAL-ADIN1110EBZ board is provided with links (jumper) and DIP switches that can be used to set the ADIN1110 configuration. The Table 1,2 and 3 describe the links and switches functions.

**Table 1. Board Link Configuration**

+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| Link | Default       | Description                                                                                                         |
| Ref. | Position      |                                                                                                                     |
+======+===============+=====================================================================================================================+
| J1   | USB inserted  | Board power supply source selection. All jumpers can be inserted simultaneously.                                    |
|      | EXT+ inserted |                                                                                                                     |
|      | ARD inserted  |                                                                                                                     |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J2   | Inserted      | Board 3.3V power supply rail                                                                                        |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J3   | Inserted      | Board 1.8V power supply rail                                                                                        |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J101 | Earth         | SHIELD - Connect the shield of the cable to the Earth node either directly or via a 4nF capacitor.                  |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J203 | LDO           | ADIN1110 1.1V power supply selection.                                                                               |
|      |               | LDO: using ADIN1110 on-chip internal 1.1V linear regulator.                                                         |
|      |               | EXT: using 1.1V output of the step-down regulator LTC3547.                                                          |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J204 | AVDD_H: 3.3V  | ADIN1110 power supplies selection. Ensure VDDIO and uC Power rails are set to the same voltage level, 3.3V or 1.8V. |
|      | AVDD_L: 3.3V  |                                                                                                                     |
|      | VDDIO: 3.3V   |                                                                                                                     |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J301 | Global        | Microcontroller Reset.                                                                                              |
|      |               | Global: Microcontroller Reset connected to S501 Reset button.                                                       |
|      |               | GND: Microcontroller Reset connected to GND                                                                         |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| J302 | 3.3V          | uC Power. 3.3V or 1.8V                                                                                              |
+------+---------------+---------------------------------------------------------------------------------------------------------------------+

\**Table 2. ADIN1110 Hardware Configuration , Schematics Ref. S201 \*\*

+----------+------------+----------+-----------------------------------------------+
| Switch   | Switch     | Default  | Description                                   |
| Position | Name       | Position |                                               |
+==========+============+==========+===============================================+
| 1        | SPI_CFG0   | OFF      | SPI configuration 0                           |
|          |            |          | OFF: SPI CRC/Protection enabled.              |
|          |            |          | ON: SPI CRC/Protection disabled               |
+----------+------------+----------+-----------------------------------------------+
| 2        | SPI_CFG1   | OFF      | SPI configuration 1                           |
|          |            |          | OFF: Open Alliance SPI                        |
|          |            |          | ON: Generic SPI                               |
+----------+------------+----------+-----------------------------------------------+
| 3        | SWPD_EN_N  | OFF      | Software power down after reset               |
|          |            |          | OFF: Software power down after reset enabled  |
|          |            |          | ON: Software power down after reset disabled. |
+----------+------------+----------+-----------------------------------------------+
| 4        | TX2P4_EN_N | OFF      | Transmit 2.4V disable                         |
|          |            |          | OFF: TX level 2.4V p-p or 1.0V p-p            |
|          |            |          | ON: TX level 1.0V p-p only                    |
+----------+------------+----------+-----------------------------------------------+
| 5        | MS_SEL     | OFF      | Master/Slave select                           |
|          |            |          | OFF: Prefer Slave                             |
|          |            |          | ON: Prefer Master                             |
+----------+------------+----------+-----------------------------------------------+

**Table 3. Board LED indicators**

+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| Name         | Colour                  | Schematics | Description                                                           |
| (silkscreen) |                         | Ref.       |                                                                       |
+==============+=========================+============+=======================================================================+
| uC0          | <fc #008000>Green</fc>  | LED400     | In media converter mode: Media Converter working - both PHYs links up |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| uC1          | <fc #FF0000>Red</fc>    | LED401     | OFF: No error                                                         |
|              |                         |            | ON: Error detected by firmware                                        |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| uC2          | <fc #808000>Yellow</fc> | LED402     | Short flash: Heartbeat.                                               |
|              |                         |            | Long flash or ON: Receiving UART commands                             |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| uC3          | <fc #0000FF>Blue</fc>   | LED403     | Reserved                                                              |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| LED_0        | <fc #008000>Green</fc>  | LED200     | ON/Flashing: 10BASE-T1L link up/activity                              |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| LED_1        | <fc #808000>Yellow</fc> | LED201     | OFF: 10BASE-T1L TX amplitude 1.0V p-p                                 |
|              |                         |            | ON: 10BASE-T1L TX amplitude 2.4V p-p                                  |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+
| POWER        | <fc #008000>Green</fc>  | LED1       | Board 3.3V power supply is present                                    |
+--------------+-------------------------+------------+-----------------------------------------------------------------------+

Microcontroller Modes of operation
----------------------------------

The EVAL-ADIN1110EBZ can be used in various modes of operations implemented in the uC firmware. Up to 16 modes of operations can be selected by setting the 4 positions of the slide switch S303. The selected configuration is latched after the board is powered up or reset.

Therefore, to change the mode of operation, the board must be reset by pressing “RESET” button S501 or by applying power cycle after changing the position of the slide switch S303. The available modes of operation are described in Table 4 below.

**Table 4. Firmware Modes of Operation, Schematics Ref. S303**

+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CFG             | Mode | Operating Mode\ :sup:`ii`               | Description                                                                                                                                                                                   |
| [3:0]\ :sup:`i` | No.  |                                         |                                                                                                                                                                                               |
+=================+======+=========================================+===============================================================================================================================================================================================+
| 0000            | 15   | TCP/IP Stack & Web Server, DHCP client, | In this mode, the TCP/IP stack can be managed via UART using dynamic IP address allocation.                                                                                                   |
|                 |      | MAC Addr1                               | The media converter board is then used to convert 10BASE-T1L to 10BASE-T ethernet, for which common web browsers can be used to access the associated information.                            |
|                 |      |                                         | MAC address 1 is used.                                                                                                                                                                        |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0001            | 14   | TCP/IP Stack & Web Server, Fixed IP,    | This is a similar mode to the previous one except fixed IP address allocation is used.                                                                                                        |
|                 |      | MAC Addr1                               | MAC address 1 is used.                                                                                                                                                                        |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0010            | 13   | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0011            | 12   | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0100            | 11   | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0101            | 10   | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0110            | 9    | PHY Frame Generator/Checker             | The PHY Frame Generator sends 10,000 frames and checks for number of frames received and potential errors. Output is shown on UART. System errors are indicted by the RED LED uc1 turning ON. |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0111            | 8    | PHY MAC Interface Remote Loopback,      | The PHY is set in MAC Interface Remote loopback mode, and in parallel MSE readings are shown on UART. Link LED is also enabled.                                                               |
|                 |      | MSE reading enabled                     |                                                                                                                                                                                               |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1000            | 7    | TCP/IP Stack & Web Server, DHCP client, | The use of this mode is depicted in Figure 11. In this mode, the TCP/IP stack can be managed via UART using dynamic IP address allocation.                                                    |
|                 |      | MAC Addr2                               | The media converter board is then used to convert 10BASE-T1L to 10BASE-T ethernet,                                                                                                            |
|                 |      |                                         | for which common web browsers can be used to access the associated information.                                                                                                               |
|                 |      |                                         | MAC address 2 is used.                                                                                                                                                                        |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1001            | 6    | TCP/IP Stack & Web Server, Fixed IP,    | This is a similar mode to the previous one except fixed IP address allocation is used.                                                                                                        |
|                 |      | MAC Addr2                               | MAC address 2 is used.                                                                                                                                                                        |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1010            | 5    | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1011            | 4    | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1100            | 3    | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1101            | 2    | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1110            | 1    | RESERVED                                | The uC makes no autonomous attempt to interact with the ADIN1110 MAC-PHY.                                                                                                                     |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1111            | 0    | Reset MAC-PHY                           | Reset the ADIN1110                                                                                                                                                                            |
+-----------------+------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| :sup:`I` //Switch in ON position = signal logic 0 for microcontroller (shorted to ground).
| Switch in OFF position = signal logic 1 (pulled up by a resistor) //

:sup:`II` *RESERVED means the microcontroller and command line interface is active (serial port).*

Software
~~~~~~~~

| The EVAL-ADIN1110EBZ can be used as a stand-alone board, with the firmware already pre-programmed in the microcontroller flash memory.
| The mode of operation can be set using the S303 "uC Config" DIP switch and the link status is indicated by LEDs. There is no software required for this stand-alone use case.

The EVAL-ADIN1110EBZ can also be interfaced with a host computer via the USB port. The full set of ADIN1110 PHY and MAC registers and features such as link quality monitoring can be accessed via the command line interface.

Driver For USB COM Port
-----------------------

The EVAL-ADIN1110EBZ has an onboard USB-UART converter (FTDI FT232R).

Ensure that the appropriate Virtual Com Port driver is installed on the host platform before connecting the EVAL-ADIN1110EBZ to the host computer via the USB cable.

The drivers are available from FTDI, at the time of writing this document at https://ftdichip.com/drivers/vcp-drivers/

COM Port and Terminal Settings
------------------------------

When the EVAL-ADIN1110EBZ is connected to the host, it will become available in the host system as a USB Com Port, and will be assigned a com port number. The number will depend on the system settings, on com port devices previously connected and assigned in the system, and on the FTDI driver settings.

The EVAL-ADIN1110EBZ microcontroller communicates over a standard UART interface, with the following settings:

-  Baudrate: 115200
-  Data Bits: 8
-  Stop Bits: 1
-  Parity: none

The protocol is based on ASCII text commands and messages. Each message sent from the firmware to the host is finished by both <CR> and <LF> characters. For the commands received from host the firmware expects <CR>, <LF> or <CR> + <LF>.

(//For information: <CR> .. “carriage return”, ASCII code 0x0D, <LF> .. “line feed”, ASCII code 0x0A //)

Terminal Commands and Messages
------------------------------

The EVAL-ADIN1110EBZ firmware works with the common serial terminals. It has been tested on Windows platform with PuTTY, RealTerm, Termite and Hyperterminal. (*The examples in this document were captured using Compuphase Termite*).

Initial Welcome Message
-----------------------

| When the EVAL-ADIN1110EBZ is correctly connected via the USB Virtual COM Port using the terminal software, the firmware sends an initial welcome message as displayed below.
| Note that a hardware reset of the board (using S501 "RESET" button) or the 'info' command will also display the welcome message. This can be useful to check the ADIN1110 information and link status.

| <fc #008000> ================================================
| ANALOG DEVICES 10BASE-T1L Demo Serial Interface
| ================================================
| (c) 2021 Analog Devices Inc. All rights reserved
| ================================================
| Firmware ver.: 1.1.0
| Board Name: EVAL-ADIN1110EBZ
| Board revision: B
| Board Serial Number: AVAS146613
| uC CFG3-2-1-0: OFF-OFF-OFF-OFF (Mode 15)
| Board Configuration:TCP/IP Stack+Web Server,DHCP,MAC Addr1
| SPI Access to ADIN1110: Success
| MAC address: 00:e0:22:fe:da:c9
| IP Address: not assigned
| Link status: Down
| Master/Slave: Not run
| Tx Level: Not run
| ================================================
| Type '<?><new line>' for a list of commands
| ================================================</fc>

Terminal Commands
-----------------

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Command       | Description                                                                                                                                | Use                                                               |
+===============+============================================================================================================================================+===================================================================+
| macwrite      | Write in MAC registers.                                                                                                                    | <fc #008000>macwrite <RegAddress>,<Data><newLine></fc>            |
|               | <regAddress> and <Data> in hex                                                                                                             |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| macread       | Read MAC registers.                                                                                                                        | <fc #008000>macread <RegAddress><newLine></fc>                    |
|               | <regAddress> in hex                                                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| phywrite      | Write in PHY registers.                                                                                                                    | <fc #008000>phywrite <RegAddress>,<Data><newLine></fc>            |
|               | <regAddress> and <Data> in hex                                                                                                             |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| phyread       | Read in PHY registers.                                                                                                                     | <fc #008000>phyread <RegAddress>,<Data><newLine></fc>             |
|               | <regAddress> in hex                                                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| machwreset    | ADIN1110 Hardware Reset                                                                                                                    | <fc #008000>machwreset<newLine></fc>                              |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| macswreset    | ADIN1110 Software Reset                                                                                                                    | <fc #008000>macswreset<newLine></fc>                              |
|               | Similar to hardware reset without the power up sequence                                                                                    |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changemac     | Change MAC address.                                                                                                                        | <fc #008000>changemac <xx>:<xx>:<xx>:<xx>:<xx>:<xx><newLine></fc> |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | All digits in hex                                                                                                                          |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changeip      | Change IP address.                                                                                                                         | <fc #008000>changeip <xxx>.<xxx>.<xxx>.<xxx><newLine></fc>        |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | <xxx> digits in dec                                                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changegw      | Change gateway, all numbers in dec.                                                                                                        | <fc #008000>changegw <xxx>.<xxx>.<xxx>.<xxx><newLine></fc>        |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | <xxx> digits in dec                                                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changenm      | Change network mask,all numbers in dec.                                                                                                    | <fc #008000>changenm <xxx>.<xxx>.<xxx>.<xxx><newLine></fc>        |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | <xxx> digits in hex                                                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changebrdname | Change board name.                                                                                                                         | <fc #008000>changebrdname <custom text><newLine></fc>             |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | Warning: Predefined in factory. Lost if overwritten                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changebrdrev  | Change board revision                                                                                                                      | <fc #008000>changebrdrev <custom text><newLine></fc>              |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | Warning: Predefined in factory. Lost if overwritten                                                                                        |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| changebrdsn   | Change board serial number                                                                                                                 | <fc #008000>changebrdsn <custom text><newLine><newLine></fc>      |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                   |
|               | Warning: Predefined in factory. Lost if overwritten.                                                                                       |                                                                   |
|               | Serial Number matches the label on the bottom of the board                                                                                 |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| eraseflash    | Erase the internal flash memory.                                                                                                           | <fc #008000>eraseflash<newLine></fc>                              |
|               | Warning:resets the board parameters to default values                                                                                      |                                                                   |
|               | Also erases board name,board serial number and board revision                                                                              |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| savetoflash   | Save configuration to flash.                                                                                                               | <fc #008000>savetoflash<newLine></fc>                             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| reset_dut     | ADIN1110 Physical Hardware Reset                                                                                                           | <fc #008000>reset_dut<newLine></fc>                               |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| reset         | Microcontroller software reset.                                                                                                            | <fc #008000>reset<newLine></fc>                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| start         | Start sending periodic diagnostics.                                                                                                        | <fc #008000>start<newLine></fc>                                   |
|               | Also provide statistics when used in Frame Generator\\checker mode (9)                                                                     |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| stop          | Stop sending periodic diagnostics.                                                                                                         | <fc #008000>stop<newLine></fc>                                    |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| clear         | Clear/reset the diagnostics counters                                                                                                       | <fc #008000>clear<newLine></fc>                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| tempread      | Read the ambiant temperature from the onboard sensor                                                                                       | <fc #008000>tempread<newLine></fc>                                |
|               | Result in ºC                                                                                                                               |                                                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| testram       | Execute the onboard RAM test                                                                                                               | <fc #008000>testram<newLine></fc>                                 |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| mode          | Overwrite the board mode in software. After MCU reset or board reset, the mode is set to hardware configuration defined by the switch S303 | <fc #008000>mode <number><newLine></fc>                           |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| modes         | List the board modes available                                                                                                             | <fc #008000>modes<newLine></fc>                                   |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| info          | Display the board information (welcome message)                                                                                            | <fc #008000>info<newLine></fc>                                    |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| getbuildnb    | Get the firmware build number                                                                                                              | <fc #008000>getbuildnb<newLine></fc>                              |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ?             | Display the list of commands available                                                                                                     | <fc #008000>?<newLine></fc>                                       |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

Microcontroller Firmware Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The microcontroller (STM32L4S5QII3P) is programmed out-of-the box with the evaluation firmware. A binary image of the production firmware is also available to download from the ADIN1110 product webpage. The default behavior of the configuration switches based on the pre-loaded firmware is listed in Table 4. The revision of the programmed firmware can be checked using the serial terminal program and pressing the RESET button (S501) which will display the welcome message.

Using the Microcontroller bootloader
------------------------------------

-  Set the interface to UART
-  Set the serial port settings

   -  Set the serial port number to the one identified in previous section (refreshed port list using the icon)
   -  Baudrate: 115200
   -  Data Bits:8
   -  Parity: Even
   -  Flow Control: OFF
   -  RTS: 0
   -  DTR:0
   -  Read Unprotect (MCU): Not selected

-  Open the **Erasing and programming** menu
-  Browse and select the firmware image file from your download location: eval-ADIN1110EBZ-1_1_0.hex

   -  Click **Open**

-  Reboot the Microcontroller in Programming Mode:

   -  Press and hold the S301 “BOOT” and S501 “RESET” buttons simultaneously on the board
   -  Release S501 “RESET” button while holding the S301 “BOOT” button, release S301 “BOOT” after 1s.
   -  The Board is now in programming mode, the microcontroller LEDs (uC3-uC0) should be OFF

-  Click **Connect**. If Connect fails, check that the Serial COM port is correct as described in **Identify the Serial COM Port** section. Also make sure no serial terminal are connected to the serial port in use.

   -  Check that the target status is “CONNECTED” as marked on Figure 8 (top right corner).

-  Un-tick the **Run After Programming** option
-  Click the **Start Programming** button
-  Wait for the programming to be completed (~35s) , Check that the blue progress bar is 100%
-  A message box appears: **File download completed**, click OK
-  Wait for ~30s. A message box pops up: **Download verified successfully**. Click OK
-  Click the **Disconnect** button
-  Power cycle the board by unplugging and plugin the USB cable and any other power supply connected.

   -  All 4 uCx LEDs (blue, orange, red and green) flash once (LED health check)
   -  **Orange LED** “uC2” is continuously blinking after (Board Heart Beat)

Using the ST-LINK JTAG programmer
---------------------------------

| The ST-LINK JTAG programmer provides a robust solution for programming and debugging source code. It is also faster to program the microcontroller using the JTAG interface.

-  Connect the ST-LINK programmer to the EVAL-ADIN1110EBZ using the ARM-20 JTAG connector P410 "uC JTAG"
-  Select the ST-LINK interface in previous STEP 1 and follow the same instructions to program the board with the provided firmware.

|image4|

.. container:: centeralign

   \ *Figure 4. STM32CubeProgrammer*\


Application Quick Start
~~~~~~~~~~~~~~~~~~~~~~~

Demo Web Page
-------------

| The EVAL-ADIN1110EBZ firmware runs a webserver that can be used to access the Demo webpage to visualize the board information, link status and onboard temperature readings.
| This feature demonstrates how the 10BASE-T1L MAC-PHY can be connected to a 10BASE-T network and accessed using conventional HTTP requests.
| A media converter board (e.g. **EVAL-ADIN1100EBZ**, see the user guide for more details) is required to interface the
| **EVAL-ADIN1110EBZ** to a 10BASE-T network (using RJ45 cable).
| A simple setup is shown below:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/macphy_mediaconvreter.png
   :align: center
   :width: 1000px

To run the webpage demo (fixed IP, mode 14):

-  Connect a single twisted pair between the EVAL-ADIN1110EBZ and the EVAL-ADIN1100EBZ media converter (10BASE-T1L)
-  Connect a RJ45 cable from the media converter board to a Local Area Network, Host Computer or router. (10BASE-T)
-  Configure the EVAL-ADIN1100EBZ in media converter mode with support for 2.4V p-p transmit level (refer to the EVAL-ADIN1100EBZ User Guide)
-  EVAL-ADIN1110EBZ board, set the CFG switch to mode 14 (see Table 4)
-  Connect a micro-USB cable between the EVAL-ADIN1100EBZ media converter board and the host computer
-  Connect a micro-USB cable between the EVAL-ADIN1110EBZ and the host computer
-  Open a serial terminal connected to the EVAL-ADIN1110EBZ Virtual COM port
-  Press the reset button on the EVAL-ADIN1110EBZ terminal, confirm that the welcome message is received and link is UP:
   "ADIN1100 Link Up" message received on terminal
   The LED_1 (orange/2.4V p-p mode) and LED_0 (green/link up) should also be ON.
-  Open a web browser (e.g. Mozilla Firefox) and enter the IP address of the board listed from the welcome message on the serial terminal (enter the 'info' command in terminal to display welcome message)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/webserver.png
   :align: center
   :width: 1000px

Frame Generator/Checker
-----------------------

To run the frame generator/checker demo (mode 9 ):

-  Connect a single twisted pair between the EVAL-ADIN1110EBZ and the EVAL-ADIN1100EBZ media converter (10BASE-T1L)
-  Connect a RJ45 cable from the media converter board to a Local Area Network, Host Computer or router. (10BASE-T)
-  Configure the EVAL-ADIN1100EBZ in MAC remote loopback (refer to the EVAL-ADIN1100EBZ User Guide)
-  EVAL-ADIN1110EBZ board, set the CFG switch to mode 9 (see Table 4)
-  Connect a micro-USB cable between the EVAL-ADIN1100EBZ media converter board and the host computer
-  Connect a micro-USB cable between the EVAL-ADIN1110EBZ and the host computer
-  Open a serial terminal connected to the EVAL-ADIN1110EBZ Virtual COM port
-  Press the reset button on the EVAL-ADIN1110EBZ terminal, confirm that the welcome message is received and link is UP:
   "ADIN1100 Link Up" message received on terminal
   The LED_1 (orange/2.4V p-p mode) and LED_0 (green/link up) should also be ON.
-  Enter the 'start' command
-  Enter the 'stop' command to stop the test
   The output should be as follow, note that the test stops automatically once 10,000 frames have been received:

| <fc #008000>start
| </fc><fc #4682b4>OK</fc>
| <fc #008000>MSE -37.2 dB Rx 0, Diff 0, Err 0
| MSE -37.2 dB Rx 500, Diff 0, Err 0
| MSE -37.2 dB Rx 1000, Diff 0, Err 0
| MSE -37.2 dB Rx 1500, Diff 0, Err 0
| MSE -37.2 dB Rx 2000, Diff 0, Err 0
| MSE -37.2 dB Rx 2500, Diff 0, Err 0
| MSE -37.2 dB Rx 3000, Diff 0, Err 0
| MSE -37.2 dB Rx 3500, Diff 0, Err 0
| MSE -37.2 dB Rx 4000, Diff 0, Err 0
| MSE -37.2 dB Rx 4500, Diff 0, Err 0
| MSE -37.2 dB Rx 5000, Diff 0, Err 0
| MSE -37.2 dB Rx 5500, Diff 0, Err 0
| MSE -37.2 dB Rx 6000, Diff 0, Err 0
| MSE -37.2 dB Rx 6500, Diff 0, Err 0
| MSE -37.2 dB Rx 7000, Diff 0, Err 0</fc>
| <fc #4682b4>stop</fc>
| <fc #008000>OK</fc>

Troubleshooting
~~~~~~~~~~~~~~~

As a general recommendation, check the jumper configuration and make sure they are all in default state as a starting point. Exception applies to the power selection on J1 that can be configured based on the required power source.

Serial Port can not be open on host
-----------------------------------

-  Make sure the FTDI drivers are installed
-  Check which virtual COM port has been assigned to the board on the device manager (windows OS). A simple way to check it is to unplug/plug the evaluation board and check the port number listed (e.g. COM1,COM2...)
-  If no device enumeration and no virtual COM port has been assigned on the device manager check the following:

   -  Power is applied to the EVAL- ADIN2111EBZ
   -  The EVAL- ADIN2111EBZ USB port is connected to the host computer

-  If a virtual COM port is assigned, check that no other application is using it

Command line interface not working
----------------------------------

-  Ensure sure the serial port can be opened properly as described in previous section
-  Verify that the serial COM port selected in the terminal is the one assigned to the evaluation board (see above)
-  Check the serial port baudrate, parity, start and stop bits settings are configured properly
-  Try perform a hardware reset, using the S501 button, this should display the Welcome Message
-  Double-Check the jumper settings, make sure that if the board is only powered from USB, J1 jumper is set accordingly.
-  Try to reprogram the board with the evaluation firmware

No link established (2-boards setup)
------------------------------------

-  Ensure the command line interface is working as described in previous section
-  Ensure that the EVAL-ADIN1110EBZ board and the link partner are powered properly
-  Ensure that the EVAL-ADIN1110EBZ onboard Microcontroller power supply selection (J302) and the onboard ADIN1110 power supply selection (J204) are the same (1.8V or 3.3V)
-  Ensure the ADIN1110 communication is working (Showns in the welcome message: SPI Access to ADIN1110:Success)
   \* If the SPI access to ADIN1110 reports a fault(from terminal welcome message), check that the ADIN1110 power rails selection is matching the intended transmit level set on S201 pin 4 (TX2P4_EN_N).

   -  Check that the SPI is configured to Open Alliance with protection on S201 pin 1 and 2

-  Ensure 10BASE-T1L cable is properly connected between P101 and the link partner board
-  Ensure that the hardware configuration is appropriate for the required linking arrangement.

   -  Transmit level mode are compatible between the 2 boards (using TX2P4_EN_N switch on S201)
   -  Recommendation to Disable Software Power Down after Reset, specially if using a custom firmware (SWPD_N ON on S201)
   -  Check the SPI Configuration on S201. The evaluation firmware uses Open Alliance SPI with protection enabled (SPI_CFG0 OFF, SPI_CFG1 OFF on S201)
   -  Measure and verify the voltage at various points on the EVAL-ADIN1110EBZ using the 3V3, 1V8, 1V1 test points.

Notes
~~~~~

**Legal Terms and Conditions**

By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed.

©2021 Analog Devices, Inc. All rights reserved. Trademarks and  registered trademarks are the property of their respective owners.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig1_t1l_adin1110.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig2_t1l_adin1110.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig3_t1l_adin1110.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig4_t1l_adin1110.png
