User Guide for the EVAL-ADATE318BCPZ Evaluation Board
=====================================================

600 MHz Dual Integrated DCL with PPMU, VHH Drive Capability, Level Setting DACs, and On-Chip Calibration Engine
---------------------------------------------------------------------------------------------------------------

Features
--------

-  Full-features evaluation board for the :adi:`ADATE318`
-  Supply voltages: +21V and -10V, On-board Voltage Regulators
-  Signal inputs/outputs breakout via SMA connectors
-  LED indicators for read/write data
-  PC Software for control via USB

Evaluation Kit Contents
-----------------------

-  EVAL-ADATE318BCPZ Evaluation Board
-  ADATE318 Customer Evaluation Software CD

Equipment Needed
----------------

-  PC running Windows®
-  USB 2.0 port and USB 2.0 High-speed A to B Cable
-  Benchtop Power Supplies and Connector Cables
-  Data Timing Generator (DTG) or equivalent
-  Oscilloscope

Additional Documents Required
-----------------------------

-  :adi:`ADATE318` Datasheet

General Description
===================

The EVAL-ADATE318BCPZ evaluation board for the :adi:`ADATE318` features breakout connections via SMA terminals for all the signal inputs and outputs. The differential pairs are provided with 50ohm controlled impedance traces with equal lengths. The board only takes in +21V and -10V supplies and the on-board regulators provides the required part supplies. Communication to the Evaluation Board Software is via USB and LED indicators on the board provide display for the read or write data.

The :adi:`ADATE318` datasheet provide additional information and should be consulted when using the evaluation board. All documents and software tools are available at the :adi:`ADATE318` main page.

Quick Start Guide
=================

-  Install the Software

   -  Insert the CD that contains the evaluation software to the PC then run “setup.exe” from CD-ROM. This will install the relevant USB drivers and software to your PC.
   -  Software should be installed prior to connection of the evaluation board to the PC’s USB port to ensure the board is correctly recognized by the PC.
   -  All software, documentation and setup files will be copied to C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\ADATE318 Evaluation Board Software by default.

-  Plug in the hardware

   -  Using the USB cable, connect the EVAL-ADATE318 to the computer.
   -  You will be prompted to install the USB drivers. The software should find these drivers automatically. You may be required to restart your PC after the installation.

-  Unplug the USB cable then apply power supplies.

   -  Now you are ready to use the ADATE318 board.
   -  Disconnect the USB cable (Power rails should always be applied prior to USB cable).
   -  Apply appropriate power supplies

      -  +21VDC = +21V
      -  -10VDC = -10V
      -  GND = 0V

   -  Connect the USB cable again then launch the software.

-  Running the Evaluation Software.

   -  Browse for ADATE318 Evaluation Board Software in your Start menu.

-  Verifying you are communicating with the Hardware

   -  When the software launches, the main window will open if there are no issues. A command prompt indicating errors will pop up otherwise.
   -  To verify the communication with the hardware, a Read All command may be initiated. The software will reflect the default values upon power up if there is successful communication.

Evaluation Board Description
============================

The EVAL-ADATE318BCPZ is a full-featured evaluation board designed to allow the user to easily evaluate all features of the :adi:`ADATE318` Dual Integrated DCL with PMU. The board can be controlled by two means, via the on-board connectors or via the USB port of a Windows- based PC using the :adi:`ADATE318` evaluation software. The default setup is for control via the USB port. Please refer to the :adi:`ADATE318` datasheet for full details on all functionality of the :adi:`ADATE318` device and for full details of the each of the Registers within the :adi:`ADATE318`.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adate318bcpz_top.jpg

Figure 1. Overview of EVAL-ADATE318BCPZ evaluation board.

ADATE318 Device Description
===========================

The :adi:`ADATE318` is a complete, single-chip ATE solution that performs the pin electronics functions of driver, comparator, and active load (DCL), four quadrant, per pin, parametric measurement unit (PPMU). It has VHH drive capability per chip to support flash memory testing applications and integrated 16-bit DACs with an on-chip calibration engine to provide all necessary dc levels for operation of the part.

The driver features three active states: data high, data low, and terminate mode, as well as a high impedance inhibit state. The inhibit state, in conjunction with the integrated dynamic clamps, facilitates the implementation of a high speed active termination. The output voltage capability is −1.5 V to +6.5 V to accommodate a wide range of ATE and instrumentation applications.

The :adi:`ADATE318` can be used as a dual, single-ended drive/ receive channel or as a single differential drive/receive channel. Each channel of the ADATE318 features a high speed window comparator as well as a programmable threshold differential comparator for differential ATE applications. A four quadrant PPMU is also provided per channel. All dc levels for DCL and PPMU functions are generated by 24 on-chip 16-bit DACs. To facilitate accurate levels programming, the :adi:`ADATE318` contains an integrated calibration function to correct gain and offset errors for each functional block. Correction coefficients can be stored on chip, and any values written to the DACs are automatically adjusted using the appropriate correction factors.

The :adi:`ADATE318` uses a serial programmable interface (SPI) bus to program all functional blocks, DACs, and on-chip calibration constants. It also has an on-chip temperature sensor and over/undervoltage fault clamps for monitoring and reporting the device temperature and any output pin or PPMU voltage faults that may occur during operation.

