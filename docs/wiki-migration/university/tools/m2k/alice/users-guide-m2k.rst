Active Learning Interface (for) Circuits (and) Electronics for M2K:
===================================================================

.. important::

   This page is no longer being maintained at the moment. You can find the source code for the Libm2k version at :git-alice:`GitHub <tree/M2K-Version-2.1>`.


Objective:
----------

This document serves as a User’s Guide for the ALICE Desktop software interface written for use with the ADALM2000 active learning kit hardware. If you are looking for ALICE for the ADALM1000 (M1K) :doc:`look here </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`.

Background:
-----------

Although the word ALICE can be spelled out from the title of this users guide, it is actually an allusion to the fantasy works of Lewis Carroll: 1865’s Alice’s Adventures in Wonderland and its 1871 sequel Through the Looking-Glass, and What Alice Found There. In these stories Alice explores a strange and wondrous world down a rabbit hole and on the other side of a mirror ( looking glass ).


|image1|

.. container:: centeralign

   Alice Meets the Caterpillar, John Tenniel illustration from Alice in Wonderland by Lewis Carroll


Hopefully, through the use of this software along with the ADALM2000 active learning module hardware, Students can explore the strange and wondrous world of Circuits, Electronics and Electrical Engineering.

Functions:
----------

The ALICE M2K Desktop software provides the following functions:

-  Two Channel Oscilloscope for time domain display and analysis of voltage and current waveforms.
-  Two Channel Arbitrary Waveform Generator (AWG) controls.
-  X-Y display for plotting captured voltage vs voltage and math data as well as voltage waveform histograms.
-  Two Channel Spectrum Analyzer for frequency domain display and analysis of voltage waveforms.
-  Bode plotter and network analyzer with built-in sweep generator.
-  Impedance Analyzer for analyzing complex RLC networks and as a RLC meter and Vector Voltmeter.
-  DC Ohmmeter, measures unknown resistance with respect to known external resistor.
-  Board Self-Calibration

Required files:
---------------

The ALICE 2.0 Desktop program for the ALM2000 is written in Python and if run from the source code requires version 2.7.8 or greater of Python be installed on the user’s computer. The program only imports modules generally included with standard Python installation packages.

Windows:
~~~~~~~~

Windows users who do not wish to install Python and the other required software packages can install and use the standalone executable by:

.. admonition:: Download
   :class: download

   First, download Windows USB drivers installer for M2K here:

   
   -  Latest


   
   |plutosdr-m2k-drivers-win|

   You should download and install the Windows USB drivers from GitHub first if not already installed on your system.


.. admonition:: Download
   :class: download

   Second. download and install, libiio-setup.exe from the :git-libiio>`__. If you have done any LibIIO development in the past you may have this already installed but the ALICE M2K Windows executable was developed using the 32 bit (x86) library and this version will need to be installed. The libiio library depends on the Visual C++ Redistributable Packages for Visual Studio 2013, generally the installer should include the needed support files but if you should encounter any difficulties when running ALICE for M2K you may need to manually install the 32 (x86) package from the |Microsoft Web Site|.


.. admonition:: Download
   :class: download

   Download Windows installer here:

   
   -  Version 2.0 `Windows executable release <https::`libiio page on GitHub </github.com/analogdevicesinc/alice/releases/download/2.0.0/alice-desktop-2.0-setup.exe>`
   
   The installer should include all required packages but not the USB device drivers for the ADALM2000. If you encounter any issues, did you remember to first install the USB drivers and the libiio library from the GitHub web pages?


Run the alice-desktop-2.0-setup.exe installer program. ALICE M2K desktop opens and saves info and data to various files in the installation directory. Because of user permission issues with some installations of Windows you may need to install the software in a directory other than the default “Program Files”. C:\\ALM Software\\M2K would be a good second choice. If you also have ALICE for the ALM1000 installed be sure to install ALICE for the ALM2000 in a different directory because they use similar file names to save info and would likely conflict with each other. The installer adds desktop icons for each tool in the suite. Alternatively, under the properties for the icons, you can change the directory the program(s) start in.

Or run ALICE Desktop from the Python 2.7 compatible source code with the following packages installed:

| Python 2.7.11 (or higher, 32 bit version recommended)
| numpy numerical package extension
| libiio and iio.py

Linux and OSX:
~~~~~~~~~~~~~~

Most releases of the Linux operating system have Python included and many also include the numpy numerical package as well. Linux ( including Raspberry Pi ) and OSX users must manually compile libiio library. Direction on how to manually install Numpy can be found |here|.

Manually installing libiio and ALICE Desktop Python source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   The latest release of the ALICE 2.0 desktop tool set Python source files is available for download:

   
   Version 2.0 :git-alice:`Python Source Archive <releases/download/2.0.0/alice-2.0-m2k.zip>`.
   


To manually install on Windows download, libiio-setup.exe from the :git-libiio>`__. The USB drivers will also need to be installed by downloading the |plutosdr-m2k-drivers-win| from GitHub. For OS X and Linux users there are installer versions of libiio for popular distributions of the OS in `GitHub <https::`libiio page on GitHub </github.com/analogdevicesinc/libiio>`. The command(s) to manually build things are shown on the GitHub page as well. You will also likely need the development version of python installed (``apt-get install python2.7-dev``).

Raspberry Pi users with Raspbian need to have the Jessie distribution installed which includes the most up to date versions of gcc ( 4.9.2 ) and libusb-1.0-0-dev (``apt-get install libusb-1.0-0-dev libudev-dev``). As with other Linux OS the command(s) to make things are shown in the GitHub Readme. You will also need the development version of python installed (``apt-get install python2.7-dev``). Cmake may also need to be installed if it has not been done already (``apt-get install cmake``).

Manually installing numpy Python extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Linux users, numpy might already be part of your Python 2.7 distribution. Otherwise you can download and install numpy through the software / package manager on your particular version of Linux.

For Windows users, there are Windows binary installers that can be downloaded from `SourceForge <https://sourceforge.net/projects/numpy/files/NumPy/1.10.2/>`__. The latest version may or may not have a Windows binary so you may need to look back one or two version releases to find a Windows binary. As of this writing the newest version with a binary is numpy-1.10.2-win32-superpack-python2.7.exe 2015-12-14. Be sure to download the version for Python 2.7! Note that the developers have only created a Windows binary for 32 bit Python 2.7. Users more familiar with building from source code can download the source archive and use the setup scripts to install ( build ) numpy for their 64 bit version of Python.

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM2000 hardware. For more on the ADALM2000 hardware please refer to the following documents:

| :doc:`ADALM2000 Overview </wiki-migration/university/tools/m2k>`
| ADALM2000 Hardware
| ADALM2000 Design Document
| ADALM2000 Analog Inputs
| Below for reference is the pinout for the ADALM2000 connector.

|image2| |image3|

The Windows executable installer, in addition to the main ALICE Desktop program, includes the following DC measurement tools:

-  volt-meter-tool-2.0.exe
-  ohm-meter-vdiv-2.0.exe
-  dc-meter-source-tool-2.0.exe
-  strip-chart-tool-2.0.exe

Main Window:
------------

Be sure that the ALM2000 board is plugged into a USB port before starting the program. The program performs an internal self calibration upon startup. Nothing should be attached to the Scope inputs or AWG outputs for the few seconds while the self calibration is running. Once the program is running the main window, as shown in figure 1, should appear. This is the main desktop window and serves as the Oscilloscope Tool Window as well as controls for opening the other display windows and certain common control functions. It is sub divided into 4 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/main-window-1.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 1, ALICE Desktop main window


Many of the drop down menus on the main oscilloscope screen and the screens for the other instruments include accelerator keys, indicated by [] around the accelerator keyboard character next to the menu item. Typing one of these characters while the mouse cursor is inside the graphics drawing area will invoke that menu function. For example typing 1 or 2 will toggle on and off the CH1 and CH2 traces.

The Right Side Menu Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Green Conn button in the top row indicates that a ALM2000 board is connected and ready to go. If the button is red and says Recon then a ALM2000 board was not found. Connect board and click on the button to connect to board.

The File drop down menu lists commands for saving and loading configuration settings (.cfg file). Save config does not save waveform data. Only the values of the various controls and settings etc. Which windows are open and where they are placed on the computer screen is also saved. When you Exit ALICE the program saves the configuration in a file named "alice-last-config.cfg". When ALICE is restarted this configuration is reloaded so the program will be set up as it was when last exited. ALICE also has a feature to read an init file that can set the sizes of the graphics display areas and the trace colors etc upon start-up ( see the section at the end of this document on configuring ALICE for more details ).

On most operating systems there is a way to capture a bit map graphic of any of the display windows at any time. Some are built in or done through a support program or application. In Windows:

Press the <alt> and <printscreen> keys to capture the currently selected window in the copy buffer (clip-board). Then start a program such as Word or Paint (any similar program). Use Paste to place the screen shot into your document or drawing etc. Then save that file to disk.

It is possible to save the graphics display area to an encapsulated postscript file (.eps). This is used to save a graphics file to be included in another program like a word processor to write a Lab report. It is also possible to save the captured channel 1 and 2 voltage signal data to a coma separated values file (.csv). For most Time/Div settings the number of sample points is 2 screen widths with a minimum of 2,000 samples and a maximum of 16,384. The sample rate and number of samples in the buffers changes based on the Time/Div setting. This saved table of raw sample values can then be loaded into other programs for analysis such as a spreadsheet program or numerical processing program like MATLAB, or Octave. Similarly, it is possible to load in trace data into the channel 1 and 2 voltage signal data buffers from a saved csv file. This only works when stopped. If the green Run button is pressed new data is captured over writing the data that was loaded from the file.

The Options drop down menu, figure 2, lists a command for enabling smoothing where spline curves are used to connect the input sample points rather than the default straight lines. A second option for connecting the sample points is to use a zero order hold function where a horizontal line and a vertical line are used. This looks like a stair step waveform much like the output of the Digital-to-Analog converters used to generate the AWG output signals actually produce.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/options-drop-down.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2, Options Drop Down Menu


The Trace Avg button turns on trace averaging. The number of sweeps to average can be set with the Num Avg button. The width of the traces in pixels can be set with the Trace Width button.

The currently displayed traces will be saved via the Snap-Shot option as reference traces. They can be added to the graphics plot area by selecting the desired trace from the Curves drop down menu for time plots. They will be drawn in a darker color corresponding to the matching live waveform trace.

The Graphics display area can be drawn with either a Black (default) or White background. Use these two buttons to select which is used. The last option buttons start the self calibration procedure, and allow the user to save or load the current calibration correction factors to a file. Nothing should be attached to the Scope inputs or AWG outputs for the few seconds while the self calibration is running. See later section for more details.

The C1 and C2 measure drop down menus, figure 3, list which vertical measurements for the Channel 1 and 2 voltage signals are to be displayed along the bottom of the graphics display area.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/meas-drop-down.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 3, Measurements Drop Down Menu (C1)


The displayed vertical measurements can be the following:

-  Average, which is the sample by sample sum of the data record divided by the number of samples. For most Time/Div settings the number of samples is 2 screen widths.
-  Minimum, which is the minimum value within the data record.
-  Maximum, which is the maximum value within the data record.
-  Base, used mainly for square waves it is the voltage level of the lower flat portion of the wave which may be different from the Min value due to undershoot.
-  Top, used mainly for square waves it is the voltage level of the upper flat portion of the wave which may be different from the Max value due to overshoot.
-  Midpoint, which is the maximum value plus the minimum value divided by two.
-  Peak-to-Peak, which is the maximum value minus the minimum value.
-  RMS, or True RMS which is the square root of the sum of the sample by sample data record squared divided by the number of samples.
-  C1-C2 and C2-C1 differences of the Average ( DC ) voltage values of the channels.
-  The true RMS value of the sample by sample difference of the channel 1 and channel 2 voltages (1-2 RMS)
-  Display User defined measurement.

