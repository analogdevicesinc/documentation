:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Summation
=========

| 
| |summation.png|

Description
-----------

| The Summation block adds the input to the sum of previous inputs and outputs the result of sum.
| ===== Usage ===== The Reset pin is available to reset the summation result. Other than the zero to reset pin, resets the summation value.
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
Summation B          B                NA            B
========= ========== ================ ============= ================

Pins
----

Input
~~~~~

====== ======= ===========================
Name   Type    Description
====== ======= ===========================
Reset  Control Resets the summation result
Input0 Audio   Input channel 10
====== ======= ===========================

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

Configurable Parameters
-----------------------

+--------------------+---------------+-------+-------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                    |
+====================+===============+=======+=========================================================================+
| NumChannels        | 2             | 20    | Number of in/out channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+-------------------------------------------------------------------------+

DSP Parameters
--------------

No DSP parameters

.. |summation.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/summation.png
