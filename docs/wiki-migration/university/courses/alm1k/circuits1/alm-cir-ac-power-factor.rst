Activity: Power and Power Factor in AC circuits, For ADALM1000
==============================================================

Objective:
----------

In this lab activity you will determine real, reactive, and apparent power in RC, RL and RLC circuits. You will also determine the amount of capacitance that is required to correct the power factor in a series RL circuit.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

For time varying voltages and currents, the power delivered to a given load also varies with time. This time varying power is called instantaneous power. The power at any instant in time can be either positive or negative. That is to say power is going into the load and being dissipated as head or stored in the load as energy when positive and coming out of the load ( from the stored energy in the load ) when negative. The real (or actual) power delivered to the load is the average value of the instantaneous power.

For AC sinusoidal voltages and currents, the real power (P), in units of Watts, dissipated in an RC, RL or RLC load circuit is dissipated in only the resistance part. There is no real power dissipated in an ideal reactive element like a capacitor or inductor. In a reactive element, energy is stored during half of the AC cycle and released (sourced) during the other half of the cycle. The power in a reactive element is referred to as reactive power (Q) and has the units of vars (Volt-Amps-Reactive).

The real power (P) dissipated in a load can be calculated as follows:

:math:`P = I^2 R`

Where R is the resistive part of the load and I is the (True) RMS current.

The reactive power in a load can be calculated as follows:

:math:`Q = I^2 X`

Where X is the reactance of the load and I is the AC RMS current.

When a load has an AC RMS voltage (V) across it and an AC RMS current (I) through it, the apparent power (S) is the product of the RMS voltage and RMS current in Volt-Amperes (VA). The apparent power can be calculated as follows:

:math:`S = V I`

If the load has both resistive and reactive parts, apparent power represents neither real power or reactive power. It is called apparent power because it uses the same equation as DC power but does not take into account the possible phase difference between the voltage and current waveforms.

A power triangle (vector diagram) can be drawn using the real, reactive and apparent power. The real power is along the horizontal axis, the reactive power is along the vertical axis and the apparent power forms the hypotenuse of the triangle as shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-pf-f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Power triangle


Using geometry, S can be calculated by:

:math:`S = sqrt(P^2 + Q^2)`

Cosine of the angle θ is defined as the power factor (pf). The power factor is the ratio of the real power (P) to the apparent power (S) and is calculated as follows:

:math:`pf – cos \theta = P/S = P/(VI)`

Where θ is the phase difference between the voltage waveform (across the load) and the current waveform (through the load). The power factor is thought of as lagging when the load current lags the load voltage (inductive) and leading when the load current leads the load voltage (capacitive).

The real power can also be found from the apparent power by multiplying the apparent power by the power factor:

:math:`P = VI cos \theta`

The real power in Watts, dissipated in the load can be calculated from the true RMS resistor current and the resistance as follows:

:math:`P = I^2R`

The reactive power in an RC circuit as in figure 2 can be calculated using:

:math:`Q = V_C I = I^2 X_C`

Where V\ :sub:`C` is the RMS voltage across the capacitor, I is the RMS capacitor current, and X\ :sub:`C` is the capacitive reactance.

The reactive power in an RL circuit as in figure 4 can be calculated using:

:math:`Q = V_L I = I^2 X_L`

Where V\ :sub:`L` is the RMS voltage across the inductor, I is the RMS inductor current, and X\ :sub:`L` is the inductive reactance.

The reactive power in an RLC circuit as in figure 6 can be calculated using:

:math:`Q = V_X I = I^2 X`

Where V\ :sub:`X` = V\ :sub:`C` – V\ :sub:`L` is the RMS voltage across the combined total reactance, I is the RMS current in the reactance, and X = X\ :sub:`C` – X\ :sub:`L` is the combined total reactance. The RMS voltage across the total reactance is equal to the difference between the capacitor voltage (V\ :sub:`C`) and the inductor voltage (V\ :sub:`L`) because the voltages have a 180° phase difference (out of phase) between each other.

Power Factor Correction
~~~~~~~~~~~~~~~~~~~~~~~

