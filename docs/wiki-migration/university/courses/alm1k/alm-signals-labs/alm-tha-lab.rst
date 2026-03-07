Activity: Track-and-Hold Amplifier
==================================

Objective:
----------

The Track-and-Hold amplifier, or THA, is a critical part of most data acquisition systems. In this activity two different THA configurations will be examined. You will also investigate the selection of the optimum Op-amp and Hold capacitor. Charge injection from the analog switch will be explored and circuit techniques to cancel it will be investigated.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The Track and Hold amplifier captures an analog signal and holds it constant during some operation (most commonly analog-to-digital conversion). The circuitry involved is demanding, and unexpected properties of commonplace components such as capacitors and printed circuit boards may degrade THA performance. When the track-and-hold is in the track (or sample) mode, the output follows the input with ideally only a small voltage offset. There do exist sampling configurations where the output during the sample mode does not follow the input accurately (may even return to a reset or zero value), and the output is only accurate during the hold period. These will not be considered here. Strictly speaking, a sample-and-hold with good tracking performance should be referred to as a track-and-hold circuit, but in practice the terms are often used interchangeably.

Analog to Digital converters are typically made up of two sections. The first section is a sampling circuit which holds a changing input signal constant at the output of the track and hold for a short time while the second section, or quantizing stage generates the digital result. Most often the track-and-hold circuit has a gain of 1, but in some applications it can have gains greater or less than 1. When the THA is used with an ADC (either externally or internally), the THA performance is critical to the overall dynamic performance of the combination, and plays a major role in determining the Spurious Free Dynamic Range, Signal to Noise Ratio, etc., of the system.

Regardless of the circuit details or type of THA in question, all such devices have four major components. The input buffer amplifier, switching circuit, energy storage device (capacitor), and output buffer are common to all THAs. The basic idea of a simple track-and-hold circuit is shown below:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Basic Track-and-Hold Circuit


The energy-storage device, the heart of the THA, is a capacitor. The input amplifier stage buffers the input by presenting a high impedance to the signal source and providing current gain to charge the hold capacitor. In the track mode, the switch is closed and the voltage on the hold capacitor follows (or tracks) the input signal (with some delay and bandwidth limiting). In the hold mode, the switch is opened, and the capacitor retains the voltage present at the time it was disconnected from the input buffer. The output buffer stage offers a high impedance to the hold capacitor to keep the held voltage from discharging prematurely. The switching circuit and its driver form the mechanism by which the THA is alternately switched between track and hold.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| LTC1043 Switched Capacitor Building Block
| OP484 Quad Rail-Rail Op-amp
| AD8542 Dual CMOS Op-amp
| C\ :sub:`H` 4.7 nF capacitor (472)
| C\ :sub:`H` 100 pF capacitor (101)
| C\ :sub:`H` 39 pF capacitor (39)
| Cosc 4.7 nF capacitor (472)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Open Loop, Cascade of Followers THA


With Sine wave AWG channel A set to 250 Hz with Max value set to 4.6 and Min value set to 0.2, use a 10 nF capacitor for C\ :sub:`H` and a 4.7 nF capacitor for C\ :sub:`OSC`. You should see an output waveform on channel B that looks something like what is shown in figure 3. The 4.7 nF C\ :sub:`OSC` capacitor slows down the internal oscillator in the LTC1043 to about 1.5 KHz (see notes on adjusting the frequency at the end of this document).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, C\ :sub:`H`\ =10 nF, C\ :sub:`OSC`\ =4.7 nF


Testing Droop:
~~~~~~~~~~~~~~

An important specification of a THA is how constant it holds the sampled value while in hold mode and is what is known as droop. Droop is defined as the rate of change in the hold voltage while in Hold Mode. A principal source of droop while in hold mode is leakage current from the analog switch or the input bias current of the second amplifier. Note the leakage current could be positive or negative and the output can "droop" in either direction up or down.

To test the THA droop rate we apply a constant DC input and switch the circuit from Track to Hold mode. The circuit is held in the Hold mode long enough to observe the output drift off or droop. Connect the THA input at pin 10 of the OP484 to the fixed 2.5 V rail. Connect channel A AWG output to pin 16 of the LTC1043. The C\ :sub:`OSC` capacitor can be removed at this point. Set channel A shape to square wave. Keep the Min value set to 0.2, the Max value set to 4.8 and set the Freq to 500 Hz. Use a 39 pF capacitor for C\ :sub:`H` to start with. Capture the channel A S/H input wave form and the THA output waveform on channel B. Now change C\ :sub:`H` to a 100 pF capacitor.

Your results should look something like figure 4. For the 39 pF hold capacitor the output droops 1.31 V over the 1 mSec Hold time (voltage on pin 17 low) or 1310 volts/second. For the 100 pF hold capacitor the output droops 0.64 V over the 1 mSec Hold time or 640 volts/second. We know that the current charging or discharging the hold capacitor is equal to C times dV/dT.

