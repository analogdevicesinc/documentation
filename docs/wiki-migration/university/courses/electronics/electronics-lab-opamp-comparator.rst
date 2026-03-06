Activity: Op Amp as Comparator, For ADALM2000
=============================================

Objective:
----------

In this lab we introduce the operational amplifier (op amp) in switching mode configuration, obtaining a op-amp voltage comparator behavior. The voltage comparator circuit has the purpose of highlighting via two different states of the output voltage, the relative state of the two input voltage. The comparison is made using the sign of the difference between the two input voltages, while response is one of the two possible output values, dependent on the sign of that specific difference.

Background:
-----------

The op-amp as a "comparator":
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider an op-amp used to amplify a signal without feedback as shown in figure 1a. Because no feedback is used, the input signal is amplified by the full open-loop gain of the op-amp. Even a very small input voltage (less than a millivolt either side of Vth) will be enough to drive the output to either the minimum or maximum output voltage, as shown in the plots of Vin and Vout. Thus, in this case because the op-amp -Input is connected to Vth, the output represents the sign of Vin ( "0" if Vin < Vth, "1" if Vin > Vth ) 1, and the circuit is like a one-bit analog to digital converter (ADC), and functions like a voltage comparator.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-comp-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1a, An op-amp used as a comparator


Op Amps and comparators may seem interchangeable at first glance based on their symbols and pinouts. The Analog Parts Kits is supplied with a variety of op-amps and the AD8561 high speed voltage comparator that was used in other activities. Some designers might be tempted to use or substitute readily available op amps as voltage comparators in their projects. There are very important differences however. Comparators are designed to work without negative feedback or open-loop, they are generally designed to drive digital logic circuits from their outputs, and they are designed to work at high speed with minimal instability. Op amps are not generally designed for use as comparators, their input structures may saturate if over-driven which may cause it to respond comparatively slowly. Many have input stages which behave in unexpected ways when driven with large differential voltages or beyond the specified common mode range. In fact, in many cases, the differential input voltage range of an op amp is limited or clamped to prevent damage to the input stage devices. Note this article on ":adi:`Amplifier Input Protection... Friend or Foe? <en/analog-dialogue/articles/amplifier-input-protection-friend-or-foe.html>`" for more background on this issue.

.. important::

   Warning: Using op-amps with built-in input clamps as a voltage comparator may damage the IC!


Yet many designers still try to use op amps as comparators. While this may work in some cases at low speeds and low resolutions, many times the results are not satisfactory. Not all of the issues involved with using an op amp as a comparator can be resolved by reference to the op amp datasheet, since op amps are not intended for use as comparators.

The most common issues are speed (as we have already mentioned), the effects of input structures (protection diodes, phase inversion in FET amplifiers such as the ADTL082, and many others), output structures which are not intended to drive logic, hysteresis and stability, and common-mode effects.

For an op-amp comparator we can consider a single input v\ :sub:`D` as the difference betwee v\ :sup:`+` and v\ :sup:`-`. Therefore, the output voltage V\ :sub:`O` can get one of the two possible values:

-  V\ :sub:`O` = V\ :sub:`OH` (High), meaning that v\ :sup:`+` > v\ :sup:`-` (v\ :sub:`D` > 0)
-  V\ :sub:`O` = V\ :sub:`OL` (Low), meaning that v\ :sup:`+` < v\ :sup:`-` (v\ :sub:`D` < 0)

We consider the threshold voltage V\ :sub:`Th` as the particular value/values of the intput voltage v\ :sub:`I` for which the switching at the output takes place. (setting v\ :sub:`D` = 0).

Two main types of voltage comparators are to be considered:

-  Simple comparators - without feedback and with only one threshold voltage
-  Hysteresis comparators - with positive feedback and two threshold voltages

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 3 10 kΩ resistor
| 1 20 kΩ resistor
| 1 OP97 ( Low slew rate amplifier supplied with the recent versions of ADALP2000 Analog Parts Kit )

Simple Comparator
-----------------

.. _background-1:

Background:
^^^^^^^^^^^

