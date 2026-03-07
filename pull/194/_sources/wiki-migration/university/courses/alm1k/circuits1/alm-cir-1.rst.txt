Activity: Kirchhoff's Voltage and Current Laws, For ADALM1000
=============================================================

Objective:
----------

The objective of this Lab activity is to verify Kirchhoff's Voltage Law (KVL) and Kirchhoff's Current Law (KCL) using mesh and nodal analysis of the given circuit.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

1. Kirchhoff's Voltage Law states that the algebraic sum of all the voltages around any closed path (loop or mesh) is zero. If we define the voltages across each resistor R\ :sub:`1` through R\ :sub:`5` as V\ :sub:`1` through V\ :sub:`5`, applying Kirchhoff's voltage law to the first and the second loops in the circuit shown in figure 1 yields:

| Loop 1: -Vs +V\ :sub:`1` +V\ :sub:`2` +V\ :sub:`5` = 0
| Loop 2: -V\ :sub:`2` +V\ :sub:`3` +V\ :sub:`4` = 0

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab1-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Kirchhoff's Laws


2. Kirchhoff's Current Law states that the algebraic sum of all the currents at any node is zero. If we define the currents through each resistor R\ :sub:`1` through R\ :sub:`5` as I\ :sub:`1` through I\ :sub:`5`, applying Kirchhoff's current law to the first four nodes in the circuit shown in figure1 yields the following equations;

| Node a: -Is+I\ :sub:`1`\ =0
| Node b: -I\ :sub:`1`\ +I\ :sub:`2`\ +I\ :sub:`3`\ =0
| Node c: -I\ :sub:`3`\ + I\ :sub:`4` = 0
| Node d: -I\ :sub:`2`-I\ :sub:`4`\ +I\ :sub:`5`\ =0

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Various Resistors :1 KΩ (2) ,1.2 KΩ (2), 2.4 KΩ

Procedure:
~~~~~~~~~~

Step 1. Construct the circuit shown in figure 1 using these resistor values:

| R1 = 1 KΩ
| R2 = 2.4 KΩ
| R3 = 1.2 KΩ
| R4 = 1 KΩ
| R5 = 1.2 KΩ

Step 2. Use the Ohmmeter Tool to measure the actual resistor values.

Step 3. Connect the fixed power supply (5 Volts) at node a and connect node e to ground as Vs.

Step 4. Accurately measure all voltages and calculate currents in the circuit using the Volt Meter Tool.

Step 5. Record the measurements in a tabular form containing the measured voltage and current values as shown below.

======================== ========== ====== ======
Branch current/voltage   V [volts ] I [mA] R [KΩ]
======================== ========== ====== ======
V\ :sub:`1`, I\ :sub:`1`                   
V\ :sub:`2`, I\ :sub:`2`                   
V\ :sub:`3`, I\ :sub:`3`                   
V\ :sub:`4`, I\ :sub:`4`                   
V\ :sub:`5`, I\ :sub:`5`                   
V\ :sub:`s`, I\ :sub:`s`                   
======================== ========== ====== ======

Step 6. Verify KVL for the loops in the circuit using loop equations 1 and 2.

Step 7. Verify KCL for the nodes in the circuit using node equations a, b, c and d.

Questions:
~~~~~~~~~~

1. Calculate the ideal voltages and currents for each element in the circuit and compare them to the measured values.

2. Compute the percentage error in the two measurements and provide a brief explanation for the error.

**For Further Reading:**

| DC Voltmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/voltmeter_lab-0.pdf>`_ (volt-meter-tool-1.2.exe)
| DC Ohmmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/ohmmeter_lab-0.pdf>`_ (ohm-meter-vdiv-1.2.exe)
| DC Meter-Source `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/meter-source-lab0.pdf>`_ (dc-meter-source-tool-1.3.exe)

:doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
