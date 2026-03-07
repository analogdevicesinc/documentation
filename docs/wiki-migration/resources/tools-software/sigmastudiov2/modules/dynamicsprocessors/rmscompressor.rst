:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors>`

RMS Compressor
==============

| 
| |rmscomp.png|
| |rmscompgraph.png|

Description
-----------

| The RMS Compressor block computes the RMS level of the input signal and applies the compressor gain to the input signal based on the RMS value.
| ===== Variants =====

-  RMS Compressor
-  RMS Compressor with Gain Out

| 
| ===== Targets Supported =====

+------------------------------+------------+------------------+---------------+------------------+
| Name                         | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==============================+============+==================+===============+==================+
| RMS Compressor               | B/S        | B/S              | S             | B                |
+------------------------------+------------+------------------+---------------+------------------+
| RMS Compressor with Gain Out | NA         | NA               | S             | NA               |
+------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Input1 Audio Input channel1
====== ===== ==============

Output
~~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output1 Audio Output channel1
======= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value    | Range           | Function Description                                                                                                                                                                                                                                                  |
+====================+==================+=================+=======================================================================================================================================================================================================================================================================+
| TimeConstant       | 121              | 1 to 10000 dB/s | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the “Attack” time.                                            |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold               | 0 ms             | 0 to 2000 ms    | Controls the time (in ms) the compressor maintains its current output gain setting before it starts decreasing as the input level decrease.                                                                                                                           |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay              | 10 dB/s          | 0 to 10000 dB/s | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the “Release” time.                                                                                                                                  |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SoftKnee           | False            | True/False      | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. If it is not activated, the default is hard-knee behavior, in which compression rate reduces or increases abruptly with the threshold level |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table              | All values are 1 | -               | Table values are the gain points used to apply for input signal level                                                                                                                                                                                                 |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IsDBps             | True             | True/False      | Enable /Disable the control's Decay and TimeConstant either in dB or linear                                                                                                                                                                                           |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1                | 1 to 20         | Number of input and/or output channels. Change in this value requires re-compilation                                                                                                                                                                                  |
+--------------------+------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------+------------------------+---------------+
| Parameter Name | Description             | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=========================+========================+===============+
| TimeConstant   | RMS time constant value | Float                  | 8.24 format   |
+----------------+-------------------------+------------------------+---------------+
| Hold           | Hold value              | Float                  | 8.24 format   |
+----------------+-------------------------+------------------------+---------------+
| Decay          | Decay value             | Float                  | 8.24 format   |
+----------------+-------------------------+------------------------+---------------+
| Table          | Table values            | Float                  | 8.24 format   |
+----------------+-------------------------+------------------------+---------------+
| LogCoeff       | Constant coefficients   | Float                  | 8.24 format   |
+----------------+-------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== TimeConstant = Abs(1 - 10^(TimeConstant/(10 \* (FS + 0.0000001)))), Where TimeConstant is 20000/TimeConstant in dBps Decay = (20000/Decay)/(FS + 0.0000001) (When Decay is in dBps) or Decay/(FS + 0.0000001) (When Decay is in linear) Hold = FS \* Hold/1000
| Where FS is the sampling rate

.. |rmscomp.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/rmscomp.png
.. |rmscompgraph.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/rmscompgraph.png
   :width: 450px
