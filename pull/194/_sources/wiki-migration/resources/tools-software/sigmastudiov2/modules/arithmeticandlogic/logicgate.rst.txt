:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Logic Gate
==========

| 
| |logicgate.png|

Description
-----------

| The Logic block applies one of five selectable logic operations to the two input signals and outputs the result on the output pin.
| ===== Usage ===== Click on the icon button, each click will toggle the active operator which is shown in the icon image and label.

-  AND
-  NAND
-  OR
-  NOR
-  XOR

| 
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
LogicGate B/S        B/S              S             B
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

.. |logicgate.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/logicgate.png
