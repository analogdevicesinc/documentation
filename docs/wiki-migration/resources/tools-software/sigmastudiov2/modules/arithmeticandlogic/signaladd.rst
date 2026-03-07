:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Signal Add
==========

| 
| |add.png|

Description
-----------

| The Signal Add block adds the inputs together and no other modification of the signal is done. Care must be taken to avoid clipping.
| ===== Variants =====

-  Signal Add
-  Complex Signal Add
-  Scalar Add

| 
| ===== Targets Supported =====

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| Signal Add         | B/S        | B/S              | S             | B                |
+--------------------+------------+------------------+---------------+------------------+
| Complex Signal Add | NA         | NA               | B             | NA               |
+--------------------+------------+------------------+---------------+------------------+
| Scalar Add         | NA         | NA               | B             | NA               |
+--------------------+------------+------------------+---------------+------------------+

| 

Pins
----

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

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

Configurable Parameters
-----------------------

+--------------------+---------------+-------+----------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                 |
+====================+===============+=======+======================================================================+
| NumChannels        | 2             | 20    | Number of input channels.Change in this value require re-compilation |
+--------------------+---------------+-------+----------------------------------------------------------------------+

DSP Parameters
--------------

NO DSP Parameters

.. |add.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/add.png
