Activity: Making a full Operational Amplifier from previous blocks - ADALM2000
==============================================================================

High gain amplifier
===================

Objective:
----------

By combining the circuit blocks already explored, the goal is to build a complete high open loop gain amplifier from a few discrete devices.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 8.2KΩ Resistor (close approx. can be made by connecting your 1.5KΩ and 6.8KΩ in series)
| 1 - 47KΩ Resistor
| 1 - 100KΩ Resistor
| 2 - 470KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - 1KΩ Resistor
| 2 - 22uF capacitor
| 1 - 1uF capacitor
| 1 - 47nF capacitor
| 1 - Small signal PNP transistors (2N3906)
| 3 - Small signal NPN transistors (2N3904 SSM2212)

Directions:
-----------

On your solder-less breadboard construct the amplifier circuit shown in figure 1 below. The breadboard connections are shown in figure 2. The green boxes indicate connections to the connector on ADALM2000.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a13_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1 Three stage amplifier


Hardware Setup:
---------------

Connect your circuit to the ADALM2000 I/O connector as indicated by the green boxes. It is best to ground the unused negative scope inputs when not being used. If the SSM2212 NPN matched pair is used then it is best to use it for Q\ :sub:`1` and Q\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a13_amp.png
   :align: right

.. container:: centeralign

   Figure 2 Three stage amplifier Breadboard Circuit


Procedure:
----------

Configure waveform generator for a 1 KHz sine wave with an amplitude of 400 mV peak-to-peak and zero offset. Using scope channel 1 to observe the input at W1 and scope channel 2 to observe the output of the amplifier at R\ :sub:`L`, record the input to output amplitude and phase relationship.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a13_wf_amp.png
   :align: center

.. container:: centeralign

   Figure 3 Three stage amplifier Waveforms


Questions:
----------

What is the DC voltage seen at the base of Q\ :sub:`1`? What sets this DC level?

What is the gain from the input source, W1, to the output seen at R\ :sub:`L`? Which components set this gain and why?

Run a computer simulation of the amplifier and calculate the open loop gain as seen from the base of transistor Q\ :sub:`1` to the output at the collector of Q\ :sub:`4`. Report this gain vs. frequency.

Change the value of the load resistor R\ :sub:`L`. How does lowering the value of R\ :sub:`L` affect the open loop and closed loop gain and why?

Change the value of compensation capacitor C\ :sub:`3`. How does raising and lowering the value of C\ :sub:`3`\ affect the frequency response and why?

What happens if C\ :sub:`3` is completely removed and why?

What happens when C\ :sub:`2`\ is removed and why?

Unity gain amplifier
====================

.. _objective-1:

Objective:
----------

By combining some of the circuit blocks already explored, the goal is to build a complete unity gain buffer amplifier. The addition of the current mirror load for the differential stage is a key improvement to this simple amplifier.

.. _materials-1:

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 15KΩ Resistor (a 10KΩ in series with a 4.7KΩ can be substituted)
| 2 - Small signal PNP transistors (2N3906, or SSM2220 PNP match pair can be used)
| 6 - Small signal NPN transistors (2N3904, use SSM2212 NPN matched pair for Q\ :sub:`1` and Q\ :sub:`2` A TIP31C may be substituted for Q\ :sub:`5` if you don't have enough 2N3904 devices)

.. _directions-1:

Directions:
-----------

Construct the circuit shown in figure 4 on your solder-less breadboard. The breadboard connections are shown in figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a13_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4 Amplifier with unity gain


.. _hardware-setup-1:

Hardware Setup:
---------------

Connect your circuit to the ADALM2000 I/O connector as indicated by the green boxes. It is best to ground the unused negative scope inputs when not being used.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a13_ug.png
   :align: center

.. container:: centeralign

   Figure 5 Amplifier with unity gain Breadboard Circuit


.. _procedure-1:

Procedure:
----------

Configure AWG1 for a 1 KHz sine wave with an amplitude of 2 V peak-to-peak and zero offset. Using scope channel 1 to observe the input at W1 and scope channel 2 to observe the output of the amplifier, record the input to output amplitude and phase relationship.


|image1|

.. container:: centeralign

   Figure 6 Amplifier with unity gain Waveforms


.. _questions-1:

Questions:
----------

.. note::

   Add questions here:


Here is a good technical paper on how to make :adi:`Simple Op Amp Measurements <en/analog-dialogue/articles/simple-op-amp-measurements.html>`.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/full_op_amp_blocks_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/full_op_amp_blocks_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/electronics>`

Appendix: More advanced versions on a PC board
----------------------------------------------

.. include:: ../alm1k/alm-lab-13.rst

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_wf_ug.png
