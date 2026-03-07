Arbitrary Waveform Generator Virtual Instrument for ADALM1000 in ALICE 1.3
==========================================================================

Objective:
----------

This document serves as the Arbitrary Waveform Generator (AWG) section of the User’s Guide in the ALICE 1.3 Desktop software interface written for use with the ADALM1000 active learning kit hardware.

AWG Controls Window:
--------------------

The AWG controls window is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/awg-controls-window.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 1 AWG Controls window


There are two identical sets of controls for configuring the Channel A and B outputs. First there is a drop down menu for selecting the Mode, figure 2. The SVMI option is for sourcing voltage / measure current. The SIMV option is for sourcing current / measure voltage. The Hi-Z option disables the generator output (High Impedance mode). The default at start-up is that both channels are in Hi-Z mode. The Split I/O option separates the generator output signal from the voltage measurement input. In the Rev D version of ALM1000 hardware only the source current function operates when the output and input are on separate pins so the Split I/O option automatically puts the hardware into the source current configuration. To turn the sourced current into a voltage the output termination options can be used. The hardware includes two 50 Ohm resistors that can be connected to the generator output pin. One resistor is tied to ground and the other is tied to the 2.5 V power supply. The drop down menu provides three options Open, To GND, and To 2.5V. If you are just looking at voltage in SVMI mode there should be no noticeable change in the voltage waveform. The current waveform should change to reflect the current now flowing into the resistor. If you are in SIMV then the resistors can act as current to voltage converters.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/awg-controls-modes.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 2, AWG Modes drop down menu


The Min and Max entry windows program the minimum and maximum values for the output waveform. When in the source voltage mode the values are in Volts, when in source current mode the values are in mAmps. If the value entered in the Min window is higher ( more positive ) than the value entered in the Max window the apparent phase of the output wave is inverted. While this is somewhat redundant for the Sine, Triangle and Square wave shapes, given the Phase control described later, it is useful for determining if the Sawtooth or Stairstep shapes are rising or falling ramps.

The Freq entry window programs the frequency of the waveform in Hertz. Given the 100KSPS maximum sample rate, the maximum possible frequency is, by definition, 50 KHz but the practical upper limit is more like 20 KHz or less.

The relative timing between the two AWG channels can be set as either a phase angle or delay in time. The Phase and Delay buttons choose between the two methods. The entry window programs either the phase of the output waveform in degrees from 0 to 360 or the time delay in mSec. The % entry window only applies to the Square shape and programs the duty cycle in percent from 0% to 100%.

The 0.89 version of the low level ALM1000 software library used in ALICE 1.1 only outputs the signals as single bursts each sweep when the analog signals ( voltage and current ) are being generated. The analog outputs will enter the high impedance state ( Hi-Z ) between sweeps and when the program is stopped ( Red Stop button pressed ). The 1.0 version of the low level ALM1000 software library used in ALICE 1.3 supports outputting the signals as single bursts each sweep or as continuous streams when the analog signals ( voltage and current ) are being generated.

With the Sync AWG check box in either version the outputs are produced in sync with the analog trace sweeps. In version 1.1 if the Sync AWG check box is not checked the outputs are in Hi-Z mode. In version 1.3 if the Sync AWG check box is not checked the outputs stream continuously.

The Shape drop down menu is used to select the shape of the output waveform. There are 6 built in waveform shapes, DC, Sine, Triangle, Sawtooth, Square, and a 10 level Stair Step. When DC is selected the constant value of the output voltage or current is set by the value in the Max entry window.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/awg-controls-shapes.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 3, AWG Shapes drop down menu


Random "Noise" can be added or superimposed on all but the waveform shapes that are built into (use) the Libsmu library functions (Square, Triangle, Sawtooth, Stairstep). When the selector is set to None no noise is added to the waveform. Uniform distribution or Gaussian distribution random values can be chosen. The amplitude of the added noise can be entered in the Amplitude entry space. The noise is calculated and added to the waveform once when the wave shape is selected and a new set of noise values will be calculated and added each time the waveform parameters ( Min, Max, Freq, etc. ) are changed. To add noise to a DC value, use the UU Noise or UG Noise wave shapes and set the Min and Max value so that they are centered on the desired DC value and are above and below the DC value by the desired noise amplitude.

Wave Shapes below the line separator in the menu use the AWGAwaveform or AWGBwaveform array buffers to contain the waveform sample data points. A new data set based on the entered values is generated each time the button is clicked or the waveform parameters ( Min, Max, Freq, etc. ) are changed.

The Impulse, Trapezoid, U-D Ramp, UU Noise ( uncorrelated uniform distribution ) and UG Noise (uncorrelated Gaussian distribution ) buttons are used to build waveform arrays based on user input parameters.

The basic shape of the Impulse waveform is shown in figure 10. The Max, Min, Freq, Phase and Duty-Cycle values are used to construct the waveform. The Freq setting determines the Period ( 1/Freq ) or spacing between the pulses. The output starts and ends at a value midway between the Min and Max values. The impulse consists of a positive peak followed by a negative peak. The width of the peaks are equal to (Period \* DutyCycle)/ 2. The center of the pulse is delayed by the Phase setting. For example if the phase is set to 180 then the pulse is delayed by ½ the Period (Phase/360).

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impulse-waveform.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 4, Impulse waveform


The Trapezoid waveform makes a pulse with a rise and fall time set by the number of mSec entered in the delay entry slot. The Min, Max, Freq, and Duty-cycle entries operate as in the Square Shape.

