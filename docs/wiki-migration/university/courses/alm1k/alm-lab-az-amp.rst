Activity: Auto Zero Amplifier
=============================

Objective:
----------

The objective of this lab activity is to investigate and evaluate a CMOS based input/output offset auto zeroing amplifier technique.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALMM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

For the lowest offset and temperature drift performance, auto zeroing amplifiers may be the only solution. The best bipolar amplifiers offer offset voltages of 25 μV and 0.1 μV/ºC drift. Offset voltages less than 5 μV with practically no measurable offset drift over temperature are obtainable by auto zeroing, albeit with some penalties.

A basic auto zero amplifier circuit is shown in figure 1. When the switches are in the "Z" (auto-zero) position, capacitors C\ :sub:`1` and C\ :sub:`2` are charged to the amplifier input and output offset voltage, respectively. When the switches are in the "S" (sample) position, VIN is connected to VOUT through the path comprised of C\ :sub:`1`, R\ :sub:`1`, the amplifier, R\ :sub:`2`, and C\ :sub:`2`. The switching frequency is usually between a few hundred Hz and several kHz, and it should be noted that because this is a sampling system, the input frequency must be much less than one-half the switching frequency in order to prevent errors due to aliasing. It is also assumed that after a steady state condition is reached, there is only a minimal amount of charge transferred during the switching cycles. The output capacitor, C\ :sub:`3`, and any load, RL, must be chosen such that there is minimal VOUT droop during the auto-zero cycle. The R\ :sub:`3`, C\ :sub:`3` low pass filter minimizes the high frequency clock ripple in the output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab-az-amp-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Auto Zero amplifier block diagram


In this lab activity, a simple un-buffered CMOS inverting stage (such as an inverter made with the CD4007 transistor array, or the CD4069AUB and 74HCU04 un-buffered hex CMOS inverters) and a LTC1043 analog switch are used as elements of an auto zeroed amplifier. Referring to the simulation schematic shown in figure 2, the various functions of this circuit can be identified. Resistors R1 and R2 along with the CMOS inverter form a unity gain inverting amplifier. The simple CMOS inverter stage consisting of M1 and M2 is used as an AC coupled amplifier stage similar to what was looked at in this other :doc:`Activity on CMOS amplifier stages </wiki-migration/university/courses/alm1k/alm-lab-20>`. The LTC1043 analog switch (U1) contains an oscillator that drives the single pole double throw (SPDT) switches. Capacitor C4 sets the oscillator frequency. Switches at pins S1A and S2A function as a SPDT switch, alternately connecting the AC coupled input of the amplifier stage to the input and a common mode level (+2.5V) through pin Ca+. The Input DC offset of the CMOS amplifier is stored on AC coupling capacitor C1.

Switches pins S3A and S4A perform the same function alternately connecting the AC coupled output of the amplifier stage to the output low pass filter (C3 and R3) and a common mode level (+2.5V) through pin Ca-. The output DC offset of the CMOS amplifier is stored on AC coupling capacitor C2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab-az-amp-fig2.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 2, Auto Zero amplifier simulation schematic


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – LTC1043 analog switch
| 1 – CMOS Inverter (CD4007 array, CD4069AUB or 74HCU04 un-buffered hex CMOS inverters)
| 2 – 100 KΩ resistors
| 2 – 20 KΩ resistors
| 2 – 1 uF capacitors
| 2 – 1 nF capacitors
| 2 – 100 pF capacitors

Directions
~~~~~~~~~~

Making an inverter with the CD4007 transistor array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below in figure 3 is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3, CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one that can be configured is shown in figure 4, by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f6.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4, CD4007 CMOS Inverter


A second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

One of These three inverters will be used to construct the CMOS inverter gain stage amplifier in the auto zero amplifier circuit shown in figure.

Making the Auto Zero Amplifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the components on your breadboard as indicated in figure 5. Note that resistor R2 consists of a 100 KΩ in series with a 20 KΩ, capacitor C3 consists of two 1 nF in parallel and capacitor C4 consists of two 100 pF in parallel.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab-az-amp-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Auto Zero Amplifier


AC Amplifier Response to Pulse Modulated Signals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect scope BIN to the output of the AC amplifier stage at. Display the input at (with scope channel 1+) and output the AC Amplifier on the scope. Save the scope waveforms for DC inputs (CHA) for each value from 2.0V, 2.2V, 2.5, 2.7V and 3.0V.

