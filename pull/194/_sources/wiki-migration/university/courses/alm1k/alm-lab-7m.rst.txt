Activity: Zero gain amplifier (MOS) - ADALM1000
===============================================

Objective:
----------

In the design of a circuit it is important to take into account the wide variation in certain device values from one to another. A central objective of the designer is to desensitize the circuit to these variations to produce a circuit which meets the specifications across all possible conditions. One aspect of design which is common to nearly all circuits is the establishment of stable bias or operating point levels. This seemingly minor portion of the design can provide the most challenging and interesting circuit problems. Many bias generators are centered around the generation of currents to operate the core of the circuit. Current generated from simple resistors and diodes or diode connected transistors connected across the power supply will vary approximately proportional to the variation of the supply voltage. This variation in the resulting bias current is often undesirable.

This lab is to introduce a current "mirror" in Activity 8M which has an output which had been desensitized to variation in input current. To understand this circuit, it is helpful to examine the behavior of a "zero-gain amplifier" first.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| 1 - 2.2 KΩ Resistor (or any similar value)
| 1 - 168 Ω resistor ( use a 100 Ω in series with a 68 Ω )
| 1 - small signal NMOS transistor (enhancement mode CD4007 or ZVN2110A)

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in the diagram below. The channel A generator voltage output drives one end of resistor R\ :sub:`1`. Resistor R\ :sub:`2` is connected between the gate and drain of transistor M\ :sub:`1` with the other end of resistor R\ :sub:`1` connected to the gate as well. The source of M\ :sub:`1`\ is grounded thus M\ :sub:`1` is in a common source configuration.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab7m_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NMOS Zero Gain Amplifier


Hardware Setup:
~~~~~~~~~~~~~~~

The waveform generator CHA-V should be configured for a 100 Hz triangle wave with 4 volt Max and 0 V Min. Select scope trace for CHA-V for display. The input of scope CHB-H is used to measure alternately the gate and drain voltage of M\ :sub:`1`.

Procedure:
~~~~~~~~~~

Remembering back to the common source amplifier in the previous section, if R\ :sub:`L` is set equal to r\ :sub:`s` (1/g\ :sub:`m`) then the gain A will be -1. If the gate is connected to the top of resistor R\ :sub:`L`\ then the gain from the gate to the drain (bottom of R\ :sub:`L`) will be -1. Also, neglecting the drain source output impedance of the transistor the gain from the top of load resistor R\ :sub:`L` to the drain (bottom of R\ :sub:`L`) will be +1. Thus the net gain superimposing both paths will be 1 - 1 = 0.

In the figure below we have a transistor biased into saturation region with a drain voltage which is less than the gate voltage by , (equal to I\ :sub:`D` times 50 ohms) and is essentially constant with input voltage changes applied from the waveform generator.

Questions:
~~~~~~~~~~

What are the relative gains of the two paths when the drain current is less than and greater than the "ideal" zero gain value?

**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
