| :doc:`Click here to return to the filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

Tracking Filter(ADSP-SC5xx/215xx)
=================================

| 
| Tracking Filters are useful for dynamic shifting of filtering. The tracking filter allows for the centre frequency to be determined by an external input.
| |image1|
| ====Input Pins====

+----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description                                                                                         |
+======================+====================================+==============================================================================================================+
| Pin 0: Input         | decimal - Audio                    | Audio Input                                                                                                  |
+----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Pin 1: Control Input | decimal - Control                  | Control Input (should be (2\*fc)/fs, where fc is the centre frequency and fs is the Schematic Sampling Rate) |
+----------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------+

| 
| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Filtered Output
============= ================================== ====================

| 
| ==== Grow Algorithm ==== The module does not support Add and Growth.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

====== ==== ============= ============================
Gain   0    -15dB to 15dB Gain of the filter in DB
QValue 0.04 0.04 to 16    Quiscent value of the filter
Boost  0dB  -15dB to 15dB Filter boost value in DB
====== ==== ============= ============================

| 
| ====DSP Parameter Information====

+------------------+-----------------------------------------------------------------------------------+------------------------------+
| GUI Control Name | Compiler Name                                                                     | Function Description         |
+==================+===================================================================================+==============================+
| Gain             | <fc #008000>TrackingFilter_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Gain</fc>   | Gain of the filter in DB     |
+------------------+-----------------------------------------------------------------------------------+------------------------------+
| QValue           | <fc #008000>TrackingFilter_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>QValue</fc> | Quiscent value of the filter |
+------------------+-----------------------------------------------------------------------------------+------------------------------+
| boost            | <fc #008000>TrackingFilter_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>boost</fc>  | Filter boost value in DB     |
+------------------+-----------------------------------------------------------------------------------+------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== Tracking Filters are useful for dynamic shifting of filtering. The tracking filter allows for the centre frequency to be determined by an external input.Control Input is calculated as (2\*fc)/fs, where fc is the centre frequency and fs is the Schematic Sampling Rate
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

| 
| ======Tracking(ADAU145x)======

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |trackingpic1.png| Tracking Filters are useful for dynamic shifting of filtering. This particular tracking Filter is a Peaking Filter algorithm. In many applications rather than having a fixed center frequency for a Peaking filter, it would be useful to have a moving center frequency. For example a LFO (low-frequency oscillator) could drive a Tracking Filter in order to produce a phasing audio effect. The tracking filter allows for the center frequency to be determined by an external input.

Input Pins:
-----------

There are two inputs and one output to the tracking filter block. The first input is the actual audio input that you want to filter. The second input pin is the value of the center frequency of the filter. You will notice that this pin is orange, denoting that it is a control pin and not an audio pin. Here you can connect LFOs or DC input blocks to designate the desired fixed or moving center frequency of the tracking filter.

Algorithm Description:
----------------------

The Tracking Filter is a unique filter in the SigmaStudio Filter library. It is one of the only filters in which the coefficients are calculated dynamically by the DSP processor. The equations are embedded in the block's algorithm code, and depending on the input center frequency, the coefficients are then generated.

The input center frequency that the tracking filter algorithm is expecting, is a 5.23 data format value, computed by: Hz/(fs/2). For example if you are operating at fs = 44100 Hz and you have an fc = 500 Hz the value being sent should be: 0.0226757 = 500 /(44100/2).

The Tracking Filter is based on the coefficient generation for an IIR Peaking Filter. The following equations show how the DSP attains the 5 biquad coefficients from the controls. The controls of the tracking filter are overall_gain which is the dB value of the overall gain of the filter, boost which is the dB value of the cut or boost of the Peaking filter, and Q which determines the width of the frequency cut or boost. The center frequency fc of the Peaking Filter is given by the second input pin.

gainLinear = 10^(overall_gain/20) w = 2\*pi\*fc/Fs alpha = sin(w)/(2\*Q) A = 10^(boost/40) a0 = 1 + alpha/A a1 = -2 \* cos(w) a2 = 1 - alpha/A b0 = (1 + alpha\*A) \* gainLinear b1 = -(2 \* cos(w)) \* gainLinear b2 = (1 - alpha\*A) \* gainLinear

Usage:
------

The tracking filter can be used in many situations. It should be used when a changing center frequency to a peaking filter is desired. For fixed center frequency applications you should use a general second order filter. There is a lot of overhead in MIPS/Memory in order for the changing center frequency to be supported for this algorithm. However, the first example here using the tracking filter has a fixed center frequency just for ease in explaining the format of the center frequency.

--------------

Example 1:
----------

| Here a DC entry block is connected to the second pin of the tracking filter. The value inside the block corresponds to 500Hz. Thus the audio coming in on the first pin will be boosted 5dB at 500Hz with a Q of 1.71, and an overall gain adjustment of -3dB will be applied over the entire frequency range.
| |trackingpic2.png|

Example 2:
----------

Here is a more complex example showing how the tracking filter can be used with a LFO to create a phasing effect. The first input pin is receiving a merged version of the input signal (essentially a mono version of the input signal). The blocks preceding the second input pin create a LFO that sweeps the center frequency at a rate of .1Hz. The range of the sweeped center frequency is 441 – 11025 Hz.

These are the equations explaining how the range is determined:

Fc control input = (F2 – F1)*sin(.1Hz) + F2 + F1

Since a normal sine tone ranges from ±1, this LFO ranges from:

+(F2-F1) + F2 + F1 = 2\*F2 -(F2-F1) + F2 + F1 = 2\* F1

Then to figure out what the frequencies are in Hz corresponding to .01 and .25 in the schematic use the following formula:

(44100/2) \* Fc = Value in Hz

Keep in mind though that F1 and F2 are the numbers in the DC block, but the range will go from 2\*F1 to 2\*F2, so first multiply by 2 to get the correct range value, then use the above formula to find out the value in Hz:

| (0.01\*2)*44100/2 = 441 Hz (0.25\*2)*(44100/2) = 11025 Hz
| |trackingpic3.png|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/trackingfilter-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/trackingfilter-gui.jpg
.. |trackingpic1.png| image:: https://wiki.analog.com/_media/trackingpic1.png
.. |trackingpic2.png| image:: https://wiki.analog.com/_media/trackingpic2.png
.. |trackingpic3.png| image:: https://wiki.analog.com/_media/trackingpic3.png