The displayed horizontal measurements for the voltage traces can be the following:

-  High pulse width ( time waveform is above the mid-value )
-  Low pulse width ( time waveform is below the mid-value )
-  Duty Cycle ( percent of time waveform is High )
-  Period ( time between 2 rising edges where waveform crosses mid-value )
-  Frequency ( 1 / period )

Figure 3g shows examples of many of the possible waveform measurements. Six of the vertical measurements are derived directly from the waveform data array. These are Avg, Min, Max, Top, Base and RMS. The rest are calculated from these six. P-P is obviously Max – Min. Mid is (Max + Min / 2). C1-C2 is C1 Avg – C2 Avg.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/meas-examples.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 3g, Measurement examples


The User measurement option allows the user to calculate any other measurements based off these constants. When clicked on the user is prompted for a label to be used while displaying the value and a formula for calculating the value. Clicking on Cancel for either the label or formula turns off the display of the User measurement.

For example the overshoot can be calculated by the formula:

(MaxV1 –VATop)/(VATop-VABase)

A second example would be the gain of a circuit where channel 1 is considered the input and channel 2 is the output. The gain would be the ratio of the two P-P values:

(MaxV2-MinV2)/(MaxV1-MinV1)

A third example is to calculate the rms value of just the AC portion of a signal. The built-in True RMS calculation includes any DC offset component. To remove the DC portion and just display the rms value of the AC portion of Channel 1 you can use the following formula:

math.sqrt(SV1**2 - DCV1**2)

The Crest factor can be calculated which is the ratio of peak-to-RMS values. The crest factor for single frequency sine waves is 1.414 (1/0.707), but can be as high as five or more for random noise. The crest factor for the channel A waveform would be the ratio of the Max and RMS values:

MaxV1/SV1

Another common waveform calculation is the peak-to-average ratio or PAR.

MaxV1/DCV1

Two more examples are to calculate the Peak positive and negative slew rates. The Numpy ediff1d function takes the differences between consecutive elements of an array. We can use this to calculate the dv/dt or the time rate of change between samples. Each sample is 10 uSec apart so we get V/10uS or we can divide by 10 for V/uS or multiply by 100 for V/mS. We can then use the Numpy max or min function to find the positive ( maximum ) slew rate or the negative ( minimum ) Slew Rate using the following formulas:

| numpy.max(numpy.ediff1d(VBuffA))*100 or
| numpy.min(numpy.ediff1d(VBuffA))*100

We can extend this calculation to estimate the rise and fall times for square wave signals assuming a more or less constant ( peak ) slew rate between the 10% to 90% levels. If we divide 0.8 ( 80% ) times the peak-to-peak value of the waveform by the peak slew rate we get the rise or fall times.

| (MaxV1-MinV1)*0.8 / (numpy.max(numpy.ediff1d(VBuffA))*100) or
| (MaxV1-MinV1)*0.8 / (numpy.min(numpy.ediff1d(VBuffA))*100)

If the waveform has significant overshoot or undershoot you could alternatively use the VATop and VABase values rather than the Max and Min values.

**Waveform calculated Vertical measurement scalars:**

| DCV1 is the channel 1 Average voltage
| MinV1 is the channel 1 Minimum voltage
| MaxV1 is the channel 1 Maximum voltage
| VATop is the channel 1 Top voltage
| VABase is the channel 1 Base voltage
| SV1 is the channel 1 RMS voltage
| DCV2 is the channel 2 Average voltage
| MinV2 is the channel 2 Minimum voltage
| MaxV2 is the channel 2 Maximum voltage
| VBTop is the channel 2 Top voltage
| VBBase is the channel 2 Base voltage
| SV2 is the channel 2 RMS voltage

Waveform calculated Horizontal measurement constants:

| CHAHW is the channel 1 High Pulse Width
| CHALW is the channel 1 Low Pulse Width
| CHADCy is the channel 1 Duty Cycle
| CHAperiod is the channel 1 Period
| CHAfreq is the channel 1 Frequency
| CHABphase is the channel 1 to channel 2 relative phase angle
| CHBHW is the channel 2 High Pulse Width
| CHBLW is the channel 2 Low Pulse Width
| CHBDCy is the channel 2 Duty Cycle
| CHBperiod is the channel 2 Period
| CHBfreq is the channel 2 Frequency

The Math drop down menu, figure 4, lists which sample point by sample point calculated waveform combining the Channel A and B voltage and current signals is to be displayed vs time.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/math-drop-down.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Math Drop Down Menu


One of the following built-in calculated waveforms can be displayed at a time:

-   C1-V + C2-V, the sum of the channel 1 and 2 voltage waveforms
-   C1-V – C2-V, the difference of the channel 1 and 2 voltage waveforms
-   C2-V – C1-V, the difference of the channel 2 and 1 voltage waveforms
-   C2-V / C1-V, the ratio of the channel 2 voltage and channels 1 voltage waveforms which is instantaneous voltage gain assuming C1-V is input and C2-V is output

The first three calculations result in voltages and share the corresponding left side voltage scale on the display grid. The final ratio calculation can be used to calculate voltage gain and is dimensionless.

If Formula is selected then the mathematical formula entered with the Enter Formula button, will be plotted vs time. This allows greater flexibility in waveform plotting at the expense of typing in the function to be plotted. See section on Advanced Math Traces below on how to enter formulas. Any one of the four channel vertical axis controls can be chosen for the Formula axis using the Math Axis button. Generally when plotting using Formula, one or the other of the four channels are not being displayed and its axis controls will be available to be used.

The AWG control Window is opened by default when the program is started. Since all of the displays use the AWGs in some fashion, it is important that this window be available to all. If you dismiss ( minimize to the tool bar ) the AWG control window, clicking on the AWG Window button will bring back the window.

The X-Y Plots Window button opens the X vs Y display window.

The Spectrum Window button opens the Spectrum Analyzer display window.

The Bode Plot Window button opens the Bode Plot display window.

The Impedance Window button opens the Impedance Analyzer display window.

The DC Ohmmeter Window button opens the DC Ohmmmeter display window.

To update the display window for a particular tool ( when running ) the matching Time Plot, X-Y Plot, Freq Plot, Bode Plot and/or Impedance Plot enable check boxes must be selected. More than one display can be selected at a time but some combinations such as X-Y and Spectrum or X-Y and Impedance would not make much sense while Time and X-Y or Time and Spectrum might.

The external positive and negative User power supply values can be set here. The positive supply can be set to any value from 0.0 to 5.0 volts and the negative supply can be set from 0.0 to -5.0 volts. The supplies can be turned on and off as well. The background of the check boxes changes from red (Off) to green when the supply is turned On.

At the bottom of this section, just above the ADI logo, are entry windows which allow input gain and offset adjustments or corrections for any external resistor divider attenuator networks that might be added to the channel 1 and 2 inputs. Save and Load Adj buttons can be found under the File drop down menu. For more on the use of input attenuators please refer to the following two documents:

| M2K Analog Inputs
| M2K Breadboard Adapters

The Top Menu Section
~~~~~~~~~~~~~~~~~~~~

The menu section along the top contains various buttons and drop-down menus that control Oscilloscope Triggering, Horizontal time base, Horizontal position, how and what signals are displayed, and run acquisition looping / stop acquisition looping / exit program.

The Trigger button is a drop down menu listing which signal to trigger on, C1-V, C2-V or none. The use of Triggering to display a stable trace is generally necessary when viewing signals.

The Auto Level option automatically sets the trigger level to the selected waveform midpoint on each sweep. The trigger point will thus track any changes in the input waveform. The Single shot option allows a single sweep to be captured each time the Run button is clicked.

The Edge button is a drop down menu listing either the rising or falling edge for triggering. The Trigger Level entry window contains the trigger level in volts for C1-V and C2-V. The 50% button sets the trigger level to the midpoint (50% point) of the selected trigger waveform. i.e. to the (maximum + minimum)/2.

The Hold Off entry window, in mS, is used to shift the horizontal position ( apparent time 0 start point ) within the acquired sample point buffers being displayed. The data used for the vertical and horizontal waveform calculations is also shifted by that amount. The sample buffer is generally two screens long so setting the hold off time to more than one screen width is not recommended.

The Horz Pos entry window is used to change the horizontal position of the time trace. Normally, with the Horz Pos set to 0 the left edge of the grid is "time 0". Setting Horz Pos to something else shifts the 0 time point on the grid by that amount ( in mSec ). So if you set Horz Poss to a negative number for example you can see time before the trigger.

The Time mS/Div spinbox entry window is used to set the horizontal time base in the standard 1, 2, 5 step increments. Other values maybe entered manually.

The Curves button allows the selection of which signal waveforms will be displayed when plotting vs time. The All button selects both channel's curves to be displayed and the None button clears all curves. The loop Back option allows the used to display the signals at the two AWG outputs without needing to move the scope channel input connections. Internal switches disconnect the + input signal paths and redirect them to the AWG outputs and the - inputs are grounded. It is also possible to select which of the possible stored reference time traces, if saved via the Snap-Shot option, will be displayed. The time and voltage cursors are turned on and off here as well.

It is good practice to turn off the supplies ( or better yet disconnect them ) when making any modifications to the circuit under test.

The green Run button starts continuous looping acquiring input samples. The red Stop button stops or pauses the acquisition looping. The Stop button also serves as a sort of refresh button. If the Stop button is clicked when stopped the graphics display is redrawn using any new settings that might have changed but using the existing data buffers. The Exit button exits (kills) the program.

The Bottom Menu Section
~~~~~~~~~~~~~~~~~~~~~~~

The menu section along the bottom contains the range ( V/Div ) and position controls for the Channel 1 and 2 voltage waveform displays. The entry labels are color coded to match the waveform trace colors. The V/Div spinboxs set the corresponding vertical ranges in the standard 1, 2, 5 step increments. Other values maybe entered manually. The position entry windows determine the vertical position of their scales with respect to the blue center line on the grid. That is to say the value entered corresponds to the number displayed next to the blue center line.

The Graphics Display Area
~~~~~~~~~~~~~~~~~~~~~~~~~

The graphics display area, show in figure 5, is where the various signal waveforms are plotted on either a black or white background depending on which is selected under the Options drop down. It consists of a main 10 by 10 grid with the center vertical and horizontal grid lines drawn in dark blue. Each major grid is sub divided into 5 sub grids by the short tick marks along the blue center lines. The horizontal grid lines are labeled with color coded text to match the corresponding waveform trace with the voltage scales on the left and Math scales on the right.

The red triangle, drawn on the left side in the example shown because the trigger input is set to C1-V indicates the trigger level.

Above the main grid area is a line of text showing the device ID, Sample rate and buffer size and if the acquisition loop is running or stopped. Below the main grid are three lines of text which display various information about the displayed plots. The first line shows the current time per division setting and the horizontal position of the left most grid line with respect to 0 time i.e. the trigger point.

The second and third lines of text are for displaying information related to Channel 1 and Channel 2 respectively. The selected V/Div is displayed along with any of the vertical measurements selected for that voltage channel.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/graphics-area.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 5 Graphics display area


Grid Markers and Cursors
~~~~~~~~~~~~~~~~~~~~~~~~

While stopped (red Stop button clicked) if you left click anywhere within the display grid a numbered marker "x" point will appear at that position. In the upper left corner of the display grid the maker number along with the vertical ( voltage or current ) and horizontal ( time ) values will also appear. For marker points > 1 the vertical and horizontal delta to the previous point will also be displayed. Clicking the red Stop button again will clear the markers. Clicking on the green C1-V/Div, orange C2-V/Div buttons along the bottom of the main Time display window will select which vertical range / position axis will be used and the marker will be drawn in that color.

