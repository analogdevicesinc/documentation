Standard Peak
=============

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| --------------------------------------------------------------------------------------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| The Standard Peak Compressor is a stereo compressor that allows direct control over threshold and ratio. In the pop-up GUI, graphical controls are given for threshold, ratio, and time constants. Also there are visual indicators showing input, output, and compression levels. The detection signal used for this Peak compressor is based on the sum of Left and Right channels. | |standardpeakpic1.png| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+

Input Pins
----------

+----------------------+------------------------------------+---------------------------+---+
| Name                 | Format [int/dec] - [control/audio] | Function Description      |   |
+======================+====================================+===========================+===+
| Pin 0: Audio Input L | decimal - audio                    | Left Channel audio input  |   |
+----------------------+------------------------------------+---------------------------+---+
| Pin 1: Audio Input R | decimal - audio                    | Right Channel audio input |   |
+----------------------+------------------------------------+---------------------------+---+

Output Pins
-----------

+-----------------------+------------------------------------+---------------------------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description                  |
+=======================+====================================+=======================================+
| Pin 0: Audio Output L | decimal - audio                    | Left Channel compressed Audio Output  |
+-----------------------+------------------------------------+---------------------------------------+
| Pin 0: Audio Output R | decimal - audio                    | Right Channel compressed Audio Output |
+-----------------------+------------------------------------+---------------------------------------+

GUI Controls
------------

| \*The GUI Controls for this block exist on another window. Click on the Compressor icon to open the following Compressor window that contains the following Compressor controls:
| |standardpeakpic2.png|
| ^GUI Control Name^Default Value^Range^Function Description^

+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Threshold (dB)   | 0   | -96        | Controls the threshold point of compression/expansion.                                                                                                                                            |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Compressor       | 100 | 100 - 1    | Controls the ratio of Compression. The number selected in this box is interpreted as the ratio N:1 for compression above the threshold point.                                                     |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Expander         | 1   | 100 - 1    | Controls the ratio of Downward Expansion. The number selected in this box is interpreted as the ratio N:1 for downward expansion below the threshold point.                                       |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Knee             | 1   | 1 - 100    | Controls the hard/soft knee relationship of the curve. A knee allows a more gradual calculation of the curve around the threshold point, with "1" being a hard knee, and "100" being the softest. |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input Gain (dB)  | 0   | -96        | Controls a gain that is applied to both Left and Right prior to the compression. Allows for the curve to be shifted left and right.                                                               |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack (ms)      | 72  | 1- 500     | Controls the amount of time before the compressor reacts to an input signal that has exceeded the threshold point.                                                                                |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)        | 0   | 0 - Attack | Controls the amount of time the compression level is held before reacting to a new change in input signal level. The max hold time is limited to the Attack time setting.                         |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release (ms)     | 868 | Jan-00     | Controls the amount of time before the compressor reacts to an input signal that has dropped below the threshold point.                                                                           |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Level Indicators | off | on/off     | Turns the Indicators on or off. There is no DSP function associated with this.                                                                                                                    |
+------------------+-----+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                    | Function Description                                                                                                                                            |
+==================+==================================+=================================================================================================================================================================+
| Threshold        | StdPeakCompressorAlg1            | When the Threshold, Compressor, Expander, or Knee values are changed, 34 parameters are written to the DSP to represent the gain curve displayed in the window. |
| Compressor       |                                  |                                                                                                                                                                 |
| Expander         |                                  |                                                                                                                                                                 |
| Knee             |                                  |                                                                                                                                                                 |
+------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input Gain       | StdPeakCompressorAlg1attenuation | When the Input Gain is changed, the dB value is converted to linear and written to the DSP.                                                                     |
+------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack           | StdPeakCompressorAlg1Peak        | When the Attack time is changed, a new value is calculated and written to the DSP to control the reaction time.                                                 |
+------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold             | StdPeakCompressorAlg1hold        | When the Hold time is changed, a new value is calculated and written tot he DSP to control the hold time.                                                       |
+------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay            | StdPeakCompressorAlg1decay       | When the Decay time is changed, a new value is calculated and written to the DSP to control the reaction time.                                                  |
+------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The Standard Peak Compressor is meant to function like most other SigmaStudio peak compressors. The performance and main algorithm driving the Standard Peak is the same as the other compressors in the same library folder (Peak - Standard Resolution - Lower Range). The main differences are outlined here:

-  Compression Curve control over threshold and ratio vs. 33 customizable points
-  Attack/Decay time constant control in (ms) vs. (dB/s)
-  Visual Indicators of Input, Output, and Compression levels vs. no visual indicators
-  Fine Tune controls of Knee vs. Soft/Hard boolean control
-  Fixed Detection method vs. Ext/No-Ext Detection method \*

\*The Standard Peak Compressor is a stereo compressor with the detection method tied directly to the inputs. Thus the detection signal used to drive the compression is: Input Gain \* (L + R)/2. There is no choice for an external signal to drive the compression. This detection method is the same as selecting "No External Detection" on other compressors in the same library folder.

If independent control of the detection method is desired for compression, the Standard Independent Peak compressor should be used. This allows different functionality to link or unlink the detection method for left and right channels.

Example
-------

| This is an example of the compressor being used directly on the input signal. The compressor is connected to an external Volume Control for a post gain level before sending to the outputs.
| |standardpeakpic3.png|

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------------+
| Toolbox Path               | Peak - Standard Resolution - Lower Range - Standard Peak |
+----------------------------+----------------------------------------------------------+
| Cores Supported            | ADAU145x                                                 |
|                            | ADAU146x                                                 |
|                            | ADAU144x                                                 |
|                            | ADAU176x                                                 |
|                            | ADAU178x                                                 |
+----------------------------+----------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                       |
+----------------------------+----------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                       |
+----------------------------+----------------------------------------------------------+
| Subroutine/Loop Based      | no                                                       |
+----------------------------+----------------------------------------------------------+
| Program RAM                | 60                                                       |
+----------------------------+----------------------------------------------------------+
| Data RAM                   | 16                                                       |
+----------------------------+----------------------------------------------------------+
| Parameter RAM              | 43                                                       |
+----------------------------+----------------------------------------------------------+

.. |standardpeakpic1.png| image:: https://wiki.analog.com/_media/standardpeakpic1.png
.. |standardpeakpic2.png| image:: https://wiki.analog.com/_media/standardpeakpic2.png
.. |standardpeakpic3.png| image:: https://wiki.analog.com/_media/standardpeakpic3.png
