DC-Blocking
===========

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| ------------------------------------------------------------------------------------------------------

|dcblockingpic1.png| This filter is pre-configured, that is, it has set parameters for blocking direct-current components. It is used to remove dc that may be present in your signal.

While the block is ready to use after dragging into the workspace, there is the option to :doc:`Add </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/signaladd>` to the algorithm.

| The dc-blocking behavior is computed according to the following transfer function:
| |dcblockingpic2.png|
| Note: R = 0.9999 which is a cutoff frequency of 0.1Hz at 48kHz.

.. |dcblockingpic1.png| image:: https://wiki.analog.com/_media/dcblockingpic1.png
.. |dcblockingpic2.png| image:: https://wiki.analog.com/_media/dcblockingpic2.png
