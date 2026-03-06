Activity: Resonance in RLC Circuits, For ADALM1000
==================================================

Objective:
----------

The objective of this Lab activity is to study the phenomenon of resonance in RLC circuits. Determine the resonant frequency and bandwidth of the given network using the amplitude response to a sinusoidal source.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A resonant circuit, also called a tuned circuit, consists of an inductor and a capacitor together with a voltage or current source. It is one of the most important circuits used in electronics. For example, a resonant circuit, in one of many forms, allows us to tune into a desired radio or television station from the vast number of signals that are around us at any time.

A network is in resonance when the voltage and current at the network input terminals are in phase and the input impedance of the network is purely resistive.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1: Parallel Resonance Circuit


Consider the Parallel RLC circuit of figure 1. The steady-state admittance offered by the circuit is:

:math:`Y = 1/R + j(\omega C - 1/(\omega L) )`

Resonance occurs when the voltage and current at the input terminals are in phase. This corresponds to a purely real admittance, so that the necessary condition is given by:

:math:`\omega C - 1/\omega L = 0`

The resonant condition may be achieved by adjusting L, C, or ω. Keeping L and C constant, the resonant frequency ω\ :sub:`o` is given by:

$omega_o = 1/sqrtLC $ rad/s (1)

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz (2)

Frequency Response: It is a plot of the magnitude of the output Voltage of a resonance circuit as a function of frequency. The response, of course, starts at zero, reaches a maximum value in the vicinity of the natural resonant frequency, and then drops again to zero as ω becomes infinite. The frequency response is shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Frequency Response of Parallel Resonant Circuit


The two additional frequencies, ω\ :sub:`1` and ω\ :sub:`2`, are also indicated. These are called "half-power frequencies". These frequencies locate those points on the curve at which the voltage response is 1/sqrt(2) or 0.707 times the maximum value. They are used to measure the bandwidth of the response curve. This is called the half-power bandwidth of the resonant circuit and is defined as:

:math:`ß = omega_2 - omega_1` (3)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Series Resonance Circuit


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Resistors 100 Ω, 1 KΩ
| Capacitors 1 µF, 0.01 µF
| Inductors 20 mH

Procedure:
~~~~~~~~~~

1. Set up the RLC circuit as shown in figure 4 on your solderless breadboard, with the component values R\ :sub:`S` = 100 Ω, R\ :sub:`1` = 1 KΩ, C\ :sub:`1` = 1 µF and L\ :sub:`1`\ = 20 mH.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4: Parallel Resonance Circuit with a series resistance connected to a source


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/parallel_res_cir_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5: Breadboard connections


2. Set the channel A AWG Min value to 0.5 and Max value to 4.5V to apply a 4Vp-p sine wave centered on 2.5 V as the input voltage to the circuit. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Sine. From the AWG B Mode drop down menu select the Hi-Z mode.

3. From the ALICE Curves drop down Menu select CA-V, and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level. Set the Hold Off to 2 (mSec). Adjust the time base until you have at approximately two cycles of the sine wave on the display grid. From the Meas CA drop down menu select P-P under CA-V and do the same for CB. Also from the Meas CA menu select A-B Phase.

4. Vary the frequency of the sinewave on the AWG A menu from 500 Hz to 2.5 KHz in 100 Hz steps. For each frequency write down the P-P voltage for channel A and channel B and the A-B phase. Note at what frequency the voltage seen at the output of the circuit on Channel B, is maximum. This will be near the resonant frequency of the circuit. Note the phase should be nearly zero degrees at this frequency. Adjust the frequency in 10 Hz increments around where you see a maximum for CB P-P voltage until the A-B phase is exactly zero.

5. Repeat the experiment using for the series resonant circuitry in figure 3, and use L\ :sub:`1` = 20 mH and C\ :sub:`1` = 0.01 uF and R\ :sub:`1` = 1 KΩ. The Vo voltage on the resistor is proportional to the series RLC circuit current.

Questions:
~~~~~~~~~~

1. Find the resonant frequency, ω\ :sub:`o` using equation (1) and compare it to the experimental value in both cases.

2. Plot the voltage response of the circuit and obtain the bandwidth from the half-power frequencies using equation (3).

Appendix, Frequency response plots with ALICE-SA
------------------------------------------------

The ALICE desktop software can make generating frequency and phase response plots much easier. Using the parallel resonate RLC circuit in figure 4 we can sweep the input frequency from 10 Hz to 5000 Hz and plot the signal amplitude of both channel A and B and the relative phase angle between channel B and A.

With the circuit connected to the ALM1000 as in figure 4, start the ALICE desktop software. Open the Bode plotting window.

Under the Curves menus select CA-dBV, CB-dBV and Phase B-A.

Under the Options drop down menu click on Cut-DC to select it.

Set AWG channel A Min value to 1.086 and Max value to 3.914. This will be a 1 Vrms (0 dBV) amplitude centered on the 2.5V middle of the analog input range. Set AWG A mode to SVMI and Shape to Sine. Set AWG channel B to Mode Hi-Z. Be sure the Sync AWG check box is selected.

Use the Start Frequency button to set the frequency sweep to start at 10 Hz and use the Stop Frequency button to the sweep to stop at 5000 Hz. Under the Sweep Gen drop down menu select CHA as the channel to sweep. Also use the Sweep Steps button to enter the number of frequency steps, use 400 as the number.

You should now be able to press the green Run button and run the frequency sweep. After the sweep is completed you should see something like the screen shot in figure A1. You may want to use the LVL and dB/div buttons to optimize the plots to best fit the screen grid.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-screen1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A1, Frequency sweep from 100 Hz to 20000 Hz


**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/parallel_res_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/parallel_res_ltspice`

**For Further Reading:**

:doc:`ALICE Desk-top User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
