:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Absolute Max Value Hold
=======================

| 
| |absmaxholdnew.png|

Description
-----------

| The AbsMaxValueHold block monitors one (or more) input(s) and routes the absolute max value of the input to the output. This block holds the absolute max value while the control input is 0 and reset the absolute max value while the control input is 1. Note - In case of ADSP-214xx and ADSP-215xx/SC5xx, there will be per channel max hold and not max hold across channels.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| AbsMaxValueHold | B/S        | B/S              | S             | B                |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================= ======= =================================
Name                    Type    Description
======================= ======= =================================
Reset                   Control Resets the absolute maximum value
Input<fc #ff0000>X</fc> Audio   Input channel X
======================= ======= =================================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

Configurable Parameters
-----------------------

+--------------------+---------------+-------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                              |
+====================+===============+=======+===================================================================================+
| NumChannels        | 1             | 20    | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+-----------------------------------------------------------------------------------+

.. |absmaxholdnew.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/absmaxholdnew.png
