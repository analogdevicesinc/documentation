Chapter 1: Introduction and Chapter Objectives
==============================================

This introductory chapter will serve as a quick review of a few of the more important topics from the earlier courses Circuits I and II. It can be skipped if the reader feels he or she is sufficiently familiar with these fundamental circuit analysis and design concepts.

**After completing this chapter you should be able to:**

-   Define an Active Device vs. a Passive Device
-   Apply KVL and KCL to a circuit
-   Create Thevenin and Norton Equivalent Circuits
-   Convert between Thevenin and Norton Equivalent Circuits
-   Use the Superposition Theorem to analyze circuits with multiple sources

1.1 Active versus passive devices:
----------------------------------

An active device is any type of component with the ability to electrically control the flow of current (electricity controlled by electricity). For a circuit to be called electronic, it must contain at least one active device. Components incapable of controlling current by means of another electrical signal are called passive devices. Resistors, capacitors, inductors, transformers, and even diodes are all considered passive devices. Passive devices can have linear current vs voltage characteristic like a resistor or non-linear I vs V curves such as a diode and are commonly two terminal elements. Active devices include, but are not limited to, vacuum tubes, transistors, silicon-controlled rectifiers (SCRs), and TRIACs.

All active devices have the means to control the flow of current through them. Some active devices allow a voltage to control this current while other active devices allow another current to be the controlling signal. Devices utilizing a voltage as the controlling signal are, not surprisingly, called voltage-controlled devices. Devices working on the principle of one current controlling another current are known as current-controlled devices. The first type of solid-state transistor successfully demonstrated was a current-controlled device.

1.2 Notation and conventional terminology
-----------------------------------------

The notations used in these pages for voltages and currents correspond to the following conventions: DC bias values are indicated by an upper case letter with upper case subscripts, e.g. V\ :sub:`DS`, I\ :sub:`C`. Instantaneous values of small-signal variables are indicated by a lower-case letter with lower-case subscripts, e.g. v\ :sub:`gs`//, //i\ :sub:`d`. Total values are indicated by a lower-case letter with upper-case subscripts, e.g. *vBE, iD*. Schematic symbols for independent sources are circular and symbols for controlled sources have a diamond shape. Voltage sources have a ± sign within the symbol and current sources have an arrow. Schematics are drawn with the standard conventions where the most positive supply voltage is drawn at the top and the most negative at the bottom. Thus positive current flow is generally from top to bottom in the schematic. Inputs are generally on the left and outputs on the right with the signal flow from left to right.

Over time as the study of Electronics developed the use of certain terminology has become common or the defacto standard. Some terms and symbols have over time been used in multiple contexts and taken on somewhat different meanings. One such case is the use of the word "saturation". In the context of Bipolar Junction Transistors "saturation" has a much different meaning than in the context of Field Effect Transistors. This can lead to confusion in readers new to Electronics. Another example is the use of the Greek letter ? (beta). It is used to represent the dimensionless feedback factor in the context of Op-Amp circuits and as the dimensionless current gain of BJT devices. The reader should take care when reading though the material covered in this text to avoid confusion when these and other such context sensitive terms are encountered.

In this text the reader should expect that calculations done in the various example circuits should result in reasonable values. If the power supply voltage is +/-10 V, a calculated DC bias value of 15 V (not within the range of the power supply voltages) for example would be unreasonable. Generally, bias current levels will be between 1 microamp and a few hundred milliamps. A calculated bias current of 3.2 amps is probably unreasonable and should be reexamined (except in case of perhaps power devices). Peak-to-peak ac voltages should be within the power supply voltage range. A calculated component value that is unrealistic should be rechecked. For example, a resistance equal to 0.013 ohms. Given the inherent variations in most electronic components, three significant digits are more than adequate for representation of results.

1.3 Basic quantities.
---------------------

Two of the main laws that describe the operation of electronic systems are Ohm's law and Kirchhoff's laws. The main quantities that describe the operation of electronic systems are resistance R, capacitance C, and inductance L. The derivative quantities are reactance X, impedance Z, and admittance, or full conductivity G.

