General Eq (2nd order) Slew -(ADAU145x)
=======================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |image1|
| The General (2nd-Order) filter is a variant of a second order bi quad filter which enables smooth transition of the filter parameters when filter parameters are changed, this is done by slewing from the current filter parameters(coefficients) to the one being set. The slewing takes place approximately in the time set by the user in the GUI. The slew time can be entered in the GUI slew Text box, or open the filter control window by clicking on the icon button and enter the slew time in the slew text box or by using the slew slider. The slew time range is limited between (0 to 1 second).
| :math:`Slew function:`
| :math:`\lambda= e^{-1/{timeconstant \times F_s}}`
| :math:`Current Coefficient= Current Coffcicient \times \lambda + Target Coefficient \times (1-\lambda)`
| The above slewing function implements RC slewing. The parameter :math:`\lambda` is calculated based on the slewing time constant. The computations for slewing of filter coefficients is done on the DSP. The slew computation is always performed in single precision.

| **To open the filter control window, click on the icon button:** Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| |image2|

Configuration
=============

+------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description                                                                                   |
+==================+===============+===============+========================================================================================================+
| Enable/Bypass    | Enabled       | True/False    | Enabling or disabling of filter. On bypass, the input signal is passed through without any processing. |
+------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Phase            | In-Phase      | True/False    | Enabling the button, will invert the filter phase.                                                     |
+------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Frequency        | 1000 Hz       | 0 - 96k Hz    | Center frequency of the filter                                                                         |
+------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+
| Slew             | 0s            | 0 - 1 seconds | Set the time to slew from one set of coefficients to another.                                          |
+------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------+

| 
| This block gives access to a wide variety of 2nd-order (biquad)filter algorithms. The blend factor can be entered(0-1) or changed using the slider. The Slew time can be entered in seconds (0-1) to slew from the initial blend factor to the target value. The available filter types are:

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

Shelving
--------

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
-------

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
------------------

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
------------

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
---------------

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
-------------------

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
----------------------

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
---------

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
| ===== DSP Parameter Information =====

+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| GUI Control Name | Compiler Name                                                                                       | Function Description                       |
+==================+=====================================================================================================+============================================+
| Targ_B2\_        | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_B2\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient B2 for filter 1 |
+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_B1\_        | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_B1\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient B1 for filter 1 |
+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_B0\_        | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_B0\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient B0 for filter 1 |
+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_A2\_        | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_A2\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient A2 for filter 1 |
+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_A1\_        | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_A1\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient A1 for filter 1 |
+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| lambda\_         | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>lambda\_</fc><fc #800000>1</fc>  | Bi-quad Slewing parameter lambda           |
+------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Stage number

Supported ICs
-------------

-  ADAU145x

| 
| **NOTE: Due to fixed point operations, the filter coefficients do not slew exactly in the set slew time.**

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/generaleqslew1.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/{{/resources/tools-software/sigmastudio/toolbox/filters/generaleqslew2-form.png
   :width: 300px
