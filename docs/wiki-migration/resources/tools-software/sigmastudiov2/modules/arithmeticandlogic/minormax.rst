:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Min or Max (Block)
==================

| 
| |minormax1.png| |minormax2.png| |minormax3.png|
| ===== Description ===== Min/Max is a Block Processing module which compares the each input samples of one channel with other channels in block of input samples. By default it will check the minimum Algorithm. Option to select Minimum or Maximum Algorithm by clicking on bit map icon.
| ===== Targets Supported =====

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
Min or Max NA         NA               B             NA
========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input channel 0
Input1 Audio Input channel 1
====== ===== ===============

Output
------

====== ===== ================
Name   Type  Description
====== ===== ================
Output Audio Output channel 0
====== ===== ================

Configurable Parameters
~~~~~~~~~~~~~~~~~~~~~~~

+------------------+---------------+--------+----------------------------------------+
| GUI Control Name | Default Value | Range  | Function Description                   |
+==================+===============+========+========================================+
| StateValue       | 0             | 0 - 1  | To select Minimum or Maximum Algorithm |
+------------------+---------------+--------+----------------------------------------+
| NumChannels      | 0             | 2 - 14 | To select Minimum or Maximum Algorithm |
+------------------+---------------+--------+----------------------------------------+

DSP Parameters
~~~~~~~~~~~~~~

NO DSP parameters

.. |minormax1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/minormax1.png
.. |minormax2.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/minormax2.png
.. |minormax3.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/minormax3.png
