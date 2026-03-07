:doc:`Click here to return to the Gain page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Single Slew External Volume
===========================

| 
| |extvol.png|

Description
-----------

| The Single Slew Ext Vol block controls level of the signal through external pin. Such capability would be appropriate for an application like external control communication to ab 8-10 bit ADC.
| ===== Usage ===== This block has text filed to specify the slew rate for smooth transition from one level of the signal to another level.slew rate is configurable from 1 to 23. Signal transition from one level to another level is faster when slew rate value is low and Signal transition from one level to another level is slower when slew rate value is high.
| ===== Targets Supported =====

+---------------------+------------+------------------+---------------+------------------+
| Name                | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=====================+============+==================+===============+==================+
| Single Slew Ext Vol | B/S        | B/S              | S             | B                |
+---------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================== ======= ===================================
Name                     Type    Description
======================== ======= ===================================
ControlInput             Control Controls the signal level of output
Input <fc #ff0000>X</fc> Audio   Input channel X
======================== ======= ===================================

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                          | Function Description                                                                     |
+====================+===============+================================+==========================================================================================+
| SlewRate(StepSize) | 12            | 1 to 23                        | Controls the transition time of signal from one level to another level                   |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| SlewType           | RC            | RC,DB(only in Block & HW Slew) | Allows to select the slew type for algorithm. Change in slewType requires re-compilation |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| SlewType1          | Linear Slew   | NA                             | Slew type. Applicable to HW slew modules                                                 |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| SlewType2          | Linear Slew   | NA                             | Slew type. Applicable to HW slew modules                                                 |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| Index1             | 8             | 0 to 15                        | Slew rate which scales the Slew value                                                    |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| Index2             | 8             | 0 to 15                        | Slew rate which scales the Slew value                                                    |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 20                             | Num of input and output channels .Change in this value requires re-compilation           |
+--------------------+---------------+--------------------------------+------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------------------------------+------------------------+
| Parameter Name | Description                                                           | ADSP-214xx/SC5xx/215xx |
+================+=======================================================================+========================+
| SlewRate       | Controls the transtion time of signal from one level to another level | Float                  |
+----------------+-----------------------------------------------------------------------+------------------------+
| slew_mode      | Controls the transtion time of signal from one level to another level | NA                     |
+----------------+-----------------------------------------------------------------------+------------------------+

| 
| ===== DSP Parameter Computation ===== SlewRate = 2^(-1\*StepSize)

.. |extvol.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/extvol.png
