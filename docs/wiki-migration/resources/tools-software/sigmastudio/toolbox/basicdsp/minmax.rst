| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ====== Block Min/Max(ADAU145x) ====== Min/Max is a Block Processing module which compares the each input samples of one channel with other channels in block of input samples. By default it will check the minimum Algorithm. Option to select Minimum or Maximum Algorithm by clicking on bit map icon.
| |image1|
| ===== Input Pins =====

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 1: Input | decimal- audio                           | Input signal to the module |
+--------------+------------------------------------------+----------------------------+
| Pin 2: Input | decimal- audio                           | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

Output Pins
===========

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | decimal - audio                          | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
==============

The module supports growth of input channels up to 16 channels. Add Algorithm is not supported.

GUI Controls
============

+------------------+---------------+-------+----------------------------------------+
| GUI Control Name | Default Value | Range | Function Description                   |
+==================+===============+=======+========================================+
| Bit Map Icon     | 0             | 0 -1  | To select Minimum or Maximum Algorithm |
+------------------+---------------+-------+----------------------------------------+

DSP Parameter Information
=========================

No DSP Parameters.

Algorithm Description
=====================

This module compares the one channel input block of samples with other channel input block samples and outputs min/max block of samples based on Min or Max Algorithm chosen.

Supported IC's
==============

+----------+


| ADAU145x |

+----------+

| ADAU146x |

+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/maxormin.png
