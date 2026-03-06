User Guide \| EVAL-LTC2686
==========================

DC2904A
-------

Evaluation Board for the LTC2686 8-Channel, 16-Bit Voltage Output SoftSpan DAC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Features
--------

-  Fully featured evaluation board for the LTC2686 multichannel voltage output DAC
-  Flexible output power supply configuration
-  Easy connection to external loads
-  Test points to monitor DAC status signals
-  :adi:`ACE <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>` evaluation software compatible

Evaluation Kit Contents
-----------------------

-  DC2904A evaluation board
-  Ribbon cable to connect to the Linduino DC2026C controller

Equipment Needed
----------------

-  DC2026C controller board
-  PC running Windows® 7 or Windows 10
-  Voltmeter
-  Power Supply

Software Needed
---------------

-  ACE evaluation software (available for download from the :adi:`DC2904A <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/dc2904a.html>` product page)

Documents Needed
----------------

-  LTC2686 Data Sheet
-  DC2904A design files (see the :adi:`DC2904A <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/dc2904a.html>` product page)

Evaluation Board Photograph
---------------------------

Figure1. DC2904A Evaluation Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904atop-web.jpg
   :alt: Figure1. DC2904A Evaluation Board
   :align: right
   :width: 600px

General Description
-------------------

The DC2904A is a fully featured evaluation board that is used to evaluate the :adi:`LTC2686`, an 8-channel, precision voltage output digital-to-analog converter (DAC). The DC2904A is controlled through a serial peripheral interface (SPI) from the J1 connector. The SPI signals are sent from the :adi:`DC2026C` controller board through the ribbon cable that is connected to the DC2904A. The DC2904A uses :adi:`Analysis, Control, Evaluation (ACE) <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>` software to provide an intuitive graphical user interface (GUI) that configures and controls the LTC2686 using the SPI interface. The LTC2686 is used for various voltage mode biasing applications such as optical modulators for data communications. The output voltage range for each channel is software selectable, and any channel can be routed to the DC2904A MUX pin, allowing either the channel voltage or current to be externally monitored. For full specifications on the LTC2686, see the LTC2686 data sheet, which must be consulted in conjunction with this user guide when using the DC2904A

Evaluation Board Hardware
=========================

Evaluation Board Overview
-------------------------

The DC2904A requires the power connections and connection to the DC2026C controller board shown in Figure 2. The ribbon cable provided in the evaluation kit connects the DC2904A and the DC2026C via the J1 connector. Turrets are provided to connect the DC2904A to the power supplies. The DC2904A has other optional features to allow the user to select an external reference, provide separate supply voltages for Channel 0 to Channel 3 and Channel 4 to Channel 7, and to monitor various outputs through the on-board MUX pin. These optional features do not need to be changed for normal operation.

Power Supplies
--------------

The DC2904A is powered using external supplies. The minimum requirement to power the DC2904A is to provide 5.0 V to 21 V on E2 (V1+) and connect E3 (GND) and E4 (V−) to ground (GND). As an alternative, the supply connection to E4 (V−) can be in the range between −21 V and ground (GND) to accommodate applications that require a negative supply. The default position for JP5 (V1+ = V2+) is in the CONNECT position. This position connects the V1+ and V2+ power supplies so that they are at the same voltage. By changing JP5 to the NC (not connected) position, V1+ and V2+ are decoupled on the evaluation board and can be driven with separate supplies. V1+ and V2+ have the same requirement. They must be in the range of 5 V to 21 V but do not need to be the same voltage when decoupled. However, V2+ must be less than or equal to V1+. E10 (VCC) and E5 (IOVCC) are supplied from on-board regulators by default. If desired, these voltages can be driven with an external supply.

Figure 2. DC2904A Hardware Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904a-b_ug_connection_diagram.png
   :alt: Figure 2. DC2904A Hardware Connections
   :align: center

Analog Outputs
--------------

The analog outputs, VOUT0 to VOUT7, are available on the E13, E14, E15, E16, E17, E18, E19 and E20 turrets, respectively. Return paths for the ground currents are available on the E3 and E23 (GND) turrets. These turrets must be connected to load GND.

Digital Interface
-----------------

DC2026C Connections
^^^^^^^^^^^^^^^^^^^

The DC2904A uses the DC2026C to communicate with the ACE evaluation software through the USB port on the DC2026C. Use the provided ribbon cable to connect J1 of the DC2904A to J1 of the DC2026C. When this connection is made, the DC2026C powers the electrically erasable programmable read only memory (EEPROM) on the DC2904A. The ACE evaluation software uses the EEPROM to identify the DC2904A and load the proper plugin. To ensure proper serial transfers and compatibility, the DC2026C powers the IOVCC pin of the LTC2686, which is nominally 5 V.

