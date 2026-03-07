:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

ASRC Output
===========

| 
| |asrc_op_ssp.jpg|

Description
-----------

The ASRC Output block routes signals between the schematic design and the hardwares ASRCs (Asynchronous Sample Rate Converters).

|

.. note::

   These blocks are only available for use with DSPs that have integrated ASRCs.


   | ===== Usage ===== Use the output block's drop-down list control to select from the available ASRCs.

-  Every ASRC Output must have its input connected, else there will be errors on compilation.
-  Observe that as you drag more ASRC output blocks into the schematic, the number of available outputs in the drop-down decreases because they can only be represented by one block at a time.

|

| ===== Targets Supported =====

+-------------+------------+-----------------------+-------------------+------------------+
| Name        | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/ADAU146x | ADSP-218xx/SC8xx |
+=============+============+=======================+===================+==================+
| ASRC Output | NA         | NA                    | S                 | NA               |
+-------------+------------+-----------------------+-------------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ===== =====================================
Name  Type  Description
===== ===== =====================================
input Audio Outputs the audio to the hardware pin
===== ===== =====================================

| 
| ===== Configurable Parameters =====

===================== ============= ======= =======================
GUI Parameter Name    Default Value Range   Function Description
===================== ============= ======= =======================
SelectedASRCOPChannel 0             0 to 15 Selected output channel
===================== ============= ======= =======================

| 
| ===== DSP Parameters =====
| Not applicable

.. |asrc_op_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/asrc_op_ssp.jpg
