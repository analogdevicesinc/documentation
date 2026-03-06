EPS Hardware User's Guide
=========================

Objective:
----------

The purpose of this document is to serve as a User's Guide to the operation of the EPS plugin module for use with the Analog Discovery USB Lab instrument.

<fc #FF0000>This Draft copy of the document is specific to the 8-2-2013 version of the hardware.</fc>

Background:
-----------

This Analog Discovery plugin module is designed to support lab activities exploring a variety of electrical engineering concepts related to the generation, storage and control of energy and power.

Materials:
----------

| EPS plugin board
| Analog Discovery module
| 9 V battery or equivalent DC voltage source
| 3.6 V ( three cell ) rechargeable battery either NiCd or NiMH
| Small solar panel ( > 6 V\ :sub:`OS` or solar panel simulator board, see Appendix )

Directions:
-----------

Plug the EPS board into the 30 pin connector on the Analog Discovery module as shown in figure 1. Be sure to orient the board so that the motor/generator is at the top, Discovery connector is to the left and the 8 position DIP switch, S1, and LEDs are at the bottom. Connect the 9 V battery ( or equivalent DC voltage source ) to the two pin male header marked 9V ( upper right corner of the board ). Be sure to observe the proper polarity as marked next to the header, "+9V" and "GND". Next connect the rechargeable battery to the two pin ( right angle ) header marked BAT in the lower right corner of the board closest to the mounting hole in the board. Be sure to connect the negative side, black wire, to the lower of the two pins marked GND. Just above this header is another two pin ( right angle ) header marked SP. This is where you connect the solar panel ( or solar panel simulator board ). Again be sure to observe the proper polarity by connecting the negative side of the panel connector, black wire, to the pin marked GND.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_12.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, EPS board plugged into Discovery with solar panel and battery


Hardware Configuration:
-----------------------

The EPS board contains 6 LEDs which serve as loads to the power system. They are each individually switchable by either the 6 right most positions on the DIP switch S1, up is off, down is on, or the first six DIO pins, DIO 0-5, on the Discovery connector. When using the Discovery to control the LEDs the DIP switches must be in the up or off position.

The EPS board contains an ADG609 dual 4 into 1 analog multiplexer. This allows 8 different points around the system to be measured or monitored. The Mux is controlled by DIO bits 6,7,8. DIO 6 is Mux address pin A0, DIO 7 is Mux address A1 and DIO 8 in the Mux Enable input. Driving DIO 8 to a logic 1 ( high ) enables the Mux outputs. A logic 0 disables the outputs or forces the outputs of the Mux to a high impedance ( off ) state. The 8 possible measurements are listed in Table 1.

========== ========== =============== ==============================
Mux bit A1 Mux bit A0 Scope CH1       Scope CH2
========== ========== =============== ==============================
0          0          I\ :sub:`LOAD`  V\ :sub:`MAIN` ~ V\ :sub:`BAT`
0          1          I\ :sub:`GEN`   V\ :sub:`GEN`
1          0          I\ :sub:`SOLAR` V\ :sub:`SOLAR`
1          1          I\ :sub:`BAT`   I\ :sub:`MOTOR`
========== ========== =============== ==============================

Table 1 Analog Mux controls

The left most 2 switches of the 8 position DIP switch either connect or disconnect the analog multiplexer to scope channels 1 and 2. When up (off) the Mux is disconnected and the two positive scope channels can be accessed at two pin header AIN. The negative side of the two scope channels and be either accessed or grounded through the two 2 pin headers marked C1- and C2-. The two negative scope channels should be grounded when using the analog Mux. These connections allow the scope channels to be directly connected to higher voltage points in the system, above or below the +/- 5 V power supplies, potentially not available through the Mux. With the Mux outputs disabled, DIO 8 at logic 0, but still connected with the two DIP switches closed, any voltages applied to AIN must be within the +/- 5 V power supplies. These two switches are generally left in the down position (on) connecting the scope channels to the Mux outputs.

There are 5 current sensor amplifiers ( AD822 dual rail-to-rail opamps ) on the board. Each is configured to convert the measured current into a voltage scaled such that 10 mV is equal to 1 mA. The shunt resistors are 1.5? and the difference amplifiers have a gain of 10/1.5. You can use the Math channels to scale or calibrate the signals as needed. Four of the 1.5? shunt resistors have two pin headers across them to serve as test / calibration access points. IL is for the LED load shunt. IGEN is for the generator shunt. ISP is for the solar panel shunt. IBAT is for the rechargeable battery shunt.

There is the possibility that the measured voltages might go above the fixed +5 V supply of the analog multiplexer. To avoid this possibility divide by 2 voltage dividers are inserted between the Mux inputs and the three voltage measurement points. The voltage measured by the scope channels will thus be approximately 1/2 the actual values. Use the Math channels to scale or calibrate the signals back up to their actual values.

