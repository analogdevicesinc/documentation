Chapter 20: Analog to Digital Conversion
========================================

20.1 What they do
-----------------

Analog-to-Digital converters (ADC) translate analog signals, real world signals like temperature, pressure, voltage, current, distance, or light intensity, into a digital representation of that signal. This digital representation can then be processed, manipulated, computed, transmitted or stored.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f1.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.1 Analog to Digital conversion


In many cases, the analog to digital conversion process is just one step within a larger measurement and control loop where digitized data is processed and then reconverted back to analog signals to drive external transducers. These transducers can include things like motors, heaters and acoustic divers like loudspeakers. The performance required of the ADC will reflect the performance goals of the measurement and control loop. ADC performance needs will also reflect the capabilities and requirements of the other signal processing elements in the loop.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f2.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.2 Measurement and Control Loop


20.2 Basic Operation
--------------------

An ADC samples an analog waveform at uniform time intervals and assigns a digital value to each sample. The digital value appears on the converter’s output in a binary coded format. The value is obtained by dividing the sampled analog input voltage by the reference voltage and them multiplying by the number of digital codes. The resolution of converter is set by the number of binary bits in the output code.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f3.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.3 Digital output code


An ADC carries out two processes, sampling and quantization. The ADC represents an analog signal, which has infinite resolution, as a digital code that has finite resolution. The ADC produces 2N digital values where N represents the number of binary output bits. The analog input signal will fall between the quantization levels because the converter has finite resolution resulting in an inherent uncertainty or quantization error. That error determines the maximum dynamic range of the converter.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f4.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.4 Quantization Process


The sampling process represents a continuous time domain signal with values measured at discrete and uniform time intervals. This process determines the maximum bandwidth of the sampled signal in accordance with the Nyquist Theory. This theory states that the signal frequency must be less than or equal to one half the sampling frequency to prevent aliasing. Aliasing is a condition in which frequency signals outside the desired signal band will, through the sampling process, appear within the bandwidth of interest. However, this aliasing process can be exploited in communications systems design to down-convert a high frequency signal to a lower frequency. This technique is known as under-sampling. A criterion for under-sampling is that the ADC has sufficient input bandwidth and dynamic range to acquire the highest frequency signal of interest.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f5.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.5 Sampling Process


Sampling and quantization are important concepts because they establish the performance limits of an ideal ADC. In an ideal ADC, the code transitions are exactly 1 least significant bit (LSB) apart. So, for an N-bit ADC, there are 2N codes and 1 LSB = FS/2N, where FS is the full-scale analog input voltage. However, ADC operation in the real world is also affected by non-ideal effects, which produce errors beyond those dictated by converter resolution and sample rate. These errors are reflected in a number of AC and DC performance specifications associated with ADCs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f6.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.6 Transfer Function for an Ideal ADC


Any analog input in this range gives the same digital output code.

20.3 Understanding Key Specifications
-------------------------------------

+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Specification and terms, units of measure                  | Meaning                                                                                                                                                     | Significance                                                                                                                                             |
+============================================================+=============================================================================================================================================================+==========================================================================================================================================================+
| DC specifications                                          |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Resolution or bits                                         | Number of bits representing an analog signal, generally ranging from 6 to 24.                                                                               | Determines how small an input can be resolved.                                                                                                           |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                            |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Conversion speed or rate, ksamples/s or Msamples/s         | The number of repetitive conversions per second for a full-scale change to specified resolution and linearity                                               | Determines the fastest sampling capability of the ADC                                                                                                    |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Least significant bit (LSB)                                | The right-most bit in an ADC output code. LSB size is a function of converter resolution.                                                                   | Not a specification, but a common term.                                                                                                                  |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Most significant bit (MSB)                                 | The left-most bit in an ADC output code.                                                                                                                    | Not a specification, but a common term.                                                                                                                  |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Differential nonlinearity (DNL), expressed in terms of LSB | The deviation from the ideal (1 LSB) code width between any two adjacent codes. In an ideal converter, every code is exactly the same size and DNL is zero. | DNL, INL, offset error, and gain error specify how accurately the data represents the signal across the entire internal and external range.              |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Integral nonlinearity (INL), expressed in terms of LSB     |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| (also referred to as                                       |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| "relative accuracy error")                                 |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                            | The deviation of an actual code transition point from its ideal position on a straight line drawn between the end points of the transfer function.          | The narrowing or widening of code widths caused by DNL can lead to "missing codes" and add noise and frequency spurs beyond the effects of quantization. |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Offset, expressed in terms of LSB                          | The difference between the ideal and actual output when the converter input is zero.                                                                        | INL describes the absolute                                                                                                                               |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| accuracy of a converter.                                   |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Calculated after offset and gain errors are removed.       |                                                                                                                                                             |                                                                                                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gain error/full-scale error, expressed in terms of LSB     | The difference between the ideal and actual output when the converter input is at full scale.                                                               | INL produces additional harmonics and spurs in the frequency domain.                                                                                     |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f7.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.7 ADC Transfer Function with DNL Error


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f8.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.8 ADC Transfer Function with INL Error


