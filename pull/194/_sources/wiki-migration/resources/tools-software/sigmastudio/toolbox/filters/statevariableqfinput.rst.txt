State Variable (Q/F Input)
==========================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |stateqfpic1.png| This block allows for simultaneous access to three different filter types: lowpass, highpass, bandpass. See :doc:`State-Variable Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariable>` for information about the parameters and calculations for this algorithm.

This block performs the same function as the :doc:`State Variable Q Input </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariableqinput>`, with the difference being the frequency is now controlled by a third input pin called 'Frequency Input' instead of text window entry.

The format for Q is 5.23 or 8.24 (depending on your processor), and it is inverted. In other words...

Input to Q pin = :math:`1/Q`

The format for F is also 5.23 or 8.24, and the calculation is:

Input to F pin = $2 sin{\\pi f} / {f_s} $

where the filter cutoff frequency is :math:`f` and the sample rate is :math:`f_s` . The sine argument is unitless (radians).

.. |stateqfpic1.png| image:: https://wiki.analog.com/_media/stateqfpic1.png
