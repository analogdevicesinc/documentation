Activity: The Transresistance Amplifier Input Stage
===================================================

Objective:
----------

The objective of this lab activity is to investigate simple Transresistance amplifier Input stage configurations.

Background:
-----------

A transresistance amplifier outputs a voltage proportional to its input current. The transresistance amplifier is often referred to as a transimpedance amplifier, especially by semiconductor manufacturers. The general description for a transresistance amplifier in network analysis is as a current controlled voltage source (CCVS) .

An inverting transresistance amplifier can be configured from a conventional operational amplifier and a single resistor. The resistor is connected between the output and the inverting input of the operational amplifier and the non-inverting input is connected to ground. The output voltage will then be proportional to the input current at the inverting input node, decreasing with increasing input current and vice versa.

The activity in this lab exercise investigates an alternate differential input structure which produces an inherently low input impedance (a current input) as opposed to the relatively high input impedance of the voltage differential pair that was investigated in BJT Activities and MOS. A complete transresistance amplifier will require the addition of possible further gain stages and an output driver stage such as what was investigated in the Activity on Amplifier Output Stages.

Materials:
~~~~~~~~~~

| ADALM1000 module
| Solder-less breadboard
| Jumper wires
| 3 – 1 KΩ resistors
| 2 – 2.2 KΩ resistors
| 1 – 47 KΩ resistor
| 2 – 10 uF capacitors
| 2 – NPN transistors ( 2N3904 or SSM2212 )
| 2 – PNP transistors ( 2N3906 or SSM2220 )

Directions:
~~~~~~~~~~~

The circuit and the connections to the ALM1000 hardware are as indicated in figure 1. NPN transistors Q\ :sub:`1`, Q\ :sub:`2` and PNP transistors Q\ :sub:`3` and Q\ :sub:`4` should be selected from the available devices with the best matching of V\ :sub:`BE`. Transistors fabricated in the same package such as the SSM2212, SM2220 or the CA3046 tend to match much better than individual devices. Split I/O input AIN may optionally want to be connected to the junction of Q\ :sub:`1` and Q\ :sub:`3` emitters or the collectors of either Q\ :sub:`1` or Q\ :sub:`3` while investigating the operation of this circuit. The current input node at the junction of the emitters of Q\ :sub:`1` and Q\ :sub:`3` is nominally a low impedance so as to be driven from a current source. The AWG channel outputs of M1k are more like voltage sources. So the 1KΩ resistor R\ :sub:`IN` serves to convert the voltage output of AWG CH A to a current (I\ :sub:`IN` = V\ :sub:`IN`/1K),

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-transresistance-input-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Transresistance amplifier input stage with current drive


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A waveform generator (output on pin CH A), should be configured for a 1 KHz sine wave with 400 mV swing, Max value set to 2.7 and Min value set to 2.3. Channel B split I/O input (on pin BIN) should be connected to the combined output at the end of R\ :sub:`L`.

Procedure:
~~~~~~~~~~

Observe the output at R\ :sub:`L`, which is the AC coupled sum of the signals at the collectors of Q\ :sub:`1` and Q\ :sub:`3`. Measure the voltage gain from the AWG channel A output to R\ :sub:`L` and compare it to your calculated value. Observe the voltage amplitude of the signal seen at the current input node, at the emitters of Q\ :sub:`1` and Q\ :sub:`3`. Based on the this amplitude calculate the input current amplitude (voltage across R\ :sub:`IN` divided by R\ :sub:`IN` ) and the effective input resistance of the amplifier. Compare these values to your calculated values.

Questions:
~~~~~~~~~~

Is the voltage at the emitters of Q\ :sub:`1` and Q\ :sub:`3` equal to the common mode level (2.5V)? How much different is it and why?

Configure for Voltage drive:
----------------------------

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

1 – 470 Ω resistor

.. _directions-1:

Directions:
~~~~~~~~~~~

Now we are going to reconfigure the input for voltage drive. Replace R\ :sub:`IN` with a 470 Ω resistor and connect the other end to the 2.5 V common mode level as shown in figure 2. Disconnect the emitters of Q\ :sub:`2` and Q\ :sub:`4` from the 2.5 V common mode voltage and connect them to the output of CH A.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-transresistance-input-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Transresistance amplifier input stage with voltage drive


.. _procedure-1:

Procedure:
~~~~~~~~~~

Observe the output at R\ :sub:`L`, which is the AC coupled sum of the signals at the collectors of Q\ :sub:`1` and Q\ :sub:`3`. Measure the voltage gain from the CH A output to R\ :sub:`L` and compare it to your calculated value. Observe the voltage amplitude of the signal seen at the current input node, at the emitters of Q\ :sub:`1` and Q\ :sub:`3`. Based on the this amplitude calculate the input current amplitude ( voltage across R\ :sub:`IN` divided by R\ :sub:`IN` ) and the effective input resistance of the amplifier. Compare these values to your calculated values.

To measure the current that is required from the input driver (CH A) in this voltage drive configuration, you can turn on the CH A current trace. How does this current compare to the current seen in across the 470 Ω R\ :sub:`IN` resistor?

.. _questions-1:

Questions:
~~~~~~~~~~

How closely does the voltage at the emitters of Q\ :sub:`1` and Q\ :sub:`3` follow the voltage at emitters of Q\ :sub:`2` and Q\ :sub:`4`? Explain any differences you observe.

**For Further Reading:**

| :adi:`Current Feedback (CFB) Op Amps <static/imported-files/tutorials/MT-034.pdf>`
| `Op Amp Fundamentals: The Transresistance Amplifier <http://www.wisc-online.com/objects/ViewObject.aspx?ID=SSE3103>`_
| `Current-to-voltage converter <https://en.wikipedia.org/wiki/Transimpedance_amplifier>`_

**Return to Lab Activity Table of Contents.**
