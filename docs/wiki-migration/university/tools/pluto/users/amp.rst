Amplifiers
==========

In this article, we will examine the basics of propagation and motivate the use of amplifiers for RF transmission. We will also discuss some important specifications of amplifiers that are typically approached by practicing engineers.

Transmission
============

To understand power in RF transmission, we need to go back to high school physics and do a little thought experiment.

Imagine a `Dyson Sphere <https://en.wikipedia.org/wiki/Dyson_sphere>`__, an artificial hollow sphere of matter around a star. The energy (in Joules) that the encompassed star provides spreads out uniformly in all directions. The Luminosity or Power the star puts out is based on Joules/second, or Watts. The Brightness or power received at the surface of the Dyson-sphere received is based on the distance from the star and the surface of the inner surface of the sphere (and is measured in Watts/m^2). Suppose the Dyson-sphere has a radius of r, then the surface area of that sphere is :math:`4pir^2` .

If the total output power (or Luminosity) of the star is L Watts, and the surface area of that sphere is :math:`4pir^2` , So the energy flowing through each square meter of the sphere every second is:

:math:`B = L/4{\pi}r^2`

We call that the star’s brightness, B, and is measured in Watts/meter^2. This is known as a form of the “Inverse Square Law”, as the relationship is :math:`1/r^2` not :math:`1/r`

If the distance, r, is doubled then the brightness, B, (or received brightness) decreases by a factor of :math:`\displaystyle \frac{1}{2}^2` or a quarter the brightness.

If the distance, r, is tripled then the brightness, B, (or received brightness) decreases by a factor of :math:`\displaystyle \frac{1}{2}^3` or a eighth the brightness.

You can also look at this from the opposite way - if you need to read a book on the surface of the Dyson-sphere, what kind of output power do you need from the star, to get the appropriate amount of brightness? To double the brightness, you need to increase the power of the star by 4 times.

If you still are not sure lets go way back to the middle school butter gun analogy, by watching the excellent video, put together by `Roger Linsell <https://www.youtube.com/user/fizzicsorg>`__ of http://www.fizzics.org/.

.. image:: https://wiki.analog.com/_media/youtube>JW3tT0L2gpc
   :alt: youtube>JW3tT0L2gpc

Free Space Path Loss
====================

As energy is transmitted by any transceiver it becomes dispersed across space and absorbed by the surrounding environment. This is typically referred to as path loss or loss or attenuation of energy over a distance. Although generally not accurate in most situations, the most common model for path loss is free-space path loss (FSPL). FSPL is the energy loss in an obstacle-free, line-of-sight path through free space. FSPL is proportional to the square of the distance:

:math:`\displaystyle L=\frac{4 \pi d}{\lambda}^2 = \frac{4 \pi d f}{c}^2` ,

where :math:`d` is the distance (meters) from the transmitter, :math:`f` is the signal or carrier frequency (hertz), :math:`\lambda` is the wavelength (meters), and :math:`c` is the speed of light (meters per second). The equation above also assumes the transmitter is `isotropic <https://en.wikipedia.org/wiki/Isotropy>`__ and is measured from the far field.

This equation is typically provided in :math:`dB` which can be calculated as:

:math:`\displaystyle L_{dB}=10log_10(\frac{4 \pi d f}{c}^2) = 20log_10(\frac{4 \pi d f}{c}) = 20log_10(d) + 20log_10(f) + 20log_10\frac{4 \pi}{c}` .

Let us get some perspective on this equation from looking at the idea of receiver sensitivity (RS), which is the minimum power a signal can be received at and still recovered. For WiFi 802.11ac, this requirement is :math:`-93 dBm` [FIX ME and ref]. Operating at :math:`2.4 GHz` and examining distance as a function of transmit power we can observe the limited range of Pluto alone in orange in the figure below. However, by adding a :math:`20 dBm` amplifier to Pluto we can substantially increase its range.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/range.svg
   :alt: range.svg
   :align: center

Practical things
================

Theory of Operation
-------------------

