Activity: Parallel LC Resonance, For ADALM1000
==============================================

Objective:
----------

The objective of this activity is to examine the oscillations of a parallel LC resonate circuit. In addition the self-resonance of a real inductor will be examined.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A resonant circuit, also called a tuned circuit consists of an inductor and a capacitor together with a voltage or current source. It is one of the most important circuits used in electronics. For example, a resonant circuit, in one of many forms, allows us to tune into a desired radio or television station from the vast number of signals that are around us at any time.

A network is in resonance when the voltage and current at the network input terminals are in phase and the input impedance of the network is purely resistive.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1: Parallel Resonance Circuit


Consider the Parallel RLC circuit of figure 1. The steady-state admittance offered by the circuit is:

:math:`Y = 1/R + j(ωC – 1/ ωL)`

Resonance occurs when the voltage and current at the input terminals are in phase. This corresponds to a purely real admittance, so that the necessary condition is given by:

:math:`ωC – 1/ωL = 0`

The resonant condition may be achieved by adjusting L, C, or ω. Keeping L and C constant, the resonant frequency ω\ :sub:`o` is given by:

$ω_o = 1/sqrtLC $ rad/s (1)

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz (2)

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wires
| 1 - 4.7 mH inductor ( or larger )
| 1 - 10 μF capacitor
| 1 - 1 kΩ resistor
| 1 – small signal diode (1N914)

Directions:
~~~~~~~~~~~

First a quick diversion to examine using a diode as a switch.

Set up the circuit shown in figure 2 on your solder-less breadboard. Configure the AWG CH-A to output a sine wave with a frequency 100 Hz and Min value of 0.5 V and a Max value of 4.5 V (p-p = 4V). Set up the horizontal time scale to view two full cycles of the sine wave on Channel A and so that the signal looks as large as possible without going off the screen. Configure Channel B in Hi-Z mode and connect it to where R\ :sub:`1` connects to D\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2. Diode test circuit


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/diode_test_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3. Breadboard connections


Hand-draw the circuit diagram, carefully labeling the connections from the ALM1000 for CH-A, +2.5V, CH-B and include it in your lab report. From the Curves drop down menu select the CA-V, CA-I and CB-V traces for display. On the right hand side of the scope screen enter 2.5 for the CA-V and CB-V offset adjustment. This is because in this experiment we are referencing all the measurements to the +2.5 V common rail. Also enter 0 for the CH-A and CH-B vertical position settings ( along bottom of scope screen ). The vertical scale should now be centered on 0 and go from -2.5 to +2.5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-d1.png
   :align: center
   :width: 400px

Click Run. (You will not be given this direction at every step. It is assumed that you will know you have to start and stop the sweeps at various steps in the experiments.)

Use the Math drop down menu and add a trace that displays the difference between CH-A and CH-B. For this experiment, make sure the vertical scales are the same for all three signals being displayed.

Observe what happens to the sine wave as it passes through the diode and the current being supplied by Channel A. Describe the waveforms in a sentence. Save the display and copy and paste it into your lab report. Label the input voltage (produced by the AWG source), the input current supplied by the source and the output voltage (across the resistor). Also show the magnitude of each signal at key points (do not assume that the reader can easily figure it out from the scales on the plot).

1. Based on this observation, what is the function of a diode?

Switch the AWG A shape to square wave output and make sure the oscilloscope shows a few cycles of the signal. Save this waveform and include it in your report. Again, fully annotate your plot.

Reconfigure the breadboard circuit with the diode, inductor and capacitor as shown in figure 4. As above, connect Channel A to the diode and channel B across the capacitor and inductor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4. LC resonator test circuit


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/lc_res_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5. LC resonator breadboard connections


2. Calculate the frequency at which the circuit should oscillate.

Now you will use the oscilloscope to measure the frequency at which the circuit actually oscillates. When you apply the 100 Hz square wave, the LC circuit will oscillate immediately after the falling edge of the square wave. Change the horizontal position or hold-off time to place the oscillations at the left of the grid (so you can see as much of the oscillation as possible).

Change your Horizontal Time/Div in order to easily observe and measure the period of oscillation. With the sweeping stopped ( Red Stop Button ) left clicking on the display grid will add marker points to the display. The delta in voltage and time between the last two markers will also be displayed. Use the delta time between adjacent peaks or valleys of the oscillations to get the period. Save the display and include it in your report (fully annotated).

3. From the period, determine the frequency at which the circuit oscillates.

The frequency should be approximately equal to the calculated frequency. If not, check the component values in your circuit and calculations. Note in your report if the frequency you measured is a little smaller or a little larger than the one given by the formula.

Do you see why the diode was used? A diode passes current in one direction only. During the half of the square wave above the +2.5 V rail, the diode conducts, and energizes the LC resonator. For the half of the square wave below the +2.5 V rail the diode does not conduct, so the LC resonator is effectively isolated from the AWG source and is free to oscillate.

Show your working experiment to a TA or instructor, along with your annotated plots and your two calculations of frequency. Explain why your results make sense. Obtain a signature that you have completed this task.

4. Does the waveform have a constant amplitude, or does it grow or decay?

Describe the waveform in words and discuss why it differs from simple theory. Look up the spec sheet for the inductor and see if you can find the characteristic that causes the growth or decay. (Here is where reading the entire write-up will help you.)

Now adjust the square wave so that its Min value is 0.5V and Max value is 3.5V. (p-p =3V)

Repeat the measurements you just made, again saving and annotating the data plots. Explore other combinations of Min and Max values for the square wave.

5. What is different about the voltages measured? (Compare to previous plot.)

