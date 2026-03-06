Standard Independent Peak
=========================

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| --------------------------------------------------------------------------------------------------------------

+---+---+
| The Standard Peak Compressor is a stereo compressor that allows direct control over threshold and ratio. In the pop-up GUI, graphical controls are given for threshold, ratio, and time constants. Also there are visual indicators showing input, output, and compression levels. The detection signals used for this Peak compressor, are independent for L and R channels. The detection signal can be linked in which case the greater signal of L or R will drive the compression. | |standardindpic1.png| |
+---+---+

Input Pins
----------

+----------------------+------------------------------------+---------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description      |
+======================+====================================+===========================+
| Pin 0: Audio Input L | decimal - audio                    | Left Channel audio input  |
+----------------------+------------------------------------+---------------------------+
| Pin 1: Audio Input R | decimal - audio                    | Right Channel audio input |
+----------------------+------------------------------------+---------------------------+

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
| |standardindpic2.png|

GUI Control
-----------

+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name   | Default Value | Range      | Function Description                                                                                                                                                                                                     |
+====================+===============+============+==========================================================================================================================================================================================================================+
| Threshold (dB)     | 0             | -96        | Controls the threshold point of compression/expansion.                                                                                                                                                                   |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Compressor         | 100           | 100 - 1    | Controls the ratio of Compression. The number selected in this box is interpreted as the ratio N:1 for compression above the threshold point.                                                                            |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Expander           | 1             | 100 - 1    | Controls the ratio of Downward Expansion. The number selected in this box is interpreted as the ratio N:1 for downward expansion below the threshold point.                                                              |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Knee               | 1             | 1 - 100    | Controls the hard/soft knee relationship of the curve. A knee allows a more gradual calculation of the curve around the threshold point, with "1" being a hard knee, and "100" being the softest.                        |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input Gain (dB)    | 0             | -96        | Controls a gain that is applied to both Left and Right prior to the compression. Allows for the curve to be shifted left and right.                                                                                      |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack (ms)        | 72            | 1- 500     | Controls the amount of time before the compressor reacts to an input signal that has exceeded the threshold point.                                                                                                       |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)          | 0             | 0 - Attack | Controls the amount of time the compression level is held before reacting to a new change in input signal level. The max hold time is limited to the Attack time setting.                                                |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release (ms)       | 868           | Jan-00     | Controls the amount of time before the compressor reacts to an input signal that has dropped below the threshold point.                                                                                                  |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LINK Both Channels | unchecked (0) | 0 - 1      | Turns the LINK capability on or off. When the algorithm is UNLINKED, the compression is independent for Left and Right Channels. When the algorithm is LINKED, whichever channel is greater, will drive the compression. |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Level Indicators   | off           | on/off     | Turns the Indicators on or off. There is no DSP function associated with this.                                                                                                                                           |
+--------------------+---------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP parameter Information
-------------------------

+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name   | Compiler Name                        | Function Description                                                                                                                                            |
+====================+======================================+=================================================================================================================================================================+
| Threshold          | StdPeakCompressorAlgIndp1            | When the Threshold, Compressor, Expander, or Knee values are changed, 34 parameters are written to the DSP to represent the gain curve displayed in the window. |
| Compressor         |                                      |                                                                                                                                                                 |
| Expander           |                                      |                                                                                                                                                                 |
| Knee               |                                      |                                                                                                                                                                 |
+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input Gain         | StdPeakCompressorAlg1Indpattenuation | When the Input Gain is changed, the dB value is converted to linear and written to the DSP.                                                                     |
+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack             | StdPeakCompressorAlg1IndpPeak        | When the Attack time is changed, a new value is calculated and written to the DSP to control the reaction time.                                                 |
+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold               | StdPeakCompressorAlg1Indphold        | When the Hold time is changed, a new value is calculated and written tot he DSP to control the hold time.                                                       |
+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay              | StdPeakCompressorAlg1Indpdecay       | When the Decay time is changed, a new value is calculated and written to the DSP to control the reaction time.                                                  |
+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LINK Both Channels | StdPeakCompressorAlg1Indplinked      | When the LINK is selected on/off, a boolean value is written to the DSP to determine how to execute sections of code for this behavior.                         |
+--------------------+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The Standard Independent Peak Compressor is meant to function like most other SimgaStudio peak compressors. The performance and main algorithm driving the Standard Peak is the same as the other compressors in the same library folder (Peak - Standard Resolution - Lower Range). The main differences are outlined here:

-  Compression Curve control over threshold and ratio vs. 33 customizable points
-  Attack/Decay time constant control in (ms) vs. (dB/s)
-  Visual Indicators of Input, Output, and Compression levels vs. no visual indicators
-  Fine Tune controls of Knee vs. Soft/Hard boolean control
-  Linked/Unlinked detection vs. Ext/No Ext Detection method\*

\*The detection method for this algorithm is unique to this algorithm and differs from the other compressors in the same library folder. Independent monitoring is done for the left and right channels. Thus a detection signal is generated for both left and right channels. Depending on whether the algorithm is linked or unlinked, will have different behavior in terms of how the output gains are selected for left and right. The ability to have the linked/unlinked behavior is a real-time control.

**Unlinked:**

The detection signals for left and right will independently drive the gain curve. Both channels follow the same curve, but depending on the detection level, different gains will be selected from the curve to be applied for left and right.

**Linked:**

The detection signals for left and right will be compared. The larger of the two detection signals will be used to drive the gain curve. Thus the same gain compensation will be used for left and right.

If an average between left and right channels is desired for the detection method, the Standard Peak compressor should be used.

Example
-------

| This is an example of the compressor being used directly on the input signal. The compressor is connected to an external Volume Control for a post gain level before sending to the outputs.
| |standardindpic3.png|

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------------------------+
| Toolbox Path               | Peak - Standard Resolution - Lower Range - Standard Independent Peak |
+----------------------------+----------------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                             |
|                            | ADAU176x                                                             |
|                            | ADAU178x                                                             |
+----------------------------+----------------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Program RAM                | 119                                                                  |
+----------------------------+----------------------------------------------------------------------+
| Data RAM                   | 45                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Parameter RAM              | 46                                                                   |
+----------------------------+----------------------------------------------------------------------+

.. |standardindpic1.png| image:: https://wiki.analog.com/_media/standardindpic1.png
.. |standardindpic2.png| image:: https://wiki.analog.com/_media/standardindpic2.png
.. |standardindpic3.png| image:: https://wiki.analog.com/_media/standardindpic3.png
