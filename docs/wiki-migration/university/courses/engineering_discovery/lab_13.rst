M1K Basics and Voltage/Current Dividers
=======================================

Introduction
------------

After mastering the basic operation of the M1K and PixelPulse application software, it is useful to show how to build simple circuits on the solderless breadboard, connect them to the M1K, generate voltages and currents, and measure voltages on the PixelPulse display. In this lab we initially show how the solderless breadboard is used to construct circuits. We then build a voltage divider and a current divider, each comprised of resistors, on the solderless breadboard, and show the details regarding how to connect the ciruit to the M1K. Finally, we use a voltage source and current source in the M1K, controlled by PixelPulse software, to drive these circuits, and measure the voltages across the resistors on the computer display using the M1K and PixelPulse software.

Objective
---------

To gain a basic understanding of how to use the M1K, PixelPulse software, and the parts in the ADALP2000 Analog Parts Kit to build circuits and perform experiments on those circuits. To understand how basic schematic symbols, such as those used to represent the circuit ground and power supply voltage, are interpreted when constructing and analyzing a real circuit. To understand how voltage and current divider circuits work and how to calculate individual voltages in voltage dividers and individual currents in current dividers. Following completion of this lab you should be able to explain the basic operation the M1K and PixelPulse software, how to construct circuits on the solderless breadboard for evaluation, and calculate all voltages and currents in voltage and current divider circuits.

Materials and Apparatus
-----------------------

-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) 1.0 KΩ resistor from the ADALP2000 Analog Parts Kit
-  (1) 1.5 KΩ resistor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard\


|lab_13_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_13_assembly_image_1.png|

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Set up the M1K to source voltage/measure current on Channel A and measure voltage on Channel B
-  Set up Channel A to source a “Constant” voltage output of 5.0 V
-  Observe the output voltage of the voltage divider on Channel B and verify that it close to its calculated value
-  Observe the measured current on Channel A and compare it to its calculated value
-  Set up Channel A to source a "Sine" voltage that swings between 0.5 V and 4.5 V
-  Observe the output voltage of the voltage divider on Channel B and verify that it close to its calculated value
-  Verify that the current supplied by Channel A is swinging between its calculated values
-  Construct the following circuit on the solderless breadboard\

|lab_13_image_2.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_13_assembly_image_2.png|

-  Set up Channel A to source a “Constant” current output of 5 mA
-  Observe the output voltage across the current divider on Channel B and verify that it close to its calculated value
-  Set up Channel A to source a "Sine" current that swings between 2 mA V and 7 mA
-  Observe the output voltage of the voltage divider on Channels A and B and verify that it close to its calculated value
-  Calculate the current in each resistor using the current divider rule and compare the result to the results obtained by using Ohm's law to calculate the currents using the measured voltage across the circuit

Theory
------

This lab has two main purposes. The first is to become familiar with basic schematic symbols, with emphasis on "ground," and how to convert them into real circuits that connect to real signal generators and analyzers. The second purpose is to build and analyze two simple circuits: a voltage divider comprised of resistors connected in series, and a current divider comprised of resistors connected in parallel. The voltage divider is fed by a voltage source and the current divider is fed by a current source. In the voltage divider we calculate and measure the voltage across the resistors and in the current divider we calculate the voltage across the resistors and the current through each resistor. We derive the "voltage divider rule" and "current divider rule" below.

The concept of "ground" in circuits can sometimes lead to confusion. Terms like "signal ground," "earth ground," "chassis ground," "safety ground," "single-ended," "differential," "balanced," "common-mode," "ground loops," and many others get tossed around, often without a full understanding of their meanings. The basic concept of an ideal ground is introduced here and can be extended to any system, and imperfections in grounding systems can be understood and dealt with by modeling the grounding system with lumped and distributed circuit elements.

