FMComms Math
============

.. note::

   This is still in a draft stage. If you have any comments, please comment on the :ez:`forums <community/fpga>`\


In a traditional radio transmit architecture, a baseband signal (voice or data), is modulated to an intermediate frequency (IF) and then modulated again to the transmit radio frequency (RF) and on the receive side, the opposite happened, from RF to IF to baseband. This was done since inexpensive up-converting modulators/down-converting demodulators only provide adequate performance over roughly one decade of frequency conversion, so it is often necessary to execute the complete up-conversion in two or more frequency hops.

This is no longer the case using modern modulator devices, such as the :adi:`ADL5375` or :adi:`ADL5380`. These provide up to 200MHz of baseband bandwidth, (fig 64 in the ADL5375 datasheet and fig 6 of ADL5380) and allow up/down conversion from 400 to 6000MHz. In order to use these types of devices, a *complex* (real and imaginary, not difficult) modulation/demodulation scheme must be used.

Like most mathematical derivations, we will ignore the real world imperfections, and these will be discussed at near the end.

Complex modulation
------------------

`Complex modulation <https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation>`__ is not difficult to understand at the very basics. We take have 2 baseband signals - for now, *I* and *Q*, where one is sine, and the other is cosine.

:math:`I = sin(\omega \times t)` ; :math:`Q = cos(\omega \times t)`

.. image:: http://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Sine_cosine_one_period.svg/500px-Sine_cosine_one_period.svg.png
   :alt: http://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Sine_cosine_one_period.svg/500px-Sine_cosine_one_period.svg.png
   :align: right
   :width: 400px

Since we know through trig identities (plus `Wikipedia <https://en.wikipedia.org/wiki/Trigonometric_functions>`__ says it's true) that:

:math:`cos(\omega \times t) == sin (\pi/2 - (\omega \times t))`

then:

:math:`I = sin(\omega \times t)` ; :math:`Q = sin(\pi/2 - (\omega \times t))`

these are the two signals coming out of the DAC - two sine waves, phase offset from each other, which we call I and Q, like the picture. Whether we call them both sine, or sine and cosine, is immaterial. Sometimes both are used, whatever is easier for the (a) math, or (b) conceptual understanding, and many people will swap back and forth depending on what is being discussed at that time.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/adl5375-fbl.gif
   :alt: ADL5375 Block Diagram
   :align: right
   :width: 200px

Most modern modulators, like the :adi:`ADL5375` will take the:

-  I multiply it by a LO (local oscillator),
-  Q multiply it by a LO (local oscillator) shifted by 90 degrees (which is the equivalent of cos())
-  add the resulting waveforms together.

:math:`LO_{I} = cos(\kappa)` ; :math:`LO_{Q} = sin(\kappa)`

:math:`LO_{I} \times I = cos(\kappa) \times sin(\omega)` ; :math:`LO_{Q} \times Q = sin(\kappa) \times cos(\omega)`

And a little `Summation Trig Identities <https://en.wikipedia.org/wiki/Trigonometric_functions#Identities>`__, turns into:

:math:`cos(\kappa) \times sin(\omega) + sin(\kappa) \times cos(\omega) = sin(\kappa + \omega)`

And you get single tone, which is multiplied by the carrier.

You can derive the same using `Euler's Formulas <https://en.wikipedia.org/wiki/Euler's_formula#Relationship_to_trigonometry>`__,

:math:`\displaystyle sin(\omega \times t) = \frac{e^{j \omega t} - e^{-j \omega t}}{j2}` ;

but we end up with the same thing -- a single tone on the RF output by taking three tones (I, Q, and LO) and multiplying and adding them.

Modulation
----------

Starting to modulating signal, just from an amplitude perspective:

:math:`LO_{I} = A \times cos(\kappa)` ; :math:`LO_{Q} = B \times sin(\kappa)`

We still have our carrier:

:math:`LO_{I} = cos(\kappa)` ; :math:`LO_{Q} = sin(\kappa)`

will have the resulting:

:math:`LO_{I} \times I = A \times cos(\kappa) \times sin(\omega)` ; :math:`LO_{Q} \times Q = B \times sin(\kappa) \times cos(\omega)`

That gives an output of:

:math:`x(t) = A \times cos(\kappa) \times sin(\omega) + B \times sin(\kappa) \times cos(\omega)`

This doesn't really match with Trig Identities, and it's easier to use easier (and by that I mean possible) to use Euler's Formulas

:math:`\displaystyle sin(x) = (\frac{1}{2}e^{-j x} - \frac{1}{2}e^{j x})` ; :math:`\displaystyle cos(x) = (\frac{1}{2}e^{-j x} + \frac{1}{2}e^{j x})`

therefore:

.. math::


   x(t) = A \times (\frac{1}{2}e^{-j \kappa} + \frac{1}{2}e^{j \kappa}) \times (\frac{1}{2}e^{-j \omega} - \frac{1}{2}e^{j \omega}) +
             B \times (\frac{1}{2}e^{-j \kappa} - \frac{1}{2}e^{j \kappa}) \times (\frac{1}{2}e^{-j \omega} + \frac{1}{2}e^{j \omega})

.. math::


   x(t) = \frac{A}{2} \times (e^{-j \kappa} + e^{j \kappa}) \times (e^{-j \omega} - e^{j \omega}) +
             \frac{B}{2} \times (e^{-j \kappa} - e^{j \kappa}) \times (e^{-j \omega} + e^{j \omega})

If we expand this, we get:

.. math::


   x(t) = \frac{1}{2} \times ((Ae^{-j \kappa -j \omega} + Ae^{j \kappa -j \omega} - Ae^{-j \kappa + j \omega} - Ae^{j \kappa + j \omega}) + 
             (Be^{-j \kappa -j \omega} - Be^{j \kappa -j \omega} + Be^{-j \kappa + j \omega} - Be^{j \kappa + j \omega}))

and then:

:math:`\displaystyle x(t) = \frac{1}{2} \times (((A+B)e^{-j \kappa -j \omega} + (A - B)e^{j \kappa -j \omega} - (A - B)e^{-j \kappa + j \omega} - (A + B)e^{j \kappa + j \omega}))`

we can re-arrange this as:

:math:`\displaystyle x(t) = \frac{1}{2} \times ((A+B)(e^{-j \kappa -j \omega} - e^{j \kappa + j \omega}) + (A - B)(e^{j \kappa -j \omega} - e^{-j \kappa + j \omega}) )`

and then:

:math:`\displaystyle x(t) = \frac{A+B}{2}(sin(\kappa + \omega)) + \frac{A-B}{2}(sin(\kappa - \omega))`

If this is due to amplitude mismatch, this creates something (an image) on the other side of the local oscillator.
