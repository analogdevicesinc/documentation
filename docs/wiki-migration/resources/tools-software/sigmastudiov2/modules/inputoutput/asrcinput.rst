:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

ASRC Input
==========

| 
| |asrc_input_ssp.jpg| |asrc_ip_gain_ssp.jpg|

Description
-----------

The ASRC Input blocks route signals between the schematic design and the hardware ASRCs (Asynchronous Sample Rate Converters).

|

.. note::

   These blocks are only available for use with DSPs that have integrated ASRCs.


   | ===== Usage ===== Use the input block's check boxes to enable or disable particular inputs.

-  Every ASRC Output must have its input connected, else there will be errors on compilation.
-  To change the ASRC input's Sampling Rate , Right-click the block name and select Set Sampling Rate, which brings up the Sampling Rate window (default is 48 kHz).

|

| ===== Targets Supported =====

+------------+------------+-----------------------+-------------------+------------------+
| Name       | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/ADAU146x | ADSP-218xx/SC8xx |
+============+============+=======================+===================+==================+
| ASRC Input | NA         | NA                    | S                 | NA               |
+------------+------------+-----------------------+-------------------+------------------+

| 
| ===== Pins =====

Output
~~~~~~

====== ===== =================================
Name   Type  Description
====== ===== =================================
Output Audio Outputs the asrc audio to the pin
====== ===== =================================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+-----------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description        |
+====================+===============+==============+=============================+
| Gain               | 1.0           | 0 to 127.999 | Gain to be applied to input |
+--------------------+---------------+--------------+-----------------------------+

| 
| ===== DSP Parameters =====

============== =================================== =================
Parameter Name Description                         ADAU145x/ADAU146x
============== =================================== =================
gain           gain to be applied to input channel FixPoint8d24
============== =================================== =================

| 
| ===== DSP Parameter Computation ===== gain= Gain

.. |asrc_input_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/asrc_input_ssp.jpg
.. |asrc_ip_gain_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/asrc_ip_gain_ssp.jpg
