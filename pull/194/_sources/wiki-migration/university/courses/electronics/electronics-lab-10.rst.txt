Activity: Shunt regulator - ADALM2000
=====================================

Objective:
----------

The zero gain amplifier (Q\ :sub:`1`, R\ :sub:`2`) and stabilized current source (Q\ :sub:`2`, R\ :sub:`3`) can be used in conjunction with a common emitter amplifier stage (Q\ :sub:`3`) in negative feedback to build a two terminal circuit which provides a constant or regulated output voltage over a range of input currents.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 2.2KΩ Resistor (or any similar value)
| 1 - 100Ω resistor
| 1 - 1KΩ resistor (or similar value)
| 1 - 10KΩ variable resistor (potentiometer)
| 3 - small signal NPN transistors (2N3904 and SSM2212)

Directions:
-----------

The breadboard connections are as shown in figure 1 below. The output of the function generator drives one end of resistor R\ :sub:`4`. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor Q\ :sub:`1` are connected as in previous zero gain amplifier section. Resistor R\ :sub:`3` and transistor Q\ :sub:`2` are added as in the stabilized current source section. If the SSM2212 matched NPN pair is used it is best that it be used for devices Q\ :sub:`1` and Q\ :sub:`2`. Q\ :sub:`3` is added with its emitter grounded, its base connected to the collector of Q\ :sub:`2` and collector connected to the combined node of R\ :sub:`1`, R\ :sub:`3` R\ :sub:`4` and scope input 2+.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a10_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Band-gap shunt regulator


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/bandgap_sh_reg-bb.png

.. container:: centeralign

   Figure 2 Band-gap shunt regulator Breadboard Circuit


Waveform generator W1 should be configured for a 1 KHz triangle wave with 4 volt amplitude peak-to-peak and 2V offset. The Single ended input of scope channel 2 (2+) is used to measure the regulated output voltage at the collector of Q\ :sub:`3`.

Procedure:
----------

The regulated output voltage should be observed as the variable resistor R\ :sub:`3` is adjusted.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 output voltage vs. input voltage


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a10_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 output voltage vs. input current


Questions:
----------

What affects the regulated output voltage as a load to ground is applied to the output voltage?

What determines or limits the current available to an output load?

Using an NPN transistor array:
==============================

The CA3045,46 ( LM3045, 46 ) NPN transistor array is a good alternate choice for building this example circuit. See pinout below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a9_f3.png
   :align: center
   :width: 400px

All the emitters can be tired to ground ( pins 3,7,10,13 ). Devices Q\ :sub:`1`, Q\ :sub:`2` and Q\ :sub:`3` can be connected in parallel and serve as Q\ :sub:`2` in figure 1. Q\ :sub:`4` and Q\ :sub:`5` can be used for Q\ :sub:`1` and Q\ :sub:`3` in figure 2. The 3 to 1 emitter area ratio will result in an output voltage very nearly 1.2 volts if R\ :sub:`1` and R\ :sub:`3` are both equal to 2KΩ.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`shunt_reg_bb <m2k/fritzing/shunt_volt_reg_bb>`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/shunt_reg_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/bandgap_sh_reg-wav.png
   :width: 500px