Under the Curves Drop down menu there are selectors for displaying the T cursor ( time ) and V cursor ( voltage ). When selected if you right click anywhere within the display grid either a vertical or horizontal cursor line, or both, will be drawn at that location. The vertical, horizontal, or both values for that point will be displayed. Scrolling with the mouse wheel will move the vertical line left–right when only the T cursor is selected and the horizontal line up-down when only the V cursor is selected. When both are selected the mouse wheel moves the vertical line left–right. With the Shift key pressed the mouse wheel will move the horizontal line up-down.

Advanced Math Traces
~~~~~~~~~~~~~~~~~~~~

In addition to the pre-programed Math traces, ALICE Desktop provides a method of plotting user defined equations or formulas using the voltage waveform buffers for channels 1 and 2. The formulas are written in conventional Python syntax which is basically the same as you would expect to write any math expression. Any of the Python math ( and numpy ) module functions can be used such as math.sqrt() or math.sin() etc. Any of the ALICE global variables can be used but below is a list of the most useful available variables and constants:

Waveform Buffers:

| VBuffA is the Channel 1 voltage sample array ( in volts )
| VBuffB is the Channel 2 voltage sample array ( in volts )
| VmemoryA is the Channel 1 voltage memory array used for Trace Averaging
| VmemoryB is the Channel 2 voltage memory array used for Trace Averaging
| AWGAwaveform is the AWG 1 waveform memory array
| AWGBwaveform is the AWG 2 waveform memory array
| t is the time index ( 10 uSec per point )
| SAMPLErate is the sampling rate, which can be 1KSPS, 10KSPS, 100KSPS, 1MSPS, 10MSPS or 100MSPS

Vertical Position variables:

| CHAOffset is the value in the channel 1 voltage position entry window
| CHBOffset is the value in the channel 2 voltage position entry window
| As a simple example, to plot the difference between the channel A and B voltage waveforms the following formula would be used:

(VBuffA[t] - VBuffB[t] - CHAOffset)

As the program iterates over the time index t, the channel 2 voltage value is subtracted from the channel 1 voltage value and then offset on the screen by the channel 1 position variable. This replicates the built-in math trace C1-V – C2-V.

A more advanced example calculates the time derivative of the channel 1 voltage waveform, or slew rate, and scales it to V/mSec:

(VBuffA[t] - VBuffA[t-1] ) \* 100

Assuming a 100KSPS sample rate.

Again as the program iterates over the time index t, the channel 1 voltage value at t-1 is subtracted from the channel 1 voltage value at t and then multiplied by 100. The 100 scales the time from the 10 uSec per time sample to 1 mSec. The screen shot in figure 6, shows the result for a 4 V p-p triangle wave at 1 KHz. The green triangle wave changes 4 V in 500 uS for a slew rate of + and – 8 V/mSec shown with the magenta Math trace.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/slew-rate-example.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 6, Calculating the slew rate


A few words of caution, care must be taken when writing the formula to not cause a Python syntax error or other math exception such as divide by zero. If you make a mistake ALICE will stop and put up the math formula entry window so you can find and correct your mistake.

AWG Controls Window:
--------------------

The AWG controls window is shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/awg-controls-window.png
   :align: center
   :width: 950px

.. container:: centeralign

   Figure 7 AWG Controls window


There are two identical sets of controls for configuring the Channel 1 and 2 outputs. First there is a drop down menu for selecting the Mode, figure 8. The Hi-Z option disables the generator output (High Impedance mode). The default at start-up is that both channels are in Hi-Z mode.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/awg-controls-modes.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 8, AWG Modes drop down menu


The Min and Max entry windows program the minimum and maximum values for the output waveform. If the value entered in the Min window is higher ( more positive ) than the value entered in the Max window the apparent phase of the output wave is inverted. While this is somewhat redundant for the Sine, Triangle and Square wave shapes, given the Phase control described later, it is useful for determining if the Sawtooth or Stairstep shapes are rising or falling ramps.

The Freq entry window programs the frequency of the waveform in Hertz. Given the 75MSPS maximum AWG sample rate of the ALM2000, the maximum possible frequency is, by definition, 37.5 MHz but the practical upper limit is more like 25 MHz or less.

The Shape drop down menu is used to select the shape of the output waveform. There are 6 built in waveform shapes, DC, Sine, Triangle, Sawtooth, Square, and a Stair Step. The number of steps can be set using the % entry slot, which changes label to Steps when in the Stair Step wave shape. When DC is selected the constant value of the output voltage is set by the value in the Max entry window.

The relative timing between the two AWG channels can be set as either a phase angle or delay in time. The Phase and Delay buttons choose between the two methods. The entry window programs either the phase of the output waveform in degrees from 0 to 360 or the time delay in mSec. The % entry window applies to the Square, Trapazoid, SSQ and Up-Down Ramp shapes and programs the duty cycle or symetry in percent from 0% to 100%. For the Stairstep shape it set the number of steps.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/awg-controls-shapes.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 9, AWG Shapes drop down menu


Wave Shapes in the menu use the AWGAwaveform or AWGBwaveform array buffers to contain the waveform sample data points. A new data set based on the entered values is generated each time a shape button is clicked or a value is changed. The Impulse, Trapezoid, U-D Ramp, UU Noise ( uncorrelated uniform distribution ) and UG Noise (uncorrelated gaussian distribution ) buttons are used to build waveform arrays based on user input parameters.

The basic shape of the Impulse waveform is shown in figure 10. The Max, Min, Freq, Phase and Duty-Cycle values are used to construct the waveform. The Freq setting determines the Period ( 1/Freq ) or spacing between the pulses. The output starts and ends at a value midway between the Min and Max values. The impulse consists of a positive peak followed by a negative peak. The width of the peaks are equal to (Period \* DutyCycle)/ 2. The center of the pulse is delayed by the Phase setting. For example if the phase is set to 180 then the pulse is delayed by ½ the Period (Phase/360).

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impulse-waveform.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 10, Impulse waveform


The Trapezoid waveform makes a pulse with a rise and fall time set by the number of mSec entered in the delay entry slot. The Min, Max, Freq, and Duty-cycle entries operate as in the Square Shape.

The U-D Ramp ( ramp up ramp down ) shape is much like the triangle shape except that the Duty-cycle entry sets the symmetry of the up and down ramps. For example if the Duty-cycle is set to 25% the wave will ramp up from Min to Max for 25% of the Period ( 1/Freq ) and then ramp down from Max to Min for 75% of the period.

The Fourier Series shape builds a waveform based on the Fourier series of cosines for a square wave. The number of odd harmonics of the fundamental is entered in the % entry slot, which changes label to Harmonics when in the Fourier wave shape. The minimum and maximum values of the fundamental are set using the Min and Max entries and the fundamental frequency is set using the Freq entry. Entering 1 for the number of harmonics will result in just the cosine wave at the fundamental frequency. Entering 3 for the number of harmonics will include the third harmonic, entering 5 for the number of harmonics will include the third and fifth harmonics and so forth. More information on this can be found in the Advanced Users Guide.

There are two Noise like waveforms that can be generated. A new data set is generated each time the button is clicked. That fixed data pattern is then send to the output each time sweep. UU Noise or uncorrelated uniform distribution is made using a random number with a uniform distribution between the Min and Max settings. The average value of the noise should be equal to Max+Min/2. UG Noise or uncorrelated Gaussian distribution is made using a random number with a Gaussian distribution centered on Max+Min/2 with a sigma of (Max-Min)/3.

Waveform data point values can be read in from a simple single column csv text file ( one row per time sample ) by clicking on the Read File button. For voltage waveforms the values can be decimal numbers ranging from -5 to +5 in volts. If the .csv file contains more than one column the user will be prompted to choose which column number to import. The user is also prompted to select a sample rate. The contents of the Min, Max, Freq, Phase and % entry slots are not used for wave shapes input from a file. Use the Custom Math Waveforms feature below to change the amplitude and offset of the waveform. The contents of the AWG 1 or AWG 2 waveform arrays can be saved to a csv file by clicking on the Save File button.

Waveform data point values can also be read in from an audio file in .wav format, 16 bit data. The sample rate is can be selected form the possible AWG sample rates. Mono files can be read into either the AWG 1 or AWG 2 waveform buffers. To read a stereo file use the Read WAV File button for AWG 1. The Left channel will be loaded into AWG 1 and the Right channel will be loaded into AWG 2. The 16 bit integer data is scaled and offset to fit within the -5 to +5 V range of the ALM2000. Up to 100,000 sample points will be loaded. The open source audio program Audacity is a good option for generating and editing wave files.

A small library of example waveform files can be downloaded `HERE <https://wiki.analog.com/_media/university/tools/m1k/alice/arb_waveform_library.zip>`__.

Custom Math Waveforms
~~~~~~~~~~~~~~~~~~~~~

In addition to the built-in AWG wave shapes, ALICE Desktop provides a method of generating user defined wave shapes from equations or formulas using the AWG waveform buffers for channels 1 and 2. The formulas are written in conventional Python syntax which is basically the same as you would expect to write any math expression. As with the Math plotting, any of the ALICE global variables can be used. Only difference is that the time increment variable (t) is not used. Care must be taken if the lengths of any arrays being used in the expression are of differing lengths. As a reminder the length of the waveform array(s) will be displayed below the % entry slot if the array for that AWG channel has been generated. The following example Python syntax allows setting the start and stop points to be used in the array:

AWGAwaveform[ start : stop ] where start and stop are integers.

For example to copy the CH 1 captured data from the VBuffA array to the AWGBwaveform array you would simply click on the Math option under the AWG 2 Shape menu and type VBuffA as the formula, as in figure 11.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/awg-math-win-1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 11, Enter AWG waveform formula


As a more complex example let’s say we want to add noise to a waveform that was read from a file. The first step is to read the data into the AWGAwaveform array. The waveform chosen for this example is 8000 samples long and is a full wave rectified sinewave that is 1 V p-p, from 0.0 V to 1.0V. Then generate a noise waveform in the AWGBwaveform array by setting the AWG 2 Min and Max values to the desired amplitude of the noise ( + and - 0.2 V in this example ) and the Freq ( 937.4 ) such that the period of the noise will be as long as the waveform in AWG 1 ( length = 8000 points ).

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/figure12-awg-ctrls.png
   :align: center
   :width: 250px

Click on either UU Noise or UG noise. Now click on the Math shape button in AWG 2 and enter the following formula:

AWGAwaveform + AWGBwaveform + 1.0

The resulting output wave shapes are shown in figure 12. The first screen shot is what the waveforms look like before they are summed and offset. The CH 1 trace in the second screen shot shows the shape as read in from the file and the CH 2 trace shows the calculated wave shape with the added noise and offset.

|image4| |image5|

.. container:: centeralign

   Figure 12, Math wave shape example


DC Example:
-----------

To demonstrate how to use the Oscilloscope Tool as a DC voltmeter consider the resistor voltage divider network, shown in figure E1. We wish to measure the voltages at the 4 nodes and the voltages across the 6 resistors. In the figure the nodes are numbered from N0 to N4 with N0 being the ground or common node that all the voltage measurements will be made with respect to. With the Oscilloscope Tool we can measure two node voltages at a time and the voltage difference between those two nodes. Open the Measurements Window and / or from the Meas C1 menu select from the –C1-V- section the Avg and C1-C2 check boxes. Likewise from the Meas C1 menu select from the –C1-V- section the Avg and C2-C1 check boxes.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/volt-meter-fige1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E1, Test resistor network, measuring nodes N1 and N2


