:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors>`

RMS Compressor with Max/Avg IP
==============================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/ipmaxavg.png
   :alt: ipmaxavg.png

Description
-----------

| This Module computes the Gain of the Compressor. Compression happens by taking the RMS of the Average or Max of all inputs, and then looking up for the Gain based on the Compressor Graph.
| ===== Targets Supported =====

+-----------------------------+------------+------------------+---------------+------------------+
| Name                        | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=============================+============+==================+===============+==================+
| RMS Compressor with Max/Avg | B          | B                | NA            | NA               |
+-----------------------------+------------+------------------+---------------+------------------+

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

====== ======= ===============
Name   Type    Description
====== ======= ===============
Output Control Compressor Gain
====== ======= ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                                                                                        |
+====================+===============+================+=============================================================================================================================================+
| RMSTC              | 121           | 1 – 10000 db/s | Determines how rapidly the compressor will respond to input signal level changes                                                            |
+--------------------+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Hold               | 0             | 0-2000         | Controls the time (in ms) the compressor maintains its current output gain setting before it starts decreasing as the input level decrease. |
+--------------------+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Decay              | 10            | 1 - 10000 db/s | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level.                                 |
+--------------------+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Soft-knee          | -             | -              | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal.                   |
+--------------------+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Graph              | -             | -              | Compression Editor Graph.                                                                                                                   |
+--------------------+---------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ============================= ======================
Parameter Name Description                   ADSP-214xx/SC5xx/215xx
============== ============================= ======================
RMSTC          RMS Time Constant             Float
Decay          Decay                         Float
Hold           Hold                          Float
Graph          Compressor Graph table values Float Array
============== ============================= ======================

| 
