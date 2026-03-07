Activity: The Hartley Oscillator
================================

Objective:
----------

Oscillators come in many forms. In this lab activity we will explore the Hartley configuration which uses a taped inductor divider to provide the feedback path.

Background:
-----------

The Hartley Oscillator is a particularly good circuit for producing fairly low distortion sine wave signals in the range, 10kHz to 100KHz. The Hartley configuration can be recognized by its use of a tapped inductor divider (L\ :sub:`1` and L\ :sub:`2` in figure 1). The frequency of oscillation can be calculated in the same way as any parallel resonant circuit, using:

:math:`F_R = 1 / 2 \pi sqrt(LC)`

Where L = total inductance of L\ :sub:`1` and L\ :sub:`2`

Figure 1 shows a typical Hartley oscillator. The frequency determining parallel resonant tuned circuit is formed by L\ :sub:`1`, L\ :sub:`2` and C\ :sub:`1` and is used as the collector load impedance of the common base amplifier Q\ :sub:`1`. This gives the amplifier a high gain only at the resonant frequency. This configuration of the Hartley oscillator uses a common base amplifier, the base of Q\ :sub:`1`\ is biased to an appropriate DC level by resistor divider R\ :sub:`1` and R\ :sub:`2` but is connected directly to an AC ground by C\ :sub:`3`. In the common base mode the output voltage waveform at the collector, and the input signal at the emitter are in phase. This ensures that the fraction of the output signal from the node between L\ :sub:`1` and L\ :sub:`2`, fed back from the tuned collector load to the emitter via the coupling capacitor C\ :sub:`2` provides the required positive feedback.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ahosc_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1, Basic Hartley Oscillator


C\ :sub:`2` also forms a low frequency time constant with the emitter resistor R\ :sub:`3` to provide an average DC voltage level proportional to the amplitude of the feedback signal at the emitter of Q\ :sub:`1`. This provides automatic control of the gain of the amplifier to give the closed loop gain of 1 required by the oscillator. The emitter resistor R\ :sub:`3` is not decoupled because the emitter node is used as the common base amplifier input. The base is connected to AC ground by C\ :sub:`3`, which will provide a very low reactance at the oscillator frequency.

Pre Lab Simulations
~~~~~~~~~~~~~~~~~~~

Build a simulation schematic of the Hartley oscillator as shown in figure 1. Calculate values for bias resistors R\ :sub:`1` and R\ :sub:`2` such that with emitter resistor R\ :sub:`3`\ set to 4.7 KΩ, the collector current in NPN transistor Q\ :sub:`1` is approximately 250 uA. Assume the circuit is powered from a +5V power supply. Be sure to keep the sum of R\ :sub:`1` and R\ :sub:`2` (total resistance greater than 10 KΩ) as high as practical to keep the standing current in the resistor divider as low as practical. Remember that C\ :sub:`3` provides an AC ground at the base of Q\ :sub:`1`. Set base decoupling capacitor C\ :sub:`3` and output AC coupling capacitor C\ :sub:`4` to 0.1uF. Calculate a value for C\ :sub:`1` such that the resonate frequency, with L\ :sub:`1` connected as 1 winding of the HPH1-1400L and L\ :sub:`2` connected as 5 windings of the HPH1-1400L, will be close to 10 KHz. Perform a transient simulation. Save these results to compare with the measurements you take on the actual circuit and to include with your lab report.

Materials:
----------

| ADALM1000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 2N3904 NPN transistor
| 1 - HPH1-1400L inductor
| 2 - 0.1 uF capacitors (marked 104)
| 2 - 0.047 uF capacitor (marked 473) (C\ :sub:`1` values as listed below )
| 2 - 0.01 uF capacitor (marked 103)
| 2 - 4.7 KΩ resistors
| 1 - 10 KΩ resistor
| 2 - 20 KΩ resistor
| 1 - 1 Meg Ω resistor

Directions:
-----------

Build The Hartley Oscillator shown in figure 2 using your solder-less breadboard. Start with the standard values as shown in the schematic for bias resistors R\ :sub:`1` and R\ :sub:`2` such that with emitter resistor R\ :sub:`3`\ set to 4.7 KΩ, the collector current in NPN transistor Q\ :sub:`1` will be approximately 250 uA. The HPH1-1400L 6 winding coupled inductor is used for L\ :sub:`1` and L\ :sub:`2`. The frequency of the oscillator should be approximately 10 KHz depending on the total number windings used and the tap connections chosen for L\ :sub:`1`, L\ :sub:`2` and C\ :sub:`1`. Start with L\ :sub:`1` as 1 winding and L\ :sub:`2` as the remaining 5 windings connected in series. This oscillator circuit can produce a sine wave output beyond the 0 to 5 V range of the ADALM1000 input at the resonate frequency set by the value chosen for C\ :sub:`1`. The AC coupling capacitor C\ :sub:`4` and the DC bias resistor R\ :sub:`4` should center to output on +2.5 V.

After experimenting with various values for C\ :sub:`1` change tap position and total number of windings used on the HPH1-1400L for the feedback.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-hartley-osc-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Hartley Oscillator


Hardware Setup:
---------------

The green squares indicate where to connect the ADALM1000 module, scope channels and power supplies. Be sure to only connect on the power supplies after you double check your wiring.

Procedure:
----------

Having finished construction the Hartley oscillator check that the circuit is oscillating correctly by connecting the +5 V power supply and connecting one of the oscilloscope channels to the AC coupled output terminal. It may be found that the value of R\ :sub:`3` is fairly critical, producing either a large distorted waveform or an intermittent low or no output. To find the best value for R\ :sub:`3`, it could be replaced by a 10 KΩ potentiometer for experimentation to find the value that gives the best wave shape and reliable amplitude.

Questions:
----------

Measure the peak to peak output voltage of the output. Measure the DC ( average ) level of the output waveform at the collector of Q\ :sub:`1` and on the other (output) side of AC coupling capacitor C\ :sub:`4`. Measure the period (time T) of the output waveform and its frequency (1/T). Compare this measured frequency to what you calculated b:

:math:`F_R = 1 / 2 \pi sqrt(LC)`

Fill in the table below with the measured frequency for other C\ :sub:`1` values. Use the values in the table as suggested options but try to include as many different values as possible using series and parallel combinations of the capacitors supplied in your parts kit. Any of the C\ :sub:`1` optional values shown below should give reliable oscillation.

+---------------------+-------------------------------------+-------------------------------------+
| C\ :sub:`1` Options | L\ :sub:`1` 1Wind L\ :sub:`2` 5Wind | L\ :sub:`1` 2Wind L\ :sub:`2` 4Wind |
+=====================+=====================================+=====================================+
| Value               | Frequency                           | Frequency                           |
+---------------------+-------------------------------------+-------------------------------------+
| 10 nF               |                                     |                                     |
+---------------------+-------------------------------------+-------------------------------------+
| 20 nF               |                                     |                                     |
+---------------------+-------------------------------------+-------------------------------------+
| 23.5nF              |                                     |                                     |
+---------------------+-------------------------------------+-------------------------------------+
| 47nF                |                                     |                                     |
+---------------------+-------------------------------------+-------------------------------------+

**For Further Reading:**

http://en.wikipedia.org/wiki/Hartley_oscillator

**Return to Lab Activity Table of Contents.**
