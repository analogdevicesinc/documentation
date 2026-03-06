:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Voltage Controlled Delay With Memory Selection
==============================================

| 
| |vcdelay.png|
| |image1|

Description
-----------

| The Multi-Tap Voltage Controlled Delay cell provides a variable delay to a single audio input, producing multiple outputs. Each output signal is called a “tap.” The amount of delay for each tap can be modified in real-time by updating the value on the corresponding control input pin.

Usage
-----

| The multi-tap voltage controlled delay allows a single signal to be output as multiple, independently-delayed copies. By right-clicking and selecting the “NumChannels” option, the user can increase the number of copies, or “taps”, to be output.
| A delay “Max” size is chosen prior to compilation; this value will determine the amount of modulo data RAM that the compiler will attempt to reserve for each tap. The equivalent delay in milliseconds/samples is displayed below this menu. Note that this delay Max size is reserved for each tap. It is not a shared Max-Delay that can be used by individual taps.
| If the control input for any tap exceeds the maximum allowable delay for that tap, then the maximum value will be used. Care must be taken so that the control inputs never go below zero (integer). If the control input a negative number, the output of the algorithm will jump to -1 (decimal).

Variants
--------

-  VoltageControlledDelay
-  Fractional Delay Multi-Tap Voltage Controlled

Targets Supported
-----------------

+------------------------------------------------------------------------------+----------------------+----------------------------------+------------------------------+
| Name                                                                         | ADSP-214xx           | ADSP-215xx/SC5xx                 | ADAU145x/146x                |
+==============================================================================+======================+==================================+==============================+
| ---------------------------------------------------------------------------- | -------------------- | -------------------------------- | ---------------------------- |
+------------------------------------------------------------------------------+----------------------+----------------------------------+------------------------------+
| VoltageControlledDelay                                                       | B/S                  | B/S                              | S                            |
+------------------------------------------------------------------------------+----------------------+----------------------------------+------------------------------+
| Fractional Delay Multi-Tap Voltage Controlled                                | NA                   | NA                               | S                            |
+------------------------------------------------------------------------------+----------------------+----------------------------------+------------------------------+

| 
| ===== Pins =====

Input
~~~~~

+-----------------------------+----------------+------------------------------------+
| Name                        | Type           | Description                        |
+=============================+================+====================================+
| ----------------------      | -------------- | ----------------------             |
+-----------------------------+----------------+------------------------------------+
| Input                       | Audio          | Input channel 0                    |
+-----------------------------+----------------+------------------------------------+
| DelayTap <fc #ff0000>X</fc> | Control        | Current delay for Output channel X |
+-----------------------------+----------------+------------------------------------+

Output
~~~~~~

========================= ============== ======================
Name                      Type           Description
========================= ============== ======================
----------------------    -------------- ----------------------
Output <fc #ff0000>X</fc> Audio          Output channel X
========================= ============== ======================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+------------------------------------------+------------------------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name                       | Default Value          | Range                                   | Function Description                                                                                                                                            |
+==========================================+========================+=========================================+=================================================================================================================================================================+
| ---------------------------------------- | ---------------------- | ------------------                      | ----------------------------------------                                                                                                                        |
+------------------------------------------+------------------------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaxDelay                                 | 1                      | Depends on Size of the Memory available | Controls the maximum amount of delay that can be used for each output tap. Change in this value requires a re-compilation                                       |
+------------------------------------------+------------------------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Memory                                   | DM1                    | NA                                      | It allows the user to choose in which memory the delay buffer to be stored(Not for ADSP-214xx, ADSP-215xx/SC5xx) Change in this value requires a re-compilation |
+------------------------------------------+------------------------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels                              | 1                      | 20                                      | Number of Dealy-Tap and Output channels. Change in this value requires a re-compilation                                                                         |
+------------------------------------------+------------------------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+------------------------------------------+----------------------------------------------------------------------------------+------------------------------------------+------------------------------+
| Parameter Name                           | Description                                                                      | ADSP-214xx/SC5xx/215xx                   | ADAU145x/146x                |
+==========================================+==================================================================================+==========================================+==============================+
| ---------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------- | ---------------------------- |
+------------------------------------------+----------------------------------------------------------------------------------+------------------------------------------+------------------------------+
| MaxDelay                                 | The maximum delay (in samples) for each delay tap                                | Integer32                                | Integer32                    |
+------------------------------------------+----------------------------------------------------------------------------------+------------------------------------------+------------------------------+

| 
| ===== DSP Parameter Computation ===== MaxDelay = ( MaxDelay in ms ) \* (FS/ 1000)
| \* FS - Sampling Rate

.. |vcdelay.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/vcdelay.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/vcdelayadau.png
   :width: 150px
