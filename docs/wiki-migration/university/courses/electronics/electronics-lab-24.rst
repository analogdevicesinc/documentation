Activity: BJT Multivibrators, For ADALM2000
===========================================

Background:
-----------

A multivibrator circuit consists generally of two inverting amplifier stages. The two amplifiers are connected in series or cascade, and a feedback path connects from the output of the second amplifier back to the input of the first. Because each stages inverts the signal, the overall feedback around the loop is positive. There are three main types of multivibrators. In the astable multivibrator capacitors are used to couple the two amplifier stages and provide the feedback path. Since the capacitors block any DC signals (sometimes referred to as state) from passing from one stage to the next the astable multivibrator has no stable DC operating point and is thus a free-running oscillator. In the monostable multivibrator the coupling from one of the stages to the other uses one capacitor while the second connection is through a DC path. Thus the monostable multivibrator has one stable DC stage. Hence, monostable or as it is sometimes referred to as a one-shot. The circuit maintains this single stable state except when a triggering pulse is applied. Then the state changes for a predetermined length of time set by the RC time constant of the AC coupled part of the signal path. In the bistable multivibrator both coupling paths are DC coupled and thus the circuit has two different stable states and uses no capacitors. The bistable multivibrator is also called a flip-flop, with either of two DC stable states.

The Astable Multivibrator
=========================

Objectives:
-----------

The objective of this first experiment is to build an astable multivibrator. Two identical resistance-capacitance networks determine the frequency at which oscillation will occur. The amplifying devices (transistors) are connected in a common-emitter configuration, as shown in figure 1.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 470 Ω Resistors
| 2 - 20 KΩ Resistors
| 2 - small signal NPN transistors (2N3904)
| 1 - Red LED
| 1 - Green LED
| 2 - 47 uF Capacitors

Directions:
-----------

Construct the circuit as shown in figure 1 on your solder-less breadboard. The green boxes indicate connections to the ADALM2000. Note: there is no input from the ADALM2000 board just the power supply. The first inverting amplifier stage consists of Q\ :sub:`1` with R\ :sub:`1` and the Red LED serving as the output load. The second inverting amplifier stage consists of Q\ :sub:`2` with R\ :sub:`2` and the Green LED serving as the load. C\ :sub:`1` couples the output of the first stage at the collector of Q\ :sub:`1` to the input of the second stage at the base of Q\ :sub:`2`. Similarly, C\ :sub:`2` couples the output of the second stage at the collector of Q\ :sub:`2` back to the input of the first stage at the base of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Astable Multivibrator


Procedure:
----------

| Turn on the Vp power supply only after you have completely built and checked the circuit. The red and green LEDs should alternately blink on and off at about a 1 second interval. You can also use the scope channels to monitor the output waveforms (Q and Qbar).
| |image1|
|

.. container:: centeralign

   Figure 2, Astable Multivibrator Breadboard Circuit


| The frequency of oscillation is very slow due to the large values of capacitors C\ :sub:`1` and C\ :sub:`2`. Replace C\ :sub:`1` and C\ :sub:`2` with 0.1uF capacitors. The circuit should oscillate much faster now such that both LEDs seem to be on at the same time. Using the scope channels you should now measure the frequency and period of the output waveforms.

|image2|

.. container:: centeralign

   Figure 3, Astable Multivibrator interval at 47uF capacitor


   |image3|

.. container:: centeralign

   Figure 4, Astable Multivibrator interval at 0.1uF capacitor


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

The objective of this second experiment is to build an monostable multivibrator. One resistance-capacitance network determines the duration of the one-shot output. The amplifying devices (transistors) are connected in a common-emitter configuration, as shown in figure 2.

.. _materials-1:

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 470 Ω Resistors
| 1 - 1 KΩ Resistor
| 1 - 20 KΩ Resistor
| 1 - 47 KΩ Resistor
| 1 - small signal diode (1N914)
| 2 - small signal NPN transistors (2N3904)
| 1 - Red LED
| 1 - Green LED
| 1 - 47 uF Capacitor

.. _directions-1:

Directions:
-----------

