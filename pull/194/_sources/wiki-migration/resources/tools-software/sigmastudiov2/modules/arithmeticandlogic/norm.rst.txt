:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Normalize
=========

| 
| |norm.png|

Description
-----------

| 
| The Norm module normalizes the input value with respect to the closest power of 2 (upper side). The output is the normalized out value and the closest power of two or the number of shifts in binary.

Targets Supported
-----------------

==== ========== ================ ============= ================
Name ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
==== ========== ================ ============= ================
Norm NA         NA               S             NA
==== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

===== ===== ===============
Name  Type  Description
===== ===== ===============
Input Audio Input channel 0
===== ===== ===============

Output
~~~~~~

========= ======= ==========================
Name      Type    Description
========= ======= ==========================
Norm Out  Control Normalized output
Num Shift Audio   Number of shifts in binary
========= ======= ==========================

Configurable Parameters
-----------------------

NO DSP parameters

DSP Parameters
--------------

NO DSP parameters

.. |norm.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/norm.png
