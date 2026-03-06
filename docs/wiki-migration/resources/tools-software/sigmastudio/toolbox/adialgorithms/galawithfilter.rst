:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

GALA With Filter
================

.. image:: https://wiki.analog.com/_media/gala_filter.jpg
   :alt: gala_filter.jpg

Description
-----------

| GALA With Filter block applies the filtering to the input signal first and then applies the variable GALA gain to the filtered input signal with change in control input value(Speed/Engine Noise)
| ===== Targets Supported =====

================ ========== ================ =============
Name             ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
================ ========== ================ =============
GALA With Filter Block      Block            NA
================ ========== ================ =============

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

+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                         | Function Description                                                              |
+====================+===============+===============================+===================================================================================+
| FilterTypesList    | Parametric    | GeneralSecondOrderFilterTypes | Allows to choose desired filter type. Tunable parameter                           |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| InPhase            | True          | True/False                    | Inverts the signal by 180 degrees. Tunable parameter                              |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| EnabledorBypassed  | True          | True/False                    | Enables or Disables the algorithm. Tunable parameter                              |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| Boost              | 0 dB          | -20 to 20 dB                  | Boost to the signal. Tunable parameter                                            |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| Frequency          | 1000 Hz       | 20 to 20000 Hz                | Cutoff frequency for the filter. Tunable parameter                                |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| Q                  | 1.4           | 0 to 1.5                      | Q factor. Tunable parameter                                                       |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| Gain               | 0dB           | -12.6 to 12.6 dB              | Gain applied to compute the filter coefficients. Tunable parameter                |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| Slope              | 0.01          | 0.01 to 1.0                   | Slope applied to the control input. Tunable parameter                             |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| Gain_GALA          | 0             | 0 to 15dB                     | Gain applied to the input signal. Tunable parameter                               |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 15                            | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------------------------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------------+------------------------+
| Parameter Name | Description                                                            | ADSP-214xx/SC5xx/215xx |
+================+========================================================================+========================+
| Slope          | Slope applied to the control input                                     | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| GALA_Gain      | Gain applied to the input signal                                       | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| RampUpSlew     | stepsize for smooth transition of signal from low level to high level  | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| RampDownSlew   | stepsize for smooth transition of signal from high level to high level | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| B0             | Biquad coefficient B0                                                  | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| B1             | Biquad coefficient B1                                                  | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| B2             | Biquad coefficient B2                                                  | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| A1             | Biquad coefficient A1                                                  | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+
| A2             | Biquad coefficient A2                                                  | Float                  |
+----------------+------------------------------------------------------------------------+------------------------+

| 
| ===== DSP Parameter Computation ===== RampUpSlew = 10^(1/(FS \* 20)) RampDownSlew = 10^(-3/(FS \* 20))
