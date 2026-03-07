Activity: DC-DC Converters I - ADALM2000
========================================

Objective:
----------

The object of this activity is to explore an inductor based circuit which can produce an output voltage which is higher than the supplied voltage. This class of circuits are referred to as DC to DC converters or boost regulators.

Background Basics:
------------------

When the current flowing in an inductor is quickly interrupted a large voltage spike is observed across the inductor. This large voltage spike can in fact be useful in some cases. One example is the DC to DC boost converter, which is a circuit that can create a larger DC voltage from a smaller one with very high efficiency. The basic idea is to combine an inductive spike generator with a rectifier circuit, as shown in figure 1. Whenever the transistor is abruptly turned off the voltage at the drain spikes up, the diode D\ :sub:`1` is forward biased and current will flow from the inductor to charge up the high capacitance storage capacitor C\ :sub:`2`. When the drain voltage subsequently drops below the voltage on the capacitor, the diode is reverse biased and the output voltage remains constant. Just as in the chapter on AC power supplies, the output capacitor must be sized appropriately to minimize the ripple relating to the current flowing in the load. We will just use a small capacitor here and the circuit will not be able to source a large output current.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - AD8541 CMOS single supply opamp used as a comparator (or AD8561 comparator)
| 1 - 74HC00 quad CMOS NAND gate (or CD4007 see Appendix)
| 1 - ZVN2110A NMOS FET (2N7000 or power FET device such as IRF510)
| 1 - 20 KΩ resistor
| 1 - 10 KΩ resistor
| 1 - 1 mH inductor
| 1 - 47 uF capacitor
| 1 - 220 uF capacitor
| 2 - rectifier diodes (1N4001, 1N3064)

Additional Equipment:
---------------------

| Small handheld DMM
| +5 V bench power supply or battery holder for 3 AA cells to provide +4.5V

Simple inductor and switch DC/DC Converter:
-------------------------------------------

Build the circuit in figure 1 on your solder-less breadboard. Note that in this inductor based DC to DC converter the spikes of current needed may exceed the limits of the on-board +5V supply of ADALM2000 and cause it to shut down. You should use a standalone wall powered bench supply or batteries. You can use a 1N4001 or a 1N3064 for the rectifier diode. Start with a load resistance of 100kΩ and a switching frequency of 10 kHz which can be supplied by AWG1. What is the DC voltage of the "boosted" output? Record the value for your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a15_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Simple DC to DC converter


Now increase the frequency to 50 kHz. Measure and record the output voltage again. Explain why it has changed? One advantage we have here is that we can control the time period between the peaks of the signal going into the rectifier; in the power supply lab, we were stuck with a 60 Hz source.

Next decrease the load resistance to 10kΩ and again measure and record the output voltage.

Clearly what is needed if we want a constant output voltage is some active regulation to keep the voltage constant when the load resistance changes. A larger output capacitance to filter out the ripple would be a good addition as well. There are a few simple ways to implement the active regulation, and indeed there are a number of other interesting design considerations for DC to DC boost converters that you can read about if you are interested, but our goal here is really just to illustrate the concept, so the circuit shown in figure 1 is not optimal in any practical sense. With more careful design, boost converters can drive a much larger output current at very high conversion efficiency (very little wasted power). Note that the DC to DC converter requires a square-wave generator to drive it. Ordinarily this square-wave generator is part of the circuit and also powered by the input supply, so that the conversion circuit is self-contained. We will discuss the design of oscillators at the end of the lab as optional exercises.

Adding active regulation:
=========================

Directions:
-----------

The breadboard connections for the regulated version are as shown in figure 2. The DMM should be connected to measure the voltage at V\ :sub:`OUT`. The +5V bench power supply should be connected to the V\ :sub:`IN` node. The output of the arbitrary waveform generator, serving as a DC reference voltage, drives the positive input of the comparator at pin 3. The digital clock output drives the second input of the first NAND gate at pin 2. Scope input 2+ (single ended) is connected to the output of the comparator at pin 6. Diode D\ :sub:`2` is not required if a power FET, such as the IRF510, is used because devices such as that have the diode built in.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a15_f2a.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 Regulated DC to DC boost converter


Hardware Setup:
---------------

The signal generator should be configured for constant DC output of 2.5V. The digital clock output should be configured for a 50% duty cycle and 100 KHz output frequency. One of the digital outputs from the ADALM2000 could be programed for this or the second AWG output could be used as well. The single ended input of scope channel 1 ( 1+ ) is used to measure the signal seen at the output of the analog voltage comparator.

Procedure:
----------

Be sure to start up the waveform generator and digital clock outputs on the ADALM2000 board before turning on the +5V bench supply. The regulated output voltage at node Vout should be observed as the DC offset value of the waveform generator is adjusted. It should be equal to 3 times ( (R\ :sub:`1`\ +R\ :sub:`2`)/R\ :sub:`1`) ) the DC value of V\ :sub:`REF`.

Questions:
----------

