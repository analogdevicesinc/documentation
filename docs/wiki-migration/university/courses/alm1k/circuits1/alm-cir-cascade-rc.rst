Activity: Cascaded RC low pass filters - ADALM1000
==================================================

Objective:
----------

The objective of this lab activity is to explore the changes to the frequency response of simple passive RC low pass filters when the effect of loading due to a second and third cascaded filter sections is take into account.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

Background:
-----------

If two passive RC low pass filters are cascaded the frequency response is not simply the product of the two first order RC transfer functions. This is because the ideal single pole response assumes a zero source impedance is driving the filter and there is no load on the output, i.e. filter drives an infinite impedance. However, directly connecting the second filter acts as a load for the first effectively changing the combined RC time constant. If you try to analyze the cascaded circuit by simply adding phasors you will soon realize the shortcomings of that simple technique. This is where using circuit simulation software is very helpful.

As a pre-lab exercise enter the schematic shown in figure 1 into the :adi:`ADIsimPE <en/design-center/interactive-design-tools/adisimpe.html>` or :adi:`LTSpice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` circuit simulation, schematic entry software tools. Three different RC low-pass filter sections are included. The inputs of all three filters are driven by the same AC source V1. Resistor R5 and capacitor C5 form a simple single pole (1st order) filter with the output taken at node dB-0. Resistors R3 and R4 and capacitors C1 and C3 form a 2nd order filter with R4 = R3 and C3 = C1. Two points in this filter should be plotted, the output of the first section at node dB-1 and the output of the second section at node dB-2. Resistors R2 and R1 and capacitors C4 and C2 form another 2nd order filter with R1 = 10\*R2 and C2 = C4/10. The two similar points in this filter should also be plotted, the output of the first section at node dB-3 and the output of the second section at node dB-4. This second filter keeps the RC time constant the same for both sections of the filter but reduces the loading effect by increasing the value of the second resistor by a factor of 10 and decreases the value of the second capacitor by a similar factor of 10 (keeping the RC product the same). Using a factor of 10 like this is a good rule of thumb to use when designing cascaded passive RC filters.

Run the simulation sweeping the input frequency from 100 Hz to 20 KHz. You should get a frequency response plot the looks something like figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/cascade_rc_sch.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 Simulation schematic of RC filters


A simulation was run sweeping the frequency from 100 Hz to 20 KHz. As we can see in figure 2 the completely unloaded 1st order filter (dB-0 green line) and the lightly loaded 1st order point (dB-3 slightly darker green line) are nearly on top of each other. The loaded 1st order point (dB-1 blue line) is significantly lower than the other two lines at the frequency of the RC time constant. However, all three converge to the same point at high frequencies, 20 KHz. The two 2nd order output points at dB-2 (red line, loaded) and dB-4 (pink line, lightly loaded) also show significant differences at the RC time constant frequency but also converge to the same point at 20 KHz. At 20 KHz the response of the 2nd order filters is 20 dB lower than the 1st order filters as one would expect.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/cascade_rc_sim.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 AC sweep simulation plot


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 3 – 1 KΩ resistors
| 1 – 10 KΩ resistor
| 1 – 100 KΩ resistor
| 3 – 0.1 uF capacitors (marked 104)
| 1 – 0.01 uF capacitor (marked 103)
| 1 – 0.001 uF capacitor (marked 102)

Directions:
~~~~~~~~~~~

Build the first order passive RC low pass filter shown in figure 3 on your solderless breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cascade-rc-f3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3 1st order passive RC low pass filter


Set up the ALICE desktop Bode Plotter screen as follows. With the Bode screen open you can deselect the Enab Time Plot selector and minimize the main Scope window.

| Set the Frequency scale to log.
| Under the Curves drop down select CA-dBV (to confirm the input level) and CB-dB – CA-dB (to plot the output response with respect to the input).
| Set the Start Frequency to 100 Hz.
| Set the Stop Frequency to 20000 Hz.
| Select CHA as the sweep source.
| Set the number of sweep points to 300.
| Set the FFT window shape to Flat-top.
| Under the Options drop down be sure the Cut-DC option is selected.
| Use the +dB/div and/or –dB/div buttons to select 5 dB/div on the vertical scale.
| Use the LVL+1 and/or LVL-1 buttons to set the level of the top line of the grid to 5 dB.

