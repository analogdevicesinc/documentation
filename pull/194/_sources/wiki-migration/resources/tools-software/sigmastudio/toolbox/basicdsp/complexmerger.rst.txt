Complex Merger
==============

Complex Merger takes the real and imaginary part of input signal and merges to complex output signal. This is a block based module.

| 
| |image1|
| ====Input Pins====

+-----------------------+------------------------------------+------------------------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description               |
+=======================+====================================+====================================+
| Pin 0: Real Part      | control                            | Real Part of of Complex signal     |
+-----------------------+------------------------------------+------------------------------------+
| Pin 1: Imaginary Part | control                            | Imaginary Part of of Complex sinal |
+-----------------------+------------------------------------+------------------------------------+

| 
| ====Output Pins====

+-----------------------+------------------------------------+-----------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description  |
+=======================+====================================+=======================+
| Pin 0: Complex Signal | Complex                            | Complex output signal |
+-----------------------+------------------------------------+-----------------------+

| 
| ====Grow Algorithm==== Grow algorithm not supported for the module.
| ====Supported DSPs===== ADAU145x (Block Schematic only)

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/compexmerge.jpg
