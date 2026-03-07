Introduction to RC Circuits
===========================

.. image:: https://wiki.analog.com/_media/analogTV>4800540010001
   :alt: analogTV>4800540010001
   :align: right

Introduction
------------

Resistors, capacitors, and inductors are the basic passive building blocks of many circuits. These elements can be used to control timing and frequency response. In this experiment we will investigate how circuits comprised of resistors and capacitors behave when their voltages and currents are switched. We will watch the voltage increase on a capacitor as it charges over a relatively long period of time, then observe shorter-term effects with a resistor-capacitor (RC) circuit.

Objective
---------

To study how RC circuits behave with switched input voltages. Following completion of this lab you should be able to explain how a capacitor charges when a step voltage is applied to it through a resistor, describe the shape of the voltage across a capacitor when a square voltage wave is applied to it through a resistor, calculate the time constant of a RC circuit and know to what level the capacitor charges in one time constant, determine one of the more commonly-accepted time intervals that it takes to fully charge a capacitor when a step voltage is applied to it through a resistor, observe polarity requirements of electrolytic capacitors, and give a basic explanation of dielectric absorption.

Materials and Apparatus
-----------------------

-  Resistor and capacitor code handouts
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) 100 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 1 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 47 μF capacitor from the ADALP2000 Analog Parts Kit
-  (1) 1 μF capacitor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard; note the polarity of the 47 μF capacitor\


|lab_2_image_1.png|

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Set up the M1K to source voltage/measure current on Channel A and measure voltage on channel B
-  Set up Channel A source waveform for a “Constant” output of 5 V.
-  Connect a wire from Channel A to the unconnected side of the 100 KΩ resistor while monitoring the voltage on Channel B
-  Observe the voltage on Channel B increase slowly
-  Change the output voltage from Channel A to 0 V and measure how long it takes the voltage on Channel B to reach 0 V (theoretically the capacitor voltage never gets to 0 V, but we can get a good estimation within the measurement limitations of the M1K)
-  Construct the following circuit on the solderless breadboard\

|lab_2_image_3.png|

-  Set up Channel A to source a 100 Hz square wave that swings between 0 V and 5 V.
-  Observe the shape of the waveform across the capacitor. Can you describe the general shape of the edges?
-  Increase the frequency of the square wave. What happens to the voltage waveform across the capacitor?

Theory
------

A capacitor is comprised of two conductors, typically called “plates,” separated by an insulating material called a “dielectric.” In electric circuits the capacitors are used in a way in which equal and opposite charges are created on each plate. The charges are created by accumulation or depletion of free electrons in the conductors. The charges produce an electric field in the dielectric, thereby developing a voltage across the plates. For a fixed charge, Q, on the plates, the voltage, V, across the plates is determined by the capacitance value, C, according to the following relationship.

:math:`V = Q/C`

If we want to determine how the voltage and current are related, it is useful to rearrange the equation as follows.

:math:`Q = CV`

Since current is the time derivative of Q, taking the first time derivative of each side - noting that C is constant - produces an expression that relates current to the rate of change of the voltage in a capacitor.

:math:`\displaystyle dQ\frac{t}{dt} = i(t) = CdV\frac{t}{dt}`

This can be written explicitly for the rate of change in voltage.

:math:`\displaystyle dV\frac{t}{dt} = i\frac{t}{C}`

We can use this equation to study the charging of the capacitor. If we had a constant current source, I, the capacitor would charge at a constant rate of I/C volte per second. In the RC circuit, we have a voltage source in series with a resistor instead of a current source. When the 5 V is initially applied to the circuit, it all appears across the resistor because the initially zero voltage across the capacitor cannot change instantaneously (unless, of course, we had an infinite current available). In the first circuit the 5V across the resistor produces a current of 5V/100K amps by Ohm’s law, which begins to charge the capacitor. As the capacitor charges, however, the voltage across the resistor drops by Kirchhoff’s Voltage Law, thereby decreasing the current and the rate of change in capacitor voltage. This process produces an exponential slowing in the rate of increase of the capacitor voltage.

The charging rate in a RC circuit depends on the RC product, which is typically called the “time constant,” represented by the Greek letter tau. In one time constant, a charging capacitor will move 63% of the way from its current voltage to the voltage applied through the resistor. The capacitor voltage, V\ :sub:`C`, in a RC circuit with an applied step voltage of V\ :sub:`T` is governed by the following equation.

:math:`\displaystyle V_C(t) = V_T(1 - e^\frac{-t}{\tau})`

In one time constant the capacitor reaches approximately 63% of the applied voltage, and in five time constants it reaches approximately 99.3% of the applied voltage. The time it takes to fully charge a capacitor, from a practical perspective, is often taken to be five time constants. In the first circuit, the time constant was (100 KΩ)*(47 μF) = 4.7 seconds, making the time to fully charge the capacitor equal to about 23.5 seconds. Time constants are the same for charging and discharging, so it would take about 23.5 seconds ti fully discharge the capacitor when the voltage out of Channel A was reduced to zero volts.

Observations and Conclusions
----------------------------

-  Capacitors store electric charge
-  When capacitors are charged using a voltage source in series with a resistor, the rate of change in capacitor voltage slows exponentially
-  RC circuits are characterized by the RC product, called the time constant
-  A capacitor in a simple RC circuit moves to 63% of the difference between its current value and a step voltage applied to the circuit in one time constant
-  A commonly accepted time for a capacitor to fully charge is equal to five time constants

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_2_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_2_image_1.png
   :width: 300px
.. |lab_2_image_3.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_2_image_3.png
   :width: 300px
