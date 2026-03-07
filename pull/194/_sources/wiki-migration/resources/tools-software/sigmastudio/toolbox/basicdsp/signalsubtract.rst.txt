Signal Subtract
===============

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| There are two kinds of subtraction supported.

-  Subtraction (Real Signals)
-  Subtraction (Complex Signals)

Subtraction (Real Signals)
--------------------------

The Subtract Block performs a subtraction operation on the input pins and outputs the difference result. (Minuend - Subtrahend = Difference)\|\ |signalsubtractpic1.png|\ \|

Input Pins
~~~~~~~~~~

=========== ================================== ====================
Name        Format [int/dec] - [control/audio] Function Description
=========== ================================== ====================
Input_Pin 0 any - any                          Minuend term
Input_Pin 1 any - any                          Subtrahend term
=========== ================================== ====================

Output Pins
~~~~~~~~~~~

=========== ================================== ====================
Name        Format [int/dec] - [control/audio] Function Description
=========== ================================== ====================
Input_Pin 0 any - any                          Difference term
=========== ================================== ====================

Algorithm Description
~~~~~~~~~~~~~~~~~~~~~

| A standard subtraction operation is performed. When the algorithm is grown new input pins appear. These input pins represent more subtrahend terms so that the resulting output formula is:
| Output_Pin 0 = Input_Pin 0 - (Input_Pin1 + Input_Pin2 + Input_Pin3 + ... Input_PinN)

Example
~~~~~~~

The subtraction block can be used along with other arithmetic operators to realize many typical DSP functions. It is a basic building block that allows difference operations to be performed.

| The subtraction block can also be useful when debugging a schematic project. In the following example subtraction is used to compare the output of the :doc:`Crossover Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/crossover>` and two separate :doc:`General 2nd Order </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorder>` filters set-up to do a cross-over functionality. By subtracting the two "low" outputs and the two "high" outputs, you can verify that both filters are the same if the resulting output in the :doc:`Readback </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadback>` window is 0.
| |signalsubtractpic2.png|

Algorithm Details
~~~~~~~~~~~~~~~~~

+----------------------------+-----------------------------------------------------+
| Toolbox Path               | Basic DSP - Arithmetic Operations - Signal Subtract |
+----------------------------+-----------------------------------------------------+
| Cores Supported            | ADAU144x                                            |
|                            | ADAU176x                                            |
|                            | ADAU178x                                            |
|                            | ADAU170x                                            |
|                            | AD1940                                              |
+----------------------------+-----------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information              |
+----------------------------+-----------------------------------------------------+
| "Add Algorithm" Supported  | no                                                  |
+----------------------------+-----------------------------------------------------+
| Subroutine/Loop Based      | no                                                  |
+----------------------------+-----------------------------------------------------+
| Program RAM                | 3\*                                                 |
+----------------------------+-----------------------------------------------------+
| Data RAM                   | 1                                                   |
+----------------------------+-----------------------------------------------------+
| Parameter RAM              | 0                                                   |
+----------------------------+-----------------------------------------------------+

Subtraction (Complex Signals)
-----------------------------

| This algorithm subtracts the complex signals. (All real parts are subtracted to the first signal's real part and all imaginary parts are subtracted to first signals imaginary part)This is a block based module.
| |image1|

.. _input-pins-1:

Input Pins
~~~~~~~~~~

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
| ====Example Usage===== This can be used to subtract two signals FFT's result as shown below.
| |image2|

.. |signalsubtractpic1.png| image:: https://wiki.analog.com/_media/signalsubtractpic1.png
.. |signalsubtractpic2.png| image:: https://wiki.analog.com/_media/signalsubtractpic2.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/complexsubtract.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/complexsub2.jpg
