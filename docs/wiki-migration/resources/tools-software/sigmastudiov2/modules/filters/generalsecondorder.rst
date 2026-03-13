:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

General 2nd Order Filter
========================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/gen2ndorderfilt.png
   :alt: gen2ndorderfilt.png

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/genfiltsettings.png
   :alt: genfiltsettings.png

Description
-----------

The General (2nd-Order) block gives access to a wide variety of 2nd-order
(biquad)filter algorithms.

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

Usage
-----

To open the filter control window, click on the icon button. Select the desired
filter type from the drop-down combo-box list. The filter controls and the icon
button image will change to reflect the selected filter type.

Targets Supported
-----------------

+----------------------------------+------------+------------------+---------------+------------------+
| Name                             | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================================+============+==================+===============+==================+
| General Second Order             | B/S        | B/S              | S             | B                |
+----------------------------------+------------+------------------+---------------+------------------+
| General Eq Slew                  | NA         | NA               | S             | NA               |
+----------------------------------+------------+------------------+---------------+------------------+
| General Second Order SW Slew Ext | NA         | NA               | S             | NA               |
+----------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

=========================== ======= ===============================
Name                        Type    Description
=========================== ======= ===============================
Input0                      Audio   Input Channel 0
Lambda0 (For Slew Ext Only) Control External Slew Input for Stage 0
=========================== ======= ===============================

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| ===== Configurable Parameters =====

+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| GUI Parameter Name                                | Default Value     | Range                  | Function Description                                                                                      |
+===================================================+===================+========================+===========================================================================================================+
| StageX_Boost                                      | 0 dB              | -10 to +10 dB          | Set the boost value for a particular filter curve                                                         |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_Frequency                                  | 1000              | 0 to 96000Hz           | Cut-off frequency                                                                                         |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_Gain                                       | 0 dB              | -15 to +15 dB          | Filter Gain                                                                                               |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_Q                                          | 1.41              | 0.1 to 16              | Q factor of the filter                                                                                    |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_Slope                                      | 1                 | 0 to 2                 | Slope controls filter steepness and therefore the transition between the boost/cut and the flat response. |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_FilterType                                 | Parametric filter | Available filter Types | Controls the type of the filter                                                                           |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_EnabledOrBypassed                          | True              | True/False             | Enabled/Disabled the algorithm                                                                            |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_Phase                                      | False             | True/False             | Controls the phase of coefficients in 0 degree or 180 degree phase                                        |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_LockFrequency                              | False             | True/False             | Enabled/Disabled locks the frequency control                                                              |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| StageX_Slew (For Slew Variant ADAU145x/146x Only) | 0                 | 0 to 1                 | SW slew value for individual filter stages applicable only for General EQ Slew Variant                    |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| NumStages                                         | 1                 | 1 to 20                | Number of stages of filter. Change in this value requires re-compilation                                  |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| NumChannels                                       | 1                 | 1 to 20                | Number of input and output channels. Change in this value requires re-compilation                         |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| SlewType (For Slew Variant ADAU145x/146x Only)    | HWSlew            | HW/SW Slew             | Slew type for the filter HW/SW                                                                            |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| CustomSlew (For Slew Variant ADAU145x/146x Only)  | 0x208A            | 0x0 to 0xFFFF          | Custom slew value entered by user                                                                         |
+---------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+

| 
| Here, \* X - Indicates Stage Number

DSP Parameters
--------------

+----------------+-----------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                     | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=================================================================+========================+===============+
| StageX_B0      | B0 Filter Coefficient                                           | Float                  | FixPoint8d24  |
+----------------+-----------------------------------------------------------------+------------------------+---------------+
| StageX_B1      | B1 Filter Coefficient                                           | Float                  | FixPoint8d24  |
+----------------+-----------------------------------------------------------------+------------------------+---------------+
| StageX_B2      | B2 Filter Coefficient                                           | Float                  | FixPoint8d24  |
+----------------+-----------------------------------------------------------------+------------------------+---------------+
| StageX_A1      | A1 Filter Coefficient                                           | Float                  | FixPoint8d24  |
+----------------+-----------------------------------------------------------------+------------------------+---------------+
| StageX_A2      | A2 Filter Coefficient                                           | Float                  | FixPoint8d24  |
+----------------+-----------------------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew value for medium size eq slew variant only                 | NA                     | Integer32     |
+----------------+-----------------------------------------------------------------+------------------------+---------------+
| StageX_Lambda  | Exponential decay value of filter stage X for SW slew type only | NA                     | FixPoint8d24  |
+----------------+-----------------------------------------------------------------+------------------------+---------------+

| 
| Here,

-   X - Stage Number (Changes for each stage coefficients)
