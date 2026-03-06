Single Blend EQ
===============

:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

The 'Single Blend EQ' block blends the filter coefficients of two second order filters according to the blend factor specified and performs filtering operation

| 
| |image1|

| 
| This block gives access to a wide variety of 2nd-order (biquad)filter algorithms. The blend factor can be entered(0-1) or changed using the slider. The Slew time can be entered in seconds (0-1) to slew from the initial blend factor to the target value.

-  The available filter types are:
-  Parametric
-  Shelving
-  General High-Pass
-  General Low-Pass
-  General Band-Pass
-  General Band-Stop
-  Butterworth Low-Pass / High-Pass
-  Bessel Low-Pass / High-Pass
-  Tone Control
-  :doc:`IIR Coefficient (direct coefficient entry) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorder/iircoefficient>`
-  1st-Order Low-Pass / High-Pass
-  All-pass
-  Peaking
-  Notch
-  Chebyshev Low-Pass / High-Pass

The slewing functionality is added for smooth transition from one blend factor to another when the blending factor is changed. The slewing takes place approximately in the time set by the user in the GUI. The slew time can be entered in the GUI slew Text box. The slew time range is limited between (0 to 1 second).

Input Pins
----------

+-------------------+------------------------------------+----------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description |
+===================+====================================+======================+
| Pin 0: Filter In1 | decimal - audio                    | Input to the filter  |
+-------------------+------------------------------------+----------------------+

| 
| ----

Output Pins
-----------

+--------------------+------------------------------------+----------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description |
+====================+====================================+======================+
| Pin 0: Filter Out1 | decimal - audio                    | Filtered output      |
+--------------------+------------------------------------+----------------------+

--------------

| 
| =====Configuration===== |image2|

| 

+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| GUI Control Name         | Default Value | Range         | Function Description                                                                                   |
+==========================+===============+===============+========================================================================================================+
| Enable/Bypass - Filter 1 | Enabled       | True/False    | Enabling or disabling of filter. On bypass, the input signal is passed through without any processing. |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Phase - Filter 1         | In-Phase      | True/False    | Enabling the button, will invert the filter phase.                                                     |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Frequency - Filter 1     | 1000 Hz       | 0 - 96k Hz    | Center frequency of the filter                                                                         |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Enable/Bypass - Filter 2 | Enabled       | True/False    | Enabling or disabling of filter. On bypass, the input signal is passed through without any processing. |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Phase - Filter 2         | In-Phase      | True/False    | Enabling the button, will invert the filter phase.                                                     |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Frequency - Filter 2     | 1000 Hz       | 0 - 96k Hz    | Center frequency of the filter                                                                         |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Slew                     | 0.01 s        | 0 - 1 seconds | Set the time to slew from one set of coefficients to another.                                          |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Blend                    | 0             | 0-1           | Set the blend between two sets of filters                                                              |
+--------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+

| 
| Click on the |image3| icon to configure the filters. Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| The GUI controls for various types of filters are given below.

Parameteric
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/parametricsettings2.png
   :align: center

+------------------+---------------+-------------+-------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                |
+==================+===============+=============+=====================================+
| Frequency        | 1000Hz        | 0-96kHz     | Cut off frequency of the filter     |
+------------------+---------------+-------------+-------------------------------------+
| Gain             | 0dB           | -15 - 15 dB | dB gain of the filter coefficients. |
+------------------+---------------+-------------+-------------------------------------+
| Q                | 1.41          | 0-16        | Q Factor for filter calculations    |
+------------------+---------------+-------------+-------------------------------------+

--------------

Shelving
~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/ShelvingSettings2.png
   :align: center

