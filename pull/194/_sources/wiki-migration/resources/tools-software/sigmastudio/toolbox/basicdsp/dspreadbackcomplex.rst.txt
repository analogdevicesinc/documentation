DSP Readback (Complex)
======================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| The DSP Readback(complex) block lets you read complex values back from the DSP at any point in your schematic design.

| 
| |image1|
| The number displayed onscreen is the data value sent back from the DSP considering all the blocks to the left of the Readback block. Every time you click Read, this value will be updated with the latest from the DSP. By displaying the output value from any block, in any format desired, Readback is used chiefly for debugging, and probably will prove very handy.Values can be read back in either hex or decimal. For the latter, you must specify what format you want the number to be displayed in.
| ===== Input Pins====

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Input Signal | Complex                            | Input complex signal |
+---------------------+------------------------------------+----------------------+

| 
| ===== Output Pins====

+----------------------+------------------------------------+------------------------------------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description                                 |
+======================+====================================+======================================================+
| Pin 0: Output Signal | Complex                            | Output complex signal. Same as Input complex signal. |
+----------------------+------------------------------------+------------------------------------------------------+

| 
| ===== GUI Controls =====

+------------------+---------------+------------------------------------+---------------------------------------------+
| GUI Control Name | Default Value | Range                              | Function Description                        |
+==================+===============+====================================+=============================================+
| Real             | NA            | 0 - (Depends on the format select) | This control gives the read real value      |
+------------------+---------------+------------------------------------+---------------------------------------------+
| Imaginary        | NA            | 0 - (Depends on the format select) | This control gives the read imaginary value |
+------------------+---------------+------------------------------------+---------------------------------------------+
| format           | 8.24          | 1.31 to 32.0                       | This control decides the range              |
+------------------+---------------+------------------------------------+---------------------------------------------+

| 
| ===== Grow and Add Algorithm ===== The module currently does not support grow functionality and Add Algorithm is supported. Supported to Multiple Instances.
| ===== DSP Parameter Information =====

ADAU145x
--------

+------------------+-----------------------------------------------------------------------------------------+--------------------------+
| GUI Control Name | Compiler Name                                                                           | Function Description     |
+==================+=========================================================================================+==========================+
| Real             | <fc #008000>ComplexReadBackBlkAlg</fc><fc #ff0000>1</fc><fc #000080>RealValue</fc>      | Real part of signal      |
+------------------+-----------------------------------------------------------------------------------------+--------------------------+
| Imaginary        | <fc #008000>ComplexReadBackBlkAlg</fc><fc #ff0000>1</fc><fc #000080>ImaginaryValue</fc> | Imaginary part of signal |
+------------------+-----------------------------------------------------------------------------------------+--------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ====Supported DSPs=====

-  ADAU145x (Block)

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspc.jpg
