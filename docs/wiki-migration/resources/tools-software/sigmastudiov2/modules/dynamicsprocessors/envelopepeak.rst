:doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors>`

Envelope Peak
=============

| 
| |peakenv.png| |peakenvext.png|

Description
-----------

| The Envelope Peak block measures the absolute peak value of the input signal and holds the peak level of the incoming signal for the specified time before starts decaying the ramp, when signal level falls.
| ===== Variants =====

-  Envelope Peak
-  Envelope Peak with Ext Decay

| 
| ===== Targets Supported =====

+------------------------------+------------+------------------+---------------+------------------+
| Name                         | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==============================+============+==================+===============+==================+
| Envelope Peak                | B          | B                | S             | B                |
+------------------------------+------------+------------------+---------------+------------------+
| Envelope Peak with Ext Decay | B          | B                | S             | B                |
+------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+----------------------------------+---------+---------------------------------------+
| Name                             | Type    | Description                           |
+==================================+=========+=======================================+
| ControlInput(only for Ext Decay) | Control | Decay speed of the peak detect signal |
+----------------------------------+---------+---------------------------------------+
| Input                            | Audio   | Input channel                         |
+----------------------------------+---------+---------------------------------------+

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

| 
| ===== Configurable Parameters =====

+-------------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name      | Default Value | Range     | Function Description                                                                                                   |
+=========================+===============+===========+========================================================================================================================+
| Hold                    | 0             | 0 to 2000 | Controls the time (ms)the envelope maintains the output level before it starts decreasing as the input level decreases |
+-------------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------+
| Decay(NA for Ext Decay) | 10            | 1 to 1000 | Controls the rate at which envelope signal decreases in response to the decrease in the input signal                   |
+-------------------------+---------------+-----------+------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                                          | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+======================================================================================================+========================+===============+
| Hold           | Controls the time (ms)the envelope maintains the output level                                        | Float                  | 8.24 format   |
+----------------+------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Decay          | Controls the rate at which envelope signal decreases in response to the decrease in the input signal | Float                  | 8.24 format   |
+----------------+------------------------------------------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Hold = (int) FS \* Hold/1000
| Decay = 1/10^(Decay \* 2/(10 \* (FS + 0.000001)))
| Where FS is the sampling rate

.. |peakenv.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/peakenv.png
.. |peakenvext.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/dynamicsprocessors/peakenvext.png
