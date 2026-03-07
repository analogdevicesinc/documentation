Activity: CMOS Inverter Ring Oscillator
=======================================

Objective:
----------

The objective of this activity is to understand the operation of a ring oscillator made from CMOS inverters.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A ring oscillator is an odd number (N) of inverting stages connected in series with the output fed back to the input as shown in figure 1. A ring oscillator can be made with a mixture of inverting and non-inverting stages, provided the total number of inverting stages is odd. The ring oscillator and related circuits are fundamental building blocks used as clock oscillators in computers and carrier frequency generator phase locked loops in wireless communications. It is also a fundamental circuit for evaluating the intrinsic speed of a CMOS logic process. The frequency of oscillation is inversely proportional to the number of stages and the propagation delay times, and is governed by the following:

:math:`F = 1 / ( tp_LH + tp_HL) \times n`

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-ring-osc-f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1 N stage ring oscillator


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – CD4007 CMOS array
| 3 – 0.1 uF capacitors
| 3 – 0.01 uF capacitors

Making inverters with the CD4007 transistor array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below in figure 2 is the schematic and pinout for the CD4007 CMOS array:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 450px

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

First you should connect the three inverters from the CD4007 in series to create a delay line of sorts as shown in figure 4. Start with each inverter having a 0.1uF capacitor load. If you don’t have three 0.1 uF capacitors in your parts kit you can use 2 0.047 uF capacitors in parallel. Be sure that you power the circuit using the 3.3 V fixed supply from the digital I/O connector. A square wave from CA-V will be applied to the input of the first inverter and the delay of each stage will be measured by connecting CB-H in Hi-Z mode to the output of each inverter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-ring-osc-f4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4 Three stage delay line


Delay Line Procedure:
~~~~~~~~~~~~~~~~~~~~~

Set AWG A to SVMI mode, shape square. Set the Min value to 0 V and the Max to 3.3 V. Set the frequency to 250 Hz. Set channel B to Hi-Z mode.

1. With C\ :sub:`1`, C\ :sub:`2` and C\ :sub:`3` all equal to 0.1uF measure the propagation delay for both rising and falling edges at each inverter stage output. Record all your measurements in your lab report and capture any relevant waveforms to include in the report as well.

2. Connect the power to +5V and perform the same procedure as in (1) to measure the propagation delay times. Be sure to increase the Max value of the AWG A square wave to 5 V for these measurements.

3. Connect the power back to +3.3V and change all of the capacitors to 0.01 uF and measure the propagation delay times again. If you don’t have three 0.01 uF capacitors in your parts kit you can use 2 0.0047 uF capacitors in parallel. Be sure to lower the Max value of the AWG A square wave to 3.3 V for these measurements.

4. Try to measure the delay with all three capacitors removed.

Ring Oscillator Procedure:
~~~~~~~~~~~~~~~~~~~~~~~~~~

To make the three inverter delay line into a ring oscillator simply connect the output of the last stage back to the input of the first. Be sure to disconnect the channel A square wave generator from your circuit when you do this. Start this step with C\ :sub:`1`, C\ :sub:`2` and C\ :sub:`3` all equal to 0.1uF.

Set the Trigger source as CH-B and use the Auto-Level feature. You don’t need to display CH-A at this point so you can turn off the CH-A trace. Measure the frequency by using the frequency measurement function for CH-B on the Meas drop down menu. Be sure to have at least 10 cycles of the oscillation on the screen before measuring.

1. How well does your period (1/frequency) measurement correspond to the sum of the inverter transition times measured in the delay line experiment.

2. Connect the power to +5V and perform the same procedure as in (1) to measure the frequency of oscillation. How does this frequency compare with the frequency you obtained in step 1?

3. Connect the power back to +3.3V and change all of the capacitors to 0.01 uF and measure the oscillation frequency of the oscillator again. This frequency is likely to be higher, why do you think this is the case?

4. Based on your delay time measured in delay line step 4 predict the frequency that the circuit will oscillate at with all the capacitors removed. Try this and see what happens.

Extra credit:
~~~~~~~~~~~~~

The output of the ring oscillator is not a very good square wave with sharp rise and fall times and an output that swings all the way from ground to the power supply voltage. As extra credit use a ZVN3310 NMOS transistor and a ZVP2210A PMOS transistor to make another CMOS inverter. Connect the output of the ring oscillator to the input of your new inverter and observe the buffered ( amplified ) signal at the output. How much closer to a square wave is this signal?

**For Further Reading:**

`Ring oscillator <https://en.wikipedia.org/wiki/Ring_oscillator>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
