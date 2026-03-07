| :doc:`Click here to return to the basic dsp page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Trignometry
===========

| 
| This Module implements the basic trigonometric functions such as sine, cosine, tan, inverse sine, inverse cosine, inverse tan. This Module can be grown. When grown, both control and input, output pins are grown.
| |image1|
| ====Input Pins====

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Audio input
============ ================================== ====================

| 
| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Transformed Output
============= ================================== ====================

| 
| ==== Grow Algorithm ==== The module does not support Add and Growth.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

+-------------+---------+-------------------+--------------------------------------------+
| IndexIn     | 0(Sinx) | 0 to 5            | Index of the trigonometric function needed |
+-------------+---------+-------------------+--------------------------------------------+
| Input Gain  | 1       | -100000 to 100000 | Gain applied on the input                  |
+-------------+---------+-------------------+--------------------------------------------+
| phase       | 0       | -100000 to 100000 | phase of the input                         |
+-------------+---------+-------------------+--------------------------------------------+
| Output Gain | 1       | -100000 to 100000 | Gain applied on the output                 |
+-------------+---------+-------------------+--------------------------------------------+
| Offset      | 0       | -10000 to 10000   | Offset of the output                       |
+-------------+---------+-------------------+--------------------------------------------+

| 

DSP Parameter Information
-------------------------

+------------------+-------------------------------------------------------------------------------------------------------+----------------------------+
| GUI Control Name | Compiler Name                                                                                         | Function Description       |
+==================+=======================================================================================================+============================+
| IndexIn          | <fc #008000>Trignometry_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>IndenIn</fc><fc #800000>1</fc>     | function index selected    |
+------------------+-------------------------------------------------------------------------------------------------------+----------------------------+
| Input Gain       | <fc #008000>Trignometry_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Input Gain</fc><fc #800000>1</fc>  | Gain applied on the input  |
+------------------+-------------------------------------------------------------------------------------------------------+----------------------------+
| Phase            | <fc #008000>Trignometry_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Phase</fc><fc #800000>1</fc>       | phase of the input         |
+------------------+-------------------------------------------------------------------------------------------------------+----------------------------+
| Output Gain      | <fc #008000>Trignometry_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Output Gain</fc><fc #800000>1</fc> | Gain applied on the output |
+------------------+-------------------------------------------------------------------------------------------------------+----------------------------+
| Offset           | <fc #008000>Trignometry_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Offset</fc><fc #800000>1</fc>      | Offset of the output       |
+------------------+-------------------------------------------------------------------------------------------------------+----------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Stage number

| 
| ==== Algorithm Description ==== This Module implements the basic trigonometric functions such as sine, cosine, tan, inverse sine, inverse cosine, inverse tan. This Module can be grown. When grown, both control and input, output pins are grown.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/trignometry-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/trignometry-gui.jpg
