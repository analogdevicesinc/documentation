User Guide for the AD5522 Evaluation board
==========================================

Quad Parametric Measurement Unit (PMU) With Integrated 16-Bit Level Setting DACs
================================================================================

Features
--------

-  Full-features evaluation board for the :adi:`AD5522`
-  On Board References
-  Link Options
-  Direct hookup to USB port of PC
-  PC Software for control

Quick Start Guide
=================

-  Install the Software

   -  The software should self install after CD-ROM is inserted.
   -  If software installation does not launch, then run “setup.exe” from CR-ROM. This will install the relevant USB drivers and software to your pc.
   -  Software should be installed prior to connection of the eval board to the PC’s USB port to ensure the evaluation board is correctly recognized by the PC.
   -  All software, documentation and config files will be copied to C:\\Program Files\\Analog Devices\\AD5522 by default.

-  Plug in the hardware

   -  Using the USB cable, connect the EVAL-AD5522 to the computer.
   -  You will be prompted to install the USB drivers. The software should find these drivers automatically. You may be required to re-start your pc after the install, but only if prompted.

-  UnPlug the hardware and Apply power supplies.

   -  Now you are ready to use the AD5522 board.
   -  Disconnect the USB cable (Power rails should always be applied prior to USB cable).
   -  Apply appropriate power supplies

      -  AVDD = +15V
      -  AVSS = -15V
      -  DVCC = +5V
      -  +5V = +5V
      -  AGND = DGND = 0V

   -  Now connect the USB cable again, now you are ready to launch software.

-  Running the Chip Programming Software.

   -  Browse to the Analog Devices folder in your Start menu. Go to the AD5522 folder and select the Evaluation software to launch the programming tool.

-  Verifying you are communicating with the Hardware

   -  When the software launches, the main window will open.
   -  Individual Register Access
   -  By default, when the software launches, it writes two commands to the AD5522 to put it into a standard operating mode. These commands are 0x3FE4A0 to System Control register and 0xF21B300 to PMU Register.
   -  This will initialize the device and if you read the voltages at gold pin connections TP 5, 6, 7, and 8 on each channel, you should read 0V (as the FIN DAC is at default setting, 0x8000)

-  Proper sequence of USB/Power Supplies/Software:

   -  Apply power supplies
   -  Connect USB
   -  Launch Software

Evaluation Board Description
============================

The EVAL-AD5522EB is a full-featured evaluation board designed to allow the user to easily evaluate all features of the :adi:`AD5522` Quad channel PMU. The board can be controlled by two means, via the on-board connectors or via the USB port of a Windows- based PC using the :adi:`AD5522` evaluation software. The default setup is for control via the USB port. Please refer to the :adi:`AD5522` datasheet for full details on all functionality of the :adi:`AD5522`\ device and for full details of the each of the Registers within the :adi:`AD5522`.

|image1| Figure 1. Overview of Paddle-Up AD5522 evaluation board (note not all evaluation boards use the socket clamps shown here). The Paddle-Down AD5522 evaluation board is similar.

System Requirements
~~~~~~~~~~~~~~~~~~~

Microsoft Windows 2000/NT/XP/ Microsoft Windows 7 (64-bit/32-bit) USB 2.0 Port

Software needed
^^^^^^^^^^^^^^^

Enclosed CD or available via Website download

Evaluation Kit Contents
^^^^^^^^^^^^^^^^^^^^^^^

-  Evaluation board (as ordered EVAL-AD5522EBUZ (paddle-up package version) or EVAL-AD5522EBDZ (paddle-down paddle version))
-  Software CD

