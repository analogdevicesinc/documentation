User Guide for the AD5560 Device Power Supply (DPS) with DACs
=============================================================

Features
--------

-  Full-features evaluation board for the :adi:`AD5560`
-  On Board References
-  Link Options
-  On Board ADC
-  Direct hookup to USB port of PC
-  PC Software for control

Quick Start Guide
=================

-  Install the Software

   -  The software should self install after CD-ROM is inserted.
   -  If software installation does not launch, then run “setup.exe” from CD-ROM. This will install the relevant USB drivers and software to your pc. Note that the software is currently only compatible with PCs running OS up to Windows XP.
   -  Software should be installed prior to connection of the eval board to the PC’s USB port to ensure the evaluation board is correctly recognized by the PC.
   -  All software, documentation and config files will be copied to C:\\Program Files\\Analog Devices\\AD5560 by default.

-  Plug in the hardware

   -  using the USB cable, connect the EVAL-AD5560 to the computer.
   -  You will be prompted to install the USB drivers. The software should find these drivers automatically. You may be required to re-start your pc after the install, but only if prompted.

-  UnPlug the hardware and apply power supplies.

   -  Now you are ready to use the AD5560 board.
   -  Disconnect the USB cable (Power rails should always be applied prior to USB cable).
   -  Apply appropriate power supplies

      -  AVDD = +15V
      -  AVSS = -15V
      -  HCAVDD = as required for your evaluations - can be left open and HCAVDD will be pulled up to AVDD
      -  HCAVSS = as required for your evaluations - can be left open and HCAVSS will be pulled up to AVSS
      -  DVCC = +5V
      -  +5V = +5V
      -  AGND = DGND = 0V

   -  Now connect the USB cable again, now you are ready to launch software.

-  Running the Chip Programming Software.

   -  Browse to the Analog Devices folder in your Start menu. Go to the AD5560 folder and select the Evaluation software to launch the programming tool.

-  Verifying you are communicating with the Hardware

   -  When the software launches, the main window will open
   -  By default, when the software launches, it writes two commands to the AD5560 to put it into a standard operating mode. These commands are 0x12200 to System Control register and 0x29950 to DPS1 Register.
   -  This will initialize the device into powered up mode, with the Force Amplifier Enabled. It will select the 2.5mA current range, the Measout = MV and the Clamps will be enabled. The Measout Gain setting = 0.2. The Offset DAC is at default of 0x8000 as are all other DAC registers. Safe mode compensation is the power on default here.

-  Proper sequence of USB/Power Supplies/Software:

   -  Apply power supplies
   -  Connect USB
   -  Launch Software

Evaluation Board Description
============================

The EVAL-AD5560EB is a full-featured evaluation board designed to allow the user to easily evaluate all features of the :adi:`AD5560` DPS The board can be controlled by two means, via the on-board connectors or via the USB port of a Windows- based PC using the :adi:`AD5560` evaluation software. The default setup is for control via the USB port. Please refer to the :adi:`AD5560` datasheet for full details on all functionality of the :adi:`AD5560` device and for full details of the each of the Registers within the :adi:`AD5560` .


|image1|

AD5560 Device Description
-------------------------

The :adi:`AD5560` is a high performance, highly integrated device power supply consisting of programmable force and measure channels. This product includes the required DAC levels to set the programmable inputs for the drive amplifier, clamping and comparator circuitry. Offset and Gain correction is included on chip for DAC functions. A number of programmable measure current ranges are available, five internal fixed ranges and two external customer selectable ranges (EXTFORCE 1 and EXTFORCE 2) which can supply currents up to 1.2A and 500mA respectively. For purposes of this evaluation board, the Rsense resistors used for the two external EXT1 and EXT2 ranges are larger than that required for a 1.2A and 500mA range respectively. This is due to the lack of cooling available for a demonstration board. The voltage range possible at this high current level is limited by headroom and the maximum power dissipation. Current ranges in excess of 1.2A or at high current and high voltage combinations may be achieved by ganging multiple DPS devices. Open drain alarm outputs are provided in the event of over-current, over-temperature or Kelvin alarm on either the sense or DUTGND lines.

Evaluation Board Hardware
=========================

Power Supplies
--------------

The following external supplies must be provided.

-  5V/3V between DVCC and DGND inputs for the digital supply of the :adi:`AD5560` circuitry and other digital circuitry.
-  Supply the AVDD, AVSS and AGND inputs for the positive supply of the :adi:`AD5560`, such that AVDD >=10V, AVSS <=5V, \|AVDD – AVSS\| >= 20V and <= 33V,
-  +5V for +5V power supply input on power block, this is the power supply for the ADC and for accurate conversions should be a clean supply.
-  Supplies for HCAVDD1, HCAVDD2, HCAVSS1, HCAVSS2 may be chosen such that minimum power dissipation will be dissipated in the device. Alternatively, they may be connected to the AVDD, AVSS supplies. (see datasheet supplies section for more details on using the HC supplies).

Both AGND and DGND inputs are provided on the board. The AGND and DGND planes are connected at one location close to the AD5560. It is recommended not to connect the AGND and DGND elsewhere in the system to avoid ground loop problems.

Each supply is decoupled to the relevant ground plane with 10μF and 0.1μF capacitors. Each device supply pin is again decoupled with a 0.1μF capacitor to the relevant ground plane. Exposed paddle on AD5560 is internally connected to AVSS. Addition of a DUT is required for operation; please connect to gold pins or SM connections provided.

Link Options
------------

