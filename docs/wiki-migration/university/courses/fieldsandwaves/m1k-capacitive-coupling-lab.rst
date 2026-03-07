Activity: Capacitive Coupling – For ADALM1000
=============================================

Objective:
----------

The objective of this lab activity is to study the coupling of a varying electric field between adjacent parallel wires.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

**Capacitive coupling**

Capacitive coupling is the transfer of signals or energy within an electrical network or between distant networks by means of displacement current between circuit nodes, induced by a changing electric field. This coupling can be intentional or an unintentional parasitic effect.

Materials:
----------

| ADALM1000 hardware module
| 2 12 inch / 30 cm long 3 wire female to female header jumper wires (should be included with ADALM1000)

| From ADALP2000 parts kit:
| Solder-less breadboard
| Male to Male jumper wires
| Male to male header pins (gender changers)
| 1 100 KΩ resistor

| 8 solid core jumper wires, 4 Red and 4 Green
| The jumper wires may need to be cut from the reels of solid hook-up wire. Cut them to be about the length of the solder-less breadboard. Note that the spatial layout of the jumper wires is important in this experiment.

Directions:
-----------

Using one of the female to female header jumper wires, connect the circuit together as shown in figure 1. You will need to place the 100 KΩ resistor on the solder-less breadboard to connect the wires from the ADALM1000 analog connector pins.

Set the AWG A generator Max value to 4.5V and the Min value to 0.5V. Set the waveform shape to Sine. Set the frequency to 15 kHz. Because of the higher output frequency setting it is desirable to switch the AWG A sample rate to 2X by clicking on CH A 2X selector. To use the 2X mode the AWG B DAC is not used and the AWG B Mode should be set to SVMI Split I/O Mode and the wave shape set to DC as shown in figure 3. The rest of the AWG B settings are unimportant.

In this part of the experiment the varying electric field is applied on the center Red wire of the cable. The induced (coupled) voltage is measured on one of the other wires, White wire, in the cable. At first the third Black wire is left floating (not connected to anything).

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Parallel wire testing


**Alternatively**

If you do not have the 3 wire header cables you can build a similar test structure on the solder-less breadboard as shown in figure 2. Insert four red solid jumper wires in same column of holes (number 48 in picture) in the breadboard so the four red wires are all shorted together. Insert four green solid jumper wires in a column of holes adjacent to the column you just used (number 47 in picture) in the breadboard so the four green wires are all shorted together. The red and green wires should not be shorted together. Arrange all 8 wires so they lie flat against the breadboard but are interleaved with each other red/green as shown. Adding a short jumper about half way down the long jumpers across the 8 wires can help keep the wires neatly arranged together and flat.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Parallel wires on a solder-less breadboard.


You do not need to use different color wires but it will help to keep them separate when inserted into the breadboard. The overall length of the wires in parallel can be changed by adding or removing pairs of red and green jumpers.

We use a sine wave signal to drive one of the parallel wires and generate the time varying electric field. The AWG settings are shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, AWG settings.


.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4, Scope settings screen.


Using one of the male to male jumper wires connect the Black wire in the cable to the White wire. How has adding the Black wire changed the coupled signal amplitude?

Use three of the male-to-male header pins to connect the second 3 wire header cable to the end of the first cable. If you are not using the three wire cable, change the number of parallel wires on the breadboard. This will increase the overall length of the cable. How has this changed the coupled signal amplitude?

Questions to be answered in your Lab report:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Describe two qualitative differences between the input and output voltage waveforms.

Does the voltage amplitude at on the output increase or decrease when the length of the parallel wires is increased?

How does the frequency of the signal being coupled change the amplitude of coupled signal? Change the frequency of AWG A, increase and decrease to determine the answer.

Crosstalk due to capacitive coupling
------------------------------------

Crosstalk is the coupling of signals and noise between 2 or more wires or lines. Crosstalk is also often called interference. The term "crosstalk" hearkens back to the age of analog telephony where multiple phone lines or circuits were combined or bundled in single larger cables. One phone conversation could often be heard on adjacent phone lines in the same bundle thus the term "talking across lines". Ideally, if two wires are separate (including wiring on a printed circuit board), then electrical signals and noise should not propagate or couple between them. However, if two lines are close and parallel to each other, the stray (parasitic) capacitance that exists between the two lines results in signal and/or noise transmission between the wires. The best method to reduce this capacitance is to increase the separation between the wires. This is often not practical. A common way to reduce the amount of coupling is to introduce grounded conductors between the wires.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig5.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5, Adding a shield between adjacent parallel signals


Test this by changing the way the signal source is connected to the 3 wire cable as we see in figure 6. Here the channel A AWG generator signal is connected to one of the outside wires, White. The BIN pin, which is used to measure the amount of coupling, is connected to the opposite outside wire, Black. The middle wire, Red, is alternately left floating and connected to ground.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Testing effect of adding a ground shield


Measure the amplitude of the coupled signal on the black wire with the Red wire floating and grounded and compare what you measure to the amplitude of the coupled signal you measured previously (from figure 1).

Quantifying the amount of Capacitance:
--------------------------------------

We can use the Impedance Analyzer Tool in ALICE to measure the capacitance between various combinations of the wires in the cable. Figure 7 shows the connections to measure the cable capacitance.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Testing cable capacitance.


.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-cap-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Impedance Analyzer Screen settings.


After entering the correct settings, first measure and zero out any stray capacitance of the test jig by leaving the cable unconnected to BIN and the end of the 100 K resistor. This can be done by clicking on the Zero button under Capacitance Offset. The offset can be reset to zero by clicking on the Reset button. Once the stray capacitance is zeroed out connect the cable as shown in the figure. Take a first measurement with just one wire (White or Black) connected to the 2.5V common supply rail. Now connect the other wire and compare your reading. Now connect both the White and Black to the 2.5 V rail and compare what you measure with just one wire connected to 2.5V. Here is a good question: Does it matter if the White and/or Black wires are connected to GND or the +5 V supply rail?

If you have time repeat your measurements with both header cables connected end to end with three male-to-male header pins (a longer overall cable). How does this change the capacitance measured?

Extra Credit Experiment
-----------------------

Find some other cables to measure. The ADALP2000 kit contains a micro USB breakout connector that you could use to connect to a spare USB cable you might have. There is also a 3.5mm audio jack breakout connector in the Kit. If you have an audio extension cable try and measure that. It has to be just an extension cable and not a headphone cable. The headphone element will load down the test fixture and not measure the capacitance.

**For Further Reading:**

| `Capacitive coupling <https://en.wikipedia.org/wiki/Capacitive_coupling>`_
| `Crosstalk <https://en.wikipedia.org/wiki/Crosstalk>`_
| `From learn EMC <https://learnemc.com/electric-field-coupling>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/fieldsandwaves>`\ **.**
