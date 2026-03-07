Activity: Zener Diode Regulator
===============================

Objectives:
-----------

The objective of this lab activity is explore the use of Zener diodes to build a circuit which provides a constant or regulated output voltage over a range of input voltages and load currents.

Background:
-----------

A voltage regulator is a circuit used to maintain a constant output voltage at a load independent of changes in the load current. For example, the "load" could be a microcontroller based system that requires a constant supply voltage even as the current demand varies with system activity. The zener diode regulator of figure 1 offers a very simplified way to maintain the load voltage V\ :sub:`L` at the same value as the reverse breakdown voltage of the zener diode, provided that the load resistance R\ :sub:`L` remains higher than some lower limit. The voltage source V\ :sub:`IN` and resistor R\ :sub:`S` model the Thévenin resistance of a possible circuit that has converted a high voltage such as the 120V AC mains power to an unregulated and unfiltered lower DC voltage source.

Materials:
----------

| Analog Discovery Instrument
| Solder-less Breadboard
| 1 - 1 KΩ Resistor (R\ :sub:`S`)
| 1 - 5 KΩ Variable resistor, potentiometer (R\ :sub:`L`)
| 1 - 4.7V Zener diode (1N5230 or similar)

Directions:
-----------

Build the circuit shown in figure 1 on your solder-less breadboard using the 1N5230 4.7 volt zener diode. Use AWG1 and the -5V Vn user supply to establish the DC supply V\ :sub:`IN`. Use various fixed and variable resistors for R\ :sub:`L`.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_zener-reg-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Zener Diode regulator


Measurements:
-------------

| 1. Monitor and report the load voltage V\ :sub:`L` by using the Waveforms Voltmeter instrument to measure V\ :sub:`L` for R\ :sub:`L` equal to:
| (a) Open circuit
| (b) 10 kΩ
| (c) 1 kΩ
| (d) 100 Ω

2. Replace the load R\ :sub:`L` with a 5KΩ potentiometer, and adjust the potentiometer to determine the minimum value of R\ :sub:`L` for which V\ :sub:`L` remains within 10% of the zener voltage V\ :sub:`Z`. Measure and report the resistance you set the potentiometer to. How does this resistance relate to the value of R\ :sub:`S`?

Further Exploration:
~~~~~~~~~~~~~~~~~~~~

Investigate the current/voltage characteristic curve for the zener diode using the same technique described in the Activity on diode characteristics by measuring the current in R\ :sub:`S` with scope channel 2 and plotting the voltage across the zener vs the current in the Oscilloscope XY mode. Be sure to adjust the horizontal voltage range and offset to include the 6.1 volt breakdown voltage. Discuss your results, in particular the ways in which the zener diode is similar to and different from a conventional diode.

Driving larger load currents:
-----------------------------

As we saw in the simple zener diode regulator in figure 1, the maximum load current is determined by resistor R\ :sub:`S`. Also the circuit is very inefficient for smaller load currents with respect to the maximum in that the excess current flows in the zener when not flowing in the load. The inclusion of an emitter follower or Darlington emitter follower current amplifier can greatly improve the efficiency of this regulator circuit as shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_zener-reg-f2.png
   :align: center
   :width: 550px

<WRAP centeralign> Figure 2, Adding a current amplifier stage </WARP>

.. _directions-1:

Directions:
-----------

Build either of the circuits shown in figure 2 on your solder-less breadboard using the 1N5230 4.7 volt zener diode as D\ :sub:`1` and a 2N3904 or TIP31 power transistor for Q\ :sub:`1`. Q\ :sub:`2` can be a 2N3904 and D\ :sub:`2`, D\ :sub:`3` can be a 1N4001. The extra diode D\ :sub:`2` is added in series with the zener to partially cancel the additional V\ :sub:`BE` drop due to the emitter follower Q\ :sub:`1`. Likewise in the Darlington configuration two diodes (D\ :sub:`2`, D\ :sub:`3`) are added to again partially cancel the two V\ :sub:`BE` drop of the Darlington follower.

**For Further Reading:**

| http:*en.wikipedia.org/wiki/Zener_diode
  http:*\ www.mathworks.com/help/physmod/powersys/examples/zener-diode-regulator.html
| http://www.analog.com/static/imported-files/tutorials/MT-087.pdf

**Return to EPS Activity** :doc:`Table of Contents. </wiki-migration/university/courses/eps/main-page>`
