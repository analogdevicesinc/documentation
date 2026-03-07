Activity: Introduction to Two-Port Networks - ADALM1000
=======================================================

Objective:
----------

The objective of this activity is to become familiar with the equations that are used to describe two-port networks, measure currents and voltages of a two-port network and learn to use these measurements to calculate any of the two-port parameters, and to learn the use of the table for converting from one set of two-port parameters to another set.

Educational
~~~~~~~~~~~

The objective of this activity is to gain familiarity with alternative two-port network parameter sets, to learn to measure the parameter sets, and to demonstrate the operational definition of these parameters.

Experimental
~~~~~~~~~~~~

To determine the impedance, admittance, and hybrid parameter sets for a two-port network.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CH A and CH B.

Pre Lab Reading:
----------------

Study the Background section below.

Read the Wikipedia page on two-port networks. Pay particular attention to the way in which the various parameters in each set (i.e., the z parameters, the y parameters, the h parameters, etc.) are defined.

Background:
-----------

In theory, a network may have one port, two-ports, or N ports, depending on the number of circuit mesh. The concept of a “port” is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1: Defining network ports.


Figure 1(a) is a one-port network. The port could be either an input or an output, but not both at the same time. The network in figure 1(b) is described by a port on the left, called the input port. The port on the right is usually called the output port. This is a standard convention used in describing two-port networks. In this activity you will be considering networks described as two-port networks. There are four sets of parameters commonly used to describe two-port networks. There is a fifth set which is omitted here because its use is beyond the scope of this activity. The four you will be considering in this activity are: the Z (impedance) parameters, Y (admittance) parameters, H (hybrid) parameters and ABCD (transmission) parameters.

The network inside the “box” of figure 1(b) can contain resistors, inductors, capacitors, transformers, transistors and in general any linear circuit device, including dependent sources but not independent (power generating) sources.

Essentially, there are two ways to view the two-port network problem. First, view the problem as if you were in a laboratory and you actually had a “box” with an input port and output port as shown above. Depending on the parameters one desires to find, measurements are made for currents I\ :sub:`1` and I\ :sub:`2` with sources V\ :sub:`1` or V\ :sub:`2` connected (other port left open-circuit) and with the other source replaced with a short circuit (zero volts). This becomes clear in the further explanation below. The second way to view the problem is as if you knew the construction of the network and you determined the various open-circuit voltages and short-circuit currents. In both cases one uses open-circuit voltage, shorted terminals, and short-circuit current to determine the parameters. This may sound confusing but the whole process is rather straightforward.

The Z parameters:
~~~~~~~~~~~~~~~~~

The impedance parameters (z parameters) relate the input and output voltages to the input and output currents by the following two equations:

:math:`V¬_1 = z_11 I_1 + z_12 I_2`

And,

:math:`V_2 = z_21 I_1 + z_22 I_2`

Or in matrix notation:

:math:`delim[matrix{2}{1}{V_1 V_2}] = delim[matrix{2}{2}{z_11 z_12 z_21 z_22}] delim[matrix{2}{1}{I_1 I_2}]`

The z parameters have units of ohms and are most easily found by applying a set of open-circuit tests on the circuit. When we apply a voltage to the input port with the output port open-circuited, we can measure the input current and output voltage and find the first two z parameters as follows:

:math:`\displaystyle z_11 = \frac{V_1 }{ I_1}` I\ :sub:`2` = 0

And,

:math:`\displaystyle z_21 = \frac{V_2 }{ I_1}` I\ :sub:`2` = 0

We can determine the other two z parameters by applying a similar test to the output port with the input port open-circuited:

:math:`\displaystyle z_12 = \frac{V_1 }{ I_2}` I\ :sub:`1` = 0

And,

:math:`\displaystyle z_22 = \frac{V_2 }{ I_2}` I\ :sub:`1` = 0

Sometimes the impedance parameters do not exist because the voltages cannot be described by the first equation. Therefore, we need alternatives, such as the admittance parameters.

The Y parameters:
~~~~~~~~~~~~~~~~~

The admittance parameters (y parameters) relate the input and output currents to the input and output voltages by the following two equations:

:math:`I_1 = y_11 V_1 + y_12 V_2`

And,

:math:`I_2 = y_21 V_1 + y_22 V_2`

Or in matrix notation:

:math:`delim[matrix{2}{1}{I_1 I_2}] = delim[matrix{2}{2}{y_11 y_12 y_21 y_22}] delim[matrix{2}{1}{V_1 V_2}]`

The y parameters have units of siemens (or mhos, 1/ohms) and are most easily found by applying a set of short-circuit tests on the circuit. When we apply a voltage to the input port with the output port short circuited, we can measure the input current and output current to find the first two y parameters:

:math:`\displaystyle y_11 = \frac{I_1 }{ V_1}` V\ :sub:`2` = 0

And,

:math:`\displaystyle y_21 = \frac{I_2 }{ V_1}` V\ :sub:`2` = 0

