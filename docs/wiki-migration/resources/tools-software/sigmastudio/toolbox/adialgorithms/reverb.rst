Reverb
======

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| |reverbpic1.png| The Reverb algorithm simulates the natural reverberation of an echoic space, such as a performance hall, and mixes it back into the original signal. Technically, reverberation is the total soundfield remaining in an enclosed space after initial sources are not active.

This block lets you control the following three parameters:

**Reverb Time** - These radio buttons let you control the Reverb Time settings, short to long. The Reverb time is the amount of time it takes for the reverberations to decay. (Technically this is specified by measuring how long it takes the signal SPL [sound-pressure level] to decay 60dB, to one-millionth its original value.)

**HF Damping** - These radio buttons let you control the HF Damping settings, bright to dim. HF damping refers to the brightness of the reverb reflections.

**Bass Reverb Gain** - These radio buttons let you control the Bass Reverb Gain settings, high to low. Bass reverb refers to the level and richness of the LF reflections.

After the default algorithm has been established, this block is able to have other algorithms :doc:`added </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` to it. Right-click the block and select **Add Algorithm > IC N > Reverb**, which will add another pair of stereo inputs/outputs.

.. |reverbpic1.png| image:: https://wiki.analog.com/_media/reverbpic1.png
