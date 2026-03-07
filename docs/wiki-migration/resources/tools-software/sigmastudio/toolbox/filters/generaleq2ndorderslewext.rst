General Eq (2nd order) Slew Ext-(ADAU145x)
==========================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |image1|
| The General (2nd-Order)Slew Ext block gives access to a wide variety of 2nd-order (biquad)filter algorithms. The Slew time can be input to the module using the external control pin in seconds (0-1) to slew from the initial set of coefficients to the target value when any filter parameter is changed.

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

| The slewing functionality is added for smooth transition from one set of filter coefficients to another when the filter parameters are changed. The slewing takes place approximately in the slew time set by the user. The slew time can be set by providing the value :math:`\lambda` to the control pin. The parameter :math:`\lambda` determines the slew rate. Upon growing the number of filter stages, a new control pin is added to the module for :math:`\lambda` value for each stage. The slew computation is always performed in single precision.
| **To open the filter control window, click on the icon button:** Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| |image2|

--------------

| This block's algorithms use biquad filter designs (:ez:`Direct Form I <message/16011#16011>`) based on Robert Bristow-Johnson's work in this field.
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
| :math:`Slew function:`
| :math:`\lambda= e^{-1/{timeconstant \times F_s}}`
| :math:`Current Coefficient= Current Coffcicient \times \lambda + Target Coefficient \times (1-\lambda)`
| The above slewing function implements RC slewing. The parameter :math:`\lambda` is calculated based on the slewing time constant. The computations for slewing of filter coefficients is done on the DSP.
| For all of the above filters, the coefficients are divided by a0, normalizing them and making a0 = 1 so that only 5 coefficients must be stored. In the actual implementation on the DSP, when the coefficients are stored in parameter RAM, a1 and a2 need to be inverted. This is done automatically, in software, before the parameters are written to memory.

The Q is shown with the value adjusted (from the classical EE definition) so that a boost of N dB followed by a cut of N dB for identical Q and f0/Fs results in a precisely flat unity gain filter or "wire". This is equal to A\*Q, where A = 10^(dBgain/40).

*Note:* Some of the General 2nd order filters (those in the Type2 tree) are based on the Direct Form II implementation, which is used in the following HW ADSP-215xx & SC5xx. Please see the image below.

.. image:: https://wiki.analog.com/_media/Type2supportfor SHARCModules.png
   :alt: Type2supportfor SHARCModules.png

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/generaleqslewext1.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/generaleqslewext2.png
   :width: 200px
.. |general2ndpic4.png| image:: https://wiki.analog.com/_media/general2ndpic4.png
.. |general2ndpic5.png| image:: https://wiki.analog.com/_media/general2ndpic5.png
.. |general2ndpic6.png| image:: https://wiki.analog.com/_media/general2ndpic6.png
