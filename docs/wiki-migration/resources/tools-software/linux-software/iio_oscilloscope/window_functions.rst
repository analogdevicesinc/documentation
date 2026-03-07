FFT Window Functions
====================

Background
----------

In mathematics, a `Fourier transform <https://en.wikipedia.org/wiki/Fourier transform>`_ (FT) is a mathematical transform that traditionally decomposes time based functions (eg :math:`f(t)` or :math:`x(t)` ) into functions in the frequency domain (eg :math:`X(\omega)` or :math:`hatf(\omega)` ), and is defined by this tranform:

:math:`X(\omega) = int-infty+inftyx(t) e^{-2 \pi i \omega t} dt`

The Fourier transform of a function of time :math:`x(t)` , is a complex-valued function of frequency :math:`X(\omega)` , whose magnitude (absolute value of the complex value) represents the amount of that frequency present in the original function, and whose argument is the phase offset of the basic sinusoid in that frequency.

One of the key representations/requirements of the math is that integration is done from :math:`-infty` to :math:`+infty` time units (seconds, days, months, years, etc), and that the function :math:`f(t)` is continuous (no abrupt changes in value, or discontinuities). Things can change rapidly, but a function is only continuous if arbitrarily small changes in its value can be assured by restricting to sufficiently small changes of its argument.

