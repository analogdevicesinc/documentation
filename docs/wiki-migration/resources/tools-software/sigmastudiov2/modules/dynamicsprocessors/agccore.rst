:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors>`

AGC Core
========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/agccore.png
   :alt: agccore.png

Description
-----------

| This Module is the gain computation part of a compressor. Compression happens by taking the RMS of i/p samples i.e. by passing the input samples through a low-pass filter, converting this to dB scale and then looking up the corresponding gain value. There is a threshold set as a parameter in the Module, below which compression occurs.
| ===== Targets Supported =====

======== ========== ================ ============= ================
Name     ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
======== ========== ================ ============= ================
AGC Core B          B                NA            NA
======== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input channel
===== ===== =============

Output
~~~~~~

====== ======= ===============
Name   Type    Description
====== ======= ===============
Output Control Compressor Gain
====== ======= ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+-----------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                                  |
+====================+===============+==============+=======================================================================+
| Decay              | 20ms          | 20 to 100ms  | Decay coefficient of the compressor                                   |
+--------------------+---------------+--------------+-----------------------------------------------------------------------+
| Attack time        | 20ms          | 20 to 100ms  | Attack coefficient of the compressor                                  |
+--------------------+---------------+--------------+-----------------------------------------------------------------------+
| Ratio              | 1             | 1 to 100     | The ratio is ratio of the gain reduction below the threshold          |
+--------------------+---------------+--------------+-----------------------------------------------------------------------+
| Gain               | 0dB           | -120 to 20dB | The make-up gain of the compressor, in dB                             |
+--------------------+---------------+--------------+-----------------------------------------------------------------------+
| Threshold          | 0dB           | -80 to 20dB  | The compression threshold, in dB, below which compression takes place |
+--------------------+---------------+--------------+-----------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------------------------------+------------------------+
| Parameter Name | Description                                                           | ADSP-214xx/SC5xx/215xx |
+================+=======================================================================+========================+
| DecayCoeff     | Decay coefficient of the compressor                                   | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| SmoothDecay    | Decay smooth coefficient of the compressor                            | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| AttackCoeff    | Attack coefficient of the compressor                                  | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| SmoothAttack   | Attack smooth coefficient of the compressor                           | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| Slope          | The ratio is ratio of the gain reduction below the threshold          | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| Gain           | The make-up gain of the compressor, in dB                             | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| Threshold      | The compression threshold, in dB, below which compression takes place | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+

| 
| ===== DSP Parameter Computation ===== Hold = (int) FS \* Hold/1000
| Decay = 1/10^(Decay \* 2/(10 \* (FS + 0.000001)))
| Where FS is the sampling rate