The high intrinsic gain of the op-amp and the output saturation effects can be exploited by configuring the op-amp as a comparator as in figure 1. This is essentially a binary-state decision-making circuit: if the voltage at the “+” terminal is greater than the voltage at the “-” terminal, Vin > Vref , the output goes “high” (saturates at its maximum value). Conversely if Vin < Vref the output goes “low”. The circuit compares the voltages at the two inputs and generates an output based on the relative values. Unlike all the previous circuits there is no feedback between the input and output; we say that the circuit is operating “open-loop”.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 1 Op-Amp as Comparator


Hardware Setup:
^^^^^^^^^^^^^^^

Comparators are used in different ways, and in future sections we will see them in action in several labs. Here we will use the comparator in a common configuration that generates a square wave with a variable pulse width:

Start by shutting off the power supplies and assemble the circuit. As with the summing amplifier circuit earlier, use the second waveform generator output for the DC source Vref , and turn the amplitude to zero and the output offset all the way down so that you can adjust up from zero during the experiment.

Again configure the waveform generator Vin for a 2V amplitude peak-to-peak sine wave at 1 kHz. With the power supply on and Vref at zero volts, export the output waveform.

Now slowly increase Vref and observe what happens. Record the output waveform for Vref = 1V. Keep increasing Vref until it exceeds 2V and observe what happens. Can you explain this?

Repeat the above for a triangular input waveform and record your observations for your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/simple_comp-bb.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 2. Comparator Breadboard Circuit


Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 2V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

A plot example is presented in Figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/comp_amp-waveform.png

.. container:: centeralign

   Figure 3. Comparator Waveforms


Hysteresis Comparator
---------------------

Hysteresis is the dependence of a system's current state on previous values of quantities determining it. The output value is not a strict function of the corresponding input, but also incorporates some lag, delay, or history dependence. In particular, the response for a decrease in the input variable is different from the response for an increase in the input variable.

In this configuration, there are two threshold values V\ :sub:`ThH` and V\ :sub:`ThL` with two output values V\ :sub:`OH` and V\ :sub:`OL`. The threshold values should depend on the output value which is fed back to the input and contributes to the threshold values (positive feedback). Via a resistive divider, a fraction of the output voltage is fed back to the non-inverting input.

When analyzing hysteresis comparators, we have to take into consideration the moving direction of the hysteresis and the fact that at a certain moment only one threshold is active.

The input signal triggers the switching of the output, switching process being sustained by the positive feedback.

Non-inverting hysteresis Comparator
-----------------------------------

.. _background-2:

Background:
^^^^^^^^^^^

Consider the circuit presented in Figure 4.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 4 Non-Inverting hysteresis comparator


For the non-inverting hysteresis comparator circuit in Figure 4, Vin is applied to the non-inverting input of the op-amp. Resistors R1 and R2 form a voltage divider network across the comparator providing the positive feedback with part of the output voltage appearing at the non-inverting input along with the Vin via the same resistive divider.

The amount of feedback is determined by the resistive ratio of the two resistors used (in this particular situation, the ratio will be :math:`\displaystyle \frac{1}{2}` ).

We can compute the threshold voltages as follows:

.. container:: centeralign

   :math:`v_D=v^+ - v^- = (R_1/(R_1+R_2))v_out + (R_2/(R_1+R_2))v_In - 0`


Considering v\ :sub:`D`\ =0, v\ :sub:`in`->V\ :sub:`Th`, we obtain the following thresholds:

.. container:: centeralign

   :math:`V_ThL = -(R_1/R_2)V_OH`


.. container:: centeralign

   :math:`V_ThH = -(R_1/R_2)V_OL`


.. _hardware-setup-1:

Hardware Setup:
^^^^^^^^^^^^^^^

Build the following breadboard circuit for the non-inverting hysteresis comparator.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 5. Non-Inverting hysteresis comparator breadboard circuit


.. _procedure-1:

Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 6V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

A plot example is presented in Figure 6.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 6. Non-Inverting hysteresis comparator Waveform


.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   Figure 7. Non-Inverting hysteresis comparator XY plot


