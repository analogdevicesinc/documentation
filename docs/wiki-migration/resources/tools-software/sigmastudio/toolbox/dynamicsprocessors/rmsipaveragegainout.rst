:doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`

RMS Input Average Compressor
============================

This Module computes the Gain of the Compressor. Compression happens by taking the RMS of the Average of all inputs, and then looking up for the Gain based on the Compressor Graph.


|image1|

Input Pins
----------

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Audio Input
============ ================================== ====================


| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Gain Output
============= ================================== ====================


| ==== Grow Algorithm ==== The module supports Input Channel growth upto a maximum of 6 channels.

Configuration
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rmsipaveragecompressorconfig.png
   :width: 600px

Compressor graph has a "Point Density" context menu option for varying the resolution of the Points in the compressor graph. 288(0.5db), 720(0.2db) and 1440(0.1db) are the Point densities supported.

+------------------+---------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description                                                                                                                        |
+==================+===============+===============+=============================================================================================================================================+
| RMSTC            | 121           | 1 – 8686 db/s | Determines how rapidly the compressor will respond to input signal level changes                                                            |
+------------------+---------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Hold             | 0             | 0-2000        | Controls the time (in ms) the compressor maintains its current output gain setting before it starts decreasing as the input level decrease. |
+------------------+---------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Decay            | 10            | 1 - 8686 db/s | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level.                                 |
+------------------+---------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Soft-knee        | -             | -             | Soft-knee lets the compressor ease into action, making a less-abrupt change from unprocessed signal to compressed signal.                   |
+------------------+---------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Graph            | -             | -             | Compression Editor Graph.                                                                                                                   |
+------------------+---------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+------------------------------+-------------------------------+
| GUI Control Name | Compiler Name                | Function Description          |
+==================+==============================+===============================+
| RMSTC            | RmsIPAverageGainBlkAlg1RMS   | RMS Time Constant             |
+------------------+------------------------------+-------------------------------+
| Decay            | RmsIPAverageGainBlkAlg1decay | Decay                         |
+------------------+------------------------------+-------------------------------+
| Hold             | RmsIPAverageGainBlkAlg1hold  | Hold                          |
+------------------+------------------------------+-------------------------------+
| Graph            | RmsIPAverageGainBlkAlg1tab   | Compressor Graph table values |
+------------------+------------------------------+-------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

This module computes the Gain of the Compressor. All the inputs to the module are first averaged. RMS value corresponding to the Input Average is computed and converted to dB scale. This value is looked up in the Compressor Graph table to obtain the Gain output value.

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors/rmsipaveragecompressor.jpg
   :width: 300px
