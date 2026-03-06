:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`

Peak Full Range(no gain)
========================

| 
| |peakfullrange.png|
| |peakgraph.png|

Description
-----------

| The Peak w/Ext Detector Compressor block computes the peak level of the control signal, if peak of the signal is more than threshold, signal level is changes to new peak level and if the peak level is below the threshold level, it slowly reaches reaches the new peak level by accounting the hold and decay time.
| ===== Variants =====

-  External Detector Input - Peak Full Range(no gain)
-  No External Detector Input - Peak Full Range(no gain)

| 
| ===== Targets Supported =====

+-------------------------------------------------------+------------+------------------+---------------+
| Name                                                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x |
+=======================================================+============+==================+===============+
| External Detector Input - Peak Full Range(no gain)    | B          | B                | NA            |
+-------------------------------------------------------+------------+------------------+---------------+
| No External Detector Input - Peak Full Range(no gain) | B          | B                | S             |
+-------------------------------------------------------+------------+------------------+---------------+

| 
| ===== Pins =====

Input
~~~~~

================ ======= =============================
Name             Type    Description
================ ======= =============================
ExtDetectorInput Control Peak input for the compressor
Input1           Audio   Input channel1
================ ======= =============================

Output
~~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output1 Audio Output channel1
======= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                                                                                                                                                                                                                  |
+====================+===============+================+=======================================================================================================================================================================================================================================================================+
| Hold               | 0 ms          | 0 to 2000 ms   | Controls the time (in ms) the compressor maintains its current output gain setting before it starts decreasing as the input level decrease.                                                                                                                           |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay              | 10 dB/s       | 0 to 8686 dB/s | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the “Release” time.                                                                                                                                  |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SoftKnee           | False         | True/False     | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal. If it is not activated, the default is hard-knee behavior, in which compression rate reduces or increases abruptly with the threshold level |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ============ ====================== =============
Parameter Name Description  ADSP-214xx/SC5xx/215xx ADAU145x/146x
============== ============ ====================== =============
Hold           Hold value   Float                  8.24 format
Decay          Decay value  Float                  8.24 format
Table          Table values Float                  8.24 format
============== ============ ====================== =============

| 
| ===== DSP Parameter Computation ===== Decay = (20000/Decay)/(FS + 0.0000001) (When Decay is in dBps) or Decay/(FS + 0.0000001) (When Decay is in linear) Hold = FS \* Hold/1000
| Where FS is the sampling rate

.. |peakfullrange.png| image:: https://wiki.analog.com/_media/peakfullrange.png
.. |peakgraph.png| image:: https://wiki.analog.com/_media/peakgraph.png
