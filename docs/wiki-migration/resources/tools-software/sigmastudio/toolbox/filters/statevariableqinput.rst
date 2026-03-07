State Variable (Q Input)
========================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |stateqpic1.png| This block allows for simultaneous access to three different filter types: lowpass, highpass, bandpass. See :doc:`State-Variable Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariable>` for information about the parameters and calculations for this algorithm.

As can be seen from the figure (above right), this block has two inputs and three outputs. The green (standard input) pin is for the signal and the orange is for a value to control filter Q. It's common to control the Q of the filter either by sending a :doc:`DC input </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/dcinputentry>` value to this pin or by using it with the RMS table to generate Q parameters from the input signal instead.

To control Q from a block parameter, refer to the :doc:`State-Variable Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/statevariable>`.

The three output pins allows to choose among LP, HP, BP filters. This algorithm computes the coefficients for all filter types, giving simultaneous access. If your application does not require the use of all filter types, then the output may be connected to the :doc:`terminal block </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/schematicterminal>`.

Set the center frequency in the Freq (Hz) field or by dragging the <--> arrows.

The format for Q is 5.23 or 8.24 (depending on your processor), and it is inverted. In other words...

Input to Q pin = :math:`1/Q`

:ez:`dsp/sigmadsp/f/q-a/66757/numeric-format-for-state-variable-q-f-input`

.. |stateqpic1.png| image:: https://wiki.analog.com/_media/stateqpic1.png
