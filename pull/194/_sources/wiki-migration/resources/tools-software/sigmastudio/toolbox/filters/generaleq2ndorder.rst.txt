General Filters
===============

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| \* General 2nd Order (No-Slew)

-  General 2nd Order (HW-Slew)
-  Coefficient Calculations on DSP (ADAU145X)

--------------

1.General 2nd Order
-------------------

| |general2ndpic1.png|
| The General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms.The coefficient calculations happen in the controller.

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

**To open the filter control window, click on the icon button:**

| Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| |general2ndpic2.png|

--------------

| This block's algorithms use biquad filter designs (:ez:`Direct Form II <message/16011#16011>`) based on Robert Bristow-Johnson's work in this field.
| :math:`\displaystyle H(z)=b_0 + b_1 z^-1 + b_2 z^-\frac{2}{1} + a_1 z^-1 + a_2 z^-2`
| common variables:

-   :math:`omega_0 = 2 \pi f_0/F_s`
-   :math:`\displaystyle gainLinear = 10^\frac{gain}{20}`

| 
| |general2ndpic4.png|
| Note that the b0 and b2 coefficients for the high pass filter below are inverted from what is stored in RAM. The correct equations for b0, b1, and b2 for a high pass filter are as follows:
| b0 = -(1 + cos(ω0)) \* gainLinear / 2
| b1 = -(1 + cos(ω0)) \* gainLinear
| b2 = -(1 + cos(ω0)) \* gainLinear / 2
| |general2ndpic5.png|
| **Note that the minus signs on b0 and b2 values are erroneous for the Butterworth HP and Bessel HP. They should not be included. See** http://ez.analog.com/message/4769

| |general2ndpic6.png|
| For all of the above filters, the coefficients are divided by a0, normalizing them and making a0 = 1 so that only 5 coefficients must be stored. In the actual implementation on the DSP, when the coefficients are stored in parameter RAM, a1 and a2 need to be inverted. This is done automatically, in software, before the parameters are written to memory.

By default, the Q is shown with the value adjusted (from the classical EE definition) so that a boost of N dB followed by a cut of N dB for identical Q and f0/Fs results in a precisely flat unity gain filter or "wire". This is equal to A\*Q, where A = 10^(dBgain/40).

.. image:: https://wiki.analog.com/_media/classicqcontrol.jpg
   :alt: classicqcontrol.jpg

The "Classic EQ" version of Q can optionally be shown by clicking the small circular button next to the Q control.

.. image:: https://wiki.analog.com/_media/classicqdisplay.jpg
   :alt: classicqdisplay.jpg

2.General 2nd Order (HW-Slew)
-----------------------------

| |general2ndpic1.png|
| The General (2nd-Order) filter is a variant of a second order bi-quad filter which enables a smooth transition of the filter parameters when filter parameters are changed, this is done by slewing from the current filter parameters(coefficients) to the one being set.

The slew type and slew time can be set by the user in GUI as shown below. Right click on the General 2nd Order filter module


|image1|

On click on the Custom, the "Set Slew Mode" form will open as shown below


|image2|

The algorithm supports three slew types

::

    1. Linear Slew
    2. RC Slew
    3. Exponential Slew

This block gives access to a wide variety of 2nd-order (biquad)filter algorithms. he available filter types are:

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
| Gain             | 0dB           | -15 to +15 dB        | dB gain of the filter coefficients |
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
| Gain             | 0dB             | -15 to +15 dB                        | dB gain of the filter coefficients |
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
| Gain             | 0dB             | -15 to +15 dB                                                               | dB gain of the filter coefficients |
+------------------+-----------------+-----------------------------------------------------------------------------+------------------------------------+

--------------

Tone Control
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/ToneControlSettings2.png
   :align: center

+------------------+---------------+---------------+-------------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description                      |
+==================+===============+===============+===========================================+
| Treble Frequency | 1000Hz        | 0-96kHz       | Treble Cut off frequency of the filter    |
+------------------+---------------+---------------+-------------------------------------------+
| Treble Gain      | 0dB           | -15 to +15 dB | Treble dB gain of the filter coefficients |
+------------------+---------------+---------------+-------------------------------------------+
| Bass Frequency   | 1000Hz        | 0-96kHz       | Bass Cut off frequency of the filter      |
+------------------+---------------+---------------+-------------------------------------------+
| Bass Gain        | 0dB           | -15 to +15 dB | Bass dB gain of the filter coefficients   |
+------------------+---------------+---------------+-------------------------------------------+

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
| Gain             | 0dB                                         | -15 to +15 dB     | dB gain of the filter coefficients     |
+------------------+---------------------------------------------+-------------------+----------------------------------------+
| Q                | 1.41                                        | 0-16              | Q Factor for filter calculations       |
+------------------+---------------------------------------------+-------------------+----------------------------------------+

--------------

All Pass,Peaking,Notch
~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/AllPasssettings2.png
   :align: center

+------------------+---------------+---------------+------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description               |
+==================+===============+===============+====================================+
| Frequency        | 1000Hz        | 0-96kHz       | Cut off frequency of the filter    |
+------------------+---------------+---------------+------------------------------------+
| Gain             | 0dB           | -15 to +15 dB | dB gain of the filter coefficients |
+------------------+---------------+---------------+------------------------------------+
| Q                | 1.41          | 0-16          | Q Factor for filter calculations   |
+------------------+---------------+---------------+------------------------------------+

--------------

Chebyshev
~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/Chebysettings2.png
   :align: center

