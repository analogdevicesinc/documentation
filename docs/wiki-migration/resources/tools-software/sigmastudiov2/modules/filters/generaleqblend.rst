:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

General Eq Blend
================

| 
| |generaleqblend.png| |generaleqextblend.png|
| |geneqblendfiltsettings.png|

Description
-----------

The General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms along with equalization. Blend factor and slew rate modifications are allowed on the module for each stage.

The available filter types are:

-  Unordered List ItemOrdered List ItemParametric
-  Shelving
-  General High-Pass
-  General Low-Pass
-  General Band-Pass
-  General Band-Stop
-  Butterworth Low-Pass / High-Pass
-  Bessel Low-Pass / High-Pass
-  Tone Control
-  IIR Coefficient (direct coefficient entry)
-  1st-Order Low-Pass / High-Pass
-  All-pass
-  Peaking
-  Notch
-  Chebyshev Low-Pass / High-Pass

| 
| ===== Usage ===== To open the filter control window, click on the icon button. Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| ===== Variants ===== General Equalizer module with External blend factor(General Eq Ext Blend). The number of Blend pins varies with the number of stages opted for.
| ===== Targets Supported =====

+-------------------+------------+------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+==================+===============+==================+
| GeneralEqBlend    | B/S        | B/S              | S             | B                |
+-------------------+------------+------------------+---------------+------------------+
| GeneralEqBlendExt | B/S        | B/S              | S             | B                |
+-------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ======= ================================================
Name   Type    Description
====== ======= ================================================
Input0 Audio   Input Channel 0
Blend0 Control External Blend pin for GeneralEqExtBlend variant
====== ======= ================================================

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| GUI Parameter Name                                                 | Default Value     | Range                  | Function Description                                                                                      |
+====================================================================+===================+========================+===========================================================================================================+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_Boost             | 0 dB              | -10 to +10 dB          | Set the boost value for a particular filter curve                                                         |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_Frequency         | 1000              | 0 to 96000Hz           | Cut-off frequency                                                                                         |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_Gain              | 0 dB              | -15 to +15 dB          | Filter Gain                                                                                               |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_Q                 | 1.41              | 0.1 to 16              | Q factor of the filter                                                                                    |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_Slope             | 1                 | 0 to 2                 | Slope controls filter steepness and therefore the transition between the boost/cut and the flat response. |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_FilterType        | Parametric filter | Available filter Types | Controls the type of the filter                                                                           |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_EnabledOrBypassed | True              | True/False             | Enabled/Disabled the algorithm                                                                            |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_Phase             | False             | True/False             | Controls the phase of coefficients in 0 degree or 180 degree phase                                        |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Slew                                       | 0                 | 0 to 1                 | Slew value for individual filter stages                                                                   |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Blend                                      | 0                 | 0 to 1                 | Blend value for individual filter stage                                                                   |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| NumStages                                                          | 1                 | 1 to 20                | Number of stages of filter. Change in this value requires re-compilation                                  |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| NumChannels                                                        | 1                 | 1 to 20                | Number of input and output channels. Change in this value requires re-compilation                         |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+

| 
| Here, \* <fc #ff0000> X</fc> - Indicates Stage Number \* <fc #ff0000> Y</fc> - Indicates Filter A/Filter B

DSP Parameters
--------------

+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+
| Parameter Name                                      | Description                               | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=====================================================+===========================================+========================+===============+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_B0 | B0 Filter Coefficient                     | Float                  | FixPoint8d24  |
+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_B1 | B1 Filter Coefficient                     | Float                  | FixPoint8d24  |
+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_B2 | B2 Filter Coefficient                     | Float                  | FixPoint8d24  |
+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_A1 | A1 Filter Coefficient                     | Float                  | FixPoint8d24  |
+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>X</fc>_Filter<fc #ff0000>Y</fc>_A2 | A2 Filter Coefficient                     | Float                  | FixPoint8d24  |
+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+
| Stage<fc #ff0000>X</fc>_Slew_Lambda                 | Exponential decay value of filter stage X | Float                  | FixPoint8d24  |
+-----------------------------------------------------+-------------------------------------------+------------------------+---------------+

| 
| Here,

-  <fc #ff0000> X</fc> - Stage Number (Changes for each stage coefficients)
-  <fc #ff0000> Y</fc> - Filter A/B for each stage X

| 

.. |generaleqblend.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/generaleqblend.png
.. |generaleqextblend.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/generaleqextblend.png
.. |geneqblendfiltsettings.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/geneqblendfiltsettings.png
