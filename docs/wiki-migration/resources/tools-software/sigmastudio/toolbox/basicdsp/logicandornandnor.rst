Logic - And, Or, Nand, Nor, Xor
===============================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| --------------------------------------------------------------------------------------------------------

|logicpic1.png| The Logic block applies one of five selectable logic operations to the two input signals and outputs the result on the output pin. And, Or, Nand, Nor, and Xor operators are available.

| **To change the operator:** Left click on the icon button, each click will toggle the active operator which is shown in the icon image and label.
| |logicpic2.png|
|

.. hint::

   Note: the operator is a compile time settings you will have to compile and download the project each time you change the operator.


| **Input Values:** This block should be used with DC input signals (positive 5.23 format). Also, this block is designed for use with boolean input values only, either 1.0 or 0.0. While not recommended, if necessary some operators can still function with arbitrary floating point values as input, but the output behavior may be ambiguous depending on the selected operator.
| |logicpic3.png|

.. |logicpic1.png| image:: https://wiki.analog.com/_media/logicpic1.png
.. |logicpic2.png| image:: https://wiki.analog.com/_media/logicpic2.png
.. |logicpic3.png| image:: https://wiki.analog.com/_media/logicpic3.png
