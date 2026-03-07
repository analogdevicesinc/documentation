:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

NLMS Filter
===========

| 
| |nlmsfilter.png| |fxnlms.png|

Description
-----------

| This implementation of NLMS is a block based implementation. The weight update happens at the end of every processing block.
| ===== Variants =====

-  NLMSFilter
-  FxNLMSFilter

Targets Supported
-----------------

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
NLMSFilter   B          B                S             B
FxNLMSFilter NA         NA               S             NA
============ ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

+----------------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Type    | Description                                                                                                                            |
+================+=========+========================================================================================================================================+
| Input0         | Audio   | Input Channel 0                                                                                                                        |
+----------------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| Desired Signal | Audio   | The desired audio output signal (Applicable for NLMSFilter)                                                                            |
+----------------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| Error Signal   | Audio   | The error signal would be the difference between the desired response and the output of the FxLMS filter.(Applicable for FxNLMSFilter) |
+----------------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| Ref Signal     | Audio   | The Reference input will be the reference to the noise to be cancelled (Applicable for FxNLMSFilter)                                   |
+----------------+---------+----------------------------------------------------------------------------------------------------------------------------------------+
| Adapt On/Off   | Control | Signal which indicates whether FIR filter weights are to be updated or not                                                             |
+----------------+---------+----------------------------------------------------------------------------------------------------------------------------------------+

Output
~~~~~~

+-------------+---------+-------------------------------------------------------------------------------------------------------------+
| Name        | Type    | Description                                                                                                 |
+=============+=========+=============================================================================================================+
| Output0     | Audio   | Filtered output                                                                                             |
+-------------+---------+-------------------------------------------------------------------------------------------------------------+
| ErrorSignal | Control | Error Signal - Difference signal between desired signal and the filtered output (Applicable for NLMSFilter) |
+-------------+---------+-------------------------------------------------------------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-----------+---------------------------------------------+
| GUI Parameter Name | Default Value | Range     | Function Description                        |
+====================+===============+===========+=============================================+
| Alpha              | 0.1           | 0 to 1    | Filter learning rate                        |
+--------------------+---------------+-----------+---------------------------------------------+
| NumberOfTaps       | 256           | 8 to 3200 | Number of Filter Taps                       |
+--------------------+---------------+-----------+---------------------------------------------+
| Leakage            | 0.01          | 0.01 to 1 | Leakage factor is used as forgetting factor |
+--------------------+---------------+-----------+---------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------+------------------------+---------------+
| Parameter Name | Description           | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=======================+========================+===============+
| Alpha          | Filter learning rate  | Float                  | FixPoint8d24  |
+----------------+-----------------------+------------------------+---------------+
| leakage_factor | Filter Leakage factor | NA                     | FixPoint8d24  |
+----------------+-----------------------+------------------------+---------------+

| 

.. |nlmsfilter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/nlmsfilter.png
.. |fxnlms.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/fxnlms.png
