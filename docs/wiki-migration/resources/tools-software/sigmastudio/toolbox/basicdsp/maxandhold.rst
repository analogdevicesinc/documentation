Max and Hold
============

:doc:`Click here to return to the BasicDSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

The Max and Hold algorithm monitors one (or more) input signals and routes the maximum value to the output.

While the 'Hold' pin is held high (1), the output tracks and holds the maximum input value across all of the algorithm inputs. The maximum value is maintained and updated until the 'Hold' pin is toggled low.

While the 'Hold' pin is held low (0), the previous maximum value is forgotten. If there are multiple input signals, the maximum input value is passed through; just like the standard 'Max' algorithm. If there is only one input, it passes through to the output unaffected.

When the 'Hold' pin is brought high again, the algorithm begins tracking and holding the new maximum value of the input signals. There is no memory between consecutive 'Hold' sequences.

+---+
| |absmaxh1.png| |
+---+

.. |absmaxh1.png| image:: https://wiki.analog.com/_media/absmaxh1.png
