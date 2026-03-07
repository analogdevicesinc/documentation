:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Standard Hard Clipper
=====================

| 
| |standardclip.png|

Description
-----------

This block clips off portions of signal voltages above and/or below certain limits. In other words, the circuit limits the range of the output signal.

Usage
-----

| Click the icon to switch among the clipper options: Hi, Low, or both. Enter upper and lower limits in their text fields. This algorithm can be grown to support multiple input/output pairs for multi-channel audio.
| ===== Targets Supported =====

+-------------------------+------------+------------------+---------------+------------------+
| Name                    | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=========================+============+==================+===============+==================+
| Hard Clipper - Standard | NA         | NA               | S             | NA               |
+-------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input channel X
======================= ===== ===============

Output
~~~~~~

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range              | Function Description                                                              |
+====================+===============+====================+===================================================================================+
| ClipType           | Both          | High, Low, Both    | Signal clipping options                                                           |
+--------------------+---------------+--------------------+-----------------------------------------------------------------------------------+
| Hi                 | 1             | LowerLimit to 100  | Sets the upper limit                                                              |
+--------------------+---------------+--------------------+-----------------------------------------------------------------------------------+
| Low                | -1            | -16 to HigherLimit | Sets the lower limit                                                              |
+--------------------+---------------+--------------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 20            | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+--------------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== =========== ====================== ==============
Parameter Name Description ADSP-214xx/SC5xx/215xx ADAU145x/146x
============== =========== ====================== ==============
up             Upper Limit NA                     FixedPoint8d24
down           Lower Limit NA                     FixedPoint8d24
============== =========== ====================== ==============

.. |standardclip.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/standardclip.png
