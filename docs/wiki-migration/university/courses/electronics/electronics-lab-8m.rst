Activity: Stabilized current source (NMOS)
==========================================

Objective:
----------

The objective of this activity is to investigate the use of the zero gain concept to produce an output current which is stabilized (less sensitive) to variations of the input current level.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 1 - 2.2KΩ Resistor ( or any similar value )
| 1 - 168Ω Resistor ( connect a 100Ω in series with a 68Ω )
| 1 - 4.7KΩ Resistor
| 2 - small signal NMOS transistors (CD4007 or ZVN2110A)

Directions:
-----------

The breadboard connections are as shown in figure 1 below. The output of waveform generator W1 drives one end of resistor R\ :sub:`1`. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor M\ :sub:`1` are connected as in previous zero gain amplifier section. Since the V\ :sub:`GS` of M\ :sub:`2` is always smaller than the V\ :sub:`GS` of Q\ :sub:`1`, you should, if possible, select M\ :sub:`1` and M\ :sub:`2` from your inventory of devices such that (at the same drain current) M\ :sub:`2`'s V\ :sub:`GS` is less than M\ :sub:`1`'s V\ :sub:`GS`. The gate of transistor M\ :sub:`2` is connected to the zero gain output at the drain of M\ :sub:`1`. R\ :sub:`3`, connected between the Vp supply and the drain of M\ :sub:`2`, is used along with the 2+ (Single Ended) scope input to measure the drain current.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a8m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Stabilized current source


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_stabilized_cs-bb.png

.. container:: centeralign

   Figure 2 Stabilized current source Breadboard Circuit


The waveform generator should be configured for a 1 KHz triangle wave with 4 volt amplitude peak-to-peak and 2V offset. The input of scope channel 2 (2+) is used to measure the stabilized output current at the drain of M\ :sub:`2`.

Procedure:
----------

The zero gain amplifier can be used to create a stabilized current source. Because the voltage seen at the drain of transistor M\ :sub:`1` is now more constant with changes in the input supply voltage as represented by AWG1, it can be used as the gate voltage of M\ :sub:`2` to produce a much more constant current in transistor M\ :sub:`2`.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 M\ :sub:`2` drain voltage vs. W1 voltage


Questions:
----------

This circuit is sometimes referred to as a peaking current source. Why do you think?

Based on the delta V\ :sub:`GS` of M\ :sub:`1` and M\ :sub:`2`, at what input and output current would the gain be zero for different values of R\ :sub:`2`?

An exercise for the reader is to plot the "stabilized" output current for all the various combinations of M\ :sub:`1` and M\ :sub:`2` from the available inventory of transistors. Why does it vary and by how much? The output of the simple peaking current source is always less than the input current at the peak by a substantial fraction. What is that fraction and why?

How can the circuit be changed to make the output a larger fraction of, or even equal to or larger than, the input?

The output current has a narrow peak. How could multiple copies of the peaking current source be combined to produce a much wider, flatter peak?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  LTspice files: :git-education_tools:`m2k/ltspice/mos_stab_curr_source_ltspice`
   -  Fritzing files: :git-education_tools:`m2k/fritzing/mos_stab_cs_bb`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_stabilized_cs.png
   :width: 500px
