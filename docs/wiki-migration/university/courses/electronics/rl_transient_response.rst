Activity: Transient Response of an RL Circuit - ADALM2000
=========================================================

Objective:
----------

The objective of this Lab activity is to study the transient response of inductor circuits using a series RL configuration and understand the time constant concept.

Background:
-----------

This lab activity is similar to the "Transient response of an RC circuit" Lab activity, except that the capacitor is replaced by an inductor. In this experiment, you will apply a square waveform to the RL circuit to analyze the transient response of the circuit. The pulse width relative to the circuit's time constant determines how it is affected by the RL circuit.

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
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 100 Ω resistor
| 1 1 mH inductor

Hardware setup:
---------------

Set up the circuit shown in Figure 4 on your solderless breadboard with the component values R1 = 100Ω and L1 = 1 mH.


|image1|

.. container:: centeralign

   Figure 4. Series RL circuit schematic


   |image2|

.. container:: centeralign

   Figure 5. Breadboard connections of RL circuit


Procedure:
----------

On Channel 1 of the oscilloscope you will visualize the input voltage, and on channel 2 the voltage on the resistor(it has the same shape as the current through the inductor). Generate a square wave on the channel 1 of the signal generator with 4V amplitude peak-to-peak. The frequency will be set according to t. Calculate the applied frequency using equation (2) for tp = 5t.


|image3|

.. container:: centeralign

   Figure 6. Waveforms for pulsewidth equal to 5t


The waveform on channel 2 (voltage on the resistor) has the same shape as IL(t) waveform. From it, measure time constant t and compare with the one that you calculated from L/Rtotal. (Hint: Find the time that corresponds to 0.63VR value). Observe the response of the circuit and record the results again for tp = 25t, and tp = 0.5t.

Questions:
~~~~~~~~~~

• Include plots of IL and VR for different tp values given above in Procedure 4.

• A Capacitor stores charge. What do you think an Inductor stores? Answer in brief.

• How can you attenuate the spikes present on the input voltage?

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files::git-education_tools:`m2k/fritzing/transient_response_RL_bb`
   -  LTSpice files::git-education_tools:`m2k/ltspice/transient_response_RL_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/rl_series.png
   :width: 350px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/transient_response_rl_series_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/rl_5t.png
   :width: 900px
