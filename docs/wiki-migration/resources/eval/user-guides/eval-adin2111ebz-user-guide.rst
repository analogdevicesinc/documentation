User Guide for EVAL-ADIN2111EBZ
===============================

.. container:: group

   
   General Description
   -------------------
   
   The EVAL-ADIN2111EBZ is a flexible platform enabling quick evaluation of the ADIN2111, robust, low power 10BASE-T1L 2-Port Ethernet switch. The evaluation board provides 2 10BASE-T1L channels with 10Mbit per second Single Pair Ethernet (SPE) connections reaching up to 1.7km of link distance. The ADIN2111 internal switch can be configured in store and forward mode between the two 10BASE-T1L channels and the SPI host. Cut through mode is also available between Port 1 and Port 2 and can be used without the need of the SPI host (unmanaged configuration).
   
   The evaluation board offers two modes of operation for maximum flexibility: Connected to a PC via USB port, the full set of ADIN2111 register settings and features such as link quality monitoring and diagnostics can be accessed over the USB using the serial command interface implemented in the evaluation firmware.
   
   Alternatively, the board can operate in cut-through mode between Port 1 and Port 2 (unmanaged configuration without firmware) where the EVAL-ADIN2111EBZ acts as a network switch forwarding packets between the 2x 10BASE-T1L ports. The 2x links are configured by setting the ADIN2111 hardware configuration pins jumper and switches. The 2x On-board Activity LEDs provide Link activity status indication for each port.
   
   Custom firmware can also be developed and the ADIN2111 driver support package includes simple project examples to start a custom implementation.
   
   The SPI interface provides access to the management registers required for the switch configuration, the 2 PHYs configuration and data exchange between SPI host and ports.

   
   |image1|

   .. container:: centeralign

      //Figure 1. //

   
   Features
   ~~~~~~~~
   
   -  User friendly access to all ADIN2111 features
   -  Stand-alone hardware configured operation
   -  On-board ARM Cortex-M4 STM32L4S5QII3P ultra-low-power Microcontroller
   
   Equipment Needed
   ~~~~~~~~~~~~~~~~
   
   -  Link partner with 10BASE-T1L interface
      Recommended to use the EVAL-ADIN1100EBZ Evaluation Board (RJ45 Ethernet interface to use as media converter between 10BASE-T1L and 10BASE-T)
   -  2x 10BASE-T1L compatible Single Pair cable: max. 1.5 mm² / AWG 16 to fit screw terminal connector
   -  Power supply source: 5 to 32 Vdc, 0.6W, or USB as power for the board
   -  Optional: PC running Windows 7 and upwards with USB interface
   -  Optional: ST-LINK programmer
   


Evaluation Kit Contents
-----------------------

-  EVAL-ADIN2111EBZ board
-  3x plug-in screw-terminal connectors for 10BASE-T1L cable and external power supply
-  USB-A to Mini USB-B cable (1 meter)

Software (Optional)
-------------------

-  FTDI USB Virtual Com Port driver (Available from FTDI website)
-  Serial port terminal software (e.g. CompuPhase Termite)

Documentation Needed
--------------------

-  ADIN2111 Datasheet available from the product webpage: :adi:`adin2111.html <en/products/adin2111.html>`
-  EVAL-ADIN1100EBZ User Guide: :doc:`adin1100_userguide </wiki-migration/resources/eval/user-guides/adin1100_userguide>`

--------------

Overview
~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adin2111ebz_revc_overview.png
   :align: center

Hardware
~~~~~~~~

Power Supplies
--------------

The EVAL-ADIN2111EBZ can be powered from three different sources:

-  5-32V DC external power supply connected to P1 terminal bock or P2 barrel connector
-  USB (5V DC) using the P5 usb-mini connector

| The power supply source can be configured using the P4 "BOARD POWER" link (3-positions: USB, EXT, GND).
| Note that the two power supplies can be simultaneously enabled on P1 (2 jumpers inserted) as an internal common cathode diodes circuit selects the highest voltage source.

| The selected input power source is converted by the step-down converter U501 (LT8619) to 3.3V
| The link J2 is used to connect U2 output to the main 3.3V supply rail used on the board
| The green “PWR” LED1 is ON when the 3.3V rail is present.
| The board power consumption depends on the mode of operation, with the maximum of approximately 0.5W.

10BASE-T1L Cable Connection
---------------------------

The 10BASE-T1L cable can be connected via pluggable screw-terminal block to connector P101. If more of the pluggable connectors are needed, for easy connecting / changing cables, additional connectors can be purchased from the vendor or distributors:

