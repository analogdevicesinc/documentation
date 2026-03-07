:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

RMS Blend EQ
============

| The 'RMS Blend EQ ' block blends the filter coefficients of two second order filters according to the RMS value of the detect signal specified and performs filtering operation. The detect signal will be obtained via the control input pin.
| |module.png|
| The blend factor calculation is based on the RMS value of the detect signal, as shown in the figure below:
| |image1|

.. container:: centeralign

   \ **Figure:** Blend Factor Calculation


-  The blend factor(0-1) is obtained as input through the control pin.
-  The Slew time can be entered in GUI in seconds (0-1) to slew from the initial blend factor to the target value.

Blend factor and slew rate modifications are common for all the stages.

Description
-----------

| The RMS Blend Equalizer module along with General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms along with equalization.
| |rmsblendeqfiltsettings.png|

The available filter types are:

-  Parametric
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
| ===== Usage ===== To open the filter control window, click on the icon button. Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type. Also varying the threshold values and RMS time constant values would change the output values accordingly

Targets Supported
-----------------

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
RMSEqBlend B/S        B/S              S             NA
========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ======= ===============================================
Name   Type    Description
====== ======= ===============================================
Input0 Audio   Input Channel 0
Blend0 Control External Blend pin for SingleEqExtBlend variant
====== ======= ===============================================

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
| NumChannels                                                        | 1                 | 1 to 20                | Increases or decreases the number of input and output channels. Changing this requires re-compilation     |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| NumStages                                                          | 1                 | 1 to 20                | Increases or decreases the number of filter stages. Changing this requires re-compilation                 |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Blend                                                              | 0                 | 0 to 1                 | Blend factor for the equalizer module                                                                     |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| SlewRate                                                           | 0.01              | 0.01 to 1              | Defines the rate at which input takes the new value                                                       |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| LowerThreshold                                                     | 0.01              | 0.01 to 24             | Defines the Lower threshold for the applying the RMS Blend value                                          |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| UpperThreshold                                                     | 0.01              | 0.01 to 24             | Defines the Upper threshold for the applying the RMS Blend value                                          |
+--------------------------------------------------------------------+-------------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| RMSTC                                                              | 0.001             | 0.001 to 6             | Defines the RMS time constant value                                                                       |
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

.. |module.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/module.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/blendfactorcalculation.png
   :width: 600px
.. |rmsblendeqfiltsettings.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/rmsblendeqfiltsettings.png
