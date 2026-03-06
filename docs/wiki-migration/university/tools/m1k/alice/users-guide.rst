Active Learning Interface (for) Circuits (and) Electronics:
===========================================================

**This software uses an older version of libsmu / pysmu and is no longer recommended for use.**

:doc:`ALICE Desktop 1.1 </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` is now recommended.

Objective:
----------

This document serves as a User's Guide for the ALICE software interface written for use with the ADALM1000 active learning kit hardware.

Background:
-----------

Although the word ALICE can be spelled out from the title of this users guide, it is actually an allusion to the fantasy works of Lewis Carroll: 1865's Alice's Adventures in Wonderland and its 1871 sequel Through the Looking-Glass, and What Alice Found There. In these stories Alice explores a strange and wondrous world down a rabbit hole and on the other side of a mirror ( looking glass ). Hopefully, through the use of this software along with the ADALM1000 active learning kit hardware, Students can explore the strange and wondrous world of Circuits, Electronics and Electrical Engineering.

Required files:
---------------

The ALICE program is written in Python and requires that version 2.7.8 ( or higher ) of Python be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run ALICE:

Required external Python modules (site-packages for the correct Python version):

NUMPY

All OS:
~~~~~~~

| alice-1.0.py(w)
| `ALICE zip file <https://wiki.analog.com/_media/university/tools/alice-1.0.zip>`__

| The zip file also contains the :doc:`spectrum analyzer </wiki-migration/university/tools/m1k/alice/sa-users-guide>` version and the :doc:`analog input multiplexer </wiki-migration/university/tools/m1k/analog-mux>` version of the program, alice-mux-1.0.py(w), which is used in conjunction with the circuit outlined in this Blog:
| |Two Input Channels Not Enough for Ya|

Windows:
~~~~~~~~

`libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`__ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`__ (needs to be in Python27\\DLLs directory)

Use of the :doc:`Windows installer </wiki-migration/university/tools/m1k/alice/install>` is highly recommended.

Linux:
~~~~~~

`libpysmu.so <https://github.com/analogdevicesinc/libsmu>`__

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`ADALM1000 Digital Outputs </wiki-migration/university/tools/m1k/digital-outputs>`

First a few notes on nomenclature used in this document:

| CA-V refers to the Channel A voltage signal
| CA-I refers to the Channel A current signal
| CB-V refers to the Channel B voltage signal
| CB-I refers to the Channel B current signal

Screen Setup:
-------------

Once the program is running the main screen, as shown in figure 1, should appear. It is sub divided into 4 sections. Be sure that the ALM1000 is plugged into the USB port before starting the program. If there is no ALM1000 present the green Conn button will be red and say Recon. Click this button after plugging in your ALM1000 to connect to the board.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_f1.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 1 ALICE main screen


The menu section along the top, shown in figure 2, contains various buttons and drop-down menus that control Triggering, Horizontal time base, Horizontal position, how and what signals are displayed, and run acquisition / stop acquisition / exit program.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_f2.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 2 Top menu buttons


The Trigger button is a drop down menu listing which signal to trigger on, CA-V, CA-I, CB-V, CB-I or none. There is a toggle selector for Auto Level triggering where the trigger level is automatically set to the mid point of the channel waveform each sweep. There is a toggle selector for single shot manual triggering. When in single shot mode clicking the Run button acquires a single time sweep. The Edge button is a drop down menu listing either the rising or falling edge for triggering. The Trigger Level entry window contains the trigger level in volts for CA-V and CB-V or mA for CA-I and CB-I. The 50% button sets the trigger level to the midpoint (50% point) of the selected trigger waveform. i.e. to the (maximum + minimum)/2.

The Hold Off entry window, in mS, is used to shift the horizontal position ( apparent time 0 trigger point within the acquired sample point buffer) of the display. The data used for the vertical and horizontal waveform calculations is also shifted by that amount. The Hoz Poss entry window is used to change the horizontal posistion of the time trace. Normally, with the Hoz Poss set to 0 the left edge of the grid is "time 0". Setting Hoz Poss to something else shifts the 0 time point on the grid by that amount ( in mSec ).

