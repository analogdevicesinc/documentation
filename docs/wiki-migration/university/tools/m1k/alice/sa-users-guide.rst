ALICE Spectrum Analyzer:
========================

**This software uses an older version of libsmu / pysmu and is no longer recommended for use.**

:doc:`ALICE Desktop 1.1 </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` is now recommended.

Objective:
----------

This document serves as a User's Guide for the ALICE spectrum analyzer software interface written for use with the ADALM1000 active learning kit hardware.

Required files:
---------------

The ALICE-SA program is written in Python and requires version 2.7.8 of Python be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run ALICE-SA:

| All OS:
| alice-SA-1.0.py(w)
| `alice-1.0.zip <https://wiki.analog.com/_media/university/tools/alice-1.0.zip>`__

| Windows:
| `libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`__ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`__ (needs to be in Python27\\DLLs directory)

Use of the :doc:`Windows installer </wiki-migration/university/tools/m1k/alice/install>` is highly recommended.

| Linux:
| `libpysmu.so <https://github.com/analogdevicesinc/libsmu>`__

| Required Python version:
| Python version 2.7.8 or higher

| Required external modules (site-packages for the correct Python version):
| NUMPY

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`ADALM1000 Low Capacitance FET Input Buffers </wiki-migration/university/tools/m1k/fet-probes>`

Screen Setup:
-------------

Be sure that the ALM1000 is plugged into the USB port before starting the program. Once the program is running, the main screen should appear, as shown in figure 1. It is sub divided into 4 sections.

.. image:: https://wiki.analog.com/_media/university/tools/alice_sa_window_shot.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 1 ALICE-SA main screen


The menu buttons:
-----------------

The following sections cover the functions of the various menu buttons. All of the program controls can be found under the buttons, there are no scroll bars, or rotating knobs.

Mode drop down menu
~~~~~~~~~~~~~~~~~~~

In Normal mode the trace is continuously refreshed.

In Peak hold, the peak or maximum value for each frequency bin is remembered. For each sweep if the new value is higher, then that new data point of the trace is saved and displayed.

In Average mode, the trace values are averaged. This smooths out the randomness in the noise floor.

In Single Shot mode a single sweep is obtained each time the Run button is pressed.

FFT window drop down menu
~~~~~~~~~~~~~~~~~~~~~~~~~

Used to select an FFT window. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Flat Top window gives the highest amplitude accuracy but also has a large bandwidth, so less selectivity.

Samples +/- buttons
~~~~~~~~~~~~~~~~~~~

Used to change the number of samples in the FFT calculation. This number has to be a power of 2. More samples provides higher frequency resolution but a slower update rate for the screen. Fewer samples provides a lower frequency resolution, but a faster update rate for the screen.

Curves drop down menu
~~~~~~~~~~~~~~~~~~~~~

The Curves button allows the selection of which signal waveforms will be displayed. The All button selects all four curves to be displayed and the None button clears all four curves. The Marker option turns on a text marker which displays the amplitude and frequency at the peak of the displayed signal. Options to display the difference ( subtraction ) of the CA-dBV – CB-dBV traces or the CB-dBV – CA-dBV traces. It is also possible to select which of the possible stored reference traces, if saved via the Store trace option, will be displayed.

The color of the CA-dBV and CB-dBV traces will turn red if the input signal goes beyond the 0 to +5 V analog input signal range.

PWR-ON
~~~~~~

The green PWR-On button toggles on and off the fixed analog +2.5 V and +5 V power supplies. The button turns red when the supplies are off. The power supplies do not turn completely off but go to around +2 V and can supply only about 20 mA when shorted to ground. This is much less than the 200 mA or so they could supply if accidentally shorted when on. It is good practice to turn off the supplies ( or better yet disconnect ) when making any modifications to the circuit under test.

Run, Stop, Exit
~~~~~~~~~~~~~~~

Start and stop buttons for the sweep. Exit the program

File drop down menu
~~~~~~~~~~~~~~~~~~~

