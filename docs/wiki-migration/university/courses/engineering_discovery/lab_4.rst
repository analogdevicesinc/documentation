Audio Amplifier with Electret Microphone
========================================

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/analogtv>4800540099001
   :alt: analogTV>4800540099001
   :align: right

Introduction
------------

In this experiment we design and build an audio amplifier that takes the small
output voltage from an electret microphone and amplifies it such that it can
drive a small loudspeaker. The amplifier is comprised of an AC-coupled
non-inverting operational amplifier with a voltage gain of eleven, with an
inside-the-loop emitter-follower on its output with AC-coupling to the
loudspeaker. The op-amp section provides voltage gain, and the emitter-follower
functions as a buffer, providing the current required to drive the loudspeaker.
Placing the emitter-follower inside the feedback loop improves its overall
performance.

Objective
---------

To investigate negative feedback amplifiers and Class A amplifiers by building
an audio amplifier. To show how to bias analog circuits for use on
single-voltage power supplies. To show that a positive feedback loop can occur
in an audio amplifier with a microphone on its input and loudspeaker on its
output if the microphone is placed too close to the loudspeaker. Following
completion of this lab you should be able to describe the basic operation of an
electret microphone, explain one way to bias op-amp-based circuits for
single-supply operation, describe amplifier clipping, and be able determine the
DC- and AC-gains of a non-inverting operational amplifier circuit.

Materials and Apparatus
-----------------------

-  Data sheet handouts for OP484, electret microphone, and 2N3904
-  Audio Amplifier Experiment article handout (linked below in the "Theory" section to a wiki version)
-  IC pinout handout
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) OP484 from the ADALP2000 Analog Parts Kit
-  (1) Electret microphone from the ADALP2000 Analog Parts Kit
-  (1) 2N3904 NPN transistor from the ADALP2000 Analog Parts Kit
-  (1) 8 Ω loudspeaker from the ADALP2000 Analog Parts Kit
-  (1) 47 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 68 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 1 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 2.2 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (2) 20 KΩ resistors from the ADALP2000 Analog Parts Kit
-  (1) 4.7 μF capacitor from the ADALP2000 Analog Parts Kit
-  (2) 47 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) 220 μF capacitor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard; note that the
   +5 V power is to be supplied by the M1K

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4_image_1.png
   :alt: lab_4_image_1.png
   :align: center
   :width: 700

-  Refer to the illustration below for one way to install the components in the
   solderless breadboard; note that the top rows are reserved for 5.0 V and GND
   connections

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4_assembly_image_1.png
   :alt: lab_4_assembly_image_1.png
   :align: center
   :width: 800

-  Refer to the included section below for details regarding the microphone pin
   assignments

Activity S1: Electret microphone preamplifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objective:
==========

The objective of this Lab activity is to explore the electret microphone bias
techniques and a two stage preamplifier circuit.

Notes:
======

As in all the ALM labs we use the following terminology when referring to the
connections to the M1000 connector and configuring the hardware. The green
shaded rectangles indicate connections to the M1000 analog I/O connector. The
analog I/O channel pins are referred to as CA and CB. When configured to force
voltage / measure current -V is added as in CA-V or when configured to force
current / measure voltage -I is added as in CA-I. When a channel is configured
in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as
CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
===========

Electret is a quasi-permanently charged dielectric. It is made by heating a
ceramic material, placing it in a magnetic field then allowing it to cool while
still in the magnetic field. It is the electrostatic equivalent of a permanent
magnet. In an electret microphone a slice of this material is used as a part of
the dielectric of a capacitor in which the diaphragm of the microphone forms one
plate. Sound pressure moves the diaphragm. The movement of the plate varies the
capacitance according to the sound pressure. Given the built-in fixed charge of
the dielectric, the voltage across the capacitor will also vary. The electret
capacitor is connected to the input of a built in FET amplifier. Electret
microphones are small, have excellent sensitivity, a wide frequency response and
generally a very low cost.

The terminals:
--------------

The terminal with a solder mark (connecting to the case) is negative and the
terminal without a mark is positive as shown for a typical microphone in figure
1. Case styles and terminal markings may vary from manufacturer to manufacturer.
Double check the polarity of your microphone before connecting it to your
circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-s1_f1.png
   :align: center
   :width: 300