We start with the network powered from the fixed +5 volt power supply at node N1 and the channel 1 input also connected to N1. The channel 2 input is connected to node N2. Click on the Run button and the N1, N2 node voltages will be displayed along with the difference between them as C1-C2 and C2-C1. We can now proceed around the network measuring pairs of nodes until we can fill out table 1 below. Figure E2 shows the voltmeter inputs connected to nodes N3 and N4. Any combination of two nodes can be measured and the voltage difference between the two nodes will be displayed.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/volt-meter-fige3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E2, Test resistor network, measuring nodes N3 and N4


==== =======
Node Voltage
==== =======
N0   0.00
N1   4.931
N2   3.958
N3   1.770
N4   0.779
==== =======

Table 1 Node voltages

From the measured node voltages ( to measure the difference voltages the scope + and - inputs can be placed on the two nodes of interest ) we can get the voltages across the 6 resistors shown in table 2.

======== ==============
Resistor Voltage
======== ==============
R1       N1 – N2 =0.972
R2       N2 – N0 =3.958
R3       N2 – N3 =2.188
R4       N3 – N4 =0.991
R5       N4 – N0 =0.779
R6       N2 – N4 =3.179
======== ==============

Table 2 Resistor voltages

From these voltages and the values of the resistors the currents through the resistors can be calculated.

The X-Y Plotting Tool:
----------------------

When the X-Y Plot Window button is clicked in the Main Window the X-Y display Window should appear, as shown in figure 13. It is sub divided into 3 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/x-y-plot-window.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 13, X-Y Plots window


The menu on the right allows selection of which of the four possible input channel waveform signals or Math formula is to be used for the X and Y axis. Given two possible signals, Channel 1 voltage Channel 2 voltage there are in theory 4 possible combinations for X and Y. Not all 4 have been implemented since, for example, plotting a signal vs itself such as C1-V vs C1-V is a rather meaningless straight line.

Under the -X Axis- heading there are two options to display the histogram of either the channel A voltage or the channel B voltage waveforms. The horizontal axis is in volts and controlled by either the CA or CB V/Div and V Pos controls. The vertical axis is the histogram count or number of hits at a given voltage level. The vertical axis scale is controlled by the MC1 or MC2 controls.

It is also possible to select Math on one or the other or both axis. If Math is selected for just one axis then the selected trace from the Math drop down menu is used. Only a few of the built-in Math traces are supported. If Math is selected for both axis then the entered X formula and Y formula, using the Enter X or Y Formula buttons, will be plotted. This allows greater flexibility in X-Y plotting at the expense of the typing in the function to be plotted. See the earlier section on how to enter Advanced Math Traces for the Oscilloscope display. The same applies here to the X and Y formulas.

Any one of the four vertical axis controls can be chosen for the X and Y axis using the Math X or Y Axis buttons. Generally when X-Y plotting using Math one or the other of the four channels are not being displayed and its axis controls will be available to be used.

The X-Cur and Y-Cur check boxes select vertical and horizontal cursor lines which operate much the same as the T and V cursors in the Time display grid.

There is also a check button to display the saved X-Y reference trace (see note above in Oscilloscope section on Snap-Shot option).

Oscilloscope and X-Y Plot Examples:
-----------------------------------

To demonstrate some of the features of the ALICE Oscilloscope and X-Y Plot Tools the following example circuit is offered. In figure E3 we see a simple NPN transistor ( 2N3904 ) in the common emitter configuration with a 100 KΩ resistor used to bias the base and a 1 KΩ resistor as the collector load. The collector load is supplied from the fixed +5 V power supply. We will use the ALICE software to plot I\ :sub:`B` vs V\ :sub:`BE`. Figure E3 also shows how we will connect the scope inputs to measure the V\ :sub:`CE` (voltage at the collector with respect to ground) and I\ :sub:`C` (voltage across the 1 KΩ resistor). We will also determine the value of the base drive signal, C1-V corresponding to I\ :sub:`C` = 2 mA and then measure the input to output voltage gain around that operating point.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/alice2_userguide_e3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E3, NPN common emitter amplifier


To plot V\ :sub:`BE` and I\ :sub:`B` we first start out with the channel 1 input (C1-V) connected across the 100 KΩ base resistor. As the formula in figure E3 states, I\ :sub:`B` can be calculated by taking the differential voltage C1-V and dividing by the 100 KΩ resistor value. 100 KΩ is chosen to simplify the calculations so that the current is found by just moving the decimal point of the measured voltage ( i.e. 1 V = 10 uA ). The V\ :sub:`BE` is measured with scope input for C2 connected to the base and the emitter (ground).

Set up the AWGs as follows: AWG 1, Mode set to Enab, Shape set to Triangle, Min set to 0.0, Max set to 5.0, Freq set to 100. AWG 2 is not being used so the Mode can be set to Hi-Z.

The time base should be set to 1.0 mSec/Div so that one full cycle from 0 to 5.0 volts will fill the grid. Set the Trigger level so the start of the cycle will be displayed. Under the Curves menu select C1-V and C2-V.

Press the green Run button. You should see something like figure E4.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-1.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E4, V\ :sub:`BE` and I\ :sub:`B` plot


The green C1-V trace is the voltage across the 100 KΩ resistor and represents I\ :sub:`B` as 10 uA/V. The orange C1-V trace is the voltage on the base of the transistor or V\ :sub:`BE`.

Pause or Stop the program ( red Stop button )

To make an XY plot of I\ :sub:`B` vs V\ :sub:`BE` open the X-Y Plot Window with the X-Y Plot Enab box checked. In the X-Y Display window press the C2-V button in the -X Axis- section and the C1-V button in the -Y Axis- section. In the X-Y Window set the C1 V Pos entry to 2.5 and the C1 V/Div to 0.5 and the C2 V Pos entry to 0.5 and the C2 V/Div to 0.1.

Press the green Run button. You should see something like figure E5.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E5, I\ :sub:`B` vs V\ :sub:`BE`\


The base current is very small when V\ :sub:`BE` is less than 0.6 V so there is likely to be noise in that part of the trace. Remember that the vertical voltage scale ( 0.5 V/Div ) is divided by the 100 KΩ resistor so it is 5 uA per division.

To plot the collector current I\ :sub:`C` move the Channel 2 + input to the +5V power supply and the channel 2 - input to the collector of the transistor. Now we need to go back to the time display window. Uncheck the X-Y Plot box and make sure the Time Plot box is checked.

Press the green Run button. You should see something like figure E6.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-3.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E6, I\ :sub:`C` plot


I\ :sub:`C` should be nearly zero where C1-V is less than 0.6 V. You may need to tweak the Offset factor to get I\ :sub:`C` to be exactly on the 0.0 grid line. An easy way to check this is to temporarily move the channel 2 - input to the +5 V power supply. Now the differential input to scope channel C2-V is exactly zero.

Remember that the vertical voltage scale ( 0.5 V/Div ) is divided by the 1 KΩ resistor so it is 0.5 mA per division. With the program paused, under the Options menu press the SnapShot button. This saves a copy of the displayed C1-V and C2-V traces. Under the Curves menus select R2-V. This will now display the saved I\ :sub:`C` plot.

To plot the V<sub>CE</sub >move the Channel 2 + input to the collector of the transistor and the channel 2 - input to ground. Press the green Run button. You should see something like figure E7.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-4.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E7, V\ :sub:`CE` plot


Now move the channel 2 + input back to the base of the transistor. Press the green Run button. You should see something like figure E8.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-5.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E8, I\ :sub:`C`, I\ :sub:`B` and V\ :sub:`BE` plot


Now we have plots of I\ :sub:`C` ( dark orange ), I\ :sub:`B` ( green ) and V\ :sub:`BE` ( orange ) on the same grid as the base resistor bias from AWG 1 is swept from 0 to 5 V.

Under the Curves Menu select the V cursor. Right click on the time grid where the dark orange I\ :sub:`C` trace crosses the 2 V grid ( or 2 mA ). The voltage value at that point will appear next to the horizontal cursor line. The Use the mouse wheel it adjust the cursor up or down so it lines up exactly where the I\ :sub:`C` curve cross the time grid line. It should look like figure E9.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-6.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E9, voltage cursor added.


The beta of the transistor can now be calculated by scrolling the cursor down till it lines up exactly where base current (magenta trace) at the same time grid line. The displayed voltage will represent the base current. Beta will be I\ :sub:`C` / I\ :sub:`B`. For this example I\ :sub:`B` is about 12 uA so beta will be around 166.

The AWG 1 value where the green trace crosses the same Time Grid as I\ :sub:`C` = 2 mA should correspond to the base bias point where I\ :sub:`C` is equal to 2 mA. This is the bias point we would like to center our input signal on for the next measurement of the amplifier gain.

Move the scope channel 1 + input back to the AWG 1 output, - input to ground and the scope channel 2 + input back to the collector of the transistor, - input to ground.

Calculate new Min and Max values for AWG 1 by adding and subtracting 0.25 V to the 2 mA bias point we just measured. Enter these for AWG 1. Set AWG 1 mode to sine wave. Under the Curves menu turn off the R2-V trace and under the Math menu select none. Set the time base to 2.0 mS/Div so that two cycles of the input waveform are displayed. Under the Meas C1 and C2 menus in the -C1 V- and -C2 V- sections select Avg and P-P to be displayed.

Press the green Run button. You should see something like figure E10.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ce-example-7.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E10, Amplifier input / output gain


The DC average of the output waveform should be at about 2 V ( 2 mA in the collector load resistor ) below the +5 V power supply or about +3 V. The voltage gain of the amplifier will be the Channel 2 P-P value divided by the Channel 1 P-P value. Which for this example is about 1.5.

The Spectrum Analyzer / Bode Plotter:
-------------------------------------

Window Setup:
~~~~~~~~~~~~~

When the Spectrum window button is clicked in the Main Window the Spectrum display Window should appear, as shown in figure 14. It is sub divided into 2 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/spectrum-window.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 14, ALICE Desktop spectrum analyzer window


The menu buttons:
~~~~~~~~~~~~~~~~~

The following sections cover the functions of the various menu buttons. All of the program controls can be found under the buttons, there are no scrollbars, or rotating knobs.

\**File drop down menu \*\*

Save Config Load Config, commands for saving and loading configuration settings (.cfg file).

Save Screen, command for saving the graphics display area to an encapsulated postscript file (.eps)

Save Data, command for saving the captured channel 1 and 2 amplitude vs frequency data to a coma separated values file (.csv). The amplitude data can be saved as magnitude in Vrms ( type a 0 ) or in dBV ( type a 1 ).

**Options drop down menu**

Smooth, an option to enabling smoothing where spline curves are used to connect the FFT frequency points rather than the default straight lines.

Cut-DC, an option that will remove the DC component from the sampled data record. It element by element subtracts the average value of the sample record.

Store trace, no explanation required, you can store a reference trace with it.

Button to select the number of vertical divisions on the grid. With the Zero Stuff button, you can input the desired Zero Stuffing factor (power of 2).

**Run, Stop**

Start and stop buttons for the sweep.

**Mode drop down menu**

In Normal mode the trace is continuously refreshed.

In Peak hold, the peak or maximum value for each frequency bin is remembered. For each sweep if the new value is higher, then that new data point of the trace is saved and displayed.

In Average mode, the trace values are averaged. This smooths out the randomness in the noise floor.

In Single Shot mode a single sweep is obtained each time the Run button is pressed.

**FFT window drop down menu**

Used to select an FFT window function. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Flat Top window gives the highest amplitude accuracy but also has a large bandwidth, so less selectivity.

**Samples +/- buttons**

Used to change the number of samples in the FFT calculation. This number has to be a power of 2. More samples provides higher frequency resolution but a slower update rate for the screen. Fewer samples provides a lower frequency resolution, but a faster update rate for the screen.

