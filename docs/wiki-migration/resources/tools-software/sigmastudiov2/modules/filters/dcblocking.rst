:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

DC Blocking
===========

| 
| |dcblocking.png|

Description
-----------

The DC Blocking filter blocks the direct components in the input signal and sends the output signal without DC component.

The dc-blocking behavior is computed according to the following transfer function:

H(z) = (1 - z^-1)/(1 - Rz^-1)

| Note: R = 0.9999 which is a cutoff frequency of 0.1Hz at 48kHz.
| ===== Targets Supported =====

=========== ========== ================ ============= ================
Name        ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
=========== ========== ================ ============= ================
DC Blocking B/S        B/S              S             B
=========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

===== ===== ===============
Name  Type  Description
===== ===== ===============
Input Audio Input Channel 0
===== ===== ===============

Output
~~~~~~

================ ===== ================
Name             Type  Description
================ ===== ================
DCBlocked_Signal Audio Output channel 0
================ ===== ================

| 
| ===== Configurable Parameters ===== No configureable parameters
| ===== DSP Parameters =====

============== =========== =============
Parameter Name Description ADAU145x/146x
============== =========== =============
pole           Filter Pole 8.24
============== =========== =============

| 

.. |dcblocking.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/dcblocking.png