Evaluation board hardware
=========================

Power Supplies
--------------

The following external supplies must be provided:

-  21V between +21VDC and GND.
-  -10V between -10VDC and GND.

GND input is provided on the board. Each device supply is decoupled to GND with 10μF and 0.1μF capacitors. Each device supply pin is again decoupled with a 0.1μF capacitor to GND.

Default Jumper Setup
--------------------

The default setup is for control by the PC via the USB port. The default link options are listed in Table 1.

Table 1. Default Jumper Setup

+------------+----------+------------------------------------------------------------------+
| Jumper No. | Default  | Function                                                         |
+============+==========+==================================================================+
| P2         | Inserted | Current measurement terminal for VPLUS (0.1 Ohm Sense Resistor)  |
+------------+----------+------------------------------------------------------------------+
| P7         | Inserted | Current measurement terminal for VTT_C (0.1 Ohm Sense Resistor)  |
+------------+----------+------------------------------------------------------------------+
| P5         | Inserted | Current measurement terminal for VDD (0.1 Ohm Sense Resistor)    |
+------------+----------+------------------------------------------------------------------+
| P6         | Inserted | Current measurement terminal for VSS (0.1 Ohm Sense Resistor)    |
+------------+----------+------------------------------------------------------------------+
| P3         | Inserted | Current measurement terminal for VCC (0.1 Ohm Sense Resistor)    |
+------------+----------+------------------------------------------------------------------+
| P1         | 2-3      | BUS_RW control to indicate whether SPI bus is reading or writing |
+------------+----------+------------------------------------------------------------------+
| P12        | 1-2      | CS_B_EVAL – Device SPI Chip Select (On-board or external)        |
+------------+----------+------------------------------------------------------------------+
| P11        | 1-2      | SDO_EVAL – Device SPI Slave Device Out (On-board or external)    |
+------------+----------+------------------------------------------------------------------+
| P8         | 1-2      | SCLK_EVAL – Device SPI Clock (On-board or external)              |
+------------+----------+------------------------------------------------------------------+
| P9         | 1-2      | SDI_EVAL – Device SPI Slave Device Input (On-board or external)  |
+------------+----------+------------------------------------------------------------------+
| P10        | 1-2      | RESET_B_EVAL – Device Reset Signal (On-board or external)        |
+------------+----------+------------------------------------------------------------------+

Using the ADATE318 Evaluation Board
-----------------------------------

The :adi:`ADATE318` board requires on two voltage supplies (+21V and -10V). These supplies are enough to power the entire board including the digital portion. This board also has SMA provision for both the inputs and outputs. Recommended to be controlled via USB, this board can be used with the provided software for easy access to user registers within :adi:`ADATE318`. Designed to be interactive, the ADATE318BCPZ also features an LED array at the bottom portion to help the user know that the correct data are being written to or read from the part.

Evaluation board Software
=========================

Software Operation
------------------

To launch the software, select the :adi:`ADATE318` submenu from the Analog Devices menu or use Windows Search. Next, click :adi:`ADATE318` Evaluation Software. The main window of the :adi:`ADATE318` software looks as follows:

.. image:: https://wiki.analog.com/_media/resources/eval/adate318.jpg

This allows control of all the main functions of the :adi:`ADATE318` and access to the DAC registers as required. The main window of the software include three sections. One of them is the DAC Levels section which allows the user to write to the DACs within :adi:`ADATE318` either all in one click or singly. The Single Read and Write section meanwhile allows the user to read or write to a specific register, may it be a DAC register or a control register. The Control Register section lets the user configure the settings of :adi:`ADATE318`.

DAC Level Registers
~~~~~~~~~~~~~~~~~~~

The DAC Level Registers section, located at the upper left of the user interface, lists all the current settings of the DACs within :adi:`ADATE318`. Changing the values at a text field and pressing 'Enter' in this section is equivalent to writing that value to the specific DAC. The corresponding value (HEX code or Voltage) will change accordingly.

This section also lets the user load or save register settings for all DAC and Control registers for quicker testing.

.. image:: https://wiki.analog.com/_media/resources/eval/adate318_user_registers.jpg

Single Read and Write Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section of the user interface makes it easy for the user to write to or read from specific registers as desired. Note that when reading from a register, it is not necessary to fill the data field as this field will show the data read from the part.

.. image:: https://wiki.analog.com/_media/resources/eval/adate318_read_write.jpg

Control Registers
~~~~~~~~~~~~~~~~~

It would have been difficult for the user to manually fill the single write section to configure the settings of :adi:`ADATE318`, thus this section is built to address this. This section allows modification of the part's settings by letting the user know which register is being written to, and what specific setting is being changed. Alarms can also be read from this section.

.. image:: https://wiki.analog.com/_media/resources/eval/adate318_control_registers.jpg

Schematics and Software
=======================

EVAL-ADATE318BCPZ
-----------------

-  `Schematics <https://wiki.analog.com/_media/resources/eval/02-048233-01-c2.pdf>`_

Software
--------

-  `ADATE318 Evaluation Software <https://wcm.cldnet.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADATE318.html>`_
