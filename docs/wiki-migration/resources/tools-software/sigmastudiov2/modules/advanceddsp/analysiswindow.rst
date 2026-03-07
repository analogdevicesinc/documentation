:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

Analysis Window
===============

| |analysis.png|
| ===== Description ===== Performs the FFT analysis window operation.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Analysis Window | NA         | NA               | B             | NA               |
+-----------------+------------+------------------+---------------+------------------+

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

+----------------------------------------------------+---------------------+-------------------+
| Parameter Name                                     | Description         | ADAU145x/146x     |
+====================================================+=====================+===================+
| analysis_window\_<BlockSize> / analysis_window_DM0 | Window coefficients | 8.24 Format Array |
+----------------------------------------------------+---------------------+-------------------+

| 

.. |analysis.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/analysis.png
