Complex Splitter
================

Complex Splitter takes the complex input signal and splits real and imaginary parts separately. This is a block based module.

| 
| |image1|
| ====Input Pins====

+-----------------------+------------------------------------+----------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description |
+=======================+====================================+======================+
| Pin 0: Complex Signal | Complex                            | Complex input signal |
+-----------------------+------------------------------------+----------------------+

| 
| ====Output Pins====

+-----------------------+------------------------------------+------------------------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description               |
+=======================+====================================+====================================+
| Pin 0: Real Part      | control                            | Real Part of of Complex input      |
+-----------------------+------------------------------------+------------------------------------+
| Pin 1: Imaginary Part | control                            | Imaginary Part of of Complex input |
+-----------------------+------------------------------------+------------------------------------+

| 
| ====Grow Algorithm==== Grow algorithm not supported for the module.
| ====Supported DSPs===== ADAU145x (Block Schematic only)
| ====Example Usage==== FFT output can be split as real and imaginary using this module in the block processing.
| |image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/complexsplitter.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/csplit.jpg
