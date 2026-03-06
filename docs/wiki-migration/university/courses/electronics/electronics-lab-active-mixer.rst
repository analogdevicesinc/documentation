Activity: Active Mixers
=======================

Objective
---------

The objective of this activity is to understand the basic concept of active mixers.

Background
----------

A mixer is a three-port device that can modulate or demodulate, and which can either be passive or active. The main function of a mixer is to change the frequency of a signal while preserving every other characteristic of the initial signal. What differentiates an active mixer from a passive mixer is that an active mixer employs active devices to apply conversion gain.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/am_diagram.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 1. Symbolic Representation of a Mixer


The output of mixer can be of two forms, thus the diagram shown in Figure 1. The mixer accepts two frequency input and delivers one frequency output. The output, as shown in the diagram, can either be the sum or the difference of the two input frequencies. These frequencies can be identified as the following; Local Oscillator (LO), Radio Frequency (RF), and Intermediate Frequency (IF).

Mainly, mixers are used to perform frequency conversions which can be classified as up-conversion and down-conversion. The LO port is always an input port unlike the RF and IF port which can either be an input or output depending on the application. In a down-conversion mixer, the other input port is the RF port and the output is at a lower IF. This is shown in Figure 2a.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/downcon.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2a. Down-conversion Mixing Representation


In an up-conversion mixer, the other input is the IF and the output is the RF signal. This is shown in Figure 2b.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/upcon.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2b. Up-conversion Mixing Representation


Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 2 1 kΩ resistor
| 2 6.8k kΩ resistor
| 1 OP37 precision op-amp
| 1 LTC1043 precision switched-cap block
| 3 N-channel MOSFET (2-ZVN3310, 1-ZVN2210A)

Single Balanced Active Mixer
----------------------------

Mixers can also be classified as single balanced mixer and double balanced mixer, each has its own advantages and disadvantages.

A single-balanced mixer often called a balanced mixer, is a type of mixer which suppresses either the LO or RF signal but not both. This configuration is hardly used because of its susceptibility to noise in the input LO signal. The main drawback is its IF-LO feed-through, which means the LO signal can leak into the IF signal if the IF signal frequency is not much lower than the LO signal frequency. Shown in Figure 3 is a simple circuit of a single balanced mixer.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/singlebal_ckt.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3. Single Balanced Mixer


Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard connection shown in Figure 4.


|image1|

.. container:: centeralign

   Figure 4. Single Balanced Mixer Breadboard Connections


Procedure
~~~~~~~~~

Use Signal Generator W1 and W2, as the frequency inputs to the mixer. For the LO frequency use W1, set it to 5V 210 kHz sine wave. For the RF input, use W2. For the Up-conversion mixing, W2 should be lower than the LO frequency so set W2 to 5V, 25 kHz sine wave. So, our expected output is at 185kHz and 235kHz. Analog Ch2 monitors the RF input, W2, whereas Ch1 monitors the IF output through the Spectrum Analyzer. The result is shown in Figure 5a.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/singlebal_plot_upcon.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5a. Up-conversion Spectrum Plot


For the Down-conversion mixing, set W2 to 5V, 260kHz sine wave, this will serve as the RF input to the mixer. So, our expected output is at 50kHz and spectrum result should be like Figure 5b.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/singlebal_plot_downcon.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5b. Down-conversion Spectrum Plot


Single balanced active mixer implemented with LTC1043
-----------------------------------------------------

.. _background-1:

Background
~~~~~~~~~~

Ideally, to meet the low-noise, high-linearity objectives of a mixer we need some circuit that implements a polarity-switching function in response to the LO input. Thus, the mixer can be reduced to Figure 6, which shows the RF signal being split into in-phase (0°) and anti-phase (180°) components; a changeover switch, driven by the local oscillator (LO) signal, alternately selects the in-phase and antiphase signals. Thus reduced to essentials, the ideal mixer can be modeled as a sign-switcher.


|image2|

.. container:: centeralign

   Figure 6. An Ideal Switching Mixer


Simulation
~~~~~~~~~~

For demonstration of the mixing concept we can use the ideal switching mixer in the Figure 6. The mixer can be built with the LTC1043 CMOS analog switch, which is a monolithic, charge-balanced, dual switched capacitor instrumentation building block. A pair of switches alternately connects an external capacitor to an input voltage and then connects the charged capacitor across an output port. An internal clock is provided and its frequency can be adjusted with an external capacitor. If no capacitor is connected at pin Cosc, the internal oscillator will have the frequency 210kHz. With a 39p external capacitor (smallest value from the parts kit) the internal oscillator of LTC1043 will have an 80kHz frequency.Simulations were performed for the configuration with no capacitor connected at Cosc.


