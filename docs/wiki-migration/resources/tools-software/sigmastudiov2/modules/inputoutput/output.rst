:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Output
======

| 
| |output.png|

Description
-----------

| The Output block routes signals to the hardware's physical outputs. Each block is linked to a single output channel.
| ===== Usage ===== Using the drop-down list, select the output channel to associate with a particular block.

Observe that as you drag more output blocks to your schematic, the number of output channels available in the drop-down list decreases because each output can only be associate with a single output block at a time.

| The hardware outputs for a particular processor are limited. While designing you can see the number of outputs that are still available from the HWOutputs item of the Resources window.
| ===== Targets Supported =====

+--------+------------+-----------------------+-------------------+------------------+
| Name   | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/ADAU146x | ADSP-218xx/SC8xx |
+========+============+=======================+===================+==================+
| Output | B & S      | B & S                 | S                 | B                |
+--------+------------+-----------------------+-------------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== =====================================
Name   Type  Description
====== ===== =====================================
input0 Audio Outputs the audio to the hardware pin
====== ===== =====================================

| 
| ===== Configurable Parameters ===== Not applicable
| ===== DSP Parameters ===== No DSP Parameters

.. |output.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/output.png
