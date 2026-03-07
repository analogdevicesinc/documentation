:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

DSP Readback Generic
====================

| 
| |readgeneric.png|

Description
-----------

The DSP Readback Generic block lets allow you read a specific sample from a block of samples. The drop-down control allows you to enter the which sample be read.

The number displayed onscreen is the data value sent back from the DSP considering all the blocks to the left of the Readback block. Every time you click Read, this value will be updated with the latest from the DSP. By displaying the output value from any block, in any format desired, Readback is used chiefly for debugging, and probably will prove very handy.

| Values can be read back in either hex or decimal. For the latter, you must specify what format you want the number to be displayed in. Any changes to this format will shift the decimal value of the number displayed.
| ===== Targets Supported =====

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| DSPReadbackGeneric | B          | B                | NA            | B                |
+--------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ======= ================
Name    Type    Description
======= ======= ================
Output0 Control Output channel 0
======= ======= ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                 |
+====================+===============+================+======================================================+
| Sample             | 1             | 1 to BlockSize | Sample to read from the target from block of samples |
+--------------------+---------------+----------------+------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ============================ ======================
Parameter Name Description                  ADSP-214xx/SC5xx/215xx
============== ============================ ======================
Sample         reads the sample from target Float
Value          Read back value from the DSP Float
============== ============================ ======================

| 

.. |readgeneric.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/readgeneric.png
