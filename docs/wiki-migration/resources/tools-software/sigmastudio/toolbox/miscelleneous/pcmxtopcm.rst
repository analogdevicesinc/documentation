| :doc:`Click here to return to the miscelleneous page </wiki-migration/resources/tools-software/sigmastudio/toolbox/miscelleneous>`

PCMx to PCM
===========

| 
| PCMx to PCM conversion will have PCMx format which will have 3 \* Schematic Block Size number of samples. The output is a control signal, which will carry the header information passed by the PCMx signal, and 2 Data (PCM) pins, each carrying a Schematic Block Size Linear PCM data (since PCMx signal contains Schematic Block Size of header information and 2 \* Schematic Block Size of valid sample information). The output pins can be grown and should be in such a way that the no. of output pins (or the growth count) is always a power of 2. By default the growth count is 2 and the no. of output pins is also 2.
| |image1|
| ====Input Pins====

+--------------+------------------------------------+-----------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description              |
+==============+====================================+===================================+
| Pin 0: Input | decimal- PCMx                      | PCMx input of size 3\* Block Size |
+--------------+------------------------------------+-----------------------------------+

| 
| ====Output Pins====

+----------------+------------------------------------+-----------------------------------------------------------+
| Name           | Format [int/dec] - [control/audio] | Function Description                                      |
+================+====================================+===========================================================+
| Pin 0: Output1 | decimal - Control                  | Control signal with header information of the PCMx signal |
+----------------+------------------------------------+-----------------------------------------------------------+
| Pin 1: Output2 | decimal - PCM data                 | Linear PCM data of Block size                             |
+----------------+------------------------------------+-----------------------------------------------------------+
| Pin 2: Output3 | decimal - PCM data                 | Linear PCM data of Block size                             |
+----------------+------------------------------------+-----------------------------------------------------------+

| 
| ==== Grow Algorithm ==== The module does not support Add. The module supports growth. When grown to a growth count of 'r' the number of samples in each PCM output is given by (2\* block size)/r.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

= = = =
- - - -
= = = =

| 
| ====DSP Parameter Information====

================ ============= ====================
GUI Control Name Compiler Name Function Description
================ ============= ====================
-                -             -
================ ============= ====================

| 
| ==== Algorithm Description ==== PCMx to PCM conversion will have PCMx format which will have 3 \* Schematic Block Size number of samples. The output is a control signal, which will carry the header information passed by the PCMx signal, and 2 Data (PCM) pins, each carrying a Schematic Block Size Linear PCM data (since PCMx signal contains Schematic Block Size of header information and 2 \* Schematic Block Size of valid sample information). The output pins can be grown and should be in such a way that the no. of output pins (or the growth count) is always a power of 2. By default the growth count is 2 and the no. of output pins is also 2.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/miscelleneous/pcmxtopcm-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/miscelleneous/pcmxtopcm-gui.jpg
