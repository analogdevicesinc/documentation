Activity: Band Pass Filters, For ADALM1000
==========================================

Objective:
----------

The objective of this Lab activity is to: 1. Construct a Band Pass Filter by cascading a low pass filter and a high pass filter. 2. Obtain the frequency response of the filter and learn using Bode plotter software.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A Band Pass Filter allows a specific range of frequencies to pass, while blocking or attenuating lower and higher frequencies. It passes frequencies between the two cut-off frequencies while attenuating frequencies outside the cut-off frequencies.

One typical application of a band pass filter is in Audio Signal Processing, where a specific range of frequencies of sound are desired while attenuating the rest. Another application is in the selection of a specific signal from a range of signals in communication systems.

A band pass filter may be constructed by cascading a High Pass RL filter with a roll-off frequency f\ :sub:`L` and a Low Pass RC filter with a roll-off frequency f\ :sub:`H`, such that :

:math:`f_L<f_H`

The Lower cut-off frequency is given as:

:math:`f_L=R/(2pi L)` (1)

The higher cut-off frequency is given as:

:math:`f_H=1/(2pi RC)` (2)

The Band Width of frequencies passed is given by:

:math:`BW= f_H-f_L`

All the frequencies below f\ :sub:`L`\ and above f\ :sub:`H` are attenuated and the frequencies between are passed by the filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab9-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Band Pass Filter circuit


From this previous lab on :doc:`Parallel LC Resonance </wiki-migration/university/courses/alm1k/circuits1/alm-cir-lc-resonator>` we can also use the formula for the LC resonance to calculate the center frequency of the band pass filter, the resonant frequency ω\ :sub:`o` is given by:

$ω_o = 1/sqrtLC $ rad/s

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz

**Frequency Response:**

To show how a circuit responds to a range of frequencies a plot of the magnitude ( amplitude ) of the output voltage of the filter as a function of the frequency can be drawn. It is generally used to characterize the range of frequencies in which the filter is designed to operate within. Figure 2 shows a typical frequency response of a Band Pass filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab9-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Band Pass Filter Frequency Response


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bpf_conn.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Band Pass Filter Connections


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Resistors (1.0 KΩ)
| Capacitors (0.047 µF)
| Inductors (20 mH)

Procedure:
~~~~~~~~~~

1. Set up the filter circuit as shown in figure 1 on your solderless breadboard, with the component values R\ :sub:`1` = 1 KΩ, C\ :sub:`1` = 0.047 µF, L\ :sub:`1` =20 mH.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bpf_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Band Pass Filter Connections


2. Set the channel A AWG Min value to 0.5 and Max value to 4.5V to apply a 4Vp-p sine wave centered on 2.5 V as the input voltage to the circuit. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Sine. From the AWG B Mode drop down menu select the Hi-Z mode.

3. From the ALICE Curves drop down Menu select CA-V, and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level. Set the Hold Off to 2 (mSec). Adjust the time base until you have at approximately two cycles of the sine wave on the display grid. From the Meas CA drop down menu select P-P under CA-V and do the same for CB. Also from the Meas CA menu select A-B Phase.

4. Start with a low frequency, 100 Hz, and measure output voltage CB-V peak to peak from the scope screen. It should be much lower than the channel A output. Increase the frequency of channel A in small increments until the peak-peak voltage of channel B is roughly 0.7 times the peak to peak voltage for channel A. Compute the 70 % of Vp-p and obtain the frequency at which this happens on the Oscilloscope. This gives the cut-off (roll-off) frequency for the constructed High Pass RL section of the filter.

5. Continue increasing the frequency of channel A until the peak-peak voltage of channel B falls back to roughly 0.7 times the peak to peak voltage for channel A. Compute the frequency at which this happens on the Oscilloscope. This gives the cut-off (roll-off) frequency for the constructed Low Pass RC section of the filter. (Note that this 70% amplitude point occurs twice on the band pass filter , at the lower cutoff and upper cutoff frequencies).

Frequency response plots with ALICE Bode Plotter
------------------------------------------------

The ALICE desk-top software can display Bode Plots which are graphs of the magnitude and the phase versus the frequency of a given network. The procedure is as follows:

Use the band pass circuit in figure 1, with R\ :sub:`1`\ =1.0 KΩ, C\ :sub:`1`\ =0.047 uF, and L\ :sub:`1`\ =20 mH we can sweep the input frequency from 100 Hz to 20000 Hz and plot the signal amplitude of both channel A and B and the relative phase angle between channel B and A.

With the circuit connected to the ALM1000 as in figure 1, start the ALICE desktop software. Open the Bode Plotter. Under the Curves menus select CA-dBV, CB-dBV and Phase B-A.

Under the Options drop down menu make sure that the Cut-DC option is selected.

Set AWG channel A Min value to 1.086 and Max value to 3.914. This will be a 1 Vrms (0 dBV) amplitude centered on the 2.5V middle of the analog input range. Set AWG A mode to SVMI and Shape to Sine. Set AWG channel B to Mode Hi-Z. Be sure the Sync AWG check box is selected.

Use the Start Frequency button to set the frequency sweep to start at 100 Hz and use the Stop Frequency button to the sweep to stop at 20000 Hz. Select CHA as the channel to sweep. Also use the Sweep Steps button to enter the number of frequency steps, use 100 as the number.

You should now be able to press the green Run button and run the frequency sweep. After the sweep is completed ( could take a few seconds for 100 points ) you should see something like the screen shot in figure 5. You may want to use the LVL and dB/div buttons to optimize the plots to best fit the screen grid.

Record the results and save the Bode Plot using your favorite screen capture tool and include it in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab9-screen1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5: Bode Analyzer Settings


To better understand the frequency characteristics of this parallel LC filter plot the low pass frequency response with just the capacitor (i.e. remove the inductor). Make the same frequency sweep and take a snap-shot of the gain ( CB-db - CA-dB ) and relative phase ( CA-CB ). Now plot the high pass frequency response with just the inductor (i.e. put the inductor back and remove the capacitor). The Bode plot in figure 6 shows these results. Note that the frequency where the low pass and high pass gain is the same and the relative phase sums to zero ( at about +70 and -70 degrees) is at the resonate frequency.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab9-screen2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6: Low and High pass response


Questions:
~~~~~~~~~~

1. Compute the cut-off frequencies for each Band Pass filter constructed using the formula in equations (1) and (2). Compare these theoretical values to the ones obtained from the experiment and provide suitable explanation for any differences.

2. Graph the Frequency Response for each filter built in the lab. (Use the values recorded in the tabular column and graph with the frequency on a logarithmic scale). Compare this to the response obtained from the Bode Plot and comment.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/bpf_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/bpf_ltspice`

**For Further Reading:**

| :doc:`ALICE Desk-top User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`
| `LC filter calculator <http://circuitcalculator.com/lcfilter.htm>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
