Running Average
===============

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ---------------------------------------------------------------------------------------------------------------

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| The signal envelope block allows a running average to be computed on an input signal. This is not true RMS since the absolute value of the input signal drives the averaging, not the square of the input. Time constants are used to define the averaging time for computation. | |runningpic1.png| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+

Input Pins
----------

+--------------------+------------------------------------+----------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description             |
+====================+====================================+==================================+
| Pin 0: Input Audio | decimal - audio                    | Input Signal to compute envelope |
+--------------------+------------------------------------+----------------------------------+

Output Pins
-----------

+------------------------+------------------------------------+------------------------+
| Name                   | Format [int/dec] - [control/audio] | Function Description   |
+========================+====================================+========================+
| Pin 0: Envelope Output | decimal                            | Envelope Signal Output |
+------------------------+------------------------------------+------------------------+

GUI Controls
------------

+------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range     | Function Description                                                                                                                     |
+==================+===============+===========+==========================================================================================================================================+
| RMS TC dB/s      | 120           | 1- 10000  | Controls the main averaging time used to drive the envelope calculation                                                                  |
+------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)        | 0             | 0 - 2000  | Controls the amount of time the envelope signal is held before releasing                                                                 |
+------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+
| Decay dB/s       | 10            | 1- RMS TC | Controls how quickly the envelope will track the signal during a decay. The max value of this control is determined by the RMS TC value. |
+------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name             | Function Description                                                                                                                               |
+==================+===========================+====================================================================================================================================================+
| RMS TC dB/s      | MonoRunAvgDetectAlg1RMS   | When the RMS time is changed in the GUI a new value is written to the DSP to control the averaging time in the calculation: 1 - RMSTC / (10 \* Fs) |
+------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)        | MonoRunAvgDetectAlg1Hold  | When the Hold time is changed in the GUI, a new value is written to the DSP to control the hold time in the calculation: Fs \* Hold / 1000         |
+------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (dB/s)     | MonoRunAvgDetectAlg1Decay | When the Decay time is changed in the GUI, a new value is written to the DSP to control the decay time in the calculation: Decay / (96 \* Fs)      |
+------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

| The running average block takes the envelope of the input signal based on a running average. The absolute value of the input signal is taken and then filtered to get an averaged level. The RMS TC, hold, and decay time constants affect how the averaging is computed. RMS TC mainly affects the attack rise of the signal and decay affects the release of the signal. The hold time holds the previous envelope value for the amount of time before reacting to a new input signal level change.
| |runningpic2.png|

Example
-------

| The following example uses the Running Average block to drive a GPIO LED. Depending on the level of the input signal, in a given application, you may want to conditionally turn something on or off. In this example, the output of the running average envelope is sent to a :doc:`Tolerance </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/toleranceanalyzer>` block to check the limits of the input signal. If the signal is within the defined range, a "1" is sent to the GPIO output, otherwise a "0" is sent.
| |runningpic3.png|

Algorithm Details
-----------------

+----------------------------+--------------------------------------------------------------------+
| Toolbox Path               | Dynamics Processors - Envelope - Running Average - Signal Envelope |
+----------------------------+--------------------------------------------------------------------+
| Cores Supported            | AD1940                                                             |
|                            | ADAU170x                                                           |
|                            | ADAU144x                                                           |
|                            | ADAU176x                                                           |
|                            | ADAU178x                                                           |
+----------------------------+--------------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                                 |
+----------------------------+--------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                 |
+----------------------------+--------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                 |
+----------------------------+--------------------------------------------------------------------+
| Program RAM                | 24                                                                 |
+----------------------------+--------------------------------------------------------------------+
| Data RAM                   | 11                                                                 |
+----------------------------+--------------------------------------------------------------------+
| Parameter RAM              | 3                                                                  |
+----------------------------+--------------------------------------------------------------------+

.. |runningpic1.png| image:: https://wiki.analog.com/_media/runningpic1.png
.. |runningpic2.png| image:: https://wiki.analog.com/_media/runningpic2.png
.. |runningpic3.png| image:: https://wiki.analog.com/_media/runningpic3.png