The board contains a mechanically coupled motor-generator set. The motor is powered by an external 9 V battery or an equivalent DC voltage source up to +10 V. The switch labeled SWT, next to the 9 V power connector, turns on and off the +9 V supply to this part of the system. The drive voltage for the motor is produced by a linear voltage regulator, shown in figure 2, and can be controlled in multiple ways. Two different feedback paths are selected by the switch labeled FB ( on right side of board ). There are two switch positions, one does not have a small round dot showing and the other does have the small round dot showing.

In the first mode ( dot NOT showing ) the voltage across the motor terminals is set according to either an on board zener voltage reference adjustable with the potentiometer on the right side of the board marked R30 with jumper W1 open or, if W1 is shorted and the potentiometer is set to somewhere in the middle of its range, by the AWG1 analog voltage output from the Discovery connector. The regulator is set up with a gain of 2 so the voltage on the motor will be 2 times the voltage AWG1 is set to. This allows the voltage on the motor to be set greater than the +5 V maximum DC output of AWG1.

In the second mode ( dot showing ) the voltage at the load ( LEDs ) is set according to the on board reference or the AWG 1 output as in the first mode ( same gain of two factor ). The output of the generator is connected to the main load bus though a Schottky diode to prevent the rechargeable battery from driving the generator as a motor. In this configuration the full combined motor / generator set is included in the feedback path. The motor-generator will only supply current to the load if the voltage on the main load bus drops below the set point of the regulator, when the LED loads are switched on for example. It is not advisable to operate the board in this second mode without the rechargeable battery connected.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_user_g_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Simplified motor driver block diagram


The output of the solar panel ( or solar panel simulator ) is connected to the main load bus though a Schottky diode to again prevent the rechargeable battery from discharging though the solar panel when there is not sufficient current ( low light level condition ) generated by the panel.

The board contains a digital output Hall effect magnetic sensor positioned next to a magnet on the motor-generator shaft to measure the rotational speed of the motor. The sensor is powered from the fixed +5 V supply from the Discovery connector. The digital output of the sensor is connected to the DIO 15 digital input on the Discovery connector.

Operating Procedure:
--------------------

The EPS plugin can be manually controlled though the DIP switches and the R30 potentiometer. The Digilent Waveforms software instruments can also be used to control the hardware. The static I/O window can be used to control the LEDs and the Mux select lines by configuring DIO 0-8 as push/pull switches. The voltage window is used to turn on and off the fixed + and - 5 V power supplies to the Mux, current sense amplifiers and Hall effect sensor. The scope or the voltmeter instruments can be used to measure, monitor or display the analog voltages and currents. The digital output signal from the Hall effect RPM sensor can be viewed simultaneously with the analog signals in the scope instrument by clicking on the digital icon and adding DIO 15 as an input. The Wavegen instrument would be used to configure and adjust AWG 1 as a DC source.

An all in one software control interface, written in Python, is also available. The program is compatible with Python 2.6 ( and higher ) and does not require any add-on software packages beyond the standard install. The program was developed using the Digilent software interface DLL installed with the Waveforms program version 2.5.4.

Running the program:
~~~~~~~~~~~~~~~~~~~~

After plugging all the hardware together insure that the left two DIP switches are down connecting the Mux outputs to the scope channels and the right six DIP switches are all up (off). Insure that the potentiometer is roughly centered and that a shorting jumper is installed in W1. The program is not very smart about checking if an Analog Discovery is actually present or if there is more than one. It simply opens the first one found by the system.

Start the program by double clicking on the program file, eps_analog_discovery_interface_adg.pyw. In addition to the program itself two other files are needed, adi_logo.gif and eps_cal_file.txt. The first is self-explanatory and the second contains a list of the offset and scale (gain) calibration factors for each measurement channel. An example calibration file is listed in the Appendix.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_user_g_f3.jpg
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 3, EPS Discovery interface program


After a few seconds to initialize the Discovery hardware the control screen shown in figure 3 should appear. The DC values for the 8 measurements are color coded and displayed in the upper left of the window. Two "strip chart" plots are displayed on the right side of the window. The top grid displays the five currents and the bottom grid displays the three voltages. When the "Start" button is clicked the program takes DC measurements approximately once per second and updates the display. Clicking on the "Stop" button pauses taking the measurements. When stopped the display is updated whenever one of the LED buttons or the slider is changed. The "Restart" button clears the plot grids. 150 samples are plotted on the grid which, at ~ 1 sample per second is about two and a half minutes of data. When the grid is full it is blanked and new plots are started from zero.

