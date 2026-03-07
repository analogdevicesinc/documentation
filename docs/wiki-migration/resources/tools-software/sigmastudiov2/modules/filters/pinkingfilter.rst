:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Pink Filter
===========

| 
| |pinkfilter.png|

Description
-----------

| The classic use of this type of filter is to convert white noise, which is equal energy per hertz, to pink noise, which is equal energy per proportional or constant-percentage (e.g., logarithmic) band. Such energy displays as flat on any log scale graph when bundled (integrated) appropriately. The Pinking Filter takes any broadband input and outputs a signal with a 3dB drop per octave. The classic use of this filter is to convert white noise (equal energy per hertz) to pink noise (equal energy per constant percentage, e.g., log bundling, as with an octave or subdivision). To the human ear, which has an approximately logarithmic frequency response, white noise is distinctly trebly, while pink noise sounds broad and smooth, more like a waterfall.
| ===== Targets Supported =====

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
PinkFilter S          B/S              S             B
========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

========== ===== ===============
Name       Type  Description
========== ===== ===============
WhiteNoise Audio Input Channel 0
========== ===== ===============

Output
~~~~~~

========= ===== ===============
Name      Type  Description
========= ===== ===============
PinkNoise Audio Output Channel0
========= ===== ===============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------+---------------------------------+
| GUI Parameter Name | Default Value | Range    | Function Description            |
+====================+===============+==========+=================================+
| InGain             | -10           | -50 to 0 | Gain added to the input signal  |
+--------------------+---------------+----------+---------------------------------+
| OutGain            | 0             | -50 to 0 | Gain added to the output signal |
+--------------------+---------------+----------+---------------------------------+

| 
| ===== DSP Parameters =====

+----------------+---------------------------------+------------------------+---------------+
| Parameter Name | Description                     | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=================================+========================+===============+
| InGain         | Gain added to the input signal  | Float                  | FixPoint8d24  |
+----------------+---------------------------------+------------------------+---------------+
| OutGain        | Gain added to the output signal | Float                  | FixPoint8d24  |
+----------------+---------------------------------+------------------------+---------------+
| FilterCoeff    | Filter Coefficient              | Float                  | FixPoint8d24  |
+----------------+---------------------------------+------------------------+---------------+

| 

.. |pinkfilter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/pinkfilter.png