+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Specification and terms, units of measure                               | Meaning                                                                                                                                                                        | Significance                                                                                                                                   |
+=========================================================================+================================================================================================================================================================================+================================================================================================================================================+
| AC specifications                                                       |                                                                                                                                                                                |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Spurious-free dynamic range (SFDR), dB                                  | The ratio of the fundamental frequency's amplitude to that of the largest spurious signal in a given bandwidth.                                                                | Important in communications                                                                                                                    |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| applications where a spur may                                           |                                                                                                                                                                                |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| interfere with a neighboring channel.                                   |                                                                                                                                                                                |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Total harmonic distortion                                               |                                                                                                                                                                                |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| (THD), dB                                                               | The ratio of the rms sum of the first six harmonics to the amplitude of the fundamental frequency.                                                                             | Harmonics are noise components related to, or generated by, a-d conversion. Harmonics can limit the dynamic performance of a converter.        |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Signal-to-noise-and-distortion ratio (SINAD ), dB                       | The ratio of the rms signal amplitude to the mean value of the root-sum-squares (RSS) of all other spectral components including harmonics but excluding dc.                   | SINAD indicates the true ac linearity an ADC because it includes the effects of the 2nd and 3rd harmonics                                      |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                         |                                                                                                                                                                                |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Effective number of bits (ENOB)                                         | ENOB = SINAD ...1.76 dB 6.02                                                                                                                                                   | ENOB specifies the dynamic                                                                                                                     |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| performance of a given ADC as compared to an ideal converter.           |                                                                                                                                                                                |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Signal-to-noise ratio (SNR) or signal-to-noise ratio without harmonics. | Similar to SINAD, the ratio of the rms signal amplitude to the mean value of the root-sum-squares of all other spectral components, excluding the first five harmonics and dc. | SNR indicates noise performance of a converter compared to an ideal converter.                                                                 |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Analog bandwidth (full-power, small signal), kHz or MHz                 | The input frequency where the fundamental in an FFT of the output rolls off by 3 dB. Generally determined by the                                                               |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Converter's sample-and-hold amplifier.                                  | Important in IF under-sampling applications. This spec may not be compatible with the ADC's maximum sampling rate.                                                             |                                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Power dissipation, mW or W                                              | The amount of power consumed by the converter.                                                                                                                                 | Important for power-sensitive applications in which battery life, temperature, or space limitations may affect power dissipation requirements. |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f9.gif
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 20.9 Frequency Domain Specifications


20.4 ADC Classifications
------------------------

Speed and accuracy are two critical measures of ADC performance. As such, they provide a means for broadly categorizing today’s monolithic ADCs. ADC chips may be loosely grouped along these lines as general-purpose, high-speed, or precision. Converters with 8- to 14-bit resolution and conversion rates below 10 Msamples/s are typically considered general-purpose ADCs. Those with conversion rates above 10 Msamples/s usually get the high-speed moniker, while those with 16 bits or more of resolution fall into the precision ADC category.

These definitions, however, are somewhat arbitrary and largely reflect the current state-of-the-art.

Within these broad categories, ADCs may also be grouped according to converter architecture. The most popular types are flash, pipelined, successive approximation- register, and sigma-delta. Each architecture offers certain advantages with respect to conversion speed, accuracy, and other parameters. The characteristics associated with each architecture help determine its suitability for a given application.

ADCs have been implemented both as discrete Designs’ sometimes constructed with hybrid packaging and as monolithic designs implemented as integrated circuits (ICs). Much of the discussion of ADC performance within these pages relates specifically to ADCs in IC form. Development of monolithic ADCs has been heavily influenced by process innovation, both in high-end processes such as bipolar, biCMOS, and SiGe, as well as mainstream CMOS processes.

Over time, the migration of ADC designs to CMOS processes with smaller geometries has increased the possibilities for performance enhancements, while also allowing higher levels of integration. That integration can increase the number of conversion channels achieved on a single die, or allow conversion- related functions to be brought on-chip. As a result, die size and, consequently, package size depend on the semiconductor process employed. The process also determines supply voltage, which along with conversion speed, influences power dissipation.

20.5 How It Works - Flash Architecture
--------------------------------------

In the flash or parallel ADC architecture, an array of 2N-1 comparators converts an analog signal to digital with a resolution of N bits. The comparators receive the analog signal on one input and a unique fraction of the reference voltage on the other. The reference voltage for each comparator is often a tap off a resistive voltage divider, whereby the comparators are biased in voltage increments equivalent to 1 LSB. The comparator array is clocked simultaneously.

