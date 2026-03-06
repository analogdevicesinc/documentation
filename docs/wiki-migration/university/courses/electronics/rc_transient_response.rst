Activity: Transient Response of an RC Circuit - ADALM2000
=========================================================

Objective:
----------

The objective of this Lab activity is to study the transient response of a series RC circuit and understand the time constant concept using pulse waveforms.

Background:
-----------

In this lab activity you will apply a pulse waveform to the RC circuit to analyse the transient response of the circuit. The pulse-width relative to a circuit's time constant determines how it is affected by an RC circuit.

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
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 2.2 KΩ resistor
| 1 1 µF capacitor
| 1 10 KΩ resistor
| 1 0.01 µF capacitor
| =====Hardware setup:===== Set up the circuit shown in Figure 4 on your solderless breadboard with the component values R\ :sub:`1` = 2.2 KΩ and C\ :sub:`1` = 1 µF. |image1|

.. container:: centeralign

   Figure 4. Series RC circuit R\ :sub:`1` = 2.2 KΩ and C\ :sub:`1` = 1 µF.


   |image2|

.. container:: centeralign

   Figure 5.Breadboard connections of series RC circuit


Procedure:
----------

On Channel 1 of the oscilloscope you will visualize the input voltage, and on channel 2 the voltage on the capacitor. Generate a square wave on the channel 1 of the signal generator with 4V amplitude peak-to-peak. The frequency will be set according to t for the following three cases:

a. Pulse width » 5t : Set the frequency of W1 output such that the capacitor has enough time to fully charge and discharge during each cycle of the square wave. So let the pulse width be 15t and set the frequency according to equation (2). The value you have found should be approximately 15 Hz. Determine the time constant from the waveforms obtained on the screen if you can. If you cannot obtain the time constant easily, explain possible reasons.


|image3|

.. container:: centeralign

   Figure 6. Waveforms for pulse width equal to 15t


b. Pulse width = 5t : Set the frequency such that the pulse width = 5t (this should be approximately 45 Hz). Since the pulse width is 5t, the capacitor should just be able to fully charge and discharge during each pulse cycle. From the figure determine t (see figure 2 and figure 7 below.)



|image4|

.. container:: centeralign

   Figure 7. Waveforms for pulse width equal to 5t


c. Pulse width « 5t : In this case the capacitor does not have time to charge significantly before it is switched to discharge, and vice versa. Let the pulse width be only 1.0t in this case and set the frequency accordingly.



|image5|

.. container:: centeralign

   Figure 8. Waveforms for pulse width equal to 1t


Repeat the procedure using R1 = 10 KΩ and C1 = 0.01 µF and record the measurements.

Questions:
~~~~~~~~~~

1. Calculate the time constant using equation (1) and compare it to the measured value from 4b. Repeat this for other set of R and C values.

2. Discuss the effects of changing component values.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/transient_response_RC_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/transient_response_RC_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/series_rc.png
   :width: 350px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/rc_series_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/rc_15t.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/rc_5t.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/rc_1t.png
   :width: 900px
