Activity: Cascaded RC low pass filters - ADALM2000
==================================================

Objective:
----------

The objective of this lab activity is to explore the changes to the frequency response of simple passive RC low pass filters when the effect of loading due to a second and third cascaded filter sections is take into account.

Background:
-----------

If two passive RC low pass filters are cascaded the frequency response is not simply the product of the two first order RC transfer functions. This is because the ideal single pole response assumes a zero source impedance is driving the filter and there is no load on the output, i.e. filter drives an infinite impedance. However, directly connecting the second filter acts as a load for the first effectively changing the combined RC time constant. If you try to analyze the cascaded circuit by simply adding phasors you will soon realize the shortcomings of that simple technique. This is where using circuit simulation software is very helpful.

As a pre-lab exercise enter the schematic shown in figure 1 into the :adi:`LTSpice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` circuit simulation tool. Three different RC low-pass filter sections are included. The inputs of all three filters are driven by the same AC source V1. Resistor R5 and capacitor C5 form a simple single pole (1st order) filter with the output taken at node dB-0. Resistors R3 and R4 and capacitors C1 and C3 form a 2nd order filter with R4 = R3 and C3 = C1. Two points in this filter should be plotted, the output of the first section at node dB-1 and the output of the second section at node dB-2. Resistors R2 and R1 and capacitors C4 and C2 form another 2nd order filter with R1 = 10\*R2 and C2 = C4/10. The two similar points in this filter should also be plotted, the output of the first section at node dB-3 and the output of the second section at node dB-4. This second filter keeps the RC time constant the same for both sections of the filter but reduces the loading effect by increasing the value of the second resistor by a factor of 10 and decreases the value of the second capacitor by a similar factor of 10 (keeping the RC product the same). Using a factor of 10 like this is a good rule of thumb to use when designing cascaded passive RC filters.

Run the simulation sweeping the input frequency from 100 Hz to 20 KHz. You should get a frequency response plot the looks something like figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/cascade_rc_sch.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1: Simulation schematic of RC filters


A simulation was run sweeping the frequency from 100 Hz to 20 KHz. As we can see in figure 2 the completely unloaded 1st order filter (dB-0 green line) and the lightly loaded 1st order point (dB-3 slightly darker green line) are nearly on top of each other. The loaded 1st order point (dB-1 blue line) is significantly lower than the other two lines at the frequency of the RC time constant. However, all three converge to the same point at high frequencies, 20 KHz. The two 2nd order output points at dB-2 (red line, loaded) and dB-4 (pink line, lightly loaded) also show significant differences at the RC time constant frequency but also converge to the same point at 20 KHz. At 20 KHz the response of the 2nd order filters is 20 dB lower than the 1st order filters as one would expect.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/cascade_rc_sim.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2: AC sweep simulation plot


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 3 1 KΩ resistors
| 1 10 KΩ resistor
| 1 100 KΩ resistor
| 3 0.1 uF capacitors (marked 104)
| 1 0.01 uF capacitor (marked 103)
| 1 0.001 uF capacitor (marked 102)

First order RC filter
---------------------

Hardware setup
~~~~~~~~~~~~~~

Build the circuit presented in figure 3 on the solderless breadboard.


|image1|

.. container:: centeralign

   Figure 3: First order RC filter


   |image2|

.. container:: centeralign

   Figure 4: First order RC filter breadboard connections


Procedure
~~~~~~~~~

In network analyzer you will do a logarithmic sweep. Set the start frequency to 100 Hz and the stop frequency to 20 KHz. The magnitude axis can be set to -50 dB minimum and 10 dB maximum. The phase axis goes from -180 to 90 degrees. Run the network analyzer to obtain the frequency response plot of the RC filter.


|image3|

.. container:: centeralign

   Figure 5: First order RC filter frequency response


Second order RC filter
----------------------

.. _hardware-setup-1:

Hardware setup
~~~~~~~~~~~~~~

Add a second RC low pass section to the prevoius filter as shown in Figure 6.


|image4|

.. container:: centeralign

   Figure 6: Second order RC filter


   |image5|

.. container:: centeralign

   Figure 7: Second order RC filter breadboard connections


.. _procedure-1:

Procedure
~~~~~~~~~

Keep the same parameters set in the network analizer. Put the oscilloscope channel 2 after the first RC stage and do a single sweep. This will be the reference sweep an can be kept on the plot by pressing the Snapshot button in the Reference section of the Network analizer General Settings. Move the oscilloscope channel 2 after the second RC stage and do another sweep. You should see on the plot the frequency response after both RC stages as in Figure 8.


|image6|

.. container:: centeralign

   Figure 8: Second order RC filter frequency response


Third order RC filter
---------------------

.. _hardware-setup-2:

Hardware setup
~~~~~~~~~~~~~~

As a further extension of this cascade of RC low pass filter sections add a third RC section to make a 3rd order filter by connecting another R and C to your circuit as shown in figure 9.


|image7|

.. container:: centeralign

   Figure 9: Third order RC filter


   |image8|

.. container:: centeralign

   Figure 10: Breadboard connections of the third order RC filter


.. _procedure-2:

Procedure
~~~~~~~~~

| Keep the same parameters set in the network analizer. Put the oscilloscope channel 2 after the first RC stage ( point A shown in figure 10) and do a single sweep. This will be the reference sweep an can be kept on the plot by pressing the Snapshot button in the Reference section of the Network analizer General Settings. Move the oscilloscope channel 2 after the second RC stage (point B) and do another sweep and press the Snapshot button. You should see on the plot the frequency response after both RC stages. To obtain the frequency response of the third stage put the oscilloscope channel 2 in point C and do another sweep. You should see all three responses as in figure 11. |image9|

.. container:: centeralign

   Figure 11: Third order RC filter frequency response


| Follow the same steps you just did on the 2nd order filter with R4 = R5 = R6 and C4 = C5 = C6, and again with R4 = 1KΩ, R5 = 10KΩ, R6 = 100KΩ and C4 = 0.1uF, C5 = 0.01uF, C6 = 0.001uF and plot the frequency response for this cascaded filter.

Questions
---------

| 1. What are the differences between the plots in second order filter? (One plot obtained with 2+ in point A and the other with 2+ in point B).
| 2. What are the differences between the plots in third order filter? (The plots obtained by the same procedure, the third one being obtained with 2+ in point C).
| 3.How do your measured results compare to your simulation results (as in figure 2)? Explain any differences.
|

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/cascaded_rc_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/cascaded_rc_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/labs/1st_rc.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/labs/first_order_cascaded_rc_bb_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/labs/first_order.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/labs/2nd_rc_ab.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/university/labs/second_order_cascaded_rc_bb_bb.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/labs/second_order_rc.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/university/labs/3rd_rc_abc.png
   :width: 500px
.. |image8| image:: https://wiki.analog.com/_media/university/labs/cascaded_rc_bb_scope_ch2.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/university/labs/third_order.png
   :width: 900px