|image3|

.. container:: centeralign

   Figure 7. Switching Mixer with LTC1043


In figure 7 is presented the circuit in LTSpice, but it can be implemented with hardware parts on a breadboard. We use the inputs of the first switch of the LT1043. The input signal will be generated on channel 1 of the signal generator and connected to S1A. To obtain its inverted version we build a simple inverting amplifier with unity gain and connect it to S2A. The output is visualized at pin Ca+ with the channel 2+ of the oscilloscope. For a down-conversion mixer, Channel 1 of the signal generator must be set at a frequency higher than that of the oscillator, for example, 250kHz. The output will be the difference of the two frequencies, at 40kHz.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/downconvfftnocap.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8. FFT analysis of the Down-conversion mixer


If the Channel 1 of the signal generator will be set at 60kHz, the output will have two components (one at fLo+fin=270kHz and one at fLo-fin=150kHz).



|image4|

.. container:: centeralign

   Figure 8. FFT analysis of the Up-conversion mixer


Double Balanced Mixer or Gilbert Cell
-------------------------------------

Double Balanced Mixers are mainly used to avoid the LO product terms from the output signal. This configuration requires two single-balanced mixer circuits with two differential RF transistors which are connected in parallel and provides an anti-parallel switching pair. The LO product terms are canceled out and RF signal is doubled at the output signal. This configuration produces a high degree of isolation between LO and IF which eases the filtering requirements used after mixing the signal. For noise, these mixers are less susceptible than the single-balanced mixers because of its differential RF signal. This mixer is also known as the Gilbert Cell.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/gilbertcell.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9. Gilbert Cell Configuration


As observed in the circuit, there is a lot of symmetry of the Gilbert cell mixer. This enables the balance to be obtained and the rejection of the LO and RF signals at the output. The Gilbert cell is not as widely used within systems using discrete components because of the number of components required is high. However, for integrated circuits Gilbert cell mixers are ideal because the number of components is not particularly important, they do not require wound components like transformers or other inductors and they are able to offer a high level of performance.

LTSpice Simulation
~~~~~~~~~~~~~~~~~~

Since the component provided in the kit is not enough to construct the circuit, let’s instead simulate the circuit in LTspice. See Lab Resources to download the LTspice files for simulation. Seen in Figure 10 is the IF output of the circuit. We took the difference between the positive and negative IF output.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/gilbertcell_sim.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 10. Gilbert Cell LTSpice Simulation


Double balanced active mixer implemented with LTC1043
-----------------------------------------------------

The double balanced mixer configuration requires two single-balanced circuits. We can build this configuration with LTC1043 as it has many swithches and it provides the anti-paralell switching pair needed. In Figure 11 is presented the schematic of the circuit. The circuit and the connections are almost the same, only the inputs of the second switch(S3A S4A) are connected in reverse order to the inputs of the first switch (S1A S2A). In this case, the output is visualized with oscilloscope channel 2+ at pin Ca+ and 2- at pin Ca-.


|image5|

.. container:: centeralign

   Figure 11. Double balanced mixer with LTC1043


To analyze the Down-conversion configuration on channel 1 of the signal generator is generated a sinewave with 250kHz frequency and 1V amplitude peak-to-peak. In Figure 12 is presented the resulting FFT analysis.



|image6|

.. container:: centeralign

   Figure 12. Down-conversion FFT analysis


For Up-conversion the sinewave generated on channel 1 will have a frequency smaller than that of the LTC1043 internal oscillator, for example, 50kHz. The FFT analysis for this frequency value is seen in Figure 13.



|image7|

.. container:: centeralign

   Figure 13. Up-conversion FFT analysis


.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/active_mixers_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/active_mixers_ltspice`
   


Further Readings
----------------

Some additional resources:

-  :adi:`Mixers and Modulators <media/en/training-seminars/tutorials/MT-080.pdf?doc=AN-1422.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/singlebal_bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/ideal_mixer.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/activemixer_ltc1043_nocap.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/upconvfftnocap.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/doublebalanced_ltc1043.png
   :width: 700px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/downconvdouble_250k.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/upconvdoube_50k.png
   :width: 600px
