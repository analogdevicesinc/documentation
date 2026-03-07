Index Selectable Multiplexer
============================

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectablemultiplexer036.jpg
   :align: right

This block routes the signal from either of its two input pins, based on the control signal input index value from the Index Lookup Table, RMS Table or DC Input.

See the Multiplexer/Demultiplexer Example utilizing this block.

Drag the block into the workspace and right-click to select Add Algorithm > IC # > Mono/Stereo. Mono is shown above right. Stereo, which can be used for routing a stereo signal from one input pair, is shown here:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectablemultiplexer037.jpg
   :align: center

Like its companion blocks, this block can be grown. Right-click and select Grow Algorithms from the context menu. Growing will create additional input pins, single pins with the Mono algorithm, stereo input pin pairs with the Stereo algorithm. To select a particular input signal, set the control signal to an input pin's integer index starting from 0, using a 28.0 format integer value.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/indexselectablemultiplexer038.jpg
   :align: center
