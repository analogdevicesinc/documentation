:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Phat-Stereo
===========

| |phatstereo.png|
| ===== Description ===== Phat-Stereo is a spreading algorithm that uses stereo cross-coupling to simulate surround sound in stereo speakers and other 2-channel situations. The ear is most responsive to interaural phase shifts below 2 kHz, so this increase in phase shift results in a widening of the stereo image. A 3D enhancement, it yields an enriched surround field both for headphones and for stereo speakers.
| ===== Targets Supported =====

=========== ========== ================ ============= ================
Name        ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
=========== ========== ================ ============= ================
Phat-Stereo S          S                S             NA
=========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

====== ===== ==============
Name   Type  Description
====== ===== ==============
Input0 Audio Input Channel0
Input1 Audio Input Channel1
====== ===== ==============

Output
------

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output0 Audio Output channel0
Output1 Audio Output channel1
======= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                                                                                |
+====================+===============+================+=====================================================================================================================================+
| Cut Freq (Hz)      | 150           | 20 to 20000 Hz | Controls the cutoff frequency of the first-order low-pass filter. Determines the frequency range of the added out-of-phase signals. |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Level              | -70           | -96 to 6.0 dB  | Controls the output level of the filter                                                                                             |
+--------------------+---------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------------+------------------------+---------------+
| Parameter Name | Description                         | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=====================================+========================+===============+
| AlphaSpread    | Scales the spreading value          | Float                  | 8.24 Format   |
+----------------+-------------------------------------+------------------------+---------------+
| SpreadLevel    | Scales the gain of spreading signal | Float                  | 8.24 Format   |
+----------------+-------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== AlphaSpread = 1.0 - 2.7^(-6.28 \* CutFreq/ fs)
| SpreadLevel = 10^(Level/ 20.0)

.. |phatstereo.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/phatstereo.png
