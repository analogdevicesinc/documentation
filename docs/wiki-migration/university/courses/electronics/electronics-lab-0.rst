Activity R1: Real Voltage Sources, For ADALM2000
================================================

Household Batteries:
--------------------

We have said that an ideal voltage source will produce a constant output voltage independent of the current supplied to the load, i.e. whatever current is needed to maintain the voltage at a constant value. However, real world voltage sources can only supply current up to some limit. The power supplies built into the ADALM2000 lab hardware, for example, use active circuitry to maintain the output voltage at a constant value but only for load currents of < 25 mA. A relatively small current because the board is powered from the computer USB port. Bench top laboratory supplies, powered from the wall socket, can supply much more, often many amps. Similarly, batteries store a finite amount of energy and have a limited current capability depending on the size of the battery. As the current increases the output voltage will begin to drop as the chemical reaction in the battery tries to maintain the current. In most cases this drop in output voltage with increasing load current can be accurately modeled by including a resistor, typically a few ohms at the most, in series with an ideal voltage source, as shown in figure 1. This is the "internal" resistance of the battery, R\ :sub:`int`. This simple model isn't perfect, because as the battery discharges its voltage will drop even without significant loading. But the internal resistance model does capture the characteristics at a given state of battery charge. Since this simple model is the same as a Thevenin equivalent, we can characterize it in the same way, by measuring the open-circuit voltage and short-circuit current. We do not want to damage the battery, so a current limitingresistor ( which also allows us to measure the current ) is added in series with the battery as shown in figure 2. When the output is short-circuited, this resistor limits the maximum current that will flow.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a0_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 Equivalent circuit for a real world voltage source (battery).


For this circuit you should have one or more batteries ( AA or AAA ) and a holder for them. Insert the batteries in the holder and add an external 100Ω resistance in series with the batteries as shown in figure 2. The green boxes indicate connections to the ADALM2000 connector. Setup waveform generator 1 for a 5 volt amplitude and with an offset of -1 volt such that it swings from 1.5 volts positive to -3.5 volts negative for the case of a single cell. For two cells in series adjust the offset such that the maximum positive swing is 3 volts or twice the single battery voltage. Measure the open-circuit voltage ( when current through the 100 ohm resistor is zero ) and the drop in voltage across the battery ( scope C1 ) vs. current ( scope C2 /100 ) and determine the Thevenin equivalent resistance. Note that if the holder contains two cells in series, your answer will be twice the internal resistance of a single cell.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a0_f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 - Characterizing the battery equivalent circuit.


-  Based on your estimate of the internal resistance, what is the maximum current that the battery could supply? What is the maximum power it could deliver to a load?
-  If you have access to a "dead" battery try and measure its internal resistance. How does it compare to a "fresh" battery? Can you predict the remaining life in a battery based on its internal resistance?
-   Now place a 510O resistor across the terminals of the batteries, and record the voltage. In your lab report, discuss whether your measurement is reasonably well predicted by the internal resistance model for the batteries.

Extra Credit: Solar Cell
------------------------

For experimenters who finish early or want an extra challenge, obtain a photovoltaic ( solar ) cell from your parts supply room for experimentation. A solar cell is a "real" power source like a battery in the sense that the output current is limited, although of course the output current also depends on the intensity of the light falling on it. Under well-lit conditions, characterize the open-circuit output voltage and the short-circuit current. Then, using various resistors or a potentiometer as a variable load, characterize the output current vs. output voltage characteristic for the solar cell, and export a plot of this characteristic for your report. If you were going to use this cell in an application, what voltage level should you expect for a 10 mA load current?

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
