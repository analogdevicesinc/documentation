Square Root
===========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ---------------------------------------------------------------------------------------------------------

+---+---+
| The Square Root block takes the square root of the input and outputs the result. | |squarerootpic1.png| |
+---+---+

Input Pins
----------

============== ================================== ====================
Name           Format [int/dec] - [control/audio] Function Description
============== ================================== ====================
Pin 0: Input x decimal - any                      Input signal
============== ================================== ====================

Output Pins
-----------

+-----------------------+------------------------------------+----------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description |
+=======================+====================================+======================+
| Pin 0: Output sqrt(x) | decimal - any                      | Output signal        |
+-----------------------+------------------------------------+----------------------+

Algorithm Description
---------------------

| This is the "standard" implementation of the square root function. It provides an approximation of the square root value of the input. For negative inputs to the block, the absolute value is taken before calculating the square root. Imaginary numbers are not supported. The following graph shows an input tone signal full scale at 500Hz (blue) and the resulting output through the square root block (red).
| |squarerootpic2.png|
| **Standard Vs. Ultra Precision**
| The main difference between this "standard" implementation and the Ultra Precision square root, is instruction program count vs. accuracy. The ultra precision algorithm requires many more instructions (141 compared to 81) but is a bit accurate execution of the square root function for the SigmaDSP processor.

| The accuracy difference between the two algorithms is a noise floor around approximately -78dB. The below plot shows a subtraction of the outputs from the Ultra Precision and the Standard square root functions. Notice that the noise floor difference is independent of signal level, thus the square root using the Standard approach is less accurate for low level signals.
| |squarerootpic3.png|

Example
-------

| The sample schematic shown here was the schematic used to generate the first plot. A :doc:`sine tone </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/sinetone>` source at 500Hz is sent to the output and also to the square root block. Notice that for negative values of the sine tone, the square root block treats the values as if they were positive.
| |squarerootpic4.png|

Algorithm Details
-----------------

+----------------------------+---------------------------------------------------------------+
| Toolbox Path               | Basic DSP - Arithmetic Operations - Square Root - Square Root |
+----------------------------+---------------------------------------------------------------+
| Cores Supported            | AD1940                                                        |
|                            | ADAU170x                                                      |
|                            | ADAU144x                                                      |
|                            | ADAU176x                                                      |
|                            | ADAU178x                                                      |
+----------------------------+---------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                            |
+----------------------------+---------------------------------------------------------------+
| "Add Algorithm" Supported  | yes - see Algorithm Addition Information                      |
+----------------------------+---------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                            |
+----------------------------+---------------------------------------------------------------+
| Program RAM                | 81                                                            |
+----------------------------+---------------------------------------------------------------+
| Data RAM                   | 3                                                             |
+----------------------------+---------------------------------------------------------------+
| Parameter RAM              | none                                                          |
+----------------------------+---------------------------------------------------------------+

Algorithm Addition Information
------------------------------

+--------------------------+-----------------------------------------------------------------------------------------------+----------------------+
| Description              | When the square root algorithm is grown, a second pair of input pins is added to the control. | |squarerootpic5.png| |
+--------------------------+-----------------------------------------------------------------------------------------------+----------------------+
| Program RAM Repetition   | 81 per add                                                                                    |                      |
+--------------------------+-----------------------------------------------------------------------------------------------+----------------------+
| Data RAM Repetition      | 2 per add                                                                                     |                      |
+--------------------------+-----------------------------------------------------------------------------------------------+----------------------+
| Parameter RAM Repetition | none                                                                                          |                      |
+--------------------------+-----------------------------------------------------------------------------------------------+----------------------+

.. |squarerootpic1.png| image:: https://wiki.analog.com/_media/squarerootpic1.png
.. |squarerootpic2.png| image:: https://wiki.analog.com/_media/squarerootpic2.png
.. |squarerootpic3.png| image:: https://wiki.analog.com/_media/squarerootpic3.png
.. |squarerootpic4.png| image:: https://wiki.analog.com/_media/squarerootpic4.png
.. |squarerootpic5.png| image:: https://wiki.analog.com/_media/squarerootpic5.png
