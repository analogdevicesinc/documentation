:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

Subharmonic Synthesizer
=======================

Subharmonic Synthesizer (General)
---------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/subharmonicgeneral.png
   :alt: subharmonicgeneral.png

Subharmonic Synthesizer (Low Frequency)
---------------------------------------

| |subharmonic.png|
| ===== Description ===== Subharmonic synthesizer generates subharmonics of the input signal.
| ===== Variants =====

-  Subharmonic Synthesizer (General)
-  Subharmonic Synthesizer (Low Frequency)

| 
| ===== Targets Supported =====

+-----------------------------------------+------------+------------------+---------------+------------------+
| Name                                    | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=========================================+============+==================+===============+==================+
| Subharmonic Synthesizer (General)       | NA         | NA               | S             | NA               |
+-----------------------------------------+------------+------------------+---------------+------------------+
| Subharmonic Synthesizer (Low Frequency) | NA         | NA               | S             | NA               |
+-----------------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===========
Name   Type  Description
====== ===== ===========
Input0 Audio Input Audio
====== ===== ===========

Output
~~~~~~

======= ===== ============
Name    Type  Description
======= ===== ============
Output0 Audio Output audio
======= ===== ============

| 
| ===== Configurable Parameters =====

+----------------+---------------+----------+----------------------------------------------+
| GUI Parameter  | Default Value | Range    | Function Description                         |
+================+===============+==========+==============================================+
| LowSubHarmonic | 60            | 40 - 125 | Maximum frequency for subharmonic generation |
+----------------+---------------+----------+----------------------------------------------+

| 
| ===== DSP Parameters =====

============== ============ =============
Parameter Name Description  ADAU145x/146x
============== ============ =============
B2_1           Coefficients 8.24 Format
B2_5           Coefficients 8.24 Format
B2_6           Coefficients 8.24 Format
============== ============ =============

.. |subharmonic.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/subharmonic.png