DC2026C Connector Pin Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Figure 3 shows the pins for the DC2026C J1 connector. For descriptions of each pin, see Table 1.

Figure 3. DC2026C J1 Connector Pins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2026c_connector.png
   :alt: Figure 3 DC2026C J1 Connector Pins
   :align: center
   :width: 600px

Table 1. DC2026 Connector J1 Pin Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------+----------------+----------------------------------------------------+
| Pin No. | Mnemonic       | Description                                        |
+=========+================+====================================================+
| 1       | V\ :sup:`+`    | Unregulated voltage from the DC2026C, nominally 7V |
+---------+----------------+----------------------------------------------------+
| 2       | V\ :sub:`CCIO` | I/O voltage set by JP3 on the DC2026C              |
+---------+----------------+----------------------------------------------------+
| 3       | GND            | Ground                                             |
+---------+----------------+----------------------------------------------------+
| 4       | SCL/SCK        | Serial clock from the DC2026C                      |
+---------+----------------+----------------------------------------------------+
| 5       | MISO           | Serial data from the DC2904A                       |
+---------+----------------+----------------------------------------------------+
| 6       | CS             | Chip select from the DC2026C                       |
+---------+----------------+----------------------------------------------------+
| 7       | SDA/MOSI       | Serial data from the DC2026C                       |
+---------+----------------+----------------------------------------------------+
| 8       | GND            | Ground                                             |
+---------+----------------+----------------------------------------------------+
| 9       | EEDA           | Serial data for EEPROM                             |
+---------+----------------+----------------------------------------------------+
| 10      | EEVCC          | Power supply (VCC) for EEPROM                      |
+---------+----------------+----------------------------------------------------+
| 11      | EESCL          | Serial clock for EEPROM                            |
+---------+----------------+----------------------------------------------------+
| 12      | EEGND          | Ground for EEPROM                                  |
+---------+----------------+----------------------------------------------------+
| 13      | GND            | Ground                                             |
+---------+----------------+----------------------------------------------------+
| 14      | NC             | No connection                                      |
+---------+----------------+----------------------------------------------------+

Reference
---------

By default, the DC2904A uses the internal reference of the LTC2686. To use an external reference, place the DC2904A JP1 (REF SEL) jumper into the EXT position and apply an external reference to E11 (REF).

Multiplexer Output
------------------

The LTC2686 has an internal multiplexer that allows monitoring of compliance voltages, output currents, and internal die temperature. The output compliance voltages and representative voltages of the output current and internal die temperature are available on the LTC2686 MUX pin and can be routed to the DC2904A E21 connector (MUX) using the LTC2686-16 Memory Map view in the ACE GUI (see Figure 8), and setting the appropriate bits in the analog mux control register. Refer to the LTC2686 data sheet for more details on the multiplexer functionality and register structure.

On-Board Connectors
-------------------

Table 2 describes the on-board connectors on the DC2904A.

Table 2. On-Board Connectors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================== ======================================
Connector            Function
==================== ======================================
J1                   SPI/I2C interface pin header connector
JP1                  Internal or external reference select
JP2                  Toggle Pin 0 (TGP0)
JP3                  Toggle Pin 1 (TGP1)
JP4                  Toggle Pin 2 (TGP2)
JP5                  Connect or disconnect V1+ and V2+
E1                   V2+
E2                   V1+
E3, E6, E7, E12, E23 GND
E4                   V-
E5                   IOVCC
E8                   CLRL
E9                   LDACL
E10                  VCC
E11                  REF
E13                  Channel 0 voltage output (VOUT0)
E14                  Channel 1 voltage output (VOUT1)
E15                  Channel 2 voltage output (VOUT2)
E16                  Channel 3 voltage output (VOUT3)
E17                  Channel 4 voltage output (VOUT4)
E18                  Channel 5 voltage output (VOUT5)
E19                  Channel 6 voltage output (VOUT6)
E20                  Channel 7 voltage output (VOUT7)
E21                  MUX
E22                  FAULT
==================== ======================================

Getting Started
===============

The ACE evaluation software controls and configures the on-board LTC2686 through the DC2026C.

Software Installation Procedures
--------------------------------

Before connecting the DC2026C to the DC2904A, follow these steps to set up the DC2904A for initial use in the ACE evaluation software:

-  Download the ACE evaluation software package from the DC2904A product page at :adi:`www.analog.com/DC2904A <DC2904A>` to start the ACE evaluation software installation.
-  Open the **ACEInstall_1.21.xxxx.xxxx.exe** file and follow the instructions in the folder to complete the software installation process.

Evaluation Hardware Setup
-------------------------

When the ACE evaluation software installation is complete, follow these steps to set up the DC2026C and the DC2904A together:

