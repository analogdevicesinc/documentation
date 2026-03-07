:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Super Bass
==========

Super Bass Mono
---------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/superbassmono.png
   :alt: superbassmono.png

Super Bass Stereo
-----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/superbassstereo.png
   :alt: superbassstereo.png

Description
~~~~~~~~~~~

| 
| The Super Bass block is a bass enhancement algorithm specifically designed to compensate for the poor low end response of small speakers by using psychoacoustic principles to improve the perceived bass response.
| ===== Variants =====

-  Super Bass (Mono)
-  Super Bass (Stereo)

| 
| ===== Targets Supported =====

+---------------------+------------+------------------+---------------+------------------+
| Name                | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=====================+============+==================+===============+==================+
| Super Bass (Mono)   | B          | B                | S             | NA               |
+---------------------+------------+------------------+---------------+------------------+
| Super Bass (Stereo) | B          | B                | S             | NA               |
+---------------------+------------+------------------+---------------+------------------+

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

+--------------------+---------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                                                                                                                                                                                                                                |
+====================+===============+==============+=====================================================================================================================================================================================================================================================================+
| Intensity          | 1.3           | 0.1 to 3     | Controls how much gain is applied to the artificially generated higher harmonics(Above cross over frequency).                                                                                                                                                       |
+--------------------+---------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BassGain           | 1.2           | 0.1 to 3     | Controls the gain applied to the input signal below the cross over frequency                                                                                                                                                                                        |
+--------------------+---------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| XOverFrequency     | 90 Hz         | 20 to 500 Hz | The signals below this frequency are considered to be in the bass range. These signals will be used for the bass enhancement algorithm. Higher harmonics of these signals will be generated above the crossover frequency, giving the impression of increased bass. |
+--------------------+---------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bypass_ON          | True          | True/False   | Activates or Bypasses the algorithm                                                                                                                                                                                                                                 |
+--------------------+---------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
~~~~~~~~~~~~~~

+----------------+-----------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                             | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=========================================================================================+========================+===============+
| RMS            | RMS time constant for the detector to respond to the change in input signal level       | Float                  | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------+------------------------+---------------+
| BassGain       | Gain applied to the input signal below the cross over frequency                         | Float                  | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------+------------------------+---------------+
| Intensity      | Gain applied to the artificially generated higher harmonics(Above cross over frequency) | Flaot                  | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------+------------------------+---------------+
| Bypass_ON      | Enabled/Disabled the algorithm                                                          | Float                  | 8.24 Format   |
+----------------+-----------------------------------------------------------------------------------------+------------------------+---------------+
