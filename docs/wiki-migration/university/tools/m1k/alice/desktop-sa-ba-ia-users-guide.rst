Spectrum Analyzer / Bode Plotter / Impedance Analyzer Virtual Instruments for ADALM1000 in ALICE 1.3
====================================================================================================

Objective:
----------

This document serves as the Spectrum Analyzer / Bode Plotter / Impedance Analyzer section of the User’s Guide in the ALICE 1.3 Desktop software interface written for use with the ADALM1000 active learning kit hardware.

The Spectrum Analyzer / Bode Plotter / Impedance Analyzer:
----------------------------------------------------------

Spectrum Aanlyzer Window Setup:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the Spectrum window button is clicked in the ALICE Main Window the Spectrum display Window should appear, as shown in figure 1. It is sub divided into 2 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/spectrum-window.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 1, ALICE Desktop spectrum analyzer window


The menu buttons:
~~~~~~~~~~~~~~~~~

The following sections cover the functions of the various menu buttons. Most of the control settings can be found under the buttons.

\**File drop down menu \*\*

Save Config Load Config, commands for saving and loading configuration settings (.cfg file).

Save Screen, command for saving the graphics display area to an encapsulated postscript file (.eps)

Save Data, command for saving the captured channel A and B amplitude vs frequency data to a coma separated values file (.csv). The amplitude data can be saved as magnitude in Vrms ( type a 0 ) or in dBV ( type a 1 ).

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

The Curves button allows the selection of which signal waveforms will be displayed. The All button selects all four curves to be displayed and the None button clears all four curves. The Marker option turns on a text marker which displays the amplitude and frequency at the peak of the displayed signal. Options to display the difference ( subtraction ) of the CA-dBV – CB-dBV traces or the CB-dBV – CA-dBV traces. It is also possible to select which of the possible stored reference traces, if saved via the Store trace option, will be displayed. The color of the CA-dBV and CB-dBV traces will turn red if the input signal goes beyond the 0 to +5 V analog input signal range.

Under the Curves Drop down menu there are selectors for displaying the F cursor ( frequency ) and dB cursor ( amplitude ). When selected if you right click anywhere within the display grid either a vertical or horizontal cursor line, or both, will be drawn at that location. The vertical, horizontal, or both values for that point will be displayed. Scrolling with the mouse wheel will move the vertical line left–right when only the F cursor is selected and the horizontal up-down when only the dB cursor is selected. When both are selected the mouse wheel moves the vertical line left–right.

There are no scrollbars, or rotating knobs. The mouse wheel generally scrolls values when hovering over spin boxes and numerical entry widgets.

**Startfreq and Stopfreq**

Used to set the start and stop frequency of the display.

**Lin F and Log F selector**

Select linear or logarithmic horizontal frequency axis scale.

**Center Phase Axis**

The Angle for the Phase axis center can be set using this entry widget.

**Vertical Axis Settings**

The vertical axis can display the signal amplitude in dBV (1 Vrms = 0 dB) or Vrms. When displaying in Vrms the scale can either linear or log. The signal can also be displayed as Power Spectral Density (PSD) in Vrms or dB per square-root-Hz.

**dB/div +/- buttons**

Used to set the dB’s per division. Can be 1, 2, 3, 5, 10, 15, or 20 dB/Div.

**LVL +/- buttons**

Used to set the top line of the grid or reference level. Sometimes called the "sensitivity". 0 dB is equal to an input amplitude of 1 Vrms.

The Bode Plotter:
-----------------

Bode plots (named after `Hendrik Wade Bode <https://en.wikipedia.org/wiki/Hendrik_Wade_Bode>`_) are theoretical straight-line approximations of gain and phase response versus frequency of a system’s output relative to the input (frequency response). The plot is based on poles and zeros of the circuit’s transfer function. Testing of actual circuits, shows that the real gain and phase traces are not perfect straight lines, especially near the theoretical pole and zero frequencies.

Frequency response analysis is a critical step in the design of passive and active filters, amplifiers, and the closed-loop response of negative feedback systems. Frequency response analysis has historically been a very tedious measurement exercise using just an oscilloscope along with a sinewave function generator as the input source. It involved multiple manually-performed amplitude and phase (time difference) measurements to determine gain (A = 20LogV\ :sub:`OUT`/V\ :sub:`IN`) and phase at multiple frequencies. The ALICE desktop software can perform automatic frequency response measurements (sweeps) using the M1k's built-in waveform generator as a sinewave input source.

