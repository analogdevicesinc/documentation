Activity: Zener Diode Regulator - ADALM2000
===========================================

Objectives:
-----------

A voltage regulator is a circuit used to maintain a constant output voltage at a load independent of changes in the load current. For example, the "load" could be a microcontroller based system that requires a constant supply voltage even as its demand for current varies with system activity. The zener diode regulator of figure 1 offers a very simplified way to maintain the load voltage V\ :sub:`L` at the same value as the reverse breakdown voltage of the zener diode, provided that the load resistance R\ :sub:`L` remains higher than some lower limit. The voltage source V\ :sub:`IN` and resistor R\ :sub:`S` model the Thévenin resistance of a possible circuit that has converted a high voltage such as the 120V AC mains power to an unregulated and unfiltered lower DC voltage source.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - 1KΩ Resistor (R\ :sub:`S`)
| 1 - 5KΩ Variable resistor, potentiometer (R\ :sub:`L`)
| 1 - Zener diode (1N4735 or similar)

Directions:
-----------

Build the circuit shown in figure 1 on your solder-less breadboard using the 1N4735 6.1 volt zener diode. Use AWG1 (5V constant) and the -5V Vn user supply to establish the DC supply V\ :sub:`IN`. Use various fixed and variable resistors for R\ :sub:`L`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a26_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Zener Diode regulator


Hardware Setup:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/zener_reg-bb.png
   :align: center

.. container:: centeralign

   Figure 2 Zener Diode regulator Breadboard Circuit


Procedure:
----------

| 1. Monitor and report the load voltage V\ :sub:`L` by using the Scopy Voltmeter instrument to measure V\ :sub:`L` for R\ :sub:`L` equal to:
| \* Open circuit
| |image1|

.. container:: centeralign

   Figure 3 R\ :sub:`L` = Open Circuit Zener Diode regulator waveform


-  10 kΩ



|image2|

.. container:: centeralign

   Figure 4 R\ :sub:`L` = 10kΩ Zener Diode regulator waveform


-  1 kΩ



|image3|

.. container:: centeralign

   Figure 5 R\ :sub:`L` = 1kΩ Zener Diode regulator waveform


-  100 Ω



|image4|

.. container:: centeralign

   Figure 6 R\ :sub:`L` = 100Ω Zener Diode regulator waveform


2. Replace the load R\ :sub:`L` with a 5KΩ potentiometer, and adjust the potentiometer to determine the minimum value of R\ :sub:`L` for which V\ :sub:`L` remains within 10% of the zener voltage V\ :sub:`Z`. Measure and report the resistance you set the potentiometer to. How does this resistance relate to the value of R\ :sub:`S`?

Questions:
----------

Add questions here:

Further Exploration:
--------------------

Investigate the current/voltage characteristic curve for the zener diode using the same technique described in Activity 2 by measuring the current in R\ :sub:`S` with scope channel 2 and plotting the voltage across the zener vs the current in the Oscilloscope XY mode. Be sure to adjust the horizontal voltage range and offset to include the 6.1 volt breakdown voltage. Discuss your results, in particular the ways in which the zener diode is similar to and different from a conventional diode.

Driving larger load currents:
-----------------------------

As we saw in the simple zener diode regulator in figure 1, the maximum load current is determined by resistor R\ :sub:`S`. Also the circuit is very inefficient for smaller load currents with respect to the maximum in that the excess current flows in the zener when not flowing in the load. The inclusion of an emitter follower or Darlington emitter follower current amplifier can greatly improve the efficiency of this regulator circuit as shown in figure 2.

Additional Materials:
---------------------

| 2 - NPN transistors (2N3904 and TIP31)
| 2 - small signal diodes (1N914 or similar)
| |image5|

.. container:: centeralign

   Figure 2, Adding a current amplifier stage


.. _directions-1:

Directions:
-----------

Build either of the circuits shown in figure 2 on your solder-less breadboard using the 1N4735 6.1 volt zener diode as D\ :sub:`1` and a 2N3904 or TIP31 power transistor for Q\ :sub:`1`. Q\ :sub:`2` can be a 2N3904 and D\ :sub:`2`, D\ :sub:`3` can be a 1N914.

The extra diode D\ :sub:`2` is added in series with the zener to partially cancel the additional V\ :sub:`BE` drop due to the emitter follower Q\ :sub:`1`. Likewise in the Darlington configuration two diodes (D\ :sub:`2`, D\ :sub:`3`) are added to again partially cancel the two V\ :sub:`BE` drop of the Darlington follower.

.. _questions-1:

Questions:
----------

Add questions here:

.. admonition:: Download
   :class: download

   \*\* Resources: \*\*

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/zener_reg_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/zener_reg_ltspice`
   


For Further Reading
-------------------

Zener Diodes http://en.wikipedia.org/wiki/Zener_diode

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/zener_reg-wav1.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/zener_reg-wav2.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/zener_reg-wav3.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/zener_reg-wav4.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a26_f2.png
   :width: 500px
