:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Bit Shift
=========

| The Shift block allows you to perform an arithmetic shift operation on the input data.
| |bitshift.png|

Click the image to switch between left shift or right shift. The shift value represents the number of bits to shift the incoming value.

If a shift results in an overflow the data will be saturated to the minimum negative or maximum positive value [-128.0, +127.9999].

Targets Supported
-----------------

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
Bit Shift NA         NA               S             NA
========= ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ===== ============
Name   Type  Description
====== ===== ============
Input0 Audio Input Signal
====== ===== ============

Output
~~~~~~

======= ===== ==================
Name    Type  Description
======= ===== ==================
Output0 Audio Bit shifted output
======= ===== ==================

Configurable Parameters
-----------------------

| No Configurable parameters
| ===== DSP Parameters ===== NO DSP parameters

.. |bitshift.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/bitshift.png
