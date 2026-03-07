Activity: The Wien bridge oscillator - ADALM1000
================================================

Objective:
----------

Oscillators are circuits that generate periodic waveforms without any input signal. They generally include some form of amplifier stage like transistors or OP-AMPs with a feedback network consisting of passive devices such as resistors, capacitors, or inductors, In this activity the Wien bridge oscillator will be examined.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The Wien bridge oscillator is one of the simplest oscillators circuits, figure 1 shows the basic circuit configuration. An op-amp is used as the amplifying stage and the RC band pass Wien Bridge consisting of R1, C1 and R2, C2 is used as the frequency selective positive feedback network.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_wien-brigde-osc-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1; Wien bridge oscillator LTspice simulation schematic


The Wien Bridge oscillator as shown in figure 1 provides a good example to better understand oscillator design using feedback analysis. Feedback analysis is used to test if your design is stable (well behaved) or unstable (may oscillate). Feedback analysis simply means opening the feedback loop and injecting an AC signal where the new configuration can now be considered the input as shown in figure 2. We can open the loop of the oscillator between the output of the amplifier and the frequency selective network. This works as a good point to break the loop because of the relatively low output impedance of the amplifier. Similarly, the AC source VINJ also has a low output impedance. Therefore, opening the loop at this point does not significantly alter the circuit behavior.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_wien-brigde-osc-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Simulation schematic for injecting a test signal


By measuring the gain (magnitude) and phase (time-shift) of signal as it travels around the opened loop, it can be determined if the circuit will operate as an amplifier or an oscillator when the loop is closed.

When designing an oscillator, the idea is to choose component values that will make the open-loop analysis meet the conditions for oscillation at the frequency of interest. The conditions for oscillation are as follows: If, at the frequency of interest, the AC gain around the opened loop is (at least) 1 V/V and the total phase shift is -360° or 0°, the circuit will oscillate at that frequency.

There are two sections of the Wien Bridge oscillator circuit. The first is an RC band pass filter network and the second is an amplifier. Both are necessary to achieve the conditions for oscillations. The RC filter network is characterized by a center frequency F\ :sub:`o`.

:math:`F_o=1/(2 \pi R C)`

Where R=R\ :sub:`1`\ =R\ :sub:`2` and C=C\ :sub:`1`\ =C\ :sub:`2`. At the center frequency, two interesting things occur at V\ :sub:`FLT`. First, the phase shift goes through 0 degrees. And second, the amplitude reaches a peak of -9.5 dB (or 1/3).

Circuit Analysis
~~~~~~~~~~~~~~~~

Run an LTspice simulation of the open-loop circuit of figure 2. Plot trace V\ :sub:`FLT` to see what the amplitude looks like at the center frequency. For R\ :sub:`1`\ =R\ :sub:`2`\ =10 kΩ and C1=C2=0.1 uF, the center frequency should be near 1 kHz. What does the phase look like? Add the phase plot for V\ :sub:`FLT` to see the Phase shift. The RC network provides one of the conditions for oscillation, the phase is 0° at the design frequency.

Amplifier
~~~~~~~~~

The RC network by itself falls short of the conditions for oscillation in that the gain is only 1/3 V/V (-9.5 dB). How is the gain of 1 V/V (0 dB) around the loop to be achieved? As you might suspect, the non-inverting amplifier section provides the needed gain. How much gain? A gain of 3 V/V makes the total gain 1/3 x 3 = 1 V/V (0 dB). Setting the correct amplifier gain is critical. Not enough and any oscillation will die away. Too much and the amplitude will increase until the amplifier saturates. What is required is a mechanism to guarantee oscillations will start (Gain > 3), yet, limit the gain (Gain=3) at steady state. Diodes D\ :sub:`1`, D\ :sub:`2` and R\ :sub:`6` in the negative feedback path provide the mechanism that limits the gain when the amplitude reaches a certain level. For small signal levels, the diodes do not conduct and the gain is set by:

:math:`Gain=1+ (R_4+R_5+R_6 / R_3)`

For larger signals, the voltage across R\ :sub:`6` is large enough to make D\ :sub:`1` and D\ :sub:`2` conduct. The shunt resistance of the conducting diodes in parallel with R\ :sub:`6` effectively reduces the total feedback resistance, reducing the overall gain to Gain=3 (about +9.5dB).

Run a simulation of just the non-inverting gain stage. View the AC output of the op amp VM(4). For R\ :sub:`4`\ =6.8k, R\ :sub:`5`\ =6.8k and R\ :sub:`6`\ =6.8k, the op amp gain is (1 + (6.8+6.8+6.8)/10) = 3.3 V/V. This should make the overall open-loop gain equal to 1/3 x 3.3 = 1.1 V/V (which is slightly more than 0 dB). Does the peak at V\ :sub:`OUT` reach this expected gain?

Oscillator Operation
~~~~~~~~~~~~~~~~~~~~

It’s time to close the loop and simulate the full Wien Bridge Oscillator in the time domain. Run a transient simulation of the closed-loop circuit and plot the waveform at the output of the amplifier. Does the circuit oscillate? I it does not oscillate you may need to adjust the values of resistors R3-R6. How much time does it take for the amplitude to stabilize?

What happens if there’s not enough gain around the loop? Reduce R\ :sub:`6` to 1 kΩ making the total loop gain less than 1. Run a simulation. The output might ring briefly and die away, but there’s not enough gain to sustain oscillations.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless breadboard and jumper wires
| 2 – 1.5 KΩ resistors
| 2 – 10 KΩ resistors
| 1 – 10 K Pot
| 2 – 0.1 uF capacitors
| 2 – 1N914 small signal diodes
| 1 – OP484 R-R op-amp (or AD8542)

Directions:
~~~~~~~~~~~

Construct the oscillator circuit as shown in figure 3 on the solder-less breadboard. Be sure to carefully note the power and ground connections to the OP848 op-amp before applying power to the circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_wien-brigde-osc-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Breadboard schematic


Both AWG channels Mode should be set to Hi_Z Split I/O because we will not be using any signal sources just yet, only using the Scope channels (AIN and BIN) to measure the circuit waveforms.

Temporarily disconnect the two diodes from the circuit. Adjust Potentiometer R5 until the circuit just starts to oscillate. Note the relative P-P amplitude seen on the op-amp output (AIN) and the P-P amplitude seen on the op-amp + input pin 3. It should be 1/3.

Loop Gain Procedure:
~~~~~~~~~~~~~~~~~~~~

To measure the loop gain use the Bode Plotting tool. Open the loop by disconnecting C2 from the op-amp output. Use AWG output CH-A as the test source by connecting it to the end of C2 you just disconnected. Set AWG channel A Mode to SVMI. Disconnect AIN from the op-amp output and connect BIN to the op-amp output. Do a frequency sweep from 100 Hz to 10 KHz. Plot the relative gain CA-dB – CB-dB and the relative phase.

**For Further Reading:**

| :adi:`Bridge Circuits Application Note 43 <media/en/technical-documentation/application-notes/an43f.pdf>`
| :adi:`LT1007/LT1037 Ultrapure 1kHz Sine Wave Generator <en/design-center/reference-designs/circuit-collections/lt1007-lt1037-ultrapure-1khz-sine-wave-generator.html>`
| :adi:`Injection-Lock a Wien-Bridge Oscillator <en/technical-articles/injection-lock-a-wien-bridge-oscillator.html>`
| `"Thank You, Bill Hewlett", Jim Williams, EDN Magazine Feb. 2001 <https://m.eet.com/media/1146147/22254-61856.pdf>`_
| `U.S. Patent 2,268,872 <https://www.hp.com/us-en/pdf/002patent_tcm_245_921599.pdf>`_
| `Wien_bridge_oscillator <https://en.wikipedia.org/wiki/Wien_bridge_oscillator>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