Bode Plotting Window Setup:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you perform a frequency response test to produce a gain and phase Bode plot, you should have a basic understanding of the test setup parameters in the ALICE Bode Plot menu. When the Bode Plot window button is clicked in the ALICE Main Window the Bode Plot display Window should appear, as shown in figure 2. It is sub divided into 2 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/bode-main-window.png
   :align: center

.. container:: centeralign

   Figure 2, ALICE Desktop Bode plot window


**FFT window drop down menu**

Used to select an FFT window function. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Nuttall window function is set by default and is generally the best overall option. The Flat Top window gives the best amplitude accuracy but can have strange phase results at some frequency steps.

**Curves drop down menu**

The Curves button allows the selection of which signal waveforms will be displayed. The All button selects all four curves to be displayed and the None button clears all four curves. The Marker option turns on a text marker which displays the amplitude and frequency at the peak of the displayed signal. Options to display the difference ( subtraction ) of the CA-dBV – CB-dBV traces or the CB-dBV – CA-dBV traces. It is also possible to select which of the possible stored reference traces, if saved via the Store trace option, will be displayed.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/bode-curves-drop-down.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 3, Bode plot Curves Drop Down


The color of the CA-dBV and CB-dBV traces will turn red if the input signal goes beyond the 0 to +5 V analog input signal range.

Under the Curves Drop down menu there are selectors for displaying the F cursor ( frequency ) and dB cursor ( amplitude ). When selected if you right click anywhere within the display grid either a vertical or horizontal cursor line, or both, will be drawn at that location. The vertical, horizontal, or both values for that point will be displayed. Scrolling with the mouse wheel will move the vertical line left–right when only the F cursor is selected and the horizontal up-down when only the dB cursor is selected. When both are selected the mouse wheel moves the vertical line left–right.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/bode-cursors-drop-down.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 4, Bode plot Cursors Drop Down


**Lin F and Log F selector**

Select linear or logarithmic horizontal frequency axis scale. This also determines how the frequency steps are spaced, linearly or logarithmically.

**dB/div +/- buttons**

Used to set the dB's per division. Can be 1, 2, 3, 5, 10, 15, or 20 dB/Div.

**LVL +/- buttons**

Used to set the top line of the grid or reference level. Sometimes called the “sensitivity”. 0 dB is equal to an input amplitude of 1 Vrms.

**Center Phase Axis**

The Angle for the Phase axis center can be set using this entry widget.

**Center Impedance Axis**

The center value for the Impedance axis can be set using this entry widget.

**Sweep Generator**

Under the Sweep Gen section are controls for generating frequency sweeps of the analog output sources. The screen is up-dated after each frequency step. First are radio buttons to select which AWG output channel, or none will be swept. When using the Bode plotter the selected AWG will be forced into SVMI mode with a Sine Shape. Use the AWG controls window to set the source amplitude. The other channel will be forced into Hi-Z mode. The selected output will be swept from the Start Frequency to the Stop Frequency. The number of steps can be set using the Sweep Steps entry.

The amplitude of the swept source is generally held constant across frequency but in some special cases it might be desirable to change the source amplitude at each frequency step. Checking the Sweep From File check box will prompt the user for a .csv file. The csv file should contain two columns of values one row for each frequency amplitude combination for the sweep. The first column should contain a monotonically increasing list of frequency steps in Hz. The second column should contain the corresponding amplitude value in dB. The Start, Stop and number of Steps will be filled in based on the contents of the file. After reading in the csv file the program will display the highest ( maximum ) amplitude value found and ask the user to input the desired maximum the values should be normalized to. This is done because the ADALM1000 has an upper limit to the range of output amplitudes ( around +4.5 dBV ). Also it might be useful to scale the amplitude values up or down to optimize the dynamic range of the swept signal.

Lastly, there is a radio button selector for single or continuous sweep. The frequency sweep is started, or restarted from the beginning each time the Run button is pressed.

**Bode Polar and Rectangular Plots**

The standard Bode plot for a parallel LC tank circuit is shown in figure 5, where the relative gain or CB-dBV – CA-dBV trace and relative Phase B-A trace are plotted on the log frequency axis.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/bode-example-window.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 5, Bode Gain, Phase log Frequency Plot


