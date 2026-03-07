| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ====== Block MinMaxLimit (ADAU145x) ====== MinMaxLimit is a block processing module which compares each input sample in block of input samples with constant values entered text box.
| |image1|
| ===== Input Pins =====

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
| Pin 0: Output | decimal-audio                            | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
==============

The module supports growth of input and output channels up to 16 dependently. Add Algorithm is not supported.

GUI Controls
============

+------------------+---------------+-------------+------------------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                           |
+==================+===============+=============+================================================+
| \_MaxLimit       | 1             | -128-127.99 | Constant value used compare with input samples |
+------------------+---------------+-------------+------------------------------------------------+
| \_MinLimit       | 0             | -128-127.99 | Constant value used compare with input samples |
+------------------+---------------+-------------+------------------------------------------------+

DSP Parameter Information
=========================

+------------------+------------------------------------------------------------------------------------+----------------------------------------------+
| GUI Control Name | Compiler Name                                                                      | Function Description                         |
+==================+====================================================================================+==============================================+
| \_MaxLimit       | <fc #008000>MinMaxLimitS300BlkAlg</fc><fc #ff0000>1</fc><fc #000080>_MaxLimit</fc> | Constant value to compare with input samples |
+------------------+------------------------------------------------------------------------------------+----------------------------------------------+
| \_MinLimit       | <fc #008000>MinMaxLimitS300BlkAlg</fc><fc #ff0000>1</fc><fc #000080>_MinLimit</fc> | Constant value to compare with input samples |
+------------------+------------------------------------------------------------------------------------+----------------------------------------------+

Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

Algorithm Description
=====================

This module compares the input samples in an input block of samples with Max Limit and Min Limit values specified in the textbox.

Supported IC's
==============

+----------+


| ADAU145x |

+----------+

| ADAU146x |

+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/minmaxlimit.png
