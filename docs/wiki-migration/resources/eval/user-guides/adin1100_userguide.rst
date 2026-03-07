User Guide for EVAL-ADIN1100EBZ
===============================

ADIN1100 10BASE-T1L Ethernet PHY Evaluation Kit Media Converter to 10BASE-T with ADIN1200 Ethernet PHY
------------------------------------------------------------------------------------------------------

General Description
~~~~~~~~~~~~~~~~~~~

The EVAL-ADIN1100EBZ is a flexible platform enabling quick evaluation of ADIN1100, robust, low power 10BASE-T1L PHY. It provides 10Mbit per second Single Pair Ethernet (SPE) connections with devices over 1.7km of cable. The evaluation board offers two modes of operation for maximum flexibility. Connected to a PC via USB port, the full set of ADIN1100 register settings and features such as link quality monitoring and diagnostics can be accessed with the ADIN1100 Graphical User Interface software. Alternatively, the board can operate in stand-alone mode where it is configured by setting hardware configuration links and switches. Onboard LEDs provide status indication. The ADIN1100 data (MII, RMII and RGMII) and management (MDIO) interfaces are accessible on header connectors for easy connection to an external host controller. A small prototyping area and test points are provided for experimentation with alternative cable connection topologies including isolation transformers and/or power coupling inductors. The platform can perform as a 10BASE T1L to 10BASE-T media converter. This enables connection to other devices – demos or a custom prototypes – with a 10BASE-T1L Ethernet port and conversion of the data to standard Ethernet accessible via the RJ45 connector.


|image1|

.. container:: centeralign

   \ *Figure 1. EVAL-ADIN1100-EBZ – Simplified Block Diagram*\


.. container:: group

   
   .. container:: half column

         
         **Features**

         
         -  User friendly access to all ADIN1100 features
         -  Graphical user interface (GUI) software on PC
         -  or stand-alone hardware configured operation
         -  Flexible power supplies and prototyping options
         -  On-board ARM Cortex-M ADuCM4050 Microcontroller
         -  10BASE-T1L to 10BASE-T Media Converter
         
         **Equipment Needed**

         
         -  Link partner with 10BASE-T1L interface
         -  10BASE-T1L compatible Single Pair cable
         -   max. 1.5mm2 / AWG 16 to fit screw terminal connector
         -  Power supply source
         -  5 to 32 Vdc, 0.6W, or USB as power for the board
         -  Optional: Link partner with standard RJ45 Ethernet interface
         -  Auto-negotiation resolving to 10BASE-T Full Duplex
         -  Optional: PC running Windows 7 and upwards with USB interface
         

   
   .. container:: half column

         
         **Evaluation Kit Contents**

         
         -  EVAL-ADIN1100EBZ board
         -  2x plug-in screw-terminal connectors
         -  for 10BASE-T1L cable and external power supply
         -  Cat5e Ethernet cable with RJ45 connectors (1 meter)
         -  USB-A to Micro USB-B cable (1 meter)
         
         **Software (Optional)**

         
         -  ADIN1100 Graphical User Interface software package
         -  FTDI USB Virtual Com Port driver for selected host
         -  Serial port terminal software
         
         **Document Needed**

         
         -  ADIN1100 Datasheet
         

   


--------------

Hardware
~~~~~~~~

Power Supplies
^^^^^^^^^^^^^^

The EVAL-ADIN1100EBZ can be powered by a power supply with output voltage between 5 to 32V DC connected via the plug-in screw-terminal connector P1, or via the P2 barrel connector plug. Alternatively, the board can be powered from a host via its USB port, or by a USB charger connected to the micro-USB connector P401. The power supply source can be selected by link on J1 “BOARD PWR SELECTION”. Inserting link in position “USB” enables the board to receive power from USB connector. Inserting link in position “PWR+EXT+” enables the board to receive power from connectors P1 and P2. If both J1 “BOARD PWR SELECTION” “USB and “PWR+EXT+” links are inserted, there is a “diode or” implemented on the input of J1, and the supply with a higher voltage will supply the board. The power from the source is converted by a step-down converter U501 LT8619EDD#PBF to 3.3V, and with link inserted in position J2 “PWR 3.3V”. the 3.3V rail supplies all circuits on the board. The presence of 3.3V power is indicated by green LED1 “POWER”. The board power consumption depends on the mode of operation, with the maximum of approximately 0.5W.

