:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Dynamic Bass Boost
==================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/dynamicbassboostmono.png
   :alt: dynamicbassboostmono.png

Description
-----------

| 
| The Dynamic Bass Boost block provides a boost that varies with input signal level. A lower level of signals requires and receives more bass than a higher level of signals. By using a variable Q filter this block dynamically adjusts the amount of boost required for an input signal.

| The filter calculates its bass boost between the Threshold and minimum Gain settings. A fixed maximum bass is applied to inputs above the minimum gain and below the Threshold level.
| ===== Variants =====

-  Dynamic Bass Boost Mono
-  Dynamic Bass Boost Stereo

| 
| ===== Targets Supported =====

+---------------------------+------------------+------------------+---------------+------------------+
| Name                      | ADSP-214xx       | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===========================+==================+==================+===============+==================+
| Dynamic Bass Boost Mono   | Block and Sample | Block and Sample | Sample        | Block            |
+---------------------------+------------------+------------------+---------------+------------------+
| Dynamic Bass Boost Stereo | Block and Sample | Block and Sample | NA            | Block            |
+---------------------------+------------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ================================
Name   Type  Description
====== ===== ================================
Input0 Audio Input channel0
Input1 Audio Input Channel1 (only for stereo)
====== ===== ================================

Output
~~~~~~

======= ===== =================================
Name    Type  Description
======= ===== =================================
Output0 Audio Output channel0
Output1 Audio Output channel1 (only for stereo)
======= ===== =================================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                                                                                                              |
+====================+===============+================+===================================================================================================================================================================+
| LowPassFrequency   | 250 Hz        | 20 to 250 Hz   | Frequencies below the LowPassFrequency settings are used by the detector to determine the boost amount                                                            |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HighThreshold      | -5 dB         | -45 to 10 dB   | Higher Threshold of the detector.Any signal coming into the detector above the threshold level wil not influence the boost calculation. it recieves a fixed boost |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TimeConstant       | 100 ms        | 0 to 500ms     | This controls the rms time constant for the detector. Changing the attack and release rates                                                                       |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LowThreshold       | -25 db        | -100 to -20 dB | Lower Threshold of the detector.Any signal coming into the detector below the threshold level wil not influence the boost calculation. it recieves a fixed boost  |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CompressorRatio    | 3             | 1 to 15        | It is dynamic boost ratio.Controls the rate at which the bass boost changes from the low to the high threshold                                                    |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BoostFrequency     | 6 Hz          | 0 to 16 Hz     | Controls the maximum gain applied to the algorithm                                                                                                                |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BassFrequency      | 60 hz         | 20 to 300 Hz   | Cut off frequency for the boosting filter                                                                                                                         |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+---------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                         | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=====================================================================+========================+===============+
| TimeConstant   | Rms time constant for the detector for change in input signal level | Float                  | 8.24 Format   |
+----------------+---------------------------------------------------------------------+------------------------+---------------+
| BassFrequency  | Cut off frequency for the boosting filter                           | Float                  | 8.24 Format   |
+----------------+---------------------------------------------------------------------+------------------------+---------------+
