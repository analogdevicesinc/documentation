Activity: The Comparator, Positive Feedback and Schmitt Trigger, For ADALM1000
==============================================================================

Objective:
----------

The objective of this activity is to investigate the voltage comparator, the use of positive feedback and the operation of the Schmitt Trigger configuration. The use of conventional operational amplifiers as a substitute for voltage comparators will also be explored.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The Voltage Comparator:
-----------------------

A Differential Voltage Comparator such as the AD8561 from the analog parts kit has a pinout similar in many ways to that of a conventional opamp but with many important differences (figure 1). There are the usual V+ and V– power supply pins but a comparator will also have a ground (GND) pin as well. The differential +IN and –IN pins are essentially the same as a conventional op-amp. There will also be an output pin as in an opamp but there is often a second "inverting" ( or complementary ) output. Also, while the voltage at the output of an opamp can generally swing close to the + and – supply rails, the output of a comparator will swing only between ground and the + supply. This makes the output more like a digital signal and compatible with standard logic gates such as TTL or CMOS. The voltage comparator can be thought of as a single bit analog-to-digital converter (ADC). The AD8561 also includes a LATCH input which will latch or freeze the output and prevent it from changing even if the inputs change.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1, AD8561 Pin assignments


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| AD8561 voltage comparator
| 1 – 10 KΩ resistor
| 1 – 20 KΩ resistors
| 1 – 47 KΩ resistor
| 1 – 100 KΩ resistor
| 2 – 4.7 KΩ resistors
| 1 – 0.1 uF capacitor

Directions:
~~~~~~~~~~~

Construct the comparator test circuit as shown in figure 1 on your solder-less breadboard. The two 4.7 KΩ pull-up resistors are optional and are used to increase the peak positive output swing to closer to the +5 V supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, The Voltage Comparator


Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator CA-V for a 50 Hz triangle wave with a 0 V Min value and 5 V Max value. Channel B is set in the Hi-Z mode. Both scope channels should be set to 0.5V/Div.

Procedure:
~~~~~~~~~~

With Channel B in Hi-Z mode first connect it to the non-inverting output ( pin 7 ). You should see a square wave that is high ( near +5 V ) when the input signal level is a greater than 2.5 V and low ( near 0 V ) when the input signal is less than 2.5 V. Note the levels of the input triangle wave where the output changes from low to high and from high to low. Now connect Channel B to the inverting output ( pin 8 ). You should again see a square wave but with opposite phase to pin 7. You can remove the 4.7 KΩ pull-up resistors to compare the maximum positive output swing with and without the resistors.

With Channel B connected to pin 7, zoom into the falling edge of the output square wave by adjusting the Horizontal position and time per division settings such that the falling edge is centered on the time axis and the time per div is small enough to see the transition time of the edge (0.05 mS/div). You should see that the output does not go from the high output level all the way to the low output level all at once but stops part way and spends some time at an intermediate level before continuing the rest of the way to the low output level. Switch the settings and zoom into the rising edge as well. It should also show this delay when transitioning from low to high.

This delay is caused by noise as the input signal slowly passes through the input threshold level ( +2.5 Volts in this case ) and can cause problems.

Using positive feedback to add hysteresis: the Schmitt trigger:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common solution to the problem just outlined is to add noise immunity to the comparator circuit by incorporating hysteresis into the transition threshold voltage Vth, as shown in figure 3.

