:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Dynamic Enhancement
===================

Dynamic Enhancement Mono
------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/dbe.png
   :alt: dbe.png

Dynamic Enhancement Stereo
--------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/dbestereo.png
   :alt: dbestereo.png

Description
~~~~~~~~~~~

| 
| The Dynamic Enhancement block provides variable bass enhancement as a function of input-signal level. Lower levels require more bass than higher levels. The filter dynamically adjusts the amount of bass enhancement depending on the volume of the input signal, by using a variable-Q filter.

| A fixed enhancement is applied to input levels below the threshold while a dynamic gain is applied to input levels above the threshold.
| ===== Variants =====

-  Dynamic Enhancement (Mono)
-  Dynamic Enhancement (Stereo)

| 

Targets Supported
~~~~~~~~~~~~~~~~~

+------------------------------+------------+------------------+---------------+------------------+
| Name                         | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==============================+============+==================+===============+==================+
| Dynamic Enhancement (Mono)   | B/S        | B/S              | NA            | B                |
+------------------------------+------------+------------------+---------------+------------------+
| Dynamic Enhancement (Stereo) | B/S        | B/S              | NA            | B                |
+------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
^^^^^

====== ===== ================================
Name   Type  Description
====== ===== ================================
Input0 Audio Input channel0
Input1 Audio Input Channel1 (only for stereo)
====== ===== ================================

Output
^^^^^^

======= ===== =================================
Name    Type  Description
======= ===== =================================
Output0 Audio Output channel0
Output1 Audio Output channel1 (only for stereo)
======= ===== =================================

Configurable Parameters
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+---------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                                                                                                                               |
+====================+===============+==============+====================================================================================================================================================================+
| TimeConstant       | 100 ms        | 0 to 500ms   | This controls the RMS time constant for the detector. Changing the attack and release rates                                                                        |
+--------------------+---------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CompThreshold      | -5 db         | -24 to 20 dB | Threshold of the detector.Any signal coming into the detector below the threshold level will not influence the boost calculation. it receives a fixed enhancement. |
+--------------------+---------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CompressorRatio    | 3             | 1 to 15      | It is dynamic boost ratio.Controls the rate at which the bass boost changes from the low to the high threshold.                                                    |
+--------------------+---------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BoostFrequency     | 6 Hz          | 0 to 16 Hz   | Controls the maximum dynamic enhancement gain applied to the algorithm.                                                                                            |
+--------------------+---------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BassFrequency      | 60 hz         | 20 to 300 Hz | Cut off frequency for the boosting filter.                                                                                                                         |
+--------------------+---------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
~~~~~~~~~~~~~~

+----------------+---------------------------------------------------------------------+------------------------+
| Parameter Name | Description                                                         | ADSP-214xx/SC5xx/215xx |
+================+=====================================================================+========================+
| CompThreshold  | Threshold of the detector                                           | Float                  |
+----------------+---------------------------------------------------------------------+------------------------+
| TimeConstant   | Rms time constant for the detector for change in input signal level | Float                  |
+----------------+---------------------------------------------------------------------+------------------------+
| BoostFrequency | maximum dynamic enhancement gain applied to the algorithm           | Float                  |
+----------------+---------------------------------------------------------------------+------------------------+
| BassFrequency  | Cut off frequency for the boosting filter                           | Float                  |
+----------------+---------------------------------------------------------------------+------------------------+
