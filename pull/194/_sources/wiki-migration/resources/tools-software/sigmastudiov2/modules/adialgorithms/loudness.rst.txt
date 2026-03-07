:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Loudness
========

|loudness1.png| |loudness2.png| |loudness3.png|

Description
-----------

| **Loudness Low High**: For low levels, the Loudness (Low and High) block raises bass <60 Hz and also the treble >7kHz.
| **Loudness (Low and High) External Control**: Unlike the Loundess (Low and High) block, the loudness level parameter of the Loudness (Low and High) External Control block is controlled by an external signal instead of a volume slider.
| **Loudness (Lower End)**: The Loudness (Lower End) algorithm raises the amplitude of bass frequencies for low volume levels.

| In all the 3 variants, the boost values are derived from the well-known equal-loudness curves of Fletcher and Munson and others. This research revealed that at low levels, lows and highs need to be considerably louder in order for the tonal balance to sound correctly proportioned and the overall sound to have the same apparent loudness to the human ear. This algorithm is fixed, not dynamic: it assumes that the input level is constant.
| ===== Variants =====

-  Loudness Low High
-  Loudness Low High (Control I/P)
-  Loudness Lower End

| 
| ===== Targets Supported =====

+---------------------------------+------------+------------------+---------------+------------------+
| Name                            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================================+============+==================+===============+==================+
| Loudness Low High               | S/B        | S/B              | S             | B                |
+---------------------------------+------------+------------------+---------------+------------------+
| Loudness Low High (Control I/P) | B          | B                | S             | B                |
+---------------------------------+------------+------------------+---------------+------------------+
| Loudness Lower End              | B          | B                | NA            | B                |
+---------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+--------+---------+--------------------------------------------------------------------------------------------------------------------------+
| Name   | Type    | Description                                                                                                              |
+========+=========+==========================================================================================================================+
| Inputx | Audio   | Input channel                                                                                                            |
+--------+---------+--------------------------------------------------------------------------------------------------------------------------+
| Volume | Control | The external control pin used to set the loudness volume parameter for the algorithm for Loudness Low High (Control I/P) |
+--------+---------+--------------------------------------------------------------------------------------------------------------------------+

Output
~~~~~~

======= ===== ==============
Name    Type  Description
======= ===== ==============
Outputx Audio Output channel
======= ===== ==============

| 
| ===== Configurable Parameters =====

+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter            | Default Value | Range         | Function Description                                                                                                                                                                                                                                                                                     |
+==========================+===============+===============+==========================================================================================================================================================================================================================================================================================================+
| FilterType               | true          | true or false | Allows selection between General first order filter and Butter worth first order filter                                                                                                                                                                                                                  |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume                   | 0             | -50 - 0dB     | The output volume of the entire signal, but, more important, it is also the control for the loudness algorithm. At low levels, the loudness algorithm boosts the low frequencies somewhat more than it does the high frequencies. At 0dB, no matter what the input level is, there is no boost, LF or HF |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LowLevel/Level           | 36            | 0 - 100       | Controls the relative amount of low frequency boost that is applied                                                                                                                                                                                                                                      |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HighLevel                | 0             | 0 - 100       | Controls the relative amount of high frequency boost that is applied                                                                                                                                                                                                                                     |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LowFrequency/LPFrequency | 10            | 0 - 60        | The cutoff of the lowpass filter. The default value approximates the Fletcher-Munson curve. Higher-frequency values provide greater bass-bandwidth gain                                                                                                                                                  |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HighFrequency            | 14000         | 7000 - 96000  | The cutoff frequency of the highpass filter. The default value of 7kHz approximates the Fletcher-Munson curve                                                                                                                                                                                            |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Step                     | 12            | 1 - 23        | External volume parameter's slew rate (controls how quickly the algorithm responds to changes in the control signal)                                                                                                                                                                                     |
+--------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== =================== =================
Parameter Name Description         ADAU145x/146x
============== =================== =================
Volume         Output volume       8.24 Format
LevelLow/Level Low frequency boost 8.24 Format Array
IIRCoeff_HP_B0 Filter coefficient  8.24 Format
IIRCoeff_HP_B1 Filter coefficient  8.24 Format
IIRCoeff_HP_A1 Filter coefficient  8.24 Format
IIRCoeff_LP_B0 Filter coefficient  8.24 Format
IIRCoeff_LP_B1 Filter coefficient  8.24 Format
IIRCoeff_LP_A1 Filter coefficient  8.24 Format
Step           Slew step size      8.24 Format
IIRCoeff_b0    Filter coefficient  8.24 Format
IIRCoeff_a1    Filter coefficient  8.24 Format
============== =================== =================

.. |loudness1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/loudness1.png
.. |loudness2.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/loudness2.png
.. |loudness3.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/loudness3.png
