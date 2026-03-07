Activity: Three Stage Amplifier - ADALM1000
===========================================

Objective:
----------

The objective of this Lab activity is to gain insight into the push pull output stage (Class B), understand crossover distortion and the use of negative feedback to reduce errors. The amplifier combines an emitter degenerated NPN common emitter amplifier first stage in cascade with a PNP common emitter second stage and an NPN/PNP push-pull output stage. Negative feedback from the output to the emitter of the first NPN stage determines the overall amplifier gain.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage/measure current, –V is added as in CA-V or when configured to force current /measure voltage, –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-mstage-f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Follower with gain greater than one


Materials:
~~~~~~~~~~

| ADALM1000 Active Learning module
| 1 – 1 KΩ resistor
| 2 – 2 KΩ resistors (each can be made from 2 1 KΩ resistors in series)
| 2 – 10 KΩ resistors
| 2 – small signal NPN transistor (2N3904 Q\ :sub:`1` Q\ :sub:`3`)
| 2 – small signal PNP transistor (2N3906 Q\ :sub:`2` Q\ :sub:`4`)

Directions:
~~~~~~~~~~~

Build the amplifier as shown in figure 2 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-mstage-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, three stage amplifier


The amplifier consists of three stages, a low gain degenerated common emitter Q\ :sub:`1`, a high gain stage, Q\ :sub:`2` and the push-pull output stage, Q\ :sub:`3` and Q\ :sub:`4`. Q\ :sub:`3` and Q\ :sub:`4` are commonly referred to as a push pull configuration. NPN Q\ :sub:`3` sources (push) current to the output load on the positive half cycle while PNP Q\ :sub:`4` sinks current from the load on the negative half cycle (pull). The amplifier is class B since only one output transistor drives the load (R\ :sub:`L`) at any given time.

**Q\ 3 & Q\ 4 Analysis**

The two transistors are emitter followers so the gain from their bases to the output is one, but with a region where both are off, the crossover region. This crossover distortion is caused by the base-emitter diode drop. Note that the PNP transistor configuration is drawn with the emitter pointing up toward the positive supply which is the reverse of the NPN configuration where the emitter points toward ground (the most negative voltage).

**Q\ 2 Analysis**

PNP Q\ :sub:`2` is configured as a common emitter amplifier stage with R\ :sub:`4` as the collector load. It's similar to the NPN configuration with the appropriate change in signs for the voltages. Since the emitter is tied to +5 volts, any change at the collector of Q\ :sub:`1` changes the V\ :sub:`BE` of Q\ :sub:`2` which in turn results in an exponential change in the emitter current Ie for Q\ :sub:`2`. Assuming sufficiently large β, Ic is approximately equal to Ie.

The gain is given by:

:math:`\displaystyle A_v = -\frac{beta_0 R_L}{beta_0/g_m} = -g_m R_L`

Note that with feedback, variations in the gain of the second stage, Q\ :sub:`2` (570) will have negligible effect on the overall gain.

Because of the use of 5% resistors and variations in transistors, the quiescent output voltage Vout is mostly likely not centered exactly on 2.5 V (one half of the 5 V power supply ).

Procedure:
~~~~~~~~~~

Using AWG channel A, apply a 500 Hz sinewave, 200 mv p-p signal to the amplifier. Verify that the gain is ~5.0.

This amplifier has one drawback, the crossover distortion about 2.5 volts where the current delivered to the load R\ :sub:`L` goes to zero. Using AWG channel A, input a 500 Hz signal to generate a 4 Vpp output. Note the crossover distortion.

The crossover distortion is really apparent with a very low input signal. Attach a speaker to your amplifier. Feed the output from the function generator or your mp3 player/smartphone and see if you can hear the distortion. The cross distortion is more apparent a low volume. The distortion can be eliminated with a pair of diodes, a V\ :sub:`BE` multiplier or the addition of NPN and PNP emitter followers as we will investigate in the next section.

Lab Report:

| (1) With no input, show that the quiescent operating point for Vout is 2.5V.
| (2) Demonstrate operation of your amplifier showing cross over distortion.

Reducing the cross over distortion:
-----------------------------------

We can reduce the voltage range where both output transistors are off by changing the output stage from class B to class A-B. By inserting two additional transistors (as emitter followers) we create two different bias voltages for the bases of Q\ :sub:`3` and Q\ :sub:`4`. This reduces the voltages where both are off. If the difference between these two bias voltages is large enough there will be, in fact, a small region where both are slightly on.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 2 – 4.7 KΩ resistors
| 1 – small signal NPN transistor (2N3904 Q\ :sub:`6`)
| 1 – small signal PNP transistor (2N3906 Q\ :sub:`5`)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-mstage-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Low crossover distortion output stage


**For Further Reading:** **Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/electronics>`
