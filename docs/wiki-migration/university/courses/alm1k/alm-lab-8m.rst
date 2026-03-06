Activity: Stabilized current source (NMOS) - ADALM1000
======================================================

Objective:
----------

The objective of this activity is to investigate the use of the zero gain concept to produce an output current which is stabilized (less sensitive) to variations of the input current level.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 2.2 KΩ Resistor ( or any similar value )
| 1 - 168Ω Resistor ( connect a 100Ω in series with a 68Ω )
| 1 - 10 KΩ Resistor
| 2 - small signal NMOS transistors (enhancement mode CD4007 or ZVN2110A)

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 1. The voltage output of channel A, CA-V, drives one end of resistor R\ :sub:`1`. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor M\ :sub:`1` are connected as in previous zero gain amplifier activity. Since the V\ :sub:`GS` of M\ :sub:`2` is always smaller than the V\ :sub:`GS` of M\ :sub:`1`, you should, if possible, select M\ :sub:`1` and M\ :sub:`2` from your inventory of devices such that (at the same drain current) M\ :sub:`2`'s V\ :sub:`GS` is less than M\ :sub:`1`'s V\ :sub:`GS`. The gate of transistor M\ :sub:`2` is connected to the zero gain output at the grain of M\ :sub:`1`. R\ :sub:`3`, connected between the +5 V supply and the drain of M\ :sub:`2`, is used along with the channel B scope input, CB-H, to measure the drain current.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab8m_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NMOS Stabilized current source


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator is set to the SVMI mode and should be configured for a 100 Hz triangle wave with 4.5 volt Max and 1.0 V Min value. The input of scope channel B is used to display the stabilized output current at the drain of M\ :sub:`2`. The voltage seen at the drain of M\ :sub:`2` is an inverted version of the current. That is to say that as the current in M\ :sub:`2` increases the voltage decreases. You can use the gain and offset values for CB to shift the plot down ( set offset to the maximum voltage ) and invert the plot by setting the gain to -1.

Procedure:
~~~~~~~~~~

The zero gain amplifier can be used to create a stabilized current source. Because the voltage seen at the drain of transistor M\ :sub:`1` is now more constant with changes in the input supply voltage as represented by CA-V, it can be used as the gate voltage of M\ :sub:`2` to produce a much more constant current in transistor M\ :sub:`2`.

Questions:
~~~~~~~~~~

This circuit is sometimes referred to as a peaking current source. Why do you think?

Based on the delta V\ :sub:`GS` of M\ :sub:`1` and M\ :sub:`2`, at what input and output current would the gain be zero for different values of R\ :sub:`2`?

An exercise for the student is to plot the "stabilized" output current for all the various combinations of M\ :sub:`1` and M\ :sub:`2` from the available inventory of transistors. Why does it vary and by how much?

The output of the simple peaking current source is always less than the input current at the peak by a substantial fraction. What is that fraction and why?

How can the circuit be changed to make the output a larger fraction of, or even equal to or larger than, the input?

The output current has a narrow peak. How could multiple copies of the peaking current source be combined to produce a much wider, flatter peak?

**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
