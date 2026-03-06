:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

UP Sampling
===========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/up_down1.png
   :alt: up_down1.png

Description
-----------

The Up sampling module is mainly used to get the input samples to a higher sampling rates after processing the audio at lower sampling rates.For example the bass of the audio can be processed at lower sampling rates and then taken to the higher sampling rates.

| This module takes the upsample factor from the GUI parameters and upsample the input accordingly.
| ===== Targets Supported =====

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
Up-Sampler B          B                S             B
========== ========== ================ ============= ================

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

====== ===== =================
Name   Type  Description
====== ===== =================
Output Audio Up sampled output
====== ===== =================

| 
| ===== Configurable Parameters =====

ADSP-214xx/ADSP-215xx/ADSP-SC5xx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+---------+-------------+---------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default | Range       | Function Description                                                                        |
+====================+=========+=============+=============================================================================================+
| Factor             | 2       | 2,4,8,16,32 | The factor at with the input sample rate will be multiplied                                 |
+--------------------+---------+-------------+---------------------------------------------------------------------------------------------+
| DisableFilter      | False   | True/False  | Enabled/Disabled the filter. If enabled, filter will be applied after upsampling the signal |
+--------------------+---------+-------------+---------------------------------------------------------------------------------------------+

ADAU145x/ADAU146x
~~~~~~~~~~~~~~~~~

+--------------------+----------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default        | Range                          | Function Description                                                                                                                              |
+====================+================+================================+===================================================================================================================================================+
| NumChannels        | 1              | 1-20                           | Number of channels                                                                                                                                |
+--------------------+----------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Factor             | 2              | 2,3,4,6,8,16                   | The factor at with the input sample rate will be multiplied                                                                                       |
+--------------------+----------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| InsertionType      | Zero Insertion | Zero Insertion/Zero Order Hold | The upsampler can either insert zeros or repeat the previous sample(Zero Order Hold) during upsampling. This can be configured in the contex menu |
+--------------------+----------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-------------+----------------------------------------------------------------+------------------------+-------------------+
| Name        | Description                                                    | ADSP-214xx/215xx/SC5xx | ADAU145x/ADAU146x |
+=============+================================================================+========================+===================+
| Factor      | The factor with which the input sample rate will be multiplied | Float                  | FixPoint8d24      |
+-------------+----------------------------------------------------------------+------------------------+-------------------+
| NFilterTaps | Number of antialiasing filter coefficients                     | Float                  | NA                |
+-------------+----------------------------------------------------------------+------------------------+-------------------+
| FIRCoeffs   | coefficients                                                   | Float                  | NA                |
+-------------+----------------------------------------------------------------+------------------------+-------------------+

| 
