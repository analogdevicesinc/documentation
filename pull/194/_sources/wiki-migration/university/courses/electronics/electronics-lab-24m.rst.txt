Activity: MOS Multivibrators, For ADALM2000
===========================================

Background:
-----------

A multivibrator circuit consists generally of two inverting amplifier stages. The two amplifiers are connected in series or cascade, and a feedback path connects from the output of the second amplifier back to the input of the first. Because each stages inverts the signal, the overall feedback around the loop is positive. There are three main types of multivibrators. In the astable multivibrator capacitors are used to couple the two amplifier stages and provide the feedback path. Since the capacitors block any DC signals (sometimes referred to as state) from passing from one stage to the next the astable multivibrator has no stable DC operating point and is thus a free-running oscillator. In the monostable multivibrator the coupling from one of the stages to the other uses one capacitor while the second connection is through a DC path. Thus the monostable multivibrator has one stable DC stage. Hence, monostable or as it is sometimes referred to as a one-shot. The circuit maintains this single stable state except when a triggering pulse is applied. Then the state changes for a predetermined length of time set by the RC time constant of the AC coupled part of the signal path. In the bistable multivibrator both coupling paths are DC coupled and thus the circuit has two different stable states and uses no capacitors. The bistable multivibrator is also called a flip-flop, with either of two DC stable states.

The Astable Multivibrator
=========================

Objectives:
-----------

The objective of this first experiment is to build an astable multivibrator. Two identical resistance-capacitance networks determine the frequency at which oscillation will occur. The amplifying devices (transistors) are connected in a common source configuration, as shown in figure 1.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 470 Ω Resistors
| 2 - 20 KΩ Resistors
| 2 - 10 KΩ Resistors
| 2 - small signal NMOS transistors (ZVN2110A)
| 1 - Red LED
| 1 - Green LED
| 2 - 47 uF Capacitors

Directions:
-----------

Construct the circuit as shown in figure 1 on your solder-less breadboard. The green boxes indicate connections to the ADALM2000. Note: there is no input from the ADALM2000 board just the power supply. The first inverting amplifier stage consists of M\ :sub:`1` with R\ :sub:`1` and the Red LED serving as the output load. The second inverting amplifier stage consists of M\ :sub:`2` with R\ :sub:`2` and the Green LED serving as the load. C\ :sub:`1` couples the output of the first stage at the drain of M\ :sub:`1` to the input of the second stage at the gate of M\ :sub:`2`. Similarly, C\ :sub:`2` couples the output of the second stage at the drain of M\ :sub:`2` back to the input of the first stage at the gate of M\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Astable Multivibrator


   |image1|

.. container:: centeralign

   Figure 2, Astable Multivibrator breadboard circuit


Procedure:
----------

Turn on the Vp power supply only after you have completely built and checked the circuit. The red and green LEDs should alternately blink on and off at about a 1 second interval. You can also use the scope channels to monitor the output waveforms (Q and Qbar).

The frequency of oscillation is very slow due to the large values of capacitors C\ :sub:`1` and C\ :sub:`2`. Replace C\ :sub:`1` and C\ :sub:`2` with 0.1uF capacitors. The circuit should oscillate much faster now such that both LEDs seem to be on at the same time. Using the scope channels you should not measure the frequency and period of the output waveforms.

Questions:
----------

| 1. What are the two most important components in the multivibrator circuit shown in figure 1?
| 2. What would be the effect of increasing or decreasing the value of only one capacitor?
| 3. What would be the effect of increasing or decreasing the value of both capacitors?
| Add more questions here:

The Monostable Multivibrator
============================

.. _objectives-1:

Objectives:
-----------

The objective of this second experiment is to build an monostable multivibrator. One resistance-capacitance network determines the duration of the one-shot output. The amplifying devices (transistors) are connected in a common-source configuration, as shown in figure 2.

.. _materials-1:

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 470 Ω Resistors
| 1 - 1 KΩ Resistors
| 1 - 20 KΩ Resistor
| 1 - 10 KΩ Resistor
| 1 - 47 KΩ Resistor
| 1 - small signal diode (1N914)
| 2 - small signal NMOS transistors (ZVN2110A)
| 1 - Red LED
| 1 - Green LED
| 1 - 47 uF Capacitor

.. _directions-1:

Directions:
-----------

Construct the circuit as shown in figure 4 on your solder-less breadboard. The green boxes indicate connections to the ADALM2000. Starting with the circuit from experiment 1, remove one of the 20K? resistors (old R\ :sub:`3`) and replace capacitor C\ :sub:`1` with a 1K? resistor (new R\ :sub:`3`). Add diode D\ :sub:`1` and resistor R\ :sub:`5` as shown to the base of M\ :sub:`2`. Be sure to replace C\ :sub:`2` with the original 47 uF capacitor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Monostable Multivibrator


.. image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_monostablemultivibrator_hardwaresetup.png
   :align: center

.. container:: centeralign

   Figure 5, Monostable Multivibrator Breadboard Circuit


.. _procedure-1:

Procedure:
----------

Turn on the Vp power supply only after you have completely built and checked the circuit. The red LED should be lit and the green LED should be dark. With a length of wire, momentarily touch the trigger input (end of R\ :sub:`5`) to Vp and immediately let go. The red LED should go out and the green LED come on for about a second and then go back to the stable state with the red on and green off. Try this a few times.

.. _questions-1:

Questions:
----------

Add questions here:

The Bistable Multivibrator (or flip-flop)
=========================================

.. _objectives-2:

Objectives:
-----------

The objective of this third experiment is to build an bistable multivibrator. The amplifying devices (transistors) are connected in a common-source configuration, as shown in figure 3.

.. _materials-2:

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 470 Ω Resistors
| 2 - 1 KΩ Resistors
| 2 - 47 KΩ Resistors
| 2 - small signal NMOS transistors (ZVN2110A)
| 2 - small signal diodes (1N914)
| 1 - Red LED
| 1 - Green LED

.. _directions-2:

Directions:
-----------

Construct the circuit as shown in figure 7 on your solder-less breadboard. The green boxes indicate connections to the ADALM2000.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24m_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Bistable Multivibrator


.. _procedure-2:

Procedure:
----------

Turn on the Vp power supply only after you have completely built and checked the circuit. Either the red LED should be lit with the green LED dark or the green LED should be lit with the red LED dark. With a length of wire, momentarily touch the either the SET or RESET input (end of R\ :sub:`5` or R\ :sub:`6`) to Vp and immediately let go. The LEDs should change state or toggle back and forth depending which input is touched to Vp. Try this a few times.

.. _questions-2:

Questions:
----------

Add questions here:

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  LTspice files: :git-education_tools:`m2k/ltspice/nmos_multivib_ltspice`
   


For further reading:
~~~~~~~~~~~~~~~~~~~~

http://en.wikipedia.org/wiki/Multivibrator

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_astablemultivibrator_hardwaresetup.png
