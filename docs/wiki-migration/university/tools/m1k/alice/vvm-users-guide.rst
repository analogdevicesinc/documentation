ALICE Vector Voltmeter - Impedance Analyzer - RLC Meter:
========================================================

**This software uses an older version of libsmu / pysmu and is no longer recommended for use.**

:doc:`ALICE Desktop 1.1 </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` is now recommended.

Objective:
----------

This document serves as a User's Guide for the ALICE vector voltmeter, impedance analyzer, RLC meter software interface written for use with the ADALM1000 active learning kit hardware.

Required files:
---------------

The ALICE-VVM program is written in Python and requires version 2.7.8 or higher of Python be installed on the user's computer. The program only imports modules generally included with standard Python installation packages. The following additional files are required to run ALICE-VVM:

| All OS:
| alice-VVM-1.0.py(w)
| `alice-1.0.zip <https://wiki.analog.com/_media/university/tools/alice-1.0.zip>`_

| Windows:
| `libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`_ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`_ (needs to be in Python27\\DLLs directory)

Use of the :doc:`Windows installer </wiki-migration/university/tools/m1k/alice/install>` is highly recommended.

| Linux:
| `libpysmu.so <https://github.com/analogdevicesinc/libsmu>`_

| Required Python version:
| Python version 2.7.8 or higher

| Required external modules (site-packages for the correct Python version):
| NUMPY

Background:
-----------

The basic concept that is used to make gain/phase, impedance and RLC measurements using ALICE-VVM is shown in figure 1. Channel A of the ALM1000 is used to apply a known frequency sine wave at VA and measure the applied voltage waveform. Channel B is used to measure the voltage waveform seen across the network under test. FFTs are calculated on the two waveforms which provide amplitude and phase information at the applied frequency. From these the relative gain ( CHB amplitude / CHA amplitude ) and relative phase ( CHB phase - CHA phase) are obtained. Further these values can be used to calculate the impedance (RLC) of the network in the dashed box.

The resistor, R\ :sub:`EXT`, is a known value. For the audio frequency range measurements possible with the ALM1000 hardware it can be adjusted as needed depending on the magnitude of the impedance being tested. Impedances in the range of about 0.1 to 10 times R\ :sub:`EXT` can be accurately measured. R\ :sub:`EXT` can range from 50 Ω to 50 KΩ.

The unknown impedance to be measured is modeled as a series circuit consisting of an unknown series resistance, R\ :sub:`X`, and an unknown series reactance, jX\ :sub:`X`. The magnitude of the impedance is Z\ :sub:`X`.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1: Basic Concept


| Three voltages are measured:
| 1. VA is the applied voltage ( from Channel A of the ALM1000 ).
| 2. VZ is the voltage across the unknown impedance ( from Channel B of the ALM1000 ).
| 3. VI, the voltage across the known resistor R\ :sub:`EXT` is calculated from VA and VZ and is related to the current in both R\ :sub:`EXT` and the unknown impedance.

These three voltages are actually vectors and indicated in figure 2.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Vector Diagram


Using the law of cosines and referring to figure 2 the magnitude of VI can be calculated as:

:math:`VI = sqrtVA^2 + VZ^2 - 2 \times VA \times VZ \times cos(\phi)`

The angle Φ is the measured relative phase between channel B and channel A. The law of cosines is used to calculate the cosine of the angle, Θ.

:math:`cos(\Theta) = (VA^2 + VI^2 - VZ^2)/ (2 \times VA \times VI)`

The magnitude of the total impedance (including R\ :sub:`EXT`) can be calculated as:

:math:`Za = R_EXT \times VA / VI`

We note from figure 1 that the sum of R\ :sub:`EXT` and R\ :sub:`X` can be found by:

:math:`R_EXT + R_X = Za \times cos(\Theta)`

Thus, we can solve for R\ :sub:`X` by:

:math:`R_X = Za \times cos(\Theta) - R_EXT`

Taking possible measurement errors into account it is possible that R\ :sub:`X` could compute to be a negative value which is not likely to be the case. The thing to do if that happens is to set R\ :sub:`X` to zero. The impedance is purely reactive.

The magnitude of the unknown impedance can be calculated as:

:math:`Z_X = R_EXT \times VZ / VI`

