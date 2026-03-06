:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

DC Input No Mips
================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/dcnomips.png
   :alt: dcnomips.png

Description
-----------

| The DC Input No MIPs Block is a parameter value write utility which can write directly to any parameter. The block's controls allow the value and the format to be set. There are 32/28 available bits which can be used to represent decimal values depends on the SigmaDSP.
| ===== Targets Supported =====

+------------------+------------+-----------------------+---------------+------------------+
| Name             | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==================+============+=======================+===============+==================+
| DC Input No MIPs | NA         | NA                    | S             | NA               |
+------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Configurable Parameters
-----------------------

+--------------------+---------------+-----------------------------+-----------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                       | Function Description                                                        |
+====================+===============+=============================+=============================================================================+
| DCValue            | 0             | 0 to 2147483647             | This control gives the DC, direct current, signal(a constant numeric value) |
+--------------------+---------------+-----------------------------+-----------------------------------------------------------------------------+
| IntegerBits        | 5/8           | 0 to 32 (Only for SigmaDSP) | This control decides the range of DC control                                |
+--------------------+---------------+-----------------------------+-----------------------------------------------------------------------------+
| DecimalBits        | 23/24         | 0 to 32(Only for SigmaDSP)  | This control decides the range of DC control                                |
+--------------------+---------------+-----------------------------+-----------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+------------------------------------------------------+------------------------+------------------------+
| Parameter Name | Description                                          | ADSP-214xx/SC5xx/215xx | ADAU145x/146x          |
+================+======================================================+========================+========================+
| DCValue        | DC, direct current, signal(a constant numeric value) | Float                  | Format specified in UI |
+----------------+------------------------------------------------------+------------------------+------------------------+

| 