In a basic sense, amplifiers can be thought of as a tradeoff between signal gain and signal corruption. Gain is simply the ratio of the input to output signal amplitude. However, signal corrupt comes fin many forms but usually categorized as noise and distortion.

Power Supply Rejection Ratio (PSSR)
-----------------------------------

If the supply of an amplifier changes, its output should not, but it typically does. If a change of X volts in the supply produces an output voltage change of Y volts, then the PSRR on that supply (referred to the output, RTO) is X/Y. The dimensionless ratio is generally called the power supply rejection ratio (PSRR), and Power Supply Rejection (PSR) if it is expressed in dB. *However, PSRR and PSR are almost always used interchangeably, and there is little standardization within the semiconductor industry.*

PSSR can be expressed as a positive or negative value in dB, depending on whether the PSRR is defined as the power supply change divided by the output voltage change, or vice-versa. There is no accepted standard for this in the industry, and both conventions are in use.

Log and dB
----------

The power P\ :sub:`dBm` in dBm is equal to 10 times the base 10 logarithm of the power P\ :sub:`mW` in milliwatts (mW) divided by 1 milliwatt (mW):

:math:`P_{dBm} = 10 log_{10}(P_{mW}/{1mW})`

=========== ============
Power in mW Power in dBm
=========== ============
0.1 mW      -10 dBm
0.3 mW      -5 dBm
1 mW        0 dBm
3.2 mW      5 dBm
10 mW       10 dBm
32 mW       15 dBm
100 mW      20 dBm
316 mW      25 dBm
=========== ============

A doubling of output power (from 1mW to 2mW) is only +3dBm. A gain of +20dBm, is output power increasing by a factor of 100 times in mW.

Peak to Average
---------------

The peak-to-average power ratio (PAPR) is the peak amplitude squared (giving the peak power) divided by the RMS value squared (giving the average power).

:math:`PAPR_{%} = (t_{peak})^2/(t_{rms})^2 ;` :math:`PAPR_{dB} = 10 log_{10}(t_{peak})^2/(t_{rms})^2`

whether expressed in percent in dB, PAPR is dimensionless quantity.

When dealing with signals and amplifiers, it is the peak that we need to be concerned about, not the average power in the signal. Different types of modulation schemes have different peak to average power, and this needs to be taken into account.

P1dB
----

Normally, there is a direct relationship between input and output of an amplifier. As the input increases, the output increases the same amount. However, once the input reaches a certain level, the output signal begins to soft-limit, or compress. A parameter of interest here is the 1 dB compression point. This is the point where the output signal is compressed 1dB from an ideal input/output transfer function. This is shown in the figure within the region where the ideal slope = 1 line becomes dotted, and the actual response exhibits compression (solid).

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/p1db.svg
   :align: center

Typically, the 1 dB compression point is a function of frequency, and as one would expect, the distortion is worse at higher frequencies.

Noise
-----

Two techniques are typically used for analyzing the noise, but each can be cumbersome. Noise spectral density (NSD) defines the noise power per unit bandwidth. It is represented in mean-square dBm/Hz or dBFS/Hz for ADCs and rms nV/√Hz for amplifiers. This incompatibility in units provides an obstacle to calculating system noise when an amplifier is driving an ADC, or a DAC is driving an amplifier.

Noise figure (NF) is the log ratio of input SNR to the output SNR expressed in decibels. This specification, commonly used by RF engineers, makes sense in a purely RF world, but attempting to use NF calculations in a signal chain with an ADC can lead to misleading results.

Distortion
----------

When a spectrally pure sinewave passes through an amplifier (or other active device), various harmonic distortion products are produced depending upon the nature and the severity of the non-linearity. However, simply measuring harmonic distortion produced by single tone sinewaves of various frequencies does not give all the information required to evaluate the amplifier's potential performance in a communications application. In most communications systems there are a number of channels which are "stacked" in frequency. It is often required that an amplifier be rated in terms of the intermodulation distortion (IMD) produced with two or more specified tones applied.

