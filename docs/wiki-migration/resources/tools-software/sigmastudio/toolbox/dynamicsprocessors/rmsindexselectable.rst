RMS Index Selectable
====================

| :doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| |rms_grow.png|
| |grp.png|
| =====Description===== This block uses an rms dynamics processor that lets you control the rms TC (time constant) and Soft Knee behavior, and opens the compression curve graph for your curve drawing.

RMS works on a longer average than peak processors, thus allowing some fast loud transients to pass without compression, but operating more on longer segments that exceed the threshold.

| This module has stage growth and each stage can have its own compression ratio set using the compressor plot individually. The index selection pin selects the desired stage to be used on the target.
| ===== Targets Supported =====

==================== ========== ================ =============
Name                 ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
==================== ========== ================ =============
RMS Index Selectable NA         Block            NA
==================== ========== ================ =============

| 
| ===== Pins =====

Input
-----

============== ======= =====================
Name           Type    Description
============== ======= =====================
IndexInput     Control Index Selection Input
Input0         Audio   Input channel1
ExtDetectInput Control Ext Detector Input
============== ======= =====================

Output
------

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output0 Audio Output channel1
======= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value               | Range           | Function Description                                                                                                                                                                                                                                                  |
+====================+=============================+=================+=======================================================================================================================================================================================================================================================================+
| Hold_StageX        | 0 ms                        | 0 to 2000 ms    | Controls the time (in ms) the compressor maintains its current output gain setting before it starts decreasing as the input level decrease.                                                                                                                           |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay_StageX       | 10 dB/s                     | 0 to 10000 dB/s | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the “Release” time.                                                                                                                                  |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SoftKnee_StageX    | False                       | True/False      | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. If it is not activated, the default is hard-knee behavior, in which compression rate reduces or increases abruptly with the threshold level |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table              | All values are 1 by default | -               | Table values are the output to input gain level points                                                                                                                                                                                                                |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsDBps_StageX      | True                        | True/False      | Enable /Disable the Control Decay to be either in dB or linear scale                                                                                                                                                                                                  |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1                           | 1 to 15         | Number of input and/or output channels. Change in this value requires re-compilation                                                                                                                                                                                  |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumStages          | 1                           | 1 to 9          | Number of Stages of Compressor. Change in this value requires re-compilation                                                                                                                                                                                          |
+--------------------+-----------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| Note : \_StageX - Refers to parameters of each stage. X represents the stage index.
| ===== DSP Parameters =====

=================== ============= ====================== =============
Parameter Name      Description   ADSP-214xx/SC5xx/215xx ADAU145x/146x
=================== ============= ====================== =============
Hold_StageX         Hold value    Float                  8.24 format
Decay_StageX        Decay value   Float                  8.24 format
Table_StageX        Table values  Float                  8.24 format
TimeConstant_StageX Time Constant Float                  8.24 format
=================== ============= ====================== =============

| 
| Note : \_StageX indicates the dsp parameters associated with a particular stage. X represents the stage index

DSP Parameter Computation
=========================

| Decay = (20000/Decay)/(FS + 0.0000001) (When Decay is in dBps) or Decay/(FS + 0.0000001) (When Decay is in linear) Hold = FS \* Hold/1000
| Where FS is the sampling rate

.. |rms_grow.png| image:: https://wiki.analog.com/_media/rms_grow.png
.. |grp.png| image:: https://wiki.analog.com/_media/grp.png
