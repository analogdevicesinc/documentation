Activity: Zero gain amplifier (BJT)
===================================

Objective:
----------

In the design of a circuit it is important to take into account the wide variation in certain device values from one to another. A central objective of the designer is to desensitize the circuit to these variations to produce a circuit which meets the specifications across all possible conditions. One aspect of design which is common to nearly all circuits is the establishment of stable bias or operating point levels. This seemingly minor portion of the design can provide the most challenging and interesting circuit problems. Many bias generators are centered around the generation of currents to operate the core of the circuit. Current generated from simple resistors and diodes or diode connected transistors connected across the power supply will vary approximately proportional to the variation of the supply voltage. This variation in the resulting bias current is frequently undesirable.

This is to introduce a current “mirror” in Activity 8 which has an output which had been desensitized to variation in input current. To understand this circuit, it is helpful to examine the behavior of a “zero-gain amplifier”.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 1 - 2.2KΩ Resistor (or any similar value)
| 1 - 47Ω Resistor
| 1 - small signal NPN transistor (2N3904 or SSM2212)

Directions:
-----------

The breadboard connections are as shown in the diagram below. The waveform generator W1 output drives one end of resistor R\ :sub:`1`. Resistor R\ :sub:`2` is connected between the base and collector of transistor Q\ :sub:`1` with the other end of resistor R\ :sub:`1` connected to the base as well. The emitter of Q\ :sub:`1` is grounded.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 Zero Gain Amplifier


Hardware Setup:
---------------

The waveform generator 1 should be configured for a 1 KHz triangle wave with 3 volt amplitude peak-to-peak and 1.5V offset. Connect scope Channel 1 to display output W1 of the AWG generator. The Single ended input of scope channel 2 (2+) is used to measure alternately the base and collector voltage of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/zero_gain-bb.png

.. container:: centeralign

   Figure 2 Zero Gain Amplifier Breadboard Circuit


Procedure:
----------

Remembering back to the common emitter amplifier in the previous section, if R\ :sub:`L` is set equal to r\ :sub:`e` then the gain A will be -1. If the base is connected to the top of resistor R\ :sub:`L` then the gain from the base to the collector (bottom of R\ :sub:`L`) will be -1. Also, neglecting the collector emitter output impedance of the transistor the gain from the top of load resistor R\ :sub:`L` to the collector (bottom of R\ :sub:`L`) will be +1. Thus the net gain superimposing both paths will be 1 - 1 = 0.

In the figure below we have a transistor biased into conduction with a collector voltage which is less than the base voltage by kT/q, (equal to Ic times 47Ω) and is essentially constant with input voltage changes applied from the AWG generator.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 Scopy Plot V\ :sub:`BE`


.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 4 Scopy Plot V\ :sub:`CE`


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Excel Plot comparing V\ :sub:`BE` and V\ :sub:`CE`


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 Excel V\ :sub:`BE` and V\ :sub:`CE` vs. collector current


Questions:
----------

What are the relative gains of the two paths when the collector current is less than and greater than the “ideal” zero gain value?

Improved VBE Multiplier, Applying the Zero Gain Concept
=======================================================

As we explored in Activity 3, there are often circuits which require that a voltage greater than 1 V\ :sub:`BE` be generated. Here we explore in more detail three additional ways to accomplish this.

VBE times 2 version 1:
----------------------

The obviously simple thing to do would be to just use two diode connected transistors in series.

.. _materials-1:

Materials:
----------

| 1 - 1KΩ Resistor
| 2 - small signal NPN transistor (2N3904 or SSM2212)

.. _directions-1:

Directions:
-----------

The breadboard connections are as shown in figure 7 below. The output of the AWG generator drives one end of resistor R\ :sub:`1` as well as the 2+ input of scope channel 2. The emitter of Q\ :sub:`1` is connected to ground. The base and collector of Q\ :sub:`1` are connected to the emitter of Q\ :sub:`2`. The base and collector of Q\ :sub:`2` are connected to the other end of R\ :sub:`1` and to the 2- input of scope channel 2 and the 1+ input of scope channel 1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f4.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 7 V\ :sub:`BE` circuit


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_circuit-bb.png

.. container:: centeralign

   Figure 8 V\ :sub:`BE` Breadboard circuit


The waveform generator should be configured for a 1 KHz triangle wave with 3 volt amplitude peak-to-peak and 1.5V offset. Both scope channels can be set to 200mV per division.

.. _procedure-1:

Procedure:
----------

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 9 Scopy Voltage vs. current


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 Voltage vs. current


You should also confirm that the voltage characteristic measured at the collector, base of transistor Q\ :sub:`1` is the same as was measured in activity 3.

VBE times 2 version 2:
----------------------

A second option would be to use two resistors as a voltage divider. This could produce an output that is the addition of fractions of a V\ :sub:`BE` to the V\ :sub:`BE` of Q\ :sub:`1`.

