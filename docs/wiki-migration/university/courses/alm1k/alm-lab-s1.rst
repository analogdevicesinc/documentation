Activity S1: Electret microphone preamplifier
=============================================

Objective:
----------

The objective of this Lab activity is to explore the electret microphone bias techniques and a two stage preamplifier circuit.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Electret is a quasi-permanently charged dielectric. It is made by heating a ceramic material, placing it in a magnetic field then allowing it to cool while still in the magnetic field. It is the electrostatic equivalent of a permanent magnet. In an electret microphone a slice of this material is used as a part of the dielectric of a capacitor in which the diaphragm of the microphone forms one plate. Sound pressure moves the diaphragm. The movement of the plate varies the capacitance according to the sound pressure. Given the built-in fixed charge of the dielectric, the voltage across the capacitor will also vary. The electret capacitor is connected to the input of a built in FET amplifier. Electret microphones are small, have excellent sensitivity, a wide frequency response and generally a very low cost.

The terminals:
~~~~~~~~~~~~~~

The terminal with a solder mark (connecting to the case) is negative and the terminal without a mark is positive as shown for a typical microphone in figure 1. Case styles and terminal markings may vary from manufacturer to manufacturer. Double check the polarity of your microphone before connecting it to your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-s1_f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1 Electret Microphone terminals


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard, and jumper wire kit
| 3 - 1 KΩ resistors
| 2 - 10 KΩ resistors
| 1 - 20 KΩ resistor
| 2 - 2N3904 NPN transistor (or SSM2212 matched pair)
| 1 - 10 uF capacitor
| 1 - 47 uF capacitor
| 1 - 220 uF capacitor
| 1 - Electret microphone

Directions:
~~~~~~~~~~~

Build the microphone bias and preamplifier circuit shown in figure 2 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-s1_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Electret microphone pre-amplifier


Hardware Setup:
~~~~~~~~~~~~~~~

To produce a sound to pick up with the microphone, a good choice is a small 8 Ω audio speaker connected to the channel A voltage generator output CA-V as shown in figure 2. A mechanical or piezo electric buzzer or transducer could work to produce a sound as well. Set the channel A to produce a 1000 Hz sinewave with a 1.0 V Min value and 4.0 V Max value. Position the speaker near to and directly facing the microphone. Scope channel B is set up in the Hi-Z mode and set to 0.2 V/div centered on DC value seen at the output which should be near 2.5 V.

Procedure:
~~~~~~~~~~

Change the frequency of the CA-V generator and observe amplitude response of the combined speaker and microphone.

Measure the amplitude of the signal seen at the base of Q\ :sub:`1` and calculate the gain of the preamplifier.

Questions:
~~~~~~~~~~

Change the relative distance between the speaker and microphone an observe the amplitude response. Make special note of the relative phase of the output sine wave with respect to the channel A signal driving the speaker. How does this phase change with frequency and distance?

**For Further Reading:**

| `Electret <https://en.wikipedia.org/wiki/Electret>`__
| `Electret microphone <https://en.wikipedia.org/wiki/Electret_microphone>`__

**Return to ALM Lab Activity\ **\ :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**
