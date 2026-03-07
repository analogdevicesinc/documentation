Pitch Transposer
================

.. note::

   Under Construction


| :doc:`Click here to return to the Pitch Modification page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/pitchmodification>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+
| This algorithm shifts the frequency of an incoming signal. There are two versions of the algorithm. This version allows the user to manually set the pitch shift amount by entering it in the GUI (or writing a value directly to RAM). See :doc:`Pitch Transposer (Data Controlled) </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/pitchmodification/pitchtransposerdatacontrolled>` for the "voltage-controlled" version. | |Pitch_Transpose_Cell.png| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+

| 

Input Pins
----------

+--------------+------------------------------------+---------------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                              |
+==============+====================================+===================================================+
| Pin 0: Input | any - any                          | Input signal that will have its frequency shifted |
+--------------+------------------------------------+---------------------------------------------------+

Output Pins
-----------

+---------------+------------------------------------+------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description         |
+===============+====================================+==============================+
| Pin 0: Output | any - any                          | Outputs the processed signal |
+---------------+------------------------------------+------------------------------+

GUI Controls
------------

+------------------------+---------------+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name       | Default Value | Range                        | Function Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+========================+===============+==============================+=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Delay Reserved         | 300           | [2.0:Max Data RAM Available] | This control sets the number of samples of audio delay that are reserved in memory as a buffer used for the pitch shifting algorithm. Smaller delay buffers result in more discontinuities in the pitch shifted output signal, which causes some harmonic distortion. Setting this delay buffer to a very large size will result in less distortion, but at the cost of increased delay memory usage.                                                                                                                                               |
+------------------------+---------------+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Frequency Shift Slider | Center        | [Left:Right]                 | The slider in the middle of the cell sets the amount of pitch shift. When the slider is exactly in the middle, there will be no pitch shift. When the slider is to the right of the center, the pitch of the input signal will be shifted up in frequency. When the slider is to the left of the center, the pitch of the input signal will be shifted down in frequency. When the slider is all the way to the left or right, the pitch will be shifted by the maximum amount (down or up), as determined by the setting of the Max Shift control. |
+------------------------+---------------+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Max Shift              | 100           | [0:Delay Reserved]           | Maximum Percentage (%) change of input frequency, controlled by the Frequency shift slider. The actual percentage of frequency shift is dependent on the "Delay Reserved" amount.                                                                                                                                                                                                                                                                                                                                                                   |
+------------------------+---------------+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

================ ============= ====================
GUI Control Name Compiler Name Function Description
================ ============= ====================
TBD              TBD           TBD
TBD              TBD           TBD
================ ============= ====================

Algorithm Description
---------------------

| The algorithm takes an input signal and shifts it in frequency up or down depending on the settings of the control. Here is a time-domain display of a sine tone being shifted in frequency. The top sine tone is the input signal, and the bottom sine tone is the output.
| Approximate Output frequency = Input frequency - (Input frequency \* (Delay Reserved x 0.001) x Max shift(%))
| |pitch_shift_up.png|
| Here is the same example in the frequency domain. This picture shows the frequency domain of the input signal.
| |Before_Pitch_Shift.png|
| This picture shows the frequency domain of the output signal.
| |After_Pitch_Shift.png|

Example
-------

| The algorithm can simply be inserted into the signal chain to shift the frequency of the signal that is input to it.
| |System_Picture.png|

Algorithm Details
-----------------

========================== =================================
Toolbox Path               ADI Algorithms/Pitch Modification
Cores Supported            AD194x
                           ADAU170x
                           ADAU144x
                           ADAU176x
                           ADAU1781
                           ADAU145X
"Grow Algorithm" Supported no
"Add Algorithm" Supported  no
Subroutine/Loop Based      no
Program RAM                76
Data RAM                   1019
Parameter RAM              4
========================== =================================

.. |Pitch_Transpose_Cell.png| image:: https://wiki.analog.com/_media/Pitch_Transpose_Cell.png
.. |pitch_shift_up.png| image:: https://wiki.analog.com/_media/pitch_shift_up.png
.. |Before_Pitch_Shift.png| image:: https://wiki.analog.com/_media/Before_Pitch_Shift.png
.. |After_Pitch_Shift.png| image:: https://wiki.analog.com/_media/After_Pitch_Shift.png
.. |System_Picture.png| image:: https://wiki.analog.com/_media/System_Picture.png
