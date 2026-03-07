:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

External SPI Delay
==================

| 
| |extspidelay.png|

Description
-----------

| The External SPI Delay cell can be used to implement off-chip delay using the SPI interface.
| ===== Targets Supported =====

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| External SPI Delay | NA         | NA               | S             | NA               |
+--------------------+------------+------------------+---------------+------------------+

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

.. |extspidelay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/extspidelay.png
