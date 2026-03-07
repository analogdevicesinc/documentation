Activity: Voltage Level Shifting, For ADALM2000
===============================================

Objective:
----------

The objective of this lab activity is to explore circuits that increase the voltage swing or shift the high and/or low logic level of digital signals.

Background:
-----------

There are often many cases in digital systems where two or more sections of the system operate from different power supply voltages. When digital signals cross the boundary between these different power supply regions or domains it is necessary to insert a circuit block that translates or shifts the logic levels from the level supplied by one domain for example with a +5 Volt power supply to a second domain with a +9 Volt power supply or a +/- 5 Volt dual supply. One important application example is controlling analog switches where the signals involved are bipolar in nature and require dual ( +/- 5 Volt ) supplies. Such logic level shifting circuits can take many forms. We will be exploring a few examples in this activity.

The simplest form of a voltage level shifter as shown in figure 1(a), uses a pass NMOS device and a pull up resistor ( pull down for PMOS configuration figure 1(b) ). If V\ :sub:`IN` at the input of the inverter is at a logic high its output goes to ground turning on enhancement mode device M\ :sub:`N1` and drives V\ :sub:`OUT` to ground. Conversely if V\ :sub:`IN` is at a logic low the inverter output goes to V\ :sub:`DDI`. With the gate of M\ :sub:`N1` also at V\ :sub:`DDI` it will now be off which allows V\ :sub:`OUT` to be pulled up to V\ :sub:`DDO` by resistor R\ :sub:`1`. Similarly for the negative level shifter in figure 1(b) if V\ :sub:`IN` is at a logic low the inverter output goes to V\ :sub:`DDI` turning on enhancement mode device M\ :sub:`P1` and drives V\ :sub:`OUT` to V\ :sub:`DDI`. With V\ :sub:`IN` is at a logic high the inverter output goes to ground. With the gate of M\ :sub:`P1` also at ground it will now be off which allows V\ :sub:`OUT` to be pulled down to the negative voltage, V\ :sub:`DDO` by resistor R\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/avls_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Positive (a) and Negative (b) voltage level shift


The strength of the inverter devices, the on resistance of the pass FET, and the parasitic capacitance of the signal lines mainly determine the fall time of the output signal. Also, the rise time of the output signal is determined mostly by the value of the pull-up resistor on the output and the signal-line parasitic capacitance assuming the pass FET turns off instantaneously, which is not generally the case but we assume it is for this discussion. An annoying aspect of resistor loaded level shifters such as this is the DC current that flows in resistor R\ :sub:`1`. For the positive shifter (a) a current equal to V\ :sub:`DDO`/R\ :sub:`1` flows when V\ :sub:`OUT` is low. For the negative shifter (b) a current equal to V\ :sub:`DDI`-V\ :sub:`DDO`/R\ :sub:`1` flows when V\ :sub:`OUT` is high. As was just pointed out the transition time for the output is a function of R\ :sub:`1` and any parasitic capacitance and there will be a trade-off between power dissipation and speed which will determine the optimal value.

We can solve the DC current problem if we can replace the pull up load resistor R\ :sub:`1` with a transistor which can be turned on or off as needed. A second voltage level shifter using two complementary drivers and cross-coupled PMOS loads is shown in figure 2. The operation of circuit is as follows. When the input signal V\ :sub:`IN` is in a logic low state ( at ground ) and with V\ :sub:`INB` at V\ :sub:`DDI` because of the first inverter, M\ :sub:`N1` turns on ( M\ :sub:`N4` is off because of the second inverter ). This pulls the V\ :sub:`OUTB` signal to ground. This transition of V\ :sub:`OUTB` turns on M\ :sub:`P4` which pulls up the V\ :sub:`OUT` node to the V\ :sub:`DDO` voltage rail which turns off M\ :sub:`P3`. In the opposite case when V\ :sub:`IN` is at the V\ :sub:`DDI` rail ( V\ :sub:`INB` is at ground ), M\ :sub:`N1` is off and M\ :sub:`N4` is on, which turns on M\ :sub:`P3`. M\ :sub:`P3` pulls up V\ :sub:`OUTB` to the V\ :sub:`DDO` rail which turns off M\ :sub:`P4`. This design ensures that there is never a steady-state DC current path from V\ :sub:`DDI` or V\ :sub:`DDO` to ground, which insures very low quiescent current consumption. One design consideration is to size M\ :sub:`P3` and M\ :sub:`P4` to be weaker than M\ :sub:`N1` and M\ :sub:`N4` to reduce the potentially large current spikes when the circuit changes state.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/avls_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Level shifter with low quiescent current


