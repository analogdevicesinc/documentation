| :doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>` :doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`
| ====== Pack 16 Bit Audio ======
| |unpack_audio_ssp.jpg|
| ===== Description =====
| This module accepts a packed 16 bit packed audio (upper 16 bits - left channel, lower 16 bits- right channel) channel and un-packs them into left and right audio streams at the output.

| 
| ===== Targets Supported =====

+---------------------+------------+-----------------------+-------------------+------------------+
| Name                | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/ADAU146x | ADSP-218xx/SC8xx |
+=====================+============+=======================+===================+==================+
| Unpack 16 bit Audio | NA         | NA                    | S                 | NA               |
+---------------------+------------+-----------------------+-------------------+------------------+

| 
| ===== Pins =====

Input
=====

===== ===== ==========================
Name  Type  Description
===== ===== ==========================
Input Audio Audio Input to be unpacked
===== ===== ==========================

| 
| ==== Output ====

======= ===== ====================================
Name    Type  Description
======= ===== ====================================
Output0 Audio unpacked output audio- left channel
Output1 Audio unpacked output audio -right channel
======= ===== ====================================

| 
| ===== Configurable Parameters =====
| Not applicable
| ===== DSP Parameters =====
| Not applicable

.. |unpack_audio_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/unpack_audio_ssp.jpg