Construct the circuit as shown in figure 2 on your solder-less breadboard. The green boxes indicate connections to the ADALM2000. Starting with the circuit from experiment 1, remove one of the 20K? resistors (old R\ :sub:`3`) and replace capacitor C\ :sub:`1` with a 47K? resistor (new R\ :sub:`3`). Add diode D\ :sub:`1` and resistor R\ :sub:`5` as shown to the base of Q\ :sub:`2`. Be sure to replace C\ :sub:`2` with the original 47 uF capacitor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24_f2.png
   :align: center
   :width: 500px

|

.. container:: centeralign

   Figure 5, Monostable Multivibrator


| |image4|
|

.. container:: centeralign

   Figure 6, Monostable Multivibrator Breadboard Circuit


.. _procedure-1:

Procedure:
----------

Turn on the Vp power supply only after you have completely built and checked the circuit. The red LED should be lit and the green LED should be dark. With a length of wire, momentarily touch the trigger input (end of R\ :sub:`5`) to Vp and immediately let go. The red LED should go out and the green LED come on for about a second and then go back to the stable state with the red on and green off. Try this a few times.

| |image5|

.. container:: centeralign

   Figure 6, Monostable Multivibrator Behavior on trigger


.. _questions-1:

Questions:
----------

Add questions here:

The Bistable Multivibrator ( or flip-flop )
===========================================

.. _objectives-2:

Objectives:
-----------

The objective of this third experiment is to build an bistable multivibrator. The amplifying devices (transistors) are connected in a common-emitter configuration, as shown in figure 3.

.. _materials-2:

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 470 Ω Resistors
| 2 - 1 KΩ Resistors
| 2 - 47 KΩ Resistors
| 2 - small signal NPN transistors (2N3904)
| 2 - small signal diodes (1N914)
| 1 - Red LED
| 1 - Green LED

.. _directions-2:

Directions:
-----------

Construct the circuit as shown in figure 3 on your solder-less breadboard. The green boxes indicate connections to theADALM2000.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Bistable Multivibrator


.. image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_bistable_hardware_setup.png
   :align: center

.. container:: centeralign

   Figure 8, Bistable Multivibrator Breadboard Circuit


.. _procedure-2:

Procedure:
----------

Turn on the Vp power supply only after you have completely built and checked the circuit. Either the red LED should be lit with the green LED dark or the green LED should be lit with the red LED dark. With a length of wire, momentarily touch the either the SET or RESET input (end of R\ :sub:`5` or R\ :sub:`6`) to Vp and immediately let go. The LEDs should change state or toggle back and forth depending which input is touched to Vp. Try this a few times.


|image6|

.. container:: centeralign

   Figure 9, Bistable Multivibrator behavior triggering Set pin


   |image7|

.. container:: centeralign

   Figure 10, Bistable Multivibrator behavior triggering Reset pin


Connect the SET and RESET inputs to two of the digital I/O pins on the ADALM2000 connector. Configure the pins as push-pull outputs. Used the static digital I/O screen to control the digital pins.

.. _questions-2:

Questions:
----------

Add Questions here:

D-Type Flip-Flop
----------------

.. _objectives-3:

Objectives:
~~~~~~~~~~~

The objective of this fourth experiment is to use the bistable or set - reset flip-flop from experiment 3 to build what is known as a D-Type flip-flop.

.. _materials-3:

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 3 - 1 KΩ resistors
| 1 - 100 KΩ resistor
| 2 - 200 KΩ resistors
| 2 - 47 KΩ resistors
| 3 - small signal NPN transistors (2N3904)
| 2 - small signal diodes (1N914)
| 2 - 39 pF capacitors
| 2 - 100 pF capacitors

.. _directions-3:

Directions:
~~~~~~~~~~~

Construct the D type flip-flop circuit as shown in figure 4 on your solder-less breadboard. Note that the polarity of the two diodes is reversed compared to figure 3. Because this experiment will be done at much higher frequencies, the LEDs have been removed and simple 1 K? load resistors are used.

Switching between the two flip-flop states is achieved by applying the D (data) signal and a single clock pulse which, depending on the state of the D input with respect to the current state will, cause the "ON" transistor to turn "OFF" and the "OFF" transistor to turn "ON" on the negative or falling edge of the clock pulse. The true D signal and complement DB signal ( output of Q\ :sub:`3`, R\ :sub:`7` inverting stage ) are used to bias diodes D\ :sub:`1` and D\ :sub:`2` to steer the clock pulse to the correct base, the equivalent of the SET and RESET inputs in figure 3.

