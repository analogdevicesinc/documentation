Software Debounce
=================

| :doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`
| |softdebpic1.png| The contacts of mechanical switches and encoders can "bounce" when changing positions; meaning the voltage may fluctuate between states several times during the transition period. When the transition is not clean erroneous states can be set in your system. This block debounces (removes the transition ripple) from a signal, by waiting a specified amount of time between sampling periods. This provides a clean transition signal to the output.

Typically, this block is used to debounce a GPIO input signal.

To use this block, drag it into the schematic and connect the input to a GPIO signal.

The debounce time control sets the time constant for the debouncer, in samples; the default is 20. For best results adjust the value by trial and error for whatever hardware is connected to the GPIO input.

.. |softdebpic1.png| image:: https://wiki.analog.com/_media/softdebpic1.png