The Time mS/Div spinbox entry window is used to set the horizontal time base in the standard 1, 2, 5 step increments. Other values may be entered manually.

The Display drop down menu allows selection of either time or X vs Y display mode. It also allows selection of which of the four possible channel signals to plot on the X and Y axis. Given four possible signals, Channel A voltage and current, Channel B voltage and current, there are in theory 16 possible combinations for X and Y. Not all 16 have been implemented since, for example, plotting a signal vs itself such as CA-V vs CA-V is a rather meaningless straight line.

It is also possible to plot select Math on one or the other or both axis. If Math is selected for just one axis then the selected trace from the Math drop down menu is used. Only a few of the built-in Math traces are supported. If Math is selected for both axis then the entered X formula and Y formula, using the Enter X or Y Formula buttons, will be plotted. This allows greater flexibility in X-Y plotting at the expense of the typing in the function to be plotted. See Appendix A on how to enter formulas. Any one of the four vertical axis controls can be chosen for the X and Y axis using the Math X or Y Axis buttons. Generally when X-Y plotting using Math one or the other of the four channels are not being displayed and its axis controls will be available to be used.

There is also a check button to display the saved X-Y reference trace (see note below on Snap-Shot option).

The Curves button allows the selection of which signal waveforms will be displayed when plotting vs time. The All button selects all four curves to be displayed and the None button clears all four curves. The None button is handy to turn off all the time curves when switching to the X-Y mode. It is also possible to select which of the possible stored reference time traces, if saved via the Snap-Shot option, will be displayed.

The green PWR-On button toggles on and off the fixed analog +2.5 V and +5 V power supplies. The button turns red when the supplies are off. The power supplies do not turn completely off but go to around +2 V and can supply only about 20 mA when shorted to ground. This is much less than the 200 mA or so they could supply if accidentally shorted when on. It is good practice to turn off the supplies ( or better yet disconnect ) when making any modifications to the circuit under test.

The green Run button starts continuous looping acquiring input samples. The red Stop button stops the acquisition looping. The Exit button exits (kills) the program.

The Right Side Menu Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The section along the right hand side, shown in figure 3, mostly contains the controls for the two AWG generator outputs. In addition there are four drop down menus at the top.

The File drop down menu lists commands for saving and loading configuration settings (.cfg file). Also to save and load calibration settings (.cal files ). The calibration values are saved to a file with a unique name for your particular ALM1000 board based on the first 9 characters of the board device ID serial number. For example something like: 203131543_O.cal.

The Save Screen button saves the graphics display area to an encapsulated postscript file (.eps). The Save Data button saves the captured channel A and B voltage and current signal data to a coma separated values file (.csv). For most Time/Div settings the number of sample points is 2 screen widths with a minimum of 1,000 samples and a maximum of 50,000. This saved table of raw sample values can then be loaded into other programs for analysis such a spreadsheet program or math program like MATLAB, or Octave.

The Options drop down menu lists a command for enabling smoothing where spline curves are used to connect the input sample points rather than the default straight lines. A second option for connecting the sample points is to use a zero order hold function where a horizontal line and a vertical line are used. This looks like a stair step waveform much like the output of the Digital-to-Analog converters used to generate the output signals actually produce.

Waveform averaging is supported by selecting the Trace Avg selector under the Options drop down menu. The number of captured data sets used for the average can also be set with the Num Avg button. The default value is 8. The average is automatically reset whenever the horizontal time base is changed.

The Trace Width button allow the user to set the width of the trace lines in pixels. The default is 1.

The currently displayed traces will be saved via the Snap-Shot option as reference traces. They can be added to the graphics plot area by selecting the desired trace from the Curves drop down menu for time plots and the Display drop down for X-Y plots. They will be drawn in a darker color corresponding to the matching main waveform trace.

The Measure drop down menus, CA and CB list which vertical and horizontal measurements for the Channel A and B voltage and current traces are to be displayed along the bottom of the graphics display area. The displayed vertical measurements for both voltage and current can be the following:

-   Average, which is the sample by sample sum of the data record divided by the number of samples. For most Time/Div settings the number of samples is 2 screen widths.
-  Minimum, which is the minimum value within the data record.
-  Maximum, which is the maximum value within the data record.
-  Midpoint, which is the maximum value plus the minimum value divided by two.
-  Peak-to-Peak, which is the maximum value minus the minimum value.
-  RMS, which is the square root of the sum of the sample by sample data record squared divided by the number of samples.