-  Manufacturer: Phoenix Contact
-  Manufacturer part number: 1803581
-  Description: “Pluggable Terminal Block, 3.81 mm, 3 Ways, 28AWG to 16AWG, 1.5 mm², Screw”.

Ground Connections
------------------

The demo board has two “Earth nodes”, one for each port. We call it “Earth node” here – though this node may or may not be electrically connected to Earth ground. In a real device this node would be typically connected to the device metal housing / chassis. Each Earth node can be connected as required in a wider demo system via “Earth” terminal of the power supply connector P1, or via exposed metal plating of 2 mounting holes in the left corners of the board. (The 3rd and 4th holes on the right do not have metal plating, and also no Earth connection.)

The shield of the 10BASE-T1L cables can be disconnected from this Earth node, connected directly, or connected via a 4x 1nF capacitors array for Port 1 (C85,C86,C87,C88) and Port 2 (C89,C92,C93,C95). The required connection is selected using jumper J101 (Port 1) and P22 (Port 2).

**(!) Note: The EVAL-ADIN2111EBZ has been designed only as an Evaluation board. It has NOT been designed, and it has NOT been tested for electrical safety. Any equipment, device, wire, or cable connected to this demo must be already protected and safe to touch without danger of electric shock.**

Hardware Configuration Setup
----------------------------

The EVAL-ADIN2111EBZ board is provided with links (jumper) and DIP switches that can be used to set the ADIN2111 configuration. The Table 1,2 and 3 describe the links and switches functions.

**Table 1. Board Link Configuration**

+------------+--------------+---------------------------------------------------------------------------------------------+
| Link       | Default      | Description                                                                                 |
| Ref.       | Position     |                                                                                             |
+============+==============+=============================================================================================+
| J101       | Earth        | CH1 Shield shorted either directly to Earth, or via 4nF cap                                 |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P22        | Earth        | CH2 Shield shorted either directly to Earth, or via 4nF cap                                 |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P4         | EXT          | USB – Connects 5V USB supply to the input of the LT8619                                     |
|            |              | EXT - Connects externally supplied power from P1 or P2 to the input of LT8619               |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P10        | Burst        | FORCED CURRENT – (H) Force Continuous mode of operation of LT8619                           |
|            |              | PULSE SKIP (o/c) - Pulse-Skipping mode of operation of LT8619                               |
|            |              | BURST (L) – Burst mode of operation of LT8619                                               |
+------------+--------------+---------------------------------------------------------------------------------------------+
| J2         | Inserted     | This link supplies 3.3V rail to circuitry on the board, beyond the LT8619                   |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P11        | 3V3          | STM32 supply voltage – choice of 3.3V or 1.8V                                               |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P13        | 3V3          | AVDD_H supply voltage – 3.3V (1.8V to be supported in final product)                        |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P14        | 3V3          | AVDD_L supply voltage – choice of 3.3V or 1.8V                                              |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P15        | 3V3          | VDDIO supply voltage – choice of 3.3V or 1.8V                                               |
+------------+--------------+---------------------------------------------------------------------------------------------+
| DLDO_1V1_A | DLDO_1V1     | DVDD_A supply voltage – choice of EXT 1V1 rail or internally generated DLDO_1V1             |
+------------+--------------+---------------------------------------------------------------------------------------------+
| DLDO_1V1_B | DLDO_1V1     | DVDD_B supply voltage – choice of EXT 1V1 rail or internally generated DLDO_1P1             |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P19        | Not Inserted | Option to short AVDD_H to AVDD_L                                                            |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P20        | Not Inserted | Option to short AVDD_L to VDDIO                                                             |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P8         | LES_RST      | Option to hold STM32 in reset (GND RESET) or short it to the S5 push-button reset (LES_RST) |
+------------+--------------+---------------------------------------------------------------------------------------------+
| P25        | RESET_N      | Option to hold LES in reset (GND RESET) or short it to the RESET_N signal                   |
+------------+--------------+---------------------------------------------------------------------------------------------+

\**Table 2. ADIN2111 SPI Configuration , Schematics Ref. S1 \*\*

======== ======== ======== ================================
Switch   Switch   Default  Description
Position Name     Position 
======== ======== ======== ================================
1        SPI_CFG1 ON       SPI configuration 1
                           OFF: Generic SPI
                           ON: Open Alliance SPI
2        SPI_CFG0 OFF      SPI configuration 0
                           OFF: SPI CRC/Protection enabled.
                           ON: SPI CRC/Protection disabled
======== ======== ======== ================================

