Activity: Band Stop Filters, For ADALM1000
==========================================

Objective:
----------

| The objective of this Lab activity is to:
| 1. Construct a Band Stop Filter by combining a low pass filter and a high pass filter. A Series LC circuit will be used.
| 2. Obtain the frequency response of the filter by using Bode plotter software tool.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A Band Stop Filter, also sometimes called a notch or band reject filter allows a specific range of frequencies to not pass to the output, while allowing lower and higher frequencies to pass with little attenuation. It removes or notches out frequencies between the two cut-off frequencies while passing frequencies outside the cut-off frequencies.

One typical application of a band stop filter is in Audio Signal Processing, for removing a specific range of undesirable frequencies of sound like noise or hum, while not attenuating the rest. Another application is in the rejection of a specific signal from a range of signals in communication systems.

A band reject filter may be constructed by combining a High Pass RL filter with a roll-off frequency f\ :sub:`L` and a Low Pass RC filter with a roll-off frequency f\ :sub:`H`, such that :

:math:`f_L< f_H`

The higher cut-off frequency is given as:

:math:`f_L=R/(2 \pi L)` (1)

The lower cut-off frequency is given as :

:math:`f_H=1/(2 \pi R C)` (2)

The Band Width of frequencies rejected is given by:

:math:`BW= f_L< f_H`

All the frequencies below f\ :sub:`L`\ and above f\ :sub:`H` are allowed to pass and the frequencies between are attenuated by the filter. The series combination of an L and C as shown in figure 1 is such a filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab12-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Band reject Filter circuit


From this previous lab on :doc:`Parallel LC Resonance </wiki-migration/university/courses/alm1k/circuits1/alm-cir-lc-resonator>` we can also use the formula for the LC resonance to calculate the center frequency of the band pass filter, the resonant frequency ω\ :sub:`o` is given by:

$ω_o = 1/sqrtLC $ rad/s

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz

\**Frequency Response: \*\*

To show how a circuit responds to a range of frequencies a plot of the magnitude ( amplitude ) of the output voltage of the filter as a function of the frequency can be drawn. It is generally used to characterize the range of frequencies in which the filter is designed to operate within. Figure 2 shows a typical frequency response of a Band Pass filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab12-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Band reject Filter Frequency Response


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Resistor R\ :sub:`1` 1.0 KΩ
| Capacitor C\ :sub:`1` 0.1 µF (marked 104)
| Inductor L\ :sub:`1` (1 20 mH or 2 10 mH in series)

Procedure:
~~~~~~~~~~

1. Set up the filter circuit as shown in figure 1 on your solderless breadboard, with the component values R\ :sub:`1` = 1 KΩ, C\ :sub:`1` = 0.1 µF, L\ :sub:`1` =20 mH.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bsf_bb.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3, Band reject Filter Breadboard connections


2. Set the channel A AWG Min value to 0.5 and Max value to 4.5V to apply a 4Vp-p sine wave centered on 2.5 V as the input voltage to the circuit. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Sine. From the AWG B Mode drop down menu select the Hi-Z mode.

3. From the ALICE Curves drop down Menu select CA-V, and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level. Set the Hold Off to 2 (mSec). Adjust the time base until you have at approximately two cycles of the sine wave on the display grid. From the Meas CA drop down menu select P-P under CA-V and do the same for CB. Also from the Meas CA menu select A-B Phase.

4. Start with a low frequency, 100 Hz, and measure output voltage CB-V peak to peak from the scope screen. It should be about the same as the channel A output. Increase the frequency of channel A in small increments until the peak-peak voltage of channel B is roughly 0.7 times the peak to peak voltage for channel A. Compute the 70 % of Vp-p and obtain the frequency at which this happens on the Oscilloscope. This gives the cut-off (roll-off) frequency for the constructed RL time constant of the filter.

5. Continue increasing the frequency of channel A until the peak-peak voltage of channel B drops to its minimum value. Measure the frequency at which this happens on the Oscilloscope. This gives the center frequency for the constructed series LC resonator section of the filter. (Note that this 70% amplitude point occurs twice on the band reject filter, at the lower cutoff and upper cutoff frequencies).

Frequency response plots with ALICE Bode Plotter
------------------------------------------------

The ALICE desktop software can display Bode Plots which are graphs of the magnitude and the phase versus the frequency of a given network. The procedure is as follows:

Use the band pass circuit in figure 1, with R\ :sub:`1`\ =1.0 KΩ, C\ :sub:`1`\ =0.1 uF, and L\ :sub:`1`\ =20 mH we can sweep the input frequency from 500 Hz to 12000 Hz and plot the signal amplitude of both channel A and B and the relative phase angle between channel B and A.

With the circuit connected to the ALM1000 as in figure 1, start the ALICE Desktop software.

Open the Bode Plotting tool. Under the Curves menus select CA-dBV, CB-dBV and Phase B-A.

Under the Options menu change the setting for zero-stuffing to 2.

Set AWG channel A Min value to 1.086 and Max value to 3.914. This will be a 1 Vrms (0 dBV) amplitude centered on the 2.5V middle of the analog input range. Set AWG A mode to SVMI and Shape to Sine. Set AWG channel B to Mode Hi-Z. Be sure the Sync AWG check box is selected.

Use the Start Frequency entry to set the frequency sweep to start at 100 Hz and use the Stop Frequency entry to the sweep to stop at 20000 Hz. Under the Sweep Gen select CHA as the channel to sweep. Also use the Sweep Steps entry to enter the number of frequency steps, use 200 as the number.

You should now be able to press the green Run button and run the frequency sweep. After the sweep is completed ( could take a few seconds for 200 points ) you should see something like the screen shot in figure 4. You may want to use the LVL and dB/div buttons to optimize the plots to best fit the screen grid.

Record the results and save the Bode Plot using your favorite screen shot capture tool.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab12-screen1.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 4: Bode Analyzer Settings Band Stop filter


Questions:
~~~~~~~~~~

1. Compute the cut-off frequencies for each Band reject filter constructed using the formula in equations (1) and (2). Compare these theoretical values to the ones obtained from the experiment and provide suitable explanation for any differences.

2. Graph the Frequency Response for each filter built in the lab. (Use the values recorded in the tabular column and graph with the frequency on a logarithmic scale). Compare this to the response obtained from the Bode Plot and comment.

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/bsf_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/bsf_ltspice`

**For Further Reading:**

| :doc:`ALICE Desk-top User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`
| `RLC Band-stop Filter Design Tool <http://sim.okawa-denshi.jp/en/RLCtool.php>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
