General Filters
===============

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| \* General 2nd Order

-  Coefficient Calculations on DSP (ADAU145X)

--------------

1.General 2nd Order
-------------------

| |general2ndpic1.png|
| The General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms.The coefficient calculations happen in the controller.

The available filter types are:

-  Parametric (peaking equalizer)
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
-  Peaking (bandpass)
-  Notch (bandstop)
-  Chebyshev Low-Pass / High-Pass

**To open the filter control window, click on the icon button:**

| Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| |general2ndpic2.png|

--------------

| This block's algorithms use biquad filter designs(DF1) based on Robert Bristow-Johnson's work in this field.
| :math:`\displaystyle H(z)=b_0 + b_1 z^-1 + b_2 z^-\frac{2}{1} + a_1 z^-1 + a_2 z^-2`
| common variables:

-   :math:`omega_0 = 2 \pi f_0/F_s`
-   :math:`\displaystyle gainLinear = 10^\frac{gain}{20}`

| 
| |generalsecondorderfiltercoeffimage1.png|
| |generalsecondorderfiltercoeffimage2.png|
| Note that the b0 and b2 coefficients for the high pass filter below are inverted from what is stored in RAM. The correct equations for b0, b1, and b2 for a high pass filter are as follows:
| b0 = -(1 + cos(ω0)) \* gainLinear / 2
| b1 = -(1 + cos(ω0)) \* gainLinear
| b2 = -(1 + cos(ω0)) \* gainLinear / 2
| |image1|
| **Note that the minus signs on b0 and b2 values are erroneous for the Butterworth HP and Bessel HP. They should not be included. See** http://ez.analog.com/message/4769

| |general2ndpic6.png|
| For all of the above filters, the coefficients are divided by a0, normalizing them and making a0 = 1 so that only 5 coefficients must be stored. In the actual implementation on the DSP, when the coefficients are stored in parameter RAM, a1 and a2 need to be inverted. SigmaStudio performs this operation automatically, in software, before the parameters are written to DSP memory. Microcontrollers must invert a1 and a2 before writing new coefficients to DSP memory.

By default, the Q is shown with the value adjusted (from the classical EE definition) so that a boost of N dB followed by a cut of N dB for identical Q and f0/Fs results in a precisely flat unity gain filter or "wire". This is equal to A*Q, where A = 10^(dBgain/40).

.. image:: https://wiki.analog.com/_media/classicqcontrol.jpg
   :alt: classicqcontrol.jpg

The "Classic EQ" version of Q can optionally be shown by clicking the small circular button next to the Q control.

.. image:: https://wiki.analog.com/_media/classicqdisplay.jpg
   :alt: classicqdisplay.jpg

2.Coefficient Calculations on DSP
---------------------------------

The General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms.The coefficient calculations happen in the controller.

The available filter types are:

-  Parametric (peaking equalizer)
-  Shelving
-  General High-Pass
-  General Low-Pass
-  General Band-Pass
-  General Band-Stop
-  Butterworth Low-Pass / High-Pass
-  Bessel Low-Pass / High-Pass
-  All-pass
-  Peaking (bandpass)
-  Notch (bandstop)
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
.. |generalsecondorderfiltercoeffimage1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/generalsecondorderfiltercoeffimage1.png
.. |generalsecondorderfiltercoeffimage2.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/generalsecondorderfiltercoeffimage2.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/general2ndpic5edited.png
.. |general2ndpic6.png| image:: https://wiki.analog.com/_media/general2ndpic6.png
.. |filterconfigure.png| image:: https://wiki.analog.com/_media/filterconfigure.png
.. |filterconfiguretab.png| image:: https://wiki.analog.com/_media/filterconfiguretab.png
