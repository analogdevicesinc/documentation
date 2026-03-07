Activity: Low Pass and High Pass Filters, For ADALM1000
=======================================================

Objective:
----------

The objective of this Lab activity is to study the characteristics of passive filters by obtaining the frequency response of low pass RC filter and high pass RL filter.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The impedance of an inductor is proportional to frequency and the impedance of a capacitor is inversely proportional to frequency. These characteristics can be used to select or reject certain frequencies of an input signal. This selection and rejection of frequencies is called filtering, and a circuit which does this is called a filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab8-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1: Low Pass RC filter.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab8-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: High Pass RL filter.


If a filter passes high frequencies and rejects low frequencies, then it is a high-pass filter. Conversely, if it passes low frequencies and rejects high ones, it is a low-pass filter. Filters, like most things, aren't perfect. They don't absolutely pass some frequencies and absolutely reject others. A frequency is considered passed if its magnitude (voltage amplitude) is within 70% or 1/sqrt(2) of the maximum amplitude passed and rejected otherwise. The 70% frequency is called corner frequency, roll-off frequency or half-power frequency.

The corner frequencies for RC filter and RL filter are as follows:

For RC filters:

:math:`f_c=1/(2pi RC)` (1)

For RL filters:

:math:`f_c=R/(2pi L)` (2)

Frequency Response: It is a graph of magnitude of the output voltage of the filter as a function of the frequency. It is generally used to characterize the range of frequencies in which the filter is designed to operate within.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab8-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Frequency Response of a typical Low Pass Filter with a cut-off frequency f\ :sub:`c`\


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Resistors (1 KΩ)
| Capacitor (1µF)
| Inductor (22 mH)

Procedure:
~~~~~~~~~~

A. Low pass RC filter:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rc_lpf_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4: Low Pass RC filter breadboard connections.


1. Set up the RC circuit as shown in figure 1 on your solderless breadboard, with the component values R\ :sub:`1` = 1 KΩ, C\ :sub:`1` = 1 µF.

2. Set the channel A AWG Min value to 0.5 and Max value to 4.5V to apply a 4Vp-p sine wave centered on 2.5 V as the input voltage to the circuit. From the AWG A Mode drop down menu select the SVMI mode. From the AWG A Shape drop down menus select Sine. From the AWG B Mode drop down menu select the Hi-Z mode.

3. From the ALICE Curves drop down Menu select CA-V, and CB-V for display. From the Trigger drop down menu select CA-V and Auto Level. Set the Hold Off to 2 (mSec). Adjust the time base until you have at approximately two cycles of the sine wave on the display grid. From the Meas CA drop down menu select P-P under CA-V and do the same for CB. Also from the Meas CA menu select A-B Phase.

4. Start with a low frequency, 50 Hz, and measure output voltage CB-V peak to peak from the scope screen. It should be same as channel A output. Increase the frequency of channel A in small increments until the peak-peak voltage of channel B is roughly 0.7 times the peak to peak voltage for channel A. Compute the 70 % of Vp-p and obtain the frequency at which this happens on the Oscilloscope. This gives the cut-off (roll-off) frequency for the constructed Low Pass RC filter.

B. High-Pass RL filter

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rl_hpf_bb.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5: High Pass RL filter breadboard connections.


1. Set up the RL circuit as shown in figure 2 on your solderless breadboard, with the component values R\ :sub:`1` = 1 KΩ, L = 20 mH.

2. Repeat steps 2 and 3 as in Part A to obtain the Oscilloscope.

3. Start with a high frequency 20 KHz and measure output voltage CB-V peak to peak from the scope screen. It should be same as channel A output. Lower the frequency of channel A in small increments until the peak-peak voltage of channel B is roughly 0.7 times the peak to peak voltage for channel A. Compute the 70 % of Vp-p and obtain the frequency at which this happens on the Oscilloscope. This gives the cut-off (roll-off) frequency for the constructed High Pass RL filter.

Questions:
~~~~~~~~~~

Calculate the Cut-off frequencies for the RC low pass and RL high pass filter using equations (1) and (2). Compare the computed theoretical values to the ones obtained from the experimental measurements and provide a suitable explanation for any differences.

Appendix, Frequency response plots with ALICE Bode Plotter
----------------------------------------------------------

The ALICE desk-top Bode Plotting software can make generating frequency and phase response plots much easier. Using the low pass RC circuit in figure 1, with R\ :sub:`1`\ =100 Ω and C\ :sub:`1`\ =1.0 uF, we can sweep the input frequency from 10 Hz to 5000 Hz and plot the signal amplitude of both channel A and B and the relative phase angle between channel B and A.

With the circuit connected to the ALM1000 as in figure 1, start the ALICE desktop software. Open the Bode Plotter.

Under the Curves menus select CA-dBV, CB-dBV and Phase B-A.

Under the Options drop down menu click on Cut-DC to select it.

Set AWG channel A Min value to 1.086 and Max value to 3.914. This will be a 1 Vrms (0 dBV) amplitude centered on the 2.5V middle of the analog input range. Set AWG A mode to SVMI and Shape to Sine. Set AWG channel B to Mode Hi-Z. Be sure the Sync AWG check box is selected.

Use the Start Frequency entry to set the frequency sweep to start at 100 Hz and use the Stop Frequency entry to the sweep to stop at 20000 Hz. Select CHA as the channel to sweep. Also use the Sweep Steps button to enter the number of frequency steps, use 100 as the number.

You should now be able to press the green Run button and run the frequency sweep. After the sweep is completed you should see something like the screen shot in figure A1. You may want to use the LVL and dB/div buttons to optimize the plots to best fit the screen grid.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab8-screen1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A1, Frequency sweep from 100 Hz to 20000 Hz


**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/lpf_hpf_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/lpf_hpf_ltspice`

**For Further Reading:**

:doc:`ALICE Desk-top User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
