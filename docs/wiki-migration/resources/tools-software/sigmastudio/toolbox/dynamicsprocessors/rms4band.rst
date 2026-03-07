| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ====== RMS 4 Band Compressor- Single Precision(ADAU145x) ====== |image1|
| RMS 4 band compressor is a multi-band compressor with 4 unique filter bands each with a unique compression curve and setting. The filter bands are configurable allowing the user to adjust the frequencies fed to each compression curve. Each compressor curve is individually configurable by means of a Graph and settings - attack, release hold and knee. The compression is applied by detecting the RMS value of the input signal and multiplying it with corresponding gain as set in the graph.
| |image2|

Input Pins
==========

+---------------------+------------------------------------------+-------------------------------+
| Name                | Format [int/dec/float] - [control/audio] | Function Description          |
+=====================+==========================================+===============================+
| Pin 0: Input Signal | decimal(ADAU145x)- audio\\\\             | Input signal to be compressed |
+---------------------+------------------------------------------+-------------------------------+

Output Pins
===========

+-----------------------+------------------------------------------+-----------------------+
| Name                  | Format [int/dec/float] - [control/audio] | Function Description  |
+=======================+==========================================+=======================+
| Pin 0: Compressor Out | decimal(ADAU145x)- audio- audio          | The compressor output |
+-----------------------+------------------------------------------+-----------------------+

Grow Algorithm
==============

| The module supports growth functionality. Add is not supported.
| ===== GUI Controls =====
| ^GUI Control Name^Default Value^Range^Function Description^

+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| corner frequency low          | 40Hz                 | 10-10000Hz     | cross over frequency at the intersection of the lowpass band and midband1                           |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| corner frequency mid          | 600Hz                | 10-10000Hz     | cross over frequency at the intersection of the midbands                                            |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| corner frequency high         | 8000Hz               | 10-10000Hz     | cross over frequency at the intersection of the highpass band and midband2                          |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| Filter Type                   | 0(linkwitz riley 24) | 0-10           | filter type (linkwitz, butterworth, Bessel)                                                         |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| Link channels                 | disabled             | enable/disable | links cross channel rms gains                                                                       |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| attack                        | 72 ms                | 1- 500 (ms)    | attack time, time in which compression kicks in when the input crosses the threshold                |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| hold                          | 72 ms                | 1- 500 (ms)    | hold time                                                                                           |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| release                       | 868 ms               | 1- 2000 (ms)   | release time, time in which the compression is deactivated when the input falls below the threshold |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| knee                          | 1                    | 1-75           | softness of the compression kicking in determined by the knee                                       |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| indicator                     | disable              | enable/disable | enables or disable the gain display meters                                                          |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| compression curve             | -                    | -              | enables the user to define the compression curve by moving the points on the curve along the graph  |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| Channel display               | 0                    | 0-7            | displays the level meters for the selected channel                                                  |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| band select                   | 0                    | 0-3            | displays the compression bands                                                                      |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| pregain                       | 0                    | -90 to 6dB     | pre-gain for each compressor curve                                                                  |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+
| level indicators(out,in,comp) | -                    | -              | displays the input output and applied gain levels                                                   |
+-------------------------------+----------------------+----------------+-----------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                | Function Description                                                                                 |
+==================+==============================================+======================================================================================================+
| tc_n             | RMS4BandCompS300Alg1tc_n(ADAU145x)           | attack time (there are n values for n curves)                                                        |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| hold_n           | RMS4BandCompS300Alg1hold_n(ADAU145x)         | hold time(there are n values for n curves)                                                           |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| decay_n          | RMS4BandCompS300Alg1decay_n(ADAU145x)        | release time(there are n values for n curves)                                                        |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| B1_1             | RMS4BandCompS300Alg1B1_1(ADAU145x)           | all pass coefficients (3 sets of first order filters) (b1,b0,a1), there are 9 coefficients in total. |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| points_n         | RMS4BandCompS300Alg1points_n(ADAU145x)       | Table containing gain points array from compressor curve graph                                       |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| B2_filterIndex   | RMS4BandCompS300Alg1B2_filterIndex(ADAU145x) | B2 IIR filter coefficient of the filter band                                                         |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| B1_filterIndex   | RMS4BandCompS300Alg1B1_filterIndex(ADAU145x) | B1 IIR filter coefficient of the filter band                                                         |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| B0_filterIndex   | RMS4BandCompS300Alg1B0_filterIndex(ADAU145x) | B0 IIR filter coefficient of the filter band                                                         |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| A2_filterIndex   | RMS4BandCompS300Alg1A2_filterIndex(ADAU145x) | A2 IIR filter coefficient of the filter band                                                         |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+
| A1_filterIndex   | RMS4BandCompS300Alg1A1_filterIndex(ADAU145x) | A1 IIR filter coefficient of the filter band                                                         |
+------------------+----------------------------------------------+------------------------------------------------------------------------------------------------------+

Algorithm Description
=====================

| 
| The Algorithm implements a multiple band compressor, with the input being separated into various filter bands depending on the set corner frequencies. These filter inputs are fed into individual compressors with unique curves and settings for attack, release and hold times.The detected gain is multiplied with the individual filter outputs and summed to a single output.

Example
=======

| 
| The example shows The module configured to a single input, single output configuration. The input is a sine sweep, sweeping linearly from 50Hz to 20kHz. The multiband compressor bands are configured to provide compression of 12db,0db,5dB and 30dB at an input level of 0dB.
| |image3|
| |image4|
| |image5|

Supported IC's
==============

| 1. ADAU145x

.. hint::

   Note: The module uses single precision filters due to which the accuracy of the module is limited at low amplitude levels of input data


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/multibandcompressor_treetoolbox.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/multiband_compressor_gui.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/example_multiband_comp1.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/example_multiband_comp2.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/120-5-30_multiband_comp.png
