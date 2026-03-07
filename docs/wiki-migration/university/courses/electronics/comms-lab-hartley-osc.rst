Activity: The Hartley Oscillator
================================

Objective:
----------

Oscillators come in many forms. In this lab activity we will explore the Hartley configuration which uses a taped inductor divider to provide the feedback path.

Background:
-----------

The Hartley Oscillator is a particularly good circuit for producing fairly low distortion sine wave signals in the RF range, 30kHz to 30MHz. The Hartley configuration can be recognized by its use of a tapped inductor divider (L\ :sub:`1` and L\ :sub:`2` in figure 1). The frequency of oscillation can be calculated in the same way as any parallel resonant circuit, using:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ata1_e1.png
   :align: center
   :width: 170px

Where L = L\ :sub:`1` + L\ :sub:`2`

Figure 1 shows a typical Hartley oscillator. The frequency determining parallel resonant tuned circuit is formed by L\ :sub:`1`, L\ :sub:`2` and C\ :sub:`1` and is used as the collector load impedance of the common base amplifier Q\ :sub:`1`. This gives the amplifier a high gain only at the resonant frequency. This configuration of the Hartley oscillator uses a common base amplifier, the base of Q\ :sub:`1`\ is biased to an appropriate DC level by resistor divider R\ :sub:`1` and R\ :sub:`2` but is connected directly to an AC ground by C\ :sub:`3`. In the common base mode the output voltage waveform at the collector, and the input signal at the emitter are in phase. This ensures that the fraction of the output signal from the node between L\ :sub:`1` and L\ :sub:`2`, fed back from the tuned collector load to the emitter via the coupling capacitor C\ :sub:`2` provides the required positive feedback.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ahosc_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure1 Basic Hartley Oscillator


C\ :sub:`2` also forms a low frequency time constant with the emitter resistor R\ :sub:`3` to provide an average DC voltage level proportional to the amplitude of the feedback signal at the emitter of Q\ :sub:`1`. This provides automatic control of the gain of the amplifier to give the closed loop gain of 1 required by the oscillator. The emitter resistor R\ :sub:`3` is not decoupled because the emitter node is used as the common base amplifier input. The base is connected to AC ground by C\ :sub:`3`, which will provide a very low reactance at the oscillator frequency.

Pre Lab Simulations
~~~~~~~~~~~~~~~~~~~

Build a simulation schematic of the Hartley oscillator as shown in figure 1. Calculate values for bias resistors R\ :sub:`1` and R\ :sub:`2` such that with emitter resistor R\ :sub:`3`\ set to 1 KΩ, the collector current in NPN transistor Q\ :sub:`1` is approximately 1 mA. Assume the circuit is powered from a +10V power supply. Be sure to keep the sum of R\ :sub:`1` and R\ :sub:`2` ( total resistance greater than 10 KΩ) has high as practical to keep the standing current in the resistor divider as low as practical. Remember that C\ :sub:`3` provides an AC ground at the base of Q\ :sub:`1`. Set base decoupling capacitor C\ :sub:`3` and output AC coupling capacitor C\ :sub:`4` to 0.1uF. Calculate a value for C\ :sub:`1` such that the resonate frequency, with L\ :sub:`1` set equal to 1 uH and L\ :sub:`2` set to 10 uH, will be close to 750 KHz. Perform a transient simulation. Save these results to compare with the measurements you take on the actual circuit and to include with your lab report.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 2N3904 NPN transistor
| 1 - 1 uH inductor
| 1 - 10 uH inductor
| 1 - 100 uH inductor
| 1 - 1 nF capacitor ( C\ :sub:`1` optional values as listed below )
| 2 - 0.1 uF capacitors ( marked 104 )
| 1 - 0.01 uF capacitor ( marked 103)
| 1 - 1 KΩ resistor
| Other resistor, capacitors and inductors as needed

Directions:
-----------

Build The Hartley Oscillator shown in figure 2 using your solder-less breadboard. Pick standard values from your parts kit for bias resistors R\ :sub:`1` and R\ :sub:`2` such that with emitter resistor R\ :sub:`3`\ set to 1 KΩ, the collector current in NPN transistor Q\ :sub:`1` is approximately 1 mA. The frequency of the oscillator can be from around 500 KHz to 2 MHz depending on the values chosen for L\ :sub:`1`, L\ :sub:`2` and C\ :sub:`1`. Start with L\ :sub:`1` = 10 uH and L\ :sub:`2` = 100 uH. This oscillator circuit can produce a sine wave output in excess of 10 Vpp at an approximate frequency set by the value chosen for C\ :sub:`1`. After experimenting with various values for C\ :sub:`1` change L\ :sub:`1` = 1 uH and L\ :sub:`2` = 10 uH.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ahosc_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 Hartley Oscillator


Hardware Setup:
---------------

The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to only turn on the power supplies after you double check your wiring.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 Hartley Oscillator breadboard circuit


Procedure:
----------

Having finished construction the Hartley oscillator check that the circuit is oscillating correctly by turning on both the + and - 5 V power supplies and connecting one of the oscilloscope channels to the output terminal. It may be found that the value of R\ :sub:`3` is fairly critical, producing either a large distorted waveform or an intermittent low or no output. To find the best value for R\ :sub:`3`, it could be replaced by a 1 KΩ potentiometer for experimentation to find the value that gives the best wave shape and reliable amplitude.

A plot example using R\ :sub:`1` = 10KΩ, R\ :sub:`2` = 1KΩ, R\ :sub:`3` = 100Ω and C\ :sub:`1` = 4.7nF is presented in the figure below.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 4 Hartley Oscillator plot


Questions:
----------

Measure the peak to peak output voltage of the output. Measure the DC ( average ) level of the output waveform at the collector of Q\ :sub:`1` and on the other (output) side of AC coupling capacitor C\ :sub:`4`. Measure the period (time T) of the output waveform and its frequency (1/T). Compare this measured frequency to what you calculated by :math:`F_R = 1 / 2 \pi sqrt(LC)` .

Fill in the table below with the measured frequency for other C\ :sub:`1` values. Use the values in the table as suggested options but try to include as many different values as possible using series and parallel combinations of the capacitors supplied in your parts kit. Any of the C\ :sub:`1` optional values shown below should give reliable oscillation.

+---------------------+----------------------------------------+--------------------------------------+
| C\ :sub:`1` Options | L\ :sub:`1` = 10uH L\ :sub:`2` = 100uH | L\ :sub:`1` = 1uH L\ :sub:`2` = 10uH |
+=====================+========================================+======================================+
| Value               | Frequency                              | Frequency                            |
+---------------------+----------------------------------------+--------------------------------------+
| 1nF                 |                                        |                                      |
+---------------------+----------------------------------------+--------------------------------------+
| 2.2nF               |                                        |                                      |
+---------------------+----------------------------------------+--------------------------------------+
| 4.7nF               |                                        |                                      |
+---------------------+----------------------------------------+--------------------------------------+
| 10nF                |                                        |                                      |
+---------------------+----------------------------------------+--------------------------------------+

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/hartley_osc_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/hartley_osc_ltspice`
   


**For Further Reading:**

http://en.wikipedia.org/wiki/Hartley_oscillator

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/hartley_osc-bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/hartley_osc-wav.png
