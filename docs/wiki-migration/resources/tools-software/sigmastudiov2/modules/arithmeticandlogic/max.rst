:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Max
===

| 
| |max.png|

Description
-----------

| The Max block compares the two (or more) inputs and outputs the highest value.

Targets Supported
-----------------

==== ========== ================ ============= ================
Name ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
==== ========== ================ ============= ================
Max  B          B                S/B           B
==== ========== ================ ============= ================

|

| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input channel 0
Input1 Audio Input channel 1
====== ===== ===============

Output
~~~~~~

====== ===== ================
Name   Type  Description
====== ===== ================
MaxOut Audio Output channel 0
====== ===== ================

Configurable Parameters
-----------------------

+--------------------+---------------+-------+-----------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                  |
+====================+===============+=======+=======================================================================+
| NumChannels        | 2             | 20    | Number of input channels,Change in this value requires re-compilation |
+--------------------+---------------+-------+-----------------------------------------------------------------------+

DSP Parameters
--------------

NO DSP parameters

.. |max.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/max.png
