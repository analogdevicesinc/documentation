Activity: NMOS as a Current Mirror
==================================

Objective:
----------

The purpose of this activity is to investigate the operation of the enhancement mode NMOS transistor as a current mirror.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 1KΩ Resistors (values matched as close as possible, or measured to 3 digits or better)
| 2 - small signal NMOS transistors (ZVN2110A or CD4007 NMOS array)
| 1 - Dual Op Amp such as ADTL082)
| 2 - 4.7uF decoupling capacitors

Directions:
-----------

The good way to measure the characteristics of a current mirror is to adapt the same basic configuration that was used in the common emitter BJT curve tracer experiments. The input and output resistors R\ :sub:`1` and R\ :sub:`2` are now both 1KΩ. Be sure to accurately measure (with the most significant figures possible) the actual values of R\ :sub:`1` and R\ :sub:`2`. This is to insure accurate measurement of the input and output current of the mirror. I\ :sub:`in` will be equal to the AWG2 output voltage at W1 divided by the value of R\ :sub:`1`. I\ :sub:`out` will be the voltage measured by scope channel 2 divided by the value of R\ :sub:`2`. Diode connected M\ :sub:`1` is connected across the gate and source terminals of M\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NMOS Current mirror test circuit


   |image1|

.. container:: centeralign

   Figure 2 NMOS Current mirror test circuit breadboard connection


Hardware Setup:
---------------

In the current mirror configuration, the opamp serves as a virtual ground at the mirror input (gate) node to convert the voltage steps from AWG 1 ( W1 output ) into current steps through the 1K? resistor. The drain voltage is swept using a ramp from AWG 1(output W1). Load the stairstep.csv file, set amplitude to 3V peak-to-peak with the offset to 1.5V. V\ :sub:`DS` of output device M\ :sub:`2` is measured differentially by scope inputs 1+, 1-. The mirror output current is measured by scope inputs 2+. 2- across 1K? resistor, R\ :sub:`2`. If you don't want to use the op-amp configuration the following simplified configuration can be used as well.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 simplified test configuration


   |image2|

.. container:: centeralign

   Figure 4 Simplified test configuration breadboard connection


Procedure:
----------

Two identical transistors with the same gate to source voltage will have the same drain current I\ :sub:`D`. The second transistor, M\ :sub:`2`, in effect mirrors the current in the first, M\ :sub:`1`. Remembering the drain current to gate source voltage relationship for a MOS transistor:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6m_ne1.png
   :align: center

| where K =μ\ :sub:`n`\ C\ :sub:`ox`/2<sub></sub> and λ can be taken as process technology constants.
| Identical transistors by definition have the same W/L and process technology constants. In the simple current mirror, both transistors have the same V\ :sub:`GS`. Thus, both transistors will have the same I\ :sub:`D`. Since no current flows in the gate terminal of a FET I\ :sub:`in` = I\ :sub:`out`. |image3|

.. container:: centeralign

   Figure 5 Current Mirror waveform


.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/mos_current_mirror_bb`
   -  LTspice files: :git-education_tools:`mos_current_mirror_ltspice <m2k/ltspice/nmos_cur_mirror_ltspice>`
   


Questions:
----------

You are to measure I\ :sub:`in`, Rout seen into the drain of M\ :sub:`2`, the current mirror gain = I\ :sub:`out`/I\ :sub:`in` and determine the Norton and Thevenin equivalent circuits for this mirror.

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a6m_nf2.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a6m_nf4.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a6m_nf5.png
   :width: 500px
