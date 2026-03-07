:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Min Value Hold
==============

| 
| |minholdnew.png|

Description
-----------

| The MinValueHold block monitors one (or more) input(s) and routes the minimum value of the input to the output. This block hold's the min value while the control input is 1 and reset the min value while the control input is 0.
| ===== Targets Supported =====

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
MinValueHold B/S        B/S              B/S           B
============ ========== ================ ============= ================

Pins
----

Input
~~~~~

======================= ======= ========================
Name                    Type    Description
======================= ======= ========================
Reset                   Control Resets the minimum value
Input<fc #ff0000>X</fc> Audio   Input channel X
======================= ======= ========================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                              |
+====================+===============+=======+===================================================================================+
| NumChannels        | 1             | 20    | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+-----------------------------------------------------------------------------------+

| 

.. |minholdnew.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/minholdnew.png