The comparators with reference voltages less than the analog input will output a digital one. The comparators with reference voltages greater than the analog input will output a digital zero. When read together, the outputs present a "thermometer code," which the output logic converts to standard binary code.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f10.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.10 Flash Architecture


Pros:

+ Very fast„ converts in one ADC clock cycle.

Cons:

| - Requires many comparators. The physical limits of monolithic integration generally allow only up to 8 bits of resolution per ADC chip.
| - High input capacitance.

20.6 How It Works - Pipeline Architecture
-----------------------------------------

This architecture divides the conversion into two or more stages. Each stage consists of a sample-and-hold (S/H) circuit, an m-bit flash ADC, and a DAC. The analog signal is fed to the first stage, where it’s sampled by the S/H and converted to a digital code by the flash ADC. The code generated by the flash ADC in this stage represents the most significant bits of the ADC’s final output.

The same code is then fed to the DAC, which reconverts the code back to an analog signal that is subtracted from the original, sampled analog input signal. The resulting difference signal or residue, is next amplified and sent on to the following stage in the pipeline, where the whole process is repeated. The number of stages needed depends on the required resolution and the resolution of the flash ADCs used in each stage. In theory, the overall resolution of the ADC would be the sum of the resolutions of the flash ADCs. But in practice, some extra overlapping bits are required for error correction.

Pros:

| + Not as fast as pure flash architecture, but achieves higher resolutions and dynamic range.
| + Handles wideband inputs.
| + Use of dither noise and averaging increases the effective resolution of the converter.
| + Permits under sampling of wideband IF signal.

Cons:

| - Pipeline delay. Total throughput can be equal to that of a flash converter (one conversion per cycle), but with a latency or pipeline delay equal to the number of stages.
| - Accuracy of conversion depends on the DAC linearity.
| - Ill-suited to applications where conversion results must be available immediately after the sample clock.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f11.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.11 Single Pipelined Converter Stage


20.7 How It Works - SAR Architecture
------------------------------------

The SAR converter works like a balance scale that compares an unknown weight against a series of known weights. In lieu of weights, the SAR converter compares the analog input voltage against a series of successively smaller voltages representing each of the bits in the digital output code. These voltages are fractions of the full-scale input voltage (1/2, 1/4, 1/8, 1/16...1/2\ :sup:`N`, where N=number of bits).

The first comparison is made between the analog input voltage and a voltage representing the most significant bit (MSB). If that analog input voltage is greater than the MSB voltage, the value of the MSB is set to 1, otherwise it’s set to 0. The second comparison is made between the analog input voltage and a voltage representing the sum of the MSB and the next most significant bit. The value of the second most significant bit is then set accordingly. The third comparison is made between the analog input voltage and the voltage representing the sum of the three most significant bits. At this point, the value of the third most significant bit is set. The process repeats until the value of the LSB is established.

Pros:

| + Uses a single comparator to achieve high resolution, resulting in small die size for monolithic ADCs.
| + No pipeline delay.
| + Well-suited for non-periodic inputs.
| + Use of dither noise and averaging increases the effective resolution of the converter.
| + Permits under-sampling.

Cons:

| - Requires N comparisons to achieve N-bit resolution, which is more than both flash and pipelined.
| - Accuracy of conversion depends on the DAC linearity and comparator noise.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f12.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.12 Successive-Approximation-Register (SAR) ADC


20.8 How It Works - Sigma-Delta Architecture
--------------------------------------------

The basic elements of this architecture are an integrator, a comparator, and a one-bit DAC, which together form a sigma-delta modulator. The modulator subtracts the DAC from the analog input signal and then feeds the signal to the integrator. The output of the integrator then goes to a comparator, which converts the signal to a one-bit digital output. The resulting bit is fed to the DAC, which produces an analog signal to be subtracted from the input signal. The process repeats at a very fast “oversampled rate."

The modulator produces a binary stream in which the ratio of ones to zeros is a function of the input signal’s amplitude. By digitally filtering and decimating this stream of one and zeroes, a binary output representing the value of the analog input is obtained.

Pros:

| + Yields the highest precision for lower input-bandwidth applications.
| + Permits noise shaping whereby low-frequency noise is moved to higher frequencies, outside the band of interest.
| + Oversampling reduces requirements for anti-aliasing filtering.

Cons:

| - Latency is much greater than with other architectures.
| - Oversampling and latency discourage the use of sigma-delta ADCs when digitizing multiplexed input signals.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f13.gif
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 20.13 Sigma-Delta Architecture


**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/tutorials/cmos-dac-chapter>`

**Go to Next Chapter**

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
