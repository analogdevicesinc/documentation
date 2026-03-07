:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Index Selectable Multiple Band
==============================

| 
| |isibfiltmono.png| |isibfiltstereo.png|
| |isibfiltsettings.png|

Description
-----------

The Index Selectable Multiple Band block provides a wide variety of 2nd-order filter algorithms.

The available filter types are:

-  Low shelf filter
-  High shelf filter
-  Parametric filter
-  Peaking filter
-  First order low shelf filter
-  First order high shelf filter
-  Notch filter
-  Band pass filter
-  Band stop filter
-  All pass filter
-  High pass filter
-  Low pass filter

| 

Variants
--------

-  Index Selectable Multiple Band (1 Ch)
-  Index Selectable Multiple Band (2 Ch)

|

| ===== Targets Supported =====

+---------------------------------------+------------+------------------+---------------+------------------+
| Name                                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================================+============+==================+===============+==================+
| Index Selectable Multiple Band (1 Ch) | B/S        | B/S              | S             | B                |
+---------------------------------------+------------+------------------+---------------+------------------+
| Index Selectable Multiple Band (2 Ch) | B/S        | B/S              | S             | B                |
+---------------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

================= ======= ==============================================
Name              Type    Description
================= ======= ==============================================
IndexSelectInput0 Control Index of the selected frequency response curve
Input1            Audio   Input to the filter
================= ======= ==============================================

Output
~~~~~~

======= ===== ===================
Name    Type  Description
======= ===== ===================
Output1 Audio The filtered output
======= ===== ===================

| 
| ===== Configurable Parameters =====

+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| GUI Parameter Name | Default Value     | Range                  | Function Description                                               |
+====================+===================+========================+====================================================================+
| FilterCount        | 1                 | 1 to 16                | Selects a filter response curve by filter number selected          |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| Boost              | 0 dB              | -20 to +20 dB          | Set the boost value for a particular filter curve                  |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| Frequency          | 1000 Hz           | 0 to 96 KHz            | Cut-off frequency                                                  |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| Gain               | 0 dB              | -15 to +15 dB          | Filter Gain                                                        |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| Q                  | 1.41              | 0.1 to 15              | Q factor of the filter                                             |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| FilterType         | Parametric filter | Available filter Types | Controls the type of the filter                                    |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| EnabledOrBypassed  | True              | True/False             | Enabled/Disabled the algorithm                                     |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+
| Phase              | False             | True/False             | Controls the phase of coefficients in 0 degree or 180 degree phase |
+--------------------+-------------------+------------------------+--------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------------------+---------------------------------------------------+------------------------+---------------+
| Parameter Name             | Description                                       | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+============================+===================================================+========================+===============+
| Stage<fc #ff0000>0</fc>_B0 | B0 Filter Coefficient                             | Float                  | FixPoint8d24  |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>0</fc>_B1 | B1 Filter Coefficient                             | Float                  | FixPoint8d24  |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>0</fc>_B2 | B2 Filter Coefficient                             | Float                  | FixPoint8d24  |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>0</fc>_A1 | A1 Filter Coefficient                             | Float                  | FixPoint8d24  |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>0</fc>_A2 | A2 Filter Coefficient                             | Float                  | FixPoint8d24  |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| alpha                      | Exponential decay factor                          | Float                  | FixPoint8d24  |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| CascadeCounts              | Number of Cascaded Stages                         | Integer32              | Integer32     |
+----------------------------+---------------------------------------------------+------------------------+---------------+
| ParamSize                  | Total number of filter coefficients of all stages | Integer32              | Integer32     |
+----------------------------+---------------------------------------------------+------------------------+---------------+

| 
| Here,

-  <fc #ff0000> Red</fc> - Stage Number (Changes for each stage coefficients)

| 

.. |isibfiltmono.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/indexselectablemultiplebad/isibfiltmono.png
.. |isibfiltstereo.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/indexselectablemultiplebad/isibfiltstereo.png
.. |isibfiltsettings.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/indexselectablemultiplebad/isibfiltsettings.png
