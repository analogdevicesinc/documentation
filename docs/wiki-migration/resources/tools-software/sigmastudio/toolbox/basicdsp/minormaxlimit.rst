:doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Block MinOrMax Limit(ADAU145x)
==============================

Min or Max Limit is a block processing module which compares each input sample
in block of input samples with a constant scalar value. By default it will Max
Limit Algorithm. Option to select Max Limit or Min Limit Algorithm by clicking
on bit map icon.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/minormaxlimit.png
   :align: center

Input Pins
----------

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal- audio                           | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

Output Pins
-----------

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | decimal- audio- audio                    | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
--------------

The module supports growth of Input and Output channels dependently up to 16.
Add Algorithm is not supported.

GUI Controls
------------

+------------------+---------------+---------------+------------------------------------------------------------+
| GUI Control Name | Default Value | Range         | Function Description                                       |
+==================+===============+===============+============================================================+
| \_limit          | 0             | -128 - 127.99 | Constant value used to compare with input block of samples |
+------------------+---------------+---------------+------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+--------------------------------+-------------------------------+
| GUI Control Name | Compiler Name                  | Function Description          |
+==================+================================+===============================+
| \_limit          | MinOrMaxLimitS300BlkAlg1_limit | Constant value for comparison |
+------------------+--------------------------------+-------------------------------+

Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

This module compares the constant value specified in the textbox to each of the
input samples in an input block.

Supported IC's
--------------

+----------+

| ADAU145x |

+----------+

| ADAU146x |

+----------+