The displayed horizontal measurements for the voltage traces can be the following:

-  High pulse width ( time waveform is above the mid-value
-  Low pulse width ( time waveform is below the mid-value
-  Duty Cycle ( percent of time waveform is High )
-  Period ( time between 2 rising edges )
-  Frequency ( 1 / period )

The Math drop down menu lists which sample point by sample point calculated waveform combining the Channel A and B voltage and current signals is to be displayed: One of the following calculated waveforms can be displayed at a time:

-   CA-V + CB-V, the sum of the channel A and B voltage waveforms
-   CA-V - CB-V, the difference of the channel A and B voltage waveforms
-   CB-V - CA-V, the difference of the channel B and A voltage waveforms
-   CA-I - CB-I, the difference of the channel A and B current waveforms
-   CB-I - CA-I, the difference of the channel B and A current waveforms
-   CA-V \* CA-I, the product of the channel A voltage and current waveforms which is instantaneous power
-   CB-V \* CB-I, the product of the channel B voltage and current waveforms which is instantaneous power
-   CA-V / CA-I, the ratio of the channel A voltage and current waveforms which is instantaneous resistance
-   CB-V / CB-I, the ratio of the channel B voltage and current waveforms which is instantaneous resistance
-   CB-V / CA-V, the ratio of the channel B voltage and channels A voltage waveforms which is instantaneous voltage gain assuming CA-V is input and CB-V is output
-   CB-I / CA-I, the ratio of the channel B current and channel A current waveforms which is instantaneous current gain assuming CA-I is input and CB-I is output

The first three calculations result in voltages and share the corresponding left side voltage scale on the display grid. The two current differences result in a current and share the corresponding right side current scale on the display grid. The two product waveform calculations result in mW and share the corresponding right side scale on the display grid. The two voltage over current waveform calculations result in Ohms and share the corresponding right side scale on the display grid. These calculated waveforms can produce strange looking results for periodic waveforms driving non-resistive loads such as capacitors or inductors. The final two ratio calculations can be used to calculate voltage gain and current gain respectively and are dimensionless.

If Math is selected then the formula entered with the Formula button, will be plotted vs time. This allows greater flexibility in waveform plotting at the expense of the typing in the function to be plotted. See Appendix A on how to enter formulas. Any one of the four vertical axis controls can be chosen for the Math axis using the Math X Axis button. Generally when plotting using Math one or the other of the four channels are not being displayed and its axis controls will be available to be used.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_f3.png
   :align: center
   :width: 120px

.. container:: centeralign

   Figure 3 Right side menu buttons


There are two identical sets of controls for configuring the Channel A and B outputs. First there is a drop down menu for selecting the Mode. The SVMI option is for sourcing voltage / measure current. The SIMV option is for sourcing current / measure voltage. The Hi-Z option disables the generator output (High Impedance mode). The Split I/O option separates the generator output signal from the voltage measurement input. In the Rev D version of ALM1000 only the source current function operates when the output and input are on separate pins so the Split I/O option automatically puts the hardware into the source current configuration. To turn the sourced current into a voltage the output termination options can be used. The hardware includes two 50 Ohm resistors that can be connected to the generator output pin. One resistor is tied to ground and the other is tied to the 2.5 V power supply. The drop down menu provides three options Open, To GND, and To 2.5V.

The Shape drop down menu is used to select the shape of the output waveform. When DC is selected the constant value of the output voltage or current is set by the value in the Max entry window.

The Min and Max entry windows program the minimum and maximum values for the output waveform. When in the voltage mode the values are in Volts, when in current mode the values are in mAmps. If the value entered in the Min window is higher ( more positive ) than the value entered in the Max window the apparent phase of the output wave is inverted. While this is somewhat redundant for the Sine, Triangle and Square wave shapes, given the Phase control described later, it is useful for determining if the Sawtooth or Stairstep shapes are rising or falling ramps.

The Freq entry window programs the frequency of the waveform in Hertz. Given the 100KSPS maximum sample rate, the maximum allowed frequency is, by definition, 50 KHz but the practical upper limit is more like 20 KHz or less.

The Phase entry window programs the relative phase of the output waveform in degrees from 0 to 360. The % entry window only applies to the Square shape and programs the duty cycle in percent from 0% to 100%.

The current low level ALM1000 software only outputs signals as single shot bursts when the analog signals ( voltage and current ) are being sampled. The Sync AWG check box must be checked if you want to produce outputs in sync with the analog trace sweeps. If you are in Hi-Z mode for both CH A and CH B and are using the ALM as just a 2 input oscilloscope the box should not be checked.

The ALM hardware provides four 3.3V CMOS digital input / output pins. At this time only static hi low functionality is supported. A simple interface is provided here. Each pin on the digital connector is actually connected to two GPIO port pins on the Micro-controller through two different series resistors. Refer to this :doc:`document </wiki-migration/university/tools/m1k/digital-outputs>` which provides more details. The first digital control drop down menu controls port pins PA0-3. Each can be set to one of three states, 0, 1, or High-Z. The second digital control drop down menu controls port pins PA4-7 and again each can be set to one of three states, 0, 1, or High-Z. When both port pins for a given connector pin are set as High-Z that pin is considered a digital input. The state of the digital inputs is read each time the screen is up-dated and displayed above the upper right hand corner of the grid. A red square indicates an logic "0", a green square indicates a logic "1" and a yellow square indicates that pin is configured as an output.

At the bottom of this section, just above the ADI logo, are entry slots for both voltage and current, gain and offset calibration factors for each channel. Using the calibration procedure from the Voltmeter tool is the best way to get the voltage calibration factors. Refer to the Voltmeter User’s Guide for that procedure. Once you have the gain and offset numbers they can be entered here. Getting the current gain and offset factors requires a known resistance and is explained in the Ohmmeter User’s Guide. To save these calibration values to a file for future use, press the Save Cal button in the Files menu. To reload the saved calibration factors press the Load Cal button. The values are saved to a file with a unique name for this particular ALM1000 board based on the last 14 characters of the board device ID serial number. This program uses the same naming scheme as the Ohmmeter Tool, for example something like: 203131543_O.cal.

The correction factors can be used for any external resistor divider attenuator networks that might be added to the channel A and B inputs ( possibly used when in the high impedance or Split I/O modes ). For more on the use of input attenuators please refer to the following two documents:

| :doc:`M1K Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`M1K Breadboard Adapters </wiki-migration/university/tools/m1k/breadboard-adapter>`

The Bottom Menu Section
~~~~~~~~~~~~~~~~~~~~~~~

The menu section along the bottom, shown in figure 4, contains the range and position controls for the Channel A and B voltage and current waveform displays. The entry labels are color coded to match the waveform trace colors.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_f4.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 4 Bottom menu buttons


The V/Div and mA/Div spinboxs set the corresponding vertical ranges in the standard 1, 2, 5 step increments. Other values maybe entered manually. The position entry windows determine the vertical position of their scales with respect to the blue center line on the grid. That is to say the value entered corresponds to the number displayed next to the blue center line.

The Graphics Display Area
~~~~~~~~~~~~~~~~~~~~~~~~~

The graphics display area, show in figure 5, is where the various signal waveforms are plotted on a black background. It consists of a main 10 by 10 grid with the center vertical and horizontal grid lines drawn in dark blue. Each major grid is sub divided into 5 sub grids by the short tick marks along the blue center lines. The horizontal grid lines are labeled with color coded text to match the corresponding waveform trace with the voltage scales on the left and current scales on the right.

The red triangle, drawn on the left side in the example shown because the trigger input is set to CA-V indicates the current trigger point.

Above the main grid area is a line of text showing the device ID and Sample rate and if the acquisition loop is running, stopped or in single shot mode. Below the main grid are three lines of text which display various information about the displayed plots. The first line shows the current time per division setting and the horizontal position of the left most grid line with respect to 0 time i.e. the trigger point. It also displays horizontal measurements such as the period and frequency for channels A and B ( if it can find two rising edges ) when selected.

The second and third lines of text are for displaying vertical information related to Channel A and Channel B respectively. The selected V/Div is displayed along with any of the vertical measurements selected for that voltage channel. If a current waveform is being displayed the selected mA/Div is displayed along with any of the vertical measurements selected for that current channel.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_f5.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 5 Graphics display area


Customizing ALICE
-----------------

There are a number of variables that the user can use to customize the appearance of the user interface. These variables are located near the top of the Python program file. These two variables set the size of the graphics drawing area in screen pixels. The default values are sized to optimally fill a screen with 1024X600 resolution. The menu buttons surrounding the graphics area need this much space to be properly displayed on most screens so using sizes smaller than the default may result in mangled menus.

| GRW = 720 # Width of the grid
| GRH = 390 # Height of the grid

The colors that are used to draw the various parts of the screen can be modified.

| Color = "#rrggbb" rr=red gg=green bb=blue, Hexadecimal values 00 - ff
| COLORframes = "#000080" # 50% blue
| COLORcanvas = "#000000" # 100% black used for background color
| COLORgrid = "#808080" # 50% Gray used for grid lines
| COLORzeroline = "#0000ff" # 100% blue used for vertical and horizontal center grid lines
| COLORtrace1 = "#00ff00" # 100% green
| COLORtrace2 = "#ff8000" # 100% orange CH B voltage trace
| COLORtrace3 = "#00ffff" # 100% cyan CH A current trace
| COLORtrace4 = "#ffff00" # 100% yellow CH B current trace
| COLORtrace5 = "#ff00ff" # 100% magenta Math trace
| COLORtraceR1 = "#008000" # 50% green CH A voltage snapshot trace
| COLORtraceR2 = "#804000" # 50% orange CH B voltage snapshot trace
| COLORtraceR3 = "#008080" # 50% cyan CH A current snapshot trace
| COLORtraceR4 = "#808000" # 50% yellow CH B current snapshot trace
| COLORtraceR5 = "#800080" # 50% magenta Math snapshot trace
| COLORtext = "#ffffff" # 100% white used for Text display
| COLORtrigger = "#ff0000" # 100% red used for trigger point

Appendix A: Advanced Math Traces
--------------------------------

In addition to the pre-programed Math traces, ALICE provides a method of plotting user defined equations or formulas using the voltage and current waveform buffers for channels A and B. The formulas are written in conventional Python syntax which is basically the same as you would expect to write any math expression. Any of the Python math module functions can be used such as math.sqrt() or math.sin() etc. Any of the ALICE global variables can be used but below is a list of the most useful available variables and constants:

Waveform Buffers:

| VBuffA is the Channel A voltage sample array ( in volts )
| VBuffB is the Channel B voltage sample array ( in volts )
| IBuffA is the Channel A current sample array ( in amps, multiply by 1000 for mA )
| IBuffB is the Channel B current sample array ( in amps, multiply by 1000 for mA )
| VmemoryA is the Channel A voltage memory array used for Trace Averaging
| VmemoryB is the Channel B voltage memory array used for Trace Averaging
| ImemoryA is the Channel A current memory array used for Trace Averaging
| ImemoryB is the Channel B current memory array used for Trace Averaging

t is the time index ( 10 uSec per point )

SAMPLErate is the sampling rate, 100000 samples per Sec, or 10 uSec per sample

Vertical Position variables:

| CHAOffset is the value in the channel A voltage position entry window
| CHBOffset is the value in the channel B voltage position entry window
| CHAIOffset is the value in the channel A current position entry window
| CHBIOffset is the value in the channel B current position entry window

Waveform calculated measurements:

| DCV1 is the channel A Average voltage
| MinV1 is the channel A Minimum voltage
| MaxV1 is the channel A Maximum voltage
| DCV2 is the channel B Average voltage
| MinV2 is the channel B Minimum voltage
| MaxV2 is the channel B Maximum voltage
| DCI1is the channel A Average current in mA
| MinI1 is the channel A Minimum current in mA
| MaxI1 is the channel A Maximum current in mA
| DCI2 is the channel B Average current in mA
| MinI2 is the channel B Minimum current in mA
| MaxI2 is the channel B Maximum current in mA

As a simple example, to plot the difference between the channel A and B voltage waveforms the following formula would be used:

(VBuffA[int(t)] - VBuffB[int(t)] - CHAOffset)

As the program iterates over the time index t, the channel B voltage value is subtracted from the channel A voltage value and then offset on the screen by the channel A position variable. This replicates the built-in math trace CA-V – CB-V.

A more advanced example calculates the time derivative of the channel B voltage waveform, or slew rate, and scales it to V/mSec:

(VBuffB[int(t)] - VBuffB[int(t-1)] ) \* 100

Again as the program iterates over the time index t, the channel B voltage value at t-1 is subtracted from the channel B voltage value at t and then multiplied by 100. The 100 scales the time from the 10 uSec per time sample to 1 mSec. The screen shot in figure A1, shows the result for a 4 V p-p triangle wave at 1 KHz. Since we are not displaying the channel B current we can use its settings as the vertical axis for the math trace by setting the Math Axis to I-B. The triangle wave changes 4 V in 500 uS for a slew rate of + and – 8 V/mSec.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_a1.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure A1, Calculating the slew rate


A few words of caution, care must be taken when writing the formula to not cause a Python syntax error or other math exception such as divide by zero. If you make a mistake ALICE will stop and put up the math formula entry screen so you can find and correct your mistake.

Examples:
---------

To demonstrate some of the features of ALICE the following example circuit is offered. In figure E1 we see a simple NPN transistor ( 2N3904 ) in the common emitter configuration with a 100 KΩ resistor used to bias the base and a 1 KΩ resistor as the collector load. The collector load is supplied from the fixed +5 V power supply. We will use the ALICE software to plot I\ :sub:`B` vs V\ :sub:`BE`. We will also determine the value of CA-V corresponding to I\ :sub:`C` = 2 mA and then measure the input to output voltage gain around that operating point.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E1, NPN common emitter amplifier


To plot V\ :sub:`BE` and I\ :sub:`B` we first start out with the channel B input (CB-V) connected to the base of the transistor. As the formula in figure E1 states, I\ :sub:`B` can be calculated by taking the difference of CA-V and CB-V and dividing by the 100 KΩ resistor value. 100 KΩ is chosen to simplify the calculations so that the current is found by just moving the decimal point of the measured voltage ( i.e. 1 V = 10 uA ).

Set up ALICE as follows: Channel A, Mode set to SVMI, Shape set to Triangle, Min set to 0.0, Max set to 5.0, Freq set to 100. Channel B Mode set to Hi-Z. Be sure that the Sync AWG box is selected.

The time base should be set to 0.5 mSec/Div so that the rising half cycle from 0 to 5.0 volts will fill the grid. Under the Curves menu select CA-V and CB-V. Under the Math menu select CAV - CBV.

Press the green Run button. You should see something like figure E2.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e2.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E2, V\ :sub:`BE` and I\ :sub:`B` plot


The green CA-V trace is the 0 to 5 V ramp that is being applied to the 100 KΩ resistor. The orange CB-V trace is the voltage on the base of the transistor or V\ :sub:`BE`. The magenta CAV-CBV math trace is the voltage across the 100 KΩ resistor and represents I\ :sub:`B` as 10 uA/V.

Pause or Stop the program ( red Stop button )

To make an XY plot of I\ :sub:`B` vs V\ :sub:`BE`, under the Curves menu press none to turn off all the time traces. Under the Display menu press the X-Y button. Under the Display menu also press the CB-V button in the -X Axis- section and the Math button in the -Y Axis- section. Set the CB V Pos entry to 0.5 and the CB V/Div to 0.1.

Press the green Run button. You should see something like figure E3.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e3.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E3, I\ :sub:`B` vs V\ :sub:`BE`\


The base current is very small when V\ :sub:`BE` is less than 0.6 V so there is likely to be noise in that part of the trace. Remember that the vertical voltage scale ( 0.5 V/Div ) is divided by the 100 KΩ resistor so it is 5 uA per division.

To plot the collector current move the Channel B input to the collector of the transistor.

Now we need to go back to the time display mode so under the Display menu press the Time button and the none buttons in the -X Axis- section and in the -Y Axis- section. Now under the Curves menu again select the CA-V and CB-V traces. Under the Math menu select none for now. Also set the CB V Pos entry to back to 2.5 and the CB V/Div back to 0.5.

Press the green Run button. You should see something like figure E4.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e4.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E4, V\ :sub:`CE` plot


To turn the plot of V\ :sub:`CE` into I\ :sub:`C` we can use the gain and offset calibration equation for channel B to calculate the equation for I\ :sub:`C` in figure E1. The calibration equation is as follows:

:math:`V_dis = (V_raw - Offset ) \times Gain`

| Where:
| V\ :sub:`dis` is the calibrated value to be displayed
| V\ :sub:`raw` is the raw measured value
| Offset is the calibration value entered
| Gain is the calibration value entered

If we set the Offset equal to the actual value of the +5 V supply divided by the Gain calibration factor and change the sign of the Gain factor ( i.e. make it negative ) we have the formula for I\ :sub:`C` from figure E1. After changing the channel B offset and gain factors press the green Run button and you should see something like figure E5.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e5.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E5, I\ :sub:`C` plot


I\ :sub:`C` should be nearly zero where CA-V is less than 0.6 V. You may need to tweak the Offset factor to get I\ :sub:`C` to be exactly on the 0.0 grid line. An easy way to check this is to temporarily move the channel B input to the +5 V power supply. Now the difference between CB-V and the supply is exactly zero.

Remember that the vertical voltage scale ( 0.5 V/Div ) is divided by the 1 KΩ resistor so it is 0.5 mA per division. With the program paused, under the Options menu press the SnapShot button. This saves a copy of the displayed CA-V and CB-V traces. Under the Curves menus select RB-V. This will now display the saved I\ :sub:`C` plot.

Now move the channel B input back to the base of the transistor. Under the Math menu select the CAV-CBV math trace. Reset the Channel B Offset and Gain calibration factors to their normal values.

Press the green Run button. You should see something like figure E6.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e6.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E6, I\ :sub:`C`, I\ :sub:`B` and V\ :sub:`BE` plot


Now we have plots of I\ :sub:`C` ( dark orange ), I\ :sub:`B` ( magenta ) and V\ :sub:`BE` ( orange ) on the same grid as the base resistor bias CA-V is swept from 0 to 5 V ( green ).

With the program paused click the left mouse button while hovering over the I\ :sub:`C` trace ( dark orange ) where it crosses 2 V ( 2 mA ). A marker should appear on the screen. Click again at the exact same horizontal time point on the CA-V trace (green). A second marker should appear. In the upper left of the grid the time and voltage values for the two marker points should be displayed as we see in figure E7.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e7.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E7, markers added.


The beta of the transistor can also be calculated by adding a marker to get the value of the base current (magenta trace) at the same horizontal point where I\ :sub:`C` is 2 mA. Beta will be I\ :sub:`C` / I\ :sub:`B`. For this example I\ :sub:`B` is about 13 uA so beta will be around 154.

The CA-V value for the second marker should correspond to the bias point where I\ :sub:`C` is equal to 2 mA where we would like to center our input signal for the next measurement of the amplifier gain.

Move the channel B input back to the collector of the transistor.

Calculate new Min and Max values for Channel A by adding and subtracting 0.25 V to the 2 mA bias point we just measured. Enter these for Channel A. Set Channel A Shape to sine wave. Under the Curves menu turn off the RB-V trace and under the Math menu select none. Set the time base to 2.0 mS/Div so that two cycles of the input waveform are displayed. Under the Meas CA and CB menus in the -CA V- and -CB V- sections select Avg and P-P to be displayed.

Press the green Run button. You should see something like figure E8.

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_e8.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure E8, Amplifier input / output gain


The DC average of the output waveform should be at about 2 V below ( 2 mA in the collector load resistor ) the +5 V power supply or +3 V. The voltage gain of the amplifier will be the Channel B P-P value divided by the Channel A P-P value. Which for this example is about 1.5.

For Further Reading:

Return to :doc:`Table of Contents </wiki-migration/university/tools/m1k>`.

.. |Two Input Channels Not Enough for Ya| image:: https://wiki.analog.com/_media/:ez:`community/university-program/blog/2015/07/07/two-input-channels-not-enough-for-ya`