.. container:: centeralign

   Figure 1 Electret Microphone terminals

Materials:
----------

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
-----------

Build the microphone bias and preamplifier circuit shown in figure 2 on your
solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-s1_f2.png
   :align: center
   :width: 600

.. container:: centeralign

   Figure 2 Electret microphone pre-amplifier

Hardware Setup:
---------------

To produce a sound to pick up with the microphone, a good choice is a small 8 Ω
audio speaker connected to the channel A voltage generator output CA-V as shown
in figure 2. A mechanical or piezo electric buzzer or transducer could work to
produce a sound as well. Set the channel A to produce a 1000 Hz sinewave with a
1.0 V Min value and 4.0 V Max value. Position the speaker near to and directly
facing the microphone. Scope channel B is set up in the Hi-Z mode and set to 0.2
V/div centered on DC value seen at the output which should be near 2.5 V.

Procedure:
----------

Change the frequency of the CA-V generator and observe amplitude response of the
combined speaker and microphone.

Measure the amplitude of the signal seen at the base of Q\ :sub:`1` and calculate the gain of the preamplifier.

Questions:
----------

Change the relative distance between the speaker and microphone an observe the
amplitude response. Make special note of the relative phase of the output sine
wave with respect to the channel A signal driving the speaker. How does this
phase change with frequency and distance?

**For Further Reading:**

| `Electret <https://en.wikipedia.org/wiki/Electret>`_
| `Electret microphone <https://en.wikipedia.org/wiki/Electret_microphone>`_

**Return to ALM Lab Activity\**\ :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`**.**

-  Refer to the illustration below that shows how to connect the components

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4_assembly_image_2.png
   :alt: lab_4_assembly_image_2.png
   :align: center
   :width: 1200

-  See the illustration below that shows how to connect an extension cable to
   the loudspeaker

.. image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_4_assembly_image_3.png
   :alt: lab_4_assembly_image_3.png
   :align: center
   :width: 600

-  Run PixelPulse on the computer and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Connect the M1K +5V power supply to the circuit as indicated in the schematic
-  Verify that sound waves input to the microphone are reproduced by the loudspeaker
-  Set up PixelPulse to measure voltage on Channel A
-  Connect the emitter of the 2N3904 transistor to Channel A of the M1K using a wire from the kit and observe the waveform that corresponds to the loudspeaker output on PixelPulse; explain why the voltage is monitored at the transistor emitter rather than directly across the loudspeaker
-  Set up PixelPulse to source voltage/measure current on Channel B
-  Remove the microphone and R\ :sub:`D` and connect Channel B of the M1K in place of the microphone using a wire from the kit
-  Set up the sine wave sourced from Channel B to swing between 1.0000 V and 1.0400 V using PixelPulse
-  Observe the amplifier output on Channel A using PixelPulse and verify that the amplifier has an AC voltage gain of eleven
-  Slowly increase the high level of the sine wave sourced by Channel B using PixelPulse while observing the amplifier output on Channel A
-  Continue to increase the voltage of the sine wave sourced from Channel B until clipping is observed on the waveform measured on Channel A
-  Explain the reason for the clipping
-  Connect the microphone to two long wires and place it back in the circuit along with R\ :sub:`D` according to the schematic
-  Move the microphone directly in front of the loudspeaker until audible feedback occurs
-  Explain why this feedback occurs

Theory
------

A detailed description of the design and analysis of the audio amplifier is
provided in the Audio Amplifier Experiment article handout. Please refer to the
handout for the details of the amplifier theory, available at the link below

:doc:`theory </wiki-migration/university/courses/engineering_discovery/lab_4/theory>`

Observations and Conclusions
----------------------------

-  An op-amp can be used to amplify the voltage of audio signals and a transistor emitter-follower circuit can be placed following the op-amp to provide current drive to a loudspeaker
-  The emitter-follower circuit can be placed inside the op-amp negative feedback loop
-  Applying an input signal that is too large can cause clipping of the amplifier output signal
-  Positive feedback can occur in an audio amplifier with a microphone input and
   loudspeaker output if the microphone is placed too close to the loudspeaker

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`