AD5522 Device description
~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD5522`\ is a high performance, highly integrated parametric measurement unit consisting of four independent channels. Each PPMU channel includes five, 16-bit, voltage out DACs setting the programmable inputs levels for the force voltage input, clamp and comparator inputs (high and low). Five programmable force and measure current ranges are available ranging from 5µA to 80mA. Four of these ranges use on chip sense resistors, while a high current range up to 80mA is available per channel using off chip sense resistors. Currents in excess of 80mA require an external amplifier. Low capacitance DUT connections (FOH, EXT FOH) ensure the device is suited to relay less test systems. The PMU functions are controlled via a simple three wire serial interface compatible with SPI/QSPI/Microwire and DSP interface standards. Interface clocks of 50MHz allow fast updating of modes. LVDS (Low Voltage Differential Signaling) interface protocol at 100MHz is also supported. Comparator outputs are provided per channel for device go no-go testing and characterization. Control registers provide easy way of changing force or measure conditions, DAC levels and selected current ranges. SDO (serial data out) allows the user to readback information for diagnostic purposes.

Evaluation board hardware
=========================

Power Supplies
--------------

The following external supplies must be provided.

-  5V/3V between DVCC and DGND inputs for the digital supply of the AD5522 circuitry and other digital circuitry.
-  Supply the AVDD, AVSS and AGND inputs for the positive supply of the AD5522, such that AVDD >=10V, AVSS <=-5V, \|AVDD – AVSS\| >= 20V and <= 33V,
-  +5V for +5V power supply input on power block, this is the power supply for the ADC and for accurate conversions should be a clean supply.

Both AGND and DGND inputs are provided on the board. The AGND and DGND planes are connected at one location close to the AD5522. It is recommended not to connect the AGND and DGND elsewhere in the system to avoid ground loop problems.

Each supply is decoupled to the relevant ground plane with 10μF and 0.1μF capacitors. Each device supply pin is again decoupled with a 0.1μF capacitor to the relevant ground plane.

Link Options
------------

The default configuration for interfacing to the AD5522 device is via the USB interface. Access is provided to all input and output nodes via J3 header in the event a user wants to drive the device by other means. In this case, remove LK9 to disconnect the on board USB circuitry.

Default Link Option Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

The default setup is for control by the PC via the USB port. The default link options are listed in Table 1.

Table 1. Default link conditions

+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link No. | Default  | Function                                                                                                                                                                                                                                                 |
+==========+==========+==========================================================================================================================================================================================================================================================+
| LK1      | Removed  | An LVDS interfacing option is available to drive the AD5522 via the Connecter J3. If LVDS is the interface of choice, then insert a jumper in this position to connect a 100ohm resistor between the SDI differential inputs.                            |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK2      | A        | An LVDS interfacing option is available to drive the AD5522 via the Connecter J3. Position A Selects SPI interface. Position B selects LVDS interface.                                                                                                   |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK3      | Inserted | Link 3 is used for the RESET\\ function. In the event that user is not using PC interface and wishes to drive the RESET\\ directly, remove LK3.                                                                                                          |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK4      | B        | This link selects the reference source, there are three options. Position A selects the on board 2.5V reference. Position B selects the on board 5V reference. Position C connects to an SMB connector to allow an off board reference be connected.     |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK5      | A        | This link allows for selection between a driven DUTGND voltage or direct connection to AGND. Position A connects the DUTGND pin directly to ground. Position B connects the DUTGND pin to an SMB which may be driven by a source (no greater than ±0.5V) |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK6      | Removed  | An LVDS interfacing option is available to drive the AD5522 via the Connecter J3. If LVDS is the interface of choice, then insert a jumper in this position to connect a 100ohm resistor between the SCLK differential inputs.                           |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK7      | Removed  | An LVDS interfacing option is available to drive the AD5522 via the Connecter J3. If LVDS is the interface of choice, then insert a jumper in this position to connect a 100ohm resistor between the SYNC\\ differential inputs.                         |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK8      | Removed  | An LVDS interfacing option is available to drive the AD5522 via the Connecter J3. If LVDS is the interface of choice, then insert a jumper in this position to connect a 100ohm resistor between the SDO differential inputs.                            |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK9      | Inserted | Link 9 should be removed if the user does not intend to use the PC and USB interface to control the device.                                                                                                                                              |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK10     | Removed  | Link to be used to connect MEASOUT0 to the AD7685 ADC input. (DO NOT CONNECT MORE THAN ONE OF LK10,LK11,LK12, LK13 at any one time)                                                                                                                      |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK11     | Removed  | Link to be used to connect MEASOUT1 to the AD7685 ADC input. (DO NOT CONNECT MORE THAN ONE OF LK10,LK11,LK12, LK13 at any one time)                                                                                                                      |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK12     | Removed  | Link to be used to connect MEASOUT2 to the AD7685 ADC input.(DO NOT CONNECT MORE THAN ONE OF LK10,LK11,LK12, LK13 at any one time)                                                                                                                       |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK13     | Inserted | Link to be used to connect MEASOUT3 to the AD7685 ADC input. (DO NOT CONNECT MORE THAN ONE OF LK10,LK11,LK12, LK13 at any one time)                                                                                                                      |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK14     | B        | Used for Guard amplifier input purposed on CH2                                                                                                                                                                                                           |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK15     | B        | Used for Guard amplifier input purposed on CH0                                                                                                                                                                                                           |
+----------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Using the AD5522 Evaluation Board
---------------------------------

The :adi:`AD5522` board is flexible in that users can use any DUT at the output of each :adi:`AD5522` device. Gold pin connectors allow for RDUT and CDUT connections. The range of the CDUT load should be confined to the maximum DUT capacitance as outlined in the :adi:`AD5522` datasheet. The measure function may be accessed via the SMB connectors connected at each MEASOUT pin. The on board ADC can perform measurements on measured parameter, however, please ensure that if all MEASOUT pins are connected together, that the Hi-Z mode is used, alternatively, use Links LK10-LK13 to ensure only one MEASOUT signal is connected to the ADC at any one time. CH1 and CH3 have a selectable range of compensation and feedforward capacitors that may be selected to optimize settling and stability in a wide range of DUT loads.

Evaluation board Software
=========================

Software Installation
---------------------

The :adi:`AD5522` evaluation kit includes self-installing software on CR-ROM. The software is compatible with Windows 2000/NT/XP. If the setup file does not run automatically, setup.exe can be run from the CD-ROM. The evaluation software should be installed before connecting the evaluation board to the PC’s USB port to ensure that the evaluation board is correctly recognized when connected to the PC.

-  After the installation from the CD-ROM is complete, power up the :adi:`AD5522`\ evaluation board as described in the Power Supplies section, then connect it to the USB port of your PC using the supplied code.
-  When the evaluation board is detected, proceed through any dialog boxes that appear. This finishes the installation.

Software Operation
------------------

To launch the software, select the :adi:`AD5522`\ submenu from the Analog Devices menu. Next, click :adi:`AD5522` Evaluation Software. The main window of the :adi:`AD5522`\ software looks as follows : |image2| This allows control of all the main functions of the :adi:`AD5522`\ and access to the DAC registers as required. When the software is launched, there are two patterns loaded to the device. These commands are 0x3FE4A0 to System Control register and 0xF21B300 to PMU Register. These initialize the PMU into operation mode, where Measout Gain = 0.2, the Clamps & comparators are enabled, each PMU register is enabled and placed in Force Voltage mode, 2mA Irange and Measure Voltage mode for measuring. For access to all the individual registers within the device, open the “individual register access” window which launches the following window.


|image3|

The window shows a number of Tabs that allow the user to control different registers within the AD5522 and different functions on the AD5522 evaluation board, e.g. Write and Read functions of the following registers – System Control Reg, PMU Reg, DAC Registers in addition to Compensation selection and a small selection of routines that allow for analysis of settling performance.

System Control Register
^^^^^^^^^^^^^^^^^^^^^^^

The System control register allows the user to set up different functions within the device – refer to the AD5522 datasheet for full details.


|image4|

PMU Register
^^^^^^^^^^^^

The PMU Register allows the user to set up the different force/measure/compare functions. Simply select the channel you wish to write to, select the enable check box and the required ranges. Also, ensure that the FIN to FORCE DAC check box is checked.


|image5|

DAC Register
^^^^^^^^^^^^

The DAC register give access to all of the 21 DACs contained in this device. Simply select the PMU channel to be addressed, load the new DAC code value (x1) or gain (m) or offset (c) code in HEX and press enter/return on the keyboard. DAC updates require use of the AD5522 internal calibration engine and updates will only occur when a new x1 value is loaded. M or C values will not cause an update of the dac, until the x1 value is again loaded.


|image6|

Compensation Selection
^^^^^^^^^^^^^^^^^^^^^^

The compensation selection Tab allows for selection of compensation and feedforward capacitors on CH1 and CH3. The appropriate capacitor values may be selected depending on the load capacitance at the DUT.


|image7|

ALARM Status Register
^^^^^^^^^^^^^^^^^^^^^

The Status register shows the status of the Alarm functions and reports the output of the comparators.


|image8|

Little Routines
^^^^^^^^^^^^^^^

This option allows the user to analyse the performance of the AD5522 under different settling time conditions and range change conditions.


|image9|

Sweep Voltage, Measure versus time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The File->Sweep Voltage and Time Routine launches another window which allows the user to create voltage sweeps and time measurement sweeps while measuring voltage or current. The on board ADC allows for digital capture of the measured parameter and displays it in plot format. For number crunching, the data is also available to copy to the clipboard and port into other formats (such as Excel or Word). For these operations to function correctly, ensure you select the correct reference value. Note that LK 4 on the evaluation board selects the reference, when in position B = 2.5V, Position A = 5V. The “No Handles” function allows you to zoom in on particular parts of the plot – simply click to turn the handles on and then pull the tabs at the corners of the x or y axis.


|image10|

Test procedure for trouble shooting/testing board operation
===========================================================

Equipment
~~~~~~~~~

-  AD5522 Evaluation Board
-  USB Cable
-  Power supply with ±15V rails and +5V rail.
-  4 x 5.6k resistors (one each to be connected to gold pins at RDUT0, RDUT1, RDUT2, RDUT3)
-  PC with AD5522 evaluation software already installed
-  Voltmeter

Procedure
~~~~~~~~~

-  Apply power supplies, AVDD = +15V, AVSS = -15V, DVCC = +5V, (apply +5V to the +5V terminal block also). AGND=DGND = 0V.
-  LED, D4 should light.
-  Supply current on power up no more than +/-15mA (AVDD/AVSS), ~5mA from DVCC
-  Now connect USB, LED D1 should light, LED D4 should go out
-  Launch software from Start ->All Programs ->Analog Devices -> AD5522
-  Supply current now should be in the region of +/-25mA (AVDD/AVSS)
-  Measure VREF voltages, 5V and 2.5V voltages. tat LK4A and LK4B.
-  Place the 5.6k resistors at the RDUT0/1/2/3
-  In the main control panel window, set the FV = 5V, measure corresponding voltage at each RDUT points, should also read 5V. Check corresponding Measout voltages, noting that the MEASOUT GAIN = 0.2 setting is programmed by the software, therefore the output range will be scaled accordingly.
-  Repeat using FI mode of operation and verify channel voltages/currents for known load.

Schematics, Gerbers, BOM, Software
==================================

EVAL-AD5522EBUZ Paddle Up
-------------------------

-  `Schematics <https://wiki.analog.com/_media/resources/eval/analog_devices_ad5522ebuz_reva_schematic.pdf>`__
-  `BOM <https://wiki.analog.com/_media/resources/eval/ad5522ebuz_a.xls>`__
-  `Mentor Graphics Pads Schematic & Layout <https://wiki.analog.com/_media/resources/eval/ad5522ebuz_a.zip>`__

EVAL-AD5522EBDZ Paddle Down
---------------------------

-  `Schematics <https://wiki.analog.com/_media/resources/eval/analog_devices_ad5522ebdz_rev_b_schematic.pdf>`__
-  `Gerbers <https://wiki.analog.com/_media/resources/eval/ad5522ebdz_b1.zip>`__
-  `BOM <https://wiki.analog.com/_media/resources/eval/ad5522ebdz_b3.xls>`__
-  `Mentor Graphics Pads Schematic & Layout <https://wiki.analog.com/_media/resources/eval/ad5522ebdz_b.zip>`__

Software
--------

-  :adi:`AD5522 Evaluation software - Version 1.6 <static/imported-files/eval_boards/AD5522_evaluation_software.zip>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad5522_pu.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/software_front.jpg
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/reg_detail.jpg
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/sys_control_reg.jpg
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/write_pmu_reg.jpg
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/write_dac_reg.jpg
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/write_comp_reg.jpg
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/write_alarm_status.jpg
   :width: 800px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/little_routines.jpg
   :width: 800px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/voltage_sweep.jpg
   :width: 800px
