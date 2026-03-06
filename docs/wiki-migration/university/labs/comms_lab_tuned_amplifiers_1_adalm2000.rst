Activity: Tuned Amplifier Stages
================================

Objective:
----------

The objective of this lab activity is to study the characteristics of tuned amplifiers stages as covered in :doc:`Chapter sections 16.4 and 16.5 </wiki-migration/university/courses/electronics/text/chapter-16>` of the on-line Introduction to Electronics text.

Background:
-----------

Many communications system requirements exceed the high-frequency limits of op-amps. In cases such as these, discrete tuned amplifiers are often used. Discrete amplifiers are typically tuned using LC (parallel inductor-capacitor) resonant circuits in place of the collector (or drain) resistors. One such circuit is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/labs/ata1_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Common emitter amplifier with resonate output load


The parallel LC (resonate tank) circuit determines the frequency response of the amplifier. There is a frequency at which X\ :sub:`L` = X\ :sub:`C`. This frequency, called the resonant frequency F\ :sub:`R`, is calculated using:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ata1_e1.png
   :align: center
   :width: 170px

As we learned in the lab on :doc:`inductor self resonance </wiki-migration/university/labs/comms_lab_isr_adalm2000>` it is important to take this built-in capacitance into account when designing tuned amplifiers. In an ideal resonant circuit, inductor current lags the capacitor current by 180º and the net circuit current is zero. As a result: The impedance of a parallel resonant circuit is extremely high at F\ :sub:`R`. The common emitter amplifier voltage gain reaches its maximum value when the collector load impedance is maximum i.e. operated at F\ :sub:`R`.

When the input frequency (F\ :sub:`IN`) is lower than F\ :sub:`R`, the circuit impedance decreases from its maximum value, and is inductive. When F\ :sub:`IN` is higher than F\ :sub:`R`, the circuit impedance drops again, but is capacitive. When operated at F\ :sub:`R`, the impedance of the tank circuit reaches its maximum value. As a result, the gain of the tuned :doc:`common emitter amplifier </wiki-migration/university/courses/electronics/electronics-lab-5>` is also at its maximum value.

Pre Lab Simulations
~~~~~~~~~~~~~~~~~~~

Build a simulation schematic of the tuned amplifier as shown in figure 1. Calculate values for bias resistors R\ :sub:`1` and R\ :sub:`2` such that with emitter resistor R\ :sub:`3`\ set to 100 Ω, the collector current in NPN transistor Q\ :sub:`1` is approximately 5 mA. Assume the circuit is powered from a +10V power supply. Be sure to keep the sum of R\ :sub:`1` and R\ :sub:`2` ( total resistance ) as high as practical to maintain the input impedance of the amplifier stage as high as possible. Set input and output AC coupling capacitors C\ :sub:`2` and C\ :sub:`3` to 0.1 uF. Calculate a value for C\ :sub:`1` such that the resonate frequency, with L\ :sub:`1` set equal to 100 uH, will be close to 500 KHz. Perform a small signal AC sweep of the input and plot the amplitude and phase seen at the output. Save these results to compare with the measurements you take on the actual circuit and to include with your lab report. You may also want to create simulation schematics for the circuits shown in figures 3 and 4 as well.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 2N3904 NPN transistor
| 1 - 100 uH inductor (Various other value inductors)
| 2 - 0.1 uF capacitors ( marked 104 )
| 1 - 100 Ω resistor
| Other resistor and capacitors as needed

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 2 on your solder-less breadboard. Based on your pre lab simulations pick values for bias resistors R\ :sub:`1` and R\ :sub:`2` from your parts kit such that with the 100 Ω emitter resistor, R\ :sub:`3`, the collector current in NPN transistor Q\ :sub:`1` is between 5 mA and 10 mA. Assume the circuit is powered from the +5V and -5V power supplies ( 10 V total ). Be sure to keep the sum of R\ :sub:`1` and R\ :sub:`2` ( total resistance ) as high as practical to maintain the input impedance of the amplifier stage as high as possible. Again based on your simulations, calculate a value for C\ :sub:`1` such that the resonate frequency with the 100 uH L\ :sub:`1` will be close to 500 KHz. Pick a standard capacitor value from the ones supplied in your parts kit or combine two in series or parallel to come as close as possible to your calculated value. Calculate a new resonate frequency based on the final value you ended up with for C\ :sub:`1`. You may want to include the effect of the parasitic winding capacitance you might have measured in the lab on :doc:`inductor self resonance </wiki-migration/university/labs/comms_lab_isr_adalm2000>`.