-  Connect the DC2026C to the DC2904A via the J1 connectors with the ribbon cable provided (see Figure 2).
-  Connect the desired power supplies to E2 (V1+), E3 (GND), and E4 (V−) on the DC2904A.
-  Connect the desired load to the appropriate channel on the DC2904A.
-  Connect the load ground to a ground (GND) turrets (either E3 or E23) on the DC2904A.
-  Connect the DC2026C to a PC or laptop using the USB cable.
-  Start the ACE evaluation software (see the Software Operation section).

Software Operation
------------------

To start the ACE evaluation software, from the Start menu, click Analog Devices > ACE. The software window opens (see Figure 4) until the software recognizes the DC2904A. When the software recognizes the DC2904A, the main software window in Figure 5 opens.

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904a_interface.png
   :alt: Figure 4. Interface Window
   :align: center

Figure 4. Interface Window
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904a_main.png
   :alt: Figure 5. ACE Evaluation Software Main Window
   :align: center

Figure 5. ACE Evaluation Software Main Window
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Main Window
-----------

In the main ACE evaluation software window (see Figure 5), each channel can be controlled. Various settings for the LTC2686 are available in this window, allowing the user to configure the output range, output voltage, gain adjustment, offset adjustment, toggle options, and dither options of each channel. Refer to the LTC2686 data sheet for more information on the device features associated with the different tab functions that are described in the following sections.

Reference Configuration
~~~~~~~~~~~~~~~~~~~~~~~

The DC2904A uses the LTC2686 internal reference to set the full-scale range. To apply an external reference, click the box labeled **Reference Select** (see Figure 5).

Setting the Channel Output Range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set the output range for a specific channel on the LTC2686,

-  Select the channel from the **Channel Select** dropdown box.
-  Select the desired range for the selected channel using the **Span selection** dropdown box (see Figure 5).

Setting the Channel Voltage Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set the output voltage for a specific channel on the LTC2686,

-  Select the channel from the **Channel Select** dropdown box.
-  Type the desired value into the **Register A** text box (see Figure 5).

Toggling Between A and B Output Registers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each channel has two output registers that can be written independently.

-  Click the **Register A** or **Register B** option to select the register to write to.
-  Type the desired hexadecimal value into the **Register A** (or **Register B**) text box (see Figure 5).

Settling Offset and Gain Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each channel can have an offset and gain value applied to the output. The value is applied to each channel independently.

-  Select the channel from the **Channel Select** dropdown box.
-  Type the desired hexadecimal offset or gain adjust value into the **Offset Adjust** or **Gain Adjust** text boxes (see Figure 5).

Enabling Toggle Mode
~~~~~~~~~~~~~~~~~~~~

Toggle mode can be enabled by selecting the **Enable Toggle/Dither Functionality** check box (see Figure 5). This check box enables the toggle view shown in Figure 6. The toggle signal can then be applied to the selected pin or supplied internally.

Enabling Dither Mode
~~~~~~~~~~~~~~~~~~~~

After enabling the toggle view shown in Figure 6 as described in the Enabling Toggle Mode section, select the dither mode from the **Mode** dropdown box to bring up the dither options (see Figure 7). The default values for the dither phase (ⱷ0) and period (N) are 0° and N = 4. The phase and period of the dither can be modified using the dropdown boxes to select from a fixed list of options.

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904a_toggle.png
   :alt: Figure 6. Toggle View
   :align: center

Figure 6. Toggle View
^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904a_dither.png
   :alt: Figure 7. Dither View
   :align: center

Figure 7. Dither View
^^^^^^^^^^^^^^^^^^^^^

Memory Map View
~~~~~~~~~~~~~~~

To access the LTC2686-16 **Memory Map** view, click the **Proceed to Memory Map** button from the software main window (see Figure5).

.. image:: https://wiki.analog.com/_media/resources/eval/dac/dc2904a_memory_map.png
   :alt: Figure 8. Memory Map View
   :align: center

Figure 8. Memory Map View
^^^^^^^^^^^^^^^^^^^^^^^^^

Troubleshooting
===============

Hardware
--------

A comprehensive list of frequently asked questions (FAQ) is available on the LTC2686 FAQs page in the EngineerZone™ site. For other questions, submit them to the Precision DACs section of the EngineerZone site.

Ordering Inforamtion
====================

Table 3. Evaluation Board Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========== =========== ==========
Product    Board Model Resolution
========== =========== ==========
LTC2686-16 DC2904A-B   16 bits
========== =========== ==========

--------------

| **ESD Caution**
| ESD (electrostatic discharge) sensitive device Charged devices and circuit boards can discharge without detection. Although this product features patented or proprietary protection circuitry, damage may occur on devices subjected to high energy ESD. Therefore, properESD precautions should be taken to avoid performance degradation or loss of functionality.

--------------

| **Legal Terms and Conditions**
| By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed.
