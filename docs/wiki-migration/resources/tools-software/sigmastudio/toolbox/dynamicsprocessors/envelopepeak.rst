Envelope Peak
=============

| :doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| -----------------------------------------------------------------------------------------------------------

|envelopepeakpic1.png| The Peak Envelope is the envelope of the maximum or 'peak' levels of input signal over time, unlike the RMS envelope, which is essentially an average on the input level.

Hovering over the name says "Absolute Value Measurement Envelope Generator", so it (likely) uses an absolute value before finding the envelope.

There is also an "accurate" version, which (likely) uses inter-sample interpolation to measure "true peaks" and isn't necessary for most applications: :ez:`143717 <dsp/sigmadsp/f/discussions/65141/envelope-peak/143717>`

| **Controls:**
| |envelopepeakpic2.png|

.. |envelopepeakpic1.png| image:: https://wiki.analog.com/_media/envelopepeakpic1.png
.. |envelopepeakpic2.png| image:: https://wiki.analog.com/_media/envelopepeakpic2.png
