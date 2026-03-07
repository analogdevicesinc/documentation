:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Value Hold
==========

| 
| |valueholdnew.png|

Description
-----------

| The ValueHold block holds the incoming input while the control input is zero and allows the incoming input route to output while the control input is other than zero.
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
ValueHold B/S        B/S              S             B
========= ========== ================ ============= ================

Pins
----

Input
~~~~~

+--------------------------+---------+--------------------------------------------+
| Name                     | Type    | Description                                |
+==========================+=========+============================================+
| HoldCondition            | Control | Holds or allows the input signal to output |
+--------------------------+---------+--------------------------------------------+
| Input <fc #ff0000>X</fc> | Audio   | Input channel X                            |
+--------------------------+---------+--------------------------------------------+

Output
~~~~~~

============================ ===== ================
Name                         Type  Description
============================ ===== ================
HeldValue <fc #ff0000>X</fc> Audio Output channel X
============================ ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

+--------------------------------------+---------------+-------+-----------------------------------------------------------------------------------+
| GUI Parameter Name                   | Default Value | Range | Function Description                                                              |
+======================================+===============+=======+===================================================================================+
| NumChannels (Only for ADAU145x/146x) | 1             | 20    | Number of input and output channels. Change in this value requires re-compilation |
+--------------------------------------+---------------+-------+-----------------------------------------------------------------------------------+

.. |valueholdnew.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/valueholdnew.png