The magnitude of the unknown reactance can be calculated as:

:math:`X_X = sqrtZ_X^2 - R_X^2`

Again taking possible measurement errors into account it is possible that the square root of a negative number might occur. If that happens then X\ :sub:`X` should be set to zero.

Once we have a value for X\ :sub:`X`, we can calculate either the series capacitance ( when X\ :sub:`X` is negative = X\ :sub:`C` ) or series Inductance ( when X\ :sub:`X` is positive = X\ :sub:`L`).

:math:`C = -1/(2 \pi f X_C)`

:math:`L = X_L/(2 \pi f)`

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`ADALM1000 Spectrum Analyzer User's Guide </wiki-migration/university/tools/m1k/alice/sa-users-guide>`
| :doc:`ADALM1000 Low Capacitance FET Input Buffers </wiki-migration/university/tools/m1k/fet-probes>`

Making Measurements:
--------------------

Connections to the ALM1000 and the network to be measured are shown in figure 3. In this case we show a simple series connected resistor and capacitor. R\ :sub:`EXT` is 1000 Ohms and the series resistor R\ :sub:`S` is 100 Ohms and the capacitor C\ :sub:`S` is 1 uF.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Measurement setup


Screen Setup:
-------------

Be sure that the ALM1000 is plugged into the USB port before starting the program. Once the program is running, the main screen should appear, as shown in figure 4. It is sub divided into 3 sections.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-screen-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 ALICE-VVM main screen


The menu buttons:
-----------------

The following sections cover the functions of the various menu buttons. All of the program controls can be found under the buttons, there are no scrollbars, or rotating knobs.

FFT window drop down menu
~~~~~~~~~~~~~~~~~~~~~~~~~

Used to select an FFT window. It is generally better not to select the "Rectangle window" or no window. This window has a poor dynamic range due to the high side bands that are generated with no weighting function in the FFT calculation. The Flat Top window gives the highest amplitude accuracy but also has a large bandwidth, so less selectivity. Using the narrowest bandwidth FFT window and increasing the zero-stuffing factor can improve the measurement results. The program starts up set to the Nuttall window (BW=2.02). ( See Appendix B)

Samples +/- buttons
~~~~~~~~~~~~~~~~~~~

Used to change the number of samples in the FFT calculation. This number has to be a power of 2. More samples means a longer time sample which is important when low test frequencies are used. It also provides higher frequency resolution but a slower update rate for the screen. Fewer samples provides a lower frequency resolution, but a faster update rate for the screen. Increasing the zero-stuffing factor can improve the frequency resolution. The program starts up set to 16,384 samples.

PWR-ON, Run, Stop, Exit
~~~~~~~~~~~~~~~~~~~~~~~

PWR-ON button to turn on and off the analog power supplies of the ALM1000. Start and stop buttons for continuously taking readings. Exit the program.

Main Graphics area
~~~~~~~~~~~~~~~~~~

The main graphics area is where the measured results are displayed. The impedance magnitude and angle along with the real and imaginary parts are drawn on the polar ( circular ) grid in Ohms. The real, series resistance component is drawn in green at 0 degrees phase. The imaginary part of the series impedance is drawn in red at either +90 degrees or -90 degrees depending on the sign. A positive impedance is inductive and an negative impedance is capacitive. The combined magnitude of the total series impedance is drawn in orange and at the measured angle.

To the right of the grid, the relative gain of Channel B to Channel A is displayed in dB. Next the relative phase is displayed in degrees. Next the measured frequency in Hz is displayed. Next the measured Impedance Magnitude, Angle, R series and X series are displayed. Finally the calculated capacitance ( if X series is negative ) or inductance ( if X series is positive ) is displayed.

To convert the series values to the equivalent parallel values see Appendix A. Other setting information is also shown.

The Right Side Menu Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Conn / Recon button is used to indicate that ALM1000 is connected when green and not connected when red. Pressing the red button after connecting a board will reconnect to the ALM1000.

File drop down menu
~~~~~~~~~~~~~~~~~~~

