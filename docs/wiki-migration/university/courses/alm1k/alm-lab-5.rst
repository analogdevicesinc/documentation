Activity: Common Emitter Amplifier, For ADALM1000
=================================================

Objective:
----------

The purpose of this activity is to investigate the common emitter configuration using the BJT device.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Simple Common Emitter Amplifier
-------------------------------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| 4 - Resistors
| 1 - 50 KΩ Variable resistor, potentiometer
| 1 - small signal NPN transistor (2N3904)

Directions:
~~~~~~~~~~~

The configuration, shown in figure 1, demonstrates the NPN transistor used as a common emitter amplifier. Output load resistor R\ :sub:`L` is chosen such that for the desired nominal collector current I\ :sub:`C`, approximately one half of the +5 V voltage (2.5 V) appears at V\ :sub:`CE`. Adjustable resistor Rpot along with Rb sets the nominal bias operating point for the transistor (I\ :sub:`B`) to set the required I\ :sub:`C`. Voltage divider R\ :sub:`1`/R\ :sub:`2` is chosen to provide a sufficiently large attenuation of the input stimulus from waveform generator channel A. This is done to more easily view the channel A generator signal, given the rather small signal that will appear at the base of the transistor, V\ :sub:`BE`. The attenuated CA-V generator signal is AC coupled into the base of the transistor by the 4.7 uF capacitor so as not to disturb the DC bias condition.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Common emitter amplifier configuration


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A waveform generator output CA-V should be configured for a 1 KHz sine wave with 3 volt Max and 0 volt Min (3 V p-p). Scope channel CB-H is used to measure alternately the waveform at the base and collector of Q\ :sub:`1`.

Procedure:
~~~~~~~~~~

The voltage gain, A, of the common emitter amplifier can be expressed as the ratio of load resistor R\ :sub:`L` to the small signal emitter resistance r\ :sub:`e`. The transconductance, g\ :sub:`m`, of the transistor is a function of the collector current I\ :sub:`C` and the so called thermal voltage, kT/q which can be approximated by around 25 mV or 26 mV at room temperature.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5_e1.png
   :align: center
   :width: 170px

The small signal emitter resistance is 1/g\ :sub:`m` and can be viewed as being in series with the emitter. Now with a signal applied to the base the same current (neglecting base current) flows in r\ :sub:`e` and the collector load R\ :sub:`L`. Thus the gain A is given by the ratio of R\ :sub:`L` to r\ :sub:`e`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5_e2.png
   :align: center
   :width: 200px

Self-biased configuration with negative feedback.
-------------------------------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

The purpose of this section is to investigate effect of adding negative feedback to stabilize the DC operating point.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Self Biased configuration


Questions:
~~~~~~~~~~

How does adding negative feedback help to stabilize the DC operating point

Adding emitter degeneration
---------------------------

.. _objective-2:

Objective:
~~~~~~~~~~

The purpose of this section is to investigate effect of the addition of emitter degeneration.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

1 - 5KΩ Variable resistor, potentiometer (500Ω if one is available)

.. _directions-1:

Directions:
~~~~~~~~~~~

Disconnect the emitter of Q\ :sub:`1` from ground and insert R\ :sub:`E`, a 5KΩ potentiometer, as shown in the following diagram. Adjust R\ :sub:`E` while noting the output signal seen at the collector of the transistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Emitter degeneration added


.. _questions-1:

Questions:
~~~~~~~~~~

What effect does adding R\ :sub:`E` have to the DC operating point of the circuit and how much would you need to adjust R\ :sub:`pot` to return the circuit to the same DC bias (I\ :sub:`C`) you had in figure 1?

What is the effect on the voltage gain, A, by increasing R\ :sub:`E`?

Increasing the AC gain of emitter degenerated amplifier
-------------------------------------------------------

Adding the emitter degeneration resistor has improved the stability of the DC operating point at the cost decreased amplifier gain. A higher gain for AC signals can be restored to some extent by adding capacitor C\ :sub:`2`\ across the degeneration resistor R\ :sub:`E` as shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab5_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 C\ :sub:`2` added to increase AC gain


**Resources:**

-  LTSpice files: `comm_emit_amp_ltspice <https://wiki.analog.com/https/analogdevicesinc.github.io/downgit/>`_
-  Fritzing files: `comm_emit_amp_bb <https://wiki.analog.com/https/analogdevicesinc.github.io/downgit/>`_

**For Further Reading:**

http://en.wikipedia.org/wiki/Common_emitter_amplifier

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
