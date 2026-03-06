:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

Master Control Port Read IO
===========================

| 
| |mc_interfaceread_cell_ssp.jpg|
| ===== Description =====
| The Interface Read module reads the value of the parameter setting during selfboot and puts it to the output pin.This module can be used to start running the sigmaStudio schematic with the same parameters (like volume setting) stored before power off.Interface Read module works in tandem with the Interface Write module.

| Interface Read module will keep giving the parameter read from the EEPROM during self boot as output. When the current parameter is changed during execution, the Interface write module updates the present value in the Interface read block.The Interface read module will always have the current parameter setting.
| NOTE:
| Make sure that the interface read and interface write modules that are with each interacting have the same Interface number paramter.
| ===== Usage =====
| The interface read module can be used an input moudule to the UPDown LUT. The Interface read module serves as a starting index to the UPDown LUT. One of the outputs of the UPDown LUT module is given to the Interface write module which will write the same to the EEPROM.

| |mc_ir_usage_ssp.jpg|

Targets Supported
-----------------

+----------------+------------+-----------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+=======================+===============+==================+
| Interface Read | NA         | NA                    | S             | NA               |
+----------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Output
~~~~~~

============= ===== =============================
Name          Type  Description
============= ===== =============================
InterfaceRead Logic Interface read output channel
============= ===== =============================

| 
| ===== Configurable Parameters =====

+---------------------+---------------+-----------------+------------------------------------+
| GUI Parameter Name  | Default Value | Range           | Function Description               |
+=====================+===============+=================+====================================+
| SelectedIFIPChannel | IRCh0         | IRCh0 to IRCh19 | Selects the Interface Read channel |
+---------------------+---------------+-----------------+------------------------------------+

| 
| ===== DSP Parameters ===== Not applicable
| ===== DSP Parameter Computation ===== Not applicable

.. |mc_interfaceread_cell_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/mc_interfaceread_cell_ssp.jpg
.. |mc_ir_usage_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/mc_ir_usage_ssp.jpg
