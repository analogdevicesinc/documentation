Activity: The Phase Locked Loop - ADALM2000
===========================================

Objective:
----------

This Lab activity is an introduction to Phase Locked Loops ( PLL ). The phase locked loop circuit has a number of important applications, such as signal modulation/demodulation (mainly frequency and phase modulation), synchronization, clock and data recovery, as well as frequency multiplication and synthesis. In this activity you will set up a simple PLL circuit to gain basic understanding of PLL operation.

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
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 2.2 KΩ Resistor
| 1 - 47 KΩ Resistor
| 1 - 10 KΩ Resistor
| 1 - 4.7 nF capacitor (marked 472)
| 1 - 100 pF capacitor (marked 101)
| 1 - CD4007 CMOS array
| 2 - ZVN2110A NMOS transistors
| 2 - ZVP2110A PMOS transistors
| 1 - AD654 voltage to frequency converter
| 1 - 9 Volt battery ( with connector )

Step 1 Directions:
------------------

On your solder-less breadboard first construct the VFC circuit based on the AD654 shown in figure 2. Build the circuit to one side of your breadboard to leave space for the other parts of the PLL we will be adding in later steps of this lab activity. The control voltage is applied through a single pole low pass filter R\ :sub:`1` and C\ :sub:`1`. This is equivalent to the low pass filter block which feeds the VCO block in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a31_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Voltage to Frequency converter circuit


Hardware Setup:
---------------

Turn on the fixed +5 volt power supply and connect the 9 volt battery to your circuit. Connect AWG1 output to V\ :sub:`IN` as shown in figure 2. Configure AWG1 as a DC source and set it to 2.5 V initially. Connect scope channel input CH1+ to the V\ :sub:`SQR` output as shown in figure 2. You should ground the CH1- input as well.


|image1|

.. container:: centeralign

   Figure 3, Voltage to Frequency converter breadboard circuit


Procedure:
----------

Using the AWG 1 DC offset controls adjust the voltage at V\ :sub:`IN` from 1.0 V to 4.0 V while observing the frequency of the VFC output at V\ :sub:`SQR`. Use the Frequency Measurement feature on the scope control screen to do this. R\ :sub:`t` and C\ :sub:`t` in figure 2 set the nominal output frequency of the VFC according to the formula below.

:math:`F_SQR = V_IN / (10 R_t C_t)`

For example with V\ :sub:`IN` set in the middle of the range at 2.5V and the given R\ :sub:`t` C\ :sub:`t` values, (2.5/(10 \* 10KΩ \*100pF), the output frequency should be near 250 KHz. Verify that your measurements agree with this value. If not recheck your circuit connections and component values.


|image2|

.. container:: centeralign

   Figure 4, Voltage to Frequency converter output


Questions:
----------

Step 2 Directions:
------------------

Next add the XOR gate phase detector circuit from the earlier Lab [1] on you breadboard as shown in figure 5. After constructing the XOR gate connect it to the V to F circuit as shown in figure 6 to make the complete PLL. Be sure to turn off the +5 V power supply and disconnect the 9 volt battery before making any additions to your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a31_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Adding XOR phase detector


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a31_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Complete PLL circuit


.. _hardware-setup-1:

Hardware Setup:
---------------

Turn on the fixed +5 volt power supply and connect the 9 volt battery to your circuit. Connect AWG1 output to F\ :sub:`REF` as shown in figure 4. Configure AWG1 as a square wave with an amplitude of 5 V peak-to-peak and an offset of 2.5 V ( 0 to 5 V swing ) and initially set the frequency to what you measured in step 1 when V\ :sub:`IN` was set to 2.5 V ( should be around 250 KHz ). Connect scope channel input CH1+ to the F\ :sub:`REF` input and scope channel CH2+ to V\ :sub:`SQR` output as shown in figure 6. You should ground the CH1- and CH2- inputs as well. Set the scope to trigger off the rising edge of channel 1 ( the F\ :sub:`REF` signal ).


|image3|

.. container:: centeralign

   Figure 7, Complete PLL breadboard circuit


.. _procedure-1:

Procedure:
----------

With F\ :sub:`REF` set to the frequency corresponding to a control voltage of 2.5 volts on pin 4 of the AD654 the output frequency seen at V\ :sub:`SQR` should be locked to the input reference frequency F\ :sub:`REF`. On the scope screen you should see that the two square waves are stable ( i.e. locked to each other ) and V\ :sub:`SQR` is shifted approximately 90º with respect to F\ :sub:`REF`. Remember that the filtered output of the XOR phase detector will be at one half of its output range or about 2.5 V when its two inputs are 90º apart in phase,


|image4|

.. container:: centeralign

   Figure 8: Complete PLL F\ :sub:`REF` and V\ :sub:`SQR` plot


Increase and decrease the reference frequency, F\ :sub:`REF`, in small increments to determine the minimum and maximum frequency the PLL will lock to. Note the relative phase difference between F\ :sub:`REF` and V\ :sub:`SQR` while you are changing the frequency of the reference input. While doing this also measure the filtered DC control voltage seen on pin 4 of the AD654 and compare these readings to what you measured in step 1 when sweeping the DC control voltage of the VFC.

Connect scope channel 2 to the output of the XOR gate at point C in figure 6. Compare the square wave you see to those seen at the inputs of the XOR gate A (V\ :sub:`SQR`) and B (F\ :sub:`REF`). How does the shape of the waveform at C change when the PLL is locked to the minimum and maximum Lock frequency vs the frequency in the center of the lock range?

Bonus Step 3 Directions:
------------------------

The simple PLL circuit of figure 4 is not very interesting in that the output signal is just a phase shifted version of the input signal. If we insert a digital divider block in the feedback path from the VFC output to the phase detector input as we saw back in figure 1 then the output signal will be at a higher multiplied frequency. Using any digital divider IC you might have available such as a CD4020, CD4040, CD4060 or even SN7490 ( just about any divider chip will do ) open the connection to XOR input A and insert the divider block as shown in figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a31_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, PLL frequency multiplier


Depending on the divide factor N of the particular divider you build you will need to change the F\ :sub:`REF` input frequency by that amount. For example with N = 8, if F\ :sub:`REF` was 250 KHz before the new F\ :sub:`REF` would be 250/8 or 31.25 KHz. The frequency of the pulses at the output of the XOR gate phase detector will also be 8 times lower.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/phase_locked_loop_bb`
   


**For Further Reading:**

[1] :doc:`Activity: CMOS Logic Circuits, Transmission Gate XOR </wiki-migration/university/courses/electronics/electronics-lab-30>`

| :adi:`MT-086.pdf <static/imported-files/tutorials/MT-086.pdf>`
| `Phase-locked_loop <https://en.wikipedia.org/wiki/Phase-locked_loop>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/pll_voltage_to_frequency_converter_hardware_setup.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/pll_voltage_to_frequency_converter_scopyshot1.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/PLL_Complete_PLL_Circuit_Hardware_Setup.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/pll_complete_pll_circuit_scopeshot1.png
