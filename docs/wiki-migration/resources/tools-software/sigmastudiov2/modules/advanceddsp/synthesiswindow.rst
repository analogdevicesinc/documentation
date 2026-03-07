:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

Synthesis Window
================

| |synthesis.png|
| ===== Description ===== Performs the FFT synthesis window operation.
| ===== Targets Supported =====

+------------------+------------+------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+==================+===============+==================+
| Synthesis Window | NA         | NA               | B             | NA               |
+------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

====== ===== =============
Name   Type  Description
====== ===== =============
Input0 Audio Input channel
====== ===== =============

Output
------

======= ===== ==============
Name    Type  Description
======= ===== ==============
Output0 Audio Output channel
======= ===== ==============

| 
| ===== Configurable Parameters =====

+-------------------+---------------+---------------+-------------------------------------------------------------------------+
| GUI Parameter     | Default Value | Range         | Function Description                                                    |
+===================+===============+===============+=========================================================================+
| TableValues       |               |               | Window coefficients                                                     |
+-------------------+---------------+---------------+-------------------------------------------------------------------------+
| ShareCoefficients | False         | True or False | Indicates whether to share the coefficients between different instances |
+-------------------+---------------+---------------+-------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+--------------------------------------------------------+---------------------+-------------------+
| Parameter Name                                         | Description         | ADAU145x/146x     |
+========================================================+=====================+===================+
| synthesis_window\_<BlockSize/2> / synthesis_window_DM0 | Window coefficients | 8.24 Format Array |
+--------------------------------------------------------+---------------------+-------------------+

| 

.. |synthesis.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/synthesis.png
