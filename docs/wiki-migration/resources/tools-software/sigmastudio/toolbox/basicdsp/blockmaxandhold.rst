:doc:`Click here to return to the BasicDSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Block Max and Hold
==================

+--------------------------------------------------------------------------------------------------------------------+


| The Max and Hold is a block algorithm compares the input sample with held max value and outputs the highest value. |

+--------------------------------------------------------------------------------------------------------------------+

| 
| |image1|

Input Pins
----------

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal(ADAU145x)- control               | Reset signal to the module |
+--------------+------------------------------------------+----------------------------+
| Pin 1: Input | decimal(ADAU145x)- audio                 | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

Output Pins
-----------

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | decimal(ADAU145x)- audio- audio          | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
--------------

The module supports growth of Input channels up to 16 and one reset pin. Add Algorithm is not supported.

GUI Controls
------------

No GUI Controls

DSP Parameter Information
-------------------------

No DSP parameters

Algorithm Description
---------------------

This module compares the each channel inputs samples in Block of input samples with held_max value and outputs highest value when reset is Off. Compares the each channel inputs samples in Block of input samples and outputs the highest value when reset pin is high.

Supported IC's
--------------

+----------+


| ADAU145x |

+----------+

| ADAU146x |

+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/maxandhold.png
