| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ====== Block Scalar Addition(ADAU145x) ====== |image1|
| Scalar Addition is a block processing module which adds a constant scalar value to each of the input samples in block of input samples
| |image2|

Input Pins
==========

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal-audio                            | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

Output Pins
===========

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | decimal-audio- audio                     | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
==============

| The module supports growth functionality, the number of channels to the module can be grown. Add is not supported.
| ===== GUI Controls =====
| ^GUI Control Name^Default Value^Range^Function Description^

+--------+---+-------------+------------------------------------------------------------+
| Scalar | 1 | -128-127.99 | Scalar Value used for addition with input block of samples |
+--------+---+-------------+------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

+------------------+--------------------------------------------------------------------------------+---------------------------+
| GUI Control Name | Compiler Name                                                                  | Function Description      |
+==================+================================================================================+===========================+
| Scalar           | <fc #008000>ScalarAdditionBlkAlg</fc><fc #ff0000>1</fc><fc #000080>Scalar</fc> | Scalar Value for Addition |
+------------------+--------------------------------------------------------------------------------+---------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ===== Algorithm Description =====
| This module adds the scalar value specified in the textbox to each of the input samples in an input block.

Example
=======

| 
| In the example shown below, scalar value 110 is added to each of the DC block input samples of value 10
| |image3|

Supported IC's
==============

| 1. ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalaradd.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalaraddcell.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalaraddexample.png
