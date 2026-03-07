Activity: The Source follower (NMOS) - ADALM2000
================================================

Objective:
----------

To investigate the simple NMOS source follower amplifier also sometimes referred to as the common drain configuration.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 2.2KΩ Resistor (R\ :sub:`L`)
| 1 - small signal NMOS transistor (enhancement mode CD4007 or ZVN2110A M\ :sub:`1`)

Directions:
-----------

The breadboard connections are shown in the diagram below. The output of the waveform generator, W1, is connected to the gate terminal of M\ :sub:`1`. Scope input 1+ (Single Ended) is also connected to W1 output. The drain terminal is connected to the positive (Vp) supply. The source terminal is connected to both the 2.2KΩ load resistor and Scope input 2+ (Single Ended). The other end of the load resistor is connected to the negative (Vn) supply. To measure the input to output error, channel 2 of the scope can be used differentially by connecting 2+ to the gate of M\ :sub:`1` and 2- to the source.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11m_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 Source Follower


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/mos_src_flw-bb.png

.. container:: centeralign

   Figure 2 Source Follower Breadboard Circuit


The waveform generator should be configured for a 1 KHz Sine wave with 4 volt amplitude peak-to-peak and 0 offset. The Single ended input of scope channel 2 (2+) is used to measure the voltage at the source. The Scope configured with channel 1+ connected to display the AWG generator output. When measuring the input to output error, channel 2 of the scope should be connected to display 2+ and 2- differential.

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/mos_src_flw-wav.png

.. container:: centeralign

   Figure 3 Input, output waveforms


The incremental Gain (Vout /Vin) of the source follower should ideally be 1 but will always be slightly less than 1. The gain is generally given by the following equation:

From the equation we can see that in order to obtain a gain close to one we can either increase R\ :sub:`L` or decrease r\ :sub:`s`. We also know that r\ :sub:`s` is a function of I\ :sub:`D` and that as I\ :sub:`D` increases r\ :sub:`s` decreases. Also from the circuit we can see that I\ :sub:`D` is related to R\ :sub:`L` and that as R\ :sub:`L` increases I\ :sub:`D` decreases. These two effects work counter to each other in the simple resistive loaded source follower. Thus to optimize the gain of the follower we need to explore ways to either decrease r\ :sub:`s` or increase R\ :sub:`L` without effecting the other. It is important to remember that in MOS transistors I\ :sub:`D` = I\ :sub:`S` ( I\ :sub:`G` = 0 ).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11m_e1.png
   :align: center
   :width: 100px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11m_e2.png
   :align: center
   :width: 250px

where K = μ\ :sub:`n`\ C\ :sub:`ox`/2<sub></sub> and λ can be taken as process technology constants.

Looking at the follower in another way, because of the inherent DC shift due to the transistor's V\ :sub:`th`, the difference between input and output should be constant over the intended swing. Due to the simple resistive load R\ :sub:`L`, the drain current I\ :sub:`D` increases and decreases as the output swings up and down. We know that I\ :sub:`D` is a (square law) function of V\ :sub:`GS` In this +2V to -2V swing example the minimum I\ :sub:`D`\ =2V/2.2KΩ or 0.91 mA to a maximum I\ :sub:`D`\ = 6V/2.2KΩ or 2.7mA. This results in a significant change in V\ :sub:`GS`. This observation leads us to the first possible improvement in the source follower.

The current mirror from activity 6M is now substituted for the source load resistor to fix the amplifier transistor source current. A current mirror will sink a more or less constant current over a wide range of voltages. This more or less constant current flowing in the transistor will result in a more or less constant V\ :sub:`GS`. Viewed another way, the very high output resistance of the current source has effectively increased R\ :sub:`L` while r\ :sub:`s` remains at a low value set by the current.

Additional Materials:
---------------------

| 1 - 3.2KΩ Resistor (use a 1KΩ in series with a 2.2KΩ)
| 1 - small signal NMOS transistor (M\ :sub:`1`\ ZVN2110A)
| 2 - small signal NMOS transistors (M\ :sub:`2`, M\ :sub:`3`\ CD4007)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Improved Source Follower


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/imp_mos_src_flw-bb.png

.. container:: centeralign

   Figure 5 Improved Source Follower Breadboard Circuit


.. _procedure-1:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/imp_mos_src_flw-wav.png

.. container:: centeralign

   Figure 6 Improved Source Follower Waveform


Source follower output impedance
================================

.. _objective-1:

Objective:
----------

An important aspect of the source follower is to provide power or current gain. That is to say drive a lower resistance (impedance) load from a higher resistance (impedance) stage. Thus it is instructive to measure the source follower output impedance.

.. _materials-1:

Materials:
----------

| 1 - 4.7KΩ Resistor
| 1 - 10KΩ Resistor
| 1 - small signal NMOS transistor ( M\ :sub:`1` CD4007 or ZVN2110A)

.. _directions-1:

Directions:
-----------

The circuit configuration below adds a resistor R\ :sub:`2` to inject a test signal from AWG1 into the emitter (output) of M\ :sub:`1`. The input, base of M\ :sub:`1`, is grounded.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11m_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7 Output impedance test


.. _hardware-setup-2:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/mos_out_imp_test-bb.png

.. container:: centeralign

   Figure 8 Output Impedance Test Breadboard Circuit


The waveform generator should be configured for a 1 KHz Sine wave with 2 volt amplitude peak-to-peak with the offset set equal to minus the V\ :sub:`GS` of M\ :sub:`1` ( approximately -V ). This injects a +/- 0.1mA (1V/10KΩ) current into M\ :sub:`1`'s source. Scope input 2+ measures the change in voltage seen at the source.

.. _procedure-2:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/mos_out_imp_test-wav.png

.. container:: centeralign

   Figure 9 Output Impedance Test Waveform


Plot the measured voltage amplitude seen at the source. The nominal source current in M\ :sub:`1` is (Vn - V\ :sub:`GS`) / 4.7KΩ or 720uA. We can calculate r\ :sub:`s`\ from this current as ohms. How does this r\ :sub:`s` compare to the from the test data? Change the value of R\ :sub:`1` from 4.7 KΩ to 2.2 KΩ and re-measure the output impedance of the circuit. How has it changed and why?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: `mos_source_follower_bb <https://wiki.analog.com/https/minhaskamal.github.io/downgit/>`_
   -  LTSpice files: `mos_source_follower_ltspice <https://wiki.analog.com/https/minhaskamal.github.io/downgit/>`_
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
