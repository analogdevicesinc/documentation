Activity: Vector Summing Amplifier, For ADALM1000
=================================================

Objective:
----------

Adding and/or subtracting analog signals is potentially the most common function performed by an op-amp. This activity will investigate single op-amp circuits for adding two (or more) analog signals.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 1 – OP484 quad rail to rail amplifier
| 3 – 100 KΩ resistors
| 1 – 470 Ω resistor
| 1 – 220 Ω resistor
| 1 – 1 uF capacitor

Directions:
~~~~~~~~~~~

Build the inverting summer shown in Figure 1. R\ :sub:`5` is added to stabilize the output of the OP484 when using large feedback resistances due to the large input capacitance of the CH-B input. One input signal is provided directly from the CH-A AWG output to 100 KΩ resistor R\ :sub:`1`. Another input signal through 100 KΩ resistor R\ :sub:`2` to the inverting input terminal is driven through a phase shifting low-pass RC filter, C\ :sub:`1` and R\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labvsa_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Inverting summing amplifier with CH-A applied at both V\ :sub:`1` and V\ :sub:`2`\


Procedure:
~~~~~~~~~~

Set CH-A to SVMI mode and shape sine. Set the Min value to 1.5 V and the Max value to 3.5 V. Set the frequency of AWG channel A to 500 Hz. Set CH-B to Hi-Z mode.

Measure the amplifier output with each input applied individually and the other input "grounded" (disconnect source from the grounded input) and for when both inputs are applied simultaneously. Save these three waveforms and measure their relative phase and amplitude with respect to CH-A.

Step one, connect the left end of R\ :sub:`4` to the 2.5 V common rail. With both CA-V and CB-V traces displayed measure the relative phase of the two signals. Because the amplifier inverts it should be 180 degrees. Also measure and record the amplitudes ( p-p ) of both traces. Save a snap shot of the CB-V trace ( or save a copy of the VBuffB array to another array ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labvsa_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, CH-A applied at just V\ :sub:`1`.


In step two connect the V\ :sub:`1` end of R\ :sub:`1` to the 2.5 V common rail and connect CH-A to the left end of R\ :sub:`4` as shown in figure 3. Now a delayed ( or phase shifted ) version of CH-A will be applied at V\ :sub:`2`. With both CA-V and CB-V traces displayed measure the relative phase of the two signals. Now because of the delay the relative phase will not be 180 degrees. Also measure and record the amplitudes ( p-p ) of both traces. Save a snap shot of the CB-V trace ( or save a copy of the VBuffB array to another array ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labvsa_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, CH-A applied at just V\ :sub:`2`\


As step three apply CH-A to both V\ :sub:`1` and the R\ :sub:`4` 470Ω resistor (as in figure 1). With both CA-V and CB-V traces displayed measure the relative phase of the two signals. Also measure and record the amplitudes ( p-p ) of both traces. Now compare the output (CB-V) trace for this step with your saved output traces from step 1 and step 2.

Show that the output signal in step 3 is the inverted sum of the V\ :sub:`1`\ and V\ :sub:`2` signals.

Repeat the measurements using a square wave and a triangle wave for the input function.

Appendix:
~~~~~~~~~

By using one of the other amplifiers in the OP484 as a comparator, the sine wave from channel A can be converted into a square wave. The 0 to 5 V square wave at pin 1 of the OP484 is derived from the sine wave. The amplitude applied at V\ :sub:`2` is determined by the ratio of R\ :sub:`6`/(R\ :sub:`6`\ +R\ :sub:`4`). R\ :sub:`7` limits the current into the inverting input at pin 2 when the differential inputs are overdriven. The modified version of the summing amplifier test circuit shown in figure 4 outputs the sum of the sine and square waves.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labvsa_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Sum of sine and square waves


As an additional note, the square wave can be delayed with respect to the sine wave by adding a capacitor from pin 2 to the +2.5 V common rail ( at pin 3 ). The capacitor along with R\ :sub:`7` produces an RC low pass filter.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/vector_summing_amp_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/vector_summing_amp_ltspice`

**For Further Reading:**

:adi:`Inverting Summing Amplifier <media/en/training-seminars/tutorials/MT-214.pdf>`

**Return to the ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
