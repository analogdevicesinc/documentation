IIR Elliptical Interpolated Lowpass Filter (Mono & Stereo)
==========================================================

:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Description
-----------

::

   The IIR Elliptical Interpolated Lowpass Filter "Content should be added"

| 
| ===Mono=== |mono_eliptical_iir.png|

Stereo
~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/str_eliptical_iir.png
   :alt: str_eliptical_iir.png

Usage
-----

| To module has spin text box to control the order of the filter.
| ===== Variants =====

-  IIR Elliptical LowPass (Mono)
-  IIR Elliptical LowPass (Stereo)

| 
| ===== Targets Supported =====

+---------------------------------+------------+------------------+---------------+
| Name                            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x |
+=================================+============+==================+===============+
| IIR Elliptical LowPass (Mono)   | NA         | B                | NA            |
+---------------------------------+------------+------------------+---------------+
| IIR Elliptical LowPass (Stereo) | NA         | B                | NA            |
+---------------------------------+------------+------------------+---------------+

| 
| ===== Pins =====

Input
~~~~~

==== ===== ============================
Name Type  Description
==== ===== ============================
Pin0 Audio Input to the low pass filter
Pin1 Audio Input to the low pass filter
==== ===== ============================

Output
~~~~~~

==== ===== ===============
Name Type  Description
==== ===== ===============
Pin0 Audio filtered output
Pin1 Audio filtered output
==== ===== ===============

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

.. |mono_eliptical_iir.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mono_eliptical_iir.png