\**Table 3. ADIN2111 Transmit Level Configuration , Schematics Ref. S2 \*\*

======== ============= ======== ==================================
Switch   Switch        Default  Description
Position Name          Position 
======== ============= ======== ==================================
1        P2_TX2P4_EN_N OFF      Port 2 Transmit 2.4V disable
                                OFF: TX level 2.4V p-p or 1.0V p-p
                                ON: TX level 1.0V p-p only
2        P1_TX2P4_EN_N OFF      Port 1 Transmit 2.4V disable
                                OFF: TX level 2.4V p-p or 1.0V p-p
                                ON: TX level 1.0V p-p only
======== ============= ======== ==================================

\**Table 4. ADIN2111 Software Power Down After Reset Configuration , Schematics Ref. S3 \*\*

======== ============ ======== ======================================
Switch   Switch       Default  Description
Position Name         Position 
======== ============ ======== ======================================
1        P2_SWPD_EN_N OFF      Port 2 Software Power Down After Reset
                               OFF: Disabled
                               ON: Enabled
2        P1_SWPD_EN_N OFF      Port 1 Software Power Down After Reset
                               OFF: Disabled
                               ON: Enabled
======== ============ ======== ======================================

**Table 3. Board LED indicators**

+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Name             | Colour                 | Schematics | Description                                                                                                                                 |
| (silkscreen)     |                        | Ref.       |                                                                                                                                             |
+==================+========================+============+=============================================================================================================================================+
| PWR              | <fc #008000>GREEN</fc> | LED1       | \* OFF: 3.3V board power supply not available                                                                                               |
|                  |                        |            | ON: 3.3V board power supply available                                                                                                       |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| DEBUG            | <fc #4682b4>BLUE</fc>  | DS5        | Firmware heart beat                                                                                                                         |
|                  |                        |            | \* OFF: No firmware activity, reset or reprogram the board                                                                                  |
|                  |                        |            | \* Blinking: firmware running                                                                                                               |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| MOD              | <fc #ff0000>RED</fc>   | D10        | Microcontroller Mode LED                                                                                                                    |
|                  | <fc #008000>GREEN</fc> |            | Modes 6,14 - TCP/IP stack enabled with fixed IP:                                                                                            |
|                  |                        |            | \* <fc #008000>GREEN LED </fc> always ON                                                                                                    |
|                  |                        |            | \* <fc #ff0000>RED LED</fc> not used                                                                                                        |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|                  |                        |            | *Modes 7,15 - TCP/IP stack enabled with fixed DHCP*                                                                                         |
|                  |                        |            | \* <fc #008000>GREEN ON</fc>: IP assigned                                                                                                   |
|                  |                        |            | \* <fc #008000>GREEN blinking</fc>: waiting for IP assignment from DHCP server                                                              |
|                  |                        |            | \* <fc #ff0000>RED LED</fc> not used                                                                                                        |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|                  |                        |            | *Modes 8,9 - Frame Generator/Frame Checker*                                                                                                 |
|                  |                        |            | \* <fc #008000>GREEN OFF</fc>: No activity                                                                                                  |
|                  |                        |            | \* <fc #008000>GREEN ON</fc>: 10,000 packets transmitted and received with no error (err) or mismatched number of packets received (diff)   |
|                  |                        |            | \* <fc #ff0000>RED LED</fc> not used                                                                                                        |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| NET              | <fc #ff0000>RED</fc>   | D11        | Error LED                                                                                                                                   |
|                  | <fc #008000>GREEN</fc> |            |                                                                                                                                             |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|                  |                        |            | *All modes*                                                                                                                                 |
|                  |                        |            | \* <fc #ff0000>RED OFF </fc> No issue                                                                                                       |
|                  |                        |            | \* <fc #ff0000>RED ON </fc> Potential SPI communication error with ADIN2111 (see terminal message). Check power and SPI configuration on S1 |
|                  |                        |            | \* <fc #008000>GREEN LED </fc> not used                                                                                                     |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|                  |                        |            | *Modes 8,9 Only: Frame Generator/Frame Checker*                                                                                             |
|                  |                        |            | \* <fc #ff0000>RED OFF</fc>: No transmission error (err) or mismatch in number of packets received (diff)                                   |
|                  |                        |            | \* <fc #ff0000>RED ON</fc>: Transmission error (err) or mismatch in number of packets received (diff)                                       |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ACTIVITY_P2_LED0 | <fc #008000>GREEN</fc> | DS1        | PORT 2 Link Activity LED                                                                                                                    |
|                  |                        |            | \* ON or blinking: Link activity                                                                                                            |
|                  |                        |            | \* OFF: No link activity                                                                                                                    |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ACTIVITY_P1_LED0 | <fc #008000>GREEN</fc> | DS6        | PORT 2 Link Activity LED                                                                                                                    |
|                  |                        |            | \* ON or blinking: Link activity                                                                                                            |
|                  |                        |            | \* OFF: No link activity                                                                                                                    |
+------------------+------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Microcontroller Modes of operation
----------------------------------

