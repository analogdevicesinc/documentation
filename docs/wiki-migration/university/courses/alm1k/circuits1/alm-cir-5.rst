Activity: Transient Response of RC Circuit, For ADALM1000
=========================================================

Objective:
----------

The objective of this Lab activity is to study the transient response of a series RC circuit and understand the time constant concept using pulse waveforms.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

In this lab activity you will apply a pulse waveform to the RC circuit to analyses the transient response of the circuit. The pulse-width relative to a circuit's time constant determines how it is affected by an RC circuit.

Time Constant (τ): Denoted by the Greek letter tau, τ, it represents a measure of time required for certain changes in voltages and currents in RC and RL circuits. Generally, when the elapsed time exceeds five time constants (5τ) after switching has occurred, the currents and voltages have reached their final value, which is also called steady-state response.

The time constant of an RC circuit is the product of equivalent capacitance and the Thévenin resistance as viewed from the terminals of the equivalent capacitor.

:math:`t = R \times C` (1)

A Pulse is a voltage or current that changes from one level to another and back again. If a waveform's high time equals its low time it is called a square wave. The length of each cycle of a pulse is its period (T).

The pulse width (tp) of an ideal square wave is equal to half the time period.

The relation between pulse width and frequency is then given by,

:math:`f = 1/(2t_p)` (2)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab5-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1: Series RC circuit.


From Kirchhoff's laws, it can be shown that the charging voltage V\ :sub:`C` (t) across the capacitor is given by:

:math:`\displaystyle V_C(t) =V( 1- e^\frac{ -t}{RC }) for t >= 0` (3)

where, V is the applied source voltage to the circuit at time t = 0. The product RC is the time constant. The response curve is increasing and is shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab5-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Capacitor charging for Series RC circuit to a step input with time axis normalized by t


The discharge voltage for the capacitor is given by:

:math:`\displaystyle V_C (t) = V_o e^\frac{ -t}{RC } for t >= 0` (4)

Where Vo is the initial voltage stored in capacitor at t = 0. The product RC is often referred to the so called time constant, τ. The response curve is a decaying exponential as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab5-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Capacitor Discharging for Series RC circuit


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Resistors ( 2.2 KΩ, 10 KΩ)
| Capacitors (1 µF, 0.01 µF)

Procedure:
~~~~~~~~~~

1. Set up the circuit shown in figure 4 on your solderless breadboard with the component values R\ :sub:`1` = 2.2 KΩ and C\ :sub:`1` = 1 µF. Open the ALICE Oscilloscope software.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab5-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4. Breadboard diagram of RC circuit R\ :sub:`1` = 2.2 KΩ and C\ :sub:`1` = 1 µF.


   |image1|

.. container:: centeralign

   Figure 5. Breadboard diagram of RC circuit R\ :sub:`1` = 2.2 KΩ and C\ :sub:`1` = 1 µF.


2. Set the channel A AWG Min value to 0.5 and Max value to 4.5V to apply a 4Vp-p square wave centered on 2.5 V as the input voltage to the circuit. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Square. From the AWG B Mode drop down menu select the Hi-Z mode.

3. From the ALICE Curves drop down Menu select CA-V, and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level. Adjust the time base until you have at approximately two cycles of the square wave on the display grid.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab5-screen1.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 6: Oscilloscope Configuration.


This configuration uses the oscilloscope to look at the input of the circuit on channel A and the output of the circuit on channel B. Make sure you have checked the Sync AWG selector.

4. Observe the response of the circuit for the following three cases and record the results.

a. Pulse width >> 5t : Set the frequency of AWG A output such that the capacitor has enough time to fully charge and discharge during each cycle of the square wave. So let the pulse width be 15t and set the frequency according to equation (2). The value you have found should be approximately 15 Hz. Determine the time constant from the waveforms obtained on the screen if you can. If you cannot obtain the time constant easily, explain possible reasons.

b. Pulse width = 5t : Set the frequency such that the pulse width = 5t (this should be approximately 45 Hz). Since the pulse width is 5t, the capacitor should just be able to fully charge and discharge during each pulse cycle. From the figure determine t (see figure 2 and figure 7 below.)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab5-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7: Measuring the time constant t approximately by counting the number of squares.


c. Pulse width << 5t : In this case the capacitor does not have time to charge significantly before it is switched to discharge, and vice versa. Let the pulse width be only 1.0t in this case and set the frequency accordingly.

5. Repeat the procedure using R\ :sub:`1` = 10 KΩ and C\ :sub:`1` = 0.01 µF and record the measurements.

Questions:
~~~~~~~~~~

1. Calculate the time constant using equation (1) and compare it to the measured value from 4b. Repeat this for other set of R and C values.

2. Discuss the effects of changing component values.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/rc_filt_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/rc_filt_ltspice`

**For Further Reading:**

| :doc:`ALICE Oscilloscope User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`
| :doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/breadboard_rc.png
   :width: 400px
