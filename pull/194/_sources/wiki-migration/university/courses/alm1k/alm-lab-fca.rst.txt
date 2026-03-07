Activity: Folded Cascode Multi-stage Amplifier
==============================================

Objective:
----------

The objective of this lab activity is to investigate the folded cascode configuration of a multistage (two transistor) amplifier.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A conventional combination of a common emitter amplifier with a stacked common base ( cascode ) stage using the same type device (i.e. both NPN or both PNP ) requires at least two V\ :sub:`BE` and two V\ :sub:`SAT` of supply headroom. This can limit the available signal swing for low supply voltages. The folded cascode which uses one NPN and one PNP device requires as little as one V\ :sub:`BE` and one V\ :sub:`SAT` of supply headroom. This allows wider signal swing operation than the stacked cascode / common emitter configuration. In figure 1 PNP Q\ :sub:`1` forms an emitter degenerated common emitter amplifier with emitter resistor R\ :sub:`1`, and collector resistor R\ :sub:`2`. NPN Q\ :sub:`2` acts as a common base or cascode stage with its emitter connected to the collector of Q\ :sub:`1`.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - small signal PNP transistor, Q1 ( 2N3906 or similar )
| 1 - small signal NPN transistor, Q2 ( 2N3904 or similar )
| 3 - 1 KΩ resistors

Directions:
~~~~~~~~~~~

Build the two transistor folded cascode amplifier circuit shown in figure 1 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-fca_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Folded Cascode Circuit


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator should be configured for a 100 Hz Sine wave with 3.0 volt Max value and 2.0 V Min value. The channel B scope input, CB-H, is used to alternately measure the voltage at the collector and emitter of Q\ :sub:`2` and the emitter of Q\ :sub:`1`. To compare these waveforms at the same time use the Snap-Shot option to save and display reference waveforms. To measure the input to output gain, the CB-V / CA-V Math waveform along with the input offset feature can be used.

Procedure:
~~~~~~~~~~

Using the measurement plots and data taken calculate the input to output voltage gain.

The voltage at the emitter of Q\ :sub:`1` will be 180 degrees out of phase with the voltage at the collector of Q\ :sub:`2`. Using the DC shape for CA-V adjust its value until the two voltages are equal, i.e. the voltage across R\ :sub:`1` is equal to the voltage across R\ :sub:`L`. How does the voltage across R\ :sub:`1`, R\ :sub:`L` relate to the voltage across R\ :sub:`2`?

Place another 1 KΩ resistor in parallel with R\ :sub:`2`. Repeat the above tests and explain any differences you measure.

Questions:
~~~~~~~~~~

What is the maximum peak to peak output voltage swing that can be produced with the folded cascode stage as shown in figure 1? How does that relate to the constant voltage applied to the base of Q\ :sub:`2`?

What limits the possible maximum and minimum output voltage seen at the collector of Q\ :sub:`2` and why?

What limits the possible maximum and minimum input voltage at the base of Q\ :sub:`1` and why?

**For Further Reading:**

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
