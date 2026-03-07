Divide
======

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| There are two kinds of subtraction supported.

-  Division (Real Signals)
-  Division (Complex Signals)

Division (Real Signals)
-----------------------

|divisionpic1.png| The Division block allows you to divide two incoming signals. The division is performed using the Newton-Raphson iteration.

For a sample design using this block, see the :doc:`Basic DSP example </wiki-migration/resources/tools-software/sigmastudio/tutorials/basicdspexamples>`.

**To use this block:**

-  Drag and drop it into the workspace.
-  Right-click it and select **Add Algorithm > IC N >**

   -  **Newton Raphson 3 Iterations**

      -  **Newton Raphson 4 Iterations**

-  Connect your signals to the pins of the block so that you are performing the division
-  pin1 / pin2

| The Newton-Raphson iteration is performed according to the equation:
| |divisionpic2.png|
| This block lets you select the precision of the algorithm, whether to compute 3 or 4 iterations. There's a tradeoff between number of instructions and accuracy of computation for divisors (values of pin 2) less than 0.1. This means simply that fewer iterations are not as precise as more, but the more iterations the more instructions are entailed, with less room for programming the current DSP.

| Below are error graphs for the 3- (below top) and 4-iteration (below bottom) algorithms, showing a difference of approximately two orders of magnitude:
| |divisionpic3.png|

Division(Complex Signals)
-------------------------

| This module can be used to divide a complex signal with another complex signal.
| |image1|
| (x+iy) / (u+iv) = (xu + yv) + i(yu - xv) / (u^2 + v^2)
| Note:- The Context Menu “Input Source” option added to this module to select the algorithm for Complex FFT and Real FFT as shown below
| |image2|
| ====Input Pins====

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
| ====Grow Algorithm==== Input pins growth not supported.

| 
| ====Supported DSPs===== ADAU145x (Block Schematic only)
| ====Example Usage===== This can be used to divide complex signals |image3|

.. |divisionpic1.png| image:: https://wiki.analog.com/_media/divisionpic1.png
.. |divisionpic2.png| image:: https://wiki.analog.com/_media/divisionpic2.png
.. |divisionpic3.png| image:: https://wiki.analog.com/_media/divisionpic3.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/cdiv1.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/divisioncontextmenu.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/cdiv2.jpg
