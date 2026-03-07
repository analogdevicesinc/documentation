Metrology Terminology
=====================

Scope
=====

This document outlines common terminology used across our metrology portfolio.

Terminology
===========

Energy Measurement Error
------------------------

The accuracy of the energy measurement is assessed as follows:

-  The voltage channel is supplied with a sinusoidal signal that has peak values equal to half of full scale.
-  The current channel is supplied with sinusoidal signals that have peak values equal to full scale, 1/10 of full scale, 1/100 of full scale, 1/1000 of full scale, and 1/2000 of full scale.
-  The energy is accumulated in line cycle accumulation mode, and the accumulation time varies with the current channel signal level.

The energy calculated for current peaks equal to 1/10 of full scale is considered the reference. The energy measurement error is computed relative to a straight line that passes through this point, as follows:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/metrology-terminology/energy_measurement_error_formula.png
   :width: 600px

where:

Energy(I\ :sub:`x`) is the energy measurement when the current is I\ :sub:`x`.

Energy(I\ :sub:`1/10`) is the energy measurement when the current I\ :sub:`1/10`, which is the reference measurement.

AccTime(I\ :sub:`1/10`) is the accumulation time used to measure Energy(I\ :sub:`1/10`).

AccTime(I\ :sub:`x`) is the accumulation time used to measure Energy(Ix).

Irms and Vrms Measurement Error
-------------------------------

The accuracy of the RMS measurement is assessed as follows:

-  The voltage and current channels are supplied with sinusoidal signals of various peaks, starting with the full-scale signals and ending with ±1 mV and ±62.5 µV, respectively.
-  The RMS registers are read at least once per line cycle over 1 sec and averaged.

The measurement performed when the input signal has peaks equal to 1/10 of full scale is considered the reference. The RMS measurement error is computed relative to a straight line that passes through this point, as follows:

|image1| |image2|

where:

Irms(I\ :sub:`x`) is the current RMS measurement when the current is I\ :sub:`x`.

Irms(I\ :sub:`1/10`) is the current RMS measurement when the current is I\ :sub:`1/10`, which is the reference measurement.

Vrms(V\ :sub:`x`) is the voltage RMS measurement when the voltage is V\ :sub:`x`.

Vrms(V\ :sub:`1/10`) is the voltage RMS measurement when the voltage is V\ :sub:`1/10`, which is the reference measurement.

Signal-to-Noise Ratio (SNR)
---------------------------

SNR is the ratio of the RMS value of the actual input signal to the RMS sum of all other spectral components below the Nyquist frequency, excluding harmonics and dc. The waveform samples are acquired over 1 sec and then a Hanning window is applied. The value for SNR is expressed in decibels.

Signal-to-Noise-and-Distortion (SINAD) Ratio
--------------------------------------------

SINAD is the ratio of the RMS value of the actual input signal to the RMS sum of all other spectral components below the Nyquist frequency, including harmonics but excluding dc. The waveform samples are acquired over 1 sec and then a Hanning window is applied. The value for SINAD is expressed in decibels.

Total Harmonic Distortion (THD)
-------------------------------

THD is the ratio of the RMS sum of all harmonics (excluding the noise components) to the RMS value of the fundamental. The waveform samples are acquired over 1 sec and then a Hanning window is applied. The value for THD is expressed in decibels.

Spurious-Free Dynamic Range (SFDR)
----------------------------------

SFDR is the ratio of the RMS value of the actual input signal to the RMS value of the peak spurious component over the measurement bandwidth of the waveform samples. The waveform samples are acquired over 1 sec and then a Hanning window is applied. The value of SFDR is expressed in decibels relative to full scale, dBFS.

CF Jitter
---------

The period of pulses at one of the CF pins is continuously measured. The maximum, minimum, and average values of four consecutive pulses are computed as follows:

Maximum = :math:`max(Period_0,Period_1,Period_2,Period_3)`

Minimum = :math:`min(Period_0,Period_1,Period_2,Period_3)`

Average= :math:`(Period_0,Period_1,Period_2,Period_3)/4`

CF Jitter = :math:`((Maximum - Minimum)/ Average) \times 100%`

Crosstalk
---------

Crosstalk is measured by grounding one channel and applying a full-scale 50 Hz or 60 Hz signal on all the other channels. The crosstalk is equal to the ratio between the grounded ADC output value and its ADC full-scale output value. The ADC outputs are acquired for 100 sec. Crosstalk is expressed in decibels.

ADC Offset Error
----------------

ADC offset error is the difference between the average measured ADC output code with both inputs connected to GNDISO and the ideal ADC output code. The magnitude of the offset depends on the input range of each channel.

Gain Error
----------

Gain error represents the difference between the measured ADC output code (minus the offset) and the ideal output code. The difference is expressed as a percentage of the ideal code and represents the overall gain error of one current or voltage channel.

RMS Measurements
----------------

Root mean square (RMS) is a measurement of the magnitude of an AC signal. Its definition can be both practical and mathematical. Defined practically, the RMS value assigned to an AC signal is the amount of DC required to produce an equivalent amount of power in the load. Mathematically, the RMS value of a continuous signal f(t) is defined as:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/metrology-terminology/rms_continuous.png
   :width: 300px

For time sampled signals, RMS calculation involved squaring the signal, taking the average, and obtaining the square root.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/metrology-terminology/rms_sampled.png
   :width: 300px

Equation above implies that for signals containing harmonics, the RMScalculation contains the contribution of all harmonics, not only the fundamental.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/metrology-terminology/irms_measurement_error_formula.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/metrology-terminology/vrms_measurement_error_formula.png
   :width: 400px
