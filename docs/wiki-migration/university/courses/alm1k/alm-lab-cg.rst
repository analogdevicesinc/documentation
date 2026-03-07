Activity: The Common Gate Amplifier
===================================

Objective:
----------

To investigate the simple NMOS common gate amplifier also sometimes referred to as the cascode configuration.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 100 Ω Resistor ( R\ :sub:`D` )
| 1 - small signal NMOS transistor ( ZVN2110A or similar M\ :sub:`1` )

Directions:
~~~~~~~~~~~

The breadboard connections for the common gate amplifier tests are shown in figure 1. The 2.5V mid supply voltage output is used as the fixed common voltage point for the gate terminal. An input current is supplied to the source from channel A in source current mode. Channel B in Hi-Z mode measures the drain voltage.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_labcg_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Common Gate Amplifier


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured in the SIMV mode with a 100 Hz Sine wave with -20 mA Min and 0 mA Max value. The measured voltage waveform trace for channel A is used to display the source voltage. The scope channel CB-H is used to measure the voltage at the drain.

Procedure:
~~~~~~~~~~

Using the measurement plots and data taken calculate the voltage gain, current gain, input resistance and output resistance for the common gate amplifier.

| Voltage gain approximate expression:
| A\ :sub:`V` = g\ :sub:`m`\ R\ :sub:`D`

| Current gain approximate expression:
| A\ :sub:`I` = I\ :sub:`D`/I\ :sub:`S` = 1 ( assuming zero gate current )

| Input resistance approximate expression:
| R\ :sub:`In` ˜ 1/g\ :sub:`m`

| Output resistance approximate expression:
| R\ :sub:`Out` = R\ :sub:`D`\ \||r\ :sub:`o` ˜ R\ :sub:`D` ( when R\ :sub:`D` << r\ :sub:`o` )

Questions:
~~~~~~~~~~

| What is the maximum peak to peak output voltage swing that can be produced with the common gate stage as shown in figure 1?
| What limits the maximum and minimum voltage extremes and why?
| What happens to the input impedance when the output reaches one or the other extreme?
| What happens to the output impedance when the output reaches one or the other extreme?

The Active Cascode
------------------

The common gate amplifier is more commonly referred to as a cascode when combined with another amplifier stage such as a common source amplifier. When the input and output impedances achieved from the simple common gate or cascode are not sufficient, the active cascode configuration is employed. Other terms that might be uses are "super" common gate, "regulated" common gate or cascode, "gain boosted" common gate or cascode.

In the active cascode rather than simply connecting the gate of the transistor to a small signal ground or common an amplifier is used to adjust the voltage applied to the gate so as to reduce the changes seen at the transistor source terminal as the input current changes. In effect the small signal source resistance, r\ :sub:`s`, is reduced by the gain of the amplifier. In the following experiment we will use a second NMOS device as an inverting common source amplifier to "regulate" the gate voltage of the cascode transistor.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 1 - 1 KΩ Resistor ( R\ :sub:`1` )
| 1 - small signal NMOS transistor ( ZVN2110A or similar M\ :sub:`2` )

.. _directions-1:

Directions:
~~~~~~~~~~~

Modify the test circuit on your breadboard to look like figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_labcg_f2.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 2 Active Cascode


.. _hardware-setup-1:

Hardware setup:
~~~~~~~~~~~~~~~

You should be able to use the same settings you used for the simple common gate amplifier. You will want to use the CB-H scope channel to observe the waveform at the gate of M\ :sub:`1` as well as the drain voltage.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Compare the channel A voltage trace, CA-V, to what you observed for the simple common gate amplifier. Use the change in M\ :sub:`1`'s source voltage vs. the source current to calculate the voltage gain and input resistance as you did for the simple common gate amplifier.

With scope channel B, CB-H, connected to the gate of M\ :sub:`1`, compare the waveform observed to the source voltage waveform you observed for the simple common gate amplifier.

.. _questions-1:

Questions:
~~~~~~~~~~

Change resistor R\ :sub:`1` from a 1 KΩ to a 10 KΩ and re-measure the amplitude of the waveforms seen at the gate and source of M\ :sub:`1`. How have they changed if at all and why? Try other values for R\ :sub:`1` to see if the waveform amplitude changes. What is the small signal voltage gain of the common source stage from the gate of M\ :sub:`2` to the drain of M\ :sub:`2` for each value of R\ :sub:`1`?

Increase the negative swing of channel A's current until the channel A voltage waveform is no longer more or less constant. Observe the voltage waveform at the gate of M\ :sub:`1`. How has it changed and why?

**For Further Reading:**

| http://en.wikipedia.org/wiki/Common_gate
| http://en.wikipedia.org/wiki/Cascode

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