By "hysteresis" we mean that the threshold voltage is a function of the system’s current operating state, which is defined for this circuit by its output voltage: positive or negative saturation. Because Vth, the voltage at pin 2, is determined by the voltage divider constructed from resistors R\ :sub:`1`\ and R\ :sub:`2`, it changes in response to a change in the output voltage: once the output has gone high in response to an input which has passed below the threshold voltage, the threshold voltage is changed to a higher value Vth+ ( 2.5 V + a fraction of the output high voltage ); conversely, an input voltage climbing through Vth+ will change the output to its low state and cause the threshold voltage to be set to a lower value Vth- ( 2.5 V - a fraction of the output low voltage ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Schmitt trigger


This difference between Vth+ and Vth- means that once a transition is triggered by a change in Vin, noise excursions smaller than this difference on the input will not cause Vin to cross the hysteresis gap V\ :sub:`HIST` = Vth+ - Vth- and cause an undesired reversal of the output state. If the hysteresis gap is made large enough, then the system can be made completely impervious to the noise on the input signal, eliminating the spurious output levels suffered by the basic comparator circuit (figure 1).

**Calculating the threshold:**

Let’s call the maximum and minimum output voltages V\ :sub:`HIGH` and V\ :sub:`LOW`. The threshold voltage when the output is at V\ :sub:`HIGH` and at V\ :sub:`LOW` is:

:math:`VTH_HIGH = R_2/(R_1+R_2) ( V_HIGH - 2.5 ) + 2.5`

:math:`VTH_LOW = R_2 / (R_1 + R_2) ( V_LOW - 2.5 ) + 2.5`

The resulting hysteresis gap for the circuit of figure 3 is given by:

:math:`V_HIST = R_2 / (R_1 + R_2) ( V_HIGH - V_LOW )`

For the AD8561 with a +5 V power supply and pull-up resistor, V\ :sub:`HIGH` – V\ :sub:`LOW` ≈ 4.5 V. Because the other end of the voltage divider (bottom of R\ :sub:`2`) is connected to +2.5V ( middle of the power supply ), the threshold voltages VTH\ :sub:`HIGH` and VTH\ :sub:`LOW` will be centered around +2.5V (assuming that V\ :sub:`HIGH` and V\ :sub:`LOW` are more or less centered around 2.5 V). Connecting the bottom of R\ :sub:`2` to a different voltage reference source rather than to mid supply will not affect the hysteresis gap, but it will center that gap around a threshold proportional to the new reference voltage. In fact the negative input pin of the comparator could be connected to the fixed reference voltage and the end of R\ :sub:`2` considered as the input. This in effect reverses or inverts the sense of the two outputs.

Note that the hysteresis gap equation places a potential restriction on the ratio R\ :sub:`2`/R\ :sub:`1` for a Schmitt trigger: unless R\ :sub:`2` < R\ :sub:`1`, the hysteresis gap will be larger than one half of the peak to peak output voltage swing range of the comparator and depending on the reference voltage value, one or the other of the Schmitt trigger thresholds might be beyond the range of the output voltage. Assuming the input signal voltage range is also limited to the output swing range ( in other word the power supply rails ) then the circuit’s output could lock-up and no longer respond to any changes in the input rendering the circuit useless.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Add the two positive feedback resistors to your circuit as shown in figure 3. Use different values for R\ :sub:`1` ( 20 KΩ, 47 KΩ and 100 KΩ ) with R\ :sub:`2` equal to 10 KΩ. Using Channel B, again observe the output square wave but note the level of the input triangle wave when the output changes level from low to high and high to low. How do these levels compare to those seen in the case without hysteresis and for each of the three values for R\ :sub:`1`? Explain your results. Try a value for R\ :sub:`1` less than R\ :sub:`2` like 1 KΩ. Does the circuit still work?

To see if the delay caused by the input noise has changed, again zoom into the falling and rising edges of the output square wave by adjusting the Horizontal position and time per division setting. Does the output pause at the same intermediate level as it transitions or does it no longer have this delay?

Relaxation oscillator
---------------------

If the output of a Schmitt trigger is fed back to the inverting input through a RC low-pass filter, you get a circuit where the output switches back and forth between the comparator’s two saturation limits: a simple relaxation oscillator, as in figure 4. As can be seen from the figure, the comparator’s output charges the capacitor C\ :sub:`T` via the resistor R\ :sub:`T`. Because the capacitor’s voltage is compared by the inverting input, every time it charges up to the trigger threshold, the output changes state, and the capacitor voltage then begins to "relax" toward the opposite output saturation limit. The trigger threshold voltage at the +Input has also changed, however, so that the output again changes state as the capacitor voltage reaches this opposite threshold; the process is then repeated.

The capacitor’s voltage waveform is an exponential relaxation toward an equilibrium voltage which will equal to the output saturation voltage, Vsat, starting from the opposite trigger threshold voltage. If the + and – saturation voltages are assumed to be equal, then this exponential relaxation is described by:

:math:`\displaystyle V_CT = V_SAT – (V_SAT – V_TH) e^\frac{–t}{RC}`

If the oscillation period is T, then after half a period the capacitor voltage reaches the next trigger threshold, so in the above equation at time T/2, V\ :sub:`CT` = V\ :sub:`TH`. From the equation relating Vsat and Vth, the relationship between the period T and the circuit’s component values is:

:math:`R_1 / R_2 = coth(T/4RC)-1`

Where coth is the hyperbolic cotangent function. If we want the oscillator period to equal the feedback RC time constant ( T=RC), then:

:math:`R_1 = 3.08 R_2`

R\ :sub:`1`\ =120 KΩ, R\ :sub:`2`\ =39 KΩ gives a pair of standard resistor values which closely matches this ratio within 0.2%. ( Other combinations of standard values such as R\ :sub:`1`\ =100 KΩ, R\ :sub:`2`\ =20 KΩ + 10 KΩ in series are also close).

Note that the current drawn by the R\ :sub:`T`, C\ :sub:`T` feedback is as high as the peak to peak output swing just after the output changes state. Large currents from low values of R\ :sub:`T` and / or high values of C\ :sub:`T` will reduce the minimum and maximum output voltages as the comparator tries to deliver this much output current, distorting the output waveforms and lengthening T. Choosing R\ :sub:`T` ≥ 10 KΩ should limit the capacitor charging current to a reasonable level.

.. _directions-1:

Directions:
~~~~~~~~~~~

From here on the pin numbers and power / ground connections have been left off the schematics for simplification. Be sure power and ground are always properly connected. Add the RC feedback to your Schmitt trigger circuit as shown in figure 4. Use both scope channels in Hi-Z mode to observe the waveforms across capacitor C\ :sub:`T` at the inverting input and the output as shown.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Relaxation oscillator using a Schmitt trigger


Try different combinations of R\ :sub:`1` and R\ :sub:`2` to see how their ratio effect the amplitude of the signal seen across C\ :sub:`T` and the frequency of oscillation. Explain your results.

Function generator
------------------

Using an integrator circuit rather than a simple RC network would charge the capacitor at a constant rate, so the exponential wave shape of the capacitor voltage in the last circuit would be replaced by a linear ramp. The circuit with an op-amp based integrator ( A\ :sub:`2` ) is shown in figure 6. We must now use the noninverting form of the Schmitt trigger because the integrator is inverting.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, simple function generator


.. _directions-2:

Directions:
~~~~~~~~~~~

Modify your circuit from figure 4 to include the integrator circuit. Most any op-amp from the Analog Parts Kit will work for A2 but the rail-to-rail CMOS AD8541 single or AD8542 dual are the best choices ( the OP484 quad as well). Be sure to properly connect power and ground to A\ :sub:`2` as per the datasheet for the chosen device. Use the same resistor and capacitor for R\ :sub:`I` and C\ :sub:`I`. Use Channels A and B in Hi-Z mode to observe the waveforms at the outputs of A\ :sub:`1` and A\ :sub:`2`.

Since the voltage applied to the integrator resistor R\ :sub:`I` is constant between triggers, the integrated output voltage will have a constant slope between triggers. For this reason the period of the output signals is much easier to calculate for this circuit; the formula is left to the reader. To make the frequency variable, resistor R\ :sub:`I` can be made variable ( a digital potentiometer such as the AD8402 for example ); an analog switch could also be used to select from a set of capacitors for C\ :sub:`I`.

Figure 6 shows a variation of the function generator circuit which incorporates both frequency and symmetry adjustments of the output waveforms. Note how the diodes D\ :sub:`1` and D\ :sub:`2` select which side of the symmetry potentiometer is used to set the rising and falling current through the integrator’s capacitor (depending on the sign of the voltage follower’s output with respect to the 2.5 V common mode level). An additional opamp connected as a voltage follower (A\ :sub:`3`) isolates the Schmitt trigger’s square wave output and the frequency adjust potentiometer from the current load required by the integrator, so changing the symmetry potentiometer setting will not affect the voltage divider ratio set by the frequency potentiometer or comparator A\ :sub:`2`\ ‘s output saturation voltages, especially important when the symmetry potentiometer is set near one of its limits.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, function generator with variable frequency and waveform symmetry


Figure 6 presents one of the more complicated circuits considered to this point. You should spend some time studying this circuit so that you understand how it works and how you would select values for the components (the lab exercises will help you focus on this task). Why is the resistor in series with the output of opamp A\ :sub:`3` necessary?

The op-amp as a "comparator":
-----------------------------

Consider an op-amp used to amplify a signal without feedback as shown in figure 7. Because no feedback is used, the input signal is amplified by the full open-loop gain of the op-amp. Even a very small input voltage (less than a millivolt either side of Vth) will be enough to drive the output to either the minimum or maximum output voltage, as shown in the plots of Vin and Vout. Thus, in this case because the op-amp -Input is connected to Vth, the output represents the sign of Vin ( "0" if Vin < Vth, "1" if Vin > Vth ) 1, and the circuit is like a one-bit analog to digital converter (ADC), and functions like a voltage comparator.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7, An op-amp used as a comparator


Op Amps and comparators may seem interchangeable at first glance based on their symbols and pinouts. The Analog Parts Kits is supplied with a variety of op-amps and the AD8561 high speed voltage comparator that was used in the earlier activities. Some designers might be tempted to use or substitute readily available op amps as voltage comparators in their projects. There are very important differences however. Comparators are designed to work without negative feedback or open-loop, they are generally designed to drive digital logic circuits from their outputs, and they are designed to work at high speed with minimal instability. Op amps are not generally designed for use as comparators, their input structures may saturate if over-driven which may cause it to respond comparatively slowly. Many have input stages which behave in unexpected ways when driven with large differential voltages or beyond the specified common mode range. In fact, in many cases, the differential input voltage range of an op amp is limited or clamped to prevent damage to the input stage devices. Note this article on ":adi:`Amplifier Input Protection... Friend or Foe? <en/analog-dialogue/articles/amplifier-input-protection-friend-or-foe.html>`" for more background on this issue.

.. important::

   Warning: Using op-amps with built-in input clamps as a voltage comparator may damage the IC!


Yet many designers still try to use op amps as comparators. While this may work at low speeds and low resolutions, many times the results are not satisfactory. Not all of the issues involved with using an op amp as a comparator can be resolved by reference to the op amp datasheet, since op amps are not intended for use as comparators.

The most common issues are speed (as we have already mentioned), the effects of input structures (protection diodes, phase inversion in FET amplifiers such as the ADTL082, and many others), output structures which are not intended to drive logic, hysteresis and stability, and common-mode effects.

.. _directions-3:

Directions:
~~~~~~~~~~~

The ADALP2000 Analog Parts Kit contains a wide variety of op-amps. Using as many of the available opamps as possible, build the test circuit shown in figure 8. Be sure to properly note the different pinouts for the various op-amp packages, Single vs Dual vs Quad and connect the input, output power and ground accordingly.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8, op-amp as comparator test circuit


.. _procedure-2:

Procedure:
~~~~~~~~~~

Again configure the waveform generator CA-V, on the non-inverting input, for a 2V Min value and 3V Max value triangle wave ( centered on 2.5 V ) at 500 Hz. With the power supply reconnected, observe the input and output waveforms. What is the maximum and minimum voltages seen at the op-amp output. Compare this to the AD8561 comparator.

Try using the external pull-up resistor to the positive supply trick to increase the max output voltage. Does it work the same in the case of an opamp? If not why not?

Now slowly shift the center of the triangle wave by increasing ( positive shift ) or decreasing ( negative shift ) the Min and Max values and observe what happens at the output. Can you explain this?

Repeat the above tests for each of the different op-amps from the parts kit and record your observations in your lab report. Which op-amps would work better as a comparator and why? What datasheet parameters should be taken into consideration in these application cases?

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/voltage_comparator_ltspice`
-  Fritzing files: :git-education_tools:`voltage_comparator_bb <m1k/fritzing/voltage_comparator-bb>`

**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