**Curves drop down menu**

The Curves button allows the selection of which signal waveforms will be displayed. The All button selects all four curves to be displayed and the None button clears all four curves. The Marker option turns on a text marker which displays the amplitude and frequency at the peak of the displayed signal. Options to display the difference ( subtraction ) of the C1-dBV – C2-dBV traces or the C2-dBV – C1-dBV traces. It is also possible to select which of the possible stored reference traces, if saved via the Store trace option, will be displayed. The color of the C1-dBV and C2-dBV traces will turn red if the input signal goes beyond the -2.9 to +2.9 V analog input signal range when in the high gain setting.

Under the Curves Drop down menu there are selectors for displaying the Frequency cursor and dB cursor (amplitude) or Phase cursor. When selected if you right click anywhere within the display grid either a vertical or horizontal cursor line, or both, will be drawn at that location. The vertical, horizontal, or both values for that point will be displayed. Scrolling with the mouse wheel will move the vertical line left–right when only the Frequency cursor is selected and the horizontal up-down when only the dB or phase cursor is selected. When both vertical and horizontal cursors are displayed the mouse wheel moves the vertical line left–right. Holding down the shift key will move the horizontal line.

**Startfreq and Stopfreq**

Used to set the start and stop frequency of the display. The stop frequency is used to set the ADC sample rate.

**Lin F and Log F selector**

Select linear or logarithmic horizontal frequency axis scale.

**Gain Selectors**

There are selectors for the Channel 1 and Channel 2 input gain ranges. In high gain mode the maximum input swing is form -2.9 to +2.9 volts. The traces will turn red if this range is exceeded. In low gain mode the inputs can swing +/- 30 Volts.

**dB/div +/- buttons**

Used to set the dB’s per division. Can be 1, 2, 3, 5, 10, 15, or 20 dB/Div.

**LVL +/- buttons**

Used to set the top line of the grid or reference level. Sometimes called the "sensitivity". 0 dB is equal to an input amplitude of 1 Vrms.

The Bode Plotter:
-----------------

.. _window-setup-1:

Window Setup:
~~~~~~~~~~~~~

When the Bode Plot window button is clicked in the Main Window the Bode Plot display Window should appear, as shown in figure 14B. It is sub divided into 2 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/bode-main-window.png
   :align: center

.. container:: centeralign

   Figure 14B, ALICE Desktop Bode plot window


**FFT window drop down menu**

Used to select an FFT window function. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Nuttall window function is set by default and is generally the best overall option. The Flat Top window gives the best amplitude accuracy but can have strange phase results at some frequency steps.

**Curves drop down menu**

The Curves button allows the selection of which signal waveforms will be displayed. The All button selects all four curves to be displayed and the None button clears all four curves. The Marker option turns on a text marker which displays the amplitude and frequency at the peak of the displayed signal. Options to display the difference ( subtraction ) of the C1-dBV – C2-dBV traces or the C2-dBV – C1-dBV traces. It is also possible to select which of the possible stored reference traces, if saved via the Store trace option, will be displayed.

The color of the C1-dBV and C2-dBV traces will turn red if the input signal goes beyond the -2.9 to +2.9 V analog input signal range when in the high gain setting.

Under the Curves Drop down menu there are selectors for displaying the Frequency cursor and dB cursor (amplitude) or Phase cursor. When selected if you right click anywhere within the display grid either a vertical or horizontal cursor line, or both, will be drawn at that location. The vertical, horizontal, or both values for that point will be displayed. Scrolling with the mouse wheel will move the vertical line left–right when only the Frequency cursor is selected and the horizontal up-down when only the dB or phase cursor is selected. When both vertical and horizontal cursors are displayed the mouse wheel moves the vertical line left–right. Holding down the shift key will move the horizontal line.

**Lin F and Log F selector**

Select linear or logarithmic horizontal frequency axis scale. This also determines how the frequency steps are spaced, linearly or logarithmically.

**Gain Selectors**

There are selectors for the Channel 1 and Channel 2 input gain ranges. In high gain mode the maximum input swing is form -2.9 to +2.9 volts. The traces will turn red if this range is exceeded. In low gain mode the inputs can swing +/- 30 Volts.

**dB/div +/- buttons**

Used to set the dB's per division. Can be 1, 2, 3, 5, 10, 15, or 20 dB/Div.

**LVL +/- buttons**

Used to set the top line of the grid or reference level. Sometimes called the “sensitivity”. 0 dB is equal to an input amplitude of 1 Vrms.

**Sweep Generator**

Under the Sweep Gen section are controls for generating frequency sweeps of the analog output sources. The screen is up-dated after each frequency step. First are radio buttons to select which AWG output channel, or none will be swept. When using the Bode plotter the selected AWG will be forced into SVMI mode with a Sine Shape. Use the AWG controls window to set the source amplitude. The other channel will be forced into Hi-Z mode. The selected output will be swept from the Start Frequency to the Stop Frequency. The number of steps can be set using the Sweep Steps entry.

The amplitude of the swept source is generally held constant across frequency but in some special cases it might be desirable to change the source amplitude at each frequency step. Checking the Sweep From File check box will prompt the user for a .csv file. The csv file should contain two columns of values one row for each frequency amplitude combination for the sweep. The first column should contain a monotonically increasing list of frequency steps in Hz. The second column should contain the corresponding amplitude value in dB. The Start, Stop and number of Steps will be filled in based on the contents of the file. After reading in the csv file the program will display the highest ( maximum ) amplitude value found and ask the user to input the desired maximum the values should be normalized to. This is done because the ADALM2000 has an upper limit to the range of output amplitudes ( around +4.5 dBV ) when in the high gain range. Also it might be useful to scale the amplitude values up or down to optimize the dynamic range of the swept signal.

Lastly, there is a radio button selector for single or continuous sweep. The frequency sweep is started, or restarted from the beginning each time the Run button is pressed.

Frequency Analysis:
-------------------

The ALICE Desktop program uses the Fast Fourier Transform (FFT) to produce the frequency spectrum of a set of time samples of the input signals. The FFT takes as an input a set of time samples at a given sample rate and produces a set of frequency samples or values from DC ( 0 Hz ) to one half of the sampling frequency. In the case of the ALM2000 the sample rate is can be 1 KHz, 10 KHz, 100 KHz, 1 MHz, 10 MHz or 100 MHz so the highest frequency will be one half of that or for example 50 KHz when the sampling frequency is 100 KHz. The number of individual frequency bins the FFT produces is one half the number of time samples that are used. So the width of the bins or frequency resolution will be 50 KHz divided by one half the number of time samples taken. The number of time samples can be set from 64 ( 2\ :sup:`6` ) to 65536 ( 2\ :sup:`16` ) in the program.

What is an FFT window function?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ALICE Desktop you can choose from a number of FFT window functions. But what is an FFT window and what is it doing? The principle is very simple. The program reads a number of samples from the ALM2000 and puts them in an array. The size of the array has to be a power of 2 for the FFT calculation, for example 2048. With no window weighting function, all samples have an equal contribution or weight in the FFT calculation. You should expect to have an optimal result, but that is not the case if there is not an exact number of repeating cycles in the array. Another way of thinking about this is the starting value of the time waveform must be the same as the ending value. The end of the waveform will line up with the beginning if wrapped around on itself. This will almost never be the case in actual practice.

An FFT windowing function weights the samples from the beginning of the array to the end. With higher weights at the center and weights closer to zero near the start and end. The samples at the beginning and at the end of the array, that probably don’t line up, hardly contribute to the FFT calculation. Why would we use a only part of the samples or even not at all? There are even FFT window functions in which some sample points counteract with the other sample points.

The reason why we need an FFT window can be seen figures 15-22 in the various spectrums using different FFT window functions. No FFT window (also called a Rectangular window), generates many side bands in the spectrum of the FFT calculation. That is very visible in the first spectrum plot of the Rectangular ( dark orange ) and Cosine ( light orange ) window functions. Very low amplitude signals close to the main signal cannot be measured. So the dynamic range around the large main signal is low. By using an FFT window, the side bands are much more attenuated, how much depends on the type of FFT window. The increased side band suppression is at the expense of the selectivity. FFT windows with a very high side band suppression and therefore a very high dynamic range, have much less selectivity.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-cosine.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 15, Rectangular vs cosine window function


A Cosine window is a good compromise between a good selectivity and a good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-triangle.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 16, Rectangular vs Triangle window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-hann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 17, Rectangular vs Hann window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-blackmann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 18, Rectangular vs Blackman window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-nuttall.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 19, Rectangular vs Nuttall window function


At the expense of a little wider bandwidth the Nuttall window function provides the best side band reduction and may be the optimal compromise between good selectivity and good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-flattop.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 20, Rectangular vs Flat Top window function


A special filter is the Flat Top filter. It has a flat top as the name implies. That is why it is very usable for accurate amplitude measurements. The peak of the signal does not have to be exactly on the center of an FFT frequency bin.

| ALICE Desktop has 7 built in windowing functions.
| Rectangular, no window function B=1
| Cosine window function, medium-dynamic range B=1.24
| Triangular non-zero endpoints, medium-dynamic range B=1.33
| Hann window function, medium-dynamic range B=1.5
| Blackman window, continuous first derivate function, medium-dynamic range B=1.73
| Nuttall window, continuous first derivate function, high-dynamic range B=2.02
| Flat top window, medium-dynamic range, extra wide bandwidth B=3.77

ALICE desktop also allows the user to enter a function, generally from the numpy library, for the FFT window. Under the FFTwindow drop down menu click on Enter User Function and type in the function. Then select User Defined Window. It is also possible to enter the FFT window shape as an array from a .csv file. The length of the window shape has to be a power of 2, i.e. 256, 512, 1024, 2048, 4096.... When using an FFT window shape from a file, changing the number of samples up or down is not permitted. The number of FFT samples will be set by the length of the shape file.

Zero Stuffing
~~~~~~~~~~~~~

With the menu button "Setup" you can set the factor for the Zero stuffing. What problem are trying to solve by Zero stuffing? The bandwidth of the FFT depends on the choice of the FFT window function. For a narrow FFT filter, the bandwidth is slightly larger than the difference between 2 FFT frequency bins. When the signal frequency is exactly between the 2 FFT frequency bins, the signal will be displayed lower than its actual value because half of the signal appears in each of the two bins. Figure 21 shows good example of this. The signal is slightly more than 1 KHz and lies exactly between the two FFT frequency bins. The actual peak value should be equal to 0 dB, but the displayed value of the two adjacent samples is lower. The signal level is not displayed correctly by either of the FFT frequency bins. This is called Scalloping loss.

.. image:: https://wiki.analog.com/_media/university/tools/no-zero-stuffing.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 21, Fundamental frequency not centered, no zero stuffing


Zero stuffing provides a simple solution to this problem. For 1x Zero Stuffing, we double the size of the time sample array. The original array was say 2048 samples. We add 2048 samples with the value zero and we get a new array with 4096 samples. This may seem counterintuitive, when we add zero’s we do not add extra measurement data. However, something happens in the FFT calculation with twice as many samples. The effect can be seen in figure 22. Extra FFT frequency bins have been added. Coincidentally, here the extra frequency bin coincides with the frequency of the signal and the level of the signal is displayed correctly. Also even if the signal frequency does not coincide with the frequency of the extra FFT bin, the measured error will be smaller. As we add samples with the value zero, the bandwidth of the FFT filter remains the same.

.. image:: https://wiki.analog.com/_media/university/tools/zero-stuffing-2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 22, Fundamental frequency not centered, with zero stuffing


