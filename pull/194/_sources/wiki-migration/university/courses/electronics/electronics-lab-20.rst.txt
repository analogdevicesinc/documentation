Activity: CMOS Amplifier stages - ADALM2000
===========================================

Objective:
----------

The goal is to explore a high gain inverting amplifier constructed from complementary MOS devices.

High gain inverting amplifier
=============================

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 3 - 100 KΩ Resistor
| 1 - 10 KΩ Resistor
| 1 - 4.7 KΩ Resistor
| 2 - 22 uF capacitor
| 2 - 1 uF capacitor
| 1 - 10 pF capacitor
| 1 - CD4069A, CD4069UB or 74HCU04 unbuffered hex inverter (be sure not to use the buffered 74HC04 version)
| Alternatively a simple CMOS inverter can be built using the CD4007 transistor array. Note the appendix at the end.

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

First build the simple example shown figure 2 to test the input to output transfer function of the simple CMOS amplifier. The green boxes indicate connections to the connector on ADALM2000. Connect Vp (+5V) power to V\ :sub:`CC` (pin 14) and ground to GND (pin 7). Connect the output of the waveform generator to one of the inverter inputs (pin 1) along with scope input 1+ and connect the inverter output (pin 2) to scope input 2+. If you are using the CD4069A(UB) you can connect pin 7, V\ :sub:`SS` to the negative board supply, Vn, rather than ground because the CD4069A(UB) supports power supply voltages greater than +5 volts.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 amplifier transfer function


.. image:: https://wiki.analog.com/_media/university/courses/electronics/74hc04.png
   :align: center
   :width: 200px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/cd4069a.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 3 74HCU04 and CD4069A share the same package pinouts


Hardware Setup:
---------------

Configure the waveform generator for a 1 KHz triangle wave with 4V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div. If you are using the CD4069A on the plus and minus power supplies you will need to use a larger 8V amplitude peak-to-peak and 0V offset.


|image1|

.. container:: centeralign

   Figure 4 Hardware setup using CD4007


Procedure:
----------

Measure the slope of the output and calculate the DC gain of the amplifier as the ratio of the change in the output voltage to the change in input voltage at the center of the output swing (i.e. around 2.5V). Remember this should be a negative number because the amplifier inverts.


|image2|

.. container:: centeralign

   Figure 5 CMOS inverting amplifier Scopy plot


Adding negative feedback
========================

On your solder-less breadboard construct the amplifier circuit shown in figure 6 below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 single stage amplifier


.. _hardware-setup-1:

Hardware Setup:
---------------

Configure the waveform generator for a 1 KHz sine wave with 2V amplitude peak-to-peak and 0V offset. Both scope channels should be set to 1V/Div.


|image3|

.. container:: centeralign

   Figure 7 Hardware setup for single stage amplifier using CD4007


.. _procedure-1:

Procedure:
----------

Apply a sinusoidal signal of 2V amplitude peak-to-peak with zero offset voltage to the input and measure the gain of the entire system from 10 to 100 KHz. Use the Network (Bode) analyzer to plot gain and phase vs. frequency for the entire system.

Figure 8 Plot for single stage amplifier using CD4007 </WRAP>

Questions:
----------

What is the DC voltage seen at the input and output of the inverter? What sets this DC level?

What is the gain from the input source, W1, to the output seen at the inverter output? Which components set this gain and why?

Adding more stages for higher gain
==================================

On your solder-less breadboard construct the amplifier circuit shown in figure 8 below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8 three stage amplifier


.. _hardware-setup-2:

Hardware Setup:
---------------

Configure the waveform generator for a 1 KHz sine wave with 2V amplitude peak-to-peak and 0V offset. Both scope channels should be set to 1V/Div.


|image4|

.. container:: centeralign

   Figure 9 three stage amplifier hardware setup using CD4007


.. _procedure-2:

Procedure:
----------

Apply a sinusoidal signal of 2V amplitude peak-to-peak with zero offset voltage to the input and measure the gain of the entire system from 10 to 100 KHz. Use the Network (Bode) analyzer to plot gain and phase vs. frequency for the entire system.

