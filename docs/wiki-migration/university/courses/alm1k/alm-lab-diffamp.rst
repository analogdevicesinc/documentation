Activity: Difference Amplifier, For ADALM1000
=============================================

Objective:
----------

Adding and/or subtracting analog signals is potentially the most common function performed by an op-amp. This activity will investigate single op-amp circuits for subtracting two analog signals.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 1 – OP484 quad rail to rail amplifier
| 4 – 100 KΩ resistors
| 1 – 470 Ω resistor
| 1 – 220 Ω resistor
| 1 – 1 uF capacitor

Directions:
~~~~~~~~~~~

Build the difference amplifier shown in figure 1. R\ :sub:`6` is added to stabilize the output of the OP484 when using large feedback resistances due to the large input capacitance of the CH-B input. One input signal ( V\ :sub:`1` ) is provided directly from the CH-A AWG output to 100 KΩ resistor R\ :sub:`1`. Another input signal ( V\ :sub:`2` ) through 100 KΩ resistor R\ :sub:`2` to the non-inverting input terminal is driven through a phase shifting low-pass RC filter, C\ :sub:`1` and R\ :sub:`5`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labdifa_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Difference amplifier with CH-A applied at both V\ :sub:`1` and V\ :sub:`2`\


Procedure:
~~~~~~~~~~

Set CH-A to SVMI mode and shape sine. Set the Min value to 1.5 V and the Max value to 3.5 V. Set the frequency of AWG channel A to 500 Hz. Set CH-B to Hi-Z mode.

Measure the amplifier output with each input applied individually and the other input "grounded" (disconnect source from the grounded input) and for when both inputs are applied simultaneously. Save these three waveforms and measure their relative phase and amplitude with respect to CH-A.

Step one, connect the left end of R\ :sub:`5` to the 2.5 V common rail. With both CA-V and CB-V traces displayed measure the relative phase of the two signals. Because the amplifier inverts signal V\ :sub:`1` it should be 180 degrees. Also measure and record the amplitudes ( p-p ) of both traces. Save a snap shot of the CB-V trace ( or save a copy of the VBuffB array to another array ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labdifa_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, CH-A applied at just V\ :sub:`1`.


In step two connect the V\ :sub:`1` end of R\ :sub:`1` to the 2.5 V common rail and connect CH-A to the left end of R\ :sub:`5` as shown in figure 3. Now a delayed ( or phase shifted ) version of CH-A will be applied at V\ :sub:`2`. With both CA-V and CB-V traces displayed measure the relative phase of the two signals. The signal at V\ :sub:`2` is not inverted by the amplifier, however because of the RC delay the relative phase will not be 0 degrees. Also measure and record the amplitudes ( p-p ) of both traces. Save a snap shot of the CB-V trace ( or save a copy of the VBuffB array to another array ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labdifa_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, CH-A applied at just V\ :sub:`2`\


As step three apply CH-A to both V\ :sub:`1` and the R\ :sub:`5` 470Ω resistor (as in figure 1). With both CA-V and CB-V traces displayed measure the relative phase of the two signals. Also measure and record the amplitudes ( p-p ) of both traces. Now compare the output (CB-V) trace for this step with your saved output traces from step 1 and step 2.

Show that the output signal in step 3 is the difference of the V\ :sub:`1`\ and V\ :sub:`2` signals.

Repeat the measurements using a square wave and a triangle wave for the input function.

Appendix:
~~~~~~~~~

By using one of the other amplifiers in the OP484 as an all-pass filter, the waveform from channel A can be delayed by a fixed amount of time. An all-pass filter is a signal processing filter that passes all frequencies equally with a gain of one in this case, but changes the phase relationship among various input frequencies. It does this by varying its phase shift as a function of frequency which is the same as adding a fixed time shift. The R\ :sub:`8`, C\ :sub:`1` time constant determines the amount of time shift.

The modified version of the difference amplifier test circuit shown in figure 4 outputs the difference of the input sine wave and a time shifted version of the sine wave.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-labdifa_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Difference of delayed and un-delayed signals


As an additional note, other wave shapes such as a square wave or triangle wave can be delayed with respect to the input signal.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/difference_amp_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/difference_amp_bb`

**For Further Reading:**

| :adi:`Difference and Current Sense Amplifiers <media/en/training-seminars/tutorials/MT-068.pdf>`
| :adi:`Difference Amplifier Forms Heart of Precision Current Source <en/analog-dialogue/articles/diff-amp-heart-of-precision-current-source.html>`
| :adi:`A Deeper Look into Difference Amplifiers <library/analogDialogue/archives/48-02/diff_amp.html>`
| :adi:`Adjusting the Gain of a Fixed-Gain Difference Amplifier <media/en/analog-dialogue/raqs/raq-issue-171.pdf>`
| :adi:`Simple Ambient Light Sensor Circuit <en/analog-dialogue/articles/simple-ambient-light-sensor-circuit.html>`
| :adi:`MT-202 All Pass Filters <media/en/training-seminars/tutorials/MT-202.pdf>`
| `All Pass Filter <https://en.wikipedia.org/wiki/All-pass_filter>`__

**Return to the ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