The peak gain of this tuned amplifier can be very high. We will need to slightly attenuate the output signal of AWG1 by picking a value for R\ :sub:`S` that is 2 to 3 times larger than the parallel combination of R\ :sub:`1` and R\ :sub:`2` ( the input resistance of the amplifier). The value of the output load, R\ :sub:`L`, also determines the amplifier maximum gain. For the initial measurements leave R\ :sub:`L` out of the circuit. The approximate 1 MegΩ input resistance of the scope channel will serve as R\ :sub:`L`.

.. image:: https://wiki.analog.com/_media/university/labs/ata1_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Common emitter tuned amplifier


Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.


|image1|

.. container:: centeralign

   Figure 3 Common emitter tuned amplifier breadboard connections


Procedure:
~~~~~~~~~~

Open the network analyzer software instrument from the main Scopy window. Configure the sweep to start at 10 KHz and stop at 10 MHz. Set the Amplitude to 200 mV and the Offset to zero volts. Under the Bode scale set the magnitude top to 60 dB and range to 80 dB. Set the phase top to 180º and range to 360º. Under scope channels click on use channel 1 as reference. Set the number of steps to 100.

Run a single frequency sweep. You should see amplitude and phase vs frequency plots that look very similar to your simulation results. Once you have determined that the maximum gain of the amplifier occurs near 500 KHz then you can reduce the frequency sweep range to start at 100 KHz and stop at 1 MHz. Be sure to export all the frequency sweep data to a .csv file for further analysis in either Excel or Matlab.


|image2|

.. container:: centeralign

   Figure 4 Common emitter tuned amplifier with R\ :sub:`L` is 1MΩ


Now add the load resistor, R\ :sub:`L`, in the circuit. Start with 100 KΩ and run a new sweep. Note the maximum gain and the frequency. Compare to the result you got with just the scope input as the load. Try successively lower values for R\ :sub:`L` such as 10 KΩ and 1 KΩ etc. Note and compare your measurements.

Questions:
~~~~~~~~~~

| What is the 3 dB bandwidth of the amplifier without R\ :sub:`L`?
| What is the 3 dB bandwidth with R\ :sub:`L` equal to 100 KΩ, 10 KΩ and 1 KΩ?
| What is the effect of connecting a capacitor in parallel ( across ) with emitter resistor R\ :sub:`3`?
| Using the scope and function generator software instruments ( in the time domain ) what is the maximum peek to peek voltage swing possible at the output of the circuit? Be sure to measure it at the resonance frequency. What limits the positive and negative peak voltages? Can it be larger than the power supply voltage and why?

Frequency Multipliers
---------------------

Frequency Multipliers or harmonic generators are a special class of amplifiers that are biased at 3 to 10 times below normal cutoff bias. They are used to generate an output frequency that is a multiple (harmonic) of a lower input frequency.

The tuned amplifier circuit of figure 2 can operate as a frequency multiplier. If an input signal, such as a square wave or pulse that contains a large enough harmonic, has a frequency of say 167 KHz, which is 1/3 of the 500 KHz resonant frequency of the output tank, the output signal would contain mostly 500 KHz where the gain is highest, or three times the input frequency. The fundamental frequency and other harmonics of the input will be greatly reduced by the tuned nature of the circuit. The fifth harmonic (frequency quintupler) is normally as high in multiplication as is practical, because harmonics of an input signal higher than the fifth are generally very weak, and the multiplied output diminishes to a very weak signal.

.. _directions-1:

Directions:
~~~~~~~~~~~

Calculate new values for the input bias resistor divider R\ :sub:`1`, R\ :sub:`2` such that transistor Q\ :sub:`1` is nominally just cut off ( I\ :sub:`C` = 0 ) with no input signal applied. Sine waves generally do not contain any harmonics so set AWG1 to produce a square wave signal at 1/3 the resonate frequency you measured in the earlier tests. To generate large harmonics set the symmetry to 20% ( pulse high for 20% of the period). You will need to increase the amplitude of the input pulse to greater than 2 V or remove the input attenuation source resistor R\ :sub:`S`.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Frequency multipliers are operated by the pulses of collector current produced by a class C amplifier. Although the collector current flows in pulses, the alternating collector voltage is sinusoidal because of the action of the tank circuit. Use one of the scope channels to monitor the collector current pulses by measuring the voltage across emitter resistor R\ :sub:`3`.


