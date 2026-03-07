Activity: Real Voltage Sources, For ADALM1000
=============================================

Objective:
----------

This activity will explore the most important electrical and physical characteristics of common chemical batteries.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Household Batteries:
~~~~~~~~~~~~~~~~~~~~

We have said that an ideal voltage source will produce a constant output voltage independent of the current supplied to the load, i.e. whatever current is needed to maintain the voltage at a constant value. However, real world voltage sources can only supply current up to some limit. The power supplies built into the ADALM1000 hardware, for example, use active circuitry to maintain the output voltage at a constant value but only for load currents of +/- 200 mA. This is a relatively small current because the board is powered from the computer USB port. Bench top laboratory supplies, powered from the wall socket, can supply much more, often many amps. Similarly, batteries store a finite amount of energy and have a limited current capability depending on the size of the battery. As the current increases the output voltage will begin to drop as the chemical reaction in the battery tries to maintain the current. In most cases this drop in output voltage with increasing load current can be accurately modeled by including a resistor, typically a few ohms at the most, in series with an ideal voltage source, as shown in figure 1. This is the “internal” resistance of the battery, R\ :sub:`int`. This simple model isn’t perfect, because as the battery discharges its voltage will drop even without significant loading. But the internal resistance model does capture the characteristics at a given state of battery charge. Since this simple model is the same as a :doc:`Thévenin equivalent </wiki-migration/university/courses/alm1k/circuits1/alm-cir-4>`, we can characterize it in the same way, by measuring the open-circuit voltage and "short-circuit" current (not actually shorted but using a known load resistance). We do not want to damage the battery, so a current limiting resistor is added in series with the battery as shown in figure 2. When the output is "short-circuited", this resistor limits the maximum current that will flow.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-real-voltage-source-fig1.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 1, Equivalent circuit for a real world voltage source (battery).


You will need one or more batteries (AA or AAA) and a holder for them. Insert the batteries in the holder and add an external 100 Ω resistance in series with the battery as shown in figure 2. Open the Meter – Source tool, figure 3. Turn on Source A with CA-V set for 1.5 nominal for the case of a single cell. For two cells in series adjust the Value such that it is nominally the total battery voltage. Measure the open-circuit voltage (when current through the 100 ohm resistor is zero as measured by CA mA) and the drop in voltage across the battery ( CA-V setting ) while measuring the current (CA mA ) and the voltage across the cell, CB V. Calculate the internal Thevenin equivalent resistance based on the change in the cell voltage and the current. Note that if the holder contains two cells in series, your answer will be twice the internal resistance of a single cell.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-real-voltage-source-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Characterizing the battery equivalent circuit.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-real-voltage-source-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Meter – Source controls.


1. Based on your estimate of the internal resistance, what is the maximum current that the battery could supply? What is the maximum power it could deliver to a load?

2. If you have access to a “dead” discharged battery, try and measure its internal resistance. How does it compare to a “fresh” battery? Can you predict the remaining life in a battery based on its internal resistance?

3. Now place a 470 Ω resistor across the terminals of the batteries, and record the voltage. In your lab report, discuss whether your measurement is reasonably well predicted by the internal resistance model for the battery.

Lemon Battery
-------------

A `lemon battery <https://en.wikipedia.org/wiki/Lemon_battery>`_ is a simple battery often made for the purpose of educational experimentation. Typically, a piece of zinc metal (such as a galvanized nail or screw) and a piece of copper (such as a penny or copper wire) are inserted into a lemon and connected by wires. The typical voltage produced by a lemon battery can be between 0.5 and 0.9 Volts. The energy generated by reaction of the metals can used to power a small device such as a light emitting diode (LED) when enough cells are connected in series.

The lemon battery illustrates the type of chemical reaction (oxidation-reduction) that occurs in batteries. The zinc and copper are called the electrodes, and the acidic juice inside the lemon is called the electrolyte. There are many variations of the lemon cell that use different fruits (or liquids) as electrolytes and metals other than zinc and copper as electrodes. Zinc and copper electrodes are reasonably safe and easy to obtain.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-real-voltage-source-fig4.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 4, Lemon battery construction.


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Jumper wires (wires with alligator clips will work best)
| One or more lemons: large, fresh, "juicy" lemons work best.
| Zinc plated screws or nails
| Copper plated coins or copper nails or heavy gauge (14 or 12) copper wire.
| Red LED

Insert a copper penny into a small cut or push a copper nail or heavy gauge wire into one side of the lemon. Push a galvanized (zinc coated) screw or nail into the other side of the lemon. The zinc and copper electrodes must not touch. This will be a single cell of a battery. The zinc and the copper are called electrodes. The lemon juice is called electrolyte. All batteries have a "+" and "-" terminal. Electric current is a flow of atomic particles called electrons.

Measure the voltage of your single cell using one of the ALM1000 input channels in Hi-Z mode (as a voltmeter). This will not be enough to light an LED. You would probably need at least 3 or 4 lemon cells connected in series to generate enough voltage to light an LED, figure 4.

The quality of the copper and zinc can be a problem for a battery like this. Try substituting a length of 14 or 12 gauge copper wire (common house wire) for the penny. Experiment with different lengths and configurations of electrodes. Other sources of zinc and copper may be found in the plumbing and electrical departments of a hardware store.

Other fruits and vegetables like oranges, grapefruits and potatoes will work as well. Basically anything that contains a mild acid. Try other household items to see how much voltage and current they can produce.

Extra Credit: Solar Cell
------------------------

For experimenters who finish early or want an extra challenge, obtain a photovoltaic (solar) cell from your parts supply room for experimentation. A solar cell is a “real” power source like a battery in the sense that the output current is limited, although of course the output current also depends on the intensity of the light falling on it. Under well-lit conditions, characterize the open-circuit output voltage and the short-circuit current. Then, using various resistors or a potentiometer as a variable load, characterize the output current vs. output voltage characteristic for the solar cell, and export a plot of this characteristic for your report. If you were going to use this cell in an application, what voltage level should you expect for a 10 mA load current?

**For Further Reading:**

https://en.wikipedia.org/wiki/Lemon_battery

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