The EVAL-ADIN2111EBZ can be used in various modes of operations implemented in the uC firmware. Up to 16 modes of operations can be selected by setting the 4 positions of the slide switch S4. The selected configuration is latched after the board is powered up or reset.

Therefore, to change the mode of operation, the board must be reset by pressing “RESET” button S5 or by applying power cycle after changing the position of the slide switch S4. The available modes of operation are described in Table 4 below.

**Table 4. Firmware Modes of Operation, Schematics Ref. S4**

+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CFG             | Mode | Operating Mode\ :sup:`ii`                               | Description                                                                                                                                                        |
| [3:0]\ :sup:`i` | No.  |                                                         |                                                                                                                                                                    |
+=================+======+=========================================================+====================================================================================================================================================================+
| 0000            | 15   | TCP/IP Stack & Web Server, DHCP client,                 | In this mode, the TCP/IP stack can be managed via UART using dynamic IP address allocation.                                                                        |
|                 |      | MAC Addr1                                               | The media converter board is then used to convert 10BASE-T1L to 10BASE-T ethernet, for which common web browsers can be used to access the associated information. |
|                 |      |                                                         | MAC address 1 is used.                                                                                                                                             |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0001            | 14   | TCP/IP Stack & Web Server, Fixed IP,                    | This is a similar mode to the previous one except fixed IP address allocation is used.                                                                             |
|                 |      | MAC Addr1                                               | MAC address 1 is used.                                                                                                                                             |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0010            | 13   | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0011            | 12   | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0100            | 11   | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0101            | 10   | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0110            | 9    | PHY2 Frame Generator Checker / PHY1 MAC Remote Loopback | PHY2 is set in Frame Generator/Checker Mode                                                                                                                        |
|                 |      | MSE reading enabled                                     | PHY1 is set in MAC Interface Remote loopback mode                                                                                                                  |
|                 |      |                                                         | MSE readings are shown on UART. Link LED is also enabled.                                                                                                          |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0111            | 8    | PHY1 Frame Generator Checker / PHY2 MAC Remote Loopback | PHY1 is set in Frame Generator/Checker Mode                                                                                                                        |
|                 |      | MSE reading enabled                                     | PHY2 is set in MAC Interface Remote loopback mode                                                                                                                  |
|                 |      |                                                         | MSE readings are shown on UART. Link LED is also enabled.                                                                                                          |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1000            | 7    | TCP/IP Stack & Web Server, DHCP client,                 | The use of this mode is depicted in Figure 11. In this mode, the TCP/IP stack can be managed via UART using dynamic IP address allocation.                         |
|                 |      | MAC Addr2                                               | The media converter board is then used to convert 10BASE-T1L to 10BASE-T ethernet,                                                                                 |
|                 |      |                                                         | for which common web browsers can be used to access the associated information.                                                                                    |
|                 |      |                                                         | MAC address 2 is used.                                                                                                                                             |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1001            | 6    | TCP/IP Stack & Web Server, Fixed IP,                    | This is a similar mode to the previous one except fixed IP address allocation is used.                                                                             |
|                 |      | MAC Addr2                                               | MAC address 2 is used.                                                                                                                                             |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1010            | 5    | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1011            | 4    | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1100            | 3    | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1101            | 2    | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1110            | 1    | RESERVED                                                | The uC makes no autonomous attempt to interact with the ADIN2111                                                                                                   |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1111            | 0    | Reset ADIN2111                                          | Keep the ADIN2111 in reset mode                                                                                                                                    |
+-----------------+------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| :sup:`I` //Switch in ON position = signal logic 0 for microcontroller (shorted to ground).
| Switch in OFF position = signal logic 1 (pulled up by a resistor) //

:sup:`II` *RESERVED means the microcontroller and command line interface is active (serial port).*

Software
~~~~~~~~

| The EVAL-ADIN2111EBZ can be used as a stand-alone board, with the firmware already pre-programmed in the microcontroller flash memory.
| The mode of operation can be set using the S4 Configuration DIP switch and the link status is indicated by LEDs. There is no software required for this stand-alone use case.