In the program, you can choose a value between 0 and 5 for the Zero Stuffing. As it is a power of 2, it is a value between 1 and 32. So 0x - 31x points will be added. As a result, the FFT calculation time will be up to 32x longer as well and the spectrum analyzer screen update rate will slow down considerably. One extra point (a value of 1 for the Zero Stuffing) is often good enough to keep the Scalloping loss acceptable. As an alternative, what you can do is set Zero Stuffing to 0, and use a Flat top window. The flat top is so wide, that even without Zero Stuffing, you will have little Scalloping loss, but you will have less frequency selectivity.

Spectrum Examples:
~~~~~~~~~~~~~~~~~~

The following example shows a technique where the ALICE spectrum analyzer tool can be used to measure the amplitude vs frequency response of two simple RLC configurations. Shown in figure E11, first on the left is a parallel LC bandpass configuration and second on the right is a series LC bandstop configuration. Indicated by the green boxes are the connections to the ALM1000. AWG Channel 1 is setup to output the driving function of the network. Scope Channel 2 is setup as to measure the response seen across the LC network. For this example R\ :sub:`1` is 1 KΩ, L\ :sub:`1` is 15 mH and C\ :sub:`1` is either 0.22 uF or 0.44 uF.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/alice-sa-fig-e1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E11 RLC circuits


In a linear system, the frequency response can be obtained by sweeping sinusoidal inputs over a range of frequencies. This series of sinusoidal signals at different frequencies can then be used to compute the frequency response. While the ALICE Desktop Bode Plotter does include a sweep generator function, a sweep with many frequency points using large FFT sample sizes can take many seconds or even minutes to up-date the plot. However, FFT analysis can be used to obtain the transfer function for a network from its impulse response. We can generate a test signal with a wide frequency content, a very narrow square pulse, which will produce a plot from a single sample record at a much higher up-date rate.

Using the FFT to get a impulse transfer function of a system is not overly complex and in fact the impulse response method gives better phase results than a sinusoidal sweep.

There must be an input to the network which you can observe and record. There must be an output from the network which you can observe and record. The input and output data has to be able to be read into an analysis program, such as ALICE Desktop, that can take the Fast Fourier Transform of both input and output data records. A basic concept of linear analysis is that the unit impulse response of a network and the transfer function of the network are a Laplace transform pair, or said another way, the transfer function is the Laplace transform of the unit impulse response. The implication is that we can obtain the transfer function by getting the Laplace transform of the unit impulse response.

**Practical implementation.**

If we set the number of FFT samples to 8192 the total sample time will be 81.92 mSec which is more than one cycle at 20 Hz. By setting the AWG 1 function generator to a 20 Hz square wave with a very narrow duty cycle of only a few samples wide the resulting test signal will contain frequency content every 20 Hz with nearly equal amplitude out to high frequencies. At 20 Hz each 10 uSec sample period is equal to about 0.012 % of duty cycle. We can set the duty cycle to anything from 0.01% to 0.08% and get similar results. The only difference is how fast the signal level falls off with increasing frequency. For a given pulse amplitude, the narrower the pulse the less energy in each 20 Hz spaced frequency but the flatter vs frequency they will be. The wider the pulse the more signal energy but a faster frequency roll off. 0.04% gives an acceptable frequency roll off out to 20 KHz.

| The detailed settings for Channel A are as follows:
| Shape - Square
| Mode - Enab
| VMIN = -2.4
| VMAX = 2.4 (pulse amplitude set to allow some headroom for overshoot and ringing, it may be necessary to reduce the pulse size if inputs overload)
| Freq = 20
| Phase = 0
| DutyCycle = 0.04 ( can be adjusted down to 0.02% for flatter input signal energy )

| Other Settings:
| FFT Window – Nuttall ( has an FFT bandwidth which is wider than 20 Hz )
| FFT Samples = 8192
| Start Freq = 100 ( set to something other than 0, to ignore DC content )
| Stop Freq = 20000
| ZeroStuffing = 0 ( can be adjusted but generally has little effect on resultant plot )

Below in figure E12 is a screen shot for the bandpass RLC configuration of figure E1. The green trace for channel 1 is the narrow pulse forcing function response. The light and dark orange traces are the output responses seen by channel 2 for C1 = 0.44 uf and 0.22 uF respectively. The light and dark magenta traces are the subtraction of the Channel 1 trace ( in dBV ) and the Channel 2 trace ( in dBV ). As we know subtraction in dB ( logs ) is the same as division in magnitude. The magenta traces are the actual input to output transfer function of the RLC network. The Yellow trace is the phase response.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/band-pass-response.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E12, Bandpass response


Similarly in figure E13 is a screen shot for the bandstop RLC configuration of figure E1.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/band-stop-response.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E13 Bandstop response


**For Further Reading:**

| https:*en.wikipedia.org/wiki/Fast_Fourier_transform
  http:*\ www.analog.com/media/en/training-seminars/design-handbooks/MixedSignal_Sect5.pdf
| https:*en.wikipedia.org/wiki/Window_function
  https:*\ en.wikipedia.org/wiki/Spectral_leakage
| http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html

Impedance Analyzer / LCR Meter
------------------------------

.. _background-1:

Background:
~~~~~~~~~~~

The basic concept that is used to make gain/phase, impedance and RLC measurements using ALICE Desktop is shown in figure 23. AWG Channel 1 of the ALM2000 is used to apply a known frequency sine wave at VA and measure the applied voltage waveform. Scope Channel 1 is used to measure the input voltage waveform. Scope Channel 2 is used to measure the voltage waveform seen across the network under test. FFTs are calculated on the two waveforms which provide amplitude and phase information at the applied frequency. From these the relative gain ( CH2 amplitude / CH1 amplitude ) and relative phase ( CH2 phase – CH1 phase) are obtained. Further these values can be used to calculate the impedance (RLC) of the network in the dashed box.

The resistor, R\ :sub:`EXT`, is a known value. For the frequency range measurements possible with the ALM2000 hardware it can be adjusted as needed depending on the magnitude of the impedance being tested. Impedances in the range of about 0.1 to 10 times R\ :sub:`EXT` can be accurately measured. R\ :sub:`EXT` can range from 50 Ω to 50 KΩ.

The unknown impedance to be measured is modeled as a series circuit consisting of an unknown series resistance, R\ :sub:`X`, and an unknown series reactance, jX\ :sub:`X`. The magnitude of the impedance is Z\ :sub:`X`.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 23: Basic Concept


| Three voltages are measured:
| 1. VA is the applied voltage ( from AWG Channel 1 of the ALM2000 ).
| 2. VZ is the voltage across the unknown impedance ( from Channel 2 of the ALM2000 ).
| 3. VI, the voltage across the known resistor R\ :sub:`EXT` is calculated from VA and VZ and is related to the current in both R\ :sub:`EXT` and the unknown impedance.

These three voltages are actually vectors and indicated in figure 24.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 24: Vector Diagram


Using the law of cosines and referring to figure 23 the magnitude of VI can be calculated as:

:math:`\displaystyle VI = sqrt(\frac{VA}{2} + \frac{VZ}{2} – 2 \times VA \times VZ \times cos(Φ))`

The angle Φ is the measured relative phase between channel 2 (VZ) and channel 1 (VA). The law of cosines is used to calculate the cosine of the angle, Θ.

:math:`\displaystyle cos(Θ) = (\frac{VA}{2} + \frac{VI}{2} – \frac{VZ}{2})/ (2 \times VA \times VI)`

The magnitude of the total impedance (including R\ :sub:`EXT`) can be calculated as:

:math:`Za = R_EXT \times VA / VI`

We note from figure 1 that the sum of R\ :sub:`EXT` and R\ :sub:`X` can be found by:

:math:`R_EXT + R_X = Za \times cos(Θ)`

Thus, we can solve for R\ :sub:`X` by:

:math:`R_X = Za \times cos(Θ) – R_EXT`

Taking possible measurement errors into account it is possible that R\ :sub:`X` could compute to be a negative value which is not likely to be the case. The thing to do if that happens is to set R\ :sub:`X` to zero. The impedance is purely reactive.

The magnitude of the unknown impedance can be calculated as:

:math:`Z_X = R_EXT \times VZ / VI`

The magnitude of the unknown reactance can be calculated as:

:math:`\displaystyle X_X = sqrt(\frac{Z_X}{2} – \frac{R_X}{2})`

Again taking possible measurement errors into account it is possible that the square root of a negative number might occur. If that happens then X\ :sub:`X` should be set to zero.

Once we have a value for X\ :sub:`X`, we can calculate either the series capacitance ( when X\ :sub:`X` is negative = X\ :sub:`C` ) or series Inductance ( when X\ :sub:`X` is positive = X\ :sub:`L`).

:math:`C = -1/(2πfX_C)`

:math:`L = X_L/(2πf)`

Making Measurements:
~~~~~~~~~~~~~~~~~~~~

Connections to the ALM2000 and the network to be measured are shown in figure 25. In this case we show a simple series connected resistor and capacitor. R\ :sub:`EXT` is 1000 Ohms and the series resistor R\ :sub:`S` is 100 Ohms and the capacitor C\ :sub:`S` is 1 uF. The AWG 1 generator output should always be set to Enab and with a sine wave shape. The user can control the output voltage amplitude and offset with the Min and Max entry slots as when using the scope and spectrum analyzer displays. A good place to start is with Min set to -1.4 and Max set to 1.4 which produces about 1 Vrms amplitude centered on 2.5 V DC. The AWG 2 is not use and can be disabled.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/alice-vvm-fig3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 25, Measurement setup


.. _window-setup-2:

Window Setup:
~~~~~~~~~~~~~

The main impedance analyzer window should appear, as in figure 26. It is sub divided into 2 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-window.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 26, ALICE Impedance Analyzer window


.. _the-right-side-menu-section-1:

The Right Side Menu Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Run, Stop**

Start and stop buttons for continuously taking readings.

**Samples +/- buttons**

Used to change the number of samples in the FFT calculation. This number has to be a power of 2. More samples means a longer time sample which is important when low test frequencies are used. It also provides higher frequency resolution but a slower update rate for the screen. Fewer samples provides a lower frequency resolution, but a faster update rate for the screen. Increasing the zero-stuffing factor can improve the frequency resolution. The program starts up set to 2048 samples.

**FFT window drop down menu**

Used to select an FFT window. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Flat Top window gives the highest amplitude accuracy but also has a large bandwidth, so less selectivity. Using the narrowest bandwidth FFT window and increasing the zero-stuffing factor can improve the measurement results. The program starts up set to the Nuttall window (BW=2.02).

\**File drop down menu \*\*

Save Config Load Config buttons. Commands for saving and loading the configuration settings to a file. (.cfg file)

Save V-Cal, Load V-Cal buttons. ALICE uses the same calibration file as the Voltmeter Tool. To load the saved calibration factors press the Load button. To save the calibration values to the file for future use, press the Save button. The values are saved to a file with a unique name for this particular ALM2000 board based on the first 9 characters of the board device ID serial number. For example something like: 203131543_V.cal.

Save Screen button. Command for saving the graphics display area to an encapsulated postscript file (.eps). The Help button will open a web browser to this document on the ADI Wiki site.

**Options drop down menu**

Cut-DC, an option that will remove the DC component from the sampled data record. It sample by sample subtracts the average value of the sample record. Any DC offset in the FFT could result in that being the peak amplitude and resulting in meaningless measurements. The program starts up with this turned on.

The section along the right hand side contains the controls for making the measurements. There is a place to enter the external resistor value. The program starts up with this set to 1000. Next is a spin box to set the number of Ohms/div for the polar ( circular ) grid.

| M2K Analog Inputs
| ADALM2000 Low Capacitance FET Input Buffers
| M2K Breadboard Adapters

