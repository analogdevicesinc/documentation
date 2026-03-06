output ======Signal Detection======

| :doc:`Click here to return to the Level Detectors Lookuptables page </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| The Signal Detection algorithm is a cell that will output a flag once no signal has been present at the input for a given amount of time. The "Threshold" setting will determine the value the input is compared to in order to determine whether or not a signal is present. The "Trig Time" setting will determine how long, in seconds, the cell will wait to output the flag. The peak of the signal is detected, not the RMS value. | |signaldetection.png| |
| This flag can be used, for example, to alert a microcontroller that no audio signal is present in the signal chain, which could then allow the microcontroller to power-down unneeded parts of the system.                                                                                                                                                                                                                               |                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

.. important::

   It is important to note that the "Trig Time" setting is an approximation. It will take some experimentation to find what value is right for a given application.


Input Pins
==========

+--------------+------------------------------------+-----------------------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                                      |
+==============+====================================+===========================================================+
| Pin 0: Input | any - any                          | Input signal that will be compared to the threshold value |
+--------------+------------------------------------+-----------------------------------------------------------+

Output Pins
===========

+----------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Name           | Format [int/dec] - [control/audio] | Function Description                                                                                                          |
+================+====================================+===============================================================================================================================+
| Pin 0: Trigger | decimal - control                  | Outputs a flag (a value of 1.0 in 5.23 format) after no signal has been present for a given amount of time, and 0.0 otherwise |
+----------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

GUI Controls
============

+------------------+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range    | Function Description                                                                                                                                 |
+==================+===============+==========+======================================================================================================================================================+
| Threshold(dB)    | -60           | [-150:0] | Sets the value the input will be compared to. If the input is below this value for a given time determined by "Trig Time(s)", a flag will be output. |
+------------------+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Trig Time(s)     | 120           | [2:200]  | sets the amount of time, in seconds, that the signal level must be below the threshold before a flag is output. This value is an approximation.      |
+------------------+---------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
=========================

+------------------+-------------------------------+--------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                 | Function Description                                                                 |
+==================+===============================+======================================================================================+
| Threshold(dB)    | thresholdSignalDetectAlg1     | Actual value written to the DSP when the value in the "Threshold(dB) box is changed. |
+------------------+-------------------------------+--------------------------------------------------------------------------------------+
| Trig Time(s)     | time_constantSignalDetectAlg1 | Actual value written to the DSP when the value in the "Trig Time(s)" box is changed  |
+------------------+-------------------------------+--------------------------------------------------------------------------------------+

Algorithm Description
=====================

| The following graph shows the output (red) of the Signal Detect cell based on a given input (blue). In this scenario the "Threshold(dB)" is set to '-60' and the "Trig Time(s)" is set to '6'. Notice how the output toggles to '1' after the silence following the audio signal, based on the "Trig Time(s)" value, and then returns back to '0' once the signal reappears.
| |simulation_pic_1.png|

Example
=======

| In this example, the Signal Detection cell is being used to monitor the incoming audio signal to be processed by the equalizer. If the signal on both channels falls below the threshold for the duration of the "Trig Time(s)" parameter, a flag will be output to GPIO_0. This can be used, for example, to power down unneeded parts of the system when no signal is present.
| |circuitexample.png|

Algorithm Details
=================

+----------------------------+------------------------------------------------------------------+
| Toolbox Path               | Level Detectors/Lookup Tables - Signal Detect - Signal Detection |
+----------------------------+------------------------------------------------------------------+
| Cores Supported            | AD194x                                                           |
|                            | ADAU170x                                                         |
|                            | ADAU144x                                                         |
|                            | ADAU176x                                                         |
+----------------------------+------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes                                                              |
+----------------------------+------------------------------------------------------------------+
| "Add Algorithm" Supported  | yes                                                              |
+----------------------------+------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                               |
+----------------------------+------------------------------------------------------------------+
| Program RAM                | 11                                                               |
+----------------------------+------------------------------------------------------------------+
| Data RAM                   | 4                                                                |
+----------------------------+------------------------------------------------------------------+
| Parameter RAM              | 3                                                                |
+----------------------------+------------------------------------------------------------------+

.. |signaldetection.png| image:: https://wiki.analog.com/_media/signaldetection.png
.. |simulation_pic_1.png| image:: https://wiki.analog.com/_media/simulation_pic_1.png
   :width: 900px
.. |circuitexample.png| image:: https://wiki.analog.com/_media/circuitexample.png
