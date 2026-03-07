:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

Down Sampling
=============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/downsampler.png
   :alt: downsampler.png

Description
-----------

The Down Sampling module is mainly used to get the input samples to a lower the process and sampling rate. For example the bass portion of the audio need not to be processed at higher sampling rates as the frequencies associated with bass are low.

| This module takes the DownSample factor from the GUI parameters and down-samples the input accordingly.
| ===== Targets Supported =====

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
Down-Sampler B          B                S             B
============ ========== ================ ============= ================

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

====== ===== ===================
Name   Type  Description
====== ===== ===================
Output Audio Down sampled output
====== ===== ===================

| 
| ===== Configurable Parameters =====

ADSP-214xx/ADSP-215xx/ADSP-SC5xx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+---------+-------------+----------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default | Range       | Function Description                                                                                                 |
+====================+=========+=============+======================================================================================================================+
| Factor             | 2       | 2,4,8,16,32 | The input sample rate will be divided by Factor                                                                      |
+--------------------+---------+-------------+----------------------------------------------------------------------------------------------------------------------+
| AntiAliasFilter    | False   | True/False  | Enabled/Disabled the anti-alias filter. If enabled, anti-alias filter will be applied before DownSampling the signal |
+--------------------+---------+-------------+----------------------------------------------------------------------------------------------------------------------+

| 
| ==== ADAU145x/ADAU146x ====

+--------------------+---------+--------------+----------------------------------------------------------+
| GUI Parameter Name | Default | Range        | Function Description                                     |
+====================+=========+==============+==========================================================+
| NumChannels        | 1       | 1-20         | Number of channels                                       |
+--------------------+---------+--------------+----------------------------------------------------------+
| Factor             | 2       | 2,3,4,6,8,16 | The factor at with the input sample rate will be divided |
+--------------------+---------+--------------+----------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-------------+----------------------------------------------------------+------------------------+-------------------+
| Name        | Description                                              | ADSP-214xx/215xx/SC5xx | ADAU145x/ADAU146x |
+=============+==========================================================+========================+===================+
| Factor      | The factor at with the input sample rate will be divided | Float                  | FixedPoint8d24    |
+-------------+----------------------------------------------------------+------------------------+-------------------+
| NFilterTaps | Number of antialiasing filter coefficients               | Float                  | NA                |
+-------------+----------------------------------------------------------+------------------------+-------------------+
| FIRCoeffs   | coefficients                                             | Float                  | NA                |
+-------------+----------------------------------------------------------+------------------------+-------------------+

| 
