:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Multitap Gain
=============

| 
| |multitapgain.png|

Description
-----------

| The Multi Tap Gain cell provides a variable gain for each output from one of the selected input channel. Each input signal is called as channel and output is called as Tap.
| ===== Targets Supported =====

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
Multitap Gain NA         NA               S             NA
============= ========== ================ ============= ================

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

.. |multitapgain.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/multitapgain.png
