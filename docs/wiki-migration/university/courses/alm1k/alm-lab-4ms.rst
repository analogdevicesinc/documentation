Activity: MOS FET device as a switch, For ADALM1000
===================================================

Objective:
----------

A MOS FET (NMOS) device can be used in many circuit configurations such as an amplifier, oscillator, filter, rectifier or just used as an on-off switch. If the FET is biased into the saturation region, it will operate as an amplifier or other linear circuit, if biased alternately in the linear (triode) region and cut-off region, then it is being used as a switch, allowing current to flow or not to flow in other parts of the circuit. This lab activity describes the NMOS device when operated as a switch.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

Switching circuits are significantly different than linear circuits. They are also easier to understand. Before investigating more complex circuits, we will begin by introducing discrete solid-state switching circuits: those built around NMOS devices.

A switch consists of a NMOS transistor that is alternately driven between the triode and cutoff regions. A simple version of the switch is shown in figure 1. When the input equals -V\ :sub:`in` , the gate-source voltage is less than the threshold voltage (V\ :sub:`TH`) or off so no current flows in the drain. This is illustrated by the red load line shown in the figure. When the NMOS is in cutoff, the circuit (ideally) has the following values:

:math:`V_DS = V_DD and I_D = 0 A`

This state is similar to an open switch.

When the input equals +V\ :sub:`in`, the transistor is driven into the triode region and the following conditions occur:

:math:`V_DS ˜ 0V and I_D = V_DD/R_D`

This state is similar to a closed switch connecting the bottom of R\ :sub:`D` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab_4sm_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 NMOS FET switch and its load line.


The characteristics for an enhancement mode NMOS switch assume that:

-   -V\ :sub:`in` is low enough to drive the transistor into cutoff.
   \* +V\ :sub:`in` must be greater than V\ :sub:`TH` to drive the transistor into triode.
   \* The transistor is an ideal component.

These conditions can be assured by designing the circuit so that:

-   -V\ :sub:`in` < V\ :sub:`TH`
   \* +V\ :sub:`in` > V\ :sub:`TH` (V\ :sub:`DD` is a good maximum)

Condition 1 guarantees that the circuit is driven into the cutoff region by the input. Conditions 2 assure that the transistor will be driven into the triode region.

An actual NMOS switch differs from the ideal switch in several aspects. In practice, even in cutoff there is some small leakage current through the transistor. Also, in triode, there is always some voltage dropped across the transistor's internal resistance, R\ :sub:`ON`. Typically, this will be between 0.1 and 0.2 V in triode depending on the drain current and size of the device. These variations from the ideal are generally minor with a properly sized device, so we can assume near ideal conditions when analyzing or designing a NMOS switch circuit.

Materials:
~~~~~~~~~~

| ADALM1000 Hardware module
| Solder-less Breadboard
| 1 - 100Ω Resistor (R\ :sub:`D`)
| 1 - 5mm LED (any color)
| 1 - small signal NMOS transistor (ZVN2110A or CD4007 CMOS array)

Directions:
~~~~~~~~~~~

One common application for a NMOS (or any other) switch is to drive an LED. An LED driver is shown in figure 2. The driver shown in this figure is used to couple a low current part of the circuit to a relatively high current device (the LED). When the output from the low current circuit is low (0 V), the transistor is in cutoff and the LED is off. When the output from the low current circuit goes high (+3 V), the transistor is driven into triode and the LED lights. The driver is used because the low-current part of the circuit may not have the current capability to supply the 20 mA (typical) required to light the LED to full brightness.

Build the LED switch circuit shown in figure 2 on your solder-less breadboard. R\ :sub:`D` serves to limit the current that flows in the LED from the +5 V power supply. The switch is controlled by the channel A voltage output from the I/O connector. Scope channel B will display the voltage across the switch transistor M\ :sub:`1` (V\ :sub:`DS`) or the voltage at the LED as indicated by the green arrows.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab_4sm_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, NMOS LED switch


Hardware Setup:
~~~~~~~~~~~~~~~

The CA generator should be configured for a 100 Hz square wave with a 3 volt Max and 0 volt Min. Scope channel B is connected to measure the voltage across the transistor or the at the top of the LED. The current flowing through the transistor, can be calculated as the voltage difference between the + 5 V supply and CB-V divided by the resistor value (100Ω). The Channel A current trace measures the current in the gate terminal of M\ :sub:`1`.

Procedure:
~~~~~~~~~~

Save the voltage trace across the transistor Drain-Source ( channel B dashed green line ) and at the LED ( channel B solid green line ) and include them in your lab write-up.

Questions:
~~~~~~~~~~

How much current is flowing in resistor R\ :sub:`D` when the LED is on and when the LED is off?

How much current is flowing in the Gate terminal of M\ :sub:`1`?

Try lowering the Max value for V\ :sub:`IN` ( CA-V, the gate voltage of M\ :sub:`1` ) until the LED no longer turns on. What is the voltage? How does this compare to the V\ :sub:`TH` listed in the datasheet?

Calculate the R\ :sub:`ON` when M\ :sub:`1` is in triode. How does this value compare to the spec listed in the datasheet?

Switches in Parallel:
---------------------

Two NMOS transistors can be connected with their drains and sources in parallel, figure 3, which provides a way to switch on the load from two different signals. Either input can turn on the load but both need to be off for the load to be off. This is referred to as an “OR” function.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab_4sm_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Two Switches in parallel


Modify the circuit on your breadboard to look like figure 3. Add a second NMOS transistor, M\ :sub:`2`, as shown. Now connect the transistor gates to the digital I/O port pins PIO 0 and PIO 1 respectively. Open the digital control window and set PIO 0 and PIO 1 to all four combinations of logic 0 and 1. Note which combinations turn on the LED. The voltage on the LED and drain resistor can be monitored with the CHB scope input as before.

Switches in Series:
-------------------

Two NMOS transistors can be connected in series with the drain of the lower transistor connected to the source of the upper transistor, figure 4, which provides a way to switch off the load from two different signals. Either input can turn off the load but both need to be on for the load to be on. This is referred to as an “AND” function.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab_4sm_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Two Switches in series


Modify the circuit on your breadboard to look like figure 4. Now the second NMOS transistor is in series with the source of M\ :sub:`1`. Again the gates of M\ :sub:`1` and M\ :sub:`2` are connected to the digital I/O port pins PIO 0 and PIO 1 respectively. Again, set PIO 0 and PIO 1 to all four combinations of logic 0 and 1. Note which combinations turn on the LED. The voltage on the LED and drain resistor can be monitored with the CHB scope input as before. You should also measure the voltage at the connection between the source of M\ :sub:`1` and the drain of M\ :sub:`2` for each of the four conditions. Comment on the voltages seen at the drain of M\ :sub:`2` in your lab report and why.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/nmos_as_switch_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/nmos_as_switch_bb`

**For Further Reading:**

| `Transistor <https://en.wikipedia.org/wiki/Transistor>`__
| `Light emitting diode <https://en.wikipedia.org/wiki/Light-emitting_diode>`__
| `LED circuit <https://en.wikipedia.org/wiki/LED_circuit>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
| **Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**