+------------------+---------------+----------------------+------------------------------------+
| GUI Control Name | Default Value | Range                | Function Description               |
+==================+===============+======================+====================================+
| Shelf type       | Low Shelf     | Low Shelf/High Shelf | Shelving type for the filter       |
+------------------+---------------+----------------------+------------------------------------+
| Frequency        | 1000Hz        | 0-96kHz              | Cut off frequency of the filter    |
+------------------+---------------+----------------------+------------------------------------+
| Gain             | 0dB           | -15 - 15 dB          | dB gain of the filter coefficients |
+------------------+---------------+----------------------+------------------------------------+
| Q                | 1.41          | 0-16                 | Q Factor for filter calculations   |
+------------------+---------------+----------------------+------------------------------------+
| Slope            | 1             | 0-2                  | Slope                              |
+------------------+---------------+----------------------+------------------------------------+

| 

--------------

General
~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/GeneralFiltSettings2.png
   :align: center

+------------------+-----------------+--------------------------------------+------------------------------------+
| GUI Control Name | Default Value   | Range                                | Function Description               |
+==================+=================+======================================+====================================+
| Type             | Low Pass Filter | Low Pass/High Pass/BandPass/BandStop | General filter type                |
+------------------+-----------------+--------------------------------------+------------------------------------+
| Frequency        | 1000Hz          | 0-96kHz                              | Cut off frequency of the filter    |
+------------------+-----------------+--------------------------------------+------------------------------------+
| Gain             | 0dB             | -15 - 15 dB                          | dB gain of the filter coefficients |
+------------------+-----------------+--------------------------------------+------------------------------------+
| Q                | 1.41            | 0-16                                 | Q Factor for filter calculations   |
+------------------+-----------------+--------------------------------------+------------------------------------+

--------------

Butterworth/Bessel
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/ButterwothSettings2.png
   :align: center

+------------------+-----------------+-----------------------------------------------------------------------------+------------------------------------+
| GUI Control Name | Default Value   | Range                                                                       | Function Description               |
+==================+=================+=============================================================================+====================================+
| Type             | Bessel Low Pass | Bessel Low Pass/Bessel High Pass/Butterworth Low Pass/Butterworth High Pass | Filter type                        |
+------------------+-----------------+-----------------------------------------------------------------------------+------------------------------------+
| Frequency        | 1000Hz          | 0-96kHz                                                                     | Cut off frequency of the filter    |
+------------------+-----------------+-----------------------------------------------------------------------------+------------------------------------+
| Gain             | 0dB             | -15 - 15 dB                                                                 | dB gain of the filter coefficients |
+------------------+-----------------+-----------------------------------------------------------------------------+------------------------------------+

--------------

Tone Control
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/ToneControlSettings2.png
   :align: center

+------------------+---------------+-------------+-------------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                      |
+==================+===============+=============+===========================================+
| Treble Frequency | 1000Hz        | 0-96kHz     | Treble Cut off frequency of the filter    |
+------------------+---------------+-------------+-------------------------------------------+
| Treble Gain      | 0dB           | -15 - 15 dB | Treble dB gain of the filter coefficients |
+------------------+---------------+-------------+-------------------------------------------+
| Bass Frequency   | 1000Hz        | 0-96kHz     | Bass Cut off frequency of the filter      |
+------------------+---------------+-------------+-------------------------------------------+
| Bass Gain        | 0dB           | -15 - 15 dB | Bass dB gain of the filter coefficients   |
+------------------+---------------+-------------+-------------------------------------------+

--------------

IIR Coefficient
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/iirSettings2.png
   :align: center

================ ============= =========== =============================
GUI Control Name Default Value Range       Function Description
================ ============= =========== =============================
b0               1             -100 to 100 B0 coefficient for the filter
b1               0             -100 to 100 B1 coefficient for the filter
b2               0             -100 to 100 B2 coefficient for the filter
a1               0             -100 to 100 A1 coefficient for the filter
a2               0             -100 to 100 A2 coefficient for the filter
================ ============= =========== =============================

--------------

First Order Filters
~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/FirstOrderSettings2.png
   :align: center

