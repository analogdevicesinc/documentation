Activity: Op-Amp Gain Bandwidth Product, For ADALM1000
======================================================

Objective:
----------

The objective of this activity is to explore a key parameter that affects the performance of op-amps at high frequencies. The parameter is the gain-bandwidth product (GBW) or unity gain bandwidth.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

**Gain-bandwidth product:**

The forward gain, G is defined as the gain of the op-amp when a signal is fed differentially into the amplifier with no negative feedback applied. This gain is ideally infinite at all frequencies, but in a real op-amp is finite, and depends on the frequency. At low frequency the gain is maximum, decreases linearly with increasing frequency, and has a value of one at the frequency commonly referred to as the unity gain or cut-off frequency F\ :sub:`cf` (in equation form, G\ :sub:`fc` = 1). For the OP97 op-amp, the unity gain frequency is 900 KHz, the open-loop gain at this frequency is simply one. This is also the Closed-Loop Bandwidth or the maximum frequency when the feedback is configured with a closed loop gain of 1.

G\ :sub:`f` is defined as the gain-bandwidth product, GBW, and for all input frequencies this product is constant and equal to fc. The gain can be specified as a simple number (magnitude) or in dB.

Figure 1, from the OP97 datasheet, graphically illustrates this relationship. When feedback is provided, as in an inverting amplifier, the gain is given by G = –R\ :sub:`2`/R\ :sub:`1`; however, it must be recognized that the magnitude of this gain can never exceed the gain as given by the gain-bandwidth product.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-gbw-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 OP97 Open-Loop Gain, Phase vs. Frequency


The OP97 amplifier has a pin ( pin 5 ) which allows the user to connect an external frequency compensation capacitor to effectively lower the gain-bandwidth product. Figure 2 shows the change in bandwidth for different external capacitors.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-gbw-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, OP97 Gain Bandwidth Product vs external compensation capacitor


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless breadboard and jumper wires
| 1 – OP97 op-amp
| 1 – 100 KΩ resistor
| 1 – 47 KΩ resistor
| 2 – 100 Ω resistors
| Various other op-amps from parts kit

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 3 on your solderless breadboard to measure the frequency response of a inverting amplifier configured with a closed loop gain of 1000. Because the circuit’s gain is so high, the circuit needs to be driven with a very small input signal. Since the AWG generator cannot accurately produce small signals with low noise, a 1/1000 voltage divider, R\ :sub:`3`, R\ :sub:`4`\ \||R\ :sub:`1`, is used to reduce the 2V p-p sine signal to 2 mV p-p at the inverting amplifier input. R\ :sub:`4` and R\ :sub:`1` are effectively in parallel due to the "virtual ground" at pin 2. The parallel combination of R\ :sub:`4` and R\ :sub:`1` will be 50 Ω which with the 47 KΩ R\ :sub:`3` results in a divider ratio close to 1/1000.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-gbw-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Inverting amplifier with gain of 1000


Procedure:
~~~~~~~~~~

Set CH-A to SVMI mode and shape sine. Set the Min value to 1.5 V and the Max value to 3.5 V. Set the frequency of AWG channel A to 250 Hz. Set CH-B to Hi-Z mode. To insure that the amplifier output is the correct amplitude and not clipped, use the ALICE Oscilloscope tool to measure the signal in the time domain. Because the attenuation of the voltage divider is approximately the same as the inverting gain the output should be inverted and have about the same amplitude as the input from AWG CH-A. The input offset voltage of the op-amp is also multiplied by the gain of 1000. If the input offset is greater than 1 or 2 mV adjusting the average level of the AWG A signal will not be sufficient to bring the output signal within range. For those cases where the input offset voltage is large injecting a small DC correction voltage at the non-inverting input will be necessary.

R\ :sub:`5` can be optionally added if the amplifier shows any instability ( small oscillations ) when driving the relatively large input capacitance of CH-B.

Use the ALICE Bode plotter tool to measure the gain ( and optionally the phase ) response for frequencies in the range of 100 to 20 KHz. For the sweep generator set the Start Frequency to 100 Hz and the Stop Frequency to 20000 Hz. Select CH-A as the sweep source, the number of steps to 300 and Single sweep. Under the FFT Window select Flat-top window. Under Options be sure that Cut-DC is selected. Under Curves select CHA-dBV, CHB-dBV and CHB-dB – CHA-dB. Click on Run and you should get a plot that looks something like figure 4. Save a copy of the plot to include in your Lab report.

Find the -3dB frequency or F\ :sub:`cf` on the Bode plot ( magenta curve in figure 4). Calculate the GBW by multiplying this by the absolute value of the gain, R\ :sub:`2`/R\ :sub:`1` or 1000 in this case.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-gbw-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, typical OP97 Bode Plot Gain = 1000


Based on figure 2, connect different values of capacitors from pin 5 of the OP97 to ground. Try values in the range of 100 pF to 10 nF and see how your results compare to figure 2.

From your parts kit substitute other op-amp models and make the same frequency response plots and calculate the GBW. Be sure to properly connect each version according to its package and pinout. Single op-amps tend to have similar pinouts but not the same as duals or quads. Compare your measured results to each amplifier’s datasheet specification for GBW.

Note: the ADTL082 amplifier requires a minimum of 8 volts for the power supply and will not operate properly with just the +5 Volts available from the ALM1000. The minus supply of the ADTL082 can be connected to a 3 V battery connected from ground ( battery + ) to pin 4 ( -Vs ) such that -3V is provided.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/op_amp_gain_bandwidth_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/op_amp_gain_bandwidth_ltspice`

**For Further Reading:**

Here is a good technical paper on how to make :adi:`Simple Op Amp Measurements <en/analog-dialogue/articles/simple-op-amp-measurements.html>`.

| :adi:`OP97 datasheet <media/en/technical-documentation/data-sheets/OP97.pdf>`
| :adi:`OP27 datasheet <media/en/technical-documentation/data-sheets/OP27.pdf>`
| :adi:`OP37 datasheet <media/en/technical-documentation/data-sheets/OP37.pdf>`
| :adi:`OP484 datasheet <media/en/technical-documentation/data-sheets/OP184_284_484.pdf>`
| :adi:`OP482 datasheet <media/en/technical-documentation/data-sheets/OP282_482.pdf>`
| :adi:`AD8541 datasheet <media/en/technical-documentation/data-sheets/AD8541_8542_8544.pdf>`
| :adi:`ADTL082 datasheet <media/en/technical-documentation/data-sheets/ADTL082_084.pdf>`
| :adi:`MT-033 <media/en/training-seminars/tutorials/MT-033.pdf>`
| :adi:`MT-045 <media/en/training-seminars/tutorials/MT-045.pdf>`
| `Gain-Bandwidth Product <https://en.wikipedia.org/wiki/Gain%E2%80%93bandwidth_product>`_

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