Energy Storage:
~~~~~~~~~~~~~~~

The voltage across the parallel capacitor/inductor should be a decaying sinusoid (also called a damped sine wave ). A realistic model of an inductor includes a series resistance. Some of the energy in the resonator is converted to heat when current flows through this resistance. This loss of energy results in the amplitude of the osculation decaying over time.

In addition to the resonator voltage, we would also like to measure the capacitor and inductor currents. First to obtain the current in the capacitor we can make use of the following formula:

:math:`I_C = C dV/dT`

To calculate the discrete time derivative of the capacitor voltage we can subtract two consecutive time samples and divide by the change in time between samples. The time between samples is simply 1/samplerate. For the ALM1000 the sample rate is 100KSPS or 10 uSec per sample. The value of C1 is 10 uF which just happens to cancel when divided by the 10 uSec. The formula gives the current in Amps. To plot in mA simply multiply by 1000. Set the Math axis to ‘I-A’ and enter the following for the Math formula:

::

   (VBuffB[t]-VBuffB[t-1])*1000

Looking at the schematic in figure 4 again we note that when the diode is off and the resonator is oscillating the only place for the current in the capacitor to go is in the inductor. So:

:math:`I_L = I_C`

From the inductor current waveform and the capacitor voltage waveform we can calculate the instantaneous energy in each component. Using the Math formula feature, plot the two energy waveforms as a function of time.

The first will be the energy in the inductor. The units for inductance is joules per ampere square. So the energy in Joules is:

:math:`\displaystyle E_L = \frac{1}{2} LI^2`

One half of the 4.7 mH inductor value is 0.00235 H. A 4.7 mH inductor with 40 mA flowing through it is storing 0.00000376 joules of energy or 3.76 uJ ( microJoules). A very small number so we will scale it by 10\ :sup:`6`. To plot the energy in the inductor ( in microJoules ) enter the following for the Math formula:

::

   2350*((VBuffB[t]-VBuffB[t-1])**2)

The second will be the energy in the capacitor. The units for capacitance is coulombs squared per Joule. The number of coulombs stored on the capacitor is equal to the capacitance times the voltage. So the energy in Joules is:

:math:`\displaystyle E_C = \frac{1}{2} CV^2`

One half of the 10 uF inductor value is 0.000005 F. A 10 uF capacitor charged to 1 V has 0.000005 joules of energy or 5 uJ ( microJoules). A very small number so we will scale it by 10\ :sup:`6`. To plot the energy in the capacitor ( in microJoules ) enter the following for the Math formula:

::

   5*(VBuffB[t]**2)

Save and fully annotated these plots in your report.

Discuss the two energy values, how they change with time, their relation to one another. For example when is the energy contained mostly or entirely in the inductor? When is it contained mostly or entirely in the capacitor? What trends over time from cycle to cycle do you see? Be as quantitative as you can, but mostly address the overall picture.

The current in the inductor can be directly measured by disconnecting the inductor from the fixed 2.5 V power rail and connecting it to the output of AWG channel B as shown in figure 6. Set AWG CH-B to SVMI mode and shape DC with the Max value set to 2.5 V. Select the CB-I trace from the curves menu.

Compare the trace you get with the calculated capacitor current ( and by the same inference we just made, the inductor current ). Note any differences and explain why.

How could you use this measurement technique to directly measure the current in the capacitor?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6. Directly measuring the Inductor current


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/dir_meas_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7. Breadboard connections


Self-Resonance
~~~~~~~~~~~~~~

All real inductors possess a built-in capacitance, called a "parasitic" capacitance. The inductor acts as if it has a capacitance connected in parallel with it. This sometimes called the winding capacitance.

Remove the capacitor from your breadboard and measure the frequency at which the inductor oscillates. Adjust the horizontal time scale as needed to clearly see the oscillation. You probably want to turn on waveform smoothing ( under the options menu ) when measuring the high frequency that the inductor self resonates at.

Show your working experiment to a TA or instructor, along with your annotated plots and your calculation of the self-resonate frequency. Explain why your results make sense. Obtain a signature that you have completed this task.

1. Calculate the value of the parasitic capacitance.

Inductors also have an internal series resistance that should not be ignored when they are modeled.

Measure the series resistance of your inductor using the Ohmmeter tool or the Impedance analyzer tool ( or a DMM ohmmeter if you have one ). Also look up the resistance of your inductor to see what the manufacturer claims it is.

2. Compare the value you measured with the one found on the spec sheet. What aspect of the oscillating signal you measured for the LC circuit is caused by the resistance?

In your Lab Report, List all 7 questions/tasks. Provide the annotated data for each one along with the answers to any questions.

**Self-resonance example**

Figure 8 is a representative example of self-resonance waveform for a 4.7mH inductor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8. Self-resonance


**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/parallel_lc_res_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/parallel_lc_res_ltspice`

**For Further Reading:**

| `Inductor <https://en.wikipedia.org/wiki/Inductor>`_
| `Damped sine wave <https://en.wikipedia.org/wiki/Damped_sine_wave>`_
| `Self-resonant frequency <https://en.wikipedia.org/wiki/Self-resonant_frequency>`_
| `Parasitic capacitance <https://en.wikipedia.org/wiki/Parasitic_capacitance>`_
| http:*www.coilcraft.com/pdfs/Doc363_MeasuringSRF.pdf
  http:*\ www.coilcraft.com/pdfs/doc671_Selecting_RF_Inductors.pdf
| http://www.coilcraft.com/pdfs/doc119_TestAppFreq.pdf

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
