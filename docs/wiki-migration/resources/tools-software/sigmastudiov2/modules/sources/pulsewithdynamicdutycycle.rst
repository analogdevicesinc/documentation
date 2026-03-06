:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Pulse Generator
===============

| 
| |pulsegen.png|

Description
-----------

| The Pulse Generator block generates pulse at different frequencies with a configurable duty cycle.
| ===== Usage ===== This block has checkbox to enabled or disabled the algorithm. Check the box to enable this algorithm. It has the text fields for frequency and duty cycle to generate the pulse at different frequencies with different "ON" and "OFF" time of the pulse.It has the radio button to round the coefficients.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Pulse Generator | B          | B                | S             | B                |
+-----------------+------------+------------------+---------------+------------------+

| 

Pins
----

Output
~~~~~~

======= ======= ================
Name    Type    Description
======= ======= ================
Output0 Control Output channel 0
======= ======= ================

|

| ===== Configurable Parameters =====

+--------------------+---------------+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                     | Function Description                                                                                                            |
+====================+===============+===========================+=================================================================================================================================+
| Frequency          | 0.01          | 0.01 to 0.5\* sample rate | Sets the frequency for pulse                                                                                                    |
+--------------------+---------------+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ON                 | True          | True/False                | Enable/Disable the algorithm for the channel. When the algorithm is disabled, the output pin will send out a constant value 0.0 |
+--------------------+---------------+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| DutyCycle          | 2.08          | 0 to 100                  | Controls the ON time and OFF time of the pulse                                                                                  |
+--------------------+---------------+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| RoundCoeff         | false         | True/False                | Enable/Disable the frequency step rounding                                                                                      |
+--------------------+---------------+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+============================================================+========================+===============+
| Frequency      | Step size for generating the pulse for specified frequency | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------+------------------------+---------------+
| DutyCycle      | Controls the ON and OFF time of the pulse                  | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------+------------------------+---------------+
| ON             | Enable/Disable the module                                  | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------+------------------------+---------------+
| RoundCoeff     | Roundoff the frequency coefficient                         | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation =====

-  Frequency = fs/FS + 0.0000001 (if rounded)
-  Frequency = fs/FS (not rounded)
-  DutyCycle = DutyCylce/100

| 
| Where fs is frequency and FS is the sampling rate

.. |pulsegen.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/pulsegen.png
