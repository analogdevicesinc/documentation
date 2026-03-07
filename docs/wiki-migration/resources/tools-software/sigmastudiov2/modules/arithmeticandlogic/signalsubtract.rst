:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Signal Subtract
===============

| 
| |subtract.png|

Description
-----------

| The Signal Subtract block subtracts the input signals(all input signals are subtracted to the first signal) and outputs the difference result.

Variants
--------

-  Signal Subtract
-  Complex Signal Subtract

Targets Supported
-----------------

+-------------------------+------------+------------------+---------------+------------------+
| Name                    | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=========================+============+==================+===============+==================+
| Signal Subtract         | B/S        | B/S              | S             | B                |
+-------------------------+------------+------------------+---------------+------------------+
| Complex Signal Subtract | NA         | NA               | B             | NA               |
+-------------------------+------------+------------------+---------------+------------------+

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

+------------+-------+---------------------------------------------------------------------+
| Name       | Type  | Description                                                         |
+============+=======+=====================================================================+
| Difference | Audio | Result of the difference of first channel and sum of other channels |
+------------+-------+---------------------------------------------------------------------+

Configurable Parameters
-----------------------

+--------------------+---------------+-------+------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                   |
+====================+===============+=======+========================================================================+
| NumChannels        | 2             | 20    | Number of input channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+------------------------------------------------------------------------+

DSP Parameters
--------------

No DSP parameters

.. |subtract.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/subtract.png
