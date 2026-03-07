Signal Add
==========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| There are three version of 'Signal Add' algorithm.

-  Signal Add (Real Signals)
-  2 Channel Adder (Real Signals)
-  Signal Add (Complex Signals)

| 
| =====Signal Add (Real Signals) ===== |signaladdpic1.png| The Signal Adder block adds inputs together. No other modification of the signal is done.

| Care must be taken to avoid clipping. If automatic gain reduction is needed to avoid clipping, use the :doc:`Signal Merger </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters/signalmerger>` block.
| =====2 Channel Signal Add (Real Signals) ===== This algorithm adds the 2 signal and produces an real signal. When the algorithm is grown it takes multiple pairs of input signal and adds each pair to produce an output signal.

| 
| |image1|

Input Pins
----------

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Operand 1 any                                Input signal 1
Pin 1: Operand 2 any                                Input signal 2
================ ================================== ====================

| 
| ====Output Pins====

+----------------------+------------------------------------+----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description |
+======================+====================================+======================+
| Pin 0: Output Signal | any                                | Output signal        |
+----------------------+------------------------------------+----------------------+

| 
| ====Grow Algorithm==== Module can be grown 16 times. For each growth input is grown by 2 and output by 1.
| |image2|
| ====Supported DSPs===== ADAU145x

Signal Add (Complex Signals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This algorithm adds the complex signals. (All real parts are summed together and all imaginary parts are summed together)This is a block based module.
| |image3|

.. _input-pins-1:

Input Pins
----------

+------------------+------------------------------------+------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description   |
+==================+====================================+========================+
| Pin 0: Operand 1 | complex                            | Input complex signal 1 |
+------------------+------------------------------------+------------------------+
| Pin 1: Operand 2 | complex                            | Input Complex signal 2 |
+------------------+------------------------------------+------------------------+

| 
| ====Output Pins====

+----------------------+------------------------------------+-----------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description  |
+======================+====================================+=======================+
| Pin 0: Output Signal | Complex                            | Complex output signal |
+----------------------+------------------------------------+-----------------------+

| 
| ====Grow Algorithm==== input pins can be grown up to 8 channels.

| 
| ====Supported DSPs===== ADAU145x (Block Schematic only)
| ====Example Usage===== This can be used to add two signals FFT's result as shown below. |image4|

.. |signaladdpic1.png| image:: https://wiki.analog.com/_media/signaladdpic1.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/2chadder.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/2chadder2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/complexadd.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/complexadd2.jpg
