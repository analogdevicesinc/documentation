Activity: LED flasher, For ADALM1000
====================================

Objective:
----------

The objective of this lab activity is to build a circuit that will slowly flash LEDs. The astable multivibrator is the basis for this circuit.

Notes:
~~~~~~

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

In this Lab you will be using one or both of the channels of the ALM1000 in the split Input / Output mode. CB-OUT is used to denote the connection to the Output pin and CB-IN is used to denote the Input pin on the (expanded) 8 pin connector.

Background:
~~~~~~~~~~~

A multivibrator circuit consists generally of two inverting amplifier stages. The two amplifiers are connected in series or cascade, and a feedback path connects from the output of the second amplifier back to the input of the first. Because each stage inverts the signal, the overall feedback around the loop is positive. There are three main types of multivibrators. In the astable multivibrator capacitors are used to couple the two amplifier stages and provide the feedback path. Since the capacitors block any DC signals (sometimes referred to as state) from passing from one stage to the next the astable multivibrator has no stable DC operating point and is thus a free-running oscillator. In the monostable multivibrator the coupling from one of the stages to the other uses one capacitor while the second connection is through a DC path. Thus the monostable multivibrator has one stable DC stage. Hence, monostable or as it is sometimes referred to as a one-shot. The circuit maintains this single stable state except when a triggering pulse is applied. Then the state changes for a predetermined length of time set by the RC time constant of the AC coupled part of the signal path. In the bistable multivibrator both coupling paths are DC coupled and thus the circuit has two different stable states and uses no capacitors. The bistable multivibrator is also called a flip-flop, with either of two DC stable states.

The Astable Multivibrator
~~~~~~~~~~~~~~~~~~~~~~~~~

Two identical resistance-capacitance networks determine the frequency at which oscillation will occur. The amplifying devices (transistors) are connected in a common-emitter configuration, as shown in figure 1.

Materials:
----------

| ADALM1000 hardware module
| Solder-less breadboard and Jumper wire kit
| 2 - 470 Ω Resistors
| 2 - 20 KΩ Resistors
| 2 - small signal NPN transistors (2N3904)
| 1 - Red LED
| 1 - Green LED
| 2 - 47 uF Capacitors

Directions:
-----------

Construct the circuit as shown in figure 1 on your solder-less breadboard. Note: there is no input from the ALM1000 just the power supply. The first inverting amplifier stage consists of Q\ :sub:`1` with R\ :sub:`1` and the Red LED serving as the output load. The second inverting amplifier stage consists of Q\ :sub:`2` with R\ :sub:`2` and the Green LED serving as the load. C\ :sub:`1` couples the output of the first stage at the collector of Q\ :sub:`1` to the input of the second stage at the base of Q\ :sub:`2`. Similarly, C\ :sub:`2` couples the output of the second stage at the collector of Q\ :sub:`2` back to the input of the first stage at the base of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-24_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, NPN BJT Astable Multivibrator


Procedure:
----------

Connect the +5 V power supply only after you have completely built and checked the circuit. The red and green LEDs should alternately blink on and off at about a 1 second interval. You can also use the scope channels in high impedance mode to monitor the output waveforms (Q and Qbar).

The frequency of oscillation is very slow due to the large values of capacitors C\ :sub:`1` and C\ :sub:`2`. Replace C\ :sub:`1` and C\ :sub:`2` with smaller 1uF or 0.1 uF capacitors. The circuit should oscillate much faster now such that both LEDs seem to be on at the same time. Using the scope channels you can now measure the frequency and period of the output waveforms.

Questions:
----------

| What would be the effect of decreasing or increasing the values of both capacitors?
| What would be the effect of decreasing C\ :sub:`1` and increasing C\ :sub:`2` but keeping the total of C\ :sub:`1`\ +C\ :sub:`2` the same?

Substituting MOS transistors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The same circuit can be built substituting NMOS transistors for the NPN transistors used in figure 1. When MOS devices are used as amplifying devices we call the configuration common source, as shown in figure 2.

.. _materials-1:

Materials:
----------

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 2 - 470Ω Resistors
| 2 - 20KΩ Resistors
| 2 - 10KΩ Resistors
| 2 - small signal NMOS transistors (ZVN2110A)
| 1 - Red LED
| 1 - Green LED
| 2 - 47uF Capacitors

.. _directions-1:

Directions:
-----------

Construct the circuit as shown in figure 2 on your solder-less breadboard. The first inverting amplifier stage consists of M\ :sub:`1` with R\ :sub:`1` and the Red LED serving as the output load. The second inverting amplifier stage consists of M\ :sub:`2` with R\ :sub:`2` and the Green LED serving as the load. C\ :sub:`1` couples the output of the first stage at the drain of M\ :sub:`1` to the input of the second stage at the gate of M\ :sub:`2`. Similarly, C\ :sub:`2` couples the output of the second stage at the drain of M\ :sub:`2` back to the input of the first stage at the gate of M\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab24m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, NMOS Astable Multivibrator


.. _procedure-1:

Procedure:
----------

Connect the +5 V power supply only after you have completely built and checked the circuit. The red and green LEDs should alternately blink on and off at about a 1 second interval. You can also use the scope channels to monitor the output waveforms (Q and Qbar).

The frequency of oscillation is very slow due to the large values of capacitors C\ :sub:`1` and C\ :sub:`2`. Replace C\ :sub:`1` and C\ :sub:`2` with smaller 1uF or 0.1uF capacitors. The circuit should oscillate much faster now such that both LEDs seem to be on at the same time. Using the scope channels you should now measure the frequency and period of the output waveforms.

.. _questions-1:

Questions:
----------

| What would be the effect of decreasing or increasing the values of both capacitors?
| What would be the effect of decreasing C\ :sub:`1` and increasing C\ :sub:`2` but keeping the total of C\ :sub:`1`\ +C\ :sub:`2` the same?

**For Further Reading:**

| `The Multivibrator <https://en.wikipedia.org/wiki/Multivibrator>`__
| :doc:`BJT as a Switch </wiki-migration/university/courses/alm1k/alm-lab-4s>`
| :doc:`MOS as a Switch </wiki-migration/university/courses/alm1k/alm-lab-4ms>`

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
