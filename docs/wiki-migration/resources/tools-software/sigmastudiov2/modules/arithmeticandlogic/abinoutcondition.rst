:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

AB In-Out Condition
===================

| 
| |abinout.png|

Description
-----------

The ABIn-OutCondition block lets you compare the sample-by-sample level of two incoming signals (A & B) and output the sample of the signal meeting the condition.

| This algorithm works only for DSP's with conditional instruction.
| ===== Usage ===== Click the icon in the block to select the condition you want to check:

-  greater than
-  less than
-  greater than or equal to
-  less than or equal to

| When the condition is true, output sample is A; otherwise, it's B.
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
AB In-Out B/S        B/S              S             NA
========= ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ===== ================================
Name   Type  Description
====== ===== ================================
Input0 Audio Input channel 0 (Input Signal A)
Input1 Audio Input channel 1 (Input Signal B)
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

No configurable Parameters

DSP Parameters
--------------

NO DSP parameters

.. |abinout.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/abinout.png