In Figure 7. you can observe the voltage transfer charactersitic of the non-inverting hysteresis comparator (the arrows drawn indicate the flow of the signal with respect to the thresholds).

Inverting Hysteresis Comparator
-------------------------------

.. _background-3:

Background:
^^^^^^^^^^^

Consider the circuit presented in Figure 8.

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   Figure 8. Inverting hysteresis comparator


For the inverting hysteresis comparator circuit in Figure 8, Vin is applied to the inverting input of the op-amp. Resistors R1 and R2 form a voltage divider network across the comparator providing the positive feedback with part of the output voltage appearing at the non-inverting input.

The amount of feedback is determined by the resistive ratio of the two resistors used (in this particular situation, the ratio will be :math:`\displaystyle \frac{1}{2}` ).

We can compute the threshold voltages as follows:

.. container:: centeralign

   :math:`v_D=v^+ - v^- = (R_1/(R_1+R_2))v_out- v_In`


Considering v\ :sub:`D`\ =0, v\ :sub:`in`->V\ :sub:`Th`, we obtain the following thresholds:

.. container:: centeralign

   :math:`V_ThL = (R_1/(R_1+R_2))V_OL`


.. container:: centeralign

   :math:`V_ThH = (R_1/(R_1+R_2))V_OH`


.. _hardware-setup-2:

Hardware Setup:
^^^^^^^^^^^^^^^

Build the following breadboard circuit for the inverting hysteresis comparator.

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   Figure 9. Inverting hysteresis comparator breadboard circuit


.. _procedure-2:

Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 6V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

A plot example is presented in Figure 10.

.. container:: centeralign

   \ |image8|\


.. container:: centeralign

   Figure 10. Inverting hysteresis comparator Waveform


.. container:: centeralign

   \ |image9|\


.. container:: centeralign

   Figure 11. Inverting hysteresis comparator XY plot


In Figure 11. you can observe the voltage transfer characteristic of the non-inverting hysteresis comparator (the arrows drawn indicate the flow of the signal with respect to the thresholds).

Inverting Hysteresis Comparator with asymmetric thresholds
----------------------------------------------------------

.. _background-4:

Background:
^^^^^^^^^^^

Consider the circuit presented in Figure 12.

.. container:: centeralign

   \ |image10|\


.. container:: centeralign

   Figure 12. Inverting hysteresis comparator with asymmetric thresholds


For the inverting comparator with asymmetric thresholds circuit in Figure 12, an additional reference voltage Vref is used. Resistors R1 and R2 form a voltage divider network across the comparator providing the positive feedback with part of the output voltage appearing at the non-inverting input, along with a part of the Vref going through the same divider.

We can compute the threshold voltages as follows:

.. container:: centeralign

   :math:`v_D=v^+ - v^- = (R_1/(R_1+R_2))v_out + (R_2/(R_1+R_2))v_Ref - v_In`


Considering v\ :sub:`D`\ =0, v\ :sub:`in`->V\ :sub:`Th`, we obtain the following thresholds:

.. container:: centeralign

   :math:`V_ThL = (R_1/(R_1+R_2))V_OL + (R_2/(R_1+R_2))v_Ref`


.. container:: centeralign

   :math:`V_ThH = (R_1/(R_1+R_2))V_OH + (R_2/(R_1+R_2))v_Ref`


.. _hardware-setup-3:

Hardware Setup:
^^^^^^^^^^^^^^^

Build the following breadboard circuit for the inverting hysteresis comparator.

.. container:: centeralign

   \ |image11|\


.. container:: centeralign

   Figure 13. Inverting hysteresis comparator with asymmetric thresholds breadboard


.. _procedure-3:

Procedure:
^^^^^^^^^^

Use the first waveform generator as source Vin to provide a 6V amplitude peak-to-peak, 1 kHz sine wave excitation to the circuit and second waveform generator as constant 1V voltage reference. Supply the op amp to +/- 5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

A plot example is presented in Figure 14.

.. container:: centeralign

   \ |image12|\


.. container:: centeralign

   Figure 14. Inverting hysteresis comparator with asymmetric thresholds Waveform


