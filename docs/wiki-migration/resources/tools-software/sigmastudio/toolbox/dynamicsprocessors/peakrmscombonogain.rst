PeakRMS Combo (no gain)
=======================

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| -------------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| The PeakRMS combo compressor is a dual detection path compressor. Both Peak and RMS detection are performed on the detection input signal and then a combination of the two detection methods is used for the final gain application of the compressor. Depending on the time constants, Peak or RMS can dominate the effect on either the attack or release. The idea behind this combination detection is to provide the best of both worlds between the two detection methods, allowing fast reaction to undesired peaks, while still having a natural auditory quality to audio compression. | |peakrmsnopic1.png| |
| The image of the algorithm shown is the Mono version of the algorithm. There is also a stereo version of the algorithm, shown in the example below.                                                                                                                                                                                                                                                                                                                                                                                                                                              |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Input Pins
----------

+------------------------+------------------------------------+-------------------------------------------------------------------------------------------------+
| Name                   | Format [int/dec] - [control/audio] | Function Description                                                                            |
+========================+====================================+=================================================================================================+
| Pin 0: Audio Input     | decimal - audio                    | Input signal to be compressed                                                                   |
+------------------------+------------------------------------+-------------------------------------------------------------------------------------------------+
| Pin 1: External Detect | decimal - audio                    | Signal Detection input. This is the signal that is run through both the Peak and RMS detection. |
+------------------------+------------------------------------+-------------------------------------------------------------------------------------------------+

Output Pins
-----------

+---------------------+------------------------------------+--------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description     |
+=====================+====================================+==========================+
| Pin 0: Audio Output | decimal - audio                    | Compressed output signal |
+---------------------+------------------------------------+--------------------------+

GUI Controls
------------

+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range      | Function Description                                                                                                                                                                                    |
+==================+===============+============+=========================================================================================================================================================================================================+
| PeakHold (ms)    | 2             | 0-1000     | Controls the hold time constant used in the Peak detection path                                                                                                                                         |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PeakDecay (dB/s) | 9000          | 0 -10000   | Controls the decay time constant used in the Peak detection path                                                                                                                                        |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (dB/s)    | 1000          | 1-10000    | Controls the RMS attack time constant used in the RMS detection path                                                                                                                                    |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)        | 2             | 0 -2000    | Controls the hold time constant used in the RMS detection path                                                                                                                                          |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (dB/s)     | 500           | 0 - RMS TC | Controls the decay time constant used in the RMS detection path. The max value of the decay for the RMS path is limited by the RMS time constant value                                                  |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee        | Off           | On/Off     | Enables a soft knee calculation for the gain table threshold points. Clicking this button will toggle between having soft knee enabled or disabled, and new compressor curve points will be calculated. |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph       | n/a           | n/a        | Clicking on the "Show Graph" button, opens the compressor curve editor. In this window, 33 points can be dragged or edited to a precise compression curve.                                              |
+------------------+---------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name         | Function Description                                                                                                                                                                                                                         |
+==================+=======================+==============================================================================================================================================================================================================================================+
| PeakHold (ms)    | PeakRMSCombo1holdAll  | The peak detector hold time in (ms) is written to the DSP according to this formula: Fs \*Hold_Time/1000                                                                                                                                     |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PeakDecay (dB/s) | PeakRMSCombo1decayAll | The peak detector decay time in (dB/s) is written to the DSP according to this formula: Decay / ( 96 \*Fs)                                                                                                                                   |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (dB/s)    | PeakRMSCombo1RMS      | The RMS detector time constant affecting mainly the RMS attack time in (dB/s) is written to the DSP according to this formula: 1 - RMS/(10\*Fs)                                                                                              |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)        | PeakRMSCombo1hold     | The RMS detector hold time in (ms) is written to the DSP according to this formula: Fs \*Hold_Time/1000                                                                                                                                      |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (dB/s)     | PeakRMSCombo1decay    | The RMS detector decay time in (dB/s) is written to the DSP according to this formula: Decay / ( 96 \*Fs)                                                                                                                                    |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Soft Knee        | PeakRMSCombo1         | Clicking the Soft Knee button on the compressor control, writes the 33 gain table point parameters to the DSP. This allows a soft or smooth transition at any threshold point defined in the compressor curve.                               |
|                  | ...                   |                                                                                                                                                                                                                                              |
|                  | ...                   |                                                                                                                                                                                                                                              |
|                  | ...                   |                                                                                                                                                                                                                                              |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show Graph       | PeakRMSCombo1         | Clicking on the "Show Graph" button, opens the compressor curve editor. In this window, 33 points can be dragged or edited to a precise compression curve. Each time a point is dragged or edited, the 33 points are re-written to the DSP.  |
|                  | ...                   |                                                                                                                                                                                                                                              |
|                  | ...                   |                                                                                                                                                                                                                                              |
|                  | ...                   |                                                                                                                                                                                                                                              |
+------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The PeakRMS Combo algorithm offers a dual-detection path. The RMS and Peak envelope of the detector input signal are calculated. Depending on the time constants used for each detection (Peak and RMS) and ADI proprietary code, the algorithm switches between using RMS and Peak detection in order to apply the compressor gain adjustment. This results in getting the "best of both worlds" with both Peak and RMS compression. Typically, there are complaints that RMS is too slow to react to fast spikes in signal input. Peak detectors can handle these fast spikes, but then do not have a natural sound response to the increase in signal level. The generated images below show the difference in output signal for RMS, Peak, and Combo compressor.

