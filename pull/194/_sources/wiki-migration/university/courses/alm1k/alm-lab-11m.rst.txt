Activity: The Source follower (NMOS) - ADALM1000
================================================

Objective:
----------

To investigate the simple NMOS source follower amplifier also sometimes referred to as the common drain configuration.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

NMOS Source Follower:
---------------------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 1.5 KΩ Resistor (R\ :sub:`L`)
| 1 - small signal NMOS transistor (enhancement mode CD4007 or ZVN2110A M\ :sub:`1`)

Directions:
~~~~~~~~~~~

The breadboard connections are shown in figure 1. The output of the channel A generator, is connected to the gate terminal of M\ :sub:`1`. The drain terminal is connected to the positive (+5V) supply. The source terminal is connected to both the 1.5 KΩ load resistor and Scope channel CB-H. The other end of the load resistor is connected to dround.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11m_f1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1 Source Follower


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator should be configured for a 100 Hz Sine wave with 3 volt Max and 2 V Min. The channel B scope in Hi-Z mode CB-H is used to measure the voltage at the source. To measure the input to output error or offset, the CA-V - CB-V Math waveform can be displayed. To measure the input to output gain, the CB-V / CA-V Math waveform can be displayed.

Procedure:
~~~~~~~~~~

The incremental Gain (Vout /Vin) of the source follower should ideally be 1 but will always be slightly less than 1. The gain is generally given by the following equation:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11m_e1.png
   :align: center
   :width: 150px

From the equation we can see that in order to obtain a gain close to one we can either increase R\ :sub:`L` or decrease r\ :sub:`s`. We also know that r\ :sub:`s` is a function of I\ :sub:`D` and that as I\ :sub:`D` increases r\ :sub:`s` decreases. Also from the circuit we can see that I\ :sub:`D` is related to R\ :sub:`L` and that as R\ :sub:`L` increases I\ :sub:`D` decreases. These two effects work counter to each other in the simple resistive loaded source follower. Thus to optimize the gain of the follower we need to explore ways to either decrease r\ :sub:`s` or increase R\ :sub:`L` without effecting the other. It is important to remember that in MOS transistors I\ :sub:`D` = I\ :sub:`S` ( I\ :sub:`G` = 0 ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11m_e2.png
   :align: center
   :width: 400px

where K =μ\ :sub:`n`\ C\ :sub:`ox`/2<sub></sub>and λ can be taken as process technology constants.

Looking at the follower in another way, because of the inherent DC shift due to the transistor's V\ :sub:`th`, the difference between input and output should be constant over the intended swing. Due to the simple resistive load R\ :sub:`L`, the drain current I\ :sub:`D` increases and decreases as the output swings up and down. We know that I\ :sub:`D` is a (square law) function of V\ :sub:`GS`. In this +4V to +2V swing example the minimum I\ :sub:`S` = 2V / 2.2KΩ or 0.91 mA to a maximum I\ :sub:`S` = 4V / 2.2KΩ or 1.82mA. This results in a significant change in V\ :sub:`GS`. This observation leads us to the first possible improvement in the source follower.

The current mirror from activity 6M is now substituted for the source load resistor to fix the amplifier transistor source current. A current mirror will sink a more or less constant current over a wide range of voltages. This more or less constant current flowing in the transistor will result in a more or less constant V\ :sub:`GS`. Viewed another way, the very high output resistance of the current source has effectively increased R\ :sub:`L` while r\ :sub:`s` remains at a low value set by the current.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 1 - 1 KΩ Resistor
| 1 - small signal NMOS transistor (M\ :sub:`1`\ ZVN2110A)
| 2 - small signal NMOS transistors (M\ :sub:`2`, M\ :sub:`3`\ CD4007)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11m_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Improved Source Follower


Source follower output impedance
--------------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

An important aspect of the source follower is to provide power or current gain. That is to say drive a lower resistance (impedance) load from a higher resistance (impedance) stage. Thus it is instructive to measure the source follower output impedance.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 - 4.7 KΩ Resistor
| 1 - 10 KΩ Resistor
| 1 - small signal NMOS transistor ( M\ :sub:`1` CD4007 or ZVN2110A)

.. _directions-1:

Directions:
~~~~~~~~~~~

The circuit configuration in figure 3 adds a resistor R\ :sub:`2` to inject a test signal from AWG1 into the source (output) of M\ :sub:`1`. The input, gate of M\ :sub:`1`, is grounded.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab11m_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 Output impedance test


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator should be configured for a 100 Hz Sine wave with a Min an Max value set so that the voltage swings +/- 1 V around the source of of M\ :sub:`1`, the 2.5 volts at the gate minus V\ :sub:`GS`. This injects a +/- 0.1mA (1V/10KΩ) current into M\ :sub:`1`'s source. Scope input CB-H measures the change in voltage seen at the source.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Plot the measured voltage amplitude seen at the source. The nominal source current in M\ :sub:`1` is (2.5 - V\ :sub:`GS`) / 1.5KΩ. We can calculate r\ :sub:`s`\ from this current as ohms. How does this r\ :sub:`s` compare to the value measured for the potentiometer? Change the value of R\ :sub:`1`\ from 1.5 KΩ to 3.3 KΩ and re-measure the output impedance of the circuit. How has it changed and why?

**For Further Reading:**

http://en.wikipedia.org/wiki/Common_drain

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
