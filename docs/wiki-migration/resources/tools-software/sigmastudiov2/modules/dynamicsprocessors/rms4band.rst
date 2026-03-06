:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors>`

RMS 4 Band Compressor
=====================

| 
| |rms4band.png|
| |rms4bandgraph.png|
| ===== Description ===== The Standard Independent RMS Compressor is a stereo compressor that allows direct control over threshold and ratio. In the pop-up GUI, graphical controls are given for crossover filter settings, compressor curve table settings, threshold, ratio, and time constants. Also there are visual indicators showing input, output, and compression levels. The detection signal used for this RMS compressor is based on the sum of Left and Right channels.
| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| RMS 4 Band Compressor | NA         | NA               | S             | NA               |
+-----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input channel
===== ===== =============

Output
------

====== ===== =================
Name   Type  Description
====== ===== =================
Output Audio Compressor Output
====== ===== =================

| 
| ===== Configurable Parameters =====

+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name            | Default Value | Range      | Function Description                                                                                                                                                                              |
+===============================+===============+============+===================================================================================================================================================================================================+
| Low/Mid1/Mid2/High FilterType | 0             | 0-9        | Type of the filter selected for respective crossover curves                                                                                                                                       |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pre-Gain                      | 0             | -90 to 6   | Controls the ratio of Compression. The number selected in this box is interpreted as the ratio N:1 for compression above the threshold point.                                                     |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Corner Frequency              | 0             | 0-96000    | Respective corner frequencies of the crossover filter curves                                                                                                                                      |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Knee                          | 1             | 1 - 75     | Controls the hard/soft knee relationship of the curve. A knee allows a more gradual calculation of the curve around the threshold point, with "1" being a hard knee, and "100" being the softest. |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LinkGain                      | False         | True/False | Allows the gains of selected filters to be linked                                                                                                                                                 |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack (ms)                   | 72            | 1- 500     | Controls the amount of time before the compressor reacts to an input signal that has exceeded the threshold point.                                                                                |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)                     | 72            | 0 - Attack | Controls the amount of time the compression level is held before reacting to a new change in input signal level. The max hold time is limited to the Attack time setting.                         |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release (ms)                  | 868           | 1.0-2000   | Controls the amount of time before the compressor reacts to an input signal that has dropped below the threshold point.                                                                           |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsLevelIndicatorsEnabled      | off           | on/off     | Turns the Indicators on or off. There is no DSP function associated with this.                                                                                                                    |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels                   | 1             | 1 to 8     | Number of input and/or output channels. Change in this value requires re-compilation                                                                                                              |
+-------------------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Parameter Name | Description                                                                                                                                                     | ADAU145x/146x |
+================+=================================================================================================================================================================+===============+
| points         | When the Threshold, Compressor, Expander, or Knee values are changed, 34 parameters are written to the DSP to represent the gain curve displayed in the window. | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| attenuation    | When the Input Gain is changed, the dB value is converted to linear and written to the DSP.                                                                     | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| tc             | When the Attack time is changed, a new value is calculated and written to the DSP to control the reaction time.                                                 | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| hold           | When the Hold time is changed, a new value is calculated and written tot he DSP to control the hold time.                                                       | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| decay          | When the Decay time is changed, a new value is calculated and written to the DSP to control the reaction time.                                                  | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+

| 

.. |rms4band.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/rms4band.png
.. |rms4bandgraph.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/rms4bandgraph.png
