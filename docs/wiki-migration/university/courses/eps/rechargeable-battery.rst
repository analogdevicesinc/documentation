Activity: Rechargeable Batteries
================================

Objectives:
-----------

This activity will explore the most important electrical and physical characteristics of two of the most popular chemistries used in rechargeable batteries: Nickel-Cadmium (Ni-Cd) and Nickel Metal-Hydride (Ni-MH).

Background:
-----------

Definitions of Terms, we need to define some of the terminology surrounding batteries: A Primary battery such an a common 1.5V Alkaline AA cell is not rechargeable. A Secondary battery is rechargeable. Examples are, the lead-acid battery used in a car, Nickel-Cadmium (Ni-Cd) and Nickel Metal-Hydride (Ni-MH) cells used in portable electronic devices.

A cell is an electro-chemical device capable of supplying the energy that results from an internal chemical reaction to an external electric circuit. A battery is composed of one or more cells, either parallel or series connected to obtain a required current/voltage capability (batteries comprised of series connected cells are by far the most common).

ESR (Equivalent Series Resistance) is the internal resistance present in any cell that limits the amount of peak current it can deliver. The Amp-hour capacity of a battery (or cell) is its most important figure of merit: it is defined as the amount of current that a battery can deliver for 1 hour before the battery voltage reaches the end-of-life point. The "c" rate is a current that is numerically equal to the A-hr rating of the cell. Charge and discharge currents are typically expressed in fractions or multiples of the c rate.

The MPV (mid-point voltage) is the nominal voltage of the cell, and is the voltage that is measured when the battery has discharged 50% of its total energy. The measured cell voltage at the end of its operating life is called the EODV, which stands for End of Discharge Voltage (some manufacturers refer to this as EOL or End of Life voltage).

The gravimetric energy density of a battery is a measure of how much energy a battery contains in comparison to its weight. The volumetric energy density of a battery is a measure of how much energy a battery contains in comparison to its volume.

A constant-voltage charger is a circuit that recharges a battery by sourcing only enough current to force the battery voltage to a fixed value. A constant-current charger is a circuit that charges a battery by sourcing a fixed current into the battery, regardless of battery voltage.

Electrical model of a battery.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We know that an ideal voltage source will produce a constant output voltage independent of the current supplied to the load, i.e. whatever current is needed to maintain the voltage at a constant value. However, real world voltage sources can only supply current up to some limit. The power supplies built into the Discovery lab hardware, for example, use active circuitry to maintain the output voltage at a constant value but only for load currents of < 25 mA. A relatively small current because the board is powered from the computer USB port. Bench top laboratory supplies, powered from the wall socket, can supply much more, often many amps. Similarly, batteries store a finite amount of energy and have a limited current capability depending on the size of the battery. As the current increases the output voltage will begin to drop as the chemical reaction in the battery tries to maintain the current. In most cases this drop in output voltage with increasing load current can be accurately modeled by including a resistor, typically a few ohms at the most, in series with an ideal voltage source, as shown in figure 1. This is the "internal" resistance of the battery, R\ :sub:`int`. This simple model isn't perfect, because as the battery discharges its voltage will drop even without significant loading. But the internal resistance model does capture the characteristics at a given state of battery charge. Since this simple model is the same as a Thevenin equivalent, we can characterize it in the same way, by measuring the open-circuit voltage and short-circuit current. We do not want to damage the battery, so a current limiting resistor ( which also allows us to measure the current ) is added in series with the battery as shown in figure 2. When the output is short-circuited, this resistor limits the maximum current that will flow.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_recharg-battery-f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1 Equivalent circuit for a real world voltage source (battery).


Materials:
----------

| Analog Discovery Lab hardware
| Solder-less breadboard, and jumper wire kit
| 1 NiCd or NiMH rechargeable battery (3 cell type see appendix for suggested sources)
| 1 100 Ω resistor (R\ :sub:`L`)

Directions:
-----------

In your parts for the EPS hardware module you should have a rechargeable battery ( a three cell 3.6V nominal output NiCd or NiMH ). Battery packs like the one shown in figure 1 generally are supplied with wires and a two pin female connector already attached. Add an external 100 Ω resistance in series with the battery as shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_recharg-battery-f2.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 2 - Characterizing the battery equivalent circuit.


Hardware setup:
---------------

Setup waveform generator 1 for a 2.5 volt amplitude ( 5 V p-p ) and with an offset of -1 volt such that it swings from 1.5 volts positive to -3.5 volts negative for the case of a single cell. For two cells in series adjust the offset such that the maximum positive swing is 3 volts or twice the single battery voltage.

Procedure:
----------

Measure the open-circuit voltage ( when current through the 100 ohm resistor is zero ) and the drop in voltage across the battery ( scope C1 ) vs. current ( scope C2 /100 ) and determine the Thevenin equivalent resistance. Note that if the holder contains two cells in series, your answer will be twice the internal resistance of a single cell.

Questions:
----------

-   Based on your estimate of the internal resistance, what is the maximum current that the battery could supply? What is the maximum power it could deliver to a load?
-   Measure the internal resistance at different states of charge i.e. when the battery is fully charged, at 50% charge and when it is at the EODV voltage. How does the internal resistance compare at the different amount of charge in the battery? Can you predict the remaining life in a battery based on its internal resistance?
-   Now place a 510Ω resistor across the terminals of the battery, and record the voltage. In your lab report, discuss whether your measurement is reasonably well predicted by the internal resistance model for the batteries.

**For further reading:**

| http:*www.analog.com/static/imported-files/tutorials/ptmsect5.pdf
  http:*\ en.wikipedia.org/wiki/Rechargeable_battery
| http://web.mit.edu/evt/summary_battery_specifications.pdf

**Return to EPS Activity** :doc:`Table of Contents </wiki-migration/university/courses/eps/main-page>`\ **.**