It is presumed that the reader has a level of familiarity with the following basic circuit concepts:

-   Ohm's Law
-   Passive Circuit Analysis
-   Kirchhoff's circuit laws
-   Thevenin and Norton Equivalent Circuits
-   The Superposition Theorem
-   Controlled Sources
-   Ideal operational amplifiers
-   Transformers
-   Frequency Response
-   Familiarity with the Spice circuit simulator or similar software

What follows is a short review of some of these concepts.

1.4 Review of Kirchhoff's circuit laws
--------------------------------------

Kirchhoff's circuit laws are two equalities that deal with the conservation of charge and energy in electrical circuits, and were first described in 1845 by Gustav Kirchhoff. These "laws" are widely used in the analysis and design of electronic circuits.

1.4.1 Kirchhoff's current law (KCL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1.4.1 Currents entering and leaving a node.


The current entering any junction in a circuit network is equal to the current leaving that junction.

*i*\ :sub:`1` + *i*\ :sub:`4` = *i*\ :sub:`2` + *i*\ :sub:`3`

This law is sometimes referred to as Kirchhoff's point rule, Kirchhoff's junction rule (or nodal rule), and Kirchhoff's first rule.

The principle of conservation of electric charge implies that: At any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node. Otherwise electric charge would endlessly build up on or drain off the node which is physically impossible.

or

The algebraic sum of currents in a network of conductors meeting at a point is zero. (Assuming that current entering the junction is taken as positive and current leaving the junction is taken as negative).

Recalling that current is a signed (positive or negative) quantity reflecting direction towards or away from a node; this principle can be stated as the following equation:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-e1.png
   :align: center
   :width: 100px

Here, n is the total number of branches with currents flowing towards or away from the node. This formula is also valid for complex currents:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-e2.png
   :align: center
   :width: 100px

The law is based on the conservation of charge whereby the charge (measured in coulombs) is the product of the current (in amperes) and the time (which is measured in seconds). A matrix version of Kirchhoff's current law is the basis of most circuit simulation software, such as SPICE.

:doc:`Activity 1: Kirchhoff's Voltage and Current Laws for ADALM1000 </wiki-migration/university/courses/alm1k/circuits1/alm-cir-1>`

1.4.2 Kirchhoff's voltage law (KVL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This law is sometimes referred to as Kirchhoff's second law, Kirchhoff's loop (or mesh) rule, and Kirchhoff's second rule.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1.4.2 Kirchhoff's voltage law


The sum of all the voltages around a loop of circuit elements is equal to zero.

*v1 + v2 + v3 + v4 = 0*

The principle of conservation of energy implies that:

The directed sum of the electrical potential differences (voltage) around any closed circuit must be zero.

or

Simply, the sum of the electromotive forces in any closed loop is equivalent to the sum of the potential drops in that loop.

or

The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop.

Similarly to KCL, it can be stated as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-e3.png
   :align: center
   :width: 100px

Here, *n* is the total number of voltages measured. The voltages may also be complex:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-e4.png
   :align: center
   :width: 100px

This law is based on the conservation of "energy given/taken by potential field" (not including energy taken by dissipation). Given a voltage potential, a charge which has completed a closed loop doesn't gain or lose energy as it has gone back to initial potential level.

This law holds true even when resistance (which causes dissipation of energy) is present in a circuit. The validity of this law in this case can be understood if one realizes that a charge in fact doesn't go back to its starting point, due to dissipation of energy. A charge will just terminate at the negative terminal, instead of positive terminal. This means all the energy (from the power supply) given by the potential difference has been fully consumed by resistance which in turn loses the energy as heat dissipation.

To summarize, Kirchhoff's voltage law has nothing to do with gain or loss of energy by electronic components (resistors, capacitors, etc). It is a law referring to the potential field generated by voltage sources. In this potential field, regardless of what electronic components are present, the gain or loss in "energy given by the potential field" must be zero when a charge completes a closed loop.

