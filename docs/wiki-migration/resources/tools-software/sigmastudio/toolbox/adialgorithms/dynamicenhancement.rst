Dynamic Enhancement
===================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| The Dynamic Enhancement block provides variable bass enhancement as a function of input-signal level. Lower volume (input-signal) levels require more bass than higher levels. The filter dynamically adjusts the amount of bass enhancement depending on the volume of the input signal, by using a variable-Q filter.

| A fixed enhancement is applied to input levels below the threshold while a dynamic gain is applied to input levels above the threshold.
| |dynamicenhancepic1.png|
| There are four parameters available for control on the block, which are described below:

**Time Constant** – Enter a value for the Time Constant in the edit box, or use the updown arrows to change the value. The time constant can vary from 0 to 500 milliseconds. It controls the RMS time constant of the detector. Attack and release time will be longer as this parameter becomes larger.

**Threshold (dB)** - Enter a value for the Threshold in the edit box, or use the updown arrows to change the value. Threshold value can be from -24 to -20dB. Any signal into the detector below Threshold will not influence the boost calculation and receives a fixed Enhancement.

**Boost** – The Boost level is controlled using the Boost slider. The boost level is in the range from 0 dB to 20 dB and it controls the maximum boost level in the Dynamic Enhancement algorithm.

**Bass Freq.** – Enter a Bass Frequency value in the edit box below the boost slider, or click and drag the right-most arrow on the boost slider. The Bass Frequency can range from 20 to 300Hz, and it designates the center frequency of the boosting filter.

.. hint::

   Note: When the Boost is set to 0dB, signal still goes through the logic. So remember to remove the block if no dynamic enhancement is desired.


.. |dynamicenhancepic1.png| image:: https://wiki.analog.com/_media/dynamicenhancepic1.png
