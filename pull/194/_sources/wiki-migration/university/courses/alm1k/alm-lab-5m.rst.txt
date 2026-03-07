Activity: MOS transistor common source amplifier, For ADALM1000
===============================================================

Objective:
----------

The purpose of this activity is to investigate the common source configuration of the MOS transistor.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| 5 - Resistors
| 1 - 50KΩ Variable resistor, potentiometer
| 1 - small signal NMOS transistor (enhancement mode ZVN2110A or CD4007)

Directions:
~~~~~~~~~~~

The configuration, shown in figure 1, demonstrates the NMOS transistor used as a common source amplifier. Output load resistor R\ :sub:`L` is chosen such that, for the desired nominal drain current I\ :sub:`D`, the voltage appearing at V\ :sub:`DS` is approximately half way between +5 V and ground (2.5 volts). Adjustable resistor Rpot sets the nominal bias operating point for the transistor (V\ :sub:`GS`) to set the required I\ :sub:`D`. Voltage divider R\ :sub:`1`/R\ :sub:`2` is chosen to provide a sufficiently large attenuation of the input stimulus from the channel A generator, CA-V, such that the amplitude is approximately the same as the signal amplitude seen at V\ :sub:`DS`.. This is done to more easily view the channel A generator signal, given the rather small signal that will appear at the gate of the transistor, V\ :sub:`GS`. The attenuated CA-V signal is AC coupled into the gate of the transistor with 4.7 uF C\ :sub:`1`\ so as not to disturb the DC bias condition.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Common source amplifier test configuration


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator CA-V should be configured for a 1 KHz Sine wave with 3 volt Max and 0 volt Min ( 3 V p-p). Scope input channel CB-H is used to measure alternately the waveform at the gate and drain of M\ :sub:`1`.

Procedure:
~~~~~~~~~~

The voltage gain, A, of the common source amplifier can be expressed as the ratio of load resistor R\ :sub:`L` to the small signal source resistance r\ :sub:`s`. The transconductance, g\ :sub:`m`, of the transistor is a function of the drain current I\ :sub:`D` and the so called gate overdrive voltage, V\ :sub:`GS`-V\ :sub:`th` where V\ :sub:`th` is the threshold voltage.


|image1|

.. container:: centeralign

   (1)


The small signal source resistance is 1/g\ :sub:`m` and can be viewed as being in series with the source. Now with a signal applied to the gate the same current flows in r\ :sub:`s` and the drain load R\ :sub:`L`. Thus the gain A is given by R\ :sub:`L` times g\ :sub:`m`.



|image2|

.. container:: centeralign

   (2)


Self-biased configuration with negative feedback.
-------------------------------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

The purpose of this activity is to investigate effect of including negative feedback on the stability of the DC operating point.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Self Biased configuration


Questions:
~~~~~~~~~~

How does adding negative feedback help to stabilize the DC operating point? Adding source degeneration

.. _objective-2:

Objective:
~~~~~~~~~~

The purpose of this activity is to investigate effect of the addition of source degeneration.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

1 - 5KΩ Variable resistor, potentiometer

.. _directions-1:

Directions:
~~~~~~~~~~~

Disconnect the source of M\ :sub:`1` from ground and insert R\ :sub:`S`, a 5KΩ potentiometer, as shown in the following diagram. Adjust R\ :sub:`S` while noting the output signal seen at the drain of the transistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Source degeneration added


.. _questions-1:

Questions:
~~~~~~~~~~

What effect does adding R\ :sub:`S` have to the DC operating point of the circuit and how much would you need to adjust R\ :sub:`pot` to return the circuit to the same DC bias (I\ :sub:`D`) you had in figure 1?

What is the effect on the voltage gain, A, by increasing R\ :sub:`S`? Write down the new gain equation similar to equation (2) above.

| Source degeneration gain equation:
| |image3|

Increasing AC gain of source degenerated amplifier
--------------------------------------------------

Adding the source degeneration resistor has improved the stability of the DC operating point at the cost decreased amplifier gain. A higher gain for AC signals can be restored to some extent by adding capacitor C\ :sub:`2`\ across the degeneration resistor R\ :sub:`S` as shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 C\ :sub:`2` added to increase AC gain


**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/common_source_amp_ltspice`
-  Fritzing files: :git-education_tools:`common_source_amp_bb <m1k/fritzing/comm_source_amp_bb>`

**For Further Reading:**

http://en.wikipedia.org/wiki/Common_source_amplifier

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_e1.png
   :width: 170px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_e2.png
   :width: 160px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5m_e3.png
   :width: 170px
