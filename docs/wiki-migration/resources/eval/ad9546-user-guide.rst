AD9546 Evaluation Board User Guide
==================================

Evaluation Board Features
-------------------------

-  Full featured Evaluation Board for the AD9546
-  Simple power connection using 6 V wall adapter and on-board LDO voltage regulators
-  Ten AC-coupled output SMA connectors, with output termination for HCSL
-  Two single ended AC-coupled reference inputs, usable also as a one differential AC-coupled reference input
-  One single ended AC-coupled reference input and 1 single ended DC-coupled reference input, configurable to create together a differential AC-coupled reference input
-  Pin programmable, power on ready configurability
-  Status LEDs
-  PC control using a USB connection
-  Microsoft Windows-based Evaluation Software with simple graphical user interface

Evaluation Kit Contents
-----------------------

-  AD9546/PCBZ Evaluation Board
-  6 V wall supply
-  USB cable

Additional Equipment Needed
---------------------------

-  Reference oscillator or signal generator for reference input
-  Other Evaluation Board(s) to be driven by output clocks or test equipment

   -  Oscilloscope, spectrum analyzer, phase noise analyzer

-  50 Ω SMA cables
-  6 V wall supply (provided)
-  PC running Windows 10 with USB 2.0 port

Documents Needed
----------------

-  AD9546 data sheet
-  AD9546/PCBZ user guide (this document)
-  AD9546 register map reference manual

Software Needed
---------------

-  AD9546 Evaluation Software

Online resources
----------------

-  Design and integration files: Schematics, layout files, and bill of materials

--------------

.. _online-resources-1:

Online Resources
----------------

Required Software

