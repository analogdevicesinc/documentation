:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

High Order Shelving
===================

| |higherordershelving.png| |higherordershelvingextgain.png|

Targets Supported
-----------------

+----------------------------------------+------------+------------------+---------------+------------------+
| Name                                   | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+========================================+============+==================+===============+==================+
| High Order Shelving                    | NA         | NA               | S             | NA               |
+----------------------------------------+------------+------------------+---------------+------------------+
| High Order Shelving Table Interpolator | NA         | NA               | S             | NA               |
+----------------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== =============
Name   Type  Description
====== ===== =============
Input0 Audio Input channel
====== ===== =============

Output
~~~~~~

================================= ======= ===================
Name                              Type    Description
================================= ======= ===================
Output0                           Audio   Filter Output
ExtGain0(Table Interpolator Only) Control External Gain Input
================================= ======= ===================

| 

Configurable Parameters
-----------------------

+----------------------+---------------+---------------+---------------------------------------------------+
| GUI Parameter Name   | Default Value | Range         | Function Description                              |
+======================+===============+===============+===================================================+
| Gain_StageX          | 0             | -12 to 12 dB  | Gain for individual filter stage                  |
+----------------------+---------------+---------------+---------------------------------------------------+
| Order_StageX         | 2             | 2 to 12       | Order of individual filter stage                  |
+----------------------+---------------+---------------+---------------------------------------------------+
| FilterField1_StageX  | 100           | 1 to 96000    | Lower cutoff frequency of individual filter stage |
+----------------------+---------------+---------------+---------------------------------------------------+
| FilterField2_StageX  | 96000         | 1 to 96000    | Upper cutoff frequency of individual filter stage |
+----------------------+---------------+---------------+---------------------------------------------------+
| FilterBW_StageX      | 400           | 1 to 96000    | Bandwidth of individual filter stage              |
+----------------------+---------------+---------------+---------------------------------------------------+
| OctaveSpacing_StageX | 2.322         | 1 to 12       | Octave Spacing of individual filter stage         |
+----------------------+---------------+---------------+---------------------------------------------------+
| Precisiontype_StageX | Single        | Single/Double | Precision type of individual filter stage         |
+----------------------+---------------+---------------+---------------------------------------------------+

| Note : \_StageX - Refers to parameters of each stage. X represents the stage index.
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------------------------------+---------------+
| Parameter Name | Description                                                                              | ADAU145x/146x |
+================+==========================================================================================+===============+
| FilterX_b2x0   | Numeric Array consisting of all the filter coefficients belonging to a particular stage. | 8.24          |
+----------------+------------------------------------------------------------------------------------------+---------------+

| Note : X represents the stage index.

.. |higherordershelving.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/higherordershelving.png
.. |higherordershelvingextgain.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/higherordershelvingextgain.png
