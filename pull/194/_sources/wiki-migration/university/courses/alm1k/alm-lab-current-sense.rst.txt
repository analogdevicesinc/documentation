Activity: Current Sensing, Difference Amplifiers, For ADALM1000
===============================================================

Objective:
----------

The objective of this lab activity is to investigate current sensing techniques that use an op-amp configured as a difference amplifier.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

In this :doc:`Lab Activity </wiki-migration/university/courses/alm1k/alm-lab-diffamp>` we investigated the difference amplifier. Now we will use it as a current sense amplifier. One of the major applications of the op-amp difference amplifier is in measuring the current at point in a circuit other than where it flows into or out of ground or the common node. The current to be measured is converted into a small voltage by breaking open the current path and inserting a low value resistor in series. This resistor is called a current shunt resistor or just shunt. The resistance is kept small and the voltage drop across the shunt small to reduce any effect this change might have on the operation of the circuit. The small differential voltage drop across the shunt is amplified and converted to a single ended (common referenced) voltage by an op-amp difference amplifier.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 1 – OP484 quad rail to rail amplifier
| 2 – 10 KΩ resistors
| 2 – 100 KΩ resistors
| 1 – 10 Ω resistor
| 1 – 220 Ω resistor
| Various loads, 470 Ω resistor, 2 - 0.1 uF capacitors, 4.7 mH inductor

Directions:
~~~~~~~~~~~

Build the current sense amplifier shown in figure 1. R\ :sub:`6` is added to stabilize the output of the OP484. When using large feedback resistances the OP484 can be unstable due to the large input capacitance of the Channel B input. One input signal ( V\ :sub:`1`, + input of difference amplifier ) is provided directly from the CA-V AWG output to 10 KΩ resistor R\ :sub:`1` and the top of the current shunt resistor R\ :sub:`5`. The other input signal ( V\ :sub:`2` , - input of difference amplifier ) at 10 KΩ resistor R\ :sub:`3` is connected to the bottom of the shunt resistor. The gain of the difference amp is the ratio of R\ :sub:`2`/R\ :sub:`1` (R\ :sub:`4`/R\ :sub:`3` with R\ :sub:`1`\ =R\ :sub:`3`, R\ :sub:`2`\ =R\ :sub:`4`). In this case with R\ :sub:`2` = 100 KΩ and R\ :sub:`1` = 10 KΩ, the gain will be 10. The voltage difference between V\ :sub:`1` and V\ :sub:`2` will appear at V\ :sub:`O` multiplied by 10 and centered on 2.5 V.

The load will consist of different impedances such as a resistor, capacitor or inductor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-current-sense-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Difference Amplifier used to measure I\ :sub:`L`.


Procedure:
~~~~~~~~~~

Set CH-A to SVMI Mode and Shape sine. Set the Min value to 0.5 V and the Max value to 4.5 V. Set the frequency of AWG channel A to 5000 Hz. Set CH-B to Hi-Z mode.

For the first step in the procedure a load will not be connected. With no load I\ :sub:`L` should be zero for all values of CA-V. The voltage difference between V\ :sub:`1` and V\ :sub:`2` should then be zero. With R\ :sub:`2` connected to 2.5 V and V\ :sub:`1` = V\ :sub:`2`, V\ :sub:`O` should also be 2.5 V. Differences from the ideal values of R1-4 along with any input offset of the amplifier will result in V\ :sub:`O` being different ( offset ) from 2.5 V, the zero current reference value. Note and explain any offsets seen on V\ :sub:`O` as CA-V swings from 0.5 V to 4.5 V.

For step two you will connect a 1 KΩ resistor, R\ :sub:`L`, as the load as shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-current-sense-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Measuring current in resistive load.


Use the following ideal formula to calculate the current I\ :sub:`L`.

:math:`I_L= V_O-2.5 / 10R_5` in Amps

With R\ :sub:`5` = 10Ω. Given this value what is the scale factor to convert V\ :sub:`O` in mA/V?

Note the phase difference, if any, between the current and the voltage CA-V. You should save the CB-H trace (V\ :sub:`O`) and the calculated current trace to compare to the results of the following steps and for your lab report.

In step three connect two 0.1 uF capacitors in parallel, C\ :sub:`L`, for a total load of 0.2 uF as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-current-sense-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Measuring current in capacitive load.


Use the same formula to calculate the current from V\ :sub:`O`. Note the phase difference, if any, between the current and the voltage and explain. You should again save the CB-H trace (V\ :sub:`O`) and the calculated current trace to compare to the results of the following steps and for your lab report.

As step four connect a 4.7 mH inductor, L\ :sub:`L` as the load as shown in figure 4. Note that the bottom end of LL is connected to the 2.5 V rail and not ground. A large DC current would flow if it were connected to ground.

Now compare the output (CB-V) trace for this step with your saved output traces from steps 1, 2 and 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-current-sense-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Measuring current in inductive load.


Now compare the output (CB-H) trace for this step with your saved output traces from steps 1, 2 and 3. Include this and the other plots in your lab report.

Extra:
~~~~~~

As an extra check on your results you can turn on the CA-I curve which measures the current flowing in the output of the channel A AWG generator. The measurement made on the ALM1000 board is done in exactly the same way with a shunt resistor but uses the AD8210 current sense amplifier.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/current_sensing_diff_amp_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/current_sensing_diff_amp_ltspice`

**For Further Reading:**

| :adi:`Difference and Current Sense Amplifiers <media/en/training-seminars/tutorials/MT-068.pdf>`
| :adi:`A Deeper Look into Difference Amplifiers <library/analogDialogue/archives/48-02/diff_amp.html>`

**Return to the ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
