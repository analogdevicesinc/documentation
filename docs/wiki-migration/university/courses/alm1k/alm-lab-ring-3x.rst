Activity: Frequency Multiply by 3 CMOS Ring Oscillator
======================================================

Objective:
----------

The objective of this activity is to explore how obtain a 3X multiplied frequency from a three stage ring oscillator made from CMOS inverters.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

In this earlier :doc:`lab activity the CMOS inverter ring oscillator </wiki-migration/university/courses/alm1k/alm-lab-ring-osc>` was examined. In this lab a technique that uses the supply current pulses to obtain a output frequency that is 3 times higher than the basic ring oscillator produces is examined.

A ring oscillator is an odd number (N) of inverting stages connected in series with the output fed back to the input as shown in figure 1. The frequency of oscillation is inversely proportional to the number of stages and the propagation delay times, and is governed by the following:

:math:`F = 1 / ( tp_LH + tp_HL) \times n`

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-ring-osc-f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1, N stage ring oscillator


To increase the frequency of the ring oscillator either faster stages must be used or fewer stages. Three is the fewest possible number of stages.

Each inverter stage pulls a short pulse of current from the positive supply each time its output transitions from low to high as it charges the capacitance seen on its output. If all the pulses from each stage in the ring are combined there will be one pulse per stage each cycle around the ring. So for a three stage ring there will be three current pulses per cycle, making the overall frequency of the current pulses 3 times the oscillator frequency.

If we include a circuit to convert these current pulses to a voltage we can produce an output signal at the multiplied frequency. Two different current sensing techniques will be examined.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – CD4007 CMOS array
| 3 – 0.1 uF capacitors
| 2 – 2N3906 PNP transistors
| 1 – 47 Ω resistor
| 1 – 6.8 KΩ resistor
| 1 – AD8210 current sense monitor
| 1 – 470 Ω resistor

Making inverters with the CD4007 transistor array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below in figure 2 is the schematic and pinout for the CD4007 CMOS array:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown in figure 3 is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_labcmg_f2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 3 Three Inverters


The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input. The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Directions:
~~~~~~~~~~~

To build the first version of the frequency multiplier you should connect the three inverters from the CD4007 in series to create the basic ring oscillator as shown in figure 4. Each inverter has a 0.1uF capacitor load. If you don’t have three 0.1 uF capacitors in your parts kit you can use 2 0.047 uF capacitors in parallel.

The supply current flowing into the ring oscillator at V\ :sub:`DD` ( pins 14, 2, 11) also flows through diode connected PNP transistor Q\ :sub:`1` and its emitter resistor R\ :sub:`1`. The combined voltage drop of Q\ :sub:`1` V\ :sub:`BE` and R\ :sub:`1` forms the V\ :sub:`BE` of PNP current source transistor Q\ :sub:`2`. A larger copy of the current will flow in Q\ :sub:`2` and into the collector load resistor R\ :sub:`2` converting it to a voltage signal.

Be sure that you power the circuit using the 3.3 V fixed supply from the digital I/O connector. The output frequency of the base ring oscillator is measured by connecting CB-H in Hi-Z mode to the output of the last inverter. The 3X frequency at the collector of Q\ :sub:`2` is measured by connecting CA-H in Hi-Z mode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-ring-3x-f4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4, Frequency multiply by 3 ring oscillator (V1)


Version 1 Procedure:
~~~~~~~~~~~~~~~~~~~~

Set the Trigger source as CH-B and use the Auto-Level feature.

You should see the output signal of the ring oscillator itself on channel B. Measure the frequency by using the frequency measurement function for CH-B on the Meas drop down menu. Be sure to have more than 5 cycles of the oscillation on the screen before measuring. On channel A you should see a signal at 3 time the frequency of the channel B signal. From the Meas CHA drop down menu select the CH-A Freq measurement. If the signal is either not present or is not well centered in the 0 to 3.3 V range you may need to adjust the values of R\ :sub:`1` and or R\ :sub:`2`. The amount of current in Q\ :sub:`2` is function of the relative V\ :sub:`BE` matching between the two PNP transistors. Another possible thing to try is to interchange the two transistors.

Version 2 Procedure:
~~~~~~~~~~~~~~~~~~~~

The Q\ :sub:`1` / Q\ :sub:`2` current mirror of version one can be replaced with the AD8210 current sense monitor chip as shown in figure 5. The AD8210 senses the current flowing through R\ :sub:`1` into the ring oscillator and amplifies the signal by 20 and it appears on the output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-ring-3x-f5.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 5, Sensing the current pulses with the AD8210 (V2)


Remove Q\ :sub:`1`, Q\ :sub:`2`, R\ :sub:`1` and R\ :sub:`2` from your bread board and add the AD8210 and a new R1 as shown. The pinout for the AD8210 is included in figure 6. Note the AD8210 is powered from the +5 V supply not the +3.3 V supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/ad8210-pinout.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 6, AD8210 pinout


Again you should see the output signal of the ring oscillator itself on channel B and on channel A you should see a signal at 3 time the frequency of the channel B signal. If the output of the AD8210 is clipped you may need to reduce the value of R\ :sub:`1`.

Figure 7 is an example of what the waveforms should look like.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-ring-3x-f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Typical waveforms


Compare the 3X frequency waveform results you measured using the Version 1 current to voltage technique and the Version 2 technique.

Comment on using the current pulses in ground to produce the multiplied frequency output vs. using the positive supply current pulses.

Extra credit:
~~~~~~~~~~~~~

The output of the oscillator is not a very good square wave with sharp rise and fall times and an output that swings all the way from ground to the power supply voltage. As extra credit use a ZVN3310 NMOS transistor and a ZVP2210A PMOS transistor to make another CMOS inverter. Connect the 3X output of the ring oscillator to the input of your new inverter and observe the buffered ( amplified ) signal at the output. How much closer to a square wave is this signal?

**For Further Reading:**

| `Ring oscillator <https://en.wikipedia.org/wiki/Ring_oscillator>`_
| :adi:`AD8210 datasheet <media/en/technical-documentation/data-sheets/AD8210.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