Main Graphics area
~~~~~~~~~~~~~~~~~~

The main graphics area is where the measured results are displayed. The impedance magnitude and angle along with the real and imaginary parts are drawn on the polar ( circular ) grid in Ohms. The real, series resistance component is drawn in green at 0 degrees phase. The imaginary part of the series impedance is drawn in red at either +90 degrees or -90 degrees depending on the sign. A positive impedance is inductive and an negative impedance is capacitive. The combined magnitude of the total series impedance is drawn in orange and at the measured angle.

To the left of the grid the relative gain of Channel 2 to Channel 1 is displayed in dB. Next the relative phase is displayed in degrees. Next the measured frequency in Hz is displayed. Next the measured Impedance Magnitude, Angle, R series and X series are displayed. Finally the calculated capacitance ( if X series is negative ) or inductance ( if X series is positive ) is displayed.

To convert the series values to the equivalent parallel values see section on Calculating Parallel Impedance further down in this document.

Additional setting information is also shown.

Impedance Analyzer Examples:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 1:**

As an example to show the frequency dependent impedance of a series LC circuit we will use the ALICE impedance analyzer tool to examine the combination shown in figure E14 with L\ :sub:`1` equal to 60 mH and C\ :sub:`1` equal to 1 uF. We will use a 100 Ω R\ :sub:`EXT` to be in line with the expected impedance level of the circuit.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/alice-vvm-fige1.png
   :align: center
   :width: 375px

.. container:: centeralign

   Figure E14 Testing an series LC circuit


The LC circuit is tested at three different frequencies, the first much lower than the resonate frequency where the impedance is dominated by the capacitor shown in figure E15.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-exp-1.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E15 Measured results at low frequency, 200 Hz


The second much higher than the resonate frequency where the impedance is dominated by the inductor shown in figure E16.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-exp-2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E16 Measured results at high frequency, 2500 Hz


The third at the resonate frequency where the negative impedance of the capacitor nearly cancels the positive impedance of the inductor shown in figure E17.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-exp-3.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E17 Measured results at resonate frequency, 671 Hz


At these test frequencies the series R measured stays nearly the same at about 155 Ω.

**Example 2:**

We can use ALICE Desktop to measure the input capacitance of channel 2. We know that the input capacitance is small so we will need to use a large value for R\ :sub:`EXT` and measure at a high frequency. In figure E18 we show the connections used which is simply to connect CH1 to CH2 with a 47 KΩ resistor.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/alice-vvm-fige2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E18 Measure CH 2 input capacitance


In the ALICE Impedance Analyzer screen shot shown in figure E19 we see that Ext Res is set to 47000 and the test frequency is set to 100000 Hz. The calculated capacitance is 32.1 pF which agrees nicely with the capacitance reported in the document on the ALM2000 analog inputs.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-exp-4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E19, Measured results for CH 2 input capacitance


If we use the formula from Calculating Parallel Impedance to convert the series R to the parallel resistance we get around 1 MΩ. This is right in line with the known design value.

To measure capacitors around the same value as the input capacitance or even smaller it would be useful to null out this stray parasitic capacitance. This can be done using the Gain Cor and Phase Cor Entry widgets to enter correction factors for the gain and offset. If we enter 3.2 (dB) from the measured Gain for the Gain Cor entry and 41.1 (degrees) for the Phase Cor entry we get the result shown in figure E20.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-exp-5.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E20 Gain and Phase have be corrected


Now the Measured Gain difference is 0.0 dB and the Measured Phase difference is 0.0 degrees. The calculated capacitance is 0.2pF. If we now add a 39 pF ceramic cap, from the ALP2000 Parts Kit, from the channel 2 input to ground we get the results shown in figure E21.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/impedance-exp-6.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E21, 39 pF cap added to CHB.


Now the calculated capacitance reported is 37 pF which is what we can expect from a +/- 20% tolerance on the capacitor.

Calculating Parallel Impedance:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method used in the ALICE impedance analyzer tool determines the series resistance and reactance. Sometimes the equivalent parallel impedance of a resistance and reactance are needed. All that is required is a mathematical series to parallel conversion as follows. The concept is to relate the real and imaginary conductance of the parallel network to the conductance of the series network. The numerator and denominator of the series network conductance is multiplied by the complex conjugate of the denominator to put the result in normal form.

:math:`\displaystyle 1/R_P + 1/jX_P = 1/( R_S + jX_S) = \frac{R_S – jX_S}{ R_S/2 + X_S/2}`

where R\ :sub:`S` and X\ :sub:`S` are the series values and R\ :sub:`P` and X\ :sub:`P` are the parallel values.

By equating the real part we have the equivalent parallel resistance and by equating the imaginary part we have the equivalent parallel reactance:

:math:`R_P = (R_S/2 + X_S/2) / R_S`

:math:`X_P = (R_S/2 + X_S/2) / X_S`

Note that since the polarity of X\ :sub:`S` was known then the polarity of X\ :sub:`P` is also known and is the same sign.

DC Ohmmeter Window:
-------------------

This is the control window for the Ohmmeter tool:

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/ohm-meter-window.png
   :align: center
   :width: 200px

The DC output from AWG 1 is used to drive the voltage divider. The test voltage can be set. The Known resistor needs to be entered. The measured unknown resistance is displayed when the run button is clicked.

The method used to measure unknown resistance is based on the voltage divider configuration shown in the following figure.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-fig6.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure, Voltage Divider Method


If we assume that voltage source V\ :sub:`S` is known, resistance of R\ :sub:`1` is known and we can measure voltage V\ :sub:`2`, the voltage across R\ :sub:`2`, we can use the voltage divider formula to calculate the resistance of R\ :sub:`2`.

:math:`V_2 = V_S \times (R_2/( R_1 + R_2 ))`

Which can be rearranged to:

:math:`R_2 = R_1 \times (V_2 / (V_S - V_2))`

There is a certain advantage to using this voltage divider method over the Ohm's Law method in that a much wider range of resistances can be measured. The Ohm's Law method is limited in one extreme by the maximum current that the ALM2000 can safely source (about 50 mA) along with the internal 50 Ω in series with the AWG output and in the other by the minimum voltage resolution that the ALM2000 can accurately measure (about 1.5 mV). Using the voltage divider method, because we can choose a range of R\ :sub:`1` values, we are only limited by the voltage measurement resolution of the ALM2000 ( about 1.5mV in high gain mode). R\ :sub:`1` can range from as low as 100 Ohms to as high as 10 KOhms in practice which extends the range from 10 Ohm or less to nearly a MOhm.

For the highest values of R\ :sub:`2` the internal 1 MOhm resistance of Channel 2 comes into effect and the software removes this parallel resistance when calculating the value for R\ :sub:`2`.

Digital I/O controls Windows:
-----------------------------

The ALM2000 hardware provides 16 3.3V CMOS digital input / output pins.

|image6| |image7|

.. container:: centeralign

   Figure 27 Digital I/O section of ALM2000 connector


Part of the ALM2000 rev C schematic is shown in figure 28. As can be seen each of the 16 general purpose digital pins is connected to a 220 Ω.

.. container:: centeralign

   Figure 28 ALM2000 digital interface input/output diagram


The state of the first 8 pins can be controlled using the simple digital control interface shown in figure 29. At this time only static hi / low functionality is supported. Eight rows of selectors are provided, one for each pin for the pins (DIO 0 - DIO 7). Each port pin can be set to either a logic low, 0, as a high-impedance input or floating state, Z or a logic high, 1. When in the high-impedance or floating state that pin can be used as a logic input.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/digital-pio-window.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 29, Static Digital I/O control window


Digital pattern generator controls Windows:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any or all of the 16 digital pins can output a repeating pattern at a 100 MHz sample rate. The included rudimentary interface allows them to be configured as square waves of varying frequency with variable duty cycle and time delay. The interface screen is shown in figure 29(a).

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/dpg-controls-window.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 29(a), Digital pattern generator control window


A pattern can also be read in from a file that consists of a list of 16 bit integers representing the states of the 16 pins at each 100 MHz sample time point. For example a 1 will set DIO-0 high, a 2 will set DIO-1 high and 3 will set both DIO-0 and DIO-1 high etc. Individual bits can be enabled ( selected ). If for example the file contains a buss pattern for the first 8 bits the width can be set and the first 8 pins will be enabled.

Steps performed by ALICE 2.0 Desktop Self Calibration:
------------------------------------------------------

ALICE Desktop can perform a self-calibration sequence.

Your ALM2000 is now calibrated.

Checking the Calibration
~~~~~~~~~~~~~~~~~~~~~~~~

The way to check the calibration results is to set both AWG channels to Sine shape with -2.5 Min and 2.5 Max values set in Enabled mode.

What if I don't have an AD584
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't have access to an AD584 ( or other accurate 2.5 V reference ) but do have access to an accurate DMM with enough resolution to measure 2.5 volts with 4 decimal places you can do the following.

Support for Plug-In Boards
--------------------------

ALICE Desk-Top provides software interfaces for external plug-in boards which extend the functionality of the basic hardware. There are four types of external boards currently supported. External analog multiplexers to increase the number of analog input channels. External DDS based function generators such as the AD9837 based MiniGen from SparkFun. External serial 8 bit DACs such as the AD7303 based `PmodDA1 from Digilent <http://store.digilentinc.com/pmodda1-four-8-bit-d-a-outputs/>`__. External digital potentiometers such as the AD840X single, dual, quad family or the AD5160 based `PmodDPOT from Digilent <http://store.digilentinc.com/pmoddpot-digital-potentiometer/>`__. A generic 3 wire SPI serial output interface.

The software interfaces for these can be enabled or disabled by setting the following variables to either 1 or 0 in the alice_init.ini file, see :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>` for more details.

| EnableMuxMode
| EnableMinigenMode
| EnablePmodDA1Mode
| EnableDigPotMode

EnableMuxMode is set to 1 by default, the rest are set to 0. When these variables are set a button to open their respective control window will appear in the right side of the main ALICE window.

Multichannel analog interface for the ADALM2000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two analog input channels of the ADALM2000 provide a high input impedance and wide dynamic range which is very helpful for many of the measurements that a user would be making during laboratory activities. However, there are only the two analog inputs. Often, there are many more than two signals in the circuit under investigation that the user would like to monitor. Or there could be a number of low bandwidth sensors, such as ambient temperature or light levels around a room, that need to be measured or monitored over long durations of time when gathering experimental data. As a solution to this need ALICE desktop provides the necessary software interface to control an external multi-channel analog multiplexer such as these two breakout board from SparkFun based on `the 74HC4067 16:1 MUX <https://www.sparkfun.com/products/9056>`__ and `the 74HC4051 8:1 MUX <https://www.sparkfun.com/products/13906>`__. There are also hook-up guides on their web site

|image8| |image9| |image10|

.. container:: centeralign

   Figure 35, Analog multiplexer schematic


The analog Mux control window is shown in figure 31. The C2 voltage controls on the main scope window no longer function when this window is open and are replaced by the four new sets of voltage controls. The check boxes select which of the four Mux input channels will be displayed. The Mux-Enb checkbox sets PIO-2 either low ( when not checked ) or high ( when checked ) for Muxes like the CD4052 with enable low inputs or the ADG609 with enable high inputs.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/analog-mux-controls.png
   :align: center
   :width: 320px

.. container:: centeralign

   Figure 36, Analog Mux Control window


The analog Mux interface in ALICE desktop uses a technique common in analog CRT oscilloscopes ( with a single electron beam ) where multiple input channels are switched to the beam deflection circuits on alternating sweeps. This trick requires periodic signals and that each sweep be “triggered” or synced from the same input signal. In this case the triggering signal will be channel 1 which is not multiplexed. As an example note the screen shot in figure 37.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/analog-mux-window.png
   :align: center
   :width: 720px

