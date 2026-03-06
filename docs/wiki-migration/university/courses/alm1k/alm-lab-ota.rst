Activity: 2 Stage CMOS OTA - ADALM1000
======================================

Objective:
----------

The objective of this lab activity is to investigate and evaluate a two stage CMOS operational transconductance amplifier (OTA).

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   CD4007 functional diagram.


The CD4007 is a very versatile IC with many uses For example, a single CD4007 can be used to make complex logic functions such as Inverters, NAND and NOR gates. Analog functions such as analog switches and amplifiers can also be constructed from these transistors.

In this Lab Activity you will be using complementary NMOS and PMOS transistors to construct an operational transconductance amplifier (OTA). The OTA is an amplifier where the differential input voltage produces an output current. It can be modeled as a voltage controlled current source (VCCS). The OTA is similar to a standard operational amplifier in that it has a high impedance differential input stage and that it is most often used with negative feedback. The difference is the relatively high output impedance of the push-pull current source output stage rather than the much lower impedance push-pull emitter follower output stage used in Op-Amps.

Part 1:
-------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less Breadboard and jumper wire kit
| 1 CD4007 (CMOS array)
| 2 ZVN2110A NMOS transistors (or similar)
| 1 68 KΩ resistor
| 1 10 KΩ resistor
| 1 0.01 uF capacitor
| 3 2N3904 NPN transistors
| 1 2N3906 PNP transistor

Directions:
~~~~~~~~~~~

Construct the two stage CMOS OTA as shown in figure 1 on your solder-less breadboard. Transistors M1-M5 are contained in the CD4007 CMOS transistor array. The input differential pair M6 and M7 is composed of discrete ZVN2110A enhancement mode NMOS devices from the Analog Parts Kit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, 2 Stage CMOS OP-AMP


Feedback around the OTA is configured as an inverting gain amplifier ( 6.8 ) with the common mode level set at +2.5V, the middle of the +5 V power supply.

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator CA-V for a 200 Hz sine wave with 2.3 V Min value and 2.8 V Max value. Channel B is set in the Hi-Z mode. Both scope channels should be set to 0.5V/Div.

Procedure:
~~~~~~~~~~

On the output you should see an inverted version of the input with an approximately 6.8 times larger amplitude. Slowly increase the amplitude of the input sine wave until the output saturates ( clips ). Record the minimum and maximum output swing that can be achieved.

With the input amplitude set to slightly less than where the output saturates change the input waveform to a square wave. Measure the rise and fall times for the output waveform. Repeat the measurements with a second 0.01 uF capacitor in parallel with C\ :sub:`1`, doubling its value. Explain any differences you see.

Questions:
~~~~~~~~~~

What is the gain from the input source, CA-V, to the output CB-H seen at the OTA output? Which components set this gain and why? Probe the voltage at the gate of M6. What is the DC and AC values of the waveform?

.. _directions-1:

Directions:
~~~~~~~~~~~

Add the complementary NPN, PNP emitter follower output stage to the OTA circuit from figure 1 as shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Push-Pull output stage added


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator CA-V for a 200 Hz sine wave with 2.4 V Min value and 2.7 V Max value. Channel B is set in the Hi-Z mode. Both scope channels should be set to 0.5V/Div.

.. _procedure-1:

Procedure:
~~~~~~~~~~

On the output you should see the same inverted version of the input with an approximately 6.8 times larger amplitude as you got from the circuit in figure 1. Slowly increase the amplitude of the input sine wave until the output saturates ( clips ). Record the minimum and maximum output swing that can be achieved. Explain why it is different from what you measured for figure 1.

Again with the input amplitude set to slightly less than where the output saturates change the input waveform to a square wave. Measure the rise and fall times for the output waveform. Repeat the measurements with a second 0.01 uF capacitor in parallel with C\ :sub:`1`, doubling its value. Explain any differences you see.

.. _questions-1:

Questions:
~~~~~~~~~~

Insert additional questions here.

Alternate component choices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try replacing the NMOS input differential pair M6 and M7 with a pair of NPN, 2N3904, transistors.

