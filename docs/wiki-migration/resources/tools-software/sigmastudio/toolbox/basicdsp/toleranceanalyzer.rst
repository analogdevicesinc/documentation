Tolerance Analyzer
==================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| -------------------------------------------------------------------------------------------------------

|tolerancepic1.png| This block is for any application where you need to verify a given value's tolerance limits. It is especially useful for testing environments where the Sigma DSP needs to perform system diagnostics. The Tolerance Analyzer outputs either one or zero based on input level: if the level falls within the limits specified, it outputs one at the output pin; otherwise it outputs zero.

**Values in the controls are integer (32.0 or 28.0) format. Audio data is not directly compatible with these inputs; please refer to** :doc:`Numeric Formats </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/numericformats>` **for more information.**

| The operation of the Tolerance Analyzer can be readily understood from this graph:
| |tolerancepic2.png|
| The graph shows the instantaneous values at input and output pins of the Tolerance analyzer whose tolerance limits are 1-3.

As long as the input remains within the limit (1 - 3, designated by green lines), the block outputs 1. When the signal is out of (above or below) the limit, the block outputs 0.

.. |tolerancepic1.png| image:: https://wiki.analog.com/_media/tolerancepic1.png
.. |tolerancepic2.png| image:: https://wiki.analog.com/_media/tolerancepic2.png
