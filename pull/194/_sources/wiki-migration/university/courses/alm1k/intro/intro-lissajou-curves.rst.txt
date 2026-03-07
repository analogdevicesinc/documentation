Activity: The Lissajous pattern, A Classic phase measurement
============================================================

Objective:
----------

All periodic signals can be described in terms of amplitude and phase. To perform amplitude, frequency, and phase measurements using an oscilloscope and to make use of Lissajous figures for phase and frequency measurements.

We all learn that in basic circuit theory classes. You surely have needed to calculate a signal's phase change when it passes through a circuit. Fortunately, you can measure phase on the lab bench with oscilloscope hardware such as the ADALM1000 and its accompanying ALICE desktop software using several methods.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background: Lissajous Figures
-----------------------------

Lissajous (pronounced LEE-suh-zhoo) figures were discovered by the French physicist Jules Antoine Lissajous. He would use sounds of different frequencies to vibrate a mirror. A beam of light reflected from the mirror would trace patterns which depended on the frequencies of the sounds. Lissajous' setup was similar to the apparatus which is used today to project laser light shows.

Before the days of digital frequency meters and phase-locked loops, Lissajous figures were used to determine the frequencies of sounds or radio signals. A signal of known frequency was applied to the horizontal axis of an oscilloscope, and the signal to be measured was applied to the vertical axis. The resulting pattern was a function of the ratio of the two frequencies.

Lissajous figures often appeared as props in science fiction movies made during the 1950's. One of the best examples can be found in the opening sequence of The Outer Limits TV series. ("Do not attempt to adjust your picture--we are controlling the transmission.") The pattern of criss-cross lines is actually a Lissajous figure.

The phase difference, or phase angle, is the difference in phase between the same points, say a zero crossing, in two different waveforms with the same frequency. A common example is the phase difference between the input signal and output signal after it passes through a circuit, cable, or PC board trace. A waveform with a leading phase has a specific point occurring earlier in time than the same point on the other signal. That would be the case of when a signal passes through, a capacitor: the current in the capacitor will lead the voltage across the capacitor by 90º. Conversely, a waveform with lagging phase has a specific point occurring later in time than the other paired signal waveform. Two signals are in opposition if they are 180º out of phase. Signals that differ in phase by ±90º are in phase quadrature (one quarter of 360º).

The time (phase) relationship between two sine waves can of course be measured from a time domain plot such as figure 1. The Time measurement capabilities of most any Oscilloscope, the ADALM1000 and the ALICE software included, can display the relative phase between channel A and channel B in degrees and/or the time delay between A and B. The software scans the waveforms looking for the time points where they cross their average value (zero crossing with DC offset removed). It then uses those time points to report frequency, period, phase, delay, duty-cycle etc. Noise and jitter will introduce errors in the results.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/into-lissajou-curves-f1.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 1, Time plot of two sine waves.


Old timers who have started out their careers using an analog oscilloscope probably remember using the classic Lissajous pattern to measure the phase difference of two sine waves. It can be measured by cross plotting the two sine waveforms on the X-Y display in ALICE as shown in Figure 2. In this figure, the voltage waveform on channel A provides the horizontal or X displacement. Channel B provides the vertical or Y deflection. The Lissajous pattern indicates the phase difference by the shape of the X-Y plot. A straight line indicates a 0º or 180º phase difference. The angle of the line depends on the difference in amplitude between the two signals, a line at 45º to the horizontal means the amplitudes are equal. While a circle indicates a 90º difference. It will only be a true circle if the amplitudes are equal. Phase differences between 0º and 90º appear as tilted ellipses and phase is determined by measuring the maximum vertical deflection (Ymax) and the vertical deflection at zero horizontal deflection (Yx=0). In Figure 2, cursors mark these two locations on the X-Y plot. Note that this is only valid if the X-Y plot is centered on 0,0. Any DC offset in the two waveforms must be removed first.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/into-lissajou-curves-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Using a classic Lissajous display lets you measure the phase difference between two sine waves.


Marker readouts in upper left of the plot show the required values for computing the phase difference.

Φ2 - Φ1 = ± sin\ :sup:`−1` (Yx=0/Ymax) for when the top of the ellipse is located in quadrant 1 (Q1)

