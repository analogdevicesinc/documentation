Dynamic Bass Boost
==================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| The Dynamic Bass Boost block provides boost that varies with input-signal level: lower levels require, and receive, more bass than higher levels. Using a variable-Q filter, this block dynamically adjusts the amount of boost.

The filter calculates its bass boost between the Threshold and the Min(imum) Gain settings. A fixed maximum is applied to inputs above minimum gain and below threshold.

| Seven parameters, described below, control this block's performance. Enter their values in the appropriate field or use the arrows. While it is important for you to know how these parameters work and precisely what they do, nothing surpasses playing with each one and getting a feel for how it affects, singly and in combination, the sound you are trying to achieve.
| |DynamicBasspic1.png|

**Lowpass Freq** - The lowpass frequency ranges from 20Hz to 250Hz; frequencies below the selected point are used by the detector for determining the boost amount.

**High Threshold (dB)** - The high threshold value, ranging from -20 to 10dB, sets the upper point for detector action. Signals higher than the minimum gain will not influence the boost calculation; they're boosted a fixed amount.

**Time Constant** - Ranging from 0 to 500 ms (milliseconds), this controls the rms time constant for the detector, changing attack and release rates.

**Low Threshold (dB)** - This value, ranging from -100 to -20dB, is the lower threshold of the detector. Any signal coming into the detector below this threshold will not influence the boost calculation; it receives a fixed boost.

**Compression Ratio** - Ranging from 1 to 15, the compression ratio -- perhaps more readily understood as a dynamic-boost ratio -- controls the rate at which the bass boost changes from the low to the high threshold.

**Boost** - This slider, ranging from 0 to 16dB, controls the maximum gain that is dynamically applied to the algorithm. Also see next.

**Bass Freq.** - This field below the boost slider ranges from 20 to 300Hz and designates the center frequency for the boosting filter. Enter your desired value directly into the field or use the two horizontal arrows at the sides of the slider. Note: When the slider is all the way down at 0dB, the block is still not truly bypassed.

.. |DynamicBasspic1.png| image:: https://wiki.analog.com/_media/DynamicBasspic1.png
