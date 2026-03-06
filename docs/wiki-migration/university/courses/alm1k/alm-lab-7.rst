Activity: Zero gain amplifier (BJT) - ADALM1000
===============================================

Objective:
----------

In the design of a circuit it is important to take into account the wide variation in certain device values from one to another. A central objective of the designer is to desensitize the circuit to these variations to produce a circuit which meets the specifications across all possible conditions. One aspect of design which is common to nearly all circuits is the establishment of stable bias or operating point levels. This seemingly minor portion of the design can provide the most challenging and interesting circuit problems. Many bias generators are centered around the generation of currents to operate the core of the circuit. Current generated from simple resistors and diodes or diode connected transistors connected across the power supply will vary approximately proportional to the variation of the supply voltage. This variation in the resulting bias current is frequently undesirable.

This activity is to proceed a current source in Activity 8 which has an output current which had been desensitized to variation in input current. To understand this circuit, it is helpful to examine the behavior of a "zero-gain amplifier" first.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| Analog Discovery Lab hardware
| Solder-less breadboard
| 1 - 2.2 KΩ Resistor (or any similar value)
| 1 - 47 Ω Resistor
| 1 - small signal NPN transistor (2N3904 or SSM2212)

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 1. The channel A generator CA-V output drives one end of resistor R\ :sub:`1`. Resistor R\ :sub:`2` is connected between the base and collector of transistor Q\ :sub:`1` with the other end of resistor R\ :sub:`1` connected to the base as well. The emitter of Q\ :sub:`1`\ is grounded.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab7_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Zero Gain Amplifier


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3.0 volt Max and 0V Min. The input of scope channel B, CB-H is used to measure alternately the base and collector voltage of Q\ :sub:`1`.

Procedure:
~~~~~~~~~~

Remembering back to the common emitter amplifier in the previous section, if R\ :sub:`L` is set equal to r\ :sub:`e` then the gain A will be -1. If the base is connected to the top of resistor R\ :sub:`L`\ then the gain from the base to the collector (bottom of R\ :sub:`L`) will be -1. Also, neglecting the collector emitter output impedance of the transistor the gain from the top of load resistor R\ :sub:`L` to the collector (bottom of R\ :sub:`L`) will be +1. Thus the net gain superimposing both paths will be 1 - 1 = 0.

Questions:
~~~~~~~~~~

What are the relative gains of the two paths when the collector current is less than and greater than the "ideal" zero gain value?

Improved V_BE Multiplier, Applying the Zero Gain Concept
--------------------------------------------------------

As we explored in Activity 3, there are often circuits which require that a voltage greater than 1 V\ :sub:`BE` be generated. Here we explore in more detail three additional ways to accomplish this.

V_BE times 2 version 1:
~~~~~~~~~~~~~~~~~~~~~~~

The obviously simple thing to do would be to just use two diode connected transistors in series.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 - 1KΩ Resistor
| 2 - small signal NPN transistor (2N3904 or SSM2212)

.. _directions-1:

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 2. The output of the channel A generator drives one end of resistor R\ :sub:`1`. The emitter of Q\ :sub:`1` is connected to ground. The base and collector of Q\ :sub:`1` are connected to the emitter of Q\ :sub:`2`. The base and collector of Q\ :sub:`2`\ are connected to the other end of R\ :sub:`1` and to the scope channel B, CB-H.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab7_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 2 V\ :sub:`BE` circuit


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3.0 volt Max and 0V Min. Both channels vertical range can be set to 0.2 V per division.

.. _procedure-1:

Procedure:
~~~~~~~~~~

You should also confirm that the voltage characteristic measured at the collector, base of transistor Q\ :sub:`1` is the same as was measured in activity 3.

V_BE times 2 version 2:
-----------------------

A second option would be to use two resistors as a voltage divider. This could produce an output that is the addition of fractions of a V\ :sub:`BE` to the V\ :sub:`BE` of Q\ :sub:`1`.

.. _materials-2:

Materials:
~~~~~~~~~~

| 1 - 1KΩ Resistor
| 2 - 10KΩ Resistors
| 1 - 5KΩ Variable resistor ( a 500Ω pot would be preferable if available )
| 1 - small signal NPN transistor (2N3904 or SSM2212)

.. _directions-2:

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 3. The output of the channel A generator drives one end of resistor R\ :sub:`1`. The emitter of Q\ :sub:`1` is connected to ground. Resistor R\ :sub:`3` is connected between the base of Q\ :sub:`1` and ground. One end of resistor R\ :sub:`2` connected to the other end of R\ :sub:`1` and to the 2- input of scope channel 2 and one end and the wiper of potentiometer R\ :sub:`4`. The opposite end of R\ :sub:`2` is connected to the base of Q\ :sub:`1`. The collector of Q\ :sub:`2` is connected to the remaining end of R\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab7_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 V\ :sub:`BE` Multiplier circuit


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3 volt Max and 0V Min. Both vertical ranges can be set to 0.2 V per division.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Start out with variable resistor R\ :sub:`4` set to its minimum value of nearly zero ohms. Observe the voltage vs. current characteristics of this configuration compared to version 1. There is a small extra current that flows in the two 10 KΩ resistors before the transistor turns on. The voltage at 1mA is slightly higher and the slope of the curve is not as steep.

Let's apply the concept of the zero gain amplifier. Now adjust R\ :sub:`4` and observe the slope of the curve change. At what value of R\ :sub:`4` is the curve nearly vertical? Why is that value the correct value for "zero" gain?

V_BE times 2 version 3:
-----------------------

A minor variation on Version 2.

.. _materials-3:

Materials:
~~~~~~~~~~

| 1 - 1KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - 5KΩ Variable resistor ( 500Ω pot would be preferable if available )
| 2 - small signal NPN transistor (2N3904 or SSM2212)

.. _directions-3:

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 4. Version 3 is made from version 2 by removing 10 KΩ resistor R\ :sub:`2` and replacing it with diode connected NPN Q\ :sub:`2` as shown.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab7_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Version 3 of V\ :sub:`BE` multiplier


.. _hardware-setup-3:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3.0 volt Max and 0V Min. Both vertical ranges can be set to 0.2 V per division.

.. _procedure-3:

Procedure:
~~~~~~~~~~

Again start out with variable resistor R\ :sub:`4` set to its minimum value of nearly zero ohms. Observe the voltage vs. current characteristics of this configuration compared to version 2. There is a small extra current that flows in the one 10 KΩ resistors after Q\ :sub:`1` turns on and until both Q\ :sub:`1` and Q\ :sub:`2` are on. The voltage at 1 mA is slightly lower and the slope of the curve is steeper more like version 1.

Again, let's apply the concept of the zero gain amplifier. Now adjust R\ :sub:`4` and observe the slope of the curve change. At what value of R\ :sub:`4` is the curve nearly vertical? Why is that value the correct value for "zero" gain?

Optional extra credit problem:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How would you modify the values of R\ :sub:`2` and R\ :sub:`4` in version 2 ( figure 3 ) to produce a stabilized 1.0 volt output?

**For Further Reading:**

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
