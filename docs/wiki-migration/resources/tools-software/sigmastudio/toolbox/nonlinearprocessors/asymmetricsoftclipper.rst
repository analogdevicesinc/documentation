Asymmetric soft clipper
=======================

| 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


| The Asymmetric soft clipper block is a soft clipper that clips the level of the input signal asymmetrically according to the set clipping thresholds. As the input signal reaches the clip threshold at either ends, the algorithm rounds the edges for a smoother clipped output. |

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| The module supports two algorithms:
| 1.Standard Cubic Clip
| 2.Advanced Clip
| |image1|

Input Pins
----------

+--------------+------------------------------------+----------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description       |
+==============+====================================+============================+
| Pin 0: Input | decimal - audio                    | Input signal to be clipped |
+--------------+------------------------------------+----------------------------+

Output Pins
-----------

============= ================================== =======================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== =======================
Pin 0: Output decimal - audio                    The soft-clipped output
============= ================================== =======================

GUI Controls
------------

| 
| ====1.Standard Cubic clipper====

+------------------+---------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range  | Function Description                                                                                                                                                                                                                                                          |
+==================+===============+========+===============================================================================================================================================================================================================================================================================+
| Clip up          | 1             | 0.1-10 | This pre/post scalar determines the amount of clipping that will occur at the positive part of the input signal. Although this influences the threshold value of the clipper, this is not the value at which clipping occurs. [See the function in the Algorithm Description] |
+------------------+---------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Clip down        | 1             | 0.1-10 | This pre/post scalar determines the amount of clipping that will occur at the negative part of the input signal. Although this influences the threshold value of the clipper, this is not the value at which clipping occurs. [See the function in the Algorithm Description] |
+------------------+---------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ====2.Advanced clipper====

+------------------+---------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range   | Function Description                                                                                                                                                                                                                                                          |
+==================+===============+=========+===============================================================================================================================================================================================================================================================================+
| Clip up          | 1             | 0.1-0.9 | This pre/post scalar determines the amount of clipping that will occur at the positive part of the input signal. Although this influences the threshold value of the clipper, this is not the value at which clipping occurs. [See the function in the Algorithm Description] |
+------------------+---------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Clip down        | 1             | 0.1-0.9 | This pre/post scalar determines the amount of clipping that will occur at the negative part of the input signal. Although this influences the threshold value of the clipper, this is not the value at which clipping occurs. [See the function in the Algorithm Description] |
+------------------+---------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

1.Standard Cubic
~~~~~~~~~~~~~~~~

+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name        | Function Description                                                                                                                                                                                    |
+==================+======================+=========================================================================================================================================================================================================+
| Alpha1           | SoftClipAlg1alpha1   | When the Clip up value is changed in the GUI window, two parameters are downloaded to the DSP. The alpha1 value is written directly to the DSP as well as the inverse 1/alpha1 is written to the DSP.   |
|                  | SoftClipAlg1alpha1m1 |                                                                                                                                                                                                         |
+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Alpha2           | SoftClipAlg1alpha2   | When the Clip down value is changed in the GUI window, two parameters are downloaded to the DSP. The alpha2 value is written directly to the DSP as well as the inverse 1/alpha2 is written to the DSP. |
|                  | SoftClipAlg1alpha2m1 |                                                                                                                                                                                                         |
+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Note: There are other fixed parameters used for this algorithm, but they do not need to be updated when the alpha value is changed.
| ====2.Advance Clip====

+------------------+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name            | Function Description                                                                                                                                                                                     |
+==================+==========================+==========================================================================================================================================================================================================+
| tau1             | SoftClipAlg1tau1         | When the Clip up value is changed in the GUI window, two parameters are downloaded to the DSP. The tau1 value is written directly to the DSP as well as 1/(1-tau1) and (1-tau1) is written to the DSP.   |
|                  | SoftClipAlg1onemtau1     |                                                                                                                                                                                                          |
|                  | SoftClipAlg1inv_onemtau1 |                                                                                                                                                                                                          |
+------------------+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tau2             | SoftClipAlg1tau2         | When the Clip down value is changed in the GUI window, two parameters are downloaded to the DSP. The tau2 value is written directly to the DSP as well as 1/(1-tau2) and (1-tau2) is written to the DSP. |
|                  | SoftClipAlg1onemtau2     |                                                                                                                                                                                                          |
|                  | SoftClipAlg1inv_onemtau2 |                                                                                                                                                                                                          |
+------------------+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

.. _standard-cubic-1:

