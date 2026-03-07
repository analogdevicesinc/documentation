Activity: DC-DC Converters II - ADALM2000
=========================================

Objective:
----------

The object of this activity is to explore a capacitor based circuit which can produce an output voltage which is higher than the supplied voltage. This class of circuits are referred to as DC to DC converters or boost regulators.

Concept:
--------

The basic concept of capacitor based DC to DC converter is shown below in figure 1. These are often referred to as "flying capacitor" or "charge-pump" voltage converters. The operation alternates between the two configurations shown in figure 1. On the left, switches S\ :sub:`1` and S\ :sub:`5` are closed connecting C\ :sub:`1` between ground and V\ :sub:`IN`. On the right, switches S\ :sub:`4` and S\ :sub:`8` are closed connecting C\ :sub:`2` between V\ :sub:`IN` and V\ :sub:`OUT`. For the half cycle shown capacitor C\ :sub:`1` is charged to the voltage at V\ :sub:`IN` and V\ :sub:`OUT` is the sum of the voltage at V\ :sub:`IN` and the voltage on capacitor C\ :sub:`2`. For the second half cycle the switches are reversed. Now with S\ :sub:`2` and S\ :sub:`6` closed C\ :sub:`1` is connected between V\ :sub:`IN` and V\ :sub:`OUT`. Also switches S\ :sub:`3` and S\ :sub:`7` will now be closed connecting C\ :sub:`2` between ground and V\ :sub:`IN`. So now we can see that after a few cycles V\ :sub:`OUT`, the voltage across capacitor C\ :sub:`3` will be equal to twice V\ :sub:`IN`. As you can see the capacitors "fly" back and forth between V\ :sub:`IN` and V\ :sub:`OUT`, thus the name "flying capacitor". One can also see that what is in effect happening is the charge on capacitors C\ :sub:`1` and C\ :sub:`2` is alternately transferred or pumped onto capacitor C\ :sub:`3` charging it up to two times V\ :sub:`IN`. This action gives rise to the second "charge pump" name.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a16_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Capacitor based voltage doubler


We will now replace the ideal switches in the diagram with actual electronic switches. There are a number of possible devices that could be used but the MOS FET transistor is most often used. The next diagram shows a direct substitution of NMOS ( S\ :sub:`1`,S\ :sub:`3`,S\ :sub:`5`,S\ :sub:`7` ) and PMOS ( S\ :sub:`2`,S\ :sub:`4`,S\ :sub:`6`,S\ :sub:`8` ) devices for the switches in the first diagram. It can be noted that switches S\ :sub:`1` and S\ :sub:`2` form a complementary pair and take the same form as a CMOS inverter logic gate. The other three sets of switches form similar complementary pairs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a16_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 CMOS voltage doubler


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - ZVN2110A NMOS FET (2N7000)
| 2 - 74HC04 HEX CMOS Inverters (CD4007, CD4069)
| 2 - 10 uF capacitors
| 1 - 220 uF capacitor
| 2 - 1N914 small signal diodes

Additional Equipment:
---------------------

| Small handheld DMM
| +5 V bench power supply

Directions:
-----------

The breadboard connections for the first version are as shown in figure 3 below. The DMM should be connected to measure the voltage at V\ :sub:`OUT`. The +5V bench power supply should be connected to the Vin node. The digital pulse output drives the input of the first Inverter gate at pin 1. Scope input 1+ (single ended) is connected to the drain terminal of M\ :sub:`1` and scope input 2+ (single ended) is connected to the drain terminal of M\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a16_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 NMOS and Diode DC-DC converter


Hardware Setup:
---------------

The digital pulse source output should be configured for a 50% duty cycle and 20 KHz output frequency. The Single ended input of scope channel 1 (1+) is used to measure the waveform seen at the drain of M\ :sub:`1` and scope channel 2 (2+) is used to measure the waveform seen at the drain of M\ :sub:`2`.

Procedure:
----------

Be sure to start up the digital pulse source output on the ADALM2000 Lab board before turning on the +5V bench supply. The boosted output voltage at node V\ :sub:`OUT` should be observed and should be approximately equal to 2 times the DC value of the bench supply.

Questions:
----------

| What is the voltage on V\ :sub:`OUT`? Why is it not exactly 2 times V\ :sub:`IN`?
| What is the effect of changing the frequency of the digital pulse output?
| Is there a minimum or maximum frequency?
| How much current can the circuit supply to a load? Try various resistors as a load.
| Is that current affected by the frequency of the digital pulse output?
| Calculate the conversion efficiency of the circuit. Ratio of output power (I\ :sub:`OUT`\ \*V\ :sub:`OUT`) to input power (I\ :sub:`IN`\ \* 5V)
| Change the value of C\ :sub:`1` and C\ :sub:`2` and redo the above. How have the results changed?
| Connect the other inverters in the 74HC04 package in parallel with INV1 and INV2 in the diagram. What effect do these added drivers have on the results?

.. _directions-1:

Directions:
-----------

The breadboard connections for another version are as shown in figure 4 below. A second package of CMOS inverters is used for the upper set of switches (INV3 and INV4) rather than the discrete FETs and diodes. The ground connection of the second 74HC04 is connected to the V\ :sub:`IN` node and the supply connection at pin 14 becomes the V\ :sub:`OUT` node. The DMM should be connected to measure the voltage at V\ :sub:`OUT`. The +5V bench power supply should be connected to the V\ :sub:`IN` node. The digital pulse source output drives the input of the first Inverter gate at pin 1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a16_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 All CMOS Inverter configuration


Figure 5 shows a configuration that produces V\ :sub:`OUT` equal to -V\ :sub:`IN`. The second 74HC04 is connected below ground as shown to produce a V\ :sub:`OUT` that is equal to -V\ :sub:`IN`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a16_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Supply voltage inverter.


Circuit Additions:
------------------

What sort of circuit could you make to generate the 100 KHz square wave other than using the digital pulse source output on the ADALM2000 Lab board? There are four additional inverters in the 74HC04 package. The other inverters along with RC delay network, R\ :sub:`4` C\ :sub:`4` can be configured into a ring oscillator as shown below. The values for R\ :sub:`4` and C\ :sub:`4` are approximate for 100 KHz and can be adjusted as needed.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a16_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 square wave oscillator


.. _questions-1:

Questions:
----------

What other types of oscillator circuits might be used to generate the 100 KHz square wave?

Appendix:
=========

Hex inverter Pinouts:

|image1| |image2|

.. container:: centeralign

   Figure 7 74HC04 and CD4069 share the same package pinouts


CD4007 Pinout:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 420px

.. container:: centeralign

   Figure 8 CD4007 CMOS array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f8.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 9 CD4007 inverter connections


The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Two of these inverters can be used to construct the inverters needed in figure 3.

For further reading:
--------------------

| :adi:`The Interleaved Inverting Charge Pump—Part 1: A New Topology for Low Noise Negative Voltage Supplies <en/analog-dialogue/articles/the-interleaved-inverting-charge-pump-part-1.html>`
| `Wikipedia page on DC-to-DC converters <https://en.wikipedia.org/wiki/DC-to-DC_converter>`_
| `Wikipedia page on charge pumps <https://en.wikipedia.org/wiki/Charge_pump>`_
| :adi:`ADM660: CMOS Switched-Capacitor Voltage Converter <static/imported-files/data_sheets/ADM660_8660.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/74hc04.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/cd4069a.png
   :width: 300px