We can determine the other two y parameters by applying a similar test to the output port with the input port short-circuited:

:math:`\displaystyle y_12 = \frac{I_1 }{ V_2}` V\ :sub:`1` = 0

And,

:math:`\displaystyle y_22 = \frac{I2 }{ V_2}` V\ :sub:`1` = 0

There are occasions where neither the impedance nor the admittance parameters exist, so there is need for still another set of parameters.

The H parameters:
~~~~~~~~~~~~~~~~~

The hybrid parameters (h parameters) are based on making V\ :sub:`1` and I\ :sub:`2` the dependent variables, and relating them to cross-variables V\ :sub:`2` and I\ :sub:`1`. The h parameters satisfy the following equations:

:math:`V_1 = h_11 I_1 + h_12 V_2`

:math:`I_2 = h_21 I_1 + h_22 V_2`

Or in matrix notation:

:math:`delim[matrix{2}{1}{V_1 I_2}] = delim[matrix{2}{2}{h_11 h_12 h_21 h_22}] delim[matrix{2}{1}{I_1 V_2}]`

The h parameters are found using a mix of short and open circuit tests as follows: Short circuit tests:

:math:`\displaystyle h_11 = \frac{V_1 }{ I_1}` V\ :sub:`2` = 0

And,

:math:`\displaystyle h_21 = \frac{I_2 }{ I_1 }` V\ :sub:`2` = 0

Open circuit tests:

:math:`\displaystyle h_12 = \frac{V_1 }{ V_2}` I\ :sub:`1` = 0

And,

:math:`\displaystyle h_22 = \frac{I_2 }{ V_2}` I\ :sub:`1` = 0

The Transmission Parameters:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ABCD parameters are widely used in analysis of power transmission engineering where they are termed as “Circuit Parameters”. ABCD parameters are also known as “Transmission Parameters”. In these parameters, the voltage & current at the sending end terminals can be expressed in terms of voltage & current at the receiving end. The defining equations are given below.

:math:`V_1 = A V_2 + B ( -I_2)`

:math:`I_1 = C V_2 + D ( -I_2)`

Here “A” is called reverse voltage ratio, “B” is called transfer impedance “C” is called transfer admittance & “D” is called reverse current ratio.

Open circuit tests, I\ :sub:`2` = 0:

:math:`\displaystyle A = \frac{V_1 }{ V_2}` I\ :sub:`2` = 0 open reverse circuit voltage ratio

:math:`\displaystyle C = \frac{I_1 }{ V_2}` I\ :sub:`2` = 0 open circuit transfer admittance

Short circuit tests, V\ :sub:`2` = 0:

:math:`\displaystyle B = - \frac{V_1 }{ I_2}` V\ :sub:`2` = 0 -short circuit transfer impedance

:math:`\displaystyle D = - \frac{I_1 }{ I_2}` V\ :sub:`2` = 0 –short circuit reverse current ratio

Or in matrix notation:

:math:`delim[matrix{2}{1}{V_1 I_1}] = delim[matrix{2}{2}{A B C D}] delim[matrix{2}{1}{V_2 {-I_2}}]`

What are the units of parameters B & C? And what are the units of parameters A & D?

Directions:
-----------

Before you start it is a good idea to measure all the resistors to be used in this activity with an Ohmmeter (DMM or ALICE Ohmmeter tool) to confirm that you have the correct values and to record their actual values.

Materials:
~~~~~~~~~~

| ADALM1000 module
| Solderless breadboard
| Jumper wires
| 1 – 68 Ω resistor
| 2 – 100 Ω resistors
| 3 – 470 Ω resistors
| 1 – 1 kΩ resistor

Construct the two-port network on the solderless breadboard as shown in figure . Since the negative terminal of port 1 and negative terminal of port 2 are the same node (i.e. shorted together) only one connection to the ground of the M1k connector is needed.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Two Port Network schematic.


Use the ALICE Meter Source tool to fill in table 1 for each of the four test conditions. Drive port 1 with CH A turned on and set to 5 V DC, with port 2 open (CH B off) and shorted. To “short” port 2 simply set CH B to 0 V and turn it on. Repeat for port 2 by turning on CH B set to 5 V with port 1 open (Cha off) and shorted. To “short” port 1 simply set CH A to 0 V and turn it on.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-tab1.png
   :align: center
   :width: 600px

Table 1

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, CH A on set to 5 V, CH B off open circuit test.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, CH A on set to 5 V, CH B on set to 0 V, short circuit test.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-fig5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, CH A off, CH B set to 5 V open circuit test.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-two-port-net-fig6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, CH A on set to 0 V, CH B on set to 5 V, short circuit test.


Once you have all the measurements for V\ :sub:`1`, I\ :sub:`1`, V\ :sub:`2` and I\ :sub:`2`, calculate the z parameters, y parameters, h parameters and ABCD parameters.

**For Further Reading:**

`Two Port Networks <https://en.wikipedia.org/wiki/Two-port_network>`_

**Return to Lab Activity Table of Contents**