Φ2 - Φ1 = ± 180-sin\ :sup:`−1` (Yx=0/Ymax) for when the top of the ellipse is located in quadrant 2 (Q2)

The sign of the phase difference is determined by inspecting the channel time traces.

| In the figure 2 example, the Ymax value is 1.538, YX=0 is 1.064, and the top of the ellipse is in Q1:
| Φ2 - Φ1 = ± sin\ :sup:`−1` (1.064/1.538) = ± sin\ :sup:`−1` (0.692) = 44º

The accuracy of this method is dependent on the placement of the cursors but it produces reasonable results with certain artistic panache.

Hardware like the ADALM1000 and ALICE desktop software offer multiple techniques to measure phase. Direct measurement in the time domain supports both static and dynamic measurements of phase. Frequency domain based calculation provides somewhat more accurate results for static phase measurements but requires you to take the difference of the FFT phase data at the fundamental frequency.

Experiment
----------

| **Materials:**
| ADALM1000 hardware module

Create a Lissajous Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~

The default function of an oscilloscope is to display voltage signals on the Y axis vs time on the X axis. The ALICE software has a special function that allows the user to plot one signal on the X axis and the other on the Y axis.

Begin with both AWG generators set for 1.0 Min and 4.0 Max values and a frequency of 1 kHz. Use the Time display to ensure that both waveform generators are producing the same signal.

You should see two nearly identical sine waves, both in phase with the other. Remember that the sine wave is defined by three parameters – amplitude, frequency and phase. Check to see that the vertical range and position settings for both channels are the same. (Use the V/Div to adjust this if needed.) If the amplitudes are not the same, the sine waves will not be the same amplitude. If the phases are not the same, the sine waves will not line up horizontally. If the frequencies are not the same, the wave the oscilloscope is triggered on will be stationary, while the other wave will move (slowly we hope) to the left or right. Figure 3 shows signals that have different amplitude and frequency (and DC offset).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/into-lissajou-curves-f3.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 3, Two sine waves that vary in amplitude and frequency.


We can now generate a Lissajous pattern by opening the X-Y Plotter tool. Select CA-V for the X Axis and CB-V for the Y Axis. Compare what you see to the examples of Lissajous figures. Use your favorite screen capture software tool to take a picture of the image and save it. Your TA or instructor can help you with this. Include this picture with your report. [Hint: Use the STOP button to freeze your figure at the point you want to take a picture.]

You should now play with the AWG settings and produce several other representative patterns. Create one pattern that you find particularly interesting. Take a picture of it with the screen capture software.

Subtracting two Signals
~~~~~~~~~~~~~~~~~~~~~~~

Next, we will do a different kind of comparison of the two sine waves, one that will prove to be very important in the development of measurement techniques. In this measurement, we will compare two signals to see how close they are to one another by subtracting one from the other.

Go back to the Time display. This should the two sine waves plotted vs time. Adjust them again so that they are as identical as possible. (Try to get them displayed on top of one another by using the Min, Max, Freq and Phase controls in the AWG generator controls.)

Click on the Math Button to open the Math function controls. Click on the Built In Expression list and select CAV-CBV, which will produce a third trace that is the difference between the two channels. You will need to increase the V/Div to 1.0 on both channels to see the difference signal. The two AWG channel outputs have DC offset which should also sum to zero if they are the same. Also adjust the vertical position such that the traces do not go off the grid.

If you have adjusted the two sine waves to be identical, their difference should be zero. How well did you do? Note that the amplitude, the frequency, and the phase must be identical to make the difference zero.

Now make the two signals as identical as possible by adjusting the difference signal away. What did you have to do?

Summary
~~~~~~~

From this activity, you should see the value of comparing one signal against some kind of known reference signal. It is possible to tune a guitar, for example, by comparing the tone a string makes with an electronic reference tone. This results in a perfectly tuned instrument, even when the player has less than perfect pitch. You have also seen how we make what are called differential measurements. There are many advantages to making differential over absolute measurements. You have seen one of the key reasons since differential measurements allow you to focus on smaller quantities since you are working with the difference between two signals.

**For Further Reading:**

| `Lissajou Curves <http://datagenetics.com/blog/april22015/index.html>`_
| `Lissajou Curves <https://en.wikipedia.org/wiki/Lissajous_curve>`_

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
