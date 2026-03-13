Activity: Making a full Operational Amplifier from previous blocks - ADALM2000
==============================================================================

High gain amplifier
===================

Objective:
----------

By combining the circuit blocks already explored, the goal is to build a
complete high open loop gain amplifier from a few discrete devices.

Materials:
----------

ADALM2000 Active Learning Module Solder-less breadboard Jumper wires 1 - 8.2KΩ
Resistor (close approx. can be made by connecting your 1.5KΩ and 6.8KΩ in
series) 1 - 47KΩ Resistor 1 - 100KΩ Resistor 2 - 470KΩ Resistor 1 - 10KΩ
Resistor 1 - 1KΩ Resistor 2 - 22uF capacitor 1 - 1uF capacitor 1 - 47nF
capacitor 1 - Small signal PNP transistors (2N3906) 3 - Small signal NPN
transistors (2N3904 SSM2212)

Directions:
-----------

On your solder-less breadboard construct the amplifier circuit shown in figure 1
below. The breadboard connections are shown in figure 2. The green boxes
indicate connections to the connector on ADALM2000.

|image1|

.. container:: centeralign

   Figure 1 Three stage amplifier

Hardware Setup:
---------------

Connect your circuit to the ADALM2000 I/O connector as indicated by the green boxes. It is best to ground the unused negative scope inputs when not being used. If the SSM2212 NPN matched pair is used then it is best to use it for Q\ :sub:`1` and Q\ :sub:`2`.

|image2|

.. container:: centeralign

   Figure 2 Three stage amplifier Breadboard Circuit

Procedure:
----------

Configure waveform generator for a 1 KHz sine wave with an amplitude of 400 mV peak-to-peak and zero offset. Using scope channel 1 to observe the input at W1 and scope channel 2 to observe the output of the amplifier at R\ :sub:`L`, record the input to output amplitude and phase relationship.

|image3|

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

Objective:
----------

By combining some of the circuit blocks already explored, the goal is to build a
complete unity gain buffer amplifier. The addition of the current mirror load
for the differential stage is a key improvement to this simple amplifier.

Materials:
----------

ADALM2000 Active Learning Module Solder-less breadboard Jumper wires 1 - 15KΩ Resistor (a 10KΩ in series with a 4.7KΩ can be substituted) 2 - Small signal PNP transistors (2N3906, or SSM2220 PNP match pair can be used) 6 - Small signal NPN transistors (2N3904, use SSM2212 NPN matched pair for Q\ :sub:`1` and Q\ :sub:`2` A TIP31C may be substituted for Q\ :sub:`5` if you don't have enough 2N3904 devices)

Directions:
-----------

Construct the circuit shown in figure 4 on your solder-less breadboard. The
breadboard connections are shown in figure 5.

|image4|

.. container:: centeralign

   Figure 4 Amplifier with unity gain

Hardware Setup:
---------------

Connect your circuit to the ADALM2000 I/O connector as indicated by the green
boxes. It is best to ground the unused negative scope inputs when not being
used.

|image5|

.. container:: centeralign

   Figure 5 Amplifier with unity gain Breadboard Circuit

Procedure:
----------

Configure AWG1 for a 1 KHz sine wave with an amplitude of 2 V peak-to-peak and
zero offset. Using scope channel 1 to observe the input at W1 and scope channel
2 to observe the output of the amplifier, record the input to output amplitude
and phase relationship.

|image6|

.. container:: centeralign

   Figure 6 Amplifier with unity gain Waveforms

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

PC board design files for this experiment, and other related extensions, can be
found on the ADI GitHub education tool repository. The PCB schematic is shown in
figure 3 and a photo of the board is shown in figure 4. Component placement is
shown in figure 5.

Power and bias rail decoupling capacitors C2, C3 and C4 are optional. Pin
sockets are best used for Frequency compensation capacitor C1 to allow for
experimenting with different values.

Resistor R4 sets the bias current for the first and second stages based on the
power supply voltage. The value can be adjusted based on the range of supply
voltages the amplifier will be operating. For +5 operation 1.5kΩ is a good
working value. For 10 V (+/- 5V) a 3.3kΩ is a good working value.

Resistors R5 and R6 set the steady state bias current in the output stage. Using
2N3904 and 2N3906 in the output stage, R5 = 6.8kΩ and R6 = 10kΩ is a good safe
starting point.

Output emitter resistors R7 and R8 can be any small value in the range of 2.7 to
10 ohms.

`Experiment board design files <https://github.com/analogdevicesinc/education_tools/tree/m1k-accessory-boards/experiment-boards>`_

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-13-f2.png
   :align: center
   :width: 600

.. container:: centeralign

   Figure 3, Operational Amplifier PCB schematic.

The PC Board version with the standard 8 pin DIP single op-amp footprint is
shown in figure 4. A version with all the pins in a single row (SIP) footprint
is shown in figure 5. Either version can be inserted into a solder-less
breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/trabsistor-op-amp-pcb.png
   :align: center
   :width: 500

.. container:: centeralign

   Figure 4, Example constructed Operational Amplifier PC Board, DIP version.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/transistor-op-amp-pcb2.png
   :align: center
   :width: 500

.. container:: centeralign

   Figure 5, Example constructed Operational Amplifier PC Board, SIP version.

To make it somewhat easier to install the components, figure 6 for the DIP
version and figure 7 for the SIP version are provided.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/transistor-op-amp-placement.png
   :align: center
   :width: 600

.. container:: centeralign

   Figure 6, DIP PC Board component placement.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/transistor-op-amp-placement2.png
   :align: center
   :width: 600

.. container:: centeralign

   Figure 7, SIP PC Board component placement.

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_f1.png
   :width: 550
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_amp.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_wf_amp.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_f2.png
   :width: 550
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_ug.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/a13_wf_ug.png