Part 2:
-------

A second interesting OTA circuit, first published in 1991 in a brief paper [1] in the IEEE Journal of Solid State Circuits Journal of Solid State Circuits, is shown in the `LTspice simulation schematic <https://wiki.analog.com/_media/university/courses/alm1k/cmos_op-amp-cd4007-zvpn.zip>`__ in figure 4. Details of the operation of the complimentary differential to single ended input stage can best be understood by reading the above paper. As a short simplified description, consider the conventional CMOS differential amplifier configuration we explored in part 1, figure 2, which uses an NMOS differential pair and the complementary version that uses a PMOS differential pair. If the current mirror loads from both amplifiers are deleted, and the input pair drains of the NMOS amplifier are connected to the input pair drains of the PMOS amplifier we have the input stage of the amplifier in figure 4. To now bias the amplifier the gates of the NMOS and PMOS tail current sources need to be driven somehow. To do this, both of the tail current source gates are connected to the internal amplifier node Vbias. This self-biasing of the amplifier creates a negative-feedback loop that stabilizes the bias voltages such that the current in the P side and N side are always exactly equal to each other.

Simulation Directions:
~~~~~~~~~~~~~~~~~~~~~~

Simulate the time domain transient operation and AC frequency response of the circuit as shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f4.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 4, Simulation schematic.


The transient time domain simulation of the inverting configuration is shown in figure 4s. The output at node Vout is seen to swing nearly rail to rail. The internal Vbias node is also plotted.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f4s.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4s, Simulation Waveforms.


.. _materials-1:

Materials:
~~~~~~~~~~

| 1 CD4007 (CMOS array)
| 1 ZVN2110A NMOS transistor
| 1 ZVP2110A NMOS transistor
| 2 100 kΩ resistors
| 1 22 kΩ resistor
| 1 0.001 uF capacitor

Hardware Directions:
~~~~~~~~~~~~~~~~~~~~

Build the amplifier as shown in figure 5 on your solderless breadboard. The schematic indicates how to connect the pins on the CD4007 package. Compensation resistor R3 and capacitor C1 are potentially optional and can be used to adjust the frequency stability / response of the amplifier.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, CD4007 CMOS Op-amp Test Circuit.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Inverting Unity Gain output near rail-to-rail swing.


In figure 6b we probe the voltage of the bias node (with BIN as orange trace), at the gates of NMOS M6 and PMOS M5. Note that the bias voltage is constant because the non-inverting input (pin 3 of the CD4007) is connected to the fixed 2.5V rail in the inverting amplifier configuration. Compare the measured bias node voltage to your simulated result (from figure 4s).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f6b.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6b, Inverting Unity Gain, Bias node voltage.


Now explore the amplifier’s operation as a non-inverting follower with unity gain. Disconnect the channel A output, CH A, from the end of R1 and leave R1 floating. Disconnect the fixed +2.5 V supply from pin 3 of the CD4007 and connect the channel A output, CH A, to pin 3 of the CD4007. The amplifier should now be configured as a unity gain follower. Adjust the Min and Max values of AWG channel A until the output of the amplifier just starts to distort as shown in figure 7, green trace CH A and orange trace the amplifier output. In this example case, the output deviates from the input when the Min voltage was at 1.71 V and the Max voltage was at 3.84 V. Your results may vary. This now tells us the boundary of the usable input common mode range.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Non-Inverting Unity Gain output at extremes of the input common mode range.


In figure 8 we probe the voltage at the bias node (with BIN as orange trace), gates of NMOS M6 and PMOS M5. Note that the bias voltage is sort of an inverted version of the input common mode voltage until the limits are exceeded.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-ota-lab_f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Bias node at extremes of the input common mode range.


**For Further Reading:**

| [1] Bazes, Mel, "Two novel fully complementary self-biased CMOS differential amplifiers”, IEEE Journal of Solid State Circuits, 26.2 (1991): pg. 165-168.
| `Operational transconductance amplifier <https://en.wikipedia.org/wiki/Operational_transconductance_amplifier>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/electronics>`
