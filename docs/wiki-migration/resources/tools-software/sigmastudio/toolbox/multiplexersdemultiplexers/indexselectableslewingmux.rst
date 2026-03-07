Index Selectable Slewing Mux
============================

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectableslewingmux035.jpg
   :align: right

This block routes any one of its inputs, based on the index value from the Index Lookup Table, RMS Table or DC input, letting you ramp the source level up and down without any clicking noises when switching inputs.

Incrementing the value in the SW Slew Rate field slows the slewing speed. For the AD1940, the Index-Selectable Slewing Mux uses one hardware volume control in the target/slew RAM per input pair.

Like its companion blocks, this block can be grown. Right-click and select Grow Algorithms from the context menu. Growing will create an additional input pin or pins. To select a particular input signal, set the control signal to an input pin's integer index starting from 0, using a 28.0 format integer value.
