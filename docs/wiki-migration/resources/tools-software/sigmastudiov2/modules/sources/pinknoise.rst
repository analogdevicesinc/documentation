| :doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`
| ====== Pink Noise ====== |pinknoise.png|

Description
===========

| This module generates white noise and passes it through a sixth-order IIR filter with a 1/f power response. Pink noise has a power falloff of 1/f.
| ===== Targets Supported =====

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
PinkNoise B          B                S             B
========= ========== ================ ============= ================

| 
| ===== Pins =====

Output
------

========== ===== ================
Name       Type  Description
========== ===== ================
Pink Noise Audio Output channel 0
========== ===== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                     |
+====================+===============+==============+==========================================+
| Gain               | 0             | -120 -> 20db | Gain applied on the pink noise signal    |
+--------------------+---------------+--------------+------------------------------------------+
| On/Off             | Off           | NA           | User can on or off the pink noise signal |
+--------------------+---------------+--------------+------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+---------------------------------------+------------------------+---------------+
| Parameter Name | Description                           | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=======================================+========================+===============+
| Gain           | Gain applied on the pink noise signal | Float                  | FixPoint8d24  |
+----------------+---------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== DSP_Gain = 0.25 \* Math.Pow(10, (Configurable_gain / 20))

.. |pinknoise.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/pinknoise.png
