| :doc:`Click here to return to the Multirate processing page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multirateprocessing>`
| ====== Synchronous Sample Rate Converter(ADAU145x) ====== |image1|
| Synchronous SRC is a multi-rate processing module which interpolates or decimates the input signal sampled at the input signal to the desired signal at output sample rate. The module supports fractional (FSin/FSout) ratios. Currently the module supports conversion from 48KHz sample rate to 44.1KHz and vice versa.
| |image2|

Input Pins
==========

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal(ADAU145x)- audio                 | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

Output Pins
===========

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | decimal(ADAU145x)- audio- audio          | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
==============

| The module supports growth functionality, the number of channels to the module can be grown. Add is not supported.
| ===== GUI Controls =====
| ^GUI Control Name^Default Value^Range^Function Description^

+--------+----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| FS Out | 44.1 KHz | 44.1 KHz and 48KHz | Output sampling frequency, this is the sampling frequency at which the input signal at the input sampling frequency is re-sampled to |
+--------+----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Memory | DM0      | DM0/DM1            | Memory selection to which the filter coefficients are loaded to                                                                      |
+--------+----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

+------------------+------------------------+-----------------------------------+
| GUI Control Name | Compiler Name          | Function Description              |
+==================+========================+===================================+
| FilterCoeffs     | SRCS300AlgFilterCoeffs | interpolating filter coefficients |
+------------------+------------------------+-----------------------------------+
| constants        | SRCS300Algconstants    | constants used in the algorithm   |
+------------------+------------------------+-----------------------------------+

Algorithm Description
=====================

| 
| The Algorithm implements a Sample rate converter, which takes the input signal sampled at the input sample rate and outputs the signal at the desired output sample rate. The algorithm interpolates between the samples of the signal at the input sample rate and resamples it at the output sampling rate.

Example
=======

| 
| ==== Up sampling ====
| The module acts as an upsampler when the output sample rate is greater than the input sample rate. The following example interpolates the input signal which is a sine tone of 500Hz sampled at 44.1 KHz to an output sine tone at 500Hz sampled at the output sampling frequency of 48KHz. Here tone1_2 is set to a sampling rate of 44.1khz and tone1_3 is set to a sampling rate of 48khz.
| |image3|
| ==== Down sampling ====
| The module acts as an down sampler when the input sample rate is greater than the output sample rate. The following example interpolates the input signal which is a sine tone of 800Hz sampled at 48 KHz to an output sine tone at 800Hz sampled at the output sampling frequency of 44.1KHz. Here tone1_2 is set to a sampling rate of 48khz tone1_3 is set to a sampling rate of 44.1khz.
| |image4|
|

.. note::

   Note: The output pins of the Sample rate converter must always be connected. If the module is placed at the end of the signal chain, connect the output pins to the output modules.


Down sampling - Up sampling
---------------------------

| 
| The below figure shows a signal chain containing the SRC module which down samples the input signal sampled at 48KHz to an output signal at 44.1KHz which is fed to a gain module which multiplies the input with the gain value. The processing here happens at 44.1 KHz, the processed signal is then fed to the SRC module which Up samples the signal back to 48KHz. This allows the processing to take place at different rate than that of the original input signal.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/src_example3.png
   :align: center

| 
| ===== Supported IC's===== 1. ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/src_tree_toolbox.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/src_cell.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/src_example1.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/src_example2_schema.png
   :width: 400px