.. container:: centeralign

   Figure 37, Four channel Mux display of ALICE desktop


One important feature of the program is that a sync or sweep start pulse is output on the PIO 3 digital output pin just before each analog sweep starts. The sync pulse can be set to either a high going or low going pulse with the selector next to the pulse shaped icon. Using this “reset” pulse would be necessary whenever this program is used to observe a circuit that contains “state” for example a digital counter or state machine.

External DDS based function generators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ALM1000 has 4 general purpose digital input/output pins which can be used as a serial port (SPI). These pins are used to interface to direct digital synthesis (DDS) waveform generators such as the AD9837 and AD9833. These DDS generators are capable of producing sine, triangular, and square wave outputs. SparkFun offer a breakout board based around the AD9837 DDS called the MiniGen ($29.95).

In figure 33 we see that it is a relatively simple matter to connect the MiniGen board to the digital connector on the ALM1000. If a 6 pin right angle male header is installed as shown, the FSYNC, SDATA, and SCLK pins connect to PIO 0, PIO 1, and PIO 3 respectively. The other three header pins are open connections on the MiniGen board and the ground and power GND, The VIN pin can be wired to 3.3V and GND to GND with jumper wires. The solder bridge jumper, which shorts out the on board LDO, for powering the board directly from 3.3V will also need to be soldered in as shown. Installing a two pin female right angle connector to the analog output connection points is needed as well.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/mini-gen-connections.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 33 Adapting AD9837 MiniGen to ALM1000


The MiniGen control window, figure 34, allows the four possible waveform shapes to be selected. The master clock frequency can be set, the board comes populated with a 16 MHz crystal oscillator. And of course the output frequency can be set.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/mini-gen-controls.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 34, MiniGen control window


The MiniGen board produces a fixed 1 V p-p amplitude signal centered on the supply / 2 which is about 1.65 V in this case.

The AD9833 is a DDS waveform generator chip similar to the AD9837. The datasheet for the AD9833 indicates that the serial interface waveforms are the same as for the AD9837 and the configuration of the control, frequency and phase registers are the same as well so the ALICE Desktop interface will work for both devices by connecting which I/O pins map to FSYNC, SDATA and SCLK as needed.

**Using MiniGen with Bode Plotter**

As of the 6-19-2017 version of ALICE 1.1 Desktop it is possible to use the MiniGen as the sweep signal source for the Bode Plotter. If the MiniGen controls are opened before opening the Bode Plot window a third option will appear under Sweep Generator. The MiniGen has a fixed amplitude or 1 V p-p centered on one half the power supply, which is typically 3.3 V. The MiniGen is capable of generating much higher frequencies than the built in AWG sources. This allows sweeps all the way to just below the 50 KHz limit of the 100 KSPS.

External serial 8 bit DAC Pmods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital input/output pins can interface to the PmodDA1 4 channel DAC module sold through `Digilent <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,401,501&Prod=PMOD-DA1>`__ and other distributors such as `Mouser <http://www.mouser.com/ProductDetail/Digilent/410-063P/?qs=sGAEpiMZZMtWZAo%2fKf1JUOZxRUX4AaOJSE8oCSC4CQo%3d>`__.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmodda1-obl-400.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 35, PmodDA1


The PmodDA1 has two AD7303 8 bit dual voltage output DACs as shown in the block diagram in figure 36.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmodda1-block-336.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 36, PmodDA1 block diagram.


The module has a 6 pin male connector which plugs directly into the digital port on the ADALM1000. Because of the “Top” component side of the ALM1000 actually faces down the PmodDA1 also needs to be plugged in with the “Top” component side facing down. Carefully note the pin labels on both boards before plugging in the Pmod. The 6 pin header on the module lines up with the pins on the ALM1000 digital connector and all four of the general purpose I/O pins are used as follows. PIO 0 connects to the SYNC input on both DACs. PIO 1 connects to the data input on the first AD7303. PIO 2 connects to the data input on the second AD7303 and PIO 3 connects to the SCLK serial clock input on both DACs.

There is no external access to the reference input voltage on the DACs so they must generally be configured to use VDD/2 as the reference. In this case VDD is wired to the 3.3 Volt suppled on the digital port connector. The voltage output range for all four output channels will be 0 to 3.3 V.

The AD7303 DACs are also available in 8 pin PDIP packages and could be used plugged into solder-less breadboards with other components of a circuit project.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmod-da1-controls.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 37, PmodDA1 control window


Controls for the four DAC channels of the PmodDA1 are shown in figure 37. Enter the desired DC voltage(s) from 0 to 3.3 V ( less one LSB ) and click UpDate to send the new values to the DACs.

External digital potentiometers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD8402 dual 10 KΩ and AD8403 quad 10 KΩ digital potentiometer have 8 bit resolution and are available in PDIP packages that work well in solder-less breadboards. How to connect the AD8402 to the ALM1000 is shown in figure 39. The single 8 bit 10 KΩ digital potentiometer, AD5160, based PmodDPOT, figure 38, is also compatible with the same 6 pin male connector which plugs directly into the digital port on the ADALM1000. Because of the “Top” component side of the ALM1000 actually facing down the PmodDPOT also needs to be plugged in with the “Top” component side facing down. Carefully note the pin labels on both boards before plugging in the Pmod.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmod_dpot_top.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 38, PmodDPOT


Connections for the AD8402 dual pot are shown in figure 39. Connections for the AD8400 single and AD8403 quad are similar.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/ad8402-connections.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 39, AD8402 connections


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/dig-pot-controls.png
   :align: center
   :width: 290px

.. container:: centeralign

   Figure 40, Digital Pot control window


The digital potentiometer controls window has check boxes to select which of the up to four pots of the AD8403 are sent data. Each pot has a slider to control its value from 0 to 255. The radio button selects between the AD840X family which sends 10 bit data ( 8 bit value + 2 bit address ) and the AD5160 single pot which sends 8 bit data.



.. raw:: html

   <details><summary>Click to expand</summary>

Generic 3 wire SPI output:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital input/output pins can output serial data to generic 3 wire SPI serial input devices. The provided interface allows the user to configure any of the 4 PI/O digital pins ( 0 – 3 ) as either the SCLK, SData, or Latch ( sometimes called CS or SYNC ) outputs. The user can set the number of bits to be sent in each digital write. The data word to be sent can be entered in either decimal ( integer ) form or Hex by using the 0x00 format. The “resting” sense, i.e. the level between writes, of the latch output can be set as well ( Latch Phase selector ). Some serial devices operate on the rising edge of the Latch (CS, SYNC) signal or on the falling edge. It is possible to select order in which the serial bits are sent, either LSB first or MSB first. The current data value is sent or written each time the Send button is clicked.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/serial-out-controls.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 41, Generic Serial Interface screen

.. raw:: html

   </details>


Applying Digital Filtering:
---------------------------

With this interface, ALICE Desktop can apply digital filtering to the captured Channel 1 and 2 voltage waveform data before being displayed in the Time and/or Frequency domains. ALICE uses the numpy convolve function to perform the filtering function. The supplied list of coefficients is convolved with the captured data buffer. The list of filer coefficients for either Channel 1 or 2 is first loaded from a single column .csv file by using the “Load CH 1 Filter Coef” and “Load CH 2 Filter Coef” buttons. The length ( number of coefficients ) and file name will then be displayed. The digital filter(s) will be applied to the voltage waveform data buffers if the “Filter CH 1” and/or “Filter CH 2” checkboxes are checked.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/dig-filter-controls.png
   :align: center
   :width: 210px

.. container:: centeralign

   Figure 42, Digital Filtering Interface


The arithmetic sum of the coefficients should equal 1 for the “filter” to have an overall gain of one. A simple low pass filter for example has a rectangular (box-car) shape. The coefficients for a length of 2 would be [ 0.5, 0.5 ]. For a length of 4 the coefficients would be [ 0.25, 0.25, 0.25, 0.25 ] and so on. A few `example filter files can be found here <https://wiki.analog.com/_media/university/tools/m1k/alice/example-filters.zip>`__:

Alternatively, a formula for the filter coefficients can be entered using the CH 1 or CH 2 Filter formula buttons. The program puts up an entry window where the formula can be entered. Conventional Python syntax is used and all the math and numpy library functions are available as in the the rest of ALICE. The program looks at the arithmetic sum of the coefficients and scales them appropriately for an overall gain of 1 through the filter.

The DFiltACoef and DFiltBCoef array variable are used to store the filter coefficients. The Filter formula coefficient scaling feature can be used to scale a set of filter values read from a file. First read in the values from the file and then simply pass the array through the formula function by entering DFiltACoef or DFiltBCoef for the formula.

There are many filter design tools that can be found by searching the web. Here is one that works well but we are not necessarily endorsing it over any others that might be out there:

http://t-filter.engineerjs.com/

The array of coefficients ( filter taps ) that it generates as part of the C source code can be copy and pasted into a .csv file for use in ALICE.

The interface for the digital filters can be enabled or disabled by setting the following variable to either 1 or 0 in the alice_init.ini file, see :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>` for more details.

EnableDigitalFilter

Command Line Interface:
-----------------------

ALICE Desktop provides a simple command line interface for more advanced users who would like full access to the captured data and the inner working of the program and especially the Numpy library of array math functions. By default the button to activate this interface is not included in the Main ALICE window. To include the activate button, add the following line to the alice_init.inc file:

global EnableCommandInterface; EnableCommandInterface = 1

The interface is not complex to use if you are relatively familiar with Python syntax and the variable structure of ALICE. When creating ( using ) a variable for the first time it must be declared as global first. As a reminder, the interface starts up with the word global and a ; ( used to separate more than one command on the single line). To execute the command line either hit the <enter> or <return> key or click on the Execute button. The last line successfully executed is displayed just below where it says Last command:.

.. image:: https://wiki.analog.com/_media/university/tools/m2k/alice/command-line-window.png
   :align: center
   :width: 370px

.. container:: centeralign

   Figure 43 ALICE Command Interface


More advance information on the inner working of ALICE, variable and array names and the Numpy function library can be found in the ALICE Advanced User’s Guide.

One useful function that might come in handy is the Numpy function to write the contents of an array to a text file. For example, to save the VBuffA ( channel A voltage waveform buffer ) to a .csv file you would type:

numpy.savetxt(“my_data.csv”, VBuffA, delimiter=",", fmt='%2.4f')

Where “my_data.csv” is the name of the destination file, VBuffA is of course the data array to save, delimiter="," tells the function to use a , to separate the columns ( there won’t be multiple columns since most ALICE arrays are one dimensional ) and fmt='%2.4f' sets the format to 4 decimal places.

Customizing ALICE Desktop
-------------------------

This section has been moved to the :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>`.

Using the numpy library
-----------------------

This section has been moved to the :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>`.

**For Further Reading:**

**Return to the** :doc:`Table of Contents </wiki-migration/university/tools/m2k>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/hookah-smoking_caterpillar.png
   :width: 300px
.. |plutosdr-m2k-drivers-win| image:: https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win
.. |Microsoft Web Site| image:: https://www.microsoft.com/en-us/download/details.aspx
.. |here| image:: https://docs.scipy.org/doc/numpy-1.10.1/user/install.html
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/alice/adalm2000-pinout.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/alice/m2k-pinout-1.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/alice/awg-math-example-1a.png
   :width: 750px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/alice/awg-math-example-1.png
   :width: 750px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/alice/adalm2000-pinout.png
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/alice/m2k-pinout-1.png
   :width: 500px
.. |image8| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/analog-mux-curcuit.png
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/adg609-analog-mux.png
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/cd4052-analog-mux.png
   :width: 500px
