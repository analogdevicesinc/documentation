Activity: Voltage and Current Division, For ADALM1000
=====================================================

Objective:
----------

The objective of this Lab activity is to verify the voltage and current division properties of resistor networks.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Voltage and Current division allow us to simplify the task of analyzing a circuit. Voltage Division allows us to calculate what fraction of the total voltage across a series string of resistors is dropped across any one resistor. For the circuit of figure 1, the Voltage Division formulas are:

:math:`V_1 = V_S R_1/(R_1 + R_2)` (1)

:math:`V_2 = V_S R_2/(R_1 + R_2)` (2)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1. Voltage division


Current Division allows us to calculate what fraction of the total current into a parallel string of resistors flows through any one of the resistors.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Current division


For the circuit of figure 2, the Current Division formulas are:

:math:`I_1 = I_S R_2/(R_1 + R_2)` (3)

:math:`I_2 = I_S R_1/(R_1 + R_2)` (4)

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Various Resistors 470 Ω, 1 KΩ, 4.7 KΩ. and 1.5 KΩ

Procedure:
~~~~~~~~~~

1. Verifying the voltage division:

a) Construct the circuit as shown in figure 1. Set R\ :sub:`1`\ = 4.7 KΩ, R\ :sub:`2`\ = 1.5 KΩ and use the fixed power supply 5V as voltage source Vs. Use the Volt Meter Tool to measure the voltages V\ :sub:`1` and V\ :sub:`2`

Repeat this step for R\ :sub:`1` = R\ :sub:`2` = 4.7 KΩ. and write down the measurements.

b) Calculate the voltages V\ :sub:`1` and V\ :sub:`2` by using the formulas (1) and (2) in each case.

c) Compare the results from steps 1a and 1b.

2. Verifying the current division:

a) Construct the circuit as shown in figure 2. Set R\ :sub:`1`\ = 470 Ω, R\ :sub:`2`\ = 1 KΩ. and Rs=470 Ω. Use the Meter Source tool to measure the currents Is, I\ :sub:`1` and I\ :sub:`2` Connect the Channel A generator output as voltage source Vs. Set CHA to source a DC voltage of +5V ( SVMI mode ). Use Channel B as an ammeter to alternately measure I\ :sub:`1` and I\ :sub:`2` by connecting the lower end of R\ :sub:`1` and R\ :sub:`2` to CHB with CHB set to 0 V ( SVMI mode ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Measuring I\ :sub:`1` and I\ :sub:`2`\


Repeat this step by using R\ :sub:`1`\ =R\ :sub:`2` = 470 Ω. and write down the measurements.

b) Calculate the currents I\ :sub:`1` and I\ :sub:`2` by using the formulas (3) and (4).

c) Compare the results from steps 2a and 2b.

Questions:
~~~~~~~~~~

1. How well did the measured outputs and calculated outputs compare? Explain any difference.

2. Can you apply current division to obtain I\ :sub:`1` and I\ :sub:`2` for the circuit shown in figure 4? Explain briefly.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig5.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 5 ADALM1000 test connections


The Potentiometer as voltage divider
------------------------------------

A potentiometer is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. The schematic symbol for the potentiometer is shown in figure 6. It is similar to the standard fixed resistor symbol with the sliding or rotating contact depicted by the arrow pointing at the body of the resistor. If voltages V\ :sub:`1` and V\ :sub:`2` are connected to the two fixed terminals of the potentiometer the voltage that appears at the wiper or adjustable terminal, V\ :sub:`3`, will be some value between V\ :sub:`1` and V\ :sub:`2`. V\ :sub:`3` will equal V\ :sub:`2` when the rotating contact is all the way toward the V\ :sub:`2` terminal and V\ :sub:`3` will equal V\ :sub:`1` when the rotating contact is all the way toward the V\ :sub:`1` terminal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig6.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 6, Potentiometer schematic symbol


The resistance between the two fixed terminals is constant (R\ :sub:`POT`). The resistance between the adjustable terminal and either fixed terminal will be proportional to the wiper position. If only two terminals are used, one end and the wiper, it acts as a variable resistor.

**Potentiometer Design problem:**

Note figure 7, for R\ :sub:`POT` = 10 KΩ choose values for R\ :sub:`1` and R\ :sub:`2` such that:

:math:`\displaystyle V_3 = \frac{1}{3} (V_1-V_2)`

When the potentiometer is adjusted all the way to one end, near bottom terminal (or the one connected to R2).

:math:`\displaystyle V_3 = \frac{2}{3} (V_1-V_2)`

When the potentiometer is adjusted all the way to the other end, near top terminal (or the one connected to R1).

:math:`\displaystyle V_3 = \frac{1}{2} (V_1-V_2)`

When the potentiometer is centered (half way between the extremes).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab2-fig7.png
   :align: center
   :width: 175px

.. container:: centeralign

   Figure, 7 Potentiometer Design problem


Build the circuit from figure 7 using your values for R\ :sub:`1` and R\ :sub:`2` and verify that the voltage on V\ :sub:`3` follows the conditions set in the design problem. Use the fixed 2.5 V supply as V\ :sub:`2` and the fixed +5 V supply as V\ :sub:`1`.

**For Further Reading:**

| DC Voltmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/voltmeter_lab-0.pdf>`_ (volt-meter-tool-1.2.exe)
| DC Ohmmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/ohmmeter_lab-0.pdf>`_ (ohm-meter-vdiv-1.2.exe)
| DC Meter-Source `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/meter-source-lab0.pdf>`_ (dc-meter-source-tool-1.3.exe)

:doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

`The Potentiometer <https://en.wikipedia.org/wiki/Potentiometer>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