| What is the effect of changing the DC value at the positive input of the comparator?
| What is the effect of changing the frequency of the digital clock output?
| Is there a minimum? or a maximum?
| How much current can the circuit supply to a load?
| Is that current affected by the voltage the output is set to?
| Is that current affected by the frequency of the digital clock output?
| Calculate the conversion efficiency of the circuit. Ratio of output power ( Iout \* Vout ) to input power ( Iin \* 5V )
| Change the value of L\ :sub:`1` and redo the above. How have the results changed?

Inverting DC - DC Converter
===========================

.. _objective-1:

Objective:
----------

The object of this activity is to explore an inductor based circuit which can produce an output voltage which is negative with respect to ground. This class of circuits are referred to as inverting DC to DC converters.

.. _materials-1:

Materials:
----------

| 1 - AD8541 CMOS single supply opamp used as a comparator (or AD8561 comparator)
| 1 - 74HC00 quad NAND gate (or CD4007 see Appendix)
| 1 - generic PNP transistor (TIP32 or similar device)
| 1 - 20KΩ resistor
| 1 - 10KΩ resistor
| 1 - 2.2KΩ resistor
| 1 - 1mH inductor
| 1 - 47uF capacitor
| 1 - 220uF capacitor
| 1 - rectifier diodes (1N4001, 1N3064)

.. _additional-equipment-1:

Additional Equipment:
---------------------

| Small handheld DMM
| +5 V bench power supply

.. _directions-1:

Directions:
-----------

The breadboard connections are as shown in the diagram below. The DMM should be connected to measure the voltage at V\ :sub:`OUT` . The +5V bench power supply should be connected to the V\ :sub:`IN` node. The output of the waveform generator drives the negative input of the comparator at pin 2. The digital clock output drives the second input of the NAND gate at pin 5. Scope input 2+ (single ended) is connected to the output of the comparator at pin 6.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a15_f3a.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 Inverting DC - DC Converter


.. _hardware-setup-1:

Hardware Setup:
---------------

The signal generator should be configured for constant DC output of 2.5V. The digital clock output should be configured for a 50% duty cycle and 100 KHz output frequency. The Single ended input of scope channel 1 (1+) is used to measure the output of the analog voltage comparator.

.. _procedure-1:

Procedure:
----------

Be sure to start up the wsignal generator and digital clock outputs on the ADALM2000 board before turning on the +5V bench supply. The regulated output voltage at node V\ :sub:`OUT` should be observed as the DC offset value of the waveform generator is adjusted. It should be equal to - V\ :sub:`REF`\ when V\ :sub:`REF` is set to 2.5V (assuming V\ :sub:`IN` is +5V).

.. _questions-1:

Questions:
----------

| What is the effect of changing the DC value at the negative input of the comparator?
| What is the effect of changing the frequency of the digital clock output?
| Is there a minimum? or a maximum?
| How much current can the circuit supply to a load?
| Is that current affected by the voltage the output is set to?
| Is that current affected by the frequency of the digital clock output?
| Calculate the conversion efficiency of the circuit. Ratio of output power (Iout \* Vout) to input power ( Iin \* 5V )
| Change the value of L\ :sub:`1` and redo the above. How have the results changed?

Circuit Additions:
------------------

What sort of circuit could you make to generate the 100 KHz square wave other than using the digital clock output on the ADALM2000 board? There are two additional gates in the 74HC00 package. The other two NAND gates along with RC delay network, R\ :sub:`4` C\ :sub:`4` can be configured into a ring oscillator as shown below. The values for R\ :sub:`4` and C\ :sub:`4` are approximate for 100 KHz and can be adjusted as needed.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a15_f4.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 4 stand-alone gated oscillator


.. _questions-2:

Questions:
----------

| What other types of oscillator circuits might be used to generate the 100 KHz square wave?
| The DC reference voltage from the waveform generator output of the ADALM2000 board could be replaced by the band-gap reference circuit from Activity 8 in this series. The +5V supply can be connected where reference input is shown in the diagram and R\ :sub:`1` and R\ :sub:`2` adjusted to produce the desires reference voltage ( where 2+ is shown ) to be used at the plus input of the LM2901 comparator.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a15_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Band gap reference from Activity 9


.. _questions-3:

Questions:
----------

What other types of reference circuits might be used to generate DC voltage needed for the plus input of the comparator?

Appendix: Making an NAND / AND gate with the CD4007 transistor array
====================================================================

Below is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 420px

.. container:: centeralign

   Figure 6 CD4007 CMOS transistor array pinout


As shown in figure 7, one 2 input NAND gate and one inverter can be built from one CD4007 package. Configure the NAND gate as shown below by connecting pins 12 and 13 together as the NAND output. Pin 14 and pin 11 is connected to V\ :sub:`DD` for power and pin 7 V\ :sub:`SS` to ground. Pin 9 should be tied to pin 8 to complete N side of the NAND gate. Pin 6 will be the A input and pin 10 will be the B input.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a15_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7 2 input NAND and Inverter


The Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

An AND gate is made by connecting the output of the NAND at pins 12 and 13 to the inverter input at pin 3.

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