|image3|

.. container:: centeralign

   Figure 5 CH 2, voltage across emitter resistor R\ :sub:`3`\


Improved Tuned Amplifier Stage
------------------------------

The following circuit, shown in figure 6 is a more versatile tuned amplifier stage using an NPN :doc:`differential pair </wiki-migration/university/courses/electronics/electronics-lab-12>` with an LC resonate output load.

.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 2N3904 NPN transistor
| 1 - SSM2212 NPN matched transistor pair
| 1 - 100 uH inductor (Various other value inductors)
| 2 - 0.1 uF capacitors ( marked 104 )
| 1 - 100 Ω resistor
| 2 - 1 KΩ resistors
| 1 - 2.2 KΩ resistor
| Other resistor and capacitors as needed

.. _directions-2:

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 3 on your solder-less breadboard. Use the SSM2212 matched transistor pair for Q\ :sub:`1` and Q\ :sub:`2`. Pick values for bias resistors R\ :sub:`1` and R\ :sub:`2` from your parts kit such that with the 100 Ω emitter resistor, R\ :sub:`3`, the collector current in NPN transistor Q\ :sub:`3` is between 5 mA and 10 mA. Note in this case the R\ :sub:`1`, R\ :sub:`2` resistor divider is powered from ground and -5V power supply. Use the same combination of L\ :sub:`1` and C\ :sub:`1` as in the previous amplifier stage.

.. image:: https://wiki.analog.com/_media/university/labs/ata1_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 Differential amplifier stage with single ended resonate output load


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.


|image4|

.. container:: centeralign

   Figure 7 Differential amplifier stage with single ended resonate output load breadboard connection


.. _procedure-2:

Procedure:
~~~~~~~~~~

Open the network analyzer software instrument from the main Scopy window. Configure the sweep to start at 10 KHz and stop at 10 MHz. Set the Amplitude to 200 mV and the Offset to zero volts. Under the Bode scale set the magnitude top to 50 dB and range to 80 dB. Set the phase top to 180º and range to 360º. Under scope channels click on use channel 1 as reference. Set the number of steps to 500.

As in the first experiment, run a single frequency sweep. Once you have determined that the maximum gain of the amplifier occurs near 500 KHz then you can reduce the frequency sweep range to start at 100 KHz and stop at 1 MHz. Be sure to export the data to a .csv file for further analysis in either Excel or Matlab.


|image5|

.. container:: centeralign

   Figure 8 Improved tuned amplifier with R\ :sub:`L` is 1MΩ


As before add the load resistor, R\ :sub:`L`, in the circuit. Start with 100 KΩ and run a new sweep. Note the maximum gain and the frequency. Compare to the result you got with just the scope input as the load. Try successively lower values for R\ :sub:`L` such as 10 KΩ and 1 KΩ etc. Note and compare your measurements. They should be very similar to the results you got in the first experiment.

Bonus Experiment:
~~~~~~~~~~~~~~~~~

Amplitude modulation may be applied to the output frequency by capacitor coupling a modulating (audio frequency) signal from AWG 2 to either the base or emitter of current source transistor Q\ :sub:`3`.

Adding a 2 pole high pass filter input stage
--------------------------------------------

It is sometimes desirable to include a simple active high pass filter to the input of the single transistor tuned amplifier stage. The filter circuit shown in figure 4 provides a two pole filter with unity gain. This filter is convenient to place in a larger circuit because it contains few components and does not occupy much space.

The active high pass transistor circuit is quite straightforward, using just a total of four resistors, two capacitors and the same single transistor. The operating conditions for the transistor are set up in the normal way. As in figure 1, R\ :sub:`1` and R\ :sub:`2` are used to set up the bias point for the base of the transistor. The resistor R\ :sub:`3` is the emitter resistor and sets the current for the transistor.

