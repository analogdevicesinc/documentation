Activity: The Phase Locked Loop - ADALM1000
===========================================

Objective:
----------

This Lab activity is an introduction to Phase Locked Loops (PLL). The phase locked loop circuit has a number of important applications, such as signal modulation/demodulation (mainly frequency and phase modulation), synchronization, clock and data recovery, as well as frequency multiplication and synthesis. In this activity you will set up a simple PLL circuit to gain basic understanding of PLL operation.

General Notes:
--------------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A phase-locked loop (PLL) is a feedback system that acts to adjust or lock the phase difference between the output of a voltage-controlled oscillator (VCO) and an input reference signal as shown in figure 1. A VCO is an oscillator whose output frequency is a function of some input control voltage. Generally when a VCO is used in a feedback loop like a PLL the voltage to frequency transfer function must at least be monotonic. A special case of a VCO is the voltage-to-frequency converter (VFC) where the voltage/frequency characteristic is linear. The divide factor N of the frequency divider in the feedback loop is generally an integer number including 1, which is the same as having no divider or a direct connection from the VCO output to the input of the phase detector.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a31_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1. Basic PLL block diagram


Phase-locked loops are the subject of many in depth books and much discussion and are far too complex to deal with exhaustively in these few pages. The reader is referred to some of the additional reading materials linked to at the end of this lab for further understanding.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 – 1.5 KΩ Resistor
| 1 – 47 KΩ Resistor
| 1 – 4.7 KΩ Resistor
| 1 – 4.7 nF capacitor (marked 472)
| 1 – 1nF pF capacitor (marked 102)
| 1 – XOR gate (74HC86 or See Appendix for other XOR circuit options)
| 1 – AD654 voltage to frequency converter

Step 1 Directions:
~~~~~~~~~~~~~~~~~~

On your solder-less breadboard first construct the VFC circuit based on the AD654 shown in figure 2. Build the circuit to one side of your breadboard to leave space for the other parts of the PLL we will be adding in later steps of this lab activity. The control voltage is applied through a single pole low pass filter R\ :sub:`1` and C\ :sub:`1`. This is equivalent to the low pass filter block which feeds the VCO block in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-pll-1-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Voltage to Frequency converter circuit


Hardware Setup:
~~~~~~~~~~~~~~~

Connect the fixed +5 volt power supply. Connect CH-A output to VIN as shown in figure 2. Configure CH-A as a DC source and set it to 2.5 V initially. Connect scope channel B input set in Hi-Z mode, CB-H, to the V\ :sub:`SQR` output as shown in figure 2.

Procedure:
~~~~~~~~~~

Using the CH-A DC Max controls adjust the voltage at V\ :sub:`IN` from 0.0 V to 3.0 V while observing the frequency of the VFC output at V\ :sub:`SQR`. Use the Frequency Measurement feature Meas menu to do this. R\ :sub:`t` and C\ :sub:`t` in figure 2 set the nominal output frequency of the VFC according to the formula below.

:math:`F_SQR = V_IN / (10V R_t C_t)`

For the values of R\ :sub:`t` and C\ :sub:`t` given in figure 2 the output frequency should be between 20 KHz and 25 KHz when V\ :sub:`IN` is set to 2.5 V. Verify that your measurements agree with this value. If not recheck your circuit connections and component values.

Questions:
~~~~~~~~~~

Step 2 Directions:
~~~~~~~~~~~~~~~~~~

Next add the XOR gate phase detector circuit from an earlier Lab on you breadboard as shown in figure 3. After constructing the XOR gate connect it to the V to F circuit as shown in figure 4 to make the complete PLL. Be sure to turn off or disconnect the +5 V power supply before making any additions to your circuit. An XOR gate from a 74HC86 can be substituted if available. Or build an XOR gate using Inverters, AND, OR gates as in this :doc:`lab </wiki-migration/university/courses/alm1k/intro/basic-logic-gates-1>`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-pll-1-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Adding XOR phase detector


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-pll-1-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Complete PLL circuit


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Connect the fixed +5 volt power supply to your circuit. Connect CHA output to F\ :sub:`REF` as shown in figure 4. Configure CH-A as a square wave with a Min value of 0 V and a Max of 5 V (0 to 5 V swing) and initially set the frequency to what you measured in step 1 when V\ :sub:`IN` was set to 2.5 V (should be around 22 KHz). Connect scope channel CH-B to V\ :sub:`SQR` output as shown in figure 4. Set the scope to trigger off the rising edge of channel A (the F\ :sub:`REF` signal).

.. _procedure-1:

Procedure:
~~~~~~~~~~

With F\ :sub:`REF` set to the frequency corresponding to a control voltage of 2.5 volts on pin 4 of the AD654 the output frequency seen at V\ :sub:`SQR` should be locked to the input reference frequency F\ :sub:`REF`. On the scope screen you should see that the two square waves are stable (i.e. locked to each other) and V\ :sub:`SQR` is shifted approximately 90º with respect to F\ :sub:`REF`. Remember that the filtered output of the XOR phase detector will be at one half of its output range or about 2.5 V when its two inputs are 90º apart in phase,

Increase and decrease the reference frequency, F\ :sub:`REF`, in small increments to determine the minimum and maximum frequency the PLL will lock to. Note the relative phase difference between F\ :sub:`REF` and V\ :sub:`SQR` while you are changing the frequency of the reference input. While doing this also measure the filtered DC control voltage seen on pin 4 of the AD654 and compare these readings to what you measured in step 1 when sweeping the DC control voltage of the VFC.

Connect scope channel BIN to the output of the XOR gate at point C in figure 4. Compare the square wave you see to those seen at the inputs of the XOR gate A (V\ :sub:`SQR`) and B (F\ :sub:`REF`). How does the shape of the waveform at C change when the PLL is locked to the minimum and maximum Lock frequency vs the frequency in the center of the lock range?

Bonus Step 3 Directions:
~~~~~~~~~~~~~~~~~~~~~~~~

The simple PLL circuit of figure 4 is not very interesting in that the output signal is just a phase shifted version of the input signal. If we insert a digital divider block in the feedback path from the VFC output to the phase detector input as we saw back in figure 1 then the output signal will be at a higher multiplied frequency. Using any CMOS digital divider IC you might have available such as a CD4020, CD4040 or CD4060 (just about any divider chip will do) open the connection to XOR input A and insert the divider block as shown in figure 5. One of the D flip-flops of the 74HC273 octal register and an inverter from the 74HC04 can be wired up as a divide by 2 circuit (i.e. a toggle flop), see figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-pll-1-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, PLL frequency multiplier


Depending on the divide factor N of the particular divider you build you will need to change the F\ :sub:`REF` input frequency by that amount. For example with N = 8, if F\ :sub:`REF` was 24 KHz before the new F\ :sub:`REF` would be 24/8 or 3 KHz. The frequency of the pulses at the output of the XOR gate phase detector will also be 8 times lower and the RC low pass filter time constant will probably need to also increase by a factor of 8.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-pll-1-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, 74HC273 as divide by 2, 4, 8


The divide by two circuit from the :doc:`BJT Multivibrator Lab Activity </wiki-migration/university/courses/alm1k/alm-lab-24>` could also be used as well and can be built from parts contained in the ADALP2000 Parts Kit.

**For Further Reading:**

| :adi:`Fundamentals of Phase Locked Loops (PLLs) <static/imported-files/tutorials/MT-086.pdf>`
| `Phase-locked loop <https://en.wikipedia.org/wiki/Phase-locked_loop>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`
