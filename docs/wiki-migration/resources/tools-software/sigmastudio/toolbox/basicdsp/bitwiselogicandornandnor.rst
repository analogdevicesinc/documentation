Bitwise Logic - And, Or, Nand, Nor, Xor
=======================================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| --------------------------------------------------------------------------------------------------------

|logicpic1.png| The Bitwise Logic block applies one of five selectable logic operations to each bit of the two input signals and outputs the result on the output pin. And, Or, Nand, Nor, and Xor operators are available.

Unlike the normal :doc:`Logic - And, Or, Nand, Nor </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/logicandornandnor>` cell, which applies the logic operation to the full data word from each input, this cell applies the logic operation to each bit in each word. The first bit in each of the two words are used to create the first bit in the output word, the second bit in each of the two words are used to create the second bit in the output word, and so on.

| **To change the operator:** Left click on the icon button, each click will toggle the active operator which is shown in the icon image and label.
| |logicpic2.png|
|

.. hint::

   Note: the operator is a compile time settings you will have to compile and download the project each time you change the operator.


Example
-------

In the following example, the words 0x000000AA and 0x0000000F have the AND logic operator applied to them. The resulting output is 0x0000000A.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/bitwiselogicexample.jpg
   :alt: bitwiselogicexample.jpg

.. |logicpic1.png| image:: https://wiki.analog.com/_media/logicpic1.png
.. |logicpic2.png| image:: https://wiki.analog.com/_media/logicpic2.png
