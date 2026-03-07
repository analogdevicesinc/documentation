Activity: Band Pass Filters
===========================

Objective:
----------

The objective of this Lab activity is to: 1. Construct a Band Pass Filter by cascading a low pass filter and a high pass filter and obtain the frequency response of the filter.

Background:
-----------

A Band Pass Filter allows a specific range of frequencies to pass, while blocking or attenuating lower and higher frequencies. It passes frequencies between the two cut-off frequencies while attenuating frequencies outside the cut-off frequencies.

One typical application of a band pass filter is in Audio Signal Processing, where a specific range of frequencies of sound are desired while attenuating the rest. Another application is in the selection of a specific signal from a range of signals in communication systems.

There are many circuit configurations for building a band pass filter. The band pass filter in this lab is constructed using an RLC circuit. A parallel capacitor and inductor are placed in series with a resistor.


|image1|

.. container:: centeralign

   Figure 1: Band Pass Filter circuit


The upper and lower cut-off frequencies are determined by solving the following quadratic equation:

:math:`x^2 - 1/(15.2 RC)x - 1/(39.4 LC)` for :math:`R=1000` Ohms \|\| :math:`L=0.01` Henry \|\| :math:`C=0.000000047` Farad

You can see the solution by using this link to `Wolfram Alpha <https://www.wolframalpha.com/input/?i=x%5E2+-+%281%2F%2815.2\*1000\*0.000000047%29%29x+-+%281%2F%2839.4\*0.01\*0.000000047%29%29>`_. The solution (roots) to the equation are :math:`x_1=-6681` and :math:`x_2=8081` . The negative sign can be ignored and this gives the lower and upper cut-off frequency:

:math:`f_L=6681` Hz and :math:`f_H=8081` Hz

The Band Width of frequencies passed is given by:

:math:`BW= f_H-f_L=1400` Hz

We can also use the formula for the LC resonance to calculate the center frequency of the band pass filter, the resonant frequency ω\ :sub:`o` is given by:

$ω_o = 1/sqrtLC $ rad/s (3)

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz (4)

**Frequency Response:**

To show how a circuit responds to a range of frequencies a plot of the magnitude ( amplitude ) of the output voltage of the filter as a function of the frequency can be drawn. It is generally used to characterize the range of frequencies in which the filter is designed to operate within. Figure 2 shows a typical frequency response of a Band Pass filter.

.. image:: https://wiki.analog.com/_media/university/labs/alm-cir-lab9-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2: Band Pass Filter Frequency Response


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 1.0 KΩ resistor
| 1 0.047 µF capacitor
| 1 10 mH inductor

Hardware setup
--------------

Build the circuit presented in Figure 3 on the solderless breadboard.


|image2|

.. container:: centeralign

   Figure 3: Band Pass Filter circuit


   |image3|

.. container:: centeralign

   Figure 4: Breadboard connections of the Band Pass Filter circuit


Procedure
---------

The band pass filter frequency response can be plotted using the Network Analyzer tool. Compute the center frequency of the filter using equation (4). According to this you will set the start and stop frequencies of the logarithmic sweep. For this filter the center frequency is 7.3 KHz. In the network analyzer set the start frequency at 1 KHz and the stop frequency at 20 KHz. Set the minimum phase at -90 the maximum phase at 90. Magnitude axis can be set from -30 dB to 10dB. In Figure 5 is presented the transfer function of the filter obtained by running the network analyzer.


|image4|

.. container:: centeralign

   Figure 5: Frequency response of Band pass filter circuit


In the Signal Generator tool, on Channel 1, generate a waveform with the frequency value in the pass band of the filter and analyze it's response. Observe on the oscilloscope channel 1 the input signal and the output signal on channel 2. In Figure 6 you can see the filter input and output for a 7kHz sine waveform.

| |image5|

.. container:: centeralign

   Figure 6: Input and output signals of Band pass filter circuit for 7kHz input frequency


| =====Questions===== Compute the cut-off frequencies for each Band Pass filter constructed using the formula in equations (1) and (2). Compare these theoretical values to the ones obtained from the experiment and provide suitable explanation for any differences.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bpf_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/bpf_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/labs/alm-cir-lab9-fig1.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/labs/bpf_circuit.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/labs/bpf_bb.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/labs/bpf_freq_plot.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/labs/bpf_7.3k_signal.png
   :width: 900px
