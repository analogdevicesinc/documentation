Schematic Terminal
==================

| :doc:`Click here to return to the System page </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign>`

|

.. tip::

   This block is not included in recent versions of SigmaStudio. You can simply leave output pins unconnected if their values are not needed.


| Whenever your schematic has output pins that are not necessary in your design, the Schematic Terminal block can function as a sink for the signal flow. Drag it to the workspace for connecting signal(s) from multiple blocks that are not actually sent to an output (see the Example).
| |schemterminalpic1.png|

If you do not terminate unused block output pins, the compiler will display an unconnected pin error.

.. |schemterminalpic1.png| image:: https://wiki.analog.com/_media/schemterminalpic1.png
