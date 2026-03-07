Rotary Encoder
==============

| :doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`
| |rotaryencoderpic1.png| The Rotary Encoder block processes the inputs from a rotary encoder and outputs an “up” and a “down” signal. The algorithm also incorporates a software "de-bouncer" for each of the inputs.

| 1) Drag the block into the schematic.
| 2) Connect the inputs to two GPIOs. These would correspond to the 2 out-of-phase output pins of a rotary encoder. In hardware configuration, set the GPIOs to “no debounce.”

The value in the field sets the time constant (in samples) for the debouncer; the default is 20. Adjust this value by trial and error using the rotary encoder in your end system.

The :doc:`Example </wiki-migration/resources/tools-software/sigmastudio/tutorials/gpioconditioningexample>` illustrates use of the block.

.. |rotaryencoderpic1.png| image:: https://wiki.analog.com/_media/rotaryencoderpic1.png
