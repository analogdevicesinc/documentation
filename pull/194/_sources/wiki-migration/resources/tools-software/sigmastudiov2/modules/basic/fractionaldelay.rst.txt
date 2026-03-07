:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Fractional Delay
================

| 
| |fractionaldelay.png|

Description
-----------

| The Fractional Delay cell provides a variable delay to a single audio input. The input is delayed by the amount reflected in the percentage text box and allows for fractional delays (fractions of a sample period via linear interpolation). The top drop-down menu labeled Max represents the largest amount of delay that could be applied to the input signal and sets the data delay buffer size.
| ===== Targets Supported =====

+------------------+------------+------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+==================+===============+==================+
| Fractional Delay | NA         | NA               | S             | NA               |
+------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================== ===== ===============
Name                     Type  Description
======================== ===== ===============
Input <fc #ff0000>X</fc> Audio Input Channel X
======================== ===== ===============

| 
| ==== Output ====

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

.. |fractionaldelay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/fractionaldelay.png
