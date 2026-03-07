Division
========

| :doc:`Click here to return to the basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ------------------------------------------------------------------------------------------------------

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

.. |divisionpic1.png| image:: https://wiki.analog.com/_media/divisionpic1.png
.. |divisionpic2.png| image:: https://wiki.analog.com/_media/divisionpic2.png
.. |divisionpic3.png| image:: https://wiki.analog.com/_media/divisionpic3.png