+------------------+---------------+---------------+---------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description                  |
+==================+===============+===============+=======================================+
| Frequency        | 1000Hz        | 0-96kHz       | Cut off frequency of the filter       |
+------------------+---------------+---------------+---------------------------------------+
| Gain             | 0dB           | -15 to +15 dB | dB gain of the filter coefficients    |
+------------------+---------------+---------------+---------------------------------------+
| Ripple           | 0.1           | 0-10          | Ripple Factor for filter calculations |
+------------------+---------------+---------------+---------------------------------------+

--------------

| 
| ===== DSP Parameter Information =====

+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+
| GUI Control Name | Compiler Name                                                                                         | Function Description                       |
+==================+=======================================================================================================+============================================+
| Targ_B2\_        | <fc #008000>EQS300MultiSpHWSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_B2\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient B2 for filter 1 |
+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_B1\_        | <fc #008000>EQS300MultiSpHWSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_B1\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient B1 for filter 1 |
+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_B0\_        | <fc #008000>EQS300MultiSpHWSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_B0\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient B0 for filter 1 |
+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_A2\_        | <fc #008000>EQS300MultiSpHWSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_A2\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient A2 for filter 1 |
+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+
| Targ_A1\_        | <fc #008000>EQS300MultiSpHWSlewAlg</fc><fc #ff0000>1</fc><fc #000080>Targ_A1\_</fc><fc #800000>1</fc> | Bi-quad filter coefficient A1 for filter 1 |
+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+
| \_slewmode       | <fc #008000>EQS300MultiSpSlewAlg</fc><fc #ff0000>1</fc><fc #000080>_slewmode</fc><fc #800000>1</fc>   | Bi-quad slew mode                          |
+------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Stage number

Supported ICs
~~~~~~~~~~~~~

-  ADAU145x
-  ADAU146x

3.Coefficient Calculations on DSP
---------------------------------

The General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms.The coefficient calculations happen in the controller.

-  The available filter types are:
-  Parametric
-  Shelving
-  General High-Pass
-  General Low-Pass
-  General Band-Pass
-  General Band-Stop
-  Butterworth Low-Pass / High-Pass
-  Bessel Low-Pass / High-Pass
-  All-pass
-  Peaking
-  Notch
-  Chebyshev Low-Pass / High-Pass

**To open the filter control window, click on the icon button:**

| Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| |general2ndpic2.png|
| ====GUI Control====

+------------------+---------------+------------------------------------+-------------------------------------+
| GUI Control Name | Default Value | Range                              | Function Description                |
+==================+===============+====================================+=====================================+
| Filter Type      | Lowpass       | LowPass/Highpass/BandPass/BandStop | Type of the filter                  |
+------------------+---------------+------------------------------------+-------------------------------------+
| Frequency        | 1000 Hz       | 0-96000 Hz                         | The cut off frequency of the filter |
+------------------+---------------+------------------------------------+-------------------------------------+
| Gain             | 0 dB          | -15 to 15                          | Filter Gain                         |
+------------------+---------------+------------------------------------+-------------------------------------+
| Q Factor         | 0             | 0 to 16                            | Q Factor of the filter              |
+------------------+---------------+------------------------------------+-------------------------------------+
| Enable           | 1             | 0 t0 1                             | Enable or disable filter            |
+------------------+---------------+------------------------------------+-------------------------------------+
| Phase Shift      | 0             | 0 to 1                             | Phase shift by 180 deg              |
+------------------+---------------+------------------------------------+-------------------------------------+

DSP parameter Information
~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+------------------------------+--------------------------------------------------------------+
| GUI Control Name | Compiler Name                | Function Description                                         |
+==================+==============================+==============================================================+
| Frequency        | FREQ_DSP_CALC0\_ \_          | The cut off frequency of the filter                          |
+------------------+------------------------------+--------------------------------------------------------------+
| Gain             | GAIN_DSP_CALC0\_ \_          | Filter Gain                                                  |
+------------------+------------------------------+--------------------------------------------------------------+
| Q Factor         | Q_DSP_CALC0\_ \_             | Q Factor of the filter                                       |
+------------------+------------------------------+--------------------------------------------------------------+
| Filter Type      | FILTER_TYPE0\_ \_            | Type of the filter                                           |
+------------------+------------------------------+--------------------------------------------------------------+
| NA               | INVERT\_\_                   | Negate the Coefficients corresponding to the input           |
+------------------+------------------------------+--------------------------------------------------------------+
| NA               | ONE_BY_FS_DSP_CALC0\_ \_     | 1/ Sample Rate                                               |
+------------------+------------------------------+--------------------------------------------------------------+
| NA               | ADDRESS_DSP_CALC0\_ \_       | Starting Address of the filter coefficients.                 |
+------------------+------------------------------+--------------------------------------------------------------+
| NA               | MEM_SELECTION_DSP_CALC0\_ \_ | Memory section the filter coefficients are located (DM0/DM1) |
+------------------+------------------------------+--------------------------------------------------------------+

| It is possible to selectively disable filters which are not going to be used.To select only those filters to be used, right click on the module and select Configure Supported Filters and select only those filters which might be used.
| |filterconfigure.png|\ |filterconfiguretab.png|

.. |general2ndpic1.png| image:: https://wiki.analog.com/_media/general2ndpic1.png
.. |general2ndpic2.png| image:: https://wiki.analog.com/_media/general2ndpic2.png
.. |general2ndpic4.png| image:: https://wiki.analog.com/_media/general2ndpic4.png
.. |general2ndpic5.png| image:: https://wiki.analog.com/_media/general2ndpic5.png
.. |general2ndpic6.png| image:: https://wiki.analog.com/_media/general2ndpic6.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/hwslewfilterslewsetting.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/hwslewfiltercustomslew.png
.. |filterconfigure.png| image:: https://wiki.analog.com/_media/filterconfigure.png
.. |filterconfiguretab.png| image:: https://wiki.analog.com/_media/filterconfiguretab.png
