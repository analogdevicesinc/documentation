Activity: Zero gain amplifier (MOS)
===================================

Objective:
----------

In the design of a circuit it is important to take into account the wide variation in certain device values from one to another. A central objective of the designer is to desensitize the circuit to these variations to produce a circuit which meets the specifications across all possible conditions. One aspect of design which is common to nearly all circuits is the establishment of stable bias or operating point levels. This seemingly minor portion of the design can provide the most challenging and interesting circuit problems. Many bias generators are centered around the generation of currents to operate the core of the circuit. Current generated from simple resistors and diodes or diode connected transistors connected across the power supply will vary approximately proportional to the variation of the supply voltage. This variation in the resulting bias current is often undesirable. This lab is to introduce a current "mirror" in Activity 8M which has an output which had been desensitized to variation in input current. To understand this circuit, it is helpful to examine the behavior of a "zero-gain amplifier".

Materials :
-----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 1 - 2.2KΩ Resistor (or any similar value)
| 1 - 168Ω resistor ( use a 100Ω in series with a 68Ω )
| 1 - small signal NMOS transistor (enhancement mode CD4007 or ZVN2110A)

Directions:
-----------

The breadboard connections are as shown in the diagram below. The Arbitrary Waveform Generator 1 output drives one end of resistor R\ :sub:`1`. Resistor R\ :sub:`2` is connected between the gate and drain of transistor M\ :sub:`1` with the other end of resistor R\ :sub:`1` connected to the gate as well. The source of M\ :sub:`1`\ is grounded thus M1 is in a common source configuration.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NMOS Zero Gain Amplifier


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_zero_gain-bb.png

.. container:: centeralign

   Figure 2 NMOS Zero Gain Amplifier Breadboard Circuit


The waveform generator 1 should be configured for a 1 KHz triangle wave with 4 volt amplitude peak-to-peak and 2V offset. Connect scope Channel 1 to display output W1 of the AWG generator. The Single ended input of scope channel 2 (2+) is used to measure alternately the gate and drain voltage of M\ :sub:`1`.

Procedure:
----------

Remembering back to the common source amplifier in the previous section, if R\ :sub:`L` is set equal to r\ :sub:`s` (1/g\ :sub:`m`) then the gain A will be -1. If the gate is connected to the top of resistor R\ :sub:`L`\ then the gain from the gate to the drain (bottom of R\ :sub:`L`) will be -1. Also, neglecting the drain source output impedance of the transistor the gain from the top of load resistor R\ :sub:`L` to the drain (bottom of R\ :sub:`L`) will be +1. Thus the net gain superimposing both paths will be 1 - 1 = 0. In the figure below we have a transistor biased into saturation region with a drain voltage which is less than the gate voltage by , (equal to I\ :sub:`D` times 50 ohms) and is essentially constant with input voltage changes applied from the waveform generator.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 V\ :sub:`drain` Plot


.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 4 V\ :sub:`gate` Plot


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Plot comparing V\ :sub:`gate` and V\ :sub:`drain`


Questions:
----------

What are the relative gains of the two paths when the drain current is less than and greater than the "ideal" zero gain value?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/mos_zero_gain_amp_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/mos_zero_gain_amp_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_zero_gain_vds-wav.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_zero_gain_vgs-wav.png
   :width: 500px
