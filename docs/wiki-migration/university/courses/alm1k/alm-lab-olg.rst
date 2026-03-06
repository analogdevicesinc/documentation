Activity: Op Amp Open Loop Gain and Offset, For ADALM1000
=========================================================

Objective:
----------

This lab activity will use the ADALM1000 to measure the open‐loop gain characteristics of a OP97 opamp using two methods.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

**Open-Loop DC Gain**

Unlike the ideal op amp, a practical op amp has a finite gain. The open-loop DC gain (usually referred to as A\ :sub:`VOL` and sometimes as forward gain) is the gain of the amplifier without the feedback loop being closed, hence the name "open-loop." For a precision op amp this gain can be very high, on the order of 160 dB (100 million) or more. The open loop gain of the OP97 amplifier is somewhere between 1 million and 200 thousand.

Voltage feedback op amps operate as a voltage in / voltage out amplifier and the open-loop gain is a dimensionless ratio, so no units are necessary. However, data sheets sometimes express gain in V/mV or V/μV instead of V/V, for the convenience of using smaller numbers. Or, voltage gain can also be expressed in dB terms, as gain in dB = 20×logA\ :sub:`VOL`. Thus an open-loop gain of 1V/μV ( 1 million V/V ) is equivalent to 120 dB, etc. Be sure to read through the tutorial on Open Loop Gain and Open Loop Gain Nonlinearity ( link below ) before doing these experiments.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – OP97 opamp
| 2 – 100 Ω resistors
| 2 – 4.7 KΩ resistors
| 1 – 470 KΩ resistor ( for optional offset trim )
| 1 – 1 MΩ resistor
| 1 – 10 KΩ potentiometer ( for optional offset trim )

**Method 1**

Construct the circuit shown in figure 1. Before inserting the 1 MΩ and 100 Ω R\ :sub:`1` and R\ :sub:`2` resistors in the circuit, measure and record the values of the two resistors using a DMM if available. Use these measurements to accurately compute the ratio of the input sweep voltage output by CH-A to the attenuated voltage at the opamp non-inverting input ( pin 3 ). Offset trim resistors R\ :sub:`4` and R\ :sub:`5` are optional and may be needed if the offset voltage of the op-amp being tested is too large such that the output voltage does not change over the full range of the CHA output voltage swing.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-olg-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Open-Loop Gain test circuit, Method 1


Procedure:
~~~~~~~~~~

Set AWG CHA output Min voltage to 0 and Max voltage to 5. This will swing the voltage on R\ :sub:`1` from ‐2.5V to +2.5V with respect to the fixed 2.5 V common mode level applied at the inverting input of the opamp through R\ :sub:`3`. Set the frequency to 10 Hz and the shape to sawtooth. Adjust the horizontal time scale to display one full sweep of the sawtooth wave.

From the Curves drop down menu select the CA-V and CB-V traces for display. On the right hand side of the scope screen enter 2.5 for the CA-V and CB-V offset adjustment. This is because in this experiment we are referencing all the measurements to the +2.5 V common rail. Also enter 0 for the CH-A and CH-B vertical position settings ( along bottom of scope screen ). The vertical scale should now be centered on 0 and go from -2.5 to +2.5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-olg-f3.png
   :align: center
   :width: 500px

CH-B will display the output voltage. The open‐loop DC gain of the amplifier is measured by calculating the slope of the output voltage where it changes. The gain is simply the ratio of the change in Vout to the change in Vin. Make sure you take into account the scaling factor of the resistor voltage divider in your circuit when calculating the actual change in Vin ( difference between pins 2 and 3 ).

You may need to modify the settings in the CHA Min and Max values to reduce the sweep range of the CHA input voltage to accurately measure the output voltage swing. It should also be noted that the waveform frequency will likely needed to be adjusted and must be quite low, probably no more than a fraction of 1 Hz because of the low corner frequency of the open-loop gain (around 2 Hz for the OP97).

Reminder: You must take into account the scaling factor of the resistive divider in your circuit when calculating. The program will report values relative to the swept voltage at CHA output, not Vin.

**Method 2**

A second test circuit for measuring DC open-loop gain ( and gain nonlinearity ) is shown in figure 2. The amplifier is configured for a signal gain of –1 by adding input and feedback resistors R\ :sub:`6` and R\ :sub:`7` to the open loop circuit of figure 1 ( be careful to correctly connect pins 2 and 3 ). The open-loop gain is defined as the change in output voltage divided by the change in the input offset voltage ( difference between the voltage seen at pins 2 and 3 ). However, for large values of A\ :sub:`VOL`, the actual offset may change only a few microvolts over the entire output voltage swing. Therefore the divider consisting of the 100 Ω resistor R\ :sub:`2` and R\ :sub:`1` ( 1 MΩ ) forces the node voltage V\ :sub:`Y` to be :

:math:`V_Y=(1+ R_1/R_2)V_OS = 10001 \times V_OS`

The value of R\ :sub:`1` is chosen to result in a voltage at V\ :sub:`Y` measurable by the ALM1000 input channel B depending on the expected values of V\ :sub:`OS`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-olg-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Open-Loop Gain test circuit, Method 2


The +1 to +4 V sawtooth waveform from the channel A output is multiplied by the signal gain, –1, and forces the op amp output voltage V\ :sub:`X` to swing from + 4 V to +1 V. Because of the gain factor applied to the offset voltage, the offset adjust potentiometer, R\ :sub:`5`, is added to allow the initial output offset to be set to zero. Also, note that the waveform frequency must be quite low, probably no more than a fraction of 1 Hz because of the low corner frequency of the open-loop gain (around 2 Hz for the OP97).

Reminder: You must take into account the scaling factor of the resistive divider in your circuit when calculating. The program will report values relative to the swept voltage at CHA output, not Vin.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/opamp_open_loop_gain_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/opamp_open_loop_gain_bb`

**For Further Reading:**

| Here is a good technical paper on how to make :adi:`Simple Op Amp Measurements <en/analog-dialogue/articles/simple-op-amp-measurements.html>`
| :adi:`Open Loop Gain and Open Loop Gain Nonlinearity <media/en/training-seminars/tutorials/MT-044.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
