Up/Down Control, Index Output
=============================

:doc:`Click here to return to the GPIO Conditioning Toolbox page. </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/updowncontrolindexout_021.jpg
   :align: right

This block takes in two inputs, one up and one down, and uses them to generate an index for a lookup table. The starting index is pre-loaded into an interface register and the up/down inputs increment or decrement the value.

-  Drag the block into your schematic.
-  Connect the red control inputs to GPIOs that have been conditioned by Push and Hold, or to the outputs of the Rotary Encoder.
-  Connect the yellow input pin to an Interface Read block.
-  Connect the yellow output to an Interface Write block, with the same register selected for both the interface read and write blocks.
-  The output will be an index value, so it should be connected to a block such as a lookup table or tone control.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/updowncontrolindexout_022.jpg
   :align: center

The :doc:`GPIO Conditioning Examples </wiki-migration/resources/tools-software/sigmastudio/tutorials/gpioconditioningexample>` illustrate the use of this block.

Algorithm
---------

The algorithm first reads an index from a stored value in the interface register. This value is then adjusted by two control signals, up/down signals, generated either by buttons conditioned by Push and Hold or by the GPIOs connected to outputs of the Rotary Encoder conditioned by that block. The control signals increment or decrement the index value, which is then sent to the output pin. The algorithm also writes the value back to the interface register to be stored.
