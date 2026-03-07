DC Input Entry
==============

| :doc:`Click here to return to the sources page </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`
| The DC Input Block allows you to generate a DC (direct current) signal (a constant numerical value). This Block can be used to generate control signals for Multiplexers and Lookup Tables.

| The block's controls allow the DC value and the format to be set. There are 32 or 28 available bits which can be used to represent decimal values, depending on the SigmaDSP.
| ===== Output Pins====

+----------------------+------------------------------------+----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description |
+======================+====================================+======================+
| Pin 0: Output Signal | Decimal -                          | DC output signal     |
+----------------------+------------------------------------+----------------------+

| 
| ===== GUI Controls =====

+------------------+---------------+-------------------------------------------+-----------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                                     | Function Description                                                        |
+==================+===============+===========================================+=============================================================================+
| DC               | 1             | 0 - (Depends on the format select)        | This control gives the DC, direct current, signal(a constant numeric value) |
+------------------+---------------+-------------------------------------------+-----------------------------------------------------------------------------+
| format           | 8.24/ 5.23    | Valid fixed point formats with 32/28 bits | This control decides the range of DC control                                |
+------------------+---------------+-------------------------------------------+-----------------------------------------------------------------------------+

| 
| ===== Grow and Add Algorithm ===== The module currently does not support grow functionality and Add Algorithm is supported. Supported to Multiple Instances.
| ===== DSP Parameter Information =====

ADAU145x
--------

+------------------+--------------------------------------------------------------------------+----------------------+
| GUI Control Name | Compiler Name                                                            | Function Description |
+==================+==========================================================================+======================+
| DC               | <fc #008000>DCInp145XBlkAlg</fc><fc #ff0000>1</fc><fc #000080>value</fc> | DC output signal     |
+------------------+--------------------------------------------------------------------------+----------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ====Supported DSPs=====

-  ADAU145x (Sample and Block)
-  ADAU144x
-  ADAU170x
-  ADAU176x
-  AD194x
-  ADAU140x

| 
