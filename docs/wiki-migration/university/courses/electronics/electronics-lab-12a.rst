Activity: The Transresistance Amplifier Input Stage
===================================================

Objective:
----------

The objective of this lab activity is to investigate simple Transresistance amplifier Input stage configurations.

Background:
-----------

A transresistance amplifier outputs a voltage proportional to its input current. The transresistance amplifier is often referred to as a transimpedance amplifier, especially by semiconductor manufacturers. The general description for a transresistance amplifier in network analysis is as a current controlled voltage source (CCVS).

An inverting transresistance amplifier can be configured from a conventional operational amplifier and a single resistor. The resistor is connected between the output and the inverting input of the operational amplifier and the non-inverting input is connected to ground. The output voltage will then be proportional to the input current at the inverting input node, decreasing with increasing input current and vice versa.

The activity in this lab exercise investigates an alternate differential input structure which produces an inherently low input impedance (a current input) as opposed to the relatively high input impedance of the voltage differential pair that was investigated in Activities 12 (BJT) and 12M (MOS). A complete transresistance amplifier will require the addition of possible further gain stages and an output driver stage such as what was investigated in Activity 13A on Amplifier Output Stages.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 3 - 1 KΩ resistors
| 2 - 2.2 KΩ resistors
| 1 - 47 KΩ resistor
| 2 - 10 uF capacitors
| 2 - NPN transistors ( 2N3904 or SSM2212 )
| 2 - PNP transistors ( 2N3906 or SSM2220 )

Directions:
~~~~~~~~~~~

The circuit and the connections to the ADALM2000 are as indicated in figure 1. NPN transistors Q\ :sub:`1`, Q\ :sub:`2` and PNP transistors Q\ :sub:`3` and Q\ :sub:`4` should be selected from the available devices with the best matching of V\ :sub:`BE`. Transistors fabricated in the same package such as the SSM2212, SM2220 or the CA3046 tend to match much better than individual devices. Scope input 1+ may optionally want to be connected to the junction of Q\ :sub:`1` and Q\ :sub:`3` emitters or the collectors of either Q\ :sub:`1`\ or Q\ :sub:`3` while investigating the operation of this circuit. The current input node at the junction of the emitters of Q\ :sub:`1` and Q\ :sub:`3` is nominally a low impedance so as to be driven from a current source. The AWG outputs of ADALM2000 are more like voltage sources. So the 1KΩ resistor R\ :sub:`IN` serves to convert the voltage output of AWG1 to a current (I\ :sub:`IN` = V\ :sub:`IN`/1K),

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a12a_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Transresistance amplifier input stage with current drive


Hardware Setup:
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/tr_amp_in_cdrv-bb.png

.. container:: centeralign

   Figure 2 Transresistance amplifier input stage with current drive - Breadboard Circuit


The first waveform generator, W1, should be configured for a 1 KHz sine wave with 800 mV amplitude peak-to-peak and 0 offset. Channel one of the scope should be connected to display the output of the first generator and channel 2 should be set to display the output signal at 500 mV per division.

Procedure:
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/tr_amp_in_cdrv-wav.png

.. container:: centeralign

   Figure 3 Transresistance amplifier input stage with voltage drive - Waveforms


Observe the output at R\ :sub:`L`, which is the AC coupled sum of the signals at the collectors of Q\ :sub:`1` and Q\ :sub:`3`. Measure the voltage gain from the AWG1 output to R\ :sub:`L` and compare it to your calculated value. Observe the voltage amplitude of the signal seen at the current input node, at the emitters of Q\ :sub:`1` and Q\ :sub:`3`.<sub></sub>Based on the this amplitude calculate the input current amplitude ( voltage across R\ :sub:`IN` divided by R\ :sub:`IN` ) and the effective input resistance of the amplifier. Compare these values to your calculated values.

Questions:
~~~~~~~~~~

Is the voltage at the emitters of Q\ :sub:`1` and Q\ :sub:`3` equal to ground? How much different is it and why?

Configure for Voltage drive:
----------------------------

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 1 - 470Ω resistor

.. _directions-1:

Directions:
~~~~~~~~~~~

Now we are going to reconfigure the input for voltage drive. Replace R\ :sub:`IN` with a 470Ω resistor and ground the other end as shown in figure 4. Disconnect the emitters of Q\ :sub:`2` and Q\ :sub:`4` from ground and connect them to the output of AWG1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a12a_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Transresistance amplifier input stage with voltage drive


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/tr_amp_in_vdrv-bb.png

.. container:: centeralign

   Figure 5 Transresistance amplifier input stage with voltage drive - Breadboard Circuit


.. _procedure-1:

Procedure:
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/tr_amp_in_vdrv-wav.png

.. container:: centeralign

   Figure 6 Transresistance amplifier input stage with voltage drive - Waveforms


Observe the output at R\ :sub:`L`, which is the AC coupled sum of the signals at the collectors of Q\ :sub:`1` and Q\ :sub:`3`. Measure the voltage gain from the AWG1 output to R\ :sub:`L` and compare it to your calculated value. Observe the voltage amplitude of the signal seen at the current input node, at the emitters of Q\ :sub:`1` and Q\ :sub:`3`.<sub></sub>Based on the this amplitude calculate the input current amplitude ( voltage across R\ :sub:`IN` divided by R\ :sub:`IN` ) and the effective input resistance of the amplifier. Compare these values to your calculated values.

To measure the current that is required from the input driver (W1) in this voltage drive configuration, insert the 1KΩ resistor in series with AWG1 (and the emitters of Q\ :sub:`2` and Q\ :sub:`4`). Connect the differential channel 1 scope inputs 1+,1- across the 1KΩ resistor. Observe this voltage and calculate the current as AWG1 swings over the +/- 400mV swing.

.. _questions-1:

Questions:
~~~~~~~~~~

How closely does the voltage at the emitters of Q\ :sub:`1` and Q\ :sub:`3` follow the voltage at emitters of Q\ :sub:`2` and Q\ :sub:`4`? Explain any differences you observe.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/trans_input_stage_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/trans_input_stage_ltspice`
   


For Further Reading:
~~~~~~~~~~~~~~~~~~~~

-  :adi:`Current Feedback (CFB) Op Amps <MT-034>`
-  `Op Amp Fundamentals: The Transresistance Amplifier <http://www.wisc-online.com/objects/ViewObject.aspx?ID=SSE3103>`__
   \* `Current-to-voltage converter <https://en.wikipedia.org/wiki/Transimpedance_amplifier>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**