It is also possible to plot the relative gain and relative phase measurement on a polar axis as the frequency is swept. Figure 6 plots the CB-dBV – CA-dBV gain trace as a function of the relative phase angle.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/bode-polar-plot.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6, Bode Polar Plot


It is also possible to plot the relative gain and relative phase measurement on a rectangular axis as the frequency is swept. Figure 7 plots the CB-dBV – CA-dBV gain trace (vertical) as a function of the relative phase angle (horizontal).

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/bode-rectangular-plot.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 7, Bode Rectangular Plot


Spectrum Examples:
~~~~~~~~~~~~~~~~~~

The following example shows a technique where the ALICE spectrum analyzer tool can be used to measure the amplitude vs frequency response of two simple RLC configurations. Shown in figure E1, first on the left is a parallel LC bandpass configuration and second on the right is a series LC bandstop configuration. Indicated by the green boxes are the connections to the ALM1000. Channel A is setup to output the driving function of the network. Channel B is setup as an input to measure the response seen across the LC network. For this example R\ :sub:`1` is 1 KΩ, L\ :sub:`1` is 6.5 mH and C\ :sub:`1` is either 0.47 uF or 1.0 uF.

.. image:: https://wiki.analog.com/_media/university/tools/alice-sa-fig-e1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E1 RLC circuits


In a linear system, the frequency response can be obtained by sweeping sinusoidal inputs over a range of frequencies. This series of sinusoidal signals at different frequencies can then be used to compute the frequency response. While the ALICE Desktop Bode Plotter does include a sweep generator function, a sweep with many frequency points using large FFT sample sizes can take many seconds or even minutes to up-date the plot. However, FFT analysis can be used to obtain the transfer function for a network from its impulse response. We can generate a test signal with a wide frequency content, a very narrow square pulse, which will produce a plot from a single sample record at a much higher up-date rate.

Using the FFT to get a impulse transfer function of a system is not overly complex and in fact the impulse response method gives better phase results than a sinusoidal sweep.

There must be an input to the network which you can observe and record. There must be an output from the network which you can observe and record. The input and output data has to be able to be read into an analysis program, such as ALICE Desktop, that can take the Fast Fourier Transform of both input and output data records. A basic concept of linear analysis is that the unit impulse response of a network and the transfer function of the network are a Laplace transform pair, or said another way, the transfer function is the Laplace transform of the unit impulse response. The implication is that we can obtain the transfer function by getting the Laplace transform of the unit impulse response.

**Practical implementation.**

If we set the number of FFT samples to 8192 the total sample time will be 81.92 mSec which is the same as one cycle at 12.2 Hz. By setting the Channel A function generator to a 12.2 Hz square wave with a very narrow duty cycle of only 4 – 6 samples wide the resulting test signal will contain frequency content every 12.2 Hz with nearly equal amplitude out to high frequencies. At 12 Hz each 10 uSec sample period is equal to about 0.012 % of duty cycle. We can set the duty cycle to anything from 0.012% to 0.08% and get similar results. The only difference is how fast the signal level falls off with increasing frequency. For a given pulse amplitude, the narrower the pulse the less energy in each 12.2 Hz spaced frequency but the flatter vs frequency they will be. The wider the pulse the more signal energy but a faster frequency roll off. 0.08% gives an acceptable frequency roll off out to 10 KHz.

| The detailed settings for Channel A are as follows:
| Shape - Square
| Mode - SVMI
| VMIN = 1.3
| VMAX = 3.7 ( pulse amplitude set to allow some headroom for overshoot and ringing )
| Freq = 12.2
| Phase = 180 ( phase is set to 180 degrees to center the pulse in the time sample record )
| DutyCycle = 0.08 ( can be adjusted down to 0.012% for flatter input signal energy )

Channel B is set in Hi-Z mode as an input.

| Other Settings:
| FFT Window – Flat top ( has a wide FFT bandwidth which is wider than 12 Hz )
| FFT Samples = 8192
| Start Freq = 100 ( set to something other than 0, to ignore DC content )
| Stop Freq = 10000
| ZeroStuffing = 0 ( can be adjusted but generally has little effect on resultant plot )

