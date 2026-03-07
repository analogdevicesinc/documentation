:doc:`Click here to return to the Gain page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Mute
====

| 
| |mute.png|
| |muteswslew.png|
| ===== Variants =====

-  Mute (No Slew)
-  Mute (ClicklessSWSlew)
-  Mute (HW Slew)
-  Mute (RC Accurate)
-  Multiple Control Mute

Description
===========

| The Mute module provides an option to mute the input signal. By default the signal is passed to the output unchanged. When mute is enabled, there will be no signal available at the output.
| The mute block is available as a Slew or Non-Slew algorithm. The Slew version of the algorithm will smoothly transition the gain to its target value, eliminating any click or pops, but require more system resources.
| Multiple Control Mute provide separate mute selection control for each inputs
| ===== Usage ===== This block has checkbox to mute/unmute the audio.

Targets Supported
=================

+--------------------------+------------+------------------+---------------+------------------+
| Name                     | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==========================+============+==================+===============+==================+
| Mute (No Slew)           | B/S        | B/S              | S             | B                |
+--------------------------+------------+------------------+---------------+------------------+
| Mute (Clickless SW Slew) | B/S        | B/S              | NA            | B                |
+--------------------------+------------+------------------+---------------+------------------+
| Mute (HW Slew)           | NA         | NA               | S             | NA               |
+--------------------------+------------+------------------+---------------+------------------+
| Mute (RC Accurate)       | NA         | NA               | S             | NA               |
+--------------------------+------------+------------------+---------------+------------------+
| Multiple Control Mute    | NA         | NA               | S             | NA               |
+--------------------------+------------+------------------+---------------+------------------+

Pins
====

Input
-----

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input channel X
======================= ===== ===============

Output
------

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------------------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                   | Function Description                                                              |
+====================+===============+=========================+===================================================================================+
| Mute               | False         | True/False              | Mute/unmute the audio output                                                      |
+--------------------+---------------+-------------------------+-----------------------------------------------------------------------------------+
| SlewRate(StepSize) | 12            | 1 to 23 (RC and Linear) | Controls the rate of smooth transition of signal from one level to another level  |
|                    |               | 0.1 to 0.8(DB)          |                                                                                   |
+--------------------+---------------+-------------------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 20                      | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------------------------+-----------------------------------------------------------------------------------+
| SlewType           | RC Slew       | NA                      | Slew type. Applicable to HW slew modules                                          |
+--------------------+---------------+-------------------------+-----------------------------------------------------------------------------------+
| CustomVal          | 0x208A        | NA                      | Custom slew value. Applicable to HW slew modules                                  |
+--------------------+---------------+-------------------------+-----------------------------------------------------------------------------------+

DSP Parameters
==============

+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================================================================================+========================+===============+
| Mute           | Mute/un-mute the audio output                                                                    | Float                  | FixPoint8d24  |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| SlewRate       | StepSize to reach the target Value(NA for DB Slew Block Processing)                              | Float                  | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| StepInc        | StepSize for the signal changing from low level to high level(Only for DB Slew Block Processing) | Float                  | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| StepDec        | StepSize for the signal changing from high level to low level(Only for DB Slew Block Processing) | Float                  | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew)                                               | NA                     | Integer       |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation =====

======================== ========================================
Mute                     = Mute? 0:1
SlewRate (RC and Linear) = Math.Pow(2 , (-1 \* StepSize))
StepInc(DB Slew)         = Math.Pow(10 , (StepSize\* 1000) / Fs)
StepDec(DB Slew)         = Math.Pow(10 , (-StepSize\* 1000) / Fs)
alpha                    = Math.Exp(-1 / (0.01\* fs))
om_alpha                 = 1 - alpha
======================== ========================================

::

   *where Fs is Sampling Rate

.. |mute.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/mute.png
.. |muteswslew.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/muteswslew.png
