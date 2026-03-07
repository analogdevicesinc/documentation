SuperBass
=========

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
| The Superbass block is a bass enhancement algorithm specifically designed to compensate for the poor low end response of small speakers by using psychoacoustic principles to improve the perceived bass response. | |superbass1.png| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+

The inputs and outputs are stereo

SB On/Off: Activates or bypasses the algorithm

Xover Freq: Sets the frequency below which signals are considered to be in the "bass" range. These signals will be used for the bass enhancement algorithm. Higher harmonics of these signals will be generated above the crossover frequency, giving the impression of increased bass. Can be set from 20 Hz to 500 Hz.

Intensity: This controls how much gain is applied to the artificially generated higher harmonics (above the crossover frequency). This parameter can be set from 0.1 to 3.0. This value is a linear multiplier (not expressed in dB).

Bass Gain: This allows you to additionally apply a gain directly to the signal below the crossover frequency. Can be set from 0.1 to 3.0. This value is a linear multiplier (not expressed in dB).

http://ez.analog.com/thread/10891

Supported ICs
-------------

-  ADAU145x
-  ADSP214xx
-  ADSP213xx
-  ADSPSC58x

.. |superbass1.png| image:: https://wiki.analog.com/_media/superbass1.png