10BASE-T1L Cable Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The 10BASE-T1L cable can be connected via pluggable screw-terminal block to connector P101. If more of the pluggable connectors are needed, for easy connecting / changing cables, additional connectors can be purchased from the vendor or distributors: Phoenix Contact, part number 1803581, “Pluggable Terminal Block, 3.81 mm, 3 Ways, 28AWG to 16AWG, 1.5 mm², Screw”.

Ground Connections
^^^^^^^^^^^^^^^^^^

The demo board has an “Earth node”. We call it “Earth node” here – though this node may or may not be electrically connected to Earth ground. In a real device this node would be typically connected to the device metal housing / chassis. This Earth node can be connected as required in a wider demo system via “Earth” terminal of the power supply connector P1, or via exposed metal plating of 3 mounting holes in the corners of the board. (The 4th hole does not have metal plating, and also no Earth connection.) The shield of the 10BASE-T1L cable can be disconnected from this Earth node, connected directly, or connected via 4700pF capacitor (C104). The required connection is selected by relevant link position of J101. The 10BASE-T Earth connection and metal body of the RJ45 connector (P5) are connected directly to the Earth node. The local circuit ground, the external power supply (except the “Earth” terminal P1), and the USB connector are connected to the Earth node via approx. 2000pF capacitance and approx. 4.7M resistance. (!) Note: The EVAL-ADIN1100EBZhas been designed only as an Evaluation board. It has NOT been designed, and it has NOT been tested for electrical safety. Any equipment, device, wire, or cable connected to this demo must be already protected and safe to touch without danger of electric shock.

--------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig2_t1l.jpg
   :align: center

.. container:: centeralign

   \ *Figure 2. EVAL-ADIN1100EBZ Quick Start Info*\


   |image2|

.. container:: centeralign

   \ *Figure 3. EVAL-ADIN1100EBZ Functional Block Diagram*\


--------------

Hardware Configuration Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some of the EVAL-ADIN1100EBZ hardware configuration is determined by links (jumpers) and configuration switches on the board. The summary and the default configuration is outlined in tables Table 1 to Table 5.

**Table 1. Board Link Configuration**

+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Ref. | Default Position | Link Function                                                                                                                                                            |
+===========+==================+==========================================================================================================================================================================+
| J1        | USB, EXT+        | Board power supply source selection. Both can be inserted simultaneously.                                                                                                |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J2        | Inserted         | Board 3.3V power supply rail                                                                                                                                             |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J3        | Inserted         | Board 1.8V power supply rail                                                                                                                                             |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J101      | Earth ( )        | SHIELD - Connect the shield of the cable to the Earth node either directly or via a capacitor.                                                                           |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J203      | LDO              | ADIN1100 1.1V power supply selection. LDO … using ADIN1100 on-chip internal 1.1V linear regulator. EXT ... supplied from 1.1V output of the step-down regulator LTC3547. |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J204      | All 3.3V         | ADIN1100 power supplies selection. If changing, keep the (ADIN1100) VDDIO, ADIN1200 VDDIO and uC PWR all at the same voltage level, 3.3V or 1.8V.                        |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J301      | Not inserted     | ADIN1200 reset. Insert to keep ADIN1200 in hardware reset and release its digital signals.                                                                               |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J401      | BRD              | uC Reset. “BRD” … uC is reset by the “BOARD RESET” push button. “GND” … uC is held in reset                                                                              |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| J402      | 3.3V             | uC Power. Keep at the same level, 3.3V or 1.8V, as the (ADIN1100) VDDIO and the ADIN1200 VDDIO                                                                           |
+-----------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Table 2. uC Firmware Mode Configuration, S403, uC CFG**

+-----------------+-------------+------------------+------------------------------------------------------------------+
| Switch Position | Switch Name | Default Position | Description                                                      |
+=================+=============+==================+==================================================================+
| 1               | CFG_0       | OFF              | Mode 15 media converter (default for shipping). All switches OFF |
+-----------------+-------------+------------------+------------------------------------------------------------------+
| 2               | CFG_1       | OFF              |                                                                  |
+-----------------+-------------+------------------+------------------------------------------------------------------+
| 3               | CFG_2       | OFF              |                                                                  |
+-----------------+-------------+------------------+------------------------------------------------------------------+
| 4               | CFG_3       | OFF              |                                                                  |
+-----------------+-------------+------------------+------------------------------------------------------------------+

**Table 3. ADIN1100 Hardware Configuration, S201, HW CFG**