-  :adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9546`.html#eb-relatedsoftware

Documents Needed

-   :adi:`AD9546 Data sheet </AD9546>`

.. image:: https://wiki.analog.com/_media/resources/eval/ad9546_eval_board_top.jpg
   :width: 400px

General Description
-------------------

The AD9546 Evaluation Board is a compact, easy-to-use platform for evaluating all features of the :adi:`AD9546` multiple input, 10-Output, Dual Channel, Numeric Clock Synchronizer. The AD9546 supports existing and emerging International Telecommunications Union (ITU) standards for the delivery of frequency, phase, and time of day over service provider packet networks, including ITU-G.8262, ITU-T G.812, ITU-T G.813, ITU-T G.823, ITU-T G.824, ITU-T G.825, and ITU-T G.8273.2.

The 10 clock outputs of the AD9546 are synchronized to any one of up to four input references. The digital phase-locked loops (DPLLs) reduce timing jitter associated with the external references. The digitally controlled loop and holdover circuitry continuously generate a low jitter output signal, even when all reference inputs fail. The AD9546 system clock is provided by a 52 MHz crystal. Alternatively, an external clock signal may be provided at a SMA connector (relative components must be populated to enable this functionality).

EVALUATION BOARD HARDWARE
-------------------------

The following instructions are for setting up the physical connections to the AD9546/PCBZ Evaluation Board. The user must install the Evaluation Software prior to connecting the Evaluation Board for the first time.

The 6 V supply powers the following:

-  An Analog Devices :adi:`ADP2384 Switching Regulator <ADP2384>` configured to output 3.3 V or 1.8 V.
-  A dedicated Analog Devices 1.8 V :adi:`ADM7171 Low Noise LDO <ADM7171>` for the AD9546 power supply.
-  A dedicated Analog Devices 1.8 V :adi:`ADM7160 Ultralow Noise LDO <ADM7160>` for the AD9546 serial port and Mx pins power supplies.
-  A dedicated Analog Devices 1.8 V :adi:`ADM7160 Ultralow Noise LDO <ADM7160>` for the power supply of the level shifter and transceiver circuits.

By default, the 3.3 V ADP2384 switcher output supply supplies a 1.8 V Analog Devices :adi:`ADM7171 Low Noise LDO <ADM7171>` to power the :adi:`AD9546`. The :adi:`ADP2384 Switching Regulator <ADP2384>` can also be configured to output 1.8 V and directly power the :adi:`AD9546` to evaluate the :adi:`AD9546` when powered directly from a switching power supply. The :adi:`AD9546` can also be powered from external 3.3 V or 1.8 V supplies. To increase the SPI speed when the :adi:`AD9546` is managed through the USB connector, an additional power supply scheme is proposed. In this scheme, the :adi:`AD9546` VDD pins are supplied at 1.8 V from the above LDO, while the serial port and Mx pin VDDIOA and VDDIOB pins are supplied directly from the 3.3 V switching regulator.

In the following, various power supply solutions of the :adi:`AD9546` are presented together with the configurations of the 0 Ω resistors.

-  **AD9546 Powered by ADP2384A Step-down Switching Regulator cascaded with ADP7171 LDO (Default):**

   -  ADP2384A output is 3.3 V
   -  0 Ω resistors R701, R721, R706, R726, R708, R711, R728, R714, R716, R730, R719 are populated
   -  0 Ω resistors R812, R702, R722, R703, R723, R705, R725, R704, R724, R707, R710, R727, R712, R715, R729, R717, R720, R731 are not populated

-  **AD9546 Powered by ADP2384A Step-down Switching Regulator directly:**

   -  ADP2384A output is 1.8 V
   -  0 Ω resistors R812, R703, R723, R705, R725, R707, R710, R727, R712, R715, R729, R717, R720, R731 are populated
   -  0 Ω resistors R701, R721, R702, R722, R704, R724, R706, R726, R708, R711, R728, R714, R716, R730, R719 are not populated

-  **AD9546 Powered by an external 3.3 V Power supply:**

   -  Install P700 Connector and provide 3.3 V power supply at pin 3 and ground power supply at pin 1
   -  0 Ω resistors R702, R722, R706, R726, R708, R711, R728, R714, R716,R730, R719 are populated
   -  0 Ω resistors R812, R701, R721, R703, R723, R705, R725, R704, R724, R707, R710, R727, R712, R715, R729, R717, R720, R731 are not populated

-  **AD9546 Powered by an external 1.8 V Power supply:**

   -  Install P700 Connector and provide 1.8 V power supply at pin 4 and ground power supply at pin 1
   -  0 Ω resistors R703, R723, R707, R710, R727, R712, R715, R729, R717, R720, R731 are populated
   -  0 Ω resistors R812, R701, R721, R702, R722, R705, R725, R704, R724, R706, R726, R708, R711, R728, R714, R716, R730, R719 are not populated

-  **AD9546 serial port power supply (VDDIOA) and MX pin power supply (VDDIOB) provided at 3.3 V directly from the 3.3 V ADP2384A Step-Down Switching Regulator:**

   -  0 Ω resistors R701, R721, R704, R724, R706, R726, R708, R712, R715, R729, R717, R720, R731 are populated
   -  0 Ω resistors R812, R702, R722, R703, R723, R705, R725, R707, R710, R727, R711, R728, R714, R716, R730, R719 are not populated

PC Connections
--------------

-  Install all required software, uninstall prior versions of the software before installation updates. Administrative privileges are required for installation.
-  Connect the 6 V wall power supply to the main power connector labeled P800. The red LED labelled DS801 turns on
-  Connect the USB cables to the Evaluation Board and to the computer. The red LED labeled DS500 by the USB connector turns on and the LED labeled DS501 blinks.

Reference Clock Inputs
----------------------

The AD9546 Evaluation Board has four reference input sources. By default, REF A/AA (Connectors J301 and J302, respectively) are configured as single ended differential AC-coupled reference inputs. Each can be connected to a signal generator directly. In contrast, REF B/BB (Connectors J303 and J304, respectively) are configured for single-ended CMOS inputs by default. Each reference input logic type is configurable via the Evaluation Software.

-  REF B is intended for a single ended AC-coupled reference input terminated with a 50 Ω resistor to ground.
-  REF BB is intended for a single ended DC-coupled reference input.

System Clock Inputs
-------------------

By default, the AD9546 system clock input is configured to the on-board 52 MHz crystal. An additional path, not populated, may be used to provide a system clock input at J305 connector.

P503 Connector / USB Interface
------------------------------

The connector P503 may be used to directly access the AD9546 from an external device. A Raspberry PI 3 Model B+ may be used to interface with the AD9546 Evaluation Board at connector P503.

The signals available at connector P503 are the SPI pins (SCLK, SDIO, SDO, CSB) and the M0, M1, M2 and M3 control pins. Jumpers at connectors P507 and P508 select how these signals are managed: through connector P503 or through USB interface, that is from the PC based user interface.

Table 1 and Table 2 present the position of the jumpers when connector P503 is used and when the USB interface is used:

**Table 1. SPI Pin Management Settings at Connector P507**

=========== ================ ===============
SPI PINS    Managed via P503 Managed via USB
=========== ================ ===============
SCLK        2 - 1            2 - 3
SDIO (MOSI) 5 - 4            5 - 6
SDO (MISO)  8 - 7            8 - 9
CSB         11-10            11-12
RESETB      14-13            14-15
=========== ================ ===============

**Table 2. AD9546 Mx Pin Management Settings at Connector P508**

======= ================ ===============
Mx Pins Managed via P503 Managed via USB
======= ================ ===============
M0      2 - 1            2 - 3
M1      5 - 4            5 - 6
M2      8 - 7            8 - 9
M3      11-10            11-12
M4      14-13            14-15
======= ================ ===============

P512 Connector
--------------

A generic FPGA or a microcontroller can interface with the AD9546 through connector P512 that provides access to all SPI pins of the AD9546. See board schematics for details.

EEPROMs
-------

The AD9546 Evaluation Board contains two EEPROMS:

-  CYUSB EEPROM (U503) that is used in conjunction with the USB communication
-  PI EEPROM (U508) that is used when a Rasberry PI 3 Model B+ is connected at P503 connector

To protect the EEPROMs from being overwritten, place jumpers at P502 and P506 connectors. To make sure the CYUSB EEPROM is enabled, place jumper at P501 connector. To program the CYUSB EEPROM:

-  take out the jumper P502 to enable the operation
-  take out jumpers P504 and P505 to disable the I2C bus accessing the PI EEPROM
-  use the available programming tool.

To program the PI EEPROM, take out the jumper P506 to enable the operation and use the available programming tool.

Control Pins
------------

The control pins M0 - M6 may be managed in several ways on the on the AD9546 Evaluation Board:

-  through the Evaluation Software using the USB connection
-  M0, M1, M2 and M3 through connector P503
-  through the jumpers at the P601 and P602 connectors as shown in Table 3
-  through the SMA connectors J601, J602, J603, J604, J605, J606, and J607

**Table 3. M0 - M6 Pins Access**

============ ========= =========== =====
Control Pins Connector P601 Jumper 
============ ========= =========== =====
\                      High        Low
M0           J601      2-1         2-3
M1           J602      5-4         5-6
M2           J603      8-7         8-9
M3           J604      11-10       11-12
\                      P602 Jumper 
\                      High        Low
M4           J605      2-1         2-3
M5           J606      5-4         5-6
M6           J607      8-7         8-9
============ ========= =========== =====

Note that M5 and M6 pins are multiplexed with the SPI pins SDO and, respectively, CSB. The default board settings enable the SPI functionality, so the M5 and M6 pins are not usable.

The 0 Ω resistors R608, R657, RT658, R659, R660, R661 and R662 connect the Mx, x=0 to 6, signals from connectors J601, J602, J603, J604, J605, J606 and J607 to U602 level shifter. Unsolder them when the Mx pins are used as auxiliary references and a clean path towards the AD9546 is necessary.

AD9546 EVALUATION SOFTWARE
--------------------------

The AD9546 evaluation board is supported by Windows® based software that allows the user to access all the functionality of the AD9546. The software communicates with the board using the USB. On the evaluation board, the CY7C68013A USB microcontroller then communicates with the :adi:`AD9546` to process the requests that are sent from the PC. The evaluation software uses only the 3-wire SPI communication to communicate with the :adi:`AD9546`. The 4-wire SPI and I2C communications are not supported.

Installing the AD9546 Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the AD9546 Evaluation Software from the :adi:`AD9546 Evaluation Board Website <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad9546.html>`, unzip it and run the executable.

.. important::

   Administrator privileges are required to run the installer.

   
   The AD9546 evaluation board does not need to be connected to the PC to install the evaluation software.


Front Panel
~~~~~~~~~~~

Connect a USB cable between the PC and the AD9546 evaluation board. Power up the board by connecting the 6V wall supply provided with the evaluation kit. The Windows® Device manager recognizes the board as the ADI Evaluation System (Figure 1):


|image1|

.. container:: centeralign

   *Figure 1: AD9546 Evaluation Board Connected to the PC – as it appears in Windows Device Manager*


Then launch the evaluation software. The Front Panel shown in Figure 2 opens:



|image2|

.. container:: centeralign

   *Figure 2: AD9546 Evaluation Software Front Panel*


Click on File menu at the top left of the front panel and the following entries are available:

-  Configuration Files - Allows to save a configuration file or to load one. All the configuration registers are saved if Save Configuration entry is selected. If Save Configuration (non-default only) entry is selected, only the registers having non default values are saved.
-  Select Hardware - Opens the Select Hardware dialog shown in Figure 3 below. The Select Hardware dialog lists the evaluation boards connected to the PC using the USB ports. If the board is connected to the PC after the evaluation software is launched and if the Windows® Device manager recognizes the board, then the evaluation board will appear in list. Select the board and click OK. The evaluation software automatically connects to the first board in the list when it starts up.

|image3|

.. container:: centeralign

   *Figure 3: Select Hardware Entry in File dialog*


.. container:: center round

   Multiple AD9546 Evaluation Boards may be connected simultaneously to the same PC. Figure 3b shows the Select Hardware dialog when two boards are connected to the same PC. Proceed in the following way to use two instances of the AD9546 Evaluation Software.

   
   -  Plug in one board and launch the software. It automatically starts using the board, which is identified by the Instance Cyusb-1 in the Select Hardware dialog.
   -  Plug in the next board, launch the software, open the Select Hardware dialog and select the board identified by the Instance Cyusb-2, the last enumerated board. From that moment, the software works with the second board.
   
   | Proceed the same if other AD9546 evaluation boards must be used.
   | Do not unplug or power down one or more boards already selected in the Select Hardware dialog.


|image4|

.. container:: centeralign

   *Figure 3b: Select Hardware dialog window when Two AD9546 Evaluation Boards are Connected to the same PC*


-  Options menu - Provides the following sub menu options to manage the evaluation software: Enable Polling, Polling Interval, Enable Auto IO Update and Launch Wizard at Start Up. All the entries are enabled by default, with the polling interval being set at 1s. The user can change this interval by clicking on Polling Interval entry and introducing the desired interval in milliseconds. The recommended minimum polling interval value is 800 ms.

Click on View menu on the top of the screen and the following entries are available:

-  Register Map - Opens the window in Figure 4 below. The software visualizes all the registers of the AD9546 when the tab All is selected. The Updated tab lists the registers that the user changed in other parts of the program and has not yet downloaded into the AD9546. The NonDefault tab lists all the registers that have non default values.


|image5|

.. container:: centeralign

   // Figure 4: Register Map Window//


Click on Register Details arrow on the bottom left of the window (Figure 5 below) and the bit content of the particular selected register is displayed. Move the cursor on top of a register and the bit description of that register is visualized.



|image6|

.. container:: centeralign

   // Figure 5: Register Details section of Register Map Window//


-  Debug - Opens the debug window in Figure 6 below. Any register can be accessed by scrolling through the registers in the Register dropdown list or by starting to type the register address expressed in hexadecimal. The value of the register appears and it can be expressed in hex or decimal values. The accessed register can be written or read by clicking on the respective button. The Pin Groups section allows direct control of the AD9546 Reset, M0, M1, M2, M3, M4, M5, and M6/CS pins. The recommendation is to not manage these pins through this window and instead use the Front Panel tabs. For example, manage the M0 to M6 pins through the M_PINS tab in the Front Panel (Figure 2).



|image7|

.. container:: centeralign

   // Figure 6: Debug Window with Register Selection Scroll Down Menu//


Click on Help menu on the top of the front panel (Figure 1) and the following entries are available:

-  License - Displays the evaluation software license.
-  About - Displays version information for the evaluation software.

| The front panel has two tabs, (Figure 6b): Block Diagram and Pinout.
| The Block Diagram provides a user interface to configure all of the AD9546 registers.
| The Pinout provides the list of all the AD9546 pins, their position on the package and their description. |image8|

.. container:: centeralign

   // Figure 6b: Front Panel's Block Diagram and Pinout tabs\ *


At the bottom of the front panel, the following buttons are available:

.. container:: centeralign

   * Figure 6c: Front Panel Buttons\ *


\* WIZARD - Allows the user to introduce the broad requirements that the AD9546 needs to fulfill (like the frequency of the reference clocks, of the outputs, the system clock source, etc). The recommendation is to use the Wizard to calculate the AD9546 register values whenever a new configuration is required. \* READ ALL - Reads the entire AD9546 register map and updates the software. \* LOAD ALL - Loads the register values from the evaluation software into the AD9546 and if the Enable IO Update option is enabled in the Options entry in the File menu, an IO Update is executed automatically at the end of the registers download. \* CONTROL - Opens the window in Figure 7 below. Various tabs give access to serial port settings, calibration and synchronization commands, power down various AD9546 blocks and the Watchdog timer setting in Misc. Controls section.

.. container:: centeralign

   * Figure 7: Control Window\ *


\* STATUS - Opens the window in Figure 8 below. Various tabs give access to status flags of the AD9546 blocks.

.. container:: centeralign

   * Figure 8: Status Window//


-  REGMAP - Opens the register map window (Figure 4) that can be accessed from the front panel View, Register Map option.
-  CAL ALL - Executes the calibration of all analog PLLs of the AD9546, essentially setting bit 1 (all calibrate reg) in register 0x2000 to 1, executing an IO Update, then clearing the bit and again executing an IO Update.
-  SYNC ALL - Executes a Sync All command, essentially setting bit 3 (all sync reg) of register 0x2000 to 1, executing an IO Update, then clearing the bit and again executing an IO Update.
-  RESET - Reset the AD9546 by toggling the RESETB pin of the AD9546 low and then back high.

Frequency Configuration Wizard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, every time the AD9546 Evaluation Software is launched, the Frequency Configuration Wizard is opened. If an AD9546 configuration json file was already created, close the wizard by clicking on the x button on the top right corner of the window and load the file going into File, Configuration Files, Load Configuration File menu (Figure 2). While using the Evaluation Software, the wizard can be launched by clicking on the tab Wizard on the bottom of the front panel (Figure 6c).


|image9|

.. container:: centeralign

   // Figure 9: Frequency Configuration Wizard Window\ *


The wizard contains several tabs: System Clock, Input Sources, Channel 0 and Channel 1. Short explanations of each tab: \* In System Clock, introduce the source of the system clock and the source(s) of the auxiliary DPLL. \* In Input Sources (Figure 10), introduce the reference clock details. Leave the Solving Set Point at 200 kHz as this is the maximum allowed Time to Digital Converter (TDC) input frequency. Make sure the Input Configuration settings match the hardware design. \* In Channel 0 (Figure 11) and in Channel 1 tabs, introduce the details of the output clocks in the Outputs section and set the desired DPLL functionality. Once all this data is introduced, click Load button on the bottom right of the window for the Wizard to calculate the registers values and load them into the AD9546. The Wizard then closes automatically.

.. container:: centeralign

   * Figure 10: Input Sources Tab of the Frequency Configuration Wizard\ *


.. container:: centeralign

   * Figure 11: Channel 0 Tab of the Frequency Configuration Wizard\ *


==== Input Source Settings ==== In the Front Panel (Figure 2), clicking on Input Settings tab launches the window in Figure 12:

.. container:: centeralign

   * Figure 12: Input Source Settings Window\ *


In this window, virtually all the functionality related to the reference clocks can be configured. Click Load to download the register values that have been changed from the evaluation software into the AD9546 and if the Enable IO Update option is enabled in the Options entry in the File menu, an IO Update is executed automatically at the end of the registers download. Also, the window visualizes all the status flags related to the reference that is selected in the window. For example, in Figure 12, the REFA settings are selected. The status flags associated with REFA are also updated in the right side of the window. ==== Digitized Clocking Settings ==== In the Front Panel (Figure 2), clicking on Digitized Clocking tab launches the window in Figure 13.

.. container:: centeralign

   * Figure 13: Digitized Clocking Settings Window\ *


In this window, the Digitized Clocking settings regarding the common clock, the user time stampers and the inverse user time stampers can be introduced. ==== Stability Compensation Settings ==== In the Front Panel (Figure 2), clicking on Stability Compensation tab launches the window in Figure 14.

.. container:: centeralign

   * Figure 14: System Clock Stability Compensation Settings Window\ *


In this window, the system clock stability compensation methods can be selected and configured. ==== Multi - Function Pins Settings ==== In the Front Panel (Figure 2), clicking on M-Pins tab launches the window in Figure 15.

.. container:: centeralign

   * Figure 15: Multi-Function Pins Settings Window\ *


In this window, the multi-function M0, M1,…, M6 pins are configured. The M-pins by Function tab provides a concise view of all M-pins control or status configuration (Figure 26).

.. container:: centeralign

   * Figure 16: M-pins by Function Tab Window//


Interrupt Requests (IRQ) Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Front Panel (Figure 2), clicking on IRQ tab launches the window in Figure 17. In this window, every AD9546 interrupt can be enabled or cleared and their trigger status (set or cleared) is visualized. The Group Clear tab provides access to control bits that clear groups of interrupts, that is the bits 3:0 in register 0x2005 (Figure 18).


|image10|

.. container:: centeralign

   // Figure 17: Interrupt Requests (IRQs) Settings Window\ *


.. container:: centeralign

   * Figure 18: Group Clear Window\ *


==== Temperature Sensor Settings ==== In the Front Panel (Figure 2), clicking on Temp Sensor tab launches the window in Figure 19:

.. container:: centeralign

   * Figure 19: Temperature Settings Window\ *


Move the cursor over the white locations for their description. The Compensation section has three entries: \* Open Loop Stability Temp. Sensor Source refers to the open loop system clock compensation method 1. It selects the temperature sensor used in this method. See Open Loop section of the System Clock Stability Compensation Settings Window (Figure 14). \* Channel 0 Delay and Channel 1 Delay refer to the DPLL0 and DPLL1 delay compensation procedure. It selects the temperature sensor used by this procedure. See Propagation Delay Compensation Section of the DPLL0/DPLL1 Settings window. ==== EEPROM Control Settings ==== In the Front Panel (Figure 2), clicking on EEPROM tab launches the window in Figure 20:

.. container:: centeralign

   * Figure 20: EEPROM Controls Window\ *


This window cannot be used with the AD9546 evaluation board because the board does not contain a EEPROM usable to store the AD9546 configuration. ==== Channel 0 Settings ==== In the Front Panel (Figure 2), clicking on Channel 0 section launches the window in Figure 21:

.. container:: centeralign

   * Figure 21: Channel 0 Settings Window\ *


In this window, all DPLL0 settings can be managed. It is recommended to use the Wizard first to configure the DPLL0 and use this window for additional settings not already set by the Wizard. Click on the DPLL Settings, APLL Settings, DIST (Distribution) Settings tabs on the bottom of the window to access them. Click on Status tab to access the Channel 0 Status window (Figure 22) in which the status flags related to Channel 0 DPLL0+APLL0 are updated. DPLL Settings, APLL Settings and Distribution Settings windows are presented in Figure 23, Figure 24, Figure 25.

.. container:: centeralign

   * Figure 22: Channel 0 Status Window\ *


.. container:: centeralign

   * Figure 23: DPLL0 Settings Window\ *


.. container:: centeralign

   * Figure 24: APLL0 Settings Window\ *


.. container:: centeralign

   * Figure 25: Channel 0 Distribution Settings//


Channel 1 Settings
~~~~~~~~~~~~~~~~~~

In the Front Panel (Figure 2), clicking on Channel 1 section launches a window identical with the Channel 0 Settings window (Figure 21). Use Channel 0 Settings section for more information.

Channel x Settings
~~~~~~~~~~~~~~~~~~

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad9546_evb_connected_to_pc.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad9546_eval_sw_front_panel.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad9546_select_hw_entry_in_file_menu.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/select_hardware.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad9546_register_map_window.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad9546_registers_details_section.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad9546_debug_window.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad9546_block_diagram.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/frequency_configuration_wizard_window.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/interrupt_requests_settings.png
