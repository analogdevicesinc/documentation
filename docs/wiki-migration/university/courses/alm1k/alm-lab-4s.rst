Activity: BJT device as a switch, For ADALM1000
===============================================

Objective:
----------

A bipolar junction transistor (BJT) can be used in many circuit configurations such as an amplifier, oscillator, filter, rectifier or just used as an on-off switch. If the transistor is biased into the linear region, it will operate as an amplifier or other linear circuit, if biased alternately in the saturation and cut-off regions, then it is being used as a switch, allowing current to flow or not to flow in other parts of the circuit. This lab activity describes the BJT when operated as a switch.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Switching circuits are significantly different than linear circuits. They are also easier to understand. Before investigating more complex circuits, we will begin by introducing discrete solid-state switching circuits: those built around BJTs.

A switch consists of a BJT transistor that is alternately driven between the saturation and cutoff regions. A simple version of the switch is shown in figure 1. When the input equals -V\ :sub:`in` , the base-emitter junction is reverse biased or off so no current flows in the collector. This is illustrated by the red load line shown in the figure. When the BJT is in cutoff, the circuit (ideally) has the following values:

:math:`V_CE = V_CC and I_C = 0 A`

This state is similar to an open switch.

When the input equals +V\ :sub:`in`, the transistor is driven into saturation// //and the following conditions occur:

:math:`V_CE ˜ 0V and I_Csat = V_CC/R_C`

This state is similar to a closed switch connecting the bottom of R\ :sub:`C` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4s_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NPN BJT switch and its load line.


The characteristics for a BJT switch assume that:

-   -V\ :sub:`in` is low enough to drive the transistor into cutoff.
   \* +V\ :sub:`in` must produce enough base current through R\ :sub:`B` to drive the transistor into saturation.
   \* The transistor is an ideal component.

These conditions can be assured by designing the circuit so that:

-   -V\ :sub:`in` = V\ :sub:`BE`
   \* +V\ :sub:`in` = V\ :sub:`BE` + I\ :sub:`B`\ R\ :sub:`B` (V\ :sub:`CC` is a good maximum)
   \* I\ :sub:`B` > I\ :sub:`Csat`/ß

Condition 1 guarantees that the circuit is driven into the cutoff region by the input. Conditions 2 and 3 assure that the transistor will be driven into the saturation region. An actual BJT switch differs from the ideal switch in several aspects. In practice, even in cutoff there is some small leakage current through the transistor. Also, in saturation, there is always some voltage dropped across the transistor's internal resistance. Typically, this will be between 0.2 and 0.4 V in saturation depending on the collector current and size of the device. These variations from the ideal are generally minor with a properly sized device, so we can assume near ideal conditions when analyzing or designing a BJT switch circuit.

Materials:
~~~~~~~~~~

| ADALM1000 Hardware module
| Solder-less Breadboard
| 1 - 6.8KΩ Resistor (R\ :sub:`B`)
| 1 - 100Ω Resistor (R\ :sub:`C`)
| 1 - 5mm LED (any color)
| 1 - small signal NPN transistor (2N3904)

Directions:
~~~~~~~~~~~

One common application for a BJT (or any other) switch is to drive an LED. An LED driver is shown in figure 2. The driver shown in this figure is used to couple a low current part of the circuit to a relatively high current device (the LED). When the output from the low current circuit is low (0 V), the transistor is in cutoff and the LED is off. When the output from the low current circuit goes high (+3 V), the transistor is driven into saturation and the LED lights. The driver is used because the low-current part of the circuit may not have the current capability to supply the 20 mA (typical) required to light the LED to full brightness.

Build the LED switch circuit shown in figure 2 on your solder-less breadboard. R\ :sub:`C` serves to limit the current that flows in the LED from the +5 V power supply. The switch is controlled by the channel A voltage output from the I/O connector. Scope channel B will display the voltage across the switch transistor Q\ :sub:`1` (V\ :sub:`CE`) or the voltage at the LED as indicated by the green arrows.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4s_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, NPN LED switch


Hardware Setup:
~~~~~~~~~~~~~~~

