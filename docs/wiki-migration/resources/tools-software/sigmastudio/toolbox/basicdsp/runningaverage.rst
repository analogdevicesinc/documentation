Running Average
===============

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| |run_avg.png|

Description
-----------

| The RunningAverage block computes the average of N samples. Where N is specified in the CurrentBlockSize text field.
| ===== Targets Supported =====

=========== ========== ================ =============
Name        ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
=========== ========== ================ =============
Running Avg Block      Block            NA
=========== ========== ================ =============

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

Configurable Parameters
-----------------------

+--------------------+---------------+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                                             | Function Description                                                                        |
+====================+===============+===================================================+=============================================================================================+
| MaxBlockSizeSet    | 1             | 1 -1500 (Depends on the size of memory available) | Specifies the maximum samples for averaging. Change in this value requires a re-compilation |
+--------------------+---------------+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| CurrentBlockSize   | 1             | 1 - MaxBlockSizeSet                               | Number of samples to be averaged. Change in this value requires a re-compilation            |
+--------------------+---------------+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 15                                                | Number of input and output channels.Change in this value requires a re-compilation          |
+--------------------+---------------+---------------------------------------------------+---------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+---------------------+---------------------------------------------+------------------------+
| Parameter Name      | Description                                 | ADSP-214xx/SC5xx/215xx |
+=====================+=============================================+========================+
| MaxBlockSizeSet     | Specifies the maximum samples for averaging | Float                  |
+---------------------+---------------------------------------------+------------------------+
| MaxCurrentBlockSize | Number of samples to be averaged            | Float                  |
+---------------------+---------------------------------------------+------------------------+
| OneOverN            | Inverse of CurrentBlockSize                 | Float                  |
+---------------------+---------------------------------------------+------------------------+

DSP Parameter Computation
-------------------------

NA

.. |run_avg.png| image:: https://wiki.analog.com/_media/run_avg.png
