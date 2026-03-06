:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>` :doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Digital Microphone Input
========================

| 
| |digital_mic_ssp.jpg|
| ===== Description ===== The Digital Microphone Input block receives input from the hardware's microphone input pins and makes it available in the schematic design.
| ===== Usage ===== Check the block for the input channel(s) you with to enable. Un-check the box disable an input channel. The pin will turn blue when an input is enabled and grey when disabled. The default block has two pins enabled, for stereo connection.
| ===== Targets Supported =====

+--------------------------+------------+-----------------------+-------------------+------------------+
| Name                     | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/ADAU146x | ADSP-218xx/SC8xx |
+==========================+============+=======================+===================+==================+
| Digital Microphone Input | B & S      | B & S                 | S                 | NA               |
+--------------------------+------------+-----------------------+-------------------+------------------+

| 
| ===== Pins =====

Output
------

======= ===== ====================
Name    Type  Description
======= ===== ====================
Output0 Audio Mic Output channel 0
Output1 Audio Mic Output channel 1
======= ===== ====================

| 
| ===== Configurable Parameters =====
| Not applicable
| ===== DSP Parameters ===== No DSP Parameters

.. |digital_mic_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/digital_mic_ssp.jpg
