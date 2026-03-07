Mono Switch Nx1
===============

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/multichannelswitchnx1_031.jpg
   :align: right

The Mono Switch block routes one of many possible input signals to the output, the strip of radio buttons is used to select the input signal (each radio button corresponds to a coefficient RAM parameter).

To begin, drag the block into the workspace, right-click it and select Add Algorithm > IC # Mono/Slew or Mono. The blocks look the same, but the Mono/Slew algorithm performs a rapid fade-out fade-in of the source signals to prevent clicking noises when switching among the inputs. For the AD1940 it uses one hardware volume in the target/slew RAM per input to perform the slew.

The default block is ready to use as a 2x1 connection, and like the others can be grown by right-clicking to select your desired number of inputs. Shown above is the default block grown by 3 (= 5 inputs total).

See the Multiplexer/Demultiplexer Example utilizing this block.
