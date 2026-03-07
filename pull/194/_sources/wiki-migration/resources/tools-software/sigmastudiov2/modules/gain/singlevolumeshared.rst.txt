:doc:`Click here to return to the Gain page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Single Volume Shared
====================

| 
| |singlevolume.png|
| ===== Varaints =====

::

   -Single Control (HW Slew)
   -Single Control (No Slew)
   -Single Control (RC Accurate)
   -Single Control Adjustable (RC Accurate)
   -Complex Single Volume Control  (No-Slew)

Description
-----------

| The Single Volume Shared block controls level of the signal through slider. This block has single volume control for 'N' number of inputs. Connect an input signal and control its level with the slider. Optionally the slew rate can be adjusted in the range 1 to 23.
| ===== Usage ===== To modify the slider settings, right click on the slider control to customize the max/min and step size for slider.
| ===== Targets Supported =====

+-----------------------------------------+------------+------------------+---------------+------------------+
| Name                                    | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=========================================+============+==================+===============+==================+
| Single Control (HW Slew)                | B/S        | B/S              | S             | B                |
+-----------------------------------------+------------+------------------+---------------+------------------+
| Single Control (No Slew)                | NA         | NA               | S             | NA               |
+-----------------------------------------+------------+------------------+---------------+------------------+
| Single Control (RC Accurate)            | NA         | NA               | S             |                  |
+-----------------------------------------+------------+------------------+---------------+------------------+
| Single Control Adjustable (RC Accurate) | NA         | NA               | S             | NA               |
+-----------------------------------------+------------+------------------+---------------+------------------+
| Complex Single Volume Control (No-Slew) | NA         | NA               | B             | NA               |
+-----------------------------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

+-------------------------+----------------------------------------+-----------------+
| Name                    | Type                                   | Description     |
+=========================+========================================+=================+
| Input<fc #ff0000>X</fc> | Audio (Complex pin for Complex module) | Input channel X |
+-------------------------+----------------------------------------+-----------------+

Output
~~~~~~

+--------------------------+----------------------------------------+------------------+
| Name                     | Type                                   | Description      |
+==========================+========================================+==================+
| Output<fc #ff0000>X</fc> | Audio (Complex pin for Complex module) | Output channel X |
+--------------------------+----------------------------------------+------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                   | Function Description                                                           |
+====================+===============+=========================+================================================================================+
| Gain               | 0dB           | -200 to +200 dB         | change the level of the input signal                                           |
+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+
| SlewRate(StepSize) | 12            | 1 to 23 (RC and Linear) | Controls the transition time of the signal from one level to another level     |
|                    |               | 0.1 to 0.8 (DB)         |                                                                                |
+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+
| SlewType           | RC Slew       | NA                      | Slew type. Applicable to HW slew modules                                       |
+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+
| CustomVal          | 0x208A        | NA                      | Custom slew value. Applicable to HW slew modules                               |
+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+
| IsDBChosen         | True          | True/False              | Controls the volume slider is in dBps/Linear                                   |
+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 20                 | Num of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------------------------+--------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                  | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==============================================================================+========================+===============+
| Gain           | change the level of the input signal                                         | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------------------------+------------------------+---------------+
| SlewRate       | Controls the transition time of the signal from one level to another level   | Float                  | NA            |
+----------------+------------------------------------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew)                           | NA                     | Integer32     |
+----------------+------------------------------------------------------------------------------+------------------------+---------------+
| alpha          | scales the value based on Slew mode and value for HW slew (only for HW slew) | NA                     | FixPoint8d24  |
+----------------+------------------------------------------------------------------------------+------------------------+---------------+
| om_alpha       | scales the value based on Slew mode and value for HW slew (only for HW slew) | NA                     | FixPoint8d24  |
+----------------+------------------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation =====

======== ==============================================
SlewRate = Math.Pow(2, (-1 \* StepSize))
Gain     = Math.Pow(10, (DbGain/20))
tc       = 0.04 \* Math.Pow(2, (\_slewRate - 1)) / 1000
alpha    = Math.Exp(-1 / (tc \* FS))
om_alpha = 1 - alpha
======== ==============================================

| 

.. |singlevolume.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/singlevolume.png