The `discrete Fourier transform <https://en.wikipedia.org/wiki/discrete Fourier transform>`_ transforms a sequence of N complex numbers representing time domain data (such as :math:`delimlbracex_nrbrace = x_0, x_1, ..., x_{N-1}` into another sequence of complex numbers representing frequency domain data (such as :math:`delimlbraceX_krbrace = X_0, X_1, ..., X_{N-1}` and is defined by:

:math:`X_k = sumn = 0N -1x_n e^{{2 \pi i k}/{N}}`

For those what want to understand what is really going on in a very intuative description, spend the 20 min and watch the video by `Grant Sanderson <https://www.3blue1brown.com/>`_ on his excellent `3Blue1Brown <https://www.youtube.com/3Blue1Brown>`_ Youtube channel, which describes this in a very initiative, math-light methodology (which some prefer).

.. image:: https://wiki.analog.com/_media/youtube>spUNpyF58BY
   :alt: youtube>spUNpyF58BY
   :width: 500px

However - even when using modern algorithms like the `Fast Fourier transform <https://en.wikipedia.org/wiki/Fast Fourier transform>`_ are used, those tenets still apply:

-  the input is an infinite, continuous, complex valued time series
-  the output is an infinite, continuous, complex valued frequency series

If you are capturing a sine wave on a converter, it's important to make sure you understand how the FFT/DFT is working, since it can dramatically effect the output. The easiest way to understand things, is to work through an example. Although the numbers may seem arbitrary - they are based on prime numbers to keep things as uncorrelated as possible.

Sampling a complex 1.304639 MHz sine way at 11.503888 MSPS, on a 12-bit converter gives us this data:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64-samples.png
   :width: 600px

And if we look at the FFT of that we get:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64_fft_rect_line.png
   :width: 600px

If we try to look at the points only, to better understand what's going on, it's just as puzzling. We are only putting in a single size wave, but we clearly see the DFT thinks there is more than one, and there is lots of noise everywhere (the noise floor of -38 dB is only ~6 ENOB [1]_ of dynamic range - so we need to understand what is going on..

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64_fft_rect.png
   :width: 700px

which is actually pretty terrible performance. What we forgot is that the DFT thinks that the data is:

-  the input is an infinite, continuous, complex valued time series
-  the output is an infinite, continuous, complex valued frequency series

If we think of the data like that - we can clearly see that there is a giant discontinuity between repeating buffers.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/repeated-64-samples.png
   :width: 800px

So, we need a way to remove the discontinuous samples at the start and the end of the function. A simple way to do that is to use coherent sampling, and ensure that we only have full sine waves in our buffer. This would limit the measurements to integers of sample rate divided by the number of samples we are taking.

:math:`F_{measured} = k Sample Rate/N_{Samples}`

In this case, of sampling a complex 2.5 MHz sine way at 10 MSPS, using 64-points (exactly 4 samples per full sine wave cycle, 16-waveforms per capture, where the on a 12-bit converter gives us this data (in the time and frequency domain).

|image1| |image2|

While this does improve the results (our noise floor is now ~ -85 dBFS, or an ENOB of greater than 12-bits). Sampling everything coherently would severely limit the practical effectiveness using the DFT to analyze unknown signals / spectrum.

Reverting back to our previous example of capturing a complex 1.304639 MHz sine way at 11.503888 MSPS, on a 12-bit converter, we need to have some way of reducing the discontinuities between buffers/samples. A way to do this would be to pass the data through a "window" function before computing the DFT to manipulate the data, and eliminate the possibility of discontinuities at the start/ends of the samples. A simple Window function is the "Triangle Window",

|image3| |image4|

This improves our results, but also changes the DFT results, so we need to understand what's happening in the math to ensure we don't misinterpret the changes we are making. What we have done is added a window function :math:`w(t)` into the FFT equation.

:math:`Result = int-infty+inftyw(t) x(t) e^{-2 \pi i \omega t} dt`

Multiplication in the time domain is `convolution <https://en.wikipedia.org/wiki/Convolution_theorem>`_ in the frequency domain (where the '∗' symbol is the convolution operator):

:math:`Result = W(\omega)` ∗ :math:`X(\omega) = int-infty+inftyw(t) x(t) e^{-2 \pi i \omega t} dt`

This is why it is critical to understand both the time domain and frequency domain changes that might occur from applying a specific window function.

Choosing a Window Function
==========================

A `window function <https://en.wikipedia.org/wiki/Window_function>`_ is a mathematical function that is normally symmetric around the middle of the interval, usually near a maximum in the middle, and usually tapering away from the middle.

Each `window function <https://en.wikipedia.org/wiki/Window_function>`_ has its own characteristics and suitability for different applications (some are more frequency accurate, others are more amplitude accurate). To choose a window function, you (the user) must select the most appropriate one. Some suggestions:

-  Sine wave or combination of sine waves: Hann
-  Sine wave (amplitude accuracy is important): Flat Top
-  Narrowband random signal (vibration data): Hann
-  Broadband random (white noise): Rectangular
-  Closely spaced sine waves: Uniform, Hamming
-  Excitation signals (hammer blow): Force
-  Response signals: Exponential
-  Unknown content: Hann
-  Two tones with frequencies close but amplitudes very different: Kaiser-Bessel
-  Two tones with frequencies close and almost equal amplitudes: Rectangular

Hann Window
-----------

`Hann <https://en.wikipedia.org/wiki//Hann_function>`_ (also known as Hanning, raised cosine, or von Hann) window, is named after the Austrian meteorologist `Julius von Hann <https://en.wikipedia.org/wiki/Julius_von_Hann>`_. The math looks like:

:math:`\displaystyle w[n] = \frac{1}{2}(1 - cos\frac{2 \pi n}{N})`

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/window_function-hann.png
   :width: 400px

Rectangular window
------------------

The rectangular window (also known as as boxcar, uniform or Dirichlet window) is the simplest window, equivalent to replacing all but N values of a data sequence by zeros, making it appear as though the waveform suddenly turns on and off.

:math:`w[n] = 1`

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/window_function-rectangular.png
   :width: 400px

Triangular
----------

Triangular windows are given by:

:math:`\displaystyle w[n] = 1 - delim|\frac{n - N}{2}/\frac{N}{2}{|}`

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/window_function-triangular.png
   :width: 400px

Welch
-----

The Welch window consists of a single parabolic section:

:math:`\displaystyle w[n] = 1 - (n - \frac{N}{2}/\frac{N}{2})^2`

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/window_function-welch.png
   :width: 400px

Blackman
--------

General purpose Blackman windows are defined as:

:math:`\displaystyle w[n] = a_{0} - a_{1}cos\frac{2 \pi n}{N} + a_{2}cos\frac{4 \pi n}{N}`

The version that we implement is known as the *Exact Blackman* and uses:

-   :math:`\displaystyle a_{0} = \frac{7938}{18608}`
-   :math:`\displaystyle a_{1} = \frac{9240}{18608}`
-   :math:`\displaystyle a_{2} = \frac{1430}{18608}`

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/window_function-blackman.png
   :width: 400px

Cosine
------

The cosine window is also known as the sine window, as it represents half a cycle of a sinusoidal function,

:math:`\displaystyle w[n] = cos\frac{\pi n}{{N} - \pi/2} = sin\frac{\pi n}{{N}}`

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/window_function-cosine.png
   :width: 400px

Hamming
-------

Chebyshev
---------

Kaiser
------

Blackman-Harris
---------------

Flat Top
--------

3 Term Cosine
-------------

.. _term-cosine-1:

4 Term Cosine
-------------

.. _term-cosine-2:

5 Term Cosine
-------------

.. _term-cosine-3:

6 Term Cosine
-------------

.. _term-cosine-4:

7 Term Cosine
-------------

.. [1]
   Effective number of bits

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64_coherent_time.png
   :width: 420px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64_coherent_fft.png
   :width: 420px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64_triangle_time.png
   :width: 420px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/64_triangle_fft.png
   :width: 420px
