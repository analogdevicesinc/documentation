Activity: Low Pass and High Pass Filters, For ADALM2000
=======================================================

Objective:
----------

The objective of this Lab activity is to study the characteristics of passive filters by obtaining the frequency response of low pass RC filter and high pass RL filter.

Background:
-----------

The impedance of an inductor is proportional to frequency and the impedance of a capacitor is inversely proportional to frequency. These characteristics can be used to select or reject certain frequencies of an input signal. This selection and rejection of frequencies is called filtering, and a circuit which does this is called a filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab8-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1: Low Pass RC filter.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-lab8-fig2.png
   :align: center
   :width: 400px

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
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 1 KΩ resistor
| 1 1 µF capacitor
| 1 10 mH inductor

A. RC Low-pass filter
---------------------

Hardware setup:
~~~~~~~~~~~~~~~

On the solderless breadboard build the circuit presented in Figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/lpf_rc.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4: RC low pass filter


.. image:: https://wiki.analog.com/_media/university/courses/electronics/rc_lpf_bb.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 5: Breadboard connections of RC low pass filter


Procedure:
~~~~~~~~~~

To analyze the filter transfer function you must use the Network Analyzer tool. Compute the cutoff frequency of the filter using equation (1). According to this you will set the start and stop frequencies of the logarithmic sweep. In this case the cutoff frequency is 160 Hz. In the network analyzer set the start frequency at 1 Hz and the stop frequency at 10 KHz. Set the minimum phase at -90 the maximum phase at 90. Magnitude axis can be set from -50 dB to 10dB. In Figure 6 is presented the transfer function of the filter obtained by running the network analyzer.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/lpf_rc_network_analyzer.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 6:RC low pass filter transfer function


Further you can use the signal generator and the oscilloscope to observe how the filter affects the input signal. On the channel 1 of the signal generator generate a sine waveform with a frequency lower than the cutoff frequency, for example 50 Hz.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/lpf_50hz.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 7: Input and output signals of RC low pass filter for a frequency lower than the cutoff frequency


If the frequency of the input signal increases to a value greater than the cutoff frequency, for example 500Hz in this case, you will see an attenuation and a phase difference on the output signal according to the filter transfer function.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/lpf_500hz.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 8: Input and output signals of RC low pass filter for a frequency higher than the cutoff frequency


B. RL High-pass filter
----------------------

.. _hardware-setup-1:

Hardware setup:
~~~~~~~~~~~~~~~

On the solderless breadboard build the circuit presented in Figure 9.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/hpf_rl.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 9: RL high pass filter


.. image:: https://wiki.analog.com/_media/university/courses/electronics/rl_hpf_bb.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 10: Breadboard connections of RL high pass filter


.. _procedure-1:

Procedure:
~~~~~~~~~~

The procedure is similar to the LPF case. After computing the cutoff frequency using equation (2) set the sweep parameters accordingly. The logarithmic sweep can start in this case at 1 KHz and stop at 100kHz. Phase and magnitude axes can be kept as the same values as in the LPF case. Run the network analyzer to obtain the transfer function as presented in Figure 11.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/hfp_rl_network_analyzer.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 11: RL high pass filter transfer function


As in the previous case, generate a sinusoidal waveform on the channel 1 of the signal generator. Observe how at frequency values lower than the cutoff frequency the output signal is attenuated.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/hpf_1khz.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 12: Input and output signals of RL high pass filter for a frequency lower than the cutoff frequency


If the frequency is higher than the cutoff frequency, the signal is in the pass-band of the filter and the attenuation tends to be 0dB.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/hpf_50khz.png
   :align: center
   :width: 900px

.. container:: centeralign

   Figure 12: Input and output signals of RL high pass filter for a frequency higher than the cutoff frequency


Questions:
----------

Calculate the Cut-off frequencies for the RC low pass and RL high pass filter using equations (1) and (2). Compare the computed theoretical values to the ones obtained from the experimental measurements and provide a suitable explanation for any differences.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/lpf_hpf_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/lpf_hpf_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
