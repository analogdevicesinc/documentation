Activity: CMOS LC Oscillator - ADALM1000
========================================

Objective:
----------

The goal is to explore the use of the high gain inverting CMOS amplifier in a LC oscillator.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

21.1 High gain inverting amplifier
----------------------------------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 2 - 1uF capacitor
| 1 - 68 Ω resistor
| 2 - 10 mH inductors
| 1 - CD4069A, CD4069UB or 74HCU04 unbuffered hex inverter (be sure not to use the buffered 74HC04 version) Alternatively three simple CMOS inverters can be built using the CD4007 transistor array. Note the appendix at the end.

Background:
~~~~~~~~~~~

A CMOS inverter can also be viewed as a high gain amplifier. It consists of one PMOS device, M\ :sub:`1` and one NMOS device M\ :sub:`2`. Generally the CMOS fabrication process is designed such that the threshold voltage, V\ :sub:`TH`, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance is also equal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 CMOS Inverting amplifier


Directions:
~~~~~~~~~~~

First build the simple example shown figure 2 to test the input to output transfer function of the simple CMOS amplifier. The green boxes indicate connections to the connector on ALM1000. Connect +5V power to V\ :sub:`CC` (pin 14) and ground to GND (pin 7). Connect the output of the channel A voltage generator, CA-V to one of the inverter inputs (pin 1) and connect the inverter output (pin 2) to the channel B Hi-Z scope input CB-H.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 amplifier transfer function


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 74HCU04 and CD4069A(UB) share the same package pinouts


Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A voltage generator CA-V for a 200 Hz triangle wave with 0 V Min value and 5V Max value. Both scope channels should be set to 0.5V/Div.

Procedure:
~~~~~~~~~~

Measure the DC input offset where the gain in the highest. Measure the slope of the output and calculate the DC gain of the amplifier as the ratio of the change in the output voltage to the change in input voltage at the center of the output swing (i.e. approx. around 2.5V). Remember the answer should be a negative number because the amplifier inverts.

21.2 Adding LC resonator
------------------------

On your solder-less breadboard construct the filter network shown in figure 4 below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab21_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 LC filter network


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator, CA-V, should be set as a sine wave with a 0.5 V Min value and a 4.5 V Max value. Channel B is set in the Hi-Z mode.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Use the equation for the cut-off frequency of the pi LC lowpass filter section used in figure 4 and calculate F\ :sub:`C`.

There is a variety of different pi section filter variants that can be used dependent upon the required band ripple, rate of roll off, etc. The equation below is for the case where C\ :sub:`1` = C\ :sub:`2`:

:math:`F_C = 1 / (\pi \times sqrt(L \times C))`

| Where:
| C = C\ :sub:`1` + C\ :sub:`2` the total capacitance in Farads
| L = Inductance of L\ :sub:`1` in Henries
| Fc = Cutoff frequency in Hertz

Measure the gain and phase response of the LC network at frequencies of one half F\ :sub:`C`, F\ :sub:`C` and twice F\ :sub:`C`.

Questions:
~~~~~~~~~~

How does the calculated F\ :sub:`C` compare to what you measured? Based on the frequency response of the LC network, at what frequency do you think the circuit will oscillate?

Using your second 10 mH inductor place it in series with the first 10 mH inductor to make the total inductance 20 mH and repeat your calculations and measurements.

Now place the two inductors in parallel for a total inductance of 5 mH. Again repeating your calculations and measurements. Record all your results for all three inductance values.

21.3 Placing LC network in feedback of amplifier
------------------------------------------------

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab21_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 LC oscillator


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

Be sure that pin 14 of the 74HCU04 (CD4069) is connected to +5 V and Pin 7 is connected to ground. Both scope channels should in the HI-Z mode and be set to 0.5V/Div, and the time base to 0.2 mSec/Div.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Compare amplitudes and phases the waveforms you observe at pin 1, pin 2, and pin 4 of the Hex inverter (74HCU04). Measure the period and frequency of the oscillation. Using your second 10 mH inductor place it in series with the first 10 mH inductor to make the total inductance 20 mH. Measure the period and frequency of the oscillation with this higher inductance value. Now place the two inductors in parallel for a total inductance of 5 mH. Again measure the period and frequency of the oscillation with this lower inductance value.

.. _questions-1:

Questions:
~~~~~~~~~~

What are the criteria for a circuit to oscillate stably?

At what frequency does the circuit oscillate and how does this compare with your prediction from the frequency sweep of the LC filter back in step 2? Does doubling the inductance to 20 mH and reducing it by half to 5 mH result in the correct oscillation frequency based on calculations?

Appendix: Making an inverter with the CD4007 transistor array
-------------------------------------------------------------

Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 300px

.. container:: centeralign

   CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f6.png
   :align: center
   :width: 500px

The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Two of these inverters can be used to construct the LC oscillator in figure 5 for example.

**For Further Reading:**

http://en.wikipedia.org/wiki/LC_circuit

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
