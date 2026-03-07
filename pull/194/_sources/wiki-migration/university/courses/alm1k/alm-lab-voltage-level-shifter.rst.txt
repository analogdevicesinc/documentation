Activity: Logic Voltage Level Shifting, For ADALM1000
=====================================================

Objective:
----------

The objective of this lab activity is to explore a simple circuit that increase the voltage swing of a 3.3 V logic signal to 5.0 V or decrease the voltage swing of a 5.0 logic signal to 3.3 V.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

There are often many cases in digital systems where two or more sections of the system operate from different power supply voltages. When digital signals cross the boundary between these different power supply regions or domains it is necessary to insert a circuit block that translates or shifts the logic levels from the level supplied by one domain for example with a +3.3 Volt power supply to a second domain with a +5 Volt power supply.

The simplest form of a voltage level shifter as shown in figure 1, uses a pass NMOS device and a pull up resistor. If V\ :sub:`IN` at the input is at a logic low ( source of M\ :sub:`N1` ) the output ( drain of M\ :sub:`N1` ) goes to ground. M\ :sub:`N1` will be on because its gate is connected to V\ :sub:`LV` and drives V\ :sub:`OUT` to ground. Conversely if V\ :sub:`IN` is at a logic high the source is at V\ :sub:`LV`. With the gate of M\ :sub:`N1` also at V\ :sub:`LVI` it will now be off which allows V\ :sub:`OUT` to be pulled up to V\ :sub:`HV` by resistor R\ :sub:`HV`.

Similarly for a high voltage to low voltage level shifter if the input and output of the circuit is reversed, the definition of the source and drain of M\ :sub:`N1` will be reversed. If V\ :sub:`IN` is at a logic low the right hand side of M\ :sub:`N1`, now the source , goes to logic low turning on the transistor ( gate connected to V\ :sub:`LV` ) and drives V\ :sub:`OUT` to logic low. With V\ :sub:`IN` is at a logic high, the right hand side of M\ :sub:`N1` is now equal to or more positive than either the gate or left side of M\ :sub:`N1`. The left side will now be considered the source and will be pulled up to V\ :sub:`LV` by R\ :sub:`LV`. With the gate also at V\ :sub:`LV` it will now be off which allows V\ :sub:`OUT` to be pulled up to V\ :sub:`LV` only by resistor R\ :sub:`LV`\ and not the input signal.

As we can see the same circuit can be used bidirectionally to translate signals in either direction between V\ :sub:`LV` and V\ :sub:`HV`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_logic-lvsh_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Voltage level shift


The ON resistance of the pass NFET, and the parasitic capacitance of the signal lines mainly determine the fall time of the output signal. Also, the rise time of the output signal is determined mostly by the value of the pull-up resistor on the output and the signal-line parasitic capacitance assuming the pass NFET turns off instantaneously, which is not generally the case but we assume it is for this discussion. An annoying aspect of resistor loaded level shifters such as this is the DC current that flows in resistors R\ :sub:`LV`\ and R\ :sub:`HV`. For the Low to High shifter a current equal to V\ :sub:`LV`/R\ :sub:`LV` flows when V\ :sub:`IN`, and V\ :sub:`HV`/R\ :sub:`HV` with V\ :sub:`OUT` low. As was just pointed out the transition time for the output is a function of R\ :sub:`HV` and any parasitic capacitance and there will be a trade-off between power dissipation and speed which will determine the optimal value for the pull up resistors.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 2 Each 100 KΩ, 47 KΩ 10 KΩ and 1 KΩ resistors
| 1 – NMOS transistor (ZVN2110A)

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 2 on your solder-less breadboard. Start by using 1 KΩ resistors for R\ :sub:`LV` and R\ :sub:`HV`. Use CHA-V to drive V\ :sub:`IN` and use the positive power supply, the fixed 3.3 V supply from the digital port connector for V\ :sub:`LV`. The fixed +5 V supplies V\ :sub:`HV`. Scope CB-H will be used to view the output waveforms.

There are two configurations of the level shifter circuit. The upper configuration in figure 2 shifts a low voltage logic signal to a high voltage logic level. The lower configuration in figure 2 shifts a high voltage logic signal to a low voltage logic level.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_logic-lvsh_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Two directions of level shifter


Hardware Setup:
~~~~~~~~~~~~~~~

For the upper Low – High level shift, configure channel A as a square wave with a 0 V Min and a 3.3V Max (0 to 5V swing). For the lower High - Low level shift set CHA max to 5.0 V. Set the frequency to 1 KHz.

Procedure:
~~~~~~~~~~

Display CHA-V and CHA-I traces to monitor the input signal. and CHB-V trace to observe the rising and falling edges of the output waveform. Replace the 1 KΩ resistors, R\ :sub:`LV` and R\ :sub:`HV`, with 10 KΩ, 47 KΩ and 100 KΩ resistors and compare the relative rise / fall times and CHA max current for each value. Do this for both the Low-High shift and High-Low shift configurations.

Questions:
~~~~~~~~~~

Are there any differences in delay or rise/fall times between the different pull-up resistor values of the level shifter? If so why? Compare the measured CHA max current for each resistor value and configuration. Are there any difference between the low to high vs high to low configurations especially for the higher values of R\ :sub:`LV` and R\ :sub:`HV`? If so explain why.

Using BJTs
----------

Two NPN transistors can be substituted for the single NMOS transistor connected as shown in figure 3. When the Enable input is high, a low-going input signal drives the emitter of one of the transistors as a common-base amplifier. The 10-kΩ resistor in the base circuit provides enough current to saturate the transistor and drop the V\ :sub:`CE` voltage to approximately 0.1 V, thereby pulling the output side low.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_logic-lvsh_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, NPN level shifter


The circuit acts in a way like an efficient diode. With the Enable input low, Both transistors are in effect off with or without input or output side power applied. This example shows a translation between a 3.3 V part of a system and a 5 V part of a system. For proper operation, the Enable input must not go above than the lower of the two supply voltages.

Extra Credit:
~~~~~~~~~~~~~

For extra credit try substituting the fixed 2.5 V supply for V\ :sub:`LV`\ and using either the fixed 3.3 V or fixed 5 V supply for V\ :sub:`HV`. Be sure to adjust the MAX voltage setting for the CHA output depending on which supplies are being used for V\ :sub:`LV` and V\ :sub:`HV`.

**For Further Reading:**

| `Logic Levels <http://en.wikipedia.org/wiki/Logic_level>`_
| `Low Voltage Logic Interfacing <http://www.analog.com/static/imported-files/tutorials/MT-098.pdf>`_

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**
