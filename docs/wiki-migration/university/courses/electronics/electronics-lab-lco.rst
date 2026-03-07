Activity, Light Controlled RC Oscillator.
=========================================

Objective:
----------

The goal of this activity is to explore the use of the high gain inverting CMOS amplifier along with a light dependent resistor to construct an RC oscillator who's frequency is controlled by the amount of light falling on the photo resistor.

High gain inverting amplifier
-----------------------------

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 0.01 uF capacitor (103)
| 1 - 5-20 KΩ photo resistor (photocell)
| 1 - CD4007 simple CMOS inverters built using the transistor array (or CMOS hex inverter 74HC04)

Background:
~~~~~~~~~~~

The simple two transistor CMOS inverter can also be viewed as a high gain amplifier. It consists of one PMOS device, M\ :sub:`1` and one NMOS device M\ :sub:`2`. Generally the CMOS fabrication process is designed such that the magnitude of the threshold voltage, V\ :sub:`TH`, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance is also equal.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 CMOS Inverting amplifier


Below in figure 2 is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/alco_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 one CD4007 CMOS inverter


A second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input. A third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Directions:
~~~~~~~~~~~

First build the simple example shown in figure 4 to test the input to output transfer function of the CMOS amplifier. The green boxes indicate connections to the connector on the ADALM2000. Connect V+ (+5V) power to V\ :sub:`CC` (pin 14) and ground to GND (pin 7). Connect the output of the waveform generator to one of the inverter inputs (pin 6) along with scope input 1+ and connect the inverter output (pin 8,13) to scope input 2+.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/alco_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 amplifier transfer function


Hardware Setup:
~~~~~~~~~~~~~~~

Configure the waveform generator for a 1 KHz triangle wave with 5V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div.

Procedure:
~~~~~~~~~~

Measure the slope of the output and calculate the DC gain of the amplifier as the ratio of the change in the output voltage to the change in input voltage at the center of the output swing (i.e. around 2.5V). Remember this should be a negative number because the amplifier inverts.

Questions:
~~~~~~~~~~

What is the gain from the input source, W1, to the output seen at the inverter output? At what DC voltage at the input is the gain the highest?

Two stage astable multivibrator:
--------------------------------

.. _background-1:

Background:
~~~~~~~~~~~

There are basically two requirements to make an oscillator. The first is some sort of gain stage such as the CMOS inverter we just looked at and the second is some sort of frequency dependent or phase delay block like a RC time constant. Positive feedback around a cascade of two of these inverter stages such as was looked at in the :doc:`MOS Multivibrator Activity </wiki-migration/university/courses/electronics/electronics-lab-24m>` completes the oscillator.

To understand how the circuit shown in figure 5 oscillates we first assume that the output of the first inverter stage ( at pins 8 and 13 ) is high, near V\ :sub:`DD`. This means that the output of the second inverter stage ( at pin 12 ) is low, near V\ :sub:`SS`. The high voltage on pins 8,13 will begin charging capacitor C\ :sub:`1` through the photo resistor. The voltage on C\ :sub:`1` is also the input to the first inverter stage at pin 6. Eventually the voltage on C\ :sub:`1` becomes high enough to be above the threshold of the first inverter stage and the output will switch from the high voltage to a low voltage ( near V\ :sub:`SS` ). This also causes the output of the second inverter stage to switch from low to high. Now C\ :sub:`1` driven by the output of stage 2, discharges through the photo resistor. Again, eventually the voltage at C\ :sub:`1` and the photo resistor becomes low enough to switch stage 1 back to its original starting state completing one cycle and starting the next.

.. _directions-1:

Directions:
~~~~~~~~~~~

First, be sure the power supplies are switched off before modifying your circuit. Working from the single inverter you constructed in figure 4 add a second inverter stage along with capacitor C\ :sub:`1` and the photo resistor to build the oscillator as shown in figure 5. The waveform generator is no longer needed but keep scope channels 1 and 2 connected to the output of both inverter stages.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/alco_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 Light dependent oscillator


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Scope channels 1 and 2 should be set to 1v/div and the horizontal time base will need to be adjusted so that a few cycles of the oscillator output frequency are displayed. This will change based on the amount of light falling on the photocell.

Turn on the V+ positive 5 V power supply only after double checking you circuit connections.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Place a finger or something else over the photo resistor to block any light from falling on it. Note the frequency of the oscillator. Now move your finger slightly to allow some light from the room to fall on the photo resistor. Again note the frequency of the oscillator. The more light falling on the photo resistor reduces its resistance and should noticeably increase the frequency of the oscillation.

.. _questions-1:

Questions:
~~~~~~~~~~

What is the lowest ( full darkness ) and highest ( bright light ) frequency that the circuit will oscillate at? Try substituting other higher and lower value capacitors for C\ :sub:`1` and again determine the range of frequencies from full darkness to bright light.

Try substituting a 50 KΩ potentiometer for the photo resistor. Adjust the pot from maximum to minimum resistance and record the lowest and highest frequency you are able to get. How do these values compare to those you were able to get with the photo resistor?

For Further Reading:
~~~~~~~~~~~~~~~~~~~~

| http://en.wikipedia.org/wiki/Photoresistor
| http://en.wikipedia.org/wiki/Multivibrator

Additional Activity:
~~~~~~~~~~~~~~~~~~~~

Could you modify this circuit to make the frequency of the oscillator temperature dependent by substituting the photo resistor with the thermistor from the ADALP2000 Analog Parts Kit?

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
