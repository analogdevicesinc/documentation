Limiter
=======

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ----------------------------------------------------------------------------------------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| The limiter tracks the RMS level of an incoming audio signal and attempts to prevent it from exceeding a user-defined threshold by automatically reducing its gain. | |limiterpic1.png| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+

Input Pins
----------

+--------------------+------------------------------------+-----------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description        |
+====================+====================================+=============================+
| Pin 0: Audio Input | dec - audio                        | Audio signal to be limited. |
+--------------------+------------------------------------+-----------------------------+

Output Pins
-----------

.. warning::

   As of SigmaStudio 4.7, Pin 2 is labeled "Limter ratio" but is actually the limiter active flag, while Pin 3 is labeled Limiter Active Flag but is actually the limiter ratio.


+----------------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                       | Format [int/dec] - [control/audio] | Function Description                                                                                                                                                                                      |
+============================+====================================+===========================================================================================================================================================================================================+
| Pin 1: Audio Output        | dec - audio                        | Limited audio output signal.                                                                                                                                                                              |
+----------------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pin 2: Limiter Ratio       | dec - control                      | Value representing the current gain factor being applied to the audio signal.                                                                                                                             |
+----------------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pin 3: Limiter Active Flag | int - control                      | Flag outputting a 1 if the limiter is active, or a 0 if the limiter is not active. This essentially shows if the input signal has exceeded the threshold or not. The number is an unsigned integer format |
+----------------------------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

GUI Controls
------------

+------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range      | Function Description                                                                                                                                                                                                                                                                                                                                                                   |
+==================+===============+============+========================================================================================================================================================================================================================================================================================================================================================================================+
| RMS TC (dB/s)    | 50            | 1 to 10000 | Controls the tracking rate of the RMS-approximation calculation used to track the input level.                                                                                                                                                                                                                                                                                         |
+------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (dB/s)     | 12            | 5 to 23    | Controls the rate at which the signal compression ratio will subside after the input signal level has dropped below the limiter threshold. Larger values result in longer decays, with 23 never recovering to the original gain.                                                                                                                                                       |
+------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Threshold (dB)   | 0             | -24 to 24  | Sets the threshold point. If the input signal's approximated RMS level exceeds the threshold point, the limiter will apply compression in order to prevent the signal from exceeding that level. This threshold level does not need to be an integer; its resolution can be set in steps of less than 0.01 dB. A full-scale sine wave is a level of -3 dB, due to the RMS measurement. |
+------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+----------------------------+---------------------------------------------------------+
| GUI Control Name | Compiler Name              | Function Description                                    |
+==================+============================+=========================================================+
| N/A              | limiterAlg1slope_1         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1inter_1         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1slope_2         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1inter_2         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1slope_3         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1inter_3         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1slope_4         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1inter_4         | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1comp_1          | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1comp_2          | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| N/A              | limiterAlg1comp_3          | Internal parameter. Do not modify.                      |
+------------------+----------------------------+---------------------------------------------------------+
| Threshold (dB)   | limiterAlg1threshold       | The limiter threshold, in decimal format.               |
+------------------+----------------------------+---------------------------------------------------------+
| RMS TC (dB/s)    | limiterAlg1RMS_MONO_TCONST | The time constant of the RMS approximation calculation. |
+------------------+----------------------------+---------------------------------------------------------+
| Decay (dB/s)     | limiterAlg1decay           | The decay value.                                        |
+------------------+----------------------------+---------------------------------------------------------+
| Decay (dB/s)     | limiterAlg1decaycomplement | The complement of the decay value.                      |
+------------------+----------------------------+---------------------------------------------------------+

Algorithm Description
---------------------

The Limiter block is an extreme compressor, completely preventing signals from exceeding the threshold. Whenever the level signal starts to go above it, the limiter immediately stops it and keeps it at threshold.

This block can control the detected rms value and attack-time constant (TC), as well as the processor's decay.

| The following graph shows the input/output relationship for a 1kHz tone with 6dB-increments thresholds.
| |limiterpic2.png|
| Signal output is computed according to the following formula:
| |limiterpic3.png|
| Signals below threshold remain unaffected; those above it are attenuated by the firm ratio shown above.

In the block figure, top right, the blue pin outputs the dynamically limited input signal. The second red pin (bottom of three pins) outputs ZERO (a flag) when the rms value of the input is below threshold. If the rms value exceeds the threshold, it will output ONE, giving you the option to read whether the limiter is active.

The first red pin (middle of the three pins) outputs the instantaneous-limiting ratio, and you can use this value to derive the compressed signal by employing a multiplier block to measure the signal envelope and the input. Compressed-signal displays are widely used in professional audio equipment.

Calculating Parameter Values
----------------------------

The equations for the limiter parameters are:

**RMS dB/s value stored in RAM** = abs(1.0 - 10^(rms/10\*fs)), where "rms" is the value entered in the block and "fs" is the sample rate in Hz.

**Decay dB/s Value stored in RAM** = (fs / 26373 \* Decay), where "Decay" is the value entered in the block.

**Decay complement value store in RAM** = 1.0 - 2^(-1.0*(23 + DecayRAM)), where "DecayRAM" is the value calculated in the previous formula.

The decay complement is only used to determine the flag output of the limiter and is not used in the limiting processing.

**Note:** For Griffin/Sharc processors, decay = Math.Pow(10, (double)decay / (fs + 0.000001) / 10), where "Decay" is the value entered in the block and "fs" is the sample rate in Hz.

Example
-------

For a sample design using this block, see the :doc:`Dynamics Processor Example </wiki-migration/resources/tools-software/sigmastudio/tutorials/dynamicsprocessorexamples>`.

Here is a screenshot showing the use of the cell:


|image1|

Here is a screenshot of its location in the Tree Toolbox:


|image2|

Algorithm Details
-----------------

+---------------------------------------+-------------------------------------+
| Toolbox Path                          | Dynamics Processors - RMS - Limiter |
+---------------------------------------+-------------------------------------+
| Cores Supported                       | AD194x                              |
|                                       | ADAU170x                            |
|                                       | ADAU144x                            |
|                                       | ADAU176x                            |
|                                       | ADSP214xx                           |
|                                       | ADSP 215xx                          |
|                                       | ADSP-SC5xx                          |
+---------------------------------------+-------------------------------------+
| "Grow Algorithm" Supported            | no                                  |
+---------------------------------------+-------------------------------------+
| "Add Algorithm" Supported             | no                                  |
+---------------------------------------+-------------------------------------+
| Subroutine/Loop Based                 | no                                  |
+---------------------------------------+-------------------------------------+
| Program RAM (ADAU144x and ADAU176x)   | 77                                  |
+---------------------------------------+-------------------------------------+
| Data RAM (ADAU144x and ADAU176x)      | 13                                  |
+---------------------------------------+-------------------------------------+
| Parameter RAM (ADAU144x and ADAU176x) | 15                                  |
+---------------------------------------+-------------------------------------+

.. |limiterpic1.png| image:: https://wiki.analog.com/_media/limiterpic1.png
.. |limiterpic2.png| image:: https://wiki.analog.com/_media/limiterpic2.png
.. |limiterpic3.png| image:: https://wiki.analog.com/_media/limiterpic3.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/screenhunter_711_dec._01_09.18.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/screenhunter_712_dec._01_09.19.jpg
   :width: 200px