| In the AWG controls window confirm that Channel A is set to SVMI mode, Shape Sin and Channel B is set to Hi-Z mode.
| Set Channel A Min value to 1.0 and Max value to 4.0.

With Single sweep mode selected click on the green Run button. After a few seconds you should have the frequency response plot of the RC filter. Under the Options drop down click on the Store trace button to save a copy of the plot. Under the Curves drop down select the saved Math plot to be displayed also.

**Second order filter**

Now add a second RC low pass section to the filter as shown in figure 4. The Channel B input will be alternately connected to the top of C\ :sub:`1`, the output of the first RC section and the top of C\ :sub:`2`, the output of the second RC section.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cascade-rc-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 2nd order passive RC low pass filter


With channel B connected to the top of C\ :sub:`1` click the green start button again. After the new sweep is completed you should see the saved 1st order plot from the first sweep of the filter from figure 3 and the new "live" (loaded) 1st order plot from the circuit in figure 4.

Are the two plots the same? If not explain any differences and why. You will want to capture a screen shot of this plot to include in your lab report. Use your favorite screen capture method or under the File drop down window click on either Save Screen or Save Data buttons.

Under the Options drop down click on the Store trace button to save a copy of the new sweep plot. Now the saved and "live" plots will be on top of each other.

Move Channel B to the top of C\ :sub:`2` and click the green start button again. After the new sweep is completed you should see the saved 1st order plot of the response seen at the top of C\ :sub:`1` and the new "live" 2nd order response seen at the top of C\ :sub:`2`. You will want to again capture a screen shot of this plot to include in your lab report.

Under the Options drop down click on the Store trace button to save a copy of the new sweep plot. Now the saved and "live" plots will be on top of each other.

Change the value of R\ :sub:`2` to 10 KΩ and the value of C\ :sub:`2` to 0.01 uF and click the green start button again. After the new sweep is completed you should see the saved 2nd order plot of the response seen at the top of the 0.1 uF C\ :sub:`2` capacitor and the new "live" 2nd order response seen at the top of the 0.01uF C\ :sub:`2` capacitor.

Are the two plots the same? If not explain any differences and why. You will want to again capture a screen shot of this plot to include in your lab report.

As a way to better understand what is happening due to the changes to R\ :sub:`2` and C\ :sub:`2` move Channel B back to the top of C\ :sub:`1` and click the green start button again. Compare this response curve to the one you observed at the top of C\ :sub:`1` when R\ :sub:`2` was 1 KΩ and C\ :sub:`2` was 0.1 uF. Explain any difference you observe and why. You will want to again capture a screen shot of this plot to include in your lab report.

**Third order filter**

As a further extension of this cascade of RC low pass filter sections add a third RC section to make a 3rd order filter by connecting R\ :sub:`3` and C\ :sub:`3` to your circuit as shown in figure 5. Follow the same steps you just did on the 2nd order filter with R\ :sub:`1` = R\ :sub:`2` = R\ :sub:`3` and C\ :sub:`1` = C\ :sub:`2` = C\ :sub:`3`, and again with R\ :sub:`1` = 1KΩ, R\ :sub:`2` = 10KΩ, R\ :sub:`3` = 100KΩ and C\ :sub:`1` = 0.1uF, C\ :sub:`2` = 0.01uF, C\ :sub:`3` = 0.001uF.

Explain any differences you observe in the frequency responses and be sure to save screen shots along the way to include in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cascade-rc-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5. 3rd order passive RC low pass filter


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/cascaded_rc_bb.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6. 3rd order passive RC low pass filter breadboard connections


One final question, how do your measured results compare to your simulation results (as in figure 2)? Explain any differences.

**Resources:**

-  Fritzing files: :git-education_tools:`cascade_rc_bb <m1k/fritzing/cascaded_rc_bb>`
-  LTSpice files: :git-education_tools:`m1k/ltspice/cascade_rc_ltspice`
-  ADISimPE files: :git-education_tools:`cascade_rc_adisimpe <m1k/adisimpe/cascaded_rc_adisimpe>`

**For Further Reading:**

| :adi:`LTSpice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>`
| :adi:`ADIsimPE <en/design-center/interactive-design-tools/adisimpe.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
