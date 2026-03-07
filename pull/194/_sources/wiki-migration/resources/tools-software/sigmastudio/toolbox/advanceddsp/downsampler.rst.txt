Down-Sampler
============

| :doc:`Click here to return to the the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/advanceddsp>`
| The down-sampler module is mainly used to get the input samples to a lower sampling rate and process. For example the bass portion of the audio need not be processed at higher sampling rates as the frequencies associated with bass are low.

| This module takes the downsample factor from the GUI parameters and down sample the input accordingly.
| |image1|

Input Pins
----------

+--------------+------------------------------------+----------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description             |
+==============+====================================+==================================+
| Pin 0: Input | decimal- audio                     | Input Signal to be down-sampled. |
+--------------+------------------------------------+----------------------------------+

| 
| ===== Output Pins =====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - audio                    Downsampled Output
============= ================================== ====================

| 
| ===== Grow Algorithm ===== The module currently does not support grow functionality.
| ===== Add Algorithm ===== Add Algorithm with multiple instance support is available in this module.
| ===== Configurations ===== The downsample factor can be changed by combo box.

+------------------+---------------+-------------+----------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                                                                                                 |
+==================+===============+=============+======================================================================================================================+
| Factor           | 2             | 2,4,8,16,32 | The factor at with the input sample rate will be divided                                                             |
+------------------+---------------+-------------+----------------------------------------------------------------------------------------------------------------------+
| AntiAliasFilter  | False         | True/False  | Enabled/Disabled the anti-alias filter. If enabled, anti-alias filter will be applied before DownSampling the signal |
+------------------+---------------+-------------+----------------------------------------------------------------------------------------------------------------------+

| 
| ===== Supported ICs =====

-  ADSP-SC58x
-  ADSP-215xx

| 
| ===== DSP Parameters =====

+-----------------------------+------------------------------------------------------------------------------------+------------------------------------------+
| Name                        | Description                                                                        | ADSP-214xx/215xx/SC5xx                   |
+=============================+====================================================================================+==========================================+
| --------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------- |
+-----------------------------+------------------------------------------------------------------------------------+------------------------------------------+
| Factor                      | The factor at with the input sample rate will be divided                           | Float                                    |
+-----------------------------+------------------------------------------------------------------------------------+------------------------------------------+
| NFilterTaps                 | Number of antialiasing filter coefficients                                         | Float                                    |
+-----------------------------+------------------------------------------------------------------------------------+------------------------------------------+
| FIRCoeffs                   | coefficients                                                                       | Float                                    |
+-----------------------------+------------------------------------------------------------------------------------+------------------------------------------+

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/advanceddsp/downsampler.jpg