Power factor correction is generally required for inductive loads like large AC motors. Because a power factor of 1 (unity) requires less peak current, it is advantageous to compensate for the inductance bringing the power factor as close to unity as possible. By doing this we make the real power close to being equal to the apparent power (VI). Power factor is corrected by connecting a capacitor in parallel with the inductive load.

To find the correct capacitor value required (figure 6), first we need to know the reactive power of the original RL circuit. This is done by drawing the power triangle and solving for the reactive power. The power triangle can be drawn from the real power and the apparent power and the power factor angle, θ. Once the reactive power for the original load circuit has been found, the capacitive reactance, X\ :sub:`C`, needed to correct the power factor can be calculated as follows:

:math:`Q = V^2 / X_C`

Where V is the RMS voltage across the RL circuit. Rearranging…

:math:`X_C = V^2 / Q`

With a value for XC, the required capacitance can be found based on the frequency (F) as follows:

:math:`X_C = 1/(2 \pi FC)`

Rearranging:

:math:`C = 1/(2 \pi FX_C)`

With the correct capacitor connected in parallel with the RL load (motor) the power factor will be close to unity, i.e. the voltage and current are in phase with each other. And the real power will be nearly equal to the apparent power.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless breadboard and jumper wires
| 1 – 47 Ω resistor
| 1 – 100 Ω resistor
| 1 – 10 uF capacitor
| 1 – 47 mH inductor

Directions for RC circuit:
~~~~~~~~~~~~~~~~~~~~~~~~~~

Construct the RC circuit shown in figure 2 on your solderless breadboard with the component values R\ :sub:`1` = 100 Ω and C\ :sub:`1` = 10 µF. Three connections to the ALM1000 are required as shown by the green boxes. Open the ALICE Oscilloscope software.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-pf-f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2. RC AC load circuit


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rc_load_bb.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3. RC AC breadboard connections


Procedure:
~~~~~~~~~~

On the right hand side of the main scope window enter 2.5 for the CA-V and CB-V offset adjustment. This is because in this experiment we need to apply AC signals (+/- voltage) across the load and are referencing all the measurements to the +2.5 V common rail. Also enter 0 for the CH-A and CH-B vertical position settings (along bottom of scope window). The vertical scales should now be centered on 0 and go from -2.5 to +2.5. Set the CA-I vertical scale to 5 mA/Div.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-d1.png
   :align: center
   :width: 400px

Set the channel A AWG Min value to 1.08 and Max value to 3.92V to apply a 2.84Vp-p, 1 V RMS, sine wave centered on 2.5 V as the input voltage to the circuit. Set the frequency to 250 Hz and the phase to 90°. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Sine. From the AWG B Mode drop down menu select the Hi-Z mode.

From the ALICE Curves drop down Menu select CA-V, CA-I and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level.

This configuration uses the oscilloscope to look at the AC voltage and current signals driving the circuit on channel A and the voltage across the resistance on channel B. The voltage across the capacitor is simply the difference between channel A and channel B (select CAV – CBV from the Math drop down menu). Make sure you have checked the Sync AWG selector.

The software can calculate the RMS values for the channel A voltage and current waveforms as well as the channel B voltage waveform. In addition the software also calculates the RMS value of the point by point difference between the channel A and B voltage waveforms. In this experiment this will be the RMS value of the voltage across the capacitor. To display these values select RMS and CA-CB RMS under -CA-V- and RMS under -CA-I- sections of the Meas CA drop down menu. Select RMS under -CB-V- section of the Meas CB drop down menu. You may also wish to display the Max ( or positive peak ) values for CA-V CA-I and CB-V.

Click on the Run button. Adjust the time base until you have more than two cycles of the sine wave on the display grid. Set the Hold off to 4.0 mS. You should see 4 traces, channel A voltage, channel B voltage, channel A current and the CA-CB voltage Math trace. Because 100 Ω was chosen for the resistor and the vertical scale for the current is 5 mA/Div, the trace of the current in the resistor will fall right on top of the trace for voltage across the resistor, channel B, with its vertical scale set to 0.5 V/Div, (0.5 mA time 100 Ω = 0.5 V).

