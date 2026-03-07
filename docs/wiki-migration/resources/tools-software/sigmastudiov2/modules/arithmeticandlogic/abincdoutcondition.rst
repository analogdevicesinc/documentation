:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

AB-In CD-Out Condition
======================

| 
| |abincdout.png|

Description
-----------

The AB In-CD Out Condition block lets you compare the sample-by-sample level of two incoming signals (A & B) and output the sample of one of two new signals (C & D), depending on the condition.

| This algorithm works only for DSP's with conditional instruction.
| ===== Usage ===== Click the icon in the block to select the condition you want to check:

-  Greater than
-  Less than
-  Greater than or equal to
-  Less than or equal to
-  Equal to

| When the condition is true, output sample is C; otherwise, it's D.
| ===== Targets Supported =====

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
AB-In CD-Out B/S        B/S              S             B
============ ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ===== ================================
Name   Type  Description
====== ===== ================================
Input0 Audio Input channel 0 (Input Signal A)
Input1 Audio Input channel 1 (Input Signal B)
Input2 Audio Input channel 2 (Input Signal C)
Input3 Audio Input channel 3 (Input Signal D)
====== ===== ================================

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

Configurable Parameters
-----------------------

No configurable parameter

DSP Parameters
--------------

NO DSP parameters

.. |abincdout.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/abincdout.png
