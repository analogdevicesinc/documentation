Up-Sampler
==========

| :doc:`Click here to return to the the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/advanceddsp>`
| The Up-sampler module is mainly used to get the input samples to a higher sampling rates after processing the audio at lower sampling rates.For example the bass of the audio can be processed at lower sampling rates and then taken to the higher sampling rates.

| This module takes the upsample factor from the GUI parameters and upsample the input accordingly.
| |image1|

Input Pins
----------

+--------------+------------------------------------+--------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description           |
+==============+====================================+================================+
| Pin 0: Input | decimal- audio                     | Input Signal to be up-sampled. |
+--------------+------------------------------------+--------------------------------+

| 
| ===== Output Pins =====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - audio                    Upsampled Output
============= ================================== ====================

| 
| ===== Grow Algorithm ===== The module currently does not support grow functionality.
| ===== Add Algorithm ===== Add Algorithm with multiple instance support is available in this module.
| ===== Configurations ===== The upsample factor can be changed by combo box.

+------------------+---------------+-------------+---------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                                                                        |
+==================+===============+=============+=============================================================================================+
| Factor           | 2             | 2,4,8,16,32 | The factor at with the input sample rate will be multipiled                                 |
+------------------+---------------+-------------+---------------------------------------------------------------------------------------------+
| DisableFilter    | False         | True/False  | Enabled/Disabled the filter. If enabled, filter will be applied after upsampling the signal |
+------------------+---------------+-------------+---------------------------------------------------------------------------------------------+

| 
| ===== Supported ICs =====

-  ADSP-SC58x
-  ADSP-215xx

| 
| ===== DSP Parameters =====

+-----------------------------+------------------------------------------------------------------------------------+--------------------------------------+
| Name                        | Description                                                                        | ADSP-214xx/215xx/SC5xx               |
+=============================+====================================================================================+======================================+
| --------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------ |
+-----------------------------+------------------------------------------------------------------------------------+--------------------------------------+
| Factor                      | The factor with which the input sample rate will be multiplied                     | Float                                |
+-----------------------------+------------------------------------------------------------------------------------+--------------------------------------+
| NFilterTaps                 | Number of antialiasing filter coefficients                                         | Float                                |
+-----------------------------+------------------------------------------------------------------------------------+--------------------------------------+
| FIRCoeffs                   | coefficients                                                                       | Float                                |
+-----------------------------+------------------------------------------------------------------------------------+--------------------------------------+

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/advanceddsp/up-sampler.jpg