The EVAL-ADIN2111EBZ can also be interfaced with a host computer via the USB port. The full set of ADIN2111 PHY and MAC registers and features such as link quality monitoring can be accessed via the command line interface.

<fc #ff0000>Note that the default firmware is configured with the SPI interface set to OPEN Alliance SPI with Protection enabled. The ADIN2111 hardware configurations pins must be set accordingly using the DIP switch S1 (see table 2 for reference).</fc>

Driver For USB COM Port
-----------------------

The EVAL-ADIN2111EBZ has an onboard USB-UART converter (FTDI FT232R).

Ensure that the appropriate Virtual Com Port driver is installed on the host platform before connecting the EVAL-ADIN2111EBZ to the host computer via the USB cable.

The drivers are available from FTDI, at the time of writing this document at https://ftdichip.com/drivers/vcp-drivers/

COM Port and Terminal Settings
------------------------------

When the EVAL-ADIN2111EBZ is connected to the host, it will become available in the host system as a USB Com Port, and will be assigned a com port number. The number will depend on the system settings, on com port devices previously connected and assigned in the system, and on the FTDI driver settings.

The EVAL-ADIN2111EBZ microcontroller communicates over a standard UART interface, with the following settings:

-  Baudrate: 115200
-  Data Bits: 8
-  Stop Bits: 1
-  Parity: none

The protocol is based on ASCII text commands and messages. Each message sent from the firmware to the host is finished by both <CR> and <LF> characters. For the commands received from host the firmware expects <CR>, <LF> or <CR> + <LF>.

