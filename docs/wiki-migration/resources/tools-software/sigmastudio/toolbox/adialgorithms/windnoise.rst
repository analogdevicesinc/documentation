Wind Noise
==========

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+---+---+
| The Wind Noise reduction block is an algorithm that detects and removes wind noise signal coming from 2 microphones. When wind noise is present an output flag is set high signaling that wind noise is present and a proprietary filter is enabled to remove the wind noise. When no wind noise is present, the output flag is set low, and the input signal is passed directly to the outputs with no processing. This algorithm is only meant to be used for a signal coming from a stereo pair of microphones. | |windnoisepic1.png| |
+---+---+

Input Pins
----------

+-------------------+------------------------------------+---------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description      |
+===================+====================================+===========================+
| Pin 0: Audio In L | decimal - audio                    | Left Channel audio input  |
+-------------------+------------------------------------+---------------------------+
| Pin 1: Audio In R | decimal - audio                    | Right Channel audio input |
+-------------------+------------------------------------+---------------------------+

Output Pins
-----------

+--------------------+------------------------------------+----------------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description                   |
+====================+====================================+========================================+
| Pin 0: Audio Out L | decimal - audio                    | Left Channel audio output              |
+--------------------+------------------------------------+----------------------------------------+
| Pin 1: Audio Out R | decimal - audio                    | Right Channel audio output             |
+--------------------+------------------------------------+----------------------------------------+
| Pin 2: Flag Output | decimal - control                  | Wind noise detector fading flag output |
+--------------------+------------------------------------+----------------------------------------+

GUI Controls
------------

+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range    | Function Description                                                                                                                                                                                                                                    |
+==================+===============+==========+=========================================================================================================================================================================================================================================================+
| Frequency        | 1000          | 0- 22000 | Controls the cut-off frequency of the Wind Noise reduction filter. Recommended values should be kept between 250 and 2000.                                                                                                                              |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack (ms)      | 5             | 0- 22000 | Attack time for going into Wind Noise reduction mode (How quickly the algorithm reacts to windnoise). Quick attack time is recommended for fast reaction time to the onset of wind noise reduction.                                                     |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release (ms)     | 2500          | 0- 22000 | Release time for coming out of Wind Noise reduction mode (How smoothly the algorithm returns to normal unprocessed audio). Slow release time is recommended to provide smooth transition back to unprocessed audio.                                     |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Eff Gain         | 5             | 0 - 10   | Gain of the effect when Wind Noise filtering is active. If overall output signal level is too low when wind noise filter is active, raise this gain. If the overall output signal level is too high, when wind noise filter is active,  lower the gain. |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Level 1          | 70            | 0 - 100  | Controls the level limit for detecting wind noise. Recommended values should be kept between 60-90 and are system dependent.                                                                                                                            |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TC 1 (ms)        | 22            | 0- 11000 | Time constant averaging for signal level measurements.                                                                                                                                                                                                  |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Level 2          | 4             | 0 - 100  | Controls the sensitivity level for the strength of the wind noise signal. Recommended values should be kept between 0 (very strong wind signal) to 15 (very weak wind signal).                                                                          |
+------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name        | Function Description                                                                                                 |
+==================+======================+======================================================================================================================+
| Frequency Gain   | WindNoiseAlg1F11     | When The Frequency or Gain values are changed on the GUI control, 7 parameters are calculated and written to the DSP |
|                  | WindNoiseAlg1F12     |                                                                                                                      |
|                  | WindNoiseAlg1F20     |                                                                                                                      |
|                  | WindNoiseAlg1F21     |                                                                                                                      |
|                  | WindNoiseAlg1F30     |                                                                                                                      |
|                  | WindNoiseAlg1F31     |                                                                                                                      |
|                  | WindNoiseAlg1F42     |                                                                                                                      |
+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+
| Attack           | WindNoiseAlg1attack  | The Attack time is calculated and written to the DSP                                                                 |
+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+
| Release          | WindNoiseAlg1release | The Release time is calculated and written to the DSP                                                                |
+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+
| Level1           | WindNoiseAlg1Level1  | The Level value is written to the DSP                                                                                |
+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+
| TC 1             | WindNoiseAlg1tc1     | When the Time Constant value is changed, 4 parameters are calculated and written to the DSP                          |
|                  | WindNoiseAlg1tc11    |                                                                                                                      |
|                  | WindNoiseAlg1tc2     |                                                                                                                      |
|                  | WindNoiseAlg1tc22    |                                                                                                                      |
+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+
| Level2           | WindNoiseAlg1Level2  | The Level value is calculated and written to the DSP                                                                 |
+------------------+----------------------+----------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The Wind Noise block is a stereo algorithm that operates on two microphones. In a system design, it is important to have the block as close to the inputs as possible with no other processing before the algorithm. This algorithm relies on having the direct microphone signal to detect and process the any wind noise components in the signal.

| The algorithm is structured in two parts: the detection and the wind noise reduction.
| |windnoisepic2.png|
| When wind noise is detected, the algorithm smoothly applies a proprietary filter to remove the unwanted noise signal. When wind noise is no longer detected, the algorithm smoothly transitions to having no filtering and the direct input signal is passed to the outputs. The fading into and out of the wind noise mode can be monitored via the Flag output pin. The Flag output pin shows the fading in and out of wind reduction mode.

The default values in the GUI control for this algorithm provide a good starting point for system design tuning. However, depending on the application, some adjustments might be necessary to get the optimal performance from this algorithm. Much of this tuning is a subjective response to what sounds best, but it is important to mind the recommended value ranges mentioned in the GUI Controls Function Description.

Example
-------

| The schematic image below shows the Wind Noise block being used with a Level Detector to monitor the fading output. The input of the algorithm is driven from a stereo microphone pair.
| |windnoisepic3.png|

Algorithm Details
-----------------

+----------------------------+-------------------------------------------------+
| Toolbox Path               | ADI Algorithms - Record Algorithms - Wind Noise |
+----------------------------+-------------------------------------------------+
| Cores Supported            | ADAU144x                                        |
|                            | ADAU176x                                        |
|                            | ADAU178x                                        |
+----------------------------+-------------------------------------------------+
| "Grow Algorithm" Supported | no                                              |
+----------------------------+-------------------------------------------------+
| "Add Algorithm" Supported  | no                                              |
+----------------------------+-------------------------------------------------+
| Subroutine/Loop Based      | no                                              |
+----------------------------+-------------------------------------------------+
| Program RAM                | 84                                              |
+----------------------------+-------------------------------------------------+
| Data RAM                   | 31                                              |
+----------------------------+-------------------------------------------------+
| Parameter RAM              | 15                                              |
+----------------------------+-------------------------------------------------+

.. |windnoisepic1.png| image:: https://wiki.analog.com/_media/windnoisepic1.png
.. |windnoisepic2.png| image:: https://wiki.analog.com/_media/windnoisepic2.png
.. |windnoisepic3.png| image:: https://wiki.analog.com/_media/windnoisepic3.png
