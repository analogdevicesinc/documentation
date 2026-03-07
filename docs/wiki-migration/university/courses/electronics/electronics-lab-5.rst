Activity: Common Emitter Amplifier
==================================

Objective:
----------

The purpose of this activity is to investigate the common emitter configuration of the BJT.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 4 - Resistors
| 1 - 50KΩ Variable resistor, potentiometer
| 1 - small signal NPN transistor (2N3904)

Directions:
-----------

The configuration, shown in figure 1, demonstrates the NPN transistor used as the common emitter amplifier. Output load resistor R\ :sub:`L` is chosen such that for the desired nominal collector current I\ :sub:`C`, approximately one half of the Vp voltage (2.5V) appears at V\ :sub:`CE`. Adjustable resistor Rpot along with Rb sets the nominal bias operating point for the transistor (I\ :sub:`B`) to set the required I\ :sub:`C`. Voltage divider R\ :sub:`1`/R\ :sub:`2` is chosen to provide a sufficiently large attenuation of the input stimulus from waveform generator 1. This is done to more easily view the generator W1 signal, given the rather small signal that will appear at the base of the transistor, V\ :sub:`BE`. The attenuated waveform generator W1 signal is AC coupled into the base of the transistor by the 4.7 uF capacitor so as not to disturb the DC bias condition.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Common emitter amplifier test configuration


Hardware Setup:
---------------

|image1|

.. container:: centeralign

   Figure 2 Common emitter amplifier test configuration breadboard connection


The waveform generator output W1 should be configured for a 1 KHz sine wave with 3 volt amplitude peak-to-peak and 0 volt offset. The setup should be configured with scope channel 1+ connected to display the output W1. Scope channel 2 (2+) is used to measure alternately the waveform at the base and collector of Q\ :sub:`1`.



|image2|

.. container:: centeralign

   Figure 3 Common emitter amplifier test configuration, V\ :sub:`in` and V\ :sub:`BE`\


   |image3|

.. container:: centeralign

   Figure 4 Common emitter amplifier test configuration, V\ :sub:`in` and V\ :sub:`BE`\


Procedure:
----------

The voltage gain, A, of the common emitter amplifier can be expressed as the ratio of load resistor R\ :sub:`L` to the small signal emitter resistance r\ :sub:`e`. The transconductance, g\ :sub:`m`, of the transistor is a function of the collector current I\ :sub:`C` and the so called thermal voltage, kT/q which can be approximated by around 25 mV or 26 mV at room temperature.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_e1.png
   :align: center
   :width: 200px

The small signal emitter resistance is 1/g\ :sub:`m` and can be viewed as being in series with the emitter. Now with a signal applied to the base the same current (neglecting base current) flows in r\ :sub:`e` and the collector load R\ :sub:`L`. Thus the gain A is given by the ratio of R\ :sub:`L` to r\ :sub:`e`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_e2.png
   :align: center
   :width: 200px

Alternately, the curve tracer circuit from activity 7 can be modified slightly, (might be simplest way since it was already constructed in the earlier section) to produce a common emitter amplifier test circuit shown below. All the attributes are basically the same with two slight advantages. One is the base current bias is no longer dependent on the exponential base voltage (V\ :sub:`BE`). The second is the summation of the small AC signal from the attenuated AWG 1 output is independent of the base bias circuit and does not need to be AC coupled. The small signal AC input is applied to the non-inverting terminal of the op-amp and thus due to the negative feedback also appears at the base of the transistor (inverting op-amp input).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Alternate Common emitter amplifier test configuration


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_nf2.png
   :align: center

.. container:: centeralign

   Figure 6 Alternate Common emitter amplifier test configuration breadboard connection


   |image4|

.. container:: centeralign

   Figure 7 Alternate Common emitter amplifier test configuration, Vin and VBE


   |image5|

.. container:: centeralign

   Figure 8 Alternate Common emitter amplifier test configuration VBE zoom


Self-biased configuration with negative feedback
================================================

.. _objective-1:

Objective:
----------

The purpose of this section is to investigate effect of adding negative feedback to stabilize the DC operating point.


|image6|

.. container:: centeralign

   Figure 9 Self Biased configuration


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_nf3.png
   :align: center

.. container:: centeralign

   Figure 10 Self Biased configuration breadboard connection


   |image7|

.. container:: centeralign

   Figure 11 Self Biased configuration, V\ :sub:`in` and V\ :sub:`CE`


   |image8|

.. container:: centeralign

   Figure 12 Self Biased configuration, V\ :sub:`in` and V\ :sub:`BE`\


Questions:
----------

How does adding negative feedback help to stabilize the DC operating point?

Adding emitter degeneration
===========================

.. _objective-2:

Objective:
----------

The purpose of this activity is to investigate effect of the addition of emitter degeneration.

Additional Materials:
---------------------

1 - 5KΩ Variable resistor, potentiometer (500? if one is available)

.. _directions-1:

Directions:
-----------

Disconnect the emitter of Q\ :sub:`1` from ground and insert R\ :sub:`E`, a 5KΩ potentiometer, as shown in the following diagram. Adjust R\ :sub:`E` while noting the output signal seen at the collector of the transistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 13 Emitter degeneration added


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_nf4.png
   :align: center

.. container:: centeralign

   Figure 14 Emitter degeneration added breadboard connection


   |image9|

.. container:: centeralign

   Figure 15 Emitter degeneration added, V\ :sub:`in` and V\ :sub:`CE`\


   |image10|

.. container:: centeralign

   Figure 16 Emitter degeneration added, V\ :sub:`in` and V\ :sub:`BE`


.. _questions-1:

Questions:
----------

What effect does adding R\ :sub:`E` have to the DC operating point of the circuit and how much would you need to adjust R\ :sub:`pot` to return the circuit to the same DC bias (I\ :sub:`C`) you had in figure 1?

What is the effect on the voltage gain, A, by increasing R\ :sub:`E`?

Increasing AC gain of emitter degenerated amplifier
===================================================

Adding the emitter degeneration resistor has improved the stability of the DC operating point at the cost decreased amplifier gain. A higher gain for AC signals can be restored to some extent by adding capacitor C\ :sub:`2`\ across the degeneration resistor R\ :sub:`E` as shown in figure 9.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 17 C\ :sub:`2` added to increase AC gain


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5_nf5.png
   :align: center

.. container:: centeralign

   Figure 18 C\ :sub:`2` added to increase AC gain


   |image11|

.. container:: centeralign

   Figure 19 C\ :sub:`2` added to increase AC gain, V\ :sub:`in` and V\ :sub:`CE`


   |image12|

.. container:: centeralign

   Figure 20 C\ :sub:`2` added to increase AC gain, V\ :sub:`in` and V\ :sub:`BE`


.. admonition:: Download
   :class: download

   \*\* Lab Resources:\*\*

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/comm_emit_amp_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/comm_emit_amp_ltspice`
   


References for further reading:
-------------------------------

http://en.wikipedia.org/wiki/Common_emitter_amplifier

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/ce_amp_test_config-bb_bb.png
   :width: 900px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/1vce-gnd.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/1vbe-gnd.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/alt_ce_vb.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/alt_ce_vb_zoom.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/a5_f3.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/self_b_vc.png
   :width: 900px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/self_b_vb.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/emit_deg_vc-gnd.png
   :width: 900px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/emit_deg_vb-gnd.png
   :width: 900px
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/inc_gain_vc.png
   :width: 900px
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/inc_gain_vb.png
   :width: 900px
