Activity: Transient Response of an RL Circuit, For ADALM1000
============================================================

Objective:
----------

The objective of this Lab activity is to study the transient response of inductor circuits using a series RL configuration and understand the time constant concept.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

This lab activity is similar to the RC Lab activity 5, except that the capacitor is replaced by an inductor. In this experiment, you will apply a square waveform to the RL circuit to analyze the transient response of the circuit. The pulse width relative to the circuit's time constant determines how it is affected by the RL circuit.

Time Constant (t): It is a measure of time required for certain changes in voltages and currents in RC and RL circuits. Generally, when the elapsed time exceeds five time constants (5t) after switching has occurred, the currents and voltages have reached their final value, which is also called steady-state response.

The time constant of an RL circuit is the equivalent inductance divided by the Thévenin resistance as viewed from the terminals of the equivalent inductor.

:math:`t = L / R` (1)

A Pulse is a voltage or current that changes from one level to another and back again. If a waveform's high time equals its low time, it is called a square wave. The length of each cycle of a pulse train is its period (T). The pulse width (tp) of an ideal square wave is equal to half the time period.

The relation between pulse width and frequency for the square wave is given by:

:math:`f=1/(2t_p)` (2)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab6-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1: Series RL circuit


In an R-L circuit, voltage across the inductor decreases with time while in the RC circuit the voltage across the capacitor increased with time. Thus, current in an RL circuit has the same form as voltage in an RC circuit: they both rise to their final value exponentially according to 1 - e :sup:`(-t*R/L)`.

The expression for the current in the Inductor is given by:

:math:`\displaystyle I_L(t) =(V / R)( 1 - e^\frac{- t R }{ L }) t >= 0` (3)

where, V is the applied source voltage to the circuit for t = 0. The response curve is increasing and is shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab6-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Current in Inductor increasing in a Series RL circuit.


(Time axis normalized by t)

The expression for the current decay across the Inductor is given by:

:math:`I_L(t) = I_0 e^ (- t R/L) t >= 0` (4)

where,

I\ :sub:`0` is the initial current stored in the inductor at t = 0

L/R = t is time constant.

The response curve is a decaying exponential and is shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab6-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Current decay through the Inductor for Series RL circuit.


Since it is possible to directly measure the current through the Inductor ( current supplied by driving source ) with the ALM1000, we will measure and compare both the current and the output voltage across the Resistor. The resistor waveform should be similar to the inductor current as V\ :sub:`R`\ =I*L\ :sub:`R`. From the waveforms on the scope, we should be able to measure the time constant t which should be equal to t = L / R\ :sub:`total`.

Here, R\ :sub:`total` is the total resistance and can be calculated from R\ :sub:`total` = R inductance+ R.

R inductance is the measured value of inductor resistance and can be measured by connecting inductance to an ohmmeter prior to running the experiment.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - Resistor 100 Ω
| 1 - Inductor 7 mH ( 6 windings of HPH1-1400L in series ) or similar value 5 to 20 mH

Procedure:
~~~~~~~~~~

1. Measure the combined inductor and resistor resistance R\ :sub:`total` by using an Ohmmeter. You can use the ALM1000 Ohmmeter Tool to do this. Remember that the Ohmmeter tool measures resistance with respect to ground when you connect the series connected windings of L\ :sub:`1` and R\ :sub:`1`.

2. Set up the circuit shown in figure 4 on your solderless breadboard with the component values R\ :sub:`1` = 220 Ω and L\ :sub:`1` = 20mH. Open the ALICE 1.2 Desktop software

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab6-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4: Experiment Set-Up


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/tr_rl_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5: Breadboard Connections


3. Set the channel A AWG Min value to 0.5 and Max value to 4.5V, Freq = 350 to apply a 4Vp-p square wave centered on 2.5 V as the input voltage to the circuit. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Square. From the AWG B Mode drop down menu select the Hi-Z mode.

Calculate the applied frequency using equation (2) for tp = 5t

4. From the ALICE Curves drop down Menu select CA-V, CA-I and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level. Adjust the time base until you have at approximately two cycles of the square wave on the display grid.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab6-screen1.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 6: Oscilloscope Configuration.


This configuration allows the oscilloscope to look at the input voltage of the circuit and the current through the inductor on channel A and the output voltage of the circuit on channel B. Make sure you have checked the Sync AWG selector.

5. The V\ :sub:`R` waveform has the same shape as I\ :sub:`L`\ (t) waveform. From V\ :sub:`R` waveform measure time constant t and compare with the one that you calculated from L/Rtotal. (Hint: Find the time that corresponds to 0.63V\ :sub:`R` value). See Background section for details.

6. Observe the response of the circuit and record the results again for tp = 25t, and tp = 0.5t.

Questions:
~~~~~~~~~~

• Include plots of I\ :sub:`L` and V\ :sub:`R` for different tp values given above in Procedure 4.

• A Capacitor stores charge. What do you think an Inductor stores? Answer in brief.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/rl_filt_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/rl_filt_ltspice`

**For Further Reading:**

| :doc:`ALICE Oscilloscope User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`
| :doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
