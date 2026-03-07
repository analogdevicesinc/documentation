:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Soft Clipper - Standard Cubic
=============================

| 
| |standardcubic.png|

Description
-----------

| The Standard Cubic block is a soft clipper that uses a cubic function to clip the level of the input signal. As the input signal reaches the clip threshold, the algorithm rounds the edges for a smoother clipped output.
| ===== Targets Supported =====

+----------------------+------------+------------------+---------------+------------------+
| Name                 | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+======================+============+==================+===============+==================+
| Soft Clipper - Cubic | B/S        | B/S              | S             | B                |
+----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input channel X
======================= ===== ===============

Output
~~~~~~

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                                                                                                                                                |
+====================+===============+==============+=====================================================================================================================================================================================+
| IsLinear           | True          | True / False | Allows the values in linear or DB                                                                                                                                                   |
+--------------------+---------------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Alpha              | 1             | 0.1 to 10    | This pre/post scalar determines the amount of clipping that will occur. Although this influences the threshold value of the clipper, this is not the value at which clipping occurs |
+--------------------+---------------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 20           | Number of input and output channels. Change in this value requires re-compilation                                                                                                   |
+--------------------+---------------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------+------------------------+----------------+
| Parameter Name | Description                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x  |
+================+===============================+========================+================+
| Alpha          | Current Alpha value           | Float                  | FixedPoint8d24 |
+----------------+-------------------------------+------------------------+----------------+
| AlphaInv       | Inverse alpha value (1/Alpha) | Float                  | FixedPoint8d24 |
+----------------+-------------------------------+------------------------+----------------+

DSP Parameter Computation
-------------------------

Alpha = 10^(Alpha in dB / 20)

.. |standardcubic.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/standardcubic.png