(//For information: <CR> .. “carriage return”, ASCII code 0x0D, <LF> .. “line feed”, ASCII code 0x0A //)

Terminal Commands and Messages
------------------------------

The EVAL-ADIN2111EBZ firmware works with the common serial terminals. It has been tested on Windows platform with PuTTY, RealTerm, Termite and Hyperterminal. (*The examples in this document were captured using Compuphase Termite*).

Initial Welcome Message
-----------------------

| When the EVAL-ADIN2111EBZ is correctly connected via the USB Virtual COM Port using the terminal software, the firmware sends an initial welcome message as displayed below.
| Note that a hardware reset of the board (using S5 "RESET" button) or the 'info' command will also display the welcome message. This can be useful to check the ADIN2111 information and link status.

| <fc #008000>================================================
| ANALOG DEVICES 10BASE-T1L Demo Serial Interface
| ================================================
| (c) 2021 Analog Devices Inc. All rights reserved
| ================================================
| Firmware ver.: 1.2.1
| Board Name: EVAL-ADIN2111EBZ
| Board revision: B
| Board Serial Number: 12345
| uC CFG3-2-1-0: ON-OFF-OFF-OFF (Mode 7)
| Board Configuration:TCP/IP Stack+WebServer,DHCP,MAC Addr2
| SPI Access to ADIN2111: Success
| MAC address: 00:e0:22:fe:da:ca
| IP Address: not assigned
| CH1 Link status: Down
| Master/Slave: Not run
| Tx Level: Not run
| CH2 Link status: Down
| Master/Slave: Not run
| Tx Level: Not run
| ================================================
| Type '<?><new line>' for a list of commands
| ================================================</fc>
| ==== Terminal Commands ====

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Command       | Description                                                                                                                                | Use                                                                 |
+===============+============================================================================================================================================+=====================================================================+
| macwrite      | Write in MAC registers.                                                                                                                    | <fc #008000>macwrite <RegAddress>,<Data><newLine></fc>              |
|               | <regAddress> and <Data> in hex                                                                                                             |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| macread       | Read MAC registers.                                                                                                                        | <fc #008000>macread <RegAddress><newLine></fc>                      |
|               | <regAddress> in hex                                                                                                                        |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| phywrite      | Write in PHY registers.                                                                                                                    | <fc #008000>phywrite <PortNumber>,<RegAddress>,<Data><newLine></fc> |
|               | <PortNumber>, <regAddress> and <Data> in hex                                                                                               |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| phyread       | Read in PHY registers.                                                                                                                     | <fc #008000>phyread <PortNumber>,<RegAddress>,<Data><newLine></fc>  |
|               | <PortNumber> and <regAddress> in hex                                                                                                       |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| machwreset    | ADIN2111 Hardware Reset                                                                                                                    | <fc #008000>machwreset<newLine></fc>                                |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| macswreset    | ADIN2111 Software Reset                                                                                                                    | <fc #008000>macswreset<newLine></fc>                                |
|               | Similar to hardware reset without the power up sequence                                                                                    |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changemac     | Change MAC address.                                                                                                                        | <fc #008000>changemac <xx>:<xx>:<xx>:<xx>:<xx>:<xx><newLine></fc>   |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | All digits in hex                                                                                                                          |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changeip      | Change IP address.                                                                                                                         | <fc #008000>changeip <xxx>.<xxx>.<xxx>.<xxx><newLine></fc>          |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | <xxx> digits in dec                                                                                                                        |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changegw      | Change gateway, all numbers in dec.                                                                                                        | <fc #008000>changegw <xxx>.<xxx>.<xxx>.<xxx><newLine></fc>          |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | <xxx> digits in dec                                                                                                                        |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changenm      | Change network mask,all numbers in dec.                                                                                                    | <fc #008000>changenm <xxx>.<xxx>.<xxx>.<xxx><newLine></fc>          |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | <xxx> digits in hex                                                                                                                        |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changebrdname | Change board name.                                                                                                                         | <fc #008000>changebrdname <custom text><newLine></fc>               |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | Warning: Predefined in factory. Lost if overwritten                                                                                        |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changebrdrev  | Change board revision                                                                                                                      | <fc #008000>changebrdrev <custom text><newLine></fc>                |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | Warning: Predefined in factory. Lost if overwritten                                                                                        |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| changebrdsn   | Change board serial number                                                                                                                 | <fc #008000>changebrdsn <custom text><newLine><newLine></fc>        |
|               | Applies after 'savetoflash' and reset.                                                                                                     |                                                                     |
|               | Warning: Predefined in factory. Lost if overwritten.                                                                                       |                                                                     |
|               | Serial Number matches the label on the bottom of the board                                                                                 |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| eraseflash    | Erase the internal flash memory.                                                                                                           | <fc #008000>eraseflash<newLine></fc>                                |
|               | Warning:resets the board parameters to default values                                                                                      |                                                                     |
|               | Also erases board name,board serial number and board revision                                                                              |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| savetoflash   | Save configuration to flash.                                                                                                               | <fc #008000>savetoflash<newLine></fc>                               |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| reset         | Microcontroller software reset.                                                                                                            | <fc #008000>reset<newLine></fc>                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| start         | Start sending periodic diagnostics.                                                                                                        | <fc #008000>start<newLine></fc>                                     |
|               | Also provide statistics when used in Frame Generator\\checker mode (9)                                                                     |                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| stop          | Stop sending periodic diagnostics.                                                                                                         | <fc #008000>stop<newLine></fc>                                      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| clear         | Clear/reset the diagnostics counters                                                                                                       | <fc #008000>clear<newLine></fc>                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| mode          | Overwrite the board mode in software. After MCU reset or board reset, the mode is set to hardware configuration defined by the switch S303 | <fc #008000>mode <number><newLine></fc>                             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| modes         | List the board modes available                                                                                                             | <fc #008000>modes<newLine></fc>                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| info          | Display the board information (welcome message)                                                                                            | <fc #008000>info<newLine></fc>                                      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| getbuildnb    | Get the firmware build number                                                                                                              | <fc #008000>getbuildnb<newLine></fc>                                |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| ?             | Display the list of commands available                                                                                                     | <fc #008000>?<newLine></fc>                                         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

Microcontroller Firmware Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The microcontroller (STM32L4S5QII3P) is programmed out-of-the box with the evaluation firmware. A binary image of the production firmware is also available to download from the ADIN2111 product webpage. The default behavior of the configuration switches based on the pre-loaded firmware is listed in Table 4. The revision of the programmed firmware can be checked using the serial terminal program and pressing the RESET button (S5) which will display the welcome message.

Using the Microcontroller bootloader
------------------------------------

-  In STM32CubeProgrammer, set the interface to UART
-  Set the serial port settings

   -  Set the serial port number to the one identified in previous section (refresh port list using the circle arrow icon)
   -  Baudrate: 115200
   -  Data Bits:8
   -  Parity: Even
   -  Flow Control: OFF
   -  RTS: 0
   -  DTR:0
   -  Read Unprotect (MCU): Not selected

-  Open the **Erasing and programming** menu
-  Browse and select the firmware image file from your download location: eval-adin2111ebz-1_2_1.hex (or any more up to date version)

   -  Click **Open**

-  Reboot the Microcontroller in Programming Mode:

   -  Press and hold the S6 “BOOT” and S5 “RESET” buttons simultaneously on the board
   -  Release S5 “RESET” button while holding the S6 “BOOT” button, release S6 “BOOT” after 1s.
   -  The Board is now in programming mode, the microcontroller LEDs (DS5,D10,D11) should be OFF

-  Click **Connect**. If Connect fails, check that the Serial COM port is correct as described in **Identify the Serial COM Port** section. Also make sure no serial terminal are connected to the serial port in use.

   -  Check that the target status is “CONNECTED” as marked on Figure 8 (top right corner).

-  Un-tick the **Run After Programming** option and make sure **Verify programming** is ticked
-  Click the **Start Programming** button
-  Wait for the programming to be completed (~35s) , Check that the blue progress bar is 100%
-  A message box appears: **File download completed**, click OK
-  Wait for ~30s. A message box pops up: **Download verified successfully**. Click OK
-  Click the **Disconnect** button
-  Power cycle the board by unplugging and plugging in the USB cable and any other power supply connected.

   -  All MCU LEDs (DS5-BLUE, D10-RED,D11-RED) flash once (LED health check)
   -  “DEBUG” LED (BLUE) is continuously blinking while firmware is running (Board Heart Beat)

Using the ST-LINK JTAG programmer
---------------------------------

| The ST-LINK JTAG programmer provides a robust solution for programming and debugging source code. It is also faster to program the microcontroller using the JTAG interface.

-  Connect the ST-LINK programmer to the EVAL-ADIN2111EBZ using the ARM-20 JTAG connector P3
-  Select the ST-LINK interface in previous STEP 1 and follow the same instructions to program the board with the provided firmware.

|image2|

.. container:: centeralign

   \ *Figure 4. STM32CubeProgrammer*\


Application Quick Start
~~~~~~~~~~~~~~~~~~~~~~~

Demo Web Page
-------------

| The EVAL-ADIN2111EBZ firmware runs a webserver that can be used to access the Demo webpage to visualize the board information and link status for each port.
| This feature demonstrates how the 10BASE-T1L Low Complexity Ethernet Switch can be connected to a 10BASE-T network and accessed using conventional HTTP requests.
| A media converter board (e.g. **EVAL-ADIN1100EBZ**, see the user guide for more details) is required to interface the
| **EVAL-ADIN2111EBZ** to a 10BASE-T network (using RJ45 cable).
| A simple setup is shown below:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adin2111ebz_demo_setup.png
   :align: center

To run the webpage demo (DHCP, mode 7):

-  Connect a single twisted pair between the EVAL-ADIN2111EBZ PORT1 or PORT2 and the EVAL-ADIN1100EBZ media converter (10BASE-T1L). PORT1 is used in this demonstration.
-  Connect a RJ45 cable from the media converter board to a Local Area Network, Host Computer or router. (10BASE-T)
-  Configure the EVAL-ADIN1100EBZ in media converter mode with support for 2.4V p-p transmit level (refer to the EVAL-ADIN1100EBZ User Guide)
-  Set the CFG switch to mode 7 on the EVAL-ADIN2111EBZ board (see Table 4, mode 7 is the shipping configuration, alternatively the “mode 9” command can be entered in the EVAL-ADIN2111EBZ terminal while the firmware is running, this will be overridden by the configuration switch if the board is reset)
-  Connect a USB-micro cable between the EVAL-ADIN1100EBZ media converter board and the host computer
-  Connect a USB-mini cable between the EVAL-ADIN2111EBZ and the host computer
-  Open a serial terminal connected to the EVAL-ADIN2111EBZ Virtual COM port
-  Press the reset button on the EVAL-ADIN2111EBZ terminal, confirm that the welcome message is received and link is UP: 10BASE-T1L CH1 Link-Up received on ADIN2111 terminal
-  Open a web browser (e.g. Mozilla Firefox) and enter the IP address of the board listed from the welcome message on the serial terminal. If the IP is not listed yet, enter the 'info' command in terminal to display the welcome message). Note that the "MOD" LED D10 will flash green while waiting for the IP to be assigned by the DHCP server. Once the IP is assigned, D10 stops blinking and stays ON Green. // //

