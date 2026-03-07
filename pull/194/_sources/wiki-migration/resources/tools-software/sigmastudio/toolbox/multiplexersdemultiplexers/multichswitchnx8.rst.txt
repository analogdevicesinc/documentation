Multi-channel Switch Nx8
========================

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/multichannelswitchnx8026.jpg
   :align: right

Use the radio buttons in this multi-channel block to select among sets of 8 inputs and send one set to one of the (8-channel) outputs.

To begin, drag the block into the workspace, right-click it and select Add Algorithm > IC # > 8 Channel/Slew or 8 Channel. (The result, shown at right top, appears the same either way.)

The 8 Channel/Slew algorithm lets you rapidly ramp the source level up and down without any clicking noises when switching among outputs. It uses N hardware volume controls in the target/slew RAM to do the job.

The default block (above right) is ready to use as a 2x1 connection, and like the others can be grown by right-clicking to select your desired number of input sets. At lower right is the default grown by 5 (= 7 input sets total).
