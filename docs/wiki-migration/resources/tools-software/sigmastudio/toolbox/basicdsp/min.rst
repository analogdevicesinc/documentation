Min
===

:doc:`Click here to return to the BasicDSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

+---+---+
| The Min algorithm compares 2 (or more) inputs and outputs the input with the lowest value. | |min1.png| |
+---+---+

Min and Hold
============

+-------------------------------------------------------------------------------------------------------------+


| The Min and Hold is a algorithm compares the input sample with held min value and outputs the lowest value. |

+-------------------------------------------------------------------------------------------------------------+

| 
| |image1|

Input Pins
----------

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal- control                         | Reset signal to the module |
+--------------+------------------------------------------+----------------------------+
| Pin 1: Input | decimal- audio                           | Input signal to the module |
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

The module supports growth of Input channels up to 16 and one reset pin. Add Algorithm is not supported.

GUI Controls
------------

No GUI Controls

DSP Parameter Information
-------------------------

No DSP parameters

Algorithm Description
---------------------

This module compares the each channel input samples with held_min value and outputs lowest value when reset is Off. Compares the each channel input samples and outputs the lowest value when reset pin is high.

Supported IC's
--------------

+----------+


| ADAU145x |

+----------+

| ADAU146x |

+----------+

.. |min1.png| image:: https://wiki.analog.com/_media/min1.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/minandhold.png