The default configuration for interfacing to the :adi:`AD5560` device is via the USB interface. Access is provided to all input and output nodes via J3 in the event a user wants to drive the device by other means. In this case, remove LK9 to disconnect the on board USB circuitry. Default Link Option Setup The default setup is for control by the PC via the USB port. The default link options are listed in Table 1.

**Table 1. Link Options for PC control**

======== ============== =======================================
Link No. Default option Function
======== ============== =======================================
LK1      Inserted       Remove if USB interface is not required
LK2      Inserted       Used for RESET cct
LK3      Inserted       Used to connect GPO to temp Sensor
LK4      Inserted       
LK5      Inserted       In series with EXTMEASIL path
LK6      Inserted       In series with FORCE path
LK7      Inserted       In series with SENSE path
LK8      Inserted       Used to connect DUTGND to AGND
LK11     A              Reference selection
\                       A: 5V
\                       B: 2.5V
\                       C: External Reference input
======== ============== =======================================

The ADC is a 5V device, so gain of 0.2 (for MEASOUT) should always be selected if using ADC for measurements. If gain = 1, then LK 4 should be removed to protect the ADC (assuming that LK 4 is in position A).

Using the AD5560 board
----------------------

The :adi:`AD5560` board is flexible in that users can use any DUT at the output of each AD5560 device. Gold pin connectors allow for RDUT and CDUT connections. The range of the CDUT load should be confined to the maximum DUT capacitance as outlined in the AD5560 datasheet. (max of 160uF) The measure function may be accessed via the SMB connectors connected at the MEASOUT pin. The on board ADC can perform measurements on measured parameter, however, please remember the ADC is a 5V device, therefore, should only be used with MEASOUT GAIN = 0.2. Please remove LK4 if using MEASOUT GAIN = 1.

Evaluation Board Softare
========================

Software Installation
---------------------

The :adi:`AD5560` evaluation kit includes self-installing software on CR-ROM. The software is compatible with Windows 2000/NT/XP. If the setup file does not run automatically, setup.exe can be run from the CD-ROM. The evaluation software should be installed before connecting the evaluation board to the PC’s USB port to ensure that the evaluation board is correctly recognized when connected to the PC.

-  After the installation from the CD-ROM is complete, power up the AD5560 evaluation board as described in the Power Supplies section, then connect it to the USB port of your PC using the supplied code.
-  When the evaluation board is detected, proceed through any dialog boxes that appear. This finishes the installation.

Software Operation
------------------

Main software menu
~~~~~~~~~~~~~~~~~~

To launch the software, select the :adi:`AD5560` submenu from the Analog Devices menu. Next, click AD5560 Evaluation Software. The main window of the :adi:`AD5560` software looks as follows : |image2| This window allows user to set up all functions. Once the information is loaded to the GUI, it is loaded to the device.

Access all registers window
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The window shows a number of Tabs that allow the user to control different registers within the AD5560 and different functions on the :adi:`AD5560` evaluation board, e.g. Write and Read functions of the following registers – System Control Reg, DPS Registers, DAC Registers. |image3| The ADC is a 5V device, so gain of 0.2 (for MEASOUT) should always be selected if using ADC for measurements. If gain = 1, then LK4 should be removed to protect the ADC. Each of these registers require that the GREEN button be hit to load the relevant register.

Compensation Selection Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The compensation selection Tabs allows access to the compensation registers to set the different compensation parameters manually or automatically. The appropriate capacitor values may be automatically selected depending on the load capacitance at the DUT. By default, the power on mode of the device (and the eval s/w) is “SAFE MODE”. Please bear this in mind when making settling time measurements.

|image4| Each of these registers require that the GREEN button be hit to load the relevant register.

Temperature Sensor & Diagnostic Features Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This register allows access to internal nodes within the AD5560 such as the thermal array scattered across the different portions of the die. Included on the evaluation board is a temp sensor to allow conversion of the diode voltages to temperature, see ADT7461 tab for temp sampling. The `ADT7461 <http://www.onsemi.com/PowerSolutions/product.do?id=ADT7461>`_ is an ON Semiconductor product.


|image5|

Voltage Measurement Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here sweeps of current/voltage may be performed. Also measurements with respect to time (Note: time measurements will be affected by other PC operations – so may not in fact be truly representative of time). Settling time routines and range change transients also all for analysis of the AD5560 device. The ADC is a 5V device, so gain of 0.2 (for MEASOUT) should always be selected if using ADC for measurements. |image6|


|image7|

Schematics, Layout, Gerbers, BOM and Software
=============================================

-  `Schematics in pdf format <https://wiki.analog.com/_media/resources/eval/analog_devices_ad5560ebuz_rev_a_schematic.pdf>`_
-  `Mentor Graphics Pads Schematic & Layout <https://wiki.analog.com/_media/resources/eval/analog_devices_ad5560ebuz_rev_a_schematic_layout.zip>`_
-  `Gerbers <https://wiki.analog.com/_media/resources/eval/ad5560ebu_a.zip>`_
-  `BOM <https://wiki.analog.com/_media/resources/eval/ad5560ebu_a3.xls>`_
-  Software Download available from: :adi:`AD5560_Evaluation_Software.zip <static/imported-files/eval_boards/AD5560_Evaluation_Software.zip>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/simple_block_evb.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad5560_front_panel.jpg
   :width: 700px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad5560_all_regs.jpg
   :width: 700px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ad5560_compensation.jpg
   :width: 700px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad5560_temp_sensor.jpg
   :width: 700px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad5560_votlage_measure.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad5560_votlage_measure2.jpg
   :width: 600px
