:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

GALA Gain
=========

.. image:: https://wiki.analog.com/_media/galagain.jpg
   :alt: galagain.jpg

Description
-----------

| In GALA Gain block, the gain applied to the input signal varies with the changes in the control input(Speed/Engine noise).
| ===== Targets Supported =====

========= ========== ================ =============
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
========= ========== ================ =============
GALA Gain Block      Block            NA
========= ========== ================ =============

| 
| ===== Pins =====

Input
~~~~~

========== ======= =====================
Name       Type    Description
========== ======= =====================
SpeedInput Control Speed or Engine Noise
Input0     Audio   Input Channel0
========== ======= =====================

Output
~~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Output0 Audio Output channel0
======= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                              |
+====================+===============+================+===================================================================================+
| Slope              | 0.01          | 0.01 to 1.0    | It is used to multiply with the control input                                     |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------+
| DBGain             | 0.1           | 0.0 to 15.0 dB | Scales the input signal                                                           |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 15             | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------+------------------------+
| Parameter Name | Description                                                      | ADSP-214xx/SC5xx/215xx |
+================+==================================================================+========================+
| Slope          | Scales the speed(Control input)                                  | Float                  |
+----------------+------------------------------------------------------------------+------------------------+
| DBGain         | Scales the input signal                                          | Float                  |
+----------------+------------------------------------------------------------------+------------------------+
| RampUpSlew     | Rate of smooth transition of signal from low level to high level | Float                  |
+----------------+------------------------------------------------------------------+------------------------+
| RampDownSlew   | Rate of smooth transition of signal from high level to low level | Float                  |
+----------------+------------------------------------------------------------------+------------------------+

| 
| ===== DSP Parameter Computation ===== RampUpSlew = 10^(1/(FS \* 20))
| RampDownSlew = 10^(-3/(FS \* 20))