Record the RMS value for the voltage across the total RC circuit (CHA V RMS), the RMS value for the current through R\ :sub:`1`, which is also the current in channel A in this series circuit (CHA I RMS), the RMS value for the voltage across the resistor (CHB V RMS) and the RMS value for the voltage across the capacitor (A-B RMS).

Based on these values calculate the real power (P) for the RC circuit. Calculate the reactive power (Q). Calculate the apparent power (S).

Based on your calculated values for P, Q and S draw the power triangle as in figure 1. Determine the power factor (pf) and θ for the RC circuit.

The oscilloscope traces are displaying the time relationship between the voltage (green channel A voltage trace) and current (cyan channel A current trace). Using the display markers or time cursor measure the time difference between the zero crossings of the two traces and from that the phase angle between them. Use this angle (θ) to calculate the power factor.

How does this compare to the value you obtained from the P, Q and S and the power triangle? Is the power factor lagging or leading and why?

Directions for RL circuit:
~~~~~~~~~~~~~~~~~~~~~~~~~~

First measure the DC resistance of the 47 mH inductor using the DC Ohmmeter tool in ALICE. The total series resistance of the RL circuit will be the inductor resistance plus the 47 Ω external resistor R\ :sub:`1`. The total resistance will need to be factored into your calculations for the real and reactive power.

Construct the RL circuit shown in figure 4 on your solderless breadboard with the component values R\ :sub:`1` = 47 Ω and L\ :sub:`1` = 47 mH.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-pf-f3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4. RL AC load circuit


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rl_load_bb.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 5. RL AC load circuit


.. _procedure-1:

Procedure:
~~~~~~~~~~

Click on the Run button. Adjust the time base until you have more than two cycles of the sine wave on the display grid. Set the Hold off to 4.0 mS. You should see 4 traces, channel A voltage, channel B voltage, channel A current and the CA-CB voltage Math trace.

Record the RMS value for the voltage across the total RL circuit (CHA V RMS), the RMS value for the current through R\ :sub:`1`, which is also the current in channel A in this series circuit (CHA I RMS), the RMS value for the voltage across the resistor (CHB V RMS) and the RMS value for the voltage across the inductor (A-B RMS).

Based on these values calculate the real power (P) for the RL circuit. Calculate the reactive power (Q). Calculate the apparent power (S).

Based on your calculated values for P, Q and S draw the power triangle as in figure 1. Determine the power factor (pf) and θ for the RL circuit.

The oscilloscope traces are displaying the time relationship between the voltage (green channel A voltage trace) and current (cyan channel A current trace). Using the display markers or time cursor measure the time difference between the zero crossings of the two traces and from that the phase angle between them. Use this angle (θ) to calculate the power factor.

How does this compare to the value you obtained from the P, Q and S and the power triangle? Is the power factor lagging or leading and why?

Directions for RLC circuit:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Construct the RLC circuit shown in figure 6 on your solderless breadboard with the component values R\ :sub:`1` = 47 Ω, C1 = 10 uF, and L\ :sub:`1` = 47 mH.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-pf-f41.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6. RLC AC load circuit measuring the capacitor


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rlc_load_bb.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 7. RLC AC load breadboard connections


.. _procedure-2:

Procedure:
~~~~~~~~~~

For the RLC circuit you will need measurements for the AC RMS voltage across each element. In the configuration shown in figure 6, with the channel B connected to the junction of C\ :sub:`1` and L\ :sub:`1` we can get the RMS voltage across C\ :sub:`1` from the difference between the CA and CB waveforms. With the channel B connected to the junction of L\ :sub:`1` and R\ :sub:`1` we can get the RMS voltage across R1 directly from the CB waveform. Record the RMS value for the voltage across the total RLC circuit (CHA V RMS), the RMS value for the current through R\ :sub:`1`, which is also the current in channel A in this series circuit (CHA I RMS), the RMS value for the voltage across the resistor (CHB V RMS) and the RMS value for the voltage across the capacitor (A-B RMS) when CHB is connected to the junction of C\ :sub:`1` and L\ :sub:`1` and the combined reactance of L\ :sub:`1` and C\ :sub:`1` when CHB is connected to the junction of L\ :sub:`1` and R\ :sub:`1`.