For the first measurement:

:math:`I_LEAKAGE = 39 pF \times 1310` or 51 nA

For the second measurement:

:math:`I_LEAKAGE = 100 pF \times 640` or 64 nA

Both results are within the OP484 input bias current specification which is 60 nA typical and 450 nA maximum.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, 39 pF C\ :sub:`H` (dark orange) and 100 pF C\ :sub:`H` (light orange)


The OP484 is not a low input bias current amplifier and we could use a much larger hold capacitor, as much as 1000 times larger. That would require a more powerful first amplifier stage and lower on resistance switch to charge the hold capacitor quickly. We would like to use as small a hold capacitor as practical. The AD8542 dual CMOS Rail-to-Rail amplifier has a typical input bias current of only 6 pA and a maximum of 60 pA, a thousand times smaller than the OP484.

To measure how this difference will affect the droop rate, switch out the OP484 amplifiers with the AD8542 as shown in figure 5. If you don't have the AD8542 dual you can use a AD8541 single for the second amplifier in figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Low Droop Design


Repeat the droop measurements using a 39 pF capacitor for C\ :sub:`H` to start with. As before, capture the channel A S/H input waveform and the THA output waveform on channel B. Now change C\ :sub:`H` to a 100 pF capacitor. The droop rate should now be as much as 1000 times lower to the point of being basically not measurable as can be seen in figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, AD8542 droop with 39 pF C\ :sub:`H`


What conclusions can we draw from these droop rate tests? Only that not all op-amps will perform the same and a careful check of the datasheet specifications is always a good idea.

Testing Pedestal Error:
~~~~~~~~~~~~~~~~~~~~~~~

There are certain parasitic capacitances associated with an analog switch as depicted in figure 7. Capacitor C\ :sub:`Q` is of interest when designing a THA because it acts to couple some of the switch control signal to the switch output. A step in the control voltage of as much as the supply voltage appears on C\ :sub:`Q` when the switch turns off. The change in the voltage across C\ :sub:`Q` causes a small amount of charge to flow onto C\ :sub:`LOAD` in figure 7 which is the hold capacitor C\ :sub:`H` in our case. Hopefully, C\ :sub:`Q` is much smaller than C\ :sub:`H`. The charge that is injected onto the hold capacitor causes a step in the output voltage. This unwanted step is called pedestal error.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Switch charge injection


The LTC1043 contains 4 single pole double throw (SPDT) switches to select from to build our THA. In figure 8 we show the pinout for one of the SPDT switches. The center pole is pin 3 and the normally close switch direction (closed when pin 16 is low) is on pin 18 with the normally open switch direction (closed when pin 16 is high) on pin 15. We can connect the switch in four possible ways.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-8.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 8, One set of LTC1043 SPDT switch pins


**Note:**

A few comments on building the breadboard for these circuits, in general you should avoid using the long flexible jumper wires supplied in the ADALP2000 Analog Parts Kit as much as possible. It is better to use the short "staple" like jumpers from wire kits like the one shown in figure 9. Neatness and careful arrangement of the components on the breadboard are key to obtaining accurate results.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-jumper-wire-kit.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 9 Jumper wire kit


The hold capacitor node is a very high impedance node when in the Hold mode and is susceptible to external interference and noise such as from the main AC power lines. It may even be beneficial to use a grounded metal shield under the solderless breadboard and ALM1000. A small sheet of copper clad PC board material is a good option.

We can choose to drive any of the three pins from the first buffer amplifier stage. We can then choose to connect the hold capacitor to other end of the switch. Based on what we know from the example in figure 7, the logical assumption would be that the parasitic capacitance would be larger on pin 3 and that would be the best choice for the driven node with the hold cap connected to either pin 18 (pin 16 low for Hold mode) or pin 15 (pin 16 high for Hold mode). Figure 10 is a screen shot for this arrangement with 39 pF and 100 pF C\ :sub:`H`. The pedestal error for 39 pF is 8 mV and 5 mV for 100 pF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, Drive pin 3 with C\ :sub:`H` on pin 18


In figure 11 we have interchanged the two pins and the first buffer amplifier now drive pin 18 with C\ :sub:`H` on pin 3 for both 39 pF and 100 pF. The pedestal error for 39 pF is -100 mV and -58 mV for 100 pF or about a factor of 10 times worse. Clearly the charge injection from the parasitic capacitance is much large now. Also note that the pedestal error step is now negative which means the injected charge is in the opposite direction.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, Drive pin 18 with C\ :sub:`H` on pin 3


