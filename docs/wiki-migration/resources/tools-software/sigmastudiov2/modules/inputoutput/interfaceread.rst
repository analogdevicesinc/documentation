:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Interface Read
==============

| 
| |interfaceread_ssp.jpg|
| ===== Description =====
| The Interface Read block takes value from one of eight interface registers and makes it available in the schematic design. The yellow pin can connect to GPIO Conditioning block's yellow input pins. It is especially useful for parts that self-boot and use external interface registers.

| 
| ===== Usage =====
| Select a particular interface from the drop-down.

-  Every input must be connected to an output, else there will be errors on compilation.
-  Observe that as you drag more output blocks to your schematic, your number of interfaces available decreases.

| Note: This block is only available for DSPs with GPIOs or auxiliary ADC.
| ===== Targets Supported =====

+----------------+------------+-----------------------+----------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/1456x | ADSP-218xx/SC8xx |
+================+============+=======================+================+==================+
| Interface Read | NA         | NA                    | S              | NA               |
+----------------+------------+-----------------------+----------------+------------------+

| 
| ===== Pins =====

Output
------

============= ===== =============================
Name          Type  Description
============= ===== =============================
InterfaceRead Logic Interface read output channel
============= ===== =============================

| 
| ===== Configurable Parameters =====

+---------------------+---------------+------------------------+------------------------------------+
| GUI Parameter Name  | Default Value | Range                  | Function Description               |
+=====================+===============+========================+====================================+
| SelectedIFIPChannel | INTFACE_0     | INTFACE_0 to INTFACE_7 | Selects the Interface Read channel |
+---------------------+---------------+------------------------+------------------------------------+

| 
| ===== DSP Parameters ===== Not applicable

| 
| ===== DSP Parameter Computation ===== Not applicable

.. |interfaceread_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/interfaceread_ssp.jpg
