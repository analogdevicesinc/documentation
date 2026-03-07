State Variable
==============

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |statepic1.png| The State-Variable block allows for simultaneous access to three different filter types: lowpass, highpass, and bandpass.

Set the center frequency in the Freq (Hz) field or by dragging the arrows. For examples and details, see :doc:`Filters Example </wiki-migration/resources/tools-software/sigmastudio/tutorials/filterexamples>`.

To have external control over Q from the block, refer to the :doc:`State-Variable (Q input) Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariableqinput>`.

To have external control over Q and F from the block, refer to the :doc:`State-Variable (Q/F input) Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariableqfinput>`.

The three output pins let you choose among LP, HP, BP filters. The nature of this algorithm is to compute the coefficients for all filter types, giving you access to all of the filters simultaneously.

Parameter Calculation
---------------------

The following describes how the DSP uses input parameters to calculate the filter outputs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/statevariable_topology.png
   :align: center
   :width: 400px

:math:`\displaystyle f = 2 sin (\pi \frac{F }{ Fs})` :math:`\displaystyle q = \frac{1}{Q}`

:math:`D(z) = 1 + (f^2 + q f - 2) z^{-1} + (1 - q f) z^{-2}`

:math:`H_{BPF}(z) = f - f z^{-1} / D(z)` :math:`H_{HPF}(z) = 1 - 2z^{-1} + z^{-2} / D(z)` :math:`H_{LPF}(z) = f^2 z^{-1} / D(z)`

.. |statepic1.png| image:: https://wiki.analog.com/_media/statepic1.png