+------------------+---------------------------------------------+-------------------+----------------------------------------+
| GUI Control Name | Default Value                               | Range             | Function Description                   |
+==================+=============================================+===================+========================================+
| Filter Frequency | 1000Hz                                      | 0-96kHz           | Cut off frequency of the filter        |
+------------------+---------------------------------------------+-------------------+----------------------------------------+
| Active           | Checked                                     | Checked/Unchecked | Indicates whether the filter is active |
+------------------+---------------------------------------------+-------------------+----------------------------------------+
| Type             | High for 1st filter,Low - for second filter | Low/High/All pass | Type of the filter                     |
+------------------+---------------------------------------------+-------------------+----------------------------------------+
| Gain             | 0dB                                         | -15 - 15 dB       | dB gain of the filter coefficients     |
+------------------+---------------------------------------------+-------------------+----------------------------------------+
| Q                | 1.41                                        | 0-16              | Q Factor for filter calculations       |
+------------------+---------------------------------------------+-------------------+----------------------------------------+

--------------

All Pass,Peaking,Notch
~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/AllPasssettings2.png
   :align: center

+------------------+---------------+-------------+------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description               |
+==================+===============+=============+====================================+
| Frequency        | 1000Hz        | 0-96kHz     | Cut off frequency of the filter    |
+------------------+---------------+-------------+------------------------------------+
| Gain             | 0dB           | -15 - 15 dB | dB gain of the filter coefficients |
+------------------+---------------+-------------+------------------------------------+
| Q                | 1.41          | 0-16        | Q Factor for filter calculations   |
+------------------+---------------+-------------+------------------------------------+

--------------

Chebyshev
~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/Chebysettings2.png
   :align: center

+------------------+---------------+-------------+---------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                  |
+==================+===============+=============+=======================================+
| Frequency        | 1000Hz        | 0-96kHz     | Cut off frequency of the filter       |
+------------------+---------------+-------------+---------------------------------------+
| Gain             | 0dB           | -15 - 15 dB | dB gain of the filter coefficients    |
+------------------+---------------+-------------+---------------------------------------+
| Ripple           | 0.1           | 0-10        | Ripple Factor for filter calculations |
+------------------+---------------+-------------+---------------------------------------+

--------------

| 
| ====DSP Parameter Information====

+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                                          | Function Description                                                                                                                                                |
+==================+========================================================================================================+=====================================================================================================================================================================+
| F1_B2\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F1_B2\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient B2 for filter 1                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F1_B1\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F1_B1\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient B1 for filter 1                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F1_B0\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F1_B0\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient B0 for filter 1                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F1_A2\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F1_A2\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient A2 for filter 1                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F1_A1\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F1_A1\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient A1 for filter 1                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F2_B2\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F2_B2\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient B2 for filter 2                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F2_B1\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F2_B1\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient B1 for filter 2                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F2_B0\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F2_B0\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient B0 for filter 2                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F2_A2\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F2_A2\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient A2 for filter 2                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| F2_A1\_          | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>F2_A1\_</fc><fc #800000>1</fc>        | Bi-quad filter coefficient A1 for filter 2                                                                                                                          |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lambda\_         | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>lambda\_</fc><fc #800000>1</fc>       | time_constant = slew_time/(PI \* 1.5),Lambda\_= exp(-1/(time_constant*FS)) where,slew_time is the time required to slew from initial to final value of coefficient. |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BlendFactor      | <fc #008000>SingleBlendEQSPAlg</fc><fc #ff0000>1</fc><fc #000080>blend_factor\_</fc><fc #800000>1</fc> | Blending factor.                                                                                                                                                    |
+------------------+--------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Stage number

Note: The algorithm names for different algorithms for this module are:

-  Single Blend EQ single precision algorithm(ADAU145x): SingleBlendEQSPAlg
-  Single Blend EQ double precision algorithm(ADAU145x): SingleBlendEQDPAlg
-  Single Blend EQ single precision algorithm(ADSPSC5xx): MChSingleBlendFiltAlg
-  Single Blend EQ extended precision algorithm(ADSPSC5xx): MChSingleBlendFiltEPAlg

--------------

Supported ICs
~~~~~~~~~~~~~

-  ADAU145x/ADAU146x
-  ADSPSC5xx

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/singleblendtreetool.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/singleblendcell.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/filter_icon.png
