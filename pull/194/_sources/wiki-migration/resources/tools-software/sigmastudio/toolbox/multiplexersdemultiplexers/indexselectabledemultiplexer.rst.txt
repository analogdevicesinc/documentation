Index Selectable DeMultiplexer
==============================

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectabledemultiplexer039.jpg
   :align: right

This block lets you route an input to one of two selectable output pins. The output is selected based on a control signal value (orange pin), in 28.0 integer format from an Index Lookup Table, RMS Table, or DC Input block.

See the Multiplexer/Demultiplexer Example utilizing this block.

Algorithms
----------

The default algorithm for this block is the Mono Demux(unselected outputs 0). Selecting the Stereo Demux(unselected outputs 0) allows you to use a single control signal to control 2 input to output groups. Typically, this is used for routing a stereo signal to one of two pairs of stereo output pins.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectabledemultiplexer040.jpg
   :align: center

This block can be grown by Right-clicking and selecting Grow Algorithm from the menu. Growing will create additional output pins: single pins with the Mono algorithm, stereo output pin pairs with the Stereo algorithm. To select an output signal, set the control signal to the output pin's integer index starting from 0.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectabledemultiplexer041.jpg
   :align: center
