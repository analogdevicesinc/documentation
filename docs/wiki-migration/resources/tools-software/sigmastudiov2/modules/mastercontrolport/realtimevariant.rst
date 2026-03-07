:doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mastercontrolport>`

Real Time Variant
=================

| 
| |rtv_ssp.jpg|
| ===== Description =====
| The Variant Editor is a SigmaStudio tool that helps the users utilize different variations(variants) of their original audio program flow already programmed into an external memory.
| A Variant is a set of parameters from the current schematic. Real Time variant module allows users to create multiple variants. Parameters selection for a variant can be done through drag and drop from capture window to the variant configuration form. The parameter addresses and values in the variant are stored in the EEPROM after the self boot image. Address for each of the variant in EEPROM can be either updated by the users or can be generated automatically.
| Module allows users to select a variant dynamically through external input pin. It takes an input index in 32.0 format to select the current variant from EEPROM. The module will read the variant (parameter set) corresponding to the input index from the EEPROM and replaces the actual parameters in the run-time whenever input index is changed.
| ===== Usage =====
| Follow the steps shown below to configure real time variant module.
| \* Create a SigmaStudio audio flow that compiles without any errors.

-  Drag and drop 'Real Time Variant' module and connect a DC source to it. Then change the fixed point format of DC source to 32.0

| 
| |rtv_usage_sspjpg.jpg|
| \* Add modes to the RTV module and sequence packets to each mode to write new parameter values as shown below.

-  Click on Update button to update param addresses
-  Using the selfboot options on the processor, write the latest compilation to DSP.
-  Selfboot the board
-  Change the dc value at the input of the RTV to change modes and write the sequence data to DSP

| 
| |image1|
| ===== Targets Supported =====

+-------------------+------------+-----------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+=======================+===============+==================+
| Real-Time Variant | NA         | NA                    | S             | NA               |
+-------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====
| ====Input Pins====

===== ======= =================================================
Name  Type    Description
===== ======= =================================================
Input Control Acts as the selection index for variant data copy
===== ======= =================================================

| 
| ===== Configurable Parameters =====
| Not applicable

DSP Parameters
--------------

| 
| Not applicable
| ===== DSP Parameter Computation =====
| Not applicable

.. |rtv_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/rtv_ssp.jpg
.. |rtv_usage_sspjpg.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/rtv_usage_sspjpg.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/rtv_modes_ssp.jpg
   :width: 800px
