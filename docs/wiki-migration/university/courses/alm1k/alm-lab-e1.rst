Activity E1: Rechargeable Batteries, For ADALM1000
==================================================

Objective:
----------

This activity will explore the most important electrical and physical characteristics of two of the most popular chemistries used in rechargeable batteries: Nickel-Cadmium (Ni-Cd) and Nickel Metal-Hydride (Ni-MH).

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Definitions of Terms, we need to define some of the terminology surrounding batteries: A Primary battery such an a common 1.5 V Alkaline AA cell is not rechargeable. A Secondary battery is rechargeable. Examples are, the lead-acid battery used in a car, Nickel-Cadmium (Ni-Cd) and Nickel Metal-Hydride (Ni-MH) cells used in portable electronic devices.

A cell is an electro-chemical device capable of supplying the energy that results from an internal chemical reaction to an external electric circuit. A battery is composed of one or more cells, either parallel or series connected to obtain a required current/voltage capability (batteries comprised of series connected cells are by far the most common).

ESR (Equivalent Series Resistance) is the internal resistance present in any cell that limits the amount of peak current it can deliver. The Amp-hour capacity of a battery (or cell) is its most important figure of merit: it is defined as the amount of current that a battery can deliver for 1 hour before the battery voltage reaches the end-of-life point. The "c" rate is a current that is numerically equal to the A-hr rating of the cell. Charge and discharge currents are typically expressed in fractions or multiples of the c rate.

The MPV (mid-point voltage) is the nominal voltage of the cell, and is the voltage that is measured when the battery has discharged 50% of its total energy. The measured cell voltage at the end of its operating life is called the EODV, which stands for End of Discharge Voltage (some manufacturers refer to this as EOL or End of Life voltage). The gravimetric energy density of a battery is a measure of how much energy a battery contains in comparison to its weight. The volumetric energy density of a battery is a measure of how much energy a battery contains in comparison to its volume.

A constant-voltage charger is a circuit that recharges a battery by sourcing only enough current to force the battery voltage to a fixed value. A constant-current charger is a circuit that charges a battery by sourcing a fixed current into the battery, regardless of battery voltage.

Electrical model of a battery.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We know that an ideal voltage source will produce a constant output voltage independent of the current supplied to the load, i.e. whatever current is needed to maintain the voltage at a constant value. However, real world voltage sources can only supply current up to some limit. The power supplies built into the M1000 lab hardware, for example, use active circuitry to maintain the output voltage at a constant value but only for load currents of < 200 mA. A relatively modest current because the board is powered from the computer USB port. Bench top laboratory supplies, powered from the wall socket, can supply much more, often many amps. Similarly, batteries store a finite amount of energy and have a limited current capability depending on the size of the battery. As the current increases the output voltage will begin to drop as the chemical reaction in the battery tries to maintain the current. In most cases this drop in output voltage with increasing load current can be accurately modeled by including a resistor, typically a few ohms at the most, in series with an ideal voltage source, as shown in figure 1. This is the "internal" resistance of the battery, R\ :sub:`int`. This simple model isn't perfect, because as the battery discharges its voltage will drop even without significant loading. But the internal resistance model does capture the characteristics at a given state of battery charge. Since this simple model is the same as a Thevenin equivalent, we can characterize it in the same way, by measuring the open-circuit voltage and short-circuit current. We do not want to damage the battery, so a current limiting resistor ( which also allows us to measure the current ) is added in series with the battery as shown in figure 2. When the output is "short-circuited", this resistor limits the maximum current that will flow.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_labe1_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Equivalent circuit for a real world voltage source (battery).


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard, and jumper wire kit
| 1 NiCd or NiMH rechargeable battery (3 cell type see appendix for suggested sources)
| 1 100 Ω resistor (R\ :sub:`L`)

Directions:
~~~~~~~~~~~

In the parts Kit supplied for this Lab you should have a rechargeable battery ( typically a three cell 3.6V nominal output NiCd or NiMH ). Battery packs like the one shown in figure 1 generally are supplied with wires and a two pin female connector already attached. Add an external 100 Ω resistor in series with the battery as shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_labe1_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 - Characterizing the battery equivalent circuit.


Hardware setup:
~~~~~~~~~~~~~~~

Setup channel A generator for a 5 volt Max and with Min of 0 volt ( 5 V p-p ) with a triangle shape and a frequency of 100 Hz. Current will flow out of the battery (discharge) when the voltage is less than the open circuit battery voltage and will flow into the battery (charge) when the voltage is greater than the open circuit battery voltage.

Procedure:
~~~~~~~~~~

Measure the open-circuit voltage ( when current through the 100 ohm resistor is zero ) and the change in voltage across the battery ( CB-V ) vs. current ( CA-I ) and determine the Thevenin equivalent resistance. Note that if the holder contains two or three cells in series, your answer will be twice or three times the internal resistance of a single cell.

Questions:
~~~~~~~~~~

-   Based on your estimate of the internal resistance, what is the maximum current that the battery could supply? What is the maximum power it could deliver to a load?
-   Measure the internal resistance at different states of charge i.e. when the battery is fully charged, at 50% charge and when it is at the EODV voltage. How does the internal resistance compare at the different amount of charge in the battery? Can you predict the remaining life in a battery based on its internal resistance?
-   Now place a 470 Ω resistor across the terminals of the battery, and record the voltage. In your lab report, discuss whether your measurement is reasonably well predicted by the internal resistance model for the batteries.

**For further reading:**

| :adi:`Battery Chargers <media/en/training-seminars/design-handbooks/Practical-Design-Techniques-Power-Thermal/Section5.pdf>`
| `Rechargeable battery <https://en.wikipedia.org/wiki/Rechargeable_battery>`_
| `Battery Specifications <http://web.mit.edu/evt/summary_battery_specifications.pdf>`_
| :doc:`Electrochemical Impedance Spectroscopy </wiki-migration/university/courses/alm1k/alm-eis-lab>`

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
