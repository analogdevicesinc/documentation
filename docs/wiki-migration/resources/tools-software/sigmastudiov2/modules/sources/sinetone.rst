:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

SineTone
========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/sine.png
   :alt: sine.png

Description
-----------

| 
| The SineTone block generates a sinetone at different frequencies. The gain and phase of the algorithm can be configured for each channel individually.
| ===== Usage =====
| This block has checkbox to enabled or disabled the algorithm. Check the box to enable this algorithm. It has the text fields for frequency, phase and gain to generate the sinetone at different frequencies with different phase and gain.

Targets Supported
-----------------

======== ========== ===================== ============= ================
Name     ADSP-214xx ADSP-215xx/ADSP-SC5xx ADAU145x/146x ADSP-218xx/SC8xx
======== ========== ===================== ============= ================
SineTone B/S        B/S                   S             B
======== ========== ===================== ============= ================

| 
| ===== Pins =====

Output
~~~~~~

======= ======= ================
Name    Type    Description
======= ======= ================
Output0 Control Output channel 0
======= ======= ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                  | Function Description                                                                                                            |
+====================+===============+========================+=================================================================================================================================+
| Frequency          | 500           | 0 to 0.5\* sample rate | Sets the frequency for sinetone                                                                                                 |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| OnOff_Channel0     | False         | True/False             | Enabled/Disabled the algorithm for the channel, When the algorithm is disabled, the output pin will output a constant value 0.0 |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Phase_Channel0     | 0             | 0 to 360 degress       | initial phase of the sinetone                                                                                                   |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Gain_Channel0      | 0             | -138 to 24 dB          | Gain, the sinetone wave to be multiplied                                                                                        |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 20                     | Number of input and output channels. Change in Channels requires re-compilation                                                 |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================================================+========================+===============+
| Sin            | Sin value for generating a sinetone wave at particular frequency | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------------+------------------------+---------------+
| Cos            | Cos value for generating a sinetone wave at particular frequency | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------------+------------------------+---------------+
| Gain_Channel0  | Gain, the sinetone wave to be multiplied                         | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------------+------------------------+---------------+
| Phase_Channel0 | initial phase of the sinetone wave                               | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------------+------------------------+---------------+
| OnOff          | Enabled/Disabled the algorithm                                   | Float                  | FixPoint8d24  |
+----------------+------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Sin = sin⁡(2*π*fs/FS)
| Cos = cos⁡(2*π*fs/FS)
| Where fs is frequency and FS is the sampling rate
