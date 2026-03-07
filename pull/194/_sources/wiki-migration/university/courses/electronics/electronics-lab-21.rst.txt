Activity: CMOS LC Oscillator
============================

Objective:
----------

The goal is to explore the use of the high gain inverting CMOS amplifier in a LC oscillator.

High gain inverting amplifier
=============================

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 0.1 uF capacitor (104)
| 1 - 47 Ω resistor
| 1 - 1 mH inductor
| 1 - CD4069A, CD4069UB or 74HCU04 unbuffered hex inverter (be sure not to use the buffered 74HC04 version) Alternatively three simple CMOS inverters can be built using the CD4007 transistor array. Note the appendix at the end.

Background:
-----------

A CMOS inverter can also be viewed as a high gain amplifier. It consists of one PMOS device, M\ :sub:`1` and one NMOS device M\ :sub:`2`. Generally the CMOS fabrication process is designed such that the threshold voltage, V\ :sub:`TH`, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance is also equal.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 CMOS Inverting amplifier


Directions:
-----------

First build the simple example shown figure 2 to test the input to output transfer function of the simple CMOS amplifier. The green boxes indicate connections to the connector on The ADALM2000. Connect Vp (+5V) power to V\ :sub:`CC` (pin 14) and ground to GND (pin 7). Connect the output of the waveform generator to one of the inverter inputs (pin 1) along with scope input 1+ and connect the inverter output (pin 2) to scope input 2+.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 amplifier transfer function


.. image:: https://wiki.analog.com/_media/university/courses/electronics/74hc04.png
   :align: center
   :width: 150px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/cd4069a.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 3 74HCU04 and CD4069A(UB) share the same package pinouts


Hardware Setup:
---------------

Configure the waveform generator for a 1 KHz triangle wave with 4V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div.

Procedure:
----------

Measure the slope of the output and calculate the DC gain of the amplifier as the ratio of the change in the output voltage to the change in input voltage at the center of the output swing (i.e. around 2.5V). Remember this should be a negative number because the amplifier inverts.

Adding LC resonator
===================

On your solder-less breadboard construct the filter network shown in figure 4 below. Using the Network (Bode) analyzer tool measure the gain and phase response of the LC network.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a21_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 LC filter network


.. _hardware-setup-1:

Hardware Setup:
---------------

Configure the Network (Bode) analyzer for 2 log decades, end frequency of 100 KHz, a max gain of 2X, run time of 10 sec, offset of 0 V and an amplitude of 2 V peak-to-peak. Run a single sweep and save the data to a file.

Question:
---------

Write down the equation for the cut-off frequency of the pi LC lowpass filter section used in figure 4 and calculate F\ :sub:`C`. How does this answer compare to what you measured?

Based on the frequency response of the LC network, at what frequency do you think the circuit will oscillate?

Placing LC network in feedback of amplifier
===========================================

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a21_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 LC oscillator


.. _hardware-setup-2:

Hardware Setup:
---------------

Be sure that pin 14 of the 74HCU04 (CD4069) is connected to Vp and Pin 7 is connected to ground. Turn on the power supplies. Both scope channels should be set to 1V/Div. and the time base to 20 uSec/Div.

.. _procedure-1:

Procedure:
----------

Compare the waveforms you observe at pin 1, pin 2, and pin 4 of the Hex inverter (74HCU04).

Questions:
----------

What are the criteria for a circuit to oscillate stably?

At what frequency does the circuit oscillate and how does this compare with your prediction from the frequency sweep of the LC filter back in step 2?

Appendix:
~~~~~~~~~

Making an inverter with the CD4007 transistor array. Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f8.png
   :align: center
   :width: 500px

The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Two of these inverters can be used to construct the LC oscillator in figure 5 for example.

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
