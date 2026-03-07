:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Input
=====

| 
| |input.png| |input_0-15_ssp.jpg|

Description
-----------

| The Input block receives input from the hardware's input pins and makes it available in the schematic design.
| ===== Usage ===== Check the block for the input channel(s) you with to enable. Un-check the box disable an input channel. The pin will turn blue when an input is enabled and grey when disabled. The default block has two pins enabled, for stereo connection.

| Every enabled input must be connected to an output, else there will be errors on compilation. Only a single input block can be associated with a processor. You will receive an error if you attempt to add multiple inputs to a schematic. To change the Input's Sampling Rate, Right-click the block name and select Set Sampling Rate, which will open the Sampling Rate window (default is 48 kHz):
| ===== Targets Supported =====

+-------+------------+-----------------------+-------------------+------------------+
| Name  | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/ADAU146x | ADSP-218xx/SC8xx |
+=======+============+=======================+===================+==================+
| Input | B & S      | B & S                 | S                 | B                |
+-------+------------+-----------------------+-------------------+------------------+

| 
| ===== Pins =====

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
Output1 Audio Output channel 1
======= ===== ================

| 
| ===== Configurable Parameters =====
| Not applicable
| ===== DSP Parameters ===== No DSP Parameters

.. |input.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/input.png
.. |input_0-15_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/input_0-15_ssp.jpg
