Activity: Resonance in RLC Circuits - ADALM2000
===============================================

Objective:
----------

The objective of this Lab activity is to study the phenomenon of resonance in RLC circuits. Determine the resonant frequency and bandwidth of the given network using the amplitude response to a sinusoidal source.

Background:
-----------

A resonant circuit, also called a tuned circuit consists of an inductor and a capacitor together with a voltage or current source. It is one of the most important circuits used in electronics. For example, a resonant circuit, in one of many forms, allows us to tune into a desired radio or television station from the vast number of signals that are around us at any time.

A network is in resonance when the voltage and current at the network input terminals are in phase and the input impedance of the network is purely resistive.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1: Parallel RLC Circuit


Consider the Parallel RLC circuit of figure 1. The steady-state admittance offered by the circuit is:

:math:`Y = 1/R + j(\omega C - 1/(\omega L) )`

Resonance occurs when the voltage and current at the input terminals are in phase. This corresponds to a purely real admittance, so that the necessary condition is given by:

:math:`\omega C - 1/\omega L = 0`

The resonant condition may be achieved by adjusting L, C, or ω. Keeping L and C constant, the resonant frequency ω\ :sub:`o` is given by:

$omega_o = 1/sqrtLC $ rad/s (1)

OR

:math:`f_o = 1/(2pi sqrtLC)` Hertz (2)

Frequency Response: It is a plot of the magnitude of the output Voltage of a resonance circuit as function of frequency. The response of course starts at zero, reaches a maximum value in the vicinity of the natural resonant frequency, and then drops again to zero as ω becomes infinite. The frequency response is shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Frequency Response of Parallel RLC Circuit


The two additional frequencies ω\ :sub:`1` and ω\ :sub:`2` are also indicated which are called half-power frequencies. These frequencies locate those points on the curve at which the voltage response is 1/sqrt(2) or 0.707 times the maximum value. They are used to measure the band-width of the response curve. This is called the half-power bandwidth of the resonant circuit and is defined as:

:math:`ß = omega_2 - omega_1` (3)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab7-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3: Series Resonance Circuit


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 100 Ω resistor
| 1 1 kΩ resistor
| 1 1 µF capacitor
| 1 20 mH inductor ( 2 x 10 mH inductors in series)

Hardware setup:
---------------

Set up the circuit shown in Figure 4 on your solderless breadboard.


|image1|

.. container:: centeralign

   Figure 4: Parallel Resonance Circuit


   |image2|

.. container:: centeralign

   Figure 5: Breadboard connections of Parallel Resonance Circuit


Procedure:
----------

Using the Network analyzer tool you can plot the frequency response of a resonant circuit. Start by computing the resonance frequency using equation (1). According to this, set the logarithmic sweep parameters. In this case, the resonance frequency is 1.1kHz so the sweep can start from 100Hz to 10 kHz. Set the minimum phase at -90 the maximum phase at 90. Magnitude axis can be set from -15 dB to 0dB. In Figure 6 is presented the transfer function of the RLC circuit obtained by running the network analyzer.


|image3|

.. container:: centeralign

   Figure 6: Frequency response of the parallel RLC circuit


The circuit response in time domain can be analyzed using Signal generator and Oscilloscope tools. On the signal generator channel 1 select a sine waveform of 2 volts amplitude peak-to-peak. Set the frequency equal to the resonance frequency. On the oscilloscope channel 1 you will see the input signal and the output signal on channel 2. Observe in Figure 7 how the output signal is almost in phase with the input.



|image4|

.. container:: centeralign

   Figure 7: Input and output signals of RLC circuit for frequency equal to 1.1 kHz


Choose another two values of frequency, for example the values at the ends of the sweep interval and see how the circuit responds for these.



|image5|

.. container:: centeralign

   Figure 8: Input and output signals of RLC circuit for frequency equal to 100 Hz


   |image6|

.. container:: centeralign

   Figure 9: Input and output signals of RLC circuit for frequency equal to 10 kHz


Questions:
----------

1. Find the resonant frequency, ω\ :sub:`o` using equation (1) and compare it to the experimental value.

2. Obtain the bandwidth from the half-power frequencies using equation (3).

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/resonance_RLC_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/resonance_RLC_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/parallel_rlc_20m.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/paralel_rlc_bb.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/rlc_paralel.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/rlc_1.1khz.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/rlc_100hz.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/rlc_10k.png
   :width: 900px