Below in figure E2 is a screen shot for the bandpass RLC configuration of figure E11. The green trace for channel A is the narrow pulse forcing function response. The light and dark orange traces are the output responses seen by channel B for C1 = 0.47 uF and 1.0 uF respectively. The light and dark magenta traces are the subtraction of the Channel A trace ( in dBV ) and the Channel B trace ( in dBV ). As we know subtraction in dB ( logs ) is the same as division in magnitude. The magenta traces are the actual input to output transfer function of the RLC network. The Yellow trace is the phase response.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/band-pass-response.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E2, Bandpass response


Similarly in figure E3 is a screen shot for the bandstop RLC configuration of figure E11.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/band-stop-response.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure E3 Bandstop response


**For Further Reading:**

| https:*en.wikipedia.org/wiki/Fast_Fourier_transform
  http:*\ www.analog.com/media/en/training-seminars/design-handbooks/MixedSignal_Sect5.pdf
| https:*en.wikipedia.org/wiki/Window_function
  https:*\ en.wikipedia.org/wiki/Spectral_leakage
| http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html

Impedance Analyzer / LCR Meter
------------------------------

Background:
~~~~~~~~~~~

The basic concept that is used to make gain/phase, impedance and RLC measurements using ALICE Desktop is shown in figure 23. Channel A of the ALM1000 is used to apply a known frequency sine wave at VA and measure the applied voltage waveform. Channel B is used to measure the voltage waveform seen across the network under test. FFTs are calculated on the two waveforms which provide amplitude and phase information at the applied frequency. From these the relative gain ( CHB amplitude / CHA amplitude ) and relative phase ( CHB phase – CHA phase) are obtained. Further these values can be used to calculate the impedance (RLC) of the network in the dashed box.

The resistor, R\ :sub:`EXT`, is a known value. For the audio frequency range measurements possible with the ALM1000 hardware it can be adjusted as needed depending on the magnitude of the impedance being tested. Impedances in the range of about 0.1 to 10 times R\ :sub:`EXT` can be accurately measured. R\ :sub:`EXT` can range from 50 Ω to 50 KΩ.

The unknown impedance to be measured is modeled as a series circuit consisting of an unknown series resistance, R\ :sub:`X`, and an unknown series reactance, jX\ :sub:`X`. The magnitude of the impedance is Z\ :sub:`X`.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 16: Basic Concept


| Three voltages are measured:
| 1. VA is the applied voltage ( from Channel A of the ALM1000 ).
| 2. VZ is the voltage across the unknown impedance ( from Channel B of the ALM1000 ).
| 3. VI, the voltage across the known resistor R\ :sub:`EXT` is calculated from VA and VZ and is related to the current in both R\ :sub:`EXT` and the unknown impedance.

These three voltages are actually vectors and indicated in figure 24.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 17: Vector Diagram


Using the law of cosines and referring to figure 23 the magnitude of VI can be calculated as:

:math:`VI = sqrt(VA^2 + VZ^2 - 2 \times VA \times VZ \times cos(\theta))`

The angle Φ is the measured relative phase between channel B and channel A. The law of cosines is used to calculate the cosine of the angle, Θ.

:math:`cos(\theta) = (VA^2 + VI^2 - VZ^2)/ (2 \times VA \times VI)`

The magnitude of the total impedance (including R\ :sub:`EXT`) can be calculated as:

:math:`Za = R_EXT \times VA / VI`

We note from figure 1 that the sum of R\ :sub:`EXT` and R\ :sub:`X` can be found by:

:math:`R_EXT + R_X = Za \times cos(\theta)`

Thus, we can solve for R\ :sub:`X` by:

:math:`R_X = Za \times cos(\theta) - R_EXT`

Taking possible measurement errors into account it is possible that R\ :sub:`X` could compute to be a negative value which is not likely to be the case. The thing to do if that happens is to set R\ :sub:`X` to zero. The impedance is purely reactive.

The magnitude of the unknown impedance can be calculated as:

:math:`Z_X = R_EXT \times VZ / VI`

The magnitude of the unknown reactance can be calculated as:

:math:`\displaystyle X_X = sqrt(\frac{Z_X}{2} – \frac{R_X}{2})`

Again taking possible measurement errors into account it is possible that the square root of a negative number might occur. If that happens then X\ :sub:`X` should be set to zero.

Once we have a value for X\ :sub:`X`, we can calculate either the series capacitance ( when X\ :sub:`X` is negative = X\ :sub:`C` ) or series Inductance ( when X\ :sub:`X` is positive = X\ :sub:`L`).

:math:`C = -1/(2 \pi f X_C)`