.. container:: centeralign

   \ |image13|\


.. container:: centeralign

   Figure 15. Inverting hysteresis comparator with asymmetric thresholds XY plot


In Figure 15. you can observe the voltage transfer characteristic of the non-inverting hysteresis comparator (the arrows drawn indicate the flow of the signal with respect to the thresholds).

Questions
---------

-  Compute the threshold voltages for all four comparator setups (simple, non-inverting hysteresis, inverting hysteresis, asymmetric thresholds) and compare the results with the ones obtained from the experimental setups.

Extra Activities
----------------

For experimenters who finish early or want an additional challenge, see if you can modify the comparator circuit using your red and green LEDs (from the last lab) at the output so that the red LED lights for negative voltages and the green LED lights for positive voltages. Turn down the frequency to 1Hz (or less) so you can see them turn on-and-off in real time. Don’t forget that the LEDs will need a current-limiting resistor so that the current through it is no more than 20mA.

You can also extend the above example to a circuit with multiple voltage levels as the circuit presented in Figure 16.

.. container:: centeralign

   \ |image14|\


.. container:: centeralign

   Figure 16. Voltage Level Indicator using LEDs


.. _materials-1:

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 3 470 Ω resistor
| 1 10 kΩ resistor
| 2 20 kΩ resistor
| 3 LED (red, green, yellow)
| 1 ADTL082 (2 integrated Op-amps)
| The circuit uses a divider (R\ :sub:`1`, R\ :sub:`2`, R\ :sub:`3`) to obtain one threshold for each of the two comparators. Based on these thresholds and the input voltage, one LED (D\ :sub:`1`, D\ :sub:`2`, D\ :sub:`3`) at a time will be on.

Exercises:

1. Compute the threshold voltages according to the circuit in Figure 16. Determine for each input voltage range which LED will be on.

2. Build the breadboard circuit. Supply the op amp to +/- 5V from the power supply. Use the first channel of the Signal Generator to generate the variable input voltage (V\ :sub:`in`) and the second channel to generate the 5V constant reference voltage.

.. container:: centeralign

   \ |image15|\


.. container:: centeralign

   Figure 17. Voltage Level Indicator using LEDs


Vary the input voltage from 0 to 5V and observe the LEDs' behavior.

This type of circuit is also known as Window Comparator. An an application on this subject can be found in the activity: :doc:`Temperature Control using Window Comparator </wiki-migration/university/courses/electronics/electronics-lab-window-comp-tmp01>`

.. admonition:: Download
   :class: download

   \*\* Lab Resources:\*\*

   
   -  LTSpice files: :git-education_tools:`m2k/ltspice/opamp_comp_ltspice`
   -  Fritzing files: :git-education_tools:`m2k/fritzing/opamp_comp_bb`
   


Further Reading
~~~~~~~~~~~~~~~

Some additional resources on Op Amps as Comparators:

-  :adi:`AN-849 - Using Op Amps as Comparators <media/en/technical-documentation/application-notes/AN-849.pdf>`
-  :adi:`Ask The Applications Engineer—31: Amplifiers as Comparators? <en/analog-dialogue/articles/amplifiers-as-comparators.html>`
-  :adi:`Curing Comparator Instability with Hysteresis <en/analog-dialogue/articles/curing-comparator-instability-with-hysteresis.html>`
-  :adi:`Comparators & Op Amps—May They Never Meet <en/analog-dialogue/raqs/raq-issue-11.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/simple_comp.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/noninv_hys_comp.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/non_inv_hys_com-bb.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/non_inv_hys_comp-wav.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/non_inv_hys_comp-xy.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_comp.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_com-bb.png
   :width: 900px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_comp-wav.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_comp-xy.png
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_comp_asy_th.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_com_asyth-bb.png
   :width: 900px
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_comp_asyth-wav.png
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/inv_hys_comp_asyth-xy.png
   :width: 500px
.. |image14| image:: https://wiki.analog.com/_media/university/courses/electronics/voltagelevelindicatorusingled.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/university/courses/electronics/optic_indicator_vlevel-bb.png
   :width: 900px
