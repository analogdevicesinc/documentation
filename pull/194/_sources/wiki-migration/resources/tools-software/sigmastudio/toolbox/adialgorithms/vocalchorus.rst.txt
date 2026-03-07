Vocal Chorus
============

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| |vocalpic1.png| Vocal Chorus produces an effect where the audio signal is given multiple delays to enrich and thicken the sound, like several voices (or instruments) playing at once. The delay time is modulated by a low-frequency oscillator (LFO) to achieve a shimmering, spacious effect due to a combination of beat frequencies and the slight pitch-bending that occurs as the delay time is changed.

This cell is intended chiefly for voice.

-  The Feedback settings, light to heavy, determine how much of the delayed signal to mix back in with the original, undelayed signal.
-  The LFO settings, slow to fast, determine the delay times that the LFO modulates to achieve the "chorus" effect.

After the default algorithm has been established, this cell is able to have other algorithms :doc:`added </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` to it. Right-click the cell and select **Add Algorithm > IC N > Reverb**, which will add another pair of stereo inputs/outputs. (If you are using more than one DSP processor, you will need to add an algorithm for the desired IC.)

.. |vocalpic1.png| image:: https://wiki.analog.com/_media/vocalpic1.png
