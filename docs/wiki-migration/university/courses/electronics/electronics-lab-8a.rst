Activity: A Floating (two terminal) Current Source / Sink
=========================================================

Objective:
----------

The objective of this activity is to investigate the ΔV\ :sub:`BE` concept to produce an output current which is stabilized (less sensitive) to variations of the input voltage level. Feedback is used to build a circuit which produces a constant or regulated output current over a range of supply voltages

Background:
-----------

The :adi:`AD590 <media/en/technical-documentation/data-sheets/AD590.pdf>` is a 2-terminal integrated circuit temperature transducer that produces an output current proportional to absolute temperature. The schematic diagram of this floating current source is shown in figure 7 of the AD590 datasheet. The a simplified and less accurate version of this concept is used as the experimental circuit in this activity.

The AD590 uses a fundamental property of silicon BJT transistors to realize its temperature proportional characteristic. If two identical transistors are operated at a constant ratio of collector current densities, r, then the difference in their base-emitter voltage is (kT/q)(In r). Because both k (Boltzman’s constant) and q (the charge of an electron) are constant, the resulting voltage is directly proportional to absolute temperature (PTAT). For more details please refer to the datasheet.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 1 - 500Ω Variable Resistor, Potentiometer
| 1 - 100Ω Resistor
| 3 - small signal NPN transistors (2N3904)
| 3 - small signal PNP transistors (2N3906)

Directions:
-----------

Build the circuit shown in figure 1 on your solder-less breadboard. The green boxes indicate where to connect the ADALM2000. PNP transistors Q\ :sub:`1`, Q\ :sub:`2` and Q\ :sub:`3` form a current mirror with a gain of two, the output current is twice the input current. NPN transistors Q\ :sub:`4`, Q\ :sub:`5` and Q\ :sub:`6` along with variable resistor R\ :sub:`1` form the ΔV\ :sub:`BE` part of the circuit. Resistor R\ :sub:`2` is used to measure the current flowing in the circuit ( scope channel 2 ) as the voltage across the circuit changes ( scope channel 1 ).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18a_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Floating current source (as a sink tied to a negative supply)


The output current is set by R\ :sub:`1`. The difference in V\ :sub:`BE` ( ΔV\ :sub:`BE` ) between Q\ :sub:`4` and the parallel combination of Q\ :sub:`5`,Q\ :sub:`6` appears across R\ :sub:`1`. The PNP mirror, Q\ :sub:`1`,Q\ :sub:`2` and Q\ :sub:`3`, has a gain of 2, if we assume they are of identical size. Thus the current in Q\ :sub:`4` is twice the combined current of Q\ :sub:`5` and Q\ :sub:`6`. Again if we assume Q\ :sub:`4`, Q\ :sub:`5` and Q\ :sub:`6` are also identical in size, the current density ratio is 4 and the difference in V\ :sub:`BE` will be:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18a_e1.png
   :align: center
   :width: 200px

Because of the absolute temperature term in this equation the current will be proportional to absolute temperature. This can be a useful characteristic in certain instances but also undesirable in others.

Hardware setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/float_curr_src_vn-bb.png

.. container:: centeralign

   Figure 2 Floating current source (as a sink tied to a negative supply) Breadboard Circuit


Configure waveform generator AWG1 as a triangle wave with a frequency of 100 Hz and an amplitude of 10 V peak-to-peak with 0 V offset. The scope display should be set in both voltage vs. time and in XY mode with channel 1 on the horizontal axis and channel 2 on the vertical axis. Be sure to turn on the power supply only after you have completed and double checked your connections.

Procedure:
----------

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 Floating current source (as a sink tied to a negative supply) XY plot


Questions:
----------

What is the minimum voltage that the current source needs across it to maintain a more or less constant current?

Is it larger or smaller than 2\*V\ :sub:`BE` and why?

Measure the ΔV\ :sub:`BE` across adjustable resistor R\ :sub:`1`\ with AWG1 set to a fixed voltage. How does the value of ΔV\ :sub:`BE` change as the resistance of R\ :sub:`1` is varied?

Prove the floating nature of circuit:
-------------------------------------

In figure 1 we referenced the negative end of the circuit to a negative power supply. To prove that this circuit is truly a floating current source, rearrange your breadboard to look like figure 5 and repeat your measurements.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18a_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Floating current source (as a source tied to a positive supply)


.. _hardware-setup-1:

Hardware setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/float_curr_src_vp-bb.png

.. container:: centeralign

   Figure 5 Floating current source (as a sink tied to a positibe supply) Breadboard Circuit


.. _procedure-1:

Procedure:
----------

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 6 Floating current source (as a sink tied to a positive supply) XY plot


.. _questions-1:

Questions:
----------

Is there any measurable difference in the current vs. voltage characteristics for the circuit used as a current sink vs. a current source?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/float_current_source_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/float_current_source_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/float_curr_src_vn-wav.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/float_curr_src_vp-wav.png
   :width: 500px