:math:`L = X_L/(2 \pi f)`

Making Measurements:
~~~~~~~~~~~~~~~~~~~~

Connections to the ALM1000 and the network to be measured are shown in figure 18. In this case we show a simple series connected resistor and capacitor. R\ :sub:`EXT` is 1000 Ohms and the series resistor R\ :sub:`S` is 100 Ohms and the capacitor C\ :sub:`S` is 1 uF. The channel A AWG generator output should always be set to be in source voltage mode (SVMI) and with a sine wave shape. The user can control the output voltage amplitude and offset with the Min and Max entry slots as when using the scope and spectrum analyzer displays. A good place to start is with Min set to 1.086 and Max set to 3.914 which produces a 1 Vrms amplitude centered on 2.5 V DC. The Channel B analog input is set in the Hi-Z mode when using the Impedance Analyzer and it always considered as an input.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 18, Measurement setup


The current low level ALM1000 software only outputs signals as single shot bursts when the analog output signal is being sampled. The Sync AWG check box must be checked if you are using the ALM1000 function generator output as the applied signal source. If you are using an external signal source rather than CH A the box should not be checked. This will keep both channel A and B in a high impedance voltage measurement mode while capturing data.

Window Setup:
~~~~~~~~~~~~~

The main impedance analyzer window should appear, as in figure 19. It is sub divided into 2 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-window.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 19, ALICE Impedance Analyzer window


The Right Side Menu Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Run, Stop**

Start and stop buttons for continuously taking readings.

**Samples +/- buttons**

Used to change the number of samples in the FFT calculation. This number has to be a power of 2. More samples means a longer time sample which is important when low test frequencies are used. It also provides higher frequency resolution but a slower update rate for the screen. Fewer samples provides a lower frequency resolution, but a faster update rate for the screen. Increasing the zero-stuffing factor can improve the frequency resolution. The program starts up set to 16,384 samples.

**FFT window drop down menu**

Used to select an FFT window. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Flat Top window gives the highest amplitude accuracy but also has a large bandwidth, so less selectivity. Using the narrowest bandwidth FFT window and increasing the zero-stuffing factor can improve the measurement results. The program starts up set to the Nuttall window (BW=2.02).

\**File drop down menu \*\*

Save Config Load Config buttons. Commands for saving and loading the configuration settings to a file. (.cfg file)

Save V-Cal, Load V-Cal buttons. ALICE-VVM uses the same calibration file as the Voltmeter Tool. To load the saved calibration factors press the Load button. To save the calibration values to the file for future use, press the Save button. The values are saved to a file with a unique name for this particular ALM1000 board based on the first 9 characters of the board device ID serial number. For example something like: 203131543_V.cal.

Save Screen button. Command for saving the graphics display area to an encapsulated postscript file (.eps). The Help button will open a web browser to this document on the ADI Wiki site.

**Options drop down menu**

Cut-DC, an option that will remove the DC component from the sampled data record. It sample by sample subtracts the average value of the sample record. Any DC offset in the FFT could result in that being the peak amplitude and resulting in meaningless measurements. The program starts up with this turned on. This is important given the 0 to 5 V analog input range of the ALM1000 and the inherent 2.5 V DC offset.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/ia-options-drop-down.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 20, Impedance Analyzer Options Drop Down


The section along the right hand side contains the controls for making the measurements. There is a place to enter the external resistor value. The program starts up with this set to 1000. Next is a spin box to set the number of Ohms/div for the polar ( circular ) grid.

| M1K Analog Inputs
| ADALM1000 Low Capacitance FET Input Buffers
| M1K Breadboard Adapters

Main Graphics area
~~~~~~~~~~~~~~~~~~

The main graphics area is where the measured results are displayed. The impedance magnitude and angle along with the real and imaginary parts are drawn on the polar ( circular ) grid in Ohms. The real, series resistance component is drawn in green at 0 degrees phase. The imaginary part of the series impedance is drawn in red at either +90 degrees or -90 degrees depending on the sign. A positive impedance is inductive and an negative impedance is capacitive. The combined magnitude of the total series impedance is drawn in orange and at the measured angle.

To the left of the grid the relative gain of Channel B to Channel A is displayed in dB. Next the relative phase is displayed in degrees. Next the measured frequency in Hz is displayed. Next the measured Impedance Magnitude, Angle, R series and X series are displayed. Finally the calculated capacitance ( if X series is negative ) or inductance ( if X series is positive ) is displayed.