The filter components are included in negative feedback from the emitter of the transistor to the input. The components that form the active filter network consist of C\ :sub:`2`, C\ :sub:`3`, R\ :sub:`4` and the combination of R\ :sub:`1` and R\ :sub:`2` in parallel, assuming that the input resistance to the base of the transistor is very high and can be ignored.

:math:`C_2 = 2 \times C_3`

:math:`\displaystyle R_4 = \frac{R_2 \times R_1}{R_2 + R_1}`

This is for values where the effect of the transistor itself within the high pass filter circuit can be ignored, i.e.:

:math:`\displaystyle R_3 (\beta+1) >> \frac{R_2 \times R_1}{R_2 + R_1}`

:math:`F_o = 1.414 / (4 \pi R_4 C_2)`

| Where:
| β = the forward current gain of the transistor
| F\ :sub:`o` = the cut-off frequency of the high pass filter
| π = equal to 3.14159

The equations for determining the component values provide a Butterworth response, which provides maximum flatness within the pass-band at the expense of achieving the ultimate roll off as quickly as possible. This has been chosen because this form of filter suits most applications and the mathematics works out easily.

.. _materials-2:

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 2N3904 NPN transistor
| 1 - 100 uH inductor (Various other value inductors)
| 1 - 0.1 uF capacitors ( marked 104 )
| 1 - 100 Ω resistor
| Other resistor and capacitors as needed

.. _directions-3:

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 4 on your solder-less breadboard. Use the same values for bias resistors R\ :sub:`1` and R\ :sub:`2` that you used in experiment 1 (figure 2). Use the same combination of L\ :sub:`1` and C\ :sub:`1` as in the previous amplifier stage. Using the formula above for the high pass cut off frequency F\ :sub:`O`, calculate values for C\ :sub:`2`, C\ :sub:`3` and R\ :sub:`4` that results in a frequency more than two octaves below the resonance frequency of L\ :sub:`1` and C\ :sub:`1`. For example if F\ :sub:`R` is equal to 500 KHz then base your calculations on F\ :sub:`O` equal to 125 KHz.

.. image:: https://wiki.analog.com/_media/university/labs/ata1_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 Adding a 2 pole high pass input filter to the tuned amplifier


.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.


|image6|

.. container:: centeralign

   Figure 10 Breadboard connection


.. _procedure-3:

Procedure:
~~~~~~~~~~

Open the network analyzer software instrument from the main Scopy window. Configure the sweep to start at 10 KHz and stop at 10 MHz. Set the Amplitude to 200 mV and the Offset to zero volts. Under the Bode scale set the magnitude top to 30 dB and range to 60 dB. Set the phase top to 180º and range to 360º. Under scope channels click on use channel 1 as reference. Set the number of steps to 100.


|image7|

.. container:: centeralign

   Figure 11 Result with R\ :sub:`L` is 1MΩ


As in the first experiment, run a single frequency sweep with scope channel 2 connected through coupling capacitor C\ :sub:`4` to the collector of Q\ :sub:`1`. To measure the response of the high pass input filter, connect scope channel 2 through coupling capacitor C\ :sub:`4` to the base of Q\ :sub:`1`. Be sure to export the data to a .csv file for further analysis in either Excel or Matlab. Compare the response curves with what you measured for the circuit in figure 2. Try different combinations of values for C\ :sub:`2`, C\ :sub:`3` and R\ :sub:`4` to see how the frequency response changes.

.. admonition:: Download
   :class: download

   \*\* Lab Resources:\*\*

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/tuned_amp_part1_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/tuned_amp_part1_ltspice`
   


**For Further Reading:**

| http:*en.wikipedia.org/wiki/LC_circuit
  http:*\ en.wikipedia.org/wiki/Q_factor
| http://en.wikipedia.org/wiki/Tuned_radio_frequency_receiver

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/labs/ata1_nf3.png
.. |image2| image:: https://wiki.analog.com/_media/university/labs/ata1_nf4.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/labs/ata1_nf5.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/university/labs/ata1_nf7.png
.. |image5| image:: https://wiki.analog.com/_media/university/labs/ata1_nf8.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/university/labs/ata1_nf10.png
.. |image7| image:: https://wiki.analog.com/_media/university/labs/ata1_nf11.png
   :width: 500px