Now let's check the normally open switch on pin 15. In the screen shot shown as figure 12 we are back to driving pin 3 but now with C\ :sub:`H` on pin 15. Because the S/H signal is now inverted the triggering was changes to the falling edge. The pedestal error for 39 pF is 61 mV and 36 mV for 100 pF. We should expect results more like figure 10 than figure 11.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Drive pin 3 with C\ :sub:`H` on pin 15


For completeness we need to check the fourth arrangement with the buffer amplifier driving pin 15 and C\ :sub:`H` on pin 3 as shown in the figure 13 screen shot. The pedestal error for 39 pF is -11 mV and -4 mV for 100 pF. The pedestal error is much closer to figure 9 in magnitude but again in the negative direction.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 13, Drive pin 15 with C\ :sub:`H` on pin 3


What conclusions can we draw from these pedestal error tests? Only that not all switches will have the same charge injection and which pin is driven and which pin the hold capacitor is connected to matters.

Extra Credit: Charge injection cancelation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an extra credit exercise read through this :adi:`Circuit Design Note <media/en/technical-documentation/application-notes/an-1515.pdf>` on a technique to reduce or cancel the charge injection from the sampling switch. Figure 14 is from the document. The suggested design in the document uses different components. Your task is to implement the same design but using the same AD8542 amplifiers, the LTC1043 as the switches and same size Hold capacitor while using a single +5 V power supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-14.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 14.


A second switch, SW1, which operates in parallel with sampling SW2, is included in this circuit to reduce pedestal error. Because both switches are at the same potential, they have similar transients, which act as a common-mode signal to the op amp, thereby minimizing charge injection effects.

Inverting THA configuration:
----------------------------

A second inverting THA configuration is shown in figure 15. The second amplifier is now configured as an inverting integrator with the Hold capacitor C\ :sub:`H` acting as the integrator capacitor. The DC gain of the stage is set by resistors R\ :sub:`1` and R\ :sub:`2` and they are 1.5 KΩ. Also try using 10 KΩ for R\ :sub:`1` and R\ :sub:`2` and 1 nF for C\ :sub:`H`. How does that change the response of the circuit?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-15.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 15, Inverting Closed loop, Virtual Ground switched THA Design


Perform the same droop and pedestal tests on this configuration and report your results comparing them to the cascade of followers circuit.

Appendix:
---------

If you are using one of the older model ALM1000 boards with the 6 pin Analog I/O connector you can only use the I/O channels as either an output or an input. This makes it very hard to simultaneously drive both the analog and S/H inputs while observing more than one other node, like the THA output. If you are using one of the new model (F) ALM1000 boards with the 8 pin Analog I/O connector then you can use the Split I/O modes in ALICE. This will allow you to drive both the Analog input sine wave and S/H square wave input with the AWG output pins for CHA and CHB while observing other signals with the AIN and BIN scope input pins.

Another alternative would be to use some other signal source. One possible source for the analog input and S/H drive signals might be the stereo audio (headphone) output from the sound card on your computer, laptop, tablet, or smart phone. There are a number of function generator programs or apps available for download on the web. The ALP2000 Analog Parts Kit contains an audio connector adapter break out board (BOB) that can be used with a male to male headphone extension cable to connect to the breadboard as shown in figure 16. The left and right outputs need to be AC coupled by two capacitors and DC biased to the center of the 0-5 V range of the ALM1000. Any value around 1 uF should work. If the caps are polarized the + end should be connected to the resistors that set the DC level equal to +2.5 V. 47 KΩ is a good value for the resistors.

It is important to note that the ground of the audio connector will likely be shorted to the USB ground that the ALM1000 uses if both are connected to the same computer. So be careful how you connect the ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-16.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16, stereo audio output connector


Adjusting the internal oscillator frequency of the LTC1043
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Cosc pin can be used with an external capacitor, Cosc, connected from Pin 16 to Pin 17, to modify the internal oscillator frequency. If Pin 16 is floating, the internal 24pF capacitor, plus any external inter-pin capacitance, sets the oscillator frequency around 190 KHz with 5V supply. The typical performance characteristics curves in the datasheet provide the necessary information to set the oscillator frequency for various power supplies. Pin 16 can also be driven with an external clock to override the internal oscillator.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-tha-fig-17.png
   :align: center
   :width: 600px

**For Further Reading:**

| :adi:`MT-090: Sample-and-Hold Amplifiers <media/en/training-seminars/tutorials/MT-090.pdf>`
| :adi:`AN270: Applying IC Sample-Hold Amplifiers <media/en/technical-documentation/application-notes/4886613927731859762198006746AN270.pdf>`
| :adi:`CN0058: Sample-and-Hold Circuit Note <media/en/technical-documentation/application-notes/an-1515.pdf>`
| :adi:`MT-088: Analog Switches and Multiplexer Basics <media/en/training-seminars/tutorials/MT-088.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
