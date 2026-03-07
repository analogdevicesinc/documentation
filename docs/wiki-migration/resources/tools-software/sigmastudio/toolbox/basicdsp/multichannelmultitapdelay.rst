Multi-Channel Multi-Tap Delay
=============================

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| The Multi Channel Multi Tap Delay cell provides a variable delay for each output from one of the selected input channel. Each input signal is called as channel and output is called as Tap. The amount of delay for each tap can be modified in real time by updating the current delay.
| |image1|
| ===== Input Pins =====

+-------------------+-------------------------------------------+----------------------+
| Name              | Format [int/dec/float] - [control/audio]  | Function Description |
+===================+===========================================+======================+
| Pin 0: Input Data | Dec : SigmaDSPs,Float: SHARC DSPs - audio | Input audio signal   |
+-------------------+-------------------------------------------+----------------------+

| 
| ===== Output Pins =====

+--------------------+-------------------------------------------+----------------------+
| Name               | Format [int/dec] - [control/audio]        | Function Description |
+====================+===========================================+======================+
| Pin 0: Output Data | Dec : SigmaDSPs,Float: SHARC DSPs - audio | Delayed audio signal |
+--------------------+-------------------------------------------+----------------------+

| 

GUI Controls
------------

+------------------+---------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                                | Function Description                                                                                                                                                                                                             |
+==================+===============+======================================+==================================================================================================================================================================================================================================+
| Max              | 1             | 1 - (Depends on Size of the SPI RAM) | This control specifies the maximum delay supported for the current instance in samples (32-bit word). Maximum value of this is calculated depends on the SPI RAM's configuration. Change in this value requires a re-compilation |
+------------------+---------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cur              | 1             | 1 - Max                              | Current delay value                                                                                                                                                                                                              |
+------------------+---------------+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== Grow Algorithm ===== The module Will support grow functionality up to 32 Inputs and 32 outputs independently and Multiple instance is supported.

| 
| =====DSP Parameter Information=====

+------------------+----------------------------------+------------------------------------------+
| GUI Control Name | Compiler Name                    | Function Description                     |
+==================+==================================+==========================================+
| current delay    | MultiChMultiTapAlgS3001CurDelay0 | Current Delay value in bytes. (Cur \* 4) |
+------------------+----------------------------------+------------------------------------------+
| Input Selection  | MultiChMultiTapAlgS3001InputIdx0 | Input Index Selectable                   |
+------------------+----------------------------------+------------------------------------------+

Supported ICs
-------------

-  ADAU145x
-  ADSP214xx
-  ADSP213xx
-  ADSPSC58x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/multichannelmultitapdelay.png
