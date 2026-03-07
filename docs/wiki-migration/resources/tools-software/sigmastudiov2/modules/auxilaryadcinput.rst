:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Auxiliary ADC Input
===================

| 
| |aux_ip_adc_ssp.jpg|
| ===== Description =====
| The Auxiliary ADC Input algorithm takes the digital signal from the auxiliary A/D (analog-to-digital converter) and makes it available in the design.

|

.. note::

   Note: This block is only available for use with DSPs that have auxiliary ADC


| ===== Usage =====
| Use the block's drop-down list control to select from the available ADC inputs.

-  Every enabled input must be connected to an output, else there will be errors on compilation.
-  Observe that as you drag more ADC input blocks into the schematic, the number of auxiliary ADCs available in the drop-down decreases because they can only be represented by one block at a time.
-  To change the Sampling Rate for an Aux ADC Input, Right-click the block name and select Set FS, which brings up the FS options (default is 48 kHz)

| 
| ===== Targets Supported =====

+---------------------+------------+-----------------------+----------------+------------------+
| Name                | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/1456x | ADSP-218xx/SC8xx |
+=====================+============+=======================+================+==================+
| Auxiliary ADC Input | NA         | NA                    | S              | NA               |
+---------------------+------------+-----------------------+----------------+------------------+

| 
| ===== Pins =====

Output
------

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

+----------------------+---------------+------------------------+-----------------------------+
| GUI Parameter Name   | Default Value | Range                  | Function Description        |
+======================+===============+========================+=============================+
| SelectedADCIPChannel | AUX_ADC_0     | AUX_ADC_0 to AUX_ADC_7 | selects the AUX ADC Channel |
+----------------------+---------------+------------------------+-----------------------------+

| 
| ===== DSP Parameters ===== Not applicable
| ===== DSP Parameter Computation ===== Not applicable

.. |aux_ip_adc_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/aux_ip_adc_ssp.jpg