The webpage shows basic information about the board, the MSE and link parameters for each channel. The page is auto-refreshed every 5s. After a long period of time, if the page is hung a simple reset of the EVAL-ADIN2111EBZ will reload the page properly.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adin2111ebz_demo_webpage.png
   :align: center

Frame Generator/Checker
-----------------------

To run the frame generator/checker demo (mode 9 using Port 1):

-  Connect a single twisted pair between the EVAL-ADIN2111EBZ Port 1 and the EVAL-ADIN1100EBZ media converter (10BASE-T1L)
-  Connect a RJ45 cable from the media converter board to a Local Area Network, Host Computer or router. (10BASE-T)
-  Configure the EVAL-ADIN1100EBZ in MAC remote loopback (refer to the EVAL-ADIN1100EBZ User Guide)
-  Set the EVAL-ADIN2111EBZ board CFG switch to mode 9 (see Table 4), (alternatively the "mode 9" command can be entered in the EVAL-ADIN2111EBZ terminal while the firmware is running, this will be overridden by the configuration switch if the board is reset)
-  Set the EVAL-ADIN1100EBZ board CFG switch to mode 13 (MAC Interface remote loopback, see EVAL-ADIN1100EBZ user guide), (alternatively the "mode 13" command can be entered in the EVAL-ADIN1100EBZ terminal while the firmware is running, this will be overridden by the configuration switch if the board is reset)
-  Connect a USB-micro cable between the EVAL-ADIN1100EBZ media converter board and the host computer
-  Connect a USB-mini cable between the EVAL-ADIN2111EBZ and the host computer
-  Open a serial terminal connected to the EVAL-ADIN2111EBZ Virtual COM port
-  Press the reset button on the EVAL-ADIN2111EBZ terminal, confirm that the welcome message is received and link is UP:
   10BASE-T1L CH1 Link-Up received on ADIN2111 terminal
   \* Enter the 'start' command
