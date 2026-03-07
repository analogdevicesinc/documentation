Activity: Band Stop Filters
===========================

Objective:
----------

| The objective of this Lab activity is to construct a Band Stop Filter by combining a low pass filter and a high pass filter and obtain the frequency response of the filter. A Series LC circuit will be used.

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


We can use the formula for the LC resonance to calculate the center frequency of the band pass filter, the resonant frequency ω\ :sub:`o` is given by:

$ω_o = 1/sqrtLC $ rad/s (3)

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz (4)

\**Frequency Response: \*\*

To show how a circuit responds to a range of frequencies a plot of the magnitude ( amplitude ) of the output voltage of the filter as a function of the frequency can be drawn. It is generally used to characterize the range of frequencies in which the filter is designed to operate within. Figure 2 shows a typical frequency response of a Band Pass filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab12-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2: Band reject Filter Frequency Response


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 1.0 KΩ resistor
| 1 0.1 µF Capacitor(marked 104)
| 1 20 mH inductor or 2 (10 mH in series)

Hardware setup
--------------

Build on your solderless breadboard the Band reject filter circuit presented in Figure 3.


|image1|

.. container:: centeralign

   Figure 3: Band reject filter circuit


   |image2|

.. container:: centeralign

   Figure 4: Breadboard connections of Band reject filter circuit


Procedure
---------

The band stop filter's frequency response can be plotted using the Network Analyzer tool. Compute the center frequency of the filter using equation (4). According to this you will set the start and stop frequencies of the logarithmic sweep. For this filter the center frequency is 3.3 KHz. In the network analyzer set the start frequency at 1 KHz and the stop frequency at 10 KHz. Set the minimum phase at -90 the maximum phase at 90. Magnitude axis can be set from -30 dB to 10dB. In Figure 5 is presented the transfer function of the filter obtained by running the network analyzer.


|image3|

.. container:: centeralign

   Figure 5: Frequency response of Band reject filter circuit


In the Signal Generator tool, on Channel 1, generate a waveform with the frequency value in the rejection interval of the filter and analyze it's response. Observe on the oscilloscope channel 1 the input signal and the output signal on channel 2. In Figure 6 you can see the filter input and output for a 3kHz sine waveform.



|image4|

.. container:: centeralign

   Figure 6:Input and output signals of Band reject filter circuit for 3kHz input frequency


Questions
---------

| Compute the cut-off frequencies for each Band reject filter constructed using the formula in equations (1) and (2). Compare these theoretical values to the ones obtained from the experiment and provide suitable explanation for any differences.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bsf_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/bsf_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/labs/bsf_circuit.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/university/labs/bsf_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/labs/bsf_freq_plot.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/labs/bsf_3k_signal.png
   :width: 900px
