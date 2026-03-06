Noise Removal
=============

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+---+---+
| The Noise Removal algorithm monitors the signal level across many audio bands and compares it to the average signal level to predict what signal components are significant and what signal components are part of the noise floor. It attempts to remove signal bands that are not considered to be significant components of the signal of interest. By removing these signal components, the overall noise level of the signal can be reduced, at the cost of some reduction in the naturalness of the desired signal. This algorithm was designed to run at a sample rate of 16 kHz, so systems using this cell must be set to run at 16 kHz. | |windremovalcell.jpg| |
+---+---+

Input Pins
----------

=============== ================================== ====================
Name            Format [int/dec] - [control/audio] Function Description
=============== ================================== ====================
Pin 0: Audio In decimal - audio                    Audio input
=============== ================================== ====================

Output Pins
-----------

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Audio Out decimal - audio                    Audio output
================ ================================== ====================

GUI Controls
------------

+------------------+---------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                   | Function Description                                                                                                                                                                                                                                                                                                                                                                                         |
+==================+===============+=========================+==============================================================================================================================================================================================================================================================================================================================================================================================================+
| Low Noise Switch | On (red)      | On (red) or Off (green) | Enables the noise reduction algorithm. The down (red) setting enables the noise reduction. The up (green) setting will set the algorithm to bypass mode.                                                                                                                                                                                                                                                     |
+------------------+---------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Delay            | 650           | 300 to 650              | Controls the length of the delay path (in samples) of the algorithm. There is some latency required to break the signal into frequency components and make decisions on which bands should be passed through or blocked. Increasing the latency will improve the perceived quality of the audio and noise reduction performance, but the tradeoff is that the delay time from input to output will increase. |
+------------------+---------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Noise Margin     | -30           | -30 to -30              | This sets the threshold used in the decision making process to determine which bands to pass or block. A lower setting will make the noise reduction algorithm more aggressive in blocking signal components. A higher setting will make the noise reduction algorithm a little more "forgiving", which results in a more natural sound but with less effective noise reduction.                             |
+------------------+---------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+-----------------------+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name      | Compiler Name                       | Function Description                                                                                                                                                                          |
+=======================+=====================================+===============================================================================================================================================================================================+
| Low Noise (switch)    | NoiseReductionAlg1enable_mingain    | Turns the noise reduction on or off.                                                                                                                                                          |
+-----------------------+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Delay (number box)    | NoiseReductionAlg1delay             | Sets the delay path length of the algorithm.                                                                                                                                                  |
+-----------------------+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Noise Margin (slider) | NoiseReductionAlg1noisemargin       | Sets the threshold for noise reduction.                                                                                                                                                       |
+-----------------------+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| N/A                   | Other noise reduction parameters... | There are over 100 parameters used by the algorithm that should not be modified by the user at run time. The only parameters that should be modified are the ones listed above in this table. |
+-----------------------+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The Noise Reduction algorithm is a "blind" processing function that operates automatically on an input signal to attempt to remove noise from the signal.

When signal components are deemed to be not part of the desired signal, the algorithm will smoothly mute those frequency components until they are required again.

This algorithm was intended to be used only in voice applications. Using this algorithm with signals such as music will not yield the desired results, because the algorithm will remove components of the signal that will degrade the quality of the music itself.

The default values in the GUI control for this algorithm provide a good starting point for system design tuning. However, depending on the application, some adjustments might be necessary to get the optimal performance from this algorithm. Much of this tuning is a subjective response to what sounds best, but it is important to mind the recommended value ranges mentioned in the GUI Controls Function Description.

Example
-------

| Typically, the algorithm is inserted as one of the first processing blocks in a signal chain.
| |noiseremovalexample.jpg|

Algorithm Details
-----------------

+----------------------------+-------------------------------------------------+
| Toolbox Path               | ADI Algorithms - Record Algorithms - Wind Noise |
+----------------------------+-------------------------------------------------+
| Cores Supported            | ADAU144x                                        |
|                            | ADAU176x                                        |
+----------------------------+-------------------------------------------------+
| "Grow Algorithm" Supported | no                                              |
+----------------------------+-------------------------------------------------+
| "Add Algorithm" Supported  | no                                              |
+----------------------------+-------------------------------------------------+
| Subroutine/Loop Based      | no                                              |
+----------------------------+-------------------------------------------------+
| Program RAM                | 606                                             |
+----------------------------+-------------------------------------------------+
| Data RAM                   | 2272                                            |
+----------------------------+-------------------------------------------------+
| Parameter RAM              | 278                                             |
+----------------------------+-------------------------------------------------+

.. |windremovalcell.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/windremovalcell.jpg
.. |noiseremovalexample.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/noiseremovalexample.jpg