First it is necessary to emphasize that all voltages are *differences* in electrical potential between two distinct points. It therefore makes no sense to speak of a voltage at one point without referencing that point to another point. It is something like relative velocities. Two vehicles traveling in the same direction at the same speed are traveling at a velocity of zero with respect to each other, but may be traveling at 60 mph relative to the road. They are traveling at different velocities relative to the sun, and so on. The voltage between two battery terminals may be nominally 9 volts, but the voltage between one of the battery terminals and the terminal of a battery connected in another system is something else. In systems that use a ground reference, sometimes the fact that voltages are measured with respect to that ground is overlooked.

An ideal ground in a system has exactly the same voltage with respect to an ideal reference no matter where in the ground that voltage is measured (this means that the ground is an *equipotential* part of the system). All voltages within this system are measured with respect to this one ideal ground potential. A clear requirement of this ideal ground is that it have zero impedance such that any currents that flow within it do not develop voltage drops that would violate the equipotential requirement. This type of ideal ground is not realizable, but can be approximated using high quality conductors. At low frequencies the resistive component of ground impedance dominates, and at higher frequencies the skin effect increases resistance, and the inductive component of impedance begins to take effect. All of these produce undesirable voltage drops in the ground. There are many ways to implement grounds that are optimized for particular applications and signal frequencies that are well beyond the scope of this lab and any experiments that can be developed for the M1K. For our purposes, we can use an ideal ground approximation because the inductance in the ground is negligible due to the low signal frequencies encountered, and the ground interconnections have negligible resistance compared with the resistance levels encountered in the labs.

There are a number of different symbols used on schematic diagrams to represent different types of grounds. Some common types are shown below.{insert drawing when computer is back from IT}

When we see a particular ground symbol on a schematic drawing, we know that it represents one of the reference potentials that is used by our system. There may be many such ground symbols on the schematic, and we can envision these as all being connected together.

The solderless breadboard used with the M1K is comprised of a plastic block with a two-sided array of holes, with internal metal contacts, that are arranged in a grid. Each side of the array is made up of a series of five-hole rows, in which all of the metal contacts are connected together. This allows us to make circuit connections by placing the leads of the elements we wish to connect together in the same row. See the illustration below for an example{Place illustration here when PC is back from IT}

When constructing the labs on the solderless breadboard all ground connections indicated on the schematic should be connected together and to one or both GND ports on the M1K. We can view ground as our zero potential reference for all voltages generated and measured in the labs.

Series circuits are defined as circuits in which the same current flows through all elements. All of the elements carry the same current, but the voltage across a series circuit is divided among its series elements. For this reason, the series circuit is sometimes referred to as a *voltage divider*. We often need to know the voltage across a particular circuit element, and this can be easily calculated using the *voltage divider rule*, which only requires knowledge of the circuit element values and the voltage across the series circuit. We will use a resistive circuit to derive the voltage divider rule.

If we apply a voltage V\ :sub:`T` (T is for *Total*) across a series circuit comprised of resistors, as illustrated below, a current I flows in the circuit that is calculated using Ohm's law as

:math:`I = V_T/R_1 + R_2 + ... + R_n`

The voltage V\ :sub:`m` across a particular resistor, R\ :sub:`m`, is calculated as

:math:`V_m = IR_m`

If we substitute the current from the first equation into the second equation and solve for V\ :sub:`m` we obtain the voltage divider rule:

:math:`V_m = (V_T)R_m/R_1 + R_2 + ... + R_n`

The voltage divider rule for resistors therefore shows that the voltage across any resistor in a series connection is equal to the voltage across the series circuit multiplied by the ratio of the value of the resistor of interest to the sum of all of the resistances in the circuit. This ratio represents the percentage of the total voltage across the series circuit that appears across the resistor of interest. We can apply the voltage divider rule to the series circuit analyzed in the lab as follows:

:math:`V_{1.5KΩ} = (5 V)1.5KΩ/1.0KΩ + 1.5KΩ = (5 V)(0.6) = 3 V`

Note that the voltage across the 1.5KΩ resistor is measured between the junction of the two resistors and the zero potential ground.

