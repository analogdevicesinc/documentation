:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Signal Detection
================

| 
| |signaldetection.png|

Description
-----------

| The Signal Detection algorithm is a cell that will output a flag once no signal has been present at the input for a given amount of time. The “Threshold” setting will determine the value the input is compared to in order to determine whether or not a signal is present. The “Trig Time” setting will determine how long, in seconds, the cell will wait to output the flag. The peak of the signal is detected, not the RMS value.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| SignalDetection | B          | B                | S             | B                |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input channel X
======================= ===== ===============

Note:

-  <fc #ff0000>X</fc> - Channel Index

Output
~~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output0 Audio Output channel0
======= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range     | Function Description                                                                                                                                |
+====================+===============+===========+=====================================================================================================================================================+
| Threshold(dB)      | -60           | -150 to 0 | Sets the value the input will be compared to. If the input is below this value for a given time determined by “Trig Time(s)”, a flag will be output |
+--------------------+---------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Trig Time(s)       | 120           | 2 to 200  | Sets the amount of time, in seconds, that the signal level must be below the threshold before a flag is output. This value is an approximation      |
+--------------------+---------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 20   | Number of input and output channels. Change in this value requires re-compilation                                                                   |
+--------------------+---------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================================+========================+===============+
| Threshold      | The input will be compared to Threshold value | Float                  | FixPoint8d24  |
+----------------+-----------------------------------------------+------------------------+---------------+
| TimeConstant   | Triggering time in ms                         | Float                  | Integer32     |
+----------------+-----------------------------------------------+------------------------+---------------+
| CounterDown    |                                               | Float                  | Integer32     |
+----------------+-----------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Threshold= 10^ (threshold/20)
| TimeConstant = 10^(-1.0 \* Log10(16.0 - 0.0001) / (TrigTime \* FS / 2)
| TimeConstant = TrigTime \* FS ( Applicable for ADAU145x/146x)

.. |signaldetection.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/signaldetection.png
