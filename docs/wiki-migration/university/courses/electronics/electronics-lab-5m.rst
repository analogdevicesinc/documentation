Activity: MOS transistor common source amplifier
================================================

Ojective:
---------

The purpose of this activity is to investigate the common source configuration of the MOS transistor.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 5 - Resistors
| 1 - 50 KΩ Variable resistor, potentiometer
| 1 - small signal NMOS transistor (enhancement mode ZVN2110A or CD4007)

Directions:
-----------

The configuration, shown in figure 1, demonstrates the NMOS transistor used as the common source amplifier. Output load resistor R\ :sub:`L` is chosen such that, for the desired nominal drain current I\ :sub:`D`, the voltage appearing at V\ :sub:`DS` is approximately half way between Vp and Vn (0 volts). Adjustable resistor Rpot a sets the nominal bias operating point for the transistor (V\ :sub:`GS`) to set the required I\ :sub:`D`. Voltage divider R\ :sub:`1`/R\ :sub:`2` is chosen to provide a sufficiently large attenuation of the input stimulus from waveform generator W1 such that the amplitude of W1 is approximately the same as the signal amplitude seen at V\ :sub:`DS`.. This is done to more easily view the waveform generator W1 signal, given the rather small signal that will appear at the gate of the transistor, V\ :sub:`GS`. The attenuated W1 signal is AC coupled into the gate of the transistor with 4.7 uF C\ :sub:`1`\ so as not to disturb the DC bias condition.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Common source amplifier test configuration


Hardware Setup:
---------------

The waveform generator W1 should be configured for a 1 KHz Sine wave with 3 volt amplitude peak-to-peak and 0 volt offset. The setup should be configured with scope channel 1+ connected to display the output W1. Scope channel 2 (2+) is used to measure alternately the waveform at the gate and drain of M\ :sub:`1`.


|image1|

.. container:: centeralign

   Figure 2 Common source amplifier test configuration breadboard connection


Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Common source amplifier test circuit, Scopy plot


The voltage gain, A, of the common source amplifier can be expressed as the ratio of load resistor R\ :sub:`L` to the small signal source resistance r\ :sub:`s`. The transconductance, g\ :sub:`m`, of the transistor is a function of the drain current I\ :sub:`D` and the so called gate overdrive voltage, V\ :sub:`GS`-V\ :sub:`th` where V\ :sub:`th` is the threshold voltage.

|image2| (1)

The small signal source resistance is 1/g\ :sub:`m` and can be viewed as being in series with the source. Now with a signal applied to the gate the same current flows in r\ :sub:`s` and the drain load R\ :sub:`L`. Thus the gain A is given by R\ :sub:`L` times g\ :sub:`m`.

|image3| (2)

Adding source degeneration
==========================

Objective:
----------

The purpose of this activity is to investigate effect of the addition of source degeneration.

Additional Materials:
---------------------

1 - 5KΩ Variable resistor, potentiometer

.. _directions-1:

Directions:
-----------

Disconnect the source of M\ :sub:`1` from ground and insert R\ :sub:`S`, a 5KΩ potentiometer, as shown in the following diagram. Adjust R\ :sub:`S` while noting the output signal seen at the drain of the transistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Source degeneration added


.. _hardware-setup-1:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf5.png
   :align: center

.. container:: centeralign

   Figure 5 Source degeneration added, breadboard connection


.. _procedure-1:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 Source degeneration added, Scopy plot


Questions:
----------

What effect does adding R\ :sub:`S` have to the DC operating point of the circuit and how much would you need to adjust R\ :sub:`pot` to return the circuit to the same DC bias (I\ :sub:`D`) you had in figure 1?

What is the effect on the voltage gain, A, by increasing R\ :sub:`S`? Write down the new gain equation similar to equation (2) above.

Source degeneration gain equation:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_e3.png
   :align: center
   :width: 100px

Increasing AC gain of source degenerated amplifier
==================================================

Adding the source degeneration resistor has improved the stability of the DC operating point at the cost decreased amplifier gain. A higher gain for AC signals can be restored to some extent by adding capacitor C\ :sub:`2`\ across the degeneration resistor R\ :sub:`S` as shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7 C\ :sub:`2` added to increase AC gain


.. _hardware-setup-2:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf8.png
   :align: center

.. container:: centeralign

   Figure 8 C\ :sub:`2` added, breadboard connection


.. _procedure-2:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 C\ :sub:`2` added, Scopy plot


Self-biased configuration with negative feedback
================================================

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 Self Biased configuration


.. _hardware-setup-3:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf11.png
   :align: center

.. container:: centeralign

   Figure 11 Self Biased configuration, breadboard connection


.. _procedure-3:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 12 Self Biased configuration, Scopy plot


.. _questions-1:

Questions:
----------

How does adding negative feedback help to stabilize the DC operating point?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/comm_source_amp_bb`
   -  LTspice files: :git-education_tools:`comm_source_amp_ltspice <m2k/ltspice/common_source_amp_ltspice>`
   


References for further reading:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://en.wikipedia.org/wiki/Common_source_amplifier

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_nf2.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_e1.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a5m_e2.png
   :width: 100px
