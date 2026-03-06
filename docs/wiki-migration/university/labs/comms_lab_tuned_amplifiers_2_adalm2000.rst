Activity: Tuned Amplifier Stages, part II
=========================================

Objective:
----------

The objective of this lab activity is to continue the study of tuned amplifiers stages that was started in this earlier :doc:`set of activities </wiki-migration/university/labs/comms_lab_tuned_amplifiers_1_adalm2000>`.

Background:
-----------

As we learned in the previous set of activities, second order LC tank circuits are commonly used as the tuned element in amplifier stages. The simple parallel LC tank, as shown in figure 1, can produce voltage gain at the expense of current to drive a resistive load. A buffer amplifier such as an emitter follower can supply the required current ( or power ) gain to drive a load.

.. image:: https://wiki.analog.com/_media/university/labs/ata2_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 parallel resonate LC tank circuit


The second coupling capacitor, C\ :sub:`2`, must be included in the calculation of the resonate frequency. The following formula will give us the resonate frequency for the circuit in figure 1:

.. image:: https://wiki.analog.com/_media/university/labs/ata2_e1.png
   :align: center
   :width: 200px

Pre Lab Simulations
~~~~~~~~~~~~~~~~~~~

Build a simulation schematic of the tuned emitter follower amplifier as shown in figure 1. Calculate a value for emitter resistor R\ :sub:`L` such that the current in NPN transistor Q\ :sub:`1` is approximately 5 mA. Assume the circuit is powered from +/- 5V power supplies (+10V total ). Hint: the DC voltage at the base of Q\ :sub:`1` is set by the DC path through L\ :sub:`1` to ground. Calculate a value for C\ :sub:`1` and C\ :sub:`2` such that the resonate frequency, with L\ :sub:`1` set equal to 100 uH, will be close to 350 KHz. Generally, C\ :sub:`1` and C\ :sub:`2` are of equal value. Perform a small signal AC sweep of the input and plot the amplitude and phase seen at the output. Save these results to compare with the measurements you take on the actual circuit and to include with your lab report. You may also want to create a simulation schematic for the circuit shown in figures 3 as well.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 - 2N3904 NPN transistor
| 1 - 100 uH inductor (Various other value inductors)
| 2 - 1.0 nF capacitors ( marked 102 )
| 2 - 1 KΩ resistors
| 1 - 2.2 KΩ resistor
| Other resistor and capacitors as needed

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 2 on your solder-less breadboard. Use a 100 uH inductor for L\ :sub:`1` and 1.0 nF capacitors for C\ :sub:`1` and C\ :sub:`2`. The peak gain of this tuned amplifier can be very high at the resonate frequency. We will need to slightly attenuate the output signal of AWG1 using resistor divider R\ :sub:`S` and R\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/labs/ata2_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Emitter follower tuned amplifier


The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.

Hardware Setup:
~~~~~~~~~~~~~~~

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 Emitter follower tuned amplifier breadboard circuit


Open the power supply control window to turn on and off the +5 and -5 volt power supplies. Open the network analyzer software instrument from the main Scopy window. Configure the sweep to start at 10 KHz and stop at 10 MHz. Set the Amplitude to 200 mV and the Offset to zero volts. Under the Bode scale set the max. magnitude at 40dB and min. magnitude at -40dB . Set the phase top to 180º and bottom to to -180º. Under scope channels click on use channel 1 as reference. Set the number of steps to 500.

Procedure:
~~~~~~~~~~

Turn on the power supplies and run a single frequency sweep. You should see amplitude and phase vs frequency plots that look very similar to your simulation results. Once you have determined that the maximum gain of the amplifier occurs near 350 KHz then you can reduce the frequency sweep range to start at 100 KHz and stop at 1 MHz. Be sure to export all the frequency sweep data to a .csv file for further analysis in either Excel or Matlab.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 4 Emitter follower tuned amplifier plot


Questions:
~~~~~~~~~~

What is the output impedance seen at the emitter of Q\ :sub:`1`? Compare this to the output impedance seen at the collector of the common emitter tuned amplifier we explored in the previous lab activity. Using the scope and function generator software instruments ( in the time domain ) what is the maximum peek to peek voltage swing possible at the output of the circuit? Be sure to measure it at the resonance frequency. What limits the positive and negative peak voltages? Can it be larger than the power supply voltage and why or why not?

Tuned amplifier with Quadrature Outputs
---------------------------------------

If we add a second conventional emitter follower stage as a non-tuned parallel path we can will have an amplifier with two outputs that will have exactly a 90º phase difference between them, at the resonant frequency. By adding a resistor in parallel with the resonate tank, L\ :sub:`1`, C\ :sub:`1`, we can lower the gain at resonance to unity ( 0 dB ) such that the gain from the input to the emitter of Q\ :sub:`1` will be the same as the non-tuned gain unity gain of the conventional emitter follower stage, Q\ :sub:`2`.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 1 - 2N3904 NPN transistor
| 2 - 470 Ω resistors
| 1 - 1 KΩ resistor

.. _directions-1:

Directions:
~~~~~~~~~~~

Modify the circuit on your solder-less breadboard to add the second emitter follower stage, Q\ :sub:`2`, as shown in figure 5. Be sure to turn off the power supplies and stop the AWG before making any changes to your circuit.

The exact value for R\ :sub:`1`, such that the gain is reduced to unity, may vary from the 470 Ω suggested in the figure. You can experiment with different values to obtain the proper amount of gain to match the amplitude seen at the emitter of Q\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/labs/ata2_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Amplifier with quadrature outputs


The green squares indicate where to connect the ADALM2000 module AWG, scope channels and power supplies. Be sure to turn on the power supplies only after you double check your wiring.

.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Build the breadboard circuit presented in Figure 6.

.. container:: centeralign


|image3|

.. container:: centeralign

   Figure 6 Amplifier with quadrature outputs breadboard circuit


.. _procedure-1:

Procedure:
~~~~~~~~~~

Set the AWG amplitude in the Network Analyzer to 2.0 V, because we have reduced the gain by adding R\ :sub:`1`. Turn on the power supplies and run a single frequency sweep. You should see amplitude and phase vs frequency plots that look very similar to your simulation results. Be sure to export all the frequency sweep data to a .csv file for further analysis in either Excel or Matlab.

.. container:: centeralign


|image4|

.. container:: centeralign

   Figure 7 Amplifier with quadrature outputs plot


Using the scope and function generator software instruments ( in the time domain ) set the AWG frequency to the resonate frequency with the amplitude set to 2V. Observer the relative amplitude and phase of the two outputs.

.. _questions-1:

Questions:
~~~~~~~~~~

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/tuned_amp2_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/tuned_amp2_ltspice`
   


**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/labs/ef_tuned_amplifier-bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/labs/ef_tuned_amplifier-wav.png
.. |image3| image:: https://wiki.analog.com/_media/university/labs/quad_amplifier-bb.png
.. |image4| image:: https://wiki.analog.com/_media/university/labs/quad_amplifier-wav.png
