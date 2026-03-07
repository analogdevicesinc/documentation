Mono Switch 1xN
===============

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/multichannelswitch1xn_032.jpg
   :align: right

The Mono Switch block routes an input signal to one of many possible outputs, the strip of radio buttons is used to select an output (each radio button corresponds to a coefficient RAM parameter).

To begin, drag the block into the workspace, right-click it and select Add Algorithm > IC N Mono/Slew or Mono. (The result appears the same.) The Mono/Slew algorithm lets you rapidly ramp the source level up and down without any clicking noises when switching outputs. It uses N hardware volume controls in the target/slew RAM to do its job.

See the Multiplexer/Demultiplexer Example utilizing this block.

The default block is ready to use as a 1x2 connection, and like the others can be grown by right-clicking and selecting the desired number of outputs. The example below has been grown by 3:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/multichannelswitch1xn_033.jpg
   :align: center