For example, applications for low voltage to high voltage translation are Thin Film Transistor-Liquid Crystal Display panels and piezoelectric motor drivers.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard and Jumper wires
| 1 - 9 Volt battery with snap connector
| 2 Each 10KΩ, 4.7KΩ and 1KΩ resistors
| 1 - CMOS Hex Inverter, 74HC004 or CD4069
| 1 - CD4007 CMOS complementary pair array
| 2 - NMOS transistors (ZVN2110A)
| 2 - PMOS transistors (ZVP2110A)

Directions:
-----------

Build the circuit shown in figure 3 on your solder-less breadboard. Use AWG1 to drive V\ :sub:`IN` and use the positive power supply, Vp from the ADALM2000 board for V\ :sub:`DDI`. A 9 Volt battery supplies V\ :sub:`DDO`. Scope channels 1 and 2 will be used to view the output waveforms.

There are two versions of a positive level shifter circuit using pull-up resistors. The first version using INV1 to drive the source of M\ :sub:`N1` with the gate of M\ :sub:`N1` connected to the +5V supply rail produces a 0 to +9V swing inverted version of V\ :sub:`IN` at V\ :sub:`OUT1`. The second, simple open-drain, version using INV3 to drive the gate of M\ :sub:`N2` with the source of M\ :sub:`N2` connected to ground produces a 0 to +9V swing non-inverted version of the signal at the input of INV3 at V\ :sub:`OUT2`. INV2 is inserted between V\ :sub:`IN` and the input of INV3 so that V\ :sub:`OUT1` and V\ :sub:`OUT2` both have the same overall inverted phase relationship to V\ :sub:`IN`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/avls_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Two versions of a positive level shifter


Hardware Setup:
---------------

Configure AWG channel 1 as a square wave with a 2.5V offset and a 5V amplitude peak-to-peak (0 to 5V swing). Set the frequency to 20KHz.

Procedure:
----------

With Scope channel 1 connected to V\ :sub:`OUT1` and Scope channel 2 connected to V\ :sub:`OUT2` observe the rising and falling edges of the waveform. Replace 10K? resistors R\ :sub:`1` and R\ :sub:`2` with 4.7KΩ and 1KΩ resistors and compare the relative rise and fall times for each value.

Questions:
----------

Are there any differences in delay or rise/fall times between the two versions of the level shifter? If so why?

.. _directions-1:

Directions:
-----------

Build the circuit shown in figure 4 on your solder-less breadboard. Use AWG1 to drive V\ :sub:`IN` and use the positive power supply, Vp from the ADALM2000 board for V\ :sub:`DDI`. A 9 Volt battery supplies V\ :sub:`DDO`. Scope channel 1 can be used to display V\ :sub:`IN` and channel 2 will be used to view the V\ :sub:`OUT` waveform. You can also observe the complementary output at the drain ( pin 13 ) of MP\ :sub:`1`. Pin 7 of the CD4007 needs to be connected to ground and the rest of the unused pins should be connected to V\ :sub:`DDO`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/avls_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Voltage level shifter with PMOS pull-up loads


The ADG3123 is an 8-channel, non-inverting CMOS to high voltage level translator.

.. _questions-1:

Questions:
----------

How does the delay or rise/fall times for the level shifters in figure 3 compare to the level shifter in figure 4? Explain why?

Appendix: Making an inverter with the CD4007 transistor array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 420px

.. container:: centeralign

   CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a20_f8.png
   :align: center
   :width: 600px

The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

These three inverters can be used to construct the three inverters in figure 3 for example.

**For Further Reading:**

| http://en.wikipedia.org/wiki/Logic_level
| http://www.analog.com/static/imported-files/tutorials/MT-098.pdf

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**