.. container:: centeralign

   Figure 10. Plot for three stage amplifier hardware setup using CD4007


.. _questions-1:

Questions:
----------

Chopper Amplifier
=================

In this part of the lab activity, the CD4069A(UB) un-buffered hex CMOS inverter and a CD4066 Quad analog switch are used as elements of a chopper amplifier. Reconnect the breadboard as indicated in figure 11. Referring to figure 11, the various functions of this circuit can be determined. The two inverters on the bottom left of figure 11 create a square wave and its complement to drive the switch controls of the CD4066. These square waves drive the switches, with switches A and B functioning as a single-pole, double-throw switch on the input, and switches C and D performing the same function on the output. The other inverter at the top of figure 6 is used as an AC coupled Amplifier similar to what we just looked at in figure 6.

In operation, the input signal is modulated by the input switches, amplified by the ac amplifier, and then demodulated by the output switches. The 20 kΩ, 560 pF low pass filter minimizes the high frequency ripple in the output.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f6.png
   :align: center
   :width: 530px

.. container:: centeralign

   Figure 11 Chopper amplifier


AC Amplifier Response to Pulse Modulated Signals
------------------------------------------------

Connect scope channel 2+ to the output of the AC amplifier stage at pin 12 of the CD4069A(UB). Display the input at W1 (with scope channel 1+) and output the AC Amplifier on the scope. Save the scope waveforms for DC inputs (W1) for each value from +0.5V, +0.2V, -0.2V and -0.5V.

Chopper Amplifier DC Transfer Characteristic
--------------------------------------------

Measure the transfer characteristic (DC gain) of the chopper amplifier by applying DC voltages between about -2 V and +2 V to the input and measuring the output. This can be done manually using waveform generator W1 with a DC wave shape and setting the offset. Be sure to take sufficient data to determine the linear and nonlinear ranges of the transfer characteristic. To reduce data taking time, try using the waveform generator to provide a very low frequency (100 Hz) triangle signal with 0V offset. For example, a 4V amplitude peak-to-peak setting will give outputs between +2V and -2V, respectively.

Chopper Amplifier Frequency Response
------------------------------------

Apply a sinusoidal signal of 400mV amplitude peak-to-peak with zero offset voltage to the input and measure the gain of the entire system from 10 to 100 KHz. Use the Network (Bode) analyzer to plot gain and phase vs. frequency for the entire system, paying special attention to the 50KHz to 100KHz range and the region near the frequency of the chopping clock.

Chopper Amplifier Results
-------------------------

Present the waveforms taken for the AC Amplifier in response to DC inputs. Discuss and explain the salient features of this response.

Plot or present the DC transfer characteristic of the chopper amplifier. Discuss and explain the salient features of this characteristic. Was the output of the chopper amplifier what you expected?

Make a Bode plot (gain/phase versus frequency) of the Chopper Amplifier from the data taken above. Comment on the bandwidth of the chopper amplifier and the gain near the chopping frequency.

For Further Study:
------------------

ADI Mini Tutorial on :adi:`Chopper Amplifiers <static/imported-files/tutorials/MT-055.pdf>`

Circuit Additions:
------------------

What sort of circuit could you make to generate the 100 KHz square wave other than using the waveform generator output on the Analog Discovery Lab board? There are three additional inverters in the 74HCU04, CD4069 package. The other inverters along with RC delay network, R\ :sub:`4` C\ :sub:`4` can be configured into a ring oscillator as shown below. The values for R\ :sub:`4` and C\ :sub:`4` are approximate for 100 KHz and can be adjusted up or down as needed.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f7.png
   :align: center
   :width: 500px

.. _questions-2:

Questions:
----------

What other types of oscillator circuits might be used to generate the 100 KHz square wave?

Add more questions here:

Appendix: Making an inverter with the CD4007 transistor array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/cd4007.png
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

These three inverters can be used to construct the three stage amplifier in section 20.3 for example.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/cmos_amplifier_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/cmos_amplifier_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/cmos_amplifier_hardware_setup_1.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/cmos_amplifier_scope_shot_1.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/cmos_amplifier_hardware_setup_2a.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/cmos_amplifier_hardware_setup_3a.png