The U-D Ramp ( ramp up ramp down ) shape is much like the triangle shape except that the Duty-cycle entry sets the symmetry of the up and down ramps. For example if the Duty-cycle is set to 25% the wave will ramp up from Min to Max for 25% of the Period ( 1/Freq ) and then ramp down from Max to Min for 75% of the period.

The Fourier Series shape builds a waveform based on the Fourier series of cosines for a square wave. The number of odd harmonics of the fundamental, is entered in the % entry slot which changes to Harmonics when in Fourier shape mode. The minimum and maximum values of the fundamental are set using the Min and Max entries and the fundamental frequency is set using the Freq entry. Entering 1 for the number of harmonics will result in just the cosine wave at the fundamental frequency. Entering 3 for the number of harmonics will include the third harmonic, entering 5 for the number of harmonics will include the third and fifth harmonics and so forth. More information on this can be found in the Advanced Users Guide.

There are two Noise like waveforms that can be generated. A new data set is generated each time the button is clicked. That fixed data pattern is then send to the output each time sweep. UU Noise or uncorrelated uniform distribution is made using a random number with a uniform distribution between the Min and Max settings. The average value of the noise should be equal to Max+Min/2. UG Noise or uncorrelated Gaussian distribution is made using a random number with a Gaussian distribution centered on Max+Min/2 with a sigma of (Max-Min)/3.

Waveform data point values can be read in from a simple single column csv text file ( one row per time sample ) by clicking on the Read File button. For voltage waveforms the values can be decimal numbers ranging from 0 to 5 in volts. For current waveforms the values can be decimal numbers ranging from -0.2 to 0.2 in amps. If the .csv file contains more than one column the user will be prompted to choose which column number to import. The contents of the Min, Max, Freq, Phase and % entry slots are not used for wave shapes input from a file. Use the Custom Math Waveforms feature below to change the amplitude and offset of the waveform. The contents of the AWG A or B waveform arrays can be saved to a csv file by clicking on the Save File button.

Waveform data point values can also be read in from an audio file in .wav format, 16 bit data. The sample rate is assumed to be 100 KSPS. Mono files can be read into either the AWG A or AWG B waveform buffers. To read a stereo file use the Read WAV File button for AWG A. The Left channel will be loaded into AWG A and the Right channel will be loaded into AWG B. The 16 bit integer data is scaled and offset to fit within the 0 to 5 V range of the ALM1000. Up to 90,000 sample points ( 900 mSec ) will be loaded. The open source audio program Audacity is a good option for generating and editing wave files.

A small library of example waveform files can be downloaded `HERE <https://wiki.analog.com/_media/university/tools/m1k/alice/arb_waveform_library.zip>`_.

If the number of sample points in the waveform array is less than the time sweep the output of the AWG will continuously output the last sample value in the array until the end of the sweep. To repeat the data samples in the waveform array for longer time sweeps click on the Repeat option button.

Custom Math Waveforms
~~~~~~~~~~~~~~~~~~~~~

In addition to the built-in AWG wave shapes, ALICE Desktop provides a method of generating user defined wave shapes from equations or formulas using the AWG waveform buffers for channels A and B. The formulas are written in conventional Python syntax which is basically the same as you would expect to write any math expression. As with the Math plotting, any of the ALICE global variables can be used. Only difference is that the time increment variable (t) is not used. Care must be taken if the lengths of any arrays being used in the expression are of differing lengths. As a reminder the length of the waveform array(s) will be displayed below the % entry slot if the array for that AWG channel has been generated. The following example Python syntax allows setting the start and stop points to be used in the array:

AWGAwaveform[ start : stop ] where start and stop are integers.

For example to copy the CH A captured data from the VBuffA array to the AWGBwaveform array you would simply click on the Math option under the AWG B Shape menu and type VBuffA as the formula, as in figure 5.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/awg-math-win-1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 5, Enter AWG waveform formula


As a more complex example let’s say we want to add noise to a waveform that was read from a file. The first step is to read the data into the AWGAwaveform array. The waveform chosen for this example is 8000 samples long and is a full wave rectified sinewave that is 1 V p-p, from 1.25 V to 2.25V. Then generate a noise waveform in the AWGBwaveform array by setting the AWG B Min and Max values to the desired amplitude of the noise ( 0.1 V in this example ) and the Freq ( 12.5 Hz or 80 mSec ) such that the period of the noise will be as long as the waveform in AWG A ( length = 8000 points ). Click on either UU Noise or UG noise. Now click on the Math shape button in AWG B and enter the following formula:

AWGAwaveform + AWGBwaveform + 1.25

The resulting output wave shapes are shown in figure 6. The CH A trace shows the shape as read in from the file. The CH B trace shows the calculated wave shape with the added noise and offset.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/awg-math-example-1.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 6, Math wave shape example


How the controls are arranged:
------------------------------

How the AWG controls are arranged is set by the global AwgLayout; AwgLayout = "Horz" variable in the alice_init.int file at start-up. Side by side horizontally is the default like this:

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/awg-controls-window.png
   :align: center
   :width: 600px

Or by setting the variable to something other than "Horz", such as "Vert", can be stacked vertically like this:

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/vertical-awg-win.png
   :align: center
   :width: 100px

**For Further Reading:**

**Return to the** :doc:`ALICE Main Page </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`\ **.**
