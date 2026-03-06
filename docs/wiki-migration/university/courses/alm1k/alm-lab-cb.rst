Activity: The Common Base Amplifier
===================================

Objective:
----------

To investigate the simple NPN common base amplifier also sometimes referred to as the cascode configuration.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 100 Ω Resistor ( R\ :sub:`C` )
| 1 - small signal NPN transistor ( 2N3904 or similar Q\ :sub:`1` )

Directions:
~~~~~~~~~~~

The breadboard connections for the common base amplifier tests are shown in figure 1. The 2.5V mid supply voltage output is used as the fixed common voltage point for the base terminal. An input current is supplied to the emitter from channel A in source current mode. Channel B in Hi-Z mode measures the collector voltage.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_labcb_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Common Base Amplifier


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured in the SIMV mode with a 100 Hz Sine wave with -20 mA Min and 0 mA Max value. The measured voltage waveform trace for channel A is used to display the emitter voltage. The scope channel CB-H is used to measure the voltage at the collector.

Procedure:
~~~~~~~~~~

Using the measurement plots and data taken calculate the voltage gain, current gain, input resistance and output resistance for the common base amplifier.

| Voltage gain approximate expression:
| A\ :sub:`V` = g\ :sub:`m`\ R\ :sub:`C`

| Current gain approximate expression:
| A\ :sub:`I` = I\ :sub:`C`/I\ :sub:`E` = αI\ :sub:`E`

| Input resistance approximate expression:
| R\ :sub:`In` = r\ :sub:`e` ˜ 1/g\ :sub:`m`

| Output resistance approximate expression:
| R\ :sub:`Out` = R\ :sub:`C`\ \||r\ :sub:`o` ˜ R\ :sub:`C` ( when R\ :sub:`C` << r\ :sub:`o` )

Questions:
~~~~~~~~~~

| What is the maximum peak to peak output voltage swing that can be produced with the common base stage as shown in figure 1?
| What limits the maximum and minimum voltage extremes and why?
| What happens to the input impedance when the output reaches one or the other extreme?
| What happens to the output impedance when the output reaches one or the other extreme?

**For Further Reading:**

http://en.wikipedia.org/wiki/Common_base

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