To illustrate how the circuit operates we will assume the circuit is in one of its two stable states with the QB output low ( collector voltage of Q\ :sub:`1` at 0 V ), and the Q output high ( collector voltage of Q\ :sub:`2` high at 5 V ). With the D input low ( DB high ) D\ :sub:`1` has a low voltage on its cathode via R\ :sub:`6` and a high voltage ( V\ :sub:`BE` of on transistor Q\ :sub:`1` ) on its anode via R\ :sub:`4`, making it forward biased. D\ :sub:`2` has a high voltage ( from DB ) on its cathode via R\ :sub:`5` and a low voltage on its anode via R\ :sub:`3` ( V\ :sub:`BE` of off transistor Q\ :sub:`2` ), making it reverse biased.

A negative going pulse on the Clock input, coupled through C\ :sub:`1` and C\ :sub:`2`, is steered to the base of Q\ :sub:`1` since D\ :sub:`1` is forward biased, but blocked from the base of Q\ :sub:`2` by reverse biased D\ :sub:`2`. Q\ :sub:`1` is turned off and Q\ :sub:`2` is turned on by the cross coupled connection through the parallel combination of C\ :sub:`3` and R\ :sub:`3`. This happens very quickly because of the positive feedback effect we saw earlier in the simple bistable multivibrator. The circuit is now in the other stable state with the Q output high and the QB output low. The circuit will remain in that state until the D input becomes high and after another negative going clock pulse arrives.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11 D type flip-flop


Hardware setup:
~~~~~~~~~~~~~~~

| The AWG1 output should be connected to the input marked Clock in figure 4. The AWG2 output should be connected to the D input. The first scope channel 1 input should also be connected to Clock input. The second input scope channel 2 should be connected to the Q output of the flip-flop in figure 4. Both the AWG1 and AWG2 should be configured as a square wave with a 5 V amplitude peak-to-peak and 2.5 V offset ( 0 - 5V swing ). Set the frequency of AWG1 to 10 KHz and set the frequency of AWG2 to 5 KHz. Set the phase of AWG2 to 45 degrees. Be sure to configure the two AWG outputs to operate synchronously.
| |image8|

.. container:: centeralign

   Figure 12 D type flip-flop breadboard circuit


.. _procedure-3:

Procedure:
~~~~~~~~~~

Turn on the Vp power supply and enable the AWG outputs only after you have completely built and checked the circuit. You should observe a square wave on the Q output which is aligned with the falling edge of the Clock input signal. Change the phase of AWG2 ( D input signal ) while observing this alignment. Does this change as the phase of the D input change? Move the channel 1 scope input to the D input. You should see a similar square wave signal but ahead in time with respect to the Q output. In other words the Q output is delayed until the falling edge of the Clock signal.


|image9|

.. container:: centeralign

   Figure 13: Plot of Q and Clock signal


   |image10|

.. container:: centeralign

   Figure 14: Plot of Q and D signal


.. _questions-3:

Questions:
~~~~~~~~~~

What is the purpose of capacitors C\ :sub:`3` and C\ :sub:`4`?

What if the highest clock frequency at which the circuit continues to function? What limits this maximum frequency?

The capacitor coupling ( AC coupling ) of the clock input relies on the rise and fall time ( dV/dT ) of the input pulse to switch the state of the flip-flop. Use the trapezoidal waveform option for AWG 1 and use the symmetry control to adjust the rise/fall time of the waveform. What is the slowest dV/dT that will change the state of the flip-flop?

Divide by 2 Flip-Flop
---------------------

.. _objectives-4:

Objectives:
~~~~~~~~~~~

The objective of this fifth experiment is to modify the D-type flip-flop from experiment 4 to build a circuit that divides the frequency of an input signal by 2.

.. _materials-4:

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 1 KΩ resistors
| 2 - 200 KΩ resistors
| 2 - 47 KΩ resistors
| 2 - small signal NPN transistors (2N3904)
| 2 - small signal diodes (1N914)
| 2 - 39 pF capacitors
| 2 - 100 pF capacitors

.. _directions-4:

Directions:
~~~~~~~~~~~

Modify the D-type flip-flop from experiment four to construct the divide by 2 circuit as shown in figure 5 on your solder-less breadboard.

Switching between the two states is achieved by applying a single clock pulse which in turn will cause the "ON" transistor to turn "OFF" and the "OFF" transistor to turn "ON" on the negative or falling edge of the clock pulse. The circuit will switch sequentially by applying a pulse to each base in turn and this is achieved from a single input clock pulse using biasing the two diodes to steer the pulse to the correct base based on the current state of the flip-flop.

To illustrate how the circuit operates we will assume the circuit is in one of its two stable states with the collector voltage of Q\ :sub:`1` low (0 V), and that of Q\ :sub:`2` high (5 V). D\ :sub:`1` has a low voltage on its cathode via R\ :sub:`6` and a high voltage ( V\ :sub:`BE` of on transistor Q\ :sub:`1` ) on its anode via R\ :sub:`4`, making it forward biased. D\ :sub:`2` has a high voltage on its cathode via R\ :sub:`5` and a low voltage on its anode via R\ :sub:`3` ( V\ :sub:`BE` of off transistor Q\ :sub:`2` ), making it reverse biased.

An external negative going pulse, coupled through C\ :sub:`1` and C\ :sub:`2`, is steered to the base of Q\ :sub:`1` since D\ :sub:`1` is forward biased, but blocked from the base of Q\ :sub:`2` by reverse biased D\ :sub:`2`. Q\ :sub:`1` is turned off and Q\ :sub:`2` is turned on by the cross coupled connection through the parallel combination of C\ :sub:`3` and R\ :sub:`3`. This happens very quickly because of the positive feedback effect we saw earlier in the simple bistable multivibrator. The circuit is now in its second stable state and waits for another negative going clock pulse.

Since the collector voltage of Q\ :sub:`2` , the Q output node, changes state for every clock pulse, there is one pulse appearing at the output for every two clock input pulses. It can therefore be used as a divide by two circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a24_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 15 Divide by 2 circuit


.. _hardware-setup-1:

Hardware setup:
~~~~~~~~~~~~~~~

The AWG1 output and scope channel 1 input should both be connected to the input marked Clock in figure 13. The second input scope channel 2 should be connected to the Q output of the flip-flop in figure 5. The AWG1 should be configured as a square wave with a 5 V amplitude peak-to-peak and 2.5 V offset ( 0 - 5V swing ). Set the frequency to 10 KHz.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_divide_by_2_flipflop_hardware_setup.png
   :align: center

.. container:: centeralign

   Figure 16 Divide by 2 flipflop breadboard circuit


.. _procedure-4:

Procedure:
~~~~~~~~~~

Turn on the Vp power supply and enable AWG1 output only after you have completely built and checked the circuit. You should observe a square wave on the Q output which is one half the frequency of the AWG 1 signal. Move the channel 2 scope input to the QB output. You should see a similar square wave signal but inverted with respect to the Q output.


|image11|

.. container:: centeralign

   Figure 15: Plot of Clock and Q output


   |image12|

.. container:: centeralign

   Figure 16: Plot of Clock and QB output


.. _questions-4:

Questions:
~~~~~~~~~~

What if the highest clock frequency at which the circuit continues to function? What limits this maximum frequency?

Reverse the polarity ( direction ) of the two steering diodes, D\ :sub:`1` and D\ :sub:`2`. What is the effect on the relative timing of the Q and QB outputs with respect to the input clock signal? Explain why it has changed.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bjt_multivib_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/bjt_multivib_ltspice`
   


For further reading:
~~~~~~~~~~~~~~~~~~~~

http://en.wikipedia.org/wiki/Multivibrator

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_astable_hardware_setup.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_astable_scopeshot_1second_interval.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_astable_scopeshot_0.1ufcap.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_monostable_hardware_setup.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_monostable_scopeshot.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_bistable_scopeshot1.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_bistable_scopeshot2.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_dflipflop_hardware_setup.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_dflipflop_scopeshot1.png
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_dflipflop_scopeshot2.png
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_divide_by_2_flipflop_scopeshot1.png
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/bjtmultivibrators_divide_by_2_flipflop_scopeshot2.png
