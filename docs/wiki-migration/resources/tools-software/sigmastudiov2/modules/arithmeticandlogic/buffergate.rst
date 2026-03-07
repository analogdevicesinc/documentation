:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Buffer Gate
===========

| 
| |buffergate.png|

Description
-----------

| The Buffer Gate is a logic block that takes any input and compares the value to 0. If the input signal is zero, the output will be zero. If the input is non-zero, the output will be a “1” in the bit position designated by the drop-down box. This is the opposite output result as the Zero Comparator block. This block is not an audio buffer; this block follows the gate logic of a buffer which acts as a double inversion.

Targets Supported
-----------------

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
BufferGate B/S        B/S              S             B
========== ========== ================ ============= ================

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

+--------------------+---------------+--------+----------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range  | Function Description                                                 |
+====================+===============+========+======================================================================+
| Selected Bit       | Bit:0         | Bit:30 | Sets bit position of Output'1' Flag.                                 |
+--------------------+---------------+--------+----------------------------------------------------------------------+
| NumChannels        | 1             | 20     | Number of input channels.Change in this value requires recompilation |
+--------------------+---------------+--------+----------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+--------------------------------------+------------------------+-------------+
| Parameter Name | Description                          | ADSP-214xx/215xx/SC5xx | ADAU145x/6x |
+================+======================================+========================+=============+
| BufferValue    | Compute & set the bit position value | FixInt32               | FixInt32    |
+----------------+--------------------------------------+------------------------+-------------+

.. |buffergate.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/buffergate.png