Auto Zero Amplifier DC Transfer Characteristic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Measure the transfer characteristic (DC gain) of the chopper amplifier by applying DC voltages between about 1.5 V and +3.5 V to the input and measuring the output. This can be done manually using generator AWGA with a DC wave shape and setting the Max value. Be sure to take sufficient data to determine the linear and nonlinear ranges of the transfer characteristic. To reduce data taking time, try using the waveform generator to provide a very low frequency (< 100 Hz) triangle signal. For example, a 1.5V Min and 3.5V Max setting.

Amplifier Frequency Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Apply a sinusoidal signal of 200mV amplitude with zero offset voltage to the input and measure the gain of the entire system from 10 Hz to 20 KHz. Use the Bode Plotting tool to plot gain and phase vs. frequency for the entire system, paying special attention to the 1KHz to 20KHz range and the region near the frequency of the chopping clock.

Auto Zero Amplifier Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Present the waveforms taken for the AC Amplifier in response to DC inputs. Discuss and explain the salient features of this response.

Plot or present the DC transfer characteristic of the auto zero amplifier. Discuss and explain the salient features of this characteristic. Was the output of the auto zero amplifier what you expected? Make a Bode plot (gain/phase versus frequency) of the auto zero amplifier from the data taken above. Comment on the bandwidth of the auto zero amplifier and the gain near the chopping frequency.

Appendix:
~~~~~~~~~

Optionally a CMOS inverter could be constructed from the discrete NMOS and PMOS transistors from ADALP2000:

| 1 – VZN2110A NMOS transistor
| 1 – VZP2110A PMOS transistor
| 1 – 1.5KΩ resistor

As shown in figure A1, NMOS transistor M\ :sub:`1` is a VZN2110A and PMOS transistor M\ :sub:`2` is a VZP2110A. Because the NMOS transistor is much stronger (with V\ :sub:`DD`/2 as the gate source voltage) than the PMOS transistor, a 1.5 KΩ resistor, R\ :sub:`4`, is added in series with its source. Everything else is the same as in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab-az-amp-figa1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A1.


LTspice compatible model files for the ZVN2110A and ZVP2110A are include below:

**ZVN2110A Spice Model .lib file**

::

   *ZETEX ZVN2110A Spice Model v1.1 Last Revised 3/5/00
   *
   .SUBCKT ZVN2110A 3 4 5 5
   *               D G S BG
   M1 3 2 5 5 MN2110a
   M2 3 2 5 5 MN2110b
   RG 4 2 200
   RL 3 5 1E9
   C1 2 5 50E-12
   C2 3 2 5E-12
   D1 5 3 DN2110a
   *
   .MODEL MN2110a NMOS VTO=2 RS=.1 RD=1.8 IS=1E-15 KP=0.3
   +CBD=60E-12 PB=1 LAMBDA=2.6E-3
   .MODEL MN2110b NMOS VTO=0.9 RS=2 KP=0.1 PB=1 LAMBDA=2.6E-3
   .MODEL DN2110a D IS=1E-12 RS=0.37
   .ENDS ZVN2110A
   *

**ZVP2110A Spice Model .lib file**

::

   *ZETEX ZVP2110A Spice Model v1.0 Last Revised 23/7/04
   *
   .SUBCKT ZVP2110A 3 4 5 5
   *                D G S
   M1 13 20 5 5 Pmod1
   RG 4 2 65
   RIN 2 5 1E9
   RL 3 5 1.2E8
   RD 3 13 Rmod1 2.5
   C1 2 5 140E-12
   **C2 3 2 15E-12
   D1 3 5 Dmod1
   D2 3 17 Dmod2
   Egs1 2 17 2 5 1
   Egt1 2 20 5 21 1
   Vgt1 5 22 1
   Igt1 5 21 1
   Rgt 21 22 Rmod2 1
   .MODEL Pmod1 PMOS VTO=-2.8 RS=2 IS=1E-15 KP=0.17
   +CBD=105E-12 PB=1 LAMBDA=6E-3
   .MODEL Dmod1 D IS=5E-12 RS=1
   .MODEL Dmod2 D CJO=60e-12 IS=1e-30 N=10
   .MODEL Rmod1 RES (TC1=8e-3 TC2=4.2E-5)
   .MODEL Rmod2 RES (TC1=-2e-3 TC2=3e-6)
   .ENDS ZVP2110A
   *

**For Further Reading:**

:adi:`Chopper Stabilized (Auto-Zero) Precision Op Amps (MT-055) <MT-055>`

**Return to Lab Activity Table of Contents**