To convert the series values to the equivalent parallel values see section on Calculating Parallel Impedance further down in this document.

Additional setting information is also shown.

Impedance Analyzer Examples:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example 1:**

As an example to show the frequency dependent impedance of a series LC circuit we will use the ALICE impedance analyzer tool to examine the combination shown in figure E4 with L\ :sub:`1` equal to 6.5 mH and C\ :sub:`1` equal to 1 uF. We will use a 1000 Ω R\ :sub:`EXT` to be in line with the expected impedance level of the circuit.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fige1.png
   :align: center
   :width: 375px

.. container:: centeralign

   Figure E4 Testing an series LC circuit


The LC circuit is tested at three different frequencies, the first much lower than the resonate frequency where the impedance is dominated by the capacitor shown in figure E5.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-exp-1.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E5 Measured results at low frequency, 500 Hz


The second much higher than the resonate frequency where the impedance is dominated by the inductor shown in figure E6.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-exp-2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E6 Measured results at high frequency, 8500 Hz


The third at the resonate frequency where the negative impedance of the capacitor nearly cancels the positive impedance of the inductor shown in figure E7.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-exp-3.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E7 Measured results at resonate frequency, 2191 Hz


In these cases the series R measured stays nearly the same at about 11 Ω.

**Example 2:**

We can use ALICE Desktop to measure the input capacitance of channel B. We know that the input capacitance is small so we will need to use a large value for R\ :sub:`EXT` and measure at a high frequency. In figure E8 we show the connections used which is simply to connect CHA to CHB with a 47 KΩ resistor.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fige2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E8 Measure CH B input capacitance


In the ALICE Impedance Analyzer screen shot shown in figure E9 we see that Ext Res is set to 47000 and the test frequency is set to 19000 Hz. The calculated capacitance is 394 pF which agrees nicely with the capacitance reported in the document on the ALM1000 analog inputs.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-exp-4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E9, Measured results for CH B input capacitance


If we use the formula from Calculating Parallel Impedance to convert the series R to the parallel resistance we get around 1 MΩ. This is right in line with the known design value.

To measure capacitors around the same value as the input capacitance or even smaller it would be useful to null out this stray parasitic capacitance. This can be done using the Gain Cor and Phase Cor Entry widgets to enter correction factors for the gain and offset. If we enter 7.74 (dB) from the measured Gain for the Gain Cor entry and 65.35 (degrees) for the Phase Cor entry we get the result shown in figure E10.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-exp-5.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E10 Gain and Phase are corrected


Now the Measured Gain difference is -0.02 dB and the Measured Phase difference is -0.13 degrees. The calculated capacitance is 1.0pF. If we now add a 39 pF ceramic cap, from the Analog Parts Kit, from the channel B input to ground we get the results shown in figure E11.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-exp-6.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure E11, 39 pF cap added to CHB.


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

Impedance Sweeps:
~~~~~~~~~~~~~~~~~

The impedance Analyzer can be combined with the Bode plotter to perform sweeps of the network impedance. In this example we use the same parallel LC tank circuit with 50 ohms of series resistance added. We will do the same 100 Hz to 10 KHz sweep as before. Note: both the Bode and Impedance screens must be open and selected for this test.

From the Bode plot Curves Drop Down (Figure 14C) along with the CHB – CHA dB gain curve, under Impedance, the Series Mag and Series Ang are selected.

In the Impedance Analyzer Options Drop Down the Sweep On and Save Sweep options are selected. The external test resistance is the same 1000 ohms and the Ohms / Div is set to 100. When a sweep is run we get the following two plots in the Bode window, figure E12, and the Impedance Analyzer window figure E13.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-sweep-bode.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E12, Impedance vs log frequency sweep


The plot colors might be a little confusing in figure E12. The magenta curve is the same relative gain in dB from the earlier Bode plot example (CB dB – CA dB) and uses the green dB vertical scale. The purple and darkish green curves are the impedance magnitude in ohms and phase in degrees respectively and use the magenta ohms and cyan angle vertical scales respectively.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/impedance-sweep-polar.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E13, Polar plot of Impedance for frequency sweep


Frequency Analysis:
-------------------

