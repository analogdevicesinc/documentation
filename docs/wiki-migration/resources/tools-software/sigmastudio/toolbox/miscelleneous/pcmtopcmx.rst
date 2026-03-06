| :doc:`Click here to return to the miscelleneous page </wiki-migration/resources/tools-software/sigmastudio/toolbox/miscelleneous>`

PCM to PCMx
===========

| 
| PCM to PCMx conversion will have a control signal, which will carry the header information required by the PCMx signal, and 2 Data (PCM) pins, each carrying Linear PCM data, of size Schematic Block Size, as input. The output is PCMx format which will have 3 \* Schematic Block Size no of samples. PCM to PCMx does the reverse of PCMx to PCM module.
| |image1|
| ====Input Pins====

+---------------+------------------------------------+------------------------------------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description                                       |
+===============+====================================+============================================================+
| Pin 0: Input1 | decimal - Control                  | Control signal with header information for the PCMx signal |
+---------------+------------------------------------+------------------------------------------------------------+
| Pin 1: Input2 | decimal - PCM data                 | Linear PCM data of Block size                              |
+---------------+------------------------------------+------------------------------------------------------------+
| Pin 2: Input3 | decimal - PCM data                 | Linear PCM data of Block size                              |
+---------------+------------------------------------+------------------------------------------------------------+

| 
| ====Output Pins====

+---------------+------------------------------------+------------------------------------------------------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description                                                         |
+===============+====================================+==============================================================================+
| Pin 0: Output | decimal- PCMx                      | PCMx input of size 2\* Block Size PCM data and 1\* Block Size of header info |
+---------------+------------------------------------+------------------------------------------------------------------------------+

| 
| ==== Grow Algorithm ==== The module does not support Add. The module supports growth. When grown to a growth count of 'r' the number of samples in each PCM input is given by (2\* block size)/r.
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
| ==== Algorithm Description ==== PCM to PCMx conversion will have a control signal, which will carry the header information required by the PCMx signal, and 2 Data (PCM) pins, each carrying Linear PCM data, of size Schematic Block Size, as input. The output is PCMx format which will have 3 \* Schematic Block Size no of samples.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/miscelleneous/pcm2pcmx-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/miscelleneous/pcm2pcmx-gui.jpg
