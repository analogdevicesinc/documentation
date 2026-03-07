:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Voltage Controlled Delay with Memory Selection
==============================================

| |module.png|
| ===== Description ===== The Multi-Tap Voltage Controlled Delay cell introduces a variable delay to a single audio input, generating multiple outputs known as 'taps.' The delay duration for each tap can be adjusted in real-time by changing the value on the corresponding control input pin. Additionally, this module provides an option to select the memory where the user wishes to create the delay buffer. Based on the memory selection of **StateA** or **StateB**, the delay buffer will be created in L1 memory, and for the option **StateC**, the buffer will be created in L3 memory.
| Please refer the *Configurable Parameters* table for further details.
| ===== Usage ===== The multi-tap voltage-controlled delay allows a single input signal to be output as multiple, independently delayed copies. By right-clicking and selecting the “NumChannels” option, the user can increase the number of copies, or “taps”, to be output.
| The "Max Delay" and "Memory" chosen prior to compilation; the equivalent delay in milliseconds/samples is displayed below this. Note that this delay Max size is a shared Max-Delay that can be used by individual taps.
| If the control input for any tap exceeds the maximum allowable delay for that tap, the maximum value will be used. The first input pin is the audio input signal, while the subsequent input pins are used to set the current delay for the input signal. The output pins provide the delayed output signal corresponding to the current delay of the tap. This algorithm can be expanded to support multiple input-tap/output pairs, allowing the same input signal to be delayed by various data control taps.

| The Max setting still corresponds to the maximum amount of delay reserved for the input signal. Therefore, any delay values designated by the data control pin must be between 0 samples and the Max Delay (samples) option.
| Please see the image below depicting how the module needs to be connected and used in the schematic.
| |voltagecontroldelayschematic.png|

.. container:: centeralign

   \ **Figure:** Usage of the Voltage-Controlled Delay module in a schematic


Pins
----

Input
~~~~~

=========================== ======= ==================================
Name                        Type    Description
=========================== ======= ==================================
Input                       Audio   Input channel 0
DelayTap <fc #ff0000>X</fc> Control Current delay for Output channel X
=========================== ======= ==================================

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

| Note: <fc #ff0000>X</fc> - Channel Index
| ===== Configurable Parameters =====

+-----------------------+---------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name    | Default Value | Range                | Function Description                                                                                                                                                                                                                                                                                                                                                                                               |
+=======================+===============+======================+====================================================================================================================================================================================================================================================================================================================================================================================================================+
| MaxDelay (in samples) | 1             | 4,80,000             | Controls the maximum amount of delay (in samples) that can be used for each output tap. Change in this value requires a re-compilation                                                                                                                                                                                                                                                                             |
+-----------------------+---------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Memory                | StateA        | StateA/StateB/StateC | It allows the user to choose in which memory the delay buffer to be stored. If **StateA** is chosen, buffer **SS Buffer 4** (**Block1_L1_space**) will be used for storing module data. If **StateB** is chosen, buffer **SS Buffer 8** (**Block3_L1_space**) will be used for storing module data. If **StateC** is chosen, buffer **SS Buffer 9** (**Block_L3_data_space**) will be used for storing module data |
+-----------------------+---------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels           | 1             | 32                   | Number of Dealy-Tap and Output channels. Change in this value requires a re-compilation                                                                                                                                                                                                                                                                                                                            |
+-----------------------+---------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+---------------------------------------------------+------------------------+
| Parameter Name | Description                                       | ADSP-214xx/SC5xx/215xx |
+================+===================================================+========================+
| MaxDelay       | The maximum delay (in samples) for each delay tap | Integer32              |
+----------------+---------------------------------------------------+------------------------+

| 
| ===== DSP Parameter Computation ===== MaxDelay = ( MaxDelay in ms ) \* (FS/ 1000)
| \* FS - Sampling Rate

.. |module.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/module.png
.. |voltagecontroldelayschematic.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/voltagecontroldelayschematic.png
