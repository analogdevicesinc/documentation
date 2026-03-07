Activity: Voltage Dividers and Lab Equipment - ADALM1000
========================================================

Objective:
----------

The objective of this activity is to learn that Lab equipment is not ideal and that “real world” behavior must be taken into account when making measurements. Batteries are not ideal voltage sources and the effective internal resistance will be measured. The actual behavior of two voltage dividers when a DC voltage and an AC voltage are applied will be examined.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

**Impedance:** Every lab instrument has an effect on the circuit it is connected to. Just as it is impossible to design a dynamic mechanical system without friction (that resists motion), it is impossible to design an electrical system without impedance (that resists the flow of electrons). Impedance has two effects on an electrical system. It changes its magnitude (the value of the voltage or current) and its phase (behavior vs time). If the impedance affects only magnitude, then we call it resistance.

All electrical measurement devices have an internal impedance, and this is also true for the M1k. The kinds of impedances that will concern us in this class are listed in table 1: (These values are not precisely correct for a given instrument, but are still of use to make the general point.)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-tab1.png
   :width: 400px

Table 1

Note that for this first part we are only concerned with the effect of the instrument on the magnitude (resistance component) of the impedance. Also note that the instruments in the lab (M1k) are designed to have as minimal an effect as possible on any circuit they are connected to. In this part of the activity, we examine how much of an effect the instrument has.

**Voltage dividers:**

In order to analyze the effect an instrument will have on a circuit under test, we need to understand a fundamental concept of circuits, the voltage divider. Basically, when a voltage in a circuit exists across two or more resistances, that voltage divides up in a manner proportional to the resistances. That is, a larger resistance will have a larger fraction of the voltage dropped across it. The voltage drop will be proportional to its resistance divided by the total resistance of all the resistors combined (Series resistance).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-fig1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1, Voltage division.


In Figure 1, voltage source V\ :sub:`S` is divided between R\ :sub:`1` and R\ :sub:`2`. Mathematically, this can be expressed as:

:math:`V_S = V_1 + V_2`

:math:`\displaystyle V_1 = V_S \frac{R_1}{(R_1 + R_2)}`

:math:`\displaystyle V_2 = V_S \frac{R_2}{(R_1 + R_2)}`

Note that R\ :sub:`1`\ +R\ :sub:`2` is the total resistance of the circuit.

\**Series and parallel circuits: \*\*

Another fundamental concept needed to understand in order to analyze the circuits you will build and measure is how to mathematically combine resistances. If any number of resistances are connected in series, you simply add them to find the total resistance. If any number of resistances are wired in parallel, the total resistance is the reciprocal of the sum of the reciprocals of all of the resistances. This is summarized in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Series and parallel circuits.


For Resistors in series:

:math:`R_T = R_1 + R_2 + R_3 + cdots + R_N`

For Resistors in parallel:

:math:`1/R_T = 1/R_1 + 1/R_2 + 1/R_3 + cdots + 1/R_N`

For only two resistors in parallel:

:math:`R_T = R_1 \times R_2 / R_1 + R_2`

Note that the voltage divider equation applies only to series circuits. Any time you use an instrument to measure the voltage across a device, V\ :sub:`Load`, as illustrated in figure 3, we are connecting that measurement instrument (R\ :sub:`Scope`) in parallel with the resistance of the circuit being measured. So just connecting the M1k analog input will affect the quantity being measured. In this case the effective load resistance on the battery is R\ :sub:`Total` and it is the parallel combination of the M1k input impedance (1 MegΩ) with the resistance of the load resistor (R\ :sub:`Load`). This results in a total load resistance, R\ :sub:`Total`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Effect of measurement instrument.


Once the total load resistance, R\ :sub:`Total` is known, the voltage divider equation can be used to find the internal resistance of the source. Note that, since the voltage drop across any number of resistors in parallel is the same, V\ :sub:`Rtotal` is equal to V\ :sub:`Rload`.

**Other circuit components:**

There are two other basic circuit components: capacitors and inductors. Inductors combine like resistors. To combine inductors in series, you add them. To combine them in parallel, you take the reciprocal of the sum of the reciprocals. Unlike with resistors, to combine capacitors in series take the reciprocal of the sum of the reciprocals. To combine capacitors in parallel, simply add the capacitances. (Note: This is the opposite of combining resistors.)

For capacitors in series:

:math:`1/C_T = 1/C_1 + 1/C_2 + 1/C_3 + cdots + 1/C_N`

For capacitors in parallel:

:math:`C_T = C_1 + C_2 + C_3 + cdots + C_N`

For inductors in series:

:math:`L_T = L_1 + L_2 + L_3 + cdots + L_N`

For inductors in parallel:

:math:`1/L_T = 1/L_1 + 1/L_2 + 1/L_3 + cdots + 1/L_N`

Materials:
----------

| ADALM1000 hardware module
| Solder-less breadboard, and jumper wire kit
| Battery (can be 1, 2, or 3 AAA or AA cells in series)
| Battery holder with breadboard leads
| 1 100 Ω resistor
| 2 1 KΩ resistors
| 2 47 KΩ resistors
| 2 470 KΩ resistors

DC Experiment :
~~~~~~~~~~~~~~~

We can use a voltage divider to determine how much effect a device has on a circuit, or in this case, the effect that a circuit has on a device. In the simple electrical model of the battery shown in figure 4, the internal resistance of the battery depends on the battery size and chemistry. This more advanced lab activity uses :doc:`Electrochemical Impedance Spectroscopy </wiki-migration/university/courses/alm1k/alm-eis-lab>` to measure the internal impedance of a battery vs frequency. The simple model in figure 4 ignores much of the internal chemistry including changes as the battery is discharged. The default assumption normally is that the voltage output of a battery doesn’t change with the load. We will investigate how this works in an actual circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-fig4.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4, Equivalent circuit for a real world voltage source (battery).


The output voltage of the battery will be measured using the M1k with and without load resistor. Remember that R\ :sub:`int` represents the internal model of the battery. You do not add this resister to the circuit. R\ :sub:`Load` represents the load, or combined resistance of whatever circuit you place on the source. Using the voltage divider formula, we know that the voltage drop across the load is given by:

:math:`V_load = V_int R_load / {{R_int} + {R_load}}`

AC Measurements
---------------

The experiment above showed that the load can affect the source, in this case a battery. Now we will look at how the instrument can affect the circuit. The M1k analog input (oscilloscope) can load the circuit and affect the circuit being tested. Now you can close the Voltmeter Tool and open the ALICE desktop Scope tool. Use the AWG generator, CHA, of the M1k to put an AC signal across a resistor divider circuit shown in figure 5. Set the CHA frequency to 500 Hz. Set Min to 1 V and Max to 4 V (the goal is 3 Vp-p) . The wave shape can be a Sine wave. Use R\ :sub:`1` = 1kΩ and R\ :sub:`2` = 1kΩ. Take data and plot the output using Excel.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-fig5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Resistor Divider.


Make all the connections on the solderless breadboard. In the circuit above, CH A is the signal source output from M1k. GND is Ground. Only one ground connection has to be made from the M1k because the AWG Generator and analog inputs are connected internally to ground. BIN is the channel B analog input (Use Split I/O mode for Channel B).

Calculate the ideal ratio of the voltage that should be measured on BIN to the voltage on CH A when R\ :sub:`1` and R\ :sub:`2` exactly equal. Now measure the actual voltages and calculate the ratio. R\ :sub:`1` and R\ :sub:`2` will never be exactly equal in the real world. Measure the voltages again with the resistors swapped, that is the resistor that is where R\ :sub:`1` is connected is now where R\ :sub:`2` is connected (R\ :sub:`2` where R\ :sub:`1` was). As shown on the right in figure 5. Compare the two ratios to determine how well matched the two resistors are.

Repeat the above experiment using R\ :sub:`1` = R\ :sub:`2` = 47 KΩ and 470 KΩ resistors. Again create a table of the measurements and calculate the ratio of the voltages.

The more exact model of this measurement is given in figure 6, were R\ :sub:`CHA` and R\ :sub:`BIN` represent the effective internal input resistances of the analog input channels of the M1k. The effective input resistance of CHA can be ignored (Do you know why?), but the input resistance of BIN effects the measurement. Using the measurements above, estimate the value of R\ :sub:`BIN`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-voltage-dividers-lab-fig6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, More exact model.


At what values of R\ :sub:`2` do you think the value of R\ :sub:`BIN` will start to matter in the accuracy of your measurement?

Useful Hints:
-------------

You can copy an image of the oscilloscope screen to Microsoft Word (or other document editing program) by taking a screen snap shot using the “Snipping Tool”.

You can save the trace data in a csv file, which you can open in Excel, using Save Data as CSV under the File drop down menu.

You can change the thickness of the waveform trace line by: Under the Options drop down menu, Opening the Change Settings controls and entering a new value for the Trace Width in pixels. The Grid width can also be changed.

**Additional related Lab Activities:**

| :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`
| :doc:`Series, Parallel Resistors </wiki-migration/university/courses/alm1k/intro/series-parallel-2>`
| :doc:`Voltage and Current Division </wiki-migration/university/courses/alm1k/circuits1/alm-cir-2>`
| :doc:`Frequency compensated voltage dividers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-voltage-divider>`

**Return to Lab Activity Table of Contents**
