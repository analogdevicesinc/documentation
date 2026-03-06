:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors>`

Signal Envelope
===============

| 
| |signalenv.png|

Description
-----------

| The Signal Envelope block measures the rms average value of the input signals.Holds the signal level for time specified in Hold Control(ms) before starting increase/decrease the output signal level,when there is a change in input signal level.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Signal Envelope | B/S        | B/S              | B/S           | NA               |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input channel
===== ===== =============

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

| 
| ===== Configurable Parameters =====

+-------------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name      | Default Value | Range      | Function Description                                                                                                                                                                                                       |
+=========================+===============+============+============================================================================================================================================================================================================================+
| RmsTC                   | 120           | 1 to 10000 | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the “Attack” time. |
+-------------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold                    | 0             | 0 to 2000  | Controls the time (ms)the envelope maintains the output level before it starts decreasing as the input level decreases                                                                                                     |
+-------------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay(NA for Ext Decay) | 10            | 1 to 10000 | Controls the rate at which envelope signal decreases in response to the decrease in the input signal                                                                                                                       |
+-------------------------+---------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                                                            | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+========================================================================================================================+========================+===============+
| RmsTC          | Controls the time constant (TC) in dB/second that is used for calculating the RMS input value.                         | Float                  | 8.24 format   |
+----------------+------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Hold           | Controls the time (ms)the envelope maintains the output level before it starts decreasing as the input level decreases | Float                  | 8.24 format   |
+----------------+------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Decay          | Controls the rate at which envelope signal decreases in response to the decrease in the input signal                   | Float                  | 8.24 format   |
+----------------+------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
-------------------------

| 
| RmsTC = Abs(1 - 10^(RmsTC/(10 \* Sampling Rate)
| Hold = (int) Sampling Rate \* Hold/1000
| Decay = 1/10^(Decay \* 2 /(10 \* Sampling Rate))

.. |signalenv.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/signalenv.png
   :width: 200px
