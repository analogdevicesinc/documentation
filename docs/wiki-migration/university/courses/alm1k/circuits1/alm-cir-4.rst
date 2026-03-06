Activity: Thévenin Equivalent Circuit and Maximum Power Transfer, For ADALM1000
===============================================================================

Objective:
----------

The objective of this Lab activity is to verify Thévenin's theorem by obtaining the Thévenin equivalent voltage (V\ :sub:`TH`) and Thévenin equivalent resistance (R\ :sub:`TH`) for the given circuit. Verify the Maximum Power Transfer Theorem.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Thévenin's Theorem is a process by which a complex circuit is reduced to an equivalent circuit consisting of a single voltage source (V\ :sub:`TH`) in series with a single resistance (R\ :sub:`TH`) and a load resistance (R\ :sub:`L`). After creating the Thévenin Equivalent Circuit, the load voltage V\ :sub:`L` or the load current I\ :sub:`L` may be easily determined.

One of the principal uses of Thévenin's theorem is to replace a large portion of a circuit, often a more complicated and uninteresting part, by a simple equivalent. The new simpler circuit enables rapid calculations of the voltage, current, and power which the more complicated original circuit is able to deliver to a load. It also helps to choose the optimal value of the load (resistance) for maximum power transfer.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Thévenin Equivalent Circuit of Figure 1


2. The Maximum Power Transfer Theorem states that an independent voltage source in series with a resistance R\ :sub:`S` or an independent current source in parallel with a resistance R\ :sub:`S`, delivers a maximum power to the load resistance R\ :sub:`L` when R\ :sub:`L` = R\ :sub:`S`.

In terms of a Thévenin Equivalent Circuit, maximum power is delivered to the load resistance R\ :sub:`L` when R\ :sub:`L` is equal to the Thévenin equivalent resistance R\ :sub:`TH` of the circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fi31.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Maximum Power Transfer


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Various Resistors (100 Ω, 330 Ω, 470 Ω, 1 KΩ and 1.5 KΩ)

Procedure:
~~~~~~~~~~

| 1. Verifying the Thévenin's theorem:
| a) Construct the circuit of figure 1 using the following component values:

| R\ :sub:`1` = 330 Ω
| R\ :sub:`2` = 470 Ω
| R\ :sub:`3` = 470 Ω
| R\ :sub:`4` = 330 Ω
| R\ :sub:`5` = 1 KΩ
| R\ :sub:`L` = 1.5 KΩ
| V\ :sub:`S` = +5V

b) Accurately measure the voltage V\ :sub:`L` across the load resistance using ALM1000 Volt Meter Tool. Use the Volt Meter Tool by connecting channel CA to the + node of V\ :sub:`L` and connect channel CB to the - node. V\ :sub:`L` will be the difference between CA volts and CB volts. This value will later be compared to the one you will find using Thevenin Equivalent.

c) Find V\ :sub:`TH`: Remove the load resistance R\ :sub:`L` and measure the open circuit voltage V\ :sub:`OC` across the terminals. Use the Volt Meter Tool by connecting channel CA to the + node of V\ :sub:`OC` and connect channel CB to the - node. V\ :sub:`OC` will be the difference between CA volts and CB volts. This is equal to V\ :sub:`TH`. See figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4: Measuring the Thevenin Voltage


d) Find R\ :sub:`TH`: Remove the source voltage V\ :sub:`S` and construct the circuit as shown in figure 5. Use the ALM1000 Ohmmeter Tool to measure the resistance looking into the opening where R\ :sub:`L` was. This gives R\ :sub:`TH`. Make sure there is no power applied to the circuit before measuring with the Ohmmeter and the ground connection has been moved as shown.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5: Measuring the Thevenin Resistance R\ :sub:`TH`.


e) Obtaining V\ :sub:`TH` and R\ :sub:`TH`, construct the circuit of figure 2. Create the value of R\ :sub:`TH` using a series and or parallel combination of resistors from your parts kit. Using the Meter - Source Tool connect channel CA for the V\ :sub:`TH` source and set the value to what you measured for VTH in step c).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig6.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6: Thevenin Equivalent Construction


f) With R\ :sub:`L` set to the 1.5 KΩ used in step b) measure the V\ :sub:`L` for the equivalent circuit and compare it to the V\ :sub:`L` obtained in step b). This verifies the Thévenin theorem.

g) Optional: Repeat steps 1 b) to 1 f) for R\ :sub:`L` = 2.2 KΩ

2. Verifying the Maximum Power Transfer theorem:

a) Construct the circuit as in figure 7 using the following values:

| V\ :sub:`S` = +5 V
| R\ :sub:`1` = R\ :sub:`2` = 470 Ω
| R\ :sub:`3` = 1 KΩ
| R\ :sub:`L` = combinations of 1 KΩ and 100 Ω resistors ( figure 8 )

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7: Circuit for Maximum Power Theorem


b) Use the Volt Meter Tool by connecting channel CA to the + node of V\ :sub:`L` and connect channel CB to the - node across R\ :sub:`L`. V\ :sub:`L` will be the difference between CA volts and CB volts.

c) To find the value of R\ :sub:`L` for which maximum power is transferred, vary the load resistances by constructing series / parallel combinations of 1 KΩ and 100 Ω for R\ :sub:`L` between 500 Ω to 1400 Ω in 100 Ω steps as shown in figure 8. For each value of R\ :sub:`L` write down V\ :sub:`L`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab4-fig7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8. R\ :sub:`L` configurations


d) Calculate the power for each load resistor value using P\ :sub:`L`\ =V\ :sub:`L`\ :sup:`2`/R\ :sub:`L`. Then, interpolate between your measurements to calculate the load resistor value corresponding to the maximum power (P\ :sub:`L`-max). This value should be equal to R\ :sub:`TH` of circuit in figure 7 with respect to load terminals.

Questions:
~~~~~~~~~~

1. Calculate the percentage error difference between the load voltages obtained for circuits of figure 1 and figure 2.

2. Using Voltage Division for circuit of figure 2, calculate V\ :sub:`L`. Compare it to the measured values. Explain any differences.

3. Calculate the maximum power transmitted to the load R\ :sub:`L` obtained for the circuit of figure 3.

**For Further Reading:**

| DC Voltmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/voltmeter_lab-0.pdf>`__ (volt-meter-tool-1.2.exe)
| DC Ohmmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/ohmmeter_lab-0.pdf>`__ (ohm-meter-vdiv-1.2.exe)
| DC Meter-Source `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/meter-source-lab0.pdf>`__ (dc-meter-source-tool-1.3.exe)

:doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

| **\*Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
