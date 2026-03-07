Multi-channel Switch Nx12
=========================

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/muxesdemuxes/n12_switch.jpg

Use the radio buttons in this multi-channel block to select among sets of 12 inputs and send one set to one of the (12-channel) outputs.

To begin, drag the block into the workspace, right-click it and select Add Algorithm > IC # > 12 Channel/Slew or 12 Channel. (The result, shown at right top, appears the same either way.)

The 12 Channel/Slew algorithm lets you rapidly ramp the source level up and down without any clicking noises when switching among outputs. It uses N hardware volume controls in the target/slew RAM to do the job.

The default block (shown at right) is ready to use as a 2x1 connection, and like the others can be grown by right-clicking to select your desired number of input sets. Shown at lower right is the default grown by 9 (= 11 input sets total).
