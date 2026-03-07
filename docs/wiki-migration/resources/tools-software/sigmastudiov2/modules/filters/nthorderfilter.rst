:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Nth Order Filter
================

| 
| |nthordfilt.png|

Description
-----------

The Nth Order Filter is a combination of bi-quad filters to form Nth order filter.The Filter has 3 selectable filter types to perform LowPass/HighPass filtering.

The available filter types are:

-  Butterworth Low-Pass / High-Pass
-  Chebyshev 1 Low-Pass / High-Pass
-  Chebyshev 2 Low-Pass / High-Pass

| 
| ===== Usage =====
| ===== Targets Supported =====

+------------------+------------+------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+==================+===============+==================+
| Nth Order Filter | NA         | B                | S             | NA               |
+------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range             | Function Description                                                              |
+====================+===============+===================+===================================================================================+
| Frequency          | 1000          | 3 to 30 KHz       | Cut-off frequency                                                                 |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| Gain               | 0 dB          | -10 to +10 dB     | Filter Gain                                                                       |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| Q                  | 1.41          | 1 to 15           | Q factor of the filter                                                            |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| Order              | 6             | 2 to 20           | Order of the filter                                                               |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| Ripple             | 1             | 0.1 to 20         | Ripple factor of the filter                                                       |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| FilterType         | Butterworth   | Available filters | Used to select the filter type                                                    |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| EnabledOrBypassed  | True          | True/False        | Enabled/Disabled the algorithm                                                    |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| Phase              | False         | True/False        | Controls the phase of coefficients in 0 degree or 180 degree phase                |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| IsLowPass          | True          | True/False        | Controls the Lowpass or HighPass filter                                           |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 6            | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------+------------------------+---------------+
| Parameter Name | Description                              | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==========================================+========================+===============+
| Stages         | number of bi-quads cascaded              | Integer32              | Integer32     |
+----------------+------------------------------------------+------------------------+---------------+
| A1_StageX      | Filter coefficient A1 of bi-quad stage X | Float                  | FixPoint8d24  |
+----------------+------------------------------------------+------------------------+---------------+
| A2_StageX      | Filter coefficient A2 of bi-quad stage X | Float                  | FixPoint8d24  |
+----------------+------------------------------------------+------------------------+---------------+
| B0_StageX      | Filter coefficient B0 of bi-quad stage X | Float                  | FixPoint8d24  |
+----------------+------------------------------------------+------------------------+---------------+
| B1_StageX      | Filter coefficient B1 of bi-quad stage X | Float                  | FixPoint8d24  |
+----------------+------------------------------------------+------------------------+---------------+
| B2_StageX      | Filter coefficient B2 of bi-quad stage X | Float                  | FixPoint8d24  |
+----------------+------------------------------------------+------------------------+---------------+

| Note - X indicates filter stage index

.. |nthordfilt.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/nthordfilt.png
