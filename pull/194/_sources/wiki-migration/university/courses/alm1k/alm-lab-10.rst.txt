Activity: Shunt regulator - ADALM1000
=====================================

Objective:
----------

The zero gain amplifier (Q\ :sub:`1`, R\ :sub:`2`) and stabilized current source (Q\ :sub:`2`, R\ :sub:`3`) can be used in conjunction with a common emitter amplifier stage (Q\ :sub:`3`) in negative feedback to build a two terminal circuit which provides a constant or regulated output voltage over a range of input currents.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - 2.2 KΩ Resistor (or any similar value)
| 1 - 100 Ω resistor
| 1 - 1K Ω resistor (or similar value)
| 1 - 10 KΩ variable resistor (potentiometer)
| 3 - small signal NPN transistors (2N3904 and SSM2212)

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 1. The output of the channel A voltage generator drives one end of resistor R\ :sub:`4`. Resistors R\ :sub:`1`, R\ :sub:`2` and transistor Q\ :sub:`1` are connected as in previous zero gain amplifier section. Resistor R\ :sub:`3` and transistor Q\ :sub:`2` are added as in the stabilized current source section. If the SSM2212 matched NPN pair is used it is best that it be used for devices Q\ :sub:`1` and Q\ :sub:`2`. Q\ :sub:`3`\ is added with its emitter grounded, its base connected to the collector of Q\ :sub:`2` and collector connected to the combined node of R\ :sub:`1`, R\ :sub:`3` R\ :sub:`4` and channel B scope input CB-H.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab10_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1 Band-gap shunt regulator


Hardware Setup:
~~~~~~~~~~~~~~~

Channel A voltage generator CA-V should be configured for a 100 Hz triangle wave with 5 volt Max and 0 V Min. The channel B scope CB-H in Hi-Z mode is used to measure the regulated output voltage at the collector of Q\ :sub:`3`.

Procedure:
~~~~~~~~~~

Plot the output voltage (as measured at the collector of Q\ :sub:`3`) vs. the input voltage. At what input voltage level does the output voltage stop changing i.e. regulate? This is called the "drop out" voltage. For input voltages above the drop out voltage, how much does the output voltage change for each volt of change at the input? The shunt type of regulator is powered by an input current. As the input voltage changes the current in R\ :sub:`4` changes. Translate the change in voltage across R\ :sub:`4` to the change in current flowing into the shunt regulator. The change in Vout / change in Iin is called line regulation.

The regulated output voltage should be observed as the variable resistor R\ :sub:`3` is adjusted. How does a change in R3 effect the performance of the shunt regulator?

Questions:
~~~~~~~~~~

What affects the regulated output voltage as a load to ground is applied to the output voltage?

What determines or limits the current available to an output load?

Using an NPN transistor array:
------------------------------

The CA3045,46 ( LM3045, 46 ) NPN transistor array is a good alternate choice for building this example circuit. See pinout below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab9_f3.png
   :align: center
   :width: 350px

All the emitters can be tired to ground ( pins 3,7,10,13 ). Devices Q\ :sub:`1`, Q\ :sub:`2` and Q\ :sub:`3` can be connected in parallel and serve as Q\ :sub:`2` in figure 1. Q\ :sub:`4` and Q\ :sub:`5`\ can be used for Q\ :sub:`1` and Q\ :sub:`3`\ in figure 2. The 3 to 1 emitter area ratio will result in an output voltage very nearly 1.2 volts if R\ :sub:`1` and R\ :sub:`3` are both equal to 2K.

**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
