Pitch Transposer (Data Controlled)
==================================

| :doc:`Click here to return to the Pitch Modification page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/pitchmodification>`

+---+---+
| This algorithm shifts the frequency of an incoming signal. The frequency shift is "voltage-controlled", meaning that there is an input pin that controls the pitch shift amount based on its value. See :doc:`Pitch Transposer </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/pitchmodification/pitchtransposer>` page for GUI/RAM controlled version. | |pitchtranposedata.jpg| |
+---+---+

| 

Input Pins
----------

+--------------+------------------------------------+---------------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                              |
+==============+====================================+===================================================+
| Pin 0: Input | any - any                          | Input signal that will have its frequency shifted |
+--------------+------------------------------------+---------------------------------------------------+
| Pin 1: Input | either                             | Frequency shift amount (percentage/sampling-rate) |
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

+------------------+---------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                        | Function Description                                                                                                                                                                                                                                                                                                                                                                                  |
+==================+===============+==============================+=======================================================================================================================================================================================================================================================================================================================================================================================================+
| Delay Reserved   | 300           | [2.0:Max Data RAM Available] | This control sets the number of samples of audio delay that are reserved in memory as a buffer used for the pitch shifting algorithm. Smaller delay buffers result in more discontinuities in the pitch shifted output signal, which causes some harmonic distortion. Setting this delay buffer to a very large size will result in less distortion, but at the cost of increased delay memory usage. |
+------------------+---------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Context Menu
------------

| Right-click on the module to open the context menu window. By default, DM1 memory is used for delay. User can choose either DM0,DM1 or PM for Delay. Change in memory used for delay leads to re-compile the project(supports for ADAU145x/ADAU146x).
| |image1|

Algorithm Description
---------------------

The algorithm takes an input signal and shifts it in frequency up or down depending on the value of the the frequency shift control signal. The control input value should be the shift percentage divided by the sampling rate, for example for a shift of +100%: control signal = (100 / 48000) = 0.0020833 (fixed-point)

| Here is a time-domain display of a sine tone being shifted in frequency. The top sine tone is the input signal, and the bottom sine tone is the output.
| Approximate Output frequency = Input frequency + (Input frequency \* (Delay Reserved x 0.001) x shift(%))

For example, consider the following schematic,

| |image2| Here,
| Shift = 0.38 (38%)
| Input frequency = 100 Hz
| Delay Reserved = 960
| control signal = 38/48000 => 0.000791667
| Approximate Output frequency = 100 + (100 \* (960 x 0.001) x 0.38) = 136.48

| |pitch_shift_up.png|
| Here is the same example in the frequency domain. This picture shows the frequency domain of the input signal.
| |Before_Pitch_Shift.png|
| This picture shows the frequency domain of the output signal.
| |After_Pitch_Shift.png|

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

.. |pitchtranposedata.jpg| image:: https://wiki.analog.com/_media/pitchtranposedata.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/pitchmodification/pitchtransfermemdelay.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/pitchmodification/pitchtransposerexample.png
.. |pitch_shift_up.png| image:: https://wiki.analog.com/_media/pitch_shift_up.png
.. |Before_Pitch_Shift.png| image:: https://wiki.analog.com/_media/Before_Pitch_Shift.png
.. |After_Pitch_Shift.png| image:: https://wiki.analog.com/_media/After_Pitch_Shift.png