1.5 Review of Thévenin's theorem
--------------------------------

In circuit theory, Thévenin's theorem for linear electrical networks states that any combination of voltage sources, current sources and resistors with two terminals is electrically equivalent to a single voltage source V and a single series resistor R. For single frequency AC systems the theorem can also be applied to general impedances, not just resistors.

This theorem states that a circuit of voltage sources and resistors can be converted into a Thévenin equivalent, which is a simplification technique used in circuit analysis. The Thévenin equivalent can be used as a good model for a power supply or battery (with the resistor representing the internal impedance and the source representing the electromotive force). The circuit consists of an ideal voltage source in series with an ideal resistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f3.png
   :align: center
   :width: 400px

Figure 1.5.1 Any black box containing only voltage sources, current sources, and other resistors can be converted to a Thévenin equivalent circuit, comprising exactly one voltage source and one resistor.

| **Review Lab Activity:** :doc:`Real voltage sources </wiki-migration/university/courses/alm1k/alm-lab-e1>` **for ADALM1000**
| **Review Lab Activity:** :doc:`Real voltage sources </wiki-migration/university/courses/electronics/electronics-lab-0>` **for ADALM2000**

1.6 Review of Norton's theorem
------------------------------

Norton's theorem for linear electrical networks states that any collection of voltage sources, current sources, and resistors with two terminals is electrically equivalent to an ideal current source, I, in parallel with a single resistor, R. For single-frequency AC systems the theorem can also be applied to general impedances, not just resistors. The Norton equivalent is used to represent any network of linear sources and impedances, at a given frequency. The circuit consists of an ideal current source in parallel with an ideal impedance (or resistor for non-reactive circuits).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f4.png
   :align: center
   :width: 400px

Figure 1.6.1 Any black box containing only voltage sources, current sources, and resistors can be converted to a Norton equivalent circuit.

:doc:`Activity 4: Thévenin Equivalent Circuit and Maximum Power Transfer for ADALM1000 </wiki-migration/university/courses/alm1k/circuits1/alm-cir-4>`

1.7 Review of the Superposition Theorem
---------------------------------------

The Superposition Theorem is one of those strokes of genius that takes a complex subject and simplifies it in a way that makes perfect sense. The strategy used in the Superposition Theorem is to eliminate all but one source of power within a network at a time, using series/parallel analysis to determine voltage drops (and/or currents) within the modified network for each power source separately. Then, once voltage drops and/or currents have been determined for each power source working separately, the values are all "superimposed" on top of each other (added algebraically) to find the actual voltage drops/currents with all sources active. To understand the concept we will analyze the following example circuit and apply the Superposition Theorem to it:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.1


There are two sources of power in this circuit, figure 1.7.1, therefore we will have to calculate two sets of values for voltage drops and/or currents. The general rule, when applying the Superposition Theorem to a circuit for series/parallel analysis with one source, all other voltage sources are replaced by shorts, and all current sources with open circuits. We have only voltage sources (batteries) in this example circuit. Every inactive source will be replaced with a short during analysis.

The first set is done for the circuit with the 5 volt source removed and replaced with a short circuit, and only the 2.6 volt source remaining, figure 1.7.2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.2


For the second set we replace the 2.6 volt source with a short and with only the 5 volt source remaining, figure 1.7.3.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.3


Analyzing the circuit with only the 2.6 volt source, we obtain the following values for voltage and current:

+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+
| R\ :sub:`1` | R\ :sub:`2` | R\ :sub:`3` | R\ :sub:`2`\ IIR\ :sub:`3` | R\ :sub:`1`\ +R\ :sub:`2`\ IIR\ :sub:`3` |       |
+=============+=============+=============+============================+==========================================+=======+
| 2           | 0.6         | 0.6         | 0.6                        | 2.6                                      | Volts |
+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+
| 5           | 3           | 2           | 5                          | 5                                        | mAmps |
+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+
| 400         | 200         | 300         | 120                        | 520                                      | Ohms  |
+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+

