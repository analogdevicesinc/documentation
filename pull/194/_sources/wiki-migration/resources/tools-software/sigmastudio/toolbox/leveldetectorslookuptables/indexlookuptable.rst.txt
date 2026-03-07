Index Lookup Table
==================

:doc:`Click here to return to the Level Detectors/Lookup Tables page </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/indexlookuptable_010.jpg
   :align: right

The Index Lookup Table block lets you access values stored in a lookup table (LUT). They're accessible through a table index.

To use this block: Drag it into the workspace and click Table to open the Table Editor window:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/indexlookuptable_011.jpg
   :align: center

There are two ways to enter values:

-  Enter them directly and use Save table value.
-  Use Load table value to load data from a file.

The first option lets you enter maximum value(s).

Description: For this algorithm, the input is the index value into the LUT. By default the module expect the index to be in integer format (32.0 or 28.0 depends on the SigmaDSP). The input format can be changed to fractional (8.24 or 5.23 depends on the SigmaDSP) by clicking the Green color circle in the module. Zero (0) will index the first value in the table. Recompiling is required when the input format is changed.

The default output format is fractional (8.24 or 5.23 depends on the SigmaDSP). This can be changed to integer by clicking the Blue color circle in the module.

There are two versions of this algorithm.

-  With Limit Protection: Checks if the index at the input is greater than the maximum index and, if so, indexes the last value in the table. Similarly, if the index is below zero, it will select the first value in the table.
-  Without Limit Protection: It does not compare the index to max and min index values.

The :doc:`Level Detectors Examples </wiki-migration/resources/tools-software/sigmastudio/tutorials/leveldetectorsexamples>` further illustrate use of this block.
