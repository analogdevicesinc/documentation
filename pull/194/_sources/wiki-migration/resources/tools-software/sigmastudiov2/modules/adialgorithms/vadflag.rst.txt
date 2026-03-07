:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Voice Activity Detector Flag
============================

| |vadflag.png|
| ===== Description ===== VAD Flag takes the Modulation Index and compares it to a threshold value. If the threshold value is met for the designated amount of time, the output flag is set high, otherwise it is low.
| ===== Targets Supported =====

======== ========== ================ ============= ================
Name     ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
======== ========== ================ ============= ================
VAD Flag NA         NA               S             NA
======== ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

=============== ======= ================
Name            Type    Description
=============== ======= ================
ModulationIndex Control Modulation Index
=============== ======= ================

Output
------

+---------------+---------+-------------------------------------------------------+
| Name          | Type    | Description                                           |
+===============+=========+=======================================================+
| ConditionFlag | Control | 0 or 1 output determining if speech is present or not |
+---------------+---------+-------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+---------------+---------------+-----------+---------------------------------------------------------------------+
| GUI Parameter | Default Value | Range     | Function Description                                                |
+===============+===============+===========+=====================================================================+
| Threshold     | -30           | -96 - 24  | dB value for comparison with Modulation Index                       |
+---------------+---------------+-----------+---------------------------------------------------------------------+
| Count         | 250           | 1 - 10000 | Time value in (ms) for condition to be met before setting flag high |
+---------------+---------------+-----------+---------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------+------------------------+---------------+
| Parameter Name | Description                       | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===================================+========================+===============+
| thresh         | Threshold value                   | NA                     | 8.24 Format   |
+----------------+-----------------------------------+------------------------+---------------+
| count          | time before setting the flag high | NA                     | Integer       |
+----------------+-----------------------------------+------------------------+---------------+

.. |vadflag.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/vadflag.png