The ALICE Desktop program uses the Fast Fourier Transform (FFT) to produce the frequency spectrum of a set of time samples of the input signals. The FFT takes as an input a set of time samples at a given sample rate and produces a set of frequency samples or values from DC ( 0 Hz ) to one half of the sampling frequency. In the case of the ALM1000 the sample rate is fixed at 100 KHz so the highest frequency will be one half of that or 50 KHz. The number of individual frequency bins the FFT produces is one half the number of time samples that are used. So the width of the bins or frequency resolution will be 50 KHz divided by one half the number of time samples taken. The number of time samples can be set from 64 ( 2\ :sup:`6` ) to 65536 ( 2\ :sup:`16` ) in the program.

What is an FFT window function?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ALICE Desktop you can choose from a number of FFT window functions. But what is an FFT window and what is it doing? The principle is very simple. The program reads a number of samples from the ALM1000 and puts them in an array. The size of the array has to be a power of 2 for the FFT calculation, for example 2048. With no window weighting function, all samples have an equal contribution or weight in the FFT calculation. You should expect to have an optimal result, but that is not the case if there is not an exact number of repeating cycles in the array. Another way of thinking about this is the starting value of the time waveform must be the same as the ending value. The end of the waveform will line up with the beginning if wrapped around on itself. This will almost never be the case in actual practice.

An FFT windowing function weights the samples from the beginning of the array to the end. With higher weights at the center and weights closer to zero near the start and end. The samples at the beginning and at the end of the array, that probably don’t line up, hardly contribute to the FFT calculation. Why would we use a only part of the samples or even not at all? There are even FFT window functions in which some sample points counteract with the other sample points.

The reason why we need an FFT window can be seen figures 8-15 in the various spectrums using different FFT window functions. No FFT window (also called a Rectangular window), generates many side bands in the spectrum of the FFT calculation. That is very visible in the first spectrum plot of the Rectangular ( dark orange ) and Cosine ( light orange ) window functions. Very low amplitude signals close to the main signal cannot be measured. So the dynamic range around the large main signal is low. By using an FFT window, the side bands are much more attenuated, how much depends on the type of FFT window. The increased side band suppression is at the expense of the selectivity. FFT windows with a very high side band suppression and therefore a very high dynamic range, have much less selectivity.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-cosine.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 8, Rectangular vs cosine window function


A Cosine window is a good compromise between a good selectivity and a good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-triangle.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 9, Rectangular vs Triangle window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-hann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 10, Rectangular vs Hann window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-blackmann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 11, Rectangular vs Blackman window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-nuttall.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 12, Rectangular vs Nuttall window function


At the expense of a little wider bandwidth the Nuttall window function provides the best side band reduction and may be the optimal compromise between good selectivity and good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-flattop.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 13, Rectangular vs Flat Top window function


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

   Figure 14, Fundamental frequency not centered, no zero stuffing


Zero stuffing provides a simple solution to this problem. For 1x Zero Stuffing, we double the size of the time sample array. The original array was say 2048 samples. We add 2048 samples with the value zero and we get a new array with 4096 samples. This may seem counterintuitive, when we add zero’s we do not add extra measurement data. However, something happens in the FFT calculation with twice as many samples. The effect can be seen in figure 22. Extra FFT frequency bins have been added. Coincidentally, here the extra frequency bin coincides with the frequency of the signal and the level of the signal is displayed correctly. Also even if the signal frequency does not coincide with the frequency of the extra FFT bin, the measured error will be smaller. As we add samples with the value zero, the bandwidth of the FFT filter remains the same.

.. image:: https://wiki.analog.com/_media/university/tools/zero-stuffing-2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 15, Fundamental frequency not centered, with zero stuffing


In the program, you can choose a value between 0 and 5 for the Zero Stuffing. As it is a power of 2, it is a value between 1 and 32. So 0x - 31x points will be added. As a result, the FFT calculation time will be up to 32x longer as well and the spectrum analyzer screen update rate will slow down considerably. One extra point (a value of 1 for the Zero Stuffing) is often good enough to keep the Scalloping loss acceptable. As an alternative, what you can do is set Zero Stuffing to 0, and use a Flat top window. The flat top is so wide, that even without Zero Stuffing, you will have little Scalloping loss, but you will have less frequency selectivity.

**For Further Reading:**

`Circuit measures capacitance or inductance <https://www.radiolocman.com/review/article.html?di=643359>`_

**Return to the** :doc:`ALICE Main Page </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`\ **.**