Intermodulation distortion products are of special interest in the IF and RF area, and a major concern in the design of radio receivers. Rather than simply examining the harmonic distortion or total harmonic distortion (THD) produced by a single tone sinewave input, it is often required to look at the distortion products produced by two tones.

As shown in the figure, two tones f\ :sub:`1` and f\ :sub:`2` will produce second and third order intermodulation products.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/ip2andip3.svg
   :width: 500px

The example shows the second and third order products produced by applying two frequencies, f\ :sub:`1` and f\ :sub:`2`, to a nonlinear device.

+-----------------+--------------------------------------------------------------------------+
| Order of Mixing | Location of mixing products/Harmomics                                    |
+=================+==========================================================================+
| first order     | :math:`2f_{1}, 2f_{2}` , :math:`3f_{1}, 3f_{2}` , :math:`4f_{1}, 4f_{2}` |
+-----------------+--------------------------------------------------------------------------+
| second order    | :math:`f_{1} - f_{2}, f_{1} + f_{2}`                                     |
+-----------------+--------------------------------------------------------------------------+
| third order     | :math:`2f_{1} - f_{2}, 2f_{2} - f_{1}, 2f_{1} + f_{2}, 2f_{2} + f_{1}`   |
+-----------------+--------------------------------------------------------------------------+

The second order products located at f\ :sub:`2` + f\ :sub:`1` and f\ :sub:`2` – f\ :sub:`1` are located far away from the two tones, and may be removed by filtering. The third order products located at 2f\ :sub:`1` + f\ :sub:`2` and 2f\ :sub:`2` + f\ :sub:`1` may likewise be filtered. The third order products located at 2f\ :sub:`1` – f\ :sub:`2` and 2f\ :sub:`2`– f\ :sub:`1`, however, are close to the original tones, and filtering them is difficult.

Third order IMD products are especially troublesome in multi-channel communications systems where the channel separation is constant across the frequency band. Third-order IMD products from large signals (blockers) can mask out smaller signals.

Power Supply Limits
-------------------

The relationship between dBm (power with respect to 1mW) and Volts peak-peak for a sinusoidal signal in a 50-Ohm systems is:

=== ==== ================= ================
dBm mW   Volts\ :sub:`rms` Volts\ :sub:`pp`
=== ==== ================= ================
-10 0.1  70.711 mV         199.970 mV
0   1    223.607 mV        632.360 mV
5   3.16 0.398 V           1.125 V
10  10   0.707 V           2.000 V
15  31.6 1.257 V           3.556 V
20  100  2.236 V           6.324 V
25  316  3.976 v           11.246 V
=== ==== ================= ================

The question is, how do we get +20dBm (6.324V :sub:`peak-peak`) out of a system, when the power supply is limited to 5V? The trick is in how we connect the output stage. The output stage (RFOUT) is connected to Vcc through the inductor L1. From a DC perspective, inductors become short circuits, and RFOUT is setting at 5.0V, allowing a 10V\ :sub:`peak-peak` swing from the amplifier. This is also why it is AC-coupled by the output capacitor before it attaches to the antenna.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/adl5606.svg
   :align: center

Power Dissipation
-----------------