We still need the RMS voltage across the inductor L\ :sub:`1`. By swapping the order of the components in this series connected circuit, as shown in figure 8, we do not change the total overall impedance of the load circuit. However, we can now obtain the RMS voltage across L\ :sub:`1` from the difference between the CA and CB waveforms as we did with the capacitor in figure 6. Record the RMS value for the voltage across the total RLC circuit (CHA V RMS), the RMS value for the current through R\ :sub:`1`, which is also the current in channel A in this series circuit (CHA I RMS), the RMS value for the voltage across the resistor (CHB V RMS) and the RMS value for the voltage across the inductor (A-B RMS). Check that the value across the total circuit as well as the current through the load and the value across R\ :sub:`1` is the same as what was measure for figure 6. Why is this true?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-pf-f42.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 8. RLC AC load circuit measuring the inductor


Based on these values calculate the real power (P) for the RLC circuit. Calculate the reactive power (Q) for the combined LC reactance and the L and C individually. Calculate the apparent power (S).

Increase the frequency of channel A from 250 Hz to 500 Hz and re-measure the RMS voltages for the RLC circuit. How has that changed the real, reactive and apparent power? Is the load current lagging or leading and why?

Decrease the frequency of channel A from to 125 Hz and re-measure the RMS voltages for the RLC circuit. How has that changed the real, reactive and apparent power? Is the load current lagging or leading and why?

Directions for Power Factor correction:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The circuit shown in figure 9 for power factor correction is the same as figure 4 with the addition of capacitor C\ :sub:`1` in parallel with L\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-pf-f5.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 9. Power Factor correction for RL AC load


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/power_factor_rl_bb.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 10. Power Factor correction breadboard connections


Based on your measurements from figure 4 and the equations in the power factor correction section in the background information for this lab activity calculate the appropriate value for C\ :sub:`1` at 250 Hz. Use the closest standard value (or parallel combination of standard values) capacitor for C\ :sub:`1`.

.. _procedure-3:

Procedure:
~~~~~~~~~~

As you did for the simple RL circuit record the RMS value for the voltage across the total RL circuit (CHA V RMS), the RMS value for the current through R\ :sub:`1`, which is also the current in channel A in this series circuit (CHA I RMS), the RMS value for the voltage across the resistor (CHB V RMS) and the RMS value for the voltage across the inductor (A-B RMS).

Based on these values calculate the real power (P) for the RL circuit. Calculate the reactive power (Q). Calculate the apparent power (S).

Based on your calculated values for P, Q and S draw the power triangle as in figure 1. Determine the power factor (pf) and θ for the pf corrected RL circuit. Compare this pf to the one you calculated for just the RL load circuit. How close was the calculated capacitor value to the optimal value needed to make the pf equal to unity? Explain any differences.

Appendix:
---------

**Using other component values**

It is possible to substitute other component values in cases where the specified values are not readily available. The reactance of a component (X\ :sub:`C` or X\ :sub:`L`) scales with frequency. For example if 4.7 mH inductors are available rather than the 47 mH called for all that is needed to do is increase the test frequency from 250 Hz to 2.5 KHz. The same would be true when substituting a 1.0 uF capacitor for the 10.0 uF capacitor specified.

**Use the Phase Analyzer Virtual Instrument**

ALICE includes a Phase Analyzer Virtual Instrument that can assist in understanding phase relationships between voltage and current signals and polar notation and polar plots.

:doc:`Phase Analyzer User Guide. </wiki-migration/university/tools/m1k/alice/phase-analyzer-user-guide>`

**Using the RLC impedance meter tool**

ALICE desktop includes an :doc:`Impedance Analyzer </wiki-migration/university/tools/m1k/alice/desktop-sa-ba-ia-users-guide>` / RLC meter which can be used to measure the series resistance (R) and reactance (X). As part of this lab activity it might be informative to use this tool to measure the components R, L and C used to confirm your test results.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/power_factor_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/power_factor_ltspice`

**For Further Reading:**

| `Power Factor <https://en.wikipedia.org/wiki/Power_factor>`_
| `Power in Resistive and Reactive AC circuits <https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/power-resistive-reactive-ac-circuits/>`_
| `Practical Power Factor Correction <https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/practical-power-factor-correction/>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