1.Standard Cubic
~~~~~~~~~~~~~~~~

| 
| The Standard Cubic block asymmetrically clips portions of signal voltages according to a cubic asymmetric soft clip function. The pre/post scalar alpha1 and alpha2 make the soft clip more or less severe. alpha1 sets the clipping threshold for the positive part of the input signal, whereas alpha2, sets the clipping threshold for the lower part of the input signal.This block limits the range of the output signal according to the following formulas:

| 
| :math:`Output = Alpha1 \times f(x), if x>0`
| :math:`Output = Alpha2 \times f(x), if x<=0`
| :math:`x= Input \times (1/Alpha1), if Input>0`
| :math:`x= Input \times (1/Alpha2), if Input<=0`

.. math::


   f(x)= -\frac{2}{3}, x<=-1;
   \\
   x-x^\frac{3}{3}, -1<x<1; 
   \\
   \frac{2}{3}, x>=1

| 
| Thus for the default value of Alpha1 = 1, Alpha2=1, the signal range will be from [-2/3, 2/3]. Changing the value of Alphas will affect the output range of the signal. The following graphs show the relationship between changing values of Alphas and obtaining different signal ranges.

Example
^^^^^^^

The following image shows the Soft Clipper, being compared to a Hard Clipper and also the direct signal coming from the Inputs.

| 
| |image2|
| The Hard Clipper and Soft Clipper are set with corresponding Alpha and threshold values so that their clip behavior occurs at the same time. However, you will notice in the following output comparison graph, the Soft Clipper has rounded smoother edges on the output where clipping begins to occur which has a more pleasing auditory effect.

| 
| |image3|

Algorithm Details
^^^^^^^^^^^^^^^^^

+----------------------------+----------------------------------------------------------------------------------------------+
| Toolbox Path               | Non Linear Processors - Clippers - Soft Clip -Asymmetric Cubic Clip- Asymmetric Soft clipper |
+----------------------------+----------------------------------------------------------------------------------------------+
| Cores Supported            | ADAU145x                                                                                     |
+----------------------------+----------------------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                                                       |
+----------------------------+----------------------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------------+

Algorithm Growth Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Description | When the SoftClip algorithm is grown, an extra pair of input/output pints is added to the control. The same Alpha parameter affects the clipping on grown Input pins. | |image5| |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

| 
| ==== 2.Advanced Clip ====
| The Advanced clip block asymmetrically clips portions of signal voltages according to a TanH asymmetric soft clip function. The pre/post scalar alpha1 and alpha2 make the soft clip more or less severe. alpha1 sets the clipping threshold for the positive part of the input signal, whereas alpha2, sets the clipping threshold for the lower part of the input signal.This block limits the range of the output signal according to the following formulas:

| 
| :math:`Output = Input, if |Input|<tau1 for Input>0, |Input|<tau2 for Input<0`
| :math:`\displaystyle Output = tau1 + (1 - tau1) \times tanh(\frac{abs(Input) - tau1}{1 - tau1}), if|Input|>=tau1 and Input>0`
| :math:`\displaystyle Output = -tau2 -(1 - tau2) \times tanh(\frac{abs(Input) - tau2}{1 - tau2}), if|Input|>=tau2 and Input<0`

| 
| Thus for the default value of tau1 = 0.5, tau2=0.5. Changing the value of taus will affect the output range of the signal.
| ===Example===
| The graph below shows an input sine tone and the resulting clipped output with threshold values at: Clip Up: 0.8 Clip Down: 0.2
| |image6|
| === Algorithm Details ===

+----------------------------+-------------------------------------------------------------------------------------------------+
| Toolbox Path               | Non Linear Processors - Clippers - Soft Clip -Asymmetric Advanced Clip- Asymmetric Soft clipper |
+----------------------------+-------------------------------------------------------------------------------------------------+
| Cores Supported            | ADAU145x                                                                                        |
+----------------------------+-------------------------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                                                          |
+----------------------------+-------------------------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                                              |
+----------------------------+-------------------------------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                                              |
+----------------------------+-------------------------------------------------------------------------------------------------+

.. _algorithm-growth-information-1:

Algorithm Growth Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Description | When the SoftClip algorithm is grown, an extra pair of input/output pints is added to the control. The same Alpha parameter affects the clipping on grown Input pins. | |image8| |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/asymm0.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/asymmschema0.png
   :width: 450px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/asymmclip3.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic006.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic006.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/datagraph.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic006.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic006.jpg