| Save Config
| Load Config, commands for saving and loading configuration settings (.cfg file)
| Save Screen, command for saving the graphics display area to an encapsulated postscript file (.eps)
| Save Data, command for saving the captured channel A and B amplitude vs frequency data to a coma separated values file (.csv). The amplitude data can be saved as magnitude in Vrms ( type a 0 ) or in dBV ( type a 1 ).

Options drop down menu
~~~~~~~~~~~~~~~~~~~~~~

Smooth, an option to enabling smoothing where spline curves are used to connect the FFT frequency points rather than the default straight lines.

Cut-DC, an option that will remove the DC component from the sampled data record. It element by element subtracts the average value of the sample record.

Store trace, no explanation required, you can store a reference trace with it.

Screen setup, to select the number of vertical divisions on the grid. Also for selecting smaller grids. Can be handy when you want to capture smaller spectrum analyzer bit map pictures for documentation or a website.

Setup, in the setup menu, you can input the desired Zero Stuffing factor (power of 2).

Startfreq and Stopfreq
~~~~~~~~~~~~~~~~~~~~~~

Used to set the start and stop frequency of the display.

LVL +/- buttons
~~~~~~~~~~~~~~~

Used to set the level of the top line of the grid or the "sensitivity". 0 dB is equal to an input amplitude of 1 V rms.

dB/div +/- buttons
~~~~~~~~~~~~~~~~~~

Used to set the dB's per division. Can be 1, 2, 3, 5, 10, 15, or 20 dB/Div.

The Right Side Menu Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The section along the right hand side, mostly contains the controls for the two AWG generator outputs.

There are two identical sets of controls for configuring the Channel A and B outputs. First there is a drop down menu for selecting the Mode. The SVMI option is for sourcing voltage / measure current. The SIMV option is for sourcing current / measure voltage. The Hi-Z option disables the generator output (High Impedance mode). The Split I/O option separates the generator output signal from the voltage measurement input. In the Rev D version of ALM1000 only the source current function operates when the output and input are on separate pins so the Split I/O option automatically puts the hardware into the source current configuration. To turn the sourced current into a voltage the output termination options can be used. The hardware includes two 50 Ohm resistors that can be connected to the generator output pin. One resistor is tied to ground and the other is tied to the 2.5 V power supply. The drop down menu provides three options Open, To GND, and To 2.5V.

The Shape drop down menu is used to select the shape of the output waveform. When DC is selected the constant value of the output voltage or current is set by the value in the Max entry window.

The Min and Max entry windows program the minimum and maximum values for the output waveform. When in the voltage mode the values are in Volts, when in current mode the values are in mAmps. If the value entered in the Min window is higher ( more positive ) than the value entered in the Max window the apparent phase of the output wave is inverted. While this is somewhat redundant for the Sine, Triangle and Square wave shapes, given the Phase control described later, it is useful for determining if the Sawtooth or Stairstep shapes are rising or falling ramps.

The Freq entry window programs the frequency of the waveform in Hertz. Given the 100KSPS maximum sample rate, the maximum allowed frequency is, by definition, 50 KHz but the practical upper limit is more like 20 KHz or less.

The Phase entry window programs the relative phase of the output waveform in degrees from 0 to 360. The % entry window only applies to the Square shape and programs the duty cycle in percent from 0% to 100%.

The current low level ALM1000 software only outputs signals as single shot bursts when the analog signals ( voltage and current ) are being sampled. The Sync AWG check box must be checked if you want to produce outputs in sync with the analog trace sweeps. If you are in Hi-Z mode for both CH A and CH B and are using the ALM as just a 2 input spectrum analyzer the box should not be checked.

The Sweep Gen drop down menu provides controls for generating frequency sweeps of the analog output sources. The screen traces are up-dated after each frequency step. It is best to select Peek Hold mode to display the amplitude response vs frequency. First is a radio button to select which output channel, or none will be swept. The selected output will be swept from the display Start Frequency to the Stop Frequency. The number of steps can be set using the Sweep Steps button. Lastly, there is a radio button selector for single or continuous sweep. The frequency sweep is started, or restarted from the beginning each time the Run button is pressed.

