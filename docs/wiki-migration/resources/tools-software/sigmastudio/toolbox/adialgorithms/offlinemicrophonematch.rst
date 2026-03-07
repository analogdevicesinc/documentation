Offline Microphone Matching
===========================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| The Offline Microphone Match algorithm analyzes the signal level coming from a stereo input pair. Depending on the target gain level designated, appropriate L/R gains are calculated offline (not running on the DSP) to match the levels between the left and right signals to the target gain. The calculated L/R gains are then applied to the left and right signals, and sent to the output. | |offlinepic1.png| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+

Input Pins
----------

+--------------------+------------------------------------+----------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description       |
+====================+====================================+============================+
| Pin 0: Left Audio  | decimal - audio                    | Left channel input signal  |
+--------------------+------------------------------------+----------------------------+
| Pin 1: Right Audio | decimal - audio                    | Right channel input signal |
+--------------------+------------------------------------+----------------------------+

Output Pins
-----------

+--------------------+------------------------------------+----------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description             |
+====================+====================================+==================================+
| Pin 0: Left Audio  | decimal - audio                    | Gain adjusted left audio output  |
+--------------------+------------------------------------+----------------------------------+
| Pin 0: Right Audio | decimal - audio                    | Gain adjusted right audio output |
+--------------------+------------------------------------+----------------------------------+

GUI Controls
------------

+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range  | Function Description                                                                                                                                                                  |
+==================+===============+========+=======================================================================================================================================================================================+
| Hold (ms)        | 1             | 0-500  | Controls the Hold time used for the peak envelope level detection                                                                                                                     |
+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (dB/s)     | 100           | 0-1000 | Controls the Decay time used for the peak envelope level detection                                                                                                                    |
+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Target Gain (dB) | 0             | -48    | This is the user-defined target gain value for the output. The algorithm will apply gains to both left and right channels to achieve this target output gain on both channel outputs. |
+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Calibrate        | n/a           | n/a    | The calibrate button triggers the microphone matching. Before pressing this button the outputs are not calibrated.                                                                    |
+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| L Gain           | n/a           | n/a    | The calculated Left gain to be applied is displayed here                                                                                                                              |
+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| R Gain           | n/a           | n/a    | The calculated Right gain to be applied is displayed here                                                                                                                             |
+------------------+---------------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+------------------------+------------------------------------------+
| GUI Control Name | Compiler Name          | Function Description                     |
+==================+========================+==========================================+
| Hold (ms)        | MicOfflineCalAlg1hold  | Hold time used for peak level detection  |
+------------------+------------------------+------------------------------------------+
| Decay (dB/s)     | MicOfflineCalAlg1decay | Decay time used for peak level detection |
+------------------+------------------------+------------------------------------------+

Algorithm Description
---------------------

The Offline Microphone Match algorithm is meant to be a system tuning algorithm in order to match a stereo input pair to a designated target output gain. The name "Offline" is used since the calculation for gain application is not running on the DSP. The actual level detection is running on the DSP and is based on a Peak Envelope level detection. Hold and Decay times can be adjusted to fine tune the level calculation.

| Upon initial run-time compilation, two signals that are mismatched will run through the algorithm as-is. Once the Calibrate button is pressed, the offline calculation will find the gains necessary to apply to L and R channels to reach a matched output equal to the target gain designated on the control. At this time, these calculated gains, will be displayed on the control, and also applied to both the L and R signals running on the DSP. The graph below shows two sine tones at different levels, and the matched output, once the Calibrate button is pressed. The target output gain was set to -4dB.
| |offlinepic2.png|

Example
-------

| The schematic image seen below was used to generate the graph seen above. This image shows the result of the Offline Microphone Match algorithm AFTER the calibrate button has been pressed. Thus the gains necessary to achieve a -4dB target output are displayed in the L gain and R gain text boxes on the control for the given input signals.
| |offlinepic3.png|

Algorithm Details
-----------------

+----------------------------+------------------------------------------------------------------------------+
| Toolbox Path               | ADI Algorithms - Record Algorithms - Mic Matching - Offline Microhpone Match |
+----------------------------+------------------------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                                     |
|                            | ADAU176x                                                                     |
|                            | ADAU178x                                                                     |
+----------------------------+------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                                           |
+----------------------------+------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                           |
+----------------------------+------------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                           |
+----------------------------+------------------------------------------------------------------------------+
| Program RAM                | 40                                                                           |
+----------------------------+------------------------------------------------------------------------------+
| Data RAM                   | 12                                                                           |
+----------------------------+------------------------------------------------------------------------------+
| Parameter RAM              | 6                                                                            |
+----------------------------+------------------------------------------------------------------------------+

.. |offlinepic1.png| image:: https://wiki.analog.com/_media/offlinepic1.png
.. |offlinepic2.png| image:: https://wiki.analog.com/_media/offlinepic2.png
.. |offlinepic3.png| image:: https://wiki.analog.com/_media/offlinepic3.png
