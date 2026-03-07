:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

IIR Elliptical LowPass Filter
=============================

| 
| |ellipticalmonofilt.png| |ellipticalstereofilt.png|

Description
-----------

| The IIR Elliptical LowPass Filter.
| ===== Usage ===== To module has spin text box to control the order of the filter.
| ===== Variants =====

-  IIR Elliptical LowPass (Mono)
-  IIR Elliptical LowPass (Stereo)

| 
| ===== Targets Supported =====

+---------------------------------+------------+------------------+---------------+------------------+
| Name                            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================================+============+==================+===============+==================+
| IIR Elliptical LowPass (Mono)   | NA         | B                | NA            | B                |
+---------------------------------+------------+------------------+---------------+------------------+
| IIR Elliptical LowPass (Stereo) | NA         | B                | NA            | B                |
+---------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============================================
Name   Type  Description
====== ===== ===============================================
Input  Audio Input to the low pass filter(Input0 for stereo)
Input1 Audio Input1 to the low pass filter (only for stereo)
====== ===== ===============================================

Output
~~~~~~

======= ===== ====================================
Name    Type  Description
======= ===== ====================================
Output  Audio Filtered Output (Output0 for stereo)
Output1 Audio Filtered Output1 (only for stereo)
======= ===== ====================================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+---------+-------------------------------------------+
| GUI Parameter Name | Default Value | Range   | Function Description                      |
+====================+===============+=========+===========================================+
| Order              | 6             | 0 to 10 | Controls the order of the filter equation |
+--------------------+---------------+---------+-------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------+------------------------+---------------+
| Parameter Name | Description                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================+========================+===============+
| Order          | Order of the filter equations | Float                  | NA            |
+----------------+-------------------------------+------------------------+---------------+
| A0             | Filter coefficient A0         | Float                  | NA            |
+----------------+-------------------------------+------------------------+---------------+
| A1             | Filter coefficient A1         | Float                  | NA            |
+----------------+-------------------------------+------------------------+---------------+
| B0             | Filter coefficient B0         | Float                  | NA            |
+----------------+-------------------------------+------------------------+---------------+
| B1             | Filter coefficient B1         | Float                  | NA            |
+----------------+-------------------------------+------------------------+---------------+
| B2             | Filter coefficient B2         | Float                  | NA            |
+----------------+-------------------------------+------------------------+---------------+

| 

.. |ellipticalmonofilt.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/ellipticalmonofilt.png
.. |ellipticalstereofilt.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/ellipticalstereofilt.png
