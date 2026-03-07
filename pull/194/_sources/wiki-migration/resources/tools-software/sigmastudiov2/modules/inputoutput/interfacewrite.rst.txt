:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Interface Write
===============

| 
| |interfacewrite_ssp.jpg|
| ===== Description =====
| The Interface Write block sends signals from the schematic to an interface output register.

| 
| ===== Usage =====
| Each block is associated with only one interface register; select the appropriate one from the drop-down menu.

Observe that as you drag more blocks to your schematic, your number of interfaces available decreases.

|

.. note::

   Note: This block is only available for DSPs with GPIOs or auxiliary ADC.


| ===== Targets Supported =====

+-----------------+------------+-----------------------+----------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/1456x | ADSP-218xx/SC8xx |
+=================+============+=======================+================+==================+
| Interface Write | NA         | NA                    | S              | NA               |
+-----------------+------------+-----------------------+----------------+------------------+

| 
| ===== Pins =====

Input
-----

===== ===== =============================
Name  Type  Description
===== ===== =============================
Input Logic Interface write input channel
===== ===== =============================

| 
| ===== Configurable Parameters =====

+---------------------+---------------+------------------------+------------------------------------+
| GUI Parameter Name  | Default Value | Range                  | Function Description               |
+=====================+===============+========================+====================================+
| SelectedIFIPChannel | INTFACE_0     | INTFACE_0 to INTFACE_7 | Selects the Interface Read channel |
+---------------------+---------------+------------------------+------------------------------------+

| 
| ===== DSP Parameters ===== Not applicable
| ===== DSP Parameter Computation ===== Not applicable

.. |interfacewrite_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/interfacewrite_ssp.jpg