.. _materials-2:

Materials:
----------

| 1 - 1KΩ Resistor
| 2 - 10KΩ Resistors
| 1 - 5KΩ Variable resistor ( a 500Ω pot would be preferable if available )
| 1 - small signal NPN transistor (2N3904 or SSM2212)

.. _directions-2:

Directions:
-----------

The breadboard connections are as shown in the diagram below. The output of the waveform generator drives one end of resistor R\ :sub:`1` as well as the 2+ input of scope channel 2. The emitter of Q\ :sub:`1` is connected to ground. Resistor R\ :sub:`3` is connected between the base of Q\ :sub:`1` and ground. One end of resistor R\ :sub:`2` connected to the other end of R\ :sub:`1` and to the 2- input of scope channel 2 and one end and the wiper of potentiometer R\ :sub:`4` 1+. The opposite end of R\ :sub:`2` is connected to the base of Q\ :sub:`1`. The collector of Q\ :sub:`2` is connected to the remaining end of R\ :sub:`4` and the 1+ input of scope channel 1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f6.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 11 V\ :sub:`BE` Multiplier circuit


.. _hardware-setup-2:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_multiplier1-bb.png

.. container:: centeralign

   Figure 12 V\ :sub:`BE` Multiplier Breadboard circuit


The waveform generator should be configured for a 1KHz triangle wave with 3 volt amplitude peak-to-peak and 1.5V offset. Both scope channels can be set to 200mV per division.

.. _procedure-2:

Procedure:
----------

Start out with variable resistor R\ :sub:`4` set to its minimum value of nearly zero ohms. Observe the voltage vs. current characteristics of this configuration compared to version 1. There is a small extra current that flows in the two 10KΩ resistors before the transistor turns on. The voltage at 1mA is slightly higher and the slope of the curve is not as steep.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 13 Scopy plot - R\ :sub:`4` set to zero ohms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 14 Excel plot - R\ :sub:`4` set to zero ohms


Let’s apply the concept of the zero gain amplifier. Now adjust R\ :sub:`4` and observe the slope of the curve change. At what value of R\ :sub:`4` is the curve nearly vertical? Why is that value the correct value for “zero” gain?

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   Figure 15 Scopy plot - R\ :sub:`4` set to approximately 100 ohms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 16 Excel plot - R\ :sub:`4` set to approximately 100 ohms


VBE times 2 version 3:
======================

A minor variation on Version 2.

.. _materials-3:

Materials:
----------

| 1 - 1KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - 5KΩ Variable resistor ( 500Ω pot would be preferable if available )
| 2 - small signal NPN transistor (2N3904 or SSM2212)

.. _directions-3:

Directions:
-----------

The breadboard connections are as shown in the diagram below in figure 17. Version 3 is made from version 2 by removing 10KΩ resistor R\ :sub:`2` and replacing it with diode connected NPN Q\ :sub:`2` as shown.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f9.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 17 Version 3 of V\ :sub:`BE` multiplier


.. _hardware-setup-3:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_multiplier3-bb.png

.. container:: centeralign

   Figure 18 Version 3 of V\ :sub:`BE` multiplier Breadboard Circuit


The waveform generator should be configured for a 1KHz triangle wave with 3 volt amplitude peak-to-peak and 1.5V offset. Both scope channels can be set to 200mV per division.

.. _procedure-3:

Procedure:
----------

Again start out with variable resistor R\ :sub:`4` set to its minimum value of nearly zero ohms. Observe the voltage vs. current characteristics of this configuration compared to version 2. There is a small extra current that flows in the one 10K resistors after Q\ :sub:`1` turns on and until both Q\ :sub:`1` and Q\ :sub:`2` are on. The voltage at 1 mA is slightly lower and the slope of the curve is steeper more like version 1.

.. container:: centeralign

   \


   |image6|

.. container:: centeralign

   Figure 19


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 20


Again, let’s apply the concept of the zero gain amplifier. Now adjust R\ :sub:`4` and observe the slope of the curve change. At what value of R\ :sub:`4` is the curve nearly vertical? Why is that value the correct value for “zero” gain?

.. container:: centeralign

   \


   |image7|

.. container:: centeralign

   Figure 22


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 22


Optional extra credit problem:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a7_f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 23


How would you modify the values of R\ :sub:`2` and R\ :sub:`4` in version 2 ( figure 11 ) to produce a stabilized 1.0 volt output?

Answer: using a potentiometer for R\ :sub:`2` the above curve was generated with R\ :sub:`2` = 5.55KΩ and R\ :sub:`4` = 69.8Ω.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bjt_zero_gain_amp_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/bjt_zero_gain_amp_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/zero_gain_vbe-wav.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/zero_gain_vce-wav.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_circuit-wav.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_multiplier-wav1.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_multiplier-wav2.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe-multiplier3-wav1.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe-multiplier3-wav2.png
   :width: 500px