Supply Current in the ADL5606 datasheet is specified for a max on 390mA at 5.0V (or 1.95W). Although the ADL5606 is packaged in a thermally efficient 4 mm × 4 mm, 16-lead LFCSP (thermal resistance from junction to air (θ\ :sub:`JA`) is 52.9°C/W. This 1.95W dissipation times the θ\ :sub:`JA` is a temperature increase of 103.2 °C. Given a maximum junction temperature of 150°C, we either only use the part in sub 46.845°C environments, or work harder on spreading the heat out of the package, onto the PCB.

S Parameters
------------

`Scattering <https://en.wikipedia.org/wiki/Scattering_parameters>`__ or S-parameters are commonly used to characterize 2-port networks. An S-parameter indicates the amount of power leaving one port of the network, given power entering another (or the same) port of the network. For a two port network (one input, one output), we number the ports 1 and 2, and measure 4 different ratios:

============ ============ =============
Measurement  Leaving Port Entering Port
============ ============ =============
S\ :sub:`11` 1            1
S\ :sub:`12` 1            2
S\ :sub:`21` 2            1
S\ :sub:`22` 2            2
============ ============ =============

.. image:: http://www.analog.com/-/media/analog/en/landing-pages/technical-articles/improve-s21-flatness-measurements/s21.jpg
   :alt: http://www.analog.com/-/media/analog/en/landing-pages/technical-articles/improve-s21-flatness-measurements/s21.jpg
   :align: center

In the case of S\ :sub:`21`, the suffix “\ :sub:`21`\ ” denotes the power leaving port 2, with power delivered to port 1. Note that in the RF world, S-parameters are measured using a 50Ω system. The source impedance driving port 1 must be 50Ω, and the load impedance presented to port 2 must also be 50Ω.

Depending on what you are measuring - each measurement can be more important than another. For example, for an amplifier, S\ :sub:`21` measures the gain of the amplifier, with port 1 being the input and port 2 being the output. If an amplifier's S\ :sub:`21`\ =0 dB, the amplifier has a gain of 1. For an antenna, S\ :sub:`11` represents how much power is reflected from the antenna back, and therefore is known as the reflection coefficient (or return loss). If an antenna's S\ :sub:`11`\ =0 dB, then all the power being sent to the antenna is reflected from the antenna and nothing is radiated.

S Parameters are normally measured over frequency, as a good amplifier will have a flat gain over frequency. When the gain varies over frequency, it is often called ripple. Ripple is evident once S\ :sub:`21` is measured over frequency.

Measurements
============

Signal To Noise Ratio
---------------------

When we consider the performance of a communication link, in the most basic sense, we are interested in the bandwidth and power of the transmitted signal. Bandwidth is measured from the power spectral density of signal and is also proportional to the bit rate. We define average energy per bit as:

:math:`overlineE_b = overline{E}_s/log_2(M)`

where :math:`M` is the order of the modulation scheme and :math:`overlineE_s` is the average symbol energy. Note that :math:`overlineE_b` is of units Joules/bit. When considering an Additive White Gaussian Noise (AWGN) channel, we can write the power efficiency as :math:`overline{E}_b/N_0` , where :math:`N_0` is the noise power spectral density (PSD). Since AWGN is flat in frequency, or equal across all frequencies, channel noise can typically be measured over 1 Hz of spectrum. Therefore, :math:`N_0` is in units Watts/Hz :math:`right` Joules. :math:`overline{E}_b/N_0` can be alternatively understood as normalized signal-to-noise ratio (SNR) and is related by the bitrate :math:`R_b` and channel bandwidth :math:`B`

:math:`SNR = overline{E}_b/N_0 \times R_s/B.`

SNR is commonly expressed in SNR in decibels (dB) and the equation above can be rewritten as:

:math:`\displaystyle SNR_{dB} = 10log_{10}(overline{E}_b/N_0) + 10log_{10}\frac{R_s}{{B}}`

When determining SNR of a signal it is important to understand that signals are band limited unlike noise. Therefore, as the observation bandwidth of the signal is increased the SNR becomes worse.

Noise Generation and Power
--------------------------

Calculation of power is a non-trivial exercise in practice and in many situations loosely defined. This is especially true when determining SNR. Let us first consider a unique example where we have scaled exponentials ( :math:`s(t) = \alpha exp(j \pi f_c t)` ) in AWGN. A resulting FFT provided in the figure below, generated from some simple code for two different source signals:

::

     r = signal+noise;
     % View averaged spectrum
     freq = linspace(-bandwidth/2,bandwidth/2,fftLen);
     R = reshape(r,fftLen,frames);
     R = fftshift(fft(R));
     R_mean = mean(abs(R),2)/fftLen;
     plot(freq,10*log10(R_mean));

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/snr_guess_dual-eps-converted-to-1.png
   :align: center
   :width: 600px

An obvious question to ask would be "What is the SNR of these signals?". However, we cannot directly derive the SNR from this plot alone. If we are using a spectrum or vector analyzer we need knowledge of the Resolution Bandwidth (RBW), which is a function of the FFT bin count and observation bandwidth. Since we already know the observation bandwidth (1 MHz), if we used a FFT of size 1024, then the true SNR is ~10 dB. An important aspect to note from the figure above is the shape of the signals :math:`r_1` and :math:`r_2` . In generation these two signals only differ in :math:`f_c` , although they appear quite different in the figure. :math:`r_2` was strictly chosen to be within a FFT bin and :math:`r_2` strattles bins. This difference is due to the window effect of the FFT applied to the signals. This is commonly known as *scalloping* and will be dependent on the window chosen. fred harris (yes that capitalization is correct) provides a detailed overview of different windows and how to compensate for their effects in [harris1978]. When performing digital signal processing it is alway important to understand effects of discrete computations over the infinite resolution of our written equations.

Now let us connect this to the theoretical concepts. We know that the power spectral density (PSD) is obtained through a Fourier Transform of a signal's autocorrelation function. Formally written as:

:math:`S_{XX}(f) = int-inftyinftyR_{XX}(\tau)e^{-j2 \pi f \tau} d\\tau`

where the autocorrelation of our process or signal :math:`X(t)` is:

:math:`R_{XX}(t_1,t_2) = E[X(t_1)X^{ast}(t_2)]` .

In the case of AWGN this autocorrelation is simply:

:math:`R_{XX}(t_1,t_2) = \sigma^2` (if :math:`t_1=t_2` , :math:`0` otherwise)

where :math:`\sigma^2` is the variance of the noise. Therefore, :math:`S_{XX}=\sigma^2` for all frequencies within the observation bandwidth. Therefore, the power of the AWGN signal is simply :math:`P_N = \sigma^2 \times B` . This result provides a mechanism for determining power from the PSD or frequency domain of a signal. However, it can be useful to calculate signal power from the time domain, and from Parseval's theorem we know power is identical between domains. For an AWGN signal calculating the variance directly provides :math:`P_N` , but this is not true for non-zero mean processes. In that case, power can be simply calculated based on the squared RMS or squared mean of the process samples. However, a significant amount of data should be collected to get a representative power value of the signal. In MATLAB for a complex input signal the power is simply:

::

   signalpower = sqrt(mean(signal.*conj(signal)))^2;

However, the power unit is a bit tricker to determine. An instrument will provide the I/Q data in voltage based on some input impedance. Therefore, we can calculate the power directly in dBm easily:

:math:`\displaystyle P_{dBm} = 10log_{10} (P_{RMS}/1mW) = 10log_{10} \frac{I^2+Q^2}{2/R \times 1mW}`

where :math:`R` is the input resistance of the device. For an SDR I/Q values will be based on some uncalibrated ADC values and we typically define them of unit dBFS. Resulting in a power calculation that is not relatable to Watts. If it was desired to use an SDR an a instrument we would need to relate each output of the ADC to a specific input voltage at the antenna. This mapping would allow us to accurate measure quantities in SI units instead of relative units.

.. _s-parameters-1:

S Parameters
------------

This data was taken on a `Keysight ENA E5080A <https://www.keysight.com/en/pdx-x202208-pn-E5080A/ena-vector-network-analyzer?>`__:

First we calibrate things with a cable, and connector, to make sure we see what is happening. We expect this to be a flat line, with 0dB of gain. (it is a cable after all).

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/cal_s21.png
   :alt: E5080A Calibration
   :width: 600px

Then we can look at the S12 of the amplifier board. Here we can see gain between 2 and 3 GHz, with the flat part being between 2.4 and 2.5 GHz, just like we hope.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/c419_s21.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/c419_s21_zoom.png
   :width: 600px

If we vary the amplitude at a constant frequency, we can see the P1dB point at +5dBm. In order to keep things operating in the linear region, we should make sure not to drive the amplifer board with more than +5dBm.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/c419_p1db.png
   :width: 600px

Results
-------

The yellow line is an antenna, the red line is with the same antenna and the amplifier. You can see the +20dB of transmission at 2.4GHz.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/c419_s21_ant_amp.png
   :width: 600px