+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| Switch Position | Switch Name | Default Position | Description                                                                    |
+=================+=============+==================+================================================================================+
| 1               | MEDIA_CNV   | OFF              | Media converter. (Only for RMII interface mode, not used on this board)        |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 2               | MACIF_SEL1  | OFF              | Mac Interface Select 1                                                         |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 3               | SWPD_N      | OFF              | Software Power Down.                                                           |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 4               | MACIF_SEL0  | ON               | Mac Interface Select 0                                                         |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 5               | TX2P4_DIS   | OFF              | Transmit Amplitude 2.4V Disable. (Always turn this switch ON if the AVDDH=1.8V |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 6               | MS_SEL      | OFF              | Master/Slave Select. (Used as preference for auto-negotiation)                 |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 7               | PHYAD_0     | OFF              | PHY Address 0. Address for management interface (MDIO)                         |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+
| 8               | PHYAD_1     | OFF              | PHY Address 1. Address for management interface (MDIO)                         |
+-----------------+-------------+------------------+--------------------------------------------------------------------------------+

**Table 4. Board LED indicators**

+--------+-------------------------+---------+--------------------------------------------------------------------------+
| Name   | Colour                  | Sch Ref | Description                                                              |
+========+=========================+=========+==========================================================================+
| uC0    | <fc #008000>Green</fc>  | LED400  | In media converter mode: Media Converter working - both PHYs links up    |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| uC1    | <fc #FF0000>Red</fc>    | LED401  | Error detected by firmware                                               |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| uC2    | <fc #F8F800>Yellow</fc> | LED402  | Short flash: Heartbeat. Long flash/most time on: Receiving UART commands |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| uC3    | <fc #0000FF>Blue</fc>   | LED403  | Reserved                                                                 |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| LED_0  | <fc #008000>Green</fc>  | LED200  | 10BASE-T1L link up/activity                                              |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| LED_1  | <fc #F8F800>Yellow</fc> | LED201  | In firmware managed modes: 10BASE-T1L TX amplitude 2.4V                  |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| (RJ45) | <fc #008000>Green</fc>  | P5      | 10BASE-T link up                                                         |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| (RJ45) | <fc #F8F800>Yellow</fc> | P5      | 10BASE-T activity                                                        |
+--------+-------------------------+---------+--------------------------------------------------------------------------+
| POWER  | <fc #008000>Green</fc>  | LED1    | Board 3.3V power supply is present                                       |
+--------+-------------------------+---------+--------------------------------------------------------------------------+

µC Modes Of Operation
^^^^^^^^^^^^^^^^^^^^^

The EVAL-ADIN1100EBZ can be used in various modes of operations implemented in the uC firmware. Up to 16 modes of operations can be selected by setting the 4 positions of the slide switch S402. The status of the switch is accepted (latched) after the board is powered up or reset. Therefore, to change the mode of operation, the board must be reset by pressing “RESET” button S400 or by applying power cycle after changing the position of the slide switch S501. The detailed description is in the relevant sections of this document.

**Table 5. Firmware Modes of Operation, set by S403, uC CFG**

+----------------+------+------+------+------+--------------------------------------------------+
| CFG3\ :sup:`1` | CFG2 | CFG1 | CFG0 | Mode | Description                                      |
+================+======+======+======+======+==================================================+
| ON             | ON   | ON   | ON   | 0    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | ON   | ON   | OFF  | 1    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | ON   | OFF  | ON   | 2    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | ON   | OFF  | OFF  | 3    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | OFF  | ON   | ON   | 4    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | OFF  | ON   | OFF  | 5    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | OFF  | OFF  | ON   | 6    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| ON             | OFF  | OFF  | OFF  | 7    | Reserved                                         |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | ON   | ON   | ON   | 8    | ADIN1100 PHY Test Mode 3 (Idle)                  |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | ON   | ON   | OFF  | 9    | ADIN1100 PHY Test Mode 2 (Droop)                 |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | ON   | OFF  | ON   | 10   | ADIN1100 PHY Test Mode 1 (Jitter)                |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | ON   | OFF  | OFF  | 11   | ADIN1100 PHY Test TX disabled                    |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | OFF  | ON   | ON   | 12   | ADIN1100 Frame Generator/Checker                 |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | OFF  | ON   | OFF  | 13   | ADIN1100 MAC Remote Loopback                     |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | OFF  | OFF  | ON   | 14   | GUI / Interactive Mode                           |
+----------------+------+------+------+------+--------------------------------------------------+
| OFF            | OFF  | OFF  | OFF  | 15   | Media Converter Mode (**Default Configuration**) |
+----------------+------+------+------+------+--------------------------------------------------+

:sup:`1` *Switch in ON position = signal logic 0 for uC (shorted to ground). Switch in OFF position = signal logic 1 (pulled up by a resistor)*

Software
~~~~~~~~

| The EVAL-ADIN1100EBZ can be used as stand-alone board, with the firmware already programmed in the uC flash memory, the mode of operation set by mode switch, and status indicated by LEDs. There is no software needed for this stand-alone use case.
| The demo can also be connected to a PC via USB port, the full set of ADIN1100 register settings and features such as link quality monitoring and diagnostics can be accessed with the ADIN1100 Graphical User Interface software, available from Analog Devices.
| Alternatively, the ADIN1100 and ADIN1200 registers, 10BASE-T1L link status monitoring and some diagnostics can be accessed using a simple set of ASCII text commands and messages exchanged over the USB Com Port and a serial port terminal software.

Driver For USB COM Port
^^^^^^^^^^^^^^^^^^^^^^^

| The EVAL-ADIN1100EBZ uses FTDI FT232 for the USB Com Port connectivity.
| Please make sure that appropriate Virtual Com Port driver is included or installed on the host platform before connecting the EVAL-ADIN1100EBZ to that host via USB cable.
| The drivers are available from FTDI, at the time of writing this document at https://ftdichip.com/drivers/vcp-drivers/.

COM Port And Terminal Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| When the EVAL-ADIN1100EBZ is connected to the host, it will become available in the host system as a USB Com Port, and will be assigned a com port number. The number will depend on the system settings, on com port devices previously connected and assigned in the system, and on the FTDI driver settings.

| The EVAL-ADIN1100EBZ uC firmware communicates over a standard UART interface, with settings:
| Speed 115200 Bd., 1 Start Bit – 8 Data Bits – No Parity – 1 Stop Bit.
| The protocol is based on ASCII text commands and messages. Each message and command are finished by <newline>. Each message sent from the firmware to the host is finished by both <CR> and <LF> characters. For the commands received from host the firmware expects the <newline> as character <CR> or <LF> or both <CR> and <LF>.
| (*To be sure and clear:
  <CR> .. “carriage return”, ASCII code 0x0D, 13dec,
  <LF> .. “line feed”, ASCII code 0x0A, 10dec.*)
| ==== Terminal Software ==== The EVAL-ADIN1100EBZ firmware works with the common serial terminals. It has been tested on Windows platform with PuTTY, RealTerm, Termite and the old Hyperterminal.

Terminal Commands And Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(*The examples here were captured using Compuphase Termite*).

Initial Welcome Message
^^^^^^^^^^^^^^^^^^^^^^^

| When the EVAL-ADIN1100EBZ is correctly connected, from the uC firmware and UART, via the USB Com Port, to the terminal software, the firmware sends after power or after pressing the board RESET button S501 an initial welcome message:

| <fc #008000>================================================
| ANALOG DEVICES 10BASE-T1L PHY Demo
| ================================================
| (c) 2021 Analog Devices Inc. All rights reserved
| ================================================
| Firmware ver.: 12 . 1 . 4784b935
| Hardware type: EVAL-ADIN1100EBZ
| Hardware ver.: A
| Hardware UID : AVAS142049
| uCCFG3-2-1-0 : OFF-OFF-OFF-ON (Mode 14)
| Firmware Mode: GUI / Interactive mode
| ================================================
| Type '<?><new line>' for a list of commands
| ================================================</fc>

Terminal Commands
^^^^^^^^^^^^^^^^^

| The most important command is “<?><new line>.
| On the host keyboard, press key “?” followed by key “Enter”, and the firmware will send a list of all commands implemented in this version:
| <fc #0000FF>?</fc>
| <fc #008000>==============================================
| List of Commands
| \* MDIO (Clause 22) write to Phy, all numbers in hex.
| 'mdiowrite <PhyAddr>,<RegAddr>,<Data>'<newLine>
| \* MDIO (Clause 22) read from Phy, all numbers in hex.
| 'mdioread <PhyAddr>,<RegAddr>'<newLine>
| \* MDIO (Clause 45) write to Phy, all numbers in hex.
| 'mdiowr_cl45 <PhyAddr>,<RegAddr>,<Data>'<newLine>
| \* MDIO (Clause 45) read from Phy, all numbers in hex.
| 'mdiord_cl45 <PhyAddr>,<RegAddr>'<newLine>
| \* Phy (hardware) reset
| </fc> <fc #008000>'phyreset'<newLine>
| \* Phy status and link properties.
| 'phystatus'<newLine>
| \* Start reporting status.
| 'start'<newLine>
| \* Stop reporting status.
| 'stop'<newLine>
| \* Clear / reset status counters.
| 'clear'<newLine>
| \* uC Software Reset.
| 'reset'<newLine>
| \* Mode change, overrides uC CFG until next Reset.
| 'mode <number>' <newLine>
| \* List implemented modes.
| 'modes'<newLine>
| \* Comment – string of up to 98 characters
| '//'<string ><newLine>
| \* Show list of commands.
| '?'<newLine>
| ==============================================</fc>

Status And Diagnostics
^^^^^^^^^^^^^^^^^^^^^^

| To see the status of the demo, use command “phystatus”, which will read and show the latest status of the ADIN1200 10BASE-T PHY and ADIN1100 10BASE-T1L PHY:
| <fc #0000FF>phystatus</fc>
| <fc #008000>ADIN1200 Link is Up,
| ADIN1100 Link is Up, Master, 2.4 V
| MSE -37.2 dB Rx 0, Err 0</fc>

| To see a continuous update, use commands “start”:
| <fc #0000FF>start</fc>
| <fc #008000>OK
| MSE -38.4 dB Rx 255, Err 0
| MSE -38.6 dB Rx 256, Err 0
| MSE -38.7 dB Rx 257, Err 0
| MSE -38.4 dB Rx 257, Err 0
| MSE -38.7 dB Rx 257, Err 0</fc>
| <fc #0000FF>stop</fc>
| <fc #008000>OK</fc>
| The firmware will periodically, with period of approx. 1 second, send an update. The update in the present firmware version includes:
| \*“MSE” – 10BASE-T1L Mean Square Error, which indicates link quality.

-  “Rx” – number of Ethernet frames received by PHY from 10BASE-T1L cable since the last board / firmware reset, or after use of command “clear”
-  “Err” – number of frames with error received since the last board / firmware reset, or after use of command “clear”

To stop the continuous update, use command “stop”. (Or reset the board.)

µC Firmware Update
~~~~~~~~~~~~~~~~~~

| The uC (U401 ADuCM4050) is programmed before shipping the demo board, and therefore there is no need to program it, unless a new version of firmware is available, and you want to update it on your board.
| The present firmware version can be checked via USB Com Port and terminal software, it is displayed in the welcome message after board reset or in response to “info” command.
| Firmware update is distributed as a compiled binary (.hex) file. The easiest way to program it to the uC is using the USB Com Port and CrossCore Serial Flash Programmer, available for free download from analog.com, presently:
| :adi:`en/design-center/evaluation-hardware-and-software/software/crosscore-serial-flash-programmer`.html#software-relatedsoftware

|image3|

.. container:: centeralign

   \ *Figure 4. CrossCore Serial Flash Programmer.*\


| USB Com Port driver (same as for using the terminal software) needs to be installed on the PC before connecting the board and using the CrossCore Serial Flash Programmer - see chapter “Driver for USB Com Port”.
| When you have the driver and programmer software installed, and firmware update hex file ready, use the following steps:
| \* Connect the board (P401) via micro-USB cable to your PC.

-   Start the CrossCore serial flash programmer software.
-  Set the programmer (also see Figure 4):

::

     *Target: ADuCM302x
     *Serial Port: COMx (USB Serial Port) – (the “x” port number is depending on your PC)
     *Baudrate: 115200
     *Action: Program
     *(Second stage kernel is not applicable)
   * File to download - browse for the firmware file on your PC
   * On the demo board, simultaneously press and hold buttons S501 “RESET” and S401 “BOOT”. Release the RESET button first, followed by releasing the BOOT button. The on board microcontroller is in the programming state now, and the yellow / orange heart beat LED402 will stop blinking.
   * Click Start and the code should start to download with messages provided in the Status window and progress bar across the bottom of the window.NOTE: If you have been using a terminal program for communicating with the board, either disconnect it / release the com port, or stop the terminal program, otherwise you will see a message “Failed to open serial device”. A message “No autobaud response” most likely indicates that the uC is not in the programming state and you need to go back to step 5.
   * After programing, press & release RESET button.

Notes
~~~~~

| **Legal Terms and Conditions**
| By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at OneTechnology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, arereserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig1_t1l.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig3_t1l.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/10base-t1l/02-063798-01-b_crosscore.png
