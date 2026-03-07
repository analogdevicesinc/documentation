Activity: MOS Multivibrators, For ADALM1000
===========================================

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A multivibrator circuit consists generally of two inverting amplifier stages. The two amplifiers are connected in series or cascade, and a feedback path connects from the output of the second amplifier back to the input of the first. Because each stages inverts the signal, the overall feedback around the loop is positive. There are three main types of multivibrators. In the astable multivibrator capacitors are used to couple the two amplifier stages and provide the feedback path. Since the capacitors block any DC signals (sometimes referred to as state) from passing from one stage to the next the astable multivibrator has no stable DC operating point and is thus a free-running oscillator. In the monostable multivibrator the coupling from one of the stages to the other uses one capacitor while the second connection is through a DC path. Thus the monostable multivibrator has one stable DC stage. Hence, monostable or as it is sometimes referred to as a one-shot. The circuit maintains this single stable state except when a triggering pulse is applied. Then the state changes for a predetermined length of time set by the RC time constant of the AC coupled part of the signal path. In the bistable multivibrator both coupling paths are DC coupled and thus the circuit has two different stable states and uses no capacitors. The bistable multivibrator is also called a flip-flop, with either of two DC stable states.

The Astable Multivibrator
-------------------------

Objectives:
~~~~~~~~~~~

The objective of this first experiment is to build an astable multivibrator. Two identical resistance-capacitance networks determine the frequency at which oscillation will occur. The amplifying devices (transistors) are connected in a common source configuration, as shown in figure 1.

Materials:
~~~~~~~~~~

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

Directions:
~~~~~~~~~~~

Construct the circuit as shown in figure 1 on your solder-less breadboard. The green boxes indicate connections to the M1000 hardware. Note: there is no input from the M1000 just the power supply. The first inverting amplifier stage consists of M\ :sub:`1` with R\ :sub:`1` and the Red LED serving as the output load. The second inverting amplifier stage consists of M\ :sub:`2` with R\ :sub:`2` and the Green LED serving as the load. C\ :sub:`1` couples the output of the first stage at the drain of M\ :sub:`1` to the input of the second stage at the gate of M\ :sub:`2`. Similarly, C\ :sub:`2` couples the output of the second stage at the drain of M\ :sub:`2` back to the input of the first stage at the gate of M\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab24m_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Astable Multivibrator


Procedure:
~~~~~~~~~~

Connect the +5 V power supply only after you have completely built and checked the circuit. The red and green LEDs should alternately blink on and off at about a 1 second interval. You can also use the scope channels to monitor the output waveforms (Q and Qbar).

The frequency of oscillation is very slow due to the large values of capacitors C\ :sub:`1` and C\ :sub:`2`. Replace C\ :sub:`1` and C\ :sub:`2` with 0.1uF capacitors. The circuit should oscillate much faster now such that both LEDs seem to be on at the same time. Using the scope channels you should now measure the frequency and period of the output waveforms.

Questions:
~~~~~~~~~~

| What would be the effect of decreasing or increasing the values of both capacitors?
| What would be the effect of decreasing C\ :sub:`1` and increasing C\ :sub:`2` but keeping the total of C\ :sub:`1`\ +C\ :sub:`2` the same?

The Monostable Multivibrator
----------------------------

.. _objectives-1:

Objectives:
~~~~~~~~~~~

The objective of this second experiment is to build an monostable multivibrator. One resistance-capacitance network determines the duration of the one-shot output. The amplifying devices (transistors) are connected in a common-source configuration, as shown in figure 2.

.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 2 - 470Ω Resistors
| 1 - 1KΩ Resistors
| 1 - 20KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - 47KΩ Resistor
| 1 - small signal diode (1N914)
| 2 - small signal NMOS transistors (ZVN2110A)
| 1 - Red LED
| 1 - Green LED
| 1 - 47uF Capacitor

.. _directions-1:

Directions:
~~~~~~~~~~~

Construct the circuit as shown in figure 2 on your solder-less breadboard. Disconnect the +5 V power supply before you make any changes to your breadboard. The green boxes indicate connections to the M1000 module. Starting with the circuit from experiment 1, remove one of the 20KΩ resistors (old R\ :sub:`3`) and replace capacitor C\ :sub:`1` with a 1KΩ resistor (new R\ :sub:`3`). Add diode D\ :sub:`1` and resistor R\ :sub:`5` as shown to the gate of M\ :sub:`2`. Be sure to replace C\ :sub:`2` with the original 47 uF capacitor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab24m_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Monostable Multivibrator


.. _procedure-1:

Procedure:
~~~~~~~~~~

Connect the +5 V power supply only after you have completely built and checked the circuit. The red LED should be lit and the green LED should be dark. With a length of wire, momentarily touch the Trigger input (end of R\ :sub:`5`) to +5 V and immediately let go. The red LED should go out and the green LED come on for about a second and then go back to the stable state with the red on and green off. Try this a few times.

Now replace C\ :sub:`2` with a 0.1uF capacitor. Connect the channel A generator output, CA-V to the Trigger input. Configure the generator as a square wave with a Max of 5V and a Min of 0 V. Set the frequency to 50 Hz and the duty cycle to 10%. Use the channel B scope input CB-H to observe the output waveforms seen at Q and Qbar.

.. _questions-1:

Questions:
~~~~~~~~~~

What would be the effect of decreasing or increasing the value of capacitor C\ :sub:`2`?

The Bistable Multivibrator (or flip-flop)
-----------------------------------------

.. _objectives-2:

Objectives:
~~~~~~~~~~~

The objective of this third experiment is to build an bistable multivibrator. The amplifying devices (transistors) are connected in a common-source configuration, as shown in figure 3.

.. _materials-2:

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 2 - 470Ω Resistors
| 2 - 1KΩ Resistors
| 2 - 47KΩ Resistors
| 2 - small signal NMOS transistors (ZVN2110A)
| 2 - small signal diodes (1N914)
| 1 - Red LED
| 1 - Green LED

.. _directions-2:

Directions:
~~~~~~~~~~~

Construct the circuit as shown in figure 3 on your solder-less breadboard. Disconnect the +5 V power supply before you make any changes to your breadboard. The green boxes indicate connections to the M1000 module.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab24m_f3.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 3, Bistable Multivibrator


.. _procedure-2:

Procedure:
~~~~~~~~~~

Connect the +5 V power supply only after you have completely built and checked the circuit. Either the red LED should be lit with the green LED dark or the green LED should be lit with the red LED dark. With a length of wire, momentarily touch either the SET or RESET input (end of R\ :sub:`5` or R\ :sub:`6`) to +5 V and immediately let go. The LEDs should change state or toggle back and forth depending which input is touched to +5 V. Try this a few times.

.. _questions-2:

Questions:
~~~~~~~~~~

**For Further Reading:**

| http://en.wikipedia.org/wiki/Multivibrator
| http://www.wisc-online.com/objects/ViewObject.aspx?ID=DIG5303

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