| Save Config Load Config buttons. Commands for saving and loading the configuration settings to a file. (.cfg file)
| Save V-Cal, Load V-Cal buttons. ALICE-VVM uses the same calibration file as the Voltmeter Tool. To load the saved calibration factors press the Load button. To save the calibration values to the file for future use, press the Save button. The values are saved to a file with a unique name for this particular ALM1000 board based on the first 9 characters of the board device ID serial number. For example something like: 203131543_V.cal.
| Save Screen button. Command for saving the graphics display area to an encapsulated postscript file (.eps).
| The Help button will open a web browser to this document on the ADI Wiki site.

Options drop down menu
~~~~~~~~~~~~~~~~~~~~~~

Cut-DC, an option that will remove the DC component from the sampled data record. It sample by sample subtracts the average value of the sample record. Any DC offset in the FFT could result in that being the peak amplitude and resulting in meaningless measurements. The program starts up with this turned on. This is important given the 0 to 5 V analog input range of the ALM1000 and the inherent 2.5 V DC offset. Zero Stuffing, you can input the desired Zero Stuffing factor (power of 2). The program starts up with this set to 1. (See Appendix B)

The section along the right hand side contains the controls for making the measurements. There is a place to enter the external resistor value. The program starts up with this set to 1000. Next is a spin box to set the number of Ohms/div for the polar ( circular ) grid.

Next are the controls for the channel A AWG generator output. The output of Channel A is hard coded to be in source voltage mode and with a sine wave shape. The user can control the output voltage amplitude and offset with the Min and Max entry slots as in the scope and spectrum analyzer software. The program starts up with Min set to 1.086 and Max set to 3.914 which produces a 1 Vrms amplitude centered on 2.5 V DC.

The Freq entry window programs the frequency of the waveform in Hertz. Given the 100KSPS maximum sample rate, the maximum allowed frequency is, by definition, 50 KHz but the practical upper limit is more like 20 KHz or less. The program starts up with the frequency set to 1000 Hz.

The Channel B analog input is hard coded in the Hi-Z mode and it always considered as an input.

The current low level ALM1000 software only outputs signals as single shot bursts when the analog output signal is being sampled. The Sync AWG check box must be checked if you are using the ALM1000 function generator output as the applied signal source. If you are using an external signal source rather than CH A the box should not be checked. This will keep both channel A and B in a high impedance voltage measurement mode while capturing data.

Extra stuff:
~~~~~~~~~~~~

The ALM1000 hardware provides four 3.3V CMOS digital input / output pins. At this time only static hi low functionality is supported. A simple interface is provided here. The D Inp line displays the current state of any of the four pins configured as input as either [0] or [1] one for each pin, PIO 0, PIO 1, PIO, 2 and PIO 3 from left to right and are updated once each time the analog scope display is refreshed. The D Out line consists of four single digit entry fields, one for each pin, PIO 0, PIO 1, PIO, 2 and PIO 3 from left to right. An 'x' in a given entry will configure the pin as input. A '0' or '1' will configure the pin as output and set it either low or high. All the pins are changed when Return ( Enter ) is typed in one of the entry fields. When a pin is configure as an Output its state will also appear in the D Input line but as a 0 or 1 without the enclosing [].

At the bottom of this section, just above the ADI logo, are entry windows which allow input gain and offset calibration to be added to the channel A and B inputs. For more on the use of input attenuators please refer to the following two documents:

| :doc:`M1K Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`M1K Breadboard Adapters </wiki-migration/university/tools/m1k/breadboard-adapter>`

Examples:
---------

Example 1:
~~~~~~~~~~

As an example to show the frequency dependent impedance of a series LC circuit we will use ALICE-VVM to examine the combination shown in figure E1 with L\ :sub:`1` equal to 60 mH and C\ :sub:`1` equal to 1 uF. We will use a 100 Ω R\ :sub:`EXT` to be in line with the expected impedance level of the circuit.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fige1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E1 Testing an series LC circuit


The LC circuit is tested at three different frequencies, the first much lower than the resonate frequency where the impedance is dominated by the capacitor shown in figure E2.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-screen-e1c.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E2 Measured results at low frequency, 200 Hz


The second much higher than the resonate frequency where the impedance is dominated by the inductor shown in figure E3.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-screen-e1i.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E3 Measured results at high frequency, 2500 Hz


The third at the resonate frequency where the negative impedance of the capacitor nearly cancels the positive impedance of the inductor shown in figure E4.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-screen-e1r.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E4 Measured results at resonate frequency, 644 Hz


In all three cases the series R measured stays nearly the same at about 155 Ω.

Example 2:
~~~~~~~~~~

We can use ALICE-VVM to measure the input capacitance of channel B. We know that the input capacitance is small so we will need to use a large value for R\ :sub:`EXT` and measure at a high frequency. In figure E5 we show the connections used which is simply to connect CHA to CHB with a 47 KΩ resistor.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-fige2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure E5 Measure CH B input capacitance


In the ALICE-VVM screen shot shown in figure E6 we see that Ext Res is set to 47000 and the test frequency is set to 19000 Hz. The calculated capacitance is 370 pF which agrees nicely with the capacitance reported in the document on the ALM1000 analog inputs.

.. image:: https://wiki.analog.com/_media/university/tools/alice-vvm-screen-e2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure E6, Measured results


If we use the formula from Appendix A to convert the series R ( 484 Ω ) to the parallel resistance we get around 1 MΩ. This is right in line with the known design value.

Appendix A, Parallel Impedance:
-------------------------------

The method used in ALICE-VVM determines the series resistance and reactance. Sometimes the equivalent parallel impedance of a resistance and reactance are needed. All that is required is a mathematical series to parallel conversion as follows. The concept is to relate the real and imaginary conductance of the parallel network to the conductance of the series network. The numerator and denominator of the series network conductance is multiplied by the complex conjugate of the denominator to put the result in normal form.

:math:`\displaystyle 1/R_P + 1/jX_P = 1/( R_S + jX_S) = \frac{R_S - jX_S}{ R_S^2 + X_S^2}`

where R\ :sub:`S` and X\ :sub:`S` are the series values and R\ :sub:`P` and X\ :sub:`P` are the parallel values.

By equating the real part we have the equivalent parallel resistance and by equating the imaginary part we have the equivalent parallel reactance:

:math:`R_P = (R_S^2 + X_S^2) / R_S`

:math:`X_P = (R_S^2 + X_S^2) / X_S`

Note that since the polarity of X\ :sub:`S` was known then the polarity of X\ :sub:`P` is also known and is the same sign.

Appendix B, Frequency Analysis:
-------------------------------

The ALICE-VVM program uses the Fast Fourier Transform (FFT) to produce the frequency spectrum of a set of time samples of the input signals. The FFT takes as an input a set of time samples at a given sample rate and produces a set of frequency samples or values from DC ( 0 Hz ) to one half of the sampling frequency. In the case of the ALM1000 the sample rate is fixed at 100 KHz so the highest frequency will be one half of that or 50 KHz. The number of individual frequency bins the FFT produces is one half the number of time samples that are used. So the width of the bins or frequency resolution will be 50 KHz divided by one half the number of time samples taken. The number of time samples can be set from 64 ( 2\ :sup:`6` ) to 65536 ( 2\ :sup:`16` ) in the program.

What is an FFT window function?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ALICE-SA you can choose from a number of FFT window functions. But what is an FFT window and what is it doing? The principle is very simple. The program reads a number of samples from the ALM1000 and puts them in an array. The size of the array has to be a power of 2 for the FFT calculation, for example 2048. With no window weighting function, all samples have an equal contribution or weight in the FFT calculation. You should expect to have an optimal result, but that is not the case if there is not an exact number of repeating cycles in the array. Another way of thinking about this is the starting value of the time waveform must be the same as the ending value. The end of the waveform will line up with the beginning if wrapped around on itself. This will almost never be the case in actual practice.

An FFT windowing function weights the samples from the beginning of the array to the end. With higher weights at the center and weights closer to zero near the start and end. The samples at the beginning and at the end of the array, that probably don't line up, hardly contribute to the FFT calculation. Why would we use a only part of the samples or even not at all? There are even FFT window functions in which some sample points counteract with the other sample points.

The reason why we need an FFT window can be seen figures B1-6 in the various spectrums using different FFT window functions. No FFT window (also called a Rectangular window), generates many side bands in the spectrum of the FFT calculation. That is very visible in the first spectrum plot of the Rectangular ( dark orange ) and Cosine ( light orange ) window functions. Very low amplitude signals close to the main signal cannot be measured. So the dynamic range around the large main signal is low. By using an FFT window, the side bands are much more attenuated, how much depends on the type of FFT window. The increased side band suppression is at the expense of the selectivity. FFT windows with a very high side band suppression and therefore a very high dynamic range, have much less selectivity.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-cosine.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B1 Rectangular vs cosine window function


A Cosine window is a good compromise between a good selectivity and a good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-triangle.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B2 Rectangular vs Triangle window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-hann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B3 Rectangular vs Hann window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-blackmann.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B4 Rectangular vs Blackman window function


.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-nuttall.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B5 Rectangular vs Nuttall window function


At the expense of a little wider bandwidth the Nuttall window function provides the best side band reduction and may be the optimal compromise between good selectivity and good dynamic range.

.. image:: https://wiki.analog.com/_media/university/tools/rect-win-vs-flattop.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B6 Rectangular vs Flat Top window function


A special filter is the Flat Top filter. It has a flat top as the name implies. That is why it is very usable for accurate amplitude measurements. The peak of the signal does not have to be exactly on the center of an FFT frequency bin.

ALICE-VVM has 7 built in windowing functions.

| Rectangular, no window function B=1
| Cosine window function, medium-dynamic range B=1.24
| Triangular non-zero endpoints, medium-dynamic range B=1.33
| Hann window function, medium-dynamic range B=1.5
| Blackman window, continuous first derivate function, medium-dynamic range B=1.73
| Nuttall window, continuous first derivate function, high-dynamic range B=2.02
| Flat top window, medium-dynamic range, extra wide bandwidth B=3.77

Zero Stuffing
~~~~~~~~~~~~~

With the menu button "Setup" you can set the factor for the Zero stuffing. What problem are trying to solve by Zero stuffing? The bandwidth of the FFT depends on the choice of the FFT window function. For a narrow FFT filter, the bandwidth is slightly larger than the difference between 2 FFT frequency bins. When the signal frequency is exactly between the 2 FFT frequency bins, the signal will be displayed lower than its actual value because half of the signal appears in each of the two bins. Figure B7 shows good example of this. The signal is slightly more than 1 KHz and lies exactly between the two FFT frequency bins. The actual peak value should be equal to 0 dB, but the displayed value of the two adjacent samples is lower. The signal level is not displayed correctly by either of the FFT frequency bins. This is called Scalloping loss.

.. image:: https://wiki.analog.com/_media/university/tools/no-zero-stuffing.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B7, Fundamental frequency not centered, no zero stuffing


Zero stuffing provides a simple solution to this problem. For 1x Zero Stuffing, we double the size of the time sample array. The original array was say 2048 samples. We add 2048 samples with the value zero and we get a new array with 4096 samples. This may seem counterintuitive, when we add zero's we do not add extra measurement data. However, something happens in the FFT calculation with twice as many samples. The effect can be seen in figure B8. Extra FFT frequency bins have been added. Coincidentally, here the extra frequency bin coincides with the frequency of the signal and the level of the signal is displayed correctly. Also even if the signal frequency does not coincide with the frequency of the extra FFT bin, the measured error will be smaller. As we add samples with the value zero, the bandwidth of the FFT filter remains the same.

.. image:: https://wiki.analog.com/_media/university/tools/zero-stuffing-2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure B8, Fundamental frequency not centered, with zero stuffing


In the program, you can choose a value between 0 and 5 for the Zero Stuffing. As it is a power of 2, it is a value between 1 and 32. So 0x - 31x points will be added. As a result, the FFT calculation time will be up to 32x longer as well and the spectrum analyzer screen update rate will slow down considerably. One extra point (a value of 1 for the Zero Stuffing) is often good enough to keep the Scalloping loss acceptable. As an alternative, what you can do is set Zero Stuffing to 0, and use a Flat top window. The flat top is so wide, that even without Zero Stuffing, you will have little Scalloping loss, but you will have less frequency selectivity.

**For Further Reading:**

| https:*en.wikipedia.org/wiki/Fast_Fourier_transform
  http:*\ www.analog.com/media/en/training-seminars/design-handbooks/MixedSignal_Sect5.pdf
| https://en.wikipedia.org/wiki/Window_function
| http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html

**Return to the** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