The slider programs the output voltage of AWG 1 and sets either the voltage on the motor or the main load bus voltage set point depending on the position of the FB feedback switch. The gain of 2 in the motor driver is taken into account in the program. There are six check buttons to turn on and off the LEDs. Checking the "Start Data Log" box starts saving samples to a file called eps_data_log.csv. The eight analog measurements along with the slider position and the state of the 6 LEDs is saved to the file. If the file already exists the new data is appended to the file. If not a new file is opened when the program is first started and written to. The "Close Device" button shuts down the Discovery module and exits the program.

Notes:
------

**Testing and Debug:**

The EPS board can be tested or debugged without a computer and being attached to the Discovery module. The LEDs can be tested with just the rechargeable battery connected. Turn on the right most six DIP switches one at a time and each LED should light up in turn. Disconnect the battery for the next test. The motor-generator can be checked with just the +9 V battery attached. With the speed control potentiometer, R30, set to its minimum turned all the way counter-clockwise and switch FB set to mode 1, dot not showing, turn on the 9 V power with switch SWT. Note that with the Discovery disconnected shorting or not shorting W1 does not matter. The motor should not be turning. Slowly turn R30 clockwise until the motor begins to just start turning. The speed of the motor should smoothly increase as R30 is turned. A hand-held DVM can be used to monitor the voltage at the motor and at the generator as the speed is adjusted. Driving the LED loads from the output of the generator can also be tested at this point by turning on one or more of the LEDs with the DIP switches.

With just the solar panel connected and disconnecting the 9 V and rechargeable batteries, place the solar panel in bright sunlight and turn on one or more LEDs. The brightness of the LEDs should change as the amount of light falling on the panel increases and decreases. A hand-held DVM can be used to monitor the voltage at the output of the solar panel.

During any of these tests a hand-held DVM can be used to measure voltages around the board and also monitor the current in various paths by measuring the voltage drop across the shunt resistors at jumpers IL, LED load shunt, IGEN, generator shunt, ISP, solar panel shunt, and IBAT, rechargeable battery shunt.

**Appendix:**

Solar Panel Simulator.

To test and use solar panels full sun light is needed. However, it is not always convenient to setup lab experiments when and where access to full sun light is possible. A workable solution would be to construct a solar panel hardware simulation. We can model the photovoltaic solar cell as shown in figure A1.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_user_g_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A1, Model of solar cell


We can construct an equivalent circuit using a collection of transistors and resistors, including a photo resistor for modulating the current level based on the intensity of the ambient light. One possible configuration is shown in figure A2.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_user_g_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A2, Solar Panel simulator schematic


Diodes D\ :sub:`2`-D\ :sub:`9` model a panel with 8 cells connected in series and determines the open circuit voltage, V\ :sub:`OS`. Power to generate the current comes from an external 9 V battery ( or similar DC voltage source ). PNP power transistor Q\ :sub:`5`\ supplies the simulated photo current. Potentiometer, R\ :sub:`3`, sets the level of the maximum output, short circuit current or I\ :sub:`SC`. The intrinsic collector resistance of PNP transistor Q\ :sub:`5`, R\ :sub:`C`, along with the reverse bias leakage of diodes D\ :sub:`2`-D\ :sub:`9` sets an upper limit on the modeled shunt resistance, R\ :sub:`SH`. R\ :sub:`SH` could be reduced further by adding a resistor across SP+ and SP-. The series resistance, R\ :sub:`S`, can be modeled by inserting a low value resistor in series with either SP+ or SP-.

**An example EPS board calibration file:**

Actual values for your EPS board could be substantially different than those listed in the example.

| ImainOffset = 0.5 # offset is in mA
| VmainOffset = 0.0 # offset is in Volts
| IgenOffset = 1.42 # offset is in mA
| VgenOffset = 0.0 # offset is in Volts
| IsolarOffset = -0.5 # offset is in mA
| IbatOffset = 1.67 # offset is in mA
| VsolarOffset = 0.0 # offset is in Volts
| ImotorOffset = 0.2 # offset is in mA
| ImainScale = 99.8 # nominal current scale factor is 100
| VmainScale = 2.029 # nominal voltage scale factor is 2
| IgenScale = 100.1
| VgenScale = 2.033
| IsolarScale = 100.2
| IbatScale = 99.5
| VsolarScale = 2.022
| ImotorScale = 99.7

It is best to start with a file that sets all the offsets to 0, all the current scale factors to 100 and all the voltage scale factors to 2. Then observe the errors and adjust the values accordingly. The current measurement offset error for Imain, Igen, Isolar and Ibat can be observed by inserting shorting jumpers on IL, IGEN, ISP and IBAT respectively. A DVM can be used to measure the actual voltage values to determine scale factor calibration factors.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_user_g_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   EPS board silkscreen layer


**Return to EPS Activity** :doc:`Table of Contents </wiki-migration/university/courses/eps/main-page>`\ **.**