Table 1.7.1

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.4


Analyzing the circuit with only the 5 volt battery, we obtain another set of values for voltage and current:

+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+
| R\ :sub:`1` | R\ :sub:`2` | R\ :sub:`3` | R\ :sub:`1`\ IIR\ :sub:`2` | R\ :sub:`3`\ +R\ :sub:`1`\ IIR\ :sub:`2` |       |
+=============+=============+=============+============================+==========================================+=======+
| 1.538       | 1.538       | 3.462       | 1.538                      | 5                                        | Volts |
+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+
| 3.845       | 7.69        | 11.54       | 11.54                      | 11.54                                    | mAmps |
+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+
| 400         | 200         | 300         | 133.33                     | 433.33                                   | Ohms  |
+-------------+-------------+-------------+----------------------------+------------------------------------------+-------+

Table 1.7.2

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.5


When superimposing these values of voltage and current, we have to be very careful to consider polarity (voltage drop) and direction (electron flow), as the values have to be added algebraically.

============ ===================== =================== =================
Voltage      With only 2.6V source With only 5V source With both sources
============ ===================== =================== =================
VR\ :sub:`1` 2                     -1.538              0.462
VR\ :sub:`2` 0.6                   1.538               2.138
VR\ :sub:`3` -0.6                  3.462               2.862
============ ===================== =================== =================

Table 1.7.3

Applying these superimposed voltages to the circuit, the end result looks something like this:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.6


Currents add up algebraically as well, and can either be superimposed as done with the resistor voltage drops, or simply calculated from the final voltage drops and respective resistances (I=V/R). Either way, the answers will be the same. Here we show the superposition method applied to current:

============ ===================== =================== =================
Current      With only 2.6V source With only 5V source With both sources
============ ===================== =================== =================
IR\ :sub:`1` 5mA                   -3.845mA            1.155mA
IR\ :sub:`2` 3mA                   7.69mA              10.69mA
IR\ :sub:`3` -2mA                  11.54mA             9.54mA
============ ===================== =================== =================

Table 1.7.4

Once again applying these superimposed figures to our circuit:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr1-f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7.7


It must be noted that the Superposition Theorem works only for circuits that are reducible to series/parallel combinations for each of the power sources at a time (thus, this theorem is useless for analyzing an unbalanced bridge circuit), and it only works where the underlying equations are linear (no mathematical powers or roots). The requisite of linearity means that Superposition Theorem is only applicable for determining voltage and current, not power. Power dissipation, being a nonlinear function, does not algebraically add to an accurate total when only one source is calculated at a time. The need for linearity also means this Theorem cannot be applied in circuits where the resistance of a component changes with voltage or current. Hence, networks containing components like incandescent light bulbs could not be analyzed. Another prerequisite for Superposition Theorem is that all components must be "bilateral," meaning that they behave the same with electrons flowing either direction through them. Resistors have no polarity-specific behavior, and so the circuits we've been studying so far all meet this criterion. Unidirectional devices like diodes cannot be included in the circuit being analyzed.

The Superposition Theorem finds use in the study of alternating current (AC) circuits, and semiconductor (amplifier) circuits, where sometimes AC is often mixed (superimposed) with DC. Because AC voltage and current equations (Ohm's Law) are linear just like DC, we can use Superposition to analyze the circuit with just the DC power source, then just the AC power source, combining the results to tell what will happen with both AC and DC sources in effect. For now, though, Superposition will suffice as a break from having to do simultaneous equations to analyze a circuit.

:doc:`Activity 3: Proportionality and Superposition for ADALM1000 </wiki-migration/university/courses/alm1k/circuits1/alm-cir-3>`

Section Review:
~~~~~~~~~~~~~~~

-   The Superposition Theorem states that a circuit can be analyzed with only one source of power at a time, the corresponding component voltages and currents algebraically added to find out what they'll do with all power sources in effect.
-   To negate all but one power source for analysis, replace any source of voltage (batteries) with a wire; replace any current source with an open (break).

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/preface>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-2>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
