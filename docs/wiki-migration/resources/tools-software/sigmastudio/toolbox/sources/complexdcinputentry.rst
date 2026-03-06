Complex DC Input Entry
======================

| :doc:`Click here to return to the sources page </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`
| The Complex DC Input Block allows you to generate a DC complex signal in the block processing domain.

The block's controls allow the DC value and the format to be set. There are 32 available bits which can be used to represent decimal values.

.. important::

   Please make sure block Size for the complex DC module is double the size of Non-Complex inputs


.

| 
| |image1|
| ===== Output Pins====

+----------------------+------------------------------------+----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description |
+======================+====================================+======================+
| Pin 0: Output Signal | Decimal -                          | DC output signal     |
+----------------------+------------------------------------+----------------------+

| 
| ===== GUI Controls =====

+------------------+---------------+-------------------------------------------+----------------------------------------------+
| GUI Control Name | Default Value | Range                                     | Function Description                         |
+==================+===============+===========================================+==============================================+
| Real             | 1             | 0 - (Depends on the format select)        | This control gives the DC real value         |
+------------------+---------------+-------------------------------------------+----------------------------------------------+
| Imaginary        | 0             | 0 - (Depends on the format select)        | This control gives the DC imaginary value    |
+------------------+---------------+-------------------------------------------+----------------------------------------------+
| format           | 8.24          | Valid fixed point formats with 32/28 bits | This control decides the range of DC control |
+------------------+---------------+-------------------------------------------+----------------------------------------------+

| 
| ===== Grow and Add Algorithm ===== The module currently does not support grow and add functionality.

| 
| ===== DSP Parameter Information =====

ADAU145x
--------

+------------------+-----------------------------------------------------------------------------------+------------------------------------+
| GUI Control Name | Compiler Name                                                                     | Function Description               |
+==================+===================================================================================+====================================+
| Real Value       | <fc #008000>ComplexDCBlkAlg</fc><fc #ff0000>1</fc><fc #000080>RealValue</fc>      | Real part of DC output signal      |
+------------------+-----------------------------------------------------------------------------------+------------------------------------+
| Imaginary Value  | <fc #008000>ComplexDCBlkAlg</fc><fc #ff0000>1</fc><fc #000080>ImaginaryValue</fc> | Imaginary part of DC output signal |
+------------------+-----------------------------------------------------------------------------------+------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ====Supported DSPs=====

-  ADAU145x (Block)

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/cdc.jpg
