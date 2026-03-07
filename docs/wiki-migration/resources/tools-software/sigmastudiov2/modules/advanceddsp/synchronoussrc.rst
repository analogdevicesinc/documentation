:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

Synchronous SRC
===============

| |src.png|
| ===== Description ===== Synchronous SRC is a multi-rate processing module which interpolates or decimates the input signal sampled at the input signal to the desired signal at output sample rate. The module supports fractional (FSin/FSout) ratios. Currently the module supports conversion from 48KHz sample rate to 44.1KHz and vice versa.
| ===== Usage ===== The module acts as an upsampler when the output sample rate is greater than the input sample rate. The module acts as an down sampler when the input sample rate is greater than the output sample rate.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Synchronous SRC | NA         | NA               | S             | NA               |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

====== ===== ==========================
Name   Type  Description
====== ===== ==========================
Input0 Audio Input signal to the module
====== ===== ==========================

Output
------

======= ===== =============================
Name    Type  Description
======= ===== =============================
Output0 Audio Output signal from the module
======= ===== =============================

| 
| ===== Configurable Parameters =====

+---------------+---------------+---------+-----------------------------------------------------------------+---+--------+----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter | Default Value | Range   | Function Description                                            |   | FS Out | 44.1 KHz | 44.1 KHz and 48KHz | Output sampling frequency, this is the sampling frequency at which the input signal at the input sampling frequency is re-sampled to |
+===============+===============+=========+=================================================================+===+========+==========+====================+======================================================================================================================================+
| Memory        | DM0           | DM0/DM1 | Memory selection to which the filter coefficients are loaded to |   |        |          |                    |                                                                                                                                      |
+---------------+---------------+---------+-----------------------------------------------------------------+---+--------+----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ================================= =============
Parameter Name Description                       ADAU145x/146x
============== ================================= =============
FilterCoeffs   Interpolating filter coefficients FixPoint8d24
constants      Constants used in the algorithm   FixPoint8d24
============== ================================= =============

.. |src.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/src.png