The CA generator should be configured for a 100 Hz square wave with a 3 volt Max and 0 volt Min. Scope channel B is connected to measure the voltage across the transistor or the at the top of the LED. The current flowing through the transistor can be calculated as the voltage difference between the +5 V supply and CB-V divided by the resistor value (100Ω). The Channel A current trace measures the current in R\ :sub:`B`.

Procedure:
~~~~~~~~~~

Save the voltage trace across the transistor collector-emitter ( channel B dashed green line ) and at the LED ( channel B solid green line ) and include them in your lab write-up.

Questions:
~~~~~~~~~~

How much current is flowing in resistors R\ :sub:`C` and R\ :sub:`B` when the LED is on and when the LED is off?

Calculate the ß when Q\ :sub:`1` is saturated. How does this value compare to the spec listed in the datasheet?

Switches in Parallel:
~~~~~~~~~~~~~~~~~~~~~

Two NPN transistors can be connected with their collectors and emitters in parallel, figure3, which provides a way to switch on the load from two different signals. Either input can turn on the load but both need to be off for the load to be off. This is referred to as an “OR” logic function.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4s_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Two Switches in parallel


Modify the circuit on your breadboard to look like figure 3. Add a second NPN transistor, Q\ :sub:`2`, and second base resistor, R\ :sub:`B2`, as shown. Now connect the other ends of R\ :sub:`B1` and R\ :sub:`B2` to the digital I/O port pins PIO 0 and PIO 1 respectively. Open the digital control window and set PIO 0 and PIO 1 to all four combinations of logic 0 and 1. Note which combinations turn on the LED. The voltage on the LED and collector resistor can be monitored with the CHB scope input as before.

Switches in Series:
~~~~~~~~~~~~~~~~~~~

Two NPN transistors can be connected in series with the collector of the lower transistor connected to the emitter of the upper transistor, figure 4, which provides a way to switch off the load from two different signals. Either input can turn off the load but both need to be on for the load to be on. This is referred to as an “AND” logic function.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4s_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Two Switches in series


Modify the circuit on your breadboard to look like figure 4. Now the second NPN transistor is in series with the emitter of Q\ :sub:`1`. Again the other ends of R\ :sub:`B1` and R\ :sub:`B2` are connected to the digital I/O port pins PIO 0 and PIO 1 respectively. Again, set PIO 0 and PIO 1 to all four combinations of logic 0 and 1. Note which combinations turn on the LED. The voltage on the LED and collector resistor can be monitored with the CHB scope input as before. You should also measure the voltage at the connection between the emitter of Q\ :sub:`1` and the collector of Q\ :sub:`2` for each of the four conditions. Comment on the voltages seen at the collector of Q\ :sub:`2` in your lab report and why.

BJT Transistor Realization of an XNOR gate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The single transistor inverter stage along with multiple input resistors can be combined to create more complex logic functions. The configuration shown in figure 5 realizes a two input exclusive NOR (XNOR) logic function. You will need a total of 5 NPN transistors, 13 resistors and one LED.

The resistors used as inputs at the bases of the 5 NPN transistors are not all the same value and they in theory should all be the same value. But a range of values will still work given the relatively high beta of the 2N3904 transistors and the values shown were chosen so as to not need more than the 5 of any one value supplied in the Analog Parts Kit. You can experiment with other resistor values to find what the range of minimum and maximum values is.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4s_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Resistor and NPN transistor XNOR gate.


Again, set PIO 0 and PIO 1 to all four combinations of logic 0 and 1. Note which combinations turn on the LED. The voltage at the LED and Q\ :sub:`5` collector resistor can be monitored with the CH-B scope input as before. You can also use the CH-B ( and / or CH-A ) input to monitor the voltages at the collectors of Q\ :sub:`1` – Q\ :sub:`4` as you change PIO 0 and 1.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/bjt_as_switch_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/bjt_as_switch_bb`

**For Further Reading:**

| `Transistor <https://en.wikipedia.org/wiki/Transistor>`__
| `Light- emitting diode <https://en.wikipedia.org/wiki/Light-emitting_diode>`__
| `LED circuit <https://en.wikipedia.org/wiki/LED_circuit>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
| **Return to Electronics Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**