The clipped brown signal is an input sine tone at a low level, that immediately increases in level. All three compressors have a limiting compressor curve set at -20dB. The Red curve is the RMS output, showing the first initial peaks still getting through to the output because the of the slower attack time constant. The purple curve is the Peak output, showing the quick attenuation of the peak, but unnatural ripple introduced by the quick attack. The light-blue output is the Combo compressor. Note that the first peak is attenuated quickly (not as severe as the Peak) but much more than the RMS. However, there still is a natural decrease in signal level from the initial attack, which subjectively sounds better than the harsh peak detection.

| Playing with both the RMS and Peak detection time constants on this control can yield different results, but the default settings on the control are recommended as a starting point. The graph below was generated with the default time constant settings.
| |peakrmsnopic2.png|

Example
-------

| The following schematic image shows the PeakRMS Combo algorithm being used on a stereo signal. The external detector path is fed with the larger signal between L and R. This ensures that any rise in signal from either channel will ensure that the output level is reduced. Other applications may be more lenient and can use the average signal between L and R to drive the detector path. For that method you would simply sum the left and right using a Signal Merger cell. The schematic below uses the Input, AB in/out Condition, and Output cells. Before the signal is compared you must obtain the absolute value of the two signals. If you do not then the AB compare cell will be comparing two signals where one can be a high level negative signal and the other can be a small positive signal so the output would be the small positive signal since it is the greater of the two. So for this to function as intended you must compare the absolute value of the two signals and take the greater of the two. Internally, the compressor sidechain will take the absolute value so this will not change how the sidechain functions.
| |peakrmstopic3-1.jpg|

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------------------------------+
| Toolbox Path               | Dynamics Processors - Combo: RMS + Peak - Stereo - PeakRMS Combo (no gain) |
+----------------------------+----------------------------------------------------------------------------+
| Cores Supported            | AD1940                                                                     |
|                            | ADAU170x                                                                   |
|                            | ADAU144x                                                                   |
|                            | ADAU176x                                                                   |
|                            | ADAU178x                                                                   |
|                            | ADAU145x                                                                   |
|                            | ADAU146x                                                                   |
+----------------------------+----------------------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                                         |
+----------------------------+----------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                         |
+----------------------------+----------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                         |
+----------------------------+----------------------------------------------------------------------------+
| Program RAM                | 70                                                                         |
+----------------------------+----------------------------------------------------------------------------+
| Data RAM                   | 24                                                                         |
+----------------------------+----------------------------------------------------------------------------+
| Parameter RAM              | 39                                                                         |
+----------------------------+----------------------------------------------------------------------------+

.. |peakrmsnopic1.png| image:: https://wiki.analog.com/_media/peakrmsnopic1.png
.. |peakrmsnopic2.png| image:: https://wiki.analog.com/_media/peakrmsnopic2.png
.. |peakrmstopic3-1.jpg| image:: https://wiki.analog.com/_media/peakrmstopic3-1.jpg
