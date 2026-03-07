State Machine
=============

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/statemachine024.jpg
   :align: right

This block outputs the input signal from the green pin, if and only if the control signal level (orange pin) falls within the range specified in the numerical spin controls (>) and (<).

If the control signal is out of range, the input is disabled and a zero value is output.

The control pin can be sourced by a DC Input Entry, Counter, or an Index Lookup Table block. The control value should be a 28.0 format integer.

See the Multiplexer/Demultiplexer Example utilizing this block.