-  Enter the 'stop' command to stop the test
   The output should be as follow, note that the test stops automatically once 10,000 frames have been received:

| <fc #008000>start
| </fc><fc #4682b4>OK</fc>
| <fc #008000>CH1 -37.2 dB,CH2 MSE n/a , Rx 0, Diff 0, Err 0
| CH1 -37.2 dB,CH2 MSE n/a , Rx 0, Diff 0, Err 0
| CH1 -37.2 dB,CH2 MSE n/a , Rx 0, Diff 0, Err 0
| CH1 -37.2 dB,CH2 MSE n/a , Rx 0, Diff 0, Err 0
| CH1 -37.2 dB,CH2 MSE n/a , Rx 0, Diff 0, Err 0 </fc>
| <fc #4682b4>stop</fc>
| <fc #008000>OK</fc>

Troubleshooting
~~~~~~~~~~~~~~~

As a general recommendation, check the jumper configuration and make sure they are all in default state as a starting point. Exception applies to the power selection on P4 that can be configured based on the required power source.

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
-  Try perform a hardware reset, using the reset button (S5), this should display the Welcome Message
-  Double-Check the jumper settings, make sure that if the board is only powered from USB, P4 jumper is set accordingly.
-  Try to reprogram the board with the evaluation firmware

No link established (2-boards setup)
------------------------------------

-  Ensure the command line interface is working as described in previous section
-  Ensure that the EVAL-ADIN2111EBZ board and the link partner are powered properly
-  Ensure that the EVAL-ADIN2111EBZ onboard Microcontroller power supply selection (P11) and the onboard ADIN2111 AVDD_H power supply selection (P13) are the same (1.8V or 3.3V)
-  Ensure the ADIN2111 communication is working (Shown in the welcome message: SPI Access to ADIN2111:Success)
   \* If the SPI access to ADIN2111 reports a fault(from terminal welcome message), check that the ADIN2111 power rail selection is matching the intended transmit level set for both ports on S2. If S2 enables 2.4V p-p transmit level on one of the port, AVDD_H rail must be powered from 3.3V.

   -  Check that the SPI is configured to Open Alliance with protection on S1 pin 1 and 2

-  Ensure 10BASE-T1L cable is properly connected between P101 (Port 1) or P21 (Port 2) and the link partner board
-  Ensure that the hardware configuration is appropriate for the required linking arrangement.

   -  Transmit level mode are compatible between the local device and the link partner
   -  Recommendation to Disable Software Power Down after Reset on both ports, specially if using a custom firmware (P1_SWPD_EN_N=OFF, P2_SWPD_EN_N=OFF on S3 switch)
   -  Check the SPI Configuration on S1. The evaluation firmware uses Open Alliance SPI with protection enabled (SPI_CFG0=OFF, SPI_CFG1=ON on S1 switch)
   -  Measure and verify the voltage at various points on the EVAL-ADIN2111EBZ using the 3V3, 1V8, 1V1 test points.

Notes
~~~~~

**Legal Terms and Conditions**

By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed.

©2021 Analog Devices, Inc. All rights reserved. Trademarks and  registered trademarks are the property of their respective owners.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adin2111ebz_simplified_block_diagram.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stm32cubeprogrammer.png
   :width: 800px
