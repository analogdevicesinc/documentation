:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

RMS With TC
===========

| 
| |rmswtc.png|

Description
-----------

| The RMSWithTC block computes the RMS of the input signals with time constant specified in the text field.
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
RMSWithTC S/B        S/B              NA            B
========= ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ===== ================
Name   Type  Description
====== ===== ================
Input0 Audio Input channel 10
====== ===== ================

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

Configurable Parameters
-----------------------

+--------------------+---------------+------------+-------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description                                                                      |
+====================+===============+============+===========================================================================================+
| TimeConstant       | 121           | 1-8686     | Determines how rapidly the RMS value is to be computed with any change in the input level |
+--------------------+---------------+------------+-------------------------------------------------------------------------------------------+
| IsDBps             | False         | True/False | Control value in dB/s or ms                                                               |
+--------------------+---------------+------------+-------------------------------------------------------------------------------------------+
| NumChannels        | 2             | 20         | Number of input and Output channels. Change in this value requires re-compilation         |
+--------------------+---------------+------------+-------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+---------------------------------------+------------------------+
| Parameter Name | Description                           | ADSP-214xx/215xx/SC5xx |
+================+=======================================+========================+
| TimeConstant   | TC for RMS value with change in input | Float                  |
+----------------+---------------------------------------+------------------------+

DSP Parameter Computation
-------------------------

TimeConstant = ABS(1-10^(TimeConstant(linear)/(10\*FS))) Where FS is the Sampling rate

.. |rmswtc.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/rmswtc.png
