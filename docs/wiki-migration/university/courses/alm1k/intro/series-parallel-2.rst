Activity: Series and Parallel Resistors - ADALM1000
===================================================

Objective:
----------

The objective of this Lab activity is to investigate series and parallel connected resistors.

Series and Parallel Circuits
----------------------------

Simple circuits with only a few components are generally straightforward for beginners to understand. But, things get more complex when larger numbers of components enter into the mix. Where is the current going? What are the node voltages doing? Can the circuit be simplified and easier to understand? The following information should help.

In this lab activity, we will first discuss the difference between series circuits and parallel circuits, using circuits containing the most basic of components, resistors and batteries ( or voltage sources ), to show the difference between the two configurations.

Before we get too far into the explanation, we need to define what a circuit node is. A node in a circuit is nothing more than the electrical junction between two or more components. When a circuit is depicted in a schematic such as figure 1, the nodes are represented by the wires (lines) between components.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Node example schematic


The schematic shows a circuit with 4 resistors and a voltage source. There are also four unique nodes. Colored nodes (lines) Red connects the (+) end of the voltage source to resistor R\ :sub:`1`, Orange connects R\ :sub:`1` and R\ :sub:`2` together, Blue connects R\ :sub:`2` to R\ :sub:`3` and R\ :sub:`4` and green connects (–) end of the voltage source to R\ :sub:`3` and R\ :sub:`4`. Note that we usually define one node as the common node that all the other nodes are referenced to, the green ground node in this case.

We also need to understand how current flows through a circuit. Conventional Current flows from a higher or more positive voltage to a lower or less positive voltage in a circuit. Some amount of current will flow through every path it can take to get to the point of lowest voltage, usually called ground (0 Volts). Using the above circuit as an example, here is how current will flow as it runs from the voltage source positive terminal to the negative terminal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-2.png
   :align: center
   :width: 500px

Notice that in some nodes (like between R\ :sub:`1` and R\ :sub:`2`) the current is the same going in as it is coming out. At other nodes (specifically the three-way junction between R\ :sub:`2`, R\ :sub:`3`, and R\ :sub:`4`) the main (red) current splits into two different ones, the purple current flowing in R\ :sub:`3` and the orange current flowing in R\ :sub:`4`. Also notice that the I\ :sub:`R3` and I\ :sub:`R4` currents recombine as the green current. That highlights the key difference between series and parallel connections.

Series Circuits Defined
~~~~~~~~~~~~~~~~~~~~~~~

When resistors are connected in series (as shown in figure 2), the terminal of one resistor is connected directly to the terminal of the next resistor, with no other possible paths such that all the current in one resistor has to flow into the next and so on.

When resistors are in series, they can be combined or lumped together as an equivalent single resistor with a resistance equal to the sum of the series resistances, i.e.,

:math:`R_SERIES = R_1 + R_2 + R_3 + ...`

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Series resistors, R\ :sub:`SERIES` = R\ :sub:`1` + R\ :sub:`2` + R\ :sub:`3` +...


Why is this true? Ohm's Law tells us that the voltage across a resistor is equal to the current through the resistor times the resistance. So for the above series circuit:

:math:`V_S=V_R1+V_R2+V_R3+V_R4`

We know that all the resistors have the same current I\ :sub:`S`.

:math:`V_R1=I_S \times R_1`

Similarly for the other three resistors so:

:math:`V_S=I_S \times R_1+I_S \times R_2+I_S \times R_3+I_S \times R_4`

Or factoring out I\ :sub:`S`:

:math:`V_S=I_S \times (R_1+R_2+R_3+R_4)`

So the total equivalent resistance is simply the sum of their values.

Parallel Circuits Defined
~~~~~~~~~~~~~~~~~~~~~~~~~

When resistors are in parallel (as shown in figure 3), all of their first terminals are connected together, and all of their second terminals are connected together.

When resistors are in parallel, they can be combined or lumped together as an equivalent single resistor whose value is given by the following equation:

:math:`R_PAR = 1/(1/R_1+1/R_2 +1/R_3+ ...)`

For two resistors in parallel this simplifies to:

:math:`\displaystyle R_PAR = \frac{R_1 \times R_2}{R_1+R_2}`

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Parallel resistors


Why is this true? Ohm's Law tells us that the voltage across a resistor is equal to the current through the resistor times the resistance. So for the above Parallel circuit:

We know that all the resistors have the same voltage V\ :sub:`S`.