The ALM hardware provides four 3.3V CMOS digital input / output pins. At this time only static hi low functionality is supported. A simple interface is provided here. The D Inp line displays the current state of any of the four pins configured as input as either [0] or [1] one for each pin, PIO 0, PIO 1, PIO, 2 and PIO 3 from left to right and are updated once each time the analog scope display is refreshed. The D Out line consists of four single digit entry fields, one for each pin, PIO 0, PIO 1, PIO, 2 and PIO 3 from left to right. An 'x' in a given entry will configure the pin as input. A '0' or '1' will configure the pin as output and set it either low or high. All the pins are changed when Return ( Enter ) is typed in one of the entry fields. When a pin is configure as an Output its state will also appear in the D Input line but as a 0 or 1 without the enclosing [].

At the bottom of this section, just above the ADI logo, are entry windows which allow input gain and offset correction for any external resistor divider attenuator networks that might be added to the channel A and B inputs ( possibly used when in the high impedance or Split I/O modes ). For more on the use of input attenuators please refer to the following two documents:

| :doc:`M1K Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`M1K Breadboard Adapters </wiki-migration/university/tools/m1k/breadboard-adapter>`

Frequency Analysis:
-------------------

The ALICE-SA program uses the Fast Fourier Transform (FFT) to produce the frequency spectrum of a set of time samples of the input signals. The FFT takes as an input a set of time samples at a given sample rate and produces a set of frequency samples or values from DC ( 0 Hz ) to one half of the sampling frequency. In the case of the ALM1000 the sample rate is fixed at 100 KHz so the highest frequency will be one half of that or 50 KHz. The number of individual frequency bins the FFT produces is one half the number of time samples that are used. So the width of the bins or frequency resolution will be 50 KHz divided by one half the number of time samples taken. The number of time samples can be set from 64 ( 2\ :sup:`6` ) to 65536 ( 2\ :sup:`16` ) in the program.

What is an FFT window function?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ALICE-SA you can choose from a number of FFT window functions. But what is an FFT window and what is it doing? The principle is very simple. The program reads a number of samples from the ALM1000 and puts them in an array. The size of the array has to be a power of 2 for the FFT calculation, for example 2048. With no window weighting function, all samples have an equal contribution or weight in the FFT calculation. You should expect to have an optimal result, but that is not the case if there is not an exact number of repeating cycles in the array. Another way of thinking about this is the starting value of the time waveform must be the same as the ending value. The end of the waveform will line up with the beginning if wrapped around on itself. This will almost never be the case in actual practice.

An FFT windowing function weights the samples from the beginning of the array to the end. With higher weights at the center and weights closer to zero near the start and end. The samples at the beginning and at the end of the array, that probably don't line up, hardly contribute to the FFT calculation. Why would we use a only part of the samples or even not at all? There are even FFT window functions in which some sample points counteract with the other sample points.

The reason why we need an FFT window can be seen figures 2-7 in the various spectrums using different FFT window functions. No FFT window (also called a Rectangular window), generates many side bands in the spectrum of the FFT calculation. That is very visible in the first spectrum plot of the Rectangular ( dark orange ) and Cosine ( light orange ) window functions. Very low amplitude signals close to the main signal cannot be measured. So the dynamic range around the large main signal is low. By using an FFT window, the side bands are much more attenuated, how much depends on the type of FFT window. The increased side band suppression is at the expense of the selectivity. FFT windows with a very high side band suppression and therefore a very high dynamic range, have much less selectivity.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-cosine.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 Rectangular vs cosine window function


A Cosine window is a good compromise between a good selectivity and a good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-triangle.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 Rectangular vs Triangle window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-hann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4 Rectangular vs Hann window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-blackmann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5 Rectangular vs Blackman window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-nuttall.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 6 Rectangular vs Nuttall window function


At the expense of a little wider bandwidth the Nuttall window function provides the best side band reduction and may be the optimal compromise between good selectivity and good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-flattop.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 7 Rectangular vs Flat Top window function


A special filter is the Flat Top filter. It has a flat top as the name implies. That is why it is very usable for accurate amplitude measurements. The peak of the signal does not have to be exactly on the center of an FFT frequency bin.

ALICE-SA has 7 built in windowing functions.

| Rectangular, no window function B=1
| Cosine window function, medium-dynamic range B=1.24
| Triangular non-zero endpoints, medium-dynamic range B=1.33
| Hann window function, medium-dynamic range B=1.5
| Blackman window, continuous first derivate function, medium-dynamic range B=1.73
| Nuttall window, continuous first derivate function, high-dynamic range B=2.02
| Flat top window, medium-dynamic range, extra wide bandwidth B=3.77

Zero Stuffing
~~~~~~~~~~~~~

With the menu button "Setup" you can set the factor for the Zero stuffing. What problem are trying to solve by Zero stuffing? The bandwidth of the FFT depends on the choice of the FFT window function. For a narrow FFT filter, the bandwidth is slightly larger than the difference between 2 FFT frequency bins. When the signal frequency is exactly between the 2 FFT frequency bins, the signal will be displayed lower than its actual value because half of the signal appears in each of the two bins. Figure 8 shows good example of this. The signal is slightly more than 1 KHz and lies exactly between the two FFT frequency bins. The actual peak value should be equal to 0 dB, but the displayed value of the two adjacent samples is lower. The signal level is not displayed correctly by either of the FFT frequency bins. This is called Scalloping loss.

.. image:: https://wiki.analog.com/_media/university/tools/no-zero-stuffing.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 8, Fundamental frequency not centered, no zero stuffing


Zero stuffing provides a simple solution to this problem. For 1x Zero Stuffing, we double the size of the time sample array. The original array was say 2048 samples. We add 2048 samples with the value zero and we get a new array with 4096 samples. This may seem counterintuitive, when we add zero's we do not add extra measurement data. However, something happens in the FFT calculation with twice as many samples. The effect can be seen in figure 9. Extra FFT frequency bins have been added. Coincidentally, here the extra frequency bin coincides with the frequency of the signal and the level of the signal is displayed correctly. Also even if the signal frequency does not coincide with the frequency of the extra FFT bin, the measured error will be smaller. As we add samples with the value zero, the bandwidth of the FFT filter remains the same.

.. image:: https://wiki.analog.com/_media/university/tools/zero-stuffing-2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 9, Fundamental frequency not centered, with zero stuffing


In the program, you can choose a value between 0 and 5 for the Zero Stuffing. As it is a power of 2, it is a value between 1 and 32. So 0x - 31x points will be added. As a result, the FFT calculation time will be up to 32x longer as well and the spectrum analyzer screen update rate will slow down considerably. One extra point (a value of 1 for the Zero Stuffing) is often good enough to keep the Scalloping loss acceptable. As an alternative, what you can do is set Zero Stuffing to 0, and use a Flat top window. The flat top is so wide, that even without Zero Stuffing, you will have little Scalloping loss, but you will have less frequency selectivity.

Examples:
---------

The following example shows a technique where ALICE-SA can be used to measure the amplitude vs frequency response of two simple RLC configurations. Shown in figure E1, first on the left is a parallel LC bandpass configuration and second on the right is a series LC bandstop configuration. Indicated by the green boxes are the connections to the ALM1000. Channel B is setup to output the driving function of the network. Channel A is setup as an input to measure the response seen across the LC network. For this example R\ :sub:`1` is 1 KΩ, L\ :sub:`1` is 15 mH and C\ :sub:`1` is either 0.2 uF or 0.5 uF.

.. image:: https://wiki.analog.com/_media/university/tools/alice-sa-fig-e1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E1 RLC circuits


In a linear system, the frequency response can be obtained by sweeping sinusoidal inputs over a range of frequencies. This series of sinusoidal signals at different frequencies can then be used to compute the frequency response. While ALICE-SA does include a sweep generator function, a sweep with many frequency points using large FFT sample sizes can take many seconds or even minutes to up-date the plot. However, FFT analysis can be used to obtain the transfer function for a network from its impulse response. We can generate a test signal with a wide frequency content, a very narrow square pulse, which will produce a plot from a single sample record at a much higher up-date rate.

**Using the FFT to get a transfer function of a system is not overly complex.**

There must be an input to the network which you can observe and record. There must be an output from the network which you can observe and record. The input and output data has to be able to be read into an analysis program, such as ALICE-SA, that can take the Fast Fourier Transform of both input and output data records. A basic concept of linear analysis is that the unit impulse response of a network and the transfer function of the network are a Laplace transform pair, or said another way, the transfer function is the Laplace transform of the unit impulse response. The implication is that we can obtain the transfer function by getting the Laplace transform of the unit impulse response.

**Practical implementation.**

If we set the number of FFT samples to 8192 the total sample time will be 81.92 mSec which is the same as one cycle at 12.2 Hz. By setting the Channel B function generator to a 12.2 Hz square wave with a very narrow duty cycle of only 4 – 6 samples wide the resulting test signal will contain frequency content every 12.2 Hz with nearly equal amplitude out to high frequencies. At 12 Hz each 10 uSec sample period is equal to about 0.012 % of duty cycle. We can set the duty cycle to anything from 0.012% to 0.08% and get similar results. The only difference is how fast the signal level falls off with increasing frequency. For a given pulse amplitude, the narrower the pulse the less energy in each 12.2 Hz spaced frequency but the flatter vs frequency they will be. The wider the pulse the more signal energy but a faster frequency roll off. 0.08% gives an acceptable frequency roll off out to 10 KHz.

| The detailed settings for Channel B are as follows:
| Shape - Square
| Mode - SVMI
| VMIN = 1.3
| VMAX = 3.7 ( pulse amplitude set to allow some headroom for overshoot and ringing )
| Freq = 12.2
| Phase = 180 ( phase is set to 180 degrees to center the pulse in the time sample record )
| DutyCycle = 0.08 ( can be adjusted down to 0.012% for flatter input signal energy )

Channel A is set in Hi-Z mode as an input.

| Other Settings:
| FFT Window – Flat top ( has a wide FFT bandwidth which is wider than 12 Hz )
| FFT Samples = 8192
| Start Freq = 100 ( set to something other than 0, to ignore DC content )
| Stop Freq = 10000
| ZeroStuffing = 0 ( can be adjusted but generally has little effect on resultant plot )

Below in figure E2 is a screen shot for the bandpass RLC configuration of figure E1. The orange trace for channel B is the narrow pulse forcing function response. The light and dark green traces are the output responses seen by channel A for C\ :sub:`1` = 0.5 uf and 0.2uF respectively. The light and dark magenta traces are the subtraction of the Channel A trace ( in dBV ) and the Channel B trace ( in dBV ). As we know subtraction in dB ( logs ) is the same as division in magnitude. The magenta traces are the actual input to output transfer function of the RLC network.

.. image:: https://wiki.analog.com/_media/university/tools/bandpass-freq-resp.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E2, Bandpass response


Similarly in figure E3 is a screen shot for the bandstop RLC configuration of figure E1.

.. image:: https://wiki.analog.com/_media/university/tools/bandstop-freq-resp.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E3 Bandstop response


**For Further Reading:**

| https:*en.wikipedia.org/wiki/Fast_Fourier_transform
  http:*\ www.analog.com/media/en/training-seminars/design-handbooks/MixedSignal_Sect5.pdf
| https:*en.wikipedia.org/wiki/Window_function
  https:*\ en.wikipedia.org/wiki/Spectral_leakage
| http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html

**Return to the** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