Parallel circuits are defined as circuits in which the same voltage appears across all elements. While all of the elements have the same voltage across them, the current flowing into a parallel circuit is divided among its parallel elements. For this reason, the parallel circuit is sometimes referred to as a *current divider*. We often need to know the current flowing through a particular circuit element, and this can be easily calculated using the *current divider rule*, which only requires knowledge of the circuit element values and the current flowing into the series circuit. There are at least two forms of the current divider rule that are in common use, and we will use the one that has the same general form as the voltage divider rule as this form is easy to remember once the voltage divider rule has been learned. We will use a resistive circuit to derive the current divider rule.

If we apply a current I\ :sub:`T` (T is for *Total*) across a parallel circuit comprised of resistors, as illustrated below, a voltage V is developed across the circuit. The current I\ :sub:`T` is the sum of the currents flowing in each resistor, and is calculated using Kirchhoff's current law as:

:math:`\displaystyle I_T = V/R_1 + V/R_2 + ... + V/R_n = V(\frac{1}{R_1} + \frac{1}{R_2} + ... + \frac{1}{R_n})`

Now is a good time to introduce *conductance*, G, which is defined as the reciprocal of resistance, or G = 1/R. We can substitute G for 1/R in the above equation and rewrite it as:

:math:`I_T = V(G_1 + G_2 + ... + G_n) ⇒ V = I_T/G_1 + G_2 + ... + G_n`

The current I\ :sub:`m` flowing through a resistor R\ :sub:`m` in the parallel circuit can be calculated using Ohm's law as:

:math:`I_m = V/R_m = VG_m`

If we substitute V from the first equation into the above equation, we can solve for I\ :sub:`m` as:

:math:`I_m = (I_T)G_m/{G_1 + G_2 + ... + G_n}`

From this result, we can see that the current divider rule has the same form as the voltage divider rule, with I\ :sub:`T` substituted for V\ :sub:`T` and conductances substituted for resistances. The current divider rule for resistors shows that the current flowing through any resistor in a parallel connection is equal to the total current flowing into the parallel circuit multiplied by the ratio of the value of the conductance of interest to the sum of all of the conductances in the circuit. This ratio represents the percentage of the total current flowing into the parallel circuit that flows through the resistor of interest. We can apply the current divider rule to the parallel circuit analyzed in the lab as follows:

:math:`I_{1.0KΩ} = (5 mA)1/{1.0KΩ}/{1/{1.0KΩ}} + {1/{1.5KΩ}} = (5 mA)(0.6) = 3 mA`

:math:`I_{1.5KΩ} = (5 mA)1/{1.5KΩ}/{1/{1.0KΩ}} + {1/{1.5KΩ}} = (5 mA)(0.4) = 2 mA`

The voltage divider and current divider rules can be extended to other circuit elements as long as these elements are in series and parallel circuits, respectively.

Observations and Conclusions
----------------------------

-  An ideal ground is an equipotential voltage reference that is distributed throughout a system with zero impedance
-  An ideal ground exhibits no voltage drops
-  The solderless breadboard in the ADALP2000 Analog Parts Kit is comprised of two halves, each containing rows of five holes that contain metal contacts that are all connected together, allowing circuit elements to be easily connected to each other
-  All ground connections shown in the schematic diagrams are connected to one or both GND ports of the M1K
-  The voltage across individual elements in a series resistive circuit are fractions of the total voltage across the circuit
-  The voltage across any resistor in a series circuit can be determined by using the voltage divider rule
-  The current flowing through individual elements in a parallel resistive circuit are fractions of the total current flowing to the circuit
-  The current flowing through any resistor in a parallel circuit can be determined by using the current divider rule
-  The voltage divider and current divider rules can be extended to other types of circuit elements, provided the elements are in series and parallel, respectively

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_13_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_13_image_1.png
   :width: 800px
.. |lab_13_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_13_assembly_image_1.png
   :width: 800px
.. |lab_13_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_13_image_2.png
   :width: 800px
.. |lab_13_assembly_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_13_assembly_image_2.png
   :width: 1000px