:math:`I_R1=V_S/R_1`

The current supplied by voltage source V\ :sub:`S` is the sum of the currents in the resistors.

:math:`I_S=I_R1+I_R2+I_R3+I_R4`

Substituting for the four resistors we get:

:math:`I_S=V_S/R_1+V_S/R_2+V_S/R_3+V_S/R_4`

Or factoring out V\ :sub:`S`:

:math:`I_S=V_S(1/R_1 + 1/R_2 + 1/R_3 + 1/R_4)`

Rearranging for resistance we get the total equivalent resistance:

:math:`R_PARALLEL = 1/(1/R_1+1/R_2 +1/R_3+ ...)`

Experiments
-----------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless breadboard and jumper wires
| 3 – 100 Ω resistors
| 3 – 470 Ω resistors

Resistors in Series:
~~~~~~~~~~~~~~~~~~~~

Place three 100Ω resistors in series on your solderless bread board as shown in figure 4. Connect using jumper wires connect the CH A input to the left side of the first resistor and the CH B input to the right side of the same resistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-5.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 4, series connected resistors


Start the ALICE M1K Ohm Meter tool. The screen is shown here. The software uses a known resistor to test the unknown resistor against. The ADALM1000 has a built in 50 Ohm resistor that can be used for this. Be sure that the Int option is selected. The voltage level that is used to measure the resistor can be set. Testing at the maximum 5.0V gives the best results for most resistor values. Click on Run and you should see something like this with the single 100 Ω resistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-6.png
   :align: center
   :width: 225px

Move the CH B jumper wire to the right end of the second resistor as shown next.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-7.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 5, two resistors in series


The ohm meter should now read the value for the two resistors in series or about 200 Ω. Now move the CH B jumper wire to the right end of the third resistor as shown next.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-8.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 6, three resistors in series


The ohm meter should now read the value for the three resistors in series or about 300 Ω.

Resistors in Parallel:
~~~~~~~~~~~~~~~~~~~~~~

Now replace the 100 Ω resistors with 470 Ω resistors as shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-9.png
   :align: center
   :width: 300px

.. container:: centeralign

   Measuring a single 470 Ω resistor


The ohm meter should now read the value for the single resistor or about 470 Ω. Move the middle 470 Ω resistor so it is in parallel with the resistor on the right as shown next.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-10.png
   :align: center
   :width: 300px

.. container:: centeralign

   Measuring two 470 Ω resistors in parallel


The ohm meter should now read the value for the two 470 Ω resistors in parallel. Does the measured value agree with the formula for resistors in parallel?

Move the third 470 Ω resistor so it is in parallel with the other two resistors on the right as shown next.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-11.png
   :align: center
   :width: 300px

.. container:: centeralign

   Measuring three 470 Ω resistors in parallel


The ohm meter should now read the value for the three 470 Ω resistors in parallel. Does the measured value agree with the formula for resistors in parallel?

Experiment with other combinations of resistors and values to check that the formulas hold for any value resistor.

Combination Circuits
~~~~~~~~~~~~~~~~~~~~

More complex connections of resistors are generally just combinations of series and parallel connections. This is commonly encountered, especially when wire resistances is considered. In that case, wire resistance is in series with other resistances that are in parallel.

A combination circuit can be broken up into similar parts that are either series or parallel, as shown in figure 7. In the figure, the total resistance can be calculated by relating the three resistors to each other as in series or in parallel.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/ser-par-12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Combined Series and parallel resistors


R\ :sub:`2` and R\ :sub:`3` are connected in parallel in relation to each other, so we know that for those two resistors the equivalent resistance will be:

:math:`\displaystyle R_PAR = \frac{R_2 \times R_3}{R_2+R_3}`

The combined resistance of R\ :sub:`2` and R\ :sub:`3` are in series with R1 so the total equivalent resistance will be:

:math:`R_EQ = R_1+R_PAR`

For more complicated combination circuits, various parts can be identified as series or parallel, reduced to their equivalents, and then further reduced until a single resistance remains.

| **For Further Study:**
| `Khan Academy - Resistor circuits <https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-resistor-circuits/v/ee-series-resistors>`_
| `Boundless Physics <https://courses.lumenlearning.com/boundless-physics/chapter/overview-5/>`_
| `Series and parallel circuits (in Physics) <http://physics.bu.edu/py106/notes/Circuits.html>`_

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
