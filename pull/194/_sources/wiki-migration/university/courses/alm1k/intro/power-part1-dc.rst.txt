Activity: Power in DC circuits - ADALM1000
==========================================

Objective:
----------

In this activity, the characteristics of power in DC circuits will be investigated.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 (M1k) connector and configuring the hardware. The green shaded rectangles indicate connections to the M1k analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background: DC Power
--------------------

A large amount of time is spent measuring voltage and current in electrical engineering. These parameters are important for characterizing how a circuit behaves. However, in terms of what it ‘costs’ to operate a circuit, we must look at the power. For any circuit component, we can define power using the relationship:

:math:`P = V \times I`

This equation is valid for all components. For DC circuits (constant sources), it becomes a relatively simple matter of identifying the voltage across and current through the component to determine power. From physics, we also know that any power produced must be equal to the power that is consumed. Typically, in circuits, sources produce power and passive components like resistors, capacitors and inductors consume (dissipate as heat or temporarily store) power.

(Note, a source might not always be a power producer and can sometimes consume power. For example, consider a rechargeable battery while it is charging.)

The ADALP2000 parts kit contains a number of 1/8W resistors (125 mW). What's the smallest value of resistance that can take the full 5V output of the ADALM1000 voltage sources without exceeding this power dissipation?

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless Breadboard
| Jumper wires
| Various Resistors

Procedure:
----------

To better understand power, analyze the familiar voltage divider circuit as shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-power-part1-dc-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, The two resistor voltage divider.


Start with load resistor R\ :sub:`L` = 1kΩ, measure the voltage across source resistor R\ :sub:`s` and R\ :sub:`L`. Use Ohm’s Law to calculate the current through each resistor (the current should be the same because the resistors are in series). Using the power equation, calculate the power consumed by each resistor. Calculate the power produced (delivered) by the source. Remember the source has the same current as the resistors. Does the power produced equal the power consumed?

Repeat your power calculations for R\ :sub:`L` = 68Ω, 100Ω, 470Ω, 2.2kΩ, 4.7kΩ, and 10kΩ. Build a table of your calculated values. Plot the power consumed by the load resistor (on the y-axis), P\ :sub:`RL`, against the load resistance (on the x-axis), R\ :sub:`L`.

**Note:** If you use the ALICE DC Meter-Source Tool to measure the voltages it will also measure the current in the channel A DC source as well as the power. How well do these measurements line up with the currents and power you calculated in your plot?

A constant source in series with a constant source resistance, R\ :sub:`s`, with a variable load, R\ :sub:`L`, is a classic circuit when trying to maximize power to a load. Based on your power vs load resistance plot, what relationship exists between the load resistor and the source resistor, R\ :sub:`s`, such that power to the load is maximized?

Two Source Experiment
---------------------

In a previous activity on superposition, we investigated the circuit in figure 2 for circuits with multiple voltage sources. For V\ :sub:`CA` = V\ :sub:`CB` = 2V, find the voltage across each resistor and the current through each resistor. Calculate the power consumed by the resistors in the circuit. With channel B in Split I/O mode you can use the BIN input to measure the voltage at the junction of the three resistors (or use AIN with channel A in Split I/O mode).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-power-part1-dc-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2. Experimental Measurements for a Circuit with Two Sources.


Using series relationships, determine the current through each source and the power produced by the sources. Do this for other combinations like V\ :sub:`CA` = V\ :sub:`CB` = 3V, 4V, 5V. Is the power produced and the power consumed equal?

Again, if you use the ALICE DC Meter-Source Tool it will also measure the current in the channel A and channel B DC sources as well as the power. How well do these measurements line up with the currents and power you calculated?

**For Further Reading:**

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
